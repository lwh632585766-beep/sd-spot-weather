# Task spec: Shandong day-ahead weather forecast error panel

## Purpose (context in five lines)

The paper studies Shandong's electricity spot market: how renewable (wind/solar)
forecast errors move real-time prices relative to day-ahead prices. The market's own
forecasts are not fully public, so we construct forecast errors from public weather
data: what a day-ahead weather model predicted for day D, minus what actually happened.
Weather surprises are exogenous to market participants — this is both the measurement
and the identification. Sample: 2021-12-01 through 2026-08-31 (extend to present).

## Output (the deliverables committed to this repo)

`data/sd_weather_errors.csv` — one row per (date_cst, hour_cst 0–23, vintage):

| column | meaning |
|---|---|
| date_cst, hour_cst | Beijing-time (UTC+8) calendar day and hour being forecast |
| vintage | which forecast run: `d1_00z` (primary) or `d1_12z` (robustness) |
| wind10_fc, wind100_fc | forecast wind speed m/s, province aggregate (see weighting) |
| dswrf_fc | forecast downward shortwave radiation W/m², province aggregate |
| wind10_an, wind100_an, dswrf_an | "actual" (analysis) values, same aggregation |
| e_wind10, e_wind100, e_dswrf | forecast − actual |
| *_cw variants | capacity-weighted versions of all of the above (see weighting) |

Plus `data/sd_grid_cells.csv` (the cell list with weights) and `PROGRESS.md`.

## Data sources (all public, anonymous)

1. **Forecasts: GFS 0.25° archive on AWS Open Data.**
   Bucket `s3://noaa-gfs-bdp-pds` (HTTPS: `https://noaa-gfs-bdp-pds.s3.amazonaws.com/`).
   Path: `gfs.YYYYMMDD/CC/atmos/gfs.tCCz.pgrb2.0p25.fFFF` (CC=cycle 00/06/12/18,
   FFF=3-digit forecast hour). Every file has a `.idx` sidecar listing byte ranges per
   variable — use HTTP Range requests to fetch ONLY the needed fields (each field
   ~0.5–1 MB vs ~500 MB whole file). GFS 0.25° has HOURLY forecast steps to f120.
   The AWS bucket reliably covers ~2021-02 onward — the whole sample.
   Library options: `herbie-data` does idx-subsetting natively; or parse `.idx`
   manually with requests (format: `msgnum:byte_start:date:VAR:level:fcst`).
2. **Actuals: GFS f000 analysis** of cycles 00/06/12/18z, hourly values interpolated
   between cycles — avoids any registration. (ERA5 would need a Copernicus CDS
   account; note it as a later robustness option, do NOT block on it.)
3. **Capacity weights: Global Energy Monitor** Global Wind Power Tracker + Global
   Solar Power Tracker (free public downloads) — filter to Shandong, sum capacity per
   0.25° grid cell. If the download stalls, start with unweighted means (still a
   deliverable) and add weights after.

## Timing convention (the part to get right)

Beijing time = UTC+8. Day D's hours 00–23 CST = UTC (D−1) 16:00 → D 15:00.
Shandong's day-ahead market for delivery day D clears on day D−1 (gate closure
mid-day D−1 CST). The primary "day-ahead vintage" is therefore the **00z run of
day D−1** (available ~04:00 UTC = ~12:00 CST on D−1, safely before gate closure):
its forecast hours f016–f039 cover delivery day D in CST. Also build the **12z run
of D−1** (available ~22:00 CST D−1 — after gate closure; robustness/upper bound on
information) with f004–f027. Record both as separate `vintage` rows.

## Spatial subset

Shandong bounding box: **lat 34.25–38.50, lon 114.75–122.75** (0.25° grid → ~18×33
cells; keep land+near-shore cells, offshore wind exists off Yantai/Weihai so do NOT
drop sea cells east of 119.5 between lat 35–38.5).
Variables in GRIB terms: `UGRD`/`VGRD` at `10 m above ground` and `100 m above
ground` (speed = sqrt(u²+v²) — compute per cell BEFORE averaging), `DSWRF` at
`surface` (forecast steps only for DSWRF at f000 can be missing/zero — for the
analysis value of radiation use the f001 step of the covering cycle as "actual",
note this in PROGRESS.md).

## Processing loop (chunked, resumable)

For each date D from 2021-12-01 to present:
1. Fetch needed fields via Range requests: runs (D−1 00z: f016–f039) and
   (D−1 12z: f004–f027), plus analysis fields covering D's CST hours
   (cycles D−1 12z…D 12z f000/f001).
2. Decode (cfgrib/eccodes or herbie→xarray), subset bbox, compute wind speeds,
   aggregate to province mean and capacity-weighted mean.
3. Append rows to the CSV; delete all raw files for that date.
4. Every ~50 dates: commit CSVs + PROGRESS.md, push.
Resume = read the max date already in the CSV and continue from there.
Politeness: this is AWS Open Data, no rate limits needed beyond sanity (a few
parallel range requests are fine).

## Validation (do last, include in PROGRESS.md)

- Sanity: diurnal DSWRF shape; wind speed distributions (Weibull-ish, 0–25 m/s);
  error means near zero with fat tails.
- Cross-checks the researcher will run locally later (not your job): correlation of
  these errors with the Shandong exchange's own published daily peak forecast-vs-actual
  numbers.

## Definition of done

`data/sd_weather_errors.csv` covering 2021-12-01 → present, both vintages, both
weightings, pushed; PROGRESS.md summarizing coverage (expected ~1,730 days × 24 h ×
2 vintages ≈ 83k rows), anomalies list, and any spec deviations.
