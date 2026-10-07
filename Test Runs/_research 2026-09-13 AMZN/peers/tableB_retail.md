# TABLE B: RETAIL / MARKETPLACE COMPETITOR ROW (AMZN run, 2026-09-13)

Transcription and arithmetic only. No conclusion about Amazon's moat is drawn in this file.
Local currency millions unless stated (USD for all except PDD, which reports RMB).
"computed" = arithmetic done here on filed figures. "filed" = the figure or percentage as printed in the filing.
Text files were read as UTF-8 and whitespace/table pipes collapsed; quotes are copied from that collapsed text. Artifacts are flagged where seen.

## DOCUMENTS READ

Paths: `MSFT/` = `Test Runs/_research 2026-09-06 MSFT/`; `AMZN/` = `Test Runs/_research 2026-09-13 AMZN/`; `peers/` = `AMZN/peers/`; `WMT/` = `Test Runs/_research 2026-09-06 WMT/`.
Accessions verified from the `SOURCE/ACCESSION` header line of each text file, or (where the file has no header: all WMT files) from `peers/submissions_WMT.json`.

| Company | Form | Period | Accession | Text on disk |
|---|---|---|---|---|
| Amazon | 10-K | FY2025 (Dec 31) | 0001018724-26-000004 | `MSFT/AMZN_FY2025_10K.txt` |
| Amazon | 10-K | FY2024 / FY2023 / FY2022 / FY2021 | 0001018724-25-000004 / -24-000008 / -23-000004 / -22-000005 | `MSFT/AMZN_FY20xx_10K.txt` |
| Amazon | 10-K | FY2017, FY2018, FY2019, FY2020, FY2015 (fee search only) | (headers not re-read) | `AMZN/10K_filed2018/2019/2020.txt`, `MSFT/AMZN_FY2020_10K.txt`, `MSFT/AMZN_FY2015_10K.txt` |
| Amazon | 10-Q | six months ended 2026-06-30 | 0001018724-26-000026 | `AMZN/10Q_2026Q2.txt` |
| Amazon | 10-Q | Q1 2026 / Q3 2025 | 0001018724-26-000014 / 0001018724-25-000123 | `AMZN/10Q_2026Q1.txt`, `AMZN/10Q_2025Q3.txt` |
| Amazon | 8-K EX-99.1 | Q3 2025 / Q4 2025 / Q1 2026 / Q2 2026 releases | Q4 2025: 0001018724-26-000002; Q2 2026: 0001018724-26-000024 | `AMZN/EX991_20xxQx.txt` |
| Walmart | 10-K | FY ended 2026-01-31 | 0000104169-26-000055 (submissions_WMT.json: 10-K, reportDate 2026-01-31, filed 2026-03-13) | `WMT/10k-fy2026-text.txt` |
| Walmart | 10-Q | six months ended 2026-07-31 (Q2 FY2027) | 0000104169-26-000154 (submissions_WMT.json: 10-Q, reportDate 2026-07-31, filed 2026-08-28) | `WMT/10q-fy2027q2-text.txt` |
| Walmart | 8-K EX-99.1 | Q4 FY2026 release (2026-02-19) / Q2 FY2027 release (2026-08-20) | 0000104169-26-000032 / 0000104169-26-000145 (8-K accessions, submissions_WMT.json) | `WMT/8k-q4fy26-ex991.txt`, `WMT/8k-q2fy27-ex991.txt` |
| eBay | 10-K | FY2025 (Dec 31) | 0001065088-26-000027 (the brief's alternative "-000006" is not the 10-K) | `peers/EBAY_10K_FY2025.txt` |
| eBay | 10-Q | six months ended 2026-06-30 | 0001065088-26-000177 | `peers/EBAY_10Q_2026Q2.txt` |
| MercadoLibre | 10-K | FY2025 (Dec 31) | 0001099590-26-000006 | `peers/MELI_10K_FY2025.txt` |
| MercadoLibre | 10-Q | six months ended 2026-06-30 | 0001099590-26-000023 | `peers/MELI_10Q_2026Q2.txt` |
| Shopify | 10-K | FY2025 (Dec 31) | 0001594805-26-000007 | `peers/SHOP_10K_FY2025.txt` |
| Shopify | 10-Q | six months ended 2026-06-30 | 0001594805-26-000047 | `peers/SHOP_10Q_2026Q2.txt` |
| PDD Holdings | 20-F | FY2025 (Dec 31) | 0001104659-26-050727 | `peers/PDD_20F_FY2025.txt` |
| PDD Holdings | 6-K EX-99.1 | Q1 2026 release (2026-05-28) / Q2 2026 release (2026-08-25) | 0001104659-26-067186 / 0001104659-26-100534 | `peers/PDD_6K_2026-05-28_ex991.txt`, `peers/PDD_6K_2026-08-25_ex991.txt` |

Artifacts: PDD 20-F text is full of zero-width-space characters (U+200B) between table cells (stripped before reading). PDD Q2 2026 release cash-flow table header reads "RMB RMB RMB RMB RMB RMB" where every other table in the release reads "RMB RMB US$"; the third and sixth columns are US$ by their magnitude. Walmart 10-K text carries HTML entities ("&#8226;", "&amp;").

---
## B.1 LATEST FULL FISCAL YEAR

### B.1a Revenue, growth, operating income

| Company / unit | Window | Revenue | Prior year | Growth | Operating income | Margin | Prior-year OI / margin | Source |
|---|---|---|---|---|---|---|---|---|
| **Amazon North America** | FY Dec-2025 | 426,305 | 387,497 | +10.0% (computed) | 29,619 | 6.9% (computed) | 24,967 / 6.4% | 10-K FY2025, Note 10 Segment Information |
| **Amazon International** | FY Dec-2025 | 161,894 | 142,906 | +13.3% (computed) | 4,750 | 2.9% | 3,792 / 2.7% | same |
| **Amazon NA + Intl combined** (computed) | FY Dec-2025 | 588,199 | 530,403 | +10.9% | 34,369 | 5.8% | 28,759 / 5.4% | computed from Note 10 |
| Amazon AWS (reconciling) | FY Dec-2025 | 128,725 | 107,556 | +19.7% | 45,606 | 35.4% | 39,834 / 37.0% | same |
| Amazon consolidated | FY Dec-2025 | 716,924 | 637,959 | +12.4% | 79,975 | 11.2% | 68,593 / 10.8% | same |
| **Walmart U.S.** (net sales) | FY Jan-31-2026 | 482,975 (total revenues 485,599) | 462,415 | +4.4% (computed) | 25,158 | 5.2% of net sales (computed) | 23,882 / 5.2% | 10-K FY2026, Note 11 Segments |
| **Walmart International** | FY Jan-31-2026 | 130,423 (TR 131,988) | 121,885 | +7.0% (filed "7.0 %") | 5,103 | 3.9% (filed) | 5,501 / 4.5% (filed) | 10-K, Note 11; MD&A segment table |
| **Sam's Club U.S.** | FY Jan-31-2026 | 93,015 (TR 95,540) | 90,238 | +3.1% (filed) | 2,442 | 2.6% (filed) | 2,404 / 2.7% (filed) | same |
| **Walmart consolidated** | FY Jan-31-2026 | net sales 706,413; total revenues 713,163 | 674,538 / 680,985 | +4.7% / +4.7% (filed) | 29,825 | 4.2% of net sales (filed) | 29,348 / 4.4% (filed) | 10-K MD&A "Consolidated Results of Operations" |
| **eBay** (net revenues) | FY Dec-2025 | 11,100 | 10,283 | +8% filed (+7.9% computed) | 2,277 | 20.5% (filed) | 2,318 / 22.5% (filed) | 10-K FY2025, income statement; MD&A |
| **MercadoLibre** (net revenues and financial income) | FY Dec-2025 | 28,893 | 20,777 | +39.1% (filed) | 3,201 | 11.1% (filed) | 2,631 / 12.7% (filed) | 10-K FY2025, MD&A |
| MELI Commerce revenues | FY Dec-2025 | 16,294 (commerce services 12,750; commerce products sales 3,544) | 12,159 | +34.0% (filed) | not filed by line | | | 10-K, Note 8 Segments disaggregation |
| MELI Fintech revenues | FY Dec-2025 | 12,599 | 8,618 | +46.2% (computed) | not filed by line | | | same |
| **Shopify** | FY Dec-2025 | 11,556 (subscription 2,752; merchant solutions 8,804) | 8,880 | +30.1% (computed); subscription +17% (filed) | 1,468 | 12.7% (computed) | 1,075 / 12.1% | 10-K FY2025, income statement |
| **PDD Holdings** (RMB) | FY Dec-2025 | RMB 431,845.7 (online marketing services and others 217,783.0; transaction services 214,062.7) | RMB 393,836.1 | +9.7% (computed) | RMB 93,102.1 | 21.6% (filed) | RMB 108,422.9 / 27.5% (filed) | 20-F FY2025, Item 5 results table (filed in RMB thousands; shown here in RMB millions) |

MELI files four geographic segments (Brazil, Mexico, Argentina, Other) measured by "direct contribution", not commerce vs fintech operating income; FY2025 direct contribution 5,903, margin 20.4% (filed). Walmart segment OI margins in the 10-K are on net sales; Amazon's are on net sales (no membership line).

### B.1b Capex and D&A, latest full year

| Company / unit | Capex (label as filed) | Capex / revenue (computed) | D&A (label as filed) | Capex / D&A (computed) | Source |
|---|---|---|---|---|---|
| Amazon consolidated | "Purchases of property and equipment" 131,819 (FY2024 82,999) | 18.4% of 716,924 | segment note "Total depreciation and amortization expense, by segment" 41,860; cash-flow line "Depreciation and amortization of property and equipment and capitalized content costs, operating lease assets, and other" 65,756 | 3.15x on 41,860; 2.00x on 65,756 | 10-K FY2025 cash flow statement; Note 10 |
| Amazon North America | segment "Total net additions to property and equipment" 35,919 (not cash capex; includes finance leases and accruals) | 8.4% of NA sales | 15,503 | 2.32x | Note 10 |
| Amazon International | net additions 7,617 | 4.7% of Intl sales | 4,907 | 1.55x | Note 10 |
| Amazon NA + Intl (computed) | net additions 43,536 | 7.4% | 20,410 | 2.13x | computed |
| Walmart U.S. | "Capital expenditures" 20,157 | 4.2% of net sales | 9,390 | 2.15x | 10-K FY2026, Note 11 |
| Walmart International | 3,197 | 2.5% | 2,304 | 1.39x | same |
| Sam's Club U.S. | 914 | 1.0% | 782 | 1.17x | same |
| Walmart consolidated | 26,642 (equals cash-flow "Payments for property and equipment") | 3.7% of total revenues | 14,203 | 1.88x | same |
| eBay | "Purchases of property and equipment" 525 | 4.7% | "Depreciation and amortization" 407 | 1.29x | 10-K FY2025 cash flow (pre-ASU 2025-06 basis; see Notes) |
| MercadoLibre | "Capital expenditures" 1,327 (KPI table; defined as "investments in property and equipment ... and intangible assets (excluding digital assets)") | 4.6% | 818 | 1.62x | 10-K FY2025 MD&A KPI table |
| Shopify | "Purchases of property and equipment" 26 | 0.2% | "Amortization and depreciation" 31 | 0.84x | 10-K FY2025 cash flow |
| PDD (RMB) | "Purchase of property, equipment and software and intangible assets" RMB 1,145.1 | 0.3% | "Depreciation and amortization" RMB 601.5 (separate line "Amortization of right-of-use assets" RMB 2,398.9 not included) | 1.90x | 20-F FY2025 cash flow statement |

Amazon segment allocation basis, verbatim (10-K FY2025, Note 10): "Technology infrastructure assets, which are included in property and equipment, net, net additions, and the depreciation and amortization expense on these assets, are allocated among the segments based on usage, with the majority allocated to the AWS segment." And: "Total net additions to property and equipment include technology infrastructure assets and the effect of non-cash activity such as property and equipment acquired but not yet paid."

Amazon FY2025 North America OI includes the FTC charge, verbatim (10-K FY2025): "During Q3 2025, we recorded $2.5 billion of expense related to the settlement of a lawsuit with the FTC. This charge was recorded in “Other operating expense (income), net” and impacted our North America segment."

---
## B.2 LATEST INTERIM (six months, stated windows)

| Company / unit | Window (6M) vs same window prior year | Revenue | Prior | Growth | OI / margin | Prior OI / margin | Capex (label) cur / prior | D&A cur / prior | Capex/D&A cur / prior (computed) | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Amazon North America | Jan-Jun 2026 vs Jan-Jun 2025 | 220,320 | 192,955 | +14.2% (filed "14 %") | 17,390 / 7.9% | 13,358 / 6.9% | net additions 23,265 / 16,368 | 8,780 / 7,272 | 2.65x / 2.25x | 10-Q Q2 2026, segment note |
| Amazon International | same | 81,986 | 70,274 | +16.7% (filed "17"; ex-FX filed "13") | 3,141 / 3.8% | 2,511 / 3.6% | net additions 4,267 / 4,037 | 2,570 / 2,316 | 1.66x / 1.74x | same |
| Amazon NA + Intl (computed) | same | 302,306 | 263,229 | +14.8% | 20,531 / 6.8% | 15,869 / 6.0% | 27,532 / 20,405 | 11,350 / 9,588 | 2.43x / 2.13x | computed |
| Amazon consolidated | same | 382,125 | 323,369 | +18.2% (filed "18") | 51,313 / 13.4% | 37,576 / 11.6% | cash purchases of P&E 98,411 / 57,202 (25.8% / 17.7% of sales) | segment D&A 26,703 / 18,822; cash-flow D&A line 38,933 / 29,489 | 3.69x / 3.04x (segment D&A); 2.53x / 1.94x (cash-flow line) | 10-Q cash flow statement |
| Walmart U.S. | Feb-Jul 2026 vs Feb-Jul 2025 | 242,358 | 233,074 | +4.0% (computed) | 14,017 / 5.8% | 12,428 / 5.3% | 10,453 / 8,547 | 5,111 / 4,539 | 2.05x / 1.88x | 10-Q Q2 FY2027, segments note |
| Walmart International | same | 70,308 | 60,955 | +15.3% (filed) | 3,041 / 4.3% (filed) | 2,527 / 4.1% (filed) | 1,812 / 1,227 | 1,263 / 1,121 | 1.43x / 1.09x | same |
| Sam's Club U.S. | same | 49,118 | 45,702 | +7.5% (computed) | 1,352 / 2.8% | 1,136 / 2.5% | 664 / 338 | 408 / 384 | 1.63x / 0.88x | same |
| Walmart consolidated | same | net sales 361,784; TR 365,688 | 339,731 / 343,011 | +6.5% / +6.6% (filed) | 16,876 / 4.7% (filed) | 14,421 / 4.2% (filed) | 14,181 / 11,409 (3.9% / 3.3% of TR) | 7,746 / 6,856 | 1.83x / 1.66x | same; MD&A |
| eBay | Jan-Jun 2026 vs Jan-Jun 2025 | 6,223 | 5,315 | +17% (filed) | 1,287 / 20.7% | 1,090 / 20.5% | 295 / 212 | 194 / 131 | 1.52x / 1.62x | 10-Q Q2 2026 (prior year recast for ASU 2025-06) |
| MercadoLibre | same | 19,014 | 12,725 | +49.4% (filed) | 1,294 / 6.8% (filed) | 1,588 / 12.5% (filed) | 712 / 543 | 538 / 371 | 1.32x / 1.46x | 10-Q Q2 2026, KPI table and income statement |
| MELI Commerce / Fintech | same | 10,630 / 8,384 | 7,142 / 5,583 | +48.8% (filed) / +50.2% (filed) | not filed by line | | | | | 10-Q Note 6 |
| Shopify | same | 6,753 (sub 1,552; merchant 5,201) | 5,040 | +34.0% (computed) | 870 / 12.9% | 494 / 9.8% | 9 / 10 | 14 / 16 | 0.64x / 0.62x | 10-Q Q2 2026 |
| PDD (RMB) | same | RMB 218,587 (OMS 107,573; TS 111,014) | RMB 199,657 (OMS 104,425; TS 95,232) | +9.5% (computed) | RMB 47,330 / 21.7% | RMB 41,879 / 21.0% | not in release | not in release | not obtained | 6-K Q2 2026 EX-99.1, six-month columns (unaudited) |

Walmart 10-Q restated prior-period segment OI, verbatim: "Beginning in February 2026, the Company updated its segment allocation methodology for certain corporate overhead allocations and, accordingly, revised the prior period amounts for comparability."
Latest quarter only, for reference: Amazon Q2 2026 NA 116,177 (+16% filed), OI 9,123; Intl 42,197 (+15% filed), OI 1,717. Walmart Q2 FY2027 (May-Jul 2026) Walmart U.S. 125,189, OI 8,120; International 35,198 (+12.8% filed), OI 1,439; Sam's 25,713, OI 678. PDD Q2 2026 revenue RMB 112,358 (+8% filed), OI RMB 27,764 (+8% filed).

---
## B.3 MARKETPLACE METRICS

### B.3a GMV, take rate, buyers, items

| Company | Window | GMV (label) | GMV growth | Take-rate measure | Buyers / items | Source |
|---|---|---|---|---|---|---|
| eBay | FY2025 | "GMV" 79,609 (FY2024 74,667) | +7% filed (+6.6% computed); FX-neutral +6% filed | filed "Take rate" 13.94% (FY2024 13.77%), defined "net revenues divided by GMV". Marketplace revenues / GMV = 9,107 / 79,609 = 11.4% (computed; FY2024 8,648 / 74,667 = 11.6%) | "135 million active buyers and 2.5 billion live listings" | 10-K FY2025 Item 1 and MD&A |
| eBay | 6M 2026 vs 6M 2025 | 44,595 vs 38,267 | +17% filed; FX-neutral +14% | filed take rate 13.95% vs 13.89%; marketplace revenues / GMV 5,046 / 44,595 = 11.3% vs 4,391 / 38,267 = 11.5% (computed) | "eBay's 136 million buyers worldwide" (10-Q MD&A overview) | 10-Q Q2 2026 MD&A |
| MercadoLibre | FY2025 | "Gross merchandise volume" 65,037 (FY2024 51,467) | +26.4% (filed, MD&A) | Commerce services / GMV = 12,750 / 65,037 = 19.6% (computed; FY2024 10,076 / 51,467 = 19.6%). Numerator "Commerce services" = "final value fees and flat fees paid by sellers derived from intermediation services and related shipping and storage fees, classified fees derived from classified advertising services, ad sales and membership subscription fees" (so it includes ads, shipping, subscriptions; GMV excludes Classifieds). MELI files no take rate. | Unique active buyers 121 million (FY2024 100); items sold 2,429 million (FY2024 1,787) | 10-K FY2025 KPI table; Note 8 |
| MercadoLibre | 6M 2026 vs 6M 2025 | 40,877 vs 28,588 | +43% (filed, MD&A) | Commerce services / GMV = 8,057 / 40,877 = 19.7% vs 5,729 / 28,588 = 20.0% (computed) | Unique active buyers 117 vs 90 million; items sold 1,517 vs 1,042 million | 10-Q Q2 2026 KPI table; Note 6 |
| Shopify | FY2025 | "Gross Merchandise Volume" 378,441 (FY2024 292,275) | +29.5% (computed) | Revenue / GMV 3.1% (FY2024 3.0%); merchant solutions / GMV 2.3% (FY2024 2.2%) (computed). Shopify files no take rate; GMV includes "certain apps and channels for which a revenue-sharing arrangement is in place". MRR 205 (+15% filed) | not filed (no buyer count found) | 10-K FY2025 MD&A KPIs |
| Shopify | 6M 2026 vs 6M 2025 | 216,310 vs 162,587 | +33.0% (computed) | Revenue / GMV 3.1% vs 3.1%; merchant solutions / GMV 2.4% vs 2.3% (computed); MRR 221 vs 185 | not filed | 10-Q Q2 2026 |
| PDD | FY2025 / 6M 2026 | not filed (no instance of "GMV" or "gross merchandise" in the 20-F or either 6-K release) | | not computable | not filed | |
| Walmart | FY2026 / 6M FY2027 | GMV not filed; marketplace revenue not filed | | not computable | not filed | |
| Amazon | FY2025 / 6M 2026 | GMV not filed | | not computable (3P seller services revenue is filed, GMV is not) | "WW paid units" growth and seller unit mix filed in EX-99.1 only (below) | |

### B.3b Walmart eCommerce (dollar amounts are FILED in the 10-K/10-Q disaggregated revenue note; growth computed)

Definition, verbatim (10-K FY2026, Note 11 "Disaggregated Revenues"): "Net sales related to eCommerce include omnichannel sales where a customer initiates an order digitally and the order is fulfilled through a store or club, as well as net sales from other business offerings that are part of the Company's ecosystem such as certain advertising arrangements, fulfillment services, and data insights."

| Walmart eCommerce net sales ($bn, filed "approximately") | FY2026 | FY2025 | FY2024 | Growth FY26 (computed) | 6M FY27 | 6M FY26 | Growth (computed) | Q2 FY27 / Q2 FY26 | Filed growth in EX-99.1 (quarter) |
|---|---|---|---|---|---|---|---|---|---|
| Walmart U.S. | 99.6 | 79.3 | 65.4 | +25.6% | 56.4 | 45.1 | +25.1% | 29.4 / 23.7 (+24.1%) | Q4 FY26 "eCommerce sales up 27%"; Q2 FY27 "eCommerce sales increased 24%" |
| International | 35.8 | 29.5 | 24.8 | +21.4% | 19.6 | 16.0 | +22.5% | 9.9 / 8.3 (+19.3%) | Q4 FY26 "eCommerce sales up 17% in Q4"; Q2 FY27 "eCommerce sales up 19%" |
| Sam's Club U.S. | 15.0 | 12.1 | 9.9 | +24.0% | 8.8 | 7.1 | +23.9% | 4.7 / 3.7 (+27.0%) | Q4 FY26 "eCommerce sales up 23%"; Q2 FY27 "eCommerce sales up 26%" |
| Total (computed sum) | 150.4 | 120.9 | 100.1 | +24.4% (21.3% of net sales) | 84.8 | 68.2 | +24.3% (23.4% of net sales) | 44.0 / 35.7 (+23.2%) | Q4 FY26 "Global eCommerce sales grew 24%"; Q2 FY27 "Global eCommerce sales grew 23%, led by store-fulfilled pickup & delivery and marketplace" |

Walmart U.S. eCommerce contribution to comparable sales (10-K FY2026 MD&A, filed): "Walmart U.S. eCommerce sales positively contributed approximately 4.3% and 2.9% to comparable sales for fiscal 2026 and 2025, respectively." Walmart marketplace offering, verbatim (10-K Item 1): "Other offerings in the Walmart U.S. business include advertising solutions for brands and online marketplace sellers, supply chain and fulfillment capabilities to online marketplace sellers, and data analytics and insights for suppliers and brands."

### B.3c Amazon third-party seller services revenue (net basis)

Footnote (3), verbatim: "Includes commissions and any related fulfillment and shipping fees, and other third-party seller services."

| Year | 3P seller services | Growth (computed) | Source (Note, "Net sales by groups of similar products and services") |
|---|---|---|---|
| FY2020 | 80,461 | +49.7% (vs FY2019 53,762) | 10-K FY2021, acc 0001018724-22-000005 |
| FY2021 | 103,366 | +28.5% | 10-K FY2021; same figure in FY2022 and FY2023 10-Ks |
| FY2022 | 117,716 | +13.9% | 10-K FY2022, acc 0001018724-23-000004 |
| FY2023 | 140,053 | +19.0% | 10-K FY2023, acc 0001018724-24-000008 |
| FY2024 | 156,146 | +11.5% | 10-K FY2025 |
| FY2025 | 172,162 | +10.3% | 10-K FY2025, acc 0001018724-26-000004 |
| 6M 2026 vs 6M 2025 | 88,358 vs 76,860 | +15.0% | 10-Q Q2 2026, acc 0001018724-26-000026 |
| Q2 2026 vs Q2 2025 | 46,780 vs 40,348 | +15.9% computed; Y/Y filed "16 %"; ex-F/X filed "16 %" | 10-Q; EX-99.1 Q2 2026 |

3P seller services ex-F/X Y/Y growth, filed quarterly (EX-99.1 Q4 2025 and Q2 2026 supplemental tables): Q3 2024 10%; Q4 2024 9%; Q1 2025 7%; Q2 2025 10%; Q3 2025 11%; Q4 2025 10%; Q1 2026 12%; Q2 2026 16%.

### B.3d Amazon seller share of units: FILED, in EX-99.1 releases only

Line as printed: "WW seller unit mix -- % of WW paid units (7)"; footnote (7): "Excludes the impact of Whole Foods Market."

| Quarter | Seller unit mix, % of WW paid units (filed) | WW paid units Y/Y growth (filed) | Release(s) carrying it |
|---|---|---|---|
| Q2 2024 | 61% | 11% | EX-99.1 Q3 2025 |
| Q3 2024 | 60% | 12% | Q3 2025, Q4 2025 |
| Q4 2024 | 62% | 11% | Q3 2025 to Q1 2026 |
| Q1 2025 | 61% | 8% | Q3 2025 to Q2 2026 |
| Q2 2025 | 62% | 12% | Q3 2025 to Q2 2026 |
| Q3 2025 | 62% | 11% | Q3 2025 to Q2 2026 |
| Q4 2025 | 61% | 12% | Q4 2025 (acc 0001018724-26-000002) to Q2 2026 |
| Q1 2026 | 60% | 15% | Q1 2026, Q2 2026 |
| Q2 2026 | 61% | 17% | Q2 2026 (acc 0001018724-26-000024) |

Overlapping quarters agree across all four releases (checked). Definitions, verbatim (EX-99.1 Q2 2026, "Certain Definitions"): "References to units mean physical and digital units sold (net of returns and cancellations) by us and sellers in our stores as well as Amazon-owned items sold in other stores. Units sold are paid units and do not include units associated with AWS, certain acquisitions, certain subscriptions, rental businesses, or advertising businesses, or Amazon gift cards." / "References to sellers means seller accounts, which are established when a seller receives an order from a customer account."
Search run: regexes "paid units"; "(third-party|independent|marketplace) sellers? ... digit %"; "digit % ... sellers"; "units (sold|shipped) ... (third-party|seller)" over all 26 AMZN text files on disk (10-Ks FY2015, FY2017 to FY2025; 10-Qs Q3 2025, Q1 2026, Q2 2026; four EX-99.1; four 8-Ks; DEF 14A; 424B3; 424B5; 425). No instance of a seller unit share in any 10-K or 10-Q; the four EX-99.1 files are the only carriers.

---
## B.4 ADVERTISING AND MEMBERSHIP

### Amazon (Note "Net sales by groups of similar products and services", 10-K of the year named in B.3c; 10-Q Q2 2026)

Footnote (4): "Includes sales of advertising services to sellers, vendors, publishers, authors, and others, through programs such as sponsored ads, display, and video advertising." Footnote (5): "Includes annual and monthly fees associated with Amazon Prime memberships, as well as digital video, audiobook, digital music, e-book, and other non-AWS subscription services."

| Year | Advertising services | Growth (computed) | Subscription services | Growth (computed) |
|---|---|---|---|---|
| FY2020 | 19,773 | | 25,207 | |
| FY2021 | 31,160 | +57.6% | 31,768 | +26.0% |
| FY2022 | 37,739 | +21.1% | 35,218 | +10.9% |
| FY2023 | 46,906 | +24.3% | 40,209 | +14.2% |
| FY2024 | 56,214 | +19.8% | 44,374 | +10.4% |
| FY2025 | 68,635 | +22.1% | 49,619 | +11.8% |
| 6M 2026 vs 6M 2025 | 37,052 vs 29,615 | +25.1% | 27,157 vs 23,923 | +13.5% |
| Q2 2026 vs Q2 2025 | 19,809 vs 15,694 | +26.2% computed; ex-F/X filed "26 %" | 13,730 vs 12,208 | +12.5% computed; ex-F/X filed "12 %" |

In the FY2020 10-K advertising sat inside "Other"; the FY2021 10-K first shows an "Advertising services" line and recasts 2019 (12,625) and 2020 (19,773).

### Walmart
- Advertising dollar revenue: filed in the earnings release only. Q4 FY2026 release (8-K 0000104169-26-000032), Full Year Highlights: "Global advertising business 3 grew 46% to nearly $6.4 billion, including VIZIO". Footnote 3: "Our global advertising business is recorded in either net sales or as a reduction to cost of sales, depending on the nature of the advertising arrangement." (The "3" is a superscript footnote marker flattened into the text.)
- Q4 FY2026: "Global advertising business 3 up 37%, including VIZIO; Walmart Connect in the U.S. up 41%"; Walmart U.S.: "Strong advertising growth continued, including 41% increase in Walmart Connect sales (ex-VIZIO)"; International: "Q4 advertising business 3 grew 10%, with full year increasing 19%".
- Q2 FY2027 release (8-K 0000104169-26-000145): "Global advertising business 3 up 38%, with strength across segments. Walmart U.S. advertising up 38%"; Walmart U.S.: "Strong advertising growth continued, up 38% overall, including 43% increase in Walmart Connect (ex-VIZIO)"; International: "Advertising business 3 grew 20%, led by Flipkart Ads".
- 10-Q Q2 FY2027 MD&A (filed): "Gross profit rate also benefited from continued growth in higher margin businesses, including advertising."
- Membership: "Membership and other income" FY2026 6,750 (FY2025 6,447): Walmart U.S. 2,624; International 1,565; Sam's Club U.S. 2,525; Corporate 36 (10-K Note 11). Membership fee revenue, verbatim (10-K, accounting policies note, "Membership and Other Income"): "Membership fee revenue was $ 4.4 billion, $ 3.8 billion and $ 3.1 billion for fiscal 2026, 2025 and 2024, respectively." (+15.8% computed on rounded figures.) Release: Q4 FY26 "Membership fee revenue grew 15.1% globally"; Q2 FY27 "Membership fee revenue grew 17% globally". 10-K MD&A Walmart U.S.: "In both years, the increases were primarily driven by double-digit growth in membership fee revenue from Walmart+." Walmart+ member count and fee: no instance found (see B.7).

### eBay
Advertising revenues (10-K FY2025 MD&A): 1,993 (FY2024 1,635), "22 %" filed; footnote: "Beginning January 1, 2025, we began classifying certain immaterial revenues previously reported as Marketplace revenues as Advertising revenues ... Under this updated basis of presentation, Marketplace and Advertising revenues would have been $8,592 million and $1,691 million, respectively, for 2024" (ellipsis marks an omitted sentence fragment). Like-for-like growth 1,993 / 1,691 = +17.9% (computed). Definition: "Advertising revenues primarily consist of fees charged to sellers to promote their listings on our Marketplace platforms, as well as third-party advertising fees." 6M 2026: 1,177 vs 924, "27 %" filed. The 10-K does not split first-party from third-party ad dollars; risk factor: "We generate a meaningful amount of our revenue from our Promoted Listings (a first-party advertising offering) and, to a lesser extent, third-party advertising."

### MercadoLibre
Advertising revenue amount: not filed. "ad sales" sits inside "Commerce services" (footnote (1) quoted in B.3a). Search: "Mercado Ads", "ad sales ... digit", "advertising ... (grew|increase|growth)" in 10-K and 10-Q; no dollar or growth figure found. Subscription: "subscription fees associated with MELI+ memberships" also inside Commerce services; no separate amount found.

### Shopify
No advertising or membership revenue line. Subscription solutions 2,752 FY2025 (+17% filed), 1,552 6M 2026 vs 1,276.

### PDD (RMB)
"Online marketing services and others" (PDD's marketing-services line, not split between ads and other): FY2025 RMB 217,783.0 (FY2024 197,934.2; +10.0% computed); 6M 2026 RMB 107,573 vs 104,425 (+3.0% computed). Transaction services FY2025 RMB 214,062.7 (+9.3% computed); 6M 2026 RMB 111,014 vs 95,232 (+16.6% computed).

---
## B.5 FEES AND PRICE CONDUCT (verbatim)

### (a) Amazon statements of raising or changing seller, fulfillment, referral or Prime fees

**No instance found.** Search: regexes "membership fee", "fulfillment fee", "referral fee", "seller fee", "fees (charged|paid) (to|by) sellers", "increase(s/d) (in|of) (the) (price|fee)", "Prime (membership) (price|fee)", "price of (an) (Amazon) Prime", "(increas|chang|rais|higher)... fees", "fees ... (increas|chang|rais|higher)", "Prime ... pric", "pric... Prime", dollar amounts "$79 / $99 / $119 / $139 / $14.99 / $12.99 / $8.99", "$1xx per year", "$x.xx per month", over the AMZN 10-Ks FY2015, FY2017 to FY2025, 10-Qs Q3 2025, Q1 2026, Q2 2026, and the four EX-99.1 releases. Every hit is either a revenue-recognition description or cost-side (interchange fees, professional fees). The only price amount found was Alexa+ (EX-99.1 Q4 2025): "Announced that Alexa+ is available to all customers in the U.S. for $19.99 per month as a standalone subscription, and free for Prime members." The Prime fee history with amounts is not stated in any document on disk.

What the filings do say about fees:
- 10-K FY2025 Item 1, "Sellers": "We offer programs that enable sellers to grow their businesses, sell their products in our stores, and fulfill orders using our services. We are not the seller of record in these transactions. We earn fixed fees, a percentage of sales, per-unit activity fees, interest, or some combination thereof, for our seller programs."
- 10-Q Q2 2026 MD&A: "Service sales primarily represent third-party seller fees, which include commissions and any related fulfillment and shipping fees, AWS sales, advertising services, Amazon Prime membership fees, and certain digital media content subscriptions."
- 10-K FY2018 (`10K_filed2019.txt`), ASU adoption: "The impact of applying this ASU for the year ended December 31, 2018 primarily resulted in a decrease in product sales and an increase in service sales driven by the reclassification of Prime membership fees of approximately $3.8 billion ." (space before period is in the text)

### (b) FTC and Prime-related matters in Amazon's Legal Proceedings

10-Q Q2 2026 (Commitments and Contingencies note, "Legal Proceedings"), and near-identical in 10-K FY2025 (same note), verbatim:
"Since March 2020, private litigants, state Attorneys General, and the Federal Trade Commission have filed cases in the U.S., Canada, and the United Kingdom alleging, among other things: price fixing arrangements between each of Amazon and its vendors and Amazon and its third-party sellers; abuse of dominance, monopolization, and attempted monopolization; and consumer protection and unjust enrichment claims, in violation of federal and state antitrust, state consumer protection, and Canadian and U.K. antitrust laws. ... These complaints seek billions of dollars of alleged damages, treble damages, punitive damages, injunctive relief, structural relief, civil penalties, attorneys’ fees, and costs. ... Some of the cases include allegations that Amazon has a monopoly in markets for online superstores, marketplace services, or intermediation services and that we unlawfully engage in anticompetitive practices relating to our pricing policies, selection of the Featured Offers, use of seller data, advertising practices, the structure of Prime, and promotion of our own products on our website. In the U.S., most of Amazon’s motions to dismiss were granted in part, but in each case, at least some of the claims survived. ... In the United Kingdom, two class actions have been certified and a third is pre-certification. In the U.S., one class action has been certified, and three others are pre-certification. We dispute the allegations of wrongdoing and intend to defend ourselves vigorously in these matters."
(Ellipses mark omitted sentences. Difference between the two filings: the 10-K FY2025 says "Two Canadian class actions before other courts are pre-certification"; the 10-Q Q2 2026 says "Three Canadian class actions before other courts are pre-certification.")

The FTC's own antitrust complaint as described separately in the 10-K FY2024 (acc 0001018724-25-000004), verbatim: "The Federal Trade Commission and a number of state Attorneys General filed a similar lawsuit in September 2023 in the W.D. Wash. alleging violations of federal antitrust and state antitrust and consumer protection laws. That complaint alleges, among other things, that Amazon has a monopoly in markets for online superstores and marketplace services, and unlawfully maintains those monopolies through anticompetitive practices relating to our pricing policies, advertising practices, the structure of Prime, and promotion of our own products on our website. The complaint seeks injunctive and structural relief, an unspecified amount of damages, and costs." And: "In September 2024, the United States District Court for the W.D. Wash. granted in part Amazon's motion to dismiss the suit brought by the FTC and certain state Attorneys General with respect to five state law claims and denied the motion with respect to the remaining claims." Also filed there: "All three courts dismissed claims alleging that Amazon's pricing policies are inherently illegal and denied dismissal of claims alleging that Amazon's pricing policies are an unlawful restraint of trade."
The 10-K FY2025 and 10-Q Q2 2026 no longer describe the FTC suit separately; no trial date, judgment or settlement of that antitrust suit is stated in either.

FTC settlement (amount filed; subject NOT named): 10-Q Q3 2025 (acc 0001018724-25-000123): "During Q3 2025, we recorded $ 2.5 billion of expense related to the settlement of a lawsuit with the Federal Trade Commission (FTC). This charge was recorded in “Other operating expense (income), net” and impacted our North America segment." and "We expect to use cash on hand to satisfy the settlement of the FTC lawsuit." EX-99.1 Q3 2025: "$2.5 billion related to a legal settlement with the Federal Trade Commission". No document on disk states which FTC lawsuit was settled or whether it concerned Prime (searched "Federal Trade Commission ... Prime", "Prime ... Federal Trade Commission", "Restore Online", "ROSCA", "enroll... Prime", "Prime ... cancel", "June 2023", "settle... (Prime|FTC)" across all 26 AMZN files).

Prime in the risk factors, verbatim (10-Q Q2 2026 Item 1A; same in 10-K FY2025): "Additionally, we face a number of open investigations based on claims that aspects of our operations infringe competition-related or consumer protection rules or regulations, including aspects of Amazon’s operation of its stores, including its fulfillment network and Prime, and certain aspects of AWS’s offering of cloud services."

Seller-related competition decision (10-K FY2025, Legal Proceedings), verbatim: "In December 2021, the Italian Competition Authority (the “ICA”) issued a decision against Amazon Services Europe S.à r.l., Amazon Europe Core S.à r.l., Amazon EU S.à r.l., Amazon Italia Services S.r.l., and Amazon Italia Logistica S.r.l. claiming that certain of our marketplace and logistics practices in Italy infringe EU competition rules. The decision imposes remedial actions and a fine of €1.13 billion, which we have paid and will seek to recover pending conclusion of all appeals. In September 2025, the Italian Administrative Tribunal (the “TAR”) affirmed the ICA's decision but reduced the fine to €752 million. In December 2025, we appealed the TAR's ruling."

### (c) Peers on fees, take rate, and multi-channel selling

- **eBay**, 10-K FY2025 MD&A: "Net revenues increased during 2025 compared to 2024 primarily due to higher GMV, increased penetration of first party advertising and the ramping of our U.K. shipping program. The increase in net revenues was partially offset by lower fees in connection with our U.K. consumer-to-consumer initiative." Also: "Changes in return and cancellation rates can impact our GMV growth rate and related take rate." 10-Q Q2 2026 MD&A: "Net revenues increased during the three and six months ended June 30, 2026 compared to the same period in 2025 primarily due to higher GMV, increased first party advertising penetration, and higher volume and favorable rates associated with our U.S. net shipping program. The increase in first party advertising revenue was driven by increased adoption and attribution changes that enhanced our ability to convert first-party ads, which increased monetization during the period."
- **eBay** on multi-channel sellers (10-K FY2025, Item 1A, "We face intense competition that may materially harm our business."): "Sellers may also choose to sell their goods through alternative channels, such as multi-channel services like Shopify or social media platforms. Consumers and sellers also can create and sell through their own sites and may choose to purchase online advertising instead of using our services or paying for our advertising products."
- **MercadoLibre**, 10-K FY2025 MD&A: "an increase of $2,674 million in Commerce services revenues mainly related to a 26.4% increase in gross merchandise volume and higher flat fee contributions for low gross merchandise volume transactions." Margin effect of a shipping-price change: "our operating margin decreased from a margin of 12.7% to a margin of 11.1%. This decrease is mainly explained by the reduction of our free shipping threshold in Brazil, together with an increase in provision of doubtful accounts, driven by the expansion of our credit card portfolio, ..." 10-Q Q2 2026: "our operating income margin decreased from 12.5% and 12.2% to 6.8% and 6.7%, respectively. This decrease is mainly explained by the reduction of our free shipping threshold in Brazil, together with an increase in our shipping operating costs, our cost of net revenues and financial expenses and our provision of doubtful accounts, ..." Fee structure: "Final value fees represent a percentage of the sale value that is charged to the seller once an item is successfully sold and flat fees represent a fixed charge for certain transactions below a certain merchandise value". Multi-channel: no instance found ("multiple (channels|marketplaces|platforms)", "sell (through|on|across) (multiple|other)" in 10-K and 10-Q).
- **Shopify**, 10-K FY2025 Item 1A: "We have changed our pricing models from time to time and expect to do so in the future. Such changes may not yield expected benefits to our business and financial results and could also negatively affect the willingness of merchants to use our products and services. ... Moreover, our merchants may be sensitive to changes in our pricing models compared to prices offered by our competitors. As a result, our pricing decisions may result in loss of market share and in the future we may be required to reduce our prices ...". MD&A: "In the year ended December 31, 2025, the MRR growth rate for the period was lower than the same period in 2024 driven by the impact of extending the length of paid trials." Multi-channel, Item 1: "Shopify offers them the tools to seamlessly manage, market and sell their products across various sales channels, including online storefronts, physical retail spaces, AI platforms, social media and more." Competition factors include "integration of multiple sales channels". **Amazon arrangement ("Buy with Prime"): no instance found**; "amazon" (case-insensitive) and "Prime" return 0 hits in both the 10-K FY2025 and 10-Q Q2 2026.
- **PDD**: no fee-change statement found in the 20-F FY2025 (searched "(fee|commission)s? ... (reduc|lower|cut|waiv|support)", "(reduc|lower|cut|waiv)... (fees|commission)"); hits are cost-side only. Revenue-line description: "We charge merchants fees for transaction-related services that we provide to merchants on our platforms." Q2 2026 release, VP Finance: "We stepped up our ecosystem investments in the second quarter, ... At this stage, our priority is helping merchants thrive and strengthening the broader industry ecosystem." (curly quote marks in the release render as separated “ ” characters in the strip). Q1 2026 release, Co-CEO: "We will commit significant resources to building the first-party brand business, unlocking new opportunities for our supply chain partners, and driving exceptional value for our customers."
- **Walmart Marketplace**: no fee or take-rate statement found in the 10-K FY2026, 10-Q Q2 FY2027 or the two releases (searched "(marketplace|seller) ... fees?", "fees? ... (marketplace|seller)", "take rate", "multiple (channels|marketplaces)").

---
## B.6 DOES THE LATEST ANNUAL FILING NAME AMAZON AS A COMPETITOR?

| Company | Filing | "Amazon" hits | Names Amazon as competitor? |
|---|---|---|---|
| Walmart | 10-K FY2026 (also checked 10-K FY2025, 10-Q Q2 FY2027, both releases) | 0 in every file | No. No competitor is named. |
| eBay | 10-K FY2025 | 2 | Yes, twice, in Item 1A |
| MercadoLibre | 10-K FY2025 | 2 | Not in the Item 1 Competition section. Named once in a regulatory antitrust passage and once as a cloud vendor. |
| Shopify | 10-K FY2025 | 0 (case-insensitive) | No |
| PDD | 20-F FY2025 | 0 (case-insensitive; also 0 in both 6-K releases) | No. Competitors described only by category. |

**Walmart** 10-K FY2026, Item 1 "Competition": "We compete with brick and mortar, eCommerce and omnichannel retailers operating discount, department, retail and wholesale grocery, drug, dollar, variety and specialty stores, supermarkets, supercenter-type stores, membership-only warehouse clubs, gasoline stations and social commerce platforms, as well as companies that offer services in digital advertising, fulfillment and delivery services, health and wellness and financial services."

**eBay** 10-K FY2025, Item 1A, under "We face intense competition that may materially harm our business.":
1. "We may not be able to engage consumers as effectively as our large competitors with broad ecosystems – Some of our competitors, such as Alibaba, Alphabet (Google), Amazon, Apple and Meta (Facebook and Instagram), are larger than we are, have greater resources, have a dominant and secure position in other industries or certain significant markets, or offer other goods and services and product ecosystems to consumers and merchants that we do not offer, which can drive consumers to, and keep them locked-in to, their platforms instead of using ours."
2. "We may not keep up with seller expectations – Consumers and merchants that sell goods on our platforms also have many alternatives, including general ecommerce marketplaces, such as Amazon and Alibaba, and more specialized marketplaces that focus on discrete categories of products."
Item 1 "Competition" names no company: "Our users can list, sell, buy and pay for similar items through a variety of competing online, mobile and offline channels."

**MercadoLibre** 10-K FY2025. Item 1 "Competition" (no company named): "While we are currently the market leader in a number of the markets in which we operate, we currently or potentially could compete with marketplace operators, businesses that offer business-to-consumer online e-commerce services or others with a focus on specific vertical categories, as well as brick and mortar retailers that have launched online offerings. Over the past few years, we have seen competition intensify not only as local players grow their e-commerce businesses, but also as international players expand, mainly in Brazil and Mexico." The two Amazon mentions: (i) regulation section headed "Competition": "The authority identified potential concerns related to the operation of Buy Box algorithms and the integration of logistics services by Amazon Mexico and Mercado Libre, however, no corrective measures were imposed and the proceeding was closed." (ii) Item 1A: "our cloud providers, the largest of which are Amazon Web Services and Google Cloud Platform."

**Shopify** 10-K FY2025, Item 1 "Competition" (no company named): "Additionally, some merchants may select one or more integrated or standalone offerings from other providers such as: • ecommerce software vendors; • content management systems; • payment processors; • point of sale providers; • domain registrars; • shipping label providers; • fulfillment service providers; • alternative lenders; • financial services; • cross-border services providers; and • marketplaces."

**PDD** 20-F FY2025, Item 4 "Competition" (no company named): "The e-commerce industry in which we compete is intensely competitive, and our platforms compete on a global scale with industry players such as (i) major e-commerce operators, (ii) major traditional and brick-and-mortar retailers, (iii) retail companies focused on specific product categories, and (iv) major internet companies that do not operate e-commerce businesses now but are in the process of initiating their e-commerce businesses or may launch e-commerce businesses in the future."

**Amazon's own** 10-K FY2025, Item 1 "Competition", verbatim in full:
"Our businesses encompass a large variety of product types, service offerings, and delivery channels. The worldwide marketplace in which we compete is evolving rapidly and intensely competitive, and we face a broad array of competitors from many different industry sectors around the world. Our current and potential competitors include: (1) physical, e-commerce, and omnichannel retailers, publishers, vendors, distributors, manufacturers, and producers of the products we offer and sell to consumers and businesses; (2) publishers, producers, and distributors of physical, digital, and interactive media of all types and all distribution channels; (3) web search engines, comparison shopping websites, social networks, web portals, virtual assistants, and other online and app-based means of discovering, using, or acquiring goods and services, either directly or in collaboration with other retailers, including through artificial intelligence; (4) companies that provide e-commerce services, including website development and hosting, omnichannel sales, inventory and supply chain management, advertising, fulfillment, customer service, and payment processing; (5) companies that provide fulfillment and logistics services for themselves or for third parties, whether online or offline; (6) companies that provide information technology services or products, including on-premises or cloud-based infrastructure, tools and services relating to artificial intelligence, and other services; (7) companies that design, manufacture, market, or sell consumer electronics, communications, and other electronic devices and services; (8) companies that sell grocery products online and in physical stores; (9) companies that provide advertising services, whether in digital or other formats; and (10) providers of virtual or in-person healthcare services. We believe that the principal competitive factors in our retail businesses include selection, price, and convenience, including fast and reliable fulfillment. Additional competitive factors for our seller and enterprise services include the quality, speed, and reliability of our services and tools, as well as customers' ability and willingness to change business practices. Some of our current and potential competitors have greater resources, longer histories, more customers, greater brand recognition, and greater control over inputs critical to our various businesses. They may secure better terms from suppliers, adopt more aggressive pricing, pursue restrictive distribution agreements that restrict our access to supply, direct consumers to their own offerings instead of ours, lock-in potential customers with restrictive terms, and devote more resources to technology, infrastructure, fulfillment, and marketing. The internet and other technologies including artificial intelligence facilitate competitive entry and comparison shopping, which enhances the ability of new, smaller, or lesser-known businesses to compete against us. Each of our businesses is also subject to rapid change and the development of new business models and the entry of new and well-funded competitors. Other companies also may enter into business combinations or alliances that strengthen their competitive positions."
Amazon names no competitor in that paragraph.

---
## B.7 NOT OBTAINED

| Metric | Company | Search run (files) | Result |
|---|---|---|---|
| GMV / GMS | Amazon | "GMV", "gross merchandise" in all 26 AMZN files | no instance found |
| Take rate | Amazon, Walmart, PDD | not computable without a filed GMV | not obtained |
| Seller fee, fulfillment fee, referral fee or Prime fee changes, and Prime fee history with amounts | Amazon | see B.5(a) search list | no instance found |
| Subject of the Q3 2025 $2.5bn FTC settlement (Prime or otherwise) | Amazon | see B.5(b) search list | not stated in any file on disk |
| Segment cash capex | Amazon | Note 10 files "net additions" only | not filed; net additions used, labelled |
| Walmart marketplace / fulfillment services revenue, GMV | Walmart | "marketplace", "seller", "fees", "take rate" in 10-K FY2026, 10-Q Q2 FY27, two releases | not filed |
| Walmart advertising revenue in 10-K/10-Q | Walmart | "advertising" in 10-K FY2026 and 10-Q | only in releases (8-K EX-99.1); 10-K/10-Q carry advertising costs and qualitative statements |
| Walmart+ member count, fee, revenue | Walmart | "Walmart+" in 10-K FY2026, 10-Q, releases | not quantified; "double-digit growth" and "record second quarter high" net adds only |
| VIZIO revenue or standalone growth | Walmart | "VIZIO" in 10-K FY2026, 10-Q, releases | not filed; growth stated "including VIZIO" and Walmart Connect "(ex-VIZIO)" |
| Flipkart GMV, revenue, or ad revenue amount | Walmart | "Flipkart" in 10-K FY2026, 10-Q, releases | not filed; "led by Flipkart Ads" only |
| Walmart global eCommerce growth for the full year as a filed % | Walmart | Q4 FY26 release Full Year Highlights | not filed (quarter only); computed from 10-K dollars in B.3b |
| First-party vs third-party ad revenue split | eBay | "first-party advertising", "Promoted Listings" in 10-K, 10-Q | not filed |
| Advertising revenue; MELI+ subscription revenue | MercadoLibre | "Mercado Ads", "ad sales", "MELI+" in 10-K, 10-Q | not filed (inside Commerce services) |
| Commerce vs fintech operating income | MercadoLibre | Note 8 / Note 6 segments | not filed (segments are geographic) |
| Buyer or merchant counts | Shopify | "buyers", "merchants" counts in KPI sections | no count found in KPI tables |
| GMV, active buyers, D&A and capex for 6M 2026 | PDD | 6-K EX-99.1 Q1 and Q2 2026 (cash flow is summary only) | not in releases; 20-F carries no GMV |
| Any Amazon arrangement ("Buy with Prime") | Shopify | "amazon" (case-insensitive), "Prime" in 10-K and 10-Q | no instance found |

---
## NOTES: BASIS DIFFERENCES

1. **Fiscal windows.** Amazon, eBay, MELI, Shopify, PDD: calendar year ended 2025-12-31; interim = six months ended 2026-06-30. Walmart: fiscal year ended 2026-01-31 ("fiscal 2026"); interim = six months ended 2026-07-31 (Q2 fiscal 2027). Walmart's interim window is shifted one month later than the others.
2. **Gross vs net revenue.** Amazon "Online stores" is product sales recorded gross (footnote (1): "Includes product sales and digital media content where we record revenue gross."); "Third-party seller services" is net (commissions and fulfillment/shipping fees only; the sellers' merchandise value is not revenue). Walmart net sales are overwhelmingly gross merchandise sales; its eCommerce line includes "certain advertising arrangements, fulfillment services, and data insights", and advertising "is recorded in either net sales or as a reduction to cost of sales". eBay revenue is net (commissions, fees, ads, shipping program) with take rate defined as net revenues / GMV. MELI "Commerce services" is net of shipping carrier costs where MELI is agent, gross where principal; "Commerce products sales" is gross first-party inventory sales; Fintech includes interest/credit revenue ("Net revenues and financial income"). Shopify merchant solutions are mainly payment-processing fees on Shopify Payments (plus lending, referral fees, shipping labels), subscription solutions are plan fees; GMV is not revenue. PDD revenues are merchant marketing services and transaction-service fees (net, platform model); PDD files no GMV.
3. **Currency.** PDD reports in RMB; RMB figures are shown without conversion. The 20-F convenience rate and the releases' rates (RMB 6.7851 per US$ at 2026-06-30; RMB 6.8980 at 2026-03-31) are the filer's convenience translations only. MELI reports in USD but operates in BRL, MXN, ARS; growth rates are USD-reported unless marked FX-neutral.
4. **Capex definitions differ.** Amazon cash "Purchases of property and equipment" (gross of incentives) vs segment "net additions" (includes finance leases and unpaid accruals). Walmart segment "Capital expenditures" reconcile to cash "Payments for property and equipment". MELI "Capital expenditures" includes intangible assets. PDD includes software and intangibles. Amazon D&A: segment-note figure is P&E only; cash-flow line adds capitalized content, lease assets and other.
5. **eBay restatement.** eBay early-adopted ASU 2025-06 on 2026-01-01 retrospectively; the 10-Q recasts 6M 2025 D&A from 186 to 131 and capex from 277 to 212 (filed "As Reported / As Adjusted" table). The FY2025 10-K figures in B.1 (capex 525, D&A 407) are the pre-adoption basis and are not comparable to the 10-Q interim figures.
6. **Walmart interim segment OI** for the prior year was revised for a new corporate overhead allocation (quote in B.2); 6M FY2026 segment OI in B.2 is not the figure in the original FY2026 10-Q.
7. **MELI KPIs** include food delivery from Q2 2025 onward (filed footnotes (3) to (5)), which affects GMV, unique buyers and items growth comparisons across 2025.
8. **Amazon segment margins** carry allocated technology-infrastructure costs "based on usage"; FY2025 North America includes the $2.5bn FTC charge and part of severance costs.
