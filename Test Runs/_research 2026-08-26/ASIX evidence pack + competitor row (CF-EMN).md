# ASIX (AdvanSix) — evidence pack — 2026-08-30
Supports `Test Runs/2026-08-30 Run - ASIX (AdvanSix) v4.1.md`. All filed figures
hand-checked against the converted filing text on disk (`ASIX_10K_FY2025.txt`,
`ASIX_10Q_Q2_2026.txt`); XBRL series from `ASIX_companyfacts.json`.

## Documents on disk (this folder)
| doc | period | filed | accession |
|---|---|---|---|
| FY2025 Form 10-K (`ASIX_10K_FY2025.htm`) | FY ended 2025-12-31 | 2026-02-20 | **0001673985-26-000008** |
| Q2 2026 Form 10-Q (`ASIX_10Q_Q2_2026.htm`) | period 2026-06-30 | 2026-08-07 | **0001673985-26-000049** |
| DEF 14A 2026 (`ASIX_DEF14A_2026.htm`) | annual meeting 2026-06-22 | 2026-04-29 | 0001673985-26-000022 |
| 8-K refinancing (`ASIX_8K_2026-08-17.htm`) | closing 2026-08-14 | 2026-08-17 | 0000950157-26-000916 |
| 8-K annual meeting (`ASIX_8K_2026-06-23.htm`) | vote 2026-06-22 | 2026-06-23 | 0001673985-26-000040 |
| 8-K + Ex-99.1 production update (`ASIX_8K_2024-01-19_ex991.htm`) | event Jan 2024 | 2024-01-19 | 0001673985-24-000005 |
| XBRL companyfacts (`ASIX_companyfacts.json`) | through Q2 2026 | pulled 2026-08-30 | — |

Auditor: PricewaterhouseCoopers LLP (ratified 2026-06-22, 8-K). CEO: Erin N. Kane
(president & CEO since the 2016-10-01 Honeywell spin). CFO: Christopher Gramm,
**Interim** CFO effective 2025-07-09 (FY2025 10-K, Recent Developments).

## Price / cap (verified)
- Price **$16.49**, NYSE close **2026-08-28** (Yahoo chart API — aggregator, live quote
  only, flagged). 52wk $14.10–26.73.
- Shares: **27,001,186** outstanding at 2026-07-31 (Q2 2026 10-Q cover).
- **Market cap ≈ $445.3M.** Operator sweep ~$446M — **verified**.
- Dividend $0.16/qtr = $0.64/yr → **3.9%** at the quote. Initiated 2021-09-28; last
  raise Q3 2023 ($0.145 → $0.16); flat since (10-K line 487-488).

## Annual series ($M — filed 10-K statements, XBRL cross-checked)
| FY | Rev | NI | OCF | capex | D&A | SBC | ROE (avg eq) |
|---|---|---|---|---|---|---|---|
| 2021 | 1,684.6 | 139.8 | 218.8 | 56.8 | 65.3 | 11.3 | 26.7% |
| 2022 | 1,945.6 | 171.9 | 273.6 | 89.4 | 69.4 | 10.3 | 25.7% |
| 2023 | 1,533.6 | 54.6 | 117.5 | 107.4 | 73.0 | 8.3 | 7.4% |
| 2024 | 1,517.6 | 44.1 | 135.4 | 133.7 | 76.2 | 7.9 | 5.8% |
| 2025 | 1,522.2 | 49.3 | 122.9 | 116.4 | 79.7 | 6.8 | 6.2% |
| H1-26 | 825.5 | **(12.3)** | **(5.3)** | 56.7 | 41.8 | 3.9 | — |

Equity (10-K instants): 444.1 (2020) → 601.2 → 738.2 → 739.2 → 774.6 → **815.2**
(2025-12-31); **796.9** at 2026-06-30 (10-Q).

**Cross-check 1 (OCF):** filed FY2025 cash-flow statement reads "Net cash provided by
operating activities | 122,863 | 135,413 | 117,550" (10-K text line 871) = XBRL
122.9/135.4/117.5. Ties.
**Cross-check 2 (EPS):** NI $49,286K ÷ 26,901,046 basic wtd shares = $1.83 = filed
basic EPS (10-K non-GAAP reconciliation table). Ties.

H1 2025 comparatives (10-Q): OCF +32.6, capex 62.3, NI +54.7. TTM (Jul-25→Jun-26,
derived, labelled estimate): OCF ≈ 85.0, capex ≈ 110.8, D&A ≈ 83e.

## The pricing mechanism — the subject's own words (Q2 evidence)
- 10-K line 519 (MD&A): "**We produce and sell caprolactam as a commodity product**
  and produce and sell our Nylon 6 resin as both a commoditized and differentiated
  resin product. **Our results of operations are primarily driven by production volume
  and the spread between the sales prices of our products and the costs of the
  underlying raw materials** built into market-based and value-based pricing models.
  The global prices for nylon resin typically track as a spread over the price of
  caprolactam, which in turn tracks as a spread over benzene…"
- 10-K line 191: "**Global prices for ammonium sulfate are influenced by several
  factors including the price of urea**, the most widely used source of nitrogen-based
  fertilizer in the world." Line 213/518: "**Sales in our Plant Nutrients business line
  are priced on a freely negotiated basis.**"
- 10-K line 522 (10-Q line ~537): acetone "the price of which is influenced by its own
  supply and demand dynamics… also… the underlying move in propylene input costs."
- 10-K line 303 (risk factor — the [E2-58] equation in the filer's own words):
  "**Periods of high demand, tight supply and increasing operating margins tend to
  result in increases in capacity and production until supply exceeds demand,
  generally followed by periods of oversupply and declining prices.**"
- Customer contracts: "formula-based pass-through pricing tied to key feedstock
  materials" (line 720); "formula-based price agreements with customers which
  structurally pass through increases or decreases in raw material costs" (line 213).

## Utilization / supply state (10-K lines 188-194, FY2025)
- Nylon 6: global capacity utilization **≈56%** in 2025; China + rest of Asia ≈ 80% of
  world capacity. "estimated operating rates out of China remain at multi-year highs
  resulting in continued nylon exports to other regions."
- Caprolactam: ≈74% global; >80% US and China; **55-65% Europe / rest of Asia**.
- Phenol/acetone: ≈70% global, "low to mid 60%" US, "significant additional capacity
  additions in Asia, particularly China."
- North America demand "weak, with continued softness in building and construction,
  food packaging and engineering plastics."

## Cost-position claims (10-K lines 149-150, 170, 202)
- "world's **lowest cost producer of caprolactam**" (their claim, Item 1); Hopewell
  "one of the world's largest single-site producers of caprolactam"; "the world's
  **largest single-site producer of ammonium sulfate**."
- Mechanism claimed: vertical integration (phenol/ammonia/oleum), scale ("spread fixed
  and overhead costs across more pounds"), US natural gas, high utilization.
- AS co-product ratio ~4 lbs per lb caprolactam vs ~2 lbs for co-product peers.
- SUSTAIN: targeting ~75% of AS converted to granular by end-2026.

## Trade-remedy regime ([E2-59] material)
- Ammonium sulfate: "significant anti-dumping duties in place in the U.S. against
  Chinese ammonium sulfate, **subject to customary sunset review in 2028**" (line 191).
- Acetone: AD orders (Belgium, Singapore, South Africa, South Korea, Spain) extended
  another five years — ITC affirmative determinations January 2026 (10-K/10-Q Recent
  Developments).

## Outage / interruption record (single-site risk)
- Risk factor (line 317): unplanned downtime or material disruptions "**have occurred
  in the past**… At the time of any unplanned interruption… we may not have enough
  intermediate chemical inventory… to offset production losses."
- **2024-01-19 8-K + Ex-99.1 (worked example):** "process-based operational disruption"
  at Frankford; phenol/acetone AND Hopewell AND Chesterfield production reduced;
  "approximately **$18 to $23 million unfavorable impact to pre-tax income** in the
  first quarter of 2024" (fixed-cost absorption, lost sales, replacement product).
- **June 2019 PES refinery fire** (cumene supplier): multi-year business-interruption
  claim; final omnibus settlement Jan 2025, **$26M received Q1 2025**; ~$39M aggregate
  since claim (10-K line 535).
- **January 2026 winter storm**: H1-26 COGS +3% "utility costs and winter storm
  related expenses" (10-Q line 557).
- Q2-26: "lower production rates and timing of plant turnaround spend" ~3% of COGS.

## H1 2026 deterioration (10-Q)
- Q2-26 volume **−14.8%** (six-month −4.8%) "driven primarily by lower in-season Plant
  Nutrients sales as a result of reduced grower application of nutrients"; price
  +17.5% mostly raw-material pass-through on higher benzene/propylene/sulfur.
- H1-26: pre-tax **−$14.0M**, NI **−$12.3M**, OCF **−$5.3M**, capex $56.7M; dividends
  still paid (~$8.7M); revolver $215M → $275M over the half; cash $19.8M → $7.2M.

## Debt / refinancing (8-K 2026-08-17)
- New credit agreement closed **2026-08-14**: $275M revolver + **$150M term loan**,
  both maturing **2031-08-14**, secured by "**substantially all tangible and
  intangible assets**." Drawn at closing: $145M revolver + $150M term = **$295M**,
  cash ~$17M → net debt ≈ **$278M**.
- Pricing SOFR + 1.50-2.50% (2.00% now); commitment fee 0.30%. Term amortization
  2.5%/yr (yr 1), 5%/yr (yrs 2-4), 7.5% (yr 5).
- Covenants: **Consolidated Interest Coverage ≥ 3.00×; Consolidated Leverage ≤ 3.75×**
  (cash netting capped at $75M).
- Debt path: $195M (12/31/24) → $215M (12/31/25) → $275M (6/30/26) → $295M (8/14/26).
- Leverage estimate (labelled): TTM GAAP EBITDA ≈ $73M → ≈3.8×; on the company's
  Adjusted-EBITDA basis (TTM ≈ $85-90M incl. addbacks) ≈ 3.1-3.3×. Thin headroom
  against 3.75× either way; the covenant definition has addbacks — estimate only.

## Capex / (c) evidence
- "**Our operations are capital intensive**" (10-K line 700; risk factor line 329 "Our
  industry is capital intensive"). Capex > D&A in 4 of the last 5 years.
- Capex purposes: "maintain and improve equipment reliability, expand production
  capacity, further improve mix, yield and cost position and comply with
  environmental and safety regulations" — no numeric maintenance/growth split filed.
- 2026 guide: "approximately **$75 million to $95 million**" (line 708) vs D&A ~$80M.
- Proxy: FY2025 FCF (their definition, OCF−capex) **$6.4M**; FY2024 $1.7M.

## Non-GAAP / comp ([E4-29] flag material)
- 10-K MD&A tables: Adjusted EBITDA $156.8M (2025), Adjusted EPS $2.28; excludes SBC,
  "non-recurring, unusual or extraordinary expenses," acquisition amortization, and
  **$7.3M of "strategic advisory and professional fees… including costs associated
  with a transaction that the Company is no longer pursuing"** (2025).
- DEF 14A: 2025 short-term incentive = **Adjusted EBITDA 80%** + Leadership Strategic
  Objectives 20% (FCF metric moved to LTI; threshold payout raised 25% → 50% of
  target). PSUs: cumulative EPS + average annual ROI + TSR modifier (±10%),
  0-200% of target. Say-on-pay passed ~98% (8-K 2026-06-23).
- Headline proxy framing leads with Adjusted EBITDA / Adjusted EPS / FCF.

## Taxes
- Effective rate 2025 ≈ 9.5% (tax $5.1M / pretax $54.4M); 2024 ≈ 3.1%. Driver named
  and quantified in the filing: **IRC §45Q carbon-capture credits ~$9.7M claimed in
  each of 2024 and 2025** (for 2018-2020 periods; LCA approved Nov 2024; ~$18M of
  credits in Taxes receivable at 12/31/25). 2023 ≈ 21%. No unrecognized tax benefits.

## Pension
- AdvanSix Retirement Earnings Plan at 2025-12-31: benefit obligation $98.2M vs plan
  assets $101.2M → **overfunded ≈ $3.0M** (the filed "Under (Over)-Funded status"
  line shows $(3,007)K under the under/(over) sign convention). Immaterial on $797M
  equity. No 2026 funding requirement; $1.1M discretionary contribution July 2026
  (10-Q). Assumptions not fanciful on read — 2025 asset return $15.7M actual.

## Legal / environmental (Q3 conduct read)
- 2013 consent decree (US + Virginia): EPA Dec 2016 notice re self-reported leak
  detection/emissions testing violations at Hopewell — negotiations ongoing (line 466).
- EPA Administrative Compliance Orders on Consent: Feb 2023 and Feb 2024 (risk
  management program, Hopewell); Feb 2024 (stormwater/discharges). EPA-approved work
  plan being implemented; possible penalties (line 468).
- VA DEQ Order by Consent Sept 2025: water discharge violations, civil charge
  **$55,841**; air-emissions allegations still being assessed (line 469).
- Class: HSE compliance matters, several self-reported; no financial-dishonesty
  matter found in the documents read (worded per the absence-claim rule).

## Buyback record
- Life-to-date through 6/30/26: **6,391,880 shares for $195.5M, weighted average
  $30.58** (incl. 1.15M tax-withholding shares); $62.0M authorization remaining;
  **no repurchases under the program since June 2024** (10-Q line 323). Share count
  ~30.5M (2018) → 27.0M (2026-07-31).

## Customer / concentration
- Largest customer Shaw Industries: 9% of H1-26 sales, long-term agreement; top-10
  customers ~40%s (10-Q note). Caprolactam 18% of 2025 sales ($271M); Plant Nutrients
  37% ($564M, +23% yoy); Chemical Intermediates 25% ($377M); Nylon ~21%.

## COMPETITOR ROW (same metric: ROE = NI ÷ avg equity, FY2021-25, filing/XBRL-sourced)
| Company | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr avg | source |
|---|---|---|---|---|---|---|---|
| **AdvanSix** | 26.7 | 25.7 | 7.4 | 5.8 | 6.2 | **14.4** | 10-K series above |
| Eastman Chemical (EMN — alkyl-amines competitor named in 10-K) | 14.6 | 14.6 | 16.9 | 16.1 | 8.1 | **14.1** | SEC XBRL companyconcept, 10-K facts |
| CF Industries (CF — nitrogen fertilizer pricing context) | 41.1 | 95.4 | 34.1 | 27.6 | 36.6 | **46.9** | SEC XBRL; **ProfitLoss incl. NCI ÷ parent equity — overstated; context only** |
| BASF (Monomers segment: caprolactam/PA6) | — | — | — | — | — | — | not separable from conglomerate segment reporting; annual report not pulled — **UNRESEARCHED** |
| UBE Corp (JP caprolactam route peer) | — | — | — | — | — | — | UBE IR English financial reports — **UNRESEARCHED** |
| Highsun Group (CN, largest caprolactam capacity) | — | — | — | — | — | — | **private — no filings exist**; recorded honestly, not retrievable |
| Sinopec / DOMO / Envalior | — | — | — | — | — | — | unsegmented (Sinopec) / private (DOMO, Envalior JV) — no usable same-metric rows |
| Nutrien (NTR — fertilizer context) | — | — | — | — | — | — | SEC filer; XBRL tag misalignment in this session — **UNRESEARCHED** (10-K on EDGAR, ordinary retrieval) |

Row read: ASIX's 5-yr average is manufactured by two boom years; its three
normal-state years (6-7% ROE) sit below the diversified specialty peer and far below
the nitrogen producer — and the H1-26 loss extends the normal-state series downward.
The caprolactam-specific rows are structurally unavailable; the moat-class verdict in
the run does NOT rest on the row (subject's own pricing disclosure decides it), so
the class is not held PROVISIONAL — same treatment as MITSY/SGU precedents.

## Sovereign
- **USD 30-year (DGS30): 5.19% at 2026-08-27**, fetched direct from
  `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS30` on 2026-08-30. Last
  five observations: 8/21 5.27, 8/24 5.23, 8/25 5.17, 8/26 5.18, 8/27 5.19.
