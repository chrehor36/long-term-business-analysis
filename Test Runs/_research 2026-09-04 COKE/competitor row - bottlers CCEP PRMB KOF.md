# COMPETITOR ROW, BOTTLERS: COCA-COLA EUROPACIFIC PARTNERS (CCEP), PRIMO BRANDS (PRMB), COCA-COLA FEMSA (KOF)
### Filed data only. Transcription and arithmetic per the specified formulas. No verdicts, no conclusions (operator rule 8).
Prepared 2026-09-04 for the COKE (Coca-Cola Consolidated) run. CCEP figures in EUR millions (IFRS); PRMB figures in USD millions (US GAAP); KOF figures in MXN millions (IFRS). Currencies are not converted and no cross-currency comparison is made. All data from SEC EDGAR, fetched with User-Agent "BRK research chrehor36@gmail.com". Rounding follows the filings.

Formula (project standard, applied exactly):
NTOA = total assets - cash and equivalents - short-term investments - goodwill - all intangible assets - operating-lease ROU assets - (total current liabilities - current debt/short-term borrowings - current operating-lease liabilities).
Return on NTOA = operating income (as filed) / NTOA. ROIC incl. goodwill = operating income / (NTOA + goodwill + intangibles).
IFRS note recorded as fact: CCEP and KOF report under IFRS 16, which has a single lessee model with no operating/finance lease split; the ROU and lease-liability figures used are the filers' total lease figures, as labeled below.

## SOURCE DOCUMENTS

| Filer | CIK | Form | Accession no. | Filed | Period | Primary document |
|---|---|---|---|---|---|---|
| Coca-Cola Europacific Partners plc | 0001650107 | 20-F (FY2025) | 0001650107-26-000029 | 2026-03-13 | 2025-12-31 | cce-20251231.htm |
| Coca-Cola Europacific Partners plc | 0001650107 | 20-F (FY2024) | 0001650107-25-000039 | 2025-03-21 | 2024-12-31 | cce-20241231.htm |
| Coca-Cola Europacific Partners plc | 0001650107 | 20-F (FY2023) | 0001650107-24-000025 | 2024-03-15 | 2023-12-31 | cce-20231231.htm |
| Coca-Cola Europacific Partners plc | 0001650107 | 20-F (FY2022) | 0001650107-23-000019 | 2023-03-17 | 2022-12-31 | cce-20221231.htm |
| Primo Brands Corporation | 0002042694 | 10-K (FY2025) | 0001628280-26-012779 | 2026-02-27 | 2025-12-31 | prmb-20251231.htm |
| Primo Brands Corporation | 0002042694 | 10-K (FY2024) | 0002042694-25-000003 | 2025-02-27 | 2024-12-31 | prmb-20241231.htm |
| Coca-Cola FEMSA, S.A.B. de C.V. | 0000910631 | 20-F (FY2025) | 0001628280-26-025313 | 2026-04-16 | 2025-12-31 | kof-20251231.htm |
| Coca-Cola FEMSA, S.A.B. de C.V. | 0000910631 | 20-F (FY2024) | 0001628280-25-017225 | 2025-04-10 | 2024-12-31 | kof-20241231.htm |
| Coca-Cola FEMSA, S.A.B. de C.V. | 0000910631 | 20-F (FY2023) | 0001628280-24-016091 | 2024-04-12 | 2023-12-31 | kof-20231231.htm |
| Coca-Cola FEMSA, S.A.B. de C.V. | 0000910631 | 20-F (FY2022) | 0001628280-23-011683 | 2023-04-17 | 2022-12-31 | kof-20221231.htm |

CIK note (fact): the task brief suggested CIK 0001999001 for PRMB; the SEC ticker file resolves CIK 0001999001 to "Six Flags Entertainment Corporation/NEW" (ticker FUN) and resolves ticker PRMB to CIK 0002042694, "Primo Brands Corp". CIK 0002042694 is used throughout.

Column sourcing convention: each fiscal year's figures are taken from the latest annual filing whose XBRL tags that year (balance sheet: FY2025/FY2024 from the FY2025 filing, FY2023 from the FY2024 filing, FY2022 from the FY2023 filing, FY2021 from the FY2022 filing; income statements analogous with three-year coverage). Exception: all KOF FY2025 figures are transcribed from the rendered financial statements of the FY2025 20-F itself (accession 0001628280-26-025313, viewer files R3 = statement of financial position, R4 = income statement, R162 = segment note), because the SEC companyfacts API carries no KOF facts dated after 2024-12-31 (see flag 2).

Cross-checks against the filed statements: CCEP Total assets EUR 29,872m, Cash and cash equivalents EUR 918m and Current portion of borrowings EUR 470m verified against the consolidated statement of financial position as rendered from cce-20251231.htm; KOF Total assets Ps. 314,539m and Gross profit Ps. 133,176m verified against the statements rendered from kof-20251231.htm; PRMB Total assets $10,602.8m, Operating income $430.4m and Total current liabilities $1,282.7m located in the text of prmb-20251231.htm.

---

# 1. COCA-COLA EUROPACIFIC PARTNERS plc (CCEP) - EUR millions, IFRS

## 1.1 Balance-sheet inputs (fiscal year end, as filed, with line labels)

| Balance-sheet line (label as filed) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| Total assets | 29,090 | 29,313 | 29,254 | 31,100 | 29,872 |
| Cash and cash equivalents | 1,407 | 1,387 | 1,419 | 1,563 | 918 |
| Short-term investments | 58 | 256 | 568 | 150 | 39 |
| Goodwill | 4,623 | 4,600 | 4,514 | 4,687 | 4,536 |
| Intangible assets | 12,639 | 12,505 | 12,395 | 12,749 | 12,490 |
| Right-of-use assets (tagged RightofuseAssets; included within "Property, plant and equipment" on the face) | 649 | 683 | 681 | 691 | 676 |
| Total current liabilities | 6,093 | 7,313 | 7,278 | 8,149 | 7,585 |
| Current portion of borrowings (INCLUDES current lease obligations) | 1,350 | 1,336 | 1,300 | 1,391 | 470 |
| of which: Lease obligations, current (borrowings note) | 134 | 141 | 150 | 161 | 167 |

Lease presentation as filed: CCEP's balance sheet carries no separate lease-liability line. The "Borrowings and leases" note's Schedule of Borrowings Outstanding lists "Lease obligations" as a component of both non-current borrowings (FY2025: 532; FY2024: 547; FY2023: 542; FY2022: 535; FY2021: 509) and current borrowings (row above). Current lease figures: FY2025/FY2024 from the FY2025 20-F (R104); FY2023/FY2022 from the FY2023 20-F (R96); FY2021 from the FY2022 20-F (R92). Right-of-use assets are inside PP&E on the face; the values above are the tagged ifrs-full:RightofuseAssets facts from the same filings as the corresponding balance-sheet columns.

Also on the face but NOT named by the formula and therefore not adjusted (FLAGGED): "Assets held for sale" 33 (FY2025) and 46 (FY2024); derivative assets (current 84, non-current 34 at FY2025); "Investment property" 86 (FY2025).

## 1.2 NTOA and return on unleveraged net tangible operating assets

Non-debt, non-lease current liabilities = Total current liabilities - Current portion of borrowings. (The current lease obligation is inside Current portion of borrowings, so subtracting total current borrowings removes debt and lease in one step; no double count.)

| Item | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| Non-debt, non-lease current liabilities | 4,743 | 5,977 | 5,978 | 6,758 | 7,115 |
| **NTOA** | **4,971** | **3,905** | **3,699** | **4,502** | **4,098** |
| Operating profit (as filed) | 1,516 | 2,086 | 2,339 | 2,132 | 2,793 |
| **Return on NTOA** | **30.5%** | **53.4%** | **63.2%** | **47.4%** | **68.2%** |

## 1.3 ROIC including goodwill and intangibles

| Item | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| Denominator (NTOA + goodwill + intangibles) | 22,233 | 21,010 | 20,608 | 21,938 | 21,124 |
| **ROIC incl. goodwill** | **6.8%** | **9.9%** | **11.3%** | **9.7%** | **13.2%** |

## 1.4 Revenue, cost of sales, gross margin, operating margin

Income-statement labels as filed (ifrs-full tags): Revenue, Cost of sales, Gross profit, Operating profit.

| Item | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| Revenue | 13,763 | 17,320 | 18,302 | 20,438 | 20,901 |
| Cost of sales | 8,677 | 11,096 | 11,582 | 13,227 | 13,461 |
| Gross profit | 5,086 | 6,224 | 6,720 | 7,211 | 7,440 |
| **Gross margin** | **37.0%** | **35.9%** | **36.7%** | **35.3%** | **35.6%** |
| Operating profit | 1,516 | 2,086 | 2,339 | 2,132 | 2,793 |
| **Operating margin** | **11.0%** | **12.0%** | **12.8%** | **10.4%** | **13.4%** |

Facts for context, from the filings (no adjustment made): FY2024 20-F: "Reported operating profit decreased by 8.8%, reflecting higher business transformation costs and non-cash impairment of our Indonesian business unit." FY2025 20-F: "Reported operating profit was EUR 2.8 billion, up 31.0%, or up 7.1% on an adjusted comparable and FX neutral basis." CCEP acquired Coca-Cola Beverages Philippines, Inc. during FY2024; reported FY2024 revenue and volume include it from acquisition, and CCEP's "adjusted comparable" measures (non-IFRS) present it as if owned from the beginning of 2024.

## 1.5 Unit case volume and revenue per unit case, as filed (MD&A "Business and financial review", transcribed)

CCEP footnote: "A unit case equals approximately 5.678 litres or 24 eight ounce servings, a typical volume measure used in our industry."

Reported volume table, FY2025 20-F ("Adjusted comparable volume - selling day shift CCEP", in millions of unit cases): Volume 3,958 (2025) vs 3,864 (2024), % change 2.4%; Comparable volume - selling day shift adjusted 3,958 vs 3,854, 2.7%; Adjusted comparable volume 3,958 vs 3,949, 0.2%.

### FY2025 (FY2025 20-F, verbatim)
"Reported revenue totalled EUR 20.9 billion, up 2.3% on a reported basis and 2.8% on an adjusted comparable and FX neutral basis."
"Volume increased 2.4% on a reported basis. Adjusted comparable volume was up 0.2% and adjusted comparable and FX neutral revenue per unit case increased 2.9%."
"We grew revenue per unit case on an adjusted comparable and FX neutral basis, driven by favourable mix, positive headline price increases and promotional optimisation."
By segment: "Revenue per unit case in Europe increased by 3.6% in 2025, on a comparable and FX neutral basis, reflecting positive headline price increases and promotional optimisation alongside favourable mix and the impact of sugar tax in France." APS: "Revenue per unit case increased by 1.4% in 2025, on an adjusted comparable and FX neutral basis. Volume increased 1.0% on an adjusted comparable basis driven by strong underlying momentum in Australia/Pacific, partially offset by a weaker consumer backdrop in Indonesia." Europe volume: "driving a volume decline of 0.2%".

### FY2024 (FY2024 20-F, verbatim)
"Reported revenue totalled EUR 20.4 billion, up 11.7% on a reported basis and 3.5% on an adjusted comparable and FX neutral basis."
"Volume increased 17.8% on a reported basis. Adjusted comparable volume was flat and adjusted comparable and FX neutral revenue per unit case increased 2.7%."
"Volume remained resilient despite mixed summer weather in Europe and strategic stock keeping unit (SKU) rationalisation, with solid underlying volume performance. Revenue per case growth reflected positive headline pricing, promotional optimisation and favourable brand mix, partially offset by geographic mix."

### FY2023 (FY2023 20-F, verbatim)
"Reported revenue increased by 5.5%, or 8.0% on a comparable and FX neutral basis. Volumes were down 0.5%(A) and revenue per unit case increased by 8.5%(B)." Filed footnotes: "(A) On a comparable basis, No selling day shift in FY23. (B) On a comparable and foreign exchange (FX) neutral basis."
"Successful implementation of our revenue and margin growth management initiatives, along with our dynamic price and promotion strategies across a broad pack offering, drove revenue per unit case growth of 8.5%."

Measurement note recorded as fact: CCEP's volume and revenue-per-unit-case percentage changes are stated by CCEP on reported, comparable, and "adjusted comparable" bases; the comparable and adjusted comparable measures are labeled non-IFRS performance measures in the filings.

## 1.6 Competitive position and pricing (verbatim; FY2025 20-F, acc 0001650107-26-000029)

1. Competition section: "CCEP competes mainly in the manufacturing, sale and distribution of NARTD beverages industry and adjacencies, including squashes/cordials, hot beverages and low ARTD beverages. CCEP competes in the Western Europe and APS segments, and primarily manufactures, sells and distributes the products of TCCC, as well as those of other franchisors, such as Monster Energy."
2. Competition section: "CCEP sells and distributes to a wide range of customers, including both physical and online food and beverage retailers, wholesalers and out of retail customers. The market is highly competitive, and all CCEP customers and consumers may choose freely between products of CCEP and its competitors."
3. Competition section: "CCEP competes with respect to a wide range of commercial factors, including brand awareness, product and packaging innovations, supply chain efficacy, customer service, sales strategy, marketing, and pricing and promotions."
4. Risk factors: "We operate in the highly competitive beverage industry and face strong competition from other general and speciality beverage companies. The timing and effectiveness of our response to continued and increased competitor and customer consolidations and marketplace competition may result in lower than expected net pricing of our products."
5. Risk factors: "A significant amount of our volume is sold through large retail chains, including supermarkets and wholesalers. Many of these customers are consolidating or are forming buying groups, which increases their purchasing power. They may seek to use this to improve their profitability through lower prices or harmonised prices across customers and/or countries, increased emphasis on generic and other private label brands, or increased promotional programmes and payment of rebates."

---

# 2. PRIMO BRANDS CORPORATION (PRMB) - USD millions, US GAAP

Structure fact, transcribed from the FY2025 10-K: "On November 8, 2024, Primo Brands consummated the transactions contemplated by the Arrangement Agreement and Plan of Merger, dated as of June 16, 2024". "We accounted for the Transaction as a business combination in which BlueTriton was the accounting acquirer." FY2023 and FY2022 comparatives filed under this CIK are therefore the predecessor BlueTriton figures; FY2024 includes Primo Water only from 2024-11-08.

## 2.1 Balance-sheet inputs (fiscal year end, as filed, with line labels)

| Balance-sheet line (tag) | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Total assets | 5,153.8 | 11,194.5 | 10,602.8 |
| Cash and cash equivalents | 44.7 | 613.7 | 376.7 |
| Short-term investments | not tagged (0) | 0 | 0 |
| Goodwill | 817.4 | 3,572.2 | 3,581.9 |
| Intangible assets, net (IntangibleAssetsNetExcludingGoodwill) | 1,420.2 | 3,191.7 | 2,992.7 |
| Operating lease right-of-use assets | 552.0 | 628.7 | 539.3 |
| Total current liabilities | 782.8 | 1,411.5 | 1,282.7 |
| Current portion of long-term debt (LongTermDebtCurrent) | 31.9 | 64.5 | 73.3 |
| Operating lease liability, current | 73.8 | 95.5 | 92.9 |

FY2022 balance-sheet columns are not tagged in either 10-K under this CIK (the FY2024 10-K balance sheet presents 2024 and 2023 only; only Goodwill carries a 2022-12-31 fact, 816.5); the FY2022 NTOA row is left blank. No ShortTermBorrowings or ShortTermInvestments facts are tagged in any year. On the face but NOT named by the formula and therefore left inside current liabilities (FLAGGED): current finance-lease liabilities (FinanceLeaseLiabilityCurrent 1.8 / 27.4 / 36.9 for FY2023/FY2024/FY2025). Restricted cash (RestrictedCashAndCashEquivalents 2.3 / 0.7 / 0.2) is not "cash and equivalents" per the filed tag and was not subtracted; FLAGGED.

## 2.2 NTOA and return on unleveraged net tangible operating assets

Non-debt, non-lease current liabilities = Total current liabilities - Current portion of long-term debt - Operating lease liability, current.

| Item | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Non-debt, non-lease current liabilities | 677.1 | 1,251.5 | 1,116.5 |
| **NTOA** | **1,642.4** | **1,936.7** | **1,995.7** |
| Operating income (OperatingIncomeLoss) | 406.0 | 360.3 | 430.4 |
| **Return on NTOA** | **24.7%** | **18.6%** | **21.6%** |

## 2.3 ROIC including goodwill and intangibles

| Item | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Denominator (NTOA + goodwill + intangibles) | 3,880.0 | 8,700.6 | 8,570.3 |
| **ROIC incl. goodwill** | **10.5%** | **4.1%** | **5.0%** |

## 2.4 Revenue, cost of sales, gross margin, operating margin

Tags: RevenueFromContractWithCustomerExcludingAssessedTax, CostOfRevenue, GrossProfit, OperatingIncomeLoss. FY2022 and FY2023 from the FY2024 10-K (predecessor BlueTriton periods); FY2024/FY2025 from the FY2025 10-K.

| Item | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|
| Net sales | 4,441.1 | 4,698.7 | 5,152.5 | 6,664.0 |
| Cost of sales | 3,446.9 | 3,346.7 | 3,530.9 | 4,643.8 |
| Gross profit | 994.2 | 1,352.0 | 1,621.6 | 2,020.2 |
| **Gross margin** | **22.4%** | **28.8%** | **31.5%** | **30.3%** |
| Operating income | 23.3 | 406.0 | 360.3 | 430.4 |
| **Operating margin** | **0.5%** | **8.6%** | **7.0%** | **6.5%** |

FY2025 and FY2024 gross margins match the MD&A's stated figures ("gross margin as a percentage of net sales was 30.3%, as compared to 31.5%"). Fact for context (no adjustment made): FY2025 operating income includes "acquisition, integration and restructuring expenses" of $167.5 million (FY2024: $204.1 million per the stated decrease of $36.6 million); the FY2024 comparison basis includes only ~8 weeks of Primo Water.

## 2.5 Volume and price/mix disclosure (where looked, and what is filed)

Unit volume: NOT DISCLOSED. Locations checked: Item 7 MD&A "Results of Operations" of the FY2025 10-K (net sales, cost of sales, gross profit discussion), the "Net sales by water type" table, and Item 1 Business. The MD&A presents net sales by water type in dollars only and attributes changes to the Transaction rather than to a volume/price decomposition; no unit-case, gallon, litre or case-count volume metric and no price/mix bridge is filed. The only quantified volume reference in the FY2025 net sales discussion is transcribed below.

Verbatim (FY2025 10-K MD&A): "During the year ended December 31, 2025, net sales were $6,664.0 million, an increase of $1,511.5 million, or 29.3%, as compared to the year ended December 31, 2024, primarily related to $1,541.6 million of net sales attributable to Primo Water as a result of the Transaction, partially offset by a decrease of $80.8 million in volumes attributable to non-recurring sales in 2024 as a result of the sale of the production facility in Ontario, Canada that was completed during the first quarter of 2025."

Net sales by water type (FY2025 10-K MD&A, $ millions): Regional spring water 3,319.9 (2025) vs 3,234.5 (2024), +2.6%; Purified water 2,102.0 vs 1,348.7, +55.9%; Premium water 349.9 vs 94.8, +269.1%; Other water 128.8 vs 140.7, (8.5)%; Other 763.4 vs 333.8, +128.7%; Total 6,664.0 vs 5,152.5, +29.3%.

## 2.6 Competitive position and pricing (verbatim; FY2025 10-K, acc 0001628280-26-012779)

1. Item 1, Competition: "We participate in the highly competitive beverage and bottled water category of the non-alcoholic beverage industry. With respect to the non-alcoholic beverages category, our products compete primarily on the basis of brand image, price, packaging design, taste, advertising, marketing, and promotional activity (including digital), product innovation, efficient production and distribution techniques, and the ability to anticipate and effectively respond to consumer preferences and trends".
2. Item 1, Competition: "Our principal competitors are local, regional, and national bottled water and beverages businesses, providers of various types of water filtration units and services and large retailers who have increasingly utilized their large distribution networks and significant economies of scale in recent years to introduce and develop private-label branded water."
3. Item 7A: "The competitive marketplace in which we operate may limit our ability to recover increased costs through higher prices."

---

# 3. COCA-COLA FEMSA, S.A.B. de C.V. (KOF) - MXN millions ("Ps."), IFRS

## 3.1 Balance-sheet inputs (fiscal year end, as filed, with line labels)

| Balance-sheet line (label as filed) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| Total assets | 271,567 | 277,995 | 273,520 | 307,986 | 314,539 |
| Cash and cash equivalents | 47,248 | 40,277 | 31,060 | 32,779 | 28,067 |
| Short-term investments | no such line on the face (0) | 0 | 0 | 0 | 0 |
| Intangible assets, net (INCLUDES goodwill; tagged IntangibleAssetsAndGoodwill) | 102,174 | 103,122 | 101,162 | 101,876 | 102,356 |
| Right-of-use assets, net | 1,472 | 2,069 | 2,388 | 2,989 | 2,617 |
| Total current liabilities | 46,221 | 57,960 | 54,916 | 67,171 | 66,757 |
| Bank loans and notes payable, current (ShorttermBorrowings) | 645 | 0 | 88 | 1,443 | 4,032 |
| Current portion of non-current debt (CurrentPortionOfLongtermBorrowings) | 1,808 | 8,524 | 52 | 1,871 | 3,912 |
| Current portion of lease liabilities | 614 | 472 | 752 | 889 | 631 |

Presentation notes (facts): KOF's balance sheet carries a single "Intangible assets, net" line that includes goodwill (the XBRL tag is ifrs-full:IntangibleAssetsAndGoodwill); the formula subtracts goodwill and intangibles alike, so the combined line is subtracted once and no split is needed for NTOA. "Other current financial assets" (931 / 2,911 / 567 / 946 / 761 for FY2021-FY2025) is on the face but is not named by the formula and was NOT subtracted; FLAGGED.

## 3.2 NTOA (return on NTOA cannot be computed; see 3.4)

Non-debt, non-lease current liabilities = Total current liabilities - Bank loans and notes payable - Current portion of non-current debt - Current portion of lease liabilities.

| Item | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| Non-debt, non-lease current liabilities | 43,154 | 48,964 | 54,024 | 62,968 | 58,182 |
| **NTOA** | **77,519** | **83,563** | **84,886** | **107,374** | **123,317** |
| Operating income as filed | n/d | n/d | n/d | n/d | n/d |
| **Return on NTOA** | blank | blank | blank | blank | blank |

n/d = not disclosed. See 3.4.

## 3.3 Revenue, cost of goods sold, gross margin

Income-statement labels as filed: "Total revenues", "Cost of goods sold", "Gross profit". FY2021/FY2022 from XBRL of the FY2023/FY2024 20-Fs; FY2023-FY2025 from the FY2025 20-F income statement.

| Item | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| Total revenues | 194,804 | 226,740 | 245,088 | 279,793 | 291,746 |
| Cost of goods sold | 106,206 | 126,440 | 134,228 | 151,057 | 158,570 |
| Gross profit | 88,598 | 100,300 | 110,860 | 128,736 | 133,176 |
| **Gross margin** | **45.5%** | **44.2%** | **45.2%** | **46.0%** | **45.6%** |
| Operating income / operating margin | n/d | n/d | n/d | n/d | n/d |

## 3.4 Operating income: not disclosed (the search trail)

KOF's consolidated income statement in the FY2025 20-F presents no operating-income subtotal: the statement runs Gross profit, Administrative expenses, Selling expenses, Other income, Other expenses, Interest expense, Interest income, FX, monetary position, market value gains, then "Income before income taxes and share of the profit or loss of associates and joint ventures accounted for using the equity method". The segment note (R162) uses that same income-before-taxes measure per segment, not operating income. No ifrs-full:ProfitLossFromOperatingActivities fact exists in KOF's companyfacts for any year. The FY2025 MD&A references "operating income growth" narratively ("This 0.5% increase was mainly driven by operating income growth...") without stating an operating-income figure. Per instruction, the operating-income component is left blank rather than derived, so Return on NTOA and operating margin are blank for all KOF years. (An FY2023 verification: the same statement structure, with no operating subtotal, appears in the FY2024 20-F income statement.)

## 3.5 Sales volume and average price per unit case, as filed (MD&A, transcribed)

KOF definitions, verbatim: "Except when specifically indicated, 'sales volume' in this annual report refers to sales volume in terms of unit cases." "A 'unit case' refers to 192 ounces of finished beverage product (24 eight-ounce servings) and, when applied to soda fountains, refers to the volume of syrup, powders and concentrate that is required to produce 192 ounces of finished beverage product." "Average Price Per Unit Case. We use average price per unit case to analyze average pricing trends in the different territories where we operate. We calculate average price per unit case by dividing net sales by total sales volume. Sales of beer and spirits, which are not included in our sales volumes, are excluded from this calculation."

### FY2025 (FY2025 20-F MD&A, verbatim)
"Our consolidated total revenues increased by 4.3% to Ps. 291,746 million in 2025 as compared to 2024, mainly as a result of our revenue management initiatives and partially offset by volume decline and unfavorable currency translation effects into Mexican pesos."
"Total sales volume decreased by 1.8% to 4,150.4 million unit cases in 2025 as compared to 2024, driven mainly by volume decline in Mexico, Colombia and Panama, and partially offset by volume growth in the rest of our territories."
"Consolidated average price per unit case increased by 6.0% to Ps. 68.09 in 2025, as compared to Ps. 64.23 in 2024, mainly as a result of our revenue management initiatives. These factors were offset by the negative translation effect resulting from the appreciation of most of our operating currencies relative to the Mexican peso."
Segment volume: Mexico, Guatemala and Central America South down 4.1% to 2,391.7 million unit cases (Mexico down 5.2% to 2,013.6, "as a result of macroeconomic deceleration and the temporary effects of negative brand sentiment at the beginning of the year"); South America up 1.6% to 1,758.7 million unit cases.

### FY2024 (same statements in the FY2025 and FY2024 20-Fs, verbatim)
"Total sales volume increased by 4.4% to 4,224.6 million unit cases in 2024 as compared to 2023, driven mainly by growth in most of our territories, including a strong performance in Mexico, Brazil and Guatemala, partially offset by volume decline in Argentina and Uruguay."
"Consolidated average price per unit case increased by 9.7% to Ps. 64.23 in 2024, as compared to Ps. 58.54 in 2023, mainly as a result of our revenue management initiatives and favorable mix effects. These factors were offset by the negative translation effect resulting from the depreciation of most of our operating currencies relative to the Mexican peso."

### FY2023 (FY2024 20-F MD&A, verbatim)
"Total sales volume increased by 7.8% to 4,047.8 million unit cases in 2023 as compared to 2022, driven mainly by growth in all of our territories, including a strong performance in Mexico, Brazil, Colombia and Guatemala in 2023."
"Consolidated average price per unit case decreased by 0.4% to Ps. 58.54 in 2023, as compared to Ps. 58.75 in 2022, mainly as a result of the negative translation effect resulting from the depreciation of most of our operating currencies relative to the Mexican peso. This was partially offset by favorable mix effects and revenue management initiatives."

## 3.6 Competitive position and pricing (verbatim; FY2025 20-F, acc 0001628280-26-025313)

1. Item 4, Competition: "Our principal competitors are local Pepsi bottlers and other bottlers and distributors of local beverage brands. We also face competition in many of our territories from producers of B brands. A number of our competitors in Central America, Brazil, Argentina and Colombia offer beer in addition to sparkling beverages, still beverages and water, which may enable them to achieve distribution efficiencies that other competitors who do not offer an integrated portfolio may not achieve."
2. Item 4, Competition (Mexico): "Our principal competitor in Mexico is Grupo GEPP, S.A.P.I. de C.V., the exclusive bottler of Pepsi beverage products and subsidiary of Organización Cultiba, S.A.B. de C.V. ... In addition, we compete with Keurig Dr Pepper in sparkling beverages and with other local brands in our Mexican territories, as well as 'B brand' producers, such as Embotelladora Aga de Mexico, S.A. de C.V. (Red Cola bottler), that offer various presentations of sparkling and still beverages." (ellipsis marks omitted listing of the joint-venture parents)
3. Item 4 (Brazil): "In Brazil, we compete against AmBev, a company that distributes Pepsi brands, local brands with flavors such as guarana, and proprietary beer brands. We also compete against B brands or 'Tubainas,' which are small, local producers of low-cost sparkling beverages that represent a significant portion of the sparkling beverage market."

---

# 4. FLAGS AND DATA OBSTACLES (all items already marked above, collected here)

1. **PRMB CIK correction.** The brief's suggested CIK 0001999001 belongs to Six Flags Entertainment Corporation/NEW (FUN). Primo Brands Corp is CIK 0002042694 per the SEC ticker file; verified by entity name and ticker in the submissions API.
2. **KOF FY2025 absent from the XBRL APIs.** The SEC companyfacts file for CIK 0000910631 contains no facts dated after 2024-12-31 even though the FY2025 20-F (acc 0001628280-26-025313, filed 2026-04-16) is on EDGAR with full inline XBRL. All KOF FY2025 figures were therefore transcribed from that filing's rendered statements (R3, R4, R162) and the FY2025/FY2024 columns cross-checked against the FY2024 20-F's tagged facts (they agree for FY2024).
3. **KOF operating income is not disclosed** in any location checked (income statement face, segment note, MD&A; FY2025 and FY2024 20-Fs; companyfacts all years). Return on NTOA and operating margin are blank for KOF in every year rather than derived from Gross profit minus expense lines, per the no-guessing instruction.
4. **KOF goodwill/intangibles are one combined line** ("Intangible assets, net", tag IntangibleAssetsAndGoodwill). NTOA subtracts the combined line once; a goodwill-only figure is not tagged after FY2020 (last tagged Goodwill fact: 100,082 at 2020-12-31).
5. **KOF "Other current financial assets"** (761 at FY2025) not subtracted; the formula names only cash and short-term investments, and KOF's face has no short-term investments line.
6. **CCEP leases sit inside borrowings.** No lease-liability line on the face; current lease obligations (134/141/150/161/167 for FY2021-FY2025) are a component of "Current portion of borrowings" per the borrowings note, so NTOA subtracts total current borrowings once (debt + lease in one step). Right-of-use assets sit inside PP&E on the face; values taken from the tagged RightofuseAssets facts. CCEP last tagged a separate CurrentLeaseLiabilities fact in a 2019 6-K, not in any 20-F.
7. **IFRS single lease model (CCEP, KOF).** The formula's "operating-lease ROU" and "current operating-lease liability" are mapped to the filers' total IFRS 16 lease figures; no operating/finance split exists.
8. **CCEP items on the face not named by the formula, not adjusted:** Assets held for sale 33 (FY2025) / 46 (FY2024); derivative assets; investment property 86 (FY2025).
9. **PRMB comparability.** The 2024-11-08 BlueTriton/Primo Water merger makes FY2022-FY2023 predecessor (BlueTriton-only) periods, FY2024 a ~8-week-Primo-Water period, and FY2025 the first full combined year; the filings state this and no adjustment was made. FY2022 balance sheet is not filed under this CIK (income statement only); the FY2022 NTOA column is blank.
10. **PRMB items left inside current liabilities (not named by the formula):** current finance-lease liabilities 36.9 (FY2025); restricted cash 0.2 (FY2025) not subtracted from cash.
11. **PRMB unit volume not disclosed** (see 2.5 for the locations checked); no price/mix decomposition is filed.
12. **One-offs inside operating income (no adjustments made):** CCEP FY2024 operating profit includes business transformation costs and a non-cash impairment of the Indonesian business unit (MD&A wording; reported operating profit down 8.8% while the filer's non-IFRS adjusted comparable measure rose 8.0%); PRMB operating income includes acquisition, integration and restructuring expenses of 167.5 (FY2025) and 204.1 (FY2024).
13. **Cross-currency and cross-GAAP.** CCEP (EUR, IFRS), PRMB (USD, US GAAP) and KOF (MXN, IFRS) figures are each in their filing currency and framework; no conversion or restatement was performed. KOF 20-Fs include a convenience translation of FY2025 at Ps. 18.0057 per USD, "solely for the convenience of the reader" (not used here).
14. **CCEP volume measures are multi-basis.** Reported (+2.4% FY2025, +17.8% FY2024 including the Philippines acquisition), comparable, and "adjusted comparable" (non-IFRS, treating the Philippines as owned from the start of 2024); each quote in 1.5 carries its basis as filed.
