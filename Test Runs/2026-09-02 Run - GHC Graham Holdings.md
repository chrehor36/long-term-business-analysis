# Company Run — Graham Holdings Company (GHC) — 2026-09-02/03
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**Method ruling (Stage 0(b), `Screens/WATCHLIST RUN QUEUE.md`, 2026-09-02): NOT
float-bearing.** The FY2025 10-K contains one occurrence of "float" and it is
vehicle floor plan / floating-rate debt; zero premiums, zero underwriting, zero
policyholders. **The ORDINARY method applies**, run as a multi-segment holding company.
Research folder: `Test Runs/_research 2026-09-02 GHC/`.

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
- rate **5.27%** · date **2026-09-01** · source **US Treasury daily par yield curve, 30Y
  (issuing authority, via `tools/sources.py`)**
- FX: quote and earnings both USD. ~22% of revenue is non-US (~$1,074M, mostly Kaplan
  International, of which ~$609M UK) — earned through USD-reporting consolidated
  subsidiaries; the USD sovereign is used and the GBP exposure is named at Q4, not priced
  as a second rate.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document: **FY2025 Form 10-K, fiscal year ended 2025-12-31, filed 2026-02-25, accession
  0001628280-26-011405** (primary doc `ghc-20251231.htm`); plus **Q2-2026 Form 10-Q, filed
  2026-07-30, accession 0001628280-26-050826**.
- figure cross-checked against the filed statement: **FY2025 consolidated operating
  revenues $4,911,563k** — income statement (p.71) against the segment-note reconciliation
  (Note 19: $4,553,919k five reportable segments + $360,139k Other/Corporate − $2,495k
  intersegment = $4,911,563k). Ties exactly.

**STAGE 0 SHARE COUNT — verified off both covers, both classes, charter equivalence:**
- FY2025 10-K cover (at 2026-02-20): Class A **964,001** + Class B **3,397,834** = 4,361,835
- Q2-2026 10-Q cover (latest): Class A **964,001** + Class B **3,270,927** = **4,234,928**
  — matches the `cover_shares.py` audit figure exactly. The screen's "no share count"
  bucket was the companyfacts dimension-drop on the A/B class split; the cover is the count.
- **Economic equivalence, from the filed charter description (Note 14, FY2025 10-K):**
  *"Each share of Class A common stock and Class B common stock participates equally in
  dividends."* Class A (family-held, unlisted) elects 70% of the Board; Class B (NYSE)
  elects 30%. Control differs; per-share economics do not. **The arithmetic sum IS the
  economic count: 4,234,928.** (126,907 B shares repurchased between the two covers —
  noted at Q3.)

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: **a family-controlled holding
  company with five operating legs, a securities portfolio and a pension surplus.**
  FY2025 revenue $4,911.6M; segment OI before amortization $440.9M, less Other-business
  losses (−$94.2M) and corporate (−$67.4M):
  1. **Kaplan (35% of revenue, OI $166.0M):** sells education services three ways —
     university pathway/language programs for international students (KI, $1,079.6M rev,
     10.5% margin; the student's visa is granted by governments, not Kaplan), a
     fee-for-service contract running Purdue Global's online university (KHE, $349.2M rev;
     the Purdue fee itself was $70.0M in 2025 and is re-assessed quarterly), and test
     prep/professional education (Supplemental, $317.2M rev).
  2. **Television (8.7% of revenue, OI $117.7M):** seven network-affiliated local stations
     (Houston, Detroit, Orlando, San Antonio, Jacksonville, Roanoke) selling advertising
     plus retransmission fees per pay-TV subscriber. Biennial political windfalls
     (2024: +$87.9M political revenue vs 2025). Margin 26% in the off year, 38% political.
  3. **Healthcare (16.6%, OI $97.4M):** 87.5% of CSI, a home-infusion pharmacy growing 55%/yr,
     plus home health/hospice JVs. Reimbursement- and referral-driven.
  4. **Automotive (23.1%, OI $28.1M):** eight D.C.-area dealerships, 90% owned, managed by
     the Ourisman family for a fee ($8.4M, 2025). The OEM franchise agreement is the asset
     and the OEM holds the power.
  5. **Manufacturing (8.9%, OI $31.7M):** four niche industrials (fire-retardant wood,
     workspace electrical, screw jacks, combustion monitoring). Cyclical, commodity inputs.
  6. **Other (loss −$94.2M):** 14 restaurants, Framebridge (investment stage, significant
     losses), small media. Plus corporate: **$1,081.9M in five public stocks**, **$2,772.4M
     pension surplus** (assets $3,412.7M vs PBO $640.3M), **$880.8M debt at 5.7% (Ba1/BB)**.
- The scarce input this business controls: **per leg, and mostly it doesn't** — FCC licenses
  + network affiliations (TV, genuinely scarce); the Purdue Global contract (KHE); OEM
  franchises (auto, controlled by the OEM); pharmacy licenses and payer contracts (CSI, not
  scarce). The one input the *holding company* controls is permanent family capital and the
  pension surplus.
- Will the fundamentals look broadly the same in ten years? **The holding company yes; the
  mix no.** TV is in filed structural decline ("this trend is expected to continue" — the
  10-K on retrans net of network fees); Kaplan is hostage to visa and regulatory policy;
  healthcare is the growth leg. The money-making is understandable leg by leg; nothing here
  is opaque.
- **VERDICT: [x] IN** — comprehensible per segment from the filing. Understanding is the
  gate; durability of each leg is judged at Q2/Q4.

## Q2 — IS IT A FRANCHISE? **[E3-03]**
**Per-segment, per [E5-37] (metric set chosen by business type first). The security is the
conglomerate; a franchise verdict must hold for what the shareholder actually buys.**

**[E3-03] three criteria, per segment:**
- **Television (GMG):** needed/desired [x] (local news leadership, six big-four
  affiliations) · no close substitute [ ] — **fails**: the 10-K itself names them (vMVPDs
  outside the retrans regime; "YouTube TV has reported 10 million subscribers and is
  poised to become the largest pay-TV provider"; network D2C platforms carrying the same
  programming; WJXT not carried on Hulu+Live TV) · not price-regulated [~] — retrans is a
  statutory-consent regime and [E2-59] applies: **the moat belongs to the regime**, which
  does not extend to the growing half of distribution.
- **Kaplan KHE:** the Purdue Global TOSA is a contract, not a franchise — one client, and
  Kaplan re-assesses "whether to record all or part of the fee" **quarterly** ($70.0M
  recorded 2025, $54.5M 2024). A supplier that must decide each quarter whether its own
  fee is collectible is a price-taker to a single counterparty. Fails (2) and the pricing
  test. (2U, the nearest OPM-model comp, went Chapter 11 in 2024.)
- **Kaplan KI / Supplemental:** visa regimes (US Pathways "down significantly... due to
  changes in U.S. visa policies") and open competition; margin 10.5% — the LOWEST of the
  public education group (row below). Fails (2).
- **CSI / healthcare:** growing 55% at 11.4% margin, but reimbursement caps price
  (fails (3) in substance) and pharmacy licensure is not scarce. A good business today;
  no no-close-substitute claim possible.
- **Automotive:** 2.5% segment margin vs 4.2–4.5% at LAD/AN — a below-average operator of
  a commodity retail model; the scarce asset (OEM franchise) belongs to the OEM, which
  just killed one dealership (Jeep Bethesda closed; $10.1M CDJR impairment). Fails.
- **Manufacturing / restaurants / Other:** [E2-58] commodity doctrine; Hoover's core
  business in "substantial decline"; Other runs at a −$94.2M loss. Fails.

- Must the moat be continuously rebuilt? **[E4-04]** — TV, the one candidate: yes, and
  worse, the basis is being *replaced*, not defended — the retrans regime does not cover
  vMVPDs, so every subscriber who migrates leaves the moat's jurisdiction. This is a
  **surfing run [E3-51]** on the pay-TV bundle, and the wave is receding.
- Primary moat metric, filing-sourced, and its trend: **odd-year (non-political) segment
  revenue and OI: 2023 $472.4M/$139.4M → 2025 $425.1M/$117.7M (−10%/−16% in two years)**;
  retrans net of network fees declining, "this trend is expected to continue" (MD&A).
  Per-sub rates rising while subs fall = the Precision Steel case **[E4-55]** — pricing
  hides shrinking units.

**THE COMPETITOR ROW — required [E3-28].** Full table:
`_research 2026-09-02 GHC/competitor rows.md`. Peer figures are SEC tagged data
(transcription, flagged); GHC's are the filed segment note.

| TV (the moat claim) | FY2023 margin | FY2024 political | FY2025 | odd-to-odd revenue |
|---|---|---|---|---|
| **GHC GMG (segment)** | 29.5% | 37.6% | 26.4% | **−10.0%** |
| TEGNA | 25.2% | 25.3% | 16.3% | −6.8% |
| Nexstar | 14.4% | 23.5% | 17.2% | +0.3% |
| Gray | 11.7% | 23.4% | 12.7% | −5.7% |
| Scripps | −32.9% (imprmt) | 16.4% | 8.6% | −6.2% |

Education: Kaplan 9.5% vs LOPE 24.0%, PRDO 23.2%, Adtalem 19.1%, STRA 13.7% — **Kaplan is
the lowest-margin operator in its public peer group.** Healthcare: GHC 12.0% vs OPCH 6.0%
(at 1/12th scale). Auto: 2.5% vs AN 4.5%, LAD 4.2%.

- Peers named: **TV 4 of ~5** public station groups (Sinclair excluded, broadcast buried in
  a diversified structure; TEGNA itself being absorbed by Nexstar — the industry is
  consolidating into its decline, FCC top-four rule eliminated July 2025). **Education 4 of
  4** listed publics. **Healthcare 1** pure infusion comp. **Auto 2 of ~6.**
  **Manufacturing: none clean** — stated as absence; no moat class is claimed there, so
  nothing is held PROVISIONAL on it.
- **Untapped pricing power [E3-33]:** claiming it is claiming near-monopoly **[E5-28]**.
  No segment supports the claim. TV's realized retrans pricing is the *opposite* tell
  [E4-37]: pricing power being spent into a shrinking base.
- Class: **[x] NONE** for the conglomerate; TV alone is NARROW and **eroding by the
  filing's own words**. Direction **[E4-32]: negative every year** — and direction
  outranks existence.

**The [E4-26] hunt — the strongest case FOR a franchise, stated before it is answered:**
GMG's margins run roughly DOUBLE the pure-play peers through both halves of the political
cycle — big-market legacy news leaders (Houston #6, Detroit #14, Orlando #15 DMA), the
[E2-53] dominance class in miniature. That is a real relative position. The answer: [E2-53]
was written about businesses whose *market* was intact — "Good or bad, it will prosper"
presumed the one-paper town kept reading the paper. Here the market itself is leaving:
subscribers down industry-wide, the odd-year series falling at every peer, and the
company's own filing forecasting continued decline. **The margin advantage is position
inside a shrinking arena; [E3-03](2) fails at the arena level.** A second candidate — the
$2.77bn pension surplus — is an asset, not a franchise; it makes no product needed or
desired. Cheapness and asset value have never passed a gate in this project **[E5-42]**,
and the segment-plus-loss-absorption construction ([E2-62]) fails for the same reason: the
shareholder buys the conglomerate, and the one strong segment inside it is the one in
filed decline.

- **VERDICT: [x] OUT** — no segment passes [E3-03] with [E4-04] durability; the closest
  (TV) fails on direction and on its own filing's forecast. **OUT is permanent. The file
  closes here; the price is reported below under COMPUTATION — NOT A CLEARANCE.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
**NOT OPENED — the file closed at Q2 (OUT). Hard sequence, operator rule 2.** Findings
gathered en route are recorded as observations in
`_research 2026-09-02 GHC/owner earnings workpaper.md`, not as a verdict: the [E3-54]
retention test passes (~$1.38/$1, five-year), the buyback record is price-sensitive across
five decades of family control, the candor form is per-item quantification [E2-26]; the
EBITDAP segment measure and the pension-driven cash-tax gap are prompts that were read and
resolved benignly. None of this was scored, because Q3 cannot start a run [E2-37].
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**None ticked → Q3 is a qualitative OVERLAY.** Record findings; manager quality alone does
not stop the run. **Any ticked → Q3 is a BINARY GATE and no price compensates.**
Case declared, and why: ____

**Honesty — binary, permanent, filings-based [E5-16].** *"understanding about business
mistakes; tolerance for personal misconduct is zero."* Each matter dated to when it became
PUBLIC, so the test stays point-in-time honest: ____

**STEP 2 — THE FOUR FLAGS [E4-22, E5-15].** *Accounting and disclosure, not litigation. Each
is a prompt to READ, never a verdict.*
- [ ] weak accounting — comp not expensed, fanciful pension assumptions → *"seldom just one cockroach in the kitchen"*
- [ ] unintelligible footnotes
- [ ] trumpeted earnings projections / growth targets
- [ ] serial share issuance
- [ ] EBITDA / adjusted-earnings promotion **[E4-29]** *(the fifth flag; 12+ corpus statements)*
- [ ] filed-figure tells: unnaturally smooth reported growth; cash-tax % of pretax falling **[E4-30]**
- For every box ticked, what the filing actually says: ____

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity capital employed, *without
undue leverage or accounting gimmickry* — **not** EPS growth. Multi-year series, balance
sheet before income statement.
- Years used, and the series: ____

**The half-owner test [E2-26]:** does this reporting tell me what I would want to know if the
positions were reversed? *(a one-time item quantified separately at every line passes; the
same item buried in an adjusted figure does not)* ____

**The institutional imperative — score all four [E2-30].** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [ ] resists any change in current direction
- [ ] projects/acquisitions materialise to soak up available funds
- [ ] staff studies produced to justify the leader's craving
- [ ] peer behaviour mindlessly imitated

**Capital allocation — the two buyback conditions [E5-08]:**
- (1) ample funds for operations and liquidity? ____
- (2) repurchases at a **material discount** to conservatively calculated IV? ____
  *(unquantified because the corpus leaves it unquantified)*
- If (2) fails → **CAPITAL ALLOCATION FLAG**, stated with the humility clause **[E4-13]**:
  this rests on our own IV range, and management knows the business better than we do.
  **Binds position size, never the discount rate.**
**THE GUARDRAIL — check before writing the verdict.**
- [ ] Confirmed: nothing in this Q3 is being used to **promote** the name. A strong manager
      cannot repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**.
- [ ] If this business **requires** a great manager, that is recorded at **Q2 as a moat
      defect [E4-23]** — *"the moat will go when the surgeon goes"* — not here as a strength.
- [ ] If a great manager is the reason to act: is the franchise **already intact** and the
      damage **excisable**, or is the manager the plan? **[E2-35, E2-36]** ____

- **VERDICT: [ ] IN  [ ] OUT (integrity failure is permanent)  [ ] UNRESEARCHED → ____
  [ ] UNKNOWABLE → ____**
  *IN = no disqualifier found. NOT a finding that the managers are honest — "sincerity and
  empathy can easily be faked" **[E5-17]**. IN never promotes.*

## Q4 — WILL IT SURVIVE?
**NOT OPENED — the file closed at Q2 (OUT).** The owner-earnings arithmetic the output
contract requires was still computed and sits below under **COMPUTATION — NOT A
CLEARANCE**, with the pension stripped, (c) judged per segment, and the political cycle
inside the mean. Survival observations recorded without a verdict: staying-power strength 2
is real ($1.4bn cash+securities against $881M debt), strength 3's counterweight is the
Ba1/BB rating and a $222.5M drawn revolver; the named-death candidate was never modeled
because the gate never opened.

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** *"Using precise numbers is,
in fact, foolish; working with a range of possibilities is the better approach."* Do **not**
pick a window and defend it; carry the spread alongside the capex band.
- **Short-window mean** (window: ____ ): ____
- **Long-window mean** (window: ____ ): ____
- **Spread, conservative end:** ____ %
- **Combined range** (window spread × capex band): ____ to ____
- *Is that range too wide to reach a conclusion? If yes, **that is the verdict** **[E4-25]** —
  close the file, do not resolve it by preference:* ____
- *A wide spread is also a Q4 finding: a distorted year sits in the window (a pandemic year, an
  acquisition, a disposal), which bears on earnings reliability **[E5-11]**. Name it: ____*
- Owner earnings by year: ____
- **Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT.** D&A is the default proxy
  **[E3-44, E2-41]**; for capital-intensive businesses the D&A end is INVALID and (c) is judged
  up from total capex **[E5-20]**. Which case is this, and why: ____
- Band used ____ ; where in
  the band it sits and the reason cited from the filing: ____
- Stock compensation subtracted in full **[E5-06]**: ____
- *If the capex band changes the verdict → **UNKNOWABLE**.*

### Great, good, or gruesome? **[E4-20]**
- [ ] great — high return, rising, little capital needed
- [ ] good — attractive return, earned also on added capital
- [ ] gruesome — grows, eats capital, earns little
- Evidence: ____

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings ____
- (2) massive liquid assets ____
- (3) **no significant near-term cash requirements** ____  ← *the one that usually kills*
- Leverage, named and quantified **[E4-16, E3-29]** — *there is no ratio ceiling in this
  framework and the corpus supplies none*: ____

### Name the specific way THIS business dies **[E2-27, E3-24]**
- The mechanism: ____
- Quantified from filed figures, and the resulting outcome: ____
- Likelihood: [ ] likely [ ] a real possibility [ ] a low-level possibility
- *If no mechanism can be named at all → consider **UNKNOWABLE**.*
- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?
**NOT OPENED — Q1-Q4 do not each show IN.** The price is reported under the computation
heading below, with no entry language (operator rule 3).

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."* Honest
pre-tax expectancy at this price: ____ %. Below roughly 10%, the name is not ranked — it is
quit on, whatever the sovereign is. Above it, rank, and capital goes to rank #1 [E3-45].
**No risk premium in the discount rate [E3-42]** — certainty lives at Q1 and in Bar 1's
end discount, never in the rate.

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no
vote **[E3-34]**.

**1. THE YIELD**
- owner earnings ____ ÷ market cap ____ = **____ %** · sovereign **____ %**

**2. WHAT THE PRICE ALREADY ASSUMES**
- year-1 growth needed to justify the quote: **____ %**
- what the business has actually done: ____ %

**3. WHAT YOU ARE PAID**
- return at the current price = **____ points over the sovereign**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used ____ % — **the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — a point estimate claims precision this
method cannot support:
- conservative ____ · optimistic ____ · **current price** ____

**THERE IS NO HURDLE. THERE IS A RANKING [E4-21].**
- points over sovereign, this name: ____
- against the rest of the opportunity set: ____
- *Take the best available, or nothing.*

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] **Normal method [E4-11]** — realistic inputs, one margin at the end.
      Margin used ____ %, and which corpus illustration it sits nearest:
      bridge ~35% **[E3-25]** · Grand Canyon 60%, the stated ceiling **[E3-26]** ·
      "closer to a dollar on the dollar" for a business you understand **[E4-12]** ·
      "dollar bills for 80 cents" **[E5-09]**
- [ ] **Screamer test [E4-01]** — does the price already clear the **conservative** case?
      No margin is added on top. Three outcomes: below the conservative case → act ·
      **inside the range → no useful conclusion, move on** · above the whole range → no.
- **Windage count** — conservatism applied at how many places? ____ *(more than one must be
  justified in writing)* **[E4-11]**

- **VERDICT: [ ] IN  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____ · ranking position ____**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
**NOT OPENED — no entry, so no exit rules to pre-commit.** What would prove the Q2 verdict
wrong is stated in the register.

**Pre-committed before entry [E1-02]:**
- Thesis-confirming metric: ____
- **Thesis-breaking metric and its threshold:** ____
- Next catalyst date: ____

**The sell rule [E2-28]** — two triggers, three hold conditions:
- SELL if the market judges it more valuable than the facts indicate ____
- SELL if funds are needed for something more undervalued or better understood ____
- HOLD while: return on equity capital satisfactory ____ · management competent and honest
  ____ · market does not overvalue ____
- *Price appreciation and holding period are **explicitly rejected** as reasons to sell.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring
question: is this erosion an aberrational cycle, or has the business slipped in a way that
permanently reduces intrinsic value? ____

**Do not trim winners [E5-14].** **Position size** — a judgment, stated: ____
*(sized DOWN if a capital-allocation flag is live)*

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

---
# COMPUTATION — NOT A CLEARANCE
*(Operator rule 3 and the queue's output contract: the file closed at Q2; this arithmetic
carries no entry language. Workpaper: `_research 2026-09-02 GHC/owner earnings workpaper.md`.)*

**Owner earnings, ordinary method, pension stripped.** OCF − SBC − the non-cash
remeasurement of the GHG minority put (which inflates filed OCF) − NCI attribution − (c).
The pension credit is backed out inside the filed OCF reconciliation itself, so the
construction strips pension income natively; the 2024 $653.4M settlement gain never enters.
(c) was examined per segment (the Loews-precedent demand): no segment is [E5-20]'s
exception class, capex runs at or below depreciation everywhere except growth capex at
healthcare, and the band is narrow — **the window spread, not the capex band, drives the
range.** The political cycle sits inside the mean (2022 and 2024 are the political years,
2 of the 5).

| $M | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| OE (capex end) | 32.9 | 126.9 | 143.3 | 190.5 | 204.1 |
| OE (D&A end) | 124.0 | 136.3 | 150.6 | 186.4 | 195.6 |

- Five-year means: **$139.5M** (capex end) / $158.6M (D&A end) · three-year: $179.3M / $177.5M
- **Combined range ~$140-180M · judged $155M** (five-year default [E2-42]; 2021's capex
  end carries named expansion capex — the year, not the method, is the distortion [E5-11])
- 2021's MRNI remeasurement was not separately obtained (FY2022 10-K) — 2021 stands
  unadjusted and slightly overstated; stated, immaterial to the mean's direction.

**The pension surplus, valued separately** ([E5-48]'s logic — it belongs to the plan's
assets, not the operating businesses): assets $3,412.7M vs PBO $640.3M → **$2,772.4M
gross**, less the $720.9M deferred-tax liability carried against it (Note 10) →
**$2,051.5M after tax ≈ $484/share**. It is real and the company demonstrably monetizes it
sideways — the 2024 annuity settlement, severance programs funded from plan assets, and
the Arconic purchase paid partly by assuming $107.5M of pension obligations — but it
reaches shareholders slowly and partially. Credited at 0% / 50% / 100% of after-tax value;
the 50% mid is a disclosed judgment, spent once. Its risk is named: 79% equities, one
stock + one fund = 37% of plan assets (largely Berkshire Hathaway).

**Sum of parts at the sovereign (5.27%, zero growth), 4,234,928 shares:**
| Case | OE | parity value | net marked assets* | surplus credit | $/share |
|---|---|---|---|---|---|
| Conservative | 140 | 2,657 | +570 | 0 | **~$760** |
| Middle | 160 | 3,036 | +570 | 1,026 | **~$1,090** |
| Generous | 180 | 3,416 | +570 | 2,052 | **~$1,430** |

*Securities $1,081.9M + cash $311.4M + affiliates at book $229.6M − debt $880.8M − SERP
$91.2M − minority interests $81.5M.*

**THE PRICE: $1,113.13** — Class B close 2026-09-02 (Yahoo Finance, aggregator, live quote
only, flagged). Market cap **$4,714M**. Headline owner-earnings yield **3.0-3.8% against
the 5.27% sovereign — below the bond outright.** Netting the marked assets and crediting
the surplus in FULL, the operating yield reaches 8.6% only when every generous assumption
is spent at once; **no honest construction reaches the 10% floor [E4-28]**. The price sits
inside the value range — under [E4-25] that is "no useful conclusion" even before Q2's
verdict is counted, and cheapness alone has never passed a gate here **[E5-42]**.

**The strongest facts against this file's conclusion, stated per [E4-51]:** the retention
test passes (~$1.38 of market value per $1 retained, five-year [E3-54]); real revenue per
share rose 6 of 7 years; and the family — rational allocators across five decades — is
buying stock RIGHT NOW at $1,125-1,148, above this file's judged middle. Those facts argue
the discount is real and the allocators believe it. The framework's answer stands anyway:
what is bought is a conglomerate whose best segment is in filed decline, whose largest
segment is its industry's lowest-margin operator, and whose yield is below the bond at the
quote — **the discount is not the framework's to arbitrage** [E5-42].

## THE OUTPUT CONTRACT
1. **PRICE: $1,113.13** (2026-09-02 close) against a computed value of **roughly $760 to
   $1,430 per share, judged ~$1,090** — COMPUTATION, NOT A CLEARANCE.
2. **FAIL. The file closed at Q2 (OUT): no enduring franchise in any segment.**
   Q1 IN · **Q2 OUT** · Q3-Q6 not opened.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped — Q1 IN, Q2 OUT, stop; Q3-Q6 marked
      NOT OPENED, price under the computation heading
- [x] **No question marked IN carries an "unverified" or "provisional" caveat**
- [x] Every UNRESEARCHED verdict names the artifact and where it lives — none issued; one
      research gap stated inside the computation (2021 MRNI figure, FY2022 10-K), which
      binds no verdict
- [x] Every UNKNOWABLE verdict states what specifically cannot be known — none issued
- [x] Step 0: FY2025 10-K read (MD&A, cash flow incl. detail lines, footnotes), accession
      0001628280-26-011405; revenue $4,911,563k cross-checked income statement vs Note 19
- [x] Owner earnings on a multi-year mean; five-year default plus three-year shown; capex
      band disclosed as a judgment, examined per segment; pension stripped and shown
- [x] Competitor row filled (TV 4 peers, education 4, healthcare 1, auto 2; manufacturing
      absence stated, no moat claimed there)
- [x] Sovereign 5.27% USD, US Treasury daily par yield curve (issuing authority), 2026-09-01
- [x] Value stated as a round-number range ($760-$1,430, judged ~$1,090)
- [x] One bar chosen, not both — the computation reports parity values and the [E4-25]
      inside-the-range reading; no margin was applied because no entry question was open;
      **windage count: 1** (the surplus-credit haircut, disclosed)
- [x] Prices dated; aggregator used for live quote only and flagged (Yahoo, 2026-09-02
      close)
- [x] Run committed to git after Step 0, Q1, Q2, and at close

## REGISTER
- Verdict: [x] OUT (about the business)
- One line: **A rationally-run family conglomerate at a real discount to its parts — and
  no part is an enduring franchise: the best segment (TV, margins double its peers) is in
  decline by its own filing's forecast, the biggest (Kaplan) is its peer group's
  lowest-margin operator, and the yield at the quote sits below the bond; the discount is
  not the framework's to arbitrage [E5-42].**
- What would prove the Q2 verdict wrong (for any future re-open): a filed reversal of the
  retrans/subscriber direction (vMVPDs brought inside the retrans regime by the FCC, or
  GMG's odd-year revenue series turning up), or Kaplan/CSI demonstrating priced-through
  dominance — [E4-37] agony-free price increases — in their own filings.
