# Company Run — Walmart (WMT) — 2026-09-06
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
- rate **5.24%** · date **2026-09-04** (latest row; struck fresh 2026-09-06) · source: **US
  Treasury daily par yield curve, 30-yr, issuing authority direct** (CSV pull saved to
  `_research 2026-09-06 WMT/sovereign-raw.txt`)
- FX: n/a — USD quote, USD reporting and predominantly USD earnings (Walmart International
  is ~17-18% of revenue and earns foreign currencies; consolidated reporting and the
  dominant Walmart U.S. segment are USD; noted, not adjusted)

**PRICE AND COUNT (Stage 0 by hand):**
- Price **$107.14**, 2026-09-04 close — **Yahoo aggregator, live quote only, flagged**
- Shares **7,933,746,241** hand-read off the Q2 FY2027 10-Q cover (single class of common
  stock, $0.10 par, as of 2026-08-26; acc 0000104169-26-000154, filed 2026-08-28)
- **3:1 split of 2024-02-23 guard verified:** the cover count is post-split scale (~7.93bn
  vs ~2.65bn pre-split); per-share figures in the same filing are post-split ($0.80 diluted
  for the quarter); the brief's split-guard question answered YES, handled correctly
- **Market cap $850,022M** (7,933,746,241 × $107.14)

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes (contingencies, debt,
  leases, SBC via research transcription; MD&A + cash-flow statement + Note 1 read directly
  by the analyst — `_research 2026-09-06 WMT/analyst-filing-read-notes.md`)
- document · date · accession no.: **FY2026 10-K, FYE 2026-01-31, filed 2026-03-13, acc
  0000104169-26-000055** (primary doc wmt-20260131.htm); supplemented by Q2 FY2027 10-Q,
  period 2026-07-31, filed 2026-08-28, acc 0000104169-26-000154
- figure cross-checked against the filed statement: **OCF FY2026 $41,565M — MD&A
  free-cash-flow table vs the filed Consolidated Statements of Cash Flows; identical. Capex
  $26,642M identical both places.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: Walmart buys everyday goods —
  mostly food and consumables — in the largest volumes in world retail, moves them through
  a self-owned national distribution network at the lowest delivered cost per unit in the
  industry, and resells them at a gross margin (24.2% FY2026) deliberately set below what
  higher-cost competitors need to live on. Volume is the flywheel: more volume → lower unit
  cost → lower price → more volume. 68% of sales are U.S. mass retail off an essentially
  frozen store base (4,611 units, 699M sq ft, both flat three years); ~18% international;
  ~14% a membership warehouse club (Sam's). On top of the goods margin it now sells the
  traffic itself: supplier advertising, marketplace commissions and fulfillment fees, and
  membership subscriptions — income earned twice on the same customer visit, at margins
  several times the goods margin.
- The scarce input this business controls: **delivered-cost density** — purchasing scale
  plus a store/DC lattice within ~10 miles of most of the U.S. population, built over sixty
  years, which functions as both the cheapest shelf and (now) the cheapest last-mile
  e-commerce fulfillment network in U.S. grocery. No attacker can assemble it without
  decades of capital and zoning. Second, the traffic base itself — ~convenience-frequency
  visits that advertising and membership monetize a second time.
- Will the fundamentals look broadly the same in ten years? Yes at the mechanism level:
  people will still buy groceries and staples at the lowest delivered price, and scale will
  still set that price. The fulfillment mode is shifting (eCommerce contributed ~4.3 points
  of the FY2026 U.S. comp — effectively all of it), but the shift runs THROUGH the store
  lattice ("primarily driven by store-fulfilled pickup and delivery" — FY2026 10-K), i.e.
  the same asset, monetized a second way. Simple, stable in character **[E3-31]**.
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

## Q2 — IS IT A FRANCHISE? **[E3-03]**
- Needed or desired [x] — groceries and staples; the most-visited retailer in the country
- No close substitute [x] **at the level the claim is actually made**. The correct framing
  is not "no substitute for a can of beans" — substitutes for the *goods* are everywhere.
  The claim is [E2-58]'s exception itself: **a cost advantage that is both wide and
  sustainable**, in a business whose output is otherwise commodity. That is a claim about
  *delivered cost per unit*, and it is testable against the row below.
- Not price-regulated [x] at the enterprise level. **One filed exception, recorded:** the
  Q2 FY2027 10-Q attributes a Walmart U.S. comp drag to "the impact from **maximum fair
  price regulation** on certain prescription drugs, which went into effect in January
  2026" — quantified in the ER at **125 bps of comp**. Health-and-wellness is one of three
  merchandise units; the regulation caps a category, not the business. Recorded as a
  category-level [E3-03](3) exposure, not an enterprise failure.
- Must the moat be continuously rebuilt? **No — and this is the [E4-04] scope test done
  properly.** Walmart spends enormously ($26.6bn FY2026, 3.8% of sales) but the filed
  allocation shows what the spend BUYS: only **$1,406M — 5.3% of capex — is "New stores
  and clubs"**. $5,571M is remodels of the same boxes, $16,468M is "supply chain,
  customer-facing initiatives, technology and other." The store lattice itself — 4,611
  units, 699M sq ft, both flat for four filed years — is not being replaced; it is being
  re-plumbed. Under the framework's own test (*does a lapse in spending destroy the
  structure, or merely narrow it — and does the spending defend the same advantage, or buy
  its replacement?*): a spending lapse would narrow Walmart's delivery lead, not dissolve
  its purchasing scale or its real estate. **This is [E5-23] maintenance of one advantage,
  not [E4-04] periodic replacement of the basis.** Contrast Mitsui's Rhodes Ridge.
- Does success depend on a great manager? **No, and the corpus's own test is available in
  the file:** McMillon's retirement is announced for 2027-01-31 with Furner named
  successor (2026 proxy) — and the FY2026-FY2027 record does not turn on it. More to the
  point, [E2-53]'s dominance test: Walmart's position, not its execution, sets its
  economics — it earned a 5.2% U.S. segment margin in the year it took a $0.9bn
  self-insurance charge and a $0.7bn PhonePe charge. No [E4-23] key-person defect recorded.

### Primary moat metric, filing-sourced, and its trend — AND THE [E4-55] FINDING

**[E4-55] asks for the physical series where units exist. For Walmart the honest answer is
an ABSENCE, and it is a real result about the attacker of record.** Recorded sweep by the
analyst over every vintage on disk — FY2016 and FY2017 Exhibit 13, FY2018, FY2019, FY2020,
FY2022, FY2023, FY2024, FY2025 and FY2026 10-Ks, and the Q2 FY2027 10-Q — for "average
ticket", "ticket", "transactions increased", "transaction growth", "traffic", "number of
transactions", "average transaction", "customer traffic", "comp transactions":
**no numeric transactions/ticket decomposition was found in any 10-K or 10-Q vintage.**
Every hit is a risk-factor boilerplate list item or a qualitative MD&A attribution
sentence. Walmart files the *direction* of both components and never the *magnitude*.

**This project has convicted two companies on a series Walmart does not file about
itself.** The DG run and the TGT run each used Walmart U.S. comps as the attacker's
instrument; TGT's own twelve-year traffic/ticket table is fully numeric, DG's is partly
numeric, and Walmart's is not filed at all. Stated plainly rather than glossed.

**The split does exist, one rung down and one frequency up — and it runs 42 quarters.**
The quarterly earnings release (8-K ex-99.1, "Business Highlights") carries a numeric
quarterly transactions/ticket split **unbroken from Q1 FY2017 (release 2016-05-19, acc
0000104169-16-000083) through Q2 FY2027** — 58 releases fetched, 42 quarters transcribed
(`_research 2026-09-06 WMT/quarterly-transactions.md`). The **full-year columns of that
same table read "NP — Not provided" in every vintage.** So the correct statement of the
[E4-55] position is: **Walmart files the decomposition quarterly and refuses it annually.**

**WALMART U.S. TRANSACTIONS %, as first reported, ten years by fiscal quarter:**

| FY | Q1 | Q2 | Q3 | Q4 | (ticket, same order) |
|---|---|---|---|---|---|
| 2017 | +1.5 | +1.2 | +0.7 | +1.4 | −0.5 / +0.4 / +0.5 / +0.4 |
| 2018 | +1.5 | +1.3 | +1.5 | +1.6 | −0.1 / +0.5 / +1.2 / +1.0 |
| 2019 | +0.8 | +2.2 | +1.2 | +0.9 | +1.3 / +2.3 / +2.2 / +3.3 |
| 2020 | +1.1 | +0.6 | +1.3 | +1.0 | +2.3 / +2.2 / +1.9 / +0.9 |
| **2021** | **−5.6** | **−14.0** | **−14.2** | **−10.9** | +16.5 / +27.0 / +24.0 / +21.9 |
| 2022 | **−3.2** | +6.1 | +5.7 | +3.1 | +9.5 / −0.8 / +3.3 / +2.4 |
| 2023 | flat | +1.0 | +2.1 | +1.8 | +3.0 / +5.5 / +6.0 / +6.3 |
| 2024 | +2.9 | +2.9 | +3.4 | +4.3 | +4.4 / +3.4 / +1.5 / −0.3 |
| 2025 | +3.8 | +3.6 | +3.1 | +2.8 | flat / +0.6 / +2.1 / +1.8 |
| 2026 | +1.6 | +1.5 | +1.8 | +2.6 | +2.8 / +3.1 / +2.7 / +2.0 |
| 2027 | +3.0 | +1.5 | — | — | +1.1 / +1.1 |

**[E2-44](1) RE-ESTABLISHED PRECISELY ON THE QUARTERLY DATA — and the brief's claim needs
one correction and gains one much stronger fact.**
- **The correction:** transactions were **negative in five consecutive quarters** — all
  four of FY2021 and Q1 FY2022 — bottoming at **−14.2%**. The brief's "held traffic
  positive through the price wave" is right about 2022-25 but the COVID trough was severe,
  and ticket carried the whole business (+27.0% in Q2 FY2021). Stated rather than glossed.
- **The much stronger fact: transactions have been positive in every one of the twenty-one
  quarters from Q2 FY2022 through Q2 FY2027**, and in **every pre-COVID quarter back to Q1
  FY2017**. Excluding the pandemic distortion, Walmart U.S. has not reported a negative
  traffic quarter in a decade. Against this project's own files: TGT posted traffic
  −2.4% (FY2023) and −2.2% (FY2025); KR filed "a reduction in the number of units sold."
- **The peak-inflation year was ticket-led, and this matters:** FY2023 ran transactions
  flat/+1.0/+2.1/+1.8 against ticket +3.0/+5.5/+6.0/+6.3. Walmart *did* take price in the
  wave. **The traffic re-acceleration came AFTER pricing decelerated** — FY2024-25
  transactions +2.9→+4.3 and +3.8→+2.8 while ticket fell to −0.3/flat. That is the
  sequence a genuine share-gainer produces, and it is the CMG-style demand-not-elasticity
  read, filed.
- **Two definitional breaks are recorded, not smoothed:** Q1 FY2020 renamed "Traffic" to
  "Transactions" and redefined it to include all eCommerce transactions (FY2019 restated);
  Q1 FY2021 redefined eCommerce net sales to include certain pharmacy transactions (FY2020
  restated). The series is not continuously comparable across those two points. A
  restatement register of 22 as-reported-vs-restated disagreements was built; all but
  three sit inside those breaks. **One unexplained oddity carried:** Q4 FY2019 Walmart U.S.
  comp restated 4.2% → 4.1% with no footnote found. **From Q1 FY2021 forward every
  current-quarter value matches the prior-year column published a year later — 24 quarters,
  zero exceptions**, which is a real internal check across documents filed a year apart.
- **Sam's Club U.S.:** transactions **+5.3%** (Q4 FY26) and **+7.0%** (Q2 FY27) on ticket
  **−1.3%** and **−2.5%** — average ticket negative four straight quarters (Q3 FY26 → Q2
  FY27) while trips accelerate. A club growing purely on frequency, which is the Costco
  shape — at a 2.6% segment margin against Costco's 3.85%.

**The eleven-year comp series with the filed attribution language** *(calendar basis, with
fuel; e-commerce contribution as filed)*:

| FY | comp | eComm pts | filed attribution |
|---|---|---|---|
| 2016 | +1.0 | +0.2 | "Positive customer traffic" |
| 2017 | +1.6 | +0.4 | "driven primarily by positive customer traffic" |
| 2018 | +2.1 | +0.7 | (no attribution given) |
| 2019 | +3.7 | +1.3 | "ticket and traffic growth" |
| 2020 | +2.9 | +1.7 | "ticket and transactions growth" |
| 2021 | +8.7 | +5.4 | ticket up "**while transactions decreased**" (COVID trip consolidation) |
| 2022 | +6.4 | +0.7 | "average ticket and transactions" |
| 2023 | +7.0 | +0.7 | "average ticket ... as well as growth in transactions" |
| 2024 | +5.5 | +2.6 | "**transactions** combined with growth in average ticket" |
| 2025 | +4.8 | +2.9 | "**transactions and unit volumes**" |
| 2026 | +4.3 | +4.3 | "average ticket and transactions ... **growth in unit volumes**" |
| H1-27 | +3.8 | +5.1 | "**transactions** and average ticket" |

**[E2-44](1) — THE 2022-25 RECORD, ESTABLISHED PRECISELY.** The two-characteristic test
asks whether it can raise prices when demand is flat. Walmart's filed record through the
price wave is stronger than the brief's claim, and one year is an exception the brief did
not have:
- **Transactions were filed POSITIVE in every fiscal year of the wave — FY2022, FY2023,
  FY2024, FY2025, FY2026 — and in H1 FY2027.** The one negative-transaction year in the
  eleven is **FY2021**, the COVID year, and the filed reason is trip consolidation
  (customers buying more per visit), not lost customers.
- Deflated **[E4-55]**: CPI food-at-home rose **+25.2%** CY2020→CY2025 and all-items
  **+24.4%** (BLS, `cpi-deflators.md`). Walmart U.S. nominal comps compounded
  **+31.6%** FY2022-FY2026 (1.064×1.070×1.055×1.048×1.043). **Real comp ≈ +5.1%
  cumulative over five years** — modest but POSITIVE, achieved with positive transactions
  every year, on a store base that did not grow. That is the honest deflated read: Walmart
  did not out-run inflation by much, but it out-ran it while every attacked name in this
  project's files lost traffic (TGT traffic −2.4/−2.2 in FY2023/FY2025; KR filing
  "a reduction in the number of units sold"; DG traffic only +1.1/+1.6 after years of
  decline).
- **[E2-44](2) — grow dollar volume "with only minor additional investment of capital":
  THIS HALF FAILS ON THE FILED RECORD, and it is the most important finding in the run.**
  Capex has gone $10.1bn (FY2018) → $26.6bn (FY2026), from 2.0% to 3.8% of net sales,
  while the store count *fell*. Property and equipment net went $107bn (FY2024-era) →
  **$136,083M** at FY2026, +13.4% in one year. The growth is NOT capital-light.

### THE MARGIN-MIX SHIFT — the brief's live Q5 question, answered from the filings

The claim to test: advertising (~$6.4bn), membership and marketplace are re-rating the
P&L, so operating income compounds faster than sales, durably. What the filings show:

- **The high-margin streams are real and growing fast.** "Global advertising business grew
  **46% to nearly $6.4 billion**, including VIZIO" (FY2026 ER); Walmart Connect U.S. +41%;
  "Membership fee revenue grew **15.1%** globally"; membership-and-other income $5,488M →
  $6,447M → $6,750M FY2024-26.
- **But three filed facts discipline the extrapolation.**
  1. **Advertising is not a disclosed revenue line and part of it is not revenue at all.**
     The ER's own footnote: *"Our global advertising business is recorded in **either net
     sales or as a reduction to cost of sales**, depending on the nature of the advertising
     arrangement."* A recorded sweep of the FY2022-FY2026 10-Ks found **no dollar
     advertising-revenue figure in any of them** — the only advertising dollars in a 10-K
     are advertising *costs* ($5.4bn FY2026, and rising alongside). The $6.4bn lives in an
     8-K exhibit. It also rides inside the comp metric by definition, so the same dollars
     appear in the "e-commerce contribution to comp" the moat is being judged on.
  2. **[E2-63]/[E4-44], the CTAS lesson — which lever is spent.** Decompose the decade,
     revenue × margin:
     - **Consolidated FY2016→FY2026: revenue ×1.479, operating margin ×0.84 (5.0%→4.2%),
       operating income ×1.237.** Ten years, $231bn of additional revenue, and operating
       income grew 23.7% — **+2.2%/yr**. The margin lever was not merely unspent; it ran
       *backwards* for a decade.
     - **Walmart U.S. segment FY2015→FY2026: sales ×1.677, operating margin 7.4% → 5.2%,
       OI ×1.179.** Eleven years, +$195bn of segment sales, +17.9% of segment operating
       income. **The segment's margin fell 2.2 points while the high-margin flywheel was
       being built.** The mix shift is not re-rating the P&L; it has been *offsetting*
       price investment and cost-to-serve. That is the answer to the brief's live question,
       and it is the opposite of the prior.
  3. **The company's own stated objective was missed on GAAP in the most recent year.**
     MD&A: *"Our objective is to achieve operating income leverage, which we define as
     growing operating income at a faster rate than net sales."* FY2026 GAAP: **OI +1.6%
     vs net sales +4.7%.** It was met only on the adjusted-constant-currency basis (+5.4%).
     Filed drags: ~$0.9bn self-insured general-liability claims, $0.7bn PhonePe SBC
     modification, and *"increased depreciation related to our capital investments"* — the
     last of which is the capex flowing through, and it recurs.
- **The honest counterweight, stated at full strength [E4-51]:** the *direction* since
  FY2023 is real. Walmart U.S. segment margin 4.9% → 5.0% → 5.2% → 5.2%; gross profit rate
  23.5% → 24.2%; FY2027 guidance is adjusted OI +6-8% on sales +3.5-4.5%. If the mix shift
  compounds, the decade's margin decay is the *old* regime and the recent three years the
  new one. **The burden of proof sits with that claim [E4-35]**, and the framework's base
  rate is that fewer than 10 of the 200 most profitable companies sustain 15% EPS growth
  over twenty years. Walmart is asking to be believed at the top of that distribution
  after a decade of 2.2%/yr operating-income growth.

### THE COMPETITOR ROW — required [E3-28]

Same metric, same window (fiscal years ending Jan/Feb 2026, except COST to Aug 2025), all
filing-sourced. Peer instruments taken from this project's own completed runs.

| Company | comp/ID sales, last 3 FY | physical direction (units/traffic) | operating margin | store base direction | source |
|---|---|---|---|---|---|
| **Walmart U.S.** | **+5.5 / +4.8 / +4.3** | transactions positive every year; "growth in unit volumes" | **5.2%** | **4,615→4,605→4,611; 699M sq ft flat** | WMT FY2026 10-K, acc 0000104169-26-000055 |
| Walmart Inc. (total) | n/a | — | 4.2% | 10,955 units | same |
| **COST** (FYE 2025-08-31) | +6% (+8% ex gas/FX) | **frequency +5%**; 81.0M paid members, renewal 92.3% US | 3.85% | growing | COST run; acc 0000909832-25-000101 |
| **TGT** | −3.7 / +0.1 / **−2.6** | **traffic −2.4 / +1.4 / −2.2** | 4.9% GAAP (4.6% adj) | flat/declining | TGT run; acc 0000027419-26-000016 |
| **KR** | +0.9 / +1.5 / +2.9 | **"a reduction in the number of units sold"** | **1.28% GAAP** (3.32% adj FIFO) | 2,731→2,697 stores | KR run; acc 0001104659-26-037723 |
| **DG** | +0.2 / +1.4 / +3.0 | traffic +1.1 / +1.6 | 5.16% | still opening stores | DG run; acc 0001104659-26-032325 |
| **AMZN North America** (CY2025) | no comp concept filed | "increased unit sales" (directional) | **6.9%** ($426.3bn sales, $29.6bn OI) | — | AMZN FY2025 10-K, acc 0001018724-26-000004 |
| **Sam's Club U.S.** (for the club sub-row) | +2.3 / +4.7 / +2.9 | transactions +5.3% Q4 FY26 | 2.6% | 601 clubs | WMT FY2026 10-K |

- **Peers named: 6 of the ~6-8 real competitors** (COST, TGT, KR, DG, AMZN, plus Sam's
  vs COST as an internal sub-row). Publix, Aldi/Lidl, H-E-B, Trader Joe's and Wegmans are
  **private or foreign-owned and file nothing** — named, not stretched over. Aldi and Lidl
  are the most material omission: they are the true hard-discount attackers on Walmart's
  own price flank and no filed data exists for them. **This does not make the class
  PROVISIONAL** — the moat claim here is a *relative delivered-cost* claim, and the row's
  five filed public peers all sit below Walmart on margin and below it on units. But the
  limit is recorded.
- **[E3-61] the row's limit, stated:** the row shows position, not conduct. Identical
  structures produce opposite outcomes and *"you'd have to know the people involved."*
- **[E2-45] — THE ATTACKER'S TEST, and Amazon's two-decade record IS the answer.** The
  brief is right that this is the crux, and the answer cuts BOTH ways, which is why it is
  written out in full:
  - **What Amazon took:** general merchandise and the discretionary middle. Online stores
    revenue $91.4bn (2016) → **$269.3bn (2025)**; third-party seller services $23.0bn →
    **$172.2bn**; advertising ≤$2.95bn (inside "Other") → **$68.6bn**; subscriptions
    $6.4bn → **$49.6bn**. North America segment operating margin **6.9%** in 2025 —
    *higher than Walmart U.S.'s 5.2%*. That is not a failed attack. Amazon's advertising
    business alone is **more than ten times** Walmart's $6.4bn, on a smaller retail base.
  - **What Amazon did NOT take, and this is the load-bearing half:** the grocery basket
    and the store-fulfilled last mile. Amazon's "Physical stores" line — Whole Foods and
    the store experiments, the closest thing it has to Walmart's format — went $17.2bn
    (2018) → **$22.6bn (2025)**: +31% in seven years, while Walmart U.S. added $164bn of
    sales. Amazon bought Whole Foods in 2017 for $13.7bn to attack exactly this and, on
    its own filed line, it has barely moved. Walmart's grocery lattice took the
    e-commerce war *inside its own stores*: FY2026's entire U.S. comp is e-commerce
    contribution (+4.3 of +4.3), "primarily driven by store-fulfilled pickup and
    delivery." Amazon had every advantage — capital, talent, a twenty-year head start
    online, no legacy cost structure — and did not break the delivered-cost position in
    food. **That is the strongest single piece of evidence for [E2-58]'s wide-and-
    sustainable exception in this file.**
  - The honest reading of both halves: **Walmart's moat is real and it is narrower than
    the enterprise.** It is a *food-and-consumables delivered-cost* moat with a
    store-fulfilment last mile bolted to it. It is not a moat over general merchandise
    (Amazon took that), not a moat over advertising (Amazon is 10x bigger), and not a moat
    over the club format (Costco out-earns Sam's on every filed metric: 3.85% vs 2.6%,
    $272M vs ~$155M per warehouse, disclosed 92.3% renewal vs no disclosure at all).
- **[E3-33] untapped pricing power: NO, and deliberately so.** Walmart is the one company
  in this queue where the *refusal* to raise price is the strategy — FY2025's gross-margin
  driver is filed as *"managing prices aligned to our competitive historic price gaps."*
  Under **[E5-28]** claiming the untapped-pricing class would be claiming near-monopoly,
  and the row refuses it: Amazon at 6.9% NA margin and Costco at 92.3% renewal are live
  alternatives. Under **[E4-37]**'s inverse metric, Walmart is the rare case where price
  restraint is a *chosen* investment rather than an agony — but the framework does not
  award a moat for pricing power that is real and unexercised without near-monopoly
  evidence, and there is none.
- **[E4-32] direction — the primary criterion.** Widening or narrowing? **Mixed, and I
  judge it WIDENING on position and FLAT-TO-NARROWING on economics.** Widening: share
  gains against every filed peer for three consecutive years on positive transactions from
  a frozen store base; the delivery network is a genuinely new advantage that did not
  exist in 2016; membership and advertising are new profit pools. Narrowing/flat: eleven
  years of falling segment operating margin, capex at 3.8% of sales and rising, ROI
  falling (15.5% → 15.1%) *because* of the capital going in. **The moat is widening in
  units and not in returns.** That distinction is the whole of the Q5 problem below.
- **[E3-46] the number, asked about the business:** unleveraged pre-tax return on net
  tangible assets **~22.3%** (OI 29,825 / NTA ~$133.8bn, analyst-computed from the filed
  balance sheet), ~17.2% after tax; ROE **23.0%** FY2026, ten-year mean **17.2%**. These
  are good, not extraordinary — and they are the numbers of a business that must own
  $136bn of property to earn them.

- Class: [ ] WIDE [x] **NARROW** [ ] NONE [ ] PROVISIONAL · Direction: **widening in
  units and share, flat-to-narrowing in returns**
  *Why NARROW and not WIDE, against the brief's prior of "possibly IN WIDE": the moat is
  real, durable and demonstrated by the best attacker record available — but it is
  narrower than the enterprise it is being asked to cover. Two-thirds of Walmart is a
  food-and-consumables delivered-cost position that Amazon failed to break; the rest is
  general merchandise Amazon is beating it in, a club format Costco is beating it in, and
  an international segment whose operating income FELL in FY2026. And the [E2-58]
  exception's own test is economic: a wide and sustainable cost advantage should show up
  as returns that hold or rise. Walmart's held its position and gave up 2.2 points of
  segment margin doing it. WIDE is not available on those filings.*
- **VERDICT: [x] IN (NARROW)  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**None ticked → Q3 is a qualitative OVERLAY.**
**Case declared: OVERLAY.** Reasons, each against its source:
- **Control [E1-16]: no.** Minority position in a listed security; exit is a keystroke.
- **Leverage [E3-29]: no.** Total debt $51.5bn (ER definition, incl. finance leases)
  against $105.9bn of equity and $41.6bn of annual operating cash flow. Interest paid
  $2,793M against OCF of $41,565M — coverage of ~5.3x *after* the entire $26.6bn capex
  bill. Nothing here where small asset errors destroy equity.
- **Daily execution [E3-38/E3-43]: examined, and NOT ticked — because the natural
  experiment is already in the filings.** The honest argument *for* ticking it: 2.1M
  associates, 4,600 pharmacies, food handling at national scale — and the opioid record
  proves dispensing decisions cost real money ($3.3bn accrued FY2023). The argument that
  wins: the corpus's test is whether poor management can *kill* the business, and
  Walmart's filed record is [E5-18]'s "capacity to stand it" demonstrated four separate
  times — a $3.3bn opioid accrual (FY2023), a $283M FCPA resolution (2019), the Asda and
  Seiyu exits (FY2021), and the FY2019 year in which "Other (gains) and losses" of
  $8,368M cut net income to $6,670M. Through every one of those, **Walmart U.S. segment
  operating income and comparable sales never went negative.** This is [E2-53]'s dominance
  class: position, not execution, sets the economics.
**Q3 is therefore an OVERLAY. Findings are recorded; manager quality alone does not stop
this run — and per the guardrail below, it cannot promote it either.**

**Honesty — binary, permanent, filings-based [E5-16].** *"understanding about business
mistakes; tolerance for personal misconduct is zero."* Each matter dated to when it became
PUBLIC:

**THE OPIOID RECORD, DATED, BOTH WAYS (the brief's TJX-precedent test):**
- **Against.** *United States v. Walmart Inc.* (D. Del., **filed 2020-12-22**) — DOJ civil
  Controlled Substances Act suit alleging Walmart's pharmacies filled invalid
  prescriptions and its distribution centers failed to report suspicious orders. Conduct
  period pre-dates the suit by years. **2022-11-15**: Walmart announced agreement to
  resolve substantially all state/subdivision/tribal opioid claims "for up to
  approximately $3.1 billion." **Fiscal 2023**: accrued **$3.3 billion**. MDL No. 2804
  still carries **~230 cases against the Company as of 2026-03-06**, plus 13 others in US
  and Canadian courts. *Florida Health Sciences Center*: jury trial ran 2025-09-18 to
  2025-12-08 and ended in a **MISTRIAL**; retrial set for **2026-08-27**. The DOJ suit's
  remaining dispensing theory survived the 2024-03-11 partial dismissal and is **set for
  trial November 2027**. On these unsettled matters the filing states the Company "has not
  accrued a liability ... nor can [it] reasonably estimate any loss or range of loss."
- **For.** The settlement carried "**no admission of wrongdoing or liability**." The
  accrual was taken in one year, disclosed at the line, and **"As of January 31, 2025, all
  of the accrued liability had been paid"** — paid in full out of operating cash flow with
  no financing event and no dividend interruption. Walmart won a partial dismissal of the
  DOJ case (all distribution claims and one of two dispensing theories dismissed
  2024-03-11) and the one case that has actually reached a jury did not produce a verdict
  against it. Distribution — the more culpable half — is out of the case.
- **The judgment, under [E5-22] (penalty size is not seriousness; the failure that counts
  is not acting when you learn):** this is a **priced business mistake, not an integrity
  finding**. It cost ~1.5 months of operating cash flow, it was disclosed and paid, the
  conduct was corporate-systemic rather than personal misconduct by named officers, and no
  officer-level enforcement action exists in the record read. It does not trigger
  [E5-16]'s zero-tolerance binary, which is about **personal misconduct**. The residual
  exposure — an unquantified DOJ trial in Nov 2027 and ~230 live MDL cases — is carried
  into Q4's named deaths and Q6's monitoring, not resolved here.
- **Contingency persistence [the brief's test]: the opioid liability did NOT persist —
  accrued FY2023, fully paid by 2025-01-31.** That is the opposite of the persistent-
  accrual pattern the test looks for. What persists is *litigation*, not *accrual*.
- **Other dated matters, both directions:** FCPA resolved **2019-06-20**, $283M paid
  (recorded in fiscal 2018 in anticipation — the accrual preceded the announcement, which
  is the candid direction); WMT Brasilia pleaded guilty to one books-and-records count.
  FTC/State AG *Driver Platform* action — stipulated order **2026-03-03**, $100M judgment
  with ~$63M suspended, **$37M accrued** at 2026-01-31, ten-year programmatic obligations,
  no admission. Asda equal-value claims (~73,000 claimants, UK, running since 2008),
  liability with Asda post-divestiture but Walmart indemnifies "up to a contractually
  determined amount" — phase-three hearing **2026-11-23**, no accrual, no estimable range.
  Mexico COFECE penalty 93.4M pesos (~$5M), appealed 2025-01-06. India CCI investigation
  (ordered 2020-01-13; DG report 2024-09-13) and the Flipkart FDI show-cause notice (July
  2021). EPA Clean Air Act Finding of Violation, October 2023.
- **No personal-misconduct disqualifier found in the filings read.** Per [E5-17], that is
  the absence of found disqualifiers, not a finding that the managers are honest.

**STEP 2 — THE FOUR FLAGS [E4-22, E5-15].** *Accounting and disclosure, not litigation. Each
is a prompt to READ, never a verdict.*
- [ ] weak accounting — **NOT FIRED.** SBC expensed in full and footnoted by award type
  ($3,603M FY2026). Ernst & Young, **auditor since 1969** (57 years — long, noted, but the
  corpus supplies no tenure rule). Unqualified ICFR opinion. Four cross-vintage checks by
  the transcription agent (FY2018, FY2022, FY2023, FY2024 each in two vintages) returned
  **identical figures on every target line**; the only differences found were an ASU
  2016-18 restricted-cash recast and a line-level investing reclass that nets to zero.
- [ ] unintelligible footnotes — **NOT FIRED.** Plain, and the lease, debt and contingency
  notes tie to the balance sheet (operating 1,631 + 13,941 = 15,572 ✓).
- [x] **trumpeted earnings projections / growth targets — FIRED, and it is the loudest flag
  in the file.** Quarterly *and* annual guidance on **net sales (cc), adjusted operating
  income (cc), and adjusted EPS**: FY2027 net sales +3.5-4.5%, adjusted OI **+6.0-8.0%**,
  adjusted EPS $2.75-2.85 (Q4 FY26 ER, 8-K acc 0000104169-26-000032). The 10-K's own risk
  factors name the mechanism: failure to meet "comparable store and club sales growth rates
  or earnings and **adjusted earnings per share**" could cause the stock to decline.
  **[E5-30]: this is a ratchet, not a year's fact** — *"once you start it, it's all over."*
  The guidance culture is fully institutionalized here.
  **[E3-48] action taken:** FY2027 guidance (+6-8% adjusted OI) is set against a FY2026 in
  which **GAAP operating income grew 1.6%**. The company's own stated objective — *"growing
  operating income at a faster rate than net sales"* — was **missed on GAAP in FY2026**
  (+1.6% vs +4.7%) and met only after adjustment (+5.4% cc). A full multi-year
  guidance-vs-outturn sweep of earnings releases is **an open item, confessed as a defect**.
- [ ] serial share issuance — **NOT FIRED; the opposite.** Share count is falling: 8,080M
  (Feb 2023, equity statement) → **7,933,746,241** (10-Q cover, 2026-08-26). FY2026
  repurchases **85.0 million shares for $8.1 billion** (ER) = **~$95.29 average**.
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRED, but SCOPED.** Counted by the
  analyst: **"EBITDA" appears ZERO times in the FY2026 10-K**, and "adjusted" appears 7
  times, none of them promoting a non-GAAP earnings measure. The 10-K is GAAP-clean. The
  flag fires **one rung out**: the earnings releases run on adjusted EPS and adjusted
  operating income (cc), guidance is issued only on the adjusted basis, and **the incentive
  plan is built on adjusted metrics** (below). The distinction matters and is recorded:
  the *filed annual report* does not promote non-GAAP; the *communication and pay layer*
  runs on it entirely.
- [x] **filed-figure tells [E4-30] — CASH-TAX TELL FIRES, AND IS ACQUITTED.** Income taxes
  paid ÷ income before income taxes: **FY2024 26.9% ($5,879 / $21,848) → FY2025 22.4%
  ($5,884 / $26,309) → FY2026 18.2% ($5,364 / $29,469)** — three consecutive years of
  decline, the exact shape [E4-30] flags. **Acquitted from the filed face:** the effective
  *book* rate moved the other way (25.5% → 23.4% → **24.4%**), and the reconciling item is
  disclosed on the cash-flow statement — **deferred income taxes swung to +$2,277M in
  FY2026** from −$635M and −$175M, i.e. capex-driven timing on a $26.6bn spending year.
  Not a fraud tell. **But it is an [E4-41] normalization item: roughly $2.0-2.5bn of
  FY2026 operating cash flow is tax timing that reverses, and Q4 carries it down.**
  Reported growth is *not* unnaturally smooth — operating income went 24.1 / 22.8 / 20.4 /
  22.0 / 20.6 / 22.5 / 25.9 / **20.4** / 27.0 / 29.3 / 29.8 ($bn, FY2016-26). A filer
  willing to print a 21% operating-income drop (FY2023) is not smoothing.

**A sixth item, from [E2-49] (metric-switching) and [E2-26] — the incentive-plan wedge,
recorded as a candor CASE, not a flag:** operating income *for incentive plan purposes* is
**$31,320M against $29,825M reported** (+$1,495M), while sales for plan purposes are
**$694,284M against $706,413M reported** (−$12,129M). Both adjustments are itemized in the
proxy, and the company states the direction against itself, verbatim: *"For fiscal 2026,
these adjustments, taken as a whole, had the impact of **reducing our total company sales
and increasing our operating income** for incentive plan purposes."* Naming which way your
own adjustments cut is the [E2-26] half-owner standard met. The largest FY2026 exclusion is
the **$0.7bn PhonePe share-based-compensation modification** — i.e. an SBC charge excluded
from the pay metric. That is the [E4-29] mechanism operating inside the pay design, and it
is where the flag actually bites.

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity capital employed, *without
undue leverage or accounting gimmickry* — **not** EPS growth. Multi-year series, balance
sheet before income statement. Equity read off the filed balance sheets across vintages;
return computed on **average** Walmart shareholders' equity.

| FY | NI attr. to Walmart $M | avg equity $M | **ROE** |
|---|---|---|---|
| 2016 | 14,694 | 80,970 | **18.1%** |
| 2017 | 13,643 | 79,172 | 17.2% |
| 2018 | 9,862 | 77,834 | 12.7% |
| 2019 | 6,670 | 75,182 | **8.9%** |
| 2020 | 14,881 | 73,582 | 20.2% |
| 2021 | 13,510 | 77,797 | 17.4% |
| 2022 | 13,673 | 82,089 | 16.7% |
| 2023 | 11,680 | 79,973 | 14.6% |
| 2024 | 15,511 | 80,277 | 19.3% |
| 2025 | 19,436 | 87,437 | 22.2% |
| 2026 | 21,893 | 95,315 | **23.0%** |

**Ten-year mean 17.2%; five-year mean (FY2022-26) 19.2%; and the trend is UP.** Against
[E2-42]'s red-light test (below the return on equity earned by American industry in
aggregate), Walmart passes comfortably. **[E2-43] scope applied:** unleveraged pre-tax
return on net tangible assets ≈ **22.3%** (OI $29,825M ÷ ~$133.8bn), ~17.2% after tax —
computed by the analyst from the filed balance sheet with goodwill ($28,735M) stripped out
separately rather than hidden in book equity. **Note the tension this creates with Q2:**
ROE rose over the decade while *operating margin fell* — the equity return is rising partly
because the share count is shrinking and equity is being held down by buybacks, not only
because the business earns more. Both facts are filed; both are carried.

**The half-owner test [E2-26]:** **PASSES, with one substantive complaint.** Passes:
one-time items are quantified separately at the line ($0.9bn self-insurance, $0.7bn
PhonePe, $3.3bn opioid, $0.8bn International restructuring — each named with its dollar
figure in MD&A rather than buried); the capital-expenditure allocation table is filed with
a numeric split by purpose, which most retailers in this project's files do not provide;
the incentive-plan adjustments are itemized *and* their net direction is stated against the
company's own interest; ROI is reconciled to ROA. **The complaint:** the two disclosures a
half-owner would most want on the [E2-58] moat claim — the **annual** transactions/ticket
split, and **advertising revenue in dollars** — are exactly the two withheld from the 10-K.
The quarterly ER prints transactions and ticket and then writes **"NP — Not provided"** in
the full-year columns of the same table. Advertising is disclosed once a year as a growth
rate in a press release and is *"recorded in either net sales or as a reduction to cost of
sales"* — a construction under which no reader can size it from the filed statements.
**Deliberate or not, the effect is that the two series on which the franchise claim rests
cannot be verified annually from the filings.** Recorded as the file's principal
disclosure defect.

**The institutional imperative — score all four [E2-30].** *Not a fraud test.*
- [ ] resists any change in current direction — **NOT SCORED.** The opposite: Walmart
  rebuilt its fulfilment model, exited the UK and Japan, and bought VIZIO for advertising.
- [x] **projects/acquisitions materialise to soak up available funds — SCORED, mildly.**
  Capex has gone from $10.1bn (FY2018) to $26.6bn (FY2026) and is guided to $25-27bn for
  FY2027; $16.5bn of FY2026 sits in one caption, *"Supply chain, customer-facing
  initiatives, technology and other."* ROI fell 15.5% → 15.1% *because of it*, by the
  company's own explanation. This is not an imperative *failure* — the automation case is
  coherent — but the pattern (cash generated, cash absorbed by a large internally-defined
  program, returns dipping) is exactly what [E2-30](2) describes, and it is the single
  largest capital decision in the file.
- [ ] staff studies to justify the leader's craving — no evidence found.
- [x] **peer behaviour mindlessly imitated — SCORED, mildly.** The advertising/marketplace/
  membership "flywheel" is Amazon's model, adopted by every large retailer at once (TGT's
  Roundel, KR's ad business, COST's membership). Walmart is the best-positioned imitator,
  but imitation it is; and the row shows the originator is 10x larger in the imitated line.

**Capital allocation — the two buyback conditions [E5-08], plus the third [E4-31]:**
- **(1) ample funds for operations and liquidity? YES.** $41.6bn OCF, $10.7bn cash, $14.9bn
  free cash flow after the entire capex program, dividend covered ~5.5x by OCF.
- **(2) repurchases at a material discount to conservatively calculated IV? NO — FAILS.**
  FY2026: **$8,088M spent, 85.0 million shares, ~$95.29 average.** February 2026: a **new
  $30 billion authorization**, replacing the prior one, struck at a ~$105-110 share price.
  H1 FY2027: **$5,104M** more, with $25.1bn of the authorization remaining. Against the
  zero-growth value range computed at Q5 below (**~$26-50/share, judged ~$37**; the single
  most generous construction on record — the best year ever at the D&A end — reaches only
  ~$57), every one of those repurchases was made at roughly **1.7x to 2.6x** value — and
  the $30bn authorization commits ~3.5% of the market cap to continuing at that level.
  **→ CAPITAL ALLOCATION FLAG, live.**
- **(3) [E4-31] shareholders supplied the information needed to estimate value?**
  Partially — and the two gaps are the ones named in the half-owner test above.
- **The humility clause [E4-13], stated:** this rests on *our* IV range, built on a
  zero-growth construction; management knows this business better than we do, and *"many
  CEOs never stop believing their stock is cheap"* [E5-08] — infractions here are innocent.
  **The flag binds POSITION SIZE ONLY, never the discount rate.**
- **[E2-52] dividends-funded-by-issuance: does NOT fire.** Dividends $7,507M and buybacks
  $8,088M — $15.6bn returned — against $41.6bn of OCF, with net share count *falling*.
  Nothing is being replaced by issuance.
- **[E2-60] restricted earnings: does NOT fire, and this is worth stating** because it is
  where retailers usually break. Total debt rose only $51.5bn-ish against $15.6bn/yr of
  distributions; equity ROSE from $91.0bn to $99.6bn in the same year. The payout is not
  being funded by leverage.
- **RPM DIVIDEND DECOMPOSITION (the brief's test): PASSES on the recent window, and the
  long record is weaker than the streak implies.** Dividends declared per share, filed,
  split-adjusted at 3:1 where pre-2024: FY2016 $0.653 · FY2017 $0.667 · FY2018 $0.680 ·
  FY2019 $0.693 · FY2020 $0.707 · FY2021 $0.720 · FY2022 $0.733 · FY2023 $0.747 · FY2024
  $0.76 · FY2025 $0.83 · FY2026 **$0.94** · FY2027 **$0.99** (announced Feb 2026).
  - **Five-year (FY2022→FY2026): DPS +28.2% on diluted EPS +68.5% ($1.62→$2.73); payout
    ratio FELL from 45.3% to 34.4%. Entirely earnings-driven. PASSES.**
  - **The longer record is the honest qualifier: FY2016→FY2023 DPS rose 14.3% in seven
    years — +1.9%/yr, below inflation.** The "consecutive increases" streak was kept alive
    through the flat decade by token 2-cent (pre-split) raises. A streak maintained by
    rounding is a fact about the streak, not about the earnings.
- **THE 50+ YEAR DIVIDEND CLAIM — ABSENCE FINDING, recorded sweep.** Searched the FY2026
  10-K, the 2026 DEF 14A, and the Q4 FY2026 earnings release for "consecutive":
  **zero hits in all three.** The consecutive-year claim appears in **no filed document
  read** — it lives on the corporate press release, which is **rung 3 (company IR site),
  and is labelled as non-filed here.** What *is* verifiable from filings: DPS increased in
  **every one of the fourteen fiscal years FY2013-FY2027** on the filed series above.
  Deeper than FY2013 is unverified in this run.
**PAY VERSUS PERFORMANCE (Item 402(v)), 2026 proxy, acc 0001193125-26-173673:**
TSR $100 → **$272.28** against peer index **$164.12** over the five-year table — real
outperformance, not manufactured. PEO (McMillon) SCT $29,240,930 / compensation actually
paid $36,488,421 for FY2026; FY2025 CAP was **$101,500,051** on a year TSR went 123.22 →
222.20 (the 402(v) equity-revaluation mechanic, flagged not judged). **CEO pay ratio
958:1** — CEO $29,240,930 against a median associate at **$30,520**. Company-selected
measure **Net Sales**; the three named measures are Net Sales, Operating Income, Return on
Investment — **all three "adjusted to exclude certain items."** Annual cash incentive paid
112% of target (capped 125%); performance equity 107% (capped 200%); targets are set
against plan, and the FY2026 payout of 112% on a year of +1.6% GAAP operating income growth
is the clearest single illustration of what the adjustment layer does. One-year performance
period plus two-year service vesting is a **short** performance window for a business whose
capital cycle is a decade. **Noted, not charged:** new hire Daniel Danker at $44,092,488 for
a partial year including a **$20M sign-on** grant and two annual grants in one fiscal year;
McMillon's retirement set for 2027-01-31 with his performance shares vesting on retirement.

**THE GUARDRAIL — check before writing the verdict.**
- [x] Confirmed: **nothing in this Q3 is being used to promote the name.** The Q2 verdict
      was decided on filed unit and margin series and the competitor row, not on management
      quality. **[E2-37, E2-38, E3-39]**
- [x] This business does **not** require a great manager — recorded at Q2 as the *absence*
      of an [E4-23] defect, with McMillon's announced succession as the live test.
- [x] Not a Pygmalion case: no [E2-35/E2-36] question arises — nothing here is being bought
      on the strength of a turnaround plan.

- **VERDICT: [x] IN (as an OVERLAY)  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *IN = **no disqualifier found**, which per [E5-17] is not a finding that the managers are
  honest — "sincerity and empathy can easily be faked." Two live flags carried forward: the
  **guidance ratchet [E5-30]** and the **buyback condition-2 failure [E5-08]**, the latter
  binding position size only. **IN never promotes.***

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** *"Using precise numbers is,
in fact, foolish; working with a range of possibilities is the better approach."* Do **not**
pick a window and defend it; carry the spread alongside the capex band.
**Method (CONVENTION, per the framework): OE = OCF − SBC − (c).** OCF nets the
working-capital change from one audited line, satisfying [E2-23] constraint 3. SBC is
subtracted in full **[E5-06]** — $3,603M in FY2026, and note it has grown 8x in the
window ($448M FY2016), which is why netting it matters here more than in most files.

**Owner earnings by year ($M), hand-built from five 10-K vintages** *(OCF − SBC, then both
capex ends; see `_research 2026-09-06 WMT/oe-series.md` for the transcription with
accession numbers and four cross-vintage checks)*:

| FY | OCF | SBC | capex | D&A | **OE, (c)=capex** | **OE, (c)=D&A** |
|---|---|---|---|---|---|---|
| 2016 | 27,552 | 448 | 11,477 | 9,454 | 15,627 | 17,650 |
| 2017 | 31,673 | 596 | 10,619 | 10,080 | 20,458 | 20,997 |
| 2018 | 28,337 | 626 | 10,051 | 10,529 | 17,660 | 17,182 |
| 2019 | 27,753 | 773 | 10,344 | 10,678 | 16,636 | 16,302 |
| 2020 | 25,255 | 854 | 10,705 | 10,987 | 13,696 | 13,414 |
| 2021 | 36,074 | 1,169 | 10,264 | 11,152 | 24,641 | 23,753 |
| 2022 | 24,181 | 1,163 | 13,106 | 10,658 | 9,912 | 12,360 |
| 2023 | 28,841 | 1,578 | 16,857 | 10,945 | 10,406 | 16,318 |
| 2024 | 35,726 | 2,093 | 20,606 | 11,853 | 13,027 | 21,780 |
| 2025 | 36,443 | 2,769 | 23,783 | 12,973 | 9,891 | 20,701 |
| 2026 | 41,565 | 3,603 | 26,642 | 14,203 | 11,320 | 23,759 |

**THE SINGLE MOST IMPORTANT FACT IN THIS TABLE:** at the capex end, owner earnings in
FY2026 ($11,320M) are **lower than in FY2017 ($20,458M)** — nine years, +$227bn of
revenue, and the cash left after the capital bill went *down*. At the D&A end they rose
from $20,997M to $23,759M, **+1.4%/yr**. Everything at Q5 follows from which of those two
series you believe, and the honest answer is "between them."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**

| window | mean OCF−SBC | mean capex | mean D&A | capex/D&A | OE, (c)=capex | OE, (c)=D&A |
|---|---|---|---|---|---|---|
| **3-yr FY2024-26** | 35,090 | 23,677 | 13,010 | **1.82x** | 11,413 | 22,080 |
| **5-yr FY2022-26** | 31,110 | 20,199 | 12,126 | 1.67x | 10,911 | 18,984 |
| **10-yr FY2017-26** | 30,062 | 15,298 | 11,406 | 1.34x | 14,765 | 18,657 |

- **Short-window mean** (3-yr FY2024-26): $11,413M (capex end) / $22,080M (D&A end)
- **Long-window mean** (10-yr FY2017-26): $14,765M (capex end) / $18,657M (D&A end)
- **5-yr leave-two-out** (drop best and worst): $10,546M capex end. **10-yr leave-two-out:
  $14,139M.** The trimmed means sit essentially on the untrimmed ones — no single year is
  carrying the result.
- **Spread, conservative end: 5-yr $10,911M vs 10-yr $14,765M = 35.3%.**
- **Combined range (window spread × capex band): $10,911M to $22,080M** — a **2.02x**
  width, and the widest band in this queue's history.
- ***Is the range too wide to reach a conclusion [E4-25]? NO — and the reason is the whole
  point of the run.*** The range is wide in *dollars* and irrelevantly wide in *decision
  terms*: **every construction in it, including the most generous, yields under the
  sovereign.** Top of band $22,080M ÷ $850,022M = **2.60%** against a 5.24% bond. The best
  single year ever recorded at the most generous (c) — FY2026 at the D&A end, $23,759M —
  yields **2.80%**, still 2.4 points under the bond. A range that reaches the same verdict
  at both ends *is* a conclusion, and [E4-25]'s "no useful conclusion" escape does not
  apply. **This is why the file proceeds rather than closing here.**
- **The distorted years, named in both directions [E5-11, E4-41]:**
  - **UP: FY2021** (COVID). OCF $36,074M — the second-highest ever, on capex held to
    $10,264M. Pantry-loading and stimulus. Inflates any window containing it.
  - **UP: FY2026 cash-tax timing.** Established at Q3: income taxes paid fell to 18.2% of
    pretax income while the book rate rose, with deferred taxes swinging +$2,277M.
    **Roughly $2.0-2.5bn of FY2026 OCF is timing that reverses.** Normalized down.
  - **DOWN: FY2022** ($24,181M OCF) — the inventory rebuild; working capital consumed cash.
  - **DOWN: FY2023** — carries the $3.3bn opioid accrual and ~$0.8bn International
    restructuring. Per **[E5-33]**, these are real costs and they **stay in** the mean.
  - **DOWN, structurally: FY2019** — net income $6,670M against $8,368M of "Other (gains)
    and losses" (the Flipkart/investment marks). Non-cash; OCF unaffected.
  - **The [E4-41] normalization is applied downward**, not upward: the FY2021 COVID year
    and the FY2026 tax timing are both favourable exogenous breaks, and both are inside
    the windows.

### Maintenance capex — a DISCLOSED JUDGMENT, and this is the run's hardest call

**Which case is this?** Walmart sits **between** [E3-44]'s default and [E5-20]'s exception,
and the file has unusually good evidence for placing it, because **Walmart FILES the
measured split** — the answer to the brief's question is **YES** (the DG/TSCO/CMG
precedent). FY2026 "Allocation of Capital Expenditures":

| bucket | FY2026 $M | judgment |
|---|---|---|
| New stores and clubs, incl. expansions and relocations | 1,406 | **pure growth — excluded from (c)** |
| Store and club remodels | 5,571 | **maintenance of competitive position — included in full** |
| Supply chain, customer-facing initiatives, technology and other | 16,468 | **split ~50/50** |
| Walmart International | 3,197 | **~half maintenance** (International units grew 5,566→5,743) |
| **Total capex** | **26,642** | |
| **+ finance-lease ROU additions** (the COST/HD addendum fix) | **703** (FY26; 1,455 FY25; 1,572 FY24 — avg ~1,240) | **added: debt-funded capital that never touches the capex line** |

- **The argument the D&A end is INVALID here:** capex has run at **1.5-1.9x depreciation
  for four consecutive years** while the store base *shrank* (4,769 units FY2019 → 4,611
  FY2026) — so this is not renewal of a growing footprint, it is a re-tooling of a fixed
  one, and depreciation charged on 1990s-vintage buildings cannot measure the cost of
  2026-vintage automated fulfilment (**[E4-47]**: replacement cost in current dollars
  outruns depreciation charged in old dollars). D&A is also *rising fast* (10,658 → 14,203
  in four years) precisely because the spend is being capitalized — the gap is a build-phase
  timing artifact that closes.
- **The argument the capex end is too harsh:** only **5.3% of capex is new stores**, and
  the physical lattice is genuinely maintained cheaply. A large slice of the $16.5bn is
  real expansion of throughput, which the [E2-23] test explicitly excludes from (c).
- **The tiebreaker, and it is a filed number: what did the incremental capital earn?**
  FY2023-26 capex totalled **$87,888M** against D&A of $49,974M — **~$37.9bn of net new
  capital**. Consolidated operating income went from $25,942M (FY2022, the last clean
  pre-opioid year) to $29,825M — **+$3,883M**. That is a **10.2% pre-tax / ~7.7% after-tax
  incremental return** on the retained capital, *below* [E5-40]'s ~12% "quite satisfactory"
  benchmark. If the incremental capital were genuinely expansionary it should be earning
  the business's ~22% return on tangible assets; it is earning less than half that. **The
  most likely reading is that a substantial share of what is booked as growth capex is in
  fact the price of standing still against Amazon — i.e. it belongs in (c).**
- **(c) JUDGED at ~$17,000M** — roughly **64% of FY2026 total capex** (which lands
  Walmart just above [E5-20]'s railroad benchmark of *"higher than 60 percent"*), ~1.2x
  FY2026 D&A, **including ~$1.2bn/yr of finance-lease ROU additions**. **This is a guess
  and is labelled one [E2-23].** Where in the band and why: **nearer the capex end than the
  D&A end**, on the incremental-return arithmetic above and the four-year capex/D&A ratio.
- **Band carried: $10,911M to $22,080M.** **Judged OE ≈ $15,500M** (5-yr base $31,110M
  less judged (c) $17,000M = $14,110M; 3-yr base normalized for tax timing ~$34,360M less
  $17,000M = $17,360M; midpoint ~$15,500M).
- **Does the capex band change the verdict → UNKNOWABLE? NO.** Stated explicitly because
  the template requires it: the verdict is identical at both ends of the band. See above.
- Stock compensation subtracted in full **[E5-06]**: **yes, $3,603M FY2026**, from the
  share-based-compensation footnote (it is not a cash-flow face line; it sits inside "Other
  operating activities"). **[E3-70] caveat recorded:** the reported charge is the floor of
  the correct subtraction, not the measure.

### Great, good, or gruesome? **[E4-20]**
- [ ] great — high return, rising, little capital needed
- [x] **good** — attractive return, earned also on added capital
- [ ] gruesome — grows, eats capital, earns little
- **Evidence, and the call is genuinely close to the gruesome line.** *Good*, because the
  return on capital is real and high (ROE 23.0%, ten-year mean 17.2%; ~22.3% pre-tax on net
  tangible assets), the business throws off $41.6bn of operating cash, and it is not
  consuming capital it cannot fund. *Not great*, because [E4-20]'s great class "requires
  little capital" and Walmart requires $26.6bn a year and guides to $25-27bn more. *Not
  gruesome*, because the added capital does earn a return — ~10.2% pre-tax incrementally —
  which clears [E4-20]'s "unless the cash they consume gets to earn a reasonable return"
  carve-out, if only just. **[E4-43] governs the consequence: the good class PASSES Q4 and
  ranks below great at Q5. That is all this finding does.**

### Staying power — score all three **[E5-11]**
- **(1) large and reliable stream of earnings — PASS, emphatically.** $41.6bn OCF; positive
  operating income in every year of the filed record including the opioid year, the
  pandemic year and the Flipkart-writedown year. This is one of the most reliable earnings
  streams in the queue's history.
- **(2) massive liquid assets — PASS on a relative basis, MARGINAL in absolute terms.**
  $10,727M cash at FY2026 (11,529M at Q2 FY2027) against $51.5bn of total debt — a cash
  balance equal to ~5 days of revenue. But the correct read for a retailer is the earnings
  stream plus the inventory-to-payables float: **accounts payable $63,061M against
  inventories $58,851M — suppliers finance the entire inventory and $4.2bn more.** Per
  **[E3-52]** this is the good kind of liability: customer/supplier-prepaid, no covenants,
  self-renewing. Recorded as a pass with the mechanism named rather than the cash number.
- **(3) no significant near-term cash requirements — PASS, and it is the rarest pass in
  this queue.** Long-term debt maturities: FY2027 **$3,542M** · FY2028 $3,237M · FY2029
  $3,389M · FY2030 $2,143M · FY2031 $2,600M · thereafter $23,255M. Against $41.6bn of
  annual OCF, the entire next-five-years maturity wall ($14.9bn) is **four months of
  operating cash flow.** No wall exists. FY2026 issuances carry **"no financial covenants
  which restrict the Company's ability to pay dividends or repurchase Company stock."**
  Short-term borrowings $6,596M (→$10,479M at Q2 FY2027) is commercial paper, and per
  **[E5-39]** it is *not* counted as support — but nothing depends on it either.
- **Leverage, named and quantified [E4-16, E3-29]:** total debt ~$51.5bn (incl. finance
  leases) against $105.9bn equity and $41.6bn OCF — **~1.2x OCF**. Interest paid $2,793M;
  **coverage after the entire capex bill = ($41,565 − $26,642) / $2,793 = 5.3x** — the
  [E2-54] test (all interest met out of current cash flow net of ample capex) passes with
  room. Operating lease PV $15,572M (11.3-yr WA term); finance lease PV $6,761M (11.5-yr).
  **ASC 842 is NOT immaterial in dollars ($22.3bn combined) but is immaterial in risk**:
  $2,434M of annual operating lease cost is 0.34% of revenue, against a business that owns
  most of its real estate.
- **Contingent-liability persistence [the brief's test]: does NOT fire.** The opioid accrual
  was taken in FY2023 and **fully extinguished by 2025-01-31**; the Spark Driver/FTC matter
  is accrued at $37M; nothing else carries a quantified accrual. The pattern of an accrual
  that never resolves is absent.

### Name the specific way THIS business dies **[E2-27, E3-24]** — modelled on exposure, not experience **[E4-40]**

**1. THE CAPEX TREADMILL — the [E2-27] mechanism, and the one that actually threatens the
holder.** Every large retailer is now building the same automated fulfilment capability
because every other one is. *"Viewed individually, each company's capital investment
decision appeared cost-effective and rational; viewed collectively, the decisions
neutralized each other."* Walmart, Amazon, Costco, Target and Kroger all spend to deliver
groceries in an hour; the customer captures the convenience; nobody captures a price.
- **Quantified from filed figures:** capex has already run $10.1bn → $26.6bn (FY2018 →
  FY2026), and the incremental return on the last $37.9bn of net new capital is **10.2%
  pre-tax**, against a ~22.3% return on the pre-existing tangible base. If capex holds at
  $26bn and D&A converges up to meet it — which it is doing, $10.7bn → $14.2bn in four
  years — **owner earnings converge on the capex-end construction of ~$11-13bn** and stay
  there, permanently, while revenue grows. That is the DG shape at 40x the size: growth
  without owner earnings.
- **Likelihood: [x] a real possibility.** It is not a forecast; **it is what the last four
  filed years already look like.** OE at the capex end is *lower* than it was in FY2017.
- *This is a valuation death, not a solvency death — which is exactly why it lands at Q5.*

**2. THE PHARMACY / REGULATORY BITE.** Already filed and quantified: "maximum fair price
regulation on certain prescription drugs, which went into effect in January 2026" cost
**125 bps of Walmart U.S. comp** in Q2 FY2027. Health-and-wellness has been a named comp
driver for four years. Plus the unresolved DOJ opioid trial (**November 2027**), ~230 live
MDL cases, and the *Florida Health Sciences* retrial (**2026-08-27**) — none accrued, none
estimable. **Quantified:** a second opioid-scale event at the FY2023 magnitude is $3.3bn,
or ~8 weeks of operating cash flow — absorbed without a financing event last time.
**Likelihood: [x] a real possibility** for the earnings drag; **a low-level possibility**
for anything solvency-relevant.

**3. THE MIX-SHIFT REVERSAL.** If advertising and membership growth decelerates while the
price investment continues, the FY2016-26 pattern (revenue ×1.48, margin ×0.84) resumes.
**Quantified:** a return to the FY2023 consolidated operating margin of 3.4% on FY2026
sales would put operating income at **$24.0bn instead of $29.8bn** — a 19% cut, and OE
toward the bottom of the band. **Likelihood: [x] a real possibility.**

**4. SOLVENCY.** Genuinely hard to name. It would take a multi-year collapse in U.S.
consumer staples demand plus a refusal of the commercial-paper market plus the loss of
supplier trade credit ($63bn of payables) simultaneously. **Likelihood: [ ] low-level —
and honestly, below that.** Walmart is among the most solvent large enterprises in the
world and this section is thin because the exposure is thin, not because it was skipped.

**[E4-51] — the bear case stated better than its holders would, and it is NOT the solvency
case: it is that Walmart is a magnificent business that has been converting an enormous
and rising capital budget into a slowly-growing profit stream for a decade, and is priced
as though the last three years were the trend and the previous seven were the aberration.**

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *Good, not great **[E4-20/E4-43]**; all three staying-power strengths pass, the third —
  the one that usually kills — with more room than any name yet run in this queue. The
  owner-earnings band is the widest yet built, but it reaches the same answer at both ends,
  so **[E4-25]**'s no-useful-conclusion escape does not apply and the file proceeds.*

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."*
- **Honest pre-tax expectancy at this price: ~5-6%** — a **1.82%** owner-earnings yield
  (judged) plus the growth the filed record actually supports (~3-4%/yr, evidenced below).
- To reach a 10% expectancy, owner earnings must compound at **+8.18%/yr in perpetuity**.
  On the most generous construction in the file (3-yr window, (c) = D&A, $22,080M) the
  yield is **2.60%** and the required perpetual growth is still **+7.40%**.
- **VERDICT AT THE FLOOR: BELOW IT. The name is NOT RANKED — it is quit on [E4-28],**
  *"whether short rates are 6 percent or whether short rates are 1 percent."*
  **The screen row is reproduced exactly:** at (c) ≈ D&A on the 5-year window the yield is
  **2.01%** and growth-to-floor is **7.99%** — the row's "yield ~2%, growth required ~8%",
  to the decimal, at the hand-read cover cap. **Spread verified.**

**One book. Owner earnings against the bond.** No DCF was run as a decision artifact
**[E3-34]**; what follows is a yield and a perpetuity conversion.

**1. THE YIELD**

| construction | owner earnings $M | **yield** | sovereign |
|---|---|---|---|
| 5-yr window, (c) = total capex (conservative) | 10,911 | **1.28%** | 5.24% |
| **JUDGED, (c) = $17,000M** | **15,500** | **1.82%** | **5.24%** |
| 3-yr window, (c) = D&A (generous) | 22,080 | **2.60%** | 5.24% |
| **the best single year ever filed** — FY2026 at the D&A end | 23,759 | **2.80%** | 5.24% |

**Every construction pays less than half the 30-year Treasury.** The best year in the
eleven-year record, valued on the most generous maintenance-capex assumption the framework
permits, yields **2.80% against 5.24%** — short by 2.44 points.

**2. WHAT THE PRICE ALREADY ASSUMES**
- Growth needed to justify the quote **against the bare bond: +3.42%/yr in perpetuity.**
  To clear the **[E4-28]** floor: **+8.18%/yr in perpetuity.**
- **What the business has actually done, every filed series, FY2016→FY2026:**

| series | CAGR |
|---|---|
| Total revenues ($482.1bn → $713.2bn) | **+4.0%** |
| **Consolidated operating income ($24,105M → $29,825M)** | **+2.2%** |
| Net income attributable to Walmart ($14,694M → $21,893M) | +4.1% |
| Diluted EPS ($1.523 split-adj → $2.73) | +6.0% *(buyback-assisted)* |
| Walmart U.S. segment operating income ($19,087M → $25,158M) | +2.8% |
| **Owner earnings, D&A end** (FY2017 $20,997M → FY2026 $23,759M, 9 yr) | **+1.4%** |
| **Owner earnings, capex end** (FY2017 $20,458M → FY2026 $11,320M, 9 yr) | **NEGATIVE** |

  **The required rate exceeds every filed series except EPS — and the EPS series is
  flattered by repurchases made at 1.7-2.6x our value estimate, which is value destruction
  presented as growth.** The one series the framework treats as *the* number grew at
  **+1.4%/yr** on the generous construction and **shrank** on the conservative one.

- **[E4-35] burden of proof, discharged against the name:** clearing the floor needs
  **+8.18%/yr forever** from a business whose operating income compounded at **+2.2%/yr**
  for a decade. The corpus's base rate — fewer than 10 of the 200 most profitable companies
  reach 15% EPS growth over twenty years — bites here: this asks for a permanent
  **tripling** of Walmart's own decade-long operating-income growth rate.
- **[E2-63]/[E4-44] — WHICH LEVER IS SPENT (the CTAS decomposition, and the answer to the
  brief's live question).** The decade decomposes as **revenue ×1.479 × operating margin
  ×0.84 = operating income ×1.237**:
  - **The volume lever is intact but slow.** ~+4%/yr is the honest run rate and is what was
    delivered. Bounded by U.S. population, food inflation and share gains.
  - **The price lever is deliberately refused** — it *is* the strategy (*"managing prices
    aligned to our competitive historic price gaps"*), and Q2 found no near-monopoly
    evidence licensing the [E3-33]/[E5-28] untapped-pricing class.
  - **The margin lever — the entire bull case — has been running BACKWARDS for a decade.**
    Consolidated 5.0% → 4.2%; Walmart U.S. 7.4% (FY2015) → 5.2%. For the floor to clear,
    the mix shift must not merely continue but **reverse an eleven-year trend and then
    compound on top of it.**
  - **THE CEILING, NAMED [E2-63] — and this is the arithmetic that settles the brief's
    prior even if the mix-shift thesis is entirely right.** Grant the full bull case:
    advertising ($6.4bn, +46%) and membership carry consolidated operating margin from 4.2%
    all the way back to FY2015's 5.6% over ten years. That is a **×1.33 one-time
    re-rating** — worth about **+2.9%/yr for ten years and exactly zero thereafter** — on
    top of ~4% volume growth. Total ≈ **7%/yr for a decade, ~4%/yr after.**
    **It does not reach 8.18% and it is not a perpetuity, which is what the floor
    requires.** The margin lever is arithmetically bounded by the margin itself, exactly as
    it was at CTAS; here it is bounded harder, because it must first climb back to where it
    started. **[E4-44]:** *"the value of an asset ... cannot over the long term grow faster
    than its earnings do."*

**3. WHAT YOU ARE PAID**
- **1.82% against a 5.24% sovereign = MINUS 3.42 points** (judged). On the most generous
  construction, **minus 2.64 points.** **There is no construction in this file in which
  Walmart pays a positive spread over the bond.**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used **5.24%** — **the bare rate, no per-name premium added.** Walmart is among
  the most certain businesses in this queue and that certainty is **not** rewarded with a
  lower rate; per [E3-42] doing so would be "mathematical gibberish."
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — zero-growth, capitalized at the sovereign:
- **conservative ~$26/share** ($10,911M ÷ 5.24% ÷ 7.934bn shares) · **judged ~$37/share** ·
  **optimistic ~$53/share** · *most generous construction that exists in the filed record
  (best year ever, D&A end): ~$57/share*
- **current price $107.14** — **2.0x to 4.1x the entire zero-growth band; 2.9x judged.**
- At the **[E4-28]** floor rate of 10% the band is **~$14 to ~$28/share, judged ~$20.**

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].** *(Corrected 2026-09-03, found by the
HHH run — this block still carried v4.0's "THERE IS NO HURDLE" heading, the SEVENTH
surviving home of the rule the framework rewrote on 2026-08-28. The floor section above at
[E4-28] already governs; this block is the ranking that applies only to what clears it.)*
- **Floor verdict first: honest pre-tax expectancy ~5-6% vs ~10% [E4-28] — BELOW.
  Quit on, and the ranking lines are therefore NOT filled in.**
- points over sovereign, this name: **−3.42** (judged) — recorded for the register only.
- against the rest of the opportunity set: **not ranked.** A name below the floor does not
  enter the ranking, whatever the alternatives look like.
- *Take the best available, or nothing.*

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] **Normal method [E4-11]**
- [x] **Screamer test [E4-01]** — does the price already clear the **conservative** case?
      **OUTCOME THREE: the price is ABOVE THE WHOLE RANGE** — above the conservative case
      ($26), above the judged ($37), above the optimistic ($53), and above the single most
      generous construction that exists in the filed record ($57). **The answer is no.**
      It does not *"scream at you"* **[E3-25]**; it is the opposite of a scream.
- **Windage count: ONE.** Conservatism is applied at exactly one place — the (c) judgment,
  set at $17,000M, nearer the capex end than the D&A end, on the incremental-return
  arithmetic in Q4. **The sovereign carries no per-name premium, no growth haircut is
  stacked on top, and no second margin is subtracted at the end** (Bar 2 forbids it)
  **[E4-11, E4-48]**. *And it did not matter: the verdict is identical at the D&A end,
  where no conservatism is applied at all.*

- **VERDICT: [ ] IN  [ ] UNRESEARCHED  [ ] UNKNOWABLE ·
  [x] BELOW THE [E4-28] FLOOR — QUIT ON, NOT RANKED · ranking position: none**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

*Q6 is written for the re-look, not for an entry: the file failed at Q5 on price. These
are the pre-committed markers under **[E1-02]**, "yardsticks prior to the act."*

**Pre-committed before entry [E1-02]:**
- **Thesis-confirming metric:** consolidated operating margin rising toward 5.0%+ **on
  GAAP**, with Walmart U.S. segment margin above 5.5%, while capex falls below 3.0% of net
  sales. That combination — margin up *and* capital intensity down — is the only pattern
  that turns the decade's arithmetic around, and neither half alone is sufficient.
- **Thesis-breaking metrics and their thresholds:**
  1. **Walmart U.S. transactions negative in two consecutive quarters** (excluding a
     pandemic-class distortion). The 21-quarter positive streak is the moat's live
     evidence; its loss is the [E3-30] moat downgrade.
  2. **Capex above $28bn with owner earnings at the capex end still below $13bn** — i.e.
     the treadmill confirmed rather than ending.
  3. **The [E2-49] withdrawal test: the quarterly transactions/ticket split disappearing
     from the earnings release**, or the advertising growth-rate disclosure being dropped.
     Yardsticks are discarded when they stop reading favourably.
  4. GAAP operating income growing slower than net sales for a **third** consecutive year.
- **Next catalyst dates:** Q3 FY2027 earnings release (~November 2026); *Florida Health
  Sciences* opioid **retrial commencing 2026-08-27**; Asda equal-value phase-three hearing
  **2026-11-23**; **McMillon retirement 2027-01-31** (Furner succeeds); FY2027 10-K
  (~March 2027); **DOJ opioid trial November 2027**.

**The sell rule [E2-28]** — two triggers, three hold conditions:
- SELL if the market judges it more valuable than the facts indicate — **this trigger is
  already satisfied at $107.14 against a $26-53 zero-growth band.** No position is held, so
  it operates as a do-not-buy rather than a sell.
- SELL if funds are needed for something more undervalued or better understood — n/a.
- HOLD while: return on equity capital satisfactory **(YES — ROE 23.0%, ten-year mean
  17.2%)** · management competent and honest **(YES — Q3 IN, no disqualifier found, two
  live flags)** · market does not overvalue **(FAILS)**. **Two of three hold conditions
  pass; the third is why there is nothing to hold.**
- *Price appreciation and holding period are explicitly rejected as reasons to sell.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** Monitoring
question — aberrational cycle or permanent slippage? **The eleven-year margin decline is
the item to watch, and I judge it NOT yet a moat downgrade**: the position (traffic, share,
units) is intact and improving, while the *economics* of holding that position have got
worse. That is a business paying more to stay where it is — the [E2-27] mechanism — and it
becomes a moat downgrade only if the transactions series turns negative while capex stays
high. Beliefs change gradually **[E4-17]**; this one is not yet formed.

**Do not trim winners [E5-14].** **Position size — ZERO.** The name failed the floor; there
is nothing to size. *Recorded for completeness: had it cleared, the live
**capital-allocation flag** (buybacks at 1.7-2.6x our value, with $25.1bn of authorization
remaining) would bind position size **downward** per [E4-13].*

- **VERDICT: [x] IN (as a monitoring file — pre-committed markers set)  [ ] OUT
  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**PRE-COMMITTED RE-LOOK:** **~$37/share judged zero-growth at a 5.24% sovereign,
recomputed at the rate of the day.** The floor clears at roughly **$20/share** on the
judged construction, or ~$28 on the generous one — i.e. Walmart would have to fall about
**65-74%** before it is a candidate on today's owner earnings. It is far likelier to become
a candidate by *earnings rising* than by price falling that far: **at $107.14 the floor
needs owner earnings of ~$85bn**, against $15.5bn judged today. **Re-open on the
thesis-confirming metric above (GAAP margin up AND capex intensity down), not on price
alone.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN · Q2 IN · Q3 IN · Q4 IN ·
      Q5 BELOW FLOOR · Q6 markers set.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q2's moat
      class is NARROW and *decided*, not PROVISIONAL — the row's unavailable peers (Aldi,
      Lidl, Publix, H-E-B) are named as private/non-filing with the limit stated, and the
      class does not rest on them.
- [x] No UNRESEARCHED or UNKNOWABLE verdicts were returned; nothing to work-order.
- [x] Step 0: filing read with accession number (FY2026 10-K, acc 0000104169-26-000055);
      **figure cross-checked** — OCF $41,565M, MD&A FCF table vs the filed cash-flow
      statement, identical; capex $26,642M identical both places.
- [x] Owner earnings on multi-year means (3-yr, 5-yr, 10-yr, plus leave-two-out on two
      windows); windows stated; **capex band disclosed as a judgment** with (c) = $17,000M
      labelled a guess per [E2-23].
- [x] Competitor row filled — 6 peers on identical formulas, filing-sourced.
- [x] Sovereign for the earnings currency (USD), **from the issuing authority** (US
      Treasury daily par yield curve), dated 2026-09-04, struck fresh.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (Bar 2, screamer test, outcome three); **windage count stated: ONE.**
- [x] Prices dated; **aggregator used for the live quote only and flagged** (Yahoo,
      2026-09-04 close $107.14).
- [x] Run committed to git after every question under the write-early protocol.

### DEFECTS CONFESSED (some are always there)
1. **[E3-48] guidance-vs-outturn sweep is INCOMPLETE.** The projections flag fired; I set
   FY2027 guidance against FY2026's GAAP outturn but did not sweep the full multi-year
   record of guidance against results. Open item.
2. **Brief defect corrected in-run:** the brief's [E4-55] framing assumed the
   transactions/ticket series either existed or did not. Both were wrong — it is filed
   **quarterly for 42 consecutive quarters** and refused **annually**. My own first pass
   recorded it as a flat absence; the ER sweep corrected it. The absence claim as finally
   worded is scoped to 10-K/10-Q vintages, which is what the sweep actually covered.
3. **Brief defect:** "[E2-44] Walmart held traffic POSITIVE through the price wave" is
   right for FY2022-26 but the brief did not know about the **five consecutive negative
   transaction quarters** in FY2021-Q1 FY2022 (trough −14.2%). Corrected in Q2.
4. **Brief defect:** the prior expected "the strongest Q2 IN of the entire queue — possibly
   IN WIDE." It came back **IN NARROW**, and the reason is the eleven-year segment margin
   decline plus Amazon's 6.9% North America margin — both filed, neither in the brief.
5. **Segment-vintage discrepancy carried unreconciled:** Walmart U.S. FY2017 operating
   income is **$17,745M** in the FY2017 Ex-13 and **$17,012M** in the FY2019 10-K. Both
   shown as filed; the reallocation is not explained in either document.
6. **Q4 FY2019 comp restatement (4.2% → 4.1%) has no footnote found.** Recorded,
   unreconciled.
7. **Software capex is unresolvable from the filing.** There is no capitalized-software
   disclosure in the FY2026 10-K (sweep: "capitalized software", "internal-use",
   "internally developed", "software development", "cloud computing", "hosting
   arrangement" — zero hits) and no software category in the P&E table. Where it sits
   inside "Payments for property and equipment" is **not disclosed**. The HAS defect (a
   missing capex line) does **not** bite — there is one capex caption — but the composition
   is opaque.
8. **SBC for FY2016-FY2021 comes from footnote totals across vintages**, with a scope
   wording drift at the FY2018 seam (no measured discontinuity: FY2018 = $626M in both).
9. **International is judged, not modelled.** Walmart International (18% of sales, OI
   *down* in FY2026) was handled through segment totals and the PhonePe charge; no
   country-level work was done, and **[E3-66]**'s jurisdiction question (where shareholders
   stand in the queue) was not run for Flipkart/PhonePe/Walmex minorities.
10. **The (c) = $17,000M judgment is the softest number in the file** and it is labelled a
    guess. It was tested for verdict-sensitivity across the whole band and did not change
    the answer, which is the only reason it is safe to carry.
11. **The dividend-streak claim was not run to ground below FY2013** — the filed DPS series
    verifies 14 consecutive annual increases; the "50+ years" claim is rung 3, non-filed.

## REGISTER
- Verdict: [ ] IN [x] **the business gates all returned IN; the FILE FAILS AT Q5 ON PRICE,
  below the [E4-28] floor** [ ] OUT [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** *Walmart is the best business this queue has run — a genuine [E2-58]
  wide-and-sustainable cost advantage, proven by the fact that Amazon spent two decades and
  $13.7bn on Whole Foods attacking it and moved its Physical stores line from $17.2bn to
  $22.6bn — and it is priced at 2.9x a zero-growth value, needing +8.18%/yr forever from a
  business whose operating income has compounded at +2.2%/yr for a decade.*
- **Not UNRESEARCHED and not UNKNOWABLE:** the evidence is in, the verdict is about price,
  and the file re-opens on the pre-committed markers at Q6.
