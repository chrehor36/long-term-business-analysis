# COMPETITOR ROW - five-year industrial margins (transcription from primary filings)

Built 2026-09-13 for the TM run. Transcription only. No conclusions drawn.
Every figure carries document type, fiscal year end, filing date, accession number.
Currency native. Margin = segment operating measure / segment revenue (computed here).

STATUS: COMPLETE for GM, Ford, Tesla, Honda, Stellantis (five years each). Volkswagen
partial (2 years absolute, 5 years stated ratio). Hyundai partial (2 years). BYD blocked.
A summary table sits just above the gaps table at the end.

## Method notes (apply to every section)
- Text copies of every filing used are saved in this folder as `<TICKER>_<FORM>_FY<year>.txt`
  (HTML stripped by regex; header line records the URL or local source and the accession).
  Filings already on disk in `_research 2026-09-01 GM` were re-stripped from their .htm, not
  copied from the older .txt (the older .txt files have no line breaks).
- Margins are computed here with `calc.py` (numerator / denominator, two decimals). No figure
  is taken from XBRL/companyfacts.
- Where a later filing restates a year, both values are shown and the later one is used.

---

## GM (General Motors Company, CIK 1467858), USD millions, US GAAP filer

**Sources**
| Short | Document | FYE | Filed | Accession |
|---|---|---|---|---|
| GM-25 | Form 10-K `gm-20251231.htm` | 2025-12-31 | 2026-01-27 | 0001467858-26-000013 |
| GM-24 | Form 10-K `gm-20241231.htm` | 2024-12-31 | 2025-01-28 | 0001467858-25-000032 |
| GM-23 | Form 10-K `gm-20231231.htm` | 2023-12-31 | 2024-01-30 | 0001467858-24-000031 |

**Segment measure (non-GAAP).** Note 23 row label: *"Earnings (loss) before interest and
taxes-adjusted"*. GM-25 Note 23: *"Our chief operating decision-maker evaluates the operating
results and performance of our Automotive operations through EBIT-adjusted, which is presented
net of noncontrolling interests."* Revenue label: *"Net sales and revenue"*. GM Financial is
measured on *"EBT-adjusted"*. 2025/2024/2023 from GM-25 Note 23; 2022/2021 from GM-23 Note 23.
GM-24 and GM-25 carry identical 2024 and 2023 GMNA/GMI figures to GM-23 where they overlap
(checked: GMNA 2023 141,445 / 12,306 in all three; 2024 157,509 / 14,528 in GM-24 and GM-25;
2022 GMNA 128,378 / 12,988 and GMI 15,420 / 1,143 identical in GM-24, the latest filing showing
2022). No restatement found.

### Segment revenue, EBIT-adjusted, margin
| Year | GMNA revenue | GMNA EBIT-adj | GMNA margin | GMI revenue | GMI EBIT-adj | GMI margin | GMNA+GMI revenue (computed) | GMNA+GMI EBIT-adj (computed) | margin |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 154,317 | 10,452 | 6.77% | 13,427 | 737 | 5.49% | 167,744 | 11,189 | 6.67% |
| 2024 | 157,509 | 14,528 | 9.22% | 13,890 | 303 | 2.18% | 171,399 | 14,831 | 8.65% |
| 2023 | 141,445 | 12,306 | 8.70% | 15,949 | 1,210 | 7.59% | 157,394 | 13,516 | 8.59% |
| 2022 | 128,378 | 12,988 | 10.12% | 15,420 | 1,143 | 7.41% | 143,798 | 14,131 | 9.83% |
| 2021 | 101,308 | 10,318 | 10.18% | 12,172 | 827 | 6.79% | 113,480 | 11,145 | 9.82% |

MD&A-stated *"EBIT-adjusted margin"* matches to one decimal: GMNA 6.8% / 9.2% (GM-25), 8.7% /
10.1% (GM-23); GMI 5.5% / 2.2% (GM-25), 7.6% / 7.4% (GM-23).

GM-23 Note 23 also gives a *"Total Automotive"* column that **includes Corporate**: revenue
157,667 / 143,974 / 113,584 and EBIT-adjusted 12,103 / 12,286 / 10,465 for 2023 / 2022 / 2021
(computed margins 7.68% / 8.53% / 9.21%). GM-25 no longer presents a Total Automotive column.

**GMI includes equity income from the China JVs.** GM-25 MD&A: *"The results of our joint
ventures are recorded in Equity income (loss), which is included in EBIT-adjusted above."*
GMI EBIT-adjusted excluding equity income: 2025 426; 2024 633; 2023 764; 2022 466.

**Adjustments excluded from segment EBIT-adjusted (Note 23 "Adjustments" row).** GMNA: 2025
(8,709); 2024 (738); 2023 (1,604); 2022 (411); 2021 (425). GMI: 2025 (918); 2024 (4,262); 2023
217; 2022 (657); 2021 (276). GM-25 footnote (b): *"Consists of charges for our EV strategic
realignment, legal matters, and Cruise restructuring activities in GMNA; China restructuring
actions in GMNA and GMI; and separation and exit costs in GMI."*

**Nearest GAAP figure: consolidated "Operating income (loss)"** (income statement) and
*"Total net sales and revenue"*: 2025 2,909 on 185,019 (1.57%); 2024 12,784 on 187,442 (6.82%);
2023 9,298 on 171,842 (5.41%); 2022 10,315 on 156,735 (6.58%); 2021 9,324 on 127,004 (7.34%).
2025-2023 from GM-25; 2022-2021 from GM-23. This is consolidated (includes GM Financial,
Cruise, Corporate); GM does not report GAAP operating income by segment.

### Units: "Wholesale vehicle sales" (vehicles in thousands; excludes JV vehicles)
| | 2025 | 2024 | 2023 | 2022 | 2021 |
|---|---|---|---|---|---|
| GMNA | 3,296 | 3,464 | 3,147 | 2,926 | 2,308 |
| GMI | 503 | 547 | 621 | 653 | 551 |
| Total | 3,799 | 4,010 | 3,768 | 3,579 | 2,859 |
Source: GM-25 Item 1 table (2025-2023); GM-23 Item 1 table (2023-2021). Memo, not in revenue:
*"Wholesale vehicle sales including vehicles exported to markets outside of China"* by the
Automotive China JVs 2,090 / 1,843 / 2,334 / 2,639 / 3,007.

### Captive finance: GM Financial
| Year | GM Financial EBT-adjusted | GM Financial adjustments | Consolidated "Income (loss) before income taxes" | EBT-adjusted share of consolidated pre-tax |
|---|---|---|---|---|
| 2025 | 2,802 | none | 3,117 | 89.89% |
| 2024 | 2,965 | (320) | 8,519 | 34.80% (31.05% after the (320) adjustment) |
| 2023 | 2,985 | none | 10,403 | 28.69% |
| 2022 | 4,076 | none | 11,597 | 35.15% |
| 2021 | 5,036 | none | 12,716 | 39.60% |
Mixed-basis ratio: a non-GAAP segment numerator over a GAAP consolidated denominator. GM does
not disclose GM Financial GAAP pre-tax income in Note 23 other than through the adjustments row.

### Pricing line in the causal bridge (MD&A "Variance Due To", USD billions, EBIT-adjusted row)
| | Volume | Mix | Price | Cost | Other |
|---|---|---|---|---|---|
| GMNA 2025 vs 2024 (GM-25) | (1.9) | 0.4 | **1.4** | (5.1) | 1.1 |
| GMNA 2024 vs 2023 (GM-24) | 3.9 | (3.1) | **0.7** | 1.3 | (0.6) |
| GMI 2025 vs 2024 (GM-25) | (0.2) | 0.2 | **0.5** | (0.2) | 0.3 |
| GMI 2024 vs 2023 (GM-24) | (0.4) | 0.1 | **0.2** | (0.2) | (0.7) |
| GMNA 2023 vs 2022 (GM-23) | 2.3 | (0.9) | **3.2** | (5.1) | (0.2) |
| GMI 2023 vs 2022 (GM-23) | (0.1) | 0.1 | **1.2** | (0.3) | (0.7) |

### Own words on capacity and pricing (GM-25, Item 1A Risk Factors, "Risks related to our competition and strategy")
> *"We operate in a highly competitive industry that has historically had excess manufacturing
> capacity, and attempts by our competitors to sell more vehicles could have a significant
> negative effect on our vehicle pricing, market share, and results of operations."*

> *"In light of any excess capacity and high fixed costs, many industry participants have
> attempted to sell more vehicles by providing subsidized financing or leasing programs,
> offering marketing incentives, or reducing vehicle prices. As a result, we have had, and may in
> the future need, to offer similar incentives, which may result in vehicle prices that do not
> offset our costs, including any cost increases or the impact of adverse currency fluctuations
> or tariffs, which could affect our profitability."*

---

## Ford (Ford Motor Company, CIK 37996), USD millions, US GAAP filer

**Sources**
| Short | Document | FYE | Filed | Accession |
|---|---|---|---|---|
| F-25 | Form 10-K `f-20251231.htm` | 2025-12-31 | 2026-02-11 | 0000037996-26-000015 |
| F-24 | Form 10-K `f-20241231.htm` | 2024-12-31 | 2025-02-06 | 0000037996-25-000013 |
| F-23 | Form 10-K `f-20231231.htm` | 2023-12-31 | 2024-02-07 | 0000037996-24-000009 |

**Segment measure (non-GAAP segment measure).** F-25 Note 25 row label *"Segment EBIT/EBT"*;
F-23 Note 26 labels the same row *"Income/(Loss) before income taxes"* by segment. F-25 Note 25:
*"When we report segment earnings before interest and taxes ("Segment EBIT") for each of the
Ford Blue, Ford Model e, and Ford Pro segments, it consists of the earnings for the particular
segment and does not include interest and taxes."* Special items, Corporate Other and interest
on debt are reconciling items outside the segments. **Revenue used is "External revenues"**,
which is the denominator Ford's own MD&A *"EBIT Margin (%)"* uses (e.g. Ford Blue 2025 3,024 /
101,019 = 3.0%). Total revenues including intersegment are larger for Ford Blue (2025 145,928;
2024 145,377; 2023 140,627; 2022 130,782; 2021 110,466) and Model e (2025 7,166; 2024 4,115;
2023 6,528; 2022 5,374; 2021 3,186).

### RESTATEMENTS RECORDED (later filing used)
| Year / segment | Earlier value (filing) | Later value (filing) |
|---|---|---|
| 2024 Ford Blue EBIT | 5,284 (F-24) | **5,269** (F-25) |
| 2024 Model e revenue / EBIT | 3,852 / (5,076) (F-24) | **3,858 / (5,105)** (F-25) |
| 2024 Ford Pro EBIT | 9,015 (F-24) | **9,007** (F-25) |
| 2023 Ford Blue EBIT | 7,462 (F-23, F-24) | **7,453** (F-25) |
| 2023 Model e revenue / EBIT | 5,897 / (4,701) (F-23, F-24) | **5,899 / (4,778)** (F-25) |
| 2023 Ford Pro EBIT | 7,222 (F-23, F-24) | **7,217** (F-25) |
| 2022, 2021 all segments | F-23 / F-24 basis, which still shows a separate "Ford Next" segment (2022 EBIT (926); 2021 (1,030)) | **not restated in any later filing** (F-25 shows only 2023-2025) |
So 2021-2022 and 2023-2025 are on slightly different segment bases; the 2023 differences above
measure the size of the change.

### Segment revenue (external), Segment EBIT, margin
| Year | Ford Blue rev | Blue EBIT | Blue margin | Model e rev | Model e EBIT | Model e margin | Ford Pro rev | Pro EBIT | Pro margin | Three segments rev (computed) | EBIT (computed) | margin |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025 | 101,019 | 3,024 | 2.99% | 6,670 | (4,806) | (72.05)% | 66,286 | 6,843 | 10.32% | 173,975 | 5,061 | 2.91% |
| 2024 | 101,935 | 5,269 | 5.17% | 3,858 | (5,105) | (132.32)% | 66,906 | 9,007 | 13.46% | 172,699 | 9,171 | 5.31% |
| 2023 | 101,934 | 7,453 | 7.31% | 5,899 | (4,778) | (81.00)% | 58,058 | 7,217 | 12.43% | 165,891 | 9,892 | 5.96% |
| 2022 | 94,762 | 6,847 | 7.23% | 5,253 | (2,133) | (40.61)% | 48,939 | 3,222 | 6.58% | 148,954 | 7,936 | 5.33% |
| 2021 | 80,377 | 3,293 | 4.10% | 3,098 | (892) | (28.79)% | 42,649 | 2,665 | 6.25% | 126,124 | 5,066 | 4.02% |
2025-2023 from F-25 Note 25 and MD&A; 2022-2021 from F-23 Note 26 and MD&A.

**Nearest GAAP figure: consolidated "Operating income/(loss)"** on total revenues: 2025 (9,169)
on 187,267 ((4.90)%); 2024 5,219 on 184,992 (2.82%); 2023 5,458 on 176,191 (3.10%); 2022 6,276
on 158,057 (3.97%); 2021 4,523 on 136,341 (3.32%). F-25 MD&A supplemental: *"Company excluding
Ford Credit"* Operating income/(loss) 2025 **(11,319)**; F-23 supplemental 2023 4,649.
Special items (reconciling): 2025 (17,356); 2024 (1,860); 2023 (5,147); 2022 (12,172); 2021
9,583.

### Units: "Wholesale Units (000)"
| | 2025 | 2024 | 2023 | 2022 | 2021 |
|---|---|---|---|---|---|
| Ford Blue (a) | 2,728 | 2,862 | 2,920 | 2,834 | 2,694 |
| Ford Model e | 178 | 105 | 116 | 96 | 61 |
| Ford Pro (b) | 1,488 | 1,503 | 1,377 | 1,301 | 1,187 |
| Sum (computed) | 4,394 | 4,470 | 4,413 | 4,231 | 3,942 |
(a) *"Includes Ford and Lincoln brand and JMC brand vehicles produced and sold in China by our
unconsolidated affiliates"*: about 375,000 (2025), 438,000 (2024), 455,000 (2023), 484,000
(2022), 633,000 (2021). (b) Includes Ford Otosan units: about 98,000 / 91,000 / 90,000 / 76,000
/ 61,000. **Wholesale units therefore include unconsolidated-affiliate vehicles not in revenue.**

### Captive finance: Ford Credit
| Year | Ford Credit segment EBT | Consolidated "Income/(Loss) before income taxes" | Share |
|---|---|---|---|
| 2025 | 2,557 | (11,830) | n.m. (consolidated loss) |
| 2024 | 1,654 | 7,233 | 22.87% |
| 2023 | 1,331 | 3,967 | 33.55% |
| 2022 | 2,657 | (3,016) | n.m. (consolidated loss) |
| 2021 | 4,717 | 17,780 | 26.53% |
F-25 supplemental income statement: Ford Credit *"Income/(Loss) before income taxes"* 2,557
(same as segment EBT; GAAP basis in that table); Ford Credit operating income 2,150.

### Pricing line in the causal bridge ("Net Pricing", USD millions, *"Change in EBIT by Causal Factor"*)
| | 2025 vs 2024 (F-25) | 2024 vs 2023 (F-25) | 2023 vs 2022 (F-23) | 2022 vs 2021 (F-23) |
|---|---|---|---|---|
| Ford Blue | **1,487** | **732** | 235 | 6,181 |
| Ford Model e | **(7)** | **(1,575)** | (1,005) | 418 |
| Ford Pro | **(1,024)** | **937** | 7,067 | 4,267 |
F-25: Ford Pro 2025 *"The lower EBIT was primarily driven by unfavorable fleet pricing
(including daily rental), unfavorable mix, and higher tariff-related costs."* Model e 2024:
*"primarily driven by lower net pricing due to industrywide competitive pressures"*.

### Own words on capacity and pricing (F-25)
Item 1A Risk Factors:
> *"Ford may face increased price competition for its products and services, including pricing
> pressure resulting from industry excess capacity, currency fluctuations, competitive actions,
> legal and policy changes, or economic or other factors, particularly for electrified vehicles.
> The global automotive industry is intensely competitive, with installed manufacturing capacity
> generally exceeding current demand."*

Item 1. Business (Continued), paragraph following the profitability-factors list:
> *"our industry has historically had a very competitive pricing environment, driven in part by
> excess capacity. For the past several decades, manufacturers typically have offered price
> discounts and other marketing incentives to provide value for customers and maintain market
> share and production levels"*

---

## Tesla (Tesla, Inc., CIK 1318605), USD millions, US GAAP filer

**Sources**
| Short | Document | FYE | Filed | Accession |
|---|---|---|---|---|
| T-25 | Form 10-K `tsla-20251231.htm` | 2025-12-31 | 2026-01-29 | 0001628280-26-003952 |
| T-24 | Form 10-K `tsla-20241231.htm` | 2024-12-31 | 2025-01-30 | 0001628280-25-003063 |
| T-23 | Form 10-K `tsla-20231231.htm` | 2023-12-31 | 2024-01-29 | 0001628280-24-002390 |
| T-22 | Form 10-K `tsla-20221231.htm` | 2022-12-31 | 2023-01-31 | 0000950170-23-001409 |
| T-21 | Form 10-K `tsla-20211231.htm` | 2021-12-31 | 2022-02-07 | 0000950170-22-000796 |
(10-K/A filings for FY2021, FY2024 and FY2025 exist on EDGAR; they were not opened or used.)

**Segment measure: segment GROSS PROFIT, not operating income.** T-25 Note 16: *"The CODM
uses gross profit to allocate operating and capital resources and assesses performance of each
segment by comparing actual gross profit results to historical results and previously forecasted
financial information."* Row labels: *"Automotive segment"* / *"Revenues"* / *"Gross profit"*.
The automotive segment includes *"services and other"* and regulatory credits. **Tesla's
segment margin is therefore not comparable to the operating-profit or EBIT measures of the
other companies in this file**; R&D and SG&A are not allocated to segments.

### Segment revenue, segment gross profit, margin; plus the nearest GAAP operating figure
| Year | Automotive segment revenues | Automotive segment gross profit | Gross margin (computed) | Consolidated "Income from operations" | Consolidated "Total revenues" | Operating margin (computed) | Source |
|---|---|---|---|---|---|---|---|
| 2025 | 82,056 | 13,292 | 16.20% | 4,355 | 94,827 | 4.59% | T-25 |
| 2024 | 87,604 | 14,810 | 16.91% | 7,076 | 97,690 | 7.24% | T-25 (same in T-24) |
| 2023 | 90,738 | 16,519 | 18.21% | 8,891 | 96,773 | 9.19% | T-25 (same in T-23, T-24) |
| 2022 | 77,553 | 20,565 | 26.52% | 13,656 | 81,462 | 16.76% | T-23 (same in T-22) |
| 2021 | 51,034 | 13,735 | 26.91% | 6,523 | 53,823 | 12.12% | T-23 (same in T-21, T-22) |
MD&A-stated *"Gross margin total automotive & services and other segment"*: 16.2% / 16.9% /
18.2% (T-25), 26.5% (2022, T-24), 26.9% (2021, T-23). Consolidated income from operations
includes the energy segment (2025 energy gross profit 3,802), so it is not an automotive-only
figure; Tesla discloses no automotive-only operating income. Memo: 2025 automotive
regulatory credits 1,993; 2024 2,763; 2023 1,790; 2022 1,776; 2021 1,465 (inside segment revenue
and, at near-zero cost, inside segment gross profit).

### Units (company's own words, Item 7 MD&A overview)
| Year | Produced | Delivered | Label | Source |
|---|---|---|---|---|
| 2025 | approximately 1.66 million | approximately 1.64 million | "consumer vehicles" | T-25 |
| 2024 | approximately 1,773,000 | approximately 1,789,000 | "consumer vehicles" | T-24 |
| 2023 | 1,845,985 | 1,808,581 | "consumer vehicles" | T-23 |
| 2022 | 1,369,611 | 1,313,851 | "consumer vehicles" | T-22 |
| 2021 | 930,422 | 936,222 | "vehicles" | T-21 |

### Captive finance
**No finance segment.** T-25 Note 16 names two reportable segments (automotive; energy
generation and storage). Consolidated "Income before income taxes": 2025 5,278; 2024 8,990; 2023
9,973; 2022 13,719; 2021 6,343. **Finance pre-tax income: not disclosed / no such segment.**

### Pricing line
**No quantified causal bridge.** Narrative only:
- T-25 MD&A: *"Automotive sales revenue decreased $6.66 billion, or 9%, in the year ended
  December 31, 2025 as compared to the year ended December 31, 2024, due a decrease of
  approximately 8% in cash deliveries and a lower average selling price per unit driven by sales
  mix and higher customer incentives such as attractive financing options."* (sic, "due a")
- T-24 MD&A: *"primarily due to lower average selling price on our vehicles driven by overall
  price reductions and attractive financing options provided in 2024 as well as mix."*

### Own words on competition and pricing (T-25, Item 1A Risk Factors)
> *"The worldwide automotive market is highly competitive today and we expect it will become
> even more so in the future. ... Increased competition could result in our lower vehicle unit
> sales, price reductions, revenue shortfalls, loss of customers and loss of market share, which
> may harm our business, financial condition and operating results."*
The terms "excess capacity", "overcapacity", "pricing pressure" and "price competition" do not
appear in T-25 or T-24 (text search).

---

## Honda (Honda Motor Co., Ltd., CIK 715153), JPY millions, IFRS

**Sources**
| Short | Document | FYE | Filed | Accession |
|---|---|---|---|---|
| H-26 | Form 20-F `d116494d20f.htm` | 2026-03-31 | 2026-06-18 | 0001193125-26-274991 |
| H-25 | Form 20-F `d877523d20f.htm` | 2025-03-31 | 2025-06-18 | 0001193125-25-142316 |
| H-24 | Form 20-F `d767050d20f.htm` | 2024-03-31 | 2024-06-20 | 0001193125-24-163995 |
| H-22 | Form 20-F `d280812d20f.htm` | 2022-03-31 | 2022-06-22 | 0001193125-22-178101 |

**Segment measure (IFRS, consistent with operating profit).** Row label *"Segment profit
(loss)"*. H-26 Note (4): *"Segment profit (loss) of each segment is measured in a consistent
manner with consolidated operating profit (loss), which is profit (loss) before income taxes
before share of profit (loss) of investments accounted for using the equity method and finance
income and finance costs."* Revenue label *"Sales revenue"*, rows *"External customers"*,
*"Intersegment"*, *"Total"*. Margins below use **Total** (incl. intersegment); external-only
margins for Automobile are given as a memo. FY2024 values are identical in H-24, H-25 and H-26;
FY2023 values (segment and unit tables) are identical in H-24 and H-25 (the latest filing
showing FY2023); FY2022 values are identical in H-22 and H-24. No restatement found.

### Automobile business and Motorcycle business
| FY ended Mar | Automobile total revenue | Automobile segment profit (loss) | Auto margin (total) | Auto margin (external) | Motorcycle revenue (all external) | Motorcycle segment profit | Moto margin | Source |
|---|---|---|---|---|---|---|---|---|
| 2026 | 14,166,910 | (1,411,140) | (9.96)% | (10.18)% | 4,018,837 | 731,926 | 18.21% | H-26 |
| 2025 | 14,467,856 | 243,853 | 1.69% | 1.72% | 3,626,603 | 663,443 | 18.29% | H-26 |
| 2024 | 13,791,515 | 560,649 | 4.07% | 4.13% | 3,220,168 | 556,232 | 17.27% | H-26 (same in H-24) |
| 2023 | 10,781,717 | (16,629) | (0.15)% | (0.16)% | 2,908,983 | 488,709 | 16.80% | H-24 |
| 2022 | 9,360,593 | 236,207 | 2.52% | 2.58% | 2,185,253 | 311,492 | 14.25% | H-24 (same in H-22) |
| *2021 (extra)* | 8,779,349 | 90,255 | 1.03% | | 1,787,283 | 224,608 | 12.57% | H-22 |
| *2020 (extra)* | 10,194,638 | 153,323 | 1.50% | | 2,059,335 | 285,668 | 13.87% | H-22 |
Automobile external revenue: 13,863,362 / 14,169,240 / 13,567,565 / 10,593,519 / 9,147,498.
FY2026 Automobile includes EV-related losses of about ¥1,577.8bn (H-26 Note (4)(d); detail in
`_research 2026-09-01 GM\COMPETITOR ROW - Toyota and Honda, from 20-F filings.md`).

**Consolidated (IFRS) operating profit (loss)** on sales revenue: FY2026 (414,346) on
21,796,610 ((1.90)%); FY2025 1,213,486 on 21,688,767 (5.59%); FY2024 1,381,977 on 20,428,802
(6.76%); FY2023 780,769 on 16,907,725 (4.62%); FY2022 871,232 on 14,552,696 (5.99%).

### Units (thousands), Item 4 tables: "Honda Group Unit Sales" and "Consolidated Unit Sales"
| FY ended Mar | Automobiles, Group | Automobiles, Consolidated | Motorcycles (incl. ATV, SxS), Group | Motorcycles, Consolidated | Source |
|---|---|---|---|---|---|
| 2026 | 3,387 | 2,711 | 22,101 | 14,673 | H-26 |
| 2025 | 3,716 | 2,840 | 20,572 | 13,685 | H-26 |
| 2024 | 4,109 | 2,856 | 18,819 | 12,219 | H-26 / H-24 |
| 2023 | 3,687 | 2,382 | 18,757 | 12,161 | H-24 |
| 2022 | 4,074 | 2,424 | 17,027 | 10,721 | H-24 |
H-26 footnote: *"Honda Group Unit Sales is the total unit sales of completed products of Honda,
its consolidated subsidiaries and its affiliates and joint ventures accounted for using the
equity method. Consolidated Unit Sales is the total unit sales of completed products
corresponding to consolidated sales revenue"*.

### Captive finance: Financial services business
| FY ended Mar | FS segment profit | Consolidated "Profit (loss) before income taxes" | Share |
|---|---|---|---|
| 2026 | 275,532 | (403,300) | n.m. (consolidated loss) |
| 2025 | 315,634 | 1,317,640 | 23.95% |
| 2024 | 273,978 | 1,642,384 | 16.68% |
| 2023 | 285,857 | 879,565 | 32.50% |
| 2022 | 333,032 | 1,070,190 | 31.12% |
Mixed basis: FS segment profit is an operating-profit measure; Honda discloses no segment
pre-tax income.

### Pricing line
**Not quantified in the 20-F.** Narrative only (H-26, Item 5, Automobile business):
- FY2026: *"Operating loss was ¥1,411.1 billion, a decrease of ¥1,654.9 billion from the previous
  fiscal year, due mainly to the impact of EV-related losses as well as tariff impacts, which was
  partially offset by increased profit attributable to price and cost impacts."* And on revenue:
  *"Despite changes in sales price, the impact of the price changes was immaterial on sales
  revenue."*
- FY2025: *"Operating profit decreased by ¥316.7 billion, or 56.5%, to ¥243.8 billion from the
  previous fiscal year, due mainly to decreased profit attributable to sales impacts, increased
  research and development expenses as well as the change in the estimation model for automobile
  product warranties, which was partially offset by increased profit attributable to price and
  cost impacts."*

### Own words on competition and pricing (H-26)
Item 3.D Risk Factors:
> *"In particular, the automotive industry is undergoing a period of major change, including
> intensifying competition due to the rise of emerging Chinese EV companies, changes in
> environmental policies in North America and Europe and global trade wars arising from the
> imposition of additional tariffs by the United States."*

Section "Management Policies and Strategies", sub-heading "Financial Strategy" (Item number
not confirmed from the stripped text):
> *"the profitability of Automobile business is currently declining due to the impact of changes
> in U.S. tariff policies on ICE and hybrid vehicles, a decline in the competitiveness of our
> products in Asia stemming from the impact of the allocation of more resources to EV
> development, and intensifying competition with the rise of new EV manufacturers."*
The terms "excess capacity", "overcapacity" and "pricing pressure" do not appear in H-26
(text search).

---

## Stellantis (Stellantis N.V., CIK 1605484), EUR millions, IFRS

**Sources**
| Short | Document | FYE | Filed | Accession |
|---|---|---|---|---|
| S-25 | Form 20-F `stellantis-20251231.htm` | 2025-12-31 | 2026-02-26 | 0001605484-26-000021 |
| S-24 | Form 20-F `stellantis-20241231.htm` | 2024-12-31 | 2025-02-27 | 0001605484-25-000013 |
| S-23 | Form 20-F `stellantis-20231231.htm` | 2023-12-31 | 2024-02-22 | 0001605484-24-000022 |
| S-21 | Form 20-F `stellantis-20211231.htm` | 2021-12-31 | 2022-02-25 | 0001605484-22-000023 |

**Segment measure (non-GAAP).** Row label *"Adjusted operating income/(loss)"*; revenue label
*"Net revenues"* (incl. transactions with other segments). S-25 segment note: *"Adjusted
operating income/(loss) is the measure used by the chief operating decision maker to assess
performance, allocate resources to the Company's operating segments"* and it *"excludes from
Net profit/(loss) from continuing operations adjustments comprising restructuring and other
termination costs, impairments, asset write-offs, disposals of investments and unusual operating
income/(expense) ... and also excludes Net financial expenses/(income) and Tax
expense/(benefit)."* Six vehicle segments: North America (NA), Enlarged Europe (EE), Middle East
& Africa (MEA), South America (SA), China and India & Asia Pacific (CIAP), Maserati. S-25 notes
the Maserati segment is eliminated from 2026-01-01.

**Restatement check.** 2023 identical in S-23, S-24, S-25; 2022 identical in S-23 and S-24;
2024 identical in S-24 and S-25. None found.

**2021 is a stub-consolidation year.** The merger closed January 2021; S-23 shows 2021 both
as reported and "Pro Forma" (adding FCA January 1 - 16, 2021). The table uses the **reported**
columns: *"Net revenues"* 149,419 and *"Adjusted operating income, as adjusted"* 18,564 (S-23
note). S-23 also shows *"Adjusted operating income, as reported"* 17,827, the difference being
*"Add: Share of profit/(loss) of equity method investees"* 737, i.e. **the AOI definition
changed after 2021 to include equity-method results**; the "as adjusted" figure is on the later
definition. Pro forma: Net revenues 152,119; AOI 18,751.

### Segment Net revenues and AOI by vehicle segment
| Year | NA rev | NA AOI | EE rev | EE AOI | MEA rev | MEA AOI | SA rev | SA AOI | CIAP rev | CIAP AOI | Maserati rev | Maserati AOI | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025 | 60,962 | (1,892) | 57,773 | (651) | 9,709 | 1,429 | 16,197 | 1,963 | 1,868 | 74 | 726 | (198) | S-25 |
| 2024 | 63,450 | 2,660 | 59,010 | 2,419 | 10,097 | 1,901 | 15,863 | 2,272 | 1,993 | (58) | 1,040 | (260) | S-25 |
| 2023 | 86,500 | 13,298 | 66,598 | 6,519 | 10,560 | 2,503 | 16,058 | 2,369 | 3,528 | 502 | 2,335 | 141 | S-25 |
| 2022 | 85,475 | 13,987 | 63,311 | 6,218 | 6,453 | 1,188 | 15,620 | 2,048 | 4,505 | 641 | 2,320 | 201 | S-24 |
| 2021 | 67,715 | 11,089 | 58,728 | 5,373 | 5,165 | 672 | 10,496 | 873 | 3,927 | 437 | 2,003 | 116 | S-23 |

### Margins (computed)
| Year | NA | EE | MEA | SA | CIAP | Maserati | Six vehicle segments: rev / AOI / margin | Total AOI / Net revenues (filing-stated margin) | IFRS "Operating income/(loss)" / Net revenues |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | (3.10)% | (1.13)% | 14.72% | 12.12% | 3.96% | (27.27)% | 147,235 / 725 / 0.49% | (842) / 153,508 = (0.55)% [filing: (0.5%)] | (26,254) = (17.10)% |
| 2024 | 4.19% | 4.10% | 18.83% | 14.32% | (2.91)% | (25.00)% | 151,453 / 8,934 / 5.90% | 8,648 / 156,878 = 5.51% [filing: 5.5%] | 3,687 = 2.35% |
| 2023 | 15.37% | 9.79% | 23.70% | 14.75% | 14.23% | 6.04% | 185,579 / 25,332 / 13.65% | 24,343 / 189,544 = 12.84% | 22,376 = 11.81% |
| 2022 | 16.36% | 9.82% | 18.41% | 13.11% | 14.23% | 8.66% | 177,684 / 24,283 / 13.67% | 24,017 / 179,592 = 13.37% | 20,276 = 11.29% |
| 2021 | 16.38% | 9.15% | 13.01% | 8.32% | 11.13% | 5.79% | 148,034 / 18,560 / 12.54% | 18,564 / 149,419 = 12.42% | 15,863 = 10.62% |
Total AOI and total Net revenues include "Other activities" (which contains financial services)
and "Unallocated items & eliminations". Total adjustments between IFRS operating income and
AOI: 2025 25,412; 2024 4,961; 2023 1,967; 2022 3,741; 2021 2,712 (Jan 1 - Dec 31 basis).

### Units: "Consolidated shipments" (thousands of units)
| Year | NA | EE | MEA | SA | CIAP | Maserati | Total Consolidated shipments | Joint venture shipments | Source |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 1,472 | 2,490 | 453 | 1,000 | 61 | 8 | 5,484 | 89 | S-25 |
| 2024 | 1,432 | 2,576 | 423 | 912 | 61 | 11 | 5,415 | 111 | S-25 |
| 2023 | 1,903 | 2,814 | 443 | 879 | 102 | 27 | 6,168 | 225 | S-23 |
| 2022 | 1,861 | 2,626 | 283 | 859 | 127 | 26 | 5,782 | 221 | S-23 |
| 2021 | 1,764 | 2,847 | 272 | 811 | 118 | 24 | 5,836 | 213 | S-21 |
S-24 shows 2024 total 5,415 and 2023 total 6,168 (same). S-21 footnote: *"Shipments for 2020
and 2019 refer to PSA only."* The 2021 column carries no footnote; whether it includes FCA
volumes for January 1-16, 2021 is **not determined** from the text.

### Captive finance
**Financial-services pre-tax income: NOT DISCLOSED in any year.** S-25 segment note: *"Other
activities includes ... our financial services activities"*. European finance is via 50% joint
ventures (equity method). Consolidated profit before taxes (computed as *"Net profit/(loss) from
continuing operations"* + *"Tax expense/(benefit)"* from the segment-note reconciliation):
2025 (22,332) + (4,273) = (26,605); 2024 5,520 + (1,488) = 4,032; 2023 18,625 + 3,793 = 22,418;
2022 16,779 + 2,729 = 19,508; 2021 13,218 + 1,911 = 15,129. Finance share: not computable.

### Pricing line in the causal bridge
**BLOCKED: the AOI "by operational driver" walks are images.** S-25 text reads *"Adjusted
operating income/(loss) by operational driver - 2025 compared to 2024 (€ million)"* followed by
no figures; the HTML carries `<img>` elements (e.g. `stellantis-20251231_g2.gif`). The driver
definition exists in text: *"Vehicle Net Price : Reflects changes in prices, net of discounts
and other sales incentive programs"*. Narrative (S-25, section "Trends, Uncertainties and
Opportunities", sub-heading "Pricing"): *"In 2025, net pricing declined in North America, Enlarged Europe
and South America and improved in Middle East & Africa."* and *"To address these inventory
levels we repositioned our pricing relative to peers and implemented incentives which had an
adverse impact on our net pricing."* (about 2024). Item numbers for these sections are not
confirmed from the stripped text; section headings are. Enlarged Europe 2025 AOI decrease *"was primarily
due to unfavorable pricing and mix, lower volumes, and higher industrial costs related to
warranty and LCV compliance provisions, partially mitigated by improved purchasing and
manufacturing performance."*

### Own words on capacity and pricing (S-25)
Section "Trends, Uncertainties and Opportunities", sub-heading "Pricing":
> *"The automotive industry has historically experienced intense price competition resulting
> from the variety of available competitive vehicles and excess global manufacturing capacity.
> Manufacturers have typically promoted products by offering dealer, retail and fleet
> incentives, including cash rebates, option package discounts, and subsidized financing or
> leasing programs, leading to increased price pressure and sharpened competition within the
> industry."*

Risk factors, sub-heading "Risks Related to the Industry in which We Operate":
> *"Intense competition, excess global manufacturing capacity and the proliferation of new
> products introduced in key segments is expected to continue to put downward pressure on
> inflation-adjusted vehicle prices and contribute to a challenging pricing environment in the
> automotive industry for the foreseeable future."*

---

## Volkswagen AG / Hyundai Motor / BYD (non-SEC; one attempt each)
Fetched with `try_ir.py` on 2026-09-13; PDFs text-extracted with PyMuPDF (`fitz`). The URLs
were located by web search, then fetched directly. Saved as `VW_AR2025.pdf/.txt`,
`HYUNDAI_2025_audit.pdf/.txt`, `BYD_HKEX_20260428.pdf/.txt`.

### Volkswagen AG, EUR millions, IFRS
**Source:** *Volkswagen Group Annual Report 2025*, URL
`https://annualreport2025.volkswagen-group.com/_assets/downloads/entire-vw-ar25.pdf` (HTTP 200,
26,086,002 bytes, 673 pages). Report text: *"This Annual Report was published on the occasion
of the Annual Media Conference on March 10, 2026."* Management board signature *"Wolfsburg,
March 6, 2026"*.

**Measure:** IFRS *"Operating result"* and *"Operating return on sales"* for the *"Automotive
Division"* (passenger cars, light commercial vehicles, commercial vehicles; excludes the
Financial Services Division). Key Figures footnote 2: *"As of January 1, 2025, the Automotive
Division no longer includes the allocation of consolidation adjustments between the Automotive
and Financial Services divisions. Figures reflect the reporting structure in force since 2025."*

| Year | Automotive sales revenue | Automotive operating result | Margin | Group vehicle sales (thousands) | Source location |
|---|---|---|---|---|---|
| 2025 | 290,390 | 5,279 | 1.82% computed; 1.8% stated | 9,022 | p.117 "Income Statement by Division"; p.666 Five-Year Review |
| 2024 | 290,646 | 16,300 | 5.61% computed; 5.6% stated | 9,037 | same |
| 2023 | not in this report | not in this report | 7.0% stated | 9,362 | p.667 "Financial Key Performance Indicators" |
| 2022 | not in this report | not in this report | 7.1% stated | 8,481 | p.667 |
| 2021 | not in this report | not in this report | 6.4% stated | 8,576 | p.667 |
p.667 footnote 3 on the Automotive Division rows: *"Since 2024 the figures reflect the adjusted
reporting structure."* 2023 and 2022 columns are footnoted *"adjusted"*. **2021-2023
operating return on sales is company-stated only; absolute revenue and operating result for
those years would need the 2021-2023 annual reports (not fetched).** The five-year "Vehicle
sales (units)" row is the Group line in the Five-Year Review, not an Automotive Division line.

**Nearest group figure:** Group operating result 8,868 / 19,060 / 22,528 / 22,109 / 19,275 on
sales revenue 321,913 / 324,656 / 322,284 / 279,050 / 250,200 (Group operating return on sales
stated 2.8 / 5.9 / 7.0 / 7.9 / 7.7%), 2025 to 2021, Five-Year Review.

**Captive finance:** Financial Services Division *"Earnings before tax"* 2025 3,340; 2024 2,994;
Group earnings before tax 9,307; 16,806; **share 35.89% (2025), 17.82% (2024)**, p.117.
Financial Services operating result 3,708 / 3,119.

**Pricing bridge:** no numeric pricing line found in the text. Narrative only (p.117, Automotive
Division): *"Changes in the mix, pricing and exchange rates and rising expenses for the
establishment of the Battery business field also weighed on earnings."* (2025 vs 2024). The
2024 vs 2023 explanation is in the 2024 report, not fetched.

**Own words (Report on Risks and Opportunities):**
> *"Excess capacity in global automotive production may result in increased inventories and
> tied-up capital, and, if demand for vehicles and parts declines, the Volkswagen Group may be
> forced to adjust capacities or intensify sales measures, presenting risks that could entail
> additional costs and increased pricing pressure."* (PDF page 184)

> *"... and lead to, among other things, intensified price competition, rising inventories,
> increase in tied-up capital and excess capacity in production."* (PDF page 172)

### Hyundai Motor Company, KRW millions, K-IFRS
**Source:** *Hyundai Motor Company and its Subsidiaries, Consolidated Financial Statements for
each of the two years in the period ended December 31, 2025*, with independent auditor's
report (Ernst & Young Han Young, dated March 4, 2026). URL
`https://www.hyundai.com/content/dam/hyundai/ww/en/images/company/investor-relations/financial-Information/report-en/2025/2025-q4-consolidated-audit-report-en.pdf`
(HTTP 200, 106 pages). This is the audited financial statements, **not the annual report**;
it carries two years only.

**Measure:** Note 37 *"SEGMENT INFORMATION"*, row *"Operating profit"*, segment *"Vehicle"*.
| Year | Vehicle "Net sales (*1)" (external) | Vehicle "Total sales (*2)" (incl. inter-company) | Vehicle operating profit | Margin on net sales | Margin on total sales |
|---|---|---|---|---|---|
| 2025 | 145,631,818 | 232,879,832 | 7,358,550 | 5.05% | 3.16% |
| 2024 | 136,725,011 | 221,891,250 | 11,074,739 | 8.10% | 4.99% |
| 2023-2021 | not in this document | | | | |
**The two denominators differ by about 60%** because inter-company sales within the vehicle
segment are large; the choice of denominator changes the margin materially.

**Captive finance:** Finance segment operating profit 2,164,043 (2025), 1,795,249 (2024);
consolidated *"Profit before income tax"* 13,841,903 / 17,781,436; mixed-basis share 15.63% /
10.10%. **Units:** not in the financial statements (Hyundai's press release cites 4,138,389
worldwide sales for 2025; press release not fetched, figure not verified).
**Capacity/pricing quotes and pricing bridge:** not in the financial statements; the annual
report / business report was not obtained.

### BYD Company Limited, CNY: BLOCKED
- Attempt 1: `https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0428/2026042803001.pdf`
  (HTTP 200, 19 pages). **Wrong document**: it is the *"2026 FIRST QUARTERLY REPORT"*
  (unaudited), not the 2025 annual report. No segment operating profit extracted.
- Attempt 2: IR site `https://www.bydglobal.com/en/Investor.html` returned **HTTP 504 Gateway
  Time-out after 57.1 seconds** (Tengine/Alibaba CDN page).
- Stopped per the attempt limit. The 2025 annual report was released on or about 2026-03-27 per
  secondary press (not used as a source).

---

## SUMMARY (transcribed and computed above; industrial segment measure only)
| Company | Measure | 2025 (HMC: FY3/26) | 2024 | 2023 | 2022 | 2021 |
|---|---|---|---|---|---|---|
| GM (GMNA+GMI) | EBIT-adjusted, non-GAAP | 6.67% | 8.65% | 8.59% | 9.83% | 9.82% |
| Ford (Blue+Model e+Pro) | Segment EBIT, non-GAAP | 2.91% | 5.31% | 5.96% | 5.33% | 4.02% |
| Tesla (automotive) | Segment GROSS profit | 16.20% | 16.91% | 18.21% | 26.52% | 26.91% |
| Honda automobile | IFRS segment op. profit | (9.96)% | 1.69% | 4.07% | (0.15)% | 2.52% |
| Honda motorcycle | IFRS segment op. profit | 18.21% | 18.29% | 17.27% | 16.80% | 14.25% |
| Stellantis (six vehicle segments) | AOI, non-GAAP | 0.49% | 5.90% | 13.65% | 13.67% | 12.54% |
| Volkswagen Automotive Division | IFRS operating result | 1.8% | 5.6% | 7.0%* | 7.1%* | 6.4%* |
| Hyundai vehicle segment | K-IFRS op. profit, on external sales | 5.05% | 8.10% | n/a | n/a | n/a |
Honda columns are fiscal years ended March 2026, 2025, 2024, 2023, 2022. *VW 2021-2023
company-stated ratio only. The measures differ by company and are not like-for-like.

---

## NOT DISCLOSED / BLOCKED
| Company | Item | Status / obstacle |
|---|---|---|
| GM | Segment GAAP operating income | Not disclosed; only consolidated operating income |
| GM | GM Financial GAAP pre-tax income | Not shown directly in Note 23; derivable only as EBT-adjusted less the adjustments row |
| Ford | 2021-2022 on the post-2025 segment basis (Ford Next folded) | Not restated in any filing; 2021-2022 remain on the F-23/F-24 basis |
| Ford | Consolidated wholesale total | Not taken; segment sum includes unconsolidated-affiliate units |
| Ford | Finance share 2022, 2025 | Not meaningful (consolidated pre-tax loss) |
| Tesla | Segment operating income | Not disclosed; CODM measure is gross profit |
| Tesla | Captive finance segment / finance pre-tax income | No such segment |
| Tesla | Causal bridge with a pricing line | Not disclosed; narrative only |
| Tesla | 10-K/A filings FY2021, FY2024, FY2025 | Not opened |
| Honda | Segment pre-tax income | Not disclosed; segment profit is an operating measure |
| Honda | Quantified pricing line | Not disclosed in the 20-F; "price and cost impacts" narrative only |
| Honda | Finance share FY2026 | Not meaningful (consolidated pre-tax loss) |
| Stellantis | Financial-services pre-tax income, all years | Not disclosed; inside "Other activities" |
| Stellantis | AOI walk by operational driver incl. "Vehicle Net Price" | BLOCKED: charts are images (e.g. `stellantis-20251231_g2.gif`), no numbers in text |
| Stellantis | 2021 comparability | Stub consolidation from 2021-01-17; AOI definition changed after 2021 (equity-method share now included); "as adjusted" figures used |
| Stellantis | Whether 2021 shipments include FCA Jan 1-16 | Not determined from text |
| Stellantis | Section Item numbers for quotes | Not confirmed from stripped text; section headings confirmed |
| Honda | Item number for "Management Policies and Strategies" quote | Not confirmed from stripped text |
| Volkswagen | Automotive Division absolute revenue and operating result 2021-2023 | Not in the 2025 report; only the stated operating return on sales. Older reports not fetched |
| Volkswagen | Automotive Division unit sales | Not transcribed; Five-Year Review units are Group vehicle sales |
| Volkswagen | Numeric pricing line in an operating-result bridge | Not disclosed numerically in the 2025 report text; narrative only. 2024 vs 2023 not obtained |
| Hyundai | 2021-2023 vehicle segment figures | Document fetched is the two-year audited FS only; annual report not obtained |
| Hyundai | Units, capacity/pricing quotes, pricing bridge | Not in the audited FS; not obtained |
| BYD | Everything | BLOCKED: HKEX link found was the 2026 Q1 report (wrong document); IR site `bydglobal.com/en/Investor.html` HTTP 504 after 57s. Attempt limit reached |
