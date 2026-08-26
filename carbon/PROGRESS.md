# 碳市场论文(选题 1:碳成本传导)——云端数据工作进度

维护:云端 session。最后更新:2026-08-26。天气面板任务(WEATHER_SPEC.md)另有 PROGRESS.md,与本文件无关。

## 已完成

### CEA 日度价格面板(核心交付,已验证)

| 文件 | 内容 | 覆盖 |
|---|---|---|
| `data/cea_daily.csv` | 环交所每日公报逐日解析(权威源),挂牌 OHLC/量额、大宗量额、单向竞价、当日总量、累计量,`price_basis` 标注口径 | 2021-07-16→2026-08-14 的 863 天(各年档案只保留最近 ~150 篇,故 2022–2025 各缺 1–5 月) |
| `data/cea_daily_by_vintage.csv` | ccn.ac.cn 月度表逐日**分配额年度**(CEA19-20/21/22/23/24/25)行情,含挂牌/大宗/单向分列 | 2023-01-03→2026-07-31,3,148 行 |
| `data/cea_daily_merged.csv` | 合并日度序列,`source` 标注 seee/ccn,ccn 填充段补齐环交所截断窗口 | 2021-07-16→2026-08-14 共 1,140 天 |
| `data/cea_weekly.csv` | 每周概况(2021-07→2022-12,73 周)——**桥接 2022 上半年日度缺口** | |
| `data/cea_monthly.csv` | 月度概况(2021-07→2026-07,61 个月)——用于验证 | |
| `data/cea_validation_report.md` | 三重交叉验证报告 | |

**验证结论**:ccn 填充段与环交所累计成交量差值吻合到吨级(2023 窗口差 46 吨/570 万吨,2024 窗口差 0);月度核对 13/15 精确匹配;唯一已知误差:ccn 的 2025 年 3 月表整体多计 271,950 吨(表内自洽,无法定位到天,价格不受影响);另有 29 个重叠日 ccn 与环交所不符(集中在 2025-12,ccn 漏行),合并文件一律取环交所值。

**已知缺口**:2022-01-04→2022-05-25 无公开日度源(环交所档案截断、聚合站尚未开始、Wayback/上证报接口/碳交易网/akshare 均已排除)。周度桥接可用;建议你本地 Wind/CSMAR 一键补齐该窗口日度后放入 `data/local/`(该目录已 gitignore)。

### 制度事实(顺带核实)

- **"综合价格行情"口径自 2023-08-28 启用**;此前公报 OHLC 是挂牌协议口径。回归里必须带 `price_basis` 断点。
- 环交所日交易数据查询工具(shyx.cneeex.com)需登录 token,不符合本仓库"匿名访问"规则,未使用。
- 大宗协议**不进实时行情**;本面板挂牌/大宗两腿分列并算 VWAP。

### 第一批典型事实(`output/stylized_facts.md`)

- 大宗协议占全样本总成交量 **77.3%**;对挂牌 VWAP 平均折价 **−3.77%**(中位 −1.83%,p10 −15.1%)。
- 履约聚集:2021-12 单月 = 当年成交量 75.8%;2024-12 = 40.0%;2025-12 = 20.1%。
- 价格:2021 收于 54.22 → 2024 峰值 105.65 → 2025 最低 51.24 → 2026-08 约 98。
- 零挂牌成交日 26/1140,零总成交日 13/1140。

## 进行中(后台核实,回来后落地为 CSV)

- `data/benchmarks.csv`:发电行业四类机组供电/供热基准值(2019-20→2025 各履约年,带 MEE 文件出处)——算 (e−b)·τ 净边际碳成本用。
- `data/events.csv`:政策事件精确日期表(Känzig 式冲击序列底稿)。
- 山东重点排放单位名录各年度公示页 URL(之后解析成 `data/shandong_entities.csv`)。

## 待办

1. 解析山东名录 → 面板(企业名+统一社会信用代码,逐履约年)。
2. 事件窗口 CEA 价格反应表(events.csv × cea_daily_merged.csv)。
3. 传导回归正式跑通:等你把本地山东现货面板放进 `carbon/data/local/sd_spot_prices.csv`(schema 见 `pipeline/carbon_passthrough.py` 头注;现在是 dry-run 模式)。
4. 天气面板(WEATHER_SPEC)尚未开始;NOAA S3 已确认可达(200/206)。

## 复现

```
python3 pipeline/cea_scraper.py list && python3 pipeline/cea_scraper.py fetch && python3 pipeline/cea_scraper.py parse
python3 pipeline/ccn_scraper.py list && python3 pipeline/ccn_scraper.py fetch && python3 pipeline/ccn_scraper.py parse
python3 pipeline/cea_weekly_monthly.py run
python3 pipeline/cea_merge.py
python3 pipeline/carbon_analysis.py
```
