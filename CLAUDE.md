# sd-spot-weather

This repo is the CLOUD WORKSPACE for one job: build the **day-ahead weather forecast
error panel for Shandong province, China (Dec 2021 – Aug 2026)** that serves as the
treatment variable in an economics paper on Shandong's electricity spot market
(day-ahead vs real-time price spreads vs renewable forecast errors, Ito–Reguant-style).

The researcher (Wenhao) runs the paper locally on his Mac; this cloud session's ONLY
deliverables are small derived CSVs committed to this repo. He pulls them locally.
You have no other context from previous conversations — everything you need is in
**WEATHER_SPEC.md**. Read it fully before doing anything.

STARTUP CHECK (do this before anything else): verify the data source is reachable —
`curl -s -o /dev/null -w "%{http_code}" -m 15 "https://noaa-gfs-bdp-pds.s3.amazonaws.com/gfs.20240101/00/atmos/gfs.t00z.pgrb2.0p25.f012.idx"`
must return 200, and a Range request (`-H "Range: bytes=0-1000"`) must return 206.
If you get 403/EGRESS_BLOCKED instead, the environment's network policy is blocking
the bucket: STOP and tell the owner to whitelist `noaa-gfs-bdp-pds.s3.amazonaws.com`
(and, if needed, `s3.amazonaws.com`) in the claude.ai/code environment network
settings — this is the one blocker you must not work around. The capacity-weights
source `globalenergymonitor.org` may also be blocked; that one is NOT blocking —
proceed with unweighted aggregates per the spec and note it.

Hard rules:
- Raw GRIB downloads are DISPOSABLE. Process one day at a time, delete raw files after
  extraction. Peak disk use must stay under ~2 GB. NEVER commit raw GRIB/idx files.
- Commit and push the growing output CSVs every ~50 processed days (they are the
  checkpoint; a killed session resumes from the last commit).
- Anonymous access only (NOAA S3 is public, no-sign-request). No credentials anywhere.
- If a step in the spec proves wrong (path pattern changed, variable missing), fix it,
  note the deviation in PROGRESS.md, and continue — do not stall waiting for input.
- Keep PROGRESS.md updated (last processed date, row counts, anomalies) every commit.
