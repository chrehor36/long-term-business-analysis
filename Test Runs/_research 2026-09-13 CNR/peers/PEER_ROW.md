# PEER ROW: filed per-ton operating metrics, US-listed coal peers (for the CNR run)

Built 2026-09-13. Source: each company's own 10-K / 10-Q primary documents on EDGAR (fetched with
`sources.SEC_UA`; raw HTML cached under `peers\cache\`, git-ignored). Every number below is transcribed
exactly as filed unless the cell says **computed**. Computed cells are simple arithmetic on filed
figures (named in the cell) and are marked so; they cast no vote on their own.

This file is research input only. It is not a clearance and carries no entry language.

## 0. Documents used

| Co. | Document | Period | Filed | Accession |
|---|---|---|---|---|
| AMR | 10-K | FY2025 | 2026-02-27 | 0001704715-26-000010 |
| AMR | 10-K | FY2024 | 2025-02-28 | 0001704715-25-000010 |
| AMR | 10-K | FY2023 | 2024-02-26 | 0001704715-24-000028 |
| AMR | 10-K | FY2022 | 2023-02-23 | 0001704715-23-000010 |
| AMR | 10-K | FY2021 | 2022-03-07 | 0001704715-22-000012 |
| AMR | 10-Q | Q2 2026 | 2026-08-07 | 0001704715-26-000031 |
| HCC | 10-K | FY2025 | 2026-02-12 | 0001193125-26-048914 |
| HCC | 10-K | FY2024 | 2025-02-13 | 0001691303-25-000010 |
| HCC | 10-K | FY2023 | 2024-02-14 | 0001691303-24-000008 |
| HCC | 10-K | FY2022 | 2023-02-15 | 0001691303-23-000010 |
| HCC | 10-K | FY2021 | 2022-02-22 | 0001691303-22-000006 |
| HCC | 10-Q | Q2 2026 | 2026-08-05 | 0001193125-26-335324 |
| METC | 10-K/A (Amendment No. 1, full re-filing) | FY2025 | 2026-07-24 | 0001104659-26-086668 |
| METC | 10-K (original) | FY2025 | 2026-02-26 | 0001104659-26-020479 |
| METC | 10-K | FY2024 | 2025-03-17 | 0001558370-25-003144 |
| METC | 10-K | FY2023 | 2024-03-14 | 0001558370-24-003256 |
| METC | 10-K | FY2022 | 2023-03-14 | 0001558370-23-003736 |
| METC | 10-K | FY2021 | 2022-04-01 | 0001558370-22-004987 |
| METC | 10-Q | Q2 2026 | 2026-08-05 | 0001104659-26-090902 |
| BTU | 10-K | FY2025 | 2026-02-19 | 0001064728-26-000006 |
| BTU | 10-K | FY2024 | 2025-02-20 | 0001064728-25-000018 |
| BTU | 10-K | FY2023 | 2024-02-23 | 0001064728-24-000021 |
| BTU | 10-K | FY2022 | 2023-02-24 | 0001064728-23-000013 |
| BTU | 10-K | FY2021 | 2022-02-18 | 0001064728-22-000008 |
| BTU | 10-Q | Q2 2026 | 2026-08-06 | 0001064728-26-000050 |
| ARLP | 10-K | FY2025 | 2026-02-26 | 0001104659-26-020468 |
| ARLP | 10-K | FY2024 | 2025-02-27 | 0001558370-25-001805 |
| ARLP | 10-K | FY2023 | 2024-02-23 | 0001558370-24-001616 |
| ARLP | 10-K | FY2022 | 2023-02-24 | 0001558370-23-002034 |
| ARLP | 10-K | FY2021 | 2022-02-25 | 0001558370-22-002091 |
| ARLP | 10-Q | Q2 2026 | 2026-08-06 | 0001104659-26-092001 |
| CRN (Coronado, see 3.4) | 10-K | FY2025 | 2026-03-03 | 0001562762-26-000024 |
| CRN | 10-K | FY2024 | 2025-02-19 | 0001562762-25-000021 |
| CRN | 10-K | FY2023 | 2024-02-20 | 0001562762-24-000028 |
| CRN | 10-K | FY2022 | 2023-02-21 | 0001562762-23-000044 |
| CRN | 10-Q | Q2 2026 | 2026-08-10 | 0001562762-26-000094 |

Rule applied: each year is taken from the MOST RECENT 10-K that carries it. Older vintages were read
to check for restatement; disagreements are listed in section 3.2.

Amendments checked and found not to touch the per-ton figures: METC FY2025 10-K/A (Brook Mine
rare-earth disclosure, per SEC comments; the per-ton tables are identical to the original 10-K);
METC FY2021 10-K/A (0001104659-23-002700, property disclosure; "does not update or otherwise affect
the financial statements"); METC FY2022 10-K/A (0001104659-23-043112, Item 15(b) only); HCC FY2022
10-K/A (0001193125-23-148198, revised Exhibits 96.1/96.2 technical report summaries); ARLP FY2021
10-K/A (0001558370-22-014018, property disclosure per SEC staff review).

---

## 1. METALLURGICAL COAL

### 1.1 Measure definitions (as filed)

- **AMR** (short tons). Price: "Non-GAAP Coal sales realization per ton" = non-GAAP coal revenues
  (coal revenues less freight and handling fulfillment revenues) / tons sold. Cost: "Non-GAAP Cost of
  coal sales per ton", non-GAAP; FY2025 10-K: "We use non-GAAP cost of coal sales to adjust cost of coal
  sales to remove freight and handling costs, depreciation, depletion and amortization - production
  (excluding the depreciation, depletion and amortization related to selling, general and administrative
  functions), accretion on asset retirement obligations, amortization of acquired intangibles, and idled
  and closed mine costs." The FY2021-FY2024 10-Ks carry the same sentence with "amortization of acquired intangibles, net". Margin: filed
  "Non-GAAP Coal margin per ton". Segments: Met and All Other (former CAPP-Thermal) through 2023; from
  2024 one reportable segment (Met), managed on a consolidated basis, which still includes by-product
  thermal (7% of 2025 coal sales volume).
- **HCC** (METRIC tons). Price: "Average net selling price per metric ton" = coal net sales revenue /
  metric tons sold, "net of demurrage and quality specification adjustments"; freight borne by HCC
  reduces it. Cost: "Cash cost of sales per metric ton", non-GAAP, "includes items such as freight,
  royalties, manpower, fuel and other similar production and sales cost items", on a basis of selling
  "free-on-board at the Port of Mobile in Alabama"; reconciliation removes ARO accretion/valuation and
  stock compensation from GAAP cost of sales; FY2025 note: "Cash cost of sales includes transportation
  and royalties and excludes depreciation and depletion". Same definition FY2021-FY2025. One segment
  (Mining). 1 metric ton = 1.102311 short tons (as filed).
- **METC** (tons; unit not defined in the filing, see limits). Price: "Non-GAAP revenue per ton sold
  (FOB mine)" = coal sales revenue less transportation revenues and demurrage / tons sold (FY2021-FY2022
  wording: less transportation costs). Cost: "Non-GAAP cash cost per ton sold (FOB mine)" = cash cost of
  sales less transportation, idle and other costs / tons sold. Definition drift: FY2021 excluded
  transportation only; FY2022 added idle mine costs; FY2024 10-K also excluded "alternative mineral
  development costs"; FY2025 10-K/A: "transportation, idle, and other costs". Figures are whole dollars.
  Also filed (10-K/A FY2025): GAAP "Total revenue per ton sold (GAAP basis)" 140 (2025) / 167 (2024) and
  "Total cost of sales per ton sold (GAAP basis)" 118 (2025) / 132 (2024).
- **BTU** (short tons: "the term “ton” refers to short or net tons, equal to 2,000 pounds").
  "Revenue per Ton" = segment revenue / segment tons sold. "Costs per Ton" = Revenue per Ton less Adjusted
  EBITDA Margin per Ton; footnote: "Includes revenue-based production taxes and royalties; excludes
  depreciation, depletion and amortization; asset retirement obligation expenses; selling and
  administrative expenses; restructuring charges; asset impairment; amortization of take-or-pay
  contract-based intangibles; insurance recoveries; and certain other costs related to post-mining
  activities." ("insurance recoveries" added from the FY2024 10-K on). Labelled "an operating/statistical
  measure not recognized in accordance with U.S. GAAP". Margin: filed "Adjusted EBITDA Margin per Ton".
- **Coronado (CRN)**: see 3.4.

### 1.2 Table

| company | segment | year | tons sold (unit) | price per ton (measure) | cost per ton (measure) | margin per ton | source doc + accession |
|---|---|---|---|---|---|---|---|
| AMR | Met | 2021 | 15,569 thousand short tons | 115.18 (Non-GAAP coal sales realization) | 77.71 (Non-GAAP cost of coal sales) | 37.47 (filed Non-GAAP coal margin) | 10-K FY2022, 0001704715-23-000010 |
| AMR | Met | 2022 | 15,478 | 225.45 | 108.22 | 117.22 (filed) | 10-K FY2023, 0001704715-24-000028 |
| AMR | Met | 2023 | 16,543 | 179.40 | 111.67 | 67.73 (filed) | 10-K FY2024, 0001704715-25-000010 |
| AMR | Met (= consolidated from 2024) | 2024 | 17,127 | 142.66 | 112.01 | 30.64 (filed) | 10-K FY2025, 0001704715-26-000010 |
| AMR | Met (= consolidated) | 2025 | 15,280 | 117.08 | 102.23 | 14.85 (filed) | 10-K FY2025, 0001704715-26-000010 |
| AMR | consolidated | Q2 2026 (3 mo) | 3,549 | 118.71 | 103.07 | 15.64 (filed) | 10-Q Q2 2026, 0001704715-26-000031 |
| AMR | consolidated | 6M 2026 | 7,145 | 121.57 | 105.54 | 16.03 (filed) | 10-Q Q2 2026, 0001704715-26-000031 |
| AMR | consolidated | 6M 2025 (comparative) | 7,644 | 119.03 | 105.12 | 13.91 (filed) | 10-Q Q2 2026, 0001704715-26-000031 |
| HCC | Mining | 2021 | 5,699 thousand METRIC tons | 180.43 (Average net selling price per metric ton) | 96.43 (Cash cost of sales per metric ton) | 84.00 **computed** (price less cash cost) | 10-K FY2023, 0001691303-24-000008 |
| HCC | Mining | 2022 | 5,099 | 334.89 | 138.35 | 196.54 **computed** | 10-K FY2024, 0001691303-25-000010 |
| HCC | Mining | 2023 | 6,820 | 241.64 | 132.60 | 109.04 **computed** | 10-K FY2025, 0001193125-26-048914 |
| HCC | Mining | 2024 | 7,235 | 207.32 | 138.10 | 69.22 **computed** | 10-K FY2025, 0001193125-26-048914 |
| HCC | Mining | 2025 | 8,735 | 146.20 | 111.66 | 34.54 **computed** | 10-K FY2025, 0001193125-26-048914 |
| HCC | Mining | Q2 2026 (3 mo) | 3,315 | 151.91 | 101.99 | 49.92 **computed** | 10-Q Q2 2026, 0001193125-26-335324 |
| HCC | Mining | 6M 2026 | 6,038 | 157.68 | 103.81 | 53.87 **computed** | 10-Q Q2 2026, 0001193125-26-335324 |
| HCC | Mining | 6M 2025 (comparative) | 3,983 | 146.48 | 117.63 | 28.85 **computed** | 10-Q Q2 2026, 0001193125-26-335324 |
| METC | total (produced + purchased) | 2021 | 2,286 thousand tons | 109 (Revenue per ton sold (FOB mine)) | 70 (Cash cost per ton sold) | 39 **computed** | 10-K FY2022, 0001558370-23-003736 |
| METC | total | 2022 | 2,450 | 207 | 108 | 99 **computed** | 10-K FY2023, 0001558370-24-003256 |
| METC | total | 2023 | 3,455 | 170 (Non-GAAP revenue per ton sold (FOB mine)) | 110 (Non-GAAP cash cost per ton sold (FOB mine)) | 60 **computed** | 10-K FY2024, 0001558370-25-003144 |
| METC | Metallurgical Coal segment | 2024 | 3,989 | 140 | 105 | 35 **computed** | 10-K/A FY2025, 0001104659-26-086668 |
| METC | Metallurgical Coal segment | 2025 | 3,834 | 120 | 98 | 22 **computed** | 10-K/A FY2025, 0001104659-26-086668 |
| METC | Metallurgical Coal segment | Q2 2026 (3 mo) | 1,056 | 116 | 99 | 17 **computed** | 10-Q Q2 2026, 0001104659-26-090902 |
| METC | Metallurgical Coal segment | 6M 2026 | 1,948 | 115 | 98 | 17 **computed** | 10-Q Q2 2026, 0001104659-26-090902 |
| METC | Metallurgical Coal segment | 6M 2025 (comparative) | 2,024 | 123 | 101 | 22 **computed** | 10-Q Q2 2026, 0001104659-26-090902 |
| BTU | Seaborne Metallurgical | 2021 | 5.5 million short tons | 131.83 (Revenues per Ton) | 99.55 (Costs per Ton) | 32.28 (filed Adjusted EBITDA Margin per Ton) | 10-K FY2022, 0001064728-23-000013 |
| BTU | Seaborne Metallurgical | 2022 | 6.6 | 243.78 | 125.92 | 117.86 (filed) | 10-K FY2023, 0001064728-24-000021 |
| BTU | Seaborne Metallurgical | 2023 | 6.9 | 188.66 | 125.18 | 63.48 (filed) | 10-K FY2024, 0001064728-25-000018 |
| BTU | Seaborne Metallurgical | 2024 | 7.3 | 144.97 | 122.77 | 22.20 (filed; excludes $80.8m Shoal Creek insurance recovery) | 10-K FY2025, 0001064728-26-000006 |
| BTU | Seaborne Metallurgical | 2025 | 8.6 | 120.88 | 114.31 | 6.57 (filed) | 10-K FY2025, 0001064728-26-000006 |
| BTU | Seaborne Metallurgical | Q2 2026 (3 mo) | 2.5 | 148.04 | 155.08 | (7.04) (filed) | 10-Q Q2 2026, 0001064728-26-000050 |
| BTU | Seaborne Metallurgical | 6M 2026 | 4.5 | 143.57 | 148.96 | (5.39) (filed) | 10-Q Q2 2026, 0001064728-26-000050 |
| BTU | Seaborne Metallurgical | 6M 2025 (comparative) | 4.0 | 119.40 | 118.39 | 1.01 (filed) | 10-Q Q2 2026, 0001064728-26-000050 |

AMR met-quality detail for older years is not segment-split below "Met"; AMR's former thermal segment is
in table 2.3.

---

## 2. THERMAL COAL

### 2.1 Powder River Basin

| company | segment | year | tons sold (unit) | price per ton (measure) | cost per ton (measure) | margin per ton | source doc + accession |
|---|---|---|---|---|---|---|---|
| BTU | Powder River Basin | 2021 | 88.4 million short tons | 10.99 (Revenues per Ton) | 9.46 (Costs per Ton) | 1.53 (filed Adjusted EBITDA Margin per Ton) | 10-K FY2022, 0001064728-23-000013 |
| BTU | Powder River Basin | 2022 | 82.6 | 12.89 | 12.06 | 0.83 (filed) | 10-K FY2023, 0001064728-24-000021 |
| BTU | Powder River Basin | 2023 | 87.2 | 13.74 | 11.98 | 1.76 (filed) | 10-K FY2024, 0001064728-25-000018 |
| BTU | Powder River Basin | 2024 | 79.6 | 13.81 | 12.07 | 1.74 (filed) | 10-K FY2025, 0001064728-26-000006 |
| BTU | Powder River Basin | 2025 | 84.5 | 13.64 | 11.56 | 2.08 (filed) | 10-K FY2025, 0001064728-26-000006 |
| BTU | Powder River Basin | Q2 2026 (3 mo) | 16.4 | 13.63 | 14.06 | (0.43) (filed) | 10-Q Q2 2026, 0001064728-26-000050 |
| BTU | Powder River Basin | 6M 2026 | 37.6 | 13.64 | 13.20 | 0.44 (filed) | 10-Q Q2 2026, 0001064728-26-000050 |
| BTU | Powder River Basin | 6M 2025 (comparative) | 39.6 | 13.92 | 11.92 | 2.00 (filed) | 10-Q Q2 2026, 0001064728-26-000050 |

### 2.2 Illinois Basin / Northern & Central Appalachia (eastern US thermal)

ARLP measure definitions (FY2025 10-K): "We calculate coal sales per ton by dividing coal sales by coal
sales volumes." Cost: "Segment Adjusted EBITDA Expense (a non-GAAP financial measure) as the sum of
operating expenses, coal purchases and other expenses as adjusted to remove certain items from operating
expenses that we characterize as unrepresentative of our ongoing operations. Transportation expenses are
excluded". Per-ton = divided by tons sold. **ARLP's FY2024 and FY2025 10-Ks do not print segment per-ton
figures in dollars** (segment totals only, plus percentage changes); segment per-ton cells for those
years are therefore **computed** from filed totals (coal sales, Segment Adjusted EBITDA Expense, tons
sold, all in thousands). Method check: the same computation reproduces every segment per-ton dollar figure
the older 10-Ks do state (IB expense 27.55 / 33.43 / 34.84 for 2021-2023; Appalachia expense 34.42 /
40.42 / 53.15; IB price 55.21 for 2023 and 56.44 for 2024). ARLP tons: unit not defined in the MD&A; the
filing prices its reserves "per short ton". Computed margin = price less expense per ton; it ignores
segment "Other revenues".

| company | segment | year | tons sold (unit) | price per ton (measure) | cost per ton (measure) | margin per ton | source doc + accession |
|---|---|---|---|---|---|---|---|
| ARLP | Illinois Basin Coal Operations | 2021 | 22,264 thousand tons | 39.25 **computed** (873,930 / 22,264 coal sales per ton) | 27.55 (filed Segment Adjusted EBITDA Expense per ton) | 11.71 **computed** | 10-K FY2022, 0001558370-23-002034 (per-ton expense stated in 10-K FY2021, 0001558370-22-002091) |
| ARLP | Illinois Basin | 2022 | 24,110 | 50.60 **computed** | 33.43 (filed) | 17.17 **computed** | 10-K FY2023, 0001558370-24-001616 |
| ARLP | Illinois Basin | 2023 | 24,724 | 55.21 (filed "coal sales price realizations ... per ton sold") | 34.84 (filed) | 20.37 **computed** | 10-K FY2024, 0001558370-25-001805 (totals); 10-K FY2023, 0001558370-24-001616 (34.84) |
| ARLP | Illinois Basin | 2024 | 24,787 | 56.44 (filed) | 37.81 **computed** (937,083 / 24,787) | 18.64 **computed** | 10-K FY2025, 0001104659-26-020468; 56.44 in 10-K FY2024, 0001558370-25-001805 |
| ARLP | Illinois Basin | 2025 | 25,769 | 52.09 **computed** (1,342,334 / 25,769) | 34.71 **computed** (894,521 / 25,769) | 17.38 **computed** | 10-K FY2025, 0001104659-26-020468 |
| ARLP | Illinois Basin | Q2 2026 (3 mo) | 6,367 | 51.87 **computed** | 35.99 **computed** | 15.88 **computed** | 10-Q Q2 2026, 0001104659-26-092001 |
| ARLP | Illinois Basin | 6M 2026 | 12,435 | 51.47 **computed** | 35.61 **computed** | 15.86 **computed** | 10-Q Q2 2026, 0001104659-26-092001 |
| ARLP | Illinois Basin | 6M 2025 (comparative) | 12,707 | 53.28 **computed** | 34.72 **computed** | 18.57 **computed** | 10-Q Q2 2026, 0001104659-26-092001 |
| ARLP | Appalachia Coal Operations | 2021 | 10,004 thousand tons | 51.28 **computed** | 34.42 (filed) | 16.86 **computed** | 10-K FY2022, 0001558370-23-002034 |
| ARLP | Appalachia | 2022 | 11,479 | 76.86 **computed** | 40.42 (filed) | 36.44 **computed** | 10-K FY2023, 0001558370-24-001616 |
| ARLP | Appalachia | 2023 | 9,718 | 86.98 **computed** | 53.15 (filed) | 33.84 **computed** | 10-K FY2024, 0001558370-25-001805; 53.15 in 10-K FY2023 |
| ARLP | Appalachia | 2024 | 8,532 | 83.53 **computed** | 64.67 **computed** | 18.87 **computed** | 10-K FY2025, 0001104659-26-020468 |
| ARLP | Appalachia | 2025 | 7,198 | 81.99 **computed** | 63.82 **computed** | 18.18 **computed** | 10-K FY2025, 0001104659-26-020468 |
| ARLP | Appalachia | Q2 2026 (3 mo) | 2,191 | 63.57 **computed** | 46.22 **computed** | 17.34 **computed** | 10-Q Q2 2026, 0001104659-26-092001 |
| ARLP | Appalachia | 6M 2026 | 3,983 | 68.49 **computed** | 53.41 **computed** | 15.08 **computed** | 10-Q Q2 2026, 0001104659-26-092001 |
| ARLP | Appalachia | 6M 2025 (comparative) | 3,446 | 80.36 **computed** | 67.73 **computed** | 12.63 **computed** | 10-Q Q2 2026, 0001104659-26-092001 |
| ARLP | Coal operations, total | 2021 | 32,268 | 42.98 (filed) | 30.24 (filed, 10-K FY2021) / 29.73 (filed, recast, 10-K FY2023) | 12.74 **computed** on 30.24 | 10-K FY2021, 0001558370-22-002091 |
| ARLP | Coal operations, total | 2022 | 35,589 | 59.07 (filed) | 36.73 (filed, 10-K FY2022) / 35.91 (filed, recast, 10-K FY2023) | 23.16 **computed** on 35.91 | 10-K FY2023, 0001558370-24-001616 |
| ARLP | Coal operations, total | 2023 | 34,442 | 64.17 (filed) | 40.38 (filed) | 23.79 **computed** | 10-K FY2023, 0001558370-24-001616; 40.38 repeated in 10-K FY2024 |
| ARLP | Coal operations, total | 2024 | 33,319 | 63.38 **computed** (2,111,803 / 33,319) | 45.07 (filed) | 18.31 **computed** | 10-K FY2025, 0001104659-26-020468 |
| ARLP | Coal operations, total | 2025 | 32,967 | 58.62 **computed** (1,932,515 / 32,967) | 41.29 (filed) | 17.33 **computed** | 10-K FY2025, 0001104659-26-020468 |
| ARLP | Coal operations, total | Q2 2026 (3 mo) | 8,558 | 54.87 **computed** | 38.68 (filed) | 16.19 **computed** | 10-Q Q2 2026, 0001104659-26-092001 |
| ARLP | Coal operations, total | 6M 2026 | 16,418 | 55.60 **computed** | 39.99 (filed) | 15.61 **computed** | 10-Q Q2 2026, 0001104659-26-092001 |
| BTU | Other U.S. Thermal | 2021 | 16.9 million short tons | 40.75 (Revenues per Ton) | 31.04 (Costs per Ton) | 9.71 (filed Adjusted EBITDA Margin per Ton) | 10-K FY2022, 0001064728-23-000013 |
| BTU | Other U.S. Thermal | 2022 | 18.4 | 51.82 | 38.63 | 13.19 (filed) | 10-K FY2023, 0001064728-24-000021 |
| BTU | Other U.S. Thermal | 2023 | 16.2 | 54.77 | 41.98 | 12.79 (filed) | 10-K FY2024, 0001064728-25-000018 |
| BTU | Other U.S. Thermal | 2024 | 14.6 | 56.38 | 46.04 | 10.34 (filed) | 10-K FY2025, 0001064728-26-000006 |
| BTU | Other U.S. Thermal | 2025 | 13.4 | 52.82 | 47.49 | 5.33 (filed) | 10-K FY2025, 0001064728-26-000006 |
| BTU | Other U.S. Thermal | Q2 2026 (3 mo) | 3.0 | 55.26 | 46.13 | 9.13 (filed) | 10-Q Q2 2026, 0001064728-26-000050 |
| BTU | Other U.S. Thermal | 6M 2026 | 6.3 | 55.54 | 45.20 | 10.34 (filed) | 10-Q Q2 2026, 0001064728-26-000050 |
| BTU | Other U.S. Thermal | 6M 2025 (comparative) | 6.0 | 54.20 | 46.43 | 7.77 (filed) | 10-Q Q2 2026, 0001064728-26-000050 |
| AMR | All Other (CAPP-Thermal) | 2021 | 1,270 thousand short tons | 61.78 (Non-GAAP coal sales realization) | 47.55 (Non-GAAP cost of coal sales) | 14.23 (filed Non-GAAP coal margin) | 10-K FY2022, 0001704715-23-000010 |
| AMR | All Other (CAPP-Thermal) | 2022 | 900 | 82.72 | 59.19 | 23.54 (filed) | 10-K FY2023, 0001704715-24-000028 |
| AMR | All Other (CAPP-Thermal) | 2023 | 529 | 94.06 | 80.84 | 13.22 (filed) | 10-K FY2023, 0001704715-24-000028 |
| AMR | (none) | 2024-2026 | not reported | no separate thermal per-ton figure; thermal folded into the single Met segment | | | 10-K FY2025 Note 22 |

### 2.3 Seaborne thermal

| company | segment | year | tons sold (unit) | price per ton (measure) | cost per ton (measure) | margin per ton | source doc + accession |
|---|---|---|---|---|---|---|---|
| BTU | Seaborne Thermal | 2021 | 17.3 million short tons | 54.09 (Revenues per Ton) | 33.64 (Costs per Ton) | 20.45 (filed Adjusted EBITDA Margin per Ton) | 10-K FY2022, 0001064728-23-000013 |
| BTU | Seaborne Thermal | 2022 | 15.6 | 86.07 | 44.65 | 41.42 (filed) | 10-K FY2023, 0001064728-24-000021 |
| BTU | Seaborne Thermal | 2023 | 15.5 | 85.94 | 48.66 | 37.28 (filed) | 10-K FY2024, 0001064728-25-000018 |
| BTU | Seaborne Thermal | 2024 | 16.4 | 73.88 | 47.71 | 26.17 (filed) | 10-K FY2025, 0001064728-26-000006 |
| BTU | Seaborne Thermal | 2025 | 15.4 | 58.97 | 44.55 | 14.42 (filed) | 10-K FY2025, 0001064728-26-000006 |
| BTU | Seaborne Thermal | Q2 2026 (3 mo) | 3.0 | 74.85 | 57.93 | 16.92 (filed) | 10-Q Q2 2026, 0001064728-26-000050 |
| BTU | Seaborne Thermal | 6M 2026 | 6.0 | 70.81 | 54.17 | 16.64 (filed) | 10-Q Q2 2026, 0001064728-26-000050 |
| BTU | Seaborne Thermal | 6M 2025 (comparative) | 8.0 | 57.25 | 42.61 | 14.64 (filed) | 10-Q Q2 2026, 0001064728-26-000050 |

No other listed peer in the brief reports a seaborne thermal segment.

---

## 3. NOTES, RESTATEMENTS, CROSS-CHECKS, AND THE AUSTRALIAN COMPARATOR

### 3.1 Cross-checks against the filed statements (one per company)
- AMR FY2025: Non-GAAP coal revenues 1,788,914 / tons 15,280 = 117.08, matching the filed realization;
  the reconciliation starts from Coal revenues 2,122,605, the same figure as the Met segment note (Note 22).
- HCC FY2025: Cash cost of sales 975,384 / 8,735 = 111.66, matching; reconciles to GAAP Cost of sales 982,401.
- METC FY2025: Non-GAAP revenue (FOB mine) 461,548 / 3,834 = 120.4, filed as 120; reconciles to Revenue 536,618.
- BTU FY2025: Total Segment Costs 3,312.2m reconciles to operating costs and expenses 3,334.9m.
  Per-ton figures are computed by BTU from unrounded tons, so 686.3 / 15.4 = 44.56 against filed 44.55.
- ARLP: the computed segment method reproduces every stated segment per-ton dollar figure (see 2.2).

### 3.2 Two vintages disagree (restatement / recast / definition drift)
- **AMR 2021 All Other**: realization 61.76 (10-K FY2021) vs 61.78 (10-K FY2022); Non-GAAP margin 14.21
  vs 14.23; GAAP coal margin (12.22) vs (10.66). Met 2021 unchanged.
- **AMR 2023 Met GAAP coal margin per ton**: 57.69 (10-K FY2023) vs 57.59 (10-K FY2024). Non-GAAP
  figures unchanged.
- **METC 2023 cash cost per ton**: 111 total (10-K FY2023) vs 110 (10-K FY2024, which newly excludes
  $3,849k "Alternative mineral development costs"). Definition change, not an error correction.
- **METC 2024 GAAP cost of sales**: 533,293 / 134 per ton (10-K FY2024) vs 528,538 / 132 per ton (10-K
  FY2025 and 10-K/A). The non-GAAP 105 cash cost is the same in both.
- **ARLP coal-operations Segment Adjusted EBITDA Expense per ton**: 2022 = 36.73 (10-K FY2022) vs 35.91
  (10-K FY2023); 2021 = 30.24 (10-K FY2021 and FY2022) vs 29.73 (10-K FY2023). The FY2023 10-K marks its
  2022 comparatives "Recast for the JC Resources Acquisition" (an oil & gas royalty acquisition); I did not
  find a sentence explaining why the coal-operations per-ton figure moved. Segment IB and Appalachia
  totals for 2021-2022 are identical across the vintages.
- **BTU**: no disagreement found; 2021-2024 figures identical across the two vintages carrying each year.
  In the FY2024 and FY2025 10-Ks, margin/cost per ton exclude insurance recoveries (2024 Seaborne Met:
  $80.8m Shoal Creek business-interruption recovery excluded); the Q2 2026 10-Q footnote does not carry
  the "insurance recoveries" wording.
- **HCC**: no disagreement found across five vintages. 2021 volumes were affected by the UMWA strike
  (FY2021 10-K: "Due to the strike, we idled Mine No. 4 and scaled back operations at Mine No. 7").
- **Coronado**: the Q2 2026 10-Q switched from "Mining costs per Mt sold" to "Mining cash cost per Mt
  produced", a different denominator; not comparable with the annual series.

### 3.3 Segment composition (from the filings' own mine tables)
- BTU "Other U.S. Thermal" is not pure Illinois Basin: Bear Run, Wild Boar, Francisco Underground
  (Indiana), Gateway North (Illinois), plus El Segundo/Lee Ranch (New Mexico) and Twentymile (Colorado).
- BTU "Seaborne Metallurgical" mixes Australian mines (Metropolitan, Coppabella, Moorvale, Centurion)
  with Shoal Creek (Alabama) (mine table, 10-K FY2024).
- BTU "Seaborne Thermal" = Wilpinjong, Wambo Open-Cut (50% share), Wambo Underground (NSW).
- ARLP "Appalachia" covers the Tunnel Ridge, Mettiki and MC Mining operations (names as used in the
  FY2025 10-K MD&A). The mine-to-state and NAPP/CAPP mapping was not taken from the filing here and is
  not asserted.

### 3.4 Australian met coal comparator: Coronado Global Resources (a 10-K filer, CIK 0001770561)
Coronado is incorporated in the US and files 10-K/10-Q with the SEC, so its figures were trivially
available and are recorded here as a comparator outside the brief's peer list. Units: "All production and
sales volumes contained in this Annual Report on Form 10-K are expressed in metric tons". Measures as
filed: "Average realized price per Mt sold" (coal revenues / sales volume), "Average realized Met price
per Mt sold" (Met coal revenues / Met sales volume), "Mining costs per Mt sold" ("mining costs divided by
sales volumes (excluding non-produced coal)"; the FY2025 reconciliation removes other royalties, the
Stanwell rebate, freight expenses and other non-mining costs from operating costs, which are themselves
total costs less SG&A and DD&A), and "Operating costs per Mt sold". The **computed** margin uses operating
costs per Mt sold (the fuller cash measure, including royalties and freight) against the all-coal
realized price. It is not like-for-like with any US peer's margin.

| segment | year | sales volume (MMt, metric) | avg realized price per Mt (all coal) | avg realized Met price per Mt | mining costs per Mt sold | operating costs per Mt sold | margin **computed** (price less operating cost) | source |
|---|---|---|---|---|---|---|---|---|
| Australia | 2021 | 11.3 | 113.1 | 143.1 | 67.6 | 98.2 | 14.9 | 10-K FY2022, 0001562762-23-000044 |
| Australia | 2022 | 10.0 | 208.9 | 303.1 | 89.5 | 158.3 | 50.6 | 10-K FY2023, 0001562762-24-000028 |
| Australia | 2023 | 9.9 | 167.0 | 230.2 | 108.5 | 170.5 | (3.5) | 10-K FY2024, 0001562762-25-000021 |
| Australia | 2024 | 10.2 | 153.1 | 203.9 | 104.6 | 156.3 | (3.2) | 10-K FY2025, 0001562762-26-000024 |
| Australia | 2025 | 10.2 | 112.9 | 149.3 | 91.0 | 131.3 | (18.4) | 10-K FY2025, 0001562762-26-000024 |
| Australia | 6M 2026 | 4.5 | 126.4 | 167.7 | n/a (2026 measure is "Mining cash cost per Mt produced": 117.0) | 153.3 | (26.9) | 10-Q Q2 2026, 0001562762-26-000094 |
| United States | 2021 | 6.4 | 128.6 | 131.2 | 62.3 | 81.3 | 47.3 | 10-K FY2022, 0001562762-23-000044 |
| United States | 2022 | 6.4 | 225.2 | 226.5 | 86.5 | 115.0 | 110.2 | 10-K FY2023, 0001562762-24-000028 |
| United States | 2023 | 6.0 | 198.4 | 196.9 | 106.0 | 132.9 | 65.5 | 10-K FY2024, 0001562762-25-000021 |
| United States | 2024 | 5.6 | 156.7 | 160.1 | 112.6 | 136.5 | 20.2 | 10-K FY2025, 0001562762-26-000024 |
| United States | 2025 | 5.3 | 143.4 | 149.2 | 109.9 | 133.7 | 9.7 | 10-K FY2025, 0001562762-26-000024 |
| United States | 6M 2026 | 2.4 | 162.3 | 168.4 | n/a (Mining cash cost per Mt produced: 106.6) | 148.9 | 13.4 | 10-Q Q2 2026, 0001562762-26-000094 |

---

## 4. VERBATIM: OWN COST POSITION, AND COMPETITORS NAMED

All quotes copied from the flattened primary document; the flattener only collapses whitespace.

### AMR (10-K FY2025, 0001704715-26-000010)
- "We operate highly productive, cost-competitive coal mines across the CAPP coal basin."
- "We operate high-quality, cost-competitive coal mines across the CAPP coal basin."
- "Of the approximately 73.1 million tons of met produced in the U.S. in 2024, we produced approximately 14.6 million tons, or 20%."
- "In the export met coal market, we compete with producers from Australia and Canada and with other international producers on many of the same factors as in the U.S. market."
- "We compete for U.S. sales with numerous coal producers in the Appalachian region and the Illinois basin, and in some cases with western coal producers."
- AMR's 10-Ks FY2021-FY2025 name no competitor company (searched: Arch, CONSOL, Core Natural Resources
  in all five vintages; the other peers' names, BHP, Glencore, Anglo, Teck, Coronado, Whitehaven in FY2025).

### HCC (10-K FY2025, 0001193125-26-048914)
- "We are a large-scale, low-cost producer and exporter of premium quality met or steelmaking coal, also known as hard coking coal (“HCC”), operating highly efficient longwall operations in our underground mines based in Alabama, Mine No. 4, Mine No. 7 and Blue Creek."
- "We believe our mines are some of the lowest cost steelmaking coal mines in North America."
- "Even in these early stages of production and sales, Blue Creek has already contributed to lower cash costs, further improving our position in the first-quartile global cost curve."
- "Our highly flexible cost structure provides us with a key competitive advantage relative to our competitors and which we expect should allow us to remain profitable in all coal market conditions."
- "Our major competitors sell into our core business areas of Asia, Europe and South America. We primarily compete with producers of premium steelmaking coal from Australia, Canada, Russia, Mozambique and the United States."
- Competitors by name: none of the searched names (as for AMR) appears as a competitor in the FY2025 10-K. Arch appears only in a stock-performance peer group
  (10-K FY2022, 0001691303-23-000010): "a peer group comprised of Arch Resources, Inc. and Peabody Energy Corp ("Custom Composite Index")". That is a return benchmark, not a statement of competition.

### METC (10-K/A FY2025, 0001104659-26-086668; same wording in the original 10-K)
- "Being a Low-Cost U.S. Producer of Metallurgical Coal . Operationally, we are committed to being a low-cost U.S. producer of metallurgical coal."
- "These characteristics contribute to a production profile that has a cash cost of production that is significantly below most U.S. metallurgical coal producers."
- "U.S. metallurgical coal exports compete with Australian metallurgical coals that are generally produced at a lower cost but are geographically disadvantaged to the Atlantic Basin."
- "Our principal domestic coal competitors include Alpha Metallurgical Resources, Inc., Blackhawk Mining, LLC, Coronado Global Resources Inc., Arch Resources, Inc. (now a subsidiary of Core Natural Resources), Peabody Energy Corporation, and Warrior Met Coal, Inc."
- Earlier vintages (10-K FY2023, 0001558370-24-003256): "Our principal domestic competitors include Alpha Metallurgical Resources, Inc., Blackhawk Mining, LLC, Coronado Global Resources Inc., Arch Resources, Inc., Peabody Energy Corporation and Warrior Met Coal, Inc."
- Flag: the 10-K/A also says "Ramaco Coal bought the property from Core Natural Resources in 2012 and started production on the Elk Creek Complex in the fourth quarter of 2016." The seller name looks anachronistic for 2012 (Core Natural Resources is the post-merger name); recorded exactly as filed, not smoothed, not verified further. Separately, METC's "CORE" references in the 10-K/A are Ramaco's own tracking-stock class, not Core Natural Resources.

### BTU (10-K FY2025, 0001064728-26-000006)
- Own cost position: **no sentence found** in which Peabody characterizes its own cost position (searched: low-cost, lowest cost, first quartile, cost position, cost-competitive, competitive cost/advantage). Nearest self-description: "Peabody is a leading producer of metallurgical and thermal coal."
- Thermal: "In addition to its alternative fuel source competitors, Peabody’s principal U.S. direct coal supply competitors (listed alphabetically) are other large coal producers, including Alliance Resource Partners; American Consolidated Natural Resources, Inc.; Core Natural Resources, Inc.; Eagle Summit; Foresight Energy; Hallador Energy; Kiewit; and Navajo Transitional Energy Company LLC, among others."
- Metallurgical: "Major international direct competitors (listed alphabetically) include Anglo American; BHP; Core Natural Resources, Inc.; Foxleigh; Glencore; Jellinbah; KRU; Oak Grove Mine; Stanmore; QCoal; Warrior Met Coal; Whitehaven Coal Limited; and Yancoal Australia Ltd, among others."
- Pre-merger vintage (10-K FY2023, 0001064728-24-000021), thermal: "... including Alliance Resource Partners; American Consolidated Natural Resources, Inc.; Arch Resources, Inc.; CONSOL Energy; Eagle Specialty Materials LLC; Foresight Energy; Hallador Energy; Kiewit; and Navajo Transitional Energy Company LLC, among others." Met: "Major international direct competitors (listed alphabetically) include Anglo American; Arch Resources, Inc.; BHP; Foxleigh; Glencore; Jellinbah; KRU; Stanmore; Teck Resources; Warrior Met Coal; Whitehaven Coal Limited; and Yancoal Australia Ltd, among others."

### ARLP (10-K FY2025, 0001104659-26-020468)
- "continuing to make productivity improvements to remain a low-cost coal producer in each region in which we operate;" (bulleted strategy item; the FY2021 10-K reads "to remain a low-cost producer in each region in which we operate;")
- "We are the second largest coal producer in the eastern United States"
- "Our principal competitors include American Consolidated Natural Resources Inc., Core Natural Resources, Inc., Alpha Metallurgical Resources, Inc., Foresight Energy Resources LLC, and Peabody Energy Corporation."
- Pre-merger (10-K FY2023, 0001558370-24-001616): "Our principal competitors include American Consolidated Natural Resources Inc., CONSOL Energy, Inc., Alpha Metallurgical Resources, Inc., Foresight Energy LP, and Peabody Energy Corporation."
- "We also compete directly with smaller producers in the Illinois Basin and Appalachian regions."

---

## 5. DATA LIMITS

1. **Units differ.** AMR and BTU: short tons (defined). HCC and Coronado: metric tons (defined; HCC gives
   1 metric ton = 1.102311 short tons). METC and ARLP: "tons" not defined in the MD&A; ARLP prices its reserves
   "per short ton"; neither filing states the unit of its tons-sold figure. No conversion has been applied anywhere in this file.
2. **Price bases differ.** AMR removes freight and handling revenue (export contracts are FOB port, with
   AMR bearing mine-to-port transport, removed from the measure); METC is FOB mine; HCC is net selling
   price with the cost measured to FOB Port of Mobile, freight included; BTU and ARLP use gross segment
   revenue per ton (ARLP excludes transportation revenue from coal sales); Coronado's realized price is
   coal revenues per tonne.
3. **Cost bases differ.** AMR excludes freight, DD&A, accretion, idle/closed mine costs; HCC includes freight
   and royalties; METC excludes transportation and idle; BTU includes royalties and production taxes and
   excludes DD&A, ARO, SG&A, restructuring, impairment; ARLP excludes transportation, DD&A and G&A;
   Coronado "mining costs" exclude royalties and freight. **A cross-company cost ranking from these
   columns is not like-for-like.** Within-company time series are comparable only where section 3.2 shows
   no definition change.
4. **Mixed product.** AMR's single segment includes 7% thermal by volume (2025); BTU Seaborne Met
   includes a US mine; METC's segment includes purchased coal; ARLP Appalachia includes export sales
   ("reduced export price realizations from our MC Mining and Mettiki mines", 10-K FY2025) that are not
   split out.
5. **Not found / not reported.** ARLP segment per-ton dollars for 2024-2025 (computed instead, labelled);
   AMR thermal per-ton from 2024 (no longer reported); BTU own-cost-position statement (none found);
   AMR and HCC FY2025 competitor names (none given); Coronado Q2 2026 on a per-Mt-sold mining-cost basis
   (the 10-Q changed to per Mt produced). METC per-ton figures are filed only as whole dollars.
6. **Quarterly seasonality.** The 2026 rows are three- or six-month figures, not annualized.
7. **Foreign producers (Teck, BHP, Glencore, Anglo, other Australian met coal).** Only two are on EDGAR:
   Teck files **40-F** (latest FY2025, filed 2026-02-19, accession 0000886986-26-000004) and BHP files
   **20-F** (latest FY2026 to June, filed 2026-08-18, accession 0001193125-26-354647). Glencore appears only
   as an ADR registrant ("Glencore plc/ADR", CIK 0001524684) with no 10-K/20-F/40-F in its submissions
   index; Anglo American was not found in the SEC ticker map (not proof it has no filings). None was
   fetched. The limits that apply: IFRS rather than US GAAP; different fiscal years (BHP to 30 June);
   metric tonnes; unit-cost measures defined on each company's own basis, with segment definitions that
   do not match US 10-K segments. Whether Teck's FY2025 40-F still carries a coal segment was not checked. **Coronado Global Resources is the exception: it files 10-K/10-Q, and its Australian
   operations (section 3.4) are the only filed, US-GAAP, per-tonne Australian met coal series available.**
   Its measures still differ from every US peer's (point 3).
