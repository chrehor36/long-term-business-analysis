# INTC COMPETITOR ROW (filing-sourced)
**Built 2026-09-07. Numbers only. No moat conclusion is drawn in this file.**

Source of record: SEC EDGAR primary filings.
- XBRL companyfacts: `https://data.sec.gov/api/xbrl/companyfacts/CIK{10-digit}.json`
- CIK map: `https://www.sec.gov/files/company_tickers.json`
- Where companyfacts lacked a figure, the number was taken from the **filed** financial-statement
  R-file inside the filing itself (`.../Archives/edgar/data/{cik}/{accn}/R{n}.htm`, generated from
  the filed Inline XBRL). Every such instance is flagged below.
- All requests carried `User-Agent: BRK research chrehor36@gmail.com`.

**Cross-check performed (operator rule 4).** Intel FY2025 10-K, accession `0000050863-26-000011`,
period ended 2025-12-27, *Consolidated Statements of Income* (R3.htm): net revenue $52,853M,
cost of sales $34,478M, gross profit $18,375M, operating loss $(2,214)M, net loss attributable to
Intel $(267)M. These match the companyfacts values used in the tables below, digit for digit.

---

## 1. THE FILERS

| Company | Ticker | CIK | Annual form | Latest annual filing used | Period end | Filed | Reporting currency |
|---|---|---|---|---|---|---|---|
| Intel | INTC | 0000050863 | 10-K | `0000050863-26-000011` | 2025-12-27 | 2026-01-23 | USD |
| Advanced Micro Devices | AMD | 0000002488 | 10-K | `0000002488-26-000018` | 2025-12-27 | 2026-02-04 | USD |
| Taiwan Semiconductor | TSM | 0001046179 | 20-F | `0001628280-26-025362` | 2025-12-31 | 2026-04-16 | **TWD** |
| NVIDIA | NVDA | 0001045810 | 10-K | `0001045810-26-000021` | 2026-01-25 | 2026-02-25 | USD |
| GlobalFoundries | GFS | 0001709048 | **20-F** (IFRS) | `0001709048-26-000022` | 2025-12-31 | 2026-02-27 | USD |
| United Microelectronics | UMC | 0001033767 | 20-F | `0001193125-26-193757` | 2025-12-31 | 2026-04-30 | **TWD** |
| Texas Instruments | TXN | 0000097476 | 10-K | `0000097476-26-000059` | 2025-12-31 | 2026-02-06 | USD |

AMD also filed a 10-K/A for FY2025, `0000002488-26-000021`, same period end, filed 2026-02-04.
The FY2025 figures used here are from the 10-K, `0000002488-26-000018`.

**GFS files a 20-F, not a 10-K.** GlobalFoundries Inc. is a Cayman-incorporated foreign private
issuer reporting under **IFRS**; its facts sit in the `ifrs-full` taxonomy, not `us-gaap`. So do
TSM's and UMC's.

### Companies that do NOT file: UNAVAILABLE

| Company | CIK | What is on EDGAR | Obstacle |
|---|---|---|---|
| **Samsung Electronics Co Ltd** | 0000879316 | 251 filings, all of them SUPPL (196, paper), ARS (9, paper), SC 13D/G, SC 14D1/14D9, SC 13E3, Forms 3/4. **No 10-K. No 20-F. No 40-F. No 6-K.** Most recent filing of any kind: SC 13G/A, 2015-01-20. `companyfacts` returns **HTTP 404**. | Samsung Electronics is listed on the Korea Exchange only, has no US-listed security registered under the Exchange Act, and is therefore not a reporting company. Its ADRs trade OTC on the unsponsored/Rule 12g3-2(b) exemption, which requires publication of home-country disclosure on its own website **in place of** SEC filing. **Nothing filing-sourced is obtainable. UNAVAILABLE.** |
| **SK hynix Inc.** | 0002120882 | DRS 2026-03-24, DRS/A ×3, F-1 2026-06-24 (`0001193125-26-280172`), F-1/A ×2 (latest `0001193125-26-295501`, 2026-07-06), F-6, 8-A12B, CERT, EFFECT ×2, 424B4 2026-07-10, then 6-K only (22 of them through 2026-09-04). **No 20-F yet.** `companyfacts` returns only five `ffd:` fee-table facts from the F-1/F-1A (total offering amount $30,192,654,300); **zero financial-statement facts**. | SK hynix registered and listed in the US in July 2026. Its **first 20-F is not yet due** (FY2026 20-F would be filed in 2027). The F-1 contains audited IFRS financials as a prospectus, but they are **not tagged into companyfacts**, and the F-1 is a registration statement, not an annual report. **No annual-report series obtainable. UNAVAILABLE.** |
| Intel Foundry's other named rivals (Rapidus, and the captive foundry arms of Samsung and SK hynix) | n/a | n/a | Rapidus Corporation is a private Japanese consortium with no SEC registration. Samsung Foundry and SK hynix's foundry are **segments inside non-filers**, so no segment disclosure reaches EDGAR. **UNAVAILABLE.** |

---

## 2. METHOD, AND WHAT EACH NUMBER IS

**Fiscal-year label = the calendar year in which the fiscal period ends.** Intel's FY2025 ended
2025-12-27; AMD's ended 2025-12-27; TSM/UMC/GFS/TXN end 12-31.

> **NVIDIA is offset by roughly eleven months and the column headings do not line up with everyone
> else's.** NVDA's FY2025 ran 2024-01-29 to **2025-01-26**, which makes it economically calendar 2024. The
> label used in the NVDA table is NVIDIA's own (= year of period end). An extra FY2026 column
> (ended 2026-01-25) is included because it is filed.

**Which value was taken when a year appears in several filings.** The value **as originally
reported in that year's own annual report**, which is the earliest-filed annual form carrying the fact.
Later restatements are listed in §5.

**Total debt is a computed sum, not a tag.** The formula differs by filer and is stated per company
in §4. **None of these totals include lease liabilities.**

---

## 3. THE TABLES

### 3.1 INTEL (INTC). 10-K, us-gaap, USD millions

| Metric (USD m) | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 59,387 | 62,761 | 70,848 | 71,965 | 77,867 | 79,024 | 63,054 | 54,228 | 53,101 | 52,853 |
| Cost of sales | 23,196 | 23,692 | 27,111 | 29,825 | 34,255 | 35,209 | 36,188 | 32,517 | 35,756 | 34,478 |
| Gross profit | 36,191 | 39,069 | 43,737 | 42,140 | 43,612 | 43,815 | 26,866 | 21,711 | 17,345 | 18,375 |
| **Gross margin %** | **60.9%** | **62.3%** | **61.7%** | **58.6%** | **56.0%** | **55.4%** | **42.6%** | **40.0%** | **32.7%** | **34.8%** |
| Operating income | 12,874 | 17,936 | 23,316 | 22,035 | 23,678 | 19,456 | 2,334 | 93 | (11,678) | (2,214) |
| **Operating margin %** | **21.7%** | **28.6%** | **32.9%** | **30.6%** | **30.4%** | **24.6%** | **3.7%** | **0.2%** | **-22.0%** | **-4.2%** |
| Net income (to Intel) | 10,316 | 9,601 | 21,053 | 21,048 | 20,899 | 19,868 | 8,014 | 1,689 | (18,756) | (267) |
| R&D expense | 12,740 | 13,098 | 13,543 | 13,362 | 13,556 | 15,190 | 17,528 | 16,046 | 16,546 | 13,774 |
| R&D / revenue % | 21.5% | 20.9% | 19.1% | 18.6% | 17.4% | 19.2% | 27.8% | 29.6% | 31.2% | 26.1% |
| Cash from operations | 21,808 | 22,110 | 29,432 | 33,145 | 35,384 | 29,991 | 15,433 | 11,471 | 8,288 | 9,697 |
| Capital expenditure | 9,625 | 11,778 | 15,181 | 16,213 | 14,259 | 18,733 | 24,844 | 25,750 | 23,944 | 14,646 |
| Capex / revenue % | 16.2% | 18.8% | 21.4% | 22.5% | 18.3% | 23.7% | 39.4% | 47.5% | 45.1% | 27.7% |
| Depreciation | 6,266 | 6,752 | 7,520 | 9,204 | 10,482 | 9,953 | 11,128 | 7,847 | 9,951 | 10,757 |
| Total assets | 113,327 | 123,249 | 127,963 | 136,524 | 153,091 | 168,406 | 182,103 | 191,572 | 196,485 | 211,429 |
| Stockholders' equity | 66,226 | 69,019 | 74,563 | 77,504 | 81,038 | 95,391 | 101,423 | 105,590 | 99,270 | 114,281 |
| Equity incl. NCI | n/a | n/a | n/a | 77,504 | 81,038 | 95,391 | 103,286 | 109,965 | 105,032 | 126,360 |
| Total debt | 25,283 | 26,813 | 26,359 | 29,001 | 36,401 | 38,101 | 42,051 | 49,266 | 50,011 | 46,585 |

`Equity incl. NCI` = `StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest`; Intel
only began tagging it from FY2019 and the gap opens from FY2022 (Mobileye, and the SCIP
co-investment vehicles). **Cash from operations 2016** is `NetCashProvidedByUsedInOperating
ActivitiesContinuingOperations`. Intel had discontinued operations that year and did not tag the
undifferentiated concept.

### 3.2 AMD. 10-K, us-gaap, USD millions

| Metric (USD m) | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 4,319 | 5,253 | 6,475 | 6,731 | 9,763 | 16,434 | 23,601 | 22,680 | 25,785 | 34,639 |
| Cost of sales | 3,316 | 3,466 | 4,028 | 3,863 | 5,416 | 8,505 | 12,998 | 12,220 | 13,060 | 17,487 |
| Gross profit | 998 | 1,823 | 2,447 | 2,868 | 4,347 | 7,929 | 10,603 | 10,460 | 12,725 | 17,152 |
| **Gross margin %** | **23.1%** | **34.7%** | **37.8%** | **42.6%** | **44.5%** | **48.2%** | **44.9%** | **46.1%** | **49.4%** | **49.5%** |
| Operating income | (372) | 204 | 451 | 631 | 1,369 | 3,648 | 1,264 | 401 | 1,900 | 3,694 |
| **Operating margin %** | **-8.6%** | **3.9%** | **7.0%** | **9.4%** | **14.0%** | **22.2%** | **5.4%** | **1.8%** | **7.4%** | **10.7%** |
| Net income | (497) | 43 | 337 | 341 | 2,490 | 3,162 | 1,320 | 854 | 1,641 | 4,335 |
| R&D expense | 1,008 | 1,160 | 1,434 | 1,547 | 1,983 | 2,845 | 5,005 | 5,872 | 6,456 | 8,091 |
| R&D / revenue % | 23.3% | 22.1% | 22.1% | 23.0% | 20.3% | 17.3% | 21.2% | 25.9% | 25.0% | 23.4% |
| Cash from operations | 90 | 68 | 34 | 493 | 1,071 | 3,521 | 3,565 | 1,667 | 3,041 | 7,709 |
| Capital expenditure | 77 | 113 | 163 | 217 | 294 | 301 | 450 | 546 | 636 | 974 |
| Capex / revenue % | 1.8% | 2.2% | 2.5% | 3.2% | 3.0% | 1.8% | 1.9% | 2.4% | 2.5% | 2.8% |
| Depreciation | 71 | 77 | 94 | 142 | 217 | 296 | 439 | 441 | 454 | 521 |
| Total assets | 3,321 | 3,540 | 4,556 | 6,028 | 8,962 | 12,419 | 67,580 | 67,885 | 69,226 | 76,926 |
| Stockholders' equity | 416 | 611 | 1,266 | 2,827 | 5,837 | 7,497 | 54,750 | 55,892 | 57,568 | 62,999 |
| Total debt | 1,435 | 1,395 | 1,250 | 486 | 330 | 313 | 2,467 | 2,468 | 1,721 | 3,222 |

The 2022 step in assets and equity is the Xilinx acquisition (closed 2022-02-14), an all-stock deal;
it is a balance-sheet event, not an operating one. AMD's `Depreciation` tag is depreciation only;
`DepreciationDepletionAndAmortization` was tagged 2013-2019 (2016: 133; 2017: 144; 2018: 170;
2019: 222) and dropped thereafter, so the D&A series is not continuous and only the narrow
depreciation line is shown.

### 3.3 TSMC (TSM). 20-F, **ifrs-full**, **TWD millions**. NOT CONVERTED

| Metric (**TWD m**) | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 947,938 | 977,447 | 1,031,474 | 1,069,985 | 1,339,255 | 1,587,415 | 2,263,891 | 2,161,736 | 2,894,308 | 3,809,054 |
| Cost of sales | 473,077 | 482,616 | 533,488 | 577,287 | 628,108 | 767,878 | 915,536 | 986,625 | 1,269,954 | 1,527,760 |
| Gross profit | 474,832 | 494,826 | 497,874 | 492,702 | 711,130 | 819,537 | 1,348,355 | 1,175,111 | 1,624,354 | 2,281,294 |
| **Gross margin %** | **50.1%** | **50.6%** | **48.3%** | **46.0%** | **53.1%** | **51.6%** | **59.6%** | **54.4%** | **56.1%** | **59.9%** |
| Operating income | 377,958 | 385,559 | 383,624 | 372,701 | 566,784 | 649,981 | 1,121,279 | 921,466 | 1,322,053 | 1,936,092 |
| **Operating margin %** | **39.9%** | **39.4%** | **37.2%** | **34.8%** | **42.3%** | **40.9%** | **49.5%** | **42.6%** | **45.7%** | **50.8%** |
| Net income (incl. NCI) | 331,797 | 345,039 | 363,106 | 354,027 | 511,008 | 592,881 | 993,295 | 851,028 | 1,157,524 | 1,695,125 |
| R&D expense | 71,208 | 80,732 | 85,896 | 91,419 | 109,486 | 124,735 | 163,262 | 182,370 | 204,182 | 246,427 |
| R&D / revenue % | 7.5% | 8.3% | 8.3% | 8.5% | 8.2% | 7.9% | 7.2% | 8.4% | 7.1% | 6.5% |
| Cash from operations | 539,835 | 585,318 | 573,954 | 615,139 | 822,666 | 1,112,161 | 1,610,599 | 1,241,967 | 1,826,177 | 2,274,976 |
| Capital expenditure (PP&E) | 328,045 | 330,588 | 315,582 | 460,422 | 507,239 | 839,196 | 1,082,672 | 949,817 | 956,006 | 1,272,410 |
| Capex / revenue % | 34.6% | 33.8% | 30.6% | 43.0% | 37.9% | 52.9% | 47.8% | 43.9% | 33.0% | 33.4% |
| Depreciation | 220,085 | 255,796 | 288,125 | 281,412 | 324,538 | 414,188 | 428,498 | 522,933 | 653,610 | 679,684 |
| Total assets | 1,886,297 | 1,991,732 | 2,090,031 | 2,264,725 | 2,760,600 | 3,725,302 | 4,964,459 | 5,532,197 | 6,691,765 | 7,932,842 |
| Total equity | 1,359,846 | 1,494,446 | 1,661,105 | 1,614,387 | 1,835,764 | 2,151,682 | 2,917,832 | 3,453,866 | 4,279,272 | 5,396,219 |
| Equity attrib. to parent | 1,359,051 | 1,493,747 | 1,660,429 | 1,613,706 | 1,834,811 | 2,149,260 | 2,903,020 | 3,429,522 | 4,244,266 | 5,355,039 |
| Total liabilities | 526,451 | 497,286 | 428,926 | 650,338 | 924,837 | 1,573,620 | 2,046,627 | 2,078,330 | 2,412,493 | 2,536,623 |
| Total debt | 249,162 | 213,968 | 180,555 | 175,422 | 347,232 | 732,868 | 858,410 | 927,576 | 1,018,287 | 1,032,988 |

**Units are TWD millions. Nothing has been converted.** TSM's 20-F also carries a convenience-
translation USD column (from FY2017 on) which is *not* used here. For scale only, TSM's own FY2025
convenience column shows revenue US$121,423.5M and gross profit US$72,722.2M, at the 20-F's own
stated rate. That is TSM's arithmetic, not mine, and it is a convenience translation, not a
measurement.

> **FY2025 is NOT from companyfacts.** TSM's FY2025 20-F (`0001628280-26-025362`, filed 2026-04-16)
> is filed and tagged, but as of 2026-09-07 `companyfacts` and `companyconcept` for CIK 1046179 stop
> at 2024-12-31. The FY2025 column was read from the filed statements inside that filing:
> R4.htm (profit or loss), R3.htm (financial position), R6.htm (cash flows). This is a lag in the
> aggregation API, not in the filing.

### 3.4 NVIDIA (NVDA). 10-K, us-gaap, USD millions. **Fiscal years end late January.**

| Metric (USD m) | FY16 | FY17 | FY18 | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Period end | 01-31-16 | 01-29-17 | 01-28-18 | 01-27-19 | 01-26-20 | 01-31-21 | 01-30-22 | 01-29-23 | 01-28-24 | 01-26-25 | 01-25-26 |
| Revenue | 5,010 | 6,910 | 9,714 | 11,716 | 10,918 | 16,675 | 26,914 | 26,974 | 60,922 | 130,497 | 215,938 |
| Cost of sales | 2,199 | 2,847 | 3,892 | 4,545 | 4,150 | 6,279 | 9,439 | 11,618 | 16,621 | 32,639 | 62,475 |
| Gross profit | 2,811 | 4,063 | 5,822 | 7,171 | 6,768 | 10,396 | 17,475 | 15,356 | 44,301 | 97,858 | 153,463 |
| **Gross margin %** | **56.1%** | **58.8%** | **59.9%** | **61.2%** | **62.0%** | **62.3%** | **64.9%** | **56.9%** | **72.7%** | **75.0%** | **71.1%** |
| Operating income | 747 | 1,934 | 3,210 | 3,804 | 2,846 | 4,532 | 10,041 | 4,224 | 32,972 | 81,453 | 130,387 |
| **Operating margin %** | **14.9%** | **28.0%** | **33.0%** | **32.5%** | **26.1%** | **27.2%** | **37.3%** | **15.7%** | **54.1%** | **62.4%** | **60.4%** |
| Net income | 614 | 1,666 | 3,047 | 4,141 | 2,796 | 4,332 | 9,752 | 4,368 | 29,760 | 72,880 | 120,067 |
| R&D expense | 1,331 | 1,463 | 1,797 | 2,376 | 2,829 | 3,924 | 5,268 | 7,339 | 8,675 | 12,914 | 18,497 |
| R&D / revenue % | 26.6% | 21.2% | 18.5% | 20.3% | 25.9% | 23.5% | 19.6% | 27.2% | 14.2% | 9.9% | 8.6% |
| Cash from operations | 1,175 | 1,672 | 3,502 | 3,743 | 4,761 | 5,822 | 9,108 | 5,641 | 28,090 | 64,089 | 102,718 |
| Capital expenditure | 86 | 176 | 593 | 600 | 489 | 1,128 | 976 | 1,833 | 1,069 | 3,236 | 6,042 |
| Capex / revenue % | 1.7% | 2.5% | 6.1% | 5.1% | 4.5% | 6.8% | 3.6% | 6.8% | 1.8% | 2.5% | 2.8% |
| Depreciation | 124 | 118 | 144 | 233 | 355 | 486 | 611 | 844 | 894 | 1,300 | 2,400 |
| D&A | n/a | n/a | n/a | n/a | 381 | 1,098 | 1,174 | 1,544 | 1,508 | 1,864 | 2,843 |
| Total assets | 7,370 | 9,841 | 11,241 | 13,292 | 17,315 | 28,791 | 44,187 | 41,182 | 65,728 | 111,601 | 206,803 |
| Stockholders' equity | 4,469 | 5,762 | 7,471 | 9,342 | 12,204 | 16,893 | 26,612 | 22,101 | 42,978 | 79,327 | 157,293 |
| Total debt | 1,413 | 1,983 | 1,985 | 1,988 | 1,991 | 6,963 | 10,946 | 10,953 | 9,709 | 8,463 | 8,468 |

> **Two NVDA numbers are NOT from companyfacts.**
> 1. **Capex FY2016-FY2021.** NVIDIA tagged this line with a *company-extension* element
>    (`nvda:PurchasesOfPropertyAndEquipmentAndIntangibleAssets`, later
>    `nvda:PurchasesRelatedToPropertyAndEquipmentAndIntangibleAssets`). companyfacts carries only
>    standard taxonomies, so those six years are absent from it. They were read from the filed cash
>    flow statements: FY2016/17/18 from the FY2018 10-K `0001045810-18-000010` R7.htm (86 / 176 /
>    593), FY2019/20/21 from the FY2021 10-K `0001045810-21-000010` R8.htm (600 / 489 / 1,128).
>    From FY2022 the standard `PaymentsToAcquireProductiveAssets` is used.
> 2. **FY2019 revenue and cost of sales.** The FY2019 10-K (`0001045810-19-000023`) tagged these as
>    `RevenueFromContractWithCustomerExcludingAssessedTax` (11,716) and
>    `CostOfGoodsAndServicesSold` (4,545) rather than `Revenues` / `CostOfRevenue`. Same statement,
>    same filing, different element.
>
> **Do not read the NVDA columns against the others' columns.** NVDA FY2025 ended 2025-01-26 and is
> economically calendar 2024. Its FY2026 (ended 2026-01-25) is the year that lines up with everyone
> else's 2025.

### 3.5 GLOBALFOUNDRIES (GFS). **20-F**, **ifrs-full**, USD millions

| Metric (USD m) | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | **UNAVAIL** | **UNAVAIL** | **UNAVAIL** | 5,813 | 4,851 | 6,585 | 8,108 | 7,392 | 6,750 | 6,791 |
| Cost of sales | UNAVAIL | UNAVAIL | UNAVAIL | 6,345 | 5,563 | 5,572 | 5,869 | 5,291 | 5,099 | 5,101 |
| Gross profit | UNAVAIL | UNAVAIL | UNAVAIL | (532) | (713) | 1,013 | 2,239 | 2,101 | 1,651 | 1,690 |
| **Gross margin %** | n/a | n/a | n/a | **-9.2%** | **-14.7%** | **15.4%** | **27.6%** | **28.4%** | **24.5%** | **24.9%** |
| Operating income | UNAVAIL | UNAVAIL | UNAVAIL | (1,625) | (1,656) | (60) | 1,167 | 1,129 | (214) | 797 |
| **Operating margin %** | n/a | n/a | n/a | **-28.0%** | **-34.1%** | **-0.9%** | **14.4%** | **15.3%** | **-3.2%** | **11.7%** |
| Net income (incl. NCI) | UNAVAIL | UNAVAIL | UNAVAIL | (1,371) | (1,351) | (254) | 1,446 | 1,018 | (262) | 888 |
| R&D expense | UNAVAIL | UNAVAIL | UNAVAIL | 583 | 476 | 478 | 482 | 428 | 496 | 518 |
| R&D / revenue % | n/a | n/a | n/a | 10.0% | 9.8% | 7.3% | 5.9% | 5.8% | 7.3% | 7.6% |
| Cash from operations | UNAVAIL | UNAVAIL | UNAVAIL | 497 | 1,006 | 2,839 | 2,624 | 2,125 | 1,722 | 1,731 |
| Capital expenditure | UNAVAIL | UNAVAIL | UNAVAIL | 588 | 449 | 1,662 | 3,059 | 1,804 | 625 | 722 |
| Capex / revenue % | n/a | n/a | n/a | 10.1% | 9.3% | 25.2% | 37.7% | 24.4% | 9.3% | 10.6% |
| D&A | UNAVAIL | UNAVAIL | UNAVAIL | 2,382 | 2,187 | 1,422 | 1,468 | 1,321 | 1,424 | 1,168 |
| Total assets | UNAVAIL | UNAVAIL | UNAVAIL | **n/a** | 12,322 | 15,028 | 17,841 | 18,044 | 16,799 | 17,141 |
| Total equity | UNAVAIL | UNAVAIL | 10,780 | 9,019 | 7,242 | 8,033 | 9,960 | 11,151 | 10,824 | 11,983 |
| Total liabilities | UNAVAIL | UNAVAIL | UNAVAIL | n/a | 5,080 | 6,994 | 7,881 | 6,893 | 5,975 | 5,158 |
| Total debt (Borrowings) | UNAVAIL | UNAVAIL | UNAVAIL | 2,729 | 2,338 | 2,013 | 2,511 | 2,372 | 1,806 | 1,151 |

**GFS 2016-2018 is UNAVAILABLE and the reason is structural, not a search failure.** GlobalFoundries
IPO'd on Nasdaq on 2021-10-28. Its first annual report, the FY2021 20-F `0001709048-22-000008`, is
the earliest annual filing in existence, and it presents **three** income-statement years (2019,
2020, 2021) and **two** balance-sheet dates (2020, 2021). Nothing before 2019 was ever filed with
the SEC. 2019 total assets and total liabilities are absent for the same reason, that the FY2021 20-F's
balance sheet starts at 2020-12-31. GFS's 2018 equity figure survives only because it is the
opening line of the FY2019-2021 statement of changes in equity.

**GFS D&A note.** GFS's `ifrs-full:DepreciationExpense` is **tagged inconsistently across 20-Fs**.
FY2022 alone carries three different values in three filings (2,238 / 1,447 / 1,365), and the
FY2021 20-F reports 2,238 for FY2020 while the FY2022 20-F reports 1,447 for the same year. The
tag is unreliable. The row above therefore uses `ifrs-full:DepreciationAndAmortisationExpense`,
which is stable across every filing that repeats it. Flagged, not smoothed.

### 3.6 UMC. 20-F, **ifrs-full**, **TWD millions**. NOT CONVERTED

| Metric (**TWD m**) | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 147,870 | 149,285 | 151,253 | 148,202 | 176,821 | 213,011 | 278,705 | 222,533 | 232,303 | 237,553 |
| Cost of sales | 117,491 | 122,227 | 128,413 | 126,887 | 137,824 | 140,961 | 152,941 | 144,789 | 156,649 | 168,647 |
| Gross profit | 30,379 | 27,058 | 22,840 | 21,315 | 38,997 | 72,050 | 125,764 | 77,744 | 75,654 | 68,906 |
| **Gross margin %** | **20.5%** | **18.1%** | **15.1%** | **14.4%** | **22.1%** | **33.8%** | **45.1%** | **34.9%** | **32.6%** | **29.0%** |
| Operating income | 6,194 | 6,568 | 5,680 | 4,884 | 21,931 | 51,686 | 104,292 | 57,891 | 51,613 | 43,949 |
| **Operating margin %** | **4.2%** | **4.4%** | **3.8%** | **3.3%** | **12.4%** | **24.3%** | **37.4%** | **26.0%** | **22.2%** | **18.5%** |
| Net income (incl. NCI) | 4,169 | 6,679 | 3,248 | 4,576 | 20,852 | 50,578 | 90,299 | 60,139 | 48,675 | 40,179 |
| R&D expense | 13,532 | 13,670 | 13,025 | 11,860 | 12,896 | 12,935 | 12,954 | 13,284 | 15,616 | 17,725 |
| R&D / revenue % | 9.2% | 9.2% | 8.6% | 8.0% | 7.3% | 6.1% | 4.6% | 6.0% | 6.7% | 7.5% |
| Cash from operations | 46,450 | 52,474 | 50,935 | 54,904 | 65,745 | 90,352 | 145,861 | 86,000 | 93,872 | 99,864 |
| Capital expenditure (PP&E) | 91,561 | 44,236 | 19,590 | 16,518 | 26,345 | 48,035 | 80,128 | 91,474 | 88,544 | 47,745 |
| Capex / revenue % | 61.9% | 29.6% | 13.0% | 11.1% | 14.9% | 22.6% | 28.7% | 41.1% | 38.1% | 20.1% |
| Depreciation | 49,596 | 50,825 | 49,776 | 46,911 | 45,896 | 43,911 | 41,062 | 37,551 | 45,337 | 56,427 |
| Total assets | 384,227 | 391,132 | 362,597 | 366,262 | 366,454 | 450,955 | 524,646 | 546,577 | 560,169 | 567,275 |
| Total equity | 214,946 | 209,621 | 204,397 | 202,914 | 223,140 | 264,375 | 322,811 | 343,717 | 365,707 | 365,912 |
| Equity attrib. to parent | 212,785 | 208,664 | 203,931 | 202,504 | 223,026 | 264,152 | 322,467 | 343,376 | 365,450 | 365,825 |
| Total liabilities | 169,280 | 181,511 | 158,200 | 163,348 | 143,315 | 186,580 | 201,835 | 202,860 | 194,462 | 201,363 |
| Total debt | 91,780 | 106,129 | 85,308 | 84,699 | 62,814 | 79,086 | 47,464 | 74,773 | 75,043 | 72,969 |

**Units are TWD millions. Nothing has been converted.** UMC's own statements are printed in TWD
*thousands*; the figures above are those divided by 1,000 to sit in the same TWD-millions frame as
TSM. **FY2025 is NOT from companyfacts**, the same API lag as TSM. UMC's FY2025 20-F
(`0001193125-26-193757`, filed 2026-04-30) is filed and tagged; companyfacts for CIK 1033767 stops
at 2024-12-31. The FY2025 column was read from R4.htm (comprehensive income), R2.htm (balance
sheet), R6.htm (cash flows) inside that filing.

### 3.7 TEXAS INSTRUMENTS (TXN). 10-K, us-gaap, USD millions

| Metric (USD m) | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 13,370 | 14,961 | 15,784 | 14,383 | 14,461 | 18,344 | 20,028 | 17,519 | 15,641 | 17,682 |
| Cost of sales | 5,113 | 5,347 | 5,507 | 5,219 | 5,192 | 5,968 | 6,257 | 6,500 | 6,547 | 7,599 |
| Gross profit | 8,240 | 9,614 | 10,277 | 9,164 | 9,269 | 12,376 | 13,771 | 11,019 | 9,094 | 10,083 |
| **Gross margin %** | **61.6%** | **64.3%** | **65.1%** | **63.7%** | **64.1%** | **67.5%** | **68.8%** | **62.9%** | **58.1%** | **57.0%** |
| Operating income | 4,799 | 6,083 | 6,713 | 5,723 | 5,894 | 8,960 | 10,140 | 7,331 | 5,465 | 6,023 |
| **Operating margin %** | **35.9%** | **40.7%** | **42.5%** | **39.8%** | **40.8%** | **48.8%** | **50.6%** | **41.8%** | **34.9%** | **34.1%** |
| Net income | 3,595 | 3,682 | 5,580 | 5,017 | 5,595 | 7,769 | 8,749 | 6,510 | 4,799 | 5,001 |
| R&D expense | 1,370 | 1,508 | 1,559 | 1,544 | 1,530 | 1,554 | 1,670 | 1,863 | 1,959 | 2,083 |
| R&D / revenue % | 10.2% | 10.1% | 9.9% | 10.7% | 10.6% | 8.5% | 8.3% | 10.6% | 12.5% | 11.8% |
| Cash from operations | 4,614 | 5,363 | 7,189 | 6,649 | 6,139 | 8,756 | 8,720 | 6,420 | 6,318 | 7,153 |
| Capital expenditure | 531 | 695 | 1,131 | 847 | 649 | 2,462 | 2,797 | 5,071 | 4,820 | 4,550 |
| Capex / revenue % | 4.0% | 4.6% | 7.2% | 5.9% | 4.5% | 13.4% | 14.0% | 28.9% | 30.8% | 25.7% |
| Depreciation | 605 | 539 | 590 | 708 | 733 | 755 | 925 | 1,175 | 1,508 | 1,918 |
| Total assets | 16,431 | 17,642 | 17,137 | 18,018 | 19,351 | 24,676 | 27,207 | 32,348 | 35,509 | 34,585 |
| Stockholders' equity | 10,473 | 10,337 | 8,994 | 8,907 | 9,187 | 13,333 | 14,577 | 16,897 | 16,903 | 16,273 |
| Total debt | 3,609 | 4,077 | 5,068 | 5,803 | 6,798 | 7,741 | 8,735 | 11,223 | 13,596 | 14,048 |

TXN cash from operations 2016 is `NetCashProvidedByUsedInOperatingActivitiesContinuingOperations`
(the concept TXN used through FY2017); the undifferentiated tag is used from 2017 on and the two
agree where they overlap (2016: 4,614; 2017: 5,363).

---

## 4. TAG PROVENANCE: every row, its element and its form

### 4.1 US-GAAP filers (INTC, AMD, NVDA, TXN), form **10-K**

| Row | Element | Notes |
|---|---|---|
| Revenue | `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` | NVDA uses `us-gaap:Revenues`, except FY2019 (see §3.4) |
| Cost of sales | `us-gaap:CostOfGoodsAndServicesSold` | AMD 2015-2017 `CostOfGoodsSold`; TXN 2015 & NVDA `CostOfRevenue` |
| Gross profit | `us-gaap:GrossProfit` | continuous for all four, all years |
| Operating income | `us-gaap:OperatingIncomeLoss` | |
| Net income | `us-gaap:NetIncomeLoss` | Intel: this is net income **attributable to Intel**. `us-gaap:ProfitLoss` (incl. NCI) is FY2025 $26M vs $(267)M attributable |
| Cash from operations | `us-gaap:NetCashProvidedByUsedInOperatingActivities` | INTC 2016 and TXN 2016 use `…ContinuingOperations` |
| Capital expenditure | `us-gaap:PaymentsToAcquirePropertyPlantAndEquipment` | NVDA FY2022+ `PaymentsToAcquireProductiveAssets`; NVDA FY2016-21 is a company extension, read from the filed statement |
| Depreciation | `us-gaap:Depreciation` | |
| D&A | `us-gaap:DepreciationDepletionAndAmortization` | shown for NVDA only; discontinuous for AMD (2013-2019) and absent for INTC/TXN |
| Total assets | `us-gaap:Assets` | |
| Equity | `us-gaap:StockholdersEquity` | Intel's incl.-NCI line is `StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest` |
| R&D | `us-gaap:ResearchAndDevelopmentExpense` | |

**Total debt formulas (US-GAAP filers).** No single element carries it.
- **INTC** = `us-gaap:DebtCurrent` + `us-gaap:LongTermDebtNoncurrent`. Note this is *wider* than
  Intel's own `us-gaap:LongTermDebt` in 2022, where `DebtCurrent` 4,367 exceeds `LongTermDebtCurrent`
  423 by $3,944M of other short-term debt. FY2025: 2,499 + 44,086 = 46,585.
- **AMD** = `us-gaap:DebtLongtermAndShorttermCombinedAmount` for 2020-2025;
  `us-gaap:LongTermDebt` for 2016-2019 (AMD carried no separate short-term borrowings those years).
  The two agree in the 2020 overlap (330 / 330).
- **NVDA** and **TXN** = `us-gaap:LongTermDebt`, which for both equals
  `LongTermDebtNoncurrent + LongTermDebtCurrent` in every year checked.

### 4.2 IFRS filers (TSM and UMC, form **20-F**; GFS, form **20-F**)

| Row | Element |
|---|---|
| Revenue | `ifrs-full:Revenue` (GFS also tags `RevenueFromContractsWithCustomers`, identical) |
| Cost of sales | `ifrs-full:CostOfSales` |
| Gross profit | `ifrs-full:GrossProfit` |
| Operating income | `ifrs-full:ProfitLossFromOperatingActivities` |
| Net income | `ifrs-full:ProfitLoss`, which **includes non-controlling interests** |
| Cash from operations | `ifrs-full:CashFlowsFromUsedInOperatingActivities` |
| Capital expenditure | `ifrs-full:PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities` |
| Depreciation | `ifrs-full:DepreciationExpense` (TSM, UMC); GFS uses `ifrs-full:DepreciationAndAmortisationExpense`, see §3.5 |
| Total assets | `ifrs-full:Assets` |
| Total equity | `ifrs-full:Equity`; parent-only `ifrs-full:EquityAttributableToOwnersOfParent` |
| Total liabilities | `ifrs-full:Liabilities` |
| R&D | `ifrs-full:ResearchAndDevelopmentExpense` |

**Total debt formulas (IFRS filers).**
- **TSM** = `ShorttermBorrowings` + `CurrentPortionOfLongtermBorrowings` + `LongtermBorrowings`
  + `NoncurrentPortionOfNoncurrentBondsIssued`. TSM carried no short-term loans from FY2022 on.
  FY2024: 0 + 59,858 + 31,824 + 926,604 = 1,018,287. FY2025 (from R3.htm): long-term liabilities
  current portion 136,926 + bonds payable 856,228 + long-term bank loans 39,835 = 1,032,988.
- **UMC** = `ShorttermBorrowings` + `CurrentPortionOfLongtermBorrowings` +
  `NoncurrentPortionOfNoncurrentBondsIssued` + `NoncurrentPortionOfNoncurrentLoansReceived`
  (that last element is UMC's tag for non-current long-term bank loans).
  FY2024: 8,515 + 10,995 + 24,585 + 30,949 = 75,043.
- **GFS** = `ifrs-full:Borrowings` (a single total; it reconciles to `CurrentPortionOfLongterm
  Borrowings` + `LongtermBorrowings`, FY2025: 86 + 1,065 = 1,151).

### 4.3 Which filing supplied which year (keyed on the gross-profit series)

| FY | INTC | AMD | TSM | NVDA | GFS | UMC | TXN |
|---|---|---|---|---|---|---|---|
| 2016 | 0000050863-17-000012 | 0000002488-17-000043 | 0001193125-18-121866 | 0001045810-16-000205 | n/a | 0001193125-18-132616 | 0001564590-17-002142 |
| 2017 | 0000050863-18-000007 | 0000002488-18-000042 | 0001193125-18-121866 | 0001045810-17-000027 | n/a | 0001193125-18-132616 | 0001564590-18-002832 |
| 2018 | 0000050863-19-000007 | 0000002488-19-000011 | 0001193125-19-108390 | 0001045810-18-000010 | n/a | 0001193125-19-117861 | 0001564590-19-003839 |
| 2019 | 0000050863-20-000011 | 0000002488-20-000008 | 0001193125-20-107579 | 0001045810-19-000023 | 0001709048-22-000008 | 0001193125-20-121853 | 0000097476-20-000009 |
| 2020 | 0000050863-21-000010 | 0001628280-21-001185 | 0001193125-21-118512 | 0001045810-20-000010 | 0001709048-22-000008 | 0001564590-21-021578 | 0000097476-21-000006 |
| 2021 | 0000050863-22-000007 | 0000002488-22-000016 | 0001193125-22-104891 | 0001045810-21-000010 | 0001709048-22-000008 | 0001193125-22-125284 | 0000097476-22-000009 |
| 2022 | 0000050863-23-000006 | 0000002488-23-000047 | 0001193125-23-107214 | 0001045810-22-000036 | 0001709048-23-000013 | 0001193125-23-119772 | 0000097476-23-000007 |
| 2023 | 0000050863-24-000010 | 0000002488-24-000012 | 0001193125-24-099840 | 0001045810-23-000017 | 0001709048-24-000013 | 0001193125-24-111429 | 0000097476-24-000007 |
| 2024 | 0000050863-25-000009 | 0000002488-25-000012 | 0001193125-25-083423 | 0001045810-24-000029 | 0001709048-25-000024 | 0001193125-25-092142 | 0000097476-25-000007 |
| 2025 | 0000050863-26-000011 | 0000002488-26-000018 | **0001628280-26-025362** (R-file) | 0001045810-25-000023 | 0001709048-26-000022 | **0001193125-26-193757** (R-file) | 0000097476-26-000059 |
| 2026 | n/a | n/a | n/a | 0001045810-26-000021 | n/a | n/a | n/a |

Where a fiscal year's revenue was tagged only in a later 10-K (the ASC 606 element
`RevenueFromContractWithCustomerExcludingAssessedTax` did not exist before FY2018), the revenue row
draws on that later filing: INTC 2016-2018 revenue from `0000050863-19-000007`, AMD 2016-2018 from
`0000002488-19-000011`, TXN 2016-2018 from `0001564590-19-003839`. Gross profit, which is what the
table above is keyed on, is tagged in each year's own annual report.

---

## 5. RESTATEMENTS AND CONFLICTS: where two filings disagree about the same year

Every case below is a *later* annual report disagreeing with the original. The tables use the
**original**. Nothing here has been smoothed.

| Company | Year | Metric | As originally filed | As shown later | Cause |
|---|---|---|---|---|---|
| INTC | 2016 | Gross profit | 36,191 | 36,233 | McAfee discontinued-operations reclassification in the FY2017/2018 10-K |
| INTC | 2016 | Operating income | 12,874 | 13,133 | same |
| INTC | 2016 | R&D | 12,685, then **12,740 used** | n/a | the FY2016 10-K's own two presentations; the higher is the one repeated in FY2017 |
| INTC | 2017 | Gross profit | 39,069 | 39,098 | same reclassification |
| INTC | 2017 | Operating income | 17,936 | 18,050 | same |
| INTC | 2017 | Equity | 69,019 | 69,653 | later presentation |
| INTC | 2020 | Cash from operations | 35,384 | 35,864 | cash flow reclassification in FY2021 10-K |
| INTC | 2021 | Cash from operations | 29,991 | 29,456 | same |
| AMD | 2017 | Gross profit | 1,787 → **1,823 used** | | the FY2017 10-K itself carries both; 1,823 is the figure repeated in later filings |
| AMD | 2017 | Operating income | 127 | 204 | ASC 606 adoption restated FY2017 in the FY2018 10-K |
| AMD | 2017 | Net income | (33) | 43 | same |
| AMD | 2017 | Cash from operations | 12 | 68 | same |
| TXN | 2016 | Gross profit | 8,240 | 8,257 | FY2017 presentation |
| TXN | 2016 | Operating income | 4,799 | 4,855 | same |
| TSM | 2019, 2020 | Cost of sales | 577,283.5 / 628,108.4 | 577,286.9 / 628,124.7 | immaterial re-presentation (TWD m) |
| GFS | 2020 | Capital expenditure | **449** | **592** | the FY2022 20-F re-presents FY2020 and FY2021 capex on a wider basis |
| GFS | 2021 | Capital expenditure | **1,662** | **1,767** | same, and this one is material at about 6% |
| GFS | 2020, 2022, 2023 | `DepreciationExpense` | see §3.5 | see §3.5 | the tag is unreliable; the D&A row uses a different element |
| GFS | several | many | full precision | rounded to $M | GFS moved from exact to rounded tagging after FY2021; not a restatement |

---

## 6. THE x86 SHARE QUESTION: AMD's own 10-K disclosures

### 6.1 Segment revenue and segment operating income, FY2019-FY2025 (USD millions)

**AMD has changed its reportable segments twice inside this window, and the FY2019 shape has no
Data Center segment at all.** Three regimes:

| Regime | Fiscal years | Reportable segments |
|---|---|---|
| A | through FY2019 | 2: Computing and Graphics; Enterprise, Embedded and Semi-Custom |
| B | FY2020-FY2024 (introduced in the FY2022 10-K, which recast FY2020 and FY2021) | 4: Data Center; Client; Gaming; Embedded |
| C | FY2025 | 3: Data Center; **Client and Gaming**; Embedded |

#### Data Center segment

| | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|---|
| **Revenue** | **NOT REPORTED** | 1,685 | 3,694 | 6,043 | 6,496 | 12,579 | 16,635 |
| **Operating income** | **NOT REPORTED** | 198 | 991 | 1,848 | 1,267 | 3,482 | 3,603 |
| Operating margin % | n/a | 11.8% | 26.8% | 30.6% | 19.5% | 27.7% | 21.7% |
| Source accession | n/a | 0000002488-23-000047 | 0000002488-23-000047 | 0000002488-23-000047 | 0000002488-25-000012 | 0000002488-25-000012 | 0000002488-26-000018 |

FY2019 is **UNAVAILABLE as a reported segment**: the FY2019 10-K (`0000002488-20-000008`, R75.htm)
tags `NumberOfReportableSegments = 2` and reports only Computing and Graphics (revenue 4,709,
operating income 577) and Enterprise, Embedded and Semi-Custom (revenue 2,022, operating income 263).
AMD never went back and recast FY2019 onto the Data Center basis in any subsequent 10-K. Naming a
FY2019 Data Center number would be an invention, so it is not named.

#### Client segment revenue

| | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|---|
| **Client revenue** | NOT REPORTED | 5,189 | 6,887 | 6,201 | 4,651 | 7,054 | **10,640** |
| Client operating income | NOT REPORTED | 1,608 | 2,088 | 1,190 | (46) | 897 | *see below* |
| Gaming revenue | NOT REPORTED | 2,746 | 5,607 | 6,805 | 6,212 | 2,595 | 3,910 |
| Gaming operating income | NOT REPORTED | (138) | 934 | 953 | 971 | 290 | *see below* |
| Embedded revenue | NOT REPORTED | 143 | 246 | 4,552 | 5,321 | 3,557 | 3,454 |
| Embedded operating income | NOT REPORTED | (11) | 44 | 2,252 | 2,628 | 1,421 | 1,243 |

**FY2025 breaks the Client series.** The FY2025 10-K merges Client and Gaming into one reportable
segment: **Client and Gaming revenue 14,550, operating income 2,855** (FY2024 recast 9,649 / 1,187;
FY2023 recast 10,863 / 925). Client revenue of 10,640 and Gaming revenue of 3,910 are still
disclosed as *revenue lines within* that segment, but **there is no FY2025 Client-only operating
income**. AMD stopped reporting it. Marked as such above rather than estimated.

Elements: `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` and
`us-gaap:OperatingIncomeLoss`, dimensioned on `us-gaap:StatementBusinessSegmentsAxis`. **Segment
facts are dimensioned and therefore do NOT appear in companyfacts** (which carries consolidated,
undimensioned facts only). Every segment figure above was read from the filed
`Segment Reporting - Summary of Operations by Segment (Details)` R-file inside the 10-K itself: R70.htm of
`0000002488-23-000047`, R51.htm of `0000002488-25-000012`, R52.htm of `0000002488-26-000018`,
R75.htm of `0000002488-20-000008`.

### 6.2 AMD's own statements about server and client CPU share

**THE FINDING, STATED FIRST: in no 10-K from FY2019 through FY2025 does AMD state a market-share
figure for its own server CPUs, client/PC CPUs, or x86 processors.** All seven primary documents
were read in full. The phrases "share gains", "gained share", "unit share", "revenue share",
"leadership share" and "share growth" **appear nowhere in any of the seven 10-Ks**. No sentence in
any of them attaches a percentage to AMD's own processor share.

The only market-share leadership AMD claims for *itself* anywhere in the seven filings is in **game
consoles**, and it makes that claim in every year, in near-identical words. In FY2019-FY2021:

> "We are the market share leader in semi-custom game console products, where graphics performance
> is critical, and where we compete primarily against Nvidia."

and from FY2022 onward, with the Nvidia clause dropped:

> "We are the market share leader in semi-custom game console products, where graphics performance
> is critical."

**Consequence for the x86 share question.** If a share number is wanted, it cannot be sourced from a
filed document. AMD's share figures live in earnings calls, investor-day decks, and Mercury Research
third-party data, none of which is a primary filing. Under the framework's own test, "Can I name
the document that would resolve this?", the answer for *filing-sourced* x86 share is **no**: no such
document exists on EDGAR. The proxy that *does* exist and is filing-sourced is the segment revenue
and segment operating income in §6.1.

#### What AMD does say, verbatim, by fiscal year

All quotations below are exact sentences from the 10-K primary documents named in §6.1.

**FY2019, `0000002488-20-000008`, Item 1 Business (Competition)**

> "Intel Corporation has been the market share leader for microprocessors for many years."

> "Intel's market share, margins and significant financial resources enable it to market its
> products aggressively, to target our customers and our channel partners with special incentives
> and to influence customers who do business with us."

> "As a result of Intel's position in the microprocessor market, Intel has been able to control x86
> microprocessor and computer system standards and benchmarks and to dictate the type of products
> the microprocessor market requires of us."

> "Additionally, Intel is able to drive de facto standards and specifications for x86
> microprocessors that could cause us and other companies to have delayed access to such standards."

> "Our principal competitor in the discrete graphics market is Nvidia and they are considered the
> market share leader."

> "In the data center, our principal competitor is Nvidia as the adoption of their proprietary CUDA
> software platform established their market share in high performance computing and machine
> learning."

**FY2019, Item 1A Risk Factors**

> "As long as Intel remains in this dominant position, we may be materially adversely affected by
> Intel's business practices, including rebating and allocation strategies and pricing actions,
> designed to limit our market share and margins; product mix and introduction schedules; product
> bundling, marketing and merchandising strategies; exclusivity payments to its current and
> potential customers, retailers and channel partners; de facto control over industry standards,
> and heavy influence on PC manufacturers and other PC industry participants, including motherboard,
> memory, chipset and basic input/output system (BIOS) suppliers and software companies as well as
> the graphics interface for Intel platforms; and marketing and advertising expenditures in support
> of positioning the Intel brand over the brand of its original equipment manufacturer OEM customers
> and retailers."

> "Our ability to innovate beyond the x86 instruction set controlled by Intel depends partially on
> Microsoft designing and developing its operating systems to run on or support our x86-based
> microprocessor products."

**FY2019, Item 7 MD&A** (the EPYC line is a revenue driver, not a share statement)

> "Enterprise, Embedded and Semi-Custom net revenue of $2.0 billion in 2019 decreased by 14%
> compared to net revenue of $2.4 billion in 2018, primarily as a result of lower semi-custom
> product revenue, partially offset by higher sales of our EPYC server processors."

**FY2020, `0001628280-21-001185`, Item 1 Business.** Substantially identical to FY2019, and the
same sentences appear in both Item 1 and Item 1A.

> "Intel Corporation has been the market share leader for microprocessors for many years."

> "In the data center, our principal competitor is Nvidia as the adoption of its proprietary CUDA
> software platform established its market share in HPC and machine learning."

**FY2021, `0000002488-22-000016`.** Structural change: the Intel market-share-leader sentences move
**out of Item 1 and into Item 1A only**.

Item 1A:
> "Intel Corporation (Intel) has been the market share leader for microprocessors for many years."

> "As a result of Intel's position in the microprocessor market, Intel has been able to control x86
> microprocessor and computer system standards and benchmarks and to dictate the type of products
> the microprocessor market requires of us."

Item 1:
> "For GPU data center products, our principal competitor is NVIDIA, which established its market
> share in HPC and machine learning through its CUDA software platform."

**FY2022, `0000002488-23-000047`.** The Nvidia data-center/CUDA market-share sentence present in
FY2019-FY2021 is **dropped**. Item 1A repeats "Intel Corporation (Intel) has been the market share
leader for microprocessors for many years." unchanged.

Item 7 MD&A:
> "The increase in net revenue was driven by a 64% increase in Data Center segment revenue primarily
> due to higher sales of our EPYC™ server processors, a 21% increase in Gaming segment revenue
> primarily due to higher semi-custom product sales, and a significant increase in Embedded segment
> revenue from the prior year period driven by the inclusion of Xilinx embedded product sales."

**FY2023, `0000002488-24-000012`.** The sentence "Intel Corporation has been the market share
leader for microprocessors for many years" is **removed from the 10-K entirely and never returns**.
The risk factor is retitled, verbatim: *"Intel Corporation's dominance of the microprocessor market
and its aggressive business practices may limit our ability to compete effectively on a level
playing field."*

> "Intel's microprocessor market share position, significant financial resources, introduction of
> competitive new products, and existing relationships with top-tier OEMs have enabled it to market
> and price its products aggressively, to target our customers and our channel partners with special
> incentives and to influence customers who do business with us."

> "In the graphics market, our principal competitor in the supply of discrete graphics is NVIDIA,
> who is the market share leader, and Intel, who manufactures and sells integrated graphics
> processors and gaming-focused discrete GPUs."

> "Large multi-national public cloud service providers and hyperscale private data centers directly
> and indirectly purchase a substantial portion of our data center-focused products, including
> server CPUs, GPU accelerators, DPUs, FPGAs and Adaptive SOCs."

Item 7 MD&A:
> "The decrease in net revenue was primarily due to a 25% decrease in Client segment revenue
> primarily due to lower processor sales and a 9% decrease in Gaming segment revenue primarily due
> to lower semi-custom product sales."

**FY2024, `0000002488-25-000012`.** A **new Nvidia market-share risk factor appears for the first
time**, mirroring the Intel one.

> "Nvidia's Data Center GPU market share position, significant financial resources, introduction of
> competitive new products and proprietary software ecosystem have enabled it to market and price
> its products in a manner to encourage the selection of Nvidia-based systems and to influence
> customers who do business with us."

> "Nvidia's practices can limit customers' ability to choose non-Nvidia products, including our
> products, and in turn, may limit our market share and decrease our margins and profitability,
> which could have a material adverse effect on our business."

> "Intel's microprocessor market share position, significant financial resources, introduction of
> competitive new products, and existing relationships with top-tier OEMs have enabled it to market
> and price its products aggressively, to target our customers and our channel partners with special
> incentives and to influence customers who do business with us."

> "EPYC CPUs, which are based on the x86 architecture, are server-specific processors designed for
> high-performance computing, enterprise IT, supercomputing, and large data centers."

> "AMD was the first company to integrate a dedicated neural processing unit (NPU) on the same SoC
> as an x86 CPU for AI PCs."

**FY2025, `0000002488-26-000018`.** The named Intel and Nvidia market-share risk factors are
collapsed into a single generic competition risk factor, and **Intel is described in terms of
"market position", not "market share"**.

> "Some of our competitors may possess stronger market positions, larger customer bases, more design
> wins, and greater financial, sales, marketing, and distribution resources than us."

> "For example, Intel Corporation (Intel) uses its microprocessor market position to price its
> products aggressively and target our customers and channel partners with special incentives."

> "Similarly, Nvidia Corporation (Nvidia) leverages its market position in data center GPU,
> financial resources, and proprietary software ecosystem to promote its systems and influences
> customers who do business with us."

> "Our primary competitor in the supply of CPUs and APUs is Intel."

> "Our products consist mainly of x86 CPUs and APUs marketed under the AMD Ryzen™ and AMD Ryzen™ AI
> brands for consumer, commercial and enthusiast segments."

#### The seven-year drift in AMD's language about Intel

This is a change in *disclosure language*, not a disclosed share number. Recorded because it is
observable in the primary documents and because it is dated.

| Fiscal years | How AMD describes Intel | Where it sits |
|---|---|---|
| FY2019, FY2020 | "Intel Corporation has been the market share leader for microprocessors for many years." | Item 1 **and** Item 1A |
| FY2021, FY2022 | same sentence, unchanged | Item 1A **only** |
| FY2023, FY2024 | sentence deleted; replaced by "Intel's microprocessor **market share position**…" | Item 1A, under a risk factor headed "Intel Corporation's dominance of the microprocessor market…" |
| FY2025 | "share" dropped for Intel entirely: "Intel… uses its microprocessor **market position** to price its products aggressively" | Item 1A, folded into a **generic** competition risk factor; the named Intel and Nvidia risk factors no longer exist |

Two further observable changes, both dated: the Nvidia data-center/CUDA market-share sentence is
dropped after FY2021, and a dedicated **Nvidia** market-share risk factor appears for the first time
in FY2024.

---

## 7. WHAT COULD NOT BE OBTAINED: the complete flag list

| # | Gap | Verdict | Why |
|---|---|---|---|
| 1 | Samsung Electronics, every metric, every year | **UNAVAILABLE** | Not an SEC reporting company. No 10-K/20-F/40-F ever filed. `companyfacts` 404. Rule 12g3-2(b) exemption; discloses in Korea only. |
| 2 | SK hynix, every metric, every year | **UNAVAILABLE** | Listed in the US July 2026 via F-1; first 20-F not yet due. `companyfacts` carries only five fee-table facts. |
| 3 | Rapidus, Samsung Foundry, SK hynix foundry | **UNAVAILABLE** | Private / segments inside non-filers. |
| 4 | GFS FY2016, FY2017, FY2018, all metrics | **UNAVAILABLE** | Pre-IPO. First annual filing is the FY2021 20-F, which reaches back only to FY2019 (income statement) and FY2020 (balance sheet). |
| 5 | GFS FY2019 total assets, total liabilities | **UNAVAILABLE** | The FY2021 20-F's balance sheet begins at 2020-12-31. |
| 6 | AMD FY2019 Data Center segment revenue and operating income | **NOT REPORTED** | AMD ran 2 segments through FY2019 and never recast FY2019 onto the Data Center basis. |
| 6a | **A quantified x86 / server CPU / client CPU share figure for AMD** | **UNKNOWABLE from filings** | All seven AMD 10-Ks FY2019 to FY2025 read in full. AMD never states a share percentage for its own processors in any of them. The words "share gains", "gained share", "unit share", "revenue share", "leadership share" and "share growth" appear nowhere in any of the seven. The only self-claimed share leadership in any year is **game consoles**. See §6.2. The filing-sourced proxy is segment revenue and segment operating income, §6.1. |
| 7 | AMD FY2025 Client-only segment operating income | **NOT REPORTED** | FY2025 10-K merged Client and Gaming into one reportable segment. |
| 8 | NVDA capex FY2016-FY2021 | **RECOVERED from the filed statement** | Tagged with a company-extension element, absent from companyfacts. Read from R7.htm / R8.htm of the FY2018 and FY2021 10-Ks. |
| 9 | NVDA FY2019 revenue and cost of sales | **RECOVERED** | Tagged under the ASC 606 elements that year rather than `Revenues`/`CostOfRevenue`. Same filing. |
| 10 | TSM FY2025, UMC FY2025, all metrics | **RECOVERED from the filed statement** | Both FY2025 20-Fs are filed and tagged, but `companyfacts` / `companyconcept` for CIK 1046179 and CIK 1033767 stop at 2024-12-31 as of 2026-09-07. API lag, not a filing gap. |
| 11 | GFS `DepreciationExpense` | **UNRELIABLE TAG, substituted** | Three different values for FY2022 across three 20-Fs. `DepreciationAndAmortisationExpense` used instead. |
| 12 | INTC and TXN cash from operations, FY2016 | **RECOVERED** | Tagged as `…ContinuingOperations` that year. |
| 13 | AMD D&A (`DepreciationDepletionAndAmortization`) after FY2019 | **NOT TAGGED** | AMD stopped using the element. Only the narrower `Depreciation` line is continuous. |
| 14 | Total debt, all seven companies | **COMPUTED, NOT TAGGED** | No element carries it. Formulas in §4. **None include lease liabilities.** |
| 15 | Equity incl. NCI, INTC FY2016-2018 | **NOT TAGGED** | Intel began tagging the element at FY2019. |
