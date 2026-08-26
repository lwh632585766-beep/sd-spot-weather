#!/usr/bin/env python3
"""Scrape ccn.ac.cn (碳中和网) monthly CEA tables into a per-vintage daily panel.

ccn.ac.cn republishes the SEEE national-carbon-market daily data as one HTML
table per month ("全国碳排放权交易信息（YYYY年M月）"), with per-allowance-vintage
(配额年度: CEA, CEA19-20, CEA21, ...) daily rows: OHLC, pct change, and
volume/amount split into listed (挂牌), block (大宗) and one-way auction (单向).
Provenance: the underlying numbers are SEEE disclosures; cite SEEE as origin.

Usage:
  python3 pipeline/ccn_scraper.py list
  python3 pipeline/ccn_scraper.py fetch
  python3 pipeline/ccn_scraper.py parse   # -> carbon/data/cea_daily_by_vintage.csv
"""
import csv
import os
import re
import sys
import time
import urllib.request

BASE = "https://www.ccn.ac.cn"
INDEX = BASE + "/3060/carbon-market/carbon-emissions-trading/ceadate"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.environ.get(
    "CCN_CACHE",
    "/tmp/claude-0/-home-user-sd-spot-weather/ed0fdf4b-c3db-500a-8191-da22623353e6/scratchpad/ccn_cache",
)
INDEX_CSV = os.path.join(CACHE_DIR, "month_index.csv")
OUT_CSV = os.path.join(REPO, "carbon", "data", "cea_daily_by_vintage.csv")
ANOM_LOG = os.path.join(REPO, "carbon", "data", "ccn_parse_anomalies.txt")

TITLE_RE = re.compile(r"全国碳排放权交易信息（(\d{4})年(\d{1,2})月）")
LINK_RE = re.compile(r'href="(https://www\.ccn\.ac\.cn/carbon-market/carbon-emissions-trading/ceadate/\d+\.html)"[^>]*title="([^"]+)"')


def get(url, tries=4):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            return urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "ignore")
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(2 ** (k + 1))


def build_index():
    os.makedirs(CACHE_DIR, exist_ok=True)
    seen = {}
    page = 1
    while True:
        url = INDEX if page == 1 else f"{INDEX}/page/{page}"
        try:
            html = get(url)
        except Exception as e:
            print(f"{url} -> {e}; stop")
            break
        hits = 0
        for link, title in LINK_RE.findall(html):
            m = TITLE_RE.search(title)
            if m:
                ym = f"{m.group(1)}-{int(m.group(2)):02d}"
                if ym not in seen:
                    seen[ym] = link
                    hits += 1
        print(f"page {page}: +{hits} (total {len(seen)})")
        if hits == 0:
            break
        page += 1
        time.sleep(0.3)
    with open(INDEX_CSV, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "url"])
        for ym in sorted(seen):
            w.writerow([ym, seen[ym]])
    print(f"index: {len(seen)} months ({min(seen)} .. {max(seen)}) -> {INDEX_CSV}")


def fetch_all():
    rows = list(csv.DictReader(open(INDEX_CSV)))
    for i, r in enumerate(rows):
        path = os.path.join(CACHE_DIR, f"{r['month']}.html")
        if os.path.exists(path) and os.path.getsize(path) > 20000:
            continue
        try:
            html = get(r["url"])
            open(path, "w").write(html)
        except Exception as e:
            print(f"{r['month']} -> {e}")
        time.sleep(0.4)
        if (i + 1) % 10 == 0:
            print(f"fetched {i + 1}/{len(rows)}")
    print("fetch done")


HEADER_MAP = {
    "时间": "trade_date", "配额年度": "vintage",
    "开盘（元）": "open", "最高（元）": "high", "最低（元）": "low", "收盘（元）": "close",
    "涨跌幅度（%）": "chg_pct",
    "成交量（吨）": "total_vol_t", "成交额（元）": "total_amt_cny",
    "挂牌成交量（吨）": "listed_vol_t", "挂牌成交额（元）": "listed_amt_cny",
    "大宗成交量（吨）": "block_vol_t", "大宗成交额（元）": "block_amt_cny",
    "单向成交量（吨）": "auction_vol_t", "单向成交额（元）": "auction_amt_cny",
}
NUM_COLS = [v for v in HEADER_MAP.values() if v not in ("trade_date", "vintage")]
COLS = ["trade_date", "vintage"] + NUM_COLS + ["source_month"]


def norm_header(s):
    return re.sub(r"\s+", "", s)


def parse_month(month, html, anomalies):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "lxml")
    tables = soup.find_all("table")
    if not tables:
        anomalies.append(f"{month}: no table")
        return []
    rows_out = []
    for table in tables:
        trs = table.find_all("tr")
        if len(trs) < 2:
            continue
        header = [norm_header(td.get_text(strip=True)) for td in trs[0].find_all(["td", "th"])]
        cols = [HEADER_MAP.get(h) for h in header]
        if "trade_date" not in cols:
            continue
        unknown = [h for h, c in zip(header, cols) if c is None and h]
        if unknown:
            anomalies.append(f"{month}: unknown columns {unknown}")
        for tr in trs[1:]:
            cells = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
            if len(cells) != len(cols) or not cells[0]:
                continue
            row = {"source_month": month}
            for c, val in zip(cols, cells):
                if c is None:
                    continue
                if c == "trade_date":
                    m = re.match(r"(\d{4})[/-](\d{1,2})[/-](\d{1,2})", val)
                    if not m:
                        row = None
                        break
                    row[c] = f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
                elif c == "vintage":
                    row[c] = val
                else:
                    v = val.replace(",", "").replace("%", "").replace("—", "").replace("-", "") if c == "chg_pct" else val.replace(",", "")
                    try:
                        row[c] = float(v) if v not in ("", "—", "/") else None
                    except ValueError:
                        row[c] = None
            if row and row.get("trade_date"):
                # Known source typo: the "2023年1月" page labels its January
                # table 2022/12/D. Verified against the SEEE weekly bulletin
                # 20230103-20230106 (volumes/amounts match to the yuan).
                if month == "2023-01" and row["trade_date"].startswith("2022-12-"):
                    row["trade_date"] = "2023-01-" + row["trade_date"][8:]
                row.setdefault("vintage", "CEA")
                # normalize vintage labels (CEA-19-20 -> CEA19-20, CEA-21 -> CEA21)
                row["vintage"] = re.sub(r"^CEA-", "CEA", row["vintage"].replace(" ", ""))
                rows_out.append(row)
    if not rows_out:
        anomalies.append(f"{month}: table parsed to 0 rows")
    return rows_out


def parse_all():
    os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
    all_rows, anomalies = [], []
    for r in csv.DictReader(open(INDEX_CSV)):
        path = os.path.join(CACHE_DIR, f"{r['month']}.html")
        if not os.path.exists(path):
            anomalies.append(f"{r['month']}: not fetched")
            continue
        all_rows.extend(parse_month(r["month"], open(path).read(), anomalies))
    # dedupe (a date may appear in two adjacent monthly posts)
    dedup = {}
    for row in all_rows:
        dedup[(row["trade_date"], row.get("vintage", "CEA"))] = row
    rows = sorted(dedup.values(), key=lambda x: (x["trade_date"], x.get("vintage", "")))
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    with open(ANOM_LOG, "w") as f:
        f.write(f"{len(anomalies)} anomalies\n\n" + "\n".join(anomalies))
    dates = sorted({r["trade_date"] for r in rows})
    print(f"{len(rows)} rows, {len(dates)} dates ({dates[0]} .. {dates[-1]}) -> {OUT_CSV}")
    print(f"{len(anomalies)} anomalies -> {ANOM_LOG}")


if __name__ == "__main__":
    {"list": build_index, "fetch": fetch_all, "parse": parse_all}[sys.argv[1]]()
