#!/usr/bin/env python3
"""CEA price reactions around policy events (Kaenzig-style shock series draft).

Needs carbon/data/events.csv (date,event,category,...) and the merged daily
panel. For each event: log-return of CEA close over [-1,+k] trading-day
windows, plus abnormal volume. Events on non-trading days map to the next
trading day. Output: carbon/output/event_reactions.csv

Run: python3 pipeline/cea_events.py
"""
import csv
import math
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "carbon", "data")
OUT = os.path.join(REPO, "carbon", "output")
WINDOWS = (1, 3, 5, 10)


def main():
    rows = list(csv.DictReader(open(os.path.join(DATA, "cea_daily_merged.csv"))))
    dates = [r["trade_date"] for r in rows]
    close = {r["trade_date"]: float(r["close"]) for r in rows if r["close"]}
    vol = {r["trade_date"]: float(r["total_vol_t"] or 0) for r in rows}
    idx = {d: i for i, d in enumerate(dates)}

    ev_path = os.path.join(DATA, "events.csv")
    if not os.path.exists(ev_path):
        print(f"[dry run] {ev_path} not found yet")
        return
    events = list(csv.DictReader(open(ev_path)))
    os.makedirs(OUT, exist_ok=True)

    med_vol = sorted(vol.values())[len(vol) // 2]
    out = []
    for e in events:
        d = e["date"]
        # map to first trading day >= d
        td = next((x for x in dates if x >= d), None)
        if td is None or td not in idx:
            continue
        i = idx[td]
        row = {"date": d, "trade_day": td, "event": e["event"], "category": e["category"]}
        base_i = i - 1
        while base_i >= 0 and dates[base_i] not in close:
            base_i -= 1
        base = close.get(dates[base_i]) if base_i >= 0 else None
        for k in WINDOWS:
            j = min(i + k - 1, len(dates) - 1)
            end = None
            for jj in range(j, i - 1, -1):
                if dates[jj] in close:
                    end = close[dates[jj]]
                    break
            row[f"ret_{k}d_pct"] = round((math.log(end / base)) * 100, 3) if base and end else None
        w5 = [vol.get(dates[jj], 0) for jj in range(i, min(i + 5, len(dates)))]
        row["vol_5d_over_median"] = round(sum(w5) / len(w5) / med_vol, 2) if w5 and med_vol else None
        import datetime as _dt
        gap = (_dt.date.fromisoformat(td) - _dt.date.fromisoformat(d)).days
        row["gap_days_to_trade_day"] = gap
        if gap > 5:  # event falls in a data hole; windowed returns meaningless
            for k in WINDOWS:
                row[f"ret_{k}d_pct"] = None
            row["vol_5d_over_median"] = None
        out.append(row)

    cols = ["date", "trade_day", "event", "category"] + [f"ret_{k}d_pct" for k in WINDOWS] + [
        "vol_5d_over_median", "gap_days_to_trade_day"]
    with open(os.path.join(OUT, "event_reactions.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(out)
    print(f"{len(out)} events -> carbon/output/event_reactions.csv")


if __name__ == "__main__":
    main()
