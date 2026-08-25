# PROGRESS

_Updated: 2026-08-25 04:15 UTC_

## Coverage

- Processed through: **2022-03-10**
- Days in panel: **100**
- Rows: **4,800** (expected 48 per day: 24 hours x 2 vintages)
- Date range: 2021-12-01 .. 2022-03-10

## Value ranges

| column | mean | sd | min | max | n_missing |
|---|---|---|---|---|---|
| wind10_fc | 3.997 | 1.569 | 1.076 | 10.788 | 0 |
| wind10_an | 4.013 | 1.569 | 1.379 | 10.678 | 0 |
| e_wind10 | -0.016 | 0.239 | -1.832 | 1.045 | 0 |
| wind100_fc | 5.430 | 2.210 | 1.239 | 14.739 | 0 |
| wind100_an | 5.450 | 2.211 | 1.502 | 14.314 | 0 |
| e_wind100 | -0.020 | 0.355 | -2.441 | 1.699 | 0 |
| dswrf_fc | 137.979 | 206.846 | -0.009 | 801.330 | 0 |
| dswrf_an | 138.320 | 207.384 | -0.007 | 798.920 | 0 |
| e_dswrf | -0.342 | 9.743 | -90.677 | 105.876 | 0 |

## Spec deviations

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

3. **Near-shore bounded to 0.5 deg (~50 km) from the province boundary.** The
   spec says keep sea cells east of 119.5 between lat 35-38.5. Taken literally
   that retains 159 sea cells reaching 166 km into the Yellow Sea, where wind
   is systematically stronger, which would dominate the province mean. Bounding
   to 50 km keeps 113 cells, covering Shandong's offshore wind sites. The cell
   file exports `dist_to_province` so this can be re-cut without re-running.

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

5. **Error magnitudes are understated relative to true forecast error.** The
   "actual" is itself a GFS short-lead forecast, so it shares initial
   conditions and model physics with the day-ahead forecast. These errors
   measure the day-ahead-vs-near-analysis revision, not forecast-vs-observation
   error. The exogenous surprise component is preserved, but levels are not
   comparable to station-verified RMSE. ERA5 (needs a Copernicus CDS account)
   remains the robustness option the spec notes.

## Anomalies

- none: every GFS object requested so far decoded cleanly

_Elapsed this run: 4.4 min_
