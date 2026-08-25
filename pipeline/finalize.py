#!/usr/bin/env python3
"""Final clean-up and validation pass over ``data/sd_weather_errors.csv``.

Run once the backfill has finished. It:

1. clamps radiation columns at zero (de-accumulation amplifies float32 storage
   noise by up to 6x, which at night produces ~-0.01 W/m2 values) and
   recomputes the radiation errors from the clamped values;
2. checks panel completeness -- every delivery day present, 48 rows each,
   no duplicate keys;
3. prints the validation summary WEATHER_SPEC.md asks for: diurnal DSWRF shape,
   wind distributions, error means and tails.
"""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "data" / "sd_weather_errors.csv"

RAD = [("dswrf_fc", "dswrf_an", "e_dswrf"),
       ("dswrf_fc_cw", "dswrf_an_cw", "e_dswrf_cw")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", type=Path, default=CSV)
    ap.add_argument("--write", action="store_true",
                    help="write the clamped panel back to disk")
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    n0 = len(df)

    # --- 1. clamp radiation, recompute errors ------------------------------
    clamped = 0
    for fc, an, err in RAD:
        clamped += int((df[fc] < 0).sum() + (df[an] < 0).sum())
        df[fc] = df[fc].clip(lower=0.0)
        df[an] = df[an].clip(lower=0.0)
        df[err] = df[fc] - df[an]

    # --- 2. completeness ---------------------------------------------------
    df["date_cst"] = df["date_cst"].astype(str)
    days = sorted(df["date_cst"].unique())
    d0 = dt.date.fromisoformat(days[0])
    d1 = dt.date.fromisoformat(days[-1])
    expected = {(d0 + dt.timedelta(days=i)).isoformat()
                for i in range((d1 - d0).days + 1)}
    missing_days = sorted(expected - set(days))
    per_day = df.groupby("date_cst").size()
    short_days = per_day[per_day != 48]
    dup = int(df.duplicated(["date_cst", "hour_cst", "vintage"]).sum())
    nan_cols = df.columns[df.isna().any()].tolist()

    print(f"rows: {n0:,}   days: {len(days):,}   {days[0]} .. {days[-1]}")
    print(f"radiation values clamped at zero: {clamped}")
    print(f"duplicate keys: {dup}")
    print(f"missing days: {len(missing_days)}"
          + (f"  first few: {missing_days[:5]}" if missing_days else ""))
    print(f"days without 48 rows: {len(short_days)}"
          + (f"  {short_days.head().to_dict()}" if len(short_days) else ""))
    print(f"columns containing NaN: {nan_cols or 'none'}")

    # --- 3. validation summary --------------------------------------------
    print("\n--- diurnal DSWRF (W/m2, mean over sample, d1_00z) ---")
    diur = (df[df.vintage == "d1_00z"]
            .groupby("hour_cst")[["dswrf_fc", "dswrf_an"]].mean().round(0))
    print(diur.T.to_string())

    print("\n--- wind speed distribution (m/s) ---")
    for c in ["wind10_an", "wind100_an"]:
        q = np.percentile(df[c].dropna(), [0, 1, 25, 50, 75, 99, 100])
        print(f"  {c:12s} min {q[0]:5.2f}  p1 {q[1]:5.2f}  p25 {q[2]:5.2f}  "
              f"med {q[3]:5.2f}  p75 {q[4]:5.2f}  p99 {q[5]:5.2f}  max {q[6]:5.2f}")

    print("\n--- forecast errors (should centre near zero with fat tails) ---")
    print(f"  {'column':14s} {'vintage':8s} {'mean':>8s} {'sd':>8s} "
          f"{'kurtosis':>9s} {'p1':>8s} {'p99':>8s}")
    for col in ["e_wind10", "e_wind100", "e_dswrf",
                "e_wind10_cw", "e_wind100_cw", "e_dswrf_cw"]:
        for v, g in df.groupby("vintage"):
            s = g[col].dropna()
            print(f"  {col:14s} {v:8s} {s.mean():8.3f} {s.std():8.3f} "
                  f"{s.kurtosis():9.2f} {np.percentile(s,1):8.2f} "
                  f"{np.percentile(s,99):8.2f}")

    if args.write:
        df.to_csv(args.csv, index=False, float_format="%.4f")
        print(f"\nwrote {args.csv} ({len(df):,} rows)")
    else:
        print("\n(dry run; pass --write to save the clamped panel)")


if __name__ == "__main__":
    main()
