#!/usr/bin/env python3
"""Scrape SEEE weekly (每周概况) and monthly (月度概况) CEA bulletins.

Unlike the daily archive (capped at ~150 listed articles/year), the weekly
(~52/yr) and monthly (12/yr) archives are complete back to July 2021. They
serve two purposes:
  1. bridge the daily-coverage gap 2022-01-04 .. 2022-05-25 at weekly frequency;
  2. independently validate the ccn.ac.cn daily fills (monthly totals).

Usage: python3 pipeline/cea_weekly_monthly.py run
Outputs: carbon/data/cea_weekly.csv, carbon/data/cea_monthly.csv
"""
import csv
import os
import re
import sys
import time
import urllib.request

BASE = "https://overview.cneeex.com"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.environ.get(
    "CEA_WM_CACHE",
    "/tmp/claude-0/-home-user-sd-spot-weather/ed0fdf4b-c3db-500a-8191-da22623353e6/scratchpad/cea_wm_cache",
)
YEARS = ["2021", "2022", "2023", "2024", "2025", "2026"]
LINK_RE = re.compile(r'href="(/c/[0-9-]+/\d+\.shtml)"[^>]*>([^<]*)')
NUM = r"([\d,]+(?:\.\d+)?)"


def get(url, tries=4):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            return urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "ignore")
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(2 ** (k + 1))


def _f(s):
    return float(s.replace(",", "")) if s else None


def body(html):
    from bs4 import BeautifulSoup

    text = BeautifulSoup(html, "lxml").get_text("\n", strip=True)
    i = text.find("发布时间")
    j = text.find("声明", i)
    return re.sub(r"\s+", "", text[i : j if j > i else len(text)]).replace("，", ",").replace("；", ";")


def walk(section, title_re):
    """Yield (key, url, title) for every article in a year-dir section."""
    seen = {}
    for y in YEARS:
        page = 1
        while True:
            suffix = "" if page == 1 else f"index_{page}.shtml"
            try:
                html = get(f"{BASE}/qgtpfqjy/{section}/{y}n/{suffix}")
            except Exception:
                break
            hits = 0
            for path, title in LINK_RE.findall(html):
                m = title_re.search(title)
                if m and m.group(0) not in seen:
                    seen[m.group(0)] = (m.groups(), BASE + path, title.strip())
                    hits += 1
            if hits == 0:
                break
            page += 1
            time.sleep(0.3)
    return seen


def grab(url, key):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, key + ".html")
    if os.path.exists(path) and os.path.getsize(path) > 5000:
        return open(path).read()
    html = get(url)
    open(path, "w").write(html)
    time.sleep(0.2)
    return html


def parse_agg(t, prefix):
    """Parse a weekly/monthly aggregate bulletin body."""
    row = {}
    m = re.search(r"总成交量" + NUM + r"吨,总成交额" + NUM + r"元", t)
    if m:
        row["total_vol_t"], row["total_amt_cny"] = _f(m.group(1)), _f(m.group(2))
    m = re.search(r"挂牌协议(?:交易)?" + prefix + r"?成交量" + NUM + r"吨," + prefix + r"?成交额" + NUM + r"元", t)
    if m:
        row["listed_vol_t"], row["listed_amt_cny"] = _f(m.group(1)), _f(m.group(2))
    elif re.search(r"(无挂牌协议|挂牌协议交易无成交)", t):
        row["listed_vol_t"], row["listed_amt_cny"] = 0.0, 0.0
    m = re.search(r"大宗协议(?:交易)?" + prefix + r"?成交量" + NUM + r"吨," + prefix + r"?成交额" + NUM + r"元", t)
    if m:
        row["block_vol_t"], row["block_amt_cny"] = _f(m.group(1)), _f(m.group(2))
    elif re.search(r"(无大宗协议|大宗协议交易无成交)", t):
        row["block_vol_t"], row["block_amt_cny"] = 0.0, 0.0
    m = re.search(r"最高成交价" + NUM + r"元/吨", t)
    if m:
        row["high"] = _f(m.group(1))
    m = re.search(r"最低成交价" + NUM + r"元/吨", t)
    if m:
        row["low"] = _f(m.group(1))
    m = re.search(r"收盘价(?:为)?" + NUM + r"元/吨", t)
    if m:
        row["close"] = _f(m.group(1))
    m = re.search(r"累计成交量" + NUM + r"吨,累计成交额" + NUM + r"元", t)
    if m:
        row["cum_vol_t"], row["cum_amt_cny"] = _f(m.group(1)), _f(m.group(2))
    return row


def run():
    os.makedirs(os.path.join(REPO, "carbon", "data"), exist_ok=True)
    anomalies = []

    weekly = walk("mzgk", re.compile(r"每周成交数据(\d{8})-(\d{8})"))
    print(f"weekly bulletins found: {len(weekly)}")
    wrows = []
    for key, ((d0, d1), url, title) in sorted(weekly.items()):
        try:
            row = parse_agg(body(grab(url, f"w{d0}")), "周")
        except Exception as e:
            anomalies.append(f"weekly {d0}: {e}")
            continue
        if "total_vol_t" not in row and "listed_vol_t" not in row:
            anomalies.append(f"weekly {d0}: parsed empty")
        row["week_start"] = f"{d0[:4]}-{d0[4:6]}-{d0[6:]}"
        row["week_end"] = f"{d1[:4]}-{d1[4:6]}-{d1[6:]}"
        wrows.append(row)
    wcols = ["week_start", "week_end", "high", "low", "close",
             "listed_vol_t", "listed_amt_cny", "block_vol_t", "block_amt_cny",
             "total_vol_t", "total_amt_cny", "cum_vol_t", "cum_amt_cny"]
    with open(os.path.join(REPO, "carbon", "data", "cea_weekly.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=wcols, extrasaction="ignore")
        w.writeheader()
        w.writerows(sorted(wrows, key=lambda r: r["week_start"]))
    print(f"weekly rows: {len(wrows)}")

    monthly = walk("jysj/ydgk", re.compile(r"(?:每月综合价格行情及成交信息|每月成交数据)(\d{8})-(\d{8})"))
    print(f"monthly bulletins found: {len(monthly)}")
    mrows = []
    for key, (groups, url, title) in sorted(monthly.items()):
        ym = f"{groups[0][:4]}-{groups[0][4:6]}"
        try:
            row = parse_agg(body(grab(url, f"m{ym}")), "月")
        except Exception as e:
            anomalies.append(f"monthly {ym}: {e}")
            continue
        if "total_vol_t" not in row and "listed_vol_t" not in row:
            anomalies.append(f"monthly {ym}: parsed empty")
        row["month"] = ym
        mrows.append(row)
    mcols = ["month", "high", "low", "close",
             "listed_vol_t", "listed_amt_cny", "block_vol_t", "block_amt_cny",
             "total_vol_t", "total_amt_cny", "cum_vol_t", "cum_amt_cny"]
    with open(os.path.join(REPO, "carbon", "data", "cea_monthly.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=mcols, extrasaction="ignore")
        w.writeheader()
        w.writerows(sorted(mrows, key=lambda r: r["month"]))
    print(f"monthly rows: {len(mrows)}")

    if anomalies:
        print("ANOMALIES:")
        for a in anomalies:
            print(" ", a)


if __name__ == "__main__":
    run()
