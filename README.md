# sd-spot-weather

Cloud workspace for building the Shandong day-ahead weather forecast-error panel
(treatment variable for a paper on Shandong's electricity spot market).

- **Start here (for Claude in the cloud session): `CLAUDE.md`, then `WEATHER_SPEC.md`.**
- `PROGRESS.md` — running log: coverage, value ranges, spec deviations, anomalies.
- `data/` — derived CSVs only (small); raw GRIB is never committed.

Owner: Wenhao. Deliverables are pulled back to the local machine from this repo.

## Deliverables

| file | contents |
|---|---|
| `data/sd_weather_errors.csv` | one row per (`date_cst`, `hour_cst` 0-23, `vintage`), 2021-12-01 onward |
| `data/sd_grid_cells.csv` | the 594-cell 0.25 degree grid with land mask, province overlap and weights |

`vintage` is `d1_00z` (primary day-ahead: the 00z run of D-1, available ~12:00
CST on D-1, before gate closure) or `d1_12z` (robustness: the 12z run of D-1,
available after gate closure, so an upper bound on available information).

Each row carries forecast (`_fc`), actual (`_an`) and error (`e_`, forecast
minus actual) values for `wind10`, `wind100` and `dswrf`, in two spatial
aggregations:

- unweighted — plain mean over the 392 retained cells, which **includes**
  near-shore sea cells (so offshore wind is represented);
- `_cw` — capacity-weighted, using per-cell wind and solar capacity, which is
  concentrated onshore.

The two bracket the treatment of offshore wind; `PROGRESS.md` explains what the
capacity weights are actually derived from and where they are incomplete.

## Pipeline

```
pipeline/gfslib.py      .idx parsing, coalesced HTTP Range fetch, GRIB decode
pipeline/make_grid.py   builds data/sd_grid_cells.csv (land mask, weights)
pipeline/gfs_errors.py  builds data/sd_weather_errors.csv (resumable)
pipeline/static/        boundary + capacity inventories used to derive weights
```

Rebuild the cell file, then the panel:

```bash
cd pipeline
python3 make_grid.py
python3 gfs_errors.py                      # resumes from the last date in the CSV
python3 gfs_errors.py --start 2021-12-01   # or force a full rebuild
```

Useful flags: `--end`, `--workers`, `--threads`, `--block`, `--commit-every`,
`--no-git`, `--out`.

Dependencies: `numpy pandas requests eccodes shapely`.

### How it stays small

A whole GFS 0.25 degree file is ~500 MB. Every object has a `.idx` sidecar
listing per-field byte offsets, so the pipeline reads the index, keeps only the
five fields it needs, merges adjacent byte ranges (five fields collapse to three
requests, ~4.7 MB) and fetches those with HTTP Range requests. Fields are
decoded in memory, reduced to 594 grid cells, and dropped — no raw GRIB is ever
written to the repo, and peak disk stays in the tens of MB.

Access is anonymous throughout; `noaa-gfs-bdp-pds` is public AWS Open Data.
