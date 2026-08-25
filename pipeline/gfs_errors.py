#!/usr/bin/env python3
"""Build the Shandong day-ahead weather forecast-error panel.

Produces ``data/sd_weather_errors.csv``: one row per
(date_cst, hour_cst, vintage) with forecast, analysis ("actual") and
forecast-minus-actual values for 10 m wind, 100 m wind and surface shortwave
radiation, in both unweighted and capacity-weighted province aggregates.

Design notes that matter (see PROGRESS.md for the full deviation list):

* **Timing.** Beijing time is UTC+8, so delivery day D hours 00-23 CST span
  UTC (D-1) 16:00 -> D 15:00. The primary day-ahead vintage is the 00z run of
  D-1 (forecast hours f016-f039); the robustness vintage is the 12z run of D-1
  (f004-f027).

* **DSWRF is a bucket average, not an instantaneous field.** GFS reports it as
  a mean since the last 6-hourly bucket boundary ("12-16 hour ave fcst"), so a
  raw read at f016 gives a 4-hour mean, not the 15->16 hour value. Every
  radiation value here is de-accumulated to a true hourly mean:
  ``hourly(f) = L*A(f) - (L-1)*A(f-1)`` with ``L = f - 6*floor((f-1)/6)``.

* **Actuals.** Instead of 6-hourly f000 analyses interpolated to hourly (which
  would smooth away exactly the hourly ramps the paper is about), each hour
  uses the shortest available lead from its covering cycle: lead 0-5 of the
  most recent 00/06/12/18z cycle. Lead 0 is the true analysis; leads 1-5 are
  1-5 hour forecasts. Radiation has no f000 field at all, so the hour ending at
  a cycle time is de-accumulated from the previous cycle's f005/f006.

Raw GRIB is never written to the repo and never kept: fields are range-fetched
into memory, decoded, subset to 594 grid cells, and dropped.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import subprocess
import sys
import time
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd

import gfslib as G

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CSV = DATA / "sd_weather_errors.csv"
CELLS = DATA / "sd_grid_cells.csv"
PROGRESS = ROOT / "PROGRESS.md"

CST = dt.timezone(dt.timedelta(hours=8))
UTC = dt.timezone.utc

START = dt.date(2021, 12, 1)
VINTAGES = (("d1_00z", 0), ("d1_12z", 12))

COLUMNS = [
    "date_cst", "hour_cst", "vintage",
    "wind10_fc", "wind100_fc", "dswrf_fc",
    "wind10_an", "wind100_an", "dswrf_an",
    "e_wind10", "e_wind100", "e_dswrf",
    "wind10_fc_cw", "wind100_fc_cw", "dswrf_fc_cw",
    "wind10_an_cw", "wind100_an_cw", "dswrf_an_cw",
    "e_wind10_cw", "e_wind100_cw", "e_dswrf_cw",
]

WIND = "wind"
DSWRF = "dswrf"


# ---------------------------------------------------------------------------
# Timing helpers
# ---------------------------------------------------------------------------
def utc_at(date_cst: dt.date, hour_cst: int) -> dt.datetime:
    """UTC instant (naive) of a Beijing-time calendar hour."""
    local = dt.datetime(date_cst.year, date_cst.month, date_cst.day,
                        hour_cst, tzinfo=CST)
    return local.astimezone(UTC).replace(tzinfo=None)


def bucket_start(fhr: int) -> int:
    """First hour of the 6-hourly averaging bucket that forecast hour f sits in.

    f=13..18 -> 12,  f=19..24 -> 18,  f=6 -> 0,  f=7 -> 6.
    """
    if fhr < 1:
        raise ValueError(f"no averaging bucket for forecast hour {fhr}")
    return 6 * ((fhr - 1) // 6)


def covering_cycle(t_utc: dt.datetime) -> tuple[dt.datetime, int]:
    """Most recent 00/06/12/18z cycle at or before ``t_utc``, and the lead."""
    cyc = t_utc.replace(hour=(t_utc.hour // 6) * 6, minute=0, second=0,
                        microsecond=0)
    return cyc, int((t_utc - cyc).total_seconds() // 3600)


# ---------------------------------------------------------------------------
# What each delivery day needs from the bucket
# ---------------------------------------------------------------------------
def plan_day(day: dt.date) -> dict[tuple[dt.date, int, int], set[str]]:
    """Map (run_date, cycle, fhr) -> which field groups that object must supply."""
    need: dict[tuple[dt.date, int, int], set[str]] = defaultdict(set)
    run_day = day - dt.timedelta(days=1)

    # --- forecast vintages -------------------------------------------------
    for _, cyc in VINTAGES:
        run_dt = dt.datetime(run_day.year, run_day.month, run_day.day, cyc)
        for hour in range(24):
            fhr = int((utc_at(day, hour) - run_dt).total_seconds() // 3600)
            need[(run_day, cyc, fhr)] |= {WIND, DSWRF}
            lead = fhr - bucket_start(fhr)
            if lead > 1:                       # need previous step to de-accumulate
                need[(run_day, cyc, fhr - 1)] |= {DSWRF}

    # --- analysis (shortest-lead) series -----------------------------------
    for hour in range(24):
        t = utc_at(day, hour)
        cyc_dt, lead = covering_cycle(t)
        need[(cyc_dt.date(), cyc_dt.hour, lead)] |= {WIND}
        if lead >= 1:
            need[(cyc_dt.date(), cyc_dt.hour, lead)] |= {DSWRF}
            if lead > 1:
                need[(cyc_dt.date(), cyc_dt.hour, lead - 1)] |= {DSWRF}
        else:
            prev = cyc_dt - dt.timedelta(hours=6)
            need[(prev.date(), prev.hour, 6)] |= {DSWRF}
            need[(prev.date(), prev.hour, 5)] |= {DSWRF}
    return need


# ---------------------------------------------------------------------------
# Fetch + decode
# ---------------------------------------------------------------------------
def _load_one(item):
    (run_day, cyc, fhr), groups = item
    keys: list[tuple[str, str]] = []
    if WIND in groups:
        keys += list(G.WIND_KEYS)
    if DSWRF in groups:
        keys += list(G.DSWRF_KEYS)
    try:
        vals, _steps = G.get_decoded(run_day, cyc, fhr, keys)
        return (run_day, cyc, fhr), vals, None
    except G.MissingObject:
        return (run_day, cyc, fhr), {}, "missing"
    except Exception as exc:                                  # noqa: BLE001
        return (run_day, cyc, fhr), {}, f"error: {exc}"


def fetch_all(need, threads: int):
    store, problems = {}, {}
    with ThreadPoolExecutor(threads) as ex:
        for key, vals, err in ex.map(_load_one, list(need.items())):
            store[key] = vals
            if err:
                problems[key] = err
    return store, problems


# ---------------------------------------------------------------------------
# Worker: one contiguous block of delivery days, run in its own process
# ---------------------------------------------------------------------------
_W: "Weights | None" = None


def _init_worker():
    """Load the weight vectors once per worker process."""
    global _W
    _W = Weights(pd.read_csv(CELLS))


def process_block(job):
    """Fetch, decode and reduce one block of days. Returns (rows, anomalies)."""
    days, threads = job
    need: dict = defaultdict(set)
    for d in days:
        for k, v in plan_day(d).items():
            need[k] |= v

    store, problems = fetch_all(need, threads)
    anomalies = [
        f"{k[0]} {k[1]:02d}z f{k[2]:03d}: {err}"
        for k, err in sorted(problems.items())
    ]
    rows = []
    for d in days:
        rows += build_rows(d, store, _W)
    store.clear()
    return rows, anomalies, len(need)


# ---------------------------------------------------------------------------
# Aggregation
# ---------------------------------------------------------------------------
class Weights:
    """Normalised province weight vectors."""

    def __init__(self, cells: pd.DataFrame):
        def norm(col):
            w = cells[col].to_numpy(dtype=np.float64)
            w = np.where(cells["retain"].to_numpy() == 1, w, 0.0)
            total = w.sum()
            if total <= 0:
                raise SystemExit(f"weight column {col!r} sums to zero")
            return w / total

        self.uniform = norm("w_uniform")
        self.wind = norm("w_wind")
        self.solar = norm("w_solar")

    @staticmethod
    def apply(x: np.ndarray | None, w: np.ndarray) -> float:
        if x is None:
            return float("nan")
        return float(np.dot(x, w))


def field(store, key, name):
    vals = store.get(key)
    if not vals:
        return None
    return vals.get(name)


def wind_pair(store, key, level):
    u = field(store, key, f"u{level}")
    v = field(store, key, f"v{level}")
    if u is None or v is None:
        return None
    return G.wind_speed(u, v)


def hourly_dswrf(store, run_day, cyc, fhr):
    """De-accumulate GFS bucket-mean DSWRF to the true mean over (fhr-1, fhr]."""
    a = field(store, (run_day, cyc, fhr), "dswrf")
    if a is None:
        return None
    lead = fhr - bucket_start(fhr)
    if lead <= 1:
        return a
    prev = field(store, (run_day, cyc, fhr - 1), "dswrf")
    if prev is None:
        return None
    # De-accumulation amplifies float32 storage noise by up to L (=6), which at
    # night turns two ~1e-3 values into a ~1e-2 negative. Shortwave flux cannot
    # be negative, so clamp; the magnitude is far below any real signal.
    return np.maximum(lead * a - (lead - 1) * prev, 0.0)


def analysis_hour(store, t_utc):
    """(wind10, wind100, dswrf) cell arrays for the hour ending at ``t_utc``."""
    cyc_dt, lead = covering_cycle(t_utc)
    key = (cyc_dt.date(), cyc_dt.hour, lead)
    w10 = wind_pair(store, key, 10)
    w100 = wind_pair(store, key, 100)
    if lead >= 1:
        rad = hourly_dswrf(store, cyc_dt.date(), cyc_dt.hour, lead)
    else:
        prev = cyc_dt - dt.timedelta(hours=6)
        rad = hourly_dswrf(store, prev.date(), prev.hour, 6)
    return w10, w100, rad


# ---------------------------------------------------------------------------
# Row assembly
# ---------------------------------------------------------------------------
def build_rows(day: dt.date, store, W: Weights):
    rows = []
    run_day = day - dt.timedelta(days=1)

    # analysis is identical across vintages -- compute once per hour
    an_cache = {}
    for hour in range(24):
        an_cache[hour] = analysis_hour(store, utc_at(day, hour))

    for vintage, cyc in VINTAGES:
        run_dt = dt.datetime(run_day.year, run_day.month, run_day.day, cyc)
        for hour in range(24):
            fhr = int((utc_at(day, hour) - run_dt).total_seconds() // 3600)
            key = (run_day, cyc, fhr)
            fc10 = wind_pair(store, key, 10)
            fc100 = wind_pair(store, key, 100)
            fcrad = hourly_dswrf(store, run_day, cyc, fhr)
            an10, an100, anrad = an_cache[hour]

            row = {"date_cst": day.isoformat(), "hour_cst": hour,
                   "vintage": vintage}
            # "" = unweighted mean over retained cells;
            # "_cw" = capacity-weighted (wind weights for wind, solar for DSWRF)
            for suffix, ww, ws in (("", W.uniform, W.uniform),
                                   ("_cw", W.wind, W.solar)):
                f10 = W.apply(fc10, ww)
                f100 = W.apply(fc100, ww)
                frd = W.apply(fcrad, ws)
                a10 = W.apply(an10, ww)
                a100 = W.apply(an100, ww)
                ard = W.apply(anrad, ws)
                row[f"wind10_fc{suffix}"] = f10
                row[f"wind100_fc{suffix}"] = f100
                row[f"dswrf_fc{suffix}"] = frd
                row[f"wind10_an{suffix}"] = a10
                row[f"wind100_an{suffix}"] = a100
                row[f"dswrf_an{suffix}"] = ard
                row[f"e_wind10{suffix}"] = f10 - a10
                row[f"e_wind100{suffix}"] = f100 - a100
                row[f"e_dswrf{suffix}"] = frd - ard
            rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# Checkpointing
# ---------------------------------------------------------------------------
def git(*args, check=True):
    return subprocess.run(["git", *args], cwd=ROOT, check=check,
                          capture_output=True, text=True)


# Authorisation failures are not transient: retrying a 403 just burns time.
_FATAL_PUSH = ("403", "doesn't have GitHub access", "Permission denied",
               "Authentication failed")


def push_with_retry(branch: str, tries: int = 5) -> bool:
    """Push with backoff on *network* errors only. Returns False if blocked."""
    delay = 2
    for attempt in range(tries):
        r = git("push", "-u", "origin", branch, check=False)
        if r.returncode == 0:
            return True
        err = (r.stderr or "").strip()
        if any(tok in err for tok in _FATAL_PUSH):
            sys.stderr.write(
                "push rejected (not retryable); committing locally only: "
                f"{err.splitlines()[0][:200]}\n"
            )
            return False
        sys.stderr.write(f"push failed (try {attempt+1}): {err[:300]}\n")
        if attempt < tries - 1:
            time.sleep(delay)
            delay *= 2
    return False


# Deviations from WEATHER_SPEC.md, re-emitted into PROGRESS.md on every
# checkpoint (the file is regenerated each time, so this must live in code).
DEVIATIONS = """\
1. **DSWRF de-accumulated to true hourly means.** The spec treats DSWRF as a
   readable per-step field and only flags the f000 gap. In fact GFS stores it
   as a *mean since the last 6-hourly bucket boundary*: at f016 the record is
   labelled `12-16 hour ave fcst`, a 4-hour mean. Reading it raw would smear
   the diurnal shape (the f028 4-hour mean is 387 W/m2 where the true 11-12
   CST hour is 524 W/m2). Every radiation value here is de-accumulated as
   `hourly(f) = L*A(f) - (L-1)*A(f-1)`, `L = f - 6*floor((f-1)/6)`, which
   costs one extra step per vintage (f015 for 00z, f003 for 12z).

2. **Actuals use shortest-lead forecasts, not interpolated f000 analyses.**
   The spec suggests 6-hourly f000 analyses interpolated to hourly. Linear
   interpolation across a 6-hour gap removes exactly the hourly wind ramps the
   paper studies. Instead each hour takes the shortest available lead from its
   covering cycle (lead 0-5 of the most recent 00/06/12/18z run): lead 0 is the
   true analysis, leads 1-5 are 1-5 hour forecasts. Radiation has no f000
   record at all, so the hour ending at a cycle time is de-accumulated from the
   previous cycle's f005/f006.

3. **Near-shore bounded to 0.5 deg, and offshore enters through the capacity
   weight rather than the unweighted mean.** The spec says keep sea cells east
   of 119.5 between lat 35-38.5. Taken literally that retains 159 sea cells
   reaching 166 km into the Yellow Sea.

   The bound is set from the offshore fleet itself: in the COWT-SAR inventory
   Shandong's 1,187 offshore turbines sit a median 23 km from shore, p95 52 km.
   A 0.5 deg (~56 km) buffer covers 95.8% of them and retains 113 sea cells,
   against 67.1% coverage at 0.25 deg and 100% at 0.75 deg -- 0.5 deg is the
   knee of that curve, not a round number.

   Those 113 cells are still 31% of the retained set, while offshore is a much
   smaller share of Shandong's wind fleet. So `w_uniform` weights only the 312
   cells that actually overlap the province, not every retained cell: giving
   open water 31% of the unweighted aggregate would inflate its level (marine
   wind is stronger) and damp its diurnal cycle. Offshore instead enters
   through `w_wind`, where its share is set by observed turbine locations.
   Measured sea-cell share of each weight vector:

   | weight | sea share | cells with weight |
   |---|---|---|
   | `w_uniform` | 13.1% | 312 |
   | `w_province` | 4.6% | 312 |
   | `w_wind` | 15.2% | 71 |
   | `w_solar` | 1.2% | 194 |

   Effect on the level: over three sample days the old all-retained-equal mean
   sat 6.3% below the capacity-weighted 10 m wind and the province-equal mean
   sits 14.5% below it. The wider gap is the more honest one -- the old figure
   was close to the capacity-weighted level because open ocean happened to pull
   it up, not because it tracked where turbines are. The unweighted column is
   now a clean province-geography mean and the `_cw` column reflects siting;
   the gap between them is informative rather than an artefact.

   `dist_to_province` and `land_frac` are exported so any of this can be re-cut.

4. **Capacity weights come from substitute sources, one per technology.**
   The spec's Global Energy Monitor trackers are not obtainable here:
   globalenergymonitor.org serves an HTML landing page behind a form, GEM's
   asset API exposes no wind or solar asset classes, and OSM Overpass is
   blocked by the network policy (curl code 000). Per CLAUDE.md that is
   non-blocking, and rather than fall back to unweighted the `_cw` columns use:
   - `w_solar`: Kruitwagen et al. (2021) satellite PV inventory, restricted to
     `iso_3166_2 == CN-37`. 8,354 MW over 194 cells.
   - `w_wind`: Dunnett et al. (2020) OSM turbine clusters, turbine count x
     2 MW. 5,660 MW-equivalent over 71 cells.

   Both are level-incomplete: Kruitwagen is a mid-2018 snapshot of
   utility-scale PV and misses Shandong's large post-2018 distributed rooftop
   build-out; the OSM wind inventory carries roughly 6 GW against a real
   Shandong onshore fleet of ~20 GW. They are used as *spatial* weights, where
   only the relative distribution matters, and they are far from proportional
   to area (correlation with `w_province` is 0.14 for wind, 0.28 for solar), so
   the `_cw` columns are not a relabelled unweighted mean.

   The offshore-only inventories in `pipeline/static/` (DeepOWT, COWT-SAR) are
   deliberately NOT spliced in. Adding DeepOWT's 1.86 GW to an OSM onshore
   count implies a ~22% offshore share of Shandong wind, several times the real
   share over this sample, because the two inventories have very different
   detection completeness. They are committed so the choice can be revisited.

   Re-deriving weights does NOT require re-running the panel end to end only if
   the cell aggregation changes -- a different weight vector needs a full
   re-run, since the CSV stores province aggregates rather than cell values.

5. **Stale `.idx` files on 2022-11-29/30, recovered by scanning.** Nineteen GFS
   objects around those two cycles ship an index whose byte offsets have
   drifted from the object (the index puts message 1 at 878087 where the file
   has it at 876412), so range-fetching returned mid-message bytes and eccodes
   raised "Wrong message length". This reproduces on retry, so it is the
   archive, not the network. The objects themselves are intact: every GRIB2
   message declares its own length, and the index still lists messages in file
   order, so `gfslib.fetch_fields_scan` downloads the object once and walks the
   message chain locally to recover the fields. `get_decoded` now falls back to
   it automatically, so a future re-run self-heals. It initially left 41 rows
   NaN across 2022-11-30 and 2022-12-01; after the repair pass the panel has no
   missing values.

6. **Error magnitudes are understated relative to true forecast error.** The
   "actual" is itself a GFS short-lead forecast, so it shares initial
   conditions and model physics with the day-ahead forecast. These errors
   measure the day-ahead-vs-near-analysis revision, not forecast-vs-observation
   error. The exogenous surprise component is preserved, but levels are not
   comparable to station-verified RMSE. ERA5 (needs a Copernicus CDS account)
   remains the robustness option the spec notes.
"""


def write_progress(df: pd.DataFrame, anomalies: list[str], elapsed: float,
                   done_through: dt.date):
    n_days = df["date_cst"].nunique() if len(df) else 0
    lines = [
        "# PROGRESS",
        "",
        f"_Updated: {dt.datetime.now(UTC):%Y-%m-%d %H:%M UTC}_",
        "",
        "## Coverage",
        "",
        f"- Processed through: **{done_through.isoformat()}**",
        f"- Days in panel: **{n_days}**",
        f"- Rows: **{len(df):,}** (expected 48 per day: 24 hours x 2 vintages)",
    ]
    if len(df):
        lines += [
            f"- Date range: {df['date_cst'].min()} .. {df['date_cst'].max()}",
            "",
            "## Value ranges",
            "",
            "| column | mean | sd | min | max | n_missing |",
            "|---|---|---|---|---|---|",
        ]
        for c in ["wind10_fc", "wind10_an", "e_wind10", "wind100_fc",
                  "wind100_an", "e_wind100", "dswrf_fc", "dswrf_an", "e_dswrf"]:
            s = df[c]
            lines.append(
                f"| {c} | {s.mean():.3f} | {s.std():.3f} | {s.min():.3f} "
                f"| {s.max():.3f} | {int(s.isna().sum())} |"
            )
    # --- weighting actually in force, read back from the cell file ---------
    try:
        cells = pd.read_csv(CELLS)
        keep = cells["retain"].to_numpy() == 1
        sea = cells["land_frac"].to_numpy() < 0.5
        lines += [
            "",
            "## Spatial weighting in force",
            "",
            f"Cells: {len(cells)} in the bbox, {int(keep.sum())} retained "
            f"({int((keep & ~sea).sum())} land, {int((keep & sea).sum())} sea).",
            f"Capacity source: `{cells['cap_source'].iat[0]}`.",
            "",
            "| weight | used by | sea-cell share | cells with weight |",
            "|---|---|---|---|",
        ]
        used = {"w_uniform": "unweighted columns", "w_province": "(reference)",
                "w_wind": "`wind*_cw`", "w_solar": "`dswrf*_cw`"}
        for col, who in used.items():
            w = cells[col].to_numpy(dtype=float) * keep
            tot = w.sum()
            if tot <= 0:
                continue
            lines.append(f"| `{col}` | {who} | {100 * w[sea].sum() / tot:.1f}% "
                         f"| {int((w > 0).sum())} |")
    except Exception as exc:                                      # noqa: BLE001
        lines += ["", f"_(weighting summary unavailable: {exc})_"]

    lines += ["", "## Spec deviations", "", DEVIATIONS]
    lines += ["## Anomalies", ""]
    lines += ([f"- `{a}`" for a in anomalies[-200:]]
              or ["- none: every GFS object requested so far decoded cleanly"])
    if len(anomalies) > 200:
        lines += [f"", f"_({len(anomalies)} total; showing last 200.)_"]
    lines += ["", f"_Elapsed this run: {elapsed/60:.1f} min_", ""]
    PROGRESS.write_text("\n".join(lines))


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=dt.date.fromisoformat, default=None)
    ap.add_argument("--end", type=dt.date.fromisoformat, default=None)
    ap.add_argument("--block", type=int, default=5,
                    help="delivery days fetched per batch")
    ap.add_argument("--threads", type=int, default=16,
                    help="concurrent range requests per worker process")
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2)),
                    help="worker processes (decode is CPU-bound)")
    ap.add_argument("--commit-every", type=int, default=50,
                    help="commit + push after this many processed days")
    ap.add_argument("--branch", default="claude/startup-check-weather-spec-c56s8w")
    ap.add_argument("--no-git", action="store_true")
    ap.add_argument("--out", type=Path, default=CSV)
    args = ap.parse_args()

    cells = pd.read_csv(CELLS)
    W = Weights(cells)

    existing = None
    start = args.start or START
    if args.out.exists():
        existing = pd.read_csv(args.out)
        if len(existing) and args.start is None:
            last = dt.date.fromisoformat(str(existing["date_cst"].max()))
            start = last + dt.timedelta(days=1)
            print(f"resuming after {last}")

    end = args.end or (dt.date.today() - dt.timedelta(days=1))
    if start > end:
        print(f"nothing to do: start {start} > end {end}")
        return

    all_days = [start + dt.timedelta(days=i) for i in range((end - start).days + 1)]
    print(f"processing {len(all_days)} days: {start} .. {end}")

    frames = [existing] if existing is not None and len(existing) else []
    anomalies: list[str] = []
    t0 = time.time()
    since_commit = 0
    done_through = start - dt.timedelta(days=1)

    blocks = [all_days[i:i + args.block]
              for i in range(0, len(all_days), args.block)]
    jobs = [(b, args.threads) for b in blocks]
    processed = 0

    with ProcessPoolExecutor(args.workers, initializer=_init_worker) as pool:
        for bi, (rows, block_anoms, n_obj) in enumerate(
                pool.map(process_block, jobs)):
            block = blocks[bi]
            anomalies += [f"{block[0]}..{block[-1]}: {a}" for a in block_anoms]
            frames.append(pd.DataFrame(rows, columns=COLUMNS))

            done_through = block[-1]
            since_commit += len(block)
            processed += len(block)
            elapsed = time.time() - t0
            rate = elapsed / processed
            eta = (len(all_days) - processed) * rate / 60
            print(f"  {block[0]} .. {block[-1]}  {n_obj:4d} objs  "
                  f"{rate:5.2f}s/day  eta {eta:6.1f} min"
                  + (f"  [{len(block_anoms)} missing]" if block_anoms else ""),
                  flush=True)

            if since_commit >= args.commit_every or processed >= len(all_days):
                df = pd.concat(frames, ignore_index=True)
                df = (df.drop_duplicates(
                            subset=["date_cst", "hour_cst", "vintage"],
                            keep="last")
                        .sort_values(["date_cst", "hour_cst", "vintage"]))
                frames = [df]
                DATA.mkdir(exist_ok=True)
                df.to_csv(args.out, index=False, float_format="%.4f")
                write_progress(df, anomalies, time.time() - t0, done_through)
                print(f"  checkpoint: {len(df):,} rows -> {args.out.name}",
                      flush=True)
                if not args.no_git:
                    git("add", str(args.out), str(PROGRESS), str(CELLS),
                        check=False)
                    r = git("commit", "-m",
                            f"data: weather error panel through {done_through}",
                            check=False)
                    if r.returncode == 0:
                        push_with_retry(args.branch)
                since_commit = 0

    print(f"done in {(time.time()-t0)/60:.1f} min, {len(anomalies)} anomalies")


if __name__ == "__main__":
    main()
