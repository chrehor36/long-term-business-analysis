# Company Run — AMREP Corporation (NYSE: AXR) — 2026-08-30
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this file
and that document disagree, the document governs. Q3 annex:
`Framework/v4/THE MANAGER STANDARD - Q3.md`. Evidence pack:
`Test Runs/_research 2026-08-26/AXR evidence pack + competitor row.md`.

**Position context: NONE HELD. Fresh entry run.** Surfaced by a small-cap sweep
(cap ~$124M on ~5.3M shares). **Bias declared per operator rule 9:** ~$2,750 of taxable
capital is waiting and wants a dividend payer that compounds, so the analyst's incentive
is to clear this name. The iron prescription [E4-51] is applied and disconfirming evidence
is hunted hardest [E4-26]. **A "no" verdict is a fully successful run.**

**Stated plainly, first, because the mandate deserves it: AXR pays no dividend and has not
since fiscal 2008.** The 10-K's own words: *"The Company has paid no cash dividends on its
common stock since fiscal year 2008."* Current yield **0.00%**. On the operator's stated
mandate this name is disqualified before any gate opens. Everything below is about whether
it is a good business at a good price, which is a different question and is answered
separately.

**Two corrections to the brief, against the filings (the text wins):**
1. **The land bank is ~16,200 acres, not "17,000+".** Filed Item 1: *"the Company owned
   approximately 16,200 acres in Sandoval County, New Mexico,"* of which ~15,300 is
   undeveloped. 17,000 was the FY2023 figure; the series is 18,000 (FY2019 and FY2021),
   17,000 (FY2023), 16,600 (FY2025), 16,200 (FY2026).
2. **Karabots control ended in March 2022 and no Karabots holding remains.** The 2023
   DEF 14A (acc. 0001104659-23-086818) discloses that the Company bought **2,096,061
   shares, 28.6% of itself, from the Estate of Nicholas G. Karabots and affiliates at
   $10.45 against an $11.47 market close, for $21,903,837.45.** An EDGAR full-text search
   of AMREP filings 2023-2026 returns one hit for "Karabots," that proxy. The control
   block today is **Russo 24.3% (director), Dahl 18.8%, Robotti 9.8% (director) = 52.9%.**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- **USD 30-year: 5.19% · 2026-08-27 · FRED DGS30**, fetched directly from
  `fredgraph.csv?id=DGS30` (the operator-directed route; `tools/sources.py` USD bypassed).
  FRED's one-to-two-day lag noted, immaterial. Earnings currency is USD without
  qualification: the 10-K states *"The Company has no foreign sales."*
- FX: none. Quote currency = reporting currency = USD.
- Price: **$23.08, NYSE close 2026-08-28** (Yahoo chart API, **aggregator, live quote
  only, flagged**).

**Market capitalisation, verified against filed shares as tasked:**
**5,324,849 shares** (10-K cover, as of 2026-07-20) x **$23.08** = **$122,897,515 ≈
$122.9M**, against the sweep's ~$124M: a **0.9% gap. Verified.**
Independent corroboration from the filing: the 10-K cover reports non-affiliate market
value of **$82,217,793 at 2025-10-31**, which on ~3.3M non-affiliate shares implies
~$25/share then, consistent with the aggregator series.
**Book value $140,743,000 / 5,324,849 = $26.43/share. Price/book 0.87x.**

**Liquidity and spread friction for a $2,750 order, stated explicitly [E3-67]:**
$2,750 buys **119 shares**. That is about **1.3% of the median day** over the last month
(observed median 9,000 shares; filed 30-day average to 2026-04-30 was **13,210
shares/day**), so order *size* is not the constraint. The constraint is the book: the
observed **mean intraday high-to-low range is 3.0%**, eight of twenty-three sessions
exceeded 4%, and the thinnest observed session traded **900 shares** in total, on which
119 shares would have been 13% of volume. The 10-K says it in its own words: *"The
Company's common stock is often thinly traded. As a result, large transactions in the
Company's common stock may be difficult to execute in a short time frame and may cause
significant fluctuations in the price."* **237 holders of record**; three holders own 52%.
Honest expectation: **1% to 3% each way, $55 to $165 round-trip on $2,750**, against
[E3-67]'s stated *"3 percent per annum"* benchmark for management plus in-and-out costs.
**Limit orders only. A market order in this name is a donation to the other side.**

**The filing was read, not tagged data [E3-27, E4-14]:**
1. **FY2026 Form 10-K, filed 2026-07-24, accession 0001104659-26-086659** (year ended
   2026-04-30; auditor Rosenberg Rich Baker Berman, P.A.) — [x] MD&A in full
   [x] cash-flow statement including its detail lines [x] **all fifteen footnotes**
   (policies Note 1; real estate inventory Note 2; investment assets Note 3; accounts
   payable Note 5; **notes payable Note 6 read in full for terms [E3-52]**; revenues and
   customer concentration Note 7; cost of revenues Note 8; benefit plans Note 11;
   **income taxes Note 12**; commitments, warranty and litigation Note 13; EPS Note 14;
   segments Note 15). Item 1 Business, Item 2 Properties, Item 3, Item 5.
   **Item 1A Risk Factors is omitted** under the smaller-reporting-company election.
2. **DEF 14A, filed 2026-08-04, accession 0001104659-26-090418** — ownership, directors,
   Summary Compensation Table, audit fees, 2026 Equity Plan proposal.
3. 8-K 2026-07-24, accession 0001104659-26-086664 (Item 2.02, FY2026 results release);
   8-K 2026-07-14, accession 0001104659-26-083522 (Item 5.02, FY2027 officer pay).
4. DEF 14A 2023, accession 0001104659-23-086818 — the Karabots transaction only.
5. FY2025 / FY2023 / FY2021 / FY2019 10-Ks — acreage and trading-volume lines only, to
   build the units series.
6. Peer filings via SEC XBRL companyfacts: FOR, JOE, GRBK, STRS, MLP.
- **No 10-Q exists after the 10-K.** FY2027 Q1 ended 2026-07-31; the prior-year Q1 10-Q
  was filed 2025-09-09, so the next filing is due ~2026-09-09. The FY2026 10-K is the
  latest financial filing. Ladder rung not blocked; the document does not yet exist.
- **Figure cross-checked against the filed statement:** FY2026 operating cash flow. The
  filed Consolidated Statements of Cash Flows reads **"Net cash provided by operating
  activities ... 12,878"**; the MD&A cash-flow table reads **12,878**; XBRL companyfacts
  (CIK 0000006207) reads **12,878,000**. Three-way match. Second check: FY2025 OCF
  **10,242**, matching in all three places.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics, in my own words, without management's language.** AMREP owns roughly
  16,200 acres of high-desert ground in and around Rio Rancho, New Mexico, a city of
  114,000 that its predecessor platted and began selling in the 1960s. Almost all of that
  ground sits on the books at a sixty-year-old cost, and part of it at less than that
  after pre-2013 write-downs. Each year the company takes twenty or thirty acres of it
  through entitlement and infrastructure (zoning, roads, utilities, drainage, amenities),
  turning raw ground that changes hands at $5,000 to $10,000 an acre into finished
  residential lots that sold for **$820,000 an acre** in FY2026, and sells them to three
  homebuilders. A quarter of the gross development cost comes back through public
  improvement districts, private infrastructure covenants and impact-fee credits: **$2,375
  thousand of $10,504 thousand, 23%, in FY2026**. It also builds about sixty-five houses a
  year itself at a 24% gross margin, runs a small landscaping crew for the same builders,
  leases twenty-eight unsold houses to tenants, and earns interest on a $52.7M pile of
  cash and Treasuries. Fifty-two employees. Profit is (finished-lot price less development
  cost less a near-zero land basis) times acres converted, plus the homebuilding margin,
  less $9.0M of general and administrative expense, plus $1.7M of interest income. There
  is no debt: total liabilities are **$4,035 thousand against $140,743 thousand of
  equity**, and the only borrowing outstanding is an $18 thousand tractor loan.
- **The scarce input the business controls:** entitled, contiguously owned, infrastructure-
  served land inside one growing metro's path of growth, carried at 1961 cost. That is a
  genuinely scarce input and the company genuinely controls it. It is also a **stock, not
  a flow**, and it is being consumed. That fact is recorded here and it decides Q2.
- **Will the fundamentals look broadly the same in ten years?** Yes, and that is unusually
  easy to say. Two segments, one county, one currency, no debt, no derivatives, no
  goodwill, no acquisitions, no pension since FY2024, no off-balance-sheet arrangements,
  no non-GAAP measures anywhere in the filing, and twenty-three to forty-five years of
  inventory in the ground. This is among the simplest businesses on a US exchange.
- **The [E5-34] forecastability question, asked as the brief demands.** *"We first have to
  decide whether we can sensibly estimate an earnings range for five years out, or more.
  If the answer is yes, we will buy the stock ... If, however, we lack the ability to
  estimate future earnings — which is usually the case — we simply move on."* The **level**
  of any given year is lot-closing noise: developed residential acres sold went 28.6 to
  16.8 in one year, land sale revenue $25.6M to $20.6M, and management says outright that
  FY2027 developed residential land revenue will be **lower** again. But a **range** is
  estimable, and that is what [E5-34] asks for. Operating cash flow has run $6.4M to
  $15.5M across five years around a mean of $11.1M, from a business with no debt, a 61%
  land gross margin, and decades of inventory. [E3-55] scopes this exactly: *"If we have a
  business about which we're extremely confident as to the business result, we would prefer
  that it have high volatility than low volatility."* The mechanism here is certain and
  simple; only the timing of closings bounces. **UNKNOWABLE would be the wrong verdict at
  Q1**, and the width goes where the framework puts it, into Q4's range.
- **VERDICT: [x] IN.** The business is understandable to the point of transparency. What it
  lacks is not intelligibility.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** — builders in Rio Rancho need finished lots.
- Not price-regulated **[x]**.
- **No close substitute [ ] — FAILS, on the subject's own filings and on its own market
  share.** The 10-K: *"The Company competes with other owners and developers of land that
  offer for sale developed and undeveloped residential lots and sites for commercial and
  industrial use."* And on the homebuilding half: *"The housing industry in New Mexico is
  highly competitive. Numerous national, regional and local homebuilders compete for
  homebuyers on the basis of location, price, quality, reputation, design and community
  amenities. This competition ... could reduce the number of homes the Company delivers or
  cause the Company to accept reduced margins to maintain sales volume."*
- **Must the moat be continuously rebuilt? [E4-04].** This is the deciding test and the
  answer is on the page. AMREP's advantage is a **depleting asset**, which is [E4-04]'s
  named excluded class, the one whose *basis must be periodically replaced*. The framework's
  own scope note asks whether the spending *"defend[s] the same advantage, or buy[s] its
  replacement"* and names Mitsui's Rhodes Ridge as the disqualifying case. AMREP's
  development spending defends the same acres, which is the strongest argument in its
  favour and it is recorded honestly; but when the acres are gone the company must buy a
  replacement deposit, and the company says so itself: *"The continuity and future growth
  of the Company's real estate business ... will require that the Company acquire new
  properties in New Mexico or expand to other markets to provide sufficient assets to
  support a meaningful real estate business."* The clock is long, not absent.
- **Primary moat metric, filing-sourced, and its trend: land sale gross margin 61%
  (FY2026), 52% (FY2025).** That is the cost advantage, and it is real. Against it, the
  physical series.

**THE UNITS TEST [E4-55] — the honest series, because dollars flatter and units do not:**

| | FY2019 | FY2021 | FY2023 | FY2025 | **FY2026** |
|---|---|---|---|---|---|
| acres owned, Sandoval County (filed) | ~18,000 | ~18,000 | ~17,000 | ~16,600 | **~16,200** |
| Rio Rancho new single-family starts (filed) | | | | 973 | **805** |
| developed residential acres sold | | | | 28.6 | **16.8** |
| land sale revenue | | | | $25.6M | **$20.6M** |

Net depletion is ~360 acres a year, a ~45-year bank; gross sales of 587 to 719 acres a
year with no replacement is a **23-to-27-year** bank. Starts in its home market fell 17%
in one year and the company guides developed residential land revenue lower again.
**Direction [E4-32]: narrowing on every physical axis.**

**THE COMMODITY DOCTRINE [E2-58], and its one exception tested properly.** The equation is
*"persistent over-capacity without administered prices (or costs) equals poor
profitability,"* and the one exception is *"a cost advantage that is both **wide and
sustainable** ... By definition such exceptions are few."* Both words get tested:
- **Wide: YES, and measured.** AXR's land gross margin of **61%** against Forestar's
  **21.9%** company gross margin is a ~39-point advantage, and it exists for exactly the
  reason the framework would predict: the merchant developer pays today's price for raw
  land and AMREP paid 1961's. St. Joe, the other legacy-basis landholder in the row, runs
  43.1%. The advantage is not imaginary.
- **Sustainable: NO.** It is a stock with a 23-to-45-year clock on it, and the clock has
  been running visibly for seven years. **The [E2-58] exception fails on its second word,
  which is where it usually fails.**

**THE COMPETITOR ROW [E3-28]** — five listed comparables, each from its own latest audited
fiscal year via SEC XBRL. Full table and sources in the evidence pack.

| same metric | **AXR** FY2026 | FOR FY2025 | JOE FY2025 | GRBK FY2025 | STRS FY2025 | MLP FY2025 |
|---|---|---|---|---|---|---|
| ROE, latest FY | **7.6%** | 10.0% | 15.5% | **18.0%** | 6.0% | (31.9%) |
| ROE, prior FY | 10.3% | 13.7% | 10.5% | 26.1% | 1.0% | (21.8%) |
| gross margin | **40.5%** (land 61%) | 21.9% | 43.1% | 30.5% | n/d | n/d |
| liabilities / equity | **0.03x** | 0.77x | 0.97x | 0.32x | 1.06x | 0.45x |
| price / book | **0.87x** | 0.83x | 5.00x | 1.70x | 0.74x | 9.47x |

- **Peers named: 5**, all the listed US land-development and legacy-landholder comparables
  this run could find. AXR's *local* competitors are private and the subject does not name
  them, so the row cannot show Sandoval County share. **[E3-61]'s limit is stated: the row
  shows position, it cannot show conduct.** **No moat class is claimed that would need the
  missing private rows**, so PROVISIONAL does not arise; the verdict rests on the subject's
  own filed concessions plus the share arithmetic below.
- **The share arithmetic, which is what actually decides criterion (2).** FY2026 developed
  residential land sold: **16.8 acres**. At Rio Rancho densities of roughly five to seven
  lots per acre that is on the order of **85 to 115 lots** into a market with **805 new
  single-family starts**: about **10% to 14%**. AMREP's own homebuilder closed **65 homes,
  8% of starts**. *In the town its predecessor platted, AMREP supplies roughly one new lot
  in eight, and the other seven come from the substitutes the 10-K acknowledges but does
  not name.* (The lots-per-acre figure is this run's estimate and is labelled as one; the
  answer does not turn on it, since even ten lots per acre gives under 21%.)
- **The two-characteristic test [E2-44]: 0.5 of 2.** (1) Raise prices when demand is flat
  and capacity underutilised? Developed residential revenue per acre rose $766K to $820K,
  but the company attributes it verbatim to *"the location and mix of land sold"* and in
  the same MD&A says it *"provided sales incentives on certain homes, reduced the sale
  prices of certain homes, reduced the size of lots and homes."* Half credit at best.
  (2) Grow dollar volume with only minor additional capital? **No growth at all**: revenue
  $58.9M (FY2022) to $52.8M (FY2026), down 10% over four years, while equity grew 69% and
  real estate inventory sat flat at $66.6M. The capital went into Treasuries.
- **The dominance test [E2-53]:** *"Once dominant, the newspaper itself, not the
  marketplace, determines just how good or how bad the paper will be."* AMREP's own MD&A
  attributes its results to *"material delays in municipal entitlements, infrastructure
  availability, approvals and inspections, contractor schedules and utility response
  times"* and to affordability. **Position does not carry it; the marketplace and the city
  hall do.** That is the opposite of the dominance class.
- **Untapped pricing power [E3-33, E5-28]:** claiming this class claims *"a monopoly or a
  near monopoly."* A ten-percent supplier selling to three buyers who can buy land from
  anyone has none.
- **The attacker's test [E2-45]:** with ample capital and skilled people, competing is
  straightforward. Buy raw Sandoval County acreage at $5,000 to $10,000 an acre, which the
  subject's own filed sales prove is available, and entitle it. The barrier is the city's
  approval queue, which AMREP's MD&A says is getting *worse for AMREP too*. The advantage
  is a sunk cost paid in 1961, not a wall a new entrant cannot climb.
- **The second question about the business is a number [E3-46]:** *"the best businesses, by
  definition, are going to be businesses that earn very high returns on capital employed
  over time."* AXR earns **7.6%** on equity, **12.9%** as a five-year mean, and roughly
  **10% to 11.5%** on the equity actually employed once the cash is stripped out. Good.
  Not very high, and below three of the five peers.
- Class: **[x] NONE.** A wide but depleting cost position in one metro, held by a
  ten-percent supplier of its own home market, earning a good-not-great return on capital,
  with the physical series shrinking on every line.
- **VERDICT: [x] OUT.** Under [E3-03] a franchise's customers must believe it has no close
  substitute; AMREP's own 10-K names the substitutes, its own numbers show it supplying
  roughly an eighth of its home market, the two-characteristic test scores 0.5 of 2, the
  moat's basis is a depleting asset and therefore [E4-04]'s excluded class, and [E2-58]'s
  wide-and-sustainable exception fails on "sustainable." **What is here is not a franchise.
  It is a cheap asset, which is a different book, and the hard sequence closes the entry
  file at this gate. [E5-13]: most names should end here, and that is the system working.**

---
⛔ **Q3, Q4 and Q5 do not open for entry.** Q1 IN · Q2 OUT. The hard sequence closes the
file for any BUY decision. No position exists, so no [E2-28] hold read is required.
Everything below is **FOR THE RECORD** because the operator tasked this run with the asset
basis, the quantified deaths, the proxy read and Q6 regardless. **Everything below sits
under operator rule 3's header. Nothing below is entry language.**

---
## Q3 — FOR THE RECORD: ARE THEY HONEST, AND ARE THEY RATIONAL?
*Standard applied: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Q2 OUT stands regardless;
Q3 can stop a run, never start one.*

**STEP 1 — THE WEIGHT CASE, declared first.**
- [ ] **Daily execution [E3-38]** — LOW. This is close to the purest have-to-be-smart-once
  business on the exchange. The decisive act was buying the land in 1961. Entitlement work
  and cost-to-complete budgeting need competence, not daily brilliance, and a bad year
  costs a few million against a $140.7M balance sheet.
- [ ] **Control [E1-16]** — no. A minority stake in a listed company, exitable.
- [ ] **Leverage [E3-29]** — LOW to the point of absence. **Total liabilities $4,035
  thousand against $140,743 thousand of equity: 2.9%.** Debt outstanding is $18 thousand.
  The revolver is undrawn. There is no magnification of any managerial act.
**All three low → Q3 is a QUALITATIVE OVERLAY.** A mediocre manager here is survivable and
price does the work. Recorded per the standard; it does not stop the run and it cannot
start one.

**Honesty, the binary [E5-16], filings-based, each matter dated to when it became public.**
**No disqualifier found.** The sweep, named so the absence claim is bounded: Item 3 Legal
Proceedings discloses only *"various pending or threatened claims and legal actions
arising in the ordinary course of business"*; Note 13 states *"The Company has not accrued
any amounts related to litigation matters as of April 30, 2026 or April 30, 2025."* No
restatement, no error correction (both cover-page boxes unchecked), no SEC enforcement, no
related-party transaction in the FY2026 proxy, no unrecognised tax benefits, no accrued
interest or penalties. Worded per the absence-claim rule: **no instance found in the
documents read, not "none exists."**

**STEP 2 — THE FLAGS [E4-22, E4-29, E5-15, E4-30, E2-49, E2-52, E3-53].**
- [ ] **Weak accounting — NOT fired on substance, but two prompts to read.** Substance is
  clean: stock compensation expensed in full, no goodwill, no capitalised interest ("No
  interest was capitalized in real estate inventory in 2026 or 2025"), only $99 thousand of
  capitalised property taxes, lower-of-cost-or-net-realisable-value on investment assets,
  the defined benefit pension terminated and annuitised in FY2024, an unclassified balance
  sheet properly justified by the operating cycle, and an unqualified opinion. The two
  prompts: **(a)** the auditor changed from **Baker Tilly US, LLP to Rosenberg Rich Baker
  Berman, P.A.** in 2024, the FY2026 audit fee is **$120,000**, there is **no ICFR auditor
  attestation** (permitted for a smaller reporting company), and the report states
  *"We determined that there were no critical audit matters"* for a filer whose single most
  judgmental estimate is the allocation of common development costs across parcels by
  relative sales value. A $120,000 audit and zero CAMs is thin cover for exactly the
  estimate that could be wrong. **(b)** **Item 1A Risk Factors is omitted entirely.** Both
  are legal; both mean the reader is told less than the reader would want. Prompts, not
  verdicts.
- [ ] **Unintelligible footnotes — NOT fired.** The opposite. The notes are short, plain
  and quantified, and the reimbursement mechanisms are broken out line by line.
- [ ] **Trumpeted projections [E4-22, E3-48, E5-30] — NOT fired, and the reverse is on
  record.** The Company issues **no guidance**, holds **no earnings call**, and the one
  forward statement in the MD&A is **negative about itself**: *"This is expected to result
  in a reduction of revenues from the sale of developed residential land during fiscal year
  2027 as compared to 2026."* It adds *"The Company's past performance may not be
  indicative of future results."* Against [E2-26]'s half-owner test this is the candor
  pole. There is no [E3-48] guidance ledger to build because there has never been guidance.
- [ ] **Serial share issuance [E5-15] — NOT fired, and the reverse.** Shares issued went
  **8,358,154 (FY2020) to 5,305,199 (FY2026), down 36.5%.** The bulk was the March 2022
  purchase of **2,096,061 shares, 28.6% of the company, from the Karabots estate at $10.45
  against an $11.47 close and roughly $14.35 of book**, for $21.9M. Both [E5-08] conditions
  were plainly met and the company acted at scale, which is [E4-50]'s aggressive case
  practised. Ongoing issuance is ~17,000 to 19,000 restricted shares a year to two officers
  plus director deferred stock units.
- [ ] **EBITDA and adjusted-measure promotion [E4-29] — NOT fired.** There is no non-GAAP
  measure anywhere in the 10-K or the results 8-K cover. Nothing to restate, nothing to
  reconcile, nothing deleted from the income statement.
- [ ] **Filed-figure tells [E4-30] — NOT fired.** Reported growth is visibly lumpy, which
  is the opposite of the fraud tell: net income $15.9M, $21.8M, $6.7M, $12.7M, $10.3M
  across FY2022-26. Cash taxes paid net of refunds were **$502 thousand on $14,126 thousand
  of pretax income, 3.6%,** against a 27.0% effective rate; the gap is **fully explained**
  by the disclosed $20,620 thousand federal NOL carryforward and reconciled in Note 12.
  **Recorded as explained, not as a tell.**
- [ ] **Metric-switching [E2-49] — not applicable.** No headline metric exists to switch.
- [ ] **Dividends funded by issuance [E2-52] — not applicable.** No dividends at all.
- [ ] **Restructuring-charge management [E3-53] — NOT fired.** *"The Company did not record
  any non-cash impairment charges on real estate inventory or investment assets in 2026 or
  2025."*
- **Convergence [E4-52]:** the flags do not converge. On the accounting and disclosure axis
  this is one of the cleaner small-cap filings this framework has read. The one live flag
  is capital allocation, below, and it points in a direction none of the others do.

**STEP 3 — THE PRIMARY TEST [E2-01], scoped by [E2-47] and [E2-43].** Balance sheet first
[E5-27]. There is no leverage and no goodwill, so book equity **is** the unleveraged
net-tangible-asset denominator; the scoping carve-outs do not bite. The series:

| FY | 2021 | 2022 | 2023 | 2024 | 2025 | **2026** | 5-yr mean |
|---|---|---|---|---|---|---|---|
| ROE (NI / avg equity) | 8.5% | 18.4% | 22.4% | 5.8% | 10.3% | **7.6%** | **12.9%** |
| ROE on avg equity **ex cash** | 11.3% | 24.1% | 27.5% | 7.5% | 14.2% | **11.5%** | 16.9% |

**The finding is the gap between the two rows.** The operating business earns about
**10% to 11.5%** on the capital actually in it, which is respectable and near [E5-40]'s
*"quite satisfactory"* mark. The consolidated figure is dragged to **7.6%** because
**36% of assets, $52.3M, sits in cash and Treasuries**. That is a capital-allocation
result, not an operating one, and the framework's [E2-73] instruction to pick the
denominator by the question asked is why both rows are printed.

**The half-owner test [E2-26].** Mostly passes and passes well: reimbursements broken out,
segment profit given, per-acre realisations given for every category, the bulk sales named
and explicitly flagged as non-recurring, the negative FY2027 expectation volunteered.
Where it falls short is what is **absent** rather than misstated: no risk factors, no split
of the land carrying value between developed lots and the 15,300 undeveloped acres (the
single number an owner most wants), no water-rights disclosure, no mineral-rights carrying
value or lease income, and no explanation anywhere of why $52.3M is being held.

**The institutional imperative, scored [E2-30].** *"Institutional dynamics, not venality or
stupidity."*
- [x] **Resists any change in current direction** — partially fired. The company has done
  the same thing since 1961, and the MD&A confirms it *"reduced the number and scope of its
  active land development projects and delayed proceeding with certain new land development
  projects."*
- [ ] **Projects or acquisitions materialise to soak up available funds** — NOT fired.
  Emphatically the reverse, and that is the problem, below.
- [ ] **Staff studies to justify the leader's craving** — no evidence; 52 employees, no
  consulting line, no banker-led transactions.
- [ ] **Peer behaviour mindlessly imitated** — not fired.

**Capital allocation — the two buyback conditions [E5-08], with the third [E4-31].**
- **(1) Ample funds for operations and liquidity?** Overwhelmingly yes, and the company
  says so: *"The Company believes that it has adequate cash and cash equivalents, bank
  financing and cash flows from operations to provide for its anticipated spending in its
  fiscal year ending April 30, 2027."* $52.7M of cash and Treasuries, $4.0M of liabilities,
  an undrawn revolver.
- **(2) Repurchases at a material discount to conservatively calculated intrinsic value?**
  In March 2022 the answer was a resounding yes and the company acted: 28.6% of itself at
  $10.45 against $14.35 of book. **Since then, nothing.** Repurchases FY2023 through FY2026:
  **zero.** Dividends: zero since fiscal 2008. Cash has gone **$15.7M (FY2022) to $52.3M
  (FY2026), plus $36.6M**, while the stock trades at **0.87x a book value that this run
  argues, and management knows better than this run, is understated.** That is [E2-51]
  precisely: *"A manager who consistently turns his back on repurchases, when these clearly
  are in the interests of owners, reveals more than he knows of his motivations."*
- **CAPITAL ALLOCATION FLAG — FIRED**, stated with the humility clause [E4-13]: *"it is
  natural for CEOs to be optimistic about their own businesses. They also know a whole lot
  more about them than I do."* Management may be holding cash for a land acquisition, for
  the entitlement-delay environment it describes, or for a housing break in which land can
  be bought cheaply, and [E2-74] endorses exactly that: *"our major parking place for money
  is medium-term tax-exempt bonds ... Mr. Market will offer us opportunities."* Four years
  and $36.6M is a long park with nothing announced. **Both readings are recorded. The flag
  binds position size only, never the discount rate.**
- **The retention test [E3-54], run.** Retained earnings $54,828 (2022-04-30) to $106,312
  (2026-04-30) = **$51.5M retained**. Market value $67.4M (2022-04-30, 5,240,309 shares at
  $12.86, aggregator, flagged) to $122.9M today: **+$55.5M, i.e. $1.08 of market value per
  $1 retained.** Measured to the April 2026 peak instead: $1.53. **Passes, thinly, and both
  endpoints are published because [E4-38] requires it.**
- **Book value per share, every window [E4-38]:** 7-yr **13.8%**, 5-yr **16.9%**, 4-yr
  **13.7%**, 3-yr **7.9%**, 2-yr **8.8%**, 1-yr **7.9%**. The long windows are carried by
  the Karabots buyback. **The current rate of compounding is about 8%.**

**Compensation and conduct.** CEO Vitale, in the seat since 2017, total FY2026 compensation
**$734,100**, which is **7.1% of net income**; CFO Uleau $313,100. Two named officers,
$1,047,200 combined, **10.2% of net income**, in a company that earns $10.3M. No non-GAAP
metric drives it, there is no long-term incentive plan with adjustable yardsticks, and the
FY2027 raise (announced 2026-07-14) takes salaries to $395,000 and $205,000. Vitale owns
125,900 shares (2.4%) plus an option over 50,000 shares becoming exercisable 2026-11-01.
Audit fees $120,000. Against [E3-37]: *"pay able people well, but abhor having a bigger
head count than is needed"* is met at 52 employees; the third test, *"attack costs as
vigorously when profits are at record levels as when they are under pressure,"* is the one
that scores badly: **G&A rose 24% to $9,025 thousand, 17.1% of revenue, on 6% revenue
growth**, in a year when net income fell 19%.

**Owner orientation.** Two of the three blocks above 5% sit on the board: Russo at 24.3%
since 1996 and Robotti at 9.8% since 2016, the latter a professional value investor.
Directors and officers own **37.4%**. Shares were bought, not granted. The January 2026
addition of Timothy McNaney, co-founder of a leading private New Mexico homebuilder, is a
relevant and un-showy hire. **Set against that, the structure:** a classified board plus
Oklahoma anti-takeover provisions which the company describes in its own Item 5 as meaning
*"the concurrence of the Company's largest shareholders would generally be needed for any
'interested shareholder' to acquire control of the Company, even if a change in control
would be beneficial to the Company's other shareholders."* The filing says the quiet part.
For a stock at 0.87x an understated book, the takeover-proofing is the mechanism by which
the discount persists.

**THE GUARDRAIL — checked before the verdict.**
- [x] Confirmed: **nothing in this Q3 is being used to promote the name.** Q2 OUT stands.
  A disciplined, honest, owner-aligned management cannot repair a depleting cost position
  [E2-37, E2-38, E3-39]. *"a textile company that allocates capital brilliantly within its
  industry is a remarkable textile company — but not a remarkable business."*
- [x] No key-person moat is claimed, so nothing needs relocating to Q2 as a defect [E4-23].
- [x] Is a great manager the reason to act? **No.** There is no excisable cancer and no
  Pygmalion plan [E2-35, E2-36]. There is a good business earning ~10% on its operating
  capital with 36% of the balance sheet parked.

- **Q3 FOR-THE-RECORD READ: no honesty disqualifier found; Q3 is an overlay and it does not
  change the Q2 verdict.** On disclosure and accounting this filer scores better than most
  names this framework has run: no guidance, no non-GAAP, no goodwill, no leverage, no
  impairments, expensed comp, plain notes, a volunteered negative outlook, modest pay, and
  a genuinely excellent 2022 repurchase. **One flag is live and it is the one that matters
  for a minority holder: four years of accumulating cash with no repurchase and no dividend
  while the stock sits below an understated book, inside a takeover-proof structure the
  company itself describes as blocking a change of control that would benefit other
  shareholders.** *A pass here would be the absence of found disqualifiers, never a
  clearance [E5-17]; and IN never promotes.*

## Q4 — FOR THE RECORD: WILL IT SURVIVE?

### Owner earnings — **COMPUTATION — NOT A CLEARANCE** [E2-23]
Convention: multi-year mean of (operating cash flow less stock compensation) less (c).
Both the corpus default window and a longer one are shown [E2-42, E4-25]; the spread is
carried, not resolved by preference.

**THE (c) JUDGMENT, DISCLOSED, AND WHY THE CORPUS DEFAULT IS INVALID HERE.** [E3-44] and
[E2-41] make depreciation the default proxy for (c). **That default is invalid for this
company for the same structural reason [E5-20] invalidates it for railroads.** AMREP's
depreciation of **$312 thousand** covers office equipment and twenty-eight rental houses.
The asset that actually gets consumed to produce the earnings is **land**, and land is not
depreciated. Meanwhile the land *development* spending is already inside operating cash
flow, because real estate inventory changes run through operating activities: the FY2026
statement shows real estate inventory as a **$361 thousand source**, so the company spent
on development and acquisition roughly what it relieved in cost of sales. **Operating cash
flow therefore already nets the development capital. What it does not net is the land the
company is consuming and not replacing.** The units series is unambiguous: 18,000 acres
(FY2021) to 16,200 (FY2026), **~360 acres a year of net depletion**. That is the true (c):
the cost of buying 360 acres a year to hold unit volume constant. Priced at the company's
own filed realisations for undeveloped acreage, $4,655 to $10,218 an acre, that is **$1.7M
to $3.7M a year**, to which about $0.3M of property-and-equipment maintenance is added.
**(c) is judged at $2.0M to $4.0M, a disclosed guess per [E2-23]'s "(c) must be a guess."**
The reported-depreciation end of the band is refused in writing.

| window | OCF mean | SBC mean | OCF less SBC | (c) = $2.0M | (c) = $4.0M | yield on $122.9M |
|---|---|---|---|---|---|---|
| **5-yr FY2022-26** (corpus default [E2-42]) | $11.14M | $0.33M | $10.81M | **$8.81M** | **$6.81M** | 7.2% / 5.5% |
| **7-yr FY2020-26** | $9.87M | $0.27M | $9.60M | $7.60M | $5.60M | 6.2% / 4.6% |
| 3-yr FY2024-26 | $11.28M | $0.40M | $10.88M | $8.88M | $6.88M | 7.2% / 5.6% |

- Owner earnings by year at (c) = $3.0M: $(2.4)M (FY2020) · $9.5M (FY2021) · $12.3M
  (FY2022) · $3.2M (FY2023) · $7.4M (FY2024) · $6.8M (FY2025) · $9.4M (FY2026).
- **Combined range: $5.6M to $8.9M. Round: $5.5M to $9M.**
  **Spread at the conservative end: 7-yr $5.60M vs 5-yr $6.81M, a 22% window spread.**
- **Is the range too wide to reach a conclusion [E4-25]? No.** A 1.6x band on a business
  with no debt and 36% of assets in Treasuries is workable. The width is [E3-55]'s
  benign kind: the mechanism is certain and the closings bounce.
- **The distorted year, named [E5-11]:** FY2020 (OCF $765 thousand, net loss $5.9M) sits in
  the seven-year window and is the pandemic-and-transition year in which the company was
  still shedding its former media businesses. It is kept, not excised, because excising it
  would be the [E4-38] terminal-date sin in reverse.
- **Normalised DOWN for luck [E4-41]:** FY2026 land sale gross margin of **61%** is nine
  points above FY2025's 52%, and the company attributes the difference to *"changes in
  public improvement district reimbursements, private infrastructure covenant reimbursements
  and payments for impact fee credits and the location, size and mix of property sold."*
  Those reimbursements were $2,375 thousand, 23% of gross land cost, and are lumpy by
  nature. FY2026 is a favourable-mix year and the mean, not FY2026, is used.
- **Stock compensation subtracted in full [E5-06]**; the reported charge is used. Per
  [E3-70] the market-value measure is the standard where SBC is material; at $447 thousand,
  0.85% of revenue and 0.36% of the market cap, it is not material and the reported charge
  is accepted, with the substitution named.
- No look-through increment [E3-04]: there are no equity-method or unconsolidated investees.
- **The enterprise framing, which is the informative one here.** $52,327 thousand of the
  market cap is cash and equivalents against $18 thousand of debt, so the operating business
  is priced at **$70.6M**. Interest income of $1,734 thousand pretax, about $1,266 thousand
  after tax, is inside the owner-earnings figures above and belongs to the cash, not the
  land. **Operating owner earnings $4.3M to $7.6M against a $70.6M enterprise value =
  6.1% to 10.8%.**
- **Bottom boundary [E5-34]: owner earnings ~$5.5M to $6.5M**, i.e. **4.5% to 5.3% on the
  market cap** and **6.1% to 7.5% on the enterprise value**, against the **5.19%** sovereign.

### The asset basis, worked as the brief directs [E3-71]
*Munger's Wesco form: liquidating value plus the identifiable advantages, with the analyst
printing his own estimate against his own quote.*

**Floor.** Book equity **$140,743 thousand = $26.43/share**, of which **$52,689 thousand,
$9.89/share, is cash and US government securities**, against **$4,035 thousand of total
liabilities**. This floor is unusually hard: there is no goodwill to write off, no
leverage to wipe it out, no pension, and no off-balance-sheet arrangement. **The market
cap of $122.9M is 87% of it.**

**The understatement, bounded conservatively.** All land-carrying lines together are
**$63,325 thousand** (land inventory $54,843 + land held for long-term investment $8,482),
and that single figure covers **217 developed residential lots, 68 developed
commercial/industrial acres, 358 acres under development, and roughly 16,500 undeveloped
acres.** The filing does not split it, which is this run's largest single UNRESEARCHED gap.
The bound below assumes the **entire** $63,325 belongs to the 15,300 undeveloped acres,
which it does not, and which therefore values the developed lots at zero:

| undeveloped acres marked at | implied value | markup over all land book | adjusted equity | per share |
|---|---|---|---|---|
| $4,655/acre (the FY2026 **bulk sale**, filed) | $71.2M | +$7.9M | **$148.6M** | **$27.91** |
| $7,581/acre (FY2025-26 blended undeveloped realisation) | $116.0M | +$52.7M | $193.4M | $36.32 |
| $10,218/acre (FY2026 blended undeveloped realisation) | $156.3M | +$93.0M | **$233.7M** | **$43.89** |

**Counted at zero on top of that:** mineral rights under ~55,000 surface acres (no carrying
value, no lease income, no production disclosed anywhere); the 217 developed lots and 68
developed commercial acres, at FY2026 realisations of $735,000 to $820,000 per developed
acre; and the $1,127 thousand valuation allowance on state NOLs.
**Charged against it:** a 23-to-45-year monetisation timetable at 587 to 719 acres a year,
about $9.0M a year of G&A carried through it, and no distribution along the way.
**Asset range: roughly $145M to $235M gross, $27 to $44 a share, undiscounted.** Crediting
the timetable and the carry, the defensible **present-value** range is nearer
**$140M to $180M, $26 to $34 a share.**

### Great, good, or gruesome? [E4-20]
- [ ] great — [x] **good** — [ ] gruesome
**Good, at the low end, and not growing.** [E4-43] is explicit that the good class *passes*:
*"nothing shabby about earning $82 million pre-tax on $400 million of net tangible assets."*
AMREP earns about **10% to 11.5% on the capital actually employed**, near [E5-40]'s ~12%
mark. It is not gruesome: it does not consume capital at bad returns, it generates cash it
cannot deploy. But the [E4-20] savings-account test has a second clause, *"earned also on
deposits that are added,"* and that is exactly what fails here: the added deposits earn
**3.8% in Treasuries**, not 10% in land. **A good business with a bad reinvestment rate is
a good business shrinking toward the bond.**

### Staying power — score all three [E5-11]
1. **A large and reliable stream of earnings — PARTIAL.** Modest in size ($10.3M) and
   **not reliable year to year** (net income $21.8M, $6.7M, $12.7M, $10.3M in four years,
   and FY2027 land revenue guided down). Reliably **positive**: profitable every year
   FY2021 through FY2026. Per [E5-29], risk here means impairment, not price movement, and
   the volatility is timing, not solvency.
2. **Massive liquid assets — PASS, and passes as the corpus means it [E5-39].**
   **$52,689 thousand of cash and US Government Securities, 36% of assets and 43% of the
   market cap**, owned outright, with no reliance on bank lines. The $6.5M revolver is
   undrawn and is not counted as liquidity here.
3. **No significant near-term cash requirements — PASS, emphatically. This is the leg that
   usually kills and here it barely exists.** Total liabilities $4,035 thousand. Debt
   maturities: $8 thousand (FY2027), $9 thousand (FY2028), $1 thousand (FY2029). Operating
   lease payments $24 to $31 thousand a year through FY2032. Warranty reserve $386
   thousand. The only real contingent items are $1,812 thousand of loan reserves supporting
   a municipal subdivision-completion obligation and $338 thousand of cash collateral with
   municipalities.
- **The [E2-54] coverage test:** interest expense is **zero**; the company is a net
  receiver of $1,734 thousand. The test is trivially passed.
- **[E2-55], results under extraordinarily adverse conditions:** if land and home sales went
  to **zero**, $52.7M of cash against $9.0M a year of G&A funds roughly **six years** before
  a single acre must be sold. That is the standard actually met, not merely claimed.
- **Leverage, named and quantified [E4-16, E3-29]:** total debt $18 thousand; total
  liabilities to equity **0.03x**, the lowest in the competitor row by a factor of ten.
  There is no ratio ceiling in this framework and none is applied; the number is stated.

### Name the specific ways THIS business dies [E2-27, E3-24] — exposure, not experience [E4-40]
*Modelled from what the filing shows the business is exposed to, never from what has
recently happened, per [E4-40]. Written to the [E4-51] standard: a bear case a holder
should accept as fairly stated.*

1. **Single-metro, single-county, three-customer concentration (the demand death).**
   **Exposure:** 100% of the asset is in Sandoval County; **100% of FY2026 developed
   residential land sales went to three homebuilders**; one customer alone was **$8,954
   thousand, 17.0% of total revenue**. **Quantified from filed figures:** Rio Rancho starts
   fell **973 to 805, down 17%**, in one year. If starts halve to ~400 and AMREP's developed
   residential acres sold halve from 16.8 to ~8, land sale revenue falls about $6.9M and
   land segment profit at the 61% margin falls about **$4.2M, roughly 30% of FY2026 pretax
   income**, while $9.0M of G&A stays put. Two such years take the company to roughly
   breakeven. It has happened twice inside the record: net loss of **$5,903 thousand
   (FY2020)** and **$10,224 thousand (FY2016)**. **Likelihood: a real possibility,
   cyclically recurring.** Not fatal: the cash and the absent debt absorb it entirely.
2. **Water and entitlement (the death that would end the asset case).** **Exposure:** the
   filing names *"ensuring the availability of water service"* as part of what the land
   development segment does, and warns that regulations *"related to the availability of
   water may result in restrictions on land development or homebuilding in certain areas."*
   Rio Rancho draws on the declining Albuquerque Basin aquifer. **The 10-K discloses no
   owned water rights and quantifies nothing.** **Quantified only by exposure, which is the
   honest form here: 15,300 of 16,200 acres, roughly 94% of the bank, depends on water
   service and entitlement that does not yet exist.** The company already reports *"material
   delays in municipal entitlements, infrastructure availability, approvals and inspections
   ... and utility response times"* in two consecutive years. If the City of Rio Rancho or
   the New Mexico Office of the State Engineer restricts new service commitments, the asset
   case collapses to the developed and under-development inventory, roughly 400 acres, and
   the $27-to-$44 range in the asset table goes away. **Likelihood: a low-level possibility
   within five years; a real possibility across the 23-to-45-year life of the bank.**
   **This is the single largest UNRESEARCHED item in the run and it is named in Q6.**
3. **The depleting bank itself (the slow structural death, already in progress).**
   **Exposure:** 18,000 acres (FY2019 and FY2021) to 16,200 (FY2026). **Quantified:** the
   land development segment earned **$10,038 thousand of segment profit on 587.5 acres
   sold, about $17,100 of segment profit per acre consumed.** At the net rate of ~360 acres
   a year the bank lasts ~45 years; at the gross rate with no replacement, 23 to 27.
   Replacing raw acreage at the filed bulk price of $4,655 is cheap; replacing an
   entitled, in-path-of-growth acre is not, and the company's own Item 1 concedes that
   continuity *"will require that the Company acquire new properties in New Mexico or
   expand to other markets."* **Likelihood: likely, because it is happening; only the
   replacement price is open.**
4. **The trapped-capital death, and this is the one that actually costs a minority
   holder.** Not insolvency. Dilution of return. **Exposure, quantified from the filed
   record:** cash went **$15.7M to $52.3M in four years, plus $36.6M**, earning about 3.8%
   pretax inside a company whose operating capital earns about 10%; zero repurchases since
   March 2022; **no dividend since fiscal 2008**; a classified board; and Oklahoma
   anti-takeover provisions the company itself says would block a change of control *"even
   if a change in control would be beneficial to the Company's other shareholders."* At the
   FY2026 rate of $12.9M of operating cash flow against $0.1M of capital expenditure and
   zero distributions, **cash reaches roughly $100M, more than 80% of today's entire market
   capitalisation, within four years, and consolidated return on equity falls from 7.6%
   toward 5%.** **Likelihood: likely, on the four-year filed record.** This is [E4-16]
   inverted: not death by leverage, but death by the retention test [E3-54] failing quietly
   inside a structure that gives an outside holder no lever.
- **Q4 FOR-THE-RECORD READ: it survives almost anything.** All three [E5-11] legs pass and
  the third passes emphatically, which is rare. The [E2-54] coverage test is trivial and
  [E2-55]'s extraordinarily-adverse-conditions standard is genuinely met at roughly six
  years of zero-revenue survival. **The business does not die. The return does.** Were the
  gate live it would read IN on survival, with death 4 written in full beside it.

---
## Q5 — FOR THE RECORD — **COMPUTATION — NOT A CLEARANCE**
*(Q1-Q4 did not all close IN; Q2 is OUT; operator rule 3's header governs and no entry
language appears below.)*

**1. THE YIELD** (sovereign **5.19%**, FRED DGS30, 2026-08-27):

| basis | owner earnings | yield | points over sovereign |
|---|---|---|---|
| **Bottom boundary [E5-34], on market cap $122.9M** | **$5.5M-$6.5M** | **4.5%-5.3%** | **-0.7 to +0.1** |
| Full range, on market cap | $5.5M-$9.0M | 4.5%-7.3% | -0.7 to +2.1 |
| **Bottom boundary, on enterprise value $70.6M** | $4.3M-$5.2M | **6.1%-7.5%** | **+0.9 to +2.3** |
| Full range, on enterprise value | $4.3M-$7.6M | 6.1%-10.8% | +0.9 to +5.6 |
| FY2026 alone at (c) = $2.0M (best recent year) | $10.4M | 8.5% | +3.3 |

**2. WHAT THE PRICE ALREADY ASSUMES.** **$122.9M x the 10% floor = $12.3M of owner
earnings required.** The filed range is $5.5M to $9.0M and the **best single year in the
whole record** (FY2022: OCF $15.476M less SBC $0.217M less (c) $2.0M = **$13.3M**) is the
only year that clears it. On the enterprise basis the arithmetic is kinder:
**$70.6M x 10% = $7.06M of operating owner earnings** against $4.3M to $7.6M filed, so the
**top of the band clears and the mean does not.** What the price also assumes is that the
0.87x book multiple is either justified or will close; and per [E4-44], *"the value of an
asset, whatever its character, cannot over the long term grow faster than its earnings
do,"* so multiple closure is a one-time term, not a growth rate. **The ceiling [E2-63] is
stated:** with retained capital going into Treasuries at 3.8% rather than into land at
10%, the compounding rate is bounded near the recent book-value growth of **~8%**, not the
16.9% five-year figure the buyback produced and which cannot repeat at these prices.

**3. WHAT YOU ARE PAID.** **-0.7 to +0.1 points over the sovereign at the bottom boundary
on the market cap, +0.9 to +2.3 points on the enterprise value.** In plain terms: at
$23.08 you are paid roughly the long bond, plus $9.89 a share of cash you do not control,
plus an option on 15,300 acres whose price you cannot compute from the filing.

**THE FLOOR VERDICT, stated plainly [E4-28].** *"That's the figure we quit on ... whether
short rates are 6 percent or whether short rates are 1 percent."* Honest pre-tax
expectancy at $23.08: the earnings yield is **4.5% to 7.3%** on the cap and **6.1% to
10.8%** on the enterprise; add the ~8% current rate of book-value compounding and subtract
the fact that the compounding accrues to a book the market has discounted for four years.
**Call the honest expectancy 7% to 10%. It straddles the quit line and does not clearly
clear it.** It clears only on the enterprise framing at the top of the band, and that
framing asks you to credit yourself with cash the company has shown no intention of
distributing.

**WHICH BAR.** **[x] Screamer test [E4-01]**, for the record only. Three outcomes:

| book | conservative case | price $122.9M / $23.08 | box |
|---|---|---|---|
| **Earnings**, at the 10% quit rate | operating OE $4.3M-$7.6M / 0.10 = $42M-$77M, plus net cash $52.3M = **$95M-$130M ($18-$24/sh)** | inside | **inside the range: no useful conclusion** |
| **Earnings**, at the bare sovereign 5.19% | $81M-$148M plus cash = **$134M-$201M ($25-$38/sh)** | below | below the conservative case |
| **Asset**, present value | **$140M-$180M ($26-$34/sh)** | **below** | **below the conservative case** |
| **Asset**, undiscounted gross | $145M-$235M ($27-$44/sh) | below | below |

**The two books disagree, and the disagreement is itself the finding [E4-25].** The
earnings book says the price is fair to full once you insist on the 10% quit rate; the
asset book says the price is below a floor made largely of Treasuries and 1961 land.
**Neither reading produces a screamer.** [E3-65]'s Washington Post benchmark was *"about
20 percent of the value to a private owner"* with an aligned management; this is 87% of a
conservatively stated book with a management that has parked the cash for four years.
**It does not scream.**

**Windage count: one.** Conservatism is applied once, in the (c) band inside the bottom
boundary [E4-11]. The refusal of the reported-depreciation end of (c) is [E5-20]'s required
move, not windage; the refusal of FY2026's favourable reimbursement mix is [E4-41]'s
required move, not windage; and the asset table's bulk-sale mark is a **separate book**,
printed alongside rather than stacked on the same number.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*(No position exists. These are pre-committed yardsticks for the WATCH LIST, set prior to
any act [E1-02]. **Alert thresholds are LISTED ONLY. `tools/alerts.json` was not edited and
no shared file was touched.**)*

**THE Q2 REOPEN CONDITIONS — the only route back to an entry run. Both are required.**
1. **Evidence, not price.** Q2 failed on class, so the bar is structural, and a price move
   reopens nothing:
   - the **acreage line stops falling** for two consecutive 10-Ks, i.e. acquisitions at
     least match sales, evidencing that the cost position is being renewed rather than
     consumed; **and**
   - **return on average equity excluding cash holds at or above 12%** for two consecutive
     fiscal years, which is [E5-40]'s satisfactory mark; **and**
   - **Rio Rancho starts stop falling** and AMREP's developed-residential acres sold rise
     rather than fall, evidencing that the ten-percent share is not eroding.
2. **Price [E4-28].** The earnings book pays the 10% quit rate at roughly **$95M-$130M,
   i.e. $18 to $24 a share** with no credit for the land bank. **Below ~$19** the file gets
   re-read for the record; entry would still require condition 1, which cannot exist before
   the FY2028 10-K at the earliest.

**Thesis-confirming and thesis-breaking metrics, with thresholds (review triggers, never
auto-executions):**
- **The capital-allocation flag, which is the live one.** *Breaking:* cash and equivalents
  above **$65M** at any fiscal year end with no repurchase and no dividend = the flag
  deepening, and the FY2028 arithmetic in death 4 confirmed. *Confirming:* **any** buyback
  authorisation, tender offer, special dividend, or a disclosed land acquisition of scale =
  the single most thesis-relevant event available, and the one that would most change this
  run's reading of management.
- **The units line [E4-55].** The acreage sentence in Item 1 of each 10-K. Below **15,500
  acres** without a matching acquisition disclosure = depletion accelerating.
- **Rio Rancho starts.** The filed sentence in Item 1. A second consecutive year below
  **800** = death 1 materialising; back above **950** = the cycle turning.
- **Customer concentration.** Note 7. Two customers rather than three, or a single customer
  above **25%** of revenue, = the demand death's exposure widening.
- **Land gross margin.** Below **50%** for two years = the cheap-basis advantage being
  diluted by acquired-at-market land, which is the [E4-04] replacement problem arriving.
- **Homebuilding.** Homes sold and average selling price; homes leased to tenants rising
  above **40** = unsold inventory being warehoused rather than cleared.
- **Governance and register.** Form 4s and 13D/As from Dahl (18.8%), Russo (24.3%) and
  Robotti (9.8%). **Any sale by Dahl, the one large holder without a board seat, or any
  13D/A adding a control or strategic-alternatives purpose, is a first-order event** in a
  name whose entire minority case is the discount to asset value. Also: the outcome of the
  2026 Equity Plan vote at the annual meeting.
- **Water, the named UNRESEARCHED item.** Any appearance of water rights, service
  commitments or moratoria in Item 1 or the MD&A.
- **Auditor.** Any further change of auditor, any critical audit matter appearing, any
  ICFR conclusion other than effective.
- **Price alerts (LIST ONLY, no file edited):** **$19** (re-read the file against reopen
  condition 1) · **$26.43** (the current book value, the level at which the asset discount
  disappears entirely) · **$14** (the level at which the March-2022 repurchase discount to
  book would be reproduced).
- **Next catalysts:** FY2027 Q1 10-Q, due **~2026-09-09** (the first read on the guided-down
  FY2027 land revenue) · annual meeting, **~September 2026** · Q2 10-Q ~December 2026 ·
  Q3 10-Q ~March 2027 · **FY2027 10-K ~late July 2027** (the next acreage line, the next
  units series point, and the next capital-allocation datum) · DEF 14A ~August 2027.

**The sell rule [E2-28], answered although no position exists:** the two triggers and the
three hold conditions are recorded so that the yardsticks pre-date any act [E1-02]. Return
on equity capital: satisfactory on operating capital (~10-11.5%), unsatisfactory
consolidated (7.6%) and falling as cash accumulates. Management competent and honest: no
disqualifier found, one live allocation flag. Market overvaluing: no, the reverse.

**The taxable never-switch test, answered for the operator's actual mandate [E2-46, E3-64,
E3-67].** The earmarked $2,750 wants a dividend payer that compounds and is taxed once at
the end. **AXR is structurally not that name at any price.** It has paid **no dividend for
eighteen years**; the filing offers no policy beyond *"The Company may consider dividends
from time-to-time in the future"*; the capital that would fund one is being accumulated in
Treasuries instead; the round-trip trading friction on a 119-share order is **1% to 3%
each way** against [E3-67]'s 3%-per-annum benchmark; and the entire minority case rests on
a discount to asset value closing inside a structure the company itself describes as
blocking the event that would close it. **The bias warning in the brief is confirmed rather
than resisted: the wished-for profile is not in this filing, and saying so is the run
working.**

- **VERDICT: [x] IN** — what would prove this run wrong is written, dated and
  document-named on both sides: structural evidence plus price for the Q2 reopen, and the
  acreage, starts, margin, register and capital-allocation lines for the class thesis.

---
## SELF-AUDIT
- [x] Questions answered in order; stopped at the first non-IN (**Q2 OUT**); Q3, Q4 and Q5
      written **for the record only**, with Q4 and Q5 math under operator rule 3's
      **COMPUTATION — NOT A CLEARANCE** header
- [x] No question marked IN carries an "unverified", "general knowledge" or "provisional"
      caveat
- [x] **Market cap verified against filed shares first, as tasked:** 5,324,849 (10-K cover,
      2026-07-20) x $23.08 = **$122.9M** vs the sweep's ~$124M, a 0.9% gap; corroborated
      against the cover's $82,217,793 non-affiliate value at 2025-10-31
- [x] **Liquidity and spread friction for a $2,750 order stated explicitly [E3-67]**, with
      filed volume, observed volume, observed intraday range and a round-trip cost estimate
- [x] Step 0: FY2026 10-K and DEF 14A read with accession numbers; **FY2026 OCF
      cross-checked three ways** (filed statement $12,878 = MD&A = XBRL); FY2025 OCF
      cross-checked the same way; the absence of a later 10-Q established from the filing
      calendar, not assumed
- [x] Owner earnings on multi-year means, **two windows plus a third shown with the spread**
      [E2-42, E4-25]; **(c) disclosed as a judgment and the corpus D&A default refused in
      writing** with its reason [E3-44, E2-41, E5-20]; SBC subtracted in full [E5-06] with
      the [E3-70] substitution named; FY2026's favourable reimbursement mix normalised down
      [E4-41]
- [x] **The asset basis worked separately and both books printed** [E3-71], with the
      undeveloped-acre marks taken from the subject's own filed realisations and the
      unsplittable land carrying value named as the run's largest UNRESEARCHED gap
- [x] Competitor row filled with five listed comparables from their own audited filings via
      XBRL; the private local peers named as unavailable with [E3-61]'s limit stated; **no
      moat class claimed that needs the missing rows**, so PROVISIONAL does not arise
- [x] **The units test run [E4-55]** on acres, starts, developed acres sold and revenue
- [x] Debt footnote read in full and transcribed [E3-52]; [E2-54] coverage test run
      (interest expense zero); [E2-55] adverse-conditions case computed
- [x] Deaths quantified from filed figures with the required likelihood vocabulary
      [E3-24, E4-40], including the one that costs a minority holder rather than the company
- [x] DEF 14A read as tasked: ownership, board, comp against company size; **the brief's
      Karabots premise corrected against the 2023 proxy and an EDGAR full-text search**
- [x] Sovereign for the earnings currency (USD) from the issuing-authority series
      (FRED DGS30 via fredgraph.csv direct), dated **2026-08-27**
- [x] Value stated as round-number ranges on both books; the floor arithmetic stated
      plainly; **one bar chosen** (screamer, for the record); **windage count: one**,
      justified in writing
- [x] Prices dated; aggregators used for live quotes only and flagged at every use
- [x] Q6 written regardless; **alert thresholds LISTED ONLY**; `tools/alerts.json`,
      `PORTFOLIO.md`, `Screens/*`, `Framework/*` and other run files **not edited**
- [x] The market-beating claim is not made anywhere; every judgment carries a ledger id or
      is labelled a judgment or an estimate
- [x] Bias declared under operator rule 9 and the disconfirming evidence hunted hardest
      [E4-26]; the dividend mandate answered against the filing rather than around it
- [ ] Run committed to git — pending

## REGISTER
- **Verdict: [x] OUT (about the business, at Q2 — for entry).** No position held.
  Q1 IN. **Q2 OUT: not a franchise.** Q3 for the record: no honesty disqualifier found,
  Q3 is an overlay, and one capital-allocation flag is live. Q4 for the record: survives
  almost anything, all three [E5-11] legs pass, and the death that matters is the return
  rather than the company. Q5 computation: the earnings book puts the price inside the
  range and the asset book puts it below the floor, which is [E4-25]'s no-useful-conclusion
  box on one book and a discount on the other; **it does not scream.**
- **One line: a debt-free, honestly reported, 52-employee owner of 16,200 acres of Rio
  Rancho, New Mexico, bought in 1961 and carried at cost, that converts twenty acres a year
  into $820,000-an-acre lots at a 61% gross margin, supplies about one new lot in eight in
  the town it platted, has shrunk its revenue 10% in four years, holds 43% of its own
  market capitalisation in Treasuries earning 3.8% while its operating capital earns 10%,
  has bought back not one share since taking 28.6% of itself from the Karabots estate in
  March 2022, pays no dividend and has paid none since fiscal 2008, and sits behind a
  classified board and Oklahoma anti-takeover provisions its own 10-K says would block a
  change of control "even if a change in control would be beneficial to the Company's other
  shareholders." It is cheap against its assets and fairly priced against its earnings; it
  is not a franchise, and it is the opposite of the dividend compounder the capital is
  looking for.**
- **Work orders (UNRESEARCHED, none of which reopens Q2):**
  1. **The split of the $63,325 thousand land carrying value** between the 217 developed
     lots, the 68 developed commercial acres, the 358 acres under development and the
     ~16,500 undeveloped acres. Artifact: not in any filed document read. Route: a written
     question to the company (IR, 610-487-0905, Havertown PA), or the FY2027 10-K if
     disclosure expands. **Ladder rung: company IR. Blocked by: the company does not
     disclose it and is not required to.** This is the number that would tighten the asset
     range from $27-$44 to something usable.
  2. **Water rights and service availability.** Artifacts: New Mexico Office of the State
     Engineer water-rights records for AMREP Southwest Inc. and Sandoval County; the City of
     Rio Rancho 40-year water plan and its service-availability policy. **Route: state and
     municipal public records, ordinary retrieval, not blocked.** This is death 2 and the
     largest single unresolved exposure in the run.
  3. **Mineral rights under ~55,000 surface acres.** Artifacts: Sandoval County recorder's
     office; New Mexico Oil Conservation Division production and lease records. Route:
     public records. Carried at zero in this run's asset table.
  4. **Local competitor share.** AMREP's Rio Rancho competitors are private and unnamed.
     Artifacts: City of Rio Rancho plat and building-permit records by developer. Route:
     municipal records, ordinary retrieval. Would sharpen the ten-percent share estimate;
     would not change the Q2 class.
  5. **FY2027 Q1 10-Q (~2026-09-09) and FY2027 10-K (~July 2027)** — the next acreage line,
     the first read on the guided-down land revenue, and the next capital-allocation datum.
- **The single biggest concern:** not solvency, and not honesty. It is that **a genuinely
  cheap, genuinely clean, genuinely well-owned asset has no mechanism by which a
  $2,750 minority holder gets paid.** Four years of retained cash have gone to Treasuries
  at 3.8%; the last capital returned to shareholders was the March-2022 purchase of the
  Karabots block, which benefited the remaining holders enormously and has not been
  repeated; the dividend has been absent for eighteen years; the register is 52.9% in three
  hands with two of them on a classified board; and the company's own Item 5 explains that
  the structure requires the largest holders' concurrence for any change of control **"even
  if a change in control would be beneficial to the Company's other shareholders."** The
  land is real, the discount is real, and the closing mechanism is exactly what the filing
  says is hardest to trigger. [E2-51] reads that as revealing more than management knows of
  its motivations; [E4-13] requires the counter to be stated, and it is: they know the land
  and the entitlement queue far better than this run does, and parking capital until Mr.
  Market offers something is [E2-74]'s own doctrine.

*This file is a judgment by the AI running the framework. The underlying facts are the
FY2026 Form 10-K (acc. 0001104659-26-086659, filed 2026-07-24), the DEF 14A (acc.
0001104659-26-090418, filed 2026-08-04), the two 8-Ks cited in Step 0, the 2023 DEF 14A
(acc. 0001104659-23-086818) for the Karabots transaction, the FY2025/2023/2021/2019 10-Ks
for the acreage and volume series, SEC XBRL companyfacts for CIK 0000006207 and for the
five peers, FRED DGS30 dated 2026-08-27, and flagged aggregator quotes for price and
volume. Where a number is a judgment or an estimate — the (c) band, the bottom boundary,
the ex-cash return series, the lots-per-acre share arithmetic, the asset marks, the reopen
bands — it is labelled as one.*
