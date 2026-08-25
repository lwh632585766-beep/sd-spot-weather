# PROGRESS

_Updated: 2026-08-25 05:30 UTC_

## Coverage

- Processed through: **2026-06-07**
- Days in panel: **1650**
- Rows: **79,200** (expected 48 per day: 24 hours x 2 vintages)
- Date range: 2021-12-01 .. 2026-06-07

## Value ranges

| column | mean | sd | min | max | n_missing |
|---|---|---|---|---|---|
| wind10_fc | 3.724 | 1.536 | 0.856 | 11.469 | 11 |
| wind10_an | 3.682 | 1.521 | 0.906 | 11.867 | 16 |
| e_wind10 | 0.042 | 0.329 | -2.123 | 2.782 | 27 |
| wind100_fc | 5.557 | 2.283 | 0.899 | 16.202 | 11 |
| wind100_an | 5.484 | 2.246 | 0.931 | 16.554 | 16 |
| e_wind100 | 0.072 | 0.519 | -3.118 | 3.860 | 27 |
| dswrf_fc | 193.783 | 269.817 | 0.000 | 1014.130 | 17 |
| dswrf_an | 194.502 | 270.613 | 0.000 | 1017.918 | 24 |
| e_dswrf | -0.705 | 21.180 | -338.280 | 287.695 | 41 |

## Spatial weighting in force

Cells: 594 in the bbox, 392 retained (271 land, 121 sea).
Capacity source: `wind=OSM/Dunnett turbine counts; solar=Kruitwagen PV`.

| weight | used by | sea-cell share | cells with weight |
|---|---|---|---|
| `w_uniform` | unweighted columns | 13.1% | 312 |
| `w_province` | (reference) | 4.6% | 312 |
| `w_wind` | `wind*_cw` | 15.2% | 71 |
| `w_solar` | `dswrf*_cw` | 1.2% | 194 |

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

5. **Error magnitudes are understated relative to true forecast error.** The
   "actual" is itself a GFS short-lead forecast, so it shares initial
   conditions and model physics with the day-ahead forecast. These errors
   measure the day-ahead-vs-near-analysis revision, not forecast-vs-observation
   error. The exogenous surprise component is preserved, but levels are not
   comparable to station-verified RMSE. ERA5 (needs a Copernicus CDS account)
   remains the robustness option the spec notes.

## Anomalies

- `2022-11-26..2022-11-30: 2022-11-29 18z f002: error: Wrong message length`
- `2022-11-26..2022-11-30: 2022-11-29 18z f003: error: Wrong message length`
- `2022-11-26..2022-11-30: 2022-11-30 00z f002: error: Wrong message length`
- `2022-11-26..2022-11-30: 2022-11-30 00z f005: error: Wrong message length`
- `2022-11-26..2022-11-30: 2022-11-30 06z f002: error: Wrong message length`
- `2022-11-26..2022-11-30: 2022-11-30 06z f003: error: Wrong message length`
- `2022-11-26..2022-11-30: 2022-11-30 06z f004: error: Wrong message length`
- `2022-11-26..2022-11-30: 2022-11-30 06z f005: error: Wrong message length`
- `2022-12-01..2022-12-05: 2022-11-30 00z f016: error: Wrong message length`
- `2022-12-01..2022-12-05: 2022-11-30 00z f020: error: Wrong message length`
- `2022-12-01..2022-12-05: 2022-11-30 00z f026: error: Wrong message length`
- `2022-12-01..2022-12-05: 2022-11-30 00z f027: error: Wrong message length`
- `2022-12-01..2022-12-05: 2022-11-30 00z f028: error: Wrong message length`
- `2022-12-01..2022-12-05: 2022-11-30 00z f029: error: Wrong message length`
- `2022-12-01..2022-12-05: 2022-11-30 00z f031: error: Wrong message length`
- `2022-12-01..2022-12-05: 2022-11-30 00z f033: error: Wrong message length`
- `2022-12-01..2022-12-05: 2022-11-30 00z f035: error: Wrong message length`
- `2022-12-01..2022-12-05: 2022-11-30 00z f036: error: Wrong message length`
- `2022-12-01..2022-12-05: 2022-11-30 00z f038: error: Wrong message length`

_Elapsed this run: 71.0 min_
