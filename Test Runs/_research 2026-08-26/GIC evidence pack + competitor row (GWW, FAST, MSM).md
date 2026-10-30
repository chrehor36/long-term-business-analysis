# GIC — EVIDENCE PACK AND COMPETITOR ROW
**Global Industrial Company (NYSE: GIC), CIK 0000945114.** Assembled 2026-08-31 for
`Test Runs/2026-08-31 Run - GIC (Global Industrial) v4.1.md`. Every figure here is from an
SEC EDGAR primary document. Aggregators appear once, for the live quote, and are flagged.

---
## §1 — DOCUMENTS READ, WITH ACCESSION NUMBERS

| document | period | filed | accession | primary doc |
|---|---|---|---|---|
| **10-K (principal)** | FY ended 2025-12-31 (53 weeks, ended 2026-01-03) | 2026-02-27 | **0001628280-26-012945** | gic-20251231.htm |
| **10-Q (newest)** | Q2 ended 2026-06-30 (actual 2026-07-04) | 2026-08-04 | **0001628280-26-052687** | gic-20260630.htm |
| **DEF 14A (latest)** | FY2025 comp year | 2026-04-22 | **0001628280-26-026622** | gic-20260422.htm |
| 8-K + Ex-99.1 (Q2 2026 release) | 2026-08-04 | 2026-08-04 | 0001628280-26-052645 | gicform99106302026.htm |
| 8-K + Ex-99.1 (FY2025 release) | 2026-02-24 | 2026-02-24 | 0001628280-26-011155 | gicform99112312025.htm |
| 10-K FY2024 | 2024-12-31 | 2025-02-26 | 0000945114-25-000012 | gic-20241231.htm |
| 10-K FY2023 | 2023-12-31 | 2024-03-12 | 0000945114-24-000016 | gic-20231231.htm |
| 10-K FY2022 | 2022-12-31 | 2023-02-23 | 0000945114-23-000019 | gic-20221231.htm |
| 10-K FY2021 | 2021-12-31 | 2022-03-17 | 0000945114-22-000009 | gic-20211231.htm |
| 10-K FY2020 | 2020-12-31 | 2021-03-18 | 0000945114-21-000010 | syx-20201231.htm |
| 10-K FY2019 | 2019-12-31 | 2020-03-13 | 0000945114-20-000008 | a123119systemax10-k.htm |
| 10-K FY2018 | 2018-12-31 | 2019-03-14 | 0000945114-19-000013 | a123118systemax10-k.htm |
| 10-K FY2017 | 2017-12-31 | 2018-03-15 | 0001628280-18-003257 | a123117systemax10-k.htm |

**Sovereign.** U.S. Department of the Treasury, *Daily Treasury Par Yield Curve Rates*,
`daily-treasury-rates.csv` for 2026, retrieved 2026-08-31. **30 Yr = 5.25% at 2026-08-31.**
Adjacent: 5.22 (08-28), 5.19 (08-27), 5.18 (08-26), 5.17 (08-25), 5.23 (08-24).
*Ladder note: `fred.stlouisfed.org/graph/fredgraph.csv?id=DGS30` was attempted six times
across two sessions and returned `TimeoutError` / `RemoteDisconnected` every time. The
Treasury file used instead is the **issuing authority itself** and carries the same series
(FRED DGS30 IS the Treasury 30-year constant maturity); the four overlapping observations
above reproduce the ALG run's FRED figures exactly, so the substitution is verified, not
assumed. This is a step UP the evidence ladder, not down.*

**Price.** $39.10, 2026-08-31, via aggregator — **live quote only, flagged**.

**Cross-checks against the filed statement (protocol 4).**
1. **FY2025 net cash provided by operating activities from continuing operations = $77.7M**,
   identical in (a) the filed Consolidated Statements of Cash Flows, (b) MD&A "Historical
   Cash Flows" table, (c) MD&A Operating Activities narrative, and (d) the XBRL tag
   `NetCashProvidedByUsedInOperatingActivitiesContinuingOperations`.
2. **Q2 2026 operating income $49.3M and the $21.1M IEEPA tariff refund inside it**,
   identical in the 10-Q condensed statements, the 10-Q MD&A highlights, and the Ex-99.1
   press release's own non-GAAP reconciliation.

---
## §2 — THE FILED SERIES USED (all $ millions, from each year's own 10-K / XBRL)

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Net sales | 753.1 | 791.8 | 896.9 | 946.9 | 1029.0 | 1063.1 | 1166.1 | 1274.3 | 1315.9 | **1379.1** |
| Gross profit | 238.2 | 273.2 | 307.7 | 325.7 | 356.9 | 374.3 | 421.2 | 435.8 | 452.0 | **490.2** |
| Gross margin | 31.6% | 34.5% | 34.3% | 34.4% | 34.7% | 35.2% | **36.1%** | 34.2% | 34.3% | 35.5% |
| Operating income | 8.0 | 45.7 | 61.7 | 66.1 | 84.1 | 88.0 | **105.2** | 96.5 | 80.5 | 97.6 |
| Operating margin | 1.06% | 5.77% | 6.88% | 6.98% | 8.17% | 8.28% | **9.02%** | 7.57% | 6.12% | 7.08% |
| Net income | −32.6 | 40.4 | 224.7 | 48.5 | 65.4 | 103.3 | 78.8 | 70.7 | 61.0 | 72.1 |
| **OCF, continuing ops** | −30.2 | 44.1 | 9.8 | 70.3 | 67.3 | 47.6 | 49.8 | **112.0** | 50.4 | 77.7 |
| SBC | 1.6 | 1.6 | 0.9 | 5.4 | 4.7 | 2.9 | 4.5 | 3.0 | 2.8 | 7.4 |
| D&A | 4.5 | 4.6 | 4.5 | 4.1 | 4.1 | 3.7 | 3.9 | 6.4 | 7.6 | 7.7 |
| Depreciation only | 3.8 | 3.6 | 3.5 | 3.9 | 3.9 | 3.5 | 3.7 | 4.3 | 4.4 | 4.6 |
| Capex | 2.2 | 2.5 | 4.5 | 6.9 | 2.7 | 3.4 | 7.4 | 3.9 | 3.8 | 3.1 |
| Shareholders' equity | 214.4 | 211.8 | 137.7 | 175.5 | 106.8 | 153.6 | 210.4 | 255.2 | 281.1 | 313.2 |
| Total assets | 566.1 | 551.4 | 530.0 | 396.9 | 374.9 | 405.0 | 455.2 | 513.4 | 520.7 | 580.8 |
| Cash | — | — | 295.4 | 97.2 | 22.4 | 15.4 | 28.5 | 34.4 | 44.6 | 67.5 |
| Basic EPS | −0.88 | 1.09 | 6.03 | 1.29 | 1.72 | 2.73 | 2.07 | 1.85 | **1.59** | 1.86 |

**Pre-2020 caution.** 2016–2019 include the discontinued European technology and NATG
businesses (France sold 2018; the $224.7M FY2018 net income is overwhelmingly the France
disposal gain). The continuing-operations OCF line is used throughout precisely to strip
this. Nothing in the run's central case rests on a pre-2019 figure.

### Derived returns (identical formulas throughout)

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Return on unlev. net tangible operating assets [E2-43] | 64.4% | 66.9% | 48.4% | 49.7% | 50.7% | 39.0% | **43.6%** |
| Pre-tax return on total invested capital incl. goodwill | 27.9% | 44.6% | 39.1% | 34.8% | 28.4% | 22.8% | **24.3%** |
| Net income ÷ average equity | 31.0% | 46.3% | 79.3% | 43.3% | 30.4% | 22.7% | **24.3%** |
| Capex ÷ revenue | 0.73% | 0.26% | 0.32% | 0.63% | 0.31% | 0.29% | **0.22%** |
| Capex ÷ depreciation | 1.77x | 0.69x | 0.97x | 2.00x | 0.91x | 0.86x | **0.67x** |

*Denominators, FY2025: unleveraged net tangible operating assets = net PP&E 18.5 +
inventories 174.6 + trade receivables 139.6 − trade payables 108.7 = **$224.0M**. Total
invested capital = total assets 580.8 − total current liabilities 178.5 + short-term debt
0.0 = **$402.3M**. Average equity = (281.1 + 313.2)/2 = **$297.15M**.*

---
## §3 — THE COMPETITOR ROW [E3-28]

**Peers taken: three.** W.W. Grainger, Fastenal and MSC Industrial are the three US-listed
MRO distributors GIC's own Item 1 names as competitors. **No peer filing was unavailable**,
so the moat class is **not PROVISIONAL** and the row is **not UNRESEARCHED**. The industry
has more participants — **Uline** (private, named first by GIC), **Amazon Business** (not
separately reported inside AMZN), Motion Industrial/Genuine Parts, Applied Industrial, HD
Supply (inside HD) — and the four names taken are the four whose US filings permit the
identical computation. Uline and Amazon Business are named and their absence stated.

### Sources

| company | CIK | form | FYE used | filed | accession |
|---|---|---|---|---|---|
| **Global Industrial (GIC)** | 945114 | 10-K | **2025-12-31** | 2026-02-27 | 0001628280-26-012945 |
| **W.W. Grainger (GWW)** | 277135 | 10-K | **2025-12-31** | 2026-02-19 | 0000277135-26-000011 |
| **Fastenal (FAST)** | 815556 | 10-K | **2025-12-31** | 2026-02-05 | 0000815556-26-000009 |
| **MSC Industrial (MSM)** | 1003078 | 10-K | **2025-08-30** (52 wks) | 2025-10-23 | 0001003078-25-000123 |

*MSM's most recent **completed and filed** fiscal year ends 2025-08-30; its FY2026 10-K is
not yet filed, so the MSM column is four months staler than the December filers. Stated,
not hidden.*

### The row

| Metric, most recent filed fiscal year | **GIC** | **Grainger** | **Fastenal** | **MSC Industrial** |
|---|---|---|---|---|
| Fiscal year end | Dec-2025 | Dec-2025 | Dec-2025 | **Aug-2025** |
| Net sales | **$1,379.1M** | $17,942M | $8,200.5M | $3,769.5M |
| GIC as a multiple of | — | **1/13.0** | **1/5.9** | **1/2.7** |
| **Gross margin** | **35.54%** | 39.06% | **45.01%** | 40.75% |
| Gross margin, prior year | 34.35% | 39.36% | 45.08% | 41.16% |
| **Operating margin** | **7.08%** | 13.91% *(15.00% adj.)* | **20.19%** | 8.00% *(8.29% adj.)* |
| **Return on unlev. net tangible operating assets [E2-43]** | **43.57%** | 41.39% *(44.64% adj.)* | 43.48% | 25.36% |
| **Pre-tax ROIC incl. goodwill** *(TA − TCL + ST debt)* | **24.26%** | 34.90% *(37.65% adj.)* | **37.95%** | 14.71% |
| **Pre-tax ROIC** *(total debt + total equity)* | **31.16%** | 37.64% *(40.59% adj.)* | **40.69%** | 16.02% |
| **Net income ÷ average equity** | **24.26%** | **48.10%** | 33.29% | 14.34% |
| Goodwill + intangibles ÷ total assets | 11.07% | 6.97% | *n/d, ≤2.77%* | 32.86% |
| Total debt ÷ total equity, excl. leases | **0.00x** | 0.60x | 0.03x | 0.35x |
| Total debt ÷ total equity, incl. operating leases | 0.33x | 0.69x | 0.11x | 0.39x |
| **Revenue growth, latest year** | **+4.80%** | +4.51% | **+8.67%** | −1.35% |
| Cash dividends ÷ net income | 55.9% | 24.9% | 79.8% | 95.1% |
| Capex ÷ revenue | **0.22%** | 3.81% | 2.99% | 2.46% |
| Capex ÷ depreciation | **0.67x** | 4.00x | 1.46x | 1.29x |
| Operating cash flow | $77.8M | $2,015M | $1,295.9M | $333.7M |
| **Discloses price/volume split?** | **NO** | NO | **YES** | **YES** |
| **Discloses units?** | **NO** | NO | partial (site/device counts) | NO |
| Names Amazon in its 10-K? | **YES** | no | no | no |
| SKUs offered | *"hundreds of thousands"* | 1.5M stocked; **Zoro ~13M**; MonotaRO ~29M | *not disclosed* | **~2.5M active** |
| Distribution / selling footprint | **5 primary US DCs + 1 Canada** (2.8M sq ft) | 21 US DCs + **245 US branches** + 75 onsite; ~28.7M sq ft | 19 DCs + **1,595 branches**, 25 countries; 136,638 installed FMI units | 5 CFCs + 9 RICs + 38 warehouses |

**Adjustments disclosed:** Grainger's FY2025 operating income carries a **$196M one-time UK
exit loss** (Cromwell divestiture $186M + Zoro U.K. closure $10M); the filing's own adjusted
operating earnings are $2,691M. MSM's adjusted figure removes restructuring. Both are shown
so the comparison is not flattered in GIC's favour by a peer's bad year. **Fastenal does not
disclose goodwill anywhere** — no balance-sheet line, no XBRL fact; goodwill plus intangibles
sit inside "Other assets" of $140.2M, which is a **ceiling (2.77%), not a figure**. Flagged,
not guessed.

### What the row says

1. **GIC earns the LOWEST gross margin of the four** — 35.5% against 39.1%, 40.8% and 45.0%.
2. **GIC earns the LOWEST operating margin of the four** — 7.08% against 8.00%, 13.91% and
   20.19%. MSM's 8.00% is its own worst year in a decade and it still beats GIC.
3. **GIC earns the HIGHEST return on unleveraged net tangible operating assets** — 43.6%,
   ahead of Fastenal's 43.5%, Grainger's 41.4% and MSM's 25.4%. **This is the one row GIC
   wins and it is real.** It is the arithmetic consequence of $18.5M of net PP&E on $1.38bn
   of revenue — GIC leases everything and owns almost nothing.
4. **GIC is third of four on return on TOTAL invested capital including goodwill** — 24.3%
   pre-tax against Fastenal's 38.0% and Grainger's 34.9%, ahead only of MSM's 14.7%. This is
   the metric that decided ITW, CSL and HD, run identically, and it puts GIC well behind the
   two healthy peers.
5. **The capital-light structure is not proprietary and the peer row proves it.** Grainger's
   **Endless Assortment** segment (Zoro US + MonotaRO Japan) is the same business model:
   FY2025 revenue **$3,625M, +15.7%**, gross margin **29.93%**, segment operating margin
   **9.52%** (9.79% adjusted), operating earnings +37% adjusted. Grainger's Japan revenue of
   $2,173M is essentially all MonotaRO, which implies **Zoro US at roughly $1.4bn — about the
   size of all of Global Industrial** — offering ~13 million products against GIC's "hundreds
   of thousands", on a gross margin **5.6 points below GIC's**, earning an operating margin
   **2.4 points above GIC's**, growing **three times as fast**. *(The Zoro-alone revenue is
   my inference from the geography table; Grainger does not break Zoro out. Labelled as
   inference.)*
6. **The [E4-55] disclosure gap is comparative, not merely absent.** Fastenal publishes
   *"Changes in product pricing resulted in **170 to 200 basis points of growth in net sales
   in 2025**"* and *"higher **unit sales**"*. MSC publishes a dollar bridge: *"$51.4 million
   decrease in net sales was comprised of **$88.1 million of lower sales volume** … partially
   offset by **$21.6 million from improved pricing**"*. **GIC publishes neither** — only
   *"benefiting from price capture … and volume improvement"* and *"gains in both volume and
   price."* Two of three comparable filers publish what GIC withholds.
7. **The row's limit [E3-61]:** it shows position, not conduct. Fastenal's 20% operating
   margin comes partly from a vending/on-site model GIC has never attempted; whether GIC
   *could* is a judgment about people the row cannot make.

### Verbatim competition language, all four

**GIC**, Item 1 *Competition and Other Market Factors*:
> "The market for the sale of industrial products in North America is **highly fragmented**
> and is characterized by multiple distribution channels such as small dealerships, direct
> mail distribution, internet-based resellers, large warehouse stores and retail outlets.
> **We face competition from large diversified MRO distributors such as Uline Inc, Grainger
> Inc., MSC Industrial Direct Inc., Fastenal Inc., and other large retailers, including
> Amazon.** … Many purchasers begin sourcing products via search engine or mobile
> application… **In the industrial products market, customer purchasing decisions are
> primarily based on price, product selection, product availability, level of service,
> access to open account terms, and convenience.**"

**GIC**, Item 7, Financial Condition:
> "We expect that past performance may not be indicative of future performance due to **the
> competitive nature of our business where the need to adjust prices to gain or hold market
> share is prevalent.**"

**Grainger**, Item 1A:
> "Grainger competes in a variety of ways, including **product assortment and availability,
> services offered to customers, pricing, purchasing convenience** and the overall experience
> Grainger offers." *(Amazon: zero occurrences in the GWW 10-K.)*

**Fastenal**, Item 1:
> "**We believe the principal competitive factors affecting the markets for our products, in
> no particular order, are customer service, price, convenience, product availability, and
> cost saving solutions.**" … "Recent years have seen the emergence of **eBusiness solutions
> … it also has introduced non-traditional web-based competitors into the marketplace.**"
*(Amazon: zero occurrences.)*

**MSC**, Item 1A:
> "We also face substantial competition in the online distribution space that competes with
> price transparency. **Increased competition from online retailers (particularly those major
> internet providers who can offer a wide range of products and rapid delivery), and the
> adoption by competitors of aggressive pricing strategies or sales methods, could cause us
> to lose market share or reduce our prices, adversely affecting our sales, margins, and
> profitability.**" *(Amazon: zero occurrences.)*

**Note the asymmetry.** GIC is the only one of the four that names Amazon. Its competitive-
factor sentence is nearly word-identical to MSC's, with *"access to open account terms"*
added and *"technical support relationship"* removed — i.e. GIC's stated differentiator
against a competitor list it shares is **credit terms**.

---
## §4 — THE DIVIDEND RECORD, REGULAR VERSUS SPECIAL

Reconstructed from each year's own 10-K MD&A Financing Activities narrative and Item 5, and
tied to the XBRL `CommonStockDividendsPerShareDeclared` total for every year. **Every line
reconciles exactly.**

| year | regular/sh | special/sh | **total declared** | XBRL total | cash paid ($M) |
|---|---|---|---|---|---|
| 2016 | 0.10 | — | 0.10 | 0.10 ✓ | 3.7 |
| 2017 | 0.35 | **1.50** (Dec-2017) | 1.85 | 1.85 ✓ | 13.0 |
| 2018 | 0.44 | **1.00** (Jun-2018) + **6.50** (Dec-2018) | 7.94 | 7.94 ✓ | 109.3 |
| 2019 | **0.48** | — | 0.48 | 0.48 ✓ | 261.6 |
| 2020 | 0.56 | **1.00** (Feb-2020) + **2.00** (Dec-2020) | 3.56 | 3.56 ✓ | 134.3 |
| 2021 | 0.64 | **1.00** (Dec-2021) | 1.64 | 1.64 ✓ | 62.5 |
| 2022 | 0.72 | — | 0.72 | 0.72 ✓ | 27.6 |
| 2023 | 0.80 | — | 0.80 | 0.80 ✓ | 30.6 |
| 2024 | 1.00 | — | 1.00 | 1.00 ✓ | 38.4 |
| 2025 | 1.04 | — | 1.04 | 1.04 ✓ | 40.3 |
| **2026 annualised** | **1.12** | — | 1.12 | — | ~43 (10-K's own estimate) |

### Owner earnings and dividend payout, year by year

Owner earnings = continuing-operations OCF − SBC − (c). Both ends of the (c) band shown.
**Note the band is inverted for GIC** — D&A exceeds capex, so the D&A end is the lower.

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| OCF, continuing ops | 70.3 | 67.3 | 47.6 | 49.8 | **112.0** | 50.4 | 77.7 |
| − SBC | 5.4 | 4.7 | 2.9 | 4.5 | 3.0 | 2.8 | 7.4 |
| **OE, (c) = D&A** | **60.8** | **58.5** | **41.0** | **41.4** | **102.6** | **40.0** | **62.6** |
| OE, (c) = capex | 58.0 | 59.9 | 41.3 | 37.9 | 105.1 | 43.8 | 67.2 |
| Regular dividends paid | 18.1 | ~21.0 | ~24.2 | 27.6 | 30.6 | 38.4 | 40.3 |
| **Payout of single-year OE (D&A end)** | 29.8% | 35.9% | 59.0% | 66.7% | 29.8% | **96.0%** | 64.4% |

*(2020 and 2021 regular-dividend cash derived as declared rate × basic weighted shares
[$0.56 × 37.5M; $0.64 × 37.8M], because those years' filed cash-flow lines combine regular and
special payments. All other cells are filed figures. 2026 run rate: $1.12 × 38,108,341 =
**$42.7M**, against the five-year-mean bottom boundary of $57.5M = **74.2%**.)*

Five-year rolling constructions, on windows every year of which is post-disposal:

| window ending | window | mean OCF | − SBC | − D&A | **bottom-boundary OE** | regular dividends | **payout** |
|---|---|---|---|---|---|---|---|
| **FY2023** *(earliest fully clean)* | 2019–2023 | 69.40 | 4.10 | 4.44 | **$60.9M** | $30.6M | **50.3%** |
| **FY2025** | 2021–2025 | 67.50 | 4.12 | 5.86 | **$57.5M** | $40.3M | **70.1%** |
| FY2025, at the 2026 run rate | 2021–2025 | — | — | — | $57.5M | $42.7M | **74.2%** |

**Six specials, $13.00 a share, all between December 2017 and December 2021. None declared
in the four and a half years since.** The FY2018 10-K states the $6.50 special "resulted in
a total cash outlay of $243.5 million and was **essentially funded by the sale of our France
operations**" — an asset-sale distribution, not an earnings distribution.

Regular-only growth:

| window | rate |
|---|---|
| FY2018 $0.44 → 2026 $1.12 (8y) | **+12.39%/yr** |
| FY2019 $0.48 → 2026 $1.12 (7y) | **+12.87%/yr** |
| FY2020 $0.56 → 2026 $1.12 (6y) | **+12.25%/yr** |
| FY2019 $0.48 → FY2025 $1.04 (6y) | +13.75%/yr |
| **Including specials, 2020 $3.56 → 2026 $1.12 (6y)** | **−17.53%/yr** |

---
## §5 — INTERNAL CONTROL RECORD, DATED

| date public | event |
|---|---|
| 2023-02-23 (FY2022 10-K) | E&Y adverse ICFR opinion **for FY2022 and FY2021** — ITGC material weaknesses |
| 2024-03-12 (FY2023 10-K) | E&Y adverse ICFR opinion **for FY2023 and FY2022**; "has not maintained effective internal control … as of December 31, 2023" |
| 2024-07-30 (Q2 2024 10-Q) | Indoff control assessment completed; **Indoff ITGCs ineffective** |
| 2025-02-26 (FY2024 10-K) | E&Y adverse ICFR opinion **for FY2024** |
| 2026-02-27 (FY2025 10-K) | E&Y adverse ICFR opinion **for FY2025**. Global Industrial's own weaknesses **remediated**; Indoff's remain. Management: "the Company **expects to complete these efforts in the second quarter of 2026**" |
| 2026-08-04 (Q2 2026 10-Q) | "as of June 30, 2026, the Company's **disclosure controls and procedures were not effective** due to material weaknesses identified at its subsidiary, Indoff LLC (Indoff), **which represents approximately 12% of revenue** … change management, segregation of duties, and privileged access." **The self-imposed Q2-2026 remediation deadline was missed.** |

Offsetting, and it must be stated: **E&Y issued an unqualified opinion on the financial
statements in every one of those years**, and every filing states the weaknesses "did not
result in any identified misstatements … and there were no changes to previously issued
financial results."

---
## §6 — OWNERSHIP, CONTROL AND RELATED PARTIES (DEF 14A 2026-04-22)

- **Controlled company.** "Global Industrial is a 'controlled company' in that **more than
  50% of the voting stock for the election of directors** … is owned by certain members of
  the Leeds family … As a 'controlled company,' Global Industrial is **exempt from the NYSE
  requirement that listed companies have a majority of independent directors.**"
  Board is 8 members, **4 independent**.
- **Stockholders Agreement:** parties "beneficially owned **24,775,188 shares** … constituting
  approximately **64.8% of the shares outstanding**", and the agreement **prohibits sale
  without majority consent** of the parties, with drag-along and registration rights.
- **Richard B. Leeds** — Executive Chairman (joined 1982; Chairman/CEO 1995–2016);
  **Bruce Leeds** and **Robert Leeds** — Vice Chairmen since 1995. Three brothers, all
  officers and directors.
- **Related-party lease:** Port Washington NY headquarters leased since 1988 from an entity
  owned by the three Leeds brothers; triple net; **lease payments $1,224,143 in FY2025**.
  Reviewed under the written related-party policy.
- **Only 5% holder disclosed besides the Leeds Group: FMR LLC, 3,743,695 shares, 9.78%**
  (13G/A filed 2026-02-05).
- **CEO: Anesa T. Chaibi, effective 2025-02-17 — eighteen months in post at this run date.** Base
  $1,000,000 (2026: $1,040,000); target bonus 100% of base, cap 160%; annual equity ≥125% of
  base. Predecessor departed August 2024; **Richard B. Leeds served as Interim CEO
  2024-08-09 to 2025-02-17** and was awarded a **$1,000,000 one-time special cash bonus on
  2025-08-07**, paid ~2025-08-15, for that service. He takes no non-equity incentive
  compensation and **no equity awards**.
- **Incentive metrics:** annual bonus on **Adjusted Operating Income** (45–70% weight) and
  **Net Sales** (25–30%), plus Individual Objectives (0–30%). "Adjusted operating income is
  defined as operating income adjusted for unusual or nonrecurring items **as determined by
  our Compensation Committee**." PSUs cliff-vest on **three-year cumulative Adjusted
  Operating Income**. **There is no return-on-capital metric anywhere in the plan.**
- **2025 outcome:** Adjusted Operating Income **116% of target → 137.5% payout**; Net Sales
  **99% → 97.5% payout**; CEO weighted payout **126%**.
- **Delinquent Section 16(a):** one late Form 4 (Ms. Hughes).
- **Auditor:** Ernst & Young LLP, **since 2005**.

---
## §7 — THE 2026 ONE-OFF, QUANTIFIED

FY2025 10-K Note 17, Subsequent Event:
> "On **February 20, 2026**, the U.S. Supreme Court ruled in *Learning Resources, Inc. v.
> Trump*, that the International Emergency Economic Powers Act of 1977 (IEEPA) **does not
> authorize the President to impose tariffs.** … the Company paid a material amount on items
> imported. … the amount and timing of a potential refund … is **inestimable**."

Q2 2026 Ex-99.1:
> "the Company recorded approximately **$26.2 million associated with refunds of IEEPA
> tariffs previously paid**, comprising **$21.1 million related to cost of sales**, $4.0
> million reduction to inventory not yet sold and $1.1 million of interest income. …
> **The Company does not expect any future refunds of IEEPA tariffs assessed to date to be
> material.**"

| | as reported | **ex-refund** | prior year |
|---|---|---|---|
| Q2 2026 gross margin | 40.2% | **34.7%** | 37.1% |
| Q2 2026 operating income | $49.3M | **$28.2M** | $33.5M *(−15.8%)* |
| Q2 2026 diluted EPS (cont.) | $0.96 | **$0.54** | $0.65 *(−16.9%)* |
| H1 2026 gross margin | 37.6% | **34.8%** | 36.0% |
| H1 2026 operating income | $69.9M | **$48.8M** | $51.7M *(−5.6%)* |
| H1 2026 revenue | $737.0M | $737.0M | $679.9M *(+8.4%)* |

**The company published this reconciliation itself, unprompted, and its own non-GAAP table
removes a BENEFIT rather than a charge** — the [E2-69] deviation-toward-candor case, and the
opposite of the usual [E4-29] pattern. It also volunteers that the ex-refund gross margin was
*"in line with historical performance"*, deflating its own headline.

---
## §8 — DISCLOSURE ABSENCES, NAMED (absence-claim rule)

Each of these was **looked for** in the FY2025 10-K, the Q2 2026 10-Q, the 2026 DEF 14A and
both earnings releases, and **not found**. Worded as "no instance found," never "does not
exist."

| sought | result |
|---|---|
| Unit-volume series | **No instance found.** No units, no shipments, no order counts. |
| Price-vs-volume split, quantified | **No instance found.** Qualitative only. Two of three peers publish it. |
| SKU count, precise | **No instance found** — "hundreds of thousands". |
| Revenue by customer size or type | **No instance found.** Only US/Canada geography. |
| Public numeric guidance (revenue, margin, EPS) | **No instance found** in either earnings release. |
| EBITDA or Adjusted EBITDA | **No instance found** anywhere. |
| Restructuring charges | **No instance found** in FY2023–FY2025. |
| Preferred stock outstanding | **None issued** (25M authorised, "issued none"). |
| Pension plan | **No instance found** — no defined-benefit plan. |
| Customer above 10% of revenue | **No instance found.** No supplier above 10% of purchases either. |
