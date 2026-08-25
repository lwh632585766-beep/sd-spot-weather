"""Starter skeleton for the Shandong GFS forecast-error pipeline.

STATUS: untested draft written outside the cloud environment — the cloud session
should treat WEATHER_SPEC.md as the contract, use this as a head start, and fix
freely (note deviations in PROGRESS.md). The .idx parsing + Range-request pattern
below is the load-bearing trick: never download whole GRIB files.

Deps: requests, xarray, cfgrib, eccodes (pip wheels), pandas, numpy.
Alternative: herbie-data does the idx subsetting natively; use it if it installs
cleanly (python >= 3.10) — then only the aggregation/loop logic here matters.
"""
import io
import os
import re
import time
import datetime as dt
from pathlib import Path

import requests
import pandas as pd

BUCKET = "https://noaa-gfs-bdp-pds.s3.amazonaws.com"
BBOX = dict(lat_min=34.25, lat_max=38.50, lon_min=114.75, lon_max=122.75)
WANTED = [  # (idx-var, idx-level) exactly as they appear in .idx lines
    ("UGRD", "10 m above ground"), ("VGRD", "10 m above ground"),
    ("UGRD", "100 m above ground"), ("VGRD", "100 m above ground"),
    ("DSWRF", "surface"),
]
OUT = Path(__file__).resolve().parent.parent / "data"
CSV = OUT / "sd_weather_errors.csv"


def grib_url(day: dt.date, cycle: int, fhr: int) -> str:
    return (f"{BUCKET}/gfs.{day:%Y%m%d}/{cycle:02d}/atmos/"
            f"gfs.t{cycle:02d}z.pgrb2.0p25.f{fhr:03d}")


def fetch_fields(day: dt.date, cycle: int, fhr: int, retries: int = 3) -> bytes | None:
    """Fetch only WANTED fields of one GRIB file via .idx byte ranges; returns
    concatenated GRIB messages (cfgrib can read the concatenation)."""
    url = grib_url(day, cycle, fhr)
    for a in range(retries):
        try:
            idx = requests.get(url + ".idx", timeout=30)
            if idx.status_code == 404:
                return None
            idx.raise_for_status()
            lines = idx.text.strip().split("\n")
            # idx line: "N:byte_start:d=YYYYMMDDCC:VAR:LEVEL:fcst spec:"
            starts = [int(l.split(":")[1]) for l in lines]
            chunks = []
            for i, l in enumerate(lines):
                p = l.split(":")
                if (p[3], p[4]) in WANTED:
                    lo = starts[i]
                    hi = (starts[i + 1] - 1) if i + 1 < len(lines) else ""
                    r = requests.get(url, headers={"Range": f"bytes={lo}-{hi}"},
                                     timeout=60)
                    r.raise_for_status()
                    chunks.append(r.content)
            return b"".join(chunks)
        except Exception:
            if a == retries - 1:
                raise
            time.sleep(5 * (a + 1))


def decode_and_aggregate(grib_bytes: bytes, weights=None) -> dict:
    """Decode concatenated GRIB messages, subset bbox, return province aggregates.
    Implement with cfgrib:  xr.open_dataset(io.BytesIO?) — cfgrib needs a file path,
    so write to a NamedTemporaryFile first. Compute wind speed per cell BEFORE
    averaging. Return dict: wind10, wind100, dswrf (+ *_cw if weights given)."""
    raise NotImplementedError  # cloud session: implement per WEATHER_SPEC.md


def hours_for_delivery_day(d: dt.date):
    """Yield (vintage, run_day, cycle, fhr, hour_cst) for delivery day d per the
    spec's timing convention: d-1 00z f016..f039 and d-1 12z f004..f027 map to
    CST hours 0..23 of day d."""
    prev = d - dt.timedelta(days=1)
    for h in range(24):
        yield ("d1_00z", prev, 0, 16 + h, h)
        yield ("d1_12z", prev, 12, 4 + h, h)


def main():
    OUT.mkdir(exist_ok=True)
    start = dt.date(2021, 12, 1)
    if CSV.exists():
        done = pd.read_csv(CSV, usecols=["date_cst"])
        start = dt.date.fromisoformat(done["date_cst"].max()) + dt.timedelta(days=1)
    today = dt.date.today()
    d = start
    while d < today:
        # 1) forecasts for both vintages; 2) analyses (f000/f001 of covering cycles);
        # 3) aggregate; 4) append rows; 5) every ~50 days: git commit+push.
        ...
        d += dt.timedelta(days=1)


if __name__ == "__main__":
    main()
