#!/usr/bin/env python3
"""Scrape SEEE (cneeex.com) daily CEA bulletins into a tidy daily panel.

Source: https://overview.cneeex.com/qgtpfqjy/mrgk/{YYYY}n/ (paginated
index_N.shtml), one article per trading day since 2021-07-16.

Two title/body eras:
  - 2021 – 2023: "全国碳市场每日成交数据YYYYMMDD"; OHLC refers to 挂牌协议 (listed).
  - 2024+      : "【CEA】全国碳市场每日综合价格行情及成交信息YYYYMMDD";
                 OHLC is the 综合价格行情 (composite). Recorded in `price_basis`.

Usage:
  python3 pipeline/cea_scraper.py list          # build article index
  python3 pipeline/cea_scraper.py fetch         # download article pages (cached)
  python3 pipeline/cea_scraper.py parse         # parse cache -> carbon/data/cea_daily.csv
Raw pages are cached under CACHE_DIR (not committed); the CSV is the deliverable.
"""
import csv
import os
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = "https://overview.cneeex.com"
YEARS = ["2021", "2022", "2023", "2024", "2025", "2026"]
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.environ.get(
    "CEA_CACHE",
    "/tmp/claude-0/-home-user-sd-spot-weather/ed0fdf4b-c3db-500a-8191-da22623353e6/scratchpad/cea_cache",
)
INDEX_CSV = os.path.join(CACHE_DIR, "article_index.csv")
OUT_CSV = os.path.join(REPO, "carbon", "data", "cea_daily.csv")
ANOM_LOG = os.path.join(REPO, "carbon", "data", "cea_parse_anomalies.txt")

TITLE_RE = re.compile(r"(?:每日成交数据|每日综合价格行情及成交信息)(\d{8})")
LINK_RE = re.compile(r'href="(/c/[0-9-]+/\d+\.shtml)"[^>]*>([^<]*)')


def get(url, tries=4):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            return urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "ignore")
        except Exception as e:
            if k == tries - 1:
                raise
            time.sleep(2 ** (k + 1))


def build_index():
    os.makedirs(CACHE_DIR, exist_ok=True)
    seen = {}
    for y in YEARS:
        page = 1
        while True:
            suffix = "" if page == 1 else f"index_{page}.shtml"
            url = f"{BASE}/qgtpfqjy/mrgk/{y}n/{suffix}"
            try:
                html = get(url)
            except Exception as e:
                print(f"  {url} -> {e}; stopping year {y}")
                break
            hits = 0
            for path, title in LINK_RE.findall(html):
                m = TITLE_RE.search(title)
                if m:
                    d = m.group(1)
                    if d not in seen:
                        seen[d] = (BASE + path, title.strip())
                        hits += 1
            print(f"year {y} page {page}: +{hits} (total {len(seen)})")
            if hits == 0:
                break
            page += 1
            time.sleep(0.3)
    with open(INDEX_CSV, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["trade_date", "url", "title"])
        for d in sorted(seen):
            w.writerow([d, seen[d][0], seen[d][1]])
    print(f"index: {len(seen)} bulletins -> {INDEX_CSV}")


def fetch_one(row):
    d, url = row["trade_date"], row["url"]
    path = os.path.join(CACHE_DIR, f"{d}.html")
    if os.path.exists(path) and os.path.getsize(path) > 5000:
        return None
    try:
        html = get(url)
        with open(path, "w") as f:
            f.write(html)
        time.sleep(0.2)
        return None
    except Exception as e:
        return f"{d} {url} -> {e}"


def fetch_all():
    rows = list(csv.DictReader(open(INDEX_CSV)))
    errs = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        for i, r in enumerate(ex.map(fetch_one, rows)):
            if r:
                errs.append(r)
            if (i + 1) % 100 == 0:
                print(f"fetched {i + 1}/{len(rows)}")
    print(f"done; {len(errs)} errors")
    for e in errs:
        print(" ", e)


NUM = r"([\d,]+(?:\.\d+)?)"


def _f(s):
    return float(s.replace(",", "")) if s else None


def body_text(html):
    # main article text sits between 发布时间 and the boilerplate 声明
    from bs4 import BeautifulSoup

    text = BeautifulSoup(html, "lxml").get_text("\n", strip=True)
    i = text.find("发布时间")
    j = text.find("声明", i)
    return text[i : j if j > i else len(text)]


def parse_one(d, text, anomalies):
    row = {"trade_date": f"{d[:4]}-{d[4:6]}-{d[6:]}"}
    # bulletins wrap mid-number; Chinese needs no spaces, so drop all whitespace
    t = re.sub(r"\s+", "", text).replace("，", ",").replace("；", ";")

    m = re.search(r"开盘价" + NUM + r"元/吨.{0,20}?最高价" + NUM + r".{0,20}?最低价" + NUM + r".{0,20}?收盘价" + NUM + r"元/吨", t)
    if m:
        row["open"], row["high"], row["low"], row["close"] = map(_f, m.groups())
    else:
        # zero-trade days quote only 开盘/收盘; launch day (20210716) only 收盘
        m = re.search(r"开盘价" + NUM + r"元/吨,收盘价" + NUM + r"元/吨", t)
        if m:
            row["open"], row["close"] = _f(m.group(1)), _f(m.group(2))
        else:
            m = re.search(r"收盘价" + NUM + r"元/吨", t)
            if m:
                row["close"] = _f(m.group(1))
    m = re.search(r"收盘价(?:较前一日)?(上涨|下跌|与前一日持平|持平)" + NUM + r"?%?", t)
    if m:
        sign = {"上涨": 1, "下跌": -1, "与前一日持平": 0, "持平": 0}[m.group(1)]
        row["close_chg_pct"] = sign * (_f(m.group(2)) or 0.0)
    row["price_basis"] = "composite" if ("综合价格行情" in t or "综合价格收盘价" in t) else "listed"

    if "全国碳市场无成交" in t:
        for k in ("listed_vol_t", "listed_amt_cny", "block_vol_t", "block_amt_cny",
                  "auction_vol_t", "auction_amt_cny", "total_vol_t", "total_amt_cny"):
            row[k] = 0.0

    m = re.search(r"挂牌协议(?:交易)?成交量" + NUM + r"吨,成交额" + NUM + r"元", t)
    if m:
        row["listed_vol_t"], row["listed_amt_cny"] = _f(m.group(1)), _f(m.group(2))
    elif re.search(r"(无挂牌协议|挂牌协议交易无成交)", t):
        row["listed_vol_t"], row["listed_amt_cny"] = 0.0, 0.0
    m = re.search(r"大宗协议(?:交易)?成交量" + NUM + r"吨,成交额" + NUM + r"元", t)
    if m:
        row["block_vol_t"], row["block_amt_cny"] = _f(m.group(1)), _f(m.group(2))
    elif re.search(r"(无大宗协议|大宗协议交易无成交)", t):
        row["block_vol_t"], row["block_amt_cny"] = 0.0, 0.0
    m = re.search(r"单向竞价(?:交易)?成交量" + NUM + r"吨,成交额" + NUM + r"元", t)
    if m:
        row["auction_vol_t"], row["auction_amt_cny"] = _f(m.group(1)), _f(m.group(2))
    elif "无单向竞价" in t:
        row["auction_vol_t"], row["auction_amt_cny"] = 0.0, 0.0

    if "大宗" not in t:
        row.setdefault("block_vol_t", 0.0)
        row.setdefault("block_amt_cny", 0.0)

    m = re.search(r"总成交量" + NUM + r"吨,总成交额" + NUM + r"元", t)
    if m:
        row["total_vol_t"], row["total_amt_cny"] = _f(m.group(1)), _f(m.group(2))
    elif row.get("listed_vol_t") is not None and row.get("block_vol_t") is not None:
        row["total_vol_t"] = row["listed_vol_t"] + row["block_vol_t"] + (row.get("auction_vol_t") or 0.0)
        row["total_amt_cny"] = row["listed_amt_cny"] + row["block_amt_cny"] + (row.get("auction_amt_cny") or 0.0)
    m = re.search(r"累计成交量" + NUM + r"吨,累计成交额" + NUM + r"元", t)
    if m:
        row["cum_vol_t"], row["cum_amt_cny"] = _f(m.group(1)), _f(m.group(2))

    # derived VWAPs
    if row.get("listed_vol_t"):
        row["listed_vwap"] = round(row["listed_amt_cny"] / row["listed_vol_t"], 4)
    if row.get("block_vol_t"):
        row["block_vwap"] = round(row["block_amt_cny"] / row["block_vol_t"], 4)
    if row.get("total_vol_t"):
        row["total_vwap"] = round(row["total_amt_cny"] / row["total_vol_t"], 4)

    missing = [k for k in ("close", "listed_vol_t", "total_vol_t", "cum_vol_t") if k not in row]
    if missing:
        anomalies.append(f"{d}: missing {missing}\n---\n{text[:600]}\n===")
    return row


COLS = [
    "trade_date", "price_basis", "open", "high", "low", "close", "close_chg_pct",
    "listed_vol_t", "listed_amt_cny", "listed_vwap",
    "block_vol_t", "block_amt_cny", "block_vwap",
    "auction_vol_t", "auction_amt_cny",
    "total_vol_t", "total_amt_cny", "total_vwap",
    "cum_vol_t", "cum_amt_cny",
]


def parse_all():
    os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
    rows, anomalies = [], []
    for r in csv.DictReader(open(INDEX_CSV)):
        d = r["trade_date"]
        path = os.path.join(CACHE_DIR, f"{d}.html")
        if not os.path.exists(path):
            anomalies.append(f"{d}: page not fetched")
            continue
        rows.append(parse_one(d, body_text(open(path).read()), anomalies))
    rows.sort(key=lambda x: x["trade_date"])
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    with open(ANOM_LOG, "w") as f:
        f.write(f"{len(anomalies)} anomalies\n\n" + "\n".join(anomalies))
    print(f"{len(rows)} rows -> {OUT_CSV}; {len(anomalies)} anomalies -> {ANOM_LOG}")


if __name__ == "__main__":
    {"list": build_index, "fetch": fetch_all, "parse": parse_all}[sys.argv[1]]()
