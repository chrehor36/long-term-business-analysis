# Company Run — Chevron Corporation (NYSE: CVX) — 2026-09-02
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**Position context: NONE HELD. Fresh entry run**, surfaced from `Screens/WATCHLIST RUN QUEUE.md`
TIER 2. The operator's brief names this **the strongest Q2 candidate the energy cohort will
ever offer** and instructs, per [E4-26], that the disconfirming case against the expected
Q2 OUT be built at full strength.

**Screen input, reproduced as received and headed as what it is — a COMPUTATION** (row 104,
`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, reproduced 2026-09-02): cap $398,197M ·
OE bottom $15,433M · OE top $21,774M · spread **41.1%** · yield bottom **3.88%** · growth
required **6.12%** · level_shift **"no step"** (ratio 1.2) · best-year dependence 8.3% ·
acquisition note: *"NET CASH INFLOW on the acquisition line ($3,973M, 1% of cap) — cash
acquired exceeded cash paid."*

**TWO DEFECTS IN THE SCREEN ROW, FOUND ON REPRODUCTION, BEFORE ANY GATE OPENS:**
1. **The cap is built on an EPS denominator, not a share count.** `run.py` prices CVX off
   `WeightedAverageNumberOfDilutedSharesOutstanding` = **1,856.0M** — a FY2025 weighted
   average that blends ~6.5 pre-Hess months (~1.79bn shares) with post-Hess months (~2.04bn).
   The 10-Q cover (filed 2026-08-06) says **1,975,771,274**. The screen cap is ~5% too small
   and its 3.88% yield is overstated by the same ratio.
2. **The acquisition flag is blind exactly as documented.** Hess was a **stock** deal
   (~$53bn); the cash-flow statement's acquisition line shows a **net cash INFLOW of
   $3,973M** (Hess's cash on hand exceeded the cash element of consideration), so
   `acquisition_flag()` reads a $53bn perimeter event as "1% of cap." The DKS/Foot Locker
   shape, invisible to the tool. **The perimeter question is worked before Q1.**

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
# STAGE 0 — SHARES, PRICE, DIVIDEND — by hand, before any gate

## (a) The cover count, by hand
- **1,975,771,274 shares of common stock outstanding on June 30, 2026** — Q2 2026 Form 10-Q
  cover, verbatim: *"There were 1,975,771,274 shares of the company's common stock
  outstanding on June 30, 2026."* Accession **0000093410-26-000167**, filed 2026-08-06.
- **Single class.** One line under Section 12(b): common, $0.75 par, NYSE. Preferred
  authorized (100M shares), **none issued** (balance sheet, both dates).
- Reconciliation: 2,442,676,580 issued − 448,260,458 treasury = **1,994,416,122** at
  YE2025 (FY2025 10-K balance sheet); H1-2026 net repurchases of $4,480M bring the cover
  to 1,975.8M. Coherent. `cover_shares.py` agrees with the hand read.
- The count is **64 days old** at the run date; H2 buybacks continue (~$2-3bn/qtr), so the
  true count today is slightly LOWER and the cap below slightly overstated — conservative
  in the yield's favour by well under 1%.

## (b) The price and the cap
- Price **$211.78, NYSE close 2026-09-02** *(Yahoo chart API — aggregator, live quote only,
  flagged; snapshot `_research 2026-09-02 CVX/CVX_price_2026-09-02.txt`)*.
- **That close is the 52-week HIGH** (range $146.75–$211.78). The run is priced at the top
  of the year's range, stated before any yield is computed.
- **Market cap = 1,975,771,274 × $211.78 = $418,429M.**
- The screen's cap of $398,197M is **5.1% too small** — built on the FY2025 weighted-average
  diluted share count (1,856.0M), an EPS denominator that blends ~6.5 pre-Hess months. Every
  screen yield below is restated on the cover cap.

## (c) The dividend — regular vs special, and the record
- **38 consecutive years of annual per-share dividend increases** — FY2025 10-K, verbatim:
  *"The 2025 annual dividend was $6.84 per share, making 2025 the 38th consecutive year that
  the company increased its annual per share dividend payout."* Raised again January 2026 by
  $0.07 (~4%) to **$1.78/quarter = $7.12 annualized**.
- All regular quarterly; no specials in the filings read. Yield at $211.78: **3.36%**.
- No COLM/WEYS-shape artifact: no cut in the window, the base is not a survivor's penny.

---
## THE PERIMETER — HESS, WORKED BEFORE ANY GATE (the DKS/Foot Locker shape)

**On July 18, 2025 Chevron closed the acquisition of Hess Corporation.** FY2025 10-K,
Note 29, verbatim: *"The aggregate purchase price of Hess was approximately $48 billion,
including 15.38 million shares of Hess common stock purchased in open market transactions in
the first quarter of 2025 and 301.25 million shares of Chevron common stock issued as closing
consideration in July. As part of the transaction, the company assumed debt with an aggregate
outstanding principal value of $8.8 billion. The shares issued represented approximately 15
percent of the shares of Chevron common stock outstanding immediately after the transaction
closed."* No goodwill or bargain purchase was recognized; PP&E was stepped up to a $73.5bn
fair value.

**CORRECTION TO THE BRIEF: the filed purchase price is ~$48bn, not "roughly $53bn."** The
$53bn is the October 2023 announcement-day value; the filed ASC 805 aggregate is $48.0bn,
of which $2,225M was cash for the open-market Hess shares — so "a stock deal" is right in
substance (94% of consideration) but the filed number is the one this run uses.

**The tool blindness, confirmed on the filed statement:** the FY2025 cash-flow statement
shows *"Acquisition of businesses, net of cash received"* as a **positive $1,056M inflow**
— Hess's cash on hand exceeded the cash element at close — and the $2,225M open-market
purchase sits on its own line. `acquisition_flag()` therefore scored a $48bn perimeter event
at ~1% of cap. The documented limit, observed live.

**What Hess contributed since close (Note 29):** revenue **$5,957M**, net income
attributable **$193M** — five and a half months, ~1.6% of FY2025 net income, on ~15% of the
shares. The step-up D&A is the main reason (FY2025 consolidated D&A jumped $2.85bn to
$20,132M; the 10-K attributes upstream earnings declines to *"higher DD&A"* on both US and
international pages, *"all figures inclusive of Hess"*).

**The filed pro forma (Note 29), combined company as if 2024-01-01:**

| $M | FY2025 | FY2024 |
|---|---|---|
| Revenue | 189,416 | 204,300 |
| Net income attributable | **12,464** | **19,003** |

**Do the pre-close history and the post-close cap describe the same company? NO, and the
run therefore builds owner earnings pro forma below (Q4)** — Chevron-standalone history
plus Hess-standalone history from Hess's own 10-Ks (FY2022–FY2024, accessions
0001628280-23-005059, 0001628280-24-006845, 0001628280-25-008716, and the Q1-2025 10-Q
0001628280-25-023790), exactly as the DKS run built Foot Locker's. The share count already
carries the 301.25M new shares; an owner-earnings series that stops at Chevron-standalone
would divide one company's earnings by another company's share count.

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- **USD 30-year par yield: 5.27% · 2026-09-02 · US Treasury daily par yield curve, from the
  issuing authority** (`home.treasury.gov` daily CSV, fetched 2026-09-02; local copy
  `_research 2026-09-02 CVX/treasury_par_curve_2026.csv`; the 09-01 observation the screen
  used is also 5.27% — identical).
- FX: none. Quote and earnings both USD. International volumes (Kazakhstan, Australia,
  Guyana, Nigeria, Angola) sell into dollar-denominated markets; the filing reports USD.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A (realizations, production, liquidity, capex, sensitivities) [x] cash-flow
  statement incl. detail lines [x] footnotes (Note 29 Hess; debt; SBC; segments)
  [x] Supplemental Oil and Gas Information, Tables I–VII
- Documents:
  1. **FY2025 Form 10-K**, period 2025-12-31, filed **2026-02-24, accession
     0000093410-26-000078**
  2. **Q2 2026 Form 10-Q**, period 2026-06-30, filed **2026-08-06, accession
     0000093410-26-000167**
  3. **DEF 14A**, filed **2026-04-07, accession 0001193125-26-145617**
  4. Hess standalone filings as listed in the perimeter section above
- Figures cross-checked against the filed statement: **FY2025 Net Cash Provided by
  Operating Activities $33,939M** — filed Consolidated Statement of Cash Flows reads
  *"33,939 | 31,492 | 35,609"* for 2025/2024/2023; SEC XBRL carries identical values;
  the screen's OCF column ties to the dollar. **FY2025 capex $17,347M** ties the same way.
  **Share count** cross-checked cover-vs-balance-sheet above. **Ties, three lines.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Chevron lifts oil and gas out of
the ground and sells it at the posted price of the day; then a second, smaller business buys
crude (much of it its own), refines it and sells fuel; a third, held through equity
affiliates (CPChem, GS Caltex), makes chemicals. In 2025 the upstream produced roughly
**3.6 million Boe/day** (reserve-table basis 1,359 MMBoe incl. affiliates) and realized
**$63.22/bbl for crude, $18.91/bbl for NGLs and $4.86/Mcf for gas** (consolidated worldwide,
Table IV) against **average production costs of $9.71/Boe** — at TCO in Kazakhstan just
**$3.80/Boe**. Everything between those numbers, minus $18.4bn of upstream DD&A and the
drilling capital, is upstream earnings: **$12,822M after tax in 2025 — 104% of consolidated
net income attributable ($12,299M)**. Downstream earned $3,022M; corporate and interest
consumed $3,545M. The upstream IS the company; the refineries are a working-capital-heavy
sideline that damps (not offsets) the crude cycle.

Money is made or lost on three things Chevron chooses — where to drill (Permian, Guyana,
Kazakhstan, Gulf of America, Australia LNG), what to pay for reserves (PDC $10.6bn 2023,
Hess $48bn 2025), how much debt to carry — and one thing it does not choose: **the price.
Brent averaged $81 in 2024 and $69 in 2025 and consolidated ROCE went 10.1% → 6.6% on the
company's own published table.** Per-segment sensitivity is not separately filed the way
OXY files its $240M/$1-WTI line, but the mechanism is identical and filed in words: the
10-K's own risk factor is that prices *"may adversely affect"* everything.

- **The scarce input this business controls: none.** Same finding as OXY and MTDR, carried
  on the same evidence class: the MD&A quotes its own realizations against Brent/WTI/Henry
  Hub benchmarks; acreage is bought at auction (PDC, Hess, lease sales); the one
  arguably-scarce asset — TCO's Tengiz field and the Stabroek block in Guyana — is held
  under **concession/PSC from sovereigns**, at their terms, for a term.
- **Will the fundamentals look broadly the same in ten years?** The mechanics yes: rock,
  decline curves, a screen price, refining spreads. The level, no — set by a price the
  filer states it cannot forecast. [E3-31] splits exactly as it did at OXY: **simple, not
  stable in character.**
- Q1 asks whether I can understand it, not whether I like it. I can: the filings are
  complete, the unit economics are transparent, the whole company can be recomputed from
  Tables I–VII. The instability is recorded and carried to Q2, where the corpus files it.

- **VERDICT: [x] IN.** The business is understood. (The OXY run's ruling is precedent:
  marking a commodity producer OUT at Q1 would smuggle the moat verdict into the
  understanding gate.)

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The operator's prior, stated before the evidence [E4-26]: this is "the strongest Q2
candidate the energy cohort will ever offer," and the disconfirming case must be built at
full strength before any verdict. It is built first, below, from the filings.**

### THE DISCONFIRMING CASE AT FULL STRENGTH — the four pillars, each from the filing

**Pillar 1 — the Permian position.** The 10-K, Item 2, verbatim: *"As one of the largest
producers in the Permian Basin, Chevron continues to develop its advantaged portfolio of
more than 1,750,000 net acres in the Delaware and Midland basins … In 2025, production
reached one million barrels of net oil-equivalent per day"* — and the highlights page:
*"Grew production in the Permian Basin by more than 10 percent with lower Capex compared to
the prior year."* Volume up double digits on falling capital is a genuine capital-efficiency
achievement, filed. *(The brief's "royalty-advantaged acreage" is an investor-deck claim —
the words "royalty advantage" appear nowhere in the 10-K; the filing says "advantaged
acreage holdings" without quantifying the royalty burden. Recorded as a BRIEF DEFECT: the
claim cannot be cited from the document this run is allowed to use.)*

**Pillar 2 — TCO complete and harvesting.** Filed, and true: *"In 2025, TCO completed the
Future Growth Project (FGP) at the Tengiz oil field, which increased crude oil production by
260,000 barrels per day with a total gross output of one million barrels of oil-equivalent
per day."* TCO's production cost is **$3.80/Boe** (Table IV) — the cheapest barrel in the
portfolio and among the cheapest on earth. The harvest is visible on the cash-flow
statement: *"Distributions more (less) than income from equity affiliates"* swung to
**+$2,282M** in 2025 and affiliates repaid **$778M** of loans; affiliate capex at TCO fell
**$2,278M → $1,480M → $577M** over three years.

**Pillar 3 — 38 consecutive years of dividend increases**, verbatim in Stage 0(c). No other
name this queue has run carries a payout record like it.

**Pillar 4 — the balance sheet.** Verbatim: *"The securities that are the obligation of, or
guaranteed by, Chevron Corporation carry an AA- rating by Standard and Poor's Corporation
and an Aa2 rating by Moody's Investors Service."* Net debt ~$34.5bn against $186.5bn of
equity (YE2025); gearing far below SHEL (20.7%), BP (23.1%). *(SECOND BRIEF DEFECT: "the
only AA-rated balance sheet in the peer set" is NOT VERIFIABLE from the filings read — no
peer rating was extracted, CVX's own filing claims no uniqueness, and XOM is conventionally
rated at the same Aa2/AA- level. The pillar stands as "AA-rated"; the "only" does not.)*

**And the strongest live fact: H1-2026 operating cash flow was $25,147M against $13,765M in
H1-2025** (Q2 10-Q), with 2026 production guided **+7-10%**. At the mid-2026 strip the
combined company is a cash machine.

### THE THREE CRITERIA **[E3-03]** — where the pillars have to cash

- **(1) Needed or desired — [x] YES.** Unambiguous.
- **(2) No close substitute — [ ] FAILS.** A Chevron barrel has a *perfect* substitute: any
  other barrel of like grade at the same delivery point. The filer prices its own output by
  reference to benchmarks it does not set: the MD&A leads its Business Environment section
  with the Brent/WTI/Henry Hub chart (*"The Brent price averaged $69 per barrel for the
  full-year 2025, compared to $81 in 2024 … The majority of the company's equity crude
  production is priced based on the Brent benchmark"*), and its published ROCE went
  **11.9% → 10.1% → 6.6%** as that benchmark fell — the company's own two tables, read
  together, are the criterion-2 answer.
- **(3) Not subject to price regulation — technically YES, and the brief's head-on question
  is answered head-on: Chevron does not set its price. OPEC+ and the strip set it.** The
  10-K's own words: crude prices were lower in 2025 *"driven by supply growth in non-OPEC
  countries and slowing demand … and OPEC+ supply decisions"* — and **21% of Chevron's own
  2025 production is inside OPEC+ countries** (Kazakhstan, Nigeria, Eq. Guinea, Partitioned
  Zone, Malaysia), i.e., a fifth of its output is subject to someone else's administered
  supply decisions while its price is set by them everywhere. Under [E2-59] the only regime
  that ever floored this class is an administered-price regime Chevron does not belong to.

**0 of the 3 that matter. The pillars now have to survive [E2-58]'s one exception.**

### **[E2-58]** — the commodity equation, and the one exception tested on the row

*"persistent over-capacity without administered prices (or costs) equals poor profitability"*;
the exception: *"a cost advantage that is both **wide and sustainable** … By definition such
exceptions are few."*

**THE COMPETITOR ROW — required [E3-28].** Peers taken: **six of the industry's roughly
eight real comparables — XOM, SHEL (20-F), TTE (20-F), BP (20-F), COP, OXY** (ENI and
Equinor not taken; said per the template). Every figure from each filer's own FY2025 filing;
accessions and full workings in `_research 2026-09-02 CVX/peer_row_computed.md` and the
per-peer extract files.

**Row 1 — the return on capital, same basis (NI attributable ÷ avg(total equity + total
debt), computed identically from each balance sheet), FY2025, with each filer's own
published metric beside it:**

| filer | same-basis | filer's own published metric |
|---|---|---|
| XOM | 9.27% | ROCE **9.3%** (FY24 12.7%) |
| COP | 9.02% | — |
| TTE | 7.45% | ROACE **12.6%** (FY24 14.8%) |
| SHEL | 7.02% | ROACE **9.4%** (FY24 11.3%) |
| **CVX** | **5.99%** | **ROCE 6.6%** (FY24 10.1%, FY23 11.9%) |
| OXY | ~4.0% | — |
| BP | 0.04% (IFRS profit $55M) | "underlying" ROACE 13.9% — the definitional chasm is itself a finding |

**Chevron is LAST of the five majors on its own published metric, in FY2025 AND FY2024, and
5th of 7 on the same-basis computation.** The attacker metric (return on unleveraged net
tangible operating assets, average basis): **CVX 5.5% vs XOM 7.9%** on the identical
construction. [E3-46]'s "very high returns on capital employed" is answered by the filer's
own table: 6.6%, against a 5.27% government bond.

**Row 2 — replacement economics, 3-yr FY2023-25, each filer's own supplemental tables,
6 Mcf = 1 Boe** (the booking-convention caveat from the OXY run carried: drill-bit ratios
are not perfectly comparable across filers; the pattern below survives it):

| filer | organic replacement (drill bit) | drill-bit F&D $/Boe | reserve life, yrs |
|---|---|---|---|
| FANG | 168.9% | $8.03 | 10.8 |
| DVN | 135.3% | $9.84 | 7.9 |
| **XOM** | **127.2%** | **$12.53** | **11.0** |
| EOG | 126.5% | $11.29 | 12.2 |
| OXY | 65.1% | $18.28 | 8.8 |
| **CVX** | **43.7%** | **$27.12** | **7.8** |
| COP | 32.6% | $51.23 (books adds via revisions) | 9.6 |
| TTE / BP / SHEL | RRR 116% / 90% / n.p. (company-stated) | n/e | 12.2 / 7.2 / 7.6 |

**Chevron replaced 43.7% of production with the drill bit over three years, at the highest
finding cost of any filer whose number is not a booking artifact — and its own MD&A
publishes the honest long-window version: reserve replacement 91% over five years and 95%
over ten** (FY2022 10-K: 92%/99%; FY2019 10-K: 106%/101% — the ten-year ratio has fallen
across three successive triennial filings). Including revisions makes 2023 *worse*
(negative), not better: all-organic 3-yr is 39.3%.

**Row 3 — unit costs (the exception's direct test):** CVX consolidated production cost
**$9.71/Boe** (2025), XOM $10.20 (incl. equity cos), OXY LOE $8.94. **Parity, not width.**
The one genuinely wide cost position in the portfolio — TCO at $3.80/Boe — is 50%-owned,
non-controlled, in Kazakhstan, exported through a pipeline with filed drone-attack risk,
**under a concession that the 10-K states expires in 2033**, with no filed renewal.

> **THE EXCEPTION FAILS.** [E2-58] demands a cost advantage *wide and sustainable*. The row
> shows unit-cost parity, a last-place return on capital among the majors, and replacement
> economics that are the worst honest number in the row. The one wide advantage (TCO) has a
> contractual sunset seven years out; the second (Guyana, via Hess) was **bought at auction
> for $48bn four months before this run** — [E2-45]'s answer: the attacker with ample
> capital does not compete with Chevron, he outbids Chevron (XOM took Pioneer for $63bn in
> stock the year before; CVX took Hess; the "moat" is a bid).

### **[E4-04]** — must the moat be continuously rebuilt? The excluded class, quantified

- **Reserves per share fell 7.6% over nine years** (6.20 → 5.73 Boe/share) while production
  per share rose 38.9% — the [E4-55] physical series, nine years, three 10-Ks, in
  `peer_row_computed.md`. A business producing faster per share while holding fewer barrels
  per share is consuming its basis.
- Total proved reserves at YE2025 (10.59 BnBoe) are **below YE2023 (11.07) even after
  putting ~1.4 BnBoe of purchased Hess barrels in** (Stabroek 666 MMBoe, Bakken ~583).
- Reserve life **7.8 years** — shortest of the US peer set.
- The 2033 TCO sunset is [E4-04] in its purest form: 11% of proved reserves sit in a moat
  with a filed expiration date.
- The spending does not defend the same advantage; it **buys its replacement** (Rhodes
  Ridge): Noble 2020 (stock), PDC 2023 ($10.6bn of the $10.63bn property-acquisition line),
  Hess 2025 ($48bn, $73.7bn of stepped-up costs incurred). Three acquisitions in six years
  to hold the reserve base roughly flat per the company's own 91-95% replacement ratios.

### The pricing tests — none can be run in Chevron's favour
- **Untapped pricing power [E3-33]/[E5-28]: none, structurally.** ~3% of world liquids
  supply; not a monopoly by any measure.
- **The inverse metric [E4-37] cannot be run at all** — there is no price deliberation to
  observe. Same reading as OXY and MTDR.
- **Two-characteristic test [E2-44]: 0 of 2.** Prices cannot be raised at flat demand; and
  growing dollar volume takes **$18-19bn of guided 2026 organic capex** on a $418bn cap.
- **Dominance class [E2-53]: unavailable** — the marketplace, not Chevron, sets how good or
  bad the year is; the ROCE series is the proof.
- **Direction [E4-32]: negative on position, positive on execution.** Unit costs −15%
  nominal over nine years (real ~−35%) — genuine. Reserve life, reserves/share, RRR
  five-and-ten-year, ROCE-vs-peers: all pointing down. [E2-37] governs what execution can
  be worth: *"a textile company that allocates capital brilliantly within its industry is a
  remarkable textile company — but not a remarkable business."*
- **Real price series [E4-55 deflated]:** worldwide crude realization $48.61 (2017) →
  $63.22 (2025): roughly **flat to −1% in real terms** across nine years, with a $37-$93
  oscillation inside it. The gains from industry-wide efficiency flowed to buyers —
  [E3-62]'s second step, exactly as at OXY.

### Where the four pillars actually file
1. Permian capital efficiency → **execution**, [E2-37]: promotes nothing at Q2.
2. TCO → a **wasting contract**, not a moat: NI fell 57% in the completion year ($6,569M →
   $2,496M, Note 7), and the concession dies in 2033.
3. 38 years of dividends → a **capital-allocation output**, filed at Q3; [E3-03] tests the
   product, and the product is a commodity.
4. AA-/Aa2 → **staying power**, filed at Q4 [E5-11]; [E2-59]: a strong balance sheet does
   not administer prices.

**[E3-61]'s limit recorded:** the row shows position, not conduct — and this industry's
conduct is [E2-27]'s: every operator's individually rational barrel is collectively the next
glut; the 10-K names OPEC+ *supply growth* as what broke the 2025 price.

- Class: [x] **NONE** · Direction: negative on every metric that is a claim about position
- **VERDICT: [x] OUT.** Three independent filed grounds, any one sufficient:
  1. **[E3-03] criterion 2** — a perfect-substitute product priced off a benchmark the
     filer does not set, confirmed by the filer's own Brent-chart-plus-ROCE presentation.
  2. **[E2-58]** — the exception requires a wide and sustainable cost advantage; the
     six-peer row returns unit-cost parity, last-of-the-majors ROCE (6.6%, the filer's own
     table), and 43.7% drill-bit replacement at $27/Boe.
  3. **[E4-04]** — the excluded class: depleting basis, reserves/share −7.6% over nine
     years, 91-95% ten-and-five-year replacement by the filer's own MD&A, a $48bn purchase
     to hold the base, and 11% of reserves under a concession that expires 2033.

  **The ORLY precedent was applied: the disconfirming case was built first, at full
  strength, and it filed under execution, staying power and capital allocation — not under
  franchise. [E5-35]: entry is closed at any price. [E5-13]: most names should end here,
  and that is the system working.**

---
⛔ **Q3, Q4 AND Q5 DO NOT OPEN FOR ENTRY. Q1 IN · Q2 OUT — the hard sequence closes the file
for any BUY decision.** No position exists, so no [E2-28] hold read is required. Everything
below is **FOR THE RECORD**, per the queue's output contract; the price at the end sits
under operator rule 3's header and **nothing below is entry language**.

---
## Q3 — FOR THE RECORD: ARE THEY HONEST, AND ARE THEY RATIONAL?
*Standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Q2 OUT stands regardless — Q3 can
stop a run; it can never start one.*

**STEP 1 — THE WEIGHT CASE, declared before the evidence.**
- [x] **Daily execution — HIGH [E3-38, E3-43, E2-70].** A price-taker's only decisions are
  where to drill, what to pay for reserves, and how much debt to carry. *"a business,
  unlike a franchise, can be killed by poor management."* One mispriced $48bn acquisition
  is a decade of buybacks.
- [ ] Control — no; minority public-market position.
- [ ] Leverage — moderate, not bank-like: total debt $40,758M against $186,450M of common
  equity (YE2025); not ticked.

**One ticked → had Q2 passed, Q3 would have carried GATE weight, not overlay weight.**

**Honesty — binary, permanent, filings-based [E5-16].** No disqualifier found in the
filings read: no restatement in FY2023-FY2025; the Hess-related DOJ Clean Water Act matter
(February 2025, disclosed with a stated $1.0M+ penalty range) is inherited litigation,
disclosed; environmental accruals and the retained-liability structure are quantified in
the notes. Per [E5-17], written the way the corpus requires: **this is the absence of found
disqualifiers, not a finding that the managers are honest.**

**STEP 2 — THE FLAGS.** Each a prompt to read, never a verdict.
- [ ] EBITDA promotion **[E4-29]**: does NOT fire in the 10-K — earnings are presented on
  GAAP net income; ROCE/ROSE are reconciled from filed lines.
- [x] **Pay metrics engineered around the deal — the DKS/Foot Locker shape at 20x scale
  [E2-49].** The 2026 proxy defines the 2025 annual-incentive (CIP) measures as
  *"Consolidated Results / Results Excluding Hess Corp."* — ROCE, free cash flow, operating
  expense AND capex each carry a defined *"Results Excluding Hess Corp."* variant, and the
  proxy states the MCC's *"evaluation primarily compared legacy Chevron results against the
  legacy Plan assumptions."* Management issued 301M shares for a $48bn company in July and
  measured its own 2025 pay primarily without it.
- [x] **Target-vs-outcome (the DG/ULTA test): the MCC awarded a Corporate Performance
  Rating of 1.25 — 125% of target — for a year in which** net income fell 30.4%
  ($17,661M → $12,299M), published ROCE fell 10.1% → 6.6%, and the payout rationale is
  explicitly non-formulaic: *"instead of following a formulaic approach, taking a holistic
  view and applying disciplined judgment … is more meaningful."* The proxy's own framing —
  Plan assumptions set at Brent ~$82, actual under $70 — cuts both ways: a pay system that
  removes the commodity price from a commodity company's scorecard removes the business.
  [E2-57]: *"count the runs scored against you in all nine innings."*
- [x] **Serial share issuance — noted with its context [E5-15]:** three stock-financed
  acquisitions in six years (Noble 2020, PDC 2023, Hess 2025, ~360M shares combined),
  against a buyback that retired roughly the same. The register churns; the count is
  roughly where it was in 2017 (1,883M weighted then, 1,976M cover now — **up** 5%).
- [ ] Cash-tax tell [E4-30]: cash taxes paid $7,304M vs $7,258M expense (FY2025) — no gap.

**STEP 3 — THE PRIMARY TEST [E2-01].** ROCE series (the filer's own table plus prior
10-Ks): FY2022 ~20% (boom) → 11.9% → 10.1% → **6.6%**, and ROSE 7.3% (2025). A 6.6% return
on capital employed against a 5.27% sovereign is [E2-01]'s answer for the whole question:
the capital compounds at roughly the bond rate, with commodity risk attached.

**The institutional imperative [E2-30] — scored:**
- [x] projects/acquisitions materialise to soak up available funds — $48bn (Hess) closed in
  the same twelve months in which $12.1bn was repurchased and $12.8bn paid out; capex
  guided UP to $18-19bn for 2026.
- [x] peer behaviour mindlessly imitated — XOM bought Pioneer for $63bn in stock (May
  2024); Chevron closed Hess for $48bn in stock (July 2025). The industry consolidates in
  lockstep at the top of the ROCE cycle. *(Institutional dynamics, not venality.)*
- [ ] resists change — no; the OPEC+ line and capex flexibility statements read honestly.
- [ ] staff studies for the leader's craving — not observable from the filings read.

**Buybacks — the two conditions [E5-08]:**
- (1) Ample funds: yes — AA-/Aa2, $6.3bn cash, $9.9bn of ST debt classified long on
  committed facilities.
- (2) Material discount to conservative IV: **FAILS on this run's own arithmetic.** The
  FY2025 program spent $12.1bn at an average around $150-160; H1-2026 spent $4.5bn net
  while the price ran to a 52-week high of $211.78 — and the Q5 computation below values
  the business at roughly $130-180 at the bare sovereign on pro-forma owner earnings.
  **CAPITAL-ALLOCATION FLAG, stated with the humility clause [E4-13]:** this rests on our
  own IV range; management knows the business better than we do. Binds position size,
  never the rate.
- **[E2-60] checked:** FY2025 distributions $24,830M (dividends 12,751 + buybacks 12,079)
  against owner earnings computed below at ~$15-19bn, with total debt up $16.2bn in the
  year ($9.1bn assumed from Hess, $11.4bn issued, $5.5bn repaid). Ex-Hess the gap is
  roughly $6-9bn of distributions funded past earnings in a windfall-tail year. Fires as
  a **restricted-earnings caution**, not yet the AATC shape.

**The half-owner test [E2-26]:** passes on structure — Hess's contribution is quantified
separately (Note 29), the pro forma is filed, special items are itemized in Note 27, and
the segment tables reconcile to GAAP. The **proxy's** pay presentation is where the
half-owner standard is not met (above).

**THE GUARDRAIL.** Nothing here promotes. [x] Confirmed. The Q2 OUT is about the business
class [E2-37]; no manager repairs it.

- **VERDICT (recorded, not a gate): no integrity disqualifier found; TWO capital-allocation
  flags (pay-metric perimeter, buyback price) and one restricted-earnings caution
  [E2-60].** IN-equivalent for the record; promotes nothing.

## Q4 — FOR THE RECORD: WILL IT SURVIVE?

### Owner earnings — PRO FORMA, as the perimeter section requires **[E2-23]**

**The construction:** OCF − SBC − (c), Chevron-as-filed PLUS Hess-standalone for every
pre-close period (Hess 10-Ks FY2022/FY2024, Q1-2025 10-Q). The 2025 Hess stub
(Jan 1–Jul 17) is Q1 filed ($1,401M OCF, $1,012M capex) plus an estimated Q2-and-18-days ≈
Q1 — **an estimate, disclosed as one**; it moves the combined year by under 3%.

**Pro forma OCF and OCF−capex by year ($M):**

| yr | CVX OCF | HES OCF | PF OCF | CVX capex | HES capex | PF OCF−capex |
|---|---|---|---|---|---|---|
| 2021 | 29,187 | 2,890 | 32,077 | 8,056 | 1,747 | 22,274 |
| 2022 | 49,602 | 3,944 | 53,546 | 11,974 | 2,725 | **38,847** |
| 2023 | 35,609 | 3,942 | 39,551 | 15,829 | 4,108 | 19,614 |
| 2024 | 31,492 | 5,600 | 37,092 | 16,448 | 4,946 | 15,698 |
| 2025 | 33,939 | ~2,900* | ~36,839 | 17,347 | ~2,000* | ~17,400 |

*\*pre-close stub estimate as stated; CVX 2025 columns already include Hess from 07-18.*

**The DKS question answered: Hess ADDS, modestly.** Standalone OCF−capex: −$864M (2020),
+1,143, +1,219, −166, +654, +389 (Q1-25) — a business that roughly breaks even on cash
after its Guyana build-out, now past peak spend. The screen's non-pro-forma series was
biased slightly **down** on earnings and 5% **down** on the cap; net, its 3.88% yield was
overstated (corrected below).

- **Short-window mean** (3-yr, 2023-25, PF OCF): $37,827M
- **Long-window mean** (5-yr, 2021-25, PF OCF): $39,821M
- **[E4-41] — the windfall named and normalized DOWN:** 2022 (Brent $101, PF OCF−capex
  $38.8bn — 2.2x any neighbouring year) sits inside the 5-yr window; H1-2026 (OCF $25.1bn
  in six months) is a second live boom period. Favourable exogenous breaks are stripped:
  the **ex-2022 4-yr mean PF OCF is $36,390M**, and that is the mean the judgment uses.
- **SBC subtracted in full [E5-06]:** $472M (2025), $600M (2024), −$15M (2023, SAR
  mark-to-market); ~$500M used for unextracted years — 1.5% of OCF, immaterial at this
  scale. *(Screen defect: `run.py` tagged CVX SBC as zero — tag miss, immaterial here.)*
- **Working-capital increment:** inside OCF per the convention; CVX inventories are not
  LIFO-carved out; no separate increment added.

### Maintenance capex — THE DISCLOSED JUDGMENT **[E2-23 c.4, E5-20, E4-04]**

**Which case is this?** The [E5-20] exception class — but through the MTDR **production
channel**, and with a twist unique in this queue: **the D&A end is the CONSERVATIVE end.**
FY2025 D&A ($20,132M; full-year-Hess run-rate ~$21-22bn with the step-up) EXCEEDS total
capex ($17,347M), because ASC 805 wrote Hess's properties up to $73.5bn fair value and that
consumption now flows through D&A. The screen's "bottom" was the D&A end for this reason.

**The MTDR test — what does it cost to REPLACE a produced barrel, from the filer's own
tables:**
- Book upstream DD&A: **$15.87/Boe** (consolidated $18,445M ÷ 1,162 MMBoe).
- 3-yr drill-bit F&D: **$27.12/Boe** (booking-noisy — CVX books material adds through
  revisions; the all-organic-incl-revisions figure is $30.11).
- The filer's own capital answer: **2026 organic capex guided $18-19bn**, which management
  says delivers +7-10% reported growth — almost all of which is the mechanical full-year
  annualization of Hess. Underlying, $18-19bn holds the combined company roughly flat.
- **The SD comparison: depletion charged ($15.87) sits WELL BELOW drill-bit replacement
  cost ($27+), so on the reserve-replacement channel the accounting understates the true
  expense — but unlike SD, the capex-and-acquisition record covers the gap, because
  Chevron replaces reserves by BUYING them** (5-yr RRR 91% *including* Noble, PDC and
  Hess). The Rhodes Ridge finding from Q2, priced: ~$70bn of acquisitions over six years
  ≈ $11-12bn/yr of periodic replacement purchase on top of drilling capex.

**(c) JUDGED at $19,000M** — the top of the filer's own guided organic capex for the
combined company, which is the only filed number that holds combined volume flat.
**Disclosed caveat, per "(c) must be a guess": this understates full-cycle maintenance**,
because the drill bit alone has never held this reserve base (43.7% 3-yr organic
replacement); a (c) that includes the periodic acquisition spend would run $25bn+, at
which owner earnings on the normalized mean fall toward **$10bn** (yield ~2.5%). That
construction is reported in the range, not used as the central judgment, because the
acquisitions also bought growth (production +39%/share over nine years).

**Owner earnings, the windows × the band ($M):**

| construction | OE | yield on $418,429M |
|---|---|---|
| 3-yr mean, D&A end (~21,500 full-yr-Hess) | 15,827 | 3.78% |
| 3-yr mean, capex end (17,347) | 19,980 | 4.77% |
| **ex-2022 4-yr mean, (c) judged 19,000** | **16,890** | **4.04%** |
| 5-yr mean, (c) judged (windfall in) | 20,321 | 4.86% |
| 5-yr mean, capex end (windfall in, generous) | 22,021 | 5.26% |
| acquisition-inclusive (c) ~25,000, ex-2022 | ~10,900 | ~2.6% |

- **Combined range: ~$10.9bn to ~$22.0bn; judged central $16,900M (4.0%).** Spread ~68% on
  the conservative end (or ~39% excluding the acquisition-inclusive construction).
- **The spread is itself a Q4 finding [E5-11]:** the distorted years are named — 2022
  (windfall), 2025 (Hess perimeter + step-up D&A), H1-2026 (live boom).
- The capex band does NOT change the verdict: **every construction except the
  windfall-inclusive generous top sits below the 5.27% sovereign, and that top touches it
  exactly (5.26%)** — so [E4-25]'s width rule does not rescue or close anything the price
  hasn't already.

### Great, good, or gruesome? **[E4-20]**
- [x] **good, with the commodity asterisk — not gruesome.** Published ROCE: ~20% (2022) →
  11.9% → 10.1% → 6.6%; five-year mean ~11% spans the [E5-40] "quite satisfactory" line —
  but only the supply-tight years put it there, which is [E2-58]'s equation, not a
  franchise property. Not gruesome: over the cycle the capital earns above nothing and the
  dividend has been cash-covered in every year since 2021. Not great: 6.6% against a 5.27%
  bond in a $69-Brent year, with $18-19bn/yr of capital required.

### Staying power — score all three **[E5-11]**
- (1) **Large: yes. Reliable: NO.** OCF $10.6bn (2020) → $49.6bn (2022) → $33.9bn (2025) —
  a 4.7x swing set by an exogenous price. [E3-55] scoping as at OXY: this is not See's
  seasonality; the endgame of any given year is genuinely unknown.
- (2) **Massive liquid assets: PARTIAL FAIL, [E5-39] exercised.** Cash $6.3bn (YE25) /
  $8.5bn (H1-26) against $40.8bn of debt — and the liquidity architecture leans on
  strangers: **$4.6bn of commercial paper outstanding** (YE25) and **$9,941M of short-term
  debt classified as long-term** *"as evidenced by committed credit facilities"* (Note,
  verbatim basis). [E5-39] counts neither bank lines nor CP. The AA-/Aa2 rating is real
  strength; it is also precisely the "kindness of strangers" the corpus refuses to rely
  on. *(BRIEF DEFECT, third: "CVX's negative working capital" — working capital is
  POSITIVE at both dates: +$5.2bn YE2025, +$9.9bn at 2026-06-30. The CP-and-reclass
  structure was the right instinct; the stated fact was wrong.)*
- (3) **No significant near-term cash requirements: PASSES on contract, with one soft
  commitment named.** No UAL-shaped contracted wall; maturities are AA-spaced. But the
  38-year dividend streak ($12.8bn/yr) functions as a reputational commitment: the company
  itself lists dividend continuity ahead of buybacks in its stated priorities, and a
  streak like that is only ever broken at maximum pain.
- **Leverage, named and quantified [E4-16, E3-29]:** total debt $40,758M YE2025 →
  $37,075M at H1-2026; net debt ~$28.5bn; debt/equity 0.20. **[E2-54] coverage:** FY2025
  cash flow net of ample capex $16.6bn against $942M cash interest — **17.6x. Passes
  comfortably.** Even FY2020 (the worst year in the window) covered interest from OCF
  alone 14.7x.

### Name the specific way THIS business dies **[E2-27, E3-24]**
- **The mechanism: a supply-ample decade against a quasi-committed payout.** [E2-58]'s
  ratio inverts — say Brent at $50-55 for five-plus years (2015-2020 happened; 2020
  delivered OCF of $10.6bn against $8.9bn capex + $9.7bn dividends, a ~$8bn annual gap,
  borrowed). At that price deck the combined company runs roughly a **$10-15bn/yr
  financing gap** ($36bn normalized OCF scales with price: the FY2020 stress implies
  ~$15-18bn OCF at $45 Brent, against $14bn minimum capex + $12.8bn dividend). Five years
  consumes $50-75bn of balance sheet — the AA goes, then the streak goes, then the
  valuation identity built on 38 years of increases goes with it. **Likelihood: [x] a
  real possibility** — it is the 2015-2020 decade replayed on a bigger dividend.
- **The exposure, not the experience [E4-40]:** 21% of production inside OPEC+
  jurisdictions; **11% of proved reserves behind one Kazakh concession expiring 2033,
  exported through one pipeline (CPC) with filed drone-attack incidents**; Gulf Coast
  refining concentration; and the long-tail demand question the filer's own risk factors
  name. The TCO leg alone: $20.9bn of equity (CVX share) whose concession the filing shows
  no renewal for. A CPC interdiction year would remove roughly $1.2-2.9bn of equity income
  and the distributions with it — absorbable; the 2033 non-renewal is the quantified tail.
- **VERDICT (for the record): survival IN** — the company survives the named death's
  first decade at AA cost of funds; strengths score 1 of 3 clean, coverage 17x. **This IN
  is about solvency, not about the franchise, and promotes nothing.**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass. **Q2 returned OUT. Q5 does not open. The section below is the
queue's required price output under operator rule 3's header, with no entry language.**

---
# COMPUTATION — NOT A CLEARANCE

**The price, as the output contract requires.** One book, owner earnings against the bond,
bare sovereign 5.27% [E3-42] — no per-name premium.

**1. THE YIELD.** Pro-forma owner earnings $15.8bn-$22.0bn (judged, [E4-41]-normalized,
**$16.9bn**) ÷ cover-count cap **$418,429M** = **3.78% to 5.26%, judged 4.04%**, against a
**5.27%** sovereign. Every construction is at or below the bond; the single construction
that touches it (5.26%) needs the 2022 windfall in the mean AND the generous capex end of
(c). *(Screen restated: its 3.88% bottom yield becomes 3.78% on the true cover cap — two
errors partially offset: cap 5% too small, Hess pre-close earnings missing.)*

**2. WHAT THE PRICE ALREADY ASSUMES.** Growth needed for the [E4-28] ~10% floor:
**+5.9% to +6.2% perpetual** (screen said 6.12%; confirmed on corrected inputs). What the
business has done: production +3.5%/yr over nine years, real crude realization ~flat,
reserves per share **−7.6%**, and the filer's own ten-year reserve-replacement ratio is
**95%**. A 6% perpetual-growth belief against a shrinking per-share resource base fails
[E4-35]'s base rate. Growth needed merely to MATCH the bond: ~+1.2%/yr at the judged
construction — achievable in supply-tight years, structurally unowned [E2-58].

**3. WHAT YOU ARE PAID.** −1.5 to −0.01 points against the sovereign at the judged and
generous ends; **negative on every construction**.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** (zero-growth at the bare sovereign, per
share on 1,975,771,274 shares):
- conservative (D&A end / acquisition-inclusive (c)): **~$105-150**
- judged (ex-windfall mean, (c) = guided organic capex): **~$160-170**
- generous (windfall-in mean, capex end): **~$210**
- at the [E4-28] floor: **~$80-110, judged ~$85**
- **current price: $211.78 (2026-09-02 close — the 52-week high)**

**WHICH BAR? Bar 2, the screamer test [E4-01]** (no margin stacked; windage count: **one** —
the [E4-41] windfall strip; (c) used the filer's own guided number, realistic not padded).
**Outcome: the price sits ABOVE the entire range** — above even the construction that
averages the 2022 windfall in and charges only guided capex. Third outcome: **no.**

**What bounds the upside [E2-63]:** the H1-2026 boom (OCF $25.1bn in six months) is real
and, annualized at ~$50bn with guided capex, would put the CURRENT-strip yield near 7.5%
on the cap — that is the bull case stated at full strength, and it is [E2-58]'s
supply-tight year priced as if permanent, at a 52-week-high quote. *"nothing fails like
success"* is the filed history of this exact industry.

**RANKING: not ranked — quit on [E4-28].** Honest pre-tax expectancy at this price
(~4% yield + ~3-4% defensible growth ≈ 7-8%) sits below the ~10% *"figure we quit on"*,
and the Q2 OUT closes entry at any price regardless [E5-35].

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND? *(template retained; gate closed)*

**Q5 did not open** - Q2 returned OUT and the hard sequence governs. The price the queue
requires is above, under `COMPUTATION - NOT A CLEARANCE`. The bare sovereign (5.27%) was
used there per [E3-42]; Bar 2 was the bar; windage count one.

- **VERDICT: gate not opened (Q2 OUT).**

## Q6 - WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**No position exists and none is opened; Q6 does not arise.** For the register, the fact
that would most plainly bear on a future re-read: **a durable administered-price regime or
a filed, quantified structural cost gap** - e.g., Chevron's replacement economics moving to
the top of the peer row for several consecutive years, or a TCO concession extension filed
well before 2033. Q2 OUT is permanent for the business as it stands; a changed business is
a new file.

- **VERDICT: not applicable - no entry.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped — Q1 IN, Q2 OUT, Q3/Q4 for the
      record, Q5/Q6 not opened
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — Q1's IN
      rests on filed tables; the Hess-stub estimate at Q4 is disclosed as an estimate in a
      for-the-record section, not a gate
- [x] No UNRESEARCHED verdicts issued; peer names not taken (ENI, Equinor) are stated at
      the row with the count (6 taken of ~8)
- [x] No UNKNOWABLE verdicts issued
- [x] Step 0: FY2025 10-K read with accession 0000093410-26-000078; OCF, capex and the
      cover count cross-checked against the filed statements
- [x] Owner earnings on multi-year means; windows stated (3-yr, 5-yr, ex-2022 4-yr); (c)
      disclosed as a judgment ($19bn, filer's guided organic capex) with the
      acquisition-inclusive caveat reported
- [x] Competitor row filled: six peers, same-basis computation plus each filer's published
      metric, accessions in the research folder
- [x] Sovereign 5.27%, USD 30-yr, US Treasury daily par curve (issuing authority), 2026-09-02
- [x] Value as a round-number range (~$105-210/sh; judged ~$160-170)
- [x] One bar (Bar 2, screamer); windage count one, stated
- [x] Prices dated; Yahoo chart used for the live quote only and flagged, snapshot on disk
- [x] Run committed to git after Stage 0/Q1, Q2, Q3, Q4, and at close

## REGISTER
- Verdict: [x] **OUT (about the business), at Q2.**
- One line: **an execution-excellent, AA-rated price-taker that replaced 43.7% of its
  production with the drill bit over three years at the worst honest finding cost in its
  peer row, earned 6.6% on capital by its own published table in a $69-Brent year, and
  trades at its 52-week high above every owner-earnings construction this run could build.**

---
# OUTPUT CONTRACT — the two required lines

**PRICE (under COMPUTATION — NOT A CLEARANCE, no entry language):** zero-growth value at
the bare 5.27% sovereign **roughly $105-210 per share, judged ~$160-170**; at the [E4-28]
floor **roughly $80-110, judged ~$85**. Current price **$211.78** (2026-09-02 close, the
52-week high) — above the entire range.

**PASS/FAIL: FAIL — the file closed at Q2 (franchise), OUT, on the filer's own documents;
Q1 was the only gate passed. Entry is closed at any price [E5-35].**
