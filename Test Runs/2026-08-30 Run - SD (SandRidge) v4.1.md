# Company Run — SandRidge Energy, Inc. (NYSE: SD) — 2026-08-30
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this file
and that document disagree, the document governs. Q3 annex:
`Framework/v4/THE MANAGER STANDARD - Q3.md`. Evidence pack:
`Test Runs/_research 2026-08-26/SD evidence pack - reserves, NOL, dividends, asset basis.md`.
Competitor row: `Test Runs/_research 2026-08-26/SD competitor row (MNR-GPOR-CRK-CNX).md`.

**Position context: NONE HELD. Fresh entry run.** Surfaced by the operator's sourcing sweep
(cap ~$515M; sweep "statute yield" 11.8%).

**BIAS DECLARED, operator rule 9.** ~$2,750 of capital waits for a dividend payer that
compounds. SandRidge pays a dividend and the screen says 11.8%. Both facts push the analyst
one way, and the corpus names the antidote: *"I'm not entitled to have an opinion unless I
can state the arguments against my position better than the people who are in opposition"*
**[E4-51]**, and hunt disconfirming evidence hardest for the favourite hypothesis
**[E4-26]**. Two specific disciplines are pre-registered here before any arithmetic:
1. **The 11.8% is treated as guilty until proved.** It will be located in a named window and
   tested against [E4-41]'s normalization before it is allowed to mean anything.
2. **The dividend is decomposed before it is admired.** The WEYS precedent governs: a special
   is not a compounder. The regular and the special legs are separated from the filer's own
   table, not reconstructed.
**A "no" is a fully successful run [E5-13].**

**Method flags, declared up front (operator tasking):**
1. **Q2 tests the price-taker question against the subject's own sensitivity disclosure.**
   Format precedent: `2026-08-30 Run - ASIX (AdvanSix) v4.1.md`, itself following
   `2026-08-28 Run - MITSY (Mitsui) v4.1.md` — Q2 OUT on the filer's own words, entry closed
   at any price.
2. **Q4's (c) meets the [E5-20] exception head-on.** For an E&P, spending D&A does **not**
   hold unit volume: reserves deplete and must be **replaced**. This is [E4-04]'s excluded
   class by name — *"the moat whose basis must be periodically replaced … depleting assets"* —
   the Rhodes Ridge logic. The reserve-replacement arithmetic is stated from the filed reserve
   tables, and the D&A end of the band is refused, not merely discounted.
3. **The asset basis is worked beside the owner-earnings convention** — net cash + PV-10 +
   NOL shield against the cap — because for a depleting asset the liquidation read is a real
   second book, and because the NOL contains a double-count trap that must be shown.
4. **Q6 is completed regardless of the stopping point; alert thresholds are LISTED ONLY** —
   no alerts file edited, no shared file edited.

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- **USD 30-year: 5.19% · observation date 2026-08-27 · FRED DGS30**, fetched direct from
  `fredgraph.csv?id=DGS30` on 2026-08-31 (Treasury constant maturity, issuing-authority
  series; the 1–2 day publication lag is standing and immaterial). Local copy
  `DGS30_2026-08-31_SD.csv`.
- FX: none. Quote currency = earnings currency = USD. Sales are 100% US (Mid-Continent —
  Oklahoma, Kansas, Texas).
- **Price: $13.96, NYSE close 2026-08-28** (Yahoo chart API — aggregator, live quote only,
  flagged). 52-week range $11.10–$18.45.
- **Market cap: 37,075,296 shares × $13.96 = $517.6M.** Share count is the **filed** count
  from the Q2 2026 10-Q cover page ("as of the close of business on July 30, 2026"), and it
  agrees with the balance-sheet line (37,075 thousand issued and outstanding at 2026-06-30).
  **The operator sweep's ~$515M is verified**; the small difference is the quote date.
- Dividend at the quote: **regular $0.13/qtr → $0.52/yr → 3.7%.** Decomposed at Q3 below.

**The filing was read — not tagged data [E3-27, E4-14]:**
1. **FY2025 Form 10-K** (year ended 2025-12-31), filed **2026-03-05, accession
   0001628280-26-015318** — [x] MD&A [x] cash-flow statement incl. detail lines [x] footnotes
   (Note 11 commitments and legal; **Note 12 income taxes / NOLs**; Note 13 equity and
   dividends; Note 20 supplemental oil-and-gas — capitalized costs, costs incurred, reserve
   rollforward, standardized measure); [x] Item 1 reserve and PV-10 tables; [x] Item 1A risk
   factors; [x] Item 5 dividends and repurchases; [x] Item 7A market risk.
2. **Q2 2026 Form 10-Q** (period 2026-06-30), filed **2026-08-06, accession
   0001628280-26-054413** — statements, dividend table, liquidity, subsequent events, the
   pending acquisition, the Tax Benefits Preservation Plan amendment.
3. **8-K + Ex-99.1, Q2 2026 results**, filed **2026-08-05, accession 0001628280-26-053557** —
   the **filed dividend decomposition table** and the non-GAAP presentation.
4. **DEF 14A**, filed **2026-04-27, accession 0001140361-26-017133** — board, management,
   compensation metrics, beneficial ownership.
- **Figure cross-checked against the filed statement (operator protocol 4):** the FY2025
  Consolidated Statements of Cash Flows reads, on "Net cash provided by operating activities",
  **100,140 · 73,933 · 115,578** ($ thousands, FY2025 · FY2024 · FY2023). SEC XBRL
  `companyfacts` carries the identical three values. **Ties — the prior session's
  $100.1M / $73.9M / $115.6M is re-verified from the filed statement.** Second check:
  Q2 2026 net income $26,693K ÷ 36,906K basic weighted shares = $0.72 = the filed basic EPS.
  Ties.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language:** SandRidge owns working
  interests in 1,446 gross producing wells (825 net) across 491,197 gross developed acres in
  the Mid-Continent. It pulls a mixed stream out of the ground — in FY2025, 6.768 million
  barrels of oil equivalent, of which **50% natural gas, 32% NGL, 18% oil by volume** — and
  sells all of it at whatever the market pays that month, less transportation and quality
  differentials. In FY2025 it received **$23.10 per Boe** and spent **$6.89 per Boe** on
  production costs, leaving about $16 per barrel of field margin. Off that comes $13.2M of
  corporate overhead and the cost of drilling new wells. It pays **no cash income tax at all**
  because $1.6bn of net operating losses survive from the predecessor company's 2016
  bankruptcy. What is left, it either banks, buys more wells with, or hands back.
  FY2025: revenue $156.4M, net income $70.2M, operating cash flow $100.1M, capex $58.6M,
  cash at year end $112.3M, **no debt at all**.
  The barrel in the tank is worth what the world says. That is the whole model.
- **The scarce input this business controls: none.** The input is undrilled Cherokee-play
  acreage, and its own risk factor says who controls it: competitors *"may be able to pay more
  for productive oil and natural gas properties and exploratory prospects or identify,
  evaluate, bid for and purchase a greater number of properties and prospects than our
  financial or human resources permit."* It buys the input in an open auction against
  better-capitalised bidders. What it *does* have is an unusual liability structure — zero
  debt and a $1.6bn tax shield — but a balance sheet is not a scarce input; it is a starting
  position, and Q3/Q5 handle it.
- **Will the fundamentals look broadly the same in ten years?** The *mechanism* — yes,
  identically: pull hydrocarbons, sell at the posted price, spend to replace them. The
  *asset* — no, and this is the whole run. The reserve base is 10.2 years of production at the
  current rate (8.9 on proved developed). Ten years from now, absent replacement, there is
  nothing. That is not a forecast; it is the definition of the asset. The company's own filed
  reserve series makes the point: proved reserves went **177.6 MMBoe (2017) → 69.1 MMBoe
  (2025)**, down 61% from the post-emergence peak, while it produced 6–20 MMBoe a year through.
- **VERDICT: [x] IN.** The economics are legible in one paragraph and stable in *character*.
  Whether legible is franchise is Q2's question, and whether a ten-year-life asset can be
  "understood" as a going concern is Q4's.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** — energy, elementally.
- Not price-regulated **[x]** — the filing: *"The price of oil, natural gas and NGLs is not
  currently regulated and are made at market prices."* Criterion 3 passes on the identical
  sentence that destroys criterion 2.
- **No close substitute [ ] — FAILS, and it fails on the subject's own filed disclosure.**
  The MITSY/ASIX precedent applies. The filer's words:
  - **Item 7A, first line:** *"**Our most significant market risk relates to the prices we
    receive** for our oil, natural gas and NGLs."*
  - **Item 1A:** *"These factors and the volatility of the energy markets, which we expect
    will continue, make it **extremely difficult to predict future oil, natural gas and NGL
    price movements with any certainty**"* — attached to a twenty-item list (world politics,
    global inventories, weather, alternative fuels, pipeline capacity, the dollar) of which
    SandRidge influences **none**.
  - **MD&A:** *"Our cash flows from operations are **substantially dependent on current and
    future prices for oil, natural gas and NGL**, which historically have been, and may
    continue to be, volatile."*
  - And the quantified volatility, from the same filing: over 2021–2025 NYMEX Henry Hub spot
    ranged **$1.26 to $24.77 per Mcf** and WTI **$47.47 to $123.64 per Bbl**.
  A thousand cubic feet of Anadarko Basin gas is the same molecule as anyone else's. **Price
  taker on every product line, by its own disclosure, at every price.**

**Must the moat be continuously rebuilt? [E4-04] — this is the decisive test and it is not
close.** The corpus scopes [E4-04] precisely: what "enduring" excludes is *"the moat whose
basis must be **periodically replaced** — rapid-change industries, **depleting assets**."* The
test given is: *"does a lapse in spending destroy the structure, or merely narrow it — and
does the spending defend the same advantage, or **buy its replacement**?"* Coca-Cola's
advertising defends the same trademark; **Mitsui's Rhodes Ridge buys a replacement deposit.**

SandRidge is Rhodes Ridge with nothing else attached. Every barrel sold is permanently gone.
The filed arithmetic (evidence pack §3.3), from the 10-K's own rollforward and costs-incurred
tables, FY2023–25:

| | 3-year FY2023–25 | FY2025 alone |
|---|---|---|
| Production | 18.976 MMBoe | 6.768 MMBoe |
| Extensions and discoveries (organic) | 8.510 MMBoe | 7.298 MMBoe |
| **Organic reserve replacement** | **45%** | **108%** |
| Purchases of reserves in place | 19.393 MMBoe ($149.4M) | 1.677 MMBoe ($8.5M) |
| Total costs incurred | **$267.6M** | $77.5M |
| **Organic finding & development cost** | **$13.89/Boe** | $9.45/Boe |
| Blended all-in finding & acquisition cost | **$9.59/Boe** | — |
| Costs incurred ÷ production | $14.10/Boe | $11.45/Boe |
| Book depletion charged | — | **$5.38/Boe** |

**Over three years, drilling replaced 45% of what was produced and the rest was bought.**
$267.6M of costs incurred — 92% of the $289.7M of operating cash flow generated in the same
window — left total proved reserves at 69.1 MMBoe against 74.3 MMBoe three years earlier.

**The counter-evidence, stated as its best advocate would state it [E4-51], because it is
real:** **FY2025 alone replaced 108% organically**, at $9.45/Boe, and SandRidge carries a
proved-undeveloped book (8.8 MMBoe) for the first time since 2022 — it had **zero** PUDs at
both YE2022 and YE2023. FY2024's 0% organic replacement is explained by the filing itself:
no operated wells were drilled that year. The three-year 45% therefore averages one real
development year against two years of deliberate inactivity, and the honest reading is that
**the one-rig Cherokee program does work when it is running.** *(The [E4-25] discipline
requires both windows be shown rather than the worse one chosen.)*
**And the honest deduction from that counter-evidence:** $43.7M of FY2025's $69.0M of drilling
spend went to converting 4.7 MMBoe of existing PUDs into PDPs — moving reserves between
categories, not adding them — so the $9.45/Boe understates the true cost of standing still.
The cleanest single measure is total costs incurred per barrel produced: **$11.45/Boe in
FY2025, $14.10/Boe over three years, against $5.38/Boe of depletion charged.**
*(Further honest caveat: the YE2022 reserve base was struck at 2022's high SEC gas price, so
part of the three-year fall is price revision — the revisions line alone is −14.0 MMBoe over
the window. The physical point stands on the ten-year series in Q1 regardless.)*

**A lapse in spending does not narrow this structure; it ends it.** Stop the rig and the
proved developed base runs out in 8.9 years. That is the excluded class, stated by the corpus
and demonstrated by the filing.

**The commodity doctrine [E2-58], applied.** *"Persistent over-capacity without administered
prices (or costs) equals poor profitability"*, with long-term profitability set by *"the ratio
of supply-tight to supply-ample years"*. For US natural gas the filed reading of that ratio is
in SandRidge's own realised prices: **$1.71 (2023) → $1.10 (2024) → $2.10/Mcf (2025) → $1.36
in 2Q26** — four consecutive years in which the company's realised gas price sat at or below
$2.10 while the SEC index sat at $2.13–$3.39. Gas is 50% of volume and produced 14% of 2Q26
revenue. The supply-ample state is not a forecast here; it is the filed four-year record.
**The one exception [E2-58] is *"a cost advantage that is both wide and sustainable … By
definition such exceptions are few."*** SandRidge's FY2025 production cost of **$5.35/Boe
excluding taxes** is genuinely low. But the exception's own test is earning well *through* the
glut, and the honest owner-earnings arithmetic at Q4 says this cost position delivers
**0%–5.7%** on the current price in the normal state. Survival-grade, not franchise-grade —
and the low cost is a **property of the rock**, not of the company: the same acreage in
anyone else's hands produces at the same lifting cost.

**The second step [E3-62].** The Cherokee program's returns are asserted ("high-return, growth
projects") and never separated into what stays home and what flows to the buyer. In a
commodity with a posted price, the answer is structural: **all of an operating-cost saving
accrues to the producer, and none of a price improvement does, because there is no price to
improve.** That is why the cost advantage cannot become a franchise — there is no pricing
surface for it to act on.

**[E2-59] regime check.** No administered price, no cartel, no tariff floor, no rate base.
Nothing regulates the sales price up. The only regime item in the file runs the *other* way:
the **Tax Benefits Preservation Plan**, a 4.9% poison pill that protects a *tax attribute*, not
a margin.

**Untapped pricing power [E3-33] / [E5-28]: none available, structurally.** A price taker
cannot raise prices, and no near-monopoly claim is possible for a 19.7 MBoe/d producer in a
US market producing ~100 Bcf/d of gas.
**The inverse metric [E4-37]** — *"the agony they go through in determining whether a price
increase can be sustained"* — cannot even be run. There is no price decision to agonise over.
That is the sharpest possible reading of the negative.

**Two-characteristic test [E2-44]:** (1) raise prices with demand flat and capacity slack —
**no**; (2) grow dollar volume with only minor additional capital — **no**: the company's own
2026 budget is **$76–97M against a $517.6M market cap** and $42.9M of D&A. **0 of 2.**

**The attacker's test [E2-45]:** an attacker with ample capital does not need to attack. It
simply outbids SandRidge at the next acreage sale — which the company's own competition risk
factor concedes is exactly what happens.

**Dominance class [E2-53]:** unavailable. 19.7 MBoe/d does not make a marketplace.
**[E4-36] — which of the four causes of extreme success?** The FY2021–22 record (ROE 62.5%,
66.1%) is **wave-riding [E3-51]**: a post-COVID, post-invasion energy price wave. *"When a
surfer gets up and catches the wave … he can go a long, long time. But if he gets off the
wave, he becomes mired in shallows."* The FY2023–25 record — ROE 12.7%, 13.6%, 14.5% on a book
value shrunk by $947.1M of cumulative post-emergence ceiling impairments — is the shallows,
and even those returns are flattered by the impaired denominator ([E2-47]'s carve-out).

**Direction [E4-32]:** proved reserves 177.6 → 69.1 MMBoe over eight years; organic
replacement 45%; the profit engine (gas) realising $1.36/Mcf in the latest filed quarter.
The moat is not widening, because there is no moat to widen.

**THE COMPETITOR ROW [E3-28]** — same metric (ROE = net income ÷ average stockholders'
equity), same window (FY2021–25), filing- and XBRL-sourced. Full table with accession numbers
in `SD competitor row (MNR-GPOR-CRK-CNX).md`.

| Company | FY21 | FY22 | FY23 | FY24 | FY25 | 5-yr avg |
|---|---|---|---|---|---|---|
| **SandRidge (SD)** | **62.5** | **66.1** | **12.7** | **13.6** | **14.5** | **33.9** |
| Mach Natural Resources (MNR) — Anadarko Basin, the closest structural peer | 66.2 | 118.6 | 7.7 | 15.5 | 9.0 | *not comparable — LP* |
| Gulfport Energy (GPOR) — Anadarko SCOOP / Utica gas | n/c | 71.8 | 98.4 | (13.5) | 24.1 | 45.2 (4 yrs) |
| Comstock Resources (CRK) — Haynesville pure gas | (22.7) | 68.4 | 9.1 | (10.0) | 16.2 | 12.2 |
| CNX Resources (CNX) — Appalachian gas | (12.3) | (4.3) | 47.1 | (2.1) | 15.0 | 8.7 |

**Peers named: 4 of the peer set attempted; 4 obtained in full.** Amplify (AMPY) was obtained
and **disqualified as a comparable** — it divested its entire gas book in 2025 (gas reserves
literally zero at YE2025) and is now 93% oil. PHX Minerals could not be obtained and is a work
order. Non-comparability is recorded, not smoothed: **MNR is an LP** (no entity-level federal
tax, so a pre-tax numerator; a denominator starved by full variable distributions; FY21–22 are
predecessor private-LLC members' equity) — **do not rank it against SD on this line**.
**GPOR FY2021 is uncomputable** (fresh-start 2021-05-17; equity reset from −$300.5M to
$639.7M mid-year). **CNX's net income is dominated by hedge mark-to-market** — a $721M swing in
2025 alone — so its ROE line measures its derivative book, not its wells. And three high years
in the table carry large deferred-tax valuation-allowance releases: SD FY2022 **$64.5M of
$242.2M**; GPOR FY2023 $525.2M of $1,470.9M.

**The physical row — the one that decides anything here.** Same metric, same date, all from
FY2025 10-Ks:

| | **SD** | MNR | GPOR | CRK | CNX |
|---|---|---|---|---|---|
| Proved reserves, Bcfe | **415** | 4,228 | 4,253 | 7,005 | 9,662 |
| **Reserve life (R/P), years** | **10.2** | 18.7 | 11.2 | 15.6 | 15.4 |
| PV-10 per Mcfe | **$1.06** | $0.73 | $0.85 | not disclosed | $0.71 |
| Organic replacement, FY2025 | 108% | **0%** | 185% | 830%\* | 138% |
| Development capex per Boe produced, FY2025 | **$8.74** | $7.17 | $8.35 | $17.97 | **$4.72** |
| FY2025 FCF before acquisitions, $M | +41 | +236 | +276 | (450) | +534 |
| **Net debt ÷ FY2025 OCF (at 2026-06-30)** | **(1.1×) net cash** | 2.23× | 1.15× | 3.39× | 2.16× |
| Loss years in the window | **0 of 5** | 0 of 5 | 1 of 4 | 2 of 5 | 3 of 5 |

\* CRK's own text: a re-booking of PUDs price-excluded in 2023/24, not discovery.

- **What the row shows, and it is decisive in two directions at once.**
  **Against SD:** it has **no cost advantage** — development capex of $8.74/Boe produced sits
  *behind* CNX ($4.72), Mach ($7.17) and Gulfport ($8.35) — and it has **the shortest reserve
  life and the smallest reserve base in the set: 10.2 years and 415 Bcfe against 4,228–9,662
  Bcfe elsewhere.** The [E2-58] exception requires a cost advantage *"both wide and
  sustainable"*; the row says there is not even a narrow one. The depleting-asset problem
  [E4-04] identifies is **worse at SandRidge than at any comparable filer.**
  **For SD:** it is the only member of the set with **zero debt and net cash** while the others
  carry $0.9bn–$3.1bn of net debt; it is the only one with **no loss year in five**; and it
  carries the **highest PV-10 per Mcfe in the set ($1.06)** — though the row identifies the
  cause honestly as its 16% oil / 35% NGL product mix and its zero tax line, not operating
  skill. Against the nearest structural comparable, SandRidge drilled its 108% replacement
  while **Mach's own 10-K states it had "no extensions or discoveries in 2025"** and grew
  reserves almost entirely by purchase, adding $1.1bn of net debt to do it.
- **What the row cannot do [E3-61]:** *"In some businesses, the participants behave like a
  demented Kellogg. In other businesses, they don't … I think you'd have to know the people
  involved."* It shows position, never conduct.
- **And the moat class does not rest on the row** — the subject's own pricing disclosure and
  its own reserve rollforward decide it, exactly as at MITSY and ASIX. **The class is therefore
  NOT held PROVISIONAL and Q2 is not UNRESEARCHED.** The row is recorded because the framework
  requires it, because it disciplines the Q5 ranking, and because here it happens to
  corroborate the verdict from the outside.
- Note finally that SD's own five-year average is manufactured by two wave years and by an
  equity denominator written down by $947.1M of ceiling impairments; every gas-weighted peer's
  2021–22 is also a wave year. The comparison that would matter — normal-state returns on
  *unimpaired* capital — is not obtainable from any of these filers on a like basis, and that
  limitation is recorded rather than papered over.

- **Class: [x] NONE** · **Direction [E4-32]: negative** (reserve base down 61% from the 2017
  peak; organic replacement 45%; realised gas $1.36/Mcf in the latest filed quarter).
- **VERDICT: [x] OUT.** Two independent, filed grounds, either sufficient:
  1. **[E3-03] criterion 2 fails on the filer's own words.** Its most significant risk is *the
     prices it receives*; its cash flows are *substantially dependent* on those prices; it
     cannot predict them *with any certainty*. There is no product for which a customer
     believes there is no close substitute, because there is no product — there is a
     commodity with a screen price.
  2. **[E4-04]'s excluded class, by name.** The basis of any advantage here must be
     *periodically replaced*, and the filed replacement arithmetic shows the replacement is
     bought at $9.59–$13.89/Boe while depletion is charged at $5.38/Boe. This is the Rhodes
     Ridge case, and the corpus already decided it.
  **The MITSY/ASIX precedent applies: Q2 OUT on the subject's own disclosure — entry is
  closed at any price [E5-35]: *"You can turn any investment into a bad deal by paying too
  much. What you can't do is turn any investment into a good deal by paying little."* The
  entry run stops here. [E5-13]: most names should end here, and that is the system working.**

---
⛔ **Q3, Q4 and Q5 do not open for entry.** Q1 IN · Q2 OUT — the hard sequence closes the file
for any BUY decision. No position exists, so no [E2-28] hold read is required. Everything
below is **FOR THE RECORD** per operator tasking (Q6 regardless; both OE windows plus the
bottom boundary; the asset basis; the deaths quantified). **Everything below sits under
operator rule 3's header. Nothing below is entry language.**

---
## Q3 — FOR THE RECORD: ARE THEY HONEST, AND ARE THEY RATIONAL?
*Standard applied: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Q2 OUT stands regardless —
Q3 can stop a run, never start one.*

**STEP 1 — THE WEIGHT CASE.**
- [x] **Daily execution — HIGH.** Not because wells are hard to run, but because in a
  price-taker with a depleting base **the only two decisions that exist are where to drill and
  what to pay for acreage**, and both are made continuously. [E3-38]'s network-TV/retailer
  distinction lands on the retailer side: a shiftless nephew allocating $76–97M a year into
  Cherokee locations at $13.89/Boe would destroy the company inside one reserve life. There is
  no franchise underneath to absorb the error.
- [ ] Control — no (listed minority; exit exists at a screen price).
- [ ] **Leverage — NO, and this is the file's single strongest fact.** **Zero term or
  revolving debt** at 2026-06-30, filed in those words, against $114.7M of cash. [E3-29]'s
  magnification does not apply. [E4-16]'s *"whenever a bright person … goes broke … it's
  because of leverage"* has no purchase here.
- **One determinant high → for any entry, Q3 would be a BINARY GATE and no price would
  compensate [E3-29, E5-35].**

**Honesty — the binary [E5-16].** **No integrity disqualifier found in the documents read**
(worded per the absence-claim rule; this is the absence of found disqualifiers, never a
finding that the managers are honest [E5-17]). The conduct file is entirely predecessor-legacy:
the 2012 and 2015 securities actions were **discharged in the 2016 Chapter 11 plan**, and on
**2025-09-11** the Western District of Oklahoma granted summary judgment for the Trust and
dismissed all remaining claims against the Company with prejudice, the appeal right having
expired. One live matter: insurers who funded a **$17.0M** settlement for two individual
defendants seek indemnification; the Company refuses and is at the Fifth Circuit; **no
liability established, and the Company states it cannot determine the likelihood of an
outcome.** Per the TJX calibration, a pre-bankruptcy dispute between the successor entity and
D&O insurers is not financial dishonesty toward today's owners. **[E5-22] stands: penalty size
is not seriousness, in either direction.**

**STEP 2 — THE FLAGS [E4-22, E4-29, E5-15, E4-30, E2-52, E3-50, E2-57, E3-53].**
- [ ] **Weak accounting — not fired.** Full cost method, applied consistently and disclosed;
  97.9% of proved reserves prepared by **Cawley, Gillespie & Associates**, named, with the
  independence statement printed (*"do not own an interest in the Company or its properties
  and are not employed on a contingent basis"*); no unrecognized tax benefits in any of the
  three years; no pension. Note [E2-50]'s scope — *"where 'earnings' can be created by the
  stroke of a pen, the dishonest will gather"* — and an E&P is squarely in that class, because
  the depletion rate is a function of the reserve estimate. **The mitigant is filed and
  checkable: the reserve rollforward publishes revisions separately every year, including the
  ugly ones (−15.3 MMBoe in 2023), and the independent engineer's percentage is disclosed.**
- [ ] **Unintelligible footnotes — not fired.** Note 12 (income taxes) is the opposite: the
  NOL is broken into federal/state, expiring/non-expiring, with the §382 mechanics, the 2016
  ownership change, and the valuation allowance movement all quantified. Note 20 gives costs
  incurred, the reserve rollforward and the standardized-measure walk in full.
- [ ] **Trumpeted projections [E3-48, E5-30] — not fired.** No EPS or revenue guidance found
  in the documents read. The only forward number is the capital budget, stated as a range
  ($76–97M) with the conditions on it (*"we will adjust our program accordingly, to include
  curtailment of capital activity and wells, if needed"*). **The guidance ratchet has not
  started.**
- [ ] **Serial share issuance [E5-15] — not fired.** Shares 37,091K (2023) → 37,203K (2024) →
  36,825K (2025) → 37,075K (6/2026). Flat. *Watch item, not a flag:* the DRIP adopted
  2025-08-05 issues shares in lieu of cash dividends (92,733 in 2025; 143,343 in 2Q26), which
  is share issuance in the service of a dividend — the mechanical inverse of a buyback, and it
  makes "aggregate cash dividends paid" understate the declared distribution.
- [x] **EBITDA / adjusted promotion [E4-29] — FIRED, and read; the reading substantially
  mitigates it.** The **earnings release** (8-K Ex-99.1, 2026-08-05) leads its highlights with
  *"Adjusted net income … Adjusted EBITDA (1) of $34.0 million … Free cash flow"*. But:
  **the FY2025 10-K contains the string "Adjusted EBITDA" zero times, and "free cash flow"
  zero times. So does the Q2 2026 10-Q.** The only non-GAAP measure in the annual report is
  PV-10, labelled as one, with the standardized measure printed beside it and reconciled. And
  **no incentive-plan metric anywhere is EBITDA** (see Step 3). [E5-41]'s reverse-float warning
  is nonetheless recorded with force, because for an E&P depletion is the *most* real expense
  in the accounts and is in fact **understated** ($5.38/Boe charged against $9.59–13.89/Boe of
  replacement cost) — so an EBITDA presentation deletes an expense that is already too small.
  **Flag stands as fired at the release level; not fired at the filing level.**
- [ ] **Filed-figure tells [E4-30] — not fired.** Reported earnings are visibly, violently
  cyclical (net income $116.7M → $242.2M → $60.9M → $63.0M → $70.2M): the opposite of
  unnatural smoothness. Cash taxes as a share of pretax income are **zero throughout** — which
  would normally fire the second tell hard, and here does not, because the cause is named,
  quantified, audited and structural: $1.6bn of NOLs from the 2016 bankruptcy, with the full
  §382 history and the valuation-allowance arithmetic disclosed. **Verified, not assumed:**
  the tax-rate reconciliation shows the statutory 21% provision each year offset line-by-line
  by "changes in the valuation allowance."
- [ ] **Dividends funded by issuance [E2-52] — not fired.** No net issuance. **But its cousin
  is a live finding, recorded at [E2-60]: the dividends were funded by the balance sheet.**
  FY2024 paid $72.3M of dividends against $73.9M of operating cash flow **and** $26.4M of
  capex **and** $129.7M of acquisitions; cash fell $154.4M that year. That is not restricted
  earnings in the leverage sense (there was no borrowing) but it is a distribution of capital,
  and the filed decomposition below says so.
- [ ] **Stock-price targeting [E3-50] — not fired.** Nothing found.
- [ ] **Except-for [E2-57] / restructuring charges [E3-53] — not fired.** Restructuring
  expense is small ($1.06M in 2025, $0.47M in 2024), disclosed as *"fees and costs associated
  with our predecessor company's 2016 bankruptcy filing, the outsourcing of corporate
  functions and our exit from North Park Basin"* — it runs through the income statement every
  year and is not annualised away.
- [ ] **Metric-switching [E2-49] — not fired, and the opposite is worth recording.** The
  reserve, PV-10, production, price-per-Boe and cost-per-Boe series are presented on the same
  basis year after year, with the bad years printed at the same size as the good.

**THE DIVIDEND, DECOMPOSED [operator tasking; the WEYS precedent].** SandRidge publishes the
split itself, in the 8-K Ex-99.1 "Dividend Program" table. This is the filer's own arithmetic,
not a reconstruction:

| $ thousands | **Total since 2023** | 2Q26 | 1Q26 | FY2025 | FY2024 | FY2023 |
|---|---|---|---|---|---|---|
| **Special dividends** | **136,651** | 6,445 | — | **—** | 55,868 | 74,338 |
| **Quarterly dividends** | **47,786** | 4,190 | 3,868 | 15,862 | 16,426 | 7,440 |
| Total | 184,437 | 10,635 | 3,868 | 15,862 | 72,294 | 81,778 |
| **per share — special** | **$3.70** | $0.20 | — | — | $1.50 | $2.00 |
| **per share — quarterly** | **$1.35** | $0.13 | $0.12 | $0.46 | $0.44 | $0.20 |

**The finding, for the operator's dividend-compounder wish: 74% of every dollar SandRidge has
returned since 2023 was a special ($136.7M of $184.4M; $3.70 of $5.05 per share). The WEYS
precedent holds — specials are not compounding.** They were paid out of the cash pile, and the
pile they were paid from is visible in the filed series: cash including restricted went
$257.5M (2022) → $253.9M (2023) → **$99.5M (2024)** → $112.3M (2025) → $114.7M (6/2026).
The **regular** leg is $0.10 → $0.11 → $0.12 → $0.13 per quarter over three years — real,
growing at about a cent a quarter per year, and worth **3.7%** at $13.96. That is the number
an owner may plan on. The 11.8% screen yield and the $5.05 of headline dividends are not
that number.

**And the next distribution has already been claimed.** The **$65.0M** Cherokee acquisition
announced 2026-06-26 — *"expected to fund the acquisition with cash on hand"*, plus up to
$6.0M of WTI-linked earn-outs — takes 57% of the cash. This is the third conversion of the
balance sheet in four years: $129.7M into acquisitions (2024), $136.7M into specials
(2023–26), $65M into acquisitions now.

**STEP 3 — THE PRIMARY TEST [E2-01].** Balance sheet first, over the available post-emergence
window [E5-27]: equity $128.1M (2020) → $245.3M (2021) → $487.9M (2022) → $468.1M (2023) →
$460.5M (2024) → $510.9M (2025) → $542.7M (6/2026). **Total liabilities never exceeded
$133.2M and consist almost entirely of trade payables and asset retirement obligations —
there has been no debt at any year end in the series.**

Earnings rate on equity capital employed (net income ÷ average equity):

| FY | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| ROE as reported | 62.5% | 66.1% | 12.7% | 13.6% | 14.5% |
| ROE excluding the deferred-tax valuation-allowance swing | 62.5% | 48.5% | 15.7% | 8.8% | 13.3% |

**Two corrections the corpus requires before this series is read as managerial performance:**
1. **[E2-01]'s own parenthesis — "without … accounting gimmickry" — and [E2-47]'s carve-out
   for mis-stated asset values.** The equity denominator has been reduced by **$947.1M of
   cumulative full-cost ceiling impairments since emergence**. A business that has written off
   $947M shows a small denominator and therefore a high ratio. The reported 12.7–14.5% is not
   comparable to an unimpaired filer's 12.7–14.5%.
2. **The numerator carries no tax.** [E2-73]'s question — what return do the *operators* earn
   on the underlying assets — is answered in Note 20's own hypothetical: FY2025 oil-and-gas
   segment pretax income $73.3M less a hypothetical statutory tax of $17.8M = **$55.5M**. The
   NOL is a financing asset, not an operating achievement.
3. **[E3-59]'s two yardsticks.** *The hand they were dealt* is a legacy Mid-Continent position
   in the worst gas price environment in twenty years, and against that hand the operating
   record is competent: production costs cut from **$6.80/Boe (2023) to $5.35/Boe (2025)**,
   more than four and a half years without a recordable safety incident, LOE and adjusted-G&A
   both delivered **below** the incentive plan's target ranges. *How they treat their owners*
   is genuinely good on form — no debt, no dilution, real cash returned, buybacks at $10.75
   against a $13.96 quote — and the honest deduction is the shape of the returns (74% special,
   funded from the balance sheet) rather than any misconduct.

**Candor — the half-owner test [E2-26]: PASSES, and unusually well.** The filing tells an
owner the things that hurt without being asked: the reserve revisions are broken out
separately every year including the −15.3 MMBoe in 2023; costs incurred are published so an
outsider can compute finding cost; the twenty uncontrollable price factors are listed; the
$947.1M of cumulative impairments is stated as a cumulative figure rather than buried;
the 2026 capital budget is a range with the curtailment condition attached; the dividend is
split into regular and special **by the company** rather than by the analyst. **[E2-67]'s
positive pole is met in the sector-appropriate form**: for a reserve-driven filer the
equivalent of Berkshire's reserve-error table is the reserve rollforward with revisions
separated, and SandRidge publishes it.
**Authorship [E2-72]: FAILS as a test — there is no annual shareholder letter in the
documents read.** Recorded as an absence, not a flag.

**Institutional imperative [E2-30], scored:**
- [x] **(1) resists any change in current direction — FIRES, mildly.** The strategy has been
  the same since emergence: run a very low-cost Mid-Continent base, keep the balance sheet
  clean, protect the NOL, buy when something is cheap. Ten years on, with reserves down 61%
  from the 2017 peak and gas at $1.36/Mcf, "no change" is itself a decision.
- [x] **(2) projects or acquisitions materialise to soak up available funds — FIRES, and it
  is the sharpest Q3 finding.** The pattern is documented three times: the cash pile is built,
  and then spent. $129.7M of acquisitions in 2024 (the year operating cash flow was at its
  five-year low of $73.9M and zero operated wells were drilled); $65.0M committed in June 2026
  from a $114.7M balance. Read with [E4-13]'s humility clause — management knows the acreage
  and I do not, and the 2024 purchase did add 16.0 MMBoe at $7.70/Boe against a ~$16/Boe field
  margin, which is defensible arithmetic — but the *behaviour* is [E2-30](2) in its textbook
  form: **available funds attract projects.**
- [ ] (3) staff studies produced to justify a craving — not observable in the documents read.
- [ ] (4) peer behaviour mindlessly imitated — **not fired, and the reverse is notable.** The
  US shale peer group levered up and grew; SandRidge holds zero debt and 19.7 MBoe/d.

**Capital allocation — the two buyback conditions [E5-08, E4-31, E2-51, E5-24]:**
- **(1) ample funds for operations and liquidity — YES**, on any reading: $114.7M of cash,
  no debt, no maturities, positive operating cash flow in every year of the series.
- **(2) repurchases at a material discount to conservatively calculated IV — PASSES on the
  filed record, which is rare.** Life-to-date the program has bought **0.6M shares at an
  average of $10.75**, against a quote of $13.96 — the average purchase is **23% below today's
  price**, i.e. they bought low. This is the [E5-24] first law running the *right* way, and it
  is the inverse of the ASIX record ($195.5M at $30.58 against a $16.49 quote).
- **The [E2-51] refusal tell is the live question instead.** **$68.3M of the $75.0M
  authorisation remains open** and **no shares were repurchased in 2Q26** while the stock
  traded between $11.10 and $18.45 over the year. Condition (1) is satisfied — so the
  abstention is a *choice*, and the choice was to commit $65.0M to acreage instead of to the
  stock. Whether that is the better per-share value trade [E5-31] depends entirely on the
  acquisition's economics, which are not yet filed. **Recorded as a capital-allocation
  question, not a flag**, with [E4-13] attached: *"it is natural for CEOs to be optimistic
  about their own businesses. They also know a whole lot more about them than I do."*
  **This binds position size, never the discount rate — and no position is contemplated.**

**Compensation design — recorded because it is unusually well aligned for this industry.**
The 2025 annual incentive runs on seven metrics (HSE 10%, total capex 15%, and five others),
capped at 150%. The 2025 LTIP PSU metrics and outturns: adjusted G&A $10.0–12.0M target /
**$10.2M actual**; LOE $42.0–50.0M / **$40.4M actual**; base oil production 1.00–1.40 MMBbls /
**1.21 actual**; total production **and** capex 5.90–7.10 MMBoe and $66.0–85.0M /
**6.80 MMBoe and $76.2M actual**. **No EBITDA metric, no TSR metric, and capex is a ceiling.**
The plan pays for spending discipline and cost control, which is [E3-37]'s third attribute —
*"attack costs as vigorously when profits are at record levels as when they are under
pressure"* — written into the contract.

**THE OWNERSHIP AND CONTROL PICTURE — recorded plainly.** Carl Icahn holds **13.1%**;
BlackRock 6.6%; **all directors and executive officers together hold 1.6%**. Of the six
directors nominated for the 2026 meeting, **four have disclosed Icahn affiliations**: Chairman
**Vincent Intrieri** (*"employed by Carl C. Icahn-related entities … from 1998 to 2016"*,
Senior MD of Icahn Capital 2008–2016), **Brett Icahn** (Icahn Enterprises board; portfolio
manager at Icahn Capital), **Nancy Dunlap** (director of Icahn Enterprises G.P. Inc. since
2021), **Jaffrey Firestone** (CVR Energy; ex-Voltari, *"indirectly controlled by Carl C.
Icahn"*). And **the CFO is the former Chairman**: Jonathan Frates, ex-Managing Director of
Icahn Enterprises (2015–2021), *"served as Chairman of the Board of Directors of the Company
from June 2018 until September 2024"*, appointed CFO 2024-10-21.

Two readings are available and the run states both rather than choosing the flattering one:
- **The favourable reading:** an owner with 13.1% of the stock and a five-decade record of
  demanding cash returns is *aligned* with a small outside holder. The record is consistent
  with it — no debt, no dilution, $184.4M returned, buybacks below the current price.
- **The unfavourable reading, which is the one [E4-26] requires be stated harder:** the board
  chairman moving into the CFO seat, insiders holding 1.6%, four of six directors affiliated
  with one 13.1% holder, and a **4.9% poison pill just extended to 2029** (nominally to protect
  the NOL; in effect it prevents anyone else from accumulating a blocking stake) is a control
  structure in which **one shareholder's preferences set the distribution policy** — and that
  shareholder's needs are not the outside holder's. The 2023 $2.00 and 2024 $1.50 specials
  drained $130M from the balance sheet on a timetable no operating logic explains. Under
  [E5-17]'s cap this is not a venality finding and no misconduct is alleged; it is a statement
  that **the outside holder here is a passenger in someone else's capital allocation.**
- **CFO churn, recorded:** three people in the CFO seat inside three years (Brown Sept 2023 →
  Oct 2024; Frates Oct 2024 →). Watch item, not a flag.

**THE GUARDRAIL — checked before the verdict:**
- [x] Confirmed: **nothing in this Q3 is used to promote the name.** Q2 is OUT and stays OUT.
  *"A textile company that allocates capital brilliantly within its industry is a remarkable
  textile company — but not a remarkable business"* **[E2-37]**. A debt-free, low-cost,
  well-governed operator of a depleting Mid-Continent asset is a remarkable *operator* of that
  asset — and [E2-38]'s jockeys-and-nags sentence is the rest of it.
- [x] No key-person dependence recorded at Q2 [E4-23] — the dependence is on the gas price,
  not on a person.
- [x] No excisable-cancer case [E2-35, E2-36] — there is no localized damage to excise; the
  business is doing exactly what it should and the economics are what they are. **The manager
  is not the plan, and there is no plan a manager could be.**

- **Q3 FOR-THE-RECORD READ: no honesty disqualifier found. One flag fired and read
  (Adjusted-EBITDA in the press release only — absent from both the 10-K and the 10-Q, and
  absent from every incentive metric). Two institutional-imperative behaviours fire ((1) and
  (2) — cash attracts acquisitions). The dividend record decomposes 74% special / 26% regular,
  with the specials funded from the balance sheet [E2-60]. Buybacks pass both [E5-08]
  conditions on the filed record, which is rare, but $68.3M sits unused while $65.0M went to
  acreage.** Were the gate live, this Q3 would be the *least* obstructive of the four —
  and it would still not matter, because **Q3 never promotes and Q2 is OUT**. *A pass here
  would be the absence of found disqualifiers, never a clearance [E5-17].*

## Q4 — FOR THE RECORD: WILL IT SURVIVE?

### Owner earnings — **COMPUTATION — NOT A CLEARANCE** [E2-23]
Convention applied: multi-year mean of (OCF − SBC) − (c). OCF nets the working-capital
increment from one audited line (constraint 3). SBC subtracted in full [E5-06]; the reported
charge ($1.4–2.7M/yr) is taken as the floor of the subtraction [E3-70] and is immaterial at
this scale — judgment disclosed. No equity-method or unconsolidated stakes requiring an
[E3-04] look-through (the Royalty Trusts are proportionately consolidated).

Per year, $M, filed figures (FY2023–25 from the FY2025 10-K cash-flow statement; FY2021–22
from 10-K-sourced XBRL):

| FY | OCF | SBC | capex (PP&E) | acquisitions | D&A | OE (c=capex) | OE (c=D&A) |
|---|---|---|---|---|---|---|---|
| 2021 | 110.3 | 1.4 | 11.6 | n/d | 15.4 | 97.3 | 93.5 |
| 2022 | 164.7 | 1.5 | 44.1 | n/d | 17.9 | 119.1 | 145.3 |
| 2023 | 115.6 | 1.9 | 26.4 | 11.2 | 22.2 | 87.3 | 91.5 |
| 2024 | 73.9 | 2.4 | 26.4 | 129.7 | 32.5 | 45.1 | 39.0 |
| 2025 | **100.1** | 2.7 | 58.6 | 8.5 | 42.9 | 38.8 | 54.5 |
| H1 2026 | 62.2 | 1.5 | 40.1 | 5.1 | 23.6 | 20.6 | 37.1 |

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25]:**
- **Long-window mean (5-yr FY2021–25, the corpus default [E2-42]): $77.5M (c=capex) to
  $84.8M (c=D&A)** → **15.0%–16.4%** on $517.6M.
- **Short-window mean (3-yr FY2023–25): $57.1M (c=capex) to $61.7M (c=D&A)** → **11.0%–11.9%**.
- **Spread, conservative end: the 3-yr sits ~$20M (26%) below the 5-yr.**
- **THE OPERATOR SWEEP'S 11.8% IS IDENTIFIED: it is the 3-year window at the c = D&A end
  (11.9%).** It is refused below, on two independent grounds.

**The distorted years, named [E5-11], and the [E4-41] normalization applied in writing:**
1. **FY2021–22 is the wave.** The post-COVID / post-invasion energy price spike, quantified by
   the filer itself: Henry Hub spot ranged **$1.26 to $24.77/Mcf** across 2021–2025. FY2022
   net income of $242.2M also contains a **$64.5M non-cash income tax benefit**. [E4-41] —
   *"favourable exogenous breaks in the window are named and removed before the mean is
   trusted"* — **strips FY2021–22 from the level.**
2. **FY2024 is the reverse distortion and it cuts the other way.** *"During the year ended
   December 31, 2024, there were **no operated wells drilled**."* Its $26.4M capex is an
   underspend against maintenance, not a maintenance figure — which is precisely why the
   3-year c=capex mean of $37.1M is also too low.
3. **H1 2026 contains an oil spike.** Realised oil $62.80/Bbl (2Q25) → **$95.35/Bbl (2Q26)**,
   +52%, while realised gas fell to $1.36/Mcf. Oil was 18% of 2Q26 volume and **61% of
   revenue**. Annualising H1-26 annualises an oil price. **Not done.**
- *Scope check [E3-55]:* volatility is not automatically a defect where the endgame is
  certain. Here it is a defect, because the endgame is **not** certain — the level of the price
  determines both the cash flow *and* the size of the reserve base (the SEC-price revisions
  line moves reserves by ±15 MMBoe). The spread is a finding, not noise.

**Maintenance capex — THE DISCLOSED JUDGMENT, and this is where the run turns [E2-23]
constraint 4, [E5-20], [E4-04].**
The corpus default is D&A **[E3-44, E2-41]** — *"at 95% of American businesses, capital
expenditures that over time roughly approximate depreciation are a necessity."* [E5-20] names
the exception: *"in the case of all railroads, merely spending their depreciation expense will
not keep them in the same place."* **An oil and gas producer is the exception in its purest
form, because the asset is not merely worn — it is consumed and removed.** [E4-04]'s scoping
sentence names the class explicitly: *"the moat whose basis must be periodically replaced …
depleting assets."*

The filed arithmetic, from the 10-K's own rollforward and costs-incurred tables:

| | |
|---|---|
| FY2025 production to be replaced | **6.768 MMBoe** |
| Blended all-in finding & acquisition cost, 3-yr | **$9.59/Boe** → **≈ $65M/yr** |
| Organic finding & development cost, 3-yr | **$13.89/Boe** → **≈ $94M/yr** |
| Book depletion rate charged, FY2025 | $5.38/Boe → $36.4M |
| FY2025 total D&A | **$42.9M** |
| **The company's own 2026 capital budget** | **$76.0M–$97.0M** |

**The company's own forward number sits inside the replacement range and outside the D&A
range.** That is the filing telling the analyst which end of the band is real.
**Therefore: the D&A end of this band is INVALID, not merely optimistic [E5-20], and (c) is
judged up to $65M–$94M.** The band is displayed at all four ends below as a display of the
guess, never as four equally legitimate answers.

**THE BOTTOM BOUNDARY [E5-34]** — FY2023–25 mean OCF $96.6M less mean SBC $2.3M = $94.3M
available, less (c):

| (c) basis | (c), $M | OE, $M | yield on $517.6M |
|---|---|---|---|
| D&A (corpus default — **REFUSED under [E5-20]**) | 32.5 | 61.7 | 11.9% ← *the sweep's number* |
| capex as spent (contains the zero-rig 2024) | 37.1 | 57.1 | 11.0% |
| **blended replacement cost $9.59/Boe** | **65.0** | **29.3** | **5.7%** |
| company's own 2026 budget, midpoint | 86.5 | 7.8 | 1.5% |
| **organic F&D $13.89/Boe** | **94.0** | **0.3** | **0.1%** |

**BOTTOM BOUNDARY: owner earnings ≈ $0M to $29M — a yield of ≈ 0% to 5.7% at $13.96,
against a 5.19% sovereign.**

- *Is the combined range too wide to reach a conclusion [E4-25]?* **No — and that is the
  point.** The range is wide in absolute terms ($0–85M) but every honest configuration lands
  **at or below the sovereign**, and the only configurations that clear 10% are the ones the
  framework's own rules forbid: the wave years [E4-41], and the D&A proxy in the class [E5-20]
  excludes. **A conclusion is reachable precisely because the disqualified configurations are
  disqualified by rule and not by preference.**
- **Working capital:** netted through OCF (constraint 3). Non-cash working capital at
  2026-06-30 is **negative $20.8M**; there is no inventory build to fund.
- **[E2-60]'s third dimension — financial strength:** the payout has **not** been funded by
  rising leverage (there is none). It has been funded by the cash balance, which is a
  distribution of capital rather than of restricted earnings. Different mechanism, same
  direction, and it is quantified above.

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [ ] good · **[x] gruesome — but the reason is not the usual one, and the
  contrary case is stated first, per [E4-51].**

**The contrary case, as its best advocate would put it:** *This business has no debt, cash
worth 22% of the market cap, a lifting cost of $5.35/Boe that is genuinely at the low end of
the American onshore, an acquisition record that bought 16.0 MMBoe at $7.70/Boe against a
~$16/Boe field margin, buybacks executed 23% below today's price, a $1.6bn tax shield that
makes every pretax dollar an after-tax dollar, and reported ROEs of 12.7%, 13.6% and 14.5% in
three of the worst gas-price years on record. Call it "good" [E4-43] — the class that
passes — because it does earn an attractive return on the capital it adds, and that is
literally the definition.*

**Why it fails anyway, on the corpus's own arithmetic:**
1. **The reported return is computed against an expense that is too small.** Depletion is
   charged at $5.38/Boe; the barrel costs $9.59–$13.89 to replace. Every year that gap
   ($4–8.50/Boe × 6.768 MMBoe = **$29M–$58M**) is reported as profit and is in fact
   liquidation. Restate FY2025 net income of $70.2M for the true replacement charge and it
   falls to roughly **$13M–$42M** on average equity of $486M — **2.6% to 8.6%**.
2. **[E4-20]'s gruesome test, met literally.** *"The gruesome account both pays an inadequate
   interest rate and requires you to keep adding money at those disappointing returns."* The
   inadequate rate is the 0–5.7% bottom boundary against a 5.19% sovereign. The money you must
   keep adding is $76–97M a year, forever, **just to stand still** — 15–19% of the market
   capitalisation, annually, for zero volume growth.
3. **[E4-43] is checked and does not rescue it.** The good class earns an attractive return
   *also on the deposits that are added*. Here the deposits are added and the reserve base
   still fell from 74.3 to 69.1 MMBoe over three years while $267.6M was spent — 92% of all
   operating cash flow in the window. The deposits are not compounding; they are being
   consumed.

### Staying power — score all three **[E5-11]**
1. **Large and reliable stream of earnings: FAIL on "reliable."** Net income $116.7M →
   $242.2M → $60.9M → $63.0M → $70.2M. Revenue is volume × a price the company's own Item 7A
   names as its most significant market risk. Realised gas per Mcf: $1.71 → $1.10 → $2.10 →
   $1.36 (2Q26). Reliability is exactly what a price taker on a depleting asset cannot file.
2. **Massive liquid assets: PASS as filed, with a dated qualification.** $114.7M of cash and
   equivalents at 2026-06-30 (22% of market cap) and **zero debt**, deposited *"with multiple,
   well-capitalized financial institutions."* [E5-39]'s standard — *"we will never be
   dependent on the kindness of strangers"* — is genuinely met: there is no revolver drawn, no
   commercial paper, nothing depended on. **The qualification: $65.0M of it is committed to an
   acquisition expected to close in Q3 2026, plus up to $6.0M of earn-outs.** Post-close the
   liquid position is roughly $50M plus second-half generation — still unlevered, no longer
   massive.
3. **No significant near-term cash requirements: the answer depends on how the question is
   read, and the corpus's reading is the harder one.**
   - *Contractual* requirements: **none.** No debt, no maturities, no covenants, no leases of
     consequence. Cash interest paid in H1 2026 was **$0.4M**.
   - *[E5-11]'s actual requirement* — *"ignoring that last necessity is what usually leads
     companies to experience unexpected problems"* — is about **cash that must go out**. For
     this business two such streams exist and neither is contractual: **$76–97M a year of
     replacement capital**, without which the asset self-liquidates in under nine years; and
     **$72.4M of asset retirement obligations** (10-K rollforward: opening $68.6M, accretion
     $5.1M, closing $72.4M, of which $8.1M current), which are certain, dated by well life, and
     accrete at ~$5M a year whether or not a barrel is sold.
   - **Score: PASS on the contractual test, FAIL on the economic one.** The distinction is
     recorded rather than resolved in the company's favour.
- **Leverage, named and quantified [E4-16, E3-29]: ZERO.** Total liabilities $125.4M at
  2026-06-30, of which $74.9M is asset retirement obligations and $49.0M trade payables.
  **Net cash of $114.7M.** [E2-54]'s coverage test — *"all interest, both payable and accrued,
  … comfortably met out of current cash flow net of ample capital expenditures"* — is passed
  trivially because there is no interest. **This is the strongest single fact in the file, and
  it is a Q4 fact that cannot repair a Q2 verdict.**
- **[E3-52]'s terms test, run in reverse:** the ARO is the *opposite* of float — a
  covenant-free but **inescapable, long-dated, company-owed** liability that accretes, with no
  offsetting asset. It is the one liability an E&P cannot refinance away.

### Name the specific ways THIS business dies **[E2-27, E3-24]** — the iron prescription [E4-51]
*Modelling exposure, not experience [E4-40]. A benign recent record — a stock that has doubled
off its 2020 low, four and a half years without a recordable incident, three profitable years
in a bad market — is "not only useless, but actually dangerous" as a guide.*

1. **Natural gas stays cheap and the equity is a wasting asset: LIKELY — it is the present
   state.** Gas is 50% of volume. SandRidge's realised gas price has been **$1.71, $1.10,
   $2.10 and $1.36/Mcf** across 2023, 2024, 2025 and 2Q26. [E2-27]'s mechanism is the shale
   industry's exactly: *"viewed individually, each company's capital investment decision
   appeared cost-effective and rational; viewed collectively, the decisions neutralized each
   other."* Associated gas from oil-directed drilling arrives regardless of the gas price.
   **Quantified from filed figures:** in the present state normalized owner earnings run
   **$0M–$29M** against a $517.6M cap — 0% to 5.7% — while $76–97M/yr of replacement capital
   remains mandatory and $72.4M of retirement obligations accrete. The equity does not go to
   zero; it **runs down** as the reserve base is converted to dividends and specials, which is
   the slower and more comfortable version of the same outcome.
2. **Depletion outruns replacement: A REAL POSSIBILITY, and the meter is running — but the
   bear case must be stated at its true strength, not its most convenient [E4-51].** The filed
   record cuts both ways: organic replacement was **45% over three years** but **108% in
   FY2025** at $9.45/Boe; reserves are **177.6 → 69.1 MMBoe** since 2017 but **63.1 → 69.1**
   over the last year; proved developed life is **8.9 years**, and the competitor row says that
   is **the shortest in the peer set** (MNR 18.7, CRK 15.6, CNX 15.4, GPOR 11.2).
   **Quantified [E3-24]:** at the three-year 45% rate with acquisitions stopped, proved
   reserves fall ~3.7 MMBoe a year and the base halves in about nine years; at the FY2025 108%
   rate they hold — but only while the rig runs and only at a spend ($76–97M) that consumes
   essentially all normalized operating cash flow. **The likelihood judgment therefore
   attaches to the spending, not to the geology: the reserves can be held, and holding them
   costs everything the business earns.** The company's other answer is to buy ($149.4M in
   three years, $65.0M more committed) — which converts the balance sheet into reserves and
   means **the net cash and the reserve base are not additive assets; they are the same asset
   at two points in time.** That is the single most important sentence in this run for anyone
   valuing SD on "net cash plus PV-10."
3. **A bad acquisition at the top of an oil spike: A REAL POSSIBILITY, and it is live now.**
   [E2-30](2) fired above. The $65.0M Cherokee purchase was signed **2026-06-26, effective
   2026-05-01**, in a quarter when SandRidge's own realised oil price was **$95.35/Bbl versus
   $62.80 a year earlier**, and it carries **three $2.0M earn-outs keyed to WTI thresholds** —
   i.e. the seller is paid more if oil stays high, which is the seller's view of the same
   spike. **Quantified:** $65M is 12.6% of the market cap and 57% of the cash. If the acquired
   barrels were underwritten at $95 oil and the price reverts to the $65.34 SEC deck, the
   purchase economics move against SandRidge by roughly a third on the oil leg.
   [E5-24] governs: *"what is smart at one price is dumb at another."*
4. **The NOL is impaired by an ownership change: A LOW-LEVEL POSSIBILITY, quantified.** The
   §382 machinery is disclosed in full: a 2016 ownership change already limited the
   pre-emergence attributes, and *"future transactions involving the Company's stock **including
   those outside of the Company's control** could cause an IRC 382 ownership change."* The
   defence is a 4.9% pill just extended to 2029, which requires shareholder approval at the
   2027 meeting. **What is at risk is the $78.3M of booked deferred tax asset** — 15% of the
   market cap — plus the zero-tax assumption embedded in the entire $439.6M PV-10.
5. **The energy-transition tail [E4-40]: UNKNOWABLE in timing, real in exposure — and it is
   the exposure that is scored, not the experience.** The company's own risk factor states it:
   *"Fuel conservation measures, alternative fuel requirements, increasing consumer demand for
   alternatives to oil and natural gas, technological advances in fuel economy and energy
   generation devices could reduce demand."* The framework's discipline here is [E4-40]'s
   exactly — the terrorism-risk error was *"focusing on experience, rather than exposure."*
   A ten-year reserve life is, perversely, the mitigant: SandRidge's asset is short enough that
   a 2040s demand decline barely touches the PV-10. **The tail is real and it is mostly
   somebody else's problem, because SandRidge's proved book is gone before it arrives.** That
   is an honest finding in the company's favour and it is recorded as such.

- **Q4 FOR-THE-RECORD READ: solvency is not in question and will not be — zero debt, net cash,
  no maturities, no covenants; [E2-54] passes trivially. But [E5-11]'s three strengths score
  FAIL / PASS-with-a-dated-qualification / PASS-contractual-FAIL-economic, and the
  owner-earnings arithmetic at an honest (c) puts the bottom boundary at 0–5.7% against a
  5.19% sovereign. Were this gate live, Q4 would be OUT on [E4-20]'s gruesome test — a
  business that must add $76–97M a year to stand still and earns 0–6% while doing it. The
  business does not die; it distributes itself.**

---
## Q5 — FOR THE RECORD — **COMPUTATION — NOT A CLEARANCE**
*(Q1–Q4 did not close IN. Operator rule 3 header governs everything below; no entry language.
Cap $517.6M at $13.96, 2026-08-28. Sovereign 5.19%, 2026-08-27.)*

**1. THE YIELD** — owner earnings ÷ market cap, beside the sovereign:

| OE basis | OE ($M) | yield on $517.6M | vs 5.19% sovereign |
|---|---|---|---|
| 5-yr mean, c=D&A (**wave in — refused [E4-41]**) | 84.8 | 16.4% | +11.2 pts |
| 5-yr mean, c=capex (**wave in — refused**) | 77.5 | 15.0% | +9.8 pts |
| 3-yr mean, c=D&A (**the sweep's 11.8% — refused [E5-20]**) | 61.7 | 11.9% | +6.7 pts |
| 3-yr mean, c=capex-as-spent (contains the zero-rig year) | 57.1 | 11.0% | +5.8 pts |
| **Bottom boundary, (c) = blended replacement $9.59/Boe** | **29.3** | **5.7%** | **+0.5 pts** |
| **Bottom boundary, (c) = organic F&D $13.89/Boe** | **0.3** | **0.1%** | **−5.1 pts** |
| Cross-check: company's own 2026 capex budget midpoint | 7.8 | 1.5% | −3.7 pts |

**The sweep's 11.8% is located and disposed of: it is the FY2023–25 window with (c) set to
depreciation, in a business the corpus's own [E5-20] exception says depreciation cannot
measure.** It is not a fraudulent number; it is the right formula applied to the one industry
class where the default input is invalid.

**2. THE ASSET BASIS — the second book, worked beside the first** *(operator tasking; for a
depleting asset the liquidation read is a real cross-check, and it contains a trap)*

| component | conservative | generous | basis |
|---|---|---|---|
| PV-10, proved reserves, YE2025 SEC prices ($65.34 oil / $3.39 gas) | 439.6 | 439.6 | 10-K; net of production, development **and abandonment** costs; tax already $0 |
| Cash and equivalents incl. restricted | 114.7 | 114.7 | 10-Q, 2026-06-30 |
| Total debt | 0 | 0 | *"no outstanding term or revolving debt obligations"* |
| Non-cash working capital | (20.8) | (12.8) | CA ex-cash $37.0M − CL $57.8M; generous adds back current ARO already inside PV-10 |
| Corporate G&A, absent from PV-10 by definition | (81.1) | (62.7) | $13.2M/yr (adjusted ex-SBC $10.2M) × 10-yr annuity at 10% |
| Other PP&E, net | 0 | +72.6 | conservative treats it as subsumed in PV-10's LOE assumption |
| **NOL, incremental to PV-10** | **0** | **+78.3** | see the trap below |
| **Asset basis** | **≈ $452M** | **≈ $630M** | |
| **per share** | **≈ $12.20** | **≈ $17.00** | 37.075M shares |

**THE NOL TRAP, stated because a screen will get this wrong.** SandRidge's PV-10 **equals** its
standardized measure exactly, in all three filed years, because the standardized measure's
"future income tax expenses" line is **$0** — and the 10-K's footnote says why: future taxes are
computed *"including expected tax benefits to be realized from the utilization of net operating
loss carryforwards."* **The NOL shield on the proved reserve stream is already inside the
$439.6M.** Adding "$1.6bn of NOLs" to PV-10 double-counts it. What is genuinely incremental is
the shield on income the proved book does not generate — and management's own filed judgment of
the realisable total is **$78.3M of net deferred tax asset against a $384.9M valuation
allowance**, i.e. its own auditors' more-likely-than-not test says the rest will not be used.
**Carried as $0 (conservative, no double-count) to $78.3M (generous, management's entire booked
figure treated as incremental).** Anything above $78.3M would be the analyst overriding both
management and the auditor in the direction the analyst wants — the exact move rule 9 exists
to prevent.

**And the two books are not additive.** Death 2 above: the cash *becomes* the reserves. $149.4M
of the last three years' acquisitions turned balance sheet into PV-10, and $65.0M more is
committed. A valuation that adds net cash to PV-10 and then also credits the reserve base with
being replaced is counting the same dollar twice.

**Result: the market capitalisation of $517.6M sits inside the $452M–$630M asset range, in its
lower half.** The price is not stupid, and it is not a bargain. And the PV-10 leg is not a
floor: it is struck at a trailing-twelve-month SEC deck of $65.34 oil and $3.39 gas, while the
latest filed quarter realised **$95.35/Bbl oil** (far above) and **$1.36/Mcf gas** (far below,
on 50% of the volume), and its 10% discount rate is generous for a single-basin depleting asset.

**3. THE FLOOR [E4-28, E3-13].** *"That's the figure we quit on … whether short rates are 6
percent or whether short rates are 1 percent."* Honest pre-tax expectancy at $13.96:
**the bottom-boundary yield of 0%–5.7%, plus believable growth.** The growth case would have to
be a **gas price recovery** — which is a macro forecast, refused at [E3-32] (*"I do not have to
have a view on interest rates — and I don't have a view"*, and the same discipline applies to
commodity prices), and which [E4-35]'s base rate would in any case require to be argued in
writing against odds of fewer than one in twenty. **Below the figure we quit on, in every
configuration the framework's own rules permit.** Clearing 10% requires either crediting the
2021–22 wave as the level (refused, [E4-41]) or using depreciation as (c) in the industry class
[E5-20] excludes. **That double refusal is the bias check doing its work: a dividend-hunting
operator would like the 11.8% to be real, so the run must be hardest on exactly that number.**

**4. WHAT THE PRICE ALREADY ASSUMES.** At $517.6M against a bottom-boundary OE of $0–29M, the
market is paying 18× to infinity on normalized owner earnings — which is to say it is not
pricing owner earnings at all. It is pricing the **asset**: roughly PV-10 plus the cash, with
the NOL and the acquisition optionality as the reconciling items. The year-1 growth needed to
justify the quote on an earnings basis is not computable from a base of ~$15M without producing
a meaningless number, and the honest statement is that **the quote is an asset price, and the
asset is a ten-year annuity on a commodity nobody can forecast.** What the business has actually
done: organic reserve replacement 45%, reserves down 61% from 2017, realised gas below $2.10 for
four straight years.

**5. WHAT YOU ARE PAID.** At the bottom boundary: **+0.5 points to −5.1 points versus the
sovereign.** At the refused 3-year D&A configuration: +6.7 points. The run reports the first.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01], for the record only:**
- On the asset basis: **roughly $450M to $630M ≈ $12 to $17 a share.**
- On normalized owner earnings of $0–29M capitalised at the sovereign plus an ordinary equity
  spread: **roughly $0 to $350M ≈ $0 to $9 a share.**
- **Current price $13.96 / $517.6M.** Inside the asset range; above the earnings range.

**WHICH BAR?** **[x] Screamer test [E4-01]** only, and it fails at the first step: the price is
not below the conservative case; it is inside the range. *"Usually, the range must be so wide
that no useful conclusion can be reached"* — here the middle box applies: **price inside the
range → no useful conclusion → move on — and Q2 OUT closes entry at any price regardless
[E5-35].** No margin is stacked on top; no normal-method margin is applied, because the two
bars are never run on the same number.
**Windage count: ONE** — the [E4-41] normalization (the 2021–22 wave stripped from the level,
the H1-26 oil spike not annualised), justified in writing above. The [E5-20] refusal of the D&A
proxy is **not** a second windage: it is the framework's own required move in a named exception
class, not extra conservatism. The asset basis is displayed at both ends rather than taken at
the conservative one, which is the discipline running the other way.

**Ranking position: not ranked.** [E4-28] — a candidate below the floor *"is not ranked — it is
quit on."*

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*(No position exists; pre-committed yardsticks set prior to any act [E1-02]. **Alert
thresholds are LISTED here only** — no alerts file edited.)*

**Q2 REOPEN CONDITIONS — the only route back to entry: effectively none, and the reason is
structural, not cyclical.** A company that sells a commodity at a screen price and must buy back
its own asset base every decade cannot become a franchise by getting better at either activity.
The [E4-04] exclusion is a statement about the *kind* of asset, and the kind does not change.
The MITSY reopen status applies: **closed.** The one theoretical route would be a
framework-level ruling on whether a filed, demonstrated, wide-and-sustainable cost advantage
[E2-58] can qualify a depleting asset — which is a structural question for the framework owner
under **PRIME RULE 5**, not for this run, and which SandRidge's own 0–5.7% normal-state
owner-earnings yield does not currently support in any case.

**What would prove THIS RUN's reasoning wrong (evidence, listed, falsifiable):**
- **Organic reserve replacement ≥ 100% for three consecutive years at total costs incurred
  below $8.00/Boe of production**, computed from the 10-K's own rollforward and costs-incurred
  tables. That would falsify the depletion arithmetic that drives (c) — the (c) guess would
  fall toward $54M and the bottom-boundary yield would rise toward 8%. **The threshold is set
  at three years and on costs-incurred-per-barrel-produced deliberately, because FY2025 alone
  already cleared the volume half of it (108%) and the cost half is where the case actually
  lives** *(FY2025 actual: $11.45/Boe; FY2023–25: $14.10/Boe)*. A run that set the bar where
  the company had just passed it would be a bar chosen to be cleared.
- **Normalized owner earnings, ex-wave, with (c) at demonstrated replacement cost, sustained
  above ~$52M (10% on today's cap) across a non-spike window.** That would falsify the
  bottom-boundary arithmetic directly.
- **A filed statement that the Cherokee inventory is long enough to make the asset
  non-depleting on any relevant horizon** — e.g. a proved-plus-probable location count implying
  a 25-year+ development runway at the current rig pace. That would weaken (not remove) the
  [E4-04] exclusion by pushing the replacement obligation beyond the valuation horizon.

**Watch-list metrics and thresholds (review triggers, not auto-executions, no position held):**
- **The reserve rollforward and costs-incurred tables, FY2026 10-K (~March 2027):** organic
  replacement %, organic F&D $/Boe, and the revisions line. This is the single monitoring
  number for this name — it is [E4-32]'s direction metric and [E4-55]'s physical series in one.
- **The Cherokee acquisition, once closed and booked:** reserves acquired ÷ $65.0M = the
  realised acquisition cost per Boe, against the $7.70/Boe three-year record and the $9.59
  blended replacement cost. Whether the earn-outs trigger tells you what oil did.
- **The regular dividend line, each quarter's 8-K:** a cut in the *regular* leg is the honest
  signal; another *special* is the balance sheet being distributed again and is **not** an
  improvement. The two must never be read as one number.
- **The $68.3M unused buyback authorisation:** any repurchase below the ~$12.20 conservative
  asset basis would be [E5-08] condition (2) satisfied on this run's own numbers; continued
  abstention while acquisitions are made is the [E2-51] question staying open.
- **Cash and equivalents, each 10-Q:** post-acquisition rebuild rate. Below ~$40M with capex
  still running at $76–97M would put the regular dividend in competition with the drill bit.
- **§382 / the Tax Benefits Preservation Plan:** the third amendment goes to shareholders at
  the **2027 annual meeting**; any disclosed ownership change, or any failure to re-approve,
  puts the $78.3M booked DTA and the PV-10's zero-tax line at risk simultaneously.
- **Realised natural gas price per Mcf, each quarter** — the [E2-58] supply-tight ratio's
  reading for this filer. Four consecutive years at or below $2.10 is the current record.
- **Price alert (list only): NONE for entry.** A Q2-OUT name has no entry band at any price
  [E5-35]. For calibration only, and explicitly not a buy signal: below roughly **$9** the
  quote would sit under this run's conservative asset basis of ~$12.20 with the reserve base
  free — a fact about the market, not about the business, and the reopen conditions above
  still govern.
- **Next catalyst dates:** Q3 2026 10-Q ~early November 2026 (acquisition closed and booked,
  cash rebuild, regular dividend) · FY2026 10-K ~March 2027 (**the reserve rollforward — the
  one that matters**) · 2027 annual meeting (pill re-approval).

- **VERDICT: [x] IN** — the question is answered with pre-committed, dated, document-named,
  falsifiable conditions on both sides, and the falsifiers are computable from tables the
  company already publishes annually.

---
## SELF-AUDIT
- [x] Questions answered in order; stopped at the first non-IN (Q2 OUT); Q3–Q5 written for the
      record only, under operator rule 3's **COMPUTATION — NOT A CLEARANCE** header
- [x] No question marked IN carries an "unverified" or "provisional" caveat
- [x] Every UNRESEARCHED item names the artifact and where it lives (register below)
- [x] Q2 OUT states what specifically fails and on which filed evidence — the filer's own
      Item 7A/Item 1A/MD&A price-dependence language, and the filed reserve rollforward and
      costs-incurred tables demonstrating [E4-04]'s "periodically replaced" exclusion
- [x] Step 0: both filings read with accession numbers; **FY2025 OCF cross-checked
      filed-statement-vs-XBRL (100,140 / 73,933 / 115,578 — ties)**; EPS recomputation ties
      ($0.72); market cap verified against the **filed** share count from the 10-Q cover
- [x] Owner earnings on multi-year means; **both windows shown** (3-yr conservative end ~$20M
      below the 5-yr — the spread carried as a finding); distorted years named (2021–22 wave,
      the zero-rig 2024, the H1-26 oil spike); **(c) a disclosed judgment with the [E3-44]
      default explicitly REFUSED under [E5-20]** and judged up to filed replacement cost, with
      the company's own $76–97M budget cited as the confirming evidence; SBC subtracted in
      full; **bottom boundary [E5-34] stated**; the asset basis worked beside it
- [x] Competitor row filled — **4 of 4 attempted peers obtained in full from their FY2025
      10-Ks with accession numbers** (MNR, GPOR, CRK, CNX; AMPY obtained and disqualified as
      non-comparable; PHX not obtainable); non-comparability stated peer by peer rather than
      smoothed; **the moat class decided on the subject's own filing, not on the row**
      (MITSY/ASIX precedent) — so **not PROVISIONAL** and Q2 is not UNRESEARCHED; row limit
      [E3-61] stated; remaining gaps recorded as work orders
- [x] **The counter-evidence to this run's own thesis was hunted and printed [E4-26, E4-51]:**
      FY2025 organic replacement of 108% (against the three-year 45%), the zero-debt balance
      sheet, buybacks executed 23% below the quote, no loss year in five while three of four
      peers lost money, and the highest PV-10 per Mcfe in the peer set — each stated at full
      strength before being weighed
- [x] Sovereign for the earnings currency (USD) from the issuing-authority series (FRED DGS30
      via direct `fredgraph.csv`), observation dated **2026-08-27**
- [x] Value stated as round-number ranges; **price-inside-the-range identified as itself the
      conclusion [E4-25]**
- [x] One bar (screamer, for the record); **windage count: one** ([E4-41]), justified in
      writing; the [E5-20] refusal recorded as a rule application, not a second margin
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] **Bias declaration (rule 9) made and pre-registered at the top**; the sweep's 11.8%
      located as the 3-year c=D&A configuration and refused; **the dividend decomposed from
      the filer's own table before it was assessed**
- [x] The market-beating claim is not made anywhere; every judgment carries a ledger id or is
      labelled a judgment/estimate
- [x] Run committed to git with its evidence pack. *Recorded honestly per operator protocol 6
      (corrections go in an addendum, never by editing history): the run file, the evidence
      pack, the competitor row and the primary filings were staged by this session but were
      swept into commit **833911e** by a concurrent session's broad `git add` before this
      session's own commit ran. History is left as it is; this line and the commit carrying it
      are the record of what 833911e actually contains.*

## REGISTER
- **Verdict: [x] OUT (about the business, at Q2 — for entry, at any price).** No position held;
  no [E2-28] hold read required. Q3 for the record: **no honesty disqualifier found**; the
  Adjusted-EBITDA flag fires in the press release but **not** in the 10-K, the 10-Q, or any
  incentive metric; two [E2-30] behaviours fire (direction unchanged; cash attracts
  acquisitions); the dividend decomposes **74% special / 26% regular**; buybacks pass both
  [E5-08] conditions at an average of **$10.75 against a $13.96 quote**, which is rare and is
  recorded in the company's favour; the control structure (Icahn 13.1%, four of six directors
  affiliated, the former Chairman now CFO, a 4.9% pill extended to 2029, insiders at 1.6%) is
  recorded with both readings stated. Q4 for the record: **zero debt, $114.7M net cash, the
  [E2-54] coverage test passed trivially** — and staying-power strengths 1 and 3 fail on the
  corpus's own reading, with [E4-20]'s gruesome test met literally. Q5 computation:
  **bottom-boundary yield 0%–5.7% against a 5.19% sovereign — below the [E4-28] floor in every
  configuration the framework permits; the sweep's 11.8% was depreciation standing in for
  depletion in the one industry class [E5-20] excludes.**
- **One line: a genuinely well-run, debt-free Mid-Continent producer whose own 10-K says the
  prices it receives are its most significant risk, and whose own tables say it spent $11.45
  a barrel produced in FY2025 and $14.10 over three years while charging $5.38 a barrel of
  depletion — so the reported 14.5% return on equity is partly the reserve base being
  distributed as income; the competitor row says it has the shortest reserve life (10.2 years)
  and the smallest reserve base (415 Bcfe) of every comparable filer and no cost advantage
  over any of them; the 11.8% screen yield is depreciation standing in for depletion in the
  one industry the corpus names as the exception, the honest owner earnings are 0–6% against a
  5.19% bond, and 74% of the celebrated dividend was a special paid out of a cash pile now
  being spent on more acreage. Not a compounder, not buyable under this framework at any price
  it has shown — and, said plainly because it is true, a creditable and unlevered steward of
  an asset that is being consumed.**
- **Work orders (UNRESEARCHED — every one names its artifact and its rung):**
  1. **Competitor-row gaps** — four peers (MNR, GPOR, CRK, CNX) were obtained in full with
     accession numbers; see `SD competitor row (MNR-GPOR-CRK-CNX).md`. Outstanding:
     (a) **Comstock's PV-10**, which CRK publishes nowhere in its FY2025 10-K and which cannot
     be derived from the filed after-tax table — a gap recorded rather than estimated;
     (b) **three-year F&D cost for every peer**, which would put SD's $14.10/Boe of costs
     incurred per barrel produced into relative context — each peer's FY2023 and FY2024 10-K
     on EDGAR, ordinary retrieval; (c) **LOE per Boe for every peer**, the direct test of
     SD's $5.35/Boe cost claim — same documents; (d) **PHX Minerals**, which has no entry in
     SEC's current ticker file, consistent with its no longer being a public reporting
     company — recoverable only by name-based EDGAR search and probably ending before FY2025.
     None of these can change the Q2 verdict, which rests on SD's own filing.
  2. **The YE2025 reserve report itself** — Cawley, Gillespie & Associates, filed as **Exhibit
     99.1 to the FY2025 10-K, accession 0001628280-26-015318**. Read for the price-deck
     sensitivity, the PUD development schedule and the decline assumptions. **Ordinary
     retrieval; not obtained this session.** This is the highest-value unread document in the
     file, because the run's entire (c) judgment rests on replacement economics.
  3. **FY2021 and FY2022 10-Ks** (accessions retrievable from `SD_submissions.json`) — the
     acquisitions and costs-incurred lines for those two years, to extend the reserve-
     replacement and finding-cost series from three years to five. Ordinary retrieval.
  4. **The 8-K announcing the Cherokee acquisition and any subsequent closing 8-K/8-K-A** —
     reserves acquired, the actual $/Boe, and whether the earn-outs triggered. EDGAR, ordinary
     retrieval; the closing filing does not exist yet (expected Q3 2026).
  5. **The Q3 2026 10-Q (~November 2026)** — post-acquisition cash, the regular dividend, and
     the first booked reserves from the purchase.
  6. **Historical CEO/CFO succession detail before 2023** — 8-Ks from 2018–2022 for the
     post-bankruptcy management churn. EDGAR, ordinary retrieval; judged **not decisive** here
     because Q2 is OUT and the churn read does not change it.
- **The single biggest concern (for any future reader): death 2 — the two books are the same
  book.** The attractive version of SandRidge is "net cash plus PV-10 plus a $1.6bn NOL." All
  three legs are less additive than they look: the NOL shield is **already inside** the PV-10
  (which is why PV-10 equals standardized measure exactly, and why management books only
  $78.3M of it as realisable against a $384.9M valuation allowance); and the cash is not a
  separate asset but **the next reserve purchase** — $149.4M of it went that way in three
  years, $65.0M more is committed, and it must, because organic drilling replaces 45% of
  production. **A depleting asset that funds its own replacement out of the same balance sheet
  an investor is counting as surplus is a business whose net asset value is being quietly
  recycled rather than accumulated.** Everything else in this file is cyclical or benign;
  that one is structural, and it is what makes the 11.8% screen yield an artifact rather
  than a return.

*This file is a judgment by the AI running the framework. The underlying facts are the FY2025
10-K (acc. 0001628280-26-015318), the Q2 2026 10-Q (acc. 0001628280-26-054413), the 2026-08-05
results 8-K and Exhibit 99.1 (acc. 0001628280-26-053557), the 2026 DEF 14A (acc.
0001140361-26-017133), SEC XBRL companyfacts, FRED DGS30, and one flagged live quote. Where a
number is a judgment or an estimate — the (c) band, the G&A annuity in the asset basis, the
round-number ranges, the restated FY2025 return on equity — it is labelled as one.*
