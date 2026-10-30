# Company Run — Standex International Corporation (NYSE: SXI) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. This is a blind run: `PORTFOLIO.md`, the holding reviews,
the resume-state file, the run queue and the prepped reading list were not opened, and no attempt was made to learn
whether anyone holds or wants this name.

**CONTAMINATION, declared:** (1) the session's opening git status listed the names of three other 2026-10-05 run files
(HNI, IOSP, MBUU) and the recent commit subjects named the boxes of four other runs, among them CTS (TOO HARD (WORK) at
Q2), a company used below as a Q2 competitor; its run file was not opened, and every CTS figure below is from CTS's own
10-K data. (2) A directory listing of `Test Runs/` made to confirm that no earlier SXI file existed showed the file names
of the other 2026-10-05 runs; none was opened. (3) The auto-memory index loaded with the session carries a one-line queue
summary ("57 gate-clearers, nothing buyable") that names no company. None of these bears on SXI's facts.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $289.91 (2026-10-05, from `tools/run.py`; **aggregator quote, live quote only, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, Common Stock, par $1.50: **12,119,465** shares (10-K for
  FY ended 2026-06-30, filed 2026-08-14, accession `0001437749-26-027789`; `python Screens/cover_shares.py SXI`). No
  second class; no charter note needed. *Discrepancy recorded, not resolved:* the proxy (DEF 14A filed 2026-09-04,
  accession `0001437749-26-029660`) gives 12,281,465 shares outstanding at the 2026-08-25 record date, about 162,000 more
  than the cover eighteen days earlier; the balance sheet gives 12,054,110 at 2026-06-30. No filing read explains the
  step. The cover count is used, as the protocol directs.
- **Market cap:** $289.91 × 12,119,465 = **$3,513.6M**. With long-term debt $517.95M, less cash $178.73M, plus the $64.0M
  obligation to buy the Narayan minority (paid July 2026, 8-K accession `0001437749-26-022576`): net debt **$403.2M**;
  enterprise value about **$3,916.8M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, 10/02/2026
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4): 10-K FY2026 (filed 2026-08-14, `0001437749-26-027789`): Items 1, 1A, 7, 7A, the
  statements, the segment note. 10-K FY2025 (`0001437749-25-024450`) and FY2024 (`0001437749-24-024465`) fetched; the
  segment notes of the 10-Ks for FY2009 (`0000310354-09-000044`), FY2011 (`0000310354-11-000034`), FY2015
  (`0000310354-15-000025`), FY2018 (`0000310354-18-000016`), FY2021 (`0001437749-21-019845`) and FY2023
  (`0001437749-23-022156`). Proxy 2026 (`0001437749-26-029660`): pay, ownership, incentive metrics. 8-Ks: 2024-10-31
  (Amran/Narayan, `0001437749-24-032685`), 2026-07-02 (Narayan minority, `0001437749-26-022576`), 2026-07-31 with the
  FY2026 release (`0001437749-26-025140`), 2026-05-14 (`0001437749-26-016900`), 2025-11-10 (`0001437749-25-034131`). The
  three 10-K/As of 2025 (`0001437749-25-024609`, `0001437749-25-038746`, `0001437749-25-039046`): a signature-date fix
  and, twice, a clawback-policy exhibit "inadvertently excluded". **No 10-Q was read**: the FY2026 10-K closes at
  2026-06-30 and no later 10-Q has been filed (the next is due about 2026-11); the latest 10-Q, for the quarter to
  2026-03-31 (`0001437749-26-014992`), is superseded by the 10-K. **One figure cross-checked against the filed
  statement:** net cash provided by operating activities from continuing operations, FY2026, **$89,913K** on the filed
  cash-flow statement, against 90 in `tools/run.py` and 89.9 in the XBRL facts; stockholders' equity at 2026-06-30
  **$755,214K** filed against 755 printed. Both agree.
- `python tools/run.py SXI`, arithmetic lines only (Part VII): OCF 93 / 70 / 90 (FY2024-26); D&A 28 / 35 / 39; capex
  20 / 28 / 25. **Defect found:** the tool prints stock pay as **0** in all three years. The filed statements show
  stock-based compensation of **$9,811K, $8,691K and $8,821K** (FY2024, FY2025, FY2026). The tool's owner-earnings
  figures are therefore overstated by about $9M a year and are not used; owner cash is recomputed below from the filed
  statements.

### Owner cash after every real cost, from the filed statements ($M)
Owner cash = operating cash flow from continuing operations − stock pay − all capital spending (Q7 convention: all capex
deducted, depreciation variant shown beside). Interest is inside operating cash flow; the "unlevered" column adds back
interest after a 21% tax (the FY2026 effective rate) so that the cash can be set against today's debt, which is more than
three times the debt of FY2022-24.

| FY (June) | OCF cont. | stock pay | capex | depreciation | interest | **owner cash** | dep. variant | unlevered |
|---|---|---|---|---|---|---|---|---|
| 2022 | 78.1 | 11.2 | 22.0 | 18.0 | 5.9 | **44.9** | 48.9 | 49.6 |
| 2023 | 90.8 | 11.7 | 24.2 | 18.2 | 5.4 | **54.9** | 60.9 | 59.2 |
| 2024 | 93.3 | 9.8 | 20.3 | 18.6 | 4.5 | **63.2** | 64.9 | 66.8 |
| 2025 | 69.6 | 8.7 | 28.3 | 19.2 | 23.9 | **32.6** | 41.7 | 51.5 |
| 2026 | 89.9 | 8.8 | 25.2 | 20.3 | 30.7 | **55.9** | 60.8 | 80.2 |
| **5-yr average** | | | | | | **50.3** | 55.4 | **61.4** |

Sources: 10-K cash-flow statements and equity statements (FY2026 `0001437749-26-027789` for FY2024-26; FY2023
`0001437749-23-022156` for FY2022-23; capex FY2022-23 and stock pay FY2022-23 from the XBRL facts of those filings,
transcription). Owner cash per share (5-yr average): $4.15. **Owner cash yield at $289.91: 1.43%** (levered, on market
cap); 1.57% unlevered on enterprise value; against a sovereign of 5.63%.

What the table does not show, and what moves it: (a) FY2025 carries $21.4M of deal costs; (b) FY2026 operating cash bears
the cash tax on the $57.1M gain from selling Federal Industries, whose proceeds sit in investing (amount not stated in
the filing; not estimated here); (c) the five-year window holds Amran/Narayan's earnings for twenty months only, while
all its debt is in today's balance sheet; (d) capital spending ran 2.8% of sales in FY2026 against management's own
statement that "over the long-term" it will be "approximately 4 to 5% of net sales", and FY2027 capex is guided at
**$45-55M**, about double FY2026's $25.2M and over twice the guided FY2027 depreciation of $18.0-20.5M (10-K FY2026,
Item 7, Capital Expenditures and Capital Structure). (e) $23.9M of FY2026 net income went to the Narayan minority, and
$2.7M was paid to it in cash.

### The balance sheets, FY2013 to FY2026, read before the income account **[M2025-032]**
($M; XBRL first-filed values from the 10-Ks, checked at 2025 and 2026 against the filed balance sheet in
`0001437749-26-027789`.)

| June | sales | cash | receivables | inventory | goodwill | intangibles | LT debt | equity | retained | AOCI |
|---|---|---|---|---|---|---|---|---|---|---|
| 2013 | 701 | 51 | 102 | 85 | 112 | 26 | 50 | 291 | 546 | −65 |
| 2016 | 752 | 122 | 104 | 105 | 157 | 40 | 92 | 370 | 678 | −118 |
| 2017 | 755 | 89 | 127 | 119 | 243 | 103 | 192 | 409 | 717 | −116 |
| 2019 | 792 | 93 | 120 | 89 | 282 | 119 | 198 | 464 | 818 | −137 |
| 2020 | 604 | 119 | 98 | 85 | 271 | 106 | 199 | 462 | 828 | −148 |
| 2021 | 656 | 136 | 110 | 92 | 278 | 99 | 199 | 506 | 852 | −116 |
| 2022 | 735 | 105 | 117 | 105 | 268 | 86 | 175 | 499 | 901 | −153 |
| 2023 | 741 | 196 | 123 | 99 | 265 | 76 | 173 | 607 | 1,027 | −158 |
| 2024 | 721 | 154 | 121 | 87 | 281 | 79 | 149 | 622 | 1,086 | −183 |
| 2025 | 790 | 105 | 173 | 130 | 610 | 226 | 553 | 712 | 1,127 | −165 |
| 2026 | 892 | 179 | 173 | 129 | 582 | 199 | 518 | 755 | 1,215 | −199 |

What the figures say. **Equity against goodwill and intangibles:** purchased goodwill and intangibles went from $138M
(2013) to $360M (2024) to $836M (2025); tangible equity went from about $153M (2013) and $262M (2024) to **about −$26M at
2026-06-30**. The company is now its acquisitions. **Debt:** $50M (2013), about $195M (2017-21), $149M (2024), then
$553M after the October 2024 purchases, $518M at 2026-06-30, with the $64.0M Narayan minority paid in cash in July 2026
on top. **Cash:** $150.6M of the $178.7M is held outside the United States, and the 10-K says repatriation "could have
adverse tax consequences or be subject to capital controls". **Receivables and inventory against sales:** inventory is
steady at 12-16% of sales. Receivables were 14.6% of sales in 2013 and 16-17% in 2017-2024, then 21.9% (2025) and
19.4% (2026). Contract assets (revenue recognised over time and not yet billed, carried in prepaid and other current
assets) rose from $5.9M (2018) to $45.4M (2024), $59.2M (2025) and $44.4M (2026). Receivables plus contract assets: about
16% of sales in 2018, 23% in 2024, 29% in 2025, 24% in 2026. **Retained earnings** rose $669M over thirteen years while
AOCI fell $134M (translation and pension). **Pension:** the US plan is frozen and "not 100% funded under ERISA rules";
$6.6M contributed in FY2026, $4.6M required in FY2027.

What they don't say and can't say: what the grid business earns apart from the reed switches and magnetics (Electronics
is reported whole); whether $781M of goodwill and intangibles is worth what was paid; why the unbilled share of
receivables has risen sixfold since 2018 beyond the over-time recognition the accounting note describes. The rising
receivables-plus-contract-assets line is the kind of balance the rows say to "look twice" at **[M1995-064]**; it is
recorded here as contrary evidence, not as a finding, because Q4 is not reached.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own Standex "if the market closed for five years"
**[M1997-109]**. The quotation of $289.91 "just tells us prices" **[M2006-077]**; what matters is whether the price is "out
of line where the facts and reasoning lead you" **[M2006-077]**. The margin of safety is an attitude here: "if you have to
actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**. Who is paid to tell me: the
company's own release headlines "Record Adjusted EPS" and reports EBITDA and "Net Debt to EBITDA", and the officers'
long-term pay moved to an EBITDA metric for FY2026-28 (Q4 and Q6 would weigh this; both are not reached). The analyst's
habit is to look for "what’s wrong in things because that’s part of investing – looking at what you’re missing"
**[M2025-013]**.

**Contrary evidence, written down as found** **[M1997-127]**, in the order found:
1. `tools/run.py` prints stock pay as zero; the filed figure is $8.8-9.8M a year (above).
2. Organic sales fell **$37.7M (FY2024)** and **$53.8M, or 7.5% (FY2025)**; Electronics organic −8.3% in FY2025 (10-K
   FY2026, Item 7).
3. The 10-K's own risk factor: "many of our businesses experience sales churn as customers seek lower cost suppliers",
   and "The principal methods of competition are industry and design expertise, product performance and technology,
   price, delivery schedule ..." (10-K FY2026, Items 1 and 1A).
4. The 9.9% of Narayan valued at **$27.9M** in the 2024 purchase agreement (8-K `0001437749-24-032685`) was bought for
   **$64.0M** in cash twenty months later (8-K `0001437749-26-022576`); $23.9M of FY2026 net income was attributed to
   the minority and $17.4M more was charged through equity.
5. Tangible equity turned negative after the FY2025 purchases (balance sheets above).
6. Receivables plus contract assets rose from about 16% of sales (2018) to 24-29% (2025-26).
7. The FY2026-28 performance shares moved from ROIC to EBITDA, the proxy saying "ROIC had become less of a prevalent long
   term incentive plan metric within the Company’s peer group, while EBITDA has become more common for growth companies"
   (proxy, `0001437749-26-029660`). The FY2024-26 ROIC award paid 68%.
8. The FY2026 release features "adjusted operating income of $173.3 million" against GAAP operating income of $193.6M
   that includes a $57.1M gain, i.e. $136.5M without it (release, `0001437749-26-025140`).
9. Capex guided to $45-55M for FY2027 against $25.2M spent in FY2026.
10. FY2009: the Electronics and Hydraulics segment's sales fell 27% (84.2 to 61.2) and its operating income 57% (8.1 to
    3.5); consolidated operating income was $6.0M on $607M of sales after a $21.3M impairment; dividends paid fell from
    $0.84 a share (FY2008) to $0.20 (FY2010) (10-K FY2011, selected financial data, `0000310354-11-000034`).
11. Engraving's operating margin fell from 24.1% (FY2017) to 14.3-16.7% (FY2020-23); the combined Engraving &
    Hydraulics segment earned 14.0% in FY2025 and 15.0% in FY2026, with four site closures announced.
12. The proxy's record-date share count exceeds the cover count by about 162,000, unexplained (Step 0).
Found for the business, written down with the same care: Electronics segment margins of 20-25.5% since FY2017, above
CTS's consolidated operating margin in every year compared (Q2); a margin rise in FY2025 while Electronics organic sales
fell 8.3%, credited to "Pricing, and productivity initiatives"; no customer above 5% of sales or receivables; backlog
realisable within a year up 29.7% to $318.5M.

## THE STANDING RULE
Owning a share of Standex bought with cash, without borrowed money and at a size whose total loss could be borne, puts
the buyer at no risk of ruin; the rule binds the buyer's financing and sizing, not the target **[M2012-081]**, and
"borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing here is bought on margin.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**; the product can stay opaque if "I understand the economic dynamics of the
  industry" **[M2011-014]**. Standex is now four segments (10-K FY2026, Item 1 and Note 17, FY2026 sales and segment
  operating income): **Electronics** $475.0M / $121.3M (reed switches and relays under the MEDER, KENT and KOFU brands,
  Hall-effect and other sensors, custom magnetics, and since October 2024 grid instrument transformers through Amran and
  Narayan); **Aerospace & Defense** $135.0M / $22.0M (spin-formed metal parts for launch vehicles, missiles, nacelles);
  **Scientific** $75.7M / $18.0M (laboratory and medical refrigerators, freezers, cryogenic tanks); **Engraving &
  Hydraulics** $182.3M / $27.4M (mold texturing for car interiors and consumer goods; telescopic hydraulic cylinders);
  plus $23.5M / $4.0M of the Federal display business sold in March 2026. Electronics carries **64%** of FY2026 segment
  operating income.
- **The key variables and whether they are foreseeable** **[M1998-044]**: OEM and utility volumes (grid, defense,
  industrial, autos), the price each part commands against the next supplier, and what the company buys and sells. The
  products are old technologies: the reed switch, the wound transformer and inductor, the instrument transformer, the
  lab freezer, the spun metal dome. Their demand is a forecast about customers, not about a technology race
  **[M2017-019]**. No segment lives on continued invention or fast-moving technology of the kind that routes the file
  here to TOO HARD **[L1993-023]**.
- **Holding company read by its parts** (CONVENTION, Q1): Electronics, the part that matters most, is understood as a
  set of niche component makers selling designed-in parts to OEMs and utilities; the other three parts are likewise
  simple manufacturing. The doubt I hold is about how well these niches are protected and about the grid cycle, which
  is a castle question owned by Q2, not about what the businesses are or how they make money. One feature weighs against
  foresight and is carried forward: the company says it has "divested, and likely will continue to divest" and buys on
  debt, so the parts ten years out will not be today's parts. The rows' doubt rule **[M2002-092]** is applied to the
  economics of the parts held today, which can be read.
- **VERDICT: IN.** The economics of each part can be stated from the filings **[M1995-051]**, **[M2000-037]**; whether
  they are protected is Q2's question.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**.

**The segment record, from the company's own segment notes** ($M sales / segment operating income / margin; segment
income is before corporate expense, which ran $40.0M in FY2026, about 4.5% of sales):

| FY | Electronics (to FY2011: Electronics & Hydraulics) | Engraving (FY2024 on: Engraving & Hydraulics, recast) | source |
|---|---|---|---|
| 2008 | 84.2 / 8.1 / 9.6% | 92.2 / 9.6 / 10.4% | 10-K FY2011 `0000310354-11-000034` |
| 2009 | 61.2 / 3.5 / 5.7% | 77.3 / 7.0 / 9.1% | same |
| 2010 | 53.8 / 4.9 / 9.1% | 77.4 / 9.4 / 12.1% | same |
| 2011 | 69.5 / 9.9 / 14.2% | 85.3 / 14.2 / 16.6% | same |
| 2013 | 108.1 / 16.1 / 14.9% | 93.4 / 15.6 / 16.7% | 10-K FY2015 `0000310354-15-000025` |
| 2015 | 114.2 / 20.9 / 18.3% | 110.8 / 24.3 / 21.9% | same |
| 2016 | 118.3 / 21.1 / 17.8% | 124.1 / 29.6 / 23.8% | 10-K FY2018 `0000310354-18-000016` |
| 2017 | 136.7 / 27.7 / 20.2% | 105.9 / 25.6 / 24.1% | same |
| 2018 | 196.3 / 45.3 / 23.1% | 136.3 / 29.0 / 21.3% | same |
| 2019 | 204.1 / 41.2 / 20.2% | 149.7 / 24.0 / 16.0% | 10-K FY2021 `0001437749-21-019845` |
| 2020 | 185.3 / 29.7 / 16.1% | 143.7 / 20.5 / 14.3% | same |
| 2021 | 253.4 / 46.6 / 18.4% | 147.0 / 22.5 / 15.3% | same |
| 2022 | 304.3 / 70.4 / 23.1% | 146.3 / 21.8 / 14.9% | 10-K FY2023 `0001437749-23-022156` |
| 2023 | 305.9 / 69.0 / 22.6% | 152.1 / 25.5 / 16.7% | same |
| 2024 | 322.0 / 64.0 / 19.9% | 206.0 / 37.0 / 18.0% | 10-K FY2026 `0001437749-26-027789` |
| 2025 | 400.1 / 87.9 / 22.0% | 179.3 / 25.2 / 14.0% | same |
| 2026 | 475.0 / 121.3 / 25.5% | 182.3 / 27.4 / 15.0% | same |

Scientific (same sources): 23-24% margins FY2019-21, 21-23% FY2022-23, 27.6% / 24.1% / 23.8% FY2024-26, on sales that
peaked at $83.9M in FY2022 and were $75.7M in FY2026, with organic declines in FY2025 and FY2026 tied to NIH cuts. A&D
(formerly Engineering Technologies): 8-18% margins FY2019-26, 16.3% in FY2026.

**The competitor row** (GAAP operating margin from the competitors' own 10-K data; accession of the latest year):

| year | CTS (`0001193125-26-067039`) | Littelfuse (`0001628280-26-009585`) | Sensata (`0001477294-26-000007`) | Standex Electronics segment |
|---|---|---|---|---|
| 2009 | not in tagged data | not in tagged data | 5.2% | 5.7% (E&H) |
| 2016 | 15.9% | 12.4% | 15.4% | 17.8% |
| 2018 | 13.0% | 13.1% | 20.2% | 23.1% |
| 2020 | 10.6% | 11.2% | 11.1% | 16.1% |
| 2022 | 15.8% | 19.9% | 16.6% | 23.1% |
| 2024 | 14.1% | 7.3% | 3.8% | 19.9% |
| 2025 | 15.3% | 1.6% (impairments) | 6.4% (impairments) | 22.0% (FY2025) |

Like is not quite set against like: the peers' figures are whole-company, after corporate cost and amortization;
Standex's is a segment, before corporate cost. Standex's consolidated GAAP operating margin without the Federal gain was
15.3% in FY2026 and 11.8% in FY2025, inside CTS's range. What the competitors say of their own markets: CTS,
"highly competitive and characterized by price erosion and technological change"; Littelfuse, which also sells "reed
switch based magnetic sensing", "competes on the basis of price, product performance and quality ..." and "may not always
be able to compete on price, particularly when compared to manufacturers with lower cost structures". Neither names
Standex as a competitor.

**The castle tests, each with its filing fact.**
- *Pricing power and the agony before a rise* **[M2005-020]**: FY2025 Electronics organic sales fell 8.3%, yet the
  segment margin rose from 19.9% to 22.0% on "Pricing, and productivity initiatives, and favorable product mix"; the
  10-K says the company has "thus far been largely successful" in passing on inflation. Passing cost through is what
  businesses "with strong competitive positions" do **[M2005-017]**. **For.**
- *Would the customer still choose it over the low bid?* **[M2017-009]**: the 10-K's own words are that "many of our
  businesses experience sales churn as customers seek lower cost suppliers", and price is among "The principal methods of
  competition". That is the customer who buys on price in some part of the book **[L2004-003]**, **[M2023-074]**.
  **Against**, for an unknown share of the businesses.
- *The low-cost position* **[L2004-007]**, **[M2001-013]**: no filing claims it. The company runs a "low-cost country
  sourcing strategy" in China and India and is closing four Engraving & Hydraulics sites; custom wound magnetics are, on
  my reading, labour-heavy parts that can be made abroad **[M2007-116]**. **Against or unproven.**
- *Unit volume*: company-wide organic sales change, from the 10-Ks: FY2015 +4.8%, FY2017 −1.5%, FY2018 +5.1%, FY2019
  +$27.3M (about 4%), FY2020 −6.4%, FY2021 +$15.3M (about 2.5%), FY2022 +14.7% (credited "primarily" to pricing actions
  and Electronics demand), FY2023 +5.7% (pricing), FY2024 −$37.7M (about 5%), FY2025 −7.5%, FY2026 +5.5%. Over FY2017
  to FY2026 that compounds to roughly 1.6% a year in nominal dollars, below inflation. **Against.**
- *Widening or narrowing* **[M1999-108]**, **[L2005-010]**: Electronics' margin went from 9.6% (FY2008) and 5.7%
  (FY2009) to 25.5% (FY2026), but the step-ups came with purchases: MEDER (Electronics sales 48 to 108 in FY2013), the
  OKI sensor business (FY2018), Renco (FY2021), Minntronix and Sanyu (FY2024), Amran/Narayan (FY2025). The speakers'
  own line, "We sort of buy barriers; we don’t build them." **[M2012-105]**, describes Standex as well: the in-house
  electronics earned 5.7-14.2% on its own (FY2008-11). Engraving is narrowing: 24.1% (FY2017) to 14-17% (FY2019-26),
  with site closures. **Mixed: Electronics widening by purchase, Engraving narrowing.**
- *The money test* **[M2011-015]**: larger competitors already exist in every line (Littelfuse in reed sensing; TDK,
  Bourns, Vishay and others on Littelfuse's own competitor list; the large grid-equipment makers in instrument
  transformers). The filing names none and gives no share data. **Not answerable from the filings.**
- *Ask the competitors* **[M1999-130]**: done only through their filings (above); no competitor names Standex.
- *What could destroy, modify or reduce it* **[M2000-014]**: the end of the grid-equipment shortage, where the newest
  and highest-margin part of Electronics sells; solid-state sensing in place of reed switches; tariffs on parts from
  China and India; the movement of mold texturing and car programmes.

**The deciding question.** Electronics carries 64% of segment income, and within it the grid business, bought in
October 2024 for an enterprise value of about $467.5M, is the part whose economics have moved most. One filed fact shows
how fast: the 9.9% of Narayan valued at **$27.9M** at closing (8-K `0001437749-24-032685`) cost **$64.0M** in cash
twenty months later, under put and call terms priced at "the greater of" closing fair value and a formula on trailing
"adjusted EBITDA" (8-K `0001437749-26-022576`). That is a business whose profit has risen very fast, and the rows warn
that "if something can gain competitive advantage very quickly, you have to worry about them losing it quickly, too"
**[M2002-050]**; that supply can run ahead of demand in a business whose managers "like to build new plants"
**[M2017-043]**; and that seeing "dramatic growth ahead for an industry does not mean we can judge what its profit
margins and returns on capital will be" **[L2009-005]**. Whether Electronics' 25.5% is a standing position (designed-in
parts, few reed-switch makers, price held through FY2025's volume fall) or the top of a grid cycle bought near its peak
cannot be judged from the filings read: the 10-K does not split Electronics by product line, and the pre-acquisition
accounts of Amran and Narayan, filed on 8-K/A (2025-01-13, `0001437749-25-000976`), were not read in this run.

- A castle shown open on the evidence closes OUT; the evidence here runs both ways (Electronics' margins hold above the
  peers' and held price in FY2025; the low-bid churn, the flat organic record and Engraving point the other way). A
  castle whose future cannot be judged closes TOO HARD: "when we see a moat that’s tenuous in any way [...] it’s just
  too risky. We don’t know how to valuate that, and therefore we leave it alone." **[M2000-019]**, **[M2006-013]**.
- **Cause: WORK.** The deciding fact, what the grid business earned before the shortage, is "important and knowable"
  **[M2006-076]**: it sits in a filed document and in the filings of listed instrument-transformer makers. This is the
  reader's cause, "I haven’t done the work" **[M1994-026]**, not the industry's **[L1993-023]**. Whether the industry's
  own people would write down a ten-year grid margin **[M2000-105]** is for the research pass to say.
- **VERDICT: TOO HARD (WORK).** The file closes here. Q3 to Q12 are NOT REACHED.

---
## COMPUTATION — NOT A CLEARANCE
*(Operator rule 3: valuation arithmetic after a closing STOP. It carries no entry language and clears nothing. Reported
at the owner's request, not under a rule.)*

**(a) The value range, Q7 CONVENTION construction.** Cash input: five-year average owner cash, unlevered, **$61.4M**
(Step 0 table), so that today's net debt of **$403.2M** (including the $64.0M Narayan payment) is deducted once. Rate:
the 30-year Treasury, 5.63% **[L2000-021]**, **[M1996-025]**. Ten years, then zero nominal growth (CONVENTION).
- **Bottom, no growth:** $61.4M / 5.63% = $1,091M, less $403.2M = $688M, **$56.8 a share**.
- **Top, shown growth:** unlevered owner cash grew from $49.6M (FY2022) to $80.2M (FY2026), **12.8% a year**, carried
  ten years then flat: **$213.8 a share**. That growth was bought: $540.7M went on acquisitions in FY2022-26 against
  $143.1M of divestiture proceeds, and the convention's cash input does not deduct it. With growth capped at the organic
  record (about 1.6% a year) the top is **$68.9**; at the levered owner cash's shown growth (5.6%), **$107.4**.
- **Width:** $213.8 / $56.8 = **3.8 to 1**, wider than the convention's three to one, so the uncapped range closes TOO
  HARD **[L2000-025]**, **[M2007-022]**. With the organic cap the range is narrow (about $57 to $69) and the price sits
  far above its top, which closes OUT through the floor (CONVENTION).
- **The price against the range:** **$289.91 is above the top of every version of the range.** At the sovereign rate
  the price needs the five-year owner cash to grow **16.2% a year for ten years** before flattening.

**(b) The FAIR PRICE: $87 a share.** The price at which the central case returns about 10% pre-tax, the floor
(CONVENTION; **[M2003-149]**, **[L2002-020]**, **[M1994-004]**, qualified by **[M2003-151]**). After-tax equivalent used:
**7%**, the top of the row's own translation of 10% pre-tax "after corporate tax" **[L2002-020]**, applied because owner
cash is already after corporate tax. Central case, my judgment and labelled as such: unlevered owner cash **$70M**
(between the five-year $61.4M and FY2026's $80.2M, held down because management itself puts long-run capex at 4-5% of
sales against 2.8% spent in FY2026), growing **5% a year** for ten years (between the ~1.6% organic record and the bought
12.8%, near the levered 5.6%), then flat; discounted at 7%; less $403.2M of net debt. Applying 10% to the after-tax cash
instead gives **$48**. At $289.91 the central case's expected return is **about 2.8% a year after corporate tax**, below
the 5.63% bond.

**(c) The CHEAP PRICE: $17 a share.** Rule: the price at which the five-year average unlevered owner cash, with **no
growth at all**, earns **10% after corporate tax** on the enterprise value ($61.4M / 10% = $614M, less $403.2M). Below it
the floor is cleared on its strict reading with nothing assumed for growth, so no pencil is needed **[M1996-084]**,
**[M2009-005]**.

Against $289.91: the price is 3.3 times the fair price, 17 times the cheap price, and 1.4 times the top of the uncapped
range. Owner cash yields 1.43% on the market value.

---
## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
Facts found, recorded without a weighing: on tangible capital the business is light (FY2026 pretax operating income
before the gain and before amortization about $154M, on about $377M of net debt plus equity less goodwill and
intangibles); on the capital actually put in, including $781M of goodwill and intangibles, pretax operating income
without the gain, $136.5M, is about 12% of $1,158M. The growth came from purchases, not from reinvestment in the
businesses held **[M2001-019]**.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED.
The balance sheets were read in Step 0 **[M2025-032]**. Recorded for the research file, not weighed: the release
features adjusted earnings and EBITDA **[L2016-006]**, **[M2002-026]**; receivables plus contract assets have risen as a
share of sales **[M1995-064]**; stock pay is a real cost and is deducted above **[L2015-003]**.

## Q5 — WHO RUNS IT. NOT REACHED.
Recorded only: David Dunbar, CEO since January 2014, 64, owns 106,428 shares (about $31M at the price); FY2026 total pay
$6,407,973, 146 times the median employee; directors and officers together 2.0% (proxy `0001437749-26-029660`).

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
Recorded only: long-term pay moved from ROIC to EBITDA for FY2026-28 after a debt-financed purchase lowered ROIC
**[M2016-083]**; the stated reason is quoted in the contrary-evidence list. Buybacks fell from $31.8M (FY2024) to $4.4M
(FY2026); dividends were $16.2M in FY2026. The Narayan minority cost $36.1M more than its value at closing
**[M1995-001]**.

## Q7 — WHAT IS IT WORTH. NOT REACHED as a question; the arithmetic is the COMPUTATION above.
## Q8 — BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 — COULD IT RUIN US. NOT REACHED.
Recorded only: funded debt to adjusted EBITDA 2.41 against a 3.5 covenant; interest coverage 4.97 against 2.75; $225M
swapped to a fixed 3.48% through August 2028; the revolving facility is the main source of acquisition funds.
## Q10 — THE FAT PITCH. NOT REACHED.
## Q12 (optional) — NOT REACHED. Nothing in the businesses named would trouble the newspaper test **[M2008-011]**.

---
## THE BOX
**TOO HARD (WORK), at Q2.** Cause: the deciding question, whether Electronics' margin (grid instrument transformers
above all) is a standing position or a shortage peak bought near its top, is knowable from filed documents not read here.
COMPUTATION, not a clearance: value range **$57 to $214** a share (3.8 to 1; **$57 to $69** with growth capped at the
organic record), **fair price $87**, **cheap price $17**, against a price of **$289.91**.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. **Not fully kept:** the file was written in two sittings (Step 0 to Q1,
      then Q2 onward, the second after a session limit), not question by question, and **nothing was committed**,
      because the brief forbade commits.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact has its accession;
      numbers not from a filing are labelled COMPUTATION or CONVENTION, or marked as my judgment.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy; stock pay deducted though the tool printed zero; the
      sovereign from the Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]**.
- [x] No row dated after the anchor: the run is dated today, so the anchor rule does not bind.
- [x] Only the arithmetic lines of `tools/run.py` were used, and its stock-pay line was rejected.
- [x] `python tools/check_framework.py` run before the reply (no commit made).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Bought growth in the Q7 convention.** The convention carries owner cash "at the growth the business has actually
shown", measured on aggregate owner cash. For a serial acquirer that counts $540.7M of purchases as shown growth (12.8%
a year), because the owner-cash input does not deduct acquisition spending, and "capped by the growth arithmetic of Q3"
gives no working rule for taking it out. I showed the uncapped, organically capped and levered versions. (2) **Levered
or unlevered.** When debt rose fourfold inside the five-year window, a levered average understates future interest and
an unlevered average undercounts the bought earnings. The convention is silent; I used unlevered cash less today's net
debt and said so. (3) **Two closes at once.** The uncapped range is wider than three to one (TOO HARD) while the price is
above its top (OUT through the floor); the convention does not say which governs. (4) **The floor's after-tax
equivalent.** **[L2002-020]** translates 10% pre-tax into an after-corporate-tax figure, but owner cash is already after
corporate tax; whether the floor applies to it at 10% or at 7% moves the fair price from $48 to $87. (5) **The research
pass's "before any reading" rule** cannot be fully kept by the analyst who ran the file: several knowable questions
(Engraving's trend, Electronics' pricing through FY2025) were answered while running Q2, so step 2 below names only
questions whose evidence was not read. (6) **Q1 for a portfolio rotator.** The by-parts convention reads today's parts;
for a company that says it "likely will continue to divest" and buys on debt, the ten-year economics depend on deals
not yet made, and Q1 has no rule for that.

---
## RESEARCH PASS, STEPS 1 AND 2 (Part VII; written, not run)
**Step 1. What do I not know that I need to know?** **[M1999-129]**
- **RQ1 (deciding; knowable):** What did the grid businesses (Amran, Narayan) earn before the purchase, and is their
  present margin a standing level or a shortage peak? Knowable **[M2006-076]**: audited pre-acquisition statements are
  on file.
- **RQ2 (knowable):** Do listed instrument-transformer makers show grid margins at today's level before the current
  shortage? Knowable from their annual filings.
- **RQ3 (possibly unanswerable):** What share of Electronics' FY2026 operating income comes from grid products? The 10-K
  does not split it; the FY2026 filings give "fast growth markets" sales ($263.8M for the year) only. If no primary
  document splits it, it is recorded as unanswerable and the close is decided on RQ1 and RQ2.
- Already answered in this run and not re-researched: Electronics held and raised its margin through FY2025's volume
  fall; Engraving is narrowing; organic growth averaged about 1.6% a year over FY2017-26.

**Step 2. For each: the evidence, its span and source, and the one fact that closes OUT** **[M1998-144]**
- **RQ1.** Source: Standex 8-K/A filed 2025-01-13, accession `0001437749-25-000976`, Item 9.01 (audited statements of
  Amran and of Narayan, and the pro forma information). Span: every annual period presented. **OUT fact:** the earliest
  annual period presented shows the combined Amran and Narayan operating margin below **13.9%**, CTS's ten-year median
  GAAP operating margin (2016-2025, from CTS's 10-K data: 15.9, 9.1, 13.0, 11.5, 10.6, 14.9, 15.8, 13.6, 14.1, 15.3).
  CONVENTION, ours: the threshold is an ordinary component maker's margin, so a grid business below it before the
  shortage earned ordinary returns until the cycle lifted it.
- **RQ2.** Source: the annual reports of listed Indian and US instrument-transformer makers, FY2015 to FY2025, primary
  filings only (stock-exchange filings; any aggregator flagged). **OUT fact:** the peers' median operating margin
  averaged over FY2015-FY2020 is below half its FY2024-25 average (a margin that doubled in the shortage).
- **RQ3.** Source: Standex's 10-K FY2026, its 10-Qs and the Item 2.02 earnings-release exhibits from FY2025 to date.
  **OUT fact:** none; an answer only sizes RQ1 and RQ2.
- Close rule: IN if neither OUT fact appears; OUT on either; TOO HARD (NATURE) if the evidence cannot be read. The pass
  closes IN, OUT or TOO HARD (NATURE), never WORK twice **[M2008-086]**. An IN at Q2 reopens the run at Q3, where the
  COMPUTATION above already shows the price far above every version of the range.
