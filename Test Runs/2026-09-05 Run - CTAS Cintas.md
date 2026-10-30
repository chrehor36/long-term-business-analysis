# Company Run — Cintas Corporation (CTAS) — 2026-09-05
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

**THE PERIMETER EVENT, found before Q1 opened — the brief did not know it [E4-26]:**
On **2026-03-10 Cintas signed an Agreement and Plan of Merger to ACQUIRE UniFirst** —
$155.00 cash + 0.7720 CTAS shares per UNF share, transaction valued ~$5.5bn (FY2026 10-K,
Item 1 and Note 1). UniFirst shareholders approved 2026-06-12; HSR/antitrust clearance
**still pending**; close expected **H2 calendar 2026**. The brief's Q2 gate — "UNF and
VSTS on identical formulas ... the attacker row" — was written against an industry
structure that the subject company is in the act of dissolving: **the #1 is buying the #3**
(VSTS self-ranks: "we are the second largest provider in our industry, based on publicly
reported information ... for each of Cintas, Vestis and Unifirst" — VSTS FY2025 10-K;
UNF revenue $2,432M < VSTS $2,735M).
Consequences carried through this file: (1) the competitor row is still run on filed
FY-2025/2026 numbers, but UNF is read as the *acquired*, not the attacker; (2) this is the
DKS/ACLS/HHH perimeter class — the filed standalone history describes a company that will
shortly change shape (~$3.4bn of new debt-funded cash + ~13.1M new shares if it closes),
and the file **re-opens at close**; (3) the antitrust condition is itself Q2 evidence —
the regulator's question and this file's question are the same question.

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
- rate **5.24%** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-yr,
  issuing authority (tools/sources.py, struck fresh this session)**
- FX: none needed — US operations generated **"over 90% of its consolidated revenue in all
  periods presented"** (FY2026 10-K, Item 1); earnings currency USD, quote USD.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **FY2026 10-K, fiscal year ended 2026-05-31, filed
  2026-07-29, accession 0000723254-26-000028** (primary); vintages FY2025 / FY2023 /
  FY2020 / FY2017 10-Ks and DEF 14A 2025 on disk in `_research 2026-09-05 CTAS\`
- figure cross-checked against the filed statement: **OCF FY2026 $2,276,280k — run.py's
  XBRL 2,276 matches the filed consolidated statement of cash flows to the thousand;
  capex $395,105k and SBC $128,076k likewise hand-checked against the filed lines.**

**PRICE, SHARES, CAP — Stage 0 by hand:**
- price **$200.47** (2026-09-04, aggregator — live quote only, flagged)
- shares **400,169,561** hand-read off the FY2026 10-K cover ("As of June 30, 2026 ...
  400,169,561 shares were outstanding"; 779,589,240 issued less treasury; single class,
  no par; preferred authorized, none outstanding)
- **run.py's 406.2M was the weighted-average diluted basis — the standing run.py defect,
  corrected again by the cover count**
- **cap $80,222M**
- **THE SPLIT GUARD [brief item]: verified.** 4:1 split announced 2024-05-02, record date
  2024-09-04, distributed 2024-09-11, trading post-split from 2024-09-12; "all references
  ... retroactively adjusted" (FY2026 10-K, Item 5). Cover count and price are both
  post-split; no step artifact.

**SCREEN ROW REPRODUCED before adjudicating (operator instruction):** at the hand cap
$80,222M the 5-yr OE band $1,363-1,457M yields **1.70-1.82%** — the brief's ~1.7% row is
the 5-yr window; floor growth required ≈ 10% − ~1.7% ≈ **~8.3%** — reproduced in shape.
run.py's 3-yr window prints 1.92-2.02% and "growth the price assumes 9.9%" at the
bond-matching construction.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: **Cintas rents cleanliness on a
  weekly schedule.** A business signs a service contract; a truck on a fixed local route
  delivers clean uniforms, mats, mops, shop towels and restroom supplies every week and
  hauls the dirty ones back to an industrial laundry. The garments are Cintas' working
  asset — bought, put in service, amortized over 18-30 months (other rental items 8-60
  months), washed and re-rented (Note 1). Revenue = stops × items per stop × price per
  item-week; cost = a plant and a truck-and-driver that are ~fixed per territory plus wash
  and garment amortization. **The profit engine is route density**: a second customer on a
  street the truck already drives adds revenue at near-zero incremental delivery cost, and
  a second product line (first aid cabinet refills, fire extinguisher inspection, water)
  adds revenue **at the same stop with no new truck at all** — 12,500 local routes, 484
  facilities, 12 distribution centers at 2026-05-31 (Item 1). Rental gross margin 50.0%
  (FY2026), rental segment operating margin 24.1%, total operating margin 23.1%. No
  customer exceeds 1% of revenue (Item 1) — a million small accounts on auto-renewing
  service agreements, none of which can negotiate.
- The scarce input this business controls: **accumulated local route density** — the
  concentration of contracted customers within driving minutes of an existing plant,
  compounded since 1968, which an entrant can only buy by running half-empty trucks at a
  loss for years; plus the only national footprint that can serve a 400-site account in
  every city at once.
- Will the fundamentals look broadly the same in ten years? **Yes.** Work shirts, mats,
  restroom supplies and fire-extinguisher inspections are not subject to technological
  substitution on any visible horizon; the customer base is service/industrial
  (manufacturing, food service, healthcare, hospitality), not office desk-work. The one
  structural drift — casualization of workwear — has run for thirty years already and the
  filed record grew straight through it.
- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**
- Needed or desired [x] (clean uniforms/mats/first-aid are OSHA-adjacent operating
  necessities for service and industrial businesses) · no close substitute **[qualified]**
  — at the CATEGORY boundary substitutes exist (in-house laundering, direct garment
  purchase, casualization); INSIDE the outsourced-rental category the row below shows no
  competitor reproduces the service at CTAS's economics · not price-regulated [x]
- Must the moat be continuously rebuilt? **No — it is DEFENDED, not replaced [E4-04]:**
  the advantage is accumulated route density plus national footprint, deepened by each
  added stop and each added product line on the same stop. No depleting asset, no
  technology wave to re-ride [E3-51]; the four-causes read [E4-36] is extreme max of one
  variable (density/scale) compounded 58 years — ownable, not wave-riding. Success does
  not depend on a great manager: three CEO generations (Farmer → Kohlhepp → Farmer →
  Schneider) produced the same filed trajectory — the Mayo test [E4-23] passes.
- Primary moat metric, filing-sourced, and its trend: **operating margin on identical
  formulas vs the two filed national competitors, and the per-route density series.**
  CTAS total op margin 14.7% (FY2018, G&K integration year) → 16.4% (FY2019-20) → 20.2%
  (FY2022) → 23.1% (FY2026) — rising for eight straight filed years. Routes 11,000
  (FY2017) → 12,500 (FY2026) while operational facilities FELL 528 → 484 and revenue
  DOUBLED ($5.3bn → $11.3bn): revenue per route ~$0.48M → ~$0.90M, revenue per facility
  ~$10M → ~$23M — **the density mechanism is visible in the filed unit series.**

**THE COMPETITOR ROW — required [E3-28].** Same metric, same (latest filed) window,
filing-sourced. Full extraction: `_research 2026-09-05 CTAS\ROW - UNF VSTS identical formulas.md`.

| Company | revenue | GAAP op margin | OCF − capex | organic growth | balance sheet |
|---|---|---|---|---|---|
| **CTAS FY2026** (10-K 2026-07-29) | $11,264.8M | **23.1%** | $1,881.2M | **+8.3%** ("primarily ... increased sales volume") | debt $2,436.6M vs equity $5,139.9M; ROE 40.7% |
| UNF FY2025 (10-K 2025-10-29, FYE 8/30/25) | $2,432.4M | **7.6%** | $142.5M | +1.8% ex-53rd-week ("solid new account sales and improved customer pricing") | zero debt, $203.5M cash, equity $2,169.0M; ROE 6.8% |
| VSTS FY2025 (10-K 2025-12-02, FYE 10/3/25) | $2,734.8M | **2.4%** (net LOSS $40.2M) | $5.8M | revenue −2.5%; Q3 FY2026 "Net volumes decreased 4.5% ... partially offset by strategic pricing improvements" | debt $1,155.1M + $166.3M finance leases vs $29.7M cash; goodwill $961.7M EXCEEDS equity $865.6M |

- Peers named: **2 filed of the industry's ~4 national real competitors** (UNF's own list:
  "Cintas Corporation, Alsco, and Vestis Corporation" plus "hundreds of smaller
  businesses"). **Alsco is private — no filings exist**; that is a stated row limit
  [E3-61] (the TSCO/BMI precedent), not UNRESEARCHED — no document exists on this shelf
  that would supply its margin. The hundreds of locals are the fragmented pool CTAS has
  consolidated from for four decades (~$3.16bn of tuck-in acquisitions FY2015-26 from the
  filed cash-flow lines, G&K $2,102.4M the largest).
- **THE BRIEF'S CENTRAL QUESTION — density (structural) or price (extractable)? The row
  answers it with the attackers' own filings [E2-45], and the brief was wrong on the
  ratio: CTAS runs 3.0x UNF's margin (23.1% vs 7.6%), not ~2x.** The ALG inversion
  (premium = share-donation waiting to happen) required the low-price attacker to take
  volume. The filed record shows the OPPOSITE, in the same years, on the same customers:
  - **VSTS — the live natural experiment the brief named [E2-45]:** the #2, born with
    Aramark's national infrastructure (325+ facilities, 3,300+ routes, "more than 300,000
    customer accounts"), operating at 2.4% margin — a 20-point price umbrella to attack
    under — and it is LOSING volume: *"The $89.0 million decline in rental revenue was
    primarily due to a $69.9 million decline from lost business in excess of new
    business"* (FY2025 10-K); Q3 FY2026 volumes −4.5%. Two years post-spin: revenue
    $2,825M → $2,735M, operating income $217.9M → $64.4M, covenant relief (leverage
    ceiling raised to 5.25x, dividends and buybacks banned by lenders, 2025-05-01), three
    CEOs in ~19 months, two 10(b) securities class actions on statements about "pricing
    practices," restructuring plan raised to $35-40M. **The attacker with the largest
    price advantage in the industry cannot hold its EXISTING customers against CTAS.**
  - **UNF — the disciplined attacker:** zero debt, 62% of garments self-made, growing
    +1.8% organic at a third of CTAS's margin — and its controlling family (Croatti,
    Class B, "approximately 70.9% of the combined voting power") **chose to sell to CTAS
    at ~$5.5bn** rather than keep competing. The #3's exit-by-sale is itself row
    evidence: the family that knew the business best priced continued independence below
    CTAS's offer.
  - Cost-structure decomposition of the gap (filed): CTAS in-service inventory 11.3% of
    revenue vs UNF 9.4% vs VSTS 14.8%; garment amortization CTAS 18-30 months vs VSTS
    1-4 YEARS (the laggard stretches its amortization furthest and still loses); CTAS
    unionization ~1.7% (800/48,100) vs VSTS ~59% (10,750/18,150). The gap is delivered
    cost per stop and asset turns — **density — not an extractable price premium.**
- **[E2-44], the two-characteristic test — both halves pass on filed language:** (1)
  price raised with demand flat: the FY2020 10-K, in the COVID year (Q4 organic −8.4%),
  still attributes revenue to "price increases"; every vintage FY2020-26 files the same
  attribution through the 2022-25 inflation, and volume HELD — every year's total organic
  line is attributed "primarily ... increased sales volume" (FY2023 +12.2%, FY2025 +8.0%,
  FY2026 +8.3%); (2) minor additional capital: capex 3.5% of revenue; pre-tax RONTA ~51%
  [E2-43].
- **[E4-55] — units, the brief's demand. What CTAS actually files:** routes (11,000 →
  12,500), facilities (528 → 484), organic growth by quarter, and segment margins.
  **What it does NOT file, and has never filed in any vintage read (FY2017-26): a
  customer-count series (the phrase "more than one million businesses" is IDENTICAL in
  the FY2017 and FY2026 10-Ks while revenue doubled), a retention rate, revenue per
  customer, wearer counts, or a price/volume split (the attribution sentence is verbatim
  boilerplate every year).** Absence recorded as a finding. The physical series that IS
  filed (routes, facilities) moves the right way; the honest unit series for wearers does
  not exist on this shelf.
- **Untapped pricing power [E3-33]: NO — the power is being USED** (price increases filed
  every year). Not the [E3-33] class; no near-monopoly claim made [E5-28] — the category
  is fragmented and in-house/direct-buy substitutes cap the price at the boundary.
- **The regulator's testimony:** the FTC issued a **second request** on the UniFirst
  acquisition (disclosed in the FY2026 Q4 ER, 2026-07-15). The antitrust authority's
  concern — that #1 buying #3 may lessen competition — is itself evidence the moat class
  is real. Recorded, not celebrated: a blocked deal returns UNF to the row; a cleared
  deal removes the #3 and leaves a covenant-constrained #2 and a private Alsco.
- Class: **[x] NARROW at the category boundary, dominance-class INSIDE the outsourced
  rental niche [E2-53]** — the in-house/direct-purchase substitute caps price and blocks
  a WIDE call at the perimeter; inside the niche, position not execution sets the
  economics (the FY2020 stress year: op margin held at 16.4%, OE rose). ·
  Direction: **WIDENING [E4-32]** — margin gap vs both filed peers grew every filed year,
  routes and per-route revenue rose, and the #3 is being absorbed.
- **VERDICT: [x] IN (NARROW, direction widening; dominance-class inside the niche)**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**None ticked → Q3 is a qualitative OVERLAY.** Record findings; manager quality alone does
not stop the run. **Any ticked → Q3 is a BINARY GATE and no price compensates.**
Case declared, and why: **OVERLAY.** The Q2 finding governs the weight [E3-43]: a
dominance-class position inside the niche is exactly the franchise that "can tolerate
mis-management" — the filed proof is FY2020, when a −8.4% organic quarter left the margin
flat and OE rising. A million weekly service promises are execution-heavy, but a lapse
bleeds customers over years (VSTS's decay took two years to reach covenant relief), it
does not kill in a quarter; no control position; leverage 0.7x debt/EBITDA, 0.47x
debt/equity — small asset errors cannot destroy equity.

**Honesty — binary, permanent, filings-based [E5-16].** *"understanding about business
mistakes; tolerance for personal misconduct is zero."* Each matter dated to when it became
PUBLIC: **no disqualifier found.** Item 3 ordinary-course boilerplate only, no named
material matter in any vintage read (FY2017-26); no restatement found across the five
vintages transcribed (one ~$11.6M operating/investing reclass between the FY2023 and
FY2025 presentations of FY2023, 0.7% of OCF — noted, below any threshold); related-person
items disclosed with dollars (Farmer-family airplane 25% interest, Cintas REIMBURSED
$3.87M; KMK Law $6.49M; all audit-committee reviewed). A 2011 10-K/A exists and was not
read (pre-window) — confessed in defects.

**STEP 2 — THE FOUR FLAGS [E4-22, E5-15].** *Accounting and disclosure, not litigation. Each
is a prompt to READ, never a verdict.*
- [ ] weak accounting — comp not expensed, fanciful pension assumptions → *"seldom just one cockroach in the kitchen"*
- [ ] unintelligible footnotes
- [x] trumpeted earnings projections / growth targets
- [ ] serial share issuance
- [ ] EBITDA / adjusted-earnings promotion **[E4-29]** *(the fifth flag; 12+ corpus statements)*
- [x] filed-figure tells: unnaturally smooth reported growth; cash-tax % of pretax falling **[E4-30]**
- For every box ticked, what the filing actually says:
  **Projections/guidance [E5-30] — FIRES.** The FY2026 Q4 ER (2026-07-15) guides FY2027:
  revenue $12.10-12.25bn, "adjusted diluted EPS" $5.36-5.50. An annual guidance culture of
  long standing — the ratchet is live. The [E3-48] action (guidance vs outturn across
  years) was NOT swept this run (ER archive not pulled); the culture is flagged, the
  base-rate check is an open item. Note also the vocabulary tell: "adjusted EPS" enters
  the lexicon WITH the UniFirst deal (FY2026: GAAP $4.91, adjusted $4.94, the only
  exclusion the $0.03 transaction expense — narrow and itemized today; [E2-49]-watch that
  the exclusion category does not widen post-close when deal amortization and integration
  costs arrive).
  **Filed-figure tells [E4-30] — fire and are ACQUITTED on the disclosed record.**
  Smoothness: quarterly organic growth FY2025-26 printed 8.0/7.1/7.9/9.0/7.8/8.6/8.2/8.4 —
  remarkably smooth, but the mechanism is structural (a million small accounts on weekly
  billing is a subscription book, not an accrual choice). Cash tax % of pretax: 19.1%
  (FY2021) → 13.9% (FY2022) → 17.2% (FY2023) → 16.0% (FY2026) vs ~20% ETR — not
  monotonic-falling, and the FY2026 wedge is a DISCLOSED mechanism: $183.7M cash paid to
  acquire transferable tax credits applied against federal tax (Note 8).
  **Not fired:** EBITDA 3 hits in the 10-K, all covenant/rating context, 0 in the ER;
  zero "restructuring" in any vintage read — one-times run as separate GAAP captions (G&K
  integration FY2018-19, UniFirst expenses FY2026), the anti-[E4-52] pattern; issued
  share count FALLING (402.9M → 400.1M outstanding), options proceeds trivial — no serial
  issuance [E5-15].

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity capital employed, *without
undue leverage or accounting gimmickry* — **not** EPS growth. Multi-year series, balance
sheet before income statement.
- Years used, and the series: **ROE on average equity: FY2020 27.1% → FY2024 38.4% →
  FY2025 40.3% → FY2026 40.7%**, at debt/equity 0.47x and debt/EBITDA ~0.7x — the "without
  undue leverage" clause is satisfied on the filed balance sheet. For the acquisitive
  filer the [E2-43] denominator: **pre-tax RONTA ~51%** (op income $2,606.5M on net
  tangible operating assets ~$5,066M = assets $10,529.1M − goodwill $3,544.2M − service
  contracts $287.9M − non-interest-bearing current liabilities $1,631.5M); with the
  goodwill wedge included, ~29% pre-tax — the wedge ($3.8bn, mostly G&K) reported
  separately as the rule requires. Either denominator: a top-decile business return.

**The half-owner test [E2-26]:** does this reporting tell me what I would want to know if the
positions were reversed? **Mostly yes:** one-time items quantified separately at every line
(FY2025 property gain $15.0M effect stated by segment; UniFirst costs split $15.1M S&A /
$1.0M interest; G&K integration a separate caption for two years). **The withheld half is
the unit economics [E4-55]:** no customer count, retention rate, or price/volume split has
ever been filed — the density story must be assembled from routes, facilities and margins.
A half-owner would want the retention number; it is not given. Recorded at Q2 as the
absence finding; here it bounds candor at "good on money, silent on units."

**The institutional imperative — score all four [E2-30].** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [ ] resists any change in current direction
- [x] projects/acquisitions materialise to soak up available funds — scored HALF: the
  tuck-in cadence ($164.5/$232.9/$186.8M FY2026/25/24) is the density strategy itself,
  adjacent and disciplined; but the $5.5bn UniFirst deal is the largest use of funds in
  company history and lands exactly when the core generates more cash than the tuck-in
  pipeline absorbs. Read against it: the deal is the same consolidation motion at scale
  (G&K 2017 precedent, successfully integrated on the filed margin record), priced at
  ~2.26x revenue / ~37x UNF's standalone earnings — rational only through the synergy
  math (UNF's $2.43bn revenue at CTAS-class margins would re-price the deal to ~14x
  pre-tax). **[E5-44] stock-deal arithmetic:** ~14.4M CTAS shares (0.7720 × ~18.6M UNF
  shares) + ~$2.9bn cash. Measured at our conservative IV (~$75/sh zero-growth) the paper
  given is ~$1.1bn, total ~$4.0bn given for $148M of standalone net income plus the
  synergy option — expensive at IV terms, cheap at quote terms (paying with richly-quoted
  paper favors the giver). Flag held with [E4-13] humility; binds position size.
- [ ] staff studies produced to justify the leader's craving — not observable from filings
- [ ] peer behaviour mindlessly imitated — the peers imitate CTAS, not the reverse

**Capital allocation — the two buyback conditions [E5-08]:**
- (1) ample funds for operations and liquidity? **Yes** — $289.0M cash + $438.7M
  investments, $2.0bn undrawn revolver, OCF $2,276M vs capex $395M.
- (2) repurchases at a **material discount** to conservatively calculated IV? **NO —
  CONDITION-2 FLAG.** FY2026 program purchases 3,960k at $196.38 avg; FY2025 3,794k at
  $179.07; post-YE $48.4M at $199.70 — all 2.3-2.9x our zero-growth band (~$70-85) and
  above even growth-credited constructions. A second $1.0bn authorization (2025-10-28)
  sits unused above the band. Stated with the humility clause **[E4-13]**: management
  knows the business better than we do, and on their own ~8-11% growth guidance the
  discount test may pass in their book; "many CEOs never stop believing their stock is
  cheap" [E5-08]. **Binds position size, never the discount rate.** The dividend leg is
  clean: RPM decomposition FY2022→26 — DPS +89.5% on EPS +68.6%, payout 32.6% → 36.7%,
  ~4/5 earnings-driven — **PASSES** (the anti-SBUX/TSCO pattern); dividends 2.5x covered
  by capex-end OE, no [E2-52] issuance funding (count falls), no [E2-60] leverage funding
  (debt flat $2.44bn across FY2024-26 while $4.2bn was paid out — all from operations).
  **The "40+ consecutive increases" claim the brief asked to verify: NOT FILED — zero
  occurrences of "consecutive" in the DEF 14A and no streak claim in Item 5. It is an
  IR-rung claim. Filed-year arithmetic verifies increases in every year checked
  (quarterly rate 0.39 → 0.45 = +15.4% FY2025→26; +17.4% FY2024→25); the pre-2022
  annual-to-quarterly transition makes the long streak unverifiable from the vintages on
  disk — recorded as verified-recent, unverified-deep.**
**THE GUARDRAIL — check before writing the verdict.**
- [x] Confirmed: nothing in this Q3 is being used to **promote** the name. A strong manager
      cannot repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**.
- [x] If this business **requires** a great manager, that is recorded at **Q2 as a moat
      defect [E4-23]** — recorded at Q2 as the Mayo-test PASS (three CEO generations, same
      trajectory); no key-person dependence claimed.
- [x] No manager-as-plan case is being made **[E2-35, E2-36]** — the franchise is intact
      and no surgery is proposed.

Additional conduct notes: **control read** — Scott D. Farmer (founder's son, Executive
Chairman) 14.3% of a SINGLE-CLASS register (contrast UNF's 10:1 Class B at 70.9% voting);
family influence without structural entrenchment. **Pay design:** annual cash incentive on
GAAP diluted EPS + sales growth — the FILED figures, no adjustment layer [the anti-EAT/
ACLS pattern]; FY2025 landed "between Target and Maximum" on both; 402(v): TSR $100 →
$384.67 (FY2020-25) vs peer group $203.00 — the [E3-54] retention direction is strongly
positive on the company's own filed table. Auditor E&Y, ratified annually. Ownership
culture: every employee-partner with >1,000 hours is a shareholder (proxy).

- **VERDICT: [x] IN (as OVERLAY — no disqualifier found)**
  *NOT a finding that the managers are honest — "sincerity and empathy can easily be
  faked" **[E5-17]**. IN never promotes. Live flags carried: guidance culture [E5-30];
  buyback condition-2 [E5-08] (binds position size); the [E5-44] UniFirst paper
  arithmetic; the adjusted-EPS vocabulary watch [E2-49].*

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** All hand-transcribed
from five 10-K vintages: `_research 2026-09-05 CTAS\OE - by-year series hand-transcribed.md`.
Construction: OCF − SBC − (c), (c) at TOTAL capex (see below).
- **Short-window mean** (window: 3-yr, FY2024-26): **$1,641.3M**
- **Default window** (5-yr, FY2022-26 **[E2-42]**): **$1,454.9M**
- **Long-window mean** (10-yr, FY2017-26): **$1,095.9M** · leave-two-out (drop best
  FY2026 + distorted FY2017): $1,100.5M · FY2026 alone (best year ever): $1,753.1M
- **Spread, conservative end:** 5-yr vs 3-yr **12.8%**; 10-yr vs 3-yr 33.2%
- **Combined range carried:** **$1,455M to $1,753M**, judged **$1,600M** — the [E4-41]
  normalization: FY2026 printed gross margin "equal to the all-time high" (Q4 ER) at the
  crest of the 2022-25 CPI-plus pricing period, so the judged level sits below the 3-yr
  mean; it stays ABOVE the 5-yr mean because the level is earned, not exogenous — the
  competitors did NOT file the same wave (VSTS revenue and margin FELL those same years;
  UNF crawled at +1.8%), volume was filed positive every year, and the margin gain is the
  density mechanism Q2 established, not a commodity price tailwind.
- Range too wide to conclude? **No** — the recent-window band is tight (12.8%).
- Distorted years NAMED [E5-11]: FY2016 (Shred-it sale taxes inside OCF, gain outside),
  FY2017 (G&K close: $2.1bn acquisition, transaction/financing costs), FY2021 (COVID
  capex cut to $143.5M vs $243.8M depreciation — the one year capex ran below D&A;
  flatters that year's capex-end OE), FY2022-25 (inflation pass-through pricing).
- Owner earnings by year (capex end, $M): 315.6 / 111.2 / 401.7 / 579.6 / 651.9 / 945.8 /
  1,105.2 / 1,187.6 / 1,163.1 / 1,542.0 / 1,628.7 / **1,753.1** (FY2015→FY2026)
- **Maintenance capex — the DISCLOSED JUDGMENT, and the brief's (c)-direction question
  [E3-44] answered from Note 1:** the rental model's working asset — garments in service —
  is NOT in capex at all. It flows through OCF as a working-capital line ("Uniforms and
  other rental items in service": −$137.6M FY2026), amortized 18-30 months. **So
  OCF−SBC−capex already charges the FULL garment investment INCLUDING the growth
  increment — [E2-23] constraint 3 is satisfied by construction, in the conservative
  direction.** For (c) proper: total PP&E capex $395.1M vs depreciation $318.6M (1.24x —
  the anti-railroad; [E5-20] does not apply); (c) judged at TOTAL capex, the conservative
  end, because the filing gives no maintenance/growth split (the TGT/SBUX precedent).
  run.py's "D&A end" ($513M incl. amortization) is INVALID for this filer — amortization
  of capitalized contract costs is added back in OCF while the current cash spend already
  sits inside the working-capital lines; using it as (c) double-counts. Displayed only as
  the screen's construction. Software capex is INSIDE the single filed capex caption
  ($464.6M gross internal-use incl. CIP, 10-yr life, $34.1M/yr amortization, Note 4) —
  the HAS missing-line defect does not bite, checked.
- Band used: **$1,455-1,753M, judged $1,600M**; the judged point sits below the 3-yr mean
  for the [E4-41] reason cited above.
- Stock compensation subtracted in full **[E5-06]**: yes, $128.1M (FY2026) and every year
  of the series; reported charge used as the floor of the measure [E3-70] (options +
  restricted stock; no repricing found).

### Great, good, or gruesome? **[E4-20]**
- [x] great — high return, rising, little capital needed
- [ ] good — attractive return, earned also on added capital
- [ ] gruesome — grows, eats capital, earns little
- Evidence: pre-tax RONTA ~51% and RISING (op margin 16.4% → 23.1% in six years); capex
  3.5% of revenue; OE grew $580M → $1,753M (FY2018-26) while cumulative capex ran only
  ~$2.7bn — the added deposits earned the high rate too (the good-class feature layered
  on the great-class rate). The strongest business economics yet run in this queue beside
  BMI, at 25x BMI's scale.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings **PASS** — twelve filed years positive and
  rising OE; the COVID stress year (Q4 FY2020 organic −8.4%) left full-year OE HIGHER
  (garment purchases fall with volume — the working asset is countercyclical to cash).
- (2) massive liquid assets **FAIL on the absolute test** — $289.0M cash + $438.7M
  investments against $999.0M of notes due FY2027. The $2.0bn undrawn revolver and CP
  program exist but are refused as counted support [E5-39] — bank lines are the kindness
  of strangers.
- (3) **no significant near-term cash requirements** — **FAIL AS FILED, named:** the
  $1.0bn 3.70% notes mature in FY2027, AND the UniFirst cash consideration ~$2.9bn is
  contracted, AND the filing states the plan: *"we expect to incur approximately $2.8
  billion in additional indebtedness and, if incurred, would have consolidated
  indebtedness of approximately $5.2 billion"* (FY2026 10-K risk factor), via bridge
  financing ($5.2M of bridge fees already paid, Note 6). The near-term stack is real and
  debt-market-dependent. Mitigants, filed: coverage after ample capex 17.7x [E2-54]
  ((2,276.3−395.1)/106.2, accrued interest counted); post-close ~$5.2bn debt against a
  combined ~$3.3bn EBITDA-class cash stream is ~1.6x; walls after FY2028 are empty until
  2032. **Scored FAIL/FAIL on strengths 2-3 in the EFX/MCD shape — survivable because
  strength 1 is enormous, but the file says so plainly rather than netting it away.**
- Leverage, named and quantified **[E4-16, E3-29]**: $2,436.6M face today (avg 4.1%,
  0.47x equity, ~0.7x EBITDA) → ~$5.2bn expected post-close (~1.6x). Covenants: liens,
  sale-leaseback, merger restrictions + a debt/EBITDA maintenance ratio (unquantified in
  the filing); cross-default provisions exist between debt instruments — named.
- ASC 842: operating leases PV $277.9M, 5.68-yr weighted term, $101.2M annual cost —
  **immaterial** against the stack (the immaterial streak resumes); no material finance
  leases disclosed.
- Contingent liabilities [brief item]: ordinary-course only in every vintage read;
  environmental spend disclosed and small ($30.0M opex + $5.8M capex FY2026); standby
  LCs/surety $125.8M; no persistence pattern — the flag does not fire.

### Name the specific way THIS business dies **[E2-27, E3-24]**
- **Mechanism 1 — the leveraged-integration stumble (exposure, not experience [E4-40]):**
  close the $5.5bn UniFirst deal onto ~$5.2bn of debt, inherit a 7.6%-margin target with
  an UNREMEDIATED ICFR material weakness (E&Y issued an ADVERSE opinion on UNF's controls
  as of 2025-08-30 — in the row file), plus FTC behavioral/divestiture conditions, and
  meet a recession in the same window. Quantified: blended margin falls ~2.7 points on
  consolidation day (11.3bn@23.1% + 2.4bn@7.6% → ~20.4%); a −10% revenue shock at ~50%
  detrimental margin costs ~$560M of operating income → combined op income still >$2.4bn
  against ~$230M of interest → coverage ~9x. Ugly for the multiple, nowhere near death.
  Likelihood of the stumble: **a real possibility**; of solvency distress from it: **a
  low-level possibility**.
- **Mechanism 2 — secular substitution at the category boundary** (casualization, remote
  drift, in-house programs): slow by nature; the filed record grew through thirty years
  of it; monitored at Q6 via organic volume attribution. **A low-level possibility.**
- **Mechanism 3 — the [E2-27] collective-irrationality loop** (industry price war): the
  live experiment ran 2023-26 and the LOW-margin players lost volume; a rational #2 in
  covenant relief cannot fund a war. **A low-level possibility.**
- *The honest bear at full strength [E4-51] is a VALUE case, not a death: the 2022-25
  CPI-plus wave lifted the margin to an all-time high exactly as $5.2bn of debt and a
  7.6%-margin acquisition arrive; if pricing normalizes, OE reverts toward the 5-yr
  $1,455M while the share count has been shrunk at ~$196 a share. Nothing in that
  sentence kills the company; all of it compresses the return.*
- **VERDICT: [x] IN**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."* Honest
pre-tax expectancy at this price: **~9% (range ~8.5-9.5%), judged — BELOW the ~10% line.
The name is quit on, not ranked** — and it is the closest approach to the floor in this
queue's history, so the judgment is shown in full below rather than asserted.
**No risk premium in the discount rate [E3-42]** — the bare 5.24% is used everywhere.

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no
vote **[E3-34]**.

**1. THE YIELD**
- owner earnings **$1,600M judged ($1,455-1,753M carried)** ÷ market cap **$80,222M** =
  **1.99% (1.81-2.19%)** · sovereign **5.24%** (US Treasury 30-yr, 2026-09-04)
- Every construction pays less than the bond — including the best year ever ($1,753.1M →
  2.19%) and the absolute-ceiling construction ((c) = depreciation only, FY2026: $1,829.6M
  → 2.28%).

**2. WHAT THE PRICE ALREADY ASSUMES**
- growth needed to match the bare bond at the judged OE: **+3.25%/yr perpetual**
  (range +3.05 to +3.43) — the strongest thing sayable for the price: CTAS at $200.47 is
  priced as a bond-plus-3¼%-perpetual-growth instrument, and the filed record covers that
  rate several times over.
- growth needed to clear the [E4-28] floor: **+8.0%/yr PERPETUAL** (10% − 2.0%).
- what the business has actually done: OE +9.7%/yr (5-yr), +14.8%/yr (8-yr); revenue
  +8.7%/yr (decade); diluted EPS +11.0%/yr (5-yr); FY2027 guidance +8.5-11.3% adj EPS.

**3. WHAT YOU ARE PAID**
- return at the current price = **−3.25 points UNDER the sovereign** (−3.43 to −3.06
  across the band) before any growth belief is spent.

**THE FLOOR JUDGMENT, argued both ways [E4-51/E4-26] — this is the whole verdict:**
- **The case FOR clearing (stated at full strength): CTAS is the first name in this
  queue whose FILED record exceeds the floor's required growth on every window.** The
  +8.0% perpetual the floor demands is BELOW realized 5-yr OE growth (+9.7%), below 5-yr
  EPS growth (+11.0%), below the decade's revenue-plus-margin compound, and below the
  company's own next-year guidance. Ten consecutive pre-UNF years of ≥7.6% organic
  growth except COVID; margins rising eight straight years; the #3 competitor being
  absorbed. If any business on the watchlist earns an 8%-forever belief, it is this one.
- **Why it still fails, by decomposition [E4-44, E2-63, E4-35]:** the decade's OE growth
  splits into revenue (~1.74x, FY2018-26) × margin expansion (op margin 14.7% → 23.1%,
  ~1.57x). **The margin lever is largely spent**: from 23.1%, even a heroic march to 28%
  yields ~+21% total (~+1.5-2%/yr for a decade, then ZERO — a lever that cannot be
  perpetual by arithmetic). The volume lever is bounded by US employment (+~0.5-1%/yr)
  plus share-take from a pool the company is already consolidating (post-UNF, CTAS+UNF
  ≈ 4x the #2), and the price lever is capped at the category boundary by the in-house/
  direct-buy substitute (the Q2 NARROW finding). Honest go-forward OE growth: **~6-8%/yr
  over the visible five years, decaying toward ~4-5%** — a perpetual-equivalent of ~6-7%,
  NOT 8%. [E4-35]'s base rate stands behind the decay assumption: sustained double-digit
  growth at the $80bn scale is a fewer-than-one-in-twenty event even among the best.
  Honest expectancy ≈ 2.0% + ~6.5-7% ≈ **~9%. Under the line. Quit on** — and if the
  honest growth number were three-quarters of a point higher the verdict would flip,
  which is stated so the next reader can re-run it rather than trust it.

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
- **Zero-growth at the sovereign (5.24%):** conservative **~$70/sh** ($1,455M ÷ 0.0524 ÷
  400.17M sh) · judged **~$75** · optimistic **~$85** (best-year and (c)=depreciation
  constructions reach ~$84-87) · **current price $200.47** — **above the ENTIRE band by
  2.3-2.9x** (Bar 2 outcome three).
- **At the [E4-28] floor (10%):** ~$36-44/sh, judged **~$40**.
- **The growth engine, displayed and casting no vote [E3-34]:** at the bond rate the
  quote is recovered with +3¼%/yr perpetual growth ($1,600M ÷ (0.0524 − 0.0325) ≈
  $80bn); at the floor the quote requires **+8.0%/yr PERPETUAL** — a rate the corpus's
  base-rate wager [E4-35] prices as a rare event to sustain for even twenty years, at a
  company already $80bn large. **The RPM dividend decomposition corroborates the RECORD
  without changing the arithmetic: DPS +89.5% FY2022-26 on EPS +68.6% — ~4/5
  earnings-driven, payout only 32.6% → 36.7% — a real-growth dividend, not a
  payout-expansion illusion; it testifies that the PAST 11% was genuine, and the floor
  question is about the perpetual future, which the decomposition cannot answer.**

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].** *(Corrected 2026-09-03, found by the
HHH run — this block still carried v4.0's "THERE IS NO HURDLE" heading, the SEVENTH
surviving home of the rule the framework rewrote on 2026-08-28. The floor section above at
[E4-28] already governs; this block is the ranking that applies only to what clears it.)*
- floor verdict first: honest pre-tax expectancy **~9% (8.5-9.5%)** vs ~10% **[E4-28]** —
  **below → quit on, and the ranking lines are not filled in.** The flip condition is
  stated in the floor judgment above: an honest perpetual-equivalent growth belief of
  ~8% instead of ~6.5-7% clears it; that belief was examined and refused on the
  [E4-44]/[E2-63] decomposition (the margin lever ~spent, volume employment-bounded,
  price substitute-capped).
- points over sovereign, this name: **−3.25** (recorded for the register; not a ranking).
- *Take the best available, or nothing — this name is neither ranked nor taken.*

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [x] **Screamer test [E4-01]** — the price does not approach the conservative case:
      $200.47 vs ~$70 conservative zero-growth; **above the whole range → outcome three,
      no.** No margin added on top.
- **Windage count: ONE** — the judged OE ($1,600M, below the 3-yr mean) is the single
  conservative placement; the value was then read at zero-growth with growth displayed
  separately and unspent, no rate premium [E3-42], no end-margin stacked **[E4-11]**.

- **VERDICT: FAIL — ON PRICE, AT THE [E4-28] FLOOR · not ranked (below the floor);
  UNRESEARCHED/UNKNOWABLE not applicable — the evidence is complete and the price
  decides.**

**ORDINAL NOTE (coordinator instruction, 2026-09-06):** the parallel CMG run cleared its
four business gates the same evening; by Q4-commit order CMG's gates closed first
(98635fe before 5775f90). The coordinator's rule is Q5-COMMIT timestamp: at the moment
this Q5 verdict is committed, no CMG Q5 commit exists in the log — **CTAS therefore takes
the ELEVENTH all-four-gates slot by the Q5-commit rule, CMG the twelfth, subject to the
log itself if CMG's Q5 commit proves earlier.** The mechanism is stated so the queue
entry can be corrected from the log, not from memory.

**ADDENDUM (operator rule 6), 2026-09-06, after both files closed:** the log reveals the
two parallel runs were handed CONTRADICTORY tiebreak rules — CMG's close applied a
Q4-COMMIT rule (98635fe 16:21:05 vs 5775f90 16:22:45 → CMG first) and its queue entry
already claims eleventh; this run's instruction was Q5-COMMIT (cfc8d7b 07:06:17 vs
5956a80 07:06:21 → CTAS first by four seconds). Both timestamp claims are true; the rules
conflict; the four-second Q5 gap is coordination noise, not information. **Resolution: the
queue's already-committed ruling stands (CMG eleventh, CTAS TWELFTH by the Q4-commit
rule), and the conflict is recorded here rather than re-litigated by editing a parallel
run's committed entry.** The coordination defect (two rules issued for one ordinal) is
confessed in both files' defect lists by reference to this addendum.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Q6 NOT OPENED FOR ENTRY — the file closed at Q5 with no position. Recorded here instead,
per queue convention, is the pre-committed re-look [E1-02]:**
- **Re-look price: ~$75/sh zero-growth judged at a 5.24% sovereign — recomputed at the
  rate of the day, never at this one.** A price near the top of the zero-growth band
  (~$85) re-opens Q5 arithmetic; the floor judgment would still need the growth question
  re-argued, not assumed.
- **The file RE-OPENS (not re-prices) at UniFirst close** — the DKS/ACLS perimeter rule:
  post-close CTAS is a different company (~$5.2bn debt, +~14.4M shares, a 7.6%-margin
  book to integrate, FTC conditions if any). Re-run Q4/Q5 on the combined filings; the
  FY2027 10-K is the document.
- Reopen tests, dated: (1) FTC outcome — a BLOCK returns UNF to the competitor row as an
  independent #3 and voids the [E5-44] flag; (2) FY2027 organic growth <+5% or the first
  negative organic quarter outside a recession — the volume half of the floor argument;
  (3) the adjusted-EPS exclusion category widening beyond the $0.03 transaction item
  [E2-49] — the vocabulary watch; (4) buybacks continuing at 2.5x+ the band funded by
  post-merger debt [E2-60]; (5) VSTS filing positive volumes — the row's price-umbrella
  argument weakens if the #2 stabilizes.
- Thesis-confirming metric (if ever entered): organic growth ≥7% with the attribution
  sentence still reading volume-led; rental margin holding ≥23% through the UNF dilution.
- **Thesis-breaking metric and its threshold:** two consecutive years of organic growth
  <+4% (the honest-growth floor under the ~9% expectancy judgment collapses toward ~7%).
- Next catalyst date: UniFirst close (expected H2 calendar 2026) → FY2027 Q2 10-Q
  (~January 2027) shows the first combined balance sheet.

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

- **VERDICT: Q6 not opened (no entry); re-look block recorded above.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN → Q2 IN → Q3 IN → Q4 IN →
      Q5 FAIL on price → Q6 not opened)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — the two
      scoped items are load-bearing NOWHERE: the dividend-streak depth is marked IR-rung
      and unverified-deep inside a Q3 that passes on other evidence; Alsco's absence is a
      stated [E3-61] row limit (private, no filings exist — the TSCO/BMI precedent), not
      a provisional moat
- [x] Every UNRESEARCHED verdict names the artifact — none were issued
- [x] Every UNKNOWABLE verdict states what cannot be known — none were issued
- [x] Step 0: FY2026 10-K read (MD&A, cash-flow detail lines, footnotes), accession
      0000723254-26-000028; OCF/capex/SBC cross-checked against the filed statement
- [x] OE on multi-year means; four windows displayed; (c) a disclosed judgment at total
      capex with the garment-increment direction argued from Note 1
- [x] Competitor row filled from UNF/VSTS filings on identical formulas; row limit stated
- [x] Sovereign: US Treasury 30-yr par yield, issuing authority, 5.24%, 2026-09-04
- [x] Value as round-number ranges (~$70-85 zero-growth; ~$36-44 floor)
- [x] One bar (screamer, outcome three); windage count ONE, stated
- [x] Price dated 2026-09-04, aggregator, flagged as live-quote-only
- [x] Run committed to git after every question (incl. the kill-wave preservation commit)

**DEFECTS CONFESSED (assume the brief has an error — it had several):**
1. **The brief's Q2 premise was stale on the industry structure**: it cast UNF as the
   attacker row; CTAS had signed to ACQUIRE UniFirst on 2026-03-10, before the brief was
   written. Found at Step 0 from the filing.
2. **Brief arithmetic: "CTAS runs ~2x UNF's margin" — actual 3.0x** (23.1% vs 7.6%,
   identical GAAP formulas); and UNF is the **#3** by revenue, not #2 (VSTS files itself
   second-largest).
3. [E3-48] guidance-vs-outturn base-rate sweep not performed (prior-year ER archive not
   pulled); the guidance-culture flag is carried without its calibration.
4. The 2011 10-K/A was not read (pre-window amendment).
5. The [E5-44] arithmetic uses ~18.6M UNF shares inferred from the ~$5.5bn deal value,
   not a hand-read UNF cover count.
6. FY2023 cross-vintage reclass (~$11.6M of OCF, 0.7%) noted, unexplained by any filed
   sentence found.
7. run.py's weighted-average share basis again (406.2M vs cover 400.17M) — the standing
   screen defect, corrected by hand.
8. Session kill mid-Q5; **zero question loss** under the write-early protocol (the
   coordinator's kill-wave commit a8886a3 preserved the floor judgment mid-write) — and
   the kill-wave commit swept CMG+CTAS files together (the structural broad-add defect,
   again).
9. **The ordinal coordination defect:** the two parallel runs were issued contradictory
   tiebreak rules (Q4-commit vs Q5-commit) for the same eleventh/twelfth ordinal — see
   the ADDENDUM at Q5. Resolved by letting the queue's first-committed ruling stand.

## REGISTER
- Verdict: **FAIL at Q5, ON PRICE, at the [E4-28] floor — about the price, not the
  business. Q1 IN · Q2 IN (NARROW, widening) · Q3 IN (overlay) · Q4 IN — the TWELFTH
  name to clear all four business gates (per the ordinal ADDENDUM at Q5: the queue's
  committed Q4-commit ruling stands, CMG eleventh; the contradictory-rules coordination
  defect is recorded there).**
- One line: **The best route-density economics in the queue at any scale — 51% pre-tax
  RONTA, eight years of rising margins, the #3 being absorbed — priced at 1.99% against
  a 5.24% bond, needing +8.0% PERPETUAL growth to clear the floor; the filed record
  covers that rate, the [E4-44]/[E2-63] decomposition says the levers that produced it
  are mostly spent; honest expectancy ~9%: quit on, not ranked.**
