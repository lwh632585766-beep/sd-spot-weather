#!/usr/bin/env python3
"""Build ``data/sd_grid_cells.csv``: the Shandong 0.25-degree cell list + weights.

Columns
-------
cell_id          0..593, matching the flat order used by :mod:`gfslib`
lat, lon         cell centre (GFS grid point)
land_frac        GFS land-sea mask, 0 = open water .. 1 = all land
in_province      fraction of the cell's area inside the Shandong boundary
offshore_zone    1 if in the Yantai/Weihai offshore box the spec says to keep
retain           1 if the cell enters the province aggregate
w_uniform        unweighted weight (= retain)
w_province       province-area weight (= in_province, over retained cells)
w_wind, w_solar  installed-capacity weights (MW per cell) if a capacity
                 inventory is available, else equal to w_province (see
                 PROGRESS.md for the deviation note)
cap_source       provenance string for w_wind / w_solar

Boundary source: DataV public administrative boundary for Shandong (370000).
Land mask: GFS LAND field, so it is exactly consistent with the forecast grid.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

import numpy as np
import pandas as pd
from shapely.geometry import box, shape
from shapely.ops import unary_union

import gfslib as G

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STATIC = Path(__file__).resolve().parent / "static"
BOUNDARY = STATIC / "shandong_370000.geojson"

# Offshore box from WEATHER_SPEC.md: keep sea cells east of 119.5 between
# lat 35 and 38.5 -- Shandong's offshore wind sits off Yantai/Weihai.
OFF_LON_MIN, OFF_LAT_MIN, OFF_LAT_MAX = 119.5, 35.0, 38.5

# ...but "near-shore" needs a bound. Cells in that box run up to 1.66 deg
# (~166 km) out into the Yellow Sea; keeping all of them would let open-ocean
# wind (systematically stronger than onshore) dominate the province mean.
# 0.5 deg ~ 50 km comfortably covers Shandong's offshore wind sites while
# excluding open sea. Deviation recorded in PROGRESS.md; the exported
# dist_to_province column lets this be re-cut without re-running the pipeline.
OFFSHORE_BUFFER_DEG = 0.5


def province_polygon():
    gj = json.loads(BOUNDARY.read_text())
    geoms = [shape(f["geometry"]) for f in gj["features"]]
    poly = unary_union(geoms)
    if not poly.is_valid:
        poly = poly.buffer(0)
    return poly


def land_fraction() -> np.ndarray:
    """GFS land-sea mask on the Shandong subset (stable across time)."""
    vals, _ = G.get_decoded(dt.date(2024, 1, 1), 0, 1, G.LAND_KEYS)
    return vals["land"]


def cell_boxes():
    half = G.DEG / 2.0
    return [
        box(lon - half, lat - half, lon + half, lat + half)
        for lat, lon in zip(G.CELL_LAT, G.CELL_LON)
    ]


# Capacity inventories, one peer-reviewed source per technology.
#
# Deliberately NOT combined with the offshore-specific inventories (DeepOWT,
# COWT-SAR) that are also in static/. Those are offshore-only detections with
# their own methodology; splicing them onto an OSM onshore count implies a
# ~22% offshore share of Shandong wind, several times the real share over this
# sample. Mixing detection methodologies produces an on/offshore ratio that
# cannot be defended, so each technology gets a single consistent source and
# the limitation is documented instead.
WIND_SRC = STATIC / "dunnett_osm_wind_shandong.csv"     # OSM turbine clusters
SOLAR_SRC = STATIC / "kruitwagen_pv_shandong.csv"       # satellite PV inventory

# Dunnett/OSM gives turbine counts, not MW. Chinese onshore turbines
# commissioned over this sample average roughly 2 MW; the constant only sets
# the units of an internally-normalised weight vector, so it cancels out.
MW_PER_TURBINE = 2.0


def _cell_of(lat, lon):
    """Snap points to flat cell ids; -1 where outside the bbox."""
    j = np.rint((G.LAT_MAX - np.asarray(lat, dtype=float)) / G.DEG).astype(int)
    i = np.rint((np.asarray(lon, dtype=float) - G.LON_MIN) / G.DEG).astype(int)
    ok = (j >= 0) & (j < G.NLAT) & (i >= 0) & (i < G.NLON)
    return np.where(ok, j * G.NLON + i, -1)


def _accumulate(lat, lon, mw) -> np.ndarray:
    w = np.zeros(G.NCELL)
    cid = _cell_of(lat, lon)
    mw = np.asarray(mw, dtype=float)
    good = (cid >= 0) & np.isfinite(mw)
    np.add.at(w, cid[good], mw[good])
    return w


def capacity_weights():
    """Build (w_wind, w_solar, source_label) from the bundled inventories."""
    if not (WIND_SRC.exists() and SOLAR_SRC.exists()):
        return None, None, None

    wind = pd.read_csv(WIND_SRC)
    w_wind = _accumulate(wind["latitude"], wind["longitude"],
                         wind["count"] * MW_PER_TURBINE)

    solar = pd.read_csv(SOLAR_SRC)
    # The bbox overlaps Hebei/Henan/Jiangsu; Kruitwagen carries a province code,
    # so restrict solar to Shandong proper (CN-37) rather than the whole box.
    if "iso_3166_2" in solar.columns:
        solar = solar[solar["iso_3166_2"].astype(str).str.upper() == "CN-37"]
    w_solar = _accumulate(solar["latitude"], solar["longitude"],
                          solar["capacity_mw"])

    if w_wind.sum() <= 0 or w_solar.sum() <= 0:
        return None, None, None
    return w_wind, w_solar, "wind=OSM/Dunnett turbine counts; solar=Kruitwagen PV"


def main():
    ap = argparse.ArgumentParser()

    ap.add_argument("--offshore-buffer", type=float, default=OFFSHORE_BUFFER_DEG,
                    help="max degrees from the province boundary for sea cells")
    args = ap.parse_args()

    poly = province_polygon()
    land = land_fraction()
    boxes = cell_boxes()
    cell_area = G.DEG * G.DEG

    in_prov = np.array([b.intersection(poly).area / cell_area for b in boxes])
    in_prov = np.clip(in_prov, 0.0, 1.0)
    dist = np.array([b.distance(poly) for b in boxes])

    offshore = (
        (G.CELL_LON >= OFF_LON_MIN)
        & (G.CELL_LAT >= OFF_LAT_MIN)
        & (G.CELL_LAT <= OFF_LAT_MAX)
    )
    # Retain: any cell overlapping the province, plus near-shore sea cells in
    # the offshore wind box (which lie outside the land boundary by definition).
    near_shore = offshore & (land < 0.5) & (dist <= args.offshore_buffer)
    retain = (in_prov > 0.01) | near_shore

    cells = pd.DataFrame({
        "cell_id": np.arange(G.NCELL),
        "lat": G.CELL_LAT,
        "lon": G.CELL_LON,
        "land_frac": np.round(land, 4),
        "in_province": np.round(in_prov, 4),
        "dist_to_province": np.round(dist, 4),
        "offshore_zone": offshore.astype(int),
        "retain": retain.astype(int),
    })

    # w_uniform: equal weight over cells that actually overlap Shandong.
    #
    # It deliberately does NOT give equal weight to every retained cell. The
    # retained set includes 113 near-shore sea cells so that offshore wind is
    # not dropped, but they are 31% of the retained set while offshore is a far
    # smaller share of Shandong's wind fleet. An equal-weighted mean over all
    # retained cells would hand open water ~31% of the province aggregate --
    # marine wind is systematically stronger, so that inflates the level and
    # damps the diurnal cycle. Offshore instead enters through w_wind, where
    # its share is set by observed turbine locations (~15%), which is what the
    # spec's instruction to keep those cells was actually protecting.
    province_cell = in_prov > 0.01
    cells["w_uniform"] = np.where(province_cell, 1.0, 0.0)
    # Province-area weight: share of the cell inside Shandong.
    cells["w_province"] = np.round(np.where(province_cell, in_prov, 0.0), 4)

    w_wind, w_solar, src = capacity_weights()
    if w_wind is None:
        cells["w_wind"] = cells["w_province"]
        cells["w_solar"] = cells["w_province"]
        cells["cap_source"] = "fallback:w_province"
    else:
        cells["w_wind"] = np.round(w_wind * retain, 4)
        cells["w_solar"] = np.round(w_solar * retain, 4)
        cells["cap_source"] = src
        print(f"  wind  weight: {w_wind[retain].sum():8.0f} MW-equiv over "
              f"{int((w_wind * retain > 0).sum())} cells")
        print(f"  solar weight: {w_solar[retain].sum():8.0f} MW over "
              f"{int((w_solar * retain > 0).sum())} cells")

    DATA.mkdir(exist_ok=True)
    out = DATA / "sd_grid_cells.csv"
    cells.to_csv(out, index=False)

    # Offshore exposure of each weighting -- the number to check before a run.
    sea = cells["land_frac"].to_numpy() < 0.5
    print("\n  sea-cell share of each weight vector "
          "(land_frac < 0.5; offshore wind is a minority of Shandong's fleet):")
    for col in ("w_uniform", "w_province", "w_wind", "w_solar"):
        w = cells[col].to_numpy(dtype=float) * retain
        tot = w.sum()
        print(f"    {col:11s} {100 * w[sea].sum() / tot:5.1f}%   "
              f"({int((w > 0).sum()):3d} cells carry weight)")

    print(f"\nwrote {out}  ({len(cells)} cells, {int(retain.sum())} retained)")
    print(f"  land cells (land>=0.5): {int((land >= 0.5).sum())}")
    print(f"  in-province cells:      {int((in_prov > 0.01).sum())}")
    print(f"  offshore retained:      {int((offshore & (land < 0.5) & retain).sum())}")
    print(f"  capacity source:        {cells['cap_source'].iat[0]}")


if __name__ == "__main__":
    main()
