# Company Run — Darden Restaurants, Inc. (DRI) — 2026-09-04
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

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
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.25%** · date **2026-09-03** · source (issuing authority) **US Treasury daily par
  yield curve, 30-yr** (via `tools/sources.py`). *(The screen row was built at 5.27%; the
  rate of the day governs.)* Earnings are ~100% USD (DRI operates almost entirely in the
  US; international is a small franchised royalty stream). FX/ADR: n/a.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **10-K FY2026 (52 weeks ended 2026-05-31), filed
  2026-07-24, accession 0000940944-26-000025** (primary doc `dri-20260531.htm`). Also
  read: **DEF 14A** filed 2026-08-10 (0001193125-26-342023); **10-K FY2023** filed
  2023-07-21 (0000940944-23-000037); **10-K FY2021** filed 2021-07-23
  (0000940944-21-000041); **10-K FY2019** filed 2019-07-19 (0000940944-19-000025) for the
  vintage series. All saved to `Test Runs/_research 2026-09-04 DRI/`.
- figure cross-checked against the filed statement (say which): **OCF FY2026 — the tagged
  $1,853.1M matches the filed Consolidated Statements of Cash Flows line "Net cash
  provided by operating activities" (see Step 0 cross-check note below Q4's series).**

**PRICE AND CAP (aggregator for the live quote only, flagged):**
- price **$218.04**, 2026-09-03 close, aggregator (Stooq via `tools/sources.py`)
- shares **114,077,969** — hand-read off the FY2026 10-K cover, *"Number of shares of
  Common Stock outstanding as of May 31, 2026"*. Single class.
- **market cap $24,874M**

**SCREEN ROW — REPRODUCED before adjudicating** (`2026-09-02 MASTER RUN QUEUE
(corrected).csv`): cap 24,478 / oe_bottom 818 / oe_top 1,139 / spread 0.393 / yield
0.0334 / growth_required 0.0666 / level_shift "no step" / acq_note "acquisitions are
$1,315M, 5% of cap, inside the window." Re-running `floor_screen.owner_earnings` on
today's companyfacts returns **5y_capex 817.9 / 3y_da 1,139.3 — the row's 818 and 1,139
to the million**; spread (1,139.3−817.9)/817.9 = **39.3%** ✓; 818/24,478 = **3.34%** ✓;
growth required 10% − 3.34% = **6.66%** ✓. The screen cap implies a ~$214.57 close; at
today's $218.04 the bottom yield is 3.29%. **Row reproduced.**
- **Software-capex check (the HAS fix, ordered by the brief):** DRI's cash-flow investing
  section is checked below for a separate capitalized-software line; finding recorded at
  Q4.

**STAGE 0(b) — THE DIVIDEND RECORD, BY HAND, WITH THE RPM DECOMPOSITION.**
- **The 2020 cut, verified and dated:** DPS declared $3.00 (FY2019) → $2.64 (FY2020:
  three quarters at $0.88, **Q4 suspended — "we have suspended our dividend until
  further notice," FY2020 10-K, filed 2020-07-24**) → $1.55 (FY2021, resumed low) →
  $4.40 → $4.84 → $5.24 → $5.60 → **$6.00 (FY2026)**. The dividend went to zero for the
  quarters spanning mid-2020; no payment-streak claim is made in the 10-K.
- **RPM decomposition, FY2019 → FY2026 (pre-COVID base): DPS +100%. Multiplicatively:
  net earnings ×1.692 (76% of the log growth) · share retirement ×1.070 (10%) · payout
  expansion 52.4% → 57.8% of diluted EPS, ×1.103 (14%). Checks: 1.692 × 1.070 × 1.103 =
  2.00 ✓.** The decomposition PASSES — the anti-TGT/PEP result: this dividend's growth
  is roughly three-quarters earnings, and the payout ratio is broadly flat. (Inputs: NI
  713.4 → 1,206.7; avg diluted shares ≈124.5M → 116.3M; DPS from the filed equity
  statements.)

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: **Darden is the opposite
  structure from the restaurant name that preceded it in this queue. MCD collects a toll
  on other people's restaurants; Darden runs 2,202 restaurants itself and keeps the whole
  P&L of every one — and bears the whole P&L of every one.** Eleven brands, four
  segments; the two that matter are Olive Garden (42% of sales, $5,594.8M, and 47% of
  segment profit, $1,257.9M at a 22.5% restaurant margin) and LongHorn ($3,423.0M at
  18.6%). A typical unit takes ~$5.8M of guest spending a year (OG), pays ~30% for food,
  ~35% for labor, ~17% for occupancy/other, and hands roughly $1.3M to the center, which
  takes out ~$514M of G&A, ~$180M of marketing and ~$194M of interest for the whole
  system. **The structural fact the brief had backwards [E4-26]: Darden no longer owns
  its real estate.** Of 2,202 restaurants, 98 sit on owned sites; 2,104 are leased (1,150
  land-only where DRI owns the building, 655 ground-and-building, 299 in-line) — the
  estate largely left in the FY2016 FCPT spin and sale-leasebacks, and what remains is a
  $5.7bn lease book ($3.9bn operating + $1.7bn finance) that is 2.7x the $2.1bn of bond
  debt. What the center actually adds is purchasing scale (one supply chain buying beef,
  pasta and produce for 2,200 units), one G&A/technology platform spread over $13.2bn of
  sales, and site/brand allocation — closing Bahama Breeze while building LongHorn.
  Money is made one re-chosen meal at a time: the diner pays ~$25-30, chooses again next
  week at zero switching cost.
- The scarce input this business controls: **scale within one category — the largest
  full-service restaurant company in America** (purchasing, ad dollars: OG's $129M
  marketing line alone exceeds most casual chains' total), plus 2,200 operating leases on
  proven corners with renewal options. It does NOT control the land (98 owned sites), the
  brand loyalty of a zero-switching-cost customer, or its labor supply.
- Will the fundamentals look broadly the same in ten years? **Yes in shape** — Americans
  will still eat casual sit-down meals; the brands are 40-90 years old; the model has
  been stable since the 2014 Red Lobster exit. **The category trend is the risk, not the
  comprehensibility** — the FY2026 10-K itself hedges on "declines in the casual dining
  industry" (Item 1A). Simple, stable, fully understandable.
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The question is put at the right altitude first, and it is the OPPOSITE altitude from
MCD's.** MCD's customer was the franchisee, locked into a 20-year site; **Darden's
customer is the diner, who re-chooses every meal at zero cost** — the 167 franchised
units are noise against 2,202 owned-and-operated. [E3-03](2) therefore runs at the table:
does the guest think Olive Garden has no close substitute? On any corner there is a
Chili's, an Outback, a Texas Roadhouse. **The only route to IN for an owner-operator in
this category is [E2-58]'s named exception — "a cost advantage that is both wide and
sustainable" — plus [E2-53] dominance economics, and both are claims the filings can
test.** The MCD Q2 case does not transfer and was not used.

- Needed or desired [x] — $13.2bn of sales, 2,202 restaurants, all 50 states; casual
  dining is a permanent American habit even while it shrinks per-capita.
- no close substitute [ ] — **fails at the diner level, per se.** The whole Q2 question
  is whether scale economics rescue the class via [E2-58]'s exception.
- not price-regulated [x] — free pricing.
- Must the moat be continuously rebuilt? **No — continuously DEFENDED [E5-23], which the
  corpus permits.** The advantage (purchasing scale, shared G&A/data platform, AUV
  density) is not wave-riding [E3-51] and does not depend on a technology generation. It
  does depend on value positioning being maintained every year — marketing spend is
  RISING (144.5 → 169.9 → 180.4) and the filed marketing filter is explicit: *"we will
  not rely on deep discounts and are therefore able to provide great value to our guests
  while driving profitable sales growth"* (Item 1). Does success depend on a great
  manager? No single person; the system survived CEO transitions (Lee → Cardenas 2022)
  without a moat event. **But it does depend on operating execution compounding daily —
  recorded for Q3's weight case [E3-38].**
- Primary moat metric, filing-sourced, and its trend: **return on unleveraged net
  tangible operating assets 30.2% (FY2021) → 36.3% (FY2025) → 38.5% (FY2026)**, rising;
  **including the acquisition goodwill and trademarks 22.2% (FY2026)** — the acquisition
  engine still earns over 3x the sovereign on gross purchase capital. Restaurant-level:
  OG segment margin 22.5% on $5.8M AUV. **Direction of the DOLLAR moat: widening.
  Direction of the PHYSICAL series [E4-55]: the flagship's guest counts eroded four
  straight years FY2023-25 before FY2026's +1.0 — the honest series is below.**

**THE GUEST-COUNT SERIES [E4-55] — the run's spine.** DRI discloses same-restaurant
guest counts AND average check by segment, every year, in MD&A prose — OG and LongHorn
back to at least FY2017, all four segments from the FY2021 10-K on. **Nothing in this
series was ever withdrawn; disclosure EXPANDED, and the negative years are printed.**
(Full table with verbatim sources: `_research 2026-09-04 DRI/dri_series.md`.)

| FY | OG guests | OG check | LH guests | LH check | FD guests | Other guests |
|---|---|---|---|---|---|---|
| 2017 | +0.2 | +2.4 | −0.4 | +1.6 | n.d. | n.d. |
| 2018 | +0.2 | +2.2 | +0.3 | +2.4 | n.d. | n.d. |
| 2019 | +0.1 | +3.8 | +0.1 | +3.2 | n.d. | n.d. |
| 2020 | −10.0 | +1.4 | −10.4 | +1.6 | n.d. | n.d. |
| 2021 | −12.8 | +2.9 | +3.3 | +2.2 | −20.7 | −15.5 |
| 2022 | +18.9 | +4.4 | +22.8 | +4.3 | +53.9 | +30.4 |
| 2023 | −1.6 | +8.4 | +1.2 | +6.1 | +0.5 | +0.6 |
| 2024 | −1.7 | +3.3 | −0.4 | +5.2 | −6.9 | −3.3 |
| 2025 | −2.3 | +4.1 | +1.9 | +3.1 | −5.2 | −2.4 |
| 2026 | +1.0 | +2.9 | +3.7 | +3.4 | −0.2 | +0.6 |

**Chained on FY2019 = 100: Olive Garden guests 89.1 (−10.9% in seven years — four
consecutive declines FY2023-25, one positive year since FY2019); LongHorn 121.1 (+21.1%,
no post-2020 decline except −0.4 in FY2024).** Fine Dining (the Ruth's Chris purchase
bought INTO this): guests −11.4% cumulative FY2023-26.

**[E2-44] both halves, through the 2022-26 price wave:**
1. *Raise prices with flat demand?* FY2023-26 cumulative: **OG check +19.9%, guests
   −4.5%; LH check +19.1%, guests +6.5%.** Deflated: BLS CPI-U food-away-from-home rose
   ~+15.6% CY2022→CY2025 annual-average, ~+18-19% extended to the May-2022→May-2026
   fiscal window (approximation confessed: annual indices, window offset ≤5 months).
   **Both flagship checks tracked category inflation almost exactly — DRI priced WITH
   the category, not above it.** The value positioning is real and filed; what it is NOT
   is [E3-33]/[E5-28] pricing power — when OG pushed check +8.4% in FY2023, guests went
   negative and stayed negative three years. Half (1): **LH yes (guests grew through the
   wave), OG no.**
2. *More dollar volume with only minor additional capital?* **No.** Growth costs
   $700-880M/yr of capex against $561M D&A; every new unit is a $6-7M box. The good
   class [E4-20], not the great.
- **The average-check instrument acquits on value-integrity and convicts on pricing
  power: 6th application of the deflated instrument in this queue — direction: DRI never
  out-priced FAFH, so the guest losses at OG are demand erosion, not price-gouging
  backlash; and the corollary is that OG cannot out-price the category without losing
  its volume claim.**

**THE COMPETITOR ROW — required [E3-28].** A moat is a claim about *relative* position.
Same metrics, same windows, filing-sourced; peer workpapers with accessions in
`_research 2026-09-04 DRI/peer_*.md`. Returns are the identical NTOA formula (ROU out /
ROU-in / including goodwill+intangibles); the attacker metric is filed same-restaurant
TRAFFIC, cumulative through the price wave.

| Company | OI÷NTOA | incl. goodwill | ROU-in | Op margin | Rest.-level margin | Core AUV | Traffic, cum. thru price wave | Dividend 2020-25 |
|---|---|---|---|---|---|---|---|---|
| **DRI** (FY2026) | **38.5%** | **22.2%** | 21.6% | 12.0% | OG 22.5% / LH 18.6% | OG $5.8M / LH $5.6M | **OG −4.5% / LH +6.5%** (FY2023-26) | suspended Q4 FY2020, rebuilt to $6.00 |
| TXRH (FY2025) | 34.0% | 28.6% | 21.1% | 8.1% | 15.5% | **$8.7M** | **+15.3%** (FY2022-25; positive 11 of 12 disclosed yrs) | suspended Mar 2020, reinstated Apr 2021 ABOVE pre-cut rate |
| EAT (FY2026) | **82.1%** | 64.3% | 33.6% | 10.7% | Chili's 18.5% (computed) | Chili's $5.0M | **Chili's +14.2%** (FY2022-26; +16.0% in FY2025 alone) | eliminated 2020, never reinstated |
| BLMN (FY2025) | 4.5% | 2.6% | 2.3% | 0.9% | 11.7% | Outback $4.0M | **Outback −15.1%** (FY2022-25; negative 8 of 10 yrs) | suspended twice (2020, Oct 2025) + cut |
| CAKE (FY2025) | 23.2% | 17.7% | 9.0% | 5.0% | not disclosed in any 10-K examined | **$12.4M** | **−21.5%** (orders, FY2017-25; negative 7 of 9 yrs; ≈+30.3% pricing FY2021-25) | suspended Apr 2020 + $200M 9.5% preferred at the trough (cost ≈$276M to exit in 14 months); reinstated FY2023 |
| MCD (run 2026-09-03) | 33.4% | n/a | 24.0% | 46.1% | n/a (franchisor) | $3.07M systemwide/unit | US guest counts negative every disclosed yr but 2017 | raised through 2020 |

- Peers named: **5** (4 owner-operator comps built from filings + the MCD franchisor
  precedent) of an industry with more filers than eight (CBRL, DENN, DIN, RRGB, KRUS sit
  outside this row); the count is stated. **[E3-61]'s limit stated:** the row shows
  position, never conduct — the same structure produced Chili's turnaround and Outback's
  decay in the same three years; *"you'd have to know the people involved."* MCD's row
  carries its structural caveat from that run (a franchisor's returns measure not owning
  the moat asset).

**[E2-45] — THE ATTACKER RECORD IS THE VERDICT'S ENGINE. TXRH and Chili's ARE the
attacker record in casual dining, and both refute DRI's moat claim in its own category:**
1. **TXRH**: guest traffic positive in **eleven of twelve disclosed years**, +15.3%
  cumulative FY2022-25 while taking +25.7% of menu price — an AUV of **$8.7M against
  Olive Garden's $5.8M**, earning **34.0% on NTOA (28.6% including goodwill) with one
  brand, zero portfolio scale, and zero debt.** The scarce input DRI claims (scale) is
  demonstrably not required to match DRI's returns or to beat its traffic.
2. **Chili's (EAT)**: traffic −6.9% in FY2023 → **+16.0% in FY2025, +3.6% on top in
  FY2026**, comps +25.3% then +9.2%, on a $10.99 value bundle plus advertising — NTOA
  returns 82.1%. **A determined value attacker flipped casual-dining traffic
  double-digit inside 24 months.** The diner's willingness to move is not hypothetical;
  it is the filed record of the two years in which OG's guest counts were −2.3% and
  +1.0%.
3. The losing half (BLMN −15.1% traffic, margins to 0.9%; CAKE below) shows what the
  same category does to operators WITHOUT DRI's execution — the spread between Chili's
  and Outback is conduct, not structure [E3-61].

**The [E2-58] exception claim — "a cost advantage both wide and sustainable" — FAILS on
this row.** DRI's 38.5% is not category-unique (TXRH 34.0% without scale; EAT 82.1%);
DRI's purchasing/G&A scale did not protect the flagship's guest counts (−4.5% through
the wave while the attackers ran +14-15%); and the margin advantage over the losers is
execution-plus-AUV-density, which is [E4-36]'s "extreme performance over many factors" —
the cause of success that is NOT ownable, versus a structural cost floor. **[E2-53]
dominance fails the same way: the marketplace, not the position, is setting outcomes**
— the largest brand in the category lost guests four straight years to smaller
value attackers. That is the newspaper-downgrade shape, not the dominant-paper shape.

- **Untapped pricing power [E3-33]: not claimed, and the filed record refutes it** — the
  one year OG pushed check materially above category inflation (FY2023, +8.4%), guest
  counts went negative and stayed negative for three years. Claiming the class would
  claim near-monopoly [E5-28]; nothing here supports it.

**THE DISCONFIRMING CASE, BUILT FIRST AND STATED AT FULL STRENGTH [E4-26, E4-51]** —
what an advocate of IN would say, fairly:
1. **LongHorn's guest-count record is a decade-class exhibit**: +21.1% vs FY2019, no
  post-2020 down year but one (−0.4), through +19.1% of check — [E2-44](1) satisfied at
  the brand level for seven years. Only TXRH's record is better in the whole row.
2. **Olive Garden held its guests better than every non-attacker in the row** (−10.9%
  vs FY2019 against Outback ≈ −17% and category traffic negative per Brinker's own
  10-K) while pricing WITH the category, not above it — value integrity intact.
3. **The portfolio's returns rose through the worst casual-dining cycle on record**
  (30.2% → 38.5% NTOA; 22.2% including all acquisition goodwill), every segment ≥15.9%
  restaurant margin — no [E2-56] camouflage; the acquisition engine is 2-for-3 with
  the one failure (Cheddar's, $314.2M impaired) printed to the decimal.
4. FY2026 turned every segment's guest counts flat-to-positive (OG +1.0, LH +3.7,
  Other +0.6, FD −0.2) — the first such year since FY2022, before Q5's re-read date.
**Why it still fails: every one of those four facts is about being the best-run house in
the category — none of them is a structural reason the diner cannot defect, and the
attacker record shows the diner defecting, in size, inside 24 months, against the
category's largest brand.** [E3-03](2) has no answer at the table. The moat that exists
only against the weak half of the row is not a moat; it is a ranking of managements —
and *"a business, unlike a franchise, can be killed by poor management"* [E3-43] is
recorded at Q3 as the gate-weight it implies.

- Class: [ ] WIDE [ ] NARROW **[x] NONE — a superbly-run business at the commodity end
  of food service; the [E2-58] exception was tested and not established** · Direction:
  dollar returns widening; the flagship's physical base narrowing (−10.9% guests vs
  FY2019); LongHorn widening.
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**
  **OUT on [E3-03](2), decided by the filer's own guest-count series read against the
  filed attacker record — not by category pattern-matching. The brief's [E4-26] prior
  (expect OUT) was TESTED against the strongest owner-operator case in the category and
  the disconfirming exhibits above; the row, not the prior, decided it.** Q3 and Q4 are
  recorded below per queue convention; the file closes here and the price reports under
  COMPUTATION — NOT A CLEARANCE.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [x] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

Case declared, and why: **GATE, on the daily-execution determinant.** An owner-operator of
2,202 restaurants whose product is re-chosen every meal is [E3-43]'s "a business, unlike a
franchise, [that] can be killed by poor management" — the un-differentiated product
magnifies the manager [E2-70]. *(Queue precedent has declared retailers overlay; the DRI
structure — no franchisee layer, no toll — is judged the heavier case, and the declaration
is recorded either way because the verdict below is identical under both: no disqualifier
found.)* No control (liquid, exit at will); leverage real but covenant-light and 2.0x
lease-adjusted by the filer's own measure — not [E3-29]'s 20:1 class.

**Honesty — binary, permanent, filings-based [E5-16].** **No disqualifier found** in the
FY2019-FY2026 10-Ks, the FY2020 crisis filings, or the 2026 proxy. No restatement, no
officer misconduct matter, no SEC enforcement disclosed. Litigation note is
ordinary-course.

**STEP 2 — THE FLAGS [E4-22, E5-15].**
- [ ] weak accounting — **no.** SBC expensed, pension small, footnotes standard.
- [ ] unintelligible footnotes — **no.**
- [ ] trumpeted earnings projections — **guidance culture exists** (annual sales/EPS
  outlook in every 10-K and release) but the [E3-48] record ACQUITS: FY2025 10-K guided
  FY2026 sales +7.0-8.0% → actual +9.4%; SRS +2.0-3.5% → +4.5%; capex $700-750M → $734M.
  Beaten on every line, no walked-down-then-beaten pattern visible in the vintages read.
- [ ] serial share issuance — **no.** Count 129.9M (FY2020) → 114.1M (FY2026). The single
  issuance of the decade is recorded under capital allocation: **$505.1M follow-on sold at
  the COVID trough (Q4 FY2020)** — dilution at the low, the mirror image of buying low.
- [ ] EBITDA / adjusted-earnings promotion **[E4-29]** — **proxy: ZERO occurrences of
  EBITDA. 10-K: 4, all the covenant-form "Adjusted Debt/Adjusted EBITDAR 2.0" leverage
  ratio** (the ORLY EBITDAR shape — a credit metric disclosed as such, not an earnings
  substitute). Pay runs on SRS + adjusted EPS with D&A in. Does not fire.
- [ ] filed-figure tells **[E4-30]** — cash tax paid as % of pretax: 4.2% (FY2023) /
  11.8% / 12.7% / **7.9% (FY2026)**. Low and falling in FY2026 — read: the level is the
  structural FICA-tip-credit regime, fully reconciled in the tax note (book ETR 12.6%,
  guided 13.5%); the FY2026 dip is deferred taxes (+$71.3M). Not the Gutfreund shape;
  growth is not unnaturally smooth (FY2020 −$52.4M net loss printed). Acquits.
- **[E4-52] adjustment streak: THREE consecutive years** of adjusted-EPS exclusions
  (Ruth's Chris deal costs FY2024, Chuy's costs FY2025, closure/impairment costs FY2026)
  — acquisition-tied, small ($0.20-0.47/yr), GAAP always printed first, and the FY2026
  reconciliation is **symmetric: the $0.27 Olive Garden Canada sale GAIN is deducted**
  while $0.47 of costs are added back. Not the PEP/HAS 9-12-year streak; recorded, watch
  at Q6.

**STEP 3 — THE PRIMARY TEST [E2-01].** ROE FY2026 = 54.7% (1,206.7/2,207.5) — but equity
is a buyback artifact (retained earnings **negative $108.4M**), so per [E2-43] the
denominator is unleveraged net tangible operating assets: **30.2% (FY2021) → 36.3%
(FY2025) → 38.5% (FY2026)**, and **including all acquisition goodwill and trademarks
22.2% (FY2026)** — the goodwill wedge reported, not hidden. Passes strongly, on a rising
series, without gimmickry.

**The half-owner test [E2-26]: passes, with one deduction.** The filer prints its own
worst facts — guest-count declines every year they occur, the Cheddar's write-off
quantified to the decimal ($145.0M trademark + $169.2M goodwill), symmetric adjusted-EPS
tables, full segment economics. The deduction is the [E2-49] half-fire: **the by-brand
SRS table (which showed Cheddar's −3.4%, Yard House −1.2% in FY2019, all brands negative
in FY2020) was consolidated into four segments in the FY2021 10-K** — granularity
withdrawn where readings were worst, though the same vintage EXPANDED guest-count
disclosure to all segments and has printed the negatives since.

**The institutional imperative [E2-30]: 1 of 4.**
- [ ] resists change — no: exited Red Lobster (2014), spun the real estate (2016), closed
  Bahama Breeze and sold OG Canada (FY2026) — the portfolio is pruned.
- [x] **acquisitions materialise to soak up funds — the stated strategy IS serial brand
  acquisition** (Cheddar's $780M FY2017 → 40% impaired in three years; Ruth's Chris $715M
  FY2024; Chuy's $649M FY2025). Two of three so far earn their keep (FD margin held;
  Chuy's integrated on schedule); the Cheddar's record is the caution.
- [ ] staff studies — not observable in filings.
- [ ] peer imitation — no: refused deep-discounting through the value war (Item 1,
  in writing), kept marketing rising while PEP-class peers cut.

**Capital allocation — the two buyback conditions [E5-08]:**
- (1) ample funds for operations and liquidity? **Thin but yes at current earnings** —
  $219.5M cash against a $13.2bn cost base; liquidity is a $1.25bn revolver that [E5-39]
  refuses to count. Scored properly at Q4's staying power.
- (2) repurchases at a material discount to conservatively calculated IV? **FLAG.**
  FY2026: $671.7M repurchased at ≈$197 average (gross ~3.4M shares) — **at the top of
  the zero-growth value band computed at Q5 (~$130-200)**; a new $1.5bn authorization
  followed in June 2026. Not the ORLY accelerate-into-the-high pattern (pace is steady,
  ~$420-670M/yr), but not a material discount either. Stated with [E4-13]'s humility:
  the band is ours; they know the business better. **Binds position size only.**
- Dividends-funded-by-issuance [E2-52]: acquits ($25M/yr option proceeds vs $693M paid).
- **[E2-60] fires at the conservative construction, three years running:** dividends +
  buybacks vs capex-end OE — FY2024 $1,082.3M vs $827.6M; FY2025 $1,076.7M vs $803.2M;
  FY2026 $1,364.7M vs $893.2M — funded at the margin by $1.85bn of new debt over the
  three years (of which $1.31bn bought Ruth's Chris and Chuy's) and $194M of CP. At the
  D&A end the payouts are covered. Recorded as a Q4 input, not a venality finding.
- **[E3-54] retention: PASSES.** FY2022-26 retained ≈ $2.09bn (NI $5,218.6M − dividends
  $3,132.7M); market value added ≈ +$5.5bn (cap $24.9bn today vs ≈$19.4bn at May-2021,
  130.8M shares × ≈$148 implied by the 402(v) TSR of $167.89 less reinvested dividends —
  price basis approximate, flagged) ≈ **$2.5-2.7 of MV per $1 retained**. Item 402(v)
  corroborates: DRI $167.89 vs its own disclosed peer index $140.02 per $100.
- **The FY2020 crisis record, both halves:** suspended the dividend outright (Q4 FY2020,
  "until further notice") and **sold $505.1M of equity at the trough** — survival bought
  with dilution [E5-39's dependence, executed]; but disclosure through it was immediate
  and complete, and the dividend was rebuilt to $6.00 by FY2026 (decomposition at
  Stage 0(b) below).
- **Pay-for-performance: the DG/ULTA rigging pattern does NOT replicate.** FY2026 STIP
  targets set ABOVE prior actuals (EPS target $10.26 vs $9.55 prior actual; SRS +2.4% vs
  +2.0% prior), paid 155% on results that beat both; PSUs paid 103%. One note: a
  **one-time CEO Special Equity Award** (100% PSU, ~5-yr vest, relative-TSR gated, 5x
  cap, negative-TSR cap) lifts the CEO's FY2026 summary-comp total to $34.8M vs $12-14M
  prior years — large, disclosed, performance-gated.

**THE GUARDRAIL — checked.**
- [x] Nothing here promotes the name; Q2 is decided on the business's own row.
- [x] The daily-execution dependence is recorded at Q2 as a structural fact of the class
  ([E4-23]: an owner-operator's excellence is management-embodied, not position-embodied).
- [x] No manager-as-plan reasoning used.

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *IN = no disqualifier found, under a GATE-weight declaration — not a finding of honesty
  [E5-17]. The record (retention pass, anti-rigged pay, symmetric adjustments, printed
  bad news) is among the cleaner ones in this queue. IN never promotes.*

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**
Construction (CONVENTION, per framework): OCF − SBC − (c). Full capex = LBE + the
separate filed software line + finance-lease ROU additions (the lease note's
"right-of-use assets obtained in exchange for new finance lease liabilities" — DRI
finances real restaurant assets through finance leases every year, so they are capex).
- Owner earnings by year (capex end): **613.8 (FY2022) · 815.9 · 827.6 · 803.2 · 893.2
  (FY2026)**; D&A end: 835.7 · 1,097.5 · 1,093.3 · 1,111.8 · 1,212.9.
- **Short-window mean** (FY2024-26): capex end **841.3** · D&A end **1,139.3**
- **Long-window mean** (FY2022-26): capex end **790.7** · D&A end **1,070.2**
- **Spread, conservative end:** (1,139.3 − 790.7) ÷ 790.7 = **44.1%**
- **Combined range: $791M to $1,213M** (5-yr capex end to FY2026 D&A end)
- *Too wide to conclude?* **No — the whole range prices below the sovereign at Q5, so the
  band cannot change the verdict (the ORLY ruling); UNKNOWABLE does not fire.**
- Distortions named **[E5-11, E4-41]**: **Ruth's Chris (closed 2023-06-14) and Chuy's
  (closed 2024-10-11) sit inside every window — $1,315M of acquisitions, 5% of cap
  (screen acq_note reproduced)** — so the 5-yr mean averages three perimeters; the
  windows are displayed and the judgment leans on FY2024-26. **FY2026 is a 53-week year**
  (the extra week = +$0.25 of the $10.44 EPS; ≈ $30M) — normalized out of the judged
  figure. FY2022's capex includes a $187.8M finance-lease-addition spike.
- **Maintenance capex — the (c) judgment, disclosed:** This is **not** the [E5-20]
  exception class — the filing never says depreciation understates renewal, and the
  capex excess over D&A visibly buys **units** (+43 net in FY2026; 75-80 openings guided
  for FY2027). But the bare D&A default is judged LIGHT here **[E4-47]**: construction
  costs have inflated ("we have experienced higher than usual costs and expenses in
  recent years," Item 1A), remodel cycles are required to hold traffic ([E2-23]'s
  "fully maintain its long-term competitive position"), and **no new-vs-maintenance
  dollar split is filed in any vintage read (FY2019, FY2022, FY2026) — the DG measured
  split is unavailable.** **(c) judged $650M** — D&A $561M plus a remodel/inflation
  increment — inside a band of $561M (D&A) to $881M (total capex).
- **Judged owner earnings ≈ $990M ≈ $1.0bn**: 3-yr mean (OCF − SBC) $1,651.7M, less ~$12M
  53rd-week share, less (c) $650M. Windage count: conservatism spent ONCE ((c) above the
  D&A default); the 53-week normalization is accuracy, not conservatism.
- Stock compensation subtracted in full **[E5-06]**: $79.1M (FY2026), every year, from
  the filed cash-flow line.
- **Tool defect (queue-wide, the HAS class):** `floor_screen` capital for DRI = LBE +
  finance leases but **misses the separate "Purchases of capitalized software and other
  assets" line ($26-29M/yr)** — screen OE bottom overstated ~3%. Corrected by hand here.

### Great, good, or gruesome? **[E4-20]**
- [x] **good** — attractive return, earned also on added capital
- Evidence: 22.2% on operating assets INCLUDING all acquisition goodwill/trademarks;
  38.5% excluding; both rising. Growth consumes real capital ($6-7M a box, ~$880M/yr
  total capex) but the added capital earns: Ruth's Chris/Chuy's inside a Fine
  Dining/Other segment mix still running 16-18% restaurant margins, and [E5-40]'s ~12%
  return-on-retention bar is cleared. Not great — the flagship's physical base erodes
  and growth must be bought. Not gruesome.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings: **PASS** — OCF stayed positive ($717.4M)
  through FY2020's closed dining rooms; $1.85bn now.
- (2) massive liquid assets: **FAIL** — $219.5M cash against a $3.0bn current-liability
  stack; the $1.25bn revolver and CP program are strangers' kindness and are not counted
  **[E5-39]**. ($606.0M of gift-card unearned revenue is covenant-free customer funding
  [E3-52] — a structural cushion, not a liquid asset.)
- (3) no significant near-term cash requirements: **MARGINAL** — $500M notes due May
  2027 (already classified current) + $400M due Oct 2027 + $194M CP ≈ **$1.1bn inside
  ~17 months**, NOT pre-funded (the anti-HAS pattern); the filing plans "available
  liquidity, which may include … borrowings under our existing credit facility,
  commercial paper issuances, or refinancing transactions." Covered ~2x by one year of
  OCF−capex+payout-suspension capacity, so survivable by choice, dependent if the
  payout is defended.
- Leverage, named and quantified: **$2.14bn senior notes + $0.19bn CP + $1.74bn finance
  leases + $3.94bn operating leases = ~$8.0bn of fixed claims** on a $24.9bn cap;
  filer's own lease-adjusted Debt/EBITDAR **2.0x**; coverage [E2-54] with capex out
  first: (OCF 1,853.1 − capex 880.8 + interest ~194) ÷ 194 ≈ **6.0x** — comfortable,
  accrued interest included via the OCF start point.
- The on-record stress test: FY2020 was survived via a $750M revolver draw, a $270M term
  loan, and a **$505.1M equity sale at the trough** — three drinks from strangers.
  [E2-64]'s borrow-before-the-need pattern is absent.

### Name the specific way THIS business dies **[E2-27, E3-24]**
- Mechanism (a), solvency: a FY2020-shape demand stop. Quantified: fixed cash charges ≈
  interest $194M + op-lease rent $434M + finance-lease principal $25M ≈ **$653M/yr**
  against $220M cash; a four-month shutdown burns roughly $1.2-1.5bn — the revolver
  covers it, as it did in 2020, at the price of covenants and dilution. **A low-level
  possibility.**
- Mechanism (b), the real one — **value stagnation, the [E2-27] shape**: every casual
  chain adds units and remodels ("viewed individually … rational; viewed collectively …
  neutralized"), category traffic shrinks ~1-2%/yr (Brinker's own 10-K: casual dining
  "has not seen significant growth in customer traffic in recent years"), and DRI's
  flagship resumes its FY2023-25 path (−1.6/−1.7/−2.3) while Fine Dining continues
  (−11.4% cum. FY2023-26). Quantified: OG at −2%/yr guests for five years with margin
  reversion 22.5% → 20% takes OG segment profit $1,258M → ≈$1,010M; portfolio OE falls
  ~15-20% while the quote requires +6.7%/yr growth to clear the [E4-28] floor.
  **A real possibility** — it is what the last three pre-FY2026 years already looked
  like.
- Likelihood: [x] (b) a real possibility · (a) a low-level possibility
- **VERDICT: [x] IN — the business survives; both [E5-11] failures recorded and priced
  nowhere (MCD precedent: failed (2), verdict IN).**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

# COMPUTATION — NOT A CLEARANCE
*The file closed at Q2 (OUT). Under operator rule 3 and the queue's output contract the
price is still reported, under this heading, with no entry language.*

**THE FLOOR, before the ranking [E4-28].** Honest pre-tax expectancy at this price:
**6.2% to 9.9% (yield 3.18-4.88% plus an honest 3-5% growth guess), centered ~7.5-8%** —
below the ~10% *"figure we quit on"* on every construction. **Quit on, not ranked** —
and this is arithmetic only; the verdict above already closed the file.

**1. THE YIELD** (cap $24,874M = $218.04 × 114,077,969, 2026-09-03)
- conservative (5-yr capex end) $790.7M ÷ $24,874M = **3.18%**
- judged ≈$990M ÷ $24,874M = **3.98%**
- top (FY2026 D&A end) $1,213M ÷ $24,874M = **4.88%**
- sovereign **5.25%** — **the yield is below the bare bond on EVERY construction**
  (−2.07 to −0.37 points).

**2. WHAT THE PRICE ALREADY ASSUMES**
- perpetual growth needed just to MATCH the bond: **+0.4% (top) / +1.2% (judged) /
  +2.0% (conservative)** — achievable against a +3.0%/yr owner-earnings record
  (FY2023→26) and +2.5-3.5% guided SRS; **this is the strongest thing sayable for the
  price** (the MCD shape).
- growth needed for the [E4-28] floor: **+6.0% (judged) to +6.8% (conservative)**
  perpetual — the screen's 6.66% reproduced. Against [E4-35]'s base rate and a flagship
  losing physical volume, that is a burden the record does not carry.

**3. WHAT YOU ARE PAID**
- return at the current price = **0.4 to 2.1 points UNDER the sovereign** before any
  growth; the price is paid for growth the category record argues against.

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used **5.25%** — **the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — zero-growth at the bare sovereign
(no per-name premium in the rate [E3-42]):
- conservative **~$130/sh** ($790.7M ÷ 5.25% ÷ 114.078M) · judged **~$165/sh** ·
  optimistic **~$205/sh** (D&A-end) · **current price $218.04** — **above the entire
  zero-growth band.**
- at the [E4-28] floor: **~$70-105/sh, judged ~$85.**

**WHICH BAR?** [x] **Screamer test [E4-01]** — the price does not clear the conservative
case; it sits **above the whole zero-growth range**, the third outcome: **no.** (Bar 1
not used; no margin stacked.) **Windage count: one** — (c) judged above the D&A default;
everything else at realistic inputs.

- **VERDICT: not opened — the file closed at Q2. The computation above carries no entry
  language.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Not opened — the file closed at Q2 (OUT, permanent).** For the record, the facts that
most challenge the OUT and are already on file: FY2026 guest counts turned positive in
three of four segments (OG +1.0, LH +3.7, Other +0.6) — one year against three
structural ones [E3-30/E4-17]; LongHorn's +21.1% seven-year guest record; and the
FY2026 STIP paying on targets set above prior actuals. A Q2 OUT is about the business's
class, not its year; none of these facts changes the class.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN → Q2 OUT stop; Q3/Q4
  recorded per queue convention, price under COMPUTATION — NOT A CLEARANCE)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat**
- [x] Every UNRESEARCHED verdict names the artifact — none issued
- [x] Every UNKNOWABLE verdict states what cannot be known — none issued
- [x] Step 0: the filing was read, with accession number; OCF FY2026 cross-checked
  against the filed statement to the decimal
- [x] Owner earnings on multi-year means; two windows and the capex band displayed;
  (c) disclosed as a judgment ($650M inside $561-881M)
- [x] Competitor row filled: 5 peers, identical formulas, filing-sourced, accessions in
  the workpapers; no PROVISIONAL
- [x] Sovereign for USD earnings, US Treasury daily par yield curve (issuing authority),
  5.25%, 2026-09-03
- [x] Value stated as round-number ranges ($130-205 zero-growth; $70-105 at the floor)
- [x] One bar (screamer); windage count one, stated
- [x] Prices dated; Stooq aggregator used for the live quote only, flagged
- [x] Run committed to git after every question (see log; two session-kill rescue
  commits also on record)

**Brief defects found (assume some, the brief said):**
1. **"DRI owns real estate; check the filed new-vs-maintenance split (the DG
   precedent)"** — the premise is stale: DRI owns 98 of 2,202 sites; the estate left in
   the FY2016 FCPT spin/sale-leasebacks. What it owns is buildings on 1,150 land-only
   leases plus a $5.7bn lease book. And no new-vs-maintenance dollar split is filed in
   any vintage read — the DG precedent is unavailable for DRI.
2. **"[E4-55]: establish which vintages disclose guest counts … note what disappeared
   [E2-49]"** — nothing about guest counts disappeared; that disclosure EXPANDED in
   FY2021 from two brands to all four segments and prints its negatives. What
   disappeared is the BY-BRAND SRS table (FY2021 10-K consolidation), a different
   instrument than the brief pointed at.
3. **The Chuy's price is misstated in the queue's acq_note framing** — filed
   consideration is $649.1M total / $613.7M net cash (not "$605M"), and with Ruth's
   Chris $715M the pair is $1,364M gross, ~5.5% of cap, matching the screen's $1,315M
   only on the net-cash basis.
4. The brief's competitor set was right, but its "no step" screen framing hides that
   the screen capex construction (LBE + finance leases) misses DRI's separate software
   line — OE bottom ~3% overstated queue-wide for such filers (the HAS defect, still
   uncorrected in floor_screen for the software line when a PP&E tag resolves).

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **The best-run owner-operator in casual dining is still a business whose
  customer re-chooses every meal — the filed attacker record (TXRH +15.3%, Chili's
  +14.2% traffic through the price wave, against OG −4.5%) refutes the scale-moat
  exception, and at $218.04 the price is above even the zero-growth value of the
  earnings it does have.**
