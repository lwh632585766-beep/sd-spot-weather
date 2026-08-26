#!/usr/bin/env python3
"""First-pass stylized facts from the CEA daily panel.

Produces carbon/output/:
  monthly_structure.csv   volume by leg, compliance-clustering shares
  block_discount.csv      daily block-vs-listed VWAP discount
  stylized_facts.md       headline numbers for the paper

Run: python3 pipeline/carbon_analysis.py
The Shandong spot-price merge lives in carbon_passthrough.py (needs the
researcher's local sd spot CSV; see that file's header for the schema).
"""
import csv
import os
import statistics
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "carbon", "data")
OUT = os.path.join(REPO, "carbon", "output")

DEADLINES = {  # compliance cycle -> surrender deadline month
    "cycle1 (2019-20)": "2021-12",
    "cycle2 (2021-22)": "2023-12",
    "cycle3 (2023)": "2024-12",
    "cycle4 (2024, power+industry)": "2025-12",
}


def f(x):
    return float(x) if x not in (None, "") else None


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = list(csv.DictReader(open(os.path.join(DATA, "cea_daily_merged.csv"))))

    # ---- monthly structure ----
    mon = defaultdict(lambda: defaultdict(float))
    for r in rows:
        m = r["trade_date"][:7]
        mon[m]["days"] += 1
        for k in ("listed_vol_t", "block_vol_t", "auction_vol_t", "total_vol_t", "total_amt_cny"):
            mon[m][k] += f(r[k]) or 0.0
    with open(os.path.join(OUT, "monthly_structure.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["month", "days", "listed_vol_t", "block_vol_t", "auction_vol_t",
                    "total_vol_t", "total_amt_cny", "block_share", "vwap"])
        for m in sorted(mon):
            d = mon[m]
            w.writerow([m, int(d["days"]), d["listed_vol_t"], d["block_vol_t"], d["auction_vol_t"],
                        d["total_vol_t"], d["total_amt_cny"],
                        round(d["block_vol_t"] / d["total_vol_t"], 4) if d["total_vol_t"] else "",
                        round(d["total_amt_cny"] / d["total_vol_t"], 4) if d["total_vol_t"] else ""])

    # ---- block discount ----
    disc = []
    with open(os.path.join(OUT, "block_discount.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["trade_date", "listed_vwap", "block_vwap", "block_discount_pct", "block_vol_t"])
        for r in rows:
            lv, bv = f(r["listed_vwap"]), f(r["block_vwap"])
            if lv and bv and f(r["block_vol_t"]):
                pct = round((bv / lv - 1) * 100, 3)
                disc.append(pct)
                w.writerow([r["trade_date"], lv, bv, pct, r["block_vol_t"]])

    # ---- headline facts ----
    tot_all = sum(f(r["total_vol_t"]) or 0 for r in rows)
    lines = ["# CEA market stylized facts (auto-generated)", ""]
    lines.append(f"Sample: {rows[0]['trade_date']} .. {rows[-1]['trade_date']}, {len(rows)} trading days "
                 "(daily hole 2022-01-04..2022-05-25; weekly bridge in data/cea_weekly.csv).")
    lines.append("")
    lines.append("## Compliance-deadline clustering (share of total volume in deadline month)")
    year_tot = defaultdict(float)
    for m, d in mon.items():
        year_tot[m[:4]] += d["total_vol_t"]
    for cyc, m in DEADLINES.items():
        if m in mon and year_tot[m[:4]]:
            lines.append(f"- {cyc}: {mon[m]['total_vol_t']:,.0f} t in {m} = "
                         f"{mon[m]['total_vol_t'] / year_tot[m[:4]] * 100:.1f}% of that year's volume")
    lines.append("")
    lines.append("## Block-trade share and discount")
    block_all = sum(f(r["block_vol_t"]) or 0 for r in rows)
    lines.append(f"- Block share of total volume, full sample: {block_all / tot_all * 100:.1f}%")
    if disc:
        lines.append(f"- Daily block-vs-listed VWAP discount (days with both legs, n={len(disc)}): "
                     f"mean {statistics.mean(disc):+.2f}%, median {statistics.median(disc):+.2f}%, "
                     f"p10 {sorted(disc)[len(disc)//10]:+.2f}%, p90 {sorted(disc)[-len(disc)//10]:+.2f}%")
    lines.append("")
    lines.append("## Zero/thin trading")
    zero_listed = sum(1 for r in rows if (f(r["listed_vol_t"]) or 0) == 0)
    zero_total = sum(1 for r in rows if (f(r["total_vol_t"]) or 0) == 0)
    lines.append(f"- Days with zero listed volume: {zero_listed}/{len(rows)}")
    lines.append(f"- Days with zero total volume: {zero_total}/{len(rows)}")
    lines.append("")
    lines.append("## Price path (close, composite basis from 2023-08-28)")
    for y in sorted({r['trade_date'][:4] for r in rows}):
        yr = [f(r["close"]) for r in rows if r["trade_date"].startswith(y) and f(r["close"])]
        if yr:
            lines.append(f"- {y}: min {min(yr):.2f}, max {max(yr):.2f}, last {yr[-1]:.2f} CNY/t")
    with open(os.path.join(OUT, "stylized_facts.md"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
