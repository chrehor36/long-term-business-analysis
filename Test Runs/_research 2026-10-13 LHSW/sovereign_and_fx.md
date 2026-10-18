# Sovereign and conversion rate (fetched 2026-10-13)

## PRC 30-year government bond yield (the earnings currency is RMB)
Source: Ministry of Finance of the PRC, "财政部-中国国债收益率曲线" (China Treasury yield curve), the curve the
Ministry publishes, compiled for it by China Central Depository & Clearing (ChinaBond). Endpoint:
https://yield.chinabond.com.cn/cbweb-czb-web/czb/queryGjqxInfo (workTime=2026-10-12), the data page behind
https://yield.chinabond.com.cn/cbweb-czb-web/czb/moreInfo (page title "财政部-中国国债收益率曲线").
Why this source: the issuer of PRC government bonds is the Ministry of Finance; this is the Ministry's own
published curve, so it is the issuing authority's figure (operator rule 5), not an aggregator.

Key tenors, 2026-10-12 (percent): 3M 1.17; 6M 1.19; 1Y 1.20; 2Y 1.26; 3Y 1.28; 5Y 1.40; 7Y 1.50; 10Y 1.67; **30Y 2.07**.

## USD/CNY conversion
Central parity, CFETS (China Foreign Exchange Trade System, which publishes the rate on the People's Bank of China's
authorization), 2026-10-13 09:15: **6.7298 RMB per USD**. Endpoint:
https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/ccpr.json
The 20-F's own translation rates: period-end 6.8980 (2026-03-31), 7.2567 (2025-03-31); period average 7.1019 (FY2026),
7.2163 (FY2025), 7.1671 (FY2024) (20-F FY2026, Note 3, accession 0001213900-26-089090).

## US sovereign (shown only because tools/run.py printed it)
US Treasury daily par yield curve, 30-year, 5.60%, 2026-10-09 (run.py). Not used: the earnings currency is RMB.
