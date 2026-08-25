"""Shared GFS access helpers: .idx parsing, coalesced HTTP Range fetch, GRIB decode.

The load-bearing trick (per WEATHER_SPEC.md): never download a whole GRIB file.
Every GFS object on ``noaa-gfs-bdp-pds`` has a ``.idx`` sidecar listing the byte
offset of each field; we read it, take only the fields we want, merge adjacent
byte ranges, and issue HTTP Range requests. A whole 0.25-degree GFS file is
~500 MB; the five fields we need are ~4.7 MB.

Anonymous access only -- the bucket is public, no credentials anywhere.
"""

from __future__ import annotations

import os
import tempfile
import threading
import time
from typing import Iterable, Sequence

import numpy as np
import requests

import eccodes as ec

BUCKET = "https://noaa-gfs-bdp-pds.s3.amazonaws.com"

# ---------------------------------------------------------------------------
# Grid geometry (GFS 0.25 degree global regular lat/lon)
# ---------------------------------------------------------------------------
NI, NJ, DEG = 1440, 721, 0.25

# Shandong bounding box from WEATHER_SPEC.md
LAT_MIN, LAT_MAX = 34.25, 38.50
LON_MIN, LON_MAX = 114.75, 122.75

# GFS row 0 is 90N and rows run north -> south; column 0 is lon 0.
J0 = int(round((90.0 - LAT_MAX) / DEG))   # 206  -> lat 38.50
J1 = int(round((90.0 - LAT_MIN) / DEG))   # 223  -> lat 34.25
I0 = int(round(LON_MIN / DEG))            # 459  -> lon 114.75
I1 = int(round(LON_MAX / DEG))            # 491  -> lon 122.75

NLAT = J1 - J0 + 1                        # 18
NLON = I1 - I0 + 1                        # 33
NCELL = NLAT * NLON                       # 594

# Cell centre coordinates, flattened in the same (lat desc, lon asc) order as
# the value arrays returned by :func:`decode`.
CELL_LAT = np.repeat(LAT_MAX - DEG * np.arange(NLAT), NLON)
CELL_LON = np.tile(LON_MIN + DEG * np.arange(NLON), NLAT)

# Flat indices into the global 1038240-point GFS value array.
_FLAT = (
    (np.arange(J0, J1 + 1)[:, None] * NI) + np.arange(I0, I1 + 1)[None, :]
).ravel()

# ---------------------------------------------------------------------------
# Field selectors, keyed exactly as they appear in .idx lines
# ---------------------------------------------------------------------------
WIND_KEYS: tuple[tuple[str, str], ...] = (
    ("UGRD", "10 m above ground"),
    ("VGRD", "10 m above ground"),
    ("UGRD", "100 m above ground"),
    ("VGRD", "100 m above ground"),
)
DSWRF_KEYS: tuple[tuple[str, str], ...] = (("DSWRF", "surface"),)
LAND_KEYS: tuple[tuple[str, str], ...] = (("LAND", "surface"),)

# Canonical field lookup keyed on the numeric GRIB2 identifiers
# (discipline, parameterCategory, parameterNumber, typeOfLevel, level).
# Keying on shortName alone is NOT safe: GFS labels the 100 m winds plain
# "u"/"v" (level=100) while the 10 m winds are "10u"/"10v", and the DSWRF
# shortName varies by eccodes version ("dswrf" vs "sdswrf" vs "avg_dswrf").
_PARAM = {
    (0, 2, 2, "heightAboveGround", 10):  "u10",
    (0, 2, 3, "heightAboveGround", 10):  "v10",
    (0, 2, 2, "heightAboveGround", 100): "u100",
    (0, 2, 3, "heightAboveGround", 100): "v100",
    (0, 4, 192, "surface", 0):           "dswrf",
    (2, 0, 0, "surface", 0):             "land",
}


class MissingObject(Exception):
    """The requested GFS object does not exist in the bucket (404)."""


_local = threading.local()


def session() -> requests.Session:
    """Thread-local pooled session (one per worker thread)."""
    s = getattr(_local, "sess", None)
    if s is None:
        s = requests.Session()
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=64, pool_maxsize=64, max_retries=0
        )
        s.mount("https://", adapter)
        s.headers["User-Agent"] = "sd-spot-weather/1.0 (research; anonymous)"
        _local.sess = s
    return s


def grib_url(day, cycle: int, fhr: int) -> str:
    return (
        f"{BUCKET}/gfs.{day:%Y%m%d}/{cycle:02d}/atmos/"
        f"gfs.t{cycle:02d}z.pgrb2.0p25.f{fhr:03d}"
    )


def _get(url: str, headers: dict | None = None, timeout: int = 90,
         retries: int = 4) -> requests.Response:
    """GET with exponential backoff. Raises MissingObject on a real 404."""
    last = None
    for attempt in range(retries):
        try:
            r = session().get(url, headers=headers, timeout=timeout)
            if r.status_code == 404:
                raise MissingObject(url)
            r.raise_for_status()
            return r
        except MissingObject:
            raise
        except Exception as exc:                      # network / 5xx / timeout
            last = exc
            if attempt == retries - 1:
                break
            time.sleep(2 ** attempt)
    raise RuntimeError(f"GET failed after {retries} tries: {url}: {last}")


def idx_offsets(url: str) -> list[tuple[str, str, int, int | None]]:
    """Parse the ``.idx`` sidecar.

    Returns ``(var, level, byte_start, byte_end_inclusive_or_None)`` per record.
    Line format: ``msgnum:byte_start:d=YYYYMMDDCC:VAR:LEVEL:fcst spec:``
    """
    text = _get(url + ".idx", timeout=45).text
    lines = [ln for ln in text.strip().split("\n") if ln]
    starts = [int(ln.split(":")[1]) for ln in lines]
    out = []
    for i, ln in enumerate(lines):
        parts = ln.split(":")
        end = starts[i + 1] - 1 if i + 1 < len(starts) else None
        out.append((parts[3], parts[4], starts[i], end))
    return out


def fetch_fields(url: str, wanted: Sequence[tuple[str, str]]) -> bytes:
    """Range-fetch only ``wanted`` (var, level) fields; return concatenated GRIB.

    Adjacent byte ranges are merged so the usual five-field request costs three
    HTTP round trips rather than five.
    """
    want = set(wanted)
    segs = [
        (start, end)
        for var, lvl, start, end in idx_offsets(url)
        if (var, lvl) in want
    ]
    if not segs:
        return b""
    segs.sort()

    merged: list[list[int | None]] = []
    for lo, hi in segs:
        if merged and merged[-1][1] is not None and lo == merged[-1][1] + 1:
            merged[-1][1] = hi
        else:
            merged.append([lo, hi])

    chunks = []
    for lo, hi in merged:
        rng = f"bytes={lo}-{'' if hi is None else hi}"
        chunks.append(_get(url, headers={"Range": rng}).content)
    return b"".join(chunks)


def fetch_fields_scan(url: str, wanted: Sequence[tuple[str, str]]) -> bytes:
    """Fallback for objects whose ``.idx`` byte offsets do not match the file.

    A handful of GFS objects (2022-11-29/30 in this sample) ship an index whose
    offsets drift from the actual object -- range-fetching by index then returns
    mid-message garbage and eccodes raises "Wrong message length". The object
    itself is fine, so recover by downloading it once and walking the GRIB
    message chain locally: every GRIB2 message declares its own total length at
    bytes 8-15, and the index still lists messages in file order, so position i
    in the index names message i in the file.

    Expensive (a whole ~500 MB object) -- only ever used as a fallback.
    """
    want = set(wanted)
    names = [(var, lvl) for var, lvl, _s, _e in idx_offsets(url)]

    fd, path = tempfile.mkstemp(suffix=".grib2.scan")
    try:
        with os.fdopen(fd, "wb") as fh:
            with session().get(url, stream=True, timeout=300) as r:
                r.raise_for_status()
                for chunk in r.iter_content(chunk_size=4 << 20):
                    fh.write(chunk)

        chunks: list[bytes] = []
        with open(path, "rb") as fh:
            for i in range(len(names)):
                head = fh.read(16)
                if len(head) < 16 or head[:4] != b"GRIB":
                    break                      # ran off the end of the chain
                length = int.from_bytes(head[8:16], "big")
                body = fh.read(length - 16)
                if names[i] in want:
                    chunks.append(head + body)
        return b"".join(chunks)
    finally:
        os.unlink(path)                        # raw GRIB stays disposable


def decode(raw: bytes) -> tuple[dict[str, np.ndarray], dict[str, str]]:
    """Decode concatenated GRIB messages and subset to the Shandong bbox.

    Returns ``(values, steps)`` where ``values`` maps canonical field name to a
    float32 array of length :data:`NCELL` ordered (lat descending, lon
    ascending) to match :data:`CELL_LAT` / :data:`CELL_LON`, and ``steps`` maps
    the same names to the GRIB ``stepRange`` string (e.g. ``"12-16"``), which
    the DSWRF de-accumulation depends on.
    """
    if not raw:
        return {}, {}
    vals: dict[str, np.ndarray] = {}
    steps: dict[str, str] = {}
    fd, path = tempfile.mkstemp(suffix=".grib2")
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(raw)
        with open(path, "rb") as fh:
            while True:
                gid = ec.codes_grib_new_from_file(fh)
                if gid is None:
                    break
                try:
                    key = (
                        ec.codes_get(gid, "discipline"),
                        ec.codes_get(gid, "parameterCategory"),
                        ec.codes_get(gid, "parameterNumber"),
                        ec.codes_get(gid, "typeOfLevel"),
                        ec.codes_get(gid, "level"),
                    )
                    name = _PARAM.get(key)
                    if name is None:
                        continue
                    arr = ec.codes_get_array(gid, "values")
                    vals[name] = arr[_FLAT].astype(np.float32)
                    steps[name] = str(ec.codes_get(gid, "stepRange"))
                finally:
                    ec.codes_release(gid)
    finally:
        os.unlink(path)          # raw GRIB is disposable -- never persisted
    return vals, steps


def get_decoded(day, cycle: int, fhr: int, wanted: Sequence[tuple[str, str]],
                allow_scan: bool = True):
    """Fetch + decode one GFS object's selected fields in one call.

    Falls back to :func:`fetch_fields_scan` when the object's index turns out
    to be misaligned with the object (see that function).
    """
    url = grib_url(day, cycle, fhr)
    try:
        return decode(fetch_fields(url, wanted))
    except MissingObject:
        raise
    except Exception:
        if not allow_scan:
            raise
        return decode(fetch_fields_scan(url, wanted))


def wind_speed(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Per-cell wind speed. Computed BEFORE any spatial averaging (spec)."""
    return np.sqrt(u * u + v * v)
