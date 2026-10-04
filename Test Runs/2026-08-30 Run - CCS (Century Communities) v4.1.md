# Company Run — Century Communities, Inc. (NYSE: CCS) — 2026-08-30
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this file
and that document disagree, the document governs. Q3 annex:
`Framework/v4/THE MANAGER STANDARD - Q3.md`.

**Position context: NONE HELD. Fresh entry run.** Surfaced by the 2026-08-30 dividend
lens (1.8% statute yield; payout 0.24 of worst-5y EPS; "5y dividend CAGR ~33%"). **Bias
declared per operator rule 9:** ~$2,750 of taxable capital seeks a dividend payer that
compounds, so the analyst's incentive is to clear this name. The iron prescription
[E4-51] is applied; disconfirming evidence hunted hardest [E4-26]. **A "no" verdict is a
fully successful run.**

**The pre-recorded warning, carried as a task:** the sweep flagged that CCS's
worst-5-year EPS window spans the biggest housing boom in a generation and ruled the
statute yield unreliable until re-based [E4-41]. This run tests that flag; the result is
at Q4 ("the [E4-41] flag, tested").

**Prior verdict on file:** the 2026-07-16 homebuilders 6-pack (v3.0) eliminated CCS at
Gate 2 on its own filing's concession, "characterized by relatively low barriers to
entry." This run re-tests that finding under v4.1 with the current filings and a full
competitor row; it does not inherit it.

**Brief correction, against the filing:** the operator brief named the founder pair
"Mandile/Francescon." The FY2025 10-K and 2026 DEF 14A name the founders as **Dale
Francescon (Executive Chairman) and Robert J. Francescon (CEO & President), brothers**,
13.9% combined beneficial ownership. The text wins; corrected here.

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- **USD 30-year: 5.19% · 2026-08-27 · FRED DGS30** (Treasury constant maturity; the
  project's standing USD source). `tools/sources.py` USD fetch failed again from this
  environment (remote disconnect, same as the ETD/FLO runs); the identical series was
  pulled directly from `fredgraph.csv`, dated. FRED's 1-2 day lag noted, immaterial.
- FX: none. Quote currency = earnings currency = USD.
- Price: **$69.16, NYSE close 2026-08-28 (Yahoo — aggregator, live quote only, flagged).**
- **Market cap, verified as tasked:** 28,432,900 shares (filed cover count, Q2-2026
  10-Q, as of 2026-07-17) × $69.16 = **$1,966M**, against the sweep's ~$1,958M: a 0.4%
  gap (price-date drift). **Verified.** Book value $2,565.8M at 2026-06-30 → **$90.24/
  share; price/book 0.77×.**

**The filing was read — not tagged data [E3-27]:**
1. **FY2025 Form 10-K, filed 2026-01-29, accession 0001576940-26-000005** (year ended
   2025-12-31; auditor Ernst & Young per filing) — [x] MD&A [x] cash-flow statement
   incl. detail lines [x] footnotes (debt Note 11 area; capitalized interest; inventory
   and impairment policy incl. the 13% impairment discount rate; legal proceedings;
   segments).
2. **Q2-2026 Form 10-Q, filed 2026-07-23, accession 0001576940-26-000057** (period
   2026-06-30) — MD&A, cash-flow statement, dividend table, segment detail, ARM
   disclosure.
3. **Q1-2026 Form 10-Q, filed 2026-04-23, accession 0001576940-26-000026** (used for
   quarterly series).
4. **DEF 14A, filed 2026-03-25, accession 0001140361-26-011011** (comp, ownership,
   related-party).
5. Earnings releases: 8-K Ex-99.1 of 2025-01-29 (acc. 0001576940-25-000003, initial
   FY2025 guidance) and 8-K Ex-99.1 of 2026-07-22 (acc. 0001576940-26-000055, Q2-2026
   and revised FY2026 guidance) — for the [E3-48] guidance-vs-outturn test.
6. Prior 10-Ks for the mid-cycle base and unit series: FY2019 (acc.
   0001562762-20-000031), FY2021 (acc. 0001576940-22-000006), FY2023 (acc.
   0001576940-24-000005).
- **Figure cross-checked against the filed statement:** FY2025 OCF. The filed
  consolidated statement of cash flows reads "Net cash provided by operating activities
  **153,081**"; the MD&A prose carries "$153.1 million"; XBRL companyfacts carries
  $153.081M. Three-way match. Second check: H1-2026 OCF filed as "(132,439)" in the
  10-Q statement, XBRL −$132.4M. Match.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words:** CCS buys or options residential lots in 16 states,
  builds inexpensive single-family homes on spec (99% of FY2025 deliveries were built
  move-in-ready before a buyer was found; 94% priced below FHA mortgage limits), and
  sells them fast: 10,387 new homes in 2025 at an average $378.0K. Land and construction
  sit in inventory ($3.6B at Q2-2026) funded by $2.57B of equity and ~$1.3B of
  homebuilding debt plus a revolver; the cost of a lot flows into cost of sales when the
  home closes. A wholly-owned mortgage arm (Inspire Home Loans) finances the buyers,
  sells the loans within ~30 days off warehouse facilities, and exists mainly so the
  builder controls the buyer's closing (and can price rate buydowns as an incentive).
  The Century Complete brand is the purest form: lowest local price, fixed floor plans,
  no options or upgrades, sold partly online against RESALE homes. Profit = (price −
  lot − sticks-and-bricks − incentives) × volume, minus a fixed SG&A base; every input
  is market-priced.
- **The scarce input the business controls:** honestly, none for long. The pipeline is
  60,128 lots (Q2-2026), 57% owned, ~5.9 years of supply, which is control bought with
  the balance sheet, not a franchise input; land, subcontractor labor, and the buyer's
  mortgage rate are all market-set. That is a Q2 finding made here.
- **Ten years:** the mechanism (spec entry-level homebuilding plus captive mortgage)
  will look the same; the demand level and margin will be set by rates and land, as
  they are today. Legible, cyclical, simple.
- **VERDICT: [x] IN** — the business is understandable; what it lacks is not
  intelligibility.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** — entry-level housing in an undersupplied market.
- Not price-regulated **[x]**.
- No close substitute **[ ] — FAILS by the filing's own words.** A house has perfect
  substitutes: another builder's house, a resale, a rental. CCS's Century Complete
  strategy is explicitly to WIN the substitution contest on price ("Our goal is to be
  the price leader"; it "often competes with resales", FY2025 10-K). The 10-K concedes
  the class condition twice: the industry is "characterized by **relatively low
  barriers to entry**" (Item 1 and the risk factors, FY2025 10-K) — the same concession
  that eliminated CCS in the 2026-07-16 6-pack, still in the current filing.

**The commodity doctrine [E2-58] governs.** Homebuilding is the commodity class:
persistent over-capacity potential, no administered prices, profitability set by "the
ratio of supply-tight to supply-ample years." The one exception is a cost advantage
"wide and sustainable." Tested honestly below.

**The two-characteristic test [E2-44]: 0 of 2.**
1. Raise prices when demand is flat? No — the opposite is filed. FY2025 ASP −3.3%
   "primarily due to higher incentives"; every one of the five homebuilding segments'
   FY2025 discussion attributes margin decline "primarily to higher incentives"; H1-2026
   ASP −5.4%, same cause. This is [E4-37] agony pricing in its pure form: the company
   pays the customer (rate buydowns, closing costs, base-price discounts) to take the
   product.
2. Grow dollar volume with minor capital? No — growth is bought with inventory.
   **Cumulative operating cash flow 2013-2025, summed from the filed statements, is
   approximately −$5M** (thirteen years, ~$34B of cumulative revenue, roughly zero
   operating cash returned) while notes payable went from $1.5M to $1.1B. The earnings
   were real; they are standing in the lot pipeline.

**The entry-level-scale claim, tested as tasked.** The claim: national scale in
entry-level spec (bulk materials purchasing, subcontractor pricing, the Century
Complete no-options format, captive mortgage) is a cost advantage. What the filings
show: the format is real and the segment held up best in the downturn (Century Complete
pretax income +19.3% H1-2026 while West fell 56.7%); national purchasing exists. But
[E2-58] requires the advantage to be **wide and sustainable**, and the row answers
that: in the supply-ample year CCS earned **5.7% ROE, 8th of 9** in its peer set, ahead
of only LGI Homes (3.5%), the pure-play entry-level spec comparable. The entry-level
END of the industry is where the down-cycle bites deepest, because the affordability
buyer is the first priced out and the spec builder must clear finished inventory at
whatever incentive it takes. D.R. Horton, the actual scale owner of this segment (3.3×
CCS's volume at 14.5% trough ROE), sits above CCS on cost; NVR's capital model earns
33% through the same trough. A cost advantage that produces a bottom-quartile return in
the revealing year is not wide; the claim fails on the same-metric row. **The MITSY
price-taker precedent applies: position in a commodity class without the cost
exception.**

**THE COMPETITOR ROW [E3-28]** — built and committed as
`Test Runs/_research 2026-08-26/CCS competitor row (DHI-LEN-PHM-NVR-MTH-KBH-LGIH-TMHC).md`
(XBRL-transcribed peer facts, fiscal windows stated there; subject cross-checked to
filings):

| Company | latest-FY ROE | 5-yr mean ROE | revenue peak→latest |
|---|---|---|---|
| NVR (Dec-25) | **33.2%** | 41.3% | −2% |
| Pulte (Dec-25) | 17.7% | 26.3% | −4% |
| D.R. Horton (Sep-25) | 14.5% | 24.4% | −7% |
| Taylor Morrison (Dec-25) | 12.9% | 17.3% | −1% |
| KB Home (Nov-25) | 10.8% | 17.5% | −10% |
| Meritage (Dec-25) | 8.8% | 19.6% | n/a |
| Lennar (Nov-25) | 8.3% | 16.3% | −4% |
| **CCS (Dec-25)** | **5.7%** | 18.0% | −9% |
| LGI Homes (Dec-25) | **3.5%** | 16.1% | −44% |

- Peers named: **8 of the industry's ~10-12 real public competitors** (GRBK and DFH not
  pulled; work order in the row file). Row limit [E3-61] stated there.
- **The units series [E4-55], read honestly both ways:** deliveries 8,000 (2019) →
  10,805 (2021) → 9,568 (2023) → 11,007 (2024) → 10,387 (2025) → H1-2026 −7.2%. This is
  NOT an ETD/FLO-style melt; units grew across the cycle and share held. What the
  series shows instead is that the units are bought with price: ASP $373.3K (2021) →
  $361.1K (H1-2026) while input costs rose, the definition of a price-taker.
- **Untapped pricing power [E3-33]:** none; the pricing lever is running in reverse
  (incentives). The near-monopoly claim [E5-28] cannot be stated with a straight face
  for a 3%-share national builder.
- **Moat direction [E4-32]:** not applicable in the ETD sense; there is no moat whose
  direction could be tracked. Gross margin round-tripped the boom: 17.5% (2018) · 17.7%
  (2019) · ~24% (2021) · 21.5% (2024) · **17.6% (2025)** · 18.0% (H1-2026).
- Class: **[x] NONE** (commodity class, no wide-and-sustainable cost exception) ·
  Direction: n/a.
- **VERDICT: [x] OUT.** Under [E3-03] a franchise is thought by its customers to have
  no close substitute; a spec entry-level house is the maximally substitutable consumer
  durable, the filing concedes low barriers to entry twice, the two-characteristic test
  scores 0 of 2, pricing is agony-class [E4-37], and the row places CCS second-worst of
  nine on the primary metric in the revealing year. What remains is a legible,
  substantial, decently financed **commodity cyclical**, in the class where "a
  business, unlike a franchise, can be killed by poor management" [E3-43]. **The entry
  run stops here. [E5-13]: most names should end here, and that is the system
  working.**

---
⛔ **Q3, Q4 and Q5 do not open for entry.** Q1 IN · Q2 OUT — the hard sequence closes
the file for any BUY decision. No position exists, so no [E2-28] hold read is required.
Everything below is FOR THE RECORD — the operator tasked this run with the dividend
arithmetic, the re-based owner-earnings floor, and Q6 regardless. **Everything below
operator rule 3's header. Nothing below is entry language.**

---
## Q3 — FOR THE RECORD: ARE THEY HONEST, AND ARE THEY RATIONAL?
*Standard applied: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Q2 OUT stands
regardless; Q3 can stop a run, never start one.*

**STEP 1 — THE WEIGHT CASE.** [x] **Daily execution HIGH** — a spec builder buys land,
starts homes, and prices incentives every single day; [E3-38]'s retailer logic applies,
and [E3-43] names the class: a business without a franchise can be killed by poor
management. [ ] Control — no (marketable minority, exit exists). [~] Leverage —
MODERATE, named and quantified per [E4-16, E3-29]: homebuilding debt/capital 34.2%
(net 31.9%) at Q2-2026, up from 29.1%/25.9% at YE2025; not bank-class magnification,
but land bought with debt is how builders died in 2008. **One determinant high → Q3
would be a BINARY GATE for entry; no price compensates [E3-29, E5-35].**

**Honesty — the binary [E5-16]:** no integrity matter found. The sweep, named: FY2025
10-K Legal Proceedings (ordinary-course construction/warranty claims only, no material
loss expected); DEF 14A related-party section (aircraft time-sharing agreements with
both Francescons, personal use reimbursed at incremental hourly cost, disclosed); no
restatement, no SEC enforcement found in the documents read. Worded per the
absence-claim rule: no instance found in the documents read, not "none exists."

**STEP 2 — THE FLAGS [E4-22, E4-29, E5-15, E4-30, E2-52, E3-50, E2-57, E3-53, E2-49].**
- [x] **Trumpeted projections — FIRED, institutionalized.** The 10-K's own risk factor:
  "Each quarter, **we typically issue guidance** regarding our anticipated annual
  revenue and home deliveries." The [E5-30] ratchet is company policy in writing. The
  [E3-48] outturn test, run: initial FY2025 guidance (8-K, 2025-01-29) was **11,700 to
  12,400 deliveries and $4.5 to 4.8B revenue**; the outturn was **10,387 and $4.1B**, a
  miss of ~11-16% on the low end, guided down across the year. The 2026-07-22 release
  then leads with "raising the midpoint" of a 2026 range whose top (10,500) sits below
  the 2025 outturn.
- [x] **EBITDA / adjusted promotion [E4-29] — FIRED.** Six named non-GAAP measures in
  every release: adjusted net income, adjusted EPS, adjusted homebuilding gross margin,
  EBITDA, adjusted EBITDA, net homebuilding debt to net capital. Adjusted net income
  excludes inventory impairments and (since Q3-2025) lot-option abandonments — for a
  spec builder these are the recurring costs of the cycle, and [E5-33] answers the
  "one-time" framing: to tell owners year after year "don't count this" is misleading.
- [x] **Metric-switching [E2-49] — FIRED TWICE, both switches following deterioration,
  dated from the releases:** (1) beginning **Q3-2025**, "Abandonment of lot option
  contracts" was added to the adjusted-NI and adjusted-EBITDA definitions, in the year
  the company walked away from ~19,000 controlled lots and charged $11.2M of forfeited
  deposits; (2) beginning **Q4-2025**, "Stock-based compensation expense" was added
  back to adjusted EBITDA — the exact adjustment [E5-06] calls cavalier. Also Q4-2025:
  the impairment line was reclassified out of a separate statement line into cost of
  home sales (disclosed, conforms to peers, but the visible line disappeared in the
  quarter impairments hit a cycle high). The yardsticks moved when the readings turned.
- [ ] Serial share issuance [E5-15] — NOT fired, the reverse: diluted shares 34.4M
  (2021) → 30.4M (2025) → 28.4M cover count (Jul-2026); no dividends-by-issuance
  [E2-52].
- [ ] Filed-figure tells [E4-30] — NOT fired: growth is visibly lumpy; cash taxes ÷
  pretax = 24.3% (2021) · 24.8% · 22.9% · 23.3% · 27.6% (2025), no falling pattern.
- [ ] Weak accounting basics — not fired: SBC expensed in GAAP statements, no pension,
  unqualified opinions found in the filings read.
- **Convergence [E4-52] — the finding:** flags 1-3 all push the same direction, toward
  reporting the down-cycle as better than GAAP shows. Several flags toward one outcome
  are one reinforcing system, not a sum of prompts.

**STEP 3 — THE PRIMARY TEST [E2-01].** Balance sheet first [E5-27]: equity $859M (2018)
→ $2,592M (2025), built from retained earnings, no goodwill games found, buybacks real
and dilution negative across the window. ROE series (NI ÷ avg equity, filed figures):
**11.8% (2019) · 17.6% (2020) · 32.7% (2021) · 26.8% (2022) · 11.4% (2023) · 13.3%
(2024) · 5.7% (2025) · ~5.2% TTM at 2026-06-30.** Without undue leverage (34% debt/cap)
and, at the GAAP line, without gimmickry; the gimmickry pressure sits in the non-GAAP
layer (flags above). Mid-pack in the boom, second-worst of nine in the trough (the
row). The hand they were dealt [E3-59] is a commodity hand; they have played it
adequately, not distinctively.

**Institutional imperative [E2-30], scored:** (1) resists change — partially: the
model is unchanged, though the 2025 lot-pipeline cut shows real willingness to shrink.
(2) Projects soak up available funds — **fired**: average selling communities grew 281
(2024) → 318 (2025) → 321 (Q2-2026) while the return on the capital so employed fell
to 8th of 9; growth in community count was the stated premise of the missed FY2025
guidance. (3) Staff studies — not observable. (4) Peer imitation — fired in both
directions: the boom-era swing to optioned lots (55.7% controlled at 2024) followed
the industry's land-light fashion; when the options got expensive the book was cut to
42.9% and the owned share rose to 57.1%, so the flexibility story now runs backwards.

**Capital allocation — buybacks [E5-08, E5-31, E2-51]:** condition (1) ample funds —
qualified: H1-2026 buybacks ($59.6M) and dividends ($18.5M) ran while OCF was −$132.4M
and the revolver rose $278M; seasonal, but the payout was debt-funded in the half, the
[E2-60] restricted-earnings note. Condition (2) discount — passes at the price:
repurchases at wtd-avg $63.32 (2.3M shares, 2025) and $61.44 (969.9K, H1-2026) against
book value of $86-90/share over the window; for a builder price/book is the honest
yardstick [E5-31] and buying near 0.7× book while cutting the lot pipeline is the
rational harvest move. This is the strongest single Q3 positive, alongside the
proactive Sept-2025 refinancing of the 6.75% 2027 notes into 6.625% 2033 notes (par
call, $1.4M loss taken, maturity wall pushed six years before the need [E2-64]).

**Comp and ownership:** founder pair SCT totals 2025: Dale $7.36M + Robert $8.51M =
**$15.87M, 10.8% of a $147.6M net income year**; "compensation actually paid" peaked at
$21.0M (2021) and $30.6M (2023) each for R. Francescon. Heavy for the size. The 2026
proxy documents shareholder-pressure responsiveness: pay opportunities cut 10-30% for
2025, three-year post-vesting holds added, say-on-pay ~90% (2025 meeting). Ownership
13.9% combined is real alignment, mostly grant-accumulated.

**THE GUARDRAIL:** [x] nothing here promotes the name (Q2 OUT stands; a competent
record cannot repair a commodity class [E2-37, E2-38, E3-39]); [x] no key-person moat
exists to record; [x] no excisable-cancer case is argued.

- **Q3 FOR-THE-RECORD READ: no honesty disqualifier found; the entry gate would still
  not clear.** In a daily-execution business the guidance culture ([E5-30]: "do it once
  and you probably never stop"), the two deterioration-following yardstick switches
  [E2-49], and the adjusted-measure promotion [E4-29] converge [E4-52] exactly where
  the gate looks. Set against them: honest GAAP statements, shrinking share count,
  below-book buybacks, early refinancing, disclosed comp responsiveness. *A pass here
  would be the absence of found disqualifiers, never a clearance [E5-17]; IN never
  promotes.*

## Q4 — FOR THE RECORD: WILL IT SURVIVE?

### Owner earnings — **COMPUTATION — NOT A CLEARANCE** [E2-23]
Convention: multi-year mean of (OCF − SBC) − (c). **Homebuilder note, the disclosed
judgment the operator required:** land purchases and development run through OPERATING
cash flow, so the convention's OCF basis automatically charges ALL land spend,
including community-count growth, as if it were maintenance. (c) is therefore stated
two ways, per [E2-23]'s own definition (maintenance = what is required to hold
long-term competitive position AND unit volume):

- **Basis A — everything-is-maintenance (the OCF convention, unadjusted):** 5-yr mean
  OCF 2021-2025 = $86.9M (−201.2, +315.3, +41.6, +125.7, +153.1); less mean SBC $23.8M;
  less (c) for the small PP&E layer at the D&A..capex band ($17.4M..$28.1M) →
  **OE_A ≈ $35M-$46M** (yield 1.8-2.3%). This charges thirteen years of community
  growth as expense; the same convention over 2013-2025 gives cumulative OCF ≈ −$5M.
  Honest as a floor-of-floors; too harsh as a maintenance read while unit volume was
  being grown 8,000 → 10,400.
- **Basis B — maintenance = replacing sold lots to hold ~10,400 units/yr [E2-23]:**
  the income statement already charges each delivered lot at cost through cost of
  sales; holding volume at a flat community count requires replacing lots at CURRENT
  prices, which GAAP earnings approximate when land is not inflating ([E4-47] caveat
  stated: in a land-inflation regime NI would overstate OE; today's filed direction is
  the opposite — incentives, terminations, $21.8M impairments — so the caveat is small
  and cuts both ways). The PP&E layer's D&A ($24.8M) vs capex ($28.8M) is a wash;
  (c) judged at capex. SBC is already expensed in NI. **OE_B ≈ NI: FY2025 $147.6M;
  TTM at 2026-06-30 $134.0M** (147.6 − 74.2 H1-25 + 60.6 H1-26).
- **Windows [E2-42, E4-25], shown, not chosen-and-defended:** 5-yr NI mean 2021-2025 =
  $352.8M · 3-yr = $246.9M · FY2025 = $147.6M · TTM = $134.0M. **Spread: the 5-yr mean
  is 2.6× the TTM.** The distorted years are named: 2021-2022 delivered sub-3% mortgage
  demand at ~24% gross margins; [E4-41] governs — normalize DOWN for luck; the 5-yr and
  3-yr means are refused as OE bases.
- **The bottom boundary [E5-34], re-based as tasked:** a normal-rate year, NOT FY2021.
  FY2025/TTM is itself approximately that year: mortgage rates ~6.5-7% throughout,
  gross margin 17.6%/18.0% back at the filed pre-boom level (17.5% in 2018, 17.7% in
  2019), incentives fully deployed. **Bottom-boundary OE ≈ $110M-$150M** (TTM $134M,
  banded down for one further ~100bp of incentive drift ≈ −$29M after tax, and up to
  FY2025's $148M). Basis A's $35-46M is carried beside it as the all-growth-charged
  cross-check, not blended.
- Stock compensation subtracted in full [E5-06] (in NI for Basis B; explicitly for
  Basis A). No look-through increment [E3-04]: no material equity-method investees.

### The [E4-41] flag, tested — the answer the sweep asked for
**Partially disarmed, partially confirmed.**
- **The payout metric survives re-basing.** Worst-5y diluted EPS is FY2025's $4.86
  ($147.6M ÷ 30.36M), and FY2025 is a normal-rate, mid-cycle-margin year, not a boom
  year; the statute payout 1.16 ÷ 4.86 = 0.24 is genuinely conservative on coverage.
  TTM EPS ≈ $4.60 tells the same story.
- **The growth metric does not survive.** The "~33% 5y dividend CAGR" is an initiation
  artifact: the dividend was born May 2021 at $0.15/qtr, and 2021 paid only three
  quarters ($0.45). The quarterly-rate CAGR $0.15 → $0.32 (2026) is **16.4%/yr**, the
  recent raises are 10-12%/yr, and the funding year (2025 EPS down 53%) bounds the
  future rate at single digits. The compounding half of the operator's
  dividend-that-compounds brief is the half this name cannot document.

### Great, good, or gruesome? [E4-20]
**Cyclical: good at mid-cycle, gruesome-shaped at the trough — the class answer
[E2-58].** At mid-cycle the marginal retained dollar has earned 12-18% (2019, 2023,
2024: 11.4-13.3%; 5-yr mean 18.0% boom-inclusive), which is [E4-43]'s good class. At
the trough the pattern is the gruesome sentence verbatim: community count grew (281 →
321) while the return on the added capital fell to 5.7%, below the sovereign's 5.19%
plus nothing, and thirteen years of growth returned ≈$0 cumulative operating cash. The
2025 lot-pipeline cut and buybacks show management can run harvest mode; the class
sets when.

### Staying power — all three [E5-11]
1. **Large and reliable stream:** large, NOT reliable: NI $525M → $148M in three
   years; profitable every year since the 2014 IPO including 2023-2025 (no loss year
   in the filed record). Cyclical-pass with the reliability caveat written.
2. **Massive liquid assets:** thin as owned cash: $92.3M cash + $39.7M escrow at
   Q2-2026 against $3.6B inventory and $1.45B total debt. Stated liquidity ($1.1B at
   YE2025) is mostly the UNDRAWN revolver — [E5-39] kindness-of-strangers capital, and
   $329.6M of it was drawn by Q2-2026. Fail as the corpus means it; ordinary for the
   industry; that is the class, not an excuse.
3. **No significant near-term cash requirements:** pass on maturities: no bond due
   until Aug-2029 ($500M at 3.875%, which will refinance ~300bp higher: ≈ +$14M/yr
   interest, a named cost), 2033 notes $500M at 6.625%, revolver matures Nov-2028;
   mortgage warehouse facilities are short-dated and renewal-dependent (Inspire's
   funding is annually re-upped bank paper). Coverage test [E2-54]: interest incurred
   $77.3M (FY2025, mostly capitalized then released through COGS) vs TTM pretax before
   COGS-interest ≈ $237M → ~3.1× covered out of current earnings; comfortable now,
   gone in a 2008 replay.

### The specific ways THIS business dies [E2-27, E3-24] — exposure, not experience [E4-40]
1. **Incentive/rate-buydown compression (the live wound, filed):** every 100bp of
   homebuilding gross margin ≈ $39M pretax (~$29M after tax) on ~$3.9B home revenue ≈
   20-26% of bottom-boundary OE. GM is already AT the pre-boom level with incentives
   fully deployed, and the buyer quality tell is filed: **ARMs were ~35% of Inspire's
   Q2-2026 originations by principal, up from under 5% in Q1-2025** — affordability is
   being manufactured at the mortgage desk, the industry's pre-2008 signature.
   Another 200bp of give-up puts NI near $90M and the yield near 4.5%. **Likelihood: a
   real possibility** (order book flat, incentives still rising per every segment's
   MD&A).
2. **The land impairment cycle (the balance-sheet death, 2008 as exposure):** $3.6B of
   inventory (owned share raised to 57%) against $2.57B equity, tested for impairment
   at a 13% discount rate. A 2008-class 20-30% mark on inventory = $720M-$1,080M
   pretax = 21-31% of equity after tax; homebuilding debt/capital moves from 34%
   toward the mid-40s; the revolver's leverage and tangible-net-worth covenants come
   into play; the model's own history (impairments $21.8M and abandonments $11.2M in
   2025, rising from ~$9M in 2024) shows the marking machinery works but has never
   been stress-tested publicly — CCS was private through 2008-09. **Likelihood: a
   low-level possibility in any single year; across a permanent holding, the
   certainty the class carries [E2-27].**
3. **Spec inventory in a demand stop (the velocity death):** 99% move-in-ready means
   the order book is protection-free: backlog 1,264 homes ($469M) against $1,452M of
   homes under construction — roughly $1.0B of unsold WIP that moves only via price.
   A 2022-H2-style order stop (industry orders fell ~40% in months) clears that
   inventory at −10% ≈ −$100M, compounding death 1. **Likelihood: a real possibility
   once per cycle.**
4. **The captive mortgage arm (the channel death):** Inspire originates for CCS
   buyers, warehouses on repo facilities, sells within ~30 days, and retains
   rep-and-warranty repurchase exposure; the ARM surge (death 1) is originated HERE.
   Small today (segment pretax $19.2M, −28% in 2025, MSR book sold Q2-2025).
   **Likelihood: low-level for solvency; a live tell for demand quality.**
- **Q4 FOR-THE-RECORD READ: survives the current regime on the filed balance sheet
  (deaths 1, 3, 4 wound value, not solvency); death 2 is the class's terminal
  mechanism and no filing can retire it. Were the gate live it would read IN on
  current-regime survival, with the [E5-11] reliability leg failed and written.**

---
## Q5 — FOR THE RECORD — **COMPUTATION — NOT A CLEARANCE**
*(Q1-Q4 did not close IN; operator rule 3 header governs; no entry language.)*

**THE FLOOR [E4-28] — "that's the figure we quit on."**

**1. THE YIELD** (owner earnings ÷ market cap $1,966M · sovereign **5.19%**):
| OE basis | OE | yield | points over sovereign |
|---|---|---|---|
| Basis A, all-growth-charged | $35-46M | 1.8-2.3% | −3.4 to −2.9 |
| **Bottom boundary, re-based [E5-34, E4-41]** | **$110-150M** | **5.6-7.6%** | **+0.4 to +2.4** |
| 3-yr NI mean (refused, shown) | $247M | 12.6% | +7.4 |
| 5-yr NI mean (boom junk, shown) | $353M | 17.9% | +12.8 |

**2. WHAT THE PRICE ALREADY ASSUMES:** $1,966M × 10% floor = $197M of OE, i.e. a
~40-45% earnings recovery from TTM toward FY2023-24 incentive levels, held permanently.
Believing that is a mortgage-rate forecast, which this framework does not make
[E3-32], and a growth bet carrying [E4-35]'s burden. On the builders' yardstick
[E5-31]: price 0.77× book; even the discount does not clear the floor at trough
returns (5.7% ROE ÷ 0.77 ≈ 7.4% earnings yield on price). The ceiling [E2-63] is
stated: a commodity cyclical's mean return caps the upside unless capital is
continuously reinvested at good returns, and the row says CCS's marginal return in the
revealing year is 8th of 9.

**3. WHAT YOU ARE PAID:** +0.4 to +2.4 points over the sovereign at the re-based
bottom boundary, BEFORE crediting any recovery; the recovery is the entire bull case
and it is a rate call.

**THE FLOOR VERDICT, stated plainly as tasked:** honest pre-tax expectancy at $69.16 ≈
bottom-boundary yield 5.6-7.6% plus single-digit dividend growth minus cycle risk ≈
**6-8%. The floor does not clear.** It clears only on the 3-yr or 5-yr means that
[E4-41] instructs this run to refuse, or on a rate-recovery belief refused under
[E3-32]. Bar: screamer test only [E4-01]; the price sits INSIDE the wide range (below
a flat-forever capitalization of the bottom boundary, far above the floor-clearing
price), which is the middle box: **no useful conclusion; move on.** Windage count:
**one** — the incentive-drift shave inside the bottom boundary's low end; the
re-basing itself is [E5-34]'s and [E4-41]'s required moves, not windage.

**The value, as a round-number range [E4-01], for the record only:** roughly
**$1.1-1.5B** (bottom-boundary OE at the floor rate, the quit-on price) to roughly
**$2.1-2.9B** (bottom boundary held flat forever at the bare sovereign); cap $1,966M
sits inside. Too wide to conclude on, and that is the conclusion [E4-25].

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*(No position exists; pre-committed yardsticks for the WATCH LIST, set prior to any
act [E1-02]. **Alert thresholds LISTED ONLY** — `tools/alerts.json` not edited.)*

**Q2 REOPEN CONDITIONS (the only route back to entry) — BOTH required:**
1. **Evidence, not price:** Q2 failed on CLASS, so the reopen bar is structural, not
   cyclical: filed evidence of a wide-and-sustainable cost position — sustained
   trough-year returns in the top quartile of the row (the DHI/NVR pattern), or a
   disclosed capital-model change of the NVR/DFH kind. Note the current direction is
   the wrong way (owned lot share 44.3% → 57.1%). A demand recovery alone reopens
   nothing; it re-rates every builder in the row identically.
2. **Price [E4-28]:** the re-based bottom boundary pays the floor with zero growth
   credited at **$1.1-1.4B ≈ roughly $39-49/share** (≈0.45-0.55× current book, the
   deep-trough builder multiple). Below ~$49 this file gets re-read for the record;
   entry still requires condition 1, which today does not exist.

**Watch-list metrics and thresholds (review triggers, not auto-executions):**
- **Margin line:** homebuilding GM below 16.5% in any quarter (a full point below the
  filed mid-cycle base) = death 1 accelerating; above 20% for a year = regime change,
  re-read the row.
- **Order book:** two consecutive quarters of net new contracts −10% or worse
  year-over-year = death 3 forming (spec WIP vs backlog checked in the same read).
- **Impairment machinery:** quarterly impairments + abandonments above $25M = death 2
  beginning; also watch the adjusted-measure definitions for a third switch [E2-49].
- **ARM share of Inspire originations:** above 50% = the affordability manufacture
  deepening; any repurchase-reserve build = the channel turning.
- **Balance sheet:** homebuilding debt/capital above 40%, or the revolver above $500M
  drawn outside Q1-Q2 seasonality = staying-power leg 2 eroding.
- **Dividend:** any cut to the $0.32 quarterly = the [E2-60] arithmetic biting (also
  the event that would drop the price toward the re-read band).
- **Capital conduct:** buybacks continuing below ~0.8× book = the rational pattern
  holding; buybacks above book or a large land-bank M&A deal = conduct downgrade.
- **Price alert (list only):** CCS below **$49** → re-run both reopen conditions.
- **Next catalysts:** Q3-2026 10-Q ~late Oct 2026 · FY2026 results + initial FY2027
  guidance ~late Jan 2027 (the next [E3-48] data point) · FY2026 10-K ~Jan-Feb 2027 ·
  DEF 14A ~Mar 2027. Monthly housing starts and rate prints: context only, never a
  trigger [E3-32].

**The taxable never-switch test, answered as tasked [E2-46, E3-64]:** the earmarked
account is TAXABLE and wants a never-switch compounder taxed once at the end. **CCS is
structurally not that name, independent of price.** A commodity cyclical's return
arrives by buying below book at the trough and having the discount close; [E2-28]'s
first sell trigger (market judges the business above the facts) is EXPECTED to fire
every cycle top, so the holding is born with a sell discipline, i.e. with the tax
friction the account exists to avoid. The dividend half is real but small (1.9% at the
quote, ordinary income); the compounding half is the cycle's, not the company's. **CCS
does not qualify for this account's mandate even if it re-rated.**

**The dividend-at-mid-cycle answer, as tasked:** the $1.28/yr rate (~$37M) is **26-33%
of re-based mid-cycle owner earnings ($110-150M): covered, with room** — this is the
rare name where the statute payout survives the [E4-41] re-basing, because the worst
year in the window is itself a normal-rate year. The honest caveats: H1-2026 paid the
dividend (and buybacks) out of the revolver while OCF ran negative (seasonal, but
filed); and mid-cycle dividend GROWTH is 10-12%/yr at best, not the sweep's 33%,
which is an initiation artifact. A safe small dividend on a cyclical is not a
dividend that compounds.

- **VERDICT: [x] IN** — what would prove this run wrong is written, dated, and
  document-named on both sides (structural evidence + price for reopen; margin,
  orders, impairments, ARM share for the class thesis).

---
## SELF-AUDIT
- [x] Questions answered in order; stopped at the first non-IN (Q2 OUT); Q3-Q5 written
      for the record only, headed COMPUTATION — NOT A CLEARANCE per operator rule 3
- [x] No question marked IN carries an "unverified" or "provisional" caveat
- [x] Market cap verified against the sweep as tasked ($1,966M vs ~$1,958M, 0.4% gap,
      price-date drift; filed cover share count × dated aggregator quote, flagged)
- [x] Step 0: filings read with accession numbers; FY2025 OCF cross-checked three ways
      ($153,081K statement = MD&A = XBRL); H1-2026 OCF cross-checked twice
- [x] Owner earnings on multi-year display: both land-spend bases disclosed as the
      judgment [E2-23] requires; all four windows shown with the spread; the 5-yr and
      3-yr means refused under [E4-41] IN WRITING; SBC subtracted in full; (c) band
      shown
- [x] The pre-recorded [E4-41] flag tested and answered both ways (payout survives;
      growth CAGR does not)
- [x] Competitor row: 8 of ~10-12 peers, committed as a separate research file; XBRL
      transcription labelled as such; subject cross-checked to filings; GRBK/DFH gap
      recorded as a work order
- [x] Sovereign for the earnings currency (USD) from the issuing-authority series
      (FRED DGS30), dated 2026-08-27; tools/sources.py USD failure recorded
- [x] Value stated as round-number ranges; the too-wide range identified as itself the
      conclusion [E4-25]; floor verdict stated plainly
- [x] One bar (screamer, for the record); windage count: one, justified in writing
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Q6 written regardless, alerts LISTED ONLY, taxable never-switch test answered
- [x] The market-beating claim not made anywhere; judgments carry ledger ids or are
      labelled judgments/estimates
- [x] Operator-brief factual slip (founder names) corrected against the filing
- [ ] Run committed to git — pending

## REGISTER
- Verdict: **[x] OUT (about the business, at Q2 — for entry).** No position held.
  Q3 for the record: no honesty disqualifier found; guidance culture, two
  deterioration-following metric switches, and adjusted-measure promotion converge and
  the gate would not clear. Q4 for the record: survives the regime; the class's
  impairment death is permanent exposure. Q5 computation: floor fails at the re-based
  bottom boundary (5.6-7.6% vs 10%).
- One line: **a competently run, honestly accounted, decently financed maker of the
  world's most substitutable big-ticket product — its own 10-K concedes low barriers
  to entry, its pricing is incentives all the way down, its trough return is 8th of 9
  in its row, and the dividend, though genuinely covered at mid-cycle, grows at 11%,
  not the sweep's 33%; the statute yield's payout half survived re-basing and the
  compounding half did not.**
- **Work orders (UNRESEARCHED):** (1) GRBK and DFH competitor rows — EDGAR
  companyfacts, ordinary retrieval (row file); (2) peer same-window homebuilding gross
  margins — each peer's 10-K MD&A, EDGAR, ordinary retrieval; (3) FY2026 10-K (~Jan
  2027) — refresh TTM figures, ARM share, impairments, and the [E3-48] guidance
  ledger; (4) 2027 DEF 14A (~Mar 2027) — comp trajectory and any say-on-pay
  deterioration. None blocks the verdict; Q2 is decided on the subject's own filed
  concessions plus eight rows.
- **The single biggest concern:** the affordability machine — a spec builder whose
  buyer is defined by being barely able to buy, holding ~$1.0B of unsold homes under
  construction and 3.3 years of owned lots on a 34%-levered balance sheet, now
  manufacturing demand through its own mortgage desk with adjustable-rate loans at 35%
  of originations (up from under 5% eighteen months ago), while its non-GAAP
  definitions quietly widen in the exact quarters the cycle turns. Nothing about that
  is dishonest, and nothing about it is a franchise; it is the 2008 exposure set
  [E4-40], reassembled at entry-level price points, held by a company that was private
  the last time the tide went out.

*This file is a judgment by the AI running the framework; underlying facts are the
FY2025 10-K (acc. 0001576940-26-000005), the Q2-2026 10-Q (acc. 0001576940-26-000057),
the Q1-2026 10-Q (acc. 0001576940-26-000026), the 2026 DEF 14A (acc.
0001140361-26-011011), the 2025-01-29 and 2026-07-22 earnings 8-Ks, the FY2019/FY2021/
FY2023 10-Ks cited in Step 0, eight peer XBRL fact sets in the committed row file,
FRED DGS30, and one flagged live quote. Where a number is a judgment or estimate — the
land-spend basis choice, the bottom-boundary band, the 100bp-of-margin arithmetic, the
reopen band — it is labelled as one.*
