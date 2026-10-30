TEMPLATE = """## The Procter & Gamble Company (PG)

### Documents used

| file | form | fiscal period end | filing date | accession |
|---|---|---|---|---|
| PG_10K_FY2021_2021-06-30.txt | 10-K | 2021-06-30 | 2021-08-06 | 0000080424-21-000100 |
| PG_10K_FY2022_2022-06-30.txt | 10-K | 2022-06-30 | 2022-08-05 | 0000080424-22-000064 |
| PG_10K_FY2023_2023-06-30.txt | 10-K | 2023-06-30 | 2023-08-04 | 0000080424-23-000073 |
| PG_10K_FY2024_2024-06-30.txt | 10-K | 2024-06-30 | 2024-08-05 | 0000080424-24-000083 |
| PG_10K_FY2025_2025-06-30.txt | 10-K | 2025-06-30 | 2025-08-04 | 0000080424-25-000076 |
| PG_10K_FY2026_2026-06-30.txt | 10-K | 2026-06-30 | 2026-08-04 | 0000080424-26-000103 |

Filing metadata from peers/manifest_list.txt (PG entry). PG fiscal years end June 30. **No interim filing is on disk:** no PG 10-Q has been filed after the FY2026 10-K (filed 2026-08-04), and manifest_list.txt lists none, so there is no interim period in this section.

Conventions used below:
- Line numbers are the 0-based line index printed by `g.py` (the same index `python g.py <file> --lines START END` prints).
- PG's filed tables use the long dash character (Unicode U+2014) to mean zero or nil. Table-row quotes keep it verbatim because the quote must match the filing; in the parsed tables it is written as 0.
- Parentheses in PG tables mean negative. In parsed tables negatives are written with a minus sign.
- Each year is taken from the 10-K that first reports it. PG presents only the current year in both the Net Sales Change Drivers table and the Organic Sales Growth reconciliation, so no later 10-K re-presents those two tables for a prior year.

### 1. Organic sales decomposition

**Organic sales definition (quoted in full under Gaps; newest filing):**
@@L~~F26~~740@@

**Table footnotes (same wording in every year):**
@@L~~F26~~581@@
@@L~~F26~~582@@
@@L~~F26~~752@@

#### FY2021 (10-K for fiscal year ended June 30, 2021)
Net Sales Change Drivers table:
@@L~~F21~~596@@
@@L~~F21~~598@@
@@L~~F21~~599@@
@@L~~F21~~600@@
@@L~~F21~~602@@
@@L~~F21~~605@@

Organic Sales Growth reconciliation:
@@L~~F21~~825@@
@@L~~F21~~826@@
@@L~~F21~~828@@
@@L~~F21~~831@@

Narrative (total, Beauty, Health Care):
@@P~~F21~~549~~Excluding the net impacts~~organic volume.@@
@@P~~F21~~617~~Organic sales increased 6%~~organic volume.@@
@@P~~F21~~641~~Organic sales increased 9%.~~9%.@@

#### FY2022 (10-K for fiscal year ended June 30, 2022)
@@L~~F22~~610@@
@@L~~F22~~612@@
@@L~~F22~~613@@
@@L~~F22~~614@@
@@L~~F22~~616@@
@@L~~F22~~619@@

Organic Sales Growth reconciliation (header row is split across lines 822 to 824 by the extraction):
@@P~~F22~~823~~Year ended June 30, 2022~~Impact/Other (1)@@
@@L~~F22~~824@@
@@L~~F22~~825@@
@@L~~F22~~827@@
@@L~~F22~~830@@

Narrative:
@@P~~F22~~564~~Excluding the net impacts~~organic volume.@@
@@P~~F22~~631~~Organic sales also increased 2%.~~2%.@@
@@P~~F22~~656~~Organic sales increased 10%.~~10%.@@

#### FY2023 (10-K for fiscal year ended June 30, 2023)
@@L~~F23~~578@@
@@L~~F23~~580@@
@@L~~F23~~581@@
@@L~~F23~~582@@
@@L~~F23~~584@@
@@L~~F23~~587@@

Organic Sales Growth reconciliation (header split across lines 774 to 777 by the extraction):
@@L~~F23~~774@@
@@L~~F23~~775@@
@@L~~F23~~776@@
@@L~~F23~~777@@
@@L~~F23~~778@@
@@L~~F23~~780@@
@@L~~F23~~783@@

Narrative:
@@P~~F23~~535~~Excluding the impacts~~organic sales grew 7%.@@
@@L~~F23~~599@@
@@P~~F23~~619~~Excluding the impact of foreign exchange~~organic sales increased 8%.@@

#### FY2024 (10-K for fiscal year ended June 30, 2024)
@@L~~F24~~572@@
@@L~~F24~~574@@
@@L~~F24~~575@@
@@L~~F24~~576@@
@@L~~F24~~578@@
@@L~~F24~~581@@

Organic Sales Growth reconciliation:
@@L~~F24~~747@@
@@L~~F24~~748@@
@@L~~F24~~749@@
@@L~~F24~~750@@
@@L~~F24~~751@@
@@L~~F24~~753@@
@@L~~F24~~756@@

Narrative:
@@P~~F24~~533~~Organic sales, which exclude~~increased 4%.@@
@@P~~F24~~590~~Excluding the impact~~organic sales increased 3%.@@
@@P~~F24~~610~~Excluding the impact~~organic sales also increased 5%.@@

#### FY2025 (10-K for fiscal year ended June 30, 2025)
@@L~~F25~~570@@
@@L~~F25~~572@@
@@L~~F25~~573@@
@@L~~F25~~574@@
@@L~~F25~~576@@
@@L~~F25~~579@@

Organic Sales Growth reconciliation:
@@L~~F25~~745@@
@@L~~F25~~746@@
@@L~~F25~~747@@
@@L~~F25~~748@@
@@L~~F25~~749@@
@@L~~F25~~751@@
@@L~~F25~~754@@

Narrative:
@@L~~F25~~530@@
@@P~~F25~~531~~Organic sales, which exclude~~increased 2%.@@
@@P~~F25~~589~~Excluding the impact~~organic sales increased 1%.@@
@@P~~F25~~610~~Excluding the impact~~organic sales increased 3%.@@

#### FY2026 (10-K for fiscal year ended June 30, 2026)
@@L~~F26~~571@@
@@L~~F26~~573@@
@@L~~F26~~574@@
@@L~~F26~~575@@
@@L~~F26~~577@@
@@L~~F26~~580@@

Organic Sales Growth reconciliation:
@@L~~F26~~742@@
@@L~~F26~~743@@
@@L~~F26~~744@@
@@L~~F26~~745@@
@@L~~F26~~746@@
@@L~~F26~~748@@
@@L~~F26~~751@@

Narrative:
@@L~~F26~~528@@
@@P~~F26~~589~~Beauty net sales increased 7%~~organic sales increased 5%.@@
@@P~~F26~~610~~Health Care net sales increased 4%~~organic sales increased 1%.@@

#### Parsed table

Column labels are PG's: "Volume with Acquisitions & Divestitures" (vol incl. A&D), "Volume Excluding Acquisitions & Divestitures" (vol excl. A&D; PG's MD&A calls this "organic volume" in FY2021 and FY2022), "Foreign Exchange", "Price", "Mix", "Other" (footnote: sales mix impact of acquisitions and divestitures plus rounding), "Net Sales Growth". Organic is from the separate "Organic Sales Growth" reconciliation. The "acq/div" column below is the reconciliation's "Acquisition & Divestiture Impact/Other" column. Sign convention: in the Drivers table FX is the effect on reported sales; in the reconciliation "Foreign Exchange Impact" is the adjustment added to reported growth to reach organic growth, so it carries the opposite sign (for example FY2026 Beauty: Drivers FX +2, reconciliation FX (2)). The FX column below uses the Drivers-table sign. All figures are percent; they are PG's rounded whole-number approximations (footnote (1) of the Drivers table).

| year | scope | reported net sales growth | organic | volume incl. A&D | volume excl. A&D | Price | Mix | FX (Drivers sign) | acq/div (recon. A&D Impact/Other) | Other (Drivers) | label wording used | source line |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2021 | Total company | +7 | +6 | +3 | +3 | +1 | +2 | +1 | 0 | 0 | Volume / Price / Mix / Foreign Exchange / Other | F21 605, 831 |
| FY2021 | Health Care | +10 | +9 | +6 | +6 | +1 | +2 | +1 | 0 | 0 | same | F21 602, 828 |
| FY2021 | Beauty | +8 | +6 | +3 | +3 | +2 | +1 | +2 | 0 | 0 | same | F21 600, 826 |
| FY2022 | Total company | +5 | +7 | +2 | +2 | +4 | +1 | -2 | 0 | 0 | same | F22 619, 830 |
| FY2022 | Health Care | +9 | +10 | +4 | +4 | +3 | +3 | -1 | 0 | 0 | same | F22 616, 827 |
| FY2022 | Beauty | +2 | +2 | 0 | 0 | +3 | -1 | 0 | 0 | 0 | same | F22 614, 825 |
| FY2023 | Total company | +2 | +7 | -3 | -3 | +9 | +1 | -5 | 0 | 0 | same | F23 587, 783 |
| FY2023 | Health Care | +4 | +8 | -1 | -1 | +5 | +4 | -4 | 0 | 0 | same | F23 584, 780 |
| FY2023 | Beauty | +2 | +6 | -1 | -2 | +8 | -1 | -5 | -1 | +1 | same | F23 582, 778 |
| FY2024 | Total company | +2 | +4 | 0 | 0 | +4 | 0 | -2 | 0 | 0 | same | F24 581, 756 |
| FY2024 | Health Care | +5 | +5 | -1 | -1 | +4 | +2 | 0 | 0 | 0 | same | F24 578, 753 |
| FY2024 | Beauty | +1 | +3 | 0 | 0 | +4 | -1 | -2 | 0 | 0 | same | F24 576, 751 |
| FY2025 | Total company | 0 | +2 | 0 | +1 | +1 | 0 | -1 | +1 | 0 | same | F25 579, 754 |
| FY2025 | Health Care | +2 | +3 | -1 | -1 | +1 | +3 | -1 | 0 | 0 | same | F25 576, 751 |
| FY2025 | Beauty | -2 | +1 | -1 | +1 | +2 | -2 | -1 | +2 | 0 | same | F25 574, 749 |
| FY2026 | Total company | +3 | +1 | 0 | 0 | +1 | 0 | +2 | 0 | 0 | same | F26 580, 751 |
| FY2026 | Health Care | +4 | +1 | -2 | -2 | +2 | +1 | +3 | 0 | 0 | same | F26 577, 748 |
| FY2026 | Beauty | +7 | +5 | +4 | +4 | +1 | 0 | +2 | 0 | 0 | same | F26 575, 746 |

(F21 = PG_10K_FY2021_2021-06-30.txt, and so on for F22 to F26.)

Arithmetic note (computed, not filed): in every row above, volume incl. A&D + Price + Mix + FX + Other equals reported net sales growth, and reported growth minus FX plus the reconciliation's A&D Impact/Other equals organic. Example FY2026 Health Care: -2 + 2 + 1 + 3 + 0 = +4 reported; 4 - 3 + 0 = +1 organic. So PG's organic growth contains volume, price and mix, with mix as a separate column.

#### Oral Care sentences in the Health Care discussion (each year, first-reporting 10-K)
@@L~~F21~~642@@
@@L~~F22~~657@@
@@L~~F23~~621@@
@@L~~F24~~611@@
@@L~~F25~~611@@
@@L~~F26~~611@@

Oral Care size and share (newest filing):
@@P~~F26~~457~~In oral care, we are a leader~~Oral-B brands.@@
@@L~~F26~~438@@
@@L~~F26~~1117@@
@@L~~F26~~1124@@

### 2. GAAP operating margin (and segment margin)

Income statement caption: "OPERATING INCOME" (Consolidated Statements of Earnings). Each year from the 10-K that first reports it.

@@L~~F21~~959@@
@@L~~F21~~960@@
@@L~~F21~~961@@
@@L~~F21~~962@@
@@L~~F21~~964@@

@@L~~F22~~956@@
@@L~~F22~~957@@
@@L~~F22~~958@@
@@L~~F22~~959@@
@@L~~F22~~960@@

@@L~~F23~~879@@
@@L~~F23~~880@@
@@L~~F23~~881@@
@@L~~F23~~882@@
@@L~~F23~~883@@

@@L~~F24~~874@@
@@L~~F24~~875@@
@@L~~F24~~876@@
@@L~~F24~~877@@
@@L~~F24~~878@@
@@L~~F24~~879@@

@@L~~F25~~882@@
@@L~~F25~~883@@
@@L~~F25~~884@@
@@L~~F25~~885@@
@@L~~F25~~887@@

@@L~~F26~~884@@
@@L~~F26~~885@@
@@L~~F26~~886@@
@@L~~F26~~887@@
@@L~~F26~~889@@

PG's own MD&A operating-margin rows (cross-check of the computed figures):
@@L~~F21~~558@@
@@L~~F22~~571@@
@@L~~F23~~541@@
@@L~~F24~~538@@
@@L~~F25~~536@@
@@L~~F26~~534@@

| FY | Net sales ($m) | Operating income ($m) | GAAP operating margin (computed) | PG MD&A "Operating margin" | source lines |
|---|---|---|---|---|---|
| FY2021 | 76,118 | 17,986 | 17,986 / 76,118 = 23.6% | 23.6% | F21 960, 964, 558 |
| FY2022 | 80,187 | 17,813 | 17,813 / 80,187 = 22.2% | 22.2% | F22 957, 960, 571 |
| FY2023 | 82,006 | 18,134 | 18,134 / 82,006 = 22.1% | 22.1% | F23 880, 883, 541 |
| FY2024 | 84,039 | 18,545 | 18,545 / 84,039 = 22.1% | 22.1% | F24 875, 879, 538 |
| FY2025 | 84,284 | 20,451 | 20,451 / 84,284 = 24.3% | 24.3% | F25 883, 887, 536 |
| FY2026 | 87,032 | 19,748 | 19,748 / 87,032 = 22.7% | 22.7% | F26 885, 889, 534 |

FY2024 operating income is after an "Indefinite-lived intangible asset impairment charge" of $1,341m (Gillette), shown on the face of the income statement (F24 line 878). No adjustment is made here.

#### Segment margin (Health Care and Beauty)

**Profit line used: "Earnings/(Loss) Before Income Taxes" by segment, from Note 2 (segment note). This is a segment measure, not GAAP operating income.** PG's segments carry blended statutory tax rates, exclude items held in Corporate (including restructuring), and, from the FY2025 10-K presentation, include "Other segment items" (interest and certain non-operating items). "Net Earnings/(Loss)" by segment is also shown for reference.

@@P~~F26~~1110~~Differences between these policies and U.S. GAAP~~blended statutory rates.@@
@@P~~F26~~1112~~As the Company allocates taxes to individual segments~~Net earnings to assess segment performance and@@
@@L~~F26~~1158@@

FY2021 10-K (header row is split across lines 1243 to 1249 by the extraction; columns are Net Sales, Earnings/(Loss) Before Income Taxes, Net Earnings/(Loss), Depreciation and Amortization, Total Assets, Capital Expenditures):
@@L~~F21~~1243@@
@@L~~F21~~1244@@
@@L~~F21~~1245@@
@@L~~F21~~1250@@
@@L~~F21~~1256@@
@@L~~F21~~1269@@

FY2022 10-K (same column order; header split across lines 1235 to 1241):
@@L~~F22~~1235@@
@@L~~F22~~1242@@
@@L~~F22~~1248@@
@@L~~F22~~1260@@

FY2023 10-K (same column order; header split across lines 1156 to 1162):
@@L~~F23~~1156@@
@@L~~F23~~1163@@
@@L~~F23~~1169@@
@@L~~F23~~1181@@

FY2024 10-K (same column order; header split across lines 1135 to 1141):
@@L~~F24~~1135@@
@@L~~F24~~1142@@
@@L~~F24~~1148@@
@@L~~F24~~1160@@

FY2025 10-K (new layout: segments are columns, in the order Beauty, Grooming, Health Care, Fabric & Home Care, Baby, Feminine & Family Care, Corporate, Total Company):
@@L~~F25~~1140@@
@@L~~F25~~1142@@
@@L~~F25~~1143@@
@@L~~F25~~1144@@
@@L~~F25~~1148@@
@@L~~F25~~1149@@

FY2026 10-K (same layout as FY2025):
@@L~~F26~~1145@@
@@L~~F26~~1147@@
@@L~~F26~~1148@@
@@L~~F26~~1149@@
@@L~~F26~~1153@@
@@L~~F26~~1154@@

| FY | scope | segment net sales ($m) | Earnings before income taxes ($m) | EBT / net sales (computed, segment measure) | Net earnings ($m) | Net earnings / net sales (computed; PG MD&A "% of net sales") | source lines |
|---|---|---|---|---|---|---|---|
| FY2021 | Health Care | 9,956 | 2,398 | 24.1% | 1,851 | 18.6% | F21 1256 |
| FY2022 | Health Care | 10,824 | 2,618 | 24.2% | 2,006 | 18.5% | F22 1248 |
| FY2023 | Health Care | 11,226 | 2,759 | 24.6% | 2,125 | 18.9% | F23 1169 |
| FY2024 | Health Care | 11,793 | 2,941 | 24.9% | 2,258 | 19.1% | F24 1148 |
| FY2025 | Health Care | 11,998 | 3,149 | 26.2% | 2,440 | 20.3% | F25 1143, 1148, 1149 |
| FY2026 | Health Care | 12,456 | 3,163 | 25.4% | 2,404 | 19.3% | F26 1148, 1153, 1154 |
| FY2021 | Beauty | 14,417 | 4,018 | 27.9% | 3,210 | 22.3% | F21 1250 |
| FY2022 | Beauty | 14,740 | 3,946 | 26.8% | 3,160 | 21.4% | F22 1242 |
| FY2023 | Beauty | 15,008 | 4,009 | 26.7% | 3,178 | 21.2% | F23 1163 |
| FY2024 | Beauty | 15,220 | 3,805 | 25.0% | 2,963 | 19.5% | F24 1142 |
| FY2025 | Beauty | 14,964 | 3,454 | 23.1% | 2,715 | 18.1% | F25 1143, 1148, 1149 |
| FY2026 | Beauty | 16,023 | 3,473 | 21.7% | 2,672 | 16.7% | F26 1148, 1153, 1154 |

Computation detail (EBT / net sales): HC 2,398/9,956; 2,618/10,824; 2,759/11,226; 2,941/11,793; 3,149/11,998; 3,163/12,456. Beauty 4,018/14,417; 3,946/14,740; 4,009/15,008; 3,805/15,220; 3,454/14,964; 3,473/16,023. The net earnings margins computed here equal the "% of net sales" rows PG prints in each MD&A segment table (for example F26 line 609 "19.3%" for Health Care, F26 line 588 "16.7%" for Beauty).

Re-presentation check: the prior-year segment figures in each later 10-K were compared with the first-reporting 10-K for these two segments (for example FY2021 Health Care 9,956 / 2,398 / 1,851 in F22 line 1249 and F23 line 1171; FY2023 Beauty 15,008 / 4,009 in F25 lines 1173 and 1178; FY2024 Health Care 11,793 / 2,941 in F26 lines 1178 and 1183). No differences were found in the rows compared. Effective July 1, 2024 (fiscal 2025), PG separated the Beauty operating segment "Skin and Personal Care" into "Skin Care" and "Personal Care" (F26 line 1132); the Beauty reportable segment totals were not changed in the rows compared.

Segment gross margin (supplementary; segment "Cost of products sold" is disclosed only from the FY2025 10-K layout, which covers FY2023 to FY2025, and in the FY2026 10-K):
@@L~~F25~~1170@@
@@L~~F25~~1173@@
@@L~~F25~~1174@@
@@L~~F25~~1156@@
@@L~~F25~~1159@@
@@L~~F25~~1160@@

| FY | Health Care: net sales, COGS, gross margin (computed) | Beauty: net sales, COGS, gross margin (computed) | source lines |
|---|---|---|---|
| FY2023 | 11,226 - 4,855 = 6,371; 56.8% | 15,008 - 5,849 = 9,159; 61.0% | F25 1173, 1174 |
| FY2024 | 11,793 - 4,967 = 6,826; 57.9% | 15,220 - 5,722 = 9,498; 62.4% | F25 1159, 1160 |
| FY2025 | 11,998 - 4,974 = 7,024; 58.5% | 14,964 - 5,822 = 9,142; 61.1% | F25 1143, 1144 |
| FY2026 | 12,456 - 5,208 = 7,248; 58.2% | 16,023 - 6,397 = 9,626; 60.1% | F26 1148, 1149 |

### 3. Advertising

PG discloses advertising costs in Note 1 (accounting policies, Selling, General and Administrative Expense). Search terms used: "advertis", "advertising costs", "marketing", "media", "brand support", "A&P". PG does not use "A&P", "brand support" or "BMI" as a caption; the figure is "Advertising costs". Advertising is reported within SG&A.

@@L~~F21~~1163@@
@@L~~F22~~1157@@
@@L~~F23~~1076@@
@@L~~F23~~1079@@
@@L~~F24~~1058@@
@@L~~F25~~1067@@
@@L~~F26~~1069@@

(F23 line 1076 and line 1079 are one sentence split by a page footer at line 1078: extraction artefact.)

| FY | Advertising costs as filed | Net sales ($m) | % of net sales (computed) | source line |
|---|---|---|---|---|
| FY2021 | $8.2 billion | 76,118 | 8,200 / 76,118 = 10.8% | F21 1163 |
| FY2022 | $7.9 billion | 80,187 | 7,900 / 80,187 = 9.9% | F22 1157 |
| FY2023 | $8.0 billion | 82,006 | 8,000 / 82,006 = 9.8% | F23 1076 |
| FY2024 | $9.6 billion | 84,039 | 9,600 / 84,039 = 11.4% | F24 1058 |
| FY2025 | $9.2 billion | 84,284 | 9,200 / 84,284 = 10.9% | F25 1067 |
| FY2026 | $10.2 billion | 87,032 | 10,200 / 87,032 = 11.7% | F26 1069 |

Restated or re-presented amounts in later 10-Ks: FY2021 $8.2bn is repeated in F22 and F23; FY2022 $7.9bn in F23 and F24; FY2023 $8.0bn in F24 and F25; FY2024 $9.6bn in F25 and F26; FY2025 $9.2bn in F26. No differences. Amounts are filed in billions to one decimal, so the computed percentages carry rounding of about plus or minus 0.1 point.

PG does not give a dollar "marketing spending" total. The MD&A gives only the change in marketing spending as a percentage of net sales:
@@L~~F21~~570@@
@@L~~F22~~583@@
@@L~~F23~~555@@
@@L~~F24~~552@@
@@L~~F25~~551@@
@@L~~F26~~551@@

### 4. Gross margin and shipping/handling placement

Gross profit is not a caption on PG's Consolidated Statements of Earnings. Gross margin below is computed as (NET SALES - Cost of products sold) / NET SALES, from the income statement rows quoted in section 2, and cross-checked against the "Gross margin" row in PG's MD&A Operating Costs table.

@@L~~F21~~555@@
@@L~~F21~~556@@
@@L~~F22~~569@@
@@L~~F23~~539@@
@@L~~F24~~536@@
@@L~~F25~~534@@
@@L~~F26~~531@@
@@L~~F26~~532@@

| FY | Net sales ($m) | Cost of products sold ($m) | Gross profit (computed) | Gross margin (computed) | PG MD&A "Gross margin" | source lines |
|---|---|---|---|---|---|---|
| FY2021 | 76,118 | 37,108 | 39,010 | 51.2% | 51.2% | F21 960, 961, 556 |
| FY2022 | 80,187 | 42,157 | 38,030 | 47.4% | 47.4% | F22 957, 958, 569 |
| FY2023 | 82,006 | 42,760 | 39,246 | 47.9% | 47.9% | F23 880, 881, 539 |
| FY2024 | 84,039 | 40,848 | 43,191 | 51.4% | 51.4% | F24 875, 876, 536 |
| FY2025 | 84,284 | 41,164 | 43,120 | 51.2% | 51.2% | F25 883, 884, 534 |
| FY2026 | 87,032 | 43,362 | 43,670 | 50.2% | 50.2% | F26 885, 886, 532 |

**Shipping and handling placement: in Cost of products sold.** Search terms used: "shipping", "handling", "freight", "distribution costs", "transportation". Accounting policy (Note 1), every year:
@@L~~F21~~1161@@
@@L~~F26~~1067@@
@@P~~F26~~1064~~The revenue includes shipping and handling costs~~list price to the customer.@@

(Wording change: from the FY2025 10-K the Cost of products sold sentence adds "customs and duties" (F25 line 1065). FY2021 to FY2024 wording matches F21 line 1161.)

Trade promotion is netted against sales:
@@P~~F26~~1065~~Sales are recorded net of trade promotion spending~~at the time of the sale.@@

### 6. Competition and customer language

#### (a) "Colgate" and "Hill" searches

Case-insensitive full-text counts (grep -oi) in every PG annual filing on disk:

| file | "colgate" | "palmolive" | "hill" |
|---|---|---|---|
| PG_10K_FY2021_2021-06-30.txt | 0 | 0 | 0 |
| PG_10K_FY2022_2022-06-30.txt | 0 | 0 | 0 |
| PG_10K_FY2023_2023-06-30.txt | 0 | 0 | 0 |
| PG_10K_FY2024_2024-06-30.txt | 0 | 0 | 0 |
| PG_10K_FY2025_2025-06-30.txt | 0 | 0 | 0 |
| PG_10K_FY2026_2026-06-30.txt | 0 | 0 | 0 |

No PG 10-K on disk names Colgate, Colgate-Palmolive, Palmolive or Hill's. There are therefore no sentences to quote, and zero "Hill" hits to classify (no Hill's pet brand hits, no unrelated-word hits). PG does not name any competitor company in the competition language found. The general competition sentences in the newest filing:
@@L~~F26~~215@@
@@L~~F26~~264@@
@@L~~F26~~265@@
@@L~~F26~~418@@
@@P~~F26~~402~~(7) the ability to compete~~trade terms for products;@@

#### (b) Private label, store brands, value brands (newest filing)
Search terms: "private label", "private-label", "store brand", "own label", "retailer brand", "value brand", "private brand". Hits: lines 215, 267, 418 (quoted in full at 215 and 418 above). Remaining sentence:
@@P~~F26~~267~~Our business could also be negatively impacted~~significant business disruption.@@
"store brand", "own label", "retailer brand", "value brand", "private brand": 0 hits each. PG uses "value-tier products":
@@P~~F26~~418~~Additionally, many of the product segments~~value-tier products).@@

#### (c) Customer concentration, each year (Item 1 "Key Customers" and Note 2)
@@L~~F21~~208@@
@@L~~F21~~1239@@
@@L~~F22~~206@@
@@L~~F22~~1231@@
@@L~~F23~~204@@
@@L~~F23~~1152@@
@@L~~F24~~213@@
@@L~~F24~~1132@@
@@L~~F25~~207@@
@@L~~F25~~1139@@
@@L~~F26~~212@@
@@L~~F26~~1144@@

| FY | Walmart Inc. and affiliates, % of net sales | top ten customers, % of net sales | source line (10-K first reporting the year) |
|---|---|---|---|
| FY2021 | approximately 15% | approximately 39% | F21 208, 1239 |
| FY2022 | approximately 15% | approximately 39% | F22 206, 1231 |
| FY2023 | approximately 15% | 40% | F23 204, 1152 |
| FY2024 | approximately 16% | 42% | F24 213, 1132 |
| FY2025 | approximately 16% | 43% | F25 207, 1139 |
| FY2026 | approximately 16% | approximately 43% | F26 212, 1144 |

Note: the FY2024 10-K reports FY2024 Walmart at approximately 16% and FY2023 and FY2022 at 15%; later 10-Ks do not change the earlier years' figures.

#### (d) Pricing, elasticity, trade-down and promotion language, newest fiscal year (FY2026 10-K)
Search terms: "elastic", "trade-down"/"trade down", "promotion", "trade spend", "merchandising", "price increase", "pricing action", "lower pricing", "value", "rollback", "price investment". "elastic", "trade-down", "rollback", "price investment" and "trade spend" have 0 hits in the FY2026 10-K. No interim filing exists (see Documents used).

@@L~~F26~~528@@
@@P~~F26~~549~~40 basis points of increase~~higher pricing.@@
@@P~~F26~~476~~Consumers are changing how they perceive value~~shopping behavior.@@
@@P~~F26~~520~~offset portions of the cost impacts~~product consumption.@@
@@P~~F26~~520~~If we are unable to manage cost impacts~~cash flows.@@
@@P~~F26~~524~~The primary factors driving year-over-year changes in net sales~~sales outside the U.S.@@
@@L~~F26~~635@@
@@P~~F26~~213~~When prices for these items change~~to our customers.@@
@@P~~F26~~263~~Therefore, our business results depend~~market share.@@
@@P~~F26~~696~~Trade promotions, consisting primarily of~~customers and consumers.@@
@@P~~F26~~473~~Our objective is to drive productivity improvements~~capital spending.@@

Health Care and Beauty pricing sentences (FY2026) are inside the segment sentences quoted in section 1 (F26 lines 589 and 610) and the Oral Care bullet (F26 line 611).

### Summary row

| FY window used | organic volume by year | price by year | GAAP operating margin by year | advertising % of sales by year | gross margin by year |
|---|---|---|---|---|---|
| PG total company, FY2021 to FY2026 (fiscal years end June 30; no interim) | FY21 +3 / FY22 +2 / FY23 -3 / FY24 0 / FY25 +1 / FY26 0 [Volume Excluding Acquisitions & Divestitures] | FY21 +1 / FY22 +4 / FY23 +9 / FY24 +4 / FY25 +1 / FY26 +1 [Price; Mix separate: +2 / +1 / +1 / 0 / 0 / 0] | FY21 23.6 / FY22 22.2 / FY23 22.1 / FY24 22.1 / FY25 24.3 / FY26 22.7 [OPERATING INCOME / NET SALES] | FY21 10.8 / FY22 9.9 / FY23 9.8 / FY24 11.4 / FY25 10.9 / FY26 11.7 [Advertising costs] | FY21 51.2 / FY22 47.4 / FY23 47.9 / FY24 51.4 / FY25 51.2 / FY26 50.2 [computed; shipping and handling in COGS] |

Supplementary row, Health Care segment (contains Oral Care):

| FY window used | organic volume by year | price by year | segment margin by year | advertising % of sales by year | gross margin by year |
|---|---|---|---|---|---|
| PG Health Care, FY2021 to FY2026 | FY21 +6 / FY22 +4 / FY23 -1 / FY24 -1 / FY25 -1 / FY26 -2 [Volume Excluding Acquisitions & Divestitures] | FY21 +1 / FY22 +3 / FY23 +5 / FY24 +4 / FY25 +1 / FY26 +2 [Price; Mix separate: +2 / +3 / +4 / +2 / +3 / +1] | FY21 24.1 / FY22 24.2 / FY23 24.6 / FY24 24.9 / FY25 26.2 / FY26 25.4 [segment Earnings Before Income Taxes / segment net sales; segment measure, not GAAP] | nd by segment | FY21 nd / FY22 nd / FY23 56.8 / FY24 57.9 / FY25 58.5 / FY26 58.2 [computed from segment COGS] |

### Gaps, extraction problems and definition differences

**Not disclosed**
- No interim filing: no PG 10-Q after the FY2026 10-K exists on disk or in manifest_list.txt.
- Advertising by segment: not disclosed in any PG 10-K on disk (searched "advertis" in the segment note and MD&A segment discussions; segment discussions only describe marketing spending qualitatively).
- Dollar total of marketing spending (advertising plus consumer promotions, sampling, sales aids): not disclosed; only advertising costs are given in dollars.
- Oral Care organic growth, price and volume as numbers: not disclosed. PG gives Oral Care only in words ("low single digits", etc.) inside the Health Care discussion; the numeric drivers are for the whole Health Care segment (Oral Care plus Personal Health Care).
- Segment operating income: not disclosed. PG's segment profit measures are Earnings/(Loss) Before Income Taxes and Net Earnings/(Loss).
- Segment cost of products sold before FY2023: not disclosed in the FY2021 to FY2024 10-Ks (search "Cost of products sold" in the segment note); first shown in the FY2025 10-K layout.
- Gross profit caption: not on the income statement; computed.
- Any sentence naming Colgate, Colgate-Palmolive or Hill's: none in any PG 10-K on disk (0 hits for "colgate", "palmolive", "hill").
- Organic volume for total company as MD&A text: stated only in FY2021 ("3% increase in organic volume") and FY2022 ("2% increase in organic volume"); for FY2023 to FY2026 the figure used is the Drivers-table column "Volume Excluding Acquisitions & Divestitures".

**Extraction artefacts**
- Table header rows are split across several lines: Drivers header (for example F21 lines 596 to 599), Organic Sales Growth header (F22 lines 822 to 824, F23 lines 773 to 777, F24 747 to 750, F25 745 to 748, F26 742 to 745), segment note header (F21 1243 to 1249, F22 1235 to 1241, F23 1156 to 1162, F24 1135 to 1141). Quoted line by line.
- In the FY2024 10-K segment note, prior-year rows have no leading "|" cell (for example F24 line 1143 "2023 | 15,008 | ..."), unlike FY2021 to FY2023. Numbers are unaffected.
- Page footers break sentences: F23 advertising sentence (lines 1076, 1078 footer, 1079); F26 line 1112 and 1115 (CODM sentence); F23 line 597 to 599 (Beauty paragraph).
- Numbers in the notes carry spaces inside parentheses and after "$" (for example "( 6,397 )", "$ 10.2 billion", "15 %"). Quoted as extracted.
- The filings use the long dash character (U+2014) for zero in tables; kept in quotes, written as 0 in parsed tables.

**Definition of organic growth (PG) and differences from Colgate**
@@L~~F26~~740@@
@@P~~F26~~415~~Organic volume growth reflects~~changes in organic sales.@@
@@P~~F26~~415~~In our presentation of data in tables or other charts~~due to rounding.@@
- PG: organic = net sales growth excluding acquisitions, divestitures and foreign exchange. This matches the exclusion set in the Colgate definition given in the brief (foreign exchange, acquisitions and divestments).
- Components: PG files Volume, Price and Mix as separate columns, and organic growth includes mix. Colgate's components per the brief are "volume" and "net selling price". Where Colgate places mix is not established by this section.
- Volume: PG shows volume both with and excluding acquisitions and divestitures. The excluding figure is the organic analogue. PG's "Other" column (sales mix impact of acquisitions and divestitures, and rounding) and the reconciliation's "Acquisition & Divestiture Impact/Other" include rounding, so components are whole-number approximations that PG says "may not add due to rounding".
- Hyperinflationary markets: no exclusion of hyperinflationary markets (such as Argentina) and no cap on price growth appears in PG's organic definition in any 10-K on disk (search "hyperinflation", "highly inflationary", "Argentina" near "organic"). "Highly inflationary" appears only in the foreign currency translation policy (for example F26 line 1075) and the MD&A foreign exchange paragraph (F26 line 517).
- Fiscal year: PG's fiscal year ends June 30, not December 31, so PG FY2026 covers July 2025 to June 2026 and is offset by six months from a calendar-year filer. No 52/53-week language appears for PG (fiscal years are "ended June 30").
- Share: PG's market share references are dollar share on a constant currency basis (F26 line 415).
@@P~~F26~~415~~All market share references~~relative to all product sales in the category.@@

**Shipping and handling**
- PG includes shipping and handling (cost to distribute products to customers, inbound freight, internal transfer, warehousing, and from FY2025 customs and duties) in Cost of products sold (F26 line 1067; F21 line 1161). Colgate reports shipping and handling in SG&A, so PG's gross margin (50.2% in FY2026) is not on the same basis as Colgate's gross margin.
- Advertising is inside SG&A for PG; trade promotion is netted against net sales (F26 line 1065).
"""
