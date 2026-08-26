# 碳市场文章:相关文献综述(Related Work)

生成日期:2026-08-26。生成方式:8 路并行文献检索(每路一个检索 agent,共 333 次搜索/抓取),再加一轮独立的完备性审查(经 Crossref API 核验新增条目的存在性)。共 161 条条目。配套的选题备忘见 `carbon/TOPICS.md`。

**使用前必读的核验说明**

- 每条文献都是检索 agent 在搜索结果或抓取页面中实际见到的,不存在凭空编造的引文;但部分字段(样本区间、页码、个别作者名)标注了 "not verified / re-check"——**引用前请自查原文**。已知错误与存疑条目的清单集中在第 7 节末尾的检索笔记里(例如:Ellerman & Montero 2007 的页码应为 47–72;Zhang-Wang-Du 2017 常被错引为 REEP,实为 EEEP)。
- 检索索引以英文为主(WebSearch 仅美区);中文文献一节靠期刊官网/机构页核验,CNKI 不可直接访问,覆盖必有遗漏(经济学(季刊)、《世界经济》两刊未找到碳市场论文,可能是真空白也可能是漏检)。
- 大陆官网(cets.org.cn、mee.gov.cn 部分 PDF、hbets.cn)从境外代理访问常 503,数据源一节的访问性描述以 2026-08 从美国网络的实测为准。

---

## 第 0 节 核心结论(先读这个)

**1. 你最关心的占坑核查:「省级现货电价 × 全国碳市场 CEA 价格」的因果研究,截至 2026-08 没有被占。**
最接近的三篇都不构成占坑:

- Wang, Feng & Zhong (2023, *Energy*):CEA 价格 vs 全国层面电价,门限回归 + 系统动力学,发现基本零传导甚至负相关。非因果设计、非小时级、非省级现货。
- Liu & Jin (2020, *Energy for Sustainable Development*):广东**试点**碳价 vs **月度长协**电价,VECM,碳价不显著。试点时代、月度频率。
- Cui, Song & Jiang (2023, *China Economic Review*):碳市场 × 省级电力市场的**事前模拟**,非真实价格的因果估计。

三篇都没用 bid-level 或小时级现货数据,都没用 TPS 调整后的边际碳成本((e_i − b)·τ,见 Goulder et al. 2022),都没利用 2021-12 之后的现货试点。Fabra–Reguant 式的山东论文仍是开放选题。

**2. 但窗口在关闭。** 查漏审查发现:Zhang Naifu, Xu & Yang (2026, *Sustainability*) 已经用山东/山西/广东现货数据发了市场效率检验(弱刊、不做碳,坑仍开);而 Zhang Naifu 与 **He Guojun–Wu Libo–Zhou Yang 的在写论文 "Carbon Market with Chinese Characteristics"**(He 的 working papers 页有列,摘要未公开)是同一批人——**掌握山东现货数据的团队已经在碳市场题目上动手了**。建议尽快邮件索要该 WP 草稿确认其内容,并加快自己的时间表。

**3. 理论上有一个现成的尖锐预测可检验。** 中国 ETS 是强度基准 + 按发电量免费分配(TPS)。理论(Fischer 2001;Holland-Hughes-Knittel 2009;Goulder-Morgenstern 2018;Goulder et al. 2022)给出:机组的边际碳成本不是 τ·e_i 而是 **τ·(e_i − b)**——比基准线脏为正、干净为负,且四条基准线(常规煤电 ≥300MW / <300MW、非常规煤电、燃气)造成符号和大小的跨机组异质。预测传导远低于西班牙(Fabra–Reguant 2014 的近完全传导)且结构可检验。这是论文的理论骨架。

**4. 文献共识给了你现成的假设。** 迄今所有对中国 ETS 的因果评估都发现:减排走**产量/行政渠道**而非价格渠道(Cao, Ho, Ma & Teng 2021 *JPubE*;Wang & Duan 2025;Qian et al. 2025;Lyu et al. 2026),原因是管制调度和管制电价阻断了碳成本传导(Teng, Jotzo & Wang 2017 明确提出:碳价起效以电力市场化为前提)。**省级现货市场正是价格渠道第一次可能出现的地方**——这句话就是你论文的动机段。美国的对应证据:Fowlie (2010, *AER*) 证明电力市场制度决定排放市场如何起效;Bushnell-Holland-Hughes-Knittel (2017) 是 TPS 在批发电力市场里的美国对照。

**5. 识别策略的现成模板。**
- 碳价外生变动:Känzig (2023, NBER 31221) 的高频政策消息冲击法可直接移植——用 MEE 政策节点(2024-02-04 条例公布、2024-05-01 生效、2024-07-02 电力配额结转限制草案、2025-03 扩容工作方案、2025-08-25 中办国办《意见》、2025-11-16 工业配额方案)构造 CEA 政策冲击序列,该序列本身即是贡献。
- 事件研究模板:Bushnell, Chong & Mansur (2013);Meng (2017, *AER*)。
- banking 规则冲击:Alberola & Chevallier (2009) 的逻辑直接适用于 2024–25 的配额结转限制。
- 小时级传导:Hintermann (2016, *JAERE*) 的按小时/负荷条件异质设计直接映射到山东小时价。

**6. 数据要点(详见第 8 节)。**
- **山东是全国碳市场第一大省**(已核实,可直接引用):首个履约周期 330 家发电重点排放单位(唯一超 300 的省)、2024 年末 268 家纳入配额管理、累计履约义务约 4.7 Gt 全国第一、前三个履约周期交易量约占全国 1/4。碳论文与现货论文天然共用一个"山东实验室"。
- CEA 日度数据公开:上海环交所每日公报,挂牌协议(OHLC)与大宗协议(量、额,VWAP 可算)分列;**大宗交易不进实时行情,只用收盘价序列会系统性失真**——自建日度面板时必须两腿合并。无官方批量下载,需爬公报或用 Wind/CSMAR。
- **企业级核定排放量不公开**(只公布名单:企业名、省份、统一社会信用代码)。拿到过的论文走的是政策研究渠道(清华/MEE 系)或税务调查、电力行业统计。这决定了哪些设计可行。

**7. 综述要正反都引。** 查漏审查特别指出:现有书目只有反强度基准的一侧(输出补贴批评),必须补上支持强度指标的理论(Newell & Pizer 2008;Fischer & Springborn 2011;Jotzo & Pezzey 2007)才立得住,尤其论文若跨越 2027 年强度转绝对总量的改革。

---
## 第 1 节 碳价 × 电力市场(与山东现货论文最近的一条线)

碳成本向批发电价的传导(Fabra–Reguant 传统)、可再生出力与边际排放、中国电改与 ETS 的互动。**本节末尾的检索笔记含关键的占坑核查结论,务必读。**

**1. Fabra, Natalia and Mar Reguant (2014), "Pass-Through of Emissions Costs in Electricity Markets"** — *American Economic Review 104(9): 2872-2899*

- 问题:How completely, and through what channels, are carbon (EU ETS) emissions costs passed through into wholesale electricity prices?
- 数据:Bid-level micro data from the Spanish day-ahead electricity market during the first years of the EU ETS (mid-2000s), combined with EUA price variation as the emissions-cost shock (exact sample window not re-verified in this sweep).
- 识别/方法:Reduced-form pass-through regressions plus a structural model of optimal multi-unit auction bidding; high-frequency auctions with inelastic demand mean markup adjustment to cost shocks is limited, which is exploited and tested.
- 发现:Emissions costs are almost fully passed through to wholesale prices (estimates near complete pass-through); firms have weak incentives to adjust markups after the cost shock, so marginal emissions costs show up essentially one-for-one in bids and prices.
- 与本项目的相关性:The canonical template for the researcher's question: it defines how to measure carbon-cost internalization in an hourly bid-based market. A Shandong version (CEA cost pass-through into day-ahead spot bids/prices) would be the direct Chinese analogue, and the paper's structural bidding framework pairs naturally with the Ito-Reguant sequential-markets setup the researcher is already using.
- 链接:https://www.aeaweb.org/articles?id=10.1257/aer.104.9.2872

**2. Sijm, Jos, Karsten Neuhoff and Yihsu Chen (2006), "CO2 cost pass-through and windfall profits in the power sector"** — *Climate Policy 6(1): 49-72*

- 问题:Do power producers pass the opportunity cost of freely allocated EU ETS allowances into electricity prices, generating windfall profits?
- 数据:German and Dutch wholesale power prices and dark/spark spreads in forward and spot markets around EU ETS launch (2005), plus dispatch-model estimates.
- 识别/方法:Empirical estimation of the relationship between EUA prices and power prices/spreads, complemented by simulation modeling; an early cointegration/spread-based approach rather than a modern causal design.
- 发现:Pass-through rates of 60-100% of CO2 costs in Germany and the Netherlands despite free allocation, implying substantial windfall profits for generators.
- 与本项目的相关性:Seminal first-generation evidence that opportunity-cost pass-through occurs even with free allowances - directly relevant to China, where CEAs are freely allocated by benchmark: the question for Shandong is whether spot-market generators bid the CEA opportunity cost at all.
- 链接:https://www.tandfonline.com/doi/abs/10.1080/14693062.2006.9685588

**3. Zachmann, Georg and Christian von Hirschhausen (2008), "First evidence of asymmetric cost pass-through of EU emissions allowances: Examining wholesale electricity prices in Germany"** — *Economics Letters 99(3): 465-469*

- 问题:Is the pass-through of EUA prices into German wholesale electricity prices asymmetric (rockets-and-feathers)?
- 数据:German wholesale power prices (EEX) and EUA prices during EU ETS Phase I (2005-2007 era).
- 识别/方法:Error-correction and autoregressive distributed lag models testing for asymmetric price transmission of EUA price increases vs decreases.
- 发现:Rising EUA prices are passed through into wholesale electricity prices more strongly than falling EUA prices - first evidence of asymmetric carbon-cost pass-through.
- 与本项目的相关性:Introduces the asymmetry margin, a cheap additional test in any Chinese pass-through study; with CEA prices exhibiting long flat spells punctuated by compliance-deadline run-ups, asymmetric transmission is a plausible feature of Shandong spot prices.
- 链接:https://ideas.repec.org/a/eee/ecolet/v99y2008i3p465-469.html

**4. Hintermann, Beat (2016), "Pass-Through of CO2 Emission Costs to Hourly Electricity Prices in Germany"** — *Journal of the Association of Environmental and Resource Economists (JAERE) 3(4): 857-891*

- 问题:What is the hour-by-hour pass-through of EU ETS emission costs to German wholesale electricity prices, and is it consistent with competitive pricing?
- 数据:Hourly German day-ahead (EPEX) spot prices matched to EUA prices and marginal-technology emission rates (early-2010s sample; exact window not re-verified in this sweep).
- 识别/方法:Hourly regressions of spot prices on marginal emission costs, allowing pass-through to vary with load and the identity of the marginal technology.
- 发现:Finds essentially full pass-through of CO2 costs to hourly prices, consistent with competitive marginal-cost pricing in the German market.
- 与本项目的相关性:The cleanest hourly reduced-form pass-through design in the EU literature; its hour-of-day/load-conditional heterogeneity approach maps directly onto Shandong's hourly day-ahead price panel, where the marginal unit (coal vs gas vs renewables at the margin) varies by hour.
- 链接:https://econpapers.repec.org/article/ucpjaerec/doi_3a10.1086_2f688486.htm

**5. Leroutier, Marion (2022), "Carbon pricing and power sector decarbonization: Evidence from the UK"** — *Journal of Environmental Economics and Management 111: 102580*

- 问题:Did the UK Carbon Price Support (a carbon tax on top of the EU ETS for power generators) reduce power-sector emissions?
- 数据:UK power-sector emissions and generation data 2013-2017, with a donor pool of other European countries.
- 识别/方法:Synthetic control method: UK power-sector emissions compared to a synthetic control built from other European power sectors.
- 发现:UK power emissions fell 20-26% per year on average 2013-2017 relative to the synthetic control, largely via coal-to-gas switching induced by the carbon price floor.
- 与本项目的相关性:The benchmark modern quasi-experimental estimate of what a binding carbon price does in a liberalized power market - the counterfactual pole against which 'ETS under China's partially regulated dispatch' results (Cao et al., Wang-Duan) are judged. Useful framing for why Shandong's spot market matters for CEA effectiveness.
- 链接:https://ideas.repec.org/a/eee/jeeman/v111y2022ics0095069621001285.html

**6. Fowlie, Meredith L. (2009), "Incomplete Environmental Regulation, Imperfect Competition, and Emissions Leakage"** — *American Economic Journal: Economic Policy 1(2): 72-112*

- 问题:How do incomplete carbon regulation and imperfect competition interact to produce emissions leakage in electricity markets?
- 数据:Calibration to the western US (California/WECC) electricity market; plant-level cost and emissions data.
- 识别/方法:Analytical Cournot oligopoly model with asymmetric regulation, numerically simulated for incomplete market-based CO2 regulation of California electricity.
- 发现:Regulation exempting out-of-state producers achieves only about one-third of the emission reductions of complete regulation at more than twice the cost per ton, because production (and emissions) shift to unregulated firms.
- 与本项目的相关性:The core framework for regulation that covers only part of a connected power system - directly analogous to China, where the national ETS covers generators but inter-provincial trade, priority dispatch, and non-spot volumes are outside market pricing; leakage across the regulated/unregulated boundary is a first-order concern for a Shandong-focused design.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pol.1.2.72

**7. Cullen, Joseph A. and Erin T. Mansur (2017), "Inferring Carbon Abatement Costs in Electricity Markets: A Revealed Preference Approach Using the Shale Revolution"** — *American Economic Journal: Economic Policy 9(3): 106-133*

- 问题:How much would a carbon price reduce US electricity-sector CO2 emissions in the short run?
- 数据:US plant/grid-level emissions and generation data (EPA CEMS) combined with large natural gas price variation from the shale revolution (roughly 2006-2012).
- 识别/方法:Revealed preference: gas-price variation shifts relative coal/gas marginal costs the same way a carbon price would, so observed fuel-switching maps out the abatement supply curve.
- 发现:A $20 ($70) per ton CO2 price would cut emissions by about 5% (10%); carbon prices are most effective when gas prices are low, i.e., abatement runs through coal-to-gas dispatch switching.
- 与本项目的相关性:Shows the abatement channel a carbon price uses in a market-dispatch system (merit-order fuel switching). In Shandong, with a coal-dominated fleet and limited gas, this channel is nearly absent - which sharpens the argument that CEA prices can matter only via the spot market's dispatch and price margins the researcher studies.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pol.20150388

**8. Borenstein, Severin, James Bushnell, Frank A. Wolak and Matthew Zaragoza-Watkins (2019), "Expecting the Unexpected: Emissions Uncertainty and Environmental Market Design"** — *American Economic Review 109(11): 3953-3977*

- 问题:Given uncertainty in business-as-usual emissions, where will an emissions cap-and-trade price settle, and what does that imply for market design?
- 数据:California cap-and-trade market: historical emissions, fuel prices, demand drivers and policy information available before market launch (pre-2013).
- 识别/方法:Ex-ante simulation of the equilibrium allowance price distribution given estimated BAU emissions uncertainty and abatement supply, compared against administrative price floors/ceilings.
- 发现:BAU emissions uncertainty is far larger than plausible price-responsive abatement, so the allowance price is very likely (~95%) to end up at an administrative floor or ceiling rather than in the interior.
- 与本项目的相关性:Explains why carbon prices in quantity markets are often policy-administered corner outcomes - highly relevant to interpreting CEA price behavior (thin trading, compliance-driven spikes, implicit policy bounds) and to modeling how much genuine marginal-cost signal a CEA price can inject into Shandong bids.
- 链接:https://www.aeaweb.org/articles?id=10.1257/aer.20161218

**9. Cullen, Joseph (2013), "Measuring the Environmental Benefits of Wind-Generated Electricity"** — *American Economic Journal: Economic Policy 5(4): 107-133*

- 问题:How much pollution (CO2, NOx, SO2) does wind generation actually offset once dispatch dynamics are accounted for?
- 数据:ERCOT (Texas) grid operations data at 15-minute frequency, April 2005 - April 2007, matched to plant emissions.
- 识别/方法:Exploits quasi-random short-run variation in wind availability to estimate which fossil units are displaced on the margin, accounting for dynamic production constraints.
- 发现:Wind mostly displaces gas-fired generation in ERCOT; only under high social-cost-of-pollution values do offset benefits exceed the cost of the subsidies supporting wind.
- 与本项目的相关性:Founding paper of the 'marginal displacement' literature: identifies emissions/dispatch effects from high-frequency renewable variation - the same variation (via forecast errors) the researcher uses as treatment. The dynamic-constraints point (ramping, commitment) is central to interpreting Shandong DA-RT spreads.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pol.5.4.107

**10. Novan, Kevin (2015), "Valuing the Wind: Renewable Energy Policies and Air Pollution Avoided"** — *American Economic Journal: Economic Policy 7(3): 291-326*

- 问题:How heterogeneous is the marginal emissions benefit of renewable electricity, and what does that imply for subsidy design?
- 数据:Hourly ERCOT wind production and EPA CEMS plant-level emissions data (late-2000s sample; exact window not re-verified in this sweep).
- 识别/方法:Uses hourly variation in wind output to estimate heterogeneous marginal emissions offsets by hour and output level; compares implied external benefits across technologies and policies.
- 发现:The marginal external benefit per MWh varies widely across hours and across renewable technologies; treating renewable output as homogeneous understates the efficiency advantage of first-best pollution pricing over output subsidies.
- 与本项目的相关性:Establishes that when and where renewable output (and its errors) land determines emissions and price consequences - the heterogeneity logic behind hour-level treatment effects in the researcher's Shandong forecast-error design.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pol.20130268

**11. Callaway, Duncan S., Meredith Fowlie and Gavin McCormick (2018), "Location, Location, Location: The Variable Value of Renewable Energy and Demand-Side Efficiency Resources"** — *Journal of the Association of Environmental and Resource Economists (JAERE) 5(1): 39-75*

- 问题:How does the value of renewable energy and energy-efficiency resources (avoided operating cost, capacity value, displaced CO2) vary across US regional power systems?
- 数据:Hourly EPA CEMS emissions and system load data across multiple US regional power markets (2010s).
- 识别/方法:Estimates regional marginal operating emissions rates and avoided costs from high-frequency variation in system load and generation, then values RE/EE profiles region by region.
- 发现:Emissions-related external benefits are one-quarter to one-half of total value per MWh and vary substantially across regions, implying economically significant regional differences in second-best subsidies.
- 与本项目的相关性:The marginal-emissions-rate toolkit for valuing renewables on coal-heavy vs gas-heavy systems; Shandong's coal-dominated margin implies large emissions consequences per MWh of forecast error, a natural welfare extension of the researcher's price-spread analysis.
- 链接:https://www.journals.uchicago.edu/doi/abs/10.1086/694179

**12. Petersen, Claire, Mar Reguant and Lola Segura (2024), "Measuring the impact of wind power and intermittency"** — *Energy Economics 129: 107200*

- 问题:What is the welfare impact of wind power on the Spanish electricity market, accounting for the costs of intermittency (deviations between scheduled and delivered wind)?
- 数据:Spanish electricity market data 2009-2018: day-ahead prices, wind output and deviations, and ancillary/balancing operating-cost data.
- 识别/方法:Empirical welfare accounting of wind's price-suppression benefits vs intermittency-driven operating costs; exploits a policy change switching wind support from output-based to capacity-based subsidies.
- 发现:Wind substantially lowers wholesale prices while intermittency imposes only modest adverse operating costs even at high wind shares; the move to capacity-based subsidies improved market operations and reduced intermittency costs.
- 与本项目的相关性:This is the 'Petersen et al.' of the strand list - the closest published cousin of the researcher's project: renewable intermittency/forecast deviations priced through sequential markets, by Reguant's team. Key benchmark for magnitudes and for framing Shandong results against a liberalized-market baseline.
- 链接:https://ideas.repec.org/a/eee/eneeco/v129y2024ics0140988323006989.html

**13. Teng, Fei, Frank Jotzo and Xin Wang (2017), "Interactions between Market Reform and a Carbon Price in China's Power Sector"** — *Economics of Energy & Environmental Policy 6(2): 39-53*

- 问题:How do electricity market reform (merit-order dispatch, cost-based pricing) and a carbon price interact in decarbonizing China's power sector?
- 数据:Simulation model of China's power sector calibrated to its regulated dispatch and pricing system (equal-shares administrative dispatch as the baseline).
- 识别/方法:Counterfactual policy simulations comparing carbon pricing with and without dispatch/pricing reform.
- 发现:A carbon price is only effective if market reform gives dispatch flexibility; without reform the carbon price needed for a given non-fossil share is roughly twice as high. Reform plus a moderate carbon price is the most effective package.
- 与本项目的相关性:The clearest statement of the 'ETS in a non-market power system' argument: carbon prices need spot-market dispatch to bite. Shandong's spot pilot is exactly the reform margin this paper says is required - it hands the researcher the motivating hypothesis for testing CEA internalization in Shandong bids/prices.
- 链接:https://researchportalplus.anu.edu.au/en/publications/interactions-between-market-reform-and-a-carbon-price-in-chinas-p/

**14. Cao, Jing, Mun S. Ho, Rong Ma and Fei Teng (2021), "When carbon emission trading meets a regulated industry: Evidence from the electricity sector of China"** — *Journal of Public Economics 200: 104470*

- 问题:Did China's regional ETS pilots reduce emissions from coal-fired power plants despite regulated electricity prices and dispatch?
- 数据:Firm/plant-level panel of Chinese coal-fired power plants in pilot vs non-pilot regions (pilot era, roughly 2009-2015-era survey data).
- 识别/方法:Difference-in-differences comparing ETS-covered power plants with plants outside the pilots.
- 发现:The pilots did not change coal efficiency (heat rate) of regulated plants; coal use fell only via reduced electricity output of covered plants - i.e., abatement operated through output reallocation, not efficiency or price channels, because electricity prices/dispatch were regulated.
- 与本项目的相关性:The flagship empirical demonstration that China's ETS cannot work through price pass-through under regulated dispatch - the null against which a Shandong spot-market pass-through finding would be a genuine contribution. Also the closest top-journal precedent for the researcher's institutional setting.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0047272721001067

**15. Goulder, Lawrence H., Xianling Long, Jieyi Lu and Richard D. Morgenstern (2022), "China's unconventional nationwide CO2 emissions trading system: Cost-effectiveness and distributional impacts"** — *Journal of Environmental Economics and Management 111: 102561*

- 问题:How does China's tradable performance standard (TPS) design for the national ETS compare to cap-and-trade in cost-effectiveness and distribution?
- 数据:Analytically and numerically solved model of China's power sector calibrated to plant benchmarks and the national ETS design (NBER WP 26537 version).
- 识别/方法:Theory plus numerical simulation: compares TPS, cap-and-trade, and carbon tax equilibria under China's rate-based allocation.
- 发现:The TPS's implicit output subsidy shuts down the output-reduction abatement channel and rewards low-intensity plants for expanding output, raising abatement costs relative to cap-and-trade; but lower output prices interact favorably with pre-existing tax distortions.
- 与本项目的相关性:Defines the exact pricing wedge relevant to Shandong: under the TPS, a generator's net marginal carbon cost is (intensity - benchmark) x CEA price, not intensity x price - the object that should (or should not) appear in spot bids. Any Shandong pass-through regression should use this TPS-adjusted carbon cost.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0095069621001133

**16. Cui, Jian, Feng Song and Zhigao Jiang (2023), "Efficiency vs. equity as China's national carbon market meets provincial electricity markets"** — *China Economic Review 78: 101915*

- 问题:How does electricity market integration (provincial vs regional markets) affect the abatement potential, cost-effectiveness, and provincial distribution of China's national carbon market?
- 数据:High-frequency (hourly-level) generation/dispatch datasets for five southern Chinese provinces in 2018.
- 识别/方法:Ex-ante simulation of coupled carbon and electricity market equilibria under provincial vs regional (integrated) electricity market designs.
- 发现:A regional integrated electricity market cuts abatement costs by about 60% relative to provincial markets for the same reduction targets, but concentrates emission reductions and coal-plant exit in particular provinces, creating an efficiency-equity trade-off.
- 与本项目的相关性:The most direct existing carbon-meets-provincial-electricity-markets analysis for China - but it is simulation, not causal estimation on realized spot prices, which is precisely the gap the researcher can fill with Shandong data. Also documents the datasets and market-coupling institutions.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S1043951X22001730

**17. Wang, Hao-ran, Tian-tian Feng and Cheng Zhong (2023), "Effectiveness of CO2 cost pass-through to electricity prices under 'electricity-carbon' market coupling in China"** — *Energy 266: 126387*

- 问题:Are CEA carbon costs from China's national ETS being passed through into Chinese electricity prices, and what design changes would improve pass-through?
- 数据:Chinese national carbon market (CEA) prices and electricity price data since the national ETS launched (2021 onward), plus calibrated market-coupling parameters.
- 识别/方法:Threshold regression of electricity prices on carbon prices plus a system-dynamics simulation of the coupled 'electricity-carbon' markets; not a quasi-experimental design.
- 发现:Finds essentially no positive pass-through - the carbon price has a significant negative association with electricity prices since the national ETS began, indicating the two markets are barely linked; allowance auctioning and electricity price-formation reform would improve carbon-cost reflection.
- 与本项目的相关性:This is the closest existing paper to 'CEA prices vs Chinese electricity prices' - and it is a field-journal time-series/simulation exercise, not a causal bid-level study on provincial spot prices. It confirms the gap is open while giving the researcher a prior (near-zero pass-through pre-spot-market) to beat or overturn with Shandong hourly data.
- 链接:https://ideas.repec.org/a/eee/energy/v266y2023ics036054422203273x.html

**18. Wang, Baixue and Maosheng Duan (2025), "Have China's emissions trading systems reduced carbon emissions? Firm-level evidence from the power sector"** — *Applied Energy 378 (Part B)*

- 问题:Have China's regional ETSs causally reduced power-sector carbon emissions and intensity, and through what channels?
- 数据:Verified firm-level carbon emissions data and annually updated regulatory (covered-entity) lists for China's power sector across regional ETS jurisdictions.
- 识别/方法:Difference-in-differences with event-study designs across regional ETSs, exploiting staggered coverage of firms.
- 发现:ETSs lowered emissions mainly by curtailing generation rather than improving efficiency; larger allowance shortages and higher carbon prices did reduce intensity; outdated coal capacity retired faster; no evidence of leakage to neighboring provinces or within ownership networks.
- 与本项目的相关性:The most recent firm-level causal evaluation of Chinese carbon markets in power, updating Cao et al. (2021) and again finding quantity (output) rather than price channels - reinforcing that the missing piece is exactly price-side evidence from spot markets like Shandong's. Its verified-emissions dataset and covered-entity lists are potentially reusable.
- 链接:https://ideas.repec.org/a/eee/appene/v378y2025ipbs0306261924021858.html

**19. Liu, Y., Zhigao Jiang and Bowei Guo (2022; WP 2021), "Assessing China's provincial electricity spot market pilot operations: Lessons from Guangdong province"** — *Energy Policy (2022); Cambridge Working Papers in Economics 2165 (2021)*

- 问题:Is China's first provincial electricity spot market (Guangdong pilot) functioning well - price formation, regulatory distortions, and market power?
- 数据:Actual market data from Guangdong's spot market pilot operations (day-ahead prices, demand, bids; trial-operation period around 2019-2020).
- 识别/方法:Econometric estimation of the price-demand (supply curve) relationship, quantification of the regulatory price floor's transfers, and tests for local market power.
- 发现:The supply curve is convex; the spot price floor transferred about 1.3% of day-ahead market value from consumers to producers; localized market power exists in eastern Guangdong reflecting transmission inadequacy. No carbon/ETS analysis.
- 与本项目的相关性:The template empirical paper on a Chinese provincial spot pilot - and notably it does NOT touch carbon, confirming no one has yet joined provincial spot-market microdata to CEA prices. Its institutional detail (price floors/caps, trial-run windows) applies with variation to Shandong and matters for interpreting DA-RT spreads.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0301421522001422

**20. Xiang, Chenxi, Xinye Zheng, Feng Song, Jiang Lin and Zhigao Jiang (2023), "Assessing the roles of efficient market versus regulatory capture in China's power market reform"** — *Nature Energy 8(7): 747-757*

- 问题:Did China's post-2015 shift toward market-based economic dispatch improve efficiency, and to what extent is the gain limited by regulatory capture in provincial markets?
- 数据:Plant/provincial-level generation and dispatch data spanning China's 2015 power sector reform (provinces adopting market-based dispatch at different times).
- 识别/方法:Exploits staggered provincial adoption of market-based dispatch to identify efficiency changes, then decomposes market-driven vs politically driven allocation.
- 发现:The dispatch transition improves overall efficiency, but regulatory capture in provincial markets (favoring incumbent/connected generators) prevents realization of the full potential gains.
- 与本项目的相关性:High-profile evidence that Chinese provincial markets are partially captured - a first-order concern when interpreting Shandong spot prices as competitive marginal-cost signals, and hence when reading any estimated carbon pass-through (capture could mute or distort it).
- 链接:https://www.nature.com/articles/s41560-023-01278-9

**21. Liu, Xianbing and Zhen Jin (2020), "An analysis of the interactions between electricity, fossil fuel and carbon market prices in Guangdong, China"** — *Energy for Sustainable Development 55: 82-94*

- 问题:How do Guangdong pilot carbon prices, fossil fuel prices, and electricity market prices interact?
- 数据:Guangdong pilot-era time series: pilot carbon allowance prices, coal/diesel/LNG prices, and monthly forward electricity market prices (pre-national-ETS, pre-spot-market).
- 识别/方法:Cointegration and short-run dynamics (VECM-style) analysis among the price series; associational, not causal.
- 发现:Long-run cointegration exists between carbon prices and fuel prices, but carbon price changes are not a significant driver of Guangdong monthly forward electricity prices - i.e., no detectable carbon-to-electricity price transmission in the pilot era.
- 与本项目的相关性:The only located paper that directly regresses Chinese provincial electricity prices on carbon prices - but it uses pilot-era monthly forward prices, not national CEA prices or hourly spot prices. Confirms the specific CEA-to-provincial-spot-price question is untaken and gives a pilot-era null baseline.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0973082619310166

### 本节检索笔记(agent 原始记录,含未列入正文的文献与核验警告)

> GAP CHECK (the key deliverable): No paper was found that causally links Chinese provincial SPOT electricity prices (Shandong, Guangdong, or Shanxi day-ahead/real-time prices) to national CEA carbon prices. The closest existing work is (a) Wang, Feng & Zhong (Energy 2023) - threshold regression + system dynamics on aggregate prices, finding essentially zero/negative pass-through since the national ETS launch; (b) Liu & Jin (EfSD 2020) - Guangdong PILOT carbon prices vs monthly FORWARD electricity prices, carbon insignificant; (c) Cui, Song & Jiang (China Econ Review 2023) - ex-ante simulation of carbon-electricity market coupling, not realized prices. All are field-journal/simulation work, none uses bid-level or hourly spot data, none uses the TPS-adjusted marginal carbon cost (intensity minus benchmark, per Goulder et al. 2022), and none exploits the Dec 2021+ spot pilots. The Fabra-Reguant-style CEA pass-through paper on Shandong (or Guangdong/Shanxi) spot data appears NOT taken as of Aug 2026. Caveat: US-only search index and 403-blocked ScienceDirect abstracts mean a very recent Chinese-language or 2026 working paper could have been missed; a check of CNKI/Chinese journals and the AERE/IAEE 2025-26 conference programs is advised before claiming the gap in print.
> 
> ADDITIONAL VERIFIED PAPERS THAT DIDN'T MAKE THE 20: (1) Abrell, Kosch & Rausch (2022), "How effective is carbon pricing? - A machine learning approach to policy evaluation," JEEM 112 - ML counterfactual for the UK Carbon Price Support; 6.2% emissions cut in 2013-16 at ~EUR 18/t, effect depends on relative fuel prices (https://ideas.repec.org/a/eee/jeeman/v112y2022ics0095069621001339.html); complements Leroutier. (2) Goulder, Long, Qu & Zhang, "China's Nationwide CO2 Emissions Trading System: A General Equilibrium Assessment," NBER WP 31809 (2023) - multi-sector GE model with SOEs and electricity price regulation; benefits exceed costs ~5x; single-benchmark design would cut costs 34% (https://www.nber.org/papers/w31809). (3) Brown & Reguant (2026), "The Price Impacts of Renewable Power: A Tale of Two Sources," U. Alberta WP 2026-04 - Spain; wind/solar cut wholesale prices but raise ancillary-service costs; methodologically adjacent to the researcher's project (https://mreguant.github.io/papers/wp2026-04.pdf). (4) An iScience (2026) study using 1,957 Chinese thermal units 2018-2024: allowance-deficit units cut CO2 intensity 0.8% and emissions 3.5%, concentrated in small coal units - frontier CN-ETS evidence but author list not verified in this sweep (https://www.sciencedirect.com/science/article/pii/S2589004226007996). (5) Ito & Reguant (2016 AER) is the method anchor and deliberately excluded as known to the researcher.
> 
> DEBATES IN THE STRAND: (i) In liberalized markets (Spain, Germany, UK) carbon-cost pass-through is near-complete and carbon prices bite via merit-order fuel switching; (ii) in China, theory (Goulder et al. TPS implicit output subsidy; Teng-Jotzo-Wang regulated dispatch) and firm-level empirics (Cao et al. 2021 JPubE; Wang-Duan 2025) agree the ETS so far works through administrative/output channels, NOT prices - so the province-level spot pilots (Shandong among the first four to formal operation) are exactly where price-channel effectiveness would first appear; (iii) whether observed Chinese spot prices are competitive enough to reveal costs at all is contested (Xiang et al. Nature Energy 2023 on regulatory capture; Liu-Jiang-Guo on price floors and local market power) - any pass-through estimate needs to confront caps/floors and captured dispatch.
> 
> DATASETS DISCOVERED: verified firm-level CN emissions + MEE covered-entity lists (Wang-Duan); hourly dispatch data for five southern provinces (Cui-Song-Jiang); Guangdong spot pilot market data (Liu-Jiang-Guo); CEA price series from Shanghai Environment & Energy Exchange (used in the VECM literature); EPA CEMS and Spanish OMIE data underpin the US/EU benchmarks. TPS benchmark values by fuel/technology (four benchmarks, per Goulder et al./NBER 31809) are needed to construct the correct net marginal carbon cost for a Shandong pass-through regression.
> 
> METADATA CAVEATS: sample periods flagged as approximate for Fabra-Reguant, Hintermann, Novan, Callaway et al. (abstract pages verified, exact windows not re-checked); Cui-Song-Jiang author names verified via secondary (Jilin University) page; Liu-Jiang-Guo first author's full first name not confirmed (WP lists "Liu, Y."); Energy Policy volume/article numbers for that paper not confirmed. Everything else (authors, titles, venues, years, findings) was confirmed against journal/AEA/RePEc/NBER pages during this sweep.

## 第 2 节 中国碳市场实证评估与 TPS 设计理论

试点与全国碳市场的因果评估,以及 Goulder–Morgenstern 一系对强度基准(可交易绩效标准 TPS)设计的理论与模拟分析。

**1. Jingbo Cui, Chunhua Wang, Junjie Zhang, and Yang Zheng (2021), "The effectiveness of China's regional carbon market pilots in reducing firm emissions"** — *PNAS (Proceedings of the National Academy of Sciences)*

- 问题:Did China's regional ETS pilots causally reduce CO2 emissions of regulated firms despite low prices and thin trading?
- 数据:Firm-level tax-record/tax-survey panel covering regulated and unregulated firms across the seven original pilot jurisdictions and non-pilot regions, roughly 2009-2015 (pre/post pilot launch in 2013).
- 识别/方法:Difference-in-differences (including PSM-DiD and continuous-treatment DiD exploiting pilot price/liquidity variation) comparing regulated firms to comparable unregulated firms before/after ETS launch.
- 发现:Pilot ETSs significantly reduced firm CO2 emissions and emission intensity even at low carbon prices; channels are energy-efficiency improvement and green innovation rather than output cuts alone.
- 与本项目的相关性:The benchmark causal evaluation of China's carbon pilots — the paper any new China-ETS empirical paper must cite and position against; its firm-level DiD template and its finding that effects operate despite weak prices frame what a Shandong power-sector study of the national ETS should test.
- 链接:https://www.pnas.org/doi/10.1073/pnas.2109912118

**2. Jingbo Cui, Junjie Zhang, and Yang Zheng (2018), "Carbon Pricing Induces Innovation: Evidence from China's Regional Carbon Market Pilots"** — *AEA Papers and Proceedings 108: 453-57*

- 问题:Did the regional ETS pilots induce low-carbon innovation among publicly listed firms?
- 数据:Patent applications of publicly listed Chinese firms, 2003-2015, matched to pilot/non-pilot status and pilot activity measures (carbon price, allowance turnover).
- 识别/方法:Triple-difference (DDD): pilot vs non-pilot regions, covered vs uncovered firms, before vs after; intensity margin using pilot price and trading activity.
- 发现:ETS pilots increased low-carbon patenting; more active pilots (higher price, higher allowance turnover) induced more low-carbon innovation.
- 与本项目的相关性:Early top-outlet evidence on the dynamic/innovation margin of Chinese carbon pricing; useful comparison point when arguing about whether market signals (prices) vs administrative pressure drive firm responses in Chinese environmental markets.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pandp.20181027

**3. Junming Zhu, Yichun Fan, Xinghua Deng, and Lan Xue (2019), "Low-carbon innovation induced by emissions trading in China"** — *Nature Communications*

- 问题:Did China's pilot ETSs increase low-carbon innovation by participating firms, and through which design features?
- 数据:Patent data for firms covered by the pilot ETSs vs matched uncovered firms, spanning pre/post pilot launch (2013-) periods.
- 识别/方法:Matched difference-in-differences on covered vs uncovered firms, decomposing effects by allowance-allocation rule, permit price, auctioning, and firm characteristics.
- 发现:Pilot ETSs raised covered firms' low-carbon innovation by 5-10% without crowding out other innovation; the effect is driven by mass-based allowance allocation rather than permit price or auction design.
- 与本项目的相关性:High-profile evidence that allocation design (mass- vs intensity/rate-based) — not the carbon price — drives firm responses in China; directly relevant to interpreting incentives under the national ETS's benchmark (rate-based) allocation that covers Shandong's coal fleet.
- 链接:https://www.nature.com/articles/s41467-019-12213-6

**4. Da Zhang, Qin Zhang, Shaozhou Qi, Jinpeng Huang, Valerie J. Karplus, and Xiliang Zhang (2019), "Integrity of firms' emissions reporting in China's early carbon markets"** — *Nature Climate Change 9: 164-169*

- 问题:How accurate is firms' self-reported CO2 emissions data in China's pilot carbon markets, and does third-party verification discipline reporting?
- 数据:Matched firm-level self-reported vs third-party-verified emissions from the Beijing (2012-2015) and Hubei (2014-2015) pilot ETSs.
- 识别/方法:Descriptive/econometric comparison of reported vs verified emissions over time, relating discrepancies to firm reporting capacity; not a causal-design paper.
- 发现:Average reporting discrepancies fell (Beijing: 17% in 2012 to 4% in 2014-15; Hubei: 6% to 5%); no evidence of deliberate misreporting; improved firm reporting capacity is associated with smaller discrepancies.
- 与本项目的相关性:The MRV-integrity foundation for any empirical work using Chinese compliance emissions data — important caveat/justification when a paper relies on verified emissions or compliance data from the national ETS; also part of the Karplus/Zhang(s) author cluster the assignment flags.
- 链接:https://www.nature.com/articles/s41558-018-0394-4

**5. Jing Cao, Mun S. Ho, Rong Ma, and Fei Teng (2021), "When carbon emission trading meets a regulated industry: Evidence from the electricity sector of China"** — *Journal of Public Economics 200: 104470*

- 问题:How does an ETS work when imposed on an industry (electricity) whose output prices and dispatch are regulated?
- 数据:Plant/firm-level panel of coal-fired power plants in pilot vs non-pilot provinces around the 2013 pilot launches (retrospective firm-level power-sector data).
- 识别/方法:Difference-in-differences comparing coal power plants covered by pilot ETSs to uncovered plants, decomposing coal-use reductions into efficiency (coal per kWh) vs output channels.
- 发现:Pilot ETSs did not improve coal efficiency of regulated plants; coal use fell only via reduced electricity output, and that contraction appears driven by government decisions rather than price-based optimization, since permit costs are small relative to controlled electricity prices and the output cuts caused financial losses.
- 与本项目的相关性:Arguably the single most load-bearing paper for this researcher: it shows carbon pricing fails to transmit through China's regulated electricity prices — precisely the friction that Shandong's spot-market reform (his Ito-Reguant setting) relaxes. Sets up the hypothesis that ETS incentives only bite where marginal-cost dispatch and price pass-through exist.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0047272721001067

**6. Haoqi Qian, Yanran Gong, Shouyang Wang, and Libo Wu (2025), "Structural Substitution Rather Than Efficiency Improvement in Thermal Power Sector Achieved by China's Pilot Carbon Markets"** — *The Energy Journal*

- 问题:Through what margin (efficiency vs output reallocation) did the pilot carbon markets reduce coal use in the thermal power sector?
- 数据:Nationwide unit-level dataset of 1,000+ coal-fired power units covering pilot and non-pilot regions (pre/post pilot launch).
- 识别/方法:Quasi-experimental unit-level analysis (DiD-style) of pilot ETS exposure, separating within-unit efficiency changes from between-unit output substitution.
- 发现:Pilot ETSs cut coal consumption through electricity production shrinkage and output substitution toward high-capacity units; unit energy efficiency barely improved short-run and worsened longer-run; stringent benchmarks plus China's administrative dispatch system amplify the structural-substitution margin.
- 与本项目的相关性:Shows the administrative dispatch system mediates how carbon regulation reallocates generation across units — the same dispatch institutions Shandong's spot market replaces; provides the unit-level power-sector empirical design closest to what a Shandong ETS-electricity paper would use.
- 链接:https://doi.org/10.1177/01956574251315386

**7. Baixue Wang and Maosheng Duan (2025), "Have China's emissions trading systems reduced carbon emissions? Firm-level evidence from the power sector"** — *Applied Energy 378(PB)*

- 问题:Did China's regional ETSs reduce power-sector carbon emissions, via which channels, and was there leakage?
- 数据:Verified firm-level emissions/generation data for power firms in pilot vs non-pilot provinces.
- 识别/方法:Firm-level quasi-experimental comparison (DiD) of covered vs uncovered power firms; heterogeneity by allowance shortage, carbon price, market size/liquidity; leakage tests across neighboring provinces and ownership networks.
- 发现:Pilot ETSs significantly reduced emissions primarily via reduced generation with little intensity improvement; allowance shortage and higher prices do improve intensity; no evidence of leakage to neighboring provinces or within ownership networks; systems pressure technologically inferior firms most.
- 与本项目的相关性:Recent power-sector-specific confirmation of the output-margin result (echoing Cao et al. 2021), with leakage tests relevant to interprovincial electricity trade — a live issue for Shandong, a large power importer.
- 链接:https://ideas.repec.org/a/eee/appene/v378y2025ipbs0306261924021858.html

**8. Lawrence H. Goulder and Richard D. Morgenstern (2018), "China's Rate-Based Approach to Reducing CO2 Emissions: Attractions, Limitations, and Alternatives"** — *AEA Papers and Proceedings 108: 458-62*

- 问题:What are the efficiency properties of China's rate-based (TPS) ETS design relative to a mass-based cap?
- 数据:Analytical; illustrative calculations for China's power-sector ETS design (no microdata).
- 识别/方法:Theory: shows the rate-based structure drives a wedge between firms' perceived marginal abatement cost and society's marginal abatement cost (an implicit output subsidy).
- 发现:Rate-based trading is not cost-effective because the output subsidy suppresses the output-reduction abatement channel; converting to a mass-based system would eliminate the wedge and yield significant cost-effectiveness and efficiency gains.
- 与本项目的相关性:The canonical short statement of the Goulder-Morgenstern critique of China's TPS; the theoretical anchor for any discussion of how the national ETS distorts electricity output decisions — including bids into day-ahead/real-time markets like Shandong's.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pandp.20181028

**9. Lawrence H. Goulder, Xianling Long, Jieyi Lu, and Richard D. Morgenstern (2022), "China's unconventional nationwide CO2 emissions trading system: Cost-effectiveness and distributional impacts"** — *Journal of Environmental Economics and Management 111: 102561 (earlier NBER WP 26537, "...The Wide-Ranging Impacts of an Implicit Output Subsidy")*

- 问题:How cost-effective is China's power-sector TPS relative to cap-and-trade (and carbon tax), and what are its distributional impacts?
- 数据:Calibrated multi-period numerical model of China's power sector (generator types, benchmarks) — simulation, not econometric microdata.
- 识别/方法:Structural/simulation comparison of TPS vs C&T vs tax achieving equal emissions reductions; decomposes the implicit output subsidy and multi-benchmark distortions.
- 发现:The TPS implicitly subsidizes electricity output, shutting down the output-reduction channel, so economic costs exceed mass-based C&T for the same abatement; multiple technology-specific benchmarks add a further inefficiency; distributional impacts across generator types differ sharply from C&T.
- 与本项目的相关性:The core quantitative Goulder-Morgenstern TPS paper. Its mechanism — benchmark allocation acting as an output subsidy to generators — directly shifts marginal incentives of Shandong coal units bidding into the spot market, and should inform how the researcher models supply behavior under the national ETS.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0095069621001133

**10. Lawrence H. Goulder, Xianling Long, Chenfei Qu, and Da Zhang (2023, rev. 2025), "China's Nationwide CO2 Emissions Trading System: A General Equilibrium Assessment"** — *NBER Working Paper 31809; listed as forthcoming, American Economic Journal: Economic Policy (per Goulder's Sept 2025 CV)*

- 问题:What are the economy-wide welfare, cost, and distributional effects of China's national TPS, accounting for SOEs, fiscal interactions, and regulated electricity markets?
- 数据:Multi-sector, multi-period CGE model calibrated to China's economy, including state-owned enterprises and electricity price regulation; policy scenarios through ~2035.
- 识别/方法:Structural general-equilibrium simulation comparing current TPS design against single-benchmark, auctioning, and C&T alternatives.
- 发现:Climate benefits alone exceed policy costs ~5-fold (more with air-quality co-benefits); moving from four power-sector benchmarks to one cuts costs ~34% but widens regional income disparities; auctioning allowances would lower economy-wide costs by 30%+; fiscal interactions materially affect TPS-vs-C&T comparisons.
- 与本项目的相关性:State-of-the-art structural evaluation of the national ETS with explicit electricity-market regulation — the natural GE complement to a reduced-form/structural Shandong spot-market study, and the source of policy counterfactuals (benchmark consolidation, auctioning) a new paper can speak to.
- 链接:https://www.nber.org/papers/w31809

**11. Carolyn Fischer, Chenfei Qu, and Lawrence H. Goulder (2024), "Rate-Based Emissions Trading with Overlapping Policies: Insights from Theory and an Application to China"** — *NBER Working Paper 33197*

- 问题:How do overlapping policies (RPS, indirect-emissions accounting, etc.) interact with rate-based ETSs like China's TPS versus cap-and-trade?
- 数据:Analytical model plus computational model calibrated to China's economy (national ETS design scenarios to 2035).
- 识别/方法:Theory + calibrated simulation of a range of ETS designs (several TPS variants) crossed with overlapping policies.
- 发现:Overlapping policies that undermine cost-effectiveness under cap-and-trade can enhance it under a TPS: adding renewable portfolio standards and accounting for indirect electricity emissions under China's current design could cut the cost of hitting the national target by 20-30% through 2035.
- 与本项目的相关性:The 2024 frontier of the TPS theory line (CAERE best-paper award); crucial for a paper studying Shandong, where renewable support policies, provincial RPS, and the national TPS all overlap with the new spot market — it flips the usual policy-overlap intuition for rate-based systems.
- 链接:https://www.nber.org/papers/w33197

**12. Carolyn Fischer (2001), "Rebating Environmental Policy Revenues: Output-Based Allocations and Tradable Performance Standards"** — *RFF Discussion Paper 01-22*

- 问题:What are the incentive and welfare properties of policies that rebate emissions-policy revenues in proportion to output (including tradable performance standards)?
- 数据:Theory (analytical model); no data.
- 识别/方法:Analytical: shows TPS, emissions tax with market-share rebates, and permits with output-based allocation are all equivalent to an emissions tax combined with an output subsidy.
- 发现:Output-based rebating tilts abatement toward emissions-rate reductions and away from output contraction, raising marginal control costs and depressing output prices relative to the social optimum.
- 与本项目的相关性:The seminal theoretical statement of the 'implicit output subsidy' at the heart of China's TPS design; the primitive result underlying the entire Goulder-Morgenstern China line and any model of how benchmark allocation distorts generators' supply offers.
- 链接:https://media.rff.org/documents/RFF-DP-01-22.pdf

**13. Stephen P. Holland, Jonathan E. Hughes, and Christopher R. Knittel (2009), "Greenhouse Gas Reductions under Low Carbon Fuel Standards?"** — *American Economic Journal: Economic Policy 1(1): 106-46*

- 问题:Can intensity (rate-based) standards like an LCFS reduce emissions efficiently — or at all?
- 数据:Analytical model plus numerical simulation calibrated to US fuel markets (illustrative parameters).
- 识别/方法:Theory + simulation: an intensity standard taxes emissions above the ratio benchmark and subsidizes 'clean' output below it.
- 发现:An LCFS can perversely increase net emissions (it subsidizes low-carbon fuel production), can never be fully efficient, and has very high average abatement costs ($307-$2,272/tCO2 in their range) relative to cost-effective policies; the best LCFS may be nonbinding.
- 与本项目的相关性:The classic rate-based-regulation impossibility/efficiency result routinely cited to motivate why China's intensity-based ETS may deliver perverse output incentives; the standard theoretical citation alongside Fischer (2001) and Goulder-Morgenstern for the TPS-vs-cap comparison.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pol.1.1.106

**14. William A. Pizer and Xiliang Zhang (2018), "China's New National Carbon Market"** — *AEA Papers and Proceedings 108: 463-67*

- 问题:What is the design of China's announced national ETS, how does it differ from US/EU cap-and-trade, and what are the economic implications?
- 数据:Policy design analysis of the December 2017 national ETS announcement and pilot experience; no microdata.
- 识别/方法:Descriptive/analytical policy economics.
- 发现:The national ETS (initially power-sector, output-based/rate-based allocation) will more than double the volume of world CO2 emissions covered by pricing; its design inherits pilot features and diverges from Western cap-and-trade, with implications for efficiency and possible future modifications (e.g., moving toward mass-based caps, auctioning).
- 与本项目的相关性:The standard AEA-outlet introduction to the national ETS's institutional design; efficient citation for describing the policy environment a Shandong-focused empirical paper operates in.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pandp.20181029

**15. Da Zhang, Valerie J. Karplus, Cyril Cassisa, and Xiliang Zhang (2014), "Emissions trading in China: Progress and prospects"** — *Energy Policy 75: 9-16*

- 问题:What is the status, design, and challenge set of China's seven regional ETS pilots, and what do they imply for a national system?
- 数据:Institutional/policy data on the seven pilots (coverage, allocation, MRV, compliance rules) as of 2014.
- 识别/方法:Descriptive institutional analysis (no causal design).
- 发现:Documents pilot heterogeneity in coverage, allocation and enforcement; identifies MRV capacity, legal foundations, and interaction with energy-price regulation as the binding constraints for scaling to a national ETS.
- 与本项目的相关性:The standard early reference for pilot institutional detail (needed to define treatment in any pilot-evaluation design) and for the pilots-to-national-ETS narrative arc; part of the Karplus/Da Zhang/Xiliang Zhang cluster named in the assignment.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0301421514000275

**16. Valerie J. Karplus and Xiliang Zhang (2017), "Incentivizing firm compliance with China's national emissions trading system"** — *Economics of Energy & Environmental Policy 6(2) (special issue on China's national ETS co-edited by Goulder, Morgenstern, Karplus, von Hirschhausen)*

- 问题:What institutional factors limit firm compliance with environmental policy in China, and what would strengthen compliance under the national ETS?
- 数据:Case evidence from the Beijing pilot ETS (2013-2015 compliance records) and China's broader environmental-enforcement experience.
- 识别/方法:Institutional analysis with descriptive compliance evidence (not a causal design).
- 发现:Compliance requires a strong legal foundation, unified measurement and verification requirements, and credible signals of sustained government commitment; Beijing's escalating enforcement produced near-universal compliance, suggesting institutions rather than price levels drive early compliance.
- 与本项目的相关性:The reference point for the 'national ETS compliance behavior' sub-topic the assignment names; official MEE reports now show 99.6-99.9% surrender rates, consistent with its institutions-first account — relevant background for interpreting quasi-compliance-driven trading patterns (e.g., deadline-clustered volumes) in the national market.
- 链接:https://dspace.mit.edu/handle/1721.1/128458

**17. Fei Teng, Frank Jotzo, and Xin Wang (2017), "Interactions between market reform and a carbon price in China's power sector"** — *Economics of Energy & Environmental Policy 6(2): 39-54*

- 问题:How does China's regulated dispatch and pricing system condition the effectiveness of carbon pricing in the power sector, and how does power-market reform change this?
- 数据:Policy/model-based analysis of China's dispatch and pricing institutions circa the 13th Five-Year Plan power reforms; no firm microdata.
- 识别/方法:Analytical/simulation assessment of carbon-price pass-through and dispatch reordering under regulated vs liberalized market rules.
- 发现:Under administrative dispatch and regulated tariffs, a carbon price cannot reorder the merit curve or pass through to consumers, so ETS abatement channels are throttled; electricity market reform (economic dispatch, spot pricing) is a precondition for the ETS to deliver low-cost abatement.
- 与本项目的相关性:The explicit theoretical bridge between the two literatures the researcher straddles: it predicts that provinces adopting spot markets (Shandong, Guangdong, Shanxi) are exactly where national ETS incentives should start binding — a testable hypothesis his Shandong data can address.
- 链接:https://researchportalplus.anu.edu.au/en/publications/interactions-between-market-reform-and-a-carbon-price-in-chinas-p/

**18. Ziyu Qin, Jianhui Ruan, Hui Yu, Jieyi Li, Chen Lyu, Bofeng Cai, Shouyang Wang, and Ling Tang (2025), "The effectiveness of China's national emissions trading scheme in mitigating firm emissions"** — *Energy Economics 150*

- 问题:Has the national ETS (post-2021) reduced power-sector carbon intensity, and how does its effect compare with the regional pilots?
- 数据:Unit-level monitoring data from China's power sector spanning national-ETS and pilot coverage (period includes the national ETS's first compliance cycles).
- 识别/方法:Quasi-experimental panel comparison of units covered by national vs pilot ETSs vs uncovered units, with mediation/moderation analysis of mechanisms.
- 发现:Both national and pilot ETSs significantly reduce carbon intensity, but pilots' effects are stronger; fuel-quality improvement (lower carbon content of coal) is a key mechanism; regional growth and industrial concentration offset effectiveness; effects are larger for smaller, older units.
- 与本项目的相关性:One of the first peer-reviewed econ-journal evaluations of the national ETS itself (not just pilots), with unit-level power data over the same 2021+ window as the researcher's Shandong sample — a direct empirical benchmark for national-ETS treatment effects on coal units.
- 链接:https://ideas.repec.org/a/eee/eneeco/v150y2025ics0140988325006565.html

**19. Xiangzhen Li, Jingzhe Liu, Hao Wang, and Lihong Zhang (2025), "The Real Effects of China's Carbon Dioxide Emissions Trading Program" (working paper, Tsinghua SEM; presented AEA/AFA 2025)** — *Working paper (AEA 2025 program; AFA submission)*

- 问题:How did compliance with China's intensity-based national ETS affect firms' real decisions — investment, employment, productivity, and wages?
- 数据:Panel of Chinese compliance firms vs non-compliance firms around the national ETS's two-stage intensity-based quota allocation (listed-firm financials; exact sample period per paper draft of July 2025).
- 识别/方法:Quasi-experimental comparison of compliance vs non-compliance firms under the national ETS's intensity-based allocation, with heterogeneity by state ownership and regional market liberalization.
- 发现:Compliance firms increased (green) investment and production workforce; SOEs and firms in less-liberalized regions hired but did not invest, non-SOEs and firms in liberalized regions invested but did not hire; productivity was maintained while ordinary workers' real wages fell, especially in SOEs.
- 与本项目的相关性:Recent frontier evidence that responses to the national TPS are mediated by state ownership and regional market liberalization — the same institutional heterogeneity that determines which generators respond to Shandong's spot prices; useful for the political-economy/SOE margin of a carbon-electricity paper.
- 链接:https://www.aeaweb.org/conference/2025/program/paper/sNEDG94b

**20. Guojun He, Libo Wu, Naifu Zhang, and Yang Zhou (circa 2024-2025), "Carbon Market with Chinese Characteristics" (working paper; year and details unverified beyond author's site listing)** — *Working paper (listed on Guojun He's working-papers page)*

- 问题:How does China's carbon market function given its distinctive (administratively embedded, intensity-based) design — per the title/listing; full abstract not verified.
- 数据:Not verified — the paper is listed by title and coauthors on Guojun He's working-papers page; no public abstract located in this sweep.
- 识别/方法:Not verified; He's related work is applied micro/causal inference on Chinese environmental regulation, and coauthor Libo Wu overlaps with the unit-level power-sector ETS evaluations (e.g., Qian et al. 2025).
- 发现:Not verified. Included because the assignment flags Guojun He, and this is his directly on-topic project; details should be pulled from the draft before citing substantively.
- 与本项目的相关性:Likely to become a prominent economics treatment of the national ETS by a named author in this strand; worth tracking/emailing for the draft. The Wu coauthorship suggests unit-level power data, adjacent to the researcher's Shandong setting.
- 链接:https://www.guojunhe.com/working-papers.html

### 本节检索笔记(agent 原始记录,含未列入正文的文献与核验警告)

> Coverage and verification caveats: (1) All citations above were seen directly in search results or on fetched pages; the two weakest-verified entries are flagged in-line: He-Wu-Zhang-Zhou (title/coauthors verified from guojunhe.com only; no abstract found) and Li-Liu-Wang-Zhang (title page and abstract extracted from the AEA 2025 conference PDF; it is a WP, not a Journal of Finance publication despite appearing on the AFA paper-management site). Goulder-Long-Qu-Zhang's AEJ:Policy forthcoming status comes from Goulder's Sept 2025 CV (PDF text extracted). (2) Additional papers seen but left off the main list: Yan, Ruan, Qin, Lyu, Qian, Jia, Zhang, Cai, S. Wang, J. Wang, Tang (2025), 'Unit-level monitoring data reveal the effectiveness of China's national emissions trading scheme,' Cell Reports Sustainability — same team as the Qin et al. Energy Economics paper; an iScience (2026) paper 'Dual CO2 mitigations with diminishing margins: Evidence from China's intensity-based national ETS' appears to be the source of the balanced-panel-of-1,957-thermal-power-units (2018-2024) design finding that allowance-deficit units cut intensity 0.8% and emissions 3.5% (authors not verified; page 403'd); Goulder, Morgenstern, Munnings & Schreifels (2017) 'China's National CO2 Emissions Trading System: An Introduction,' EEEP — the Nov 2017 EEEP special issue (co-edited Goulder/Morgenstern/Karplus/von Hirschhausen) is the institutional foundation of the whole Goulder-Morgenstern line; Goulder & Long (2023) China Economic Journal review of global ETSs; Karplus (2021) Harvard HEEP overview of the national ETS; Yang, Jahanger, Hu & Awan (2024) Energy Economics on firm-level SO2 abatement and employment (double-dividend claim); Wang & Duan-adjacent ES&T (2024) 'Carbon Abatement and Leakage in China's Regional Carbon Emission Trading.' (3) Shanjun Li: despite the assignment naming him, no China-carbon-market paper by him surfaced in multiple searches; his China work found here is pollution-information/electricity (e.g., 'From Fog to Smog,' AER 2024) — treat his inclusion in this strand as unconfirmed. (4) Key debates in the strand that a synthesis should organize around: (a) the abatement-margin debate — pilots reduced emissions mainly via output contraction/structural substitution, possibly administratively driven (Cao et al. JPubE 2021; Qian et al. EJ 2025; Wang & Duan 2025) vs efficiency/innovation channels (Cui et al. PNAS 2021; Zhu et al. 2019); (b) the TPS welfare debate — implicit output subsidy makes rate-based trading costlier than cap-and-trade (Fischer 2001; HHK 2009; Goulder-Morgenstern 2018; Goulder et al. JEEM 2022), but Fischer-Qu-Goulder (NBER 33197) show overlapping policies (RPS, indirect-emissions accounting) can *improve* TPS cost-effectiveness, partially rehabilitating China's design; (c) the electricity-market-interaction question — regulated dispatch/tariffs block carbon-cost pass-through (Teng-Jotzo-Wang 2017; Cao et al. 2021), which is precisely the friction Shandong's spot market removes: an obvious contribution for the researcher is testing whether national-ETS carbon costs enter day-ahead/real-time offers where spot markets operate. No credible paper on carbon-cost pass-through in China's new provincial spot markets was found — that appears to be an open gap. (5) Datasets recurring in the literature: China National Tax Survey firm records (Cui et al.); unit-level continuous emissions/monitoring data for thermal power units (Qian et al., Qin et al., Yan et al.); pilot-exchange trading data; MEE national-ETS progress reports (2024, 2025 — compliance rates 99.6-99.98%, useful official statistics); matched reported-vs-verified emissions from Beijing/Hubei pilots (Zhang et al. NCC 2019); ICAP ETS factsheets for institutional detail.

## 第 3 节 ETS 经典因果文献(欧美市场)

审稿人默认你熟悉的可信度基准:EU ETS、RGGI、加州、SO2/NOx 市场的因果研究。重点看每条的识别策略。

**1. Colmer, Martin, Muûls, Wagner (2025), "Does Pricing Carbon Mitigate Climate Change? Firm-Level Evidence from the European Union Emissions Trading System"** — *Review of Economic Studies*

- 问题:Did the EU ETS causally reduce manufacturing firms' CO2 emissions, and at what cost to economic activity or via outsourcing?
- 数据:French administrative firm/installation data 1996-2012: manufacturing emissions, energy use, financial accounts, trade flows, and pollution-control investments.
- 识别/方法:Matched difference-in-differences exploiting the ETS's installation-level (capacity-threshold) inclusion criteria: regulated firms compared to observably similar unregulated French manufacturers, with event-study dynamics and checks for outsourcing to unregulated firms/imports.
- 发现:EU ETS reduced regulated firms' emissions by 14-16% with no detectable contraction in output or employment and no evidence of outsourcing; firms made targeted investments that cut emissions intensity, implying genuine global emissions reductions.
- 与本项目的相关性:This is the credibility benchmark for firm-level ETS evaluation a referee will hold a China ETS paper against — the matched-DiD-on-inclusion-thresholds design is the template, and China's ETS also uses capacity thresholds for coverage, so an analogous design is conceivable there.
- 链接:https://academic.oup.com/restud/article/92/3/1625/7681739

**2. Dechezleprêtre, Nachtigall, Venmans (2023), "The joint impact of the European Union emissions trading system on carbon emissions and economic performance"** — *JEEM (Journal of Environmental Economics and Management)*

- 问题:What was the joint effect of the EU ETS on regulated installations' carbon emissions and on regulated firms' economic performance?
- 数据:Installation-level emissions from national polluting emissions registries of France, Netherlands, Norway and the UK, matched to firm-level accounts, roughly 2002-2012 (Phases I-II).
- 识别/方法:Matched difference-in-differences using the ETS capacity-based inclusion criteria to compare regulated installations/firms with similar unregulated ones across four countries.
- 发现:EU ETS reduced emissions on the order of -10% between 2005 and 2012 while having no significant impact on profits or employment; regulated firms' revenues and fixed assets actually increased.
- 与本项目的相关性:Multi-country replication of the 'emissions down, no competitiveness loss' result; the joint emissions-plus-performance evaluation design is the natural blueprint for evaluating China's national ETS on power-sector firms.
- 链接:https://www.sciencedirect.com/science/article/pii/S0095069622001115

**3. Bayer, Aklin (2020), "The European Union Emissions Trading System reduced CO2 emissions despite low prices"** — *PNAS*

- 问题:Did the EU ETS reduce aggregate CO2 emissions even during years when allowance prices were very low?
- 数据:Sectoral CO2 emissions for 25 EU countries, 1990-2016, split into ETS-covered and uncovered sectors.
- 识别/方法:Generalized synthetic control / interactive fixed effects: counterfactual emissions for ETS-covered sectors constructed from the trajectory of uncovered sectors across countries.
- 发现:EU ETS saved more than 1 billion tons of CO2 in 2008-2016 (about 3.8% of total EU-wide emissions relative to a no-ETS counterfactual), implying carbon markets can cut emissions even at low prices, plausibly via expectations of future stringency.
- 与本项目的相关性:Directly on-point for China, where CEA prices have been low: it is the standard citation that low prices need not mean zero effect, and its aggregate synthetic-control design contrasts instructively with the micro DiD literature (Colmer et al.).
- 链接:https://www.pnas.org/doi/10.1073/pnas.1918128117

**4. Martin, Muûls, Wagner (2016), "The Impact of the European Union Emissions Trading Scheme on Regulated Firms: What Is the Evidence after Ten Years?"** — *Review of Environmental Economics and Policy*

- 问题:What does the first decade of ex post empirical evidence say about EU ETS effects on emissions, economic performance/competitiveness, and innovation?
- 数据:Survey article synthesizing ex post econometric studies of EU ETS Phases I-II (no new primary data).
- 识别/方法:Critical review of quasi-experimental designs used in the literature (matching, DiD on inclusion thresholds, regression discontinuity attempts), flagging selection and free-allocation endogeneity problems.
- 发现:Evidence points to modest emissions reductions relative to counterfactual with little robust evidence of negative effects on competitiveness or employment; innovation evidence was still thin at the time.
- 与本项目的相关性:Efficient entry point into the first-decade EU ETS literature and a catalogue of the identification pitfalls (endogenous allocation, selection into coverage) that a Chinese ETS evaluation must also confront.
- 链接:https://www.journals.uchicago.edu/doi/abs/10.1093/reep/rev016

**5. Calel, Dechezleprêtre (2016), "Environmental Policy and Directed Technological Change: Evidence from the European Carbon Market"** — *Review of Economics and Statistics*

- 问题:Did the EU ETS direct technological change toward low-carbon innovation among regulated firms?
- 数据:EPO/PATSTAT patent data matched to thousands of EU ETS-regulated firms and comparable unregulated firms, 2000s.
- 识别/方法:Matched difference-in-differences exploiting installation-level capacity-based inclusion criteria to compare patenting of regulated vs similar unregulated firms.
- 发现:EU ETS increased low-carbon patenting among regulated firms by up to 10% without crowding out other patenting, but with no spillover beyond regulated companies; accounts for under 1% of the increase in European low-carbon patenting overall.
- 与本项目的相关性:The canonical directed-technical-change evaluation of a carbon market; for a China ETS paper it defines the innovation margin and shows how to measure it with patent matching.
- 链接:https://direct.mit.edu/rest/article-abstract/98/1/173/58288/Environmental-Policy-and-Directed-Technological

**6. Calel (2020), "Adopt or Innovate: Understanding Technological Responses to Cap-and-Trade"** — *AEJ: Economic Policy*

- 问题:Does cap-and-trade induce adoption of existing abatement technology or genuine innovation, and did the EU ETS differ from earlier programs?
- 数据:Newly constructed panel of British firms covering patenting, R&D spending, and carbon intensity under the EU ETS.
- 识别/方法:Matched difference-in-differences comparing EU ETS-regulated British firms to similar unregulated firms (again leveraging inclusion criteria).
- 发现:The EU ETS encouraged greater low-carbon patenting and R&D among regulated firms but did not drive short-term reductions in carbon intensity of output — the reverse of older cap-and-trade programs (e.g., SO2), which mainly spurred adoption, not innovation.
- 与本项目的相关性:Sharp conceptual frame (adopt vs innovate) for asking what China's low-price ETS can plausibly induce in a coal-dominated power sector where near-term abatement is mostly dispatch and efficiency adoption.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pol.20180135

**7. Martin, Muûls, de Preux, Wagner (2014), "Industry Compensation under Relocation Risk: A Firm-Level Analysis of the EU Emissions Trading Scheme"** — *American Economic Review*

- 问题:Are the EU ETS's free-allocation (carbon leakage exemption) rules efficient compensation against relocation risk?
- 数据:Management interviews with nearly 800 manufacturing firms in six EU countries (2009), matched to allocation and administrative data.
- 识别/方法:Survey-elicited firm-level relocation/downsizing risk scores combined with an optimal-allocation framework; compares the EU's sector-level exemption criteria against an efficient permit-allocation rule.
- 发现:The EU's carbon-leakage exemption criteria substantially overcompensate firms for given leakage risk; an efficient allocation would cut aggregate job risk by more than half without increasing total compensation.
- 与本项目的相关性:The benchmark analysis of free allocation as political compensation — directly relevant to China's fully free, benchmark-based allocation and to who bears/captures rents in its ETS.
- 链接:https://www.aeaweb.org/articles?id=10.1257/aer.104.8.2482

**8. Bushnell, Chong, Mansur (2013), "Profiting from Regulation: Evidence from the European Carbon Market"** — *AEJ: Economic Policy*

- 问题:How does cap-and-trade regulation affect firm profits — do allowance price changes hit firms through compliance costs or through product prices?
- 数据:Daily stock returns for 552 EUROSTOXX firms around the April 2006 EUA price crash (a 50% price drop, ~€28bn change in annual allowance value), with firm carbon- and electricity-intensity and market-exposure measures.
- 识别/方法:Event study of the 2006 allowance price collapse; cross-sectional heterogeneity in returns by carbon intensity, electricity intensity, and share of sales within the EU identifies the channel.
- 发现:Stock prices fell even for carbon- and electricity-intensive firms when allowance prices crashed, especially firms selling within the EU — investors price the product-price (pass-through) effects of carbon costs, not just net compliance costs and free-allowance value.
- 与本项目的相关性:Shows that allowance-price shocks transmit through output prices — the same pass-through logic connecting CEA prices to Chinese electricity prices; also a clean event-study identification usable around Chinese ETS policy announcements.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pol.5.4.78

**9. Zaklan (2023), "Coase and Cap-and-Trade: Evidence on the Independence Property from the European Carbon Market"** — *AEJ: Economic Policy*

- 问题:Does the Coasean independence property hold in the EU ETS — are power producers' emissions independent of how allowances are allocated?
- 数据:EUTL account-level data on allowance allocations, emissions, and allowance trading for EU ETS power producers around the Phase 3 reform.
- 识别/方法:Difference-in-differences leveraging the 2013 policy change that ended free allocation to electricity generators, comparing affected power producers with comparison installations.
- 发现:Independence holds overall and for large emitters — losing free allocation did not change emissions, firms simply bought allowances; suggestive distortions for small emitters (trading costs/behavioral bias) are too small to break sector-level independence.
- 与本项目的相关性:First-order for China's ETS, which relies entirely on free intensity-benchmark allocation: whether allocation method distorts emissions/dispatch decisions is exactly the question, and this paper supplies the test design.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pol.20210028

**10. Fabra, Reguant (2014), "Pass-Through of Emissions Costs in Electricity Markets"** — *American Economic Review*

- 问题:How completely are emissions (EU ETS) costs passed through to wholesale electricity prices?
- 数据:Rich micro-level bid and unit-level cost data from the Spanish day-ahead electricity market during EU ETS Phase 1 (2004-2006), combined with EUA prices and unit emissions rates.
- 识别/方法:Reduced-form regressions of prices/bids on emissions costs (EUA price x unit emissions rate variation) plus a structural model of optimal multi-unit bidding, minimizing functional-form assumptions; free allocation provides opportunity-cost variation.
- 发现:Emissions costs are almost fully passed through to electricity prices (roughly 80% on average; 70-140% peak and 28-97% off-peak depending on specification); low demand elasticity limits strategic bid distortion of the carbon cost component.
- 与本项目的相关性:The single most relevant paper for this researcher: the canonical carbon-cost pass-through study in an electricity auction market, using exactly the kind of unit-level bid data an Ito-Reguant-style Shandong spot-market paper works with; the template for linking CEA prices to Shandong day-ahead bids and prices.
- 链接:https://www.aeaweb.org/articles?id=10.1257/aer.104.9.2872

**11. Cullen, Mansur (2017), "Inferring Carbon Abatement Costs in Electricity Markets: A Revealed Preference Approach Using the Shale Revolution"** — *AEJ: Economic Policy*

- 问题:How much would a carbon price reduce US electricity-sector emissions in the short run, inferred without any actual carbon price?
- 数据:US electricity generation, fuel prices, and emissions data spanning the shale-gas-driven collapse in natural gas prices (roughly 2006-2012).
- 识别/方法:Revealed preference: coal-to-gas relative fuel-price variation from the shale revolution is mapped into the equivalent variation a carbon price would induce, tracing out a short-run abatement supply curve from observed dispatch responses.
- 发现:A $20 ($70) per ton CO2 price would cut power-sector emissions by about 5% (10%); carbon prices are most effective when gas is cheap and nearly ineffective at pre-shale gas prices — abatement is mostly coal-to-gas re-dispatch.
- 与本项目的相关性:Method for estimating carbon-price responsiveness from fuel-price variation and dispatch data — portable to China's coal-heavy system, and clarifies why an ETS's power-sector bite depends on the dispatch margin, which in Shandong is now set by the spot market.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pol.20150388

**12. Fowlie (2010), "Emissions Trading, Electricity Restructuring, and Investment in Pollution Abatement"** — *American Economic Review*

- 问题:How did electricity-sector economic regulation (restructured vs cost-of-service) affect compliance investment choices and outcomes in the NOx Budget Program?
- 数据:Unit-level compliance/technology-choice data for large stationary sources (mainly power plants) in the eastern US NOx Budget Trading Program, early 2000s.
- 识别/方法:Cross-state variation in electricity industry restructuring status as (conditionally exogenous) variation in investment incentives, embedded in a discrete-choice model of environmental compliance technology adoption.
- 发现:Deregulated plants were significantly less likely to adopt capital-intensive abatement than regulated or public plants; consequently, permit trading shifted emissions toward states with worse air-quality problems.
- 与本项目的相关性:Seminal demonstration that electricity-market institutions shape how firms respond to emissions markets — the exact interaction at the heart of a paper on China's ETS meeting Shandong's newly liberalized spot market (regulated vs market-exposed generators face different carbon-cost incentives).
- 链接:https://www.aeaweb.org/articles?id=10.1257/aer.100.3.837

**13. Fowlie, Reguant, Ryan (2016), "Market-Based Emissions Regulation and Industry Dynamics"** — *Journal of Political Economy*

- 问题:What are the static and dynamic welfare effects of alternative carbon-market designs (auctioning, grandfathering, output-based rebates, border adjustment) in an imperfectly competitive, trade-exposed industry?
- 数据:Plant-level panel of the US Portland cement industry (capacity, entry/exit, production, imports) over roughly three decades.
- 识别/方法:Estimated dynamic oligopoly model (Ericson-Pakes style) of entry, exit, and investment; counterfactual simulations of carbon-pricing designs rather than quasi-experimental variation.
- 发现:Carbon pricing interacts with market power and trade-induced leakage: full auctioning can reduce welfare via exacerbated market-power distortions and leakage, while output-based rebating and border adjustments substantially mitigate leakage at modest cost.
- 与本项目的相关性:The benchmark structural treatment of output-based allocation vs auctioning — China's tradable performance standard (intensity benchmarks) is effectively output-based rebating, and this paper is the standard citation for its efficiency properties.
- 链接:https://www.journals.uchicago.edu/doi/abs/10.1086/684484

**14. Fowlie, Reguant (2022), "Mitigating Emissions Leakage in Incomplete Carbon Markets"** — *JAERE (Journal of the Association of Environmental and Resource Economists)*

- 问题:How should leakage risk be measured and output-based subsidies calibrated when a carbon market covers only a subset of emitting sources?
- 数据:US manufacturing industry data with energy price variation used as a proxy for carbon-price-induced cost variation.
- 识别/方法:Theory delivering industry-specific leakage-risk measures, calibrated empirically using historical energy price variation as the analog of a domestic carbon price; simulations of targeted output-based subsidies.
- 发现:Absent mitigation, leakage from incomplete carbon markets is substantial; output-based subsidies targeted by theoretically consistent leakage-risk measures significantly reduce leakage risk.
- 与本项目的相关性:China's ETS is the archetypal incomplete carbon market (power sector only, free intensity-based allocation = implicit output subsidy); this gives the framework for judging whether that design is a defensible leakage response or a distortion.
- 链接:https://www.journals.uchicago.edu/doi/10.1086/716765

**15. Borenstein, Bushnell, Wolak, Zaragoza-Watkins (2019), "Expecting the Unexpected: Emissions Uncertainty and Environmental Market Design"** — *American Economic Review*

- 问题:Given uncertainty in business-as-usual emissions and abatement, where will California's cap-and-trade allowance price settle?
- 数据:California GHG market: historical time series of emissions drivers (GDP, fuel prices, weather, other policies) available before the 2013 market start, plus estimated abatement supply from market and non-market policies.
- 识别/方法:Ex ante equilibrium simulation: cointegration/time-series econometrics generate the distribution of BAU emissions; combining it with estimated abatement responsiveness yields the probability distribution of allowance prices.
- 发现:Ex ante uncertainty in BAU emissions dwarfs price-responsive abatement in the politically acceptable price range, so the allowance price is very likely to sit at an administrative price floor or ceiling — a generic feature of GHG cap-and-trade markets.
- 与本项目的相关性:Explains why GHG allowance prices tend to be quasi-administered — highly relevant to interpreting China's flat, policy-driven CEA prices — and the demand-uncertainty framework parallels renewable/load forecast-error thinking familiar from the researcher's Shandong work.
- 链接:https://www.aeaweb.org/articles?id=10.1257/aer.20161218

**16. Murray, Maniloff (2015), "Why have greenhouse emissions in RGGI states declined? An econometric attribution to economic, energy market, and policy factors"** — *Energy Economics*

- 问题:How much of the post-2009 emissions decline in RGGI states is attributable to the RGGI cap-and-trade program versus the recession, gas prices, and other policies?
- 数据:State-level panel of electricity generation, fuel prices, emissions, and policy variables for RGGI and non-RGGI states (2000s through ~2012).
- 识别/方法:Three-stage econometric model of state-level generation with counterfactual simulation, decomposing the emissions decline into recession, coal/gas price changes, RPS and other policies, and the RGGI effect.
- 发现:Regional emissions would have been about 24% higher without RGGI — the program accounts for roughly half of the region's emissions reduction over the period, far exceeding reductions in the rest of the US.
- 与本项目的相关性:The canonical RGGI evaluation and a clean illustration of the attribution problem — separating ETS effects from fuel-price and demand shocks — which is the central threat to any China ETS emissions estimate. (Volume/page numbers not verified in this sweep.)
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0140988315002273

**17. Fell, Maniloff (2018), "Leakage in regional environmental policy: The case of the Regional Greenhouse Gas Initiative"** — *JEEM (Journal of Environmental Economics and Management)*

- 问题:Did RGGI's regional carbon price cause electricity generation and emissions to leak to neighboring unregulated states?
- 数据:Detailed US generator-level electricity generation, emissions, and interregional transmission data covering RGGI and adjacent regions before and after RGGI's 2009 start.
- 识别/方法:Difference-in-differences comparing generation and emissions in RGGI states versus nearby non-RGGI states/regions, using the program's start and regional exposure, with transmission data to trace displaced generation.
- 发现:RGGI reduced in-region emissions but shifted generation to units in bordering non-RGGI areas, so a substantial share of the in-region reduction was offset by leakage through the interconnected electricity market.
- 与本项目的相关性:The benchmark measurement of electricity-market leakage from an incomplete regional carbon market — the analog for China is leakage across provincial boundaries and between spot-market and regulated-dispatch provinces, measurable with the researcher's dispatch/trade data.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0095069616302984

**18. Fell (2016), "Comparing policies to confront permit over-allocation"** — *JEEM (Journal of Environmental Economics and Management)*

- 问题:Which supply-side interventions (price collar, Market Stability Reserve, cap reduction) best correct permit over-allocation and price collapse in a cap-and-trade system?
- 数据:No empirical micro data: stochastic dynamic model of a cap-and-trade market parameterized to EU ETS values.
- 识别/方法:Numerical stochastic dynamic programming with banking under demand shocks; welfare and price-volatility comparison of adaptive allocation rules versus fixed cap cuts.
- 发现:Adaptive supply mechanisms — a price collar or an MSR — reduce over-allocation and permit-price volatility more cost-effectively than simply cutting scheduled allocations.
- 与本项目的相关性:The workhorse quantitative analysis of allowance-supply flexibility; China's ETS, with ex post intensity-based allocation and rolling benchmark tightening, is an extreme form of adaptive supply, and this paper provides the evaluation framework.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0095069616000024

**19. Salant (2016), "What ails the European Union's emissions trading system?"** — *JEEM (Journal of Environmental Economics and Management)*

- 问题:Why did EUA prices collapse and behave inconsistently with Hotelling-style intertemporal arbitrage, and what role does anticipated regulatory intervention play?
- 数据:EUA price history and EU ETS institutional record (theory/asset-pricing analysis rather than micro data).
- 识别/方法:Rational-expectations asset-pricing framework in which anticipated government interventions (cap changes, backloading, MSR) enter allowance price formation; applied diagnostically to observed EU ETS price paths.
- 发现:EU ETS price behavior is better explained by anticipated future regulatory intervention (regulatory risk) than by abatement fundamentals alone; intervention expectations undermine the intertemporal efficiency of banking.
- 与本项目的相关性:China's CEA price is overwhelmingly policy-expectation-driven (benchmark announcements, compliance deadlines, banking-restriction rumors); Salant's framework is the right lens for modeling that price formation.
- 链接:https://ideas.repec.org/a/eee/jeeman/v80y2016icp6-19.html

**20. Karp, Traeger (2025), "Smart Cap"** — *Journal of the European Economic Association*

- 问题:Can a cap whose allowance supply adjusts endogenously to the permit price implement (near-)first-best emissions regulation under uncertainty, resolving the taxes-vs-quantities tradeoff?
- 数据:Theory paper — no empirical data; mechanism design with calibrations to carbon-market settings.
- 识别/方法:Mechanism design under asymmetric information: the elasticity of the price-responsive supply schedule is chosen so the market price aggregates technology/macro shocks and implements the first-best permit price; compared to fixed caps, taxes, and MSR-type rules.
- 发现:A 'smart cap' that conditions allowance supply on the permit price eliminates the welfare cost of uncertainty and can be grafted onto existing ETS institutions, outperforming both pure caps and pure taxes.
- 与本项目的相关性:Frontier design theory for responsive allowance supply; China's intensity-based (output-indexed) cap is itself a state-contingent supply rule, and this paper gives the welfare benchmark for judging such designs.
- 链接:https://academic.oup.com/jeea/article/23/2/554/7666759

**21. Känzig (2023), "The Unequal Economic Consequences of Carbon Pricing"** — *NBER Working Paper 31221 (search results indicate conditionally accepted at the American Economic Review; not yet verified in print)*

- 问题:What are the dynamic aggregate and distributional effects of tighter carbon pricing (EU ETS) on emissions, prices, innovation, and household consumption?
- 数据:113 EU ETS regulatory-update events with high-frequency EUA futures price changes in tight windows; euro-area macro aggregates; household expenditure microdata.
- 识别/方法:High-frequency event-study identification of 'carbon policy shocks' (allowance price surprises around regulatory news), used as an external instrument in VARs/local projections; heterogeneity by household income.
- 发现:A restrictive carbon policy shock raises energy prices, lowers emissions, and spurs green innovation but reduces activity, with the burden falling disproportionately on poorer households; general-equilibrium income/employment effects account for about two-thirds of the consumption response.
- 与本项目的相关性:The high-frequency policy-shock identification is directly portable to China (CEA price movements around MEE benchmark and banking announcements) and complements the researcher's high-frequency electricity market data; also the leading macro-distributional benchmark for carbon pricing.
- 链接:https://www.nber.org/papers/w31221

**22. Schmalensee, Stavins (2013), "The SO2 Allowance Trading System: The Ironic History of a Grand Policy Experiment"** — *Journal of Economic Perspectives*

- 问题:What did two decades of the US SO2 (Acid Rain Program) cap-and-trade experiment teach about market-based environmental policy, and why did the market ultimately collapse?
- 数据:Historical record of the Title IV SO2 allowance market, 1990-2012: prices, trading volumes, compliance costs, regulatory and court decisions.
- 识别/方法:Retrospective synthesis (not causal econometrics): assembles the program's cost-savings evidence and traces the institutional shocks — rail deregulation cheapening low-sulfur coal, later court decisions (CAIR/CSAPR) — that first drove and then destroyed allowance value.
- 发现:The program delivered large cost savings, but much of its cost-effectiveness came from unanticipated rail deregulation, and regulatory/judicial intervention eventually collapsed the allowance market — cap-and-trade works but is fragile to overlapping regulation and legal risk.
- 与本项目的相关性:The seminal retrospective a referee expects as the historical anchor; its central lesson — allowance markets are hostage to overlapping regulation and policy risk — maps directly onto China's ETS coexisting with administrative energy-intensity targets and dispatch controls.
- 链接:https://www.aeaweb.org/articles?id=10.1257/jep.27.1.103

### 本节检索笔记(agent 原始记录,含未列入正文的文献与核验警告)

> Coverage and verification notes. (1) Venue correction to the assignment brief: the Colmer/Martin/Muûls/Wagner paper is published in the Review of Economic Studies 92(3), May 2025, pp. 1625-1660 — not QJE. Karp-Traeger's Smart Cap landed in JEEA 23(2) 2025, not JEEM. Känzig's status ('conditionally accepted at AER as of 2026') comes from a search-result snippet and should be re-verified before citing a venue. Murray-Maniloff volume/pages were not visible in results (Energy Economics, Sept 2015). (2) Key methodological throughline for the researcher: the workhorse EU ETS identification is matched DiD exploiting installation capacity-threshold inclusion criteria (Colmer et al.; Calel-Dechezleprêtre; Calel; Dechezleprêtre-Nachtigall-Venmans); a second family uses policy-event variation in allowance prices or allocation rules (Bushnell-Chong-Mansur event study; Zaklan Phase 3 DiD; Känzig high-frequency shocks); a third uses fuel-price variation as a carbon-price analog (Cullen-Mansur; Fowlie-Reguant). (3) Active debates a synthesis should note: micro DiD estimates (10-16% firm-level reductions) vs aggregate synthetic-control estimates (Bayer-Aklin ~3.8% of EU emissions) are not fully reconciled; Borenstein et al.'s conclusion that GHG allowance prices end up at administrative collars is increasingly treated as the default model of ETS price formation and resonates with China's quasi-administered CEA price; the leakage literature has shifted from 'is there leakage' (Fell-Maniloff yes, through electricity trade) to 'how to calibrate output-based rebates' (Fowlie-Reguant JAERE), which matters because China's tradable performance standard is an implicit output subsidy. (4) Frontier papers seen but left off the main list to stay near the 20-paper scale: Fuchs, Stroebel, Terstegge, 'Carbon VIX: Carbon Price Uncertainty and Decarbonization Investments' (NBER WP 32937, 2024 — option-implied EUA uncertainty delays decarbonization investment, real-options channel; very relevant if the China paper touches CEA price informativeness), and Verde (2020, Journal of Economic Surveys) reviewing the econometric competitiveness/leakage evidence. Hernandez-Cortes and Meng's environmental-justice work on California's carbon market was not verified in this sweep and is omitted. (5) Gaps: I did not separately verify the RECLAIM/NOx spatial-trading strand (e.g., Fowlie-Holland-Mansur) or the older SO2 econometric cost literature (Carlson et al.); if the paper leans on spatial heterogeneity of damages, that strand should be added. All metadata above (venues, volumes, pages, findings) were confirmed against AEA/journal/RePEc/NBER pages seen in search results.

## 第 4 节 碳价形成与市场微观结构

EUA/CEA 价格驱动因素、履约期聚集、banking、金融中介。若做碳市场本身的论文,这是主战场。

**1. Mansanet-Bataller, Pardo and Valor (2007), "CO2 Prices, Energy and Weather"** — *The Energy Journal*

- 问题:What fundamentals (energy prices, weather) drive daily EUA price changes in the first year of the EU ETS?
- 数据:Daily EUA prices for 2005 (Phase I) plus energy prices (natural gas, crude oil, electricity) and German/Spanish temperature data.
- 识别/方法:Multivariate time-series regression of daily EUA price changes on energy-price and weather variables; no causal identification, correlational driver analysis.
- 发现:Natural gas and oil (and electricity) prices significantly move carbon prices; extreme temperatures matter. Established the canonical 'fundamentals' driver set for EUA prices.
- 与本项目的相关性:The seminal template for carbon-price-driver regressions that any CEA price-formation analysis will be benchmarked against; its weather-demand channel parallels the weather/renewable-forecast machinery the researcher is building for Shandong.
- 链接:https://journals.sagepub.com/doi/10.5547/ISSN0195-6574-EJ-Vol28-No3-5

**2. Ellerman and Montero (2007), "The Efficiency and Robustness of Allowance Banking in the U.S. Acid Rain Program"** — *The Energy Journal, 28(4): 67-91*

- 问题:Was the observed intertemporal pattern of SO2 allowance banking in the US Acid Rain Program efficient?
- 数据:Aggregate EPA data on emissions, allowance allocations and the bank from the first eight years of the US Acid Rain Program (1995-2002).
- 识别/方法:Structural model of efficient banking (Hotelling-type intertemporal optimization) compared with the observed aggregate abatement/banking path.
- 发现:Contrary to the view that banking was excessive, observed banking was reasonably efficient and robust to counterfactual assumptions; firms use banking rationally, no evidence of emission spikes from bank drawdown.
- 与本项目的相关性:The benchmark empirical test of intertemporal arbitrage in permit markets; the natural reference point for asking whether CEA banking (and China's 2024 restrictions on carrying over surplus allowances) distorts intertemporal price formation.
- 链接:https://journals.sagepub.com/doi/10.5547/ISSN0195-6574-EJ-Vol28-No4-3

**3. Alberola and Chevallier (2009), "European Carbon Prices and Banking Restrictions: Evidence from Phase I (2005-2007)"** — *The Energy Journal, 30(3): 51-80*

- 问题:Did the prohibition on banking EUAs from Phase I into Phase II explain the Phase I price collapse toward zero?
- 数据:Daily EUA spot and futures prices 2005-2007 (Powernext/ECX), plus banking-policy announcement dates (e.g., the French ban on inter-phase banking).
- 识别/方法:Event-type time-series analysis and a Hotelling-CAPM/cost-of-carry framework testing whether spot-futures relationships broke down once inter-period banking was restricted.
- 发现:Banking restrictions contributed significantly to the low Phase I prices; the cost-of-carry relationship between spot and Phase II futures fails after banking between phases was disallowed.
- 与本项目的相关性:Direct empirical demonstration that banking rules are priced into carbon markets - the cleanest analog for evaluating how China's evolving CEA rollover/hoarding rules (2024 State Council penalty rules, carry-over limits) move CEA prices.
- 链接:https://journals.sagepub.com/doi/10.5547/ISSN0195-6574-EJ-Vol30-No3-3

**4. Hintermann (2010), "Allowance Price Drivers in the First Phase of the EU ETS"** — *Journal of Environmental Economics and Management, 59(1): 43-56*

- 问题:Did Phase I EUA prices reflect marginal abatement costs, and what structural drivers (fuel prices, weather, hydro, verified-emissions news) explain them?
- 数据:Daily EUA prices 2005-2007 with fuel prices, temperature, reservoir (hydro) levels, economic indicators, and announcement dates of verified emissions.
- 识别/方法:Structural model of the allowance price as a function of marginal abatement cost drivers, estimated on daily data with attention to the April 2006 verified-emissions news break.
- 发现:Before April 2006 prices were not well explained by marginal abatement costs; the 2006 crash reflects an expectations adjustment about aggregate emissions. Price-fundamental links strengthen only later in Phase I.
- 与本项目的相关性:Canonical evidence that a young carbon market can trade away from fundamentals - precisely the null hypothesis to test on the young CEA market, where allocation news (MEE quota documents) plays the role of the 2006 verified-emissions release.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0095069609000862

**5. Bushnell, Chong and Mansur (2013), "Profiting from Regulation: Evidence from the European Carbon Market"** — *American Economic Journal: Economic Policy, 5(4): 78-106*

- 问题:How did the April 2006 EUA price crash (a ~50% drop) affect the equity values of carbon- and electricity-intensive firms?
- 数据:Daily stock returns for 552 EUROSTOXX firms around the April 2006 EUA crash, matched to industry carbon/electricity intensity and EU sales exposure.
- 识别/方法:Event study exploiting the sharp, arguably exogenous allowance-price crash as a shock to expected permit values and product prices.
- 发现:Stock prices fell for firms in carbon- and electricity-intensive industries even though compliance costs fell, implying investors price product-price (pass-through) effects, not just permit values.
- 与本项目的相关性:Shows how a single carbon-price event identifies the incidence of carbon costs via electricity prices; a template for event studies around CEA policy shocks and for linking carbon prices to power-sector valuations in China.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pol.5.4.78

**6. Fabra and Reguant (2014), "Pass-Through of Emissions Costs in Electricity Markets"** — *American Economic Review, 104(9): 2872-2899*

- 问题:How completely are EUA emissions costs passed through to wholesale electricity prices?
- 数据:Rich micro bid-level data from the Spanish day-ahead electricity market during the EU ETS, with unit-level marginal costs and emissions rates.
- 识别/方法:Reduced-form pass-through regressions plus structural estimation of optimal multi-unit auction bidding, using high-frequency variation in emissions costs.
- 发现:Emissions costs are almost fully passed through to electricity prices; with high-frequency auctions and inelastic demand, firms have weak incentives to adjust markups after a cost shock.
- 与本项目的相关性:The bridge between the carbon strand and the researcher's Ito-Reguant-style Shandong work: the benchmark for whether CEA costs enter day-ahead electricity bids - a pass-through China's TPS design and regulated tariffs may mute, which is itself a paper-worthy contrast.
- 链接:https://www.aeaweb.org/articles?id=10.1257/aer.104.9.2872

**7. Koch, Fuss, Grosjean and Edenhofer (2014), "Causes of the EU ETS price drop: Recession, CDM, renewable policies or a bit of everything? - New evidence"** — *Energy Policy, 73: 676-685*

- 问题:How much of the 2008-2013 EUA price collapse (30 EUR to under 5 EUR) is explained by observable fundamentals (recession, CDM offset inflow, renewables expansion)?
- 数据:EUA prices 2008-2013 with economic activity indices, wind/solar generation, and CDM credit (CER) supply data.
- 识别/方法:Time-series regressions decomposing EUA price variation into candidate demand-side drivers; explicitly quantifies unexplained residual variation.
- 发现:Economic activity robustly explains part of EUA dynamics but renewables and offset use have only moderate effects; the bulk of price variation (~90%) is left unexplained, pointing to policy/regulatory expectations as the missing driver.
- 与本项目的相关性:The pivotal 'fundamentals are not enough' result that motivated the policy-news literature (Kaenzig); for the CEA market - where allocation policy is the dominant news - this framing is even more apt.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0301421514003966

**8. Ellerman, Marcantonini and Zaklan (2016), "The European Union Emissions Trading System: Ten Years and Counting"** — *Review of Environmental Economics and Policy, 10(1): 89-107*

- 问题:What has ten years of the EU ETS delivered in terms of emissions, allowance prices, offset use, and institutional evolution?
- 数据:EU ETS program data 2005-2015: EUTL emissions and allocations, auction data, EUA price history, offset (CER/ERU) surrender data.
- 识别/方法:Institutional-empirical assessment (not causal econometrics): documents legislative evolution from free allocation to auctioning and evaluates performance against design intent.
- 发现:The EU ETS reduced emissions despite low prices; the shift to auctioning and centralized allocation was the key institutional development; price weakness reflects cap-setting and macro shocks rather than market failure per se.
- 与本项目的相关性:The standard institutional reference on EU ETS evolution (the 'Ellerman' anchor of this strand) against which China's free-allocation, intensity-based national market can be positioned in the paper's institutional section.
- 链接:https://academic.oup.com/reep/article/10/1/89/2583826

**9. Fan and Todorova (2017), "Dynamics of China's carbon prices in the pilot trading phase"** — *Applied Energy, 208: 1452-1467*

- 问题:Are prices in China's pilot carbon markets linked to domestic/international energy prices, stock markets, and sentiment, and to each other?
- 数据:Daily allowance prices for Beijing, Guangdong, Hubei and Shenzhen pilots, 2014-2016, plus energy, metals, equity and sentiment variables (exchange data as carried by Wind).
- 识别/方法:Time-series analysis (correlation/regression and volatility modeling) of pilot allowance returns against macro and energy factors, and across pilots.
- 发现:Chinese pilot carbon prices are largely disconnected from fundamentals and from each other (only weak links, e.g., Hubei to international gas prices), evidencing fragmented, thin, compliance-driven markets.
- 与本项目的相关性:The most-cited English-language evidence that Chinese pilot carbon prices did not behave like the EUA fundamentals benchmark - the pre-2021 baseline for any claim about what changed (or did not) with the national CEA market.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0306261917312801

**10. Hitzemann and Uhrig-Homburg (2018), "Equilibrium Price Dynamics of Emission Permits"** — *Journal of Financial and Quantitative Analysis, 53(4): 1653-1678*

- 问题:What price dynamics (volatility structure, leverage effect, terminal behavior) does the design of a cap-and-trade system induce in equilibrium?
- 数据:Model calibrated to and evaluated against EU ETS (EUA) spot/futures and options data; primarily a theory paper.
- 识别/方法:Stochastic dynamic equilibrium model of an emission permit market with banking and compliance deadlines; derives closed-form permit price processes and option pricing implications.
- 发现:Permit prices behave like an option on the compliance-shortage event: prices are bimodal near phase ends, volatility rises as prices fall (inverse leverage effect), and dynamics differ fundamentally from standard commodities.
- 与本项目的相关性:The asset-pricing foundation for carbon markets; its compliance-deadline option structure is the right theoretical lens for the CEA market where nearly all trading and price movement clusters at surrender deadlines.
- 链接:https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/abs/equilibrium-price-dynamics-of-emission-permits/F710C148DF50B4DAF00FC58FEE7389C7

**11. Pizer and Zhang (2018), "China's New National Carbon Market"** — *AEA Papers and Proceedings, 108: 463-467*

- 问题:How is China's announced national ETS designed, how does it differ from US/EU cap-and-trade, and what research questions does it raise?
- 数据:Institutional/policy documents from China's December 2017 national ETS construction program and the seven regional pilots; no econometrics.
- 识别/方法:Institutional analysis of the tradable-performance-standard (rate-based, output-indexed free allocation) design and its incentive properties.
- 发现:China's design (intensity benchmarks, ex-post allocation, power-sector-first) departs sharply from EU/US cap-and-trade; the implicit output subsidy and regulated electricity prices raise distinct efficiency and price-formation questions.
- 与本项目的相关性:Compact, citable top-venue statement of why CEA price formation cannot be interpreted through an EU ETS lens - foundational framing for a paper on the Chinese carbon market by an electricity-markets researcher.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pandp.20181029

**12. Cludius and Betz (2020), "The Role of Banks in EU Emissions Trading"** — *The Energy Journal, 41(2): 275-299*

- 问题:What roles do banks and other financial intermediaries play in EU emissions trading, and for which regulated firms do they matter most?
- 数据:EU Transaction Log (EUTL) account-level transfer data plus semi-structured interviews with market participants.
- 识别/方法:Descriptive network/transaction analysis and regressions on EUTL transfer patterns, distinguishing intermediation, exchange access, and hedging services; interview evidence for mechanisms.
- 发现:Banks account for a large and growing share of EUA transactions, providing small and mid-sized compliance firms indirect market access and hedging; intermediation is a core part of how the carbon market actually clears.
- 与本项目的相关性:The key empirical paper on financial intermediation in carbon markets - the exact institutional feature China's national ETS lacks (compliance-entities-only trading), which is the leading explanation for CEA thinness and deadline clustering.
- 链接:https://journals.sagepub.com/doi/10.5547/01956574.41.2.jclu

**13. Quemin and Trotignon (2021), "Emissions trading with rolling horizons"** — *Journal of Economic Dynamics and Control, 125: 104099*

- 问题:Can bounded, rolling planning horizons explain observed EU ETS banking behavior and the market's response to supply-side policies (MSR)?
- 数据:Calibrated to annual EU ETS market outcomes 2008-2018 (aggregate bank, prices) and futures yield-curve-implied discount rates.
- 识别/方法:Dynamic model of permit trading with rolling finite horizons; calibration/validation against observed banking dynamics, used for MSR counterfactuals.
- 发现:A rolling ~10-year horizon reconciles observed banking with discount rates implied by futures curves; bounded foresight materially changes how supply-control policies (like the MSR) transmit to prices.
- 与本项目的相关性:The modern workhorse for intertemporal carbon-price formation under behavioral frictions; directly applicable to asking what discount rate, horizon and expected-policy path is embedded in CEA prices, given China's ad hoc allocation cycles.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0165188921000348

**14. Goulder, Long, Lu and Morgenstern (2022), "China's unconventional nationwide CO2 emissions trading system: Cost-effectiveness and distributional impacts"** — *Journal of Environmental Economics and Management, 111: 102561*

- 问题:How cost-effective is China's tradable performance standard (TPS) relative to cap-and-trade, and what are its distributional impacts across provinces and generator types?
- 数据:Matched plant-level data on China's power sector (generator technologies, benchmarks, provinces) fed into a multi-period equilibrium simulation model of the TPS.
- 识别/方法:Structural/simulation analysis of the TPS as an emissions price plus implicit output subsidy; compares TPS, C&T and benchmark-design counterfactuals.
- 发现:The TPS's implicit output subsidy roughly doubles abatement costs relative to cap-and-trade for the same emissions; the four-benchmark design and absence of auctioning add further costs; distributional impacts across provinces are large.
- 与本项目的相关性:The definitive economic analysis of the instrument that generates CEA demand; its output-subsidy logic implies muted pass-through of CEA prices into electricity output decisions - a first-order issue for connecting the carbon market to Shandong spot prices.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0095069621001133

**15. Li, Yao and Wang (2022), "The first compliance cycle of China's National Emissions Trading Scheme: insights and implications"** — *Carbon Neutrality, 1: 34 (Springer; field journal)*

- 问题:How did trading, prices and compliance behave in the national ETS's first compliance cycle (July-December 2021)?
- 数据:SEEE (Shanghai Environment and Energy Exchange) daily trading data for the first cycle: listed vs bulk/block trades, volumes, prices; MEE compliance statistics.
- 识别/方法:Descriptive empirical analysis of the first-cycle trading record; no causal design.
- 发现:Trading was heavily compliance-clustered: Jul-Oct daily volume mostly under 0.3 Mt, while December alone traded 136 Mt (about double the prior five months combined); prices followed a 'smile' from 48 to ~42 to 54.22 CNY/t; trading dominated by SOEs transacting for compliance, not investment; ~99.5% compliance.
- 与本项目的相关性:The best-documented academic record of exactly the CEA microstructure facts the strand targets - thin trading, deadline clustering, block vs listed trade structure - and a guide to what SEEE daily bulletins contain as data.
- 链接:https://link.springer.com/article/10.1007/s43979-022-00035-3

**16. Quemin and Pahle (2023), "Financials threaten to undermine the functioning of emissions markets"** — *Nature Climate Change, 13: 22-31*

- 问题:When does financial-actor participation (speculation) in allowance markets support versus undermine market functioning, and how should it be monitored?
- 数据:EU ETS data including ICE EUA futures Commitments-of-Traders position reports, price/volume data, and open interest by trader category.
- 识别/方法:Diagnostic framework (perspective piece with original empirics): position-based speculation indices (e.g., Working's T) applied to EUA futures to assess the scale of speculative activity around the 2018-2021 price run-up.
- 发现:Financial players provide necessary liquidity and hedging counterparties, but tightening caps attract speculative inflows whose destabilizing potential is real; proposes a speculation-monitoring toolbox for allowance markets.
- 与本项目的相关性:Frames the policy question China faces from the opposite direction - the CEA market has too few financial participants rather than too many; also documents the COT-report data infrastructure the CEA market lacks.
- 链接:https://www.nature.com/articles/s41558-022-01560-w

**17. Kaenzig (2023), "The Unequal Economic Consequences of Carbon Pricing"** — *NBER Working Paper 31221 (also CEPR DP20405, 2025; SSRN 3786030; publication status as of Aug 2026 not verified)*

- 问题:What are the aggregate and distributional causal effects of carbon pricing, identified from carbon policy news shocks in the EU ETS?
- 数据:High-frequency EUA futures (front contract) price changes in tight windows around 113 EU ETS regulatory/supply announcements, 2005 onward, combined with euro-area macro and household expenditure-survey data.
- 识别/方法:High-frequency identification: the carbon policy surprise series instruments carbon-price movements in proxy-VAR/local-projection models of macro and distributional outcomes.
- 发现:A restrictive carbon policy shock raises energy prices, cuts emissions (~1/3 of emissions variation at 1-year horizons), spurs green innovation, and lowers activity, with the burden falling disproportionately on poor households; two-thirds of the consumption response is indirect via income/employment.
- 与本项目的相关性:The methodological centerpiece of the strand: shows regulatory news, not fundamentals, moves carbon prices, and how to build a policy-shock series from allowance futures - a design portable to CEA/pilot prices around MEE allocation and expansion announcements, and akin to the researcher's forecast-error shock logic in Shandong.
- 链接:https://www.nber.org/papers/w31221

**18. Kaenzig and Konradt (2024), "Climate Policy and the Economy: Evidence from Europe's Carbon Pricing Initiatives"** — *IMF Economic Review, 72(3)*

- 问题:How do the economic effects of carbon pricing via the EU ETS compare with national carbon taxes in Europe?
- 数据:European carbon policy shock series (EUA futures high-frequency surprises) and cross-country panel data on European economies with national carbon taxes.
- 识别/方法:Compares dynamic responses to identified EU ETS carbon policy shocks with panel local-projection estimates of national carbon tax changes.
- 发现:ETS-driven carbon pricing shows larger output and price effects than national carbon taxes, partly reflecting coverage and revenue-recycling differences; published version of the carbon-policy-shock agenda.
- 与本项目的相关性:Peer-reviewed anchor for the Kaenzig identification approach and a comparison template (trading system vs tax) useful when positioning China's ETS against alternative carbon pricing instruments.
- 链接:https://ideas.repec.org/a/pal/imfecr/v72y2024i3d10.1057_s41308-024-00256-9.html

**19. Borri, Liu, Tsyvinski and Wu (2026), "Trading Frictions in Dynamic Cap-and-Trade Markets"** — *arXiv working paper 2606.03767 (finance WP; check for NBER/SSRN version)*

- 问题:How do slow participation, limited intermediation, and heterogeneous information jointly distort prices in cap-and-trade markets?
- 数据:2.7 million transactions from the EU ETS registry (EUTL) and compliance records, 2005-2021.
- 识别/方法:Documents micro trading facts (non-participation, compliance-month clustering, return predictability from operator flows), then builds and calibrates a dynamic stochastic model with multiple interacting frictions.
- 发现:About 40% of operators do not trade in a given year; purchases cluster in April (compliance) with systematically high returns; operator trading predicts prices. Frictions interact non-additively - combined they amplify price distortions beyond the sum of parts.
- 与本项目的相关性:The 2026 frontier of exactly this strand's microstructure agenda: compliance-deadline clustering and thin participation in the EU ETS mirror the CEA facts, giving the researcher a state-of-the-art framework to port to SEEE data.
- 链接:https://arxiv.org/abs/2606.03767

**20. [Authors not verified from accessible pages] (2026), "A comparative review of compliance-linked carbon offset programs in China and California: The new CCER and the Compliance Offset Program"** — *Advances in Climate Change Research (Elsevier; inferred from PII S1674-9278, not directly confirmed)*

- 问题:How do the design, integrity safeguards and market linkage of the relaunched CCER program compare with California's Compliance Offset Program?
- 数据:Program documents and market data on the new CCER scheme (relaunched January 2024 after the 2017 suspension) and California's offset program; ScienceDirect author page suggests Da Zhang (Tsinghua) among authors but I could not open the page to confirm.
- 识别/方法:Comparative institutional review; no causal econometrics.
- 发现:Both systems prioritize environmental integrity via different governance: China emphasizes digital MRV scale-up, methodology expansion and supplier liability; California focuses on permanence and baselines. CCER credits are usable for up to 5% of ETS compliance obligations.
- 与本项目的相关性:The most substantive academic treatment found of the 2023-24 CCER restart, whose credits interact with CEA demand (5% offset limit) and whose renewable-energy methodologies (offshore wind, solar thermal) tie the offset market to the power sector the researcher studies.
- 链接:https://www.sciencedirect.com/science/article/pii/S1674927826000717

### 本节检索笔记(agent 原始记录,含未列入正文的文献与核验警告)

> COVERAGE CAVEATS AND GAPS. (1) CEA microstructure gap: I found NO top-journal (or even solid field-journal) econometric paper specifically on SEEE block/bulk trades vs listed trades (e.g., block-trade discounts) or on intraday CEA microstructure. The block-vs-listed institutional facts and volume splits are documented in Li-Yao-Wang (Carbon Neutrality 2022), MEE's annual Progress Reports of China's National Carbon Market (2024: https://www.mee.gov.cn/ywdt/xwfb/202407/W020240722528850763859.pdf ; 2025 edition also public), ICAP's China National ETS factsheet (https://icapcarbonaction.com/en/ets/china-national-ets), and IETA business briefs - these are the de facto data documentation for the market. This is a genuine hole a researcher with SEEE daily bulletin data could fill; the Borri-Tsyvinski et al. EU framework is the obvious import. (2) Pilots-vs-national price discovery: the existing literature is field/low-tier (TVP-VAR connectedness papers in PLOS One, Economic Change and Restructuring 2022 'Spillover effect among independent carbon markets', Energies) - no credible top-journal price-discovery paper between pilots and the national CEA market yet. (3) CCER: economics literature is very thin; pre-2017 CCER traded around CNY 6-20/t with price info mainly from Beijing/Shanghai exchanges; post-restart (Jan 2024) prices briefly exceeded CEA (~CNY 107 in March 2024 at Beijing Green Exchange) then fell to a discount. No rigorous pricing paper found; mostly law-firm briefs (Clifford Chance April 2024) and reviews. DATASETS: EUA - ICE/EEX EUA futures via Refinitiv/Bloomberg; EUTL registry transactions (used by Cludius-Betz and Borri et al., 2.7M transactions 2005-2021); ICE Commitments-of-Traders position reports (Quemin-Pahle); ESMA carbon market reports (2023 ESMA report: 73% of secondary-market volume involved financial institutions). CEA - SEEE daily bulletins (listed vs block volumes, OHLC); CEIC 'CEIS: Shanghai Environment and Energy Exchange: CEA' daily open/close/high/low series (from Nov 2013 for pilots); Wind and CSMAR carry pilot + national daily prices (standard in Chinese-literature papers); ICAP allowance price explorer; Beijing Green Exchange for CCER prices; MEE progress reports for compliance rates (2021: 99.5%; 2022: 99.9%) and annual volumes. KEY STYLIZED FACTS for the paper: CEA trading is compliance-clustered (Q4-2024 = 79% of annual volume; December 2021 = 136 Mt vs <0.3 Mt/day Jul-Oct 2021); only compliance entities may trade (no financial intermediaries - the mirror image of the EU debate); 2024 price surge to ~CNY 100+ driven by hoarding after February 2024 State Council regulation raising penalties for missed surrender (S&P Global reporting); 2024-25 reforms add cement/steel/aluminum (~1,500 entities, ~3 Gt) and restrict allowance carry-over, which should be priced (Alberola-Chevallier logic). DEBATES in the strand: (a) fundamentals vs policy news for EUA (Koch et al. find ~90% unexplained by fundamentals; Kaenzig shows regulatory news moves prices - now the dominant view per the useful survey Friedrich, Mauer, Pahle and Tietjen 2020, 'From fundamentals to financial assets: the evolution of understanding price formation in the EU ETS', ZBW/EconStor WP, https://www.econstor.eu/handle/10419/225210); (b) speculation harmful vs liquidity-providing (Quemin-Pahle vs ESMA's benign assessment); (c) whether China's TPS + regulated electricity prices can generate meaningful carbon-price signals at all (Goulder et al.; Pizer-Zhang). ADJACENT PAPERS worth knowing but outside this strand's core: Zhang, Karplus, Zhang et al. (2019) Nature Climate Change 9:164-169 'Integrity of firms' emissions reporting in China's early carbon markets' (Beijing/Hubei reported-vs-verified emissions discrepancies shrink with experience - relevant to CEA data credibility); Li, Liu, Wang and Zhang (Tsinghua SEM WP, July 2025) 'The Real Effects of China's Carbon Dioxide Emissions Trading Program' (firm-level DiD, investment/employment effects; circulating via the AFA/Journal of Finance submission portal - under review, not accepted); Bauer and Kaenzig et al. 'Carbon Pricing and Inflation Expectations' (Brookings WP 106, March 2026 - frontier, full author list unverified). VERIFICATION NOTES: every paper listed was seen in search results or fetched pages; the two 2026 entries are working-paper/just-published items whose details (Borri et al. author list, arXiv abstract; CCER review journal/authors) rest on single sources; Kaenzig (2023) journal placement was checked and remains unverified as published in a journal as of Aug 2026. Springer and ScienceDirect abstract pages frequently returned 403s through this environment's proxy; where that happened I verified via RePEc/EconPapers, publisher search results, or PDF fetch instead.

## 第 5 节 2024–2026 制度前沿(区分已实施 vs 已宣布)

论文制度背景部分需要的事实与日期。本节末尾检索笔记里的"ENACTED vs ANNOUNCED 阶梯"可以直接当论文附录的底稿。

**1. State Council of the People's Republic of China (2024), Interim Regulations on the Administration of Carbon Emissions Trading (碳排放权交易管理暂行条例)** — *State Council decree (primary legal document); English coverage via ICAP and gov.cn*

- 问题:First State Council-level legislation giving China's national ETS a binding legal foundation (previously it ran on ministerial rules only).
- 数据:Legal text. Published 4 February 2024, effective 1 May 2024. ENACTED.
- 识别/方法:N/A (legal instrument). Key provisions: defines tradable products, allocation and MRV responsibilities; raises non-compliance penalties from a previous CNY 30,000 maximum to fines of roughly five to ten times the market value of the allowance shortfall; explicit sanctions for emissions-data falsification; states that auctioning 'is to be introduced and gradually expanded' (no timeline).
- 发现:Elevates ETS governance from MEE ministerial level to State Council level, closing the enforcement vacuum that existed since the July 2021 launch; widely read as the precondition for sectoral expansion and stricter compliance.
- 与本项目的相关性:The baseline legal citation for any institutional section on the post-2024 Chinese carbon market; the enforcement-credibility change is a candidate structural break for price/compliance behavior. For a Shandong electricity paper, it dates when carbon obligations on coal generators became legally enforceable within the Dec 2021 - Aug 2026 sample.
- 链接:https://icapcarbonaction.com/en/news/china-strengthens-legal-foundation-national-ets

**2. Ministry of Ecology and Environment (2025), Work Plan for Covering the Steel, Cement and Aluminum Smelting Industries in the National Carbon Emissions Trading Market** — *MEE policy document; English coverage via ICAP, S&P Global, Sino-German Climate Cooperation*

- 问题:Expands national ETS coverage beyond power generation to steel, cement and aluminum smelting.
- 数据:Policy document. Public consultation September 2024; State Council approval mid-March 2025; released by MEE in late March 2025 (ICAP dates it 20 March 2025; some coverage 26 March 2025). ENACTED.
- 识别/方法:N/A (policy instrument). Adds ~1,500 entities and ~3 GtCO2e (~5% of global emissions), bringing the ETS to ~3,700 entities and ~8 GtCO2e (~60% of China's CO2). First compliance cycle covers 2024 emissions, surrender due end-2025. Inclusion threshold 26,000 tCO2e/yr.
- 发现:For 2024, new sectors get free allowances equal to verified emissions (pure grandfathering, so no net compliance cost in year one — the year is essentially an MRV shakedown cruise); from 2025 allocation shifts to intensity/performance benchmarking.
- 与本项目的相关性:Core institutional fact for the paper: the ETS moved from a power-only system to a multi-sector one during 2025, changing the marginal buyer pool and demand for CEAs. Shandong is China's largest province for steel, aluminum and cement capacity, so the expansion binds exactly where the researcher's electricity data live.
- 链接:https://icapcarbonaction.com/en/news/china-officially-expands-national-ets-cement-steel-and-aluminum-sectors

**3. General Office of the CPC Central Committee and General Office of the State Council (2025), Opinions on Advancing Green and Low-Carbon Transformation and Strengthening the Construction of the National Carbon Market** — *CPC/State Council guidance document; English coverage via ICAP, Carbon Brief-adjacent outlets, Sino-German Climate Cooperation*

- 问题:Sets the roadmap for converting the ETS from an intensity-based tradable performance standard to an absolute cap-and-trade system.
- 数据:Guidance document issued 25 August 2025. ANNOUNCED direction with dated milestones, NOT yet implementing regulation — MEE must issue supporting rules; current operations remain intensity-based.
- 识别/方法:N/A. Milestones: by 2027, ETS covers 'all major industrial emitters', sectors with stable emissions move to absolute caps, and output growth no longer automatically raises allocations; by 2030, a mature cap-and-trade system combining free and paid (auctioned) allocation, plus a credible internationally-aligned voluntary market. Next-in-line sectors flagged in coverage: civil aviation, copper smelting, flat glass, petrochemicals, chemicals, paper.
- 发现:Highest-authority commitment to date to absolute caps and auctioning; analysts read it as aligning the ETS with the 30/60 targets and as groundwork for international (CBAM) recognition of Chinese carbon prices.
- 与本项目的相关性:This is the single most important 'policy frontier' citation for 2025-2026: any forward-looking discussion of Chinese carbon prices must distinguish the current intensity regime (through at least 2026) from the announced 2027/2030 absolute-cap milestones. Cite as announced, with the 25 Aug 2025 date.
- 链接:https://icapcarbonaction.com/en/news/china-issues-landmark-guidelines-transition-absolute-cap-and-expand-scope-national-ets

**4. Ministry of Ecology and Environment (2025), 2024-2025 Allowance Cap and Allocation Plan for the Steel, Cement and Aluminum Smelting Sectors in the National Carbon Market** — *MEE allocation plan; English coverage via ICAP*

- 问题:Operationalizes allocation, banking and compliance rules for the three newly covered industrial sectors.
- 数据:Policy document released 16 November 2025, covering ~3,700 entities / ~3 Gt of allowances. ENACTED.
- 识别/方法:N/A. 2024: allowances = verified 2024 emissions (grandfathering). 2025: intensity benchmarking — within ±20% of sector benchmark, allocation scaled by (1 − deviation × 15%); beyond ±20%, adjustment capped at ±3% of verified emissions. Banking capped at 100,000 allowances plus 150% of net allowances sold (raised from 10,000 in the draft). Surrender deadlines: end-Dec 2025 for 2024, end-Dec 2026 for 2025 (70% pre-allocated). CCER offsets up to 5% of verified emissions, restricted to credits issued on/after 22 Jan 2024.
- 发现:Introduces explicit banking restrictions for industrial sectors intended to prevent hoarding and support price formation; keeps first-cycle stringency at zero and phases in benchmark discipline from 2025.
- 与本项目的相关性:The authoritative source for the 'banking restrictions announced 2025' institutional fact and for exact compliance timing (Dec 2025 surrender) that shows up as demand spikes in CEA price data.
- 链接:https://icapcarbonaction.com/en/news/china-releases-2024-2025-allowance-allocation-plan-industrial-sectors-national-ets

**5. Ministry of Ecology and Environment (2024), Allowance Allocation Plan for the Power Generation Sector, 2023-2024 compliance years** — *MEE allocation plan; English coverage via ICAP*

- 问题:Sets power-sector benchmarks and, for the first time, restricts allowance banking in the founding sector of the ETS.
- 数据:Draft released 2 July 2024 (consultation to 10 July 2024), finalized later in 2024 (exact final date not verified). ENACTED.
- 识别/方法:N/A. Power entities may bank only 10,000 tonnes plus 1.5× their net sales over 2019-2024 (unlimited banking had applied in the first compliance periods); borrowing from future periods (allowed 2021-2022) abolished from 2023. Four output-based benchmarks (coal <300MW, ≥300MW, unconventional coal, gas); shortfall for coal plants capped at 20% of verified emissions.
- 发现:The 'use it or lose it' banking rule was the proximate driver of the CEA price run-up to the all-time high of RMB 104.5/t in November 2024 and subsequent selling pressure (prices fell to ~RMB 71/t, ~US$10, by August 2025).
- 与本项目的相关性:Directly relevant to interpreting CEA price dynamics within the researcher's Dec 2021 - Aug 2026 sample, and to the carbon-cost term in Shandong coal units' marginal cost during the spot-market sample.
- 链接:https://icapcarbonaction.com/en/news/china-releases-allocation-plan-power-sector-2023-and-2024

**6. Ministry of Ecology and Environment (2024), Relaunch of the China Certified Emission Reduction (CCER) voluntary carbon market** — *MEE program launch; coverage via ICAP, Clifford Chance client briefing (April 2024)*

- 问题:Restarts China's domestic offset market (suspended 2017-2023) with new methodologies and links it to national ETS compliance.
- 数据:Trading relaunched 22 January 2024 (CCER trading on the Beijing Green Exchange; CEA trading remains on the Shanghai Environment and Energy Exchange). First four methodologies (published late 2023): afforestation, grid-connected solar thermal power, offshore wind power, mangrove restoration/creation. By August 2025, six approved methodologies (adding coal mine methane utilization and energy-efficient highway tunnel lighting). ENACTED.
- 识别/方法:N/A. Covered ETS entities may use CCERs for up to 5% of verified emissions; the Nov 2025 industrial allocation plan restricts eligible credits to post-22-Jan-2024 issuances. First transaction: CNOOC bought 250,000 t on 23 January 2024. Registry as of 2025: 38 listed projects, of which 22 offshore wind (potential ~110.6m credits).
- 发现:Restart is deliberately narrow-methodology and state-controlled; the live integrity debate is offshore-wind additionality (MEE's argument rests on offshore wind's high costs relative to onshore).
- 与本项目的相关性:CCER supply is a (capped) substitute for CEAs, hence part of any supply-demand model of the compliance market; offshore-wind CCERs also tie the offset market directly to renewable deployment economics, adjacent to the researcher's renewables work.
- 链接:https://icapcarbonaction.com/en/news/china-launches-domestic-offset-market-align-national-ets-goals

**7. International Carbon Action Partnership (2026), Emissions Trading Worldwide: ICAP Status Report 2026 (China National ETS chapter/factsheet)** — *ICAP annual status report*

- 问题:Comprehensive, dated reference compendium of China national ETS design as of early 2026.
- 数据:Published 14 April 2026. Companion continuously-updated China National ETS factsheet on the ICAP website.
- 识别/方法:N/A (reference document; compiled from official Chinese sources).
- 发现:Confirms: coverage ~8 GtCO2 (~60% of China's CO2) across power, steel, cement, aluminum; 100% free allocation in 2024 for new sectors moving to performance-based in 2025; banking limits as above; auctioning announced with no timeline; absolute-cap transition guidelines of Aug 2025; verification deadlines for 2024 emissions of June 2025 (power) and Aug-Sep 2025 (industry); pilot ETSs (incl. Shenzhen, Guangdong, Hubei, Shanghai, Tianjin) expanding into data centers, aviation, road transport, etc.
- 与本项目的相关性:The standard citable secondary source for institutional facts with dates; economists routinely cite ICAP status reports for ETS design parameters. Use the 2026 edition so facts are current through the researcher's Aug 2026 sample end.
- 链接:https://icapcarbonaction.com/system/files/document/260414_icap_sr26_web.pdf

**8. Ministry of Ecology and Environment (2025), Progress Report of China's National Carbon Market (2025) [and the 2024 edition, July 2024]** — *MEE official annual report*

- 问题:MEE's own annual account of market operation: turnover, prices, compliance rates, MRV reforms.
- 数据:2024 edition published July 2024; 2025 edition published circa 27 September 2025 (PDF on mee.gov.cn).
- 识别/方法:N/A (official statistics). Practice note on data publication: MEE publishes aggregate market statistics and entity lists (company name, province, credit identifier) but does NOT publish firm-level verified emissions; steel/cement/aluminum entities must now report monthly through the national platform; in March 2022 MEE publicly named firms and verifiers involved in data manipulation during the first compliance period.
- 发现:Documents near-universal compliance (99%+ surrender rates), rising cumulative turnover, and the tightening MRV regime (digital platform, on-site inspections, anti-falsification rules under the 2024 Interim Regulations).
- 与本项目的相关性:The primary source to cite for market statistics and for the important caveat that researchers cannot observe firm-level verified emissions in the national ETS — a data constraint that shapes what empirical designs are feasible for the researcher's paper.
- 链接:https://www.mee.gov.cn/ywgz/ydqhbh/wsqtkz/202509/W020250927515319387445.pdf

**9. IEEFA (2025), China's emissions trading system (ETS) reforms: On track, but needs robust enforcement** — *IEEFA policy report*

- 问题:Assesses whether the announced 2027 absolute-cap and expansion reforms will bite.
- 数据:Report published 3 November 2025 (author name not verified from search results).
- 识别/方法:N/A (policy analysis of the Aug 2025 Opinions, allocation plans, and price data).
- 发现:Reforms are directionally on track (absolute caps and broader industrial coverage by 2027) but their effect hinges on enforcement instruments not yet specified: permit auctioning, a fixed cap-decline rate, and penalties; without them the surplus-and-low-price equilibrium persists.
- 与本项目的相关性:A citable critical assessment of the frontier reforms, useful for the paper's discussion of whether the announced 2027 shift should be expected to move prices; complements ICAP's neutral description.
- 链接:https://ieefa.org/resources/chinas-emissions-trading-system-ets-reforms-track-needs-robust-enforcement

**10. Mazzocco, Ilaria and Ray Cai (2026), The New Carbon Order: China's Response to Europe's CBAM** — *CSIS analysis*

- 问题:How is China responding, institutionally and commercially, to the EU CBAM?
- 数据:Published 15 June 2026; qualitative policy analysis drawing on Chinese policy documents and trade data.
- 识别/方法:N/A (policy analysis).
- 发现:Despite public 'protectionism' rhetoric, China's response is pragmatic: building compliance capacity, expanding the ETS (with chemicals, petrochemicals, aviation next) and moving toward absolute caps and paid permits by 2030 — partly CBAM-motivated. In early 2026 CBAM certificates cost about EUR 75/t while Chinese allowances remain largely free and around US$10-11/t, so Chinese exporters get minimal deduction for domestic carbon costs.
- 与本项目的相关性:Best current English-language analysis of the CBAM-China ETS interaction; supports the argument that external trade policy is now a driver of Chinese carbon-market design — a mechanism the paper can cite when discussing why stringency may rise post-2026.
- 链接:https://www.csis.org/analysis/new-carbon-order-chinas-response-europes-cbam

**11. European Union (2025), CBAM Omnibus Regulation (EU) 2025/2083 and the CBAM definitive regime (institutional facts relevant to Chinese exporters)** — *EU regulation; coverage via ICAP, EY tax alert, European Commission DG TAXUD*

- 问题:Fixes the timeline and simplifications under which Chinese exports of steel, aluminum and cement face EU border carbon costs.
- 数据:Omnibus adopted 8 October 2025, in force 20 October 2025. Definitive CBAM phase begins 1 January 2026; certificate sales start 1 February 2027 covering 2026 imports; first declaration/surrender by 30 September 2027; new 50 t/yr mass threshold exempts small importers. ENACTED (EU side).
- 识别/方法:N/A. CBAM allows deduction of a carbon price effectively paid in the country of origin; with China's largely free allocation and ~US$10-11/t prices, the deductible amount is small. Analyst estimates put the early-phase cost gap for Chinese steel and aluminum exporters at roughly RMB 2-2.8 billion per year; iron and steel account for ~92% of affected Chinese exports, aluminum ~7%. Extension to downstream steel/aluminum products proposed for around 2028 (proposed, not enacted).
- 发现:From 2026 the CBAM makes the CEA-EUA price gap a direct export cost for covered Chinese sectors, creating a measurable channel from EU policy to Chinese ETS stringency preferences.
- 与本项目的相关性:Provides the enacted-vs-proposed timeline the paper needs when discussing CBAM as a driver of Chinese carbon pricing; also defines a potential natural experiment (definitive regime start Jan 2026) inside the researcher's sample window.
- 链接:https://icapcarbonaction.com/en/news/eu-adopts-simplifications-cbam-rules-ahead-compliance-phase-starting-2026

**12. International Monetary Fund (2024), Reform of the Emissions Trading System (ETS) in China, in People's Republic of China: Selected Issues, IMF Country Report No. 24/276** — *IMF Staff Country Reports (Selected Issues Paper)*

- 问题:What are the macro/welfare effects of reforming China's intensity-based ETS via partial auctioning, a quantity-based cap, and industrial extension?
- 数据:Calibrated model of China's economy; published 30 August 2024.
- 识别/方法:Structural modeling: compares the current intensity-based ETS (IB-ETS) against three reforms — partial auctioning, quantity-based ETS (QB-ETS) with an absolute cap, and sectoral extension — tracking electricity prices, fiscal revenue and welfare.
- 发现:Moving to a quantity-based cap with auctioning raises effective carbon prices and fiscal revenue with modest welfare costs; the intensity design mutes the electricity-price signal. (Exact magnitudes should be pulled from the PDF before citing.)
- 与本项目的相关性:A credible official-sector quantitative benchmark for the announced 2027 intensity-to-cap transition; its electricity-price channel connects directly to the researcher's spot-market work.
- 链接:https://www.imf.org/en/publications/cr/issues/2024/08/29/peoples-republic-of-china-selected-issues-554232

**13. IEA and Tsinghua University (2024), Enhancing China's ETS for Carbon Neutrality: Introducing Auctioning — Lessons from International Experience** — *IEA report (joint with Tsinghua)*

- 问题:How could allowance auctioning be introduced into China's national ETS?
- 数据:Comparative institutional evidence from EU ETS, RGGI, California, Korea auction programs; companion to the 2022 IEA-Tsinghua report 'Enhancing China's ETS for Carbon Neutrality: Focus on Power Sector'.
- 识别/方法:N/A (comparative policy analysis; the 2022 companion uses power-system modeling with economic dispatch scenarios from 2025).
- 发现:Auctioning would strengthen price discovery and provide revenue; design elements (share auctioned, floors, revenue use) matter; written in response to a Chinese government invitation, so it maps closely to what MEE is likely to implement under the 2030 'free plus paid' milestone.
- 与本项目的相关性:The go-to citation for 'auctioning introduction plans' — currently announced (2024 Interim Regulations and Aug 2025 Opinions) but with no timeline; the 2022 power-sector companion is also the best institutional source on ETS-electricity-market coupling, directly relevant to Shandong dispatch.
- 链接:https://www.iea.org/reports/enhancing-chinas-ets-for-carbon-neutrality-introducing-auctioning

**14. Goulder, Lawrence H., Xianling Long, Jieyi Lu and Richard D. Morgenstern (2022), China's unconventional nationwide CO2 emissions trading system: Cost-effectiveness and distributional impacts** — *Journal of Environmental Economics and Management (vol. 111); earlier as NBER WP 26537 (2019)*

- 问题:How does China's tradable performance standard (TPS, intensity-based) compare to cap-and-trade in cost-effectiveness and distribution?
- 数据:Calibrated multi-sector general equilibrium model of China's power sector and economy.
- 识别/方法:Theory/simulation: models the TPS's output-based allocation as an implicit output subsidy and compares equilibrium outcomes with an equivalent-emissions cap-and-trade system.
- 发现:The implicit output subsidy makes the TPS roughly 47% more costly than cap-and-trade for the same emissions cut in the central case, and dampens electricity price increases; distributional effects differ sharply across generator types.
- 与本项目的相关性:The seminal economics framework for understanding why the 2027 intensity-to-absolute-cap shift matters: it predicts the current design subsidizes output and mutes pass-through into electricity prices — a first-order interaction with the researcher's Shandong spot-price analysis.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0095069621001133

**15. Goulder, Lawrence H., Xianling Long, Chenfei Qu and Da Zhang (2023), China's Nationwide CO2 Emissions Trading System: A General Equilibrium Assessment** — *NBER Working Paper 31809 (also RFF WP 24-02; SSRN)*

- 问题:What are the economy-wide impacts of China's TPS, accounting for SOEs and electricity-market regulation, across future design variants?
- 数据:Multi-sector, multi-period equilibrium model of China calibrated with distinctive features: state-owned enterprises, regulated electricity pricing, planned phase-in of industrial sectors (a later phase adds pulp & paper, other non-metals, non-ferrous metals, chemicals, refining, reaching ~67% of China's CO2).
- 识别/方法:Structural general-equilibrium simulation comparing TPS variants and cap-and-trade under different benchmark-tightening and auctioning paths.
- 发现:Climate benefits alone exceed costs by ~5x; electricity-market regulation and SOE behavior materially change TPS performance; results quantify how design choices on the announced reform path (benchmarks, caps, auctions) alter costs.
- 与本项目的相关性:The frontier structural model of the exact policy transition now underway; its treatment of regulated electricity pricing is the natural benchmark to contrast with Shandong's liberalized spot market, where carbon costs can actually enter marginal bids.
- 链接:https://www.nber.org/papers/w31809

**16. Zhang [and co-authors, Tsinghua team; full author list not verified] (2025), Options to enhance China's national emission trading system design for carbon neutrality** — *Climate Policy 25(2), 240-256 (online 9 July 2024)*

- 问题:Which ETS enhancements — faster benchmark tightening, auctions, or transition to cap-and-trade — best align power-sector emissions with the 2060 neutrality target?
- 数据:China power-system planning model with an output-based ETS module; scenarios through mid-century.
- 识别/方法:Structural power-system modeling comparing three enhancement options against the current output-based design.
- 发现:The current output-based design cannot deliver a neutrality-consistent trajectory on its own; combinations of tighter benchmarks, auctioning and an eventual absolute cap are required — closely prefiguring the Aug 2025 Opinions roadmap.
- 与本项目的相关性:Peer-reviewed engineering-economics support for the official reform sequence; useful to cite alongside Goulder et al. when motivating why the intensity design suppressed carbon price signals during the researcher's sample. Verify the full author list before citing (Tsinghua Institute of Climate Change / 3E group; PDF on jcglt.tsinghua.edu.cn).
- 链接:https://www.tandfonline.com/doi/full/10.1080/14693062.2024.2375586

**17. Wang, Baixue and Maosheng Duan (2025), Have China's emissions trading systems reduced carbon emissions? Firm-level evidence from the power sector** — *Applied Energy 378 (Part B), art. 124802*

- 问题:Did China's regional ETSs causally reduce power-sector firms' emissions and intensity?
- 数据:Verified firm-level carbon emissions data and annually updated lists of regulated entities from the regional pilot ETSs.
- 识别/方法:Event-study / difference-in-differences using heterogeneity-robust (new-generation DiD) estimators on regulated vs. unregulated power firms.
- 发现:ETSs substantially reduced emissions, mainly through reduced (coal-fired) generation rather than efficiency gains; effects concentrated where allowance shortages were large and prices high; 'rewards the good, punishes the bad' across technology levels; no evidence of leakage to neighboring provinces or within ownership networks.
- 与本项目的相关性:State-of-the-art causal evidence on Chinese carbon-market effectiveness using verified emissions — the empirical standard a new China carbon-market paper will be measured against; the finding that abatement operates through the generation margin ties carbon policy directly to dispatch outcomes of the kind the researcher observes in Shandong.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0306261924021858

**18. Lyu, Chen, Ke Wang, Bofeng Cai and Yujiao Xian (2026), Dual CO2 mitigations with diminishing margins: Evidence from China's intensity-based national emissions trading scheme** — *iScience 29(4), art. 115424*

- 问题:Has the national (not pilot) intensity-based ETS reduced emission intensity and total emissions at the generating-unit level, and are effects persisting?
- 数据:Balanced panel of 1,957 thermal power units, 2018-2024 (through the third compliance period).
- 识别/方法:Unit-level panel comparison of allowance-deficit vs. surplus units over successive compliance periods (quasi-experimental panel design; check exact estimator in the paper).
- 发现:Deficit units cut CO2 intensity by ~0.8% and total emissions by ~3.5%; reductions concentrated in small coal units, achieved via efficiency, higher heat-supply ratios and better fuel quality; year-on-year marginal improvements shrink over time (-0.41% to -0.01%) as the intensity distribution compresses — evidence the intensity design is running out of headroom, motivating the absolute-cap transition.
- 与本项目的相关性:The most direct early empirical evaluation of the national ETS itself over almost exactly the researcher's sample window (2018-2024, overlapping Dec 2021 - Aug 2026); its 'diminishing margins' result is an empirical rationale for the 2027 reform the paper must discuss.
- 链接:https://www.cell.com/iscience/fulltext/S2589-0042(26)00799-6

**19. [Authors not verified — likely Duan/Tsinghua group] (2025), Enterprise responses to China's national emissions trading system: evidence from a nationwide survey** — *Climate Policy (online first, 28 November 2025)*

- 问题:How do regulated enterprises actually behave under the national ETS — allocation, trading, banking, MRV, abatement?
- 数据:Nationwide enterprise survey of ETS-covered firms (first comprehensive ex-post survey evaluation of the national ETS).
- 识别/方法:Descriptive/survey analysis comparing allowance-deficit vs. allowance-surplus enterprises.
- 发现:Deficit and surplus firms differ sharply in trading strategy, economic performance and mitigation effort; the ETS measurably improved emissions-data accuracy and carbon-management capacity; but 85% of enterprises do not know their marginal abatement cost, limiting genuine market participation.
- 与本项目的相关性:Rare micro evidence on compliance-trading behavior (thin trading, compliance-deadline bunching) that any model of Chinese carbon-price formation should confront; the MAC-ignorance result is a striking friction to cite. Verify authors from the article page before citing.
- 链接:https://www.tandfonline.com/doi/full/10.1080/14693062.2025.2591879

**20. Yu [R.], Da Zhang, Kebin He [author list partially verified] (2026), A comparative review of compliance-linked carbon offset programs in China and California: The new CCER and the Compliance Offset Program** — *Advances in Climate Change Research (online March 2026)*

- 问题:How do the institutional architectures of China's relaunched CCER and California's Compliance Offset Program shape offset integrity?
- 数据:Comparative institutional review: methodologies, MRV infrastructure, liability rules, registry data for both programs.
- 识别/方法:Qualitative comparative-institutional analysis.
- 发现:China's priorities are scaling digital MRV, expanding CCER methodologies to new sectors, and strengthening supplier (project-owner/verifier) liability for data quality; California's are permanence gaps and baseline accuracy. Frames the CCER's narrow-methodology restart as an integrity-first design choice.
- 与本项目的相关性:The most current academic treatment of the CCER restart, including the offshore-wind additionality debate; the natural citation for the paper's offset-market subsection. Verify the exact author list on the article page before citing.
- 链接:https://www.sciencedirect.com/science/article/pii/S1674927826000717

### 本节检索笔记(agent 原始记录,含未列入正文的文献与核验警告)

> ENACTED vs ANNOUNCED ladder (the cheat sheet the paper needs): ENACTED — Interim Regulations (pub. 4 Feb 2024, in force 1 May 2024); CCER relaunch (trading 22 Jan 2024; 4 methodologies late 2023, 6 by Aug 2025); expansion to steel/cement/aluminum (work plan late March 2025; first compliance = 2024 emissions, surrender due end-Dec 2025); power-sector banking limits (2023-24 allocation plan, draft 2 July 2024) and industrial banking limits (allocation plan 16 Nov 2025: 100k + 150% of net sales); EU CBAM definitive phase from 1 Jan 2026 (Omnibus Reg. (EU) 2025/2083, adopted 8 Oct 2025; certificate sales from 1 Feb 2027). ANNOUNCED — Aug 25, 2025 CPC/State Council Opinions: absolute caps for stable-emission sectors 'from around 2027', all major industrial emitters covered by 2027, full cap-and-trade with mixed free/auctioned allocation by 2030; auctioning has NO enacted timeline; next sectors expected (aviation, copper smelting, flat glass, petrochemicals, chemicals, paper). PROPOSED/SPECULATED — CBAM extension to downstream steel/aluminum products (~2028); EU recognition of Chinese carbon prices hinging on absolute-cap architecture (asserted in commentary, not an EU legal determination — CBAM Art. 9 already allows deduction of carbon prices effectively paid, but free allocation must be netted out, so the deductible Chinese amount is currently tiny). PRICES: CEA all-time high RMB 104.5/t (Nov 2024, driven by the power-sector banking restriction), monthly average ~RMB 71/t (~US$10) Aug 2025; EUA ~EUR 75+/t — the gap is the CBAM exposure. DATA RESOURCES: MEE annual Progress Reports (2024 ed. July 2024; 2025 ed. Sept 2025) for official aggregates; ICAP factsheets for design parameters; CEA prices from Shanghai Environment and Energy Exchange, CCER from Beijing Green Exchange; firm-level verified emissions are NOT published (only entity lists + named data-fraud cases, e.g. March 2022), which constrains empirical designs — the strongest recent empirical papers use pilot-era verified data (Wang-Duan) or unit-level engineering panels (Lyu et al.). COVERAGE CAVEATS: several author lists could not be fully verified because ScienceDirect/T&F/IMF block automated fetching (flagged per-entry); the MEE work-plan release date appears as both 20 and 26 March 2025 in reputable coverage — check the Chinese original before citing a day. Additional sources seen but not listed: Carbon Brief explainer on the expansion (Anika Patel, 23 Sep 2024) and in-depth ETS Q&A (24 Jun 2021, partly dated); IETA China Business Brief (July 2025); Asia Society ETS Status: China; Energy Economics 2025 'The effectiveness of China's national ETS in mitigating firm emissions' (unit-level, authors unverified); Mei et al., 'Carbon markets promote environmental justice in China', Nature Communications 17 (2026) — old-CCER program (2000-2019) air-quality co-benefits; CBAM export-cost papers of mixed quality (Wang/Wen/Zhang, Global Energy Interconnection 8(2) 2025 — industry-affiliated authors; a provincial export-cost paper on PMC). DEBATES in this strand: (i) whether intensity-based design + free allocation makes current CEA prices nearly meaningless as marginal signals (Goulder et al. output-subsidy view; IMF and IEA-Tsinghua modeling agree) vs. evidence the ETS still cut emissions at the generation margin (Wang-Duan; Lyu et al. with diminishing returns); (ii) offshore-wind CCER additionality; (iii) whether 2027 absolute caps will bind without auctioning/enforcement (IEEFA skepticism). RELEVANCE HOOK for the researcher: the ETS covers power with output-based allocation, so carbon-cost pass-through into day-ahead/real-time bids in Shandong's spot market is theoretically muted but nonzero — the intensity-to-cap transition (2027) would sharpen the carbon component of coal units' marginal costs exactly where his price-spread analysis lives, and Shandong's heavy steel/aluminum/cement base makes the 2025 expansion locally binding.

## 第 6 节 中文文献

经研/管世/中工经/金融研究等中文期刊的碳市场论文。CNKI 在本环境不可直接检索,标注"未核验"的字段引用前请上 CNKI 自查页码。

**1. 吴力波、钱浩祺、汤维祺 (2014), 《基于动态边际减排成本模拟的碳排放权交易与碳税选择机制》** — *经济研究 (Economic Research Journal), 2014年第9期*

- 问题:In China's context, should carbon pricing take the form of an emissions trading market or a carbon tax, and under what conditions does each dominate?
- 数据:Simulated Chinese provincial/sectoral data; dynamic marginal abatement cost (MAC) curves calibrated to China's economy (pre-national-ETS period). Exact calibration details not verified from full text.
- 识别/方法:Structural simulation: builds dynamic MAC curves and compares welfare/cost outcomes of ETS vs carbon tax under uncertainty and heterogeneous regional abatement costs; not a quasi-experimental design.
- 发现:Establishes the canonical Chinese-language framework for the ETS-vs-carbon-tax instrument choice; shows that with heterogeneous and dynamic MACs, allowance trading achieves cost-effective abatement where a uniform tax does not, supporting the pilot-ETS route. (Findings summarized from citations, not full text.)
- 与本项目的相关性:The seminal 经济研究 paper legitimizing carbon markets in Chinese economics; the instrument-choice framing is the standard opening citation for any Chinese carbon-market paper. Fudan team (吴力波/钱浩祺) later wrote the allocation-mechanism 经济研究 papers below.

**2. 涂正革、谌仁俊 (2015), 《排污权交易机制在中国能否实现波特效应?》** — *经济研究 (Economic Research Journal), 50(7): 160-173*

- 问题:Did China's SO2 emissions-permit trading pilots generate a Porter effect (win-win of abatement and productivity/innovation)?
- 数据:Chinese industrial SO2 emissions trading pilot provinces, panel roughly 2002-2012 (province/industry level).
- 识别/方法:Difference-in-differences comparing SO2-trading pilot provinces to non-pilot provinces over the pilot period.
- 发现:The SO2 trading pilots neither delivered significant emission reductions nor produced a Porter effect — a prominent negative result showing that a permit market without real trading activity and enforcement fails.
- 与本项目的相关性:Not carbon, but THE methodological and rhetorical antecedent for all Chinese carbon-ETS DiD evaluations; its negative result frames the later debate about whether carbon-pilot 'effects' are market-driven or administrative (cf. 吴茵茵 et al. 2021). Useful benchmark when arguing markets need real price signals — same spirit as spot-market papers.
- 链接:https://zhuanlan.zhihu.com/p/364599607

**3. 王班班、齐绍洲 (2016), 《市场型和命令型政策工具的节能减排技术创新效应——基于中国工业行业专利数据的实证》** — *中国工业经济 (China Industrial Economics), 2016年第6期*

- 问题:Do market-based vs command-and-control energy/emission policy instruments differentially induce energy-saving technological innovation in Chinese industry?
- 数据:Chinese industrial sector panel: patent counts (energy-saving/emission-reduction classes), energy price indices, and measured policy-instrument intensity by industry.
- 识别/方法:Panel regressions exploiting cross-industry, cross-time variation in instrument intensity; distinguishes invention vs utility patents. Not a single-policy quasi-experiment.
- 发现:Market-based instruments work through price/spillover channels while command instruments act more directly, with stronger effects on invention patents; policy transmission is a precondition — market instruments are notably ineffective in the electricity sector, where prices were then regulated.
- 与本项目的相关性:Directly relevant intersection: documents that market-based environmental instruments fail to transmit in China's regulated power sector — exactly the friction Shandong's spot market is meant to remove; strong motivation citation for carbon-price pass-through in liberalized dispatch.
- 链接:https://cdw.cnki.net/kcms/detail/detail.aspx?filename=GGYY201606008&dbcode=&dbname=CJFDLAST2017&pcode=CRJT

**4. 汤维祺、吴力波、钱浩祺 (2016), 《从"污染天堂"到绿色增长——区域间高耗能产业转移的调控机制研究》** — *经济研究 (Economic Research Journal), 2016年第6期: 58-70*

- 问题:How do regional carbon-market/regulation designs govern the interregional relocation of energy-intensive industry — pollution-haven dynamics vs green growth?
- 数据:Multi-region simulation calibrated to Chinese provinces and energy-intensive sectors (details from citations; full text not independently verified).
- 识别/方法:Structural/simulation modeling of interregional industry transfer under differentiated carbon regulation, in the Fudan group's dynamic-MAC tradition.
- 发现:Differentiated regional carbon constraints can push energy-intensive industries toward laxer regions (pollution-haven), but appropriately designed interregional trading/coordination converts relocation pressure into green growth. (Summary based on title/abstract-level sources.)
- 与本项目的相关性:Chinese-language theory on regional heterogeneity under carbon constraints — background for why a national ETS with uniform benchmarks interacts differently with provinces like Shandong (coal-heavy, now spot-market pioneer).

**5. 刘晔、张训常 (2017), 《碳排放交易制度与企业研发创新——基于三重差分模型的实证研究》** — *经济科学 (Economic Science), 2017年第3期: 102-114*

- 问题:Did the carbon-ETS pilots raise R&D/innovation of regulated firms?
- 数据:Chinese listed firms around the 2013 pilot launches (pilot vs non-pilot regions, covered vs uncovered industries).
- 识别/方法:Triple difference (region x industry x time) around the ETS pilot rollout.
- 发现:One of the earliest firm-level DDD evaluations in Chinese; finds the pilots stimulated R&D of covered firms (effect heterogeneous across ownership). (Detail from PDF header and citing summaries.)
- 与本项目的相关性:Early template for the region-x-industry DDD design that virtually all Chinese ETS micro papers now use; useful methodological reference.
- 链接:https://ccj.pku.edu.cn/Article/DownLoad?id=214762980&type=ArticleFile

**6. 沈洪涛、黄楠、刘浪 (2017), 《碳排放权交易的微观效果及机制研究》** — *厦门大学学报(哲学社会科学版), 2017年第1期*

- 问题:Do firms covered by the carbon pilot ETS actually cut emissions, and through what micro mechanisms?
- 数据:Firm-level data from pilot ETS regions (covered vs uncovered firms), mid-2010s. Full data details not verified.
- 识别/方法:DiD-style comparison of covered vs uncovered firms before/after pilot launch.
- 发现:Covered firms reduce emissions; the incentive of selling surplus allowances (revenue channel) is a key mechanism inducing voluntary abatement.
- 与本项目的相关性:Part of the 沈洪涛 (Jinan Univ.) series that established the firm-level ETS evidence base in Chinese accounting/finance venues; the allowance-revenue mechanism parallels how generators in Shandong monetize flexibility in the spot market.

**7. 史丹、张成、周波、杨璐 (2017), 《碳排放权交易的实践效果及其影响因素：一个文献综述》** — *城市与环境研究 (Urban and Environmental Studies, CASS), 2017年第4期: 93-110*

- 问题:Survey: what does theory and international/Chinese evidence say about ETS effectiveness, ETS-vs-carbon-tax, and the factors conditioning ETS performance?
- 数据:Literature review (Coase/property-rights lineage, EU ETS and Chinese pilot evidence through 2017).
- 识别/方法:Narrative synthesis across four dimensions: theoretical development, ETS-vs-carbon-tax mechanism comparison, implementation effects, influencing factors.
- 发现:Systematizes the pre-national-ETS Chinese literature and lays out the research agenda (allocation rules, price formation, interaction with other policies) for the national market. Verified from full PDF.
- 与本项目的相关性:Best single Chinese-language entry point to the pre-2017 literature; useful for the paper's literature-review scaffolding and for locating the CASS industrial-economics view (史丹 is the leading CASS energy economist).
- 链接:https://rieco.ajcass.com/Admin/UploadFile/Issue/a3nmwovt.pdf

**8. 齐绍洲、林屾、崔静波 (2018), 《环境权益交易市场能否诱发绿色创新?——基于我国上市公司绿色专利数据的证据》** — *经济研究 (Economic Research Journal), 2018年第12期: 129-143*

- 问题:Do environmental-rights trading markets (emissions trading pilots) induce corporate green innovation?
- 数据:Green patent data of Shanghai/Shenzhen A-share listed firms (long panel referenced as 1990s-2010s) matched to emissions-trading pilot regions and polluting vs clean industries.
- 识别/方法:Triple difference: pilot vs non-pilot regions x polluting vs clean industries x before/after policy.
- 发现:Trading pilots induced green innovation in polluting industries of pilot regions, concentrated in green invention patents (not utility models) and stronger in non-SOEs.
- 与本项目的相关性:The flagship 经济研究 green-innovation result; 崔静波 (Cui Jingbo) later published closely related English work (e.g., carbon-pilot innovation papers), giving the researcher an English bridge for citation. Wuhan Univ. (齐绍洲) is the main academic hub for Chinese ETS research.
- 链接:http://qikan.cqvip.com/Qikan/Article/Detail?id=7001084686

**9. 沈洪涛、黄楠 (2019), 《碳排放权交易机制能提高企业价值吗》** — *财贸经济 (Finance & Trade Economics), 2019年第1期*

- 问题:Does inclusion in the carbon pilot ETS raise firm value?
- 数据:Chinese listed firms covered by pilot carbon markets vs comparable uncovered firms. Details beyond this not verified.
- 识别/方法:DiD around pilot-ETS coverage.
- 发现:Carbon-market participation raises firm value, consistent with the market-incentive (allowance-asset) channel rather than pure compliance-cost channel. (Summary from search-result abstracts.)
- 与本项目的相关性:Establishes the capital-market/firm-value side of the Chinese evidence; relevant if the researcher wants to argue carbon prices are material to generator valuation and bidding.

**10. 钱浩祺、吴力波、任飞州 (2019), 《从"鞭打快牛"到效率驱动：中国区域间碳排放权分配机制研究》** — *经济研究 (Economic Research Journal), 54(3): 86-102*

- 问题:How should interregional initial allocation of carbon allowances be designed — away from 'whipping the fast ox' (penalizing efficient regions via grandfathering/intensity conventions) toward efficiency-based allocation?
- 数据:Provincial emissions/output data calibrated into an allocation-mechanism model (details from citations; full text behind CNKI).
- 识别/方法:Mechanism-design / quantitative allocation modeling comparing administrative allocation rules with market-based (efficiency-driven) allocation.
- 发现:Administrative allocation rules distort effort across regions; efficiency-driven allocation with trading substantially lowers aggregate abatement cost and redistributes burden more fairly.
- 与本项目的相关性:The core 经济研究 treatment of 配额分配 (allowance allocation) — the exact policy-design debate (基准线法 benchmark vs grandfathering, free vs auctioned) the researcher's carbon-market paper must engage; also the intellectual background to the national ETS's intensity-based benchmarks for power plants.

**11. 胡珺、黄楠、沈洪涛 (2020), 《市场激励型环境规制可以推动企业技术创新吗?——基于中国碳排放权交易机制的自然实验》** — *金融研究 (Journal of Financial Research), 2020年第1期: 171-189*

- 问题:Does market-incentive environmental regulation (the carbon pilot ETS) push covered firms to innovate technologically?
- 数据:Chinese listed firms, pilot-ETS covered vs uncovered, pre/post 2013 pilot launches.
- 识别/方法:Natural-experiment DiD on ETS coverage; heterogeneity and mechanism tests (financing, incentives).
- 发现:Pilot ETS coverage significantly increases firm technological innovation, supporting the market-incentive-regulation channel in a top Chinese finance journal.
- 与本项目的相关性:The 金融研究 anchor for the strand; pairs with 齐绍洲 et al. (2018) as the standard 'pilot ETS caused innovation' citation block in Chinese papers.

**12. 张希良、张达、余润心 (2021), 《中国特色全国碳市场设计理论与实践》** — *管理世界 (Journal of Management World), 37(8): 80-95*

- 问题:What is the design logic of China's national carbon market — cap setting, allocation, tax-vs-market choice, efficiency vs political acceptability, and coordination with other policies?
- 数据:Policy design analysis drawing on the authors' modeling (Tsinghua 3E group C-GEM etc.) and their direct role in designing the national ETS; not an econometric paper.
- 识别/方法:Theory + design synthesis by the ETS's principal academic architects (Tsinghua Institute of Energy, Environment and Economy).
- 发现:Rationalizes the 'Chinese-characteristics' choices: intensity-based (rate-based) cap, free allocation via 基准线法 (benchmarking) in the power sector, gradual sectoral expansion, and coordination with power-sector reform; discusses when to move toward auctioning and absolute caps.
- 与本项目的相关性:THE authoritative Chinese statement of national-ETS design; indispensable institutional citation. Its discussion of ETS-power-market coordination directly frames how a carbon price does (or does not) reach dispatch in provinces like Shandong with spot markets.
- 链接:https://www.3e.tsinghua.edu.cn/cn/article/328

**13. 吴茵茵、齐杰、鲜琴、陈建东 (2021), 《中国碳市场的碳减排效应研究——基于市场机制与行政干预的协同作用视角》** — *中国工业经济 (China Industrial Economics), 2021年第8期: 114-132*

- 问题:Did China's pilot carbon markets reduce CO2, and how much of the effect came from genuine market mechanisms vs administrative intervention?
- 数据:City/province-level CO2 emissions panel covering pilot vs non-pilot regions through the late 2010s (exact span not verified).
- 识别/方法:DiD on pilot regions with decomposition of channels into market-mechanism intensity (trading activity, carbon price) vs administrative-intervention measures.
- 发现:Pilot carbon markets reduced emissions, but a substantial part of the reduction operated through administrative intervention synergizing with (or substituting for) weak market mechanisms — a widely cited caution against reading pilot DiDs as pure carbon-price effects.
- 与本项目的相关性:Central to the interpretation debate the researcher's paper will face: with thin trading and low prices, 'ETS effects' may be administrative. Analogous to disentangling market-design effects from dispatch orders in Shandong's electricity market.
- 链接:http://rdbk1.ynlib.cn:6251/Qw/Paper/777724

**14. 董直庆、王辉 (2021), 《市场型环境规制政策有效性检验——来自碳排放权交易政策视角的经验证据》** — *统计研究 (Statistical Research), 38(10): 48-61 (journal/issue per search results; not confirmed on journal site)*

- 问题:Is market-based environmental regulation (carbon ETS pilots) effective at reducing emissions/improving green outcomes?
- 数据:Chinese regional/firm panel around the ETS pilots (details not verified beyond citing sources).
- 识别/方法:Quasi-experimental DiD on pilot ETS implementation.
- 发现:Reported by citing literature as confirming effectiveness of the market-based instrument with heterogeneity across regions/firms. Verification thin — include only after checking CNKI.
- 与本项目的相关性:Representative of the 统计研究/数量经济技术经济研究 tier of policy-evaluation work; a checkable secondary citation for pilot effectiveness.

**15. 庞韬、周丽、段茂盛 (2014), 《我国碳排放权交易试点体系的连接可行性分析》** — *中国人口·资源与环境 (China Population, Resources and Environment), 24(9): 6-12*

- 问题:Can China's seven regional ETS pilots be linked into one market — what design heterogeneities (coverage, allocation, MRV, price levels) block linkage?
- 数据:Comparative institutional data on the seven pilot ETSs (Beijing, Tianjin, Shanghai, Chongqing, Guangdong, Hubei, Shenzhen).
- 识别/方法:Comparative institutional/feasibility analysis (no econometrics); by the Tsinghua team (段茂盛) that co-designed the national ETS.
- 发现:Pilot design heterogeneity (caps, allocation rules, offsets, MRV) makes direct linkage costly; harmonization priorities identified — analysis that prefigured the centralized national-market design chosen in 2021.
- 与本项目的相关性:Institutional bridge from pilots to the national market; useful for the paper's background section on why the national ETS uses uniform national benchmarks rather than linked heterogeneous markets.

**16. 唐葆君、李茹、王翔宇、邹文静、许沛昀、王崇州、刘一江、霍慧娟、徐丹 (2023), 《中国碳市场与电力市场联动机制与协同效应》** — *北京理工大学学报(社会科学版) (Journal of BIT, Social Sciences), 25(6): 25-33*

- 问题:How do China's carbon market and electricity market interact (电碳联动), and what are the joint price/structure dynamics under different market-development scenarios?
- 数据:National carbon market (CEA) and power-sector data 2021 onward, calibrated into a system-dynamics model; scenario horizon to 2030.
- 识别/方法:System-dynamics simulation of the coupled carbon-electricity market system; scenario analysis, not causal econometrics.
- 发现:Carbon prices follow 'low early, fast rise later' — projected 118-200 yuan/t by 2030; electricity prices initially insulated from carbon costs but later rise to ~0.50-0.65 yuan/kWh as carbon costs pass through; carbon market accelerates exit of high-carbon units, wind+solar reaching ~29-33% by 2030. Recommends putting carbon cost into benchmark electricity price formation and letting price signals flow between the two markets.
- 与本项目的相关性:The most directly relevant Chinese econ-journal treatment of 电碳协同: it formalizes the carbon-to-electricity price pass-through channel that only exists where spot markets (like Shandong's) let marginal costs set prices. Prime citation for the carbon-electricity coupling section.
- 链接:https://journal.bit.edu.cn/sk/cn/article/doi/10.15918/j.jbitss1009-3370.2023.1795?viewType=HTML

**17. 曹洪坚、易宇灵风、蒋建刚 (2024) [author names transliterated from journal page as Cao Hongjian, Yi Yulingfeng, Jiang Jiangang — verify on CNKI], 《碳市场绿色创新的动力机制：产权界定还是市场交易？》** — *财经研究 (Journal of Finance and Economics, SUFE), 50(7): 80-94*

- 问题:Is the green-innovation effect of China's carbon markets driven by the initial definition/allocation of emission property rights or by subsequent market trading?
- 数据:Chinese firms across pilot carbon-market rollouts (staggered adoption), green-innovation outcomes.
- 识别/方法:Staggered DiD across pilot carbon markets as quasi-natural experiments, decomposing property-rights-definition vs market-trading channels.
- 发现:Carbon markets spur green innovation, but the initial property-rights definition contributes more than market trading; high transaction costs blunt reallocation gains, and very high carbon prices can weaken incentives.
- 与本项目的相关性:2024 frontier on the Coasean decomposition — speaks directly to whether China's low-liquidity markets work through prices at all, the same 'does the market mechanism bind' question as in Shandong's spot market.
- 链接:https://qks.shufe.edu.cn/J/CJYJ/Article/Details/A0hoG4ARkE-gdZb-EpU8-0Yhk-0n9RC5OxqQnl/CN

**18. 王科、吕晨 (2025), 《全球和中国碳市场回顾与展望(2025)》 (annual series, editions 2022-2026)** — *北京理工大学学报(社会科学版), 27(2): 19-36*

- 问题:Annual state-of-the-market review: national CEA market prices, volumes, compliance, sectoral expansion, CCER restart, and international comparison.
- 数据:National carbon market transaction data (e.g., 2023: 212 Mt traded, average 68.15 yuan/t, +23% vs 2022; price first broke 100 yuan/t in April 2024; cumulative 630 Mt / 43 bn yuan by end-2024), pilot-market data, EU ETS comparators.
- 识别/方法:Descriptive market-monitoring analysis with scenario outlooks (BIT CEEP annual report series led by 王科 Wang Ke).
- 发现:Documents thin-but-rising liquidity, compliance-period trading concentration, the 2024 shift to annual compliance and allowance-banking rules, and sector expansion (steel/cement/aluminum from 2024-2025).
- 与本项目的相关性:Best recurring Chinese-language source for CEA price/volume facts the researcher will need for descriptive sections; the series (2022, 2023, 2024, 2025, 2026 editions) provides a citable time line matching his Dec 2021 - Aug 2026 sample almost exactly.
- 链接:https://journal.bit.edu.cn/sk/article/doi/10.15918/j.jbitss1009-3370.2025.7132

**19. 肖祖沔、刘晓源、戴安然、向丽锦 (2025), 《碳交易与企业数字创新——基于全国碳交易市场启动的准自然实验》** — *财经研究 (Journal of Finance and Economics, SUFE), 51(12): 32-46 (per journal page; DOI 10.16538/j.cnki.jfe.20251119.201)*

- 问题:Did the July 2021 launch of the NATIONAL carbon market (covering power generators) change covered firms' digital-innovation behavior?
- 数据:A-share listed firms in high-carbon industries, 2017-2023; treatment = power-generation firms entering the national CEA market, control = other high-carbon firms.
- 识别/方法:DiD around the 2021 national-market launch (first wave of Chinese papers using the national ETS itself, not the pilots, as the experiment).
- 发现:National-market coverage significantly raised digital-innovation capacity of regulated power firms, via carbon-disclosure quality, technology integration, and R&D expansion.
- 与本项目的相关性:Frontier exemplar of the post-2021 shift from pilot-DiD to national-ETS-DiD designs with power generators as the treated group — the same firms bidding into Shandong's spot market; shows the identification template and its limits (all generators treated, no within-sector control).
- 链接:https://qks.sufe.edu.cn/J/CJYJ/Article/Details/A7nLzq4iB-JsGx-rEwO-cV3P-mK8Y0fD5HaN1/CN

### 本节检索笔记(agent 原始记录,含未列入正文的文献与核验警告)

> SCOPE/COVERAGE CAVEATS: (1) Session-wide WebSearch budget was exhausted near the end of this sweep, so two planned holes remain unfilled: no verified carbon-ETS paper from 经济学(季刊) or 《世界经济》 was located (repeated searches surfaced none — plausibly a genuine thinness of the strand in those two venues, but treat as unconfirmed), and 金融研究 coverage rests on 胡珺 et al. (2020) alone. (2) CNKI itself is paywalled/not directly searchable from this environment; metadata were verified via journal-society pages (SUFE 财经研究, BIT 学报), institution pages (Tsinghua 3E, Fudan, CASS), and full PDFs where available (史丹 et al. review read in full). Fields marked 'not verified' should be checked on CNKI before citing page numbers. (3) Two entries carry explicit uncertainty flags: 董直庆、王辉 (2021) journal attribution (统计研究 per search snippets), and the 2024 财经研究 author names (transliteration from the journal page may be garbled). DATASETS DISCOVERED: MEE 《全国碳市场发展报告(2024)》(https://www.mee.gov.cn/ywdt/xwfb/202407/W020240722528848347594.pdf) — official CEA market statistics; BIT-CEEP annual 碳市场回顾与展望 reports (ceep.bit.edu.cn) with CEA/pilot price-volume series; 《中国碳排放权交易市场报告(2023~2024)》 blue book edited at 山东财经大学中国国际低碳学院 — noteworthy given the researcher's Shandong focus. KEY DEBATES IN THE STRAND: (a) instrument choice 碳税 vs 碳市场 (吴力波 et al. 2014; 张希良 et al. 2021); (b) 配额分配 design — grandfathering vs 基准线法 benchmarking vs auction, intensity vs absolute cap ('鞭打快牛' problem, 钱浩祺 et al. 2019; 张希良 et al. 2021 defend the intensity/benchmark choice as transitional); (c) whether pilot 'effects' are market-driven or administrative (吴茵茵 et al. 2021 decomposition; 涂正革/谌仁俊 2015 negative SO2 antecedent; 曹洪坚? et al. 2024 property-rights-vs-trading decomposition); (d) 电碳协同/耦合 — mostly in engineering/energy venues (中国电机工程学报, 电力系统自动化, 浙江电力; review: 戴思婷 et al. 2025 《碳电市场耦合机制研究综述》 in 南方能源建设), with 唐葆君 et al. 2023 the best econ-journal treatment; recurring policy conclusion is that regulated tariffs block carbon-cost pass-through, so carbon prices only reach dispatch via spot markets — a direct hook for the researcher's Shandong work. ENGLISH BRIDGES for the same authors: 崔静波/Cui Jingbo (pilot ETS and innovation, English publications incl. high-profile general-science outlets), 张达/张希良 (English national-ETS design and power-sector papers), 张中祥/Zhang ZhongXiang (national-vs-local carbon market coordination, e.g. inaugural Journal of Climate Finance article, seen at https://mysoe.tju.edu.cn/info/1380/3634.htm). Post-2021 frontier is visibly shifting from pilot-DiD to national-ETS-launch quasi-experiments with power generators as treated units (肖祖沔 et al. 2025 is the verified exemplar). One structured-output note: two stray empty keys accidentally included inside two paper objects ("is a widely cited cautionary antecedent", "findings_verified") are artifacts — ignore them.

## 第 7 节 查漏补充(第二轮审查新增的必引文献)

一个独立的"查漏"agent 对上述六节的合并书目做了完备性审查(经由 Crossref API 核验存在性),补上了审稿人必然会点名的缺口:排放权市场理论基础、支持强度型设计的理论一侧、发展中国家污染市场实验等。本节末尾笔记含对全书目的纠错清单。

**1. Greenstone, Pande, Ryan, Sudarshan (2025), Can Pollution Markets Work in Developing Countries? Experimental Evidence from India** — *Quarterly Journal of Economics 140(2): 1003-1060*

- 问题:Can a cap-and-trade market for particulate emissions outperform command-and-control regulation in a developing country with weak enforcement institutions?
- 数据:RCT among coal-using industrial plants in Surat, Gujarat, with newly installed continuous emissions monitoring systems (CEMS), circa 2019-2021
- 识别/方法:Randomized controlled trial: plants randomly assigned to a particulate emissions trading market vs. status-quo command-and-control
- 发现:The emissions market reduced particulate emissions substantially (on the order of 20-30 percent) relative to command-and-control, with near-complete permit compliance and lower abatement costs. (Existence/venue/pages verified via Crossref, DOI 10.1093/qje/qjaf009; exact magnitudes recalled from the abstract - re-check before quoting.)
- 与本项目的相关性:The frontier reference on whether emissions markets work outside rich-country institutions - the closest experimental analog to the question China's ETS poses. A referee will flag its absence from any 2026 China carbon market paper; it also anchors the MRV/monitoring-quality theme (CEMS-based compliance) that runs through the CN-ETS unit-level literature.
- 链接:https://doi.org/10.1093/qje/qjaf009

**2. Duflo, Greenstone, Pande, Ryan (2013), Truth-telling by Third-party Auditors and the Response of Polluting Firms: Experimental Evidence from India** — *Quarterly Journal of Economics 128(4): 1499-1545*

- 问题:Does restructuring third-party environmental auditors' incentives (random assignment, central payment, backchecks) induce truthful pollution reporting and abatement?
- 数据:Two-year field experiment with industrial plants and environmental auditors in Gujarat, India
- 识别/方法:RCT altering the auditor market: treatment auditors randomly assigned to plants, paid from a central pool, and backchecked
- 发现:Treatment auditors reported far more truthfully (fewer false readings just below regulatory thresholds) and treated plants reduced emissions - showing conflicted verifier incentives corrupt reporting and that fixing them changes firm behavior.
- 与本项目的相关性:The canonical verification-design paper for the MRV integrity strand the bibliography already opens with Zhang et al. (NCC 2019) and the March 2022 CN-ETS data-fraud cases; China's verified-emissions system uses third-party verifiers with exactly the conflicted incentive structure this paper studies.
- 链接:https://doi.org/10.1093/qje/qjt024

**3. Fowlie, Holland, Mansur (2012), What Do Emissions Markets Deliver and to Whom? Evidence from Southern California's NOx Trading Program** — *American Economic Review 102(2): 965-993*

- 问题:Did the RECLAIM NOx trading program reduce emissions relative to command-and-control, and were reductions distributed unevenly across demographic groups?
- 数据:Facility-level NOx emissions for RECLAIM participants and matched comparison facilities in other California air districts under command-and-control
- 识别/方法:Matched difference-in-differences comparing RECLAIM facilities to observably similar non-RECLAIM facilities
- 发现:RECLAIM facilities cut NOx emissions by roughly 20 percent relative to matched controls; no evidence that trading shifted the pollution burden toward high-minority or poor neighborhoods.
- 与本项目的相关性:The canonical quasi-experimental evaluation of a cap-and-trade program and the direct methodological template for the China pilot DiD papers (Cui et al., Wang-Duan) already listed; the ets-classics strand's own notes flagged this as an unverified gap - now verified. Its spatial-equity analysis also pairs with the emerging China environmental-justice work (Mei et al. 2026).
- 链接:https://www.aeaweb.org/articles?id=10.1257/aer.102.2.965

**4. Carlson, Burtraw, Cropper, Palmer (2000), Sulfur Dioxide Control by Electric Utilities: What Are the Gains from Trade?** — *Journal of Political Economy 108(6): 1292-1326*

- 问题:How large were the realized and potential cost savings from allowance trading in the US Acid Rain Program relative to command-and-control?
- 数据:Unit-level data on fuel choices, costs, and SO2 emissions for US coal-fired generating units, 1985-1998
- 识别/方法:Econometric estimation of marginal abatement cost functions from fuel-switching behavior, then simulation of least-cost allocation vs. uniform standards
- 发现:Potential long-run gains from trade around $700-800 million per year, but realized savings in the program's early years fell well short of the least-cost benchmark because allowance prices diverged from marginal abatement costs.
- 与本项目的相关性:The original template for estimating power-sector marginal abatement costs econometrically - exactly what a unit-level CN-ETS paper (Qian et al., Lyu et al. style) implicitly emulates, and the benchmark for asking whether CEA prices bear any relation to marginal abatement cost in Chinese coal units.
- 链接:https://doi.org/10.1086/317681

**5. Montgomery (1972), Markets in Licenses and Efficient Pollution Control Programs** — *Journal of Economic Theory 5(3): 395-418*

- 问题:Can a competitive market in pollution licenses achieve the cost-minimizing allocation of abatement regardless of the initial allocation of licenses?
- 数据:Theory - no data
- 识别/方法:General-equilibrium existence and efficiency proofs for markets in emission licenses
- 发现:A competitive permit market attains the least-cost abatement allocation for any initial distribution of permits - the theoretical foundation of cap-and-trade and of the independence property.
- 与本项目的相关性:The foundational citation for the entire review; its independence-property result is what Zaklan (2023, already listed) tests for the EU and what SOE-dominated, compliance-only CEA trading plausibly violates - the natural framing for why CN-ETS allocation details (benchmarks, pre-allocation) matter for outcomes.
- 链接:https://doi.org/10.1016/0022-0531(72)90049-X

**6. Weitzman (1974), Prices vs. Quantities** — *Review of Economic Studies 41(4): 477-491*

- 问题:When regulating under uncertainty about costs, should the planner fix a price (tax) or a quantity (cap)?
- 数据:Theory - no data
- 识别/方法:Comparative-statics welfare analysis under uncertainty; relative slopes of marginal benefit and marginal cost curves determine the preferred instrument
- 发现:Quantity instruments dominate when marginal benefits are steep relative to marginal costs, and vice versa - the organizing result behind carbon taxes vs. caps, price collars, and hybrid designs.
- 与本项目的相关性:Referee-expected foundation for every design discussion the bibliography already contains: Borenstein et al.'s price-collar result, Karp-Traeger's Smart Cap, Pizer-Zhang on China's instrument choice, and the intensity-vs-absolute-cap transition planned for 2027 all descend from this paper.
- 链接:https://doi.org/10.2307/2296698

**7. Hahn (1984), Market Power and Transferable Property Rights** — *Quarterly Journal of Economics 99(4): 753-765*

- 问题:How does a dominant firm distort a tradable permit market, and how does the distortion depend on its initial allocation?
- 数据:Theory - no data
- 识别/方法:Dominant-firm/competitive-fringe model of a permit market
- 发现:With market power the equilibrium is efficient only if the dominant firm's initial allocation equals its cost-effective holdings; otherwise it manipulates the permit price and the independence property fails.
- 与本项目的相关性:Directly on point for China: CEA trading is confined to compliance entities dominated by five-plus central SOE generation groups, so Hahn's initial-allocation-dependence is the right theory for thin, concentrated CEA price formation - a gap in the carbon-price-formation strand, which has no market-power reference.
- 链接:https://doi.org/10.2307/1883124

**8. Rubin (1996), A Model of Intertemporal Emission Trading, Banking, and Borrowing** — *Journal of Environmental Economics and Management 31(3): 269-286*

- 问题:How do banking and borrowing provisions affect the equilibrium time path of emissions and permit prices?
- 数据:Theory - no data
- 识别/方法:Continuous-time optimal-control model of firms trading, banking, and borrowing permits
- 发现:With unrestricted banking and borrowing, permit prices rise at the rate of interest and firms equalize discounted marginal abatement costs over time; restrictions on borrowing raise aggregate costs and tilt abatement toward the present.
- 与本项目的相关性:The canonical banking theory behind the Alberola-Chevallier and Ellerman-Montero empirics already listed - and the right lens for China's 2024-25 allowance carry-over restrictions (power-sector banking limits; industrial limit of 100k + 150 percent of net sales), which the frontier strand documents institutionally but without the theory.
- 链接:https://doi.org/10.1006/jeem.1996.0044

**9. Pizer (2002), Combining Price and Quantity Controls to Mitigate Global Climate Change** — *Journal of Public Economics 85(3): 409-434*

- 问题:Do hybrid instruments (a cap with a price ceiling/safety valve) outperform pure price or pure quantity regulation for climate policy?
- 数据:Simulation using a stochastic integrated assessment model calibrated to global emissions and abatement costs
- 识别/方法:Welfare comparison of taxes, caps, and hybrid policies under cost uncertainty in a calibrated model
- 发现:A hybrid policy (quantity target plus safety-valve price) captures nearly all the efficiency advantage of a tax while retaining quantity features; pure caps perform worst under cost uncertainty.
- 与本项目的相关性:The applied bridge from Weitzman to modern ETS price-containment design; relevant to whether China's quasi-administered CEA price band and the planned 2027-2030 cap-with-auction architecture should include explicit price collars - a live design question the frontier strand raises without this reference.
- 链接:https://doi.org/10.1016/S0047-2727(01)00118-9

**10. Newell, Pizer (2008), Indexed Regulation** — *Journal of Environmental Economics and Management 56(3): 221-233*

- 问题:When is it optimal to index the stringency of a quantity regulation to an observable like output or GDP rather than fix it in absolute terms?
- 数据:Theory - no data
- 识别/方法:Extension of the Weitzman prices-vs-quantities framework to indexed (intensity-type) instruments under correlated uncertainty
- 发现:Indexed quantity regulation dominates a fixed cap when the index (e.g., output) is strongly positively correlated with unregulated emissions and marginal costs; the optimal degree of indexation is generally partial.
- 与本项目的相关性:China's national ETS is precisely an indexed regulation. The bibliography contains only the anti-TPS line (Fischer 2001; HHK 2009; Goulder et al.) - the output-subsidy critique - but not the uncertainty-based welfare case FOR intensity indexing. A referee will demand both sides of the intensity-vs-cap argument, especially for a paper spanning the 2027 transition to absolute caps.
- 链接:https://doi.org/10.1016/j.jeem.2008.07.001

**11. Fischer, Springborn (2011), Emissions targets and the real business cycle: Intensity targets versus caps or taxes** — *Journal of Environmental Economics and Management 62(3): 352-366*

- 问题:How do caps, taxes, and intensity targets compare in a dynamic stochastic economy subject to productivity shocks?
- 数据:Calibrated real-business-cycle (DSGE) model with an emissions externality
- 识别/方法:Welfare and volatility comparison of policy instruments in an RBC model under technology shocks
- 发现:An intensity target accommodates business-cycle fluctuations, avoiding the procyclical cost spikes of a fixed cap; for equal expected emissions it delivers higher expected welfare than a cap, while a cap dampens output volatility.
- 与本项目的相关性:The standard macro defense of China's intensity-based design (cited in exactly that role by the Goulder-Morgenstern line); needed to frame why China chose intensity targets during a high-growth era and what is given up in the 2027 move to absolute caps.
- 链接:https://doi.org/10.1016/j.jeem.2011.04.005

**12. Jotzo, Pezzey (2007), Optimal intensity targets for greenhouse gas emissions trading under uncertainty** — *Environmental and Resource Economics 38(2): 259-284*

- 问题:What degree of indexation of national emissions targets to GDP maximizes expected welfare in international emissions trading under uncertainty?
- 数据:Stochastic simulation model calibrated to national emissions and GDP uncertainty for major countries
- 识别/方法:Analytical and numerical optimization of the indexation parameter in an international permit-trading model
- 发现:Optimal targets are partially indexed to GDP; indexation raises expected welfare most for developing countries with high business-as-usual emissions uncertainty - a direct rationale for intensity targets in countries like China.
- 与本项目的相关性:With Newell-Pizer and Fischer-Springborn, completes the missing pro-intensity theory sub-strand; explicitly developed with developing-country (China-type) BAU uncertainty in mind, so it is the most China-relevant of the three.
- 链接:https://doi.org/10.1007/s10640-006-9078-z

**13. Bushnell, Holland, Hughes, Knittel (2017), Strategic Policy Choice in State-Level Regulation: The EPA's Clean Power Plan** — *American Economic Journal: Economic Policy 9(2): 57-90*

- 问题:How do rate-based versus mass-based carbon standards for the electricity sector differ in outcomes, and which will jurisdictions strategically choose?
- 数据:Calibrated simulation model of US regional electricity markets under the Clean Power Plan's rate and mass options
- 识别/方法:Theoretical and computational comparison of rate vs. mass standards in interconnected electricity markets with strategic state policy choice
- 发现:Rate-based standards act as an implicit output subsidy, raising generation and leakage; individually rational states choose rate-based standards even when mass-based is collectively efficient, and mixed rate/mass equilibria are the least efficient.
- 与本项目的相关性:The US electricity-sector analog of China's tradable performance standard - same output-subsidy mechanics as Goulder et al. but set inside wholesale electricity markets with cross-border trade, which is exactly the setting of provincial spot markets (Shandong) trading with regulated neighbors. Fills the rate-vs-mass electricity sub-strand missing between the ets-classics and carbon-electricity lists.
- 链接:https://www.aeaweb.org/articles?id=10.1257/pol.20150237

**14. Zhang, Wang, Du (2017), Lessons Learned from China's Regional Carbon Market Pilots** — *Economics of Energy & Environmental Policy 6(2)*

- 问题:What do the design features and early performance of China's seven regional ETS pilots imply for the national carbon market?
- 数据:Institutional and market data from the seven pilot ETSs (coverage, allocation rules, prices, volumes, compliance), roughly 2013-2016
- 识别/方法:Comparative institutional analysis; descriptive statistics on prices, liquidity, and compliance across pilots
- 发现:Pilots achieved high compliance but thin, compliance-clustered trading with prices too low and volatile to drive abatement; allocation generosity and ad hoc government adjustment emerge as central design risks for the national ETS.
- 与本项目的相关性:The standard English-language institutional reference on the pilots (Junjie Zhang is also senior author of the Cui et al. causal papers already listed) - it belongs in the same EEEP 6(2) special issue the bibliography cites for Teng-Jotzo-Wang and Karplus-Zhang. NOTE: often miscited to Review of Environmental Economics and Policy; Crossref confirms EEEP, DOI 10.5547/2160-5890.6.2.jzha.
- 链接:https://doi.org/10.5547/2160-5890.6.2.jzha

**15. Munnings, Morgenstern, Wang, Liu (2016), Assessing the design of three carbon trading pilots in China** — *Energy Policy 96: 688-699*

- 问题:How well designed are the Guangdong, Shanghai, and Shenzhen ETS pilots relative to best practice, and what challenges do they reveal?
- 数据:Program documents plus interviews with regulators and market participants in three pilots, circa 2013-2015
- 识别/方法:Qualitative institutional assessment against emissions-trading design criteria
- 发现:Pilots show workable MRV and compliance but suffer from ex post allowance adjustments, weak legal foundations, government price management, and limited liquidity - features later inherited by the national ETS.
- 与本项目的相关性:The earliest careful English design assessment of the pilots and the institutional root of the RFF/Goulder-Morgenstern line the bibliography leans on; documents the administrative-intervention DNA that the Chinese-language strand (Wu Yinyin et al. 2021) later quantifies.
- 链接:https://doi.org/10.1016/j.enpol.2016.06.015

**16. Zhang ZhongXiang (2015), Carbon emissions trading in China: the evolution from pilots to a nationwide scheme** — *Climate Policy 15(sup1): S104-S126*

- 问题:How did China's carbon trading policy evolve from regional pilots toward a national scheme, and what design and governance obstacles stand in the way?
- 数据:Policy documents and pilot market data through 2015
- 识别/方法:Institutional and policy analysis
- 发现:Identifies the core transition problems - legal basis, allocation, MRV capacity, interaction with electricity price regulation, and central-local coordination - most of which materialized in the national ETS's first cycles.
- 与本项目的相关性:Probably the most-cited single China-carbon-market article; the Chinese-language strand names Zhang ZhongXiang as the key English bridge author but lists none of his work. Cheap, obvious fix a referee (particularly a Chinese one) would demand.
- 链接:https://doi.org/10.1080/14693062.2015.1096231

**17. Zhang, Wang (2011), Co-benefits and additionality of the clean development mechanism: An empirical analysis** — *Journal of Environmental Economics and Management 62(2): 140-154*

- 问题:Were China's CDM projects additional, and did they generate local air-quality co-benefits?
- 数据:Project-level data on Chinese CDM projects (the world's largest CDM portfolio) with comparable non-CDM investments, 2000s
- 识别/方法:Empirical comparison of CDM and non-CDM projects to assess additionality and estimate co-benefits (detailed design not re-verified this session)
- 发现:Finds evidence consistent with limited additionality for a substantial share of Chinese CDM projects while quantifying local pollution co-benefits. (Existence/venue/pages verified via Crossref, DOI 10.1016/j.jeem.2011.03.003; direction of findings recalled - re-check before quoting.)
- 与本项目的相关性:The peer-reviewed antecedent to the CCER additionality debate the frontier strand flags (offshore-wind CCER additionality) - China's offset-market question has a 15-year-old JEEM answer the bibliography omits entirely. Junjie Zhang links this to the Cui et al. pilot papers.
- 链接:https://doi.org/10.1016/j.jeem.2011.03.003

**18. Cao, Ho, Jorgenson, Nielsen (2019), China's emissions trading system and an ETS-carbon tax hybrid** — *Energy Economics 81: 741-753*

- 问题:What are the economy-wide effects of China's electricity-sector ETS, and would supplementing it with a carbon tax on non-covered sectors improve outcomes?
- 数据:Multi-sector computable general equilibrium model of the Chinese economy calibrated to national accounts and energy data
- 识别/方法:CGE simulation of ETS-only vs. ETS-plus-carbon-tax hybrid policies
- 发现:An electricity-only ETS achieves limited coverage of national emissions at modest cost; a hybrid adding a carbon tax on non-ETS sectors reaches national targets with small GDP effects and better cost-effectiveness.
- 与本项目的相关性:The English-language instrument-choice anchor pairing with Wu Libo et al. (2014, Economic Research Journal) in the Chinese strand, and the same Cao-Ho team as the JPubE 2021 paper the bibliography leans on - it is the ex ante companion to that ex post evaluation.
- 链接:https://doi.org/10.1016/j.eneco.2019.04.029

**19. Karplus, Zhang, Almond (2018), Quantifying coal power plant responses to tighter SO2 emissions standards in China** — *Proceedings of the National Academy of Sciences 115(27): 7004-7009*

- 问题:Did Chinese coal plants actually reduce SO2 concentrations in response to the tighter 2014 standards, or did reported (CEMS) data overstate compliance?
- 数据:Hourly/daily CEMS SO2 concentration data for Chinese coal power plants around the January 2014 standard tightening, matched to satellite observations
- 识别/方法:Difference-in-differences around the policy deadline across plants facing different standard tightness ('key' vs. non-key regions); bunching/discontinuity diagnostics for misreporting
- 发现:Reported concentrations fell overall, but plants facing the tightest new standards show implausible distributional shifts in reported data consistent with misreporting; satellite data corroborate smaller true improvements in key regions.
- 与本项目的相关性:The core evidence on the credibility of Chinese power-plant monitoring data - the foundation beneath every CEMS/unit-level CN-ETS evaluation the bibliography lists (Qian et al., Qin et al., Lyu et al.) and the natural companion to Zhang et al. (NCC 2019) on reported-vs-verified emissions. Also directly relevant to trusting Shandong generator-level data.
- 链接:https://doi.org/10.1073/pnas.1800605115

**20. Hernandez-Cortes, Meng (2023), Do environmental markets cause environmental injustice? Evidence from California's carbon market** — *Journal of Public Economics 217: 104786*

- 问题:Did California's cap-and-trade program widen or narrow the pollution-exposure gap between disadvantaged and other communities?
- 数据:Facility-level GHG and co-pollutant emissions for California facilities, 2008-2017, run through an atmospheric dispersion model to compute community-level exposure
- 识别/方法:Difference-in-differences comparing covered and uncovered facilities before/after program start, translated into exposure via dispersion modeling
- 发现:After the program began, the environmental-justice gap in co-pollutant exposure between disadvantaged and other communities narrowed relative to its prior trend - trading did not concentrate pollution in disadvantaged areas.
- 与本项目的相关性:The rigorous template for carbon-market co-pollutant/distributional analysis; pairs with Fowlie-Holland-Mansur and with the China EJ result (Mei et al., Nature Communications 2026) that currently sits only in the notes. Relevant to where CN-ETS abatement (concentrated in small coal units, per Lyu et al.) happens geographically.
- 链接:https://doi.org/10.1016/j.jpubeco.2022.104786

**21. Meng (2017), Using a Free Permit Rule to Forecast the Marginal Abatement Cost of Proposed Climate Policy** — *American Economic Review 107(3): 748-784*

- 问题:Can asset prices be used to recover market expectations of the marginal abatement cost of a climate policy that never took effect (Waxman-Markey)?
- 数据:Stock returns of US firms differentially exposed to the Waxman-Markey free-permit allocation rule around legislative event dates, 2009-2010
- 识别/方法:Event-study/structural approach exploiting the bill's free permit allocation rule to separate expected allowance costs from other news
- 发现:Recovers the market-implied distribution of expected allowance prices (roughly $5-20/ton range) and the probability of passage - showing financial markets priced prospective carbon regulation.
- 与本项目的相关性:The methodological reference for extracting policy expectations from asset prices - the missing complement to Kaenzig (2023) in the carbon-price-formation strand, and the template for asking whether Chinese equity or CEA prices capitalize expected 2027 cap/auction reforms.
- 链接:https://www.aeaweb.org/articles?id=10.1257/aer.20150781

**22. Davidson, Perez-Arriaga (2020), Avoiding Pitfalls in China's Electricity Sector Reforms** — *The Energy Journal 41(3): 119-142*

- 问题:What design pitfalls threaten China's post-2015 electricity market reforms, and how should spot markets be structured given China's institutional constraints?
- 数据:Institutional analysis of China's 2015 reform round and early provincial spot market pilot designs
- 识别/方法:Comparative electricity-market design analysis (engineering-economic), drawing on international restructuring experience
- 发现:Partial liberalization risks provincial balkanization, distorted dispatch, and stranded interprovincial trade; recommends sequencing centered on well-designed provincial spot markets with locational pricing and consistent treatment of legacy generation contracts.
- 与本项目的相关性:The standard economics-journal reference on the institutional environment of the researcher's own Shandong spot market - the missing bridge between the carbon-electricity strand's China entries (Xiang et al., Liu-Jiang-Guo) and the carbon-market strands; needed to argue where carbon-cost pass-through can physically show up in dispatch.
- 链接:https://doi.org/10.5547/01956574.41.3.mdav

### 本节检索笔记(agent 原始记录,含未列入正文的文献与核验警告)

> VERIFICATION METHOD CAVEAT: the session's WebSearch budget was already exhausted (200/200) when this critic pass began, so every verification above ran through the Crossref REST API (api.crossref.org bibliographic queries returning title/authors/journal/year/volume/pages/DOI) and direct arXiv fetches. All 22 added papers were confirmed to exist this way; where a findings detail rests on memory rather than a fetched abstract, the entry says so in-line.
> 
> SUSPECTED-WRONG / GARBLED ENTRIES IN THE MERGED BIBLIOGRAPHY: (1) CONFIRMED ERROR - Ellerman & Montero (2007), The Energy Journal 28(4): pages are 47-72 (DOI 10.5547/issn0195-6574-ej-vol28-no4-3), not "67-91" as listed in carbon-price-formation. (2) MINOR - Cludius & Betz (2020): Crossref gives pages 275-300 (DOI 10.5547/01956574.41.2.jclu), bibliography says 275-299; otherwise correct. (3) CLEARED - Cui, Song & Jiang (China Economic Review 78: 101915, 2023, DOI 10.1016/j.chieco.2022.101915): verified exactly as listed; first author really is "Jian Cui" (a different person from Jingbo Cui) - the searcher's doubt can be dropped. (4) CLEARED - Xiang, Zheng, Song, Lin, Jiang (Nature Energy 8: 747-757, 2023, DOI 10.1038/s41560-023-01278-9) verified exactly as listed; note there is an Author Correction at Nature Energy 8: 1296. (5) CLEARED/UPGRADED - Borri, Liu, Tsyvinski & Wu: arXiv 2606.03767 resolves; full authors Nicola Borri, Yukun Liu, Aleh Tsyvinski, Xi Wu; submitted 2 June 2026, revised 16 June 2026; EUTL data 2005-2021; headline facts: ~40% of operators do not trade in a given year, frictions interact non-additively. (6) CLEARED - the iScience paper flagged "authors not verified" in two strands is Lyu, Wang, Cai & Xian (2026), iScience 29(4), art. 115424, DOI 10.1016/j.isci.2026.115424 - matches the china-ets-frontier attribution, so the china-ets-empirical and data-sources caveats can be closed. (7) NOT RE-VERIFIABLE HERE - Kaenzig NBER 31221 publication status and the Guojun He et al. "Carbon Market with Chinese Characteristics" WP: keep the searchers' own caution flags. (8) VENUE TRAP - Zhang-Wang-Du "Lessons Learned from China's Regional Carbon Market Pilots" is widely miscited to REEP; Crossref confirms Economics of Energy & Environmental Policy 6(2) (the same 2017 special issue as Teng-Jotzo-Wang and Karplus-Zhang already listed). No listed citation appears fabricated - the merged bibliography is unusually clean.
> 
> STRUCTURAL GAPS FILLED BY THE ADDITIONS (sub-strands a referee would flag as absent): (i) permit-market theory foundations - Montgomery 1972, Weitzman 1974, Hahn 1984 (market power: directly relevant to SOE-concentrated, compliance-only CEA trading), Rubin 1996 (banking: the theory behind China's 2024-25 carry-over restrictions), Pizer 2002 (hybrids/price collars); the bibliography currently cites Coase-property empirics (Zaklan) and collar empirics (Borenstein et al.) with none of the underlying theory. (ii) THE INTENSITY-TARGET THEORY HOLE - the most consequential gap: the bibliography carries only the anti-TPS output-subsidy line (Fischer 2001, HHK 2009, Goulder et al.) and omits the uncertainty-based case FOR intensity indexing (Newell-Pizer 2008; Fischer-Springborn 2011; Jotzo-Pezzey 2007). A balanced treatment of China's design choice, and of the 2027 intensity-to-cap transition, needs both sides. (iii) Rate-vs-mass in electricity - Bushnell-Holland-Hughes-Knittel 2017 (Clean Power Plan), the US wholesale-market analog of China's TPS with cross-jurisdiction leakage, i.e., the Shandong-trades-with-regulated-neighbors setting. (iv) Developing-country pollution-market experiments - Greenstone et al. QJE 2025 and Duflo et al. QJE 2013: the most obvious referee flags in the whole bibliography. (v) US program evaluations beyond Title-IV history - Fowlie-Holland-Mansur AER 2012 (RECLAIM) and Carlson et al. JPE 2000, both of which the ets-classics notes themselves listed as unverified holes. (vi) CDM/offset additionality antecedent - Zhang-Wang JEEM 2011, the peer-reviewed root of the CCER additionality debate. (vii) English institutional reviews of the pilots - Zhang-Wang-Du 2017, Munnings et al. 2016, Zhang ZhongXiang 2015 (the Chinese-language strand names Zhang ZhongXiang as the key bridge author but lists none of his work). (viii) Chinese monitoring-data credibility - Karplus-Zhang-Almond PNAS 2018, foundation for all the CEMS-based CN-ETS papers listed. (ix) Carbon-market environmental justice - Hernandez-Cortes & Meng JPubE 2023 (pairs with Mei et al. Nature Communications 2026, currently notes-only). (x) Expectations/asset-price identification - Meng AER 2017, complement to Kaenzig for CEA price informativeness. (xi) China electricity institutions bridge - Davidson & Perez-Arriaga Energy Journal 2020, directly relevant to the researcher's Shandong spot-market work.
> 
> GAPS I COULD NOT FILL OR VERIFY (do not treat as empty; re-check with search access): ASIF/environmental-statistics-based pilot papers in JEEM/Energy Economics (data-sources flag stands); any Shanjun Li China-carbon paper (concur with china-ets-empirical: none found - his inclusion in the strand remains unconfirmed); Schennach (2000, JEEM) on Title IV banking dynamics and Liski-Montero on banking with market power (both would slot beside Rubin - cite-check first); Goulder (2013, JEP) "Markets for Pollution Allowances: What Are the (New) Lessons?" as a survey anchor; the RECLAIM-era spatial-damages strand beyond FHM 2012; Chinese-venue holes in 经济学(季刊)/世界经济 (unverified, per the chinese-language strand). Books were excluded by construction, but a referee may still expect Ellerman, Convery & de Perthuis "Pricing Carbon" (CUP 2010) and Ellerman et al. "Markets for Clean Air" (CUP 2000) as institutional citations.
> 
> BONUS DISCOVERY RELEVANT TO THE RESEARCHER'S GAP CLAIM: Crossref surfaced Naifu Zhang, Hang Xu & Yafen Yang (2026), "Market Efficiency in China's Provincial Electricity Spot Markets: Evidence from Shandong, Shanxi and Guangdong," Sustainability 18: 4960, DOI 10.3390/su18104960. Weak venue (MDPI), and it tests spot-market efficiency, not carbon-cost pass-through - so the carbon-electricity strand's claim that no CEA-to-spot-price pass-through paper exists still stands - but note the first author overlaps with the He-Wu-Zhang-Zhou "Carbon Market with Chinese Characteristics" WP team: people with Shandong spot data are already publishing, so the Fabra-Reguant-style CEA pass-through paper on Shandong should be treated as a closing window, not an open field.

## 第 8 节 数据源指南

做中国碳市场实证需要什么数据、哪里拿、什么是公开的。条目格式:"citation"位置放数据源名称。山东相关的核实事实集中在本节。

**1. SEEE/CNEEEX daily CEA market bulletins — 【CEA】全国碳市场每日综合价格行情及成交信息 (daily comprehensive price and transaction information, national carbon market)** — *Shanghai Environment and Energy Exchange (上海环境能源交易所), operator of the national CEA trading platform*

- 问题:Primary public source for daily national-ETS (CEA) prices and volumes since market launch on 2021-07-16.
- 数据:One dated news post per trading day on overview.cneeex.com, archived by year 2021-2026 under 每日概况 (https://overview.cneeex.com/qgtpfqjy/mrgk/, subfolders /2021n/ ... /2025n/). Each bulletin separates listed-agreement trading (挂牌协议: volume, turnover, and OHLC-style price fields) from block trades (大宗协议: daily volume and turnover only — e.g. 2025-12-03: listed 639,256 t / RMB 38.27m; block 226,790 t / RMB 12.47m; block VWAP is computable from volume and amount), plus year-to-date and cumulative totals. An interactive daily-data query tool exists at https://shyx.cneeex.com/qdata.html. No official bulk CSV download — researchers scrape the daily posts or take the series from Wind/CSMAR/ICAP. Important caveat stated by the exchange: block-trade transactions are NOT included in the real-time intraday quotes, so 'closing price' series alone misstate market activity; block trades are a large share of CEA turnover.
- 识别/方法:n/a — exchange-published market data (listed continuous/agreement trading plus negotiated block trades).
- 发现:Full daily CEA price/volume history Jul 2021-present is public but only as per-day announcements; the listed/block split is recoverable day-by-day, which matters because compliance-deadline months (incl. Dec 2021, the start of the researcher's Shandong sample) show extreme volume bunching.
- 与本项目的相关性:This is the treatment/outcome price series for any Chinese carbon-market paper; for the Shandong electricity paper it provides the daily carbon-cost signal facing Shandong coal generators (Shandong entities are the largest bloc of CEA compliance traders), enabling carbon-price pass-through or interaction terms with day-ahead/real-time spreads.
- 链接:https://overview.cneeex.com/qgtpfqjy/mrgk/

**2. 全国碳市场信息网 (National Carbon Market Information Network), cets.org.cn** — *Official national carbon market information portal (MEE-affiliated; exact operating institution not verified in this sweep)*

- 问题:Centralized official portal for national ETS notices, trading-information disclosure, and covered-entity information.
- 数据:Search-indexed sections include: 名录信息公开 (covered-entity list disclosure, https://www.cets.org.cn/mlxxgk/index.jhtml), 重点排放单位信息公开 (key-emitter information disclosure, https://www.cets.org.cn/zdpfdwxxgk/index.jhtml), 交易信息披露相关问题 (FAQ on trading-data disclosure, https://www.cets.org.cn/jyxxplxgwt/index.jhtml), and 通知公告 (e.g. the 2026 annual work notice). ACCESS CAVEAT: every direct fetch from this US-based session returned HTTP 503 — the site appears to block or throttle non-China access; content was confirmed only through search-engine indexing. Plan to access from a China network or via an aggregator.
- 识别/方法:n/a — government information-disclosure portal.
- 发现:Appears to be the emerging one-stop official source for entity lists and market information for the expanded (power + steel + cement + aluminum) national ETS; verify what entity-level fields (verified emissions? compliance status?) are actually posted once accessible.
- 与本项目的相关性:If the 重点排放单位信息公开 section carries entity-level compliance/emissions fields, it would be the cleanest official cross-provincial covered-entity panel — the natural firm-list backbone for matching Shandong generators between the carbon paper and the electricity-spot-market paper.
- 链接:https://www.cets.org.cn/

**3. MEE national ETS allocation plans and compliance announcements (e.g., 2023/2024年度全国碳排放权交易发电行业配额总量和分配方案; 2024-2026 名录制定要求; Jan-2025 compliance completion announcement)** — *Ministry of Ecology and Environment (mee.gov.cn)*

- 问题:Official documents defining cap, benchmarks, covered-entity criteria, and reporting compliance outcomes for the national ETS.
- 数据:Downloadable PDFs on mee.gov.cn: the 2023/2024 power-sector allocation plan (2,096 covered power entities for 2023, ~5.2 GtCO2/yr covered; PDF https://www.mee.gov.cn/xxgk2018/xxgk/xxgk06/202407/W020240702328244215540.pdf); the April-2025 document setting 2024-2026 covered-entity list requirements by sector (https://www.mee.gov.cn/xxgk2018/xxgk/xxgk06/202504/W020250415552214741056.pdf, which delegates annual 名录 determination to provincial ecology departments); the Jan-2025 announcement that 2024 allowance trading and surrender concluded (https://www.mee.gov.cn/ywgz/ydqhbh/syqhbh/202501/t20250105_1099975.shtml, incl. cumulative CEA volume 630 Mt / RMB 43.03bn through end-2024). MEE also publishes compliance-cycle reports (e.g., first-cycle report, 全国碳市场发展报告 series) with aggregate statistics; entity-level verified emissions are NOT centrally published — published entity details are limited to company name, province, and Unified Social Credit Identifier (USCI).
- 识别/方法:n/a — regulatory documents; benchmarks/caps here define the policy intensity variables used in empirical work.
- 发现:Benchmark stringency, banking restrictions, and the shift from two-year to annual compliance (from 2023) are all documented here; verified emissions per firm remain restricted, which is the single biggest data gap in this literature.
- 与本项目的相关性:The allocation-plan benchmarks for coal/gas units determine the marginal carbon cost of Shandong generators — an input if the carbon paper (or the electricity paper) wants unit-level implied carbon cost; USCI codes in the entity lists are the match key to other firm datasets.
- 链接:https://www.mee.gov.cn/xxgk2018/xxgk/xxgk06/202407/W020240702328244215540.pdf

**4. Provincial covered-entity lists (重点排放单位名录), especially Shandong Provincial Department of Ecology and Environment 公示 lists** — *Provincial ecology and environment departments (Shandong: sthj.shandong.gov.cn)*

- 问题:Which firms are covered by the national ETS in each province, published annually as name lists with unit detail.
- 数据:Provincial DEEs determine and publicize annual lists. Shandong examples verified: 2022-vintage list 公示 (Jan 2023, http://sthj.shandong.gov.cn/ydqhbhc/gzxx_17610/202301/t20230101_4205842.html) and the Oct-2025 公示 of Shandong's 2026 lists covering power (287 entities), steel, cement, and aluminum smelting. Key verified facts for citing Shandong's prominence: 330 power-sector entities in the first compliance cycle — the most of any province and the only province above 300 (ideacarbon.org report); by end-2024, 323 Shandong entities had cumulatively traded (bjx.com.cn, Feb 2025), 268 were under quota management with ~4.7 Gt cumulative compliance obligation, ranking first nationally, and Shandong accounted for roughly one quarter of national trading volume across the first three compliance cycles (MEE local news, https://www.mee.gov.cn/ywdt/dfnews/202503/t20250310_1103648.shtml).
- 识别/方法:n/a — administrative lists; the standard research use is name/USCI matching into firm datasets for DiD designs.
- 发现:Shandong is confirmed as the province with the most covered firms and the largest compliance volume in the national ETS; annual provincial lists (2021-2026 vintages) allow construction of a covered-entity panel with entry (26,000 tCO2e/yr threshold) and sectoral expansion in 2024/2025.
- 与本项目的相关性:Directly supports the planned citation that Shandong has the most covered firms; the Shandong power-entity list is also the population of thermal generators in the researcher's Shandong spot-market paper, enabling a merged carbon-cost/bidding dataset.
- 链接:http://sthj.shandong.gov.cn/ydqhbhc/gzxx_17610/202301/t20230101_4205842.html

**5. Qingyue Open Environmental Data (上海青悦) carbon-market disclosure trackers, e.g. 第二个履约周期碳交易信息公开统计** — *Shanghai Qingyue Environmental Information Technology Service Center (epmap.org), an environmental-data NGO*

- 问题:Meta-tracking of which provinces have publicly disclosed covered-entity lists and related carbon-market information, cycle by cycle.
- 数据:Static tables tracking disclosure status (已公开 or not) of 重点排放单位名单 across 31 provinces for each compliance cycle, with links toward provincial sources (https://www.epmap.org/co2keyorglistopenstatus-2). Qingyue is best known among researchers for scraping and republishing Chinese environmental disclosure data (its broader platform offers open data/APIs for environmental records); the carbon pages verified here are disclosure-status trackers, not bulk data downloads — use them as a directory to locate each province's list.
- 识别/方法:n/a — NGO data-transparency aggregator.
- 发现:Confirms provincial disclosure of national-ETS entity lists is near-universal but decentralized and heterogeneous in format; Tibet has no covered facilities.
- 与本项目的相关性:Fastest way to assemble the all-province covered-entity panel (and to document, in a data appendix, exactly which provinces disclosed what and when) — useful both for the carbon paper and for benchmarking Shandong against other provinces.
- 链接:https://www.epmap.org/co2keyorglistopenstatus-2

**6. ICAP Allowance Price Explorer** — *International Carbon Action Partnership (icapcarbonaction.com)*

- 问题:Downloadable cross-system allowance price (and auction revenue) series including China's national ETS and all eight regional pilots.
- 数据:Web tool at https://icapcarbonaction.com/en/ets-prices with visualization and download. Per the documentation page (https://icapcarbonaction.com/en/documentation-allowance-price-explorer): China national ETS prices are sourced from the Shanghai Environment and Energy Exchange, and each Chinese pilot (Shenzhen, Beijing, Shanghai, Tianjin, Guangdong, Hubei, Chongqing, Fujian) from its regional exchange, with data provision by Shanghai Treasure Carbon New Energy Environmental Protection Technology Ltd.; updates are manual and quarterly. Terms of use: reproduction/redistribution only for non-commercial purposes and subject to ICAP's prior written permission, with citation of both ICAP and the original source. Exact start dates and download file format were not stated on the fetched pages.
- 识别/方法:n/a — curated secondary price database.
- 发现:The most convenient single English-language download of Chinese carbon prices (national + pilots), but it is a secondary quarterly-updated compilation of exchange data — for daily econometrics, reconstruct from SEEE bulletins or a terminal database and use ICAP for cross-checking and for pilot-era history.
- 与本项目的相关性:Quickest way to get a consistent CEA + pilot price panel overlapping the Dec 2021-Aug 2026 Shandong sample; note the permission requirement before redistributing the series in a replication package.
- 链接:https://icapcarbonaction.com/en/ets-prices

**7. ICAP China National ETS factsheet** — *International Carbon Action Partnership*

- 问题:Maintained English-language reference on national ETS design parameters, coverage, and prices.
- 数据:Web factsheet with downloadable PDF (https://icapcarbonaction.com/en/ets/china-national-ets; PDF version indexed at https://icapcarbonaction.com/en/ets-pdf-download/55). Verified current figures: ~3,300 covered entities after the 2025 expansion to steel, cement, and aluminum smelting; ~8 GtCO2 covered (>60% of China's CO2; world's largest ETS by covered emissions); 2025 average secondary-market price CNY 70.78 (~USD 9.85); annual compliance cycles from 2023 (previously two-year); planned expansion to petrochemicals, chemicals, flat glass, copper smelting, paper, aviation. First cycle (2019-2020 emissions, 2021 compliance) covered 2,162 power entities at the 26,000 tCO2/yr threshold.
- 识别/方法:n/a — institutional factsheet, updated continuously.
- 发现:Reliable citable source for design facts (benchmarks, banking, MRV timeline, sector expansion) without navigating Chinese-language regulations.
- 与本项目的相关性:Standard institutional citation for the paper's background section; the sector-expansion timeline matters for defining treatment in any post-2024 national-ETS empirical design.
- 链接:https://icapcarbonaction.com/en/ets/china-national-ets

**8. National CCER trading system data (全国温室气体自愿减排交易系统, ccer.com.cn) and the linked CCER registry** — *CCER trading platform operated under Beijing Green Exchange (北京绿色交易所); registry system interconnected one-to-one*

- 问题:Public data on China's restarted voluntary carbon market (CCER): transactions, daily quotes, and project/credit registrations.
- 数据:The 成交数据 section (https://www.ccer.com.cn/wcm/ccer/html/2502sjcx/index.html) publishes a transaction table with date, industry classification, volume (t), average price (yuan/t), and amount, plus navigation for 实时行情 (real-time), 每日行情 (daily), 年度数据 (annual), and 数据查询 (query). Timeline verified: trading-system trial operation and account opening from Aug 2023 (announcements on ccer.com.cn); the registry and trading systems passed acceptance June 2023; first CCERs completed registration by early March 2025 (MEE, https://www.mee.gov.cn/ywgz/ydqhbh/wsqtkz/202503/t20250306_1103521.shtml). Download options and historical depth not verifiable from the fetched page; project-level validation/registration disclosures sit in the registry system rather than the trading site.
- 识别/方法:n/a — exchange/registry disclosure.
- 发现:CCER market data is public but young (trading from Jan 2024, first credits registered 2025); volumes are thin relative to CEA, and CCERs can offset up to a share of CEA compliance obligations, linking the two markets.
- 与本项目的相关性:CCER offset use is a margin of compliance flexibility for Shandong power firms; renewable-energy CCER methodologies also interact with the same wind/solar fleet whose forecast errors drive the Shandong spot-market paper.
- 链接:https://www.ccer.com.cn/wcm/ccer/html/2502sjcx/index.html

**9. CSMAR 碳中和研究数据库 (Carbon Neutrality Research Database)** — *CSMAR / Shenzhen CSMAR Data Technology (国泰安); institutional subscription*

- 问题:Commercial research database bundling China carbon-market and carbon-neutrality data for academic use.
- 数据:Per the Tsinghua Library subscription notice (https://lib.tsinghua.edu.cn/info/1076/5976.htm and trial notice), the database includes: 全国碳排放权交易信息 (national carbon-market trading information), regional and industry CO2 emissions, environmental pollution-emission indicators, listed-company-level carbon emissions and abatement information, carbon-neutrality concept stocks, low-carbon bonds and funds, and green-credit items. Access via institutional CSMAR subscription (structured, export-to-Excel/Stata). Exact table granularity for CEA (daily vs monthly; listed vs block split) not verified in this sweep. Wind terminal also carries CEA and pilot daily price series and is the most common source cited in Chinese-language papers, but no page verifying Wind's coverage was captured in this session.
- 识别/方法:n/a — commercial data vendor.
- 发现:For most academic users a CSMAR (or Wind) pull is the practical way to get a clean machine-readable CEA + pilot series and listed-firm carbon variables without scraping SEEE bulletins.
- 与本项目的相关性:One-stop source to merge carbon prices with listed-firm data (many Shandong gencos are subsidiaries of listed utilities), and its emission tables can proxy firm-level exposure where MEE verified emissions are unavailable.
- 链接:https://lib.tsinghua.edu.cn/info/1076/5976.htm

**10. 碳中和网 (ccn.ac.cn) CEA 行情数据 compilations** — *Carbon Neutrality Net (ccn.ac.cn), free aggregator*

- 问题:Free monthly-compiled national CEA trading information pages as an alternative to scraping the exchange.
- 数据:Monthly pages of 全国碳排放权交易信息 (e.g. Feb-2024 page https://www.ccn.ac.cn/carbon-market/carbon-emissions-trading/ceadate/1054.html) under a CEA行情数据 index (https://www.ccn.ac.cn/3060/carbon-market/carbon-emissions-trading/ceadate), plus a national-carbon-market portal page (https://www.ccn.ac.cn/cets). Cumulative-to-date verified figure reproduced there: 630 Mt / RMB 43.03bn CEA traded through end-2024. HTML tables, no API; suitable for cross-checking a scraped SEEE series.
- 识别/方法:n/a — secondary aggregator of exchange announcements.
- 发现:Convenient free mirror of the SEEE monthly/daily aggregates; provenance should still be attributed to SEEE bulletins in the paper.
- 与本项目的相关性:Backup/cross-validation source when building the daily CEA series covering Dec 2021-Aug 2026 from outside China (ccn.ac.cn was reachable from a US network while cneeex.com occasionally throttles).
- 链接:https://www.ccn.ac.cn/3060/carbon-market/carbon-emissions-trading/ceadate

**11. Cui, Wang, Zhang and Zheng (2021), "The effectiveness of China's regional carbon market pilots in reducing firm emissions"** — *Proceedings of the National Academy of Sciences 118(52), e2109912118*

- 问题:Did China's regional ETS pilots reduce firm-level carbon emissions despite low prices and thin trading?
- 数据:Unique panel of firm tax records for manufacturing and public-utility sectors, 2009-2015 (China's national tax survey data; restricted-access, obtained through co-authors' institutional arrangements — the precise access route is not stated on the open pages fetched). Firm energy use in the tax records is converted to CO2 emissions.
- 识别/方法:Matched difference-in-differences exploiting the staggered, sector-selective rollout of the seven regional pilots as a quasi-natural experiment.
- 发现:Regulated firms cut total emissions by 16.7% and emission intensity by 9.7%, via energy conservation and switching to lower-carbon fuels; negative effects on employment and capital but positive productivity effects; abatement is larger in pilots with mass-based allocation, higher prices, and active trading.
- 与本项目的相关性:The benchmark firm-level evaluation of Chinese carbon pricing and the template for the tax-survey data route; its heterogeneity results (price level and liquidity matter) frame hypotheses for national-ETS work, and its utilities coverage overlaps the power firms central to the Shandong project.
- 链接:https://www.pnas.org/doi/10.1073/pnas.2109912118

**12. Cao, Ho, Ma and Teng (2021), "When carbon emission trading meets a regulated industry: Evidence from the electricity sector of China"** — *Journal of Public Economics 200, 104470*

- 问题:How do carbon-market pilots affect coal-fired power plants operating under regulated electricity prices and dispatch?
- 数据:Retrospective plant-level panel of Chinese power plants, regulated (pilot) vs unregulated regions (non-public plant-level electricity-industry data; the open pages fetched — RFF and ScienceDirect landing pages — do not name the source/years, commonly understood to be Chinese electricity-industry plant statistics obtained via the Harvard China Project/Tsinghua collaboration; treat exact source as unverified here).
- 识别/方法:Treatment-effects / DiD comparison of regulated vs unregulated coal plants across pilot and non-pilot regions.
- 发现:Pilots had no effect on coal efficiency (intensity) of regulated coal plants; emissions fell through output contraction, likely administratively driven since permit costs were small relative to controlled electricity prices; non-coal generation rose in pilot regions; no evidence of leakage, attributed to the regulated dispatch hierarchy.
- 与本项目的相关性:The canonical paper on the carbon-market-meets-regulated-electricity friction — the exact institutional tension the Shandong spot market is dissolving; it provides the pre-spot-market baseline against which an Ito-Reguant-style Shandong analysis (market-based dispatch + carbon costs) can be contrasted.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0047272721001067

**13. Goulder, Long, Lu and Morgenstern (2019), "China's Unconventional Nationwide CO2 Emissions Trading System: The Wide-Ranging Impacts of an Implicit Output Subsidy"** — *NBER Working Paper 26537 (later published in a field journal — JEEM 2022 per common citation, not verified on the NBER page)*

- 问题:How cost-effective is China's rate-based tradable performance standard (TPS) relative to cap-and-trade, given its implicit output subsidy?
- 数据:No micro data — analytically and numerically solved general-equilibrium models of China's power sector calibrated to Chinese data.
- 识别/方法:Theory/simulation: matched analytical and numerical GE models comparing TPS vs mass-based cap-and-trade.
- 发现:TPS overall costs are ~47% higher than equivalent cap-and-trade because the output subsidy distorts abatement channels and limits gains from allowance trading; offsetting advantages are distributional (multiple benchmarks) and smaller electricity-price increases, reducing leakage.
- 与本项目的相关性:The standard framework for why China's intensity-based ETS suppresses electricity-price pass-through — directly relevant to how (or whether) CEA prices show up in Shandong day-ahead bids and spreads.
- 链接:https://www.nber.org/papers/w26537

**14. Wang, Baixue and Duan, Maosheng (2025), "Have China's emissions trading systems reduced carbon emissions? Firm-level evidence from the power sector"** — *Applied Energy 378(PB), 124802*

- 问题:Did China's ETSs reduce power-sector carbon emissions, and through output or intensity margins?
- 数据:Verified firm-level carbon-emission data plus annually updated regulatory (covered-entity) lists for the power sector — i.e., MRV data that is not centrally public, presumably obtained via Tsinghua's policy-support role (access route not stated on the IDEAS page).
- 识别/方法:DiD with event-study designs, using heterogeneity-robust estimators for staggered adoption.
- 发现:ETSs significantly reduced emissions primarily via reduced generation, with little effect on carbon intensity; intensity responds only where allowance shortages are large and prices high; no leakage to neighboring provinces.
- 与本项目的相关性:Demonstrates that the key non-public dataset (verified emissions + annually updated entity lists) is obtainable through Chinese policy-research channels; the output-vs-intensity margin is exactly the dispatch margin observable in Shandong spot-market data.
- 链接:https://ideas.repec.org/a/eee/appene/v378y2025ipbs0306261924021858.html

**15. "Unit-level monitoring data reveal the effectiveness of China's national emissions trading scheme" (2025; authors and exact journal not verified — ScienceDirect open-access article, PII S2949790625000357)** — *ScienceDirect journal (PII prefix 2949-7906; fetch blocked, journal name unverified)*

- 问题:What do unit-level monitoring and order-level trading data show about compliance and abatement in the national ETS's first compliance phase?
- 数据:Detailed unit-level monitoring data on power-generating units plus order-specific trading data for the first compliance phase (2019-2020 emissions, ~4.5 GtCO2/yr regulated) — clearly restricted regulatory/registry data, not public downloads.
- 识别/方法:Descriptive-causal analysis of compliance and abatement channels using the unit-level panel (full method not verifiable; page fetch returned 403).
- 发现:93.9% of units and 99.6% of obligations compliant; carbon intensity fell 2.46-3.13% and emissions 0.86% despite 1.63% production growth; abatement via fuel quality, efficiency, cleaner fuels, and retiring outdated units; projected abatement offsets 34-47% of counterfactual 2025/2030 power-emission growth.
- 与本项目的相关性:The clearest published proof that unit-level MRV and order-level CEA trading data exist and have been released to researchers — the exact data one would request for a Shandong-focused carbon/electricity merge; also documents compliance-driven trading behavior around deadlines.
- 链接:https://www.sciencedirect.com/science/article/pii/S2949790625000357

**16. "The effectiveness of China's national emissions trading scheme in mitigating firm emissions" (2025; authors not verified, PII S0140988325006565)** — *Energy Economics*

- 问题:Firm-level evaluation of the national ETS's abatement effect (details unverified).
- 数据:Not verifiable in this sweep — ScienceDirect fetch blocked and the search budget was exhausted; seen only as a search-result link. Likely firm-level emissions data given the title; verify before citing substantively.
- 识别/方法:Unverified.
- 发现:Unverified — flagged here so the synthesis step knows a 2025 Energy Economics national-ETS firm-level evaluation exists and should be pulled manually.
- 与本项目的相关性:Recent frontier reference for the national ETS's firm-level effects; a direct comparator/citation for the planned carbon-market paper.
- 链接:https://www.sciencedirect.com/science/article/abs/pii/S0140988325006565

**17. World Carbon Pricing Database — "World carbon pricing database: sources and methods" (Scientific Data, 2022; author names not captured in this sweep)** — *Nature Scientific Data (dataset descriptor); open-access dataset*

- 问题:Economy-wide, sector-level carbon-price database across jurisdictions, including China's pilots and national ETS.
- 数据:Open-access descriptor at https://www.nature.com/articles/s41597-022-01659-x (also PMC9482624); the underlying database is openly redistributable, covering carbon tax and ETS prices by jurisdiction-sector-year. Complementary: the World Bank Carbon Pricing Dashboard (https://carbonpricingdashboard.worldbank.org/) with annual price/coverage/revenue data for China's national ETS and pilots, freely downloadable.
- 识别/方法:n/a — documented dataset compilation with stated sources and methods.
- 发现:Provides a citable, license-clean long panel of Chinese carbon prices at annual granularity — useful where ICAP's permission requirement or exchange scraping is a burden, though too coarse for daily analysis.
- 与本项目的相关性:Clean source for cross-country framing tables (China vs EU ETS price levels) in the paper's introduction without redistribution restrictions.
- 链接:https://www.nature.com/articles/s41597-022-01659-x

### 本节检索笔记(agent 原始记录,含未列入正文的文献与核验警告)

> COVERAGE CAVEATS AND CROSS-CUTTING POINTS FOR THE SYNTHESIS STEP.
> 
> (1) Access environment: WebSearch budget (200/session) was exhausted mid-sweep, and mainland-hosted sites consistently returned HTTP 503 through the US proxy (cets.org.cn, hbets.cn, ceads.net; mee.gov.cn PDFs were indexed via search but not fetched), while cneeex.com's overview subdomain, ccer.com.cn, and shandong.gov.cn snippets worked. Practical implication for the researcher: build the CEA daily series either from inside China or from Wind/CSMAR; expect official portals to be flaky from abroad. PNAS/ScienceDirect/Cell fetches returned 403 (bot-blocking), so a few paper-metadata fields are flagged unverified rather than guessed.
> 
> (2) Key structural facts about CEA data verified this session: daily bulletins split 挂牌协议 (listed) from 大宗协议 (block) trades; the exchange states block trades are excluded from real-time quotes — any daily 'price' series must be volume-weighted across both legs from the bulletins (block VWAP = amount/volume). SEEE also runs an interactive query tool (shyx.cneeex.com/qdata.html). Trading rules (price limits, block minimum size) are in SEEE rule documents on cneeex.com — numbers not verified here, do not cite from memory.
> 
> (3) Entity lists vs verified emissions: covered-entity lists (name + province + USCI) are public, decentralized to provincial DEE websites and increasingly mirrored on cets.org.cn; VERIFIED EMISSIONS AT ENTITY LEVEL ARE NOT PUBLIC. Papers that got them (Wang-Duan AppEnergy 2025; the unit-level monitoring paper 2025) did so through Chinese policy-research channels (Tsinghua/MEE-adjacent). The tax-survey route (Cui et al. PNAS 2021) and plant-level electricity-statistics route (Cao et al. JPubE 2021) are the two established non-public firm-data strategies for the pilot era.
> 
> (4) Shandong: verified — 330 power entities in cycle 1 (only province >300, national max; ideacarbon.org/news_free/56447/), 287 power entities in the 2026 list plus new steel/cement/aluminum lists (公示 Oct 2025), 268 under quota management end-2024 with ~4.7 Gt obligation (first nationally), 323 cumulative trading participants, ~1/4 of national trading volume over the first three cycles (mee.gov.cn dfnews 2025-03-10). These are strong, citable hooks tying the carbon paper to the Shandong electricity work.
> 
> (5) Not covered / cut for verification reasons: ASIF (工业企业数据库) and 环境统计 (ESR) matched-pilot papers exist in numbers (JEEM/Energy Economics), but the search budget died before I could verify specific citations — the synthesis should not treat this strand as empty, just unverified here. Same for Wind's exact CEA table coverage, Bloomberg/BNEF CEA tickers, pilot-exchange bulk downloads (Hubei hbets.cn, Guangzhou cnemission.com, Shenzhen, Beijing cbgex.com, Tianjin, Chongqing, Fujian — all publish daily quotes on their sites per ICAP documentation, which names each regional exchange as the source), CEADs (ceads.net, free-registration provincial/city inventories — site unreachable via proxy), and the Cui-Zhang-Zheng AEA P&P 2018 patents paper (not seen in this session's results, so excluded per the no-unseen-citations rule).
> 
> (6) Useful secondary overviews seen but not made entries: ADB 2024 background paper on the PRC ETS (adb.org PDF), IETA China Business Brief July 2025, Asia Society ETS Status: China, Carbon Brief in-depth Q&A, Oxford Guide to Chinese Climate Policy emissions-trading chapter, IEA 'China's Emissions Trading Scheme' report — good for institutional citations. Also seen: iScience (2026) 'Dual CO2 mitigations with diminishing margins: Evidence from China's intensity-based national ETS' (cell.com fetch 403; exists, worth pulling manually) and EST (2024) 'Carbon Abatement and Leakage in China's Regional Carbon Emission Trading'.
> 
> (7) Debate in the strand the synthesis should surface: output-margin vs intensity-margin abatement under the rate-based TPS (Goulder et al. theory; Cao et al. and Wang-Duan empirics agree reductions come via output, with intensity responding only under high prices/shortage) — this is precisely where linking CEA data to Shandong's new spot-market dispatch data has a comparative advantage.
