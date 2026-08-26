#!/usr/bin/env python3
"""Pass-through regression scaffold: CEA carbon costs -> Shandong spot prices.

STATUS: runs in dry mode until the researcher's local Shandong spot panel is
dropped into carbon/data/local/. Everything else it needs is in the repo.

Expected local file (NOT committed if confidential; carbon/data/local/ is
gitignored): carbon/data/local/sd_spot_prices.csv with columns
    date_cst   YYYY-MM-DD  (delivery day, Beijing time)
    hour_cst   0..23
    da_price   day-ahead clearing price, CNY/MWh
    rt_price   real-time price, CNY/MWh
Any extra columns are carried through.

Design (see carbon/TOPICS.md, topic 1):
  - Treatment: daily CEA price P_t (close and total VWAP; carbon/data/
    cea_daily_merged.csv), and TPS-adjusted net marginal carbon cost
    (e_type - b_type,year) * P_t once carbon/data/benchmarks.csv lands.
  - Timing: day-ahead market for delivery day D clears mid-day D-1 CST, so
    the carbon price that can enter D's DA bids is P_{D-1} (CEA trading
    09:30-15:00 CST; use close of D-1). RT prices on day D can react to P_D.
  - Baseline: Delta log(da_price_bar_D) on Delta log(CEA_{D-1}) with
    distributed lags; hour-level heterogeneity (peak/off-peak, Hintermann
    2016); event-window versions using carbon/data/events.csv.
"""
import csv
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "carbon", "data")
LOCAL = os.path.join(DATA, "local", "sd_spot_prices.csv")


def load_cea():
    cea = {}
    for r in csv.DictReader(open(os.path.join(DATA, "cea_daily_merged.csv"))):
        cea[r["trade_date"]] = {
            "close": float(r["close"]) if r["close"] else None,
            "vwap": float(r["total_vwap"]) if r["total_vwap"] else None,
            "vol": float(r["total_vol_t"]) if r["total_vol_t"] else None,
        }
    return cea


def main():
    cea = load_cea()
    print(f"CEA daily series: {len(cea)} days loaded")
    if not os.path.exists(LOCAL):
        print(f"[dry run] local Shandong spot panel not found at {LOCAL}")
        print("Drop the file there (schema in this script's header) and rerun;")
        print("the merge + first-differences regression will then execute.")
        return
    # ---- merge and baseline regression (executes only with local data) ----
    import datetime as dt
    import math

    days = {}
    for r in csv.DictReader(open(LOCAL)):
        d = r["date_cst"]
        days.setdefault(d, []).append(float(r["da_price"]))
    obs = []
    for d, prices in sorted(days.items()):
        day = dt.date.fromisoformat(d)
        prev = (day - dt.timedelta(days=1)).isoformat()
        # nearest prior CEA trading day for the D-1 information set
        p = None
        for back in range(1, 8):
            cand = (day - dt.timedelta(days=back)).isoformat()
            if cand in cea and cea[cand]["close"]:
                p = cea[cand]["close"]
                break
        if p and prices:
            obs.append((d, sum(prices) / len(prices), p))
    # first differences in logs
    xs, ys = [], []
    for (d0, da0, p0), (d1, da1, p1) in zip(obs, obs[1:]):
        if da0 > 0 and da1 > 0 and p0 > 0 and p1 > 0:
            ys.append(math.log(da1) - math.log(da0))
            xs.append(math.log(p1) - math.log(p0))
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    beta = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    resid = [y - my - beta * (x - mx) for x, y in zip(xs, ys)]
    se = (sum(r * r for r in resid) / (n - 2) / sum((x - mx) ** 2 for x in xs)) ** 0.5
    print(f"Baseline OLS (dlog daily-mean DA price on dlog CEA close, n={n}):")
    print(f"  elasticity beta = {beta:.4f} (se {se:.4f})  [descriptive only; use the R/Stata spec for the paper]")


if __name__ == "__main__":
    main()
