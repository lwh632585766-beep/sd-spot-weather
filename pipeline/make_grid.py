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


def capacity_weights(cells: pd.DataFrame, capfile: Path | None):
    """Sum plant capacity (MW) into cells from an inventory CSV, if provided.

    The CSV must have latitude/longitude/capacity columns and a technology
    column distinguishing wind from solar. Returns (w_wind, w_solar, source).
    """
    if capfile is None or not capfile.exists():
        return None, None, None

    df = pd.read_csv(capfile)
    cols = {c.lower(): c for c in df.columns}

    def pick(*names):
        for n in names:
            if n in cols:
                return cols[n]
        return None

    c_lat = pick("latitude", "lat", "y")
    c_lon = pick("longitude", "lon", "lng", "x")
    c_cap = pick("capacity_mw", "capacity (mw)", "capacity", "mw")
    c_tec = pick("technology", "type", "fuel", "source", "primary_fuel")
    if not all([c_lat, c_lon, c_cap, c_tec]):
        raise SystemExit(f"{capfile}: need lat/lon/capacity/technology columns, "
                         f"found {list(df.columns)}")

    df = df[[c_lat, c_lon, c_cap, c_tec]].copy()
    df.columns = ["lat", "lon", "cap", "tech"]
    df = df.dropna(subset=["lat", "lon", "cap"])
    df["tech"] = df["tech"].astype(str).str.lower()

    half = G.DEG / 2.0
    # snap each plant to its grid cell
    j = np.rint((G.LAT_MAX - df["lat"].to_numpy()) / G.DEG).astype(int)
    i = np.rint((df["lon"].to_numpy() - G.LON_MIN) / G.DEG).astype(int)
    ok = (j >= 0) & (j < G.NLAT) & (i >= 0) & (i < G.NLON)
    cid = j * G.NLON + i

    w_wind = np.zeros(G.NCELL)
    w_solar = np.zeros(G.NCELL)
    for k in np.nonzero(ok)[0]:
        tech, cap = df["tech"].iat[k], float(df["cap"].iat[k])
        if "wind" in tech:
            w_wind[cid[k]] += cap
        elif "solar" in tech or "pv" in tech:
            w_solar[cid[k]] += cap
    if w_wind.sum() == 0 and w_solar.sum() == 0:
        return None, None, None
    return w_wind, w_solar, capfile.name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--capacity", type=Path, default=None,
                    help="optional plant inventory CSV for w_wind/w_solar")
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

    cells["w_uniform"] = cells["retain"].astype(float)
    # Province-area weight: pure share of the cell inside Shandong, so sea
    # cells carry zero. Paired with w_uniform (which does include near-shore
    # sea) these bracket the treatment of offshore wind.
    cells["w_province"] = np.round(np.where(retain, in_prov, 0.0), 4)

    w_wind, w_solar, src = capacity_weights(cells, args.capacity)
    if w_wind is None:
        cells["w_wind"] = cells["w_province"]
        cells["w_solar"] = cells["w_province"]
        cells["cap_source"] = "fallback:w_province"
    else:
        cells["w_wind"] = np.round(w_wind * retain, 4)
        cells["w_solar"] = np.round(w_solar * retain, 4)
        cells["cap_source"] = src

    DATA.mkdir(exist_ok=True)
    out = DATA / "sd_grid_cells.csv"
    cells.to_csv(out, index=False)

    print(f"wrote {out}  ({len(cells)} cells, {int(retain.sum())} retained)")
    print(f"  land cells (land>=0.5): {int((land >= 0.5).sum())}")
    print(f"  in-province cells:      {int((in_prov > 0.01).sum())}")
    print(f"  offshore retained:      {int((offshore & (land < 0.5) & retain).sum())}")
    print(f"  capacity source:        {cells['cap_source'].iat[0]}")


if __name__ == "__main__":
    main()
