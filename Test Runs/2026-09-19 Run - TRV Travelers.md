# Company Run — The Travelers Companies, Inc. (TRV) — 2026-09-19
**MINI BERK insurance track.** Sector method: `Framework/SECTOR METHOD - owner earnings for insurers and float-bearing holding companies.md` (both amendments). CIK 0000086312, found with `tools/sources.py:cik_for()`.
**STATUS: IN PROGRESS — written early per the queue's write-early protocol.**
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
- rate **5.34 %** · date **2026-09-18** · source **US Treasury daily par yield curve, 30 Yr, from the issuing authority** (`tools/sources.py:sovereign('USD')`; no FRED fallback needed this run)
- FX if the quote and the earnings differ in currency: **not applicable.** TRV reports and earns
  substantially in USD. It has operations in the United Kingdom, the Republic of Ireland and at
  Lloyd's, and a Brazilian joint venture, and it sold the bulk of its Canadian business on
  2026-01-02. The FY2025 10-K states that for 2025 and 2024 *"changes in foreign currency
  exchange rates impacted reported line items in the statement of income by insignificant
  amounts."* So the sector method's open **FINDING 8** (one company earning in three currencies,
  left unresolved on purpose) is **checked and does not bite here**: International was $650M of
  $17,446M of Personal net written premiums and $1,934M of $22,679M in Business Insurance, and
  the Canadian leg is now gone.

**Stage 0 — the artifact check, with the two insurance-specific additions the sector method requires**

- **(a) Share class by hand off the cover.** ONE class of common stock, no par value. No A/B
  structure, so the BRK-A/BRK-B and LEVI/NKE/DKS/PINS mechanism cannot fire here — checked, not
  assumed.
  - **Cover count: 208,575,022 shares outstanding at 2026-07-10**, Form 10-Q for the quarter
    ended 2026-06-30, accession **0000086312-26-000145**, filed 2026-07-17.
  - **COVER-DEFINITION CHECK (the ERIC / IHG trap).** The cover reads *"The number of shares of
    the Registrant's Common Stock, without par value, **outstanding** at July 10, 2026 was
    208,575,022."* The word is **outstanding**, not issued. Cross-checked against the filed
    balance sheet: the common stock caption carries **208.6** shares against **treasury stock,
    at cost (586.8 shares)**, so the caption's "issued and outstanding" is already net of the
    586.8M treasury shares and the two agree. **No issued-versus-outstanding wedge.**
  - **POST-COVER ISSUANCE CHECK (the RGTI / USAR trap).** Nothing on the cover date is stale in
    the dilutive direction. The 10-Q's own statement of changes in equity shows the count moving
    the other way: 217.5 shares at 2025-12-31 to 208.6 at 2026-06-30, on 10.3 shares repurchased
    against 1.4 issued under employee plans in six months. A shelf registration expiring
    2028-06-04 permits securities issuance and $100 million of commercial paper was outstanding
    at 2026-06-30, but **no equity issuance is disclosed.** So 208.6M is the **conservative**
    count — at the 2026 repurchase pace (about 4.3M shares a quarter) the true count today is
    probably nearer 204M, which would make the market capitalisation smaller and any yield
    larger. The cover count is used unadjusted.
- **(b) Insurer, float-bearing holding company, or neither?** **An insurer, and the purest one
  this track has met.** TRV is a property-casualty underwriting group with no non-insurance
  operating leg at all, which means **CONVENTION 3** (value the insurer and the operating
  business separately) has nothing to separate. The three ratios the sector method's two
  amendments require, all computed in `arith.py` section B:

| ratio | TRV, 2025-12-31 | Berkshire **[E5-46]** | Markel (MKL run) | White Mountains (WTM run) |
|---|---|---|---|---|
| float ÷ investments | **65.0 %** | 41.8 % | 50.3 % | 22.0 % |
| investments ÷ equity | **3.08 x** | 0.45 x | 2.01 x | — |
| float, $m, by CONVENTION 4 | **65,772** | 66,000 | — | 1,831 |

  **What those two ratios mean, stated before the run uses them.** The first amendment's
  low-side guard (WTM at 22.0%) does not fire: at 65.0% TRV is **more** float-funded than
  Berkshire, so **step 2, the cost of float, is the centre of gravity of this run and not a
  rounding item** — the exact opposite of White Mountains. The second amendment's **CONVENTION 5**
  is the one that bites: investments are **3.08 times equity**, against Markel's 2.01x and
  Berkshire's 0.45x. **[E5-46]** licenses counting the whole portfolio as an element of value on
  one explicit condition — that underwriting breaks even, so the float funding it is free — and
  at 3.08x **TRV is the most dependent on that condition of any name this track has run.** That
  is not a disqualification and it is not a threshold; it is a statement of where the answer
  lives.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes (note 8 on reserves, the
      asbestos and environmental sections, the ten-year loss development tables)
- document · date · accession no.: **Form 10-K for FY2025, filed 2026-02-12, accession
  0000086312-26-000065**, primary document `trv-20251231.htm`. Also read: **Form 10-Q for
  Q2 2026, filed 2026-07-17, accession 0000086312-26-000145**; the **Form 8-K of 2026-07-17,
  accession 0000086312-26-000143, exhibits EX-99.1 earnings release and EX-99.2 financial
  supplement** — pulled *before* scoring [E4-29] and [E4-22]'s third flag, per the standing
  companion rule to the queue's brief prohibition; the **DEF 14A of 2026-04-07, accession
  0000086312-26-000103**; and for the multi-year series the 10-Ks for FY2023
  (0000086312-24-000012), FY2021 (0000086312-22-000013), FY2019, FY2018 and FY2016.
- figures cross-checked against the filed statement: **two.** (i) Reinsurance recoverables
  $7,886M and total investments $101,182M at 2025-12-31, taken from the XBRL facts, match the
  filed consolidated balance sheet in the 10-Q's 2025-12-31 comparative column line for line.
  (ii) General and administrative expense of $6,120M for 2025 from XBRL matches the filed
  consolidated statement of income in the 10-K. **A tooling defect was found doing exactly this
  and is recorded in the DEFECTS section at the foot of this file.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Travelers sells one-year promises,
mostly through independent agents and brokers, collects the premium up front, pays the claims
later, and invests the gap in the meantime. Two separate engines produce the income, and the
filing lets you see both:

1. **Underwriting.** Premium in, less claims, less the cost of acquiring and administering the
   policy. In 2025 that was $43,914M of earned premium against $27,221M of claims, $7,266M of
   amortised deferred acquisition cost and $6,120M of general and administrative expense — a
   GAAP underwriting result of **$3,307M**.
2. **The portfolio.** $101.2bn of investments at 2025-12-31, 94% of it fixed maturities and
   short-term securities, producing **$3,959M** of pre-tax net investment income.

**The three segments as filed, FY2025** (10-K accession 0000086312-26-000065):

| segment | net written premium | earned premium | combined ratio | pre-tax segment income |
|---|---|---|---|---|
| **Business Insurance** | $22,679M | $22,412M | 91.7 % | $4,586M |
| **Bond & Specialty Insurance** | $4,262M | — | 81.9 % | — |
| **Personal Insurance** | $17,446M | $17,395M | 89.5 % | $2,538M |
| **Interest Expense and Other** | — | — | — | $(373)M |
| **Consolidated** | **$44,387M** | **$43,914M** | **89.9 %** | **$7,796M** |

**Premium by line, as filed, net written, FY2025:**
- **Business Insurance by market:** Middle Market $12,541M · Select Accounts $3,830M · National
  Property and Other $3,112M · National Accounts $1,262M · International $1,934M.
- **Business Insurance by product (domestic, from the Q2 2026 financial supplement):** commercial
  multi-peril, commercial automobile, workers' compensation, commercial property and general
  liability — five roughly comparable blocks, each running $1.8-3.1bn a half-year, none dominant.
- **Personal Insurance:** homeowners and other **$9,051M** · automobile **$7,745M** ·
  international $650M. **Homeowners passed automobile in 2024 and the gap widened in 2025**;
  automobile net written premium actually **fell 2%** in 2025.
- **Bond & Specialty:** management liability and surety, $4,262M — the smallest segment and the
  most profitable, at an 81.9% combined ratio.

**WHERE THE EARNINGS COME FROM — underwriting or the portfolio? The portfolio, by a wide margin,
and it is not close.** GAAP underwriting result against pre-tax net investment income, every
year 2014-2025, computed in `arith.py` section A:

| year | underwriting result $m | net investment income $m | underwriting as % of the two |
|---|---|---|---|
| 2014 | 2,009 | 2,787 | 41.9 % |
| 2015 | 2,187 | 2,379 | 47.9 % |
| 2016 | 1,325 | 2,302 | 36.5 % |
| 2017 | **(120)** | 2,397 | **negative** |
| 2018 | 90 | 2,474 | 3.5 % |
| 2019 | 173 | 2,468 | 6.6 % |
| 2020 | 639 | 2,227 | 22.3 % |
| 2021 | 837 | 3,033 | 21.6 % |
| 2022 | 584 | 2,562 | 18.6 % |
| 2023 | **144** | 2,922 | **4.7 %** |
| 2024 | 2,090 | 3,590 | 36.8 % |
| 2025 | 3,307 | 3,959 | 45.5 % |
| **12-year total** | **13,265** | **33,100** | **28.6 %** |

**Over twelve years the portfolio produced 71.4% of the pre-tax income of the two engines
together, and in five of those twelve years underwriting produced less than a tenth of it.**
That single fact governs how this file reads every later gate: the 89.9% combined ratio of 2025
is the **best** underwriting year in a twelve-year window and is not the normal condition.

It also means the **[E5-48]** double-count trap is live and large here. An owner-earnings yield
built the ordinary way from the $10,606M of 2025 operating cash flow would be counting a $101bn
portfolio twice — once as the coupons it throws off inside operating cash flow, and again as an
asset in component 1. `arith.py` never does this, and the arithmetic that would have is named
and refused at Q4.

**The scarce input this business controls.** Candidly: **capital, and the regulatory licence that
lets capital be levered into promises** — not a product, not a location, not a brand. TRV's own
10-K counts *"approximately 1,100 property and casualty groups in the United States, comprising
approximately 2,600 property and casualty companies"*, of which the top 150 write about 94% of
industry net written premium. The one input that is plausibly scarce and plausibly theirs is the
**claims and loss-data apparatus, and the independent-agent relationships that come with 170
years of standing.** Whether that is a moat or table stakes is Q2's question, not Q1's, and it is
recorded here as a question rather than settled as a strength.

**Will the fundamentals look broadly the same in ten years?** Yes, and this is the strongest
thing in Q1. United States commercial property-casualty, personal automobile and homeowners
insurance will exist in 2036, will be sold in one-year contracts, and will be priced off loss
trend and interest rates. **[E3-31]**'s test — *"relatively simple and stable in character"* — is
met. The composition shifts (homeowners overtook automobile; the Canadian business was sold on
2026-01-02 for about US$2.4bn) but the mechanism does not.

**VERDICT: [x] IN** · *Understood, and the arithmetic of where the money comes from is on the
page. Nothing in this gate is a claim about quality. [E4-46]'s five-minute rule is satisfied —
this is not a business that would take months of study, and no fetch was needed to see the
mechanism.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The sector method's own warning applies before anything else. [E2-70]**, 1977: *"Insurance
companies offer standardized policies which can be copied by anyone. Their only products are
promises. It is not difficult to be licensed, and rates are an open book. There are no important
advantages from trademarks, patents, location, corporate longevity, raw material sources, etc."*
The method's Q2 section says plainly that **the [E3-03] question is harder here than in retail,
not easier**, and that nothing in the method makes it easier.

### The three criteria of [E3-03], scored against the filing

- **(1) Needed or desired — YES.** Automobile liability insurance is compulsory in nearly every
  state, homeowners insurance is required by mortgage lenders, workers' compensation is
  compulsory for employers, and surety bonds are required by contract and statute. This criterion
  is met about as strongly as it can be met.
- **(2) No close substitute — NO.** TRV's own Item 1 answers this against itself: *"According to
  A.M. Best, there are approximately 1,100 property and casualty groups in the United States,
  comprising approximately 2,600 property and casualty companies. Of those groups, the top 150
  accounted for approximately 94% of the consolidated industry's total net written premiums in
  2024."* And: *"The property and casualty insurance industry is **highly competitive in the
  areas of price**, service, product offerings, agent and broker relationships and other methods
  of distribution."* On the commercial side the filing goes further and names the substitutes by
  name — *"other entities offering risk alternatives, such as self-insured retentions or captive
  programs"*, plus *"large deductible programs and various forms of self-insurance … utiliz[ing]
  captive insurance companies and risk retention groups."* A product with 2,600 licensed
  suppliers and a self-insurance alternative is not a product with no close substitute.
- **(3) Not subject to price regulation — NO, and this one is a flat fail on the filer's own
  words.** From Item 1A: *"Insurers writing personal lines property and casualty policies **may be
  unable to change prices until some time after the costs associated with coverage have changed,
  primarily because of state insurance rate regulation.** … In states with prior approval laws,
  **rates must be approved by the regulator before being used by the insurer.** … **Approximately
  one-half of the states require prior approval of most rate changes.**"* And from the regulation
  section: *"The Company's domestic insurance subsidiaries are subject to each state's laws and
  regulations regarding rate and rule approvals. The applicable laws and regulations generally
  establish standards to ensure that rates are **not excessive**, inadequate, unfairly
  discriminatory or used to engage in unfair price competition."*

**Criterion 3 is not a close call and it is not a technicality.** It is the criterion **[E2-59]**
was written about: administered pricing can *floor* a commodity business's profits — pre-1970s
insurers *"could legally price their way to profitability even in the face of substantial
over-capacity"* — but *"Regulation **caps** a franchise ([E3-03] criterion 3) and **floors** a
commodity business; neither creates the class."* Here the regulator sets a ceiling ("not
excessive") and imposes a lag, and the lag is the filer's own named risk.

### The decisive series — the CURRENT-ACCIDENT-YEAR combined ratio, with prior-year development beside it

This is the test the MKL run of 2026-09-02 built and the one that closed Markel: reported
underwriting profit that is really prior-year reserve releases is **[E4-40]**'s named failure —
*"focusing on experience, rather than exposure."* Every figure below is from TRV's own 10-K
narrative, ten years, four filings; the arithmetic is `reported CR + favourable prior-year
development points`, and **`underlying` is TRV's own published measure (CR excluding both
catastrophes and prior-year development)**:

| year | reported CR | catastrophe pts | prior-year development pts | **CURRENT-ACCIDENT-YEAR CR** | TRV's own *underlying* CR | source 10-K |
|---|---|---|---|---|---|---|
| 2016 | 92.0 % | 3.6 | **+3.2 fav** | **95.2** | 91.6 | FY2018, 0000086312-19-000009 |
| 2017 | 97.9 % | 7.6 | **+2.3 fav** | **100.2** | 92.6 | FY2018 |
| 2018 | 96.9 % | 6.3 | **+1.9 fav** | **98.8** | 92.5 | FY2018 |
| 2019 | 96.5 % | 3.1 | **−0.2 ADVERSE** | **96.3** | 93.2 | FY2019, 0000086312-20-000011 |
| 2020 | 95.0 % | 5.5 | **+1.2 fav** | **96.2** | 90.7 | FY2021, 0000086312-22-000013 |
| 2021 | 94.5 % | 6.0 | **+1.8 fav** | **96.3** | 90.3 | FY2021 |
| 2022 | 95.6 % | 5.5 | **+1.9 fav** | **97.5** | 92.0 | FY2023, 0000086312-24-000012 |
| 2023 | 97.0 % | 7.9 | **+0.4 fav** | **97.4** | 89.5 | FY2023 |
| 2024 | 92.5 % | 8.0 | **+1.7 fav** | **94.2** | 86.2 | FY2025, 0000086312-26-000065 |
| 2025 | 89.9 % | 8.4 | **+2.4 fav** | **92.3** | 83.9 | FY2025 |
| **5-year mean 2021-25** | **93.9 %** | **7.2** | **+1.6** | **95.54** | **88.4** | |
| **10-year mean** | **94.8 %** | **6.2** | **+1.6** | **96.44** | **90.3** | |

**The arithmetic is checked against the filer, not assumed.** TRV publishes the year-over-year
*change* in its underlying combined ratio but not the level. Each computed level above reproduces
the filer's own stated delta at every one of the nine year-pairs — 2017 *"1.0 points higher than
the 2016 ratio"* gives 91.6 → 92.6; 2019 *"0.7 points higher than the 2018 ratio"* gives 92.5 →
93.2; 2021 *"0.4 points lower than the 2020 ratio"* gives 90.7 → 90.3; 2023 *"2.5 points lower
than the 2022 ratio"* gives 92.0 → 89.5; 2025 *"2.3 points lower than the 2024 ratio"* gives
86.2 → 83.9. **Nine independent reconciliations, no residual.** That is the cross-check operator
rule 4 requires, done on the series that decides the gate rather than on a convenient line item.

**What the series says, in three findings.**

1. **TRV is NOT Markel.** Markel's current-accident-year combined ratio was 99.3 / 101.1 / 100.3
   for 2023-25 — its reported underwriting profit *was* the reserve releases. **TRV's
   current-accident-year combined ratio is below 100 in nine of ten years**, mean 96.44. It
   earns an underwriting profit on business written in the year. **That is a real finding in
   TRV's favour and it is recorded as one.**
2. **But the profit is thin, and 1.6 points of the reported 5.2-point average underwriting margin
   is prior-year releases** — roughly 31% of it, every year, consistently, for ten years.
   A ten-year run of favourable development in nine years out of ten is a **reserving-margin
   policy**, which is a Q3 question ([E2-50]) and is read there.
3. **The catastrophe load has more than doubled and is still climbing: 3.1 points in 2019 to 8.4
   points in 2025**, while the underlying ratio improved from 93.2 to 83.9. **9.5 points of
   underlying improvement in six years have bought 5.3 points of extra catastrophe load and
   4.0 points of net gain.** Read against **[E4-40]** — *"model exposure, not experience"* — the
   improvement is real and the offset is structural: earned pricing is being spent on weather.

### The expense ratio trend

TRV's underwriting expense ratio: **31.5 % (2016) → 30.7 → 30.1 → … → 28.1 (2023) → 28.5 (2024)
→ 28.5 (2025).** A genuine 3.0-point improvement over a decade, and **it stopped two years ago**
and has ticked back up 0.4 points. Segment 2025: Business Insurance 29.5 % (up 0.1), Personal
Insurance 24.5 %, Bond & Specialty 39.3 %. This matters because of **[E2-58]**'s single exception
to the commodity verdict — *"a cost advantage that is both **wide and sustainable** … By
definition such exceptions are few"* — and the peer row below shows where that exception actually
sits.

### THE COMPETITOR ROW — required **[E3-28]**, extended from the MKL row rather than rebuilt

A moat is a claim about *relative* position and cannot be evidenced from one company's numbers.
The MKL run of 2026-09-02 built a seven-peer row (KNSL, ACGL, RLI, WRB, FFH, AXS, MKL) and the
CB run of 2026-09-19 put that row on the current-accident-year basis and added CB. **Those eight
rows are carried below unchanged, on their stated sources.** What this run adds is the set the
MKL/CB row does not contain and TRV requires: **the standard-lines peers TRV actually competes
with** — personal automobile and homeowners (PGR, ALL, CINF) and standard commercial (HIG, CNA)
— each read from the filer's own Form 10-K, same metric, same 2021-25 window.

**BASIS: current-accident-year combined ratio = reported combined ratio with prior-year reserve
development removed.** Best to worst on the five-year mean.

| company | basis | 2021 | 2022 | 2023 | 2024 | 2025 | **5-yr mean** | source |
|---|---|---|---|---|---|---|---|---|
| **KNSL** | consolidated | 82.6 | 82.9 | 78.6 | 79.1 | 79.8 | **80.60** | carried from the MKL/CB row |
| **ACGL** | consolidated | 89.6 | 89.5 | 83.6 | 85.9 | 86.3 | **86.99** | carried |
| **CB** | consolidated | 91.9 | 90.4 | 88.4 | 88.6 | 88.2 | **89.50** | carried |
| **WRB** | consolidated | 89.7 | 88.9 | 89.5 | 90.3 | 90.7 | **89.84** | carried |
| **HIG** | Business Insurance segment | 94.3 | 92.4 | 91.5 | 91.7 | 91.5 | **92.28** | **NEW.** FY2025 10-K 0000874766-26-000012; FY2023 10-K 0000874766-24-000016 |
| **PGR** | total underwriting operations | 95.3 | 96.0 | 93.0 | 89.4 | 89.1 | **92.57** | **NEW.** FY2025 10-K 0000080661-26-000086 (Annual Report exhibit); FY2023 10-K 0000080661-24-000007 |
| **RLI** | consolidated | n/a | 95.1 | 95.0 | 92.4 | 89.7 | **93.08** (4 yrs) | carried |
| **AXS** | consolidated | 98.2 | 96.3 | 91.8 | 92.8 | 91.4 | **94.10** | carried |
| **CNA** | P&C Operations, NEP-weighted | 96.8 | 94.4 | 93.8 | 95.3 | 94.2 | **94.89** | **NEW.** each year's own 10-K; FY2025 0000021175-26-000011 |
| **TRV** | **consolidated** | **96.3** | **97.5** | **97.4** | **94.2** | **92.3** | **95.54** | **THIS RUN.** table above |
| **ALL** | Property-Liability | 95.6 | 102.7 | 103.3 | 94.8 | 88.3 | **96.94** | **NEW.** FY2025 10-K 0000899051-26-000031; FY2023 10-K 0000899051-24-000013 |
| **CINF** | consolidated P&C | 95.3 | 100.4 | 97.7 | 96.1 | 96.9 | **97.28** | **NEW.** FY2025 10-K 0000020286-26-000008; FY2023 10-K 0000020286-24-000014 |
| **MKL** | consolidated | n/a | n/a | 99.3 | 101.1 | 100.4 | **100.27** (3 yrs) | carried |
| **FFH** | — | n/a | n/a | n/a | n/a | n/a | **NOT COMPARABLE** | IFRS 40-F filer; no comparable current-accident-year separation located |

- **Peers named: 13 of the industry's roughly 150 groups that write 94% of US premium**
  (TRV's own count), of which **six are TRV's direct standard-lines competitors** and seven are
  the specialty, E&S and global writers carried from the MKL and CB rows. Buffett says eight
  **[E3-28]**; thirteen were taken and the basis of each is stated.
- **TRV ranks 10th of the 13 with data, and 4th of the 6 standard-lines peers.** It is 6.0 points
  worse than Chubb, 3.3 points worse than Hartford's commercial book, 3.0 points worse than
  Progressive, and 15 points worse than Kinsale. It beats Allstate, Cincinnati and Markel.
- **Any peer unavailable?** **FFH (Fairfax)** — an IFRS 40-F filer whose combined ratio is not
  separated on this basis in Exhibit 99.3. That is carried from the MKL/CB row as
  NOT COMPARABLE rather than estimated. One name out of fourteen, and it does not move the rank.

**The row's stated limit [E3-61].** Identical structures produce opposite outcomes — *"In some
businesses, the participants behave like a demented Kellogg. In other businesses, they don't …
**I think you'd have to know the people involved.**"* The row shows position; it cannot show
conduct. Two comparability limits are also disclosed rather than smoothed: **CNA's figure is
flattered**, because the prior session's extraction (`peers/data_CNA.json`) excludes the
Corporate & Other segment where CNA's asbestos, environmental and legacy mass-tort development
ran +$50M to +$134M adverse a year in 2020-25, while **TRV's consolidated figure includes its
asbestos charges in full**; and **HIG is its Business Insurance segment only**, because HIG
publishes no consolidated property-casualty combined ratio. Correcting either would move TRV
*up* the row by a place, not more.

### THE EXPENSE RATIO ROW — where [E2-58]'s one exception actually lives

| company | underwriting expense ratio, 2025 | source |
|---|---|---|
| **PGR** | **21.5 %** | FY2025 Annual Report exhibit, total underwriting operations |
| **ALL** | **21.4 %** | FY2025 10-K, Property-Liability |
| **TRV** | **28.5 %** | FY2025 10-K |
| **CINF** | 29.3 % | FY2025 10-K |
| **CNA** | 29.8 % | computed, NEP-weighted segments |
| **HIG** | 31.2 % (+0.3 dividend) | FY2025 10-K, Business Insurance |

**[E2-58]**'s exception — *a cost advantage both wide and sustainable* — **belongs to Progressive
and Allstate, and it is seven points wide, in exactly the lines where TRV's premium growth is
concentrated.** TRV's decade of expense-ratio improvement closed the gap to Hartford and
Cincinnati; it did not touch the direct-and-low-cost personal-lines writers. **The one escape
route [E2-58] leaves open from the commodity verdict is occupied by somebody else.**

### The physical units — **[E4-55]**, and this is the sharpest thing in the gate

*"Dollar revenue flattered by pricing is how a shrinking franchise hides; the physical series is
the honest one."* Precision Steel's pounds fell 69M to 46M while price rises held dollar revenue
level, and Buffett called it *"a serious reverse, not likely to disappear in some 'bounce back'
effect."* **TRV publishes the physical series, in its own 10-K, every year.** Domestic Personal
Insurance active policies, with net written premium per policy beside them:

| year | domestic PI active policies | domestic PI net written premium | **premium per policy** |
|---|---|---|---|
| 2015 | 6.2 M | — | — |
| 2019 | 7.5 M | — | — |
| 2020 | 8.4 M | $10,666 M *(derived: 11,350 total less 684 international)* | ~$1,270 |
| 2021 | **8.9 M** | $11,807 M | **$1,327** |
| 2022 | **9.2 M ← PEAK** | $13,398 M | **$1,456** |
| 2023 | 9.1 M | $15,279 M | **$1,679** |
| 2024 | 8.8 M | $16,475 M | **$1,872** |
| 2025 | **8.4 M** | $16,796 M | **$1,999** |

**From the 2022 peak, Travelers has lost 800,000 domestic personal-lines policies — 8.7% of the
book — while raising premium per policy 37.3%.** Over 2021-25 the price is up **50.6%** and the
count is down **5.6%**. The segment's reported combined ratio improved from 104.8% (2023) to
89.5% (2025) on that trade.

**And the physical decline is accelerating, on the filer's own quarterly furnished data** (8-K of
2026-07-17, EX-99.2 financial supplement, policies in force in thousands, change from prior-year
quarter):

| | 1Q25 | 2Q25 | 3Q25 | 4Q25 | 1Q26 | 2Q26 |
|---|---|---|---|---|---|---|
| Automobile | 3,118 | 3,083 | 3,050 | 3,025 | 2,819 | 2,801 |
| change y/y | (2.9)% | (3.1)% | (3.4)% | **(4.0)%** | (9.6)% | (9.1)% |
| Homeowners and Other | 5,980 | 5,882 | 5,768 | 5,679 | 5,449 | 5,411 |
| change y/y | (4.1)% | (4.6)% | (5.5)% | **(6.3)%** | (8.9)% | (8.0)% |

The 2026 step-down is partly the Canadian disposal closing on 2026-01-02 (international net
written premium goes to zero from 1Q2026 in the same supplement, so the comparison is not clean
and is not used). **The 2025 columns are clean, and they are monotonic: automobile from −2.9% to
−4.0% and homeowners from −4.1% to −6.3% through the year, each quarter worse than the last.**
Automobile net written premium itself **fell 2% in 2025** on the annual filing.

### Retention against renewal price change — what filed data does and does not say

**The brief asked what filed retention and renewal price change did together in the most
price-shopped lines. The answer contains a disclosure finding: for Personal Insurance, TRV does
not publish either number.** The FY2025 10-K describes them in adjectives only, five times:
*"Retention rates remained strong in 2025 and were comparable with 2024. **Renewal premium
changes in 2025 remained positive but were lower than in 2024.** New business premiums in 2025
increased over 2024"* (automobile); *"Retention rates remained strong in 2025 **but decreased
from 2024.** Renewal premium changes in 2025 remained positive and were **higher** than in 2024.
New business premiums in 2025 **decreased** from 2024"* (homeowners). The word "approximately"
never attaches to a number. The EX-99.2 financial supplement carries no retention or renewal
premium change table for any segment; the quantified version lives in the earnings-call slides,
which are not filed or furnished.

**Where numbers ARE furnished — the commercial books, 8-K of 2026-07-17, EX-99.1:** Business
Insurance renewal premium change **4.8%** with retention **86%** in 2Q2026 (Middle Market renewal
premium change 6.1%, Select 9.4%); Bond & Specialty management liability retention **88%**.

**So the two tests read together, on what is actually filed:**
- **Commercial:** retention is high (86-88%) and renewal price change is decelerating from the
  2021-23 hard market — the filing says renewal premium changes were *"lower than in 2024"* in
  Select Accounts, Middle Market and National Accounts alike. Price is being given back as
  capacity returns.
- **Personal:** retention is described as strong; the policy count says otherwise, falling
  monotonically all through 2025. **Where the filer's adjective and the filer's own physical
  count disagree, the count wins** — and that is not an inference, it is what [E4-55] instructs.
  Homeowners retention is the one the filing admits *"decreased from 2024"*, and homeowners is
  where the price went up most.

### [E2-44]'s two-characteristic test, [E3-33]'s untapped pricing power, [E4-37]'s inverse metric

- **[E2-44] first half — can it raise prices *"even when product demand is flat and capacity is
  not fully utilized"*? NO.** The 2021-23 price rises came in a hard market with industry
  capacity tight, and TRV's own 2025 filing records them decelerating in every commercial market
  as capacity returned. **[E2-58]** describes exactly this: long-term profitability set by *"the
  ratio of supply-tight to supply-ample years"*, with prosperity breeding the next glut. TRV's
  ten-year current-accident-year series is that ratio made visible: 100.2 in the soft year
  (2017), 92.3 in the tight one (2025).
- **[E2-44] second half — grow dollar volume *"with only minor additional investment of
  capital"*? PARTLY YES**, and this is a real point in TRV's favour: premium grew from $24.5bn
  (2016) to $43.9bn (2025), +79%, while shareholders' equity went from $23.2bn to $32.9bn, +42%,
  and $22.7bn was returned in buybacks over twelve years. An insurer levering the same capital
  harder is the honest description of it.
- **[E3-33] untapped pricing power — NO, and the filing forecloses it.** *"Insurers … may be
  unable to change prices until some time after the costs associated with coverage have changed,
  primarily because of state insurance rate regulation."* **[E5-28]** scopes the class: claiming
  untapped pricing power *"you're talking about a business that's a monopoly or a near
  monopoly"* — against 2,600 licensed competitors, the claim cannot be made.
- **[E4-37]'s inverse metric — the agony of a price increase — reads at the maximum.** TRV must
  file rates with fifty state regulators, about half of which must approve before use, against a
  statutory standard that rates be *"not excessive"*, and its own risk factors warn that
  overpricing means *"new business growth and retention of our existing business may be adversely
  affected."* This is not *"a prayer session before you raise your prices a penny"*; it is a
  prayer session held in front of a regulator.
- **[E4-36]'s four causes of extreme success:** TRV's 2024-25 record comes from the fourth —
  **riding a wave**, the hardest commercial property-casualty pricing cycle since 2003 plus a
  bond portfolio repricing from a 3.0% to a 4.3% book yield as rates rose. **[E3-51]**: *"the
  advantage lives in the wave, not the surfer."* A surfing run is not a moat.
- **[E4-04] / [E4-23] key-person dependence:** no defect found. TRV's moat claim, such as it is,
  rests on scale, agency relationships and data, not on a named individual. This is recorded as a
  **non-finding**, not a strength.

### Class and direction

- **Class: [ ] WIDE  [ ] NARROW  [x] NONE at the group level**, with one dissent inside it:
  **Bond & Specialty Insurance has a plausibly narrow moat** — surety at an 81.9% combined ratio,
  where TRV retains *"up to $160.0 million probable maximum loss (PML) per principal"* and the
  business requires credit underwriting capacity few carriers have. It is **$4,262M of $44,387M
  of net written premium, 9.6% of the group**, and one narrow moat over a tenth of the premium
  does not make the group a franchise. The MKL precedent is the same shape and reached the same
  answer.
- **Direction: NARROWING**, on [E4-32]'s test — *"the moat widened every year"* is *"the primary
  criterion of a great business."* Three independent series point the same way: the physical
  policy count down 8.7% from peak and accelerating; the expense-ratio improvement stalled in
  2023 and partly reversed; renewal price change decelerating in every commercial market on the
  filer's own words. The one series pointing the other way is the underlying combined ratio, and
  **[E4-55]** is explicit about which of the two to trust.

### THE STRONGEST FACT AGAINST THIS VERDICT, stated as **[E4-51]** requires

*"I'm not entitled to have an opinion unless I can state the arguments against my position better
than the people who are in opposition."* Here it is, and it is a serious fact, not a courtesy:

**Over the ten years 2016-2025 Travelers' cost of float was NEGATIVE 1.73% a year.** It was
*paid* an average of $907M a year to hold an average of $52.4bn of other people's money
(`arith.py` section C, full table at Q4 below). **[E3-69]** — the corpus's own answer to *"what
should the measure of an insurer's profitability be?"* — says *"a low cost of funds signifies a
good business; a high cost translates into a poor business."* By the single measure the corpus
itself nominates for this exact business class, **Travelers is a good business, and by a wide
margin against a 5.34% sovereign.** Add that its current-accident-year combined ratio was under
100 in nine of ten years, which is more than most of the industry manages, and the case for IN is
real.

**Why it does not rescue Q2, and the reasoning is the corpus's own.** [E3-69] measures **how
cheaply the business is funded**; [E3-03] asks whether **the product has no close substitute and
is not price-regulated.** Those are different questions, and a business can pass the first while
failing the second — **that combination has a name in the corpus and the name is [E2-59]**: a
commodity business whose profits are floored by a regime rather than protected by a position.
Cheap float is the *mechanism* by which a thinly-profitable underwriter earns an acceptable
return on equity; it is not evidence of pricing power, and the peer row shows it is not
distinctive either. **Cost of float is the underwriting result over float, so a peer with a
better current-accident-year combined ratio on a comparable float ratio has a better cost of
float by construction — and four of the thirteen peers, Chubb and W. R. Berkley among them, run
6 to 15 points better.** *(Stated as an inference from the row, not as a computed peer figure:
peer float ratios were not constructed, and CONVENTION 4 would have to be run on each filing to
make it a measurement. That is named here as the honest limit of the point.)*

### VERDICT

**VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**OUT — and it is about the business, which is why it is permanent and why no price repairs it.**
Two of the three [E3-03] criteria fail on the filer's own words, the thirteen-name competitor row
puts Travelers tenth on the decisive metric and fourth of six against the peers it actually
competes with, the one exception [E2-58] allows a commodity business is held seven points wide by
Progressive and Allstate in the very lines Travelers is growing, and the physical policy count —
the series [E4-55] says is the honest one — has fallen 8.7% from its 2022 peak and is falling
faster each quarter while price per policy rises 50.6%.

**Can I name the document that would resolve this?** No document is missing. Ten years of 10-Ks,
thirteen peers' 10-Ks, the quarterly furnished supplement and the filer's own rate-regulation
disclosure are all in hand and they agree. **This is not UNRESEARCHED and it is not UNKNOWABLE.
The evidence is here and the business is not a franchise.**

**⛔ THE HARD SEQUENCE STOPS THE RUN HERE.** Q3, Q4 and Q5 below are **RECORDED, NOT GOVERNING**
— written because the brief asked for the cost of float, the two components and the
retained-earnings judgment, and because the evidence is already gathered and is worth having on
disk. **Nothing below is a clearance, and no part of it can promote the name.** Per operator
rule 3, the Q5 arithmetic carries the required heading.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
### ⚠️ RECORDED, NOT GOVERNING. Q2 closed the file OUT. Nothing here can promote the name.
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — THE WEIGHT CASE.**
- [x] **Daily execution** — **[E2-70]**, the 1977 root, is *about this industry by name*: *"Insurance
      companies offer standardized policies which can be copied by anyone. **Their only products
      are promises** … there is no question that the nature of the insurance business **magnifies
      the effect which individual managers have on company performance.**"* **[E3-43]**'s
      have-to-be-smart-every-day condition is met at its source.
- [ ] Control — no; this is a marketable security.
- [x] **Leverage** — **[E3-29]**. Not 20:1 bank leverage, but investments are **3.08x equity** and
      claim reserves are **$67.2bn against $33.1bn of equity**. A 5% error in the reserve estimate
      is $3.4bn, or 10.2% of equity. Small asset and liability errors destroy equity here.

**Two of three ticked, so Q3 IS A BINARY GATE and no price would compensate** — had the run
reached it. Case declared.

### Reserves are where dishonesty hides — **[E2-50]**, and this is the whole of Q3 here

*"Where 'earnings' can be created by the stroke of a pen, the dishonest will gather."* So the
reserve-development record is tested against **subsequent** development, from the ten-year claim
development triangles in note 8 of the FY2025 10-K — first estimate against the estimate ten
years later, by product line, net of reinsurance, $m:

| accident year | **General Liability** first → latest | change | **Workers' Compensation** first → latest | change |
|---|---|---|---|---|
| 2016 | 1,075 → 1,185 | **+10.2 % ADVERSE** | 2,768 → 2,092 | **−24.4 % favourable** |
| 2017 | 1,133 → 1,313 | **+15.9 % ADVERSE** | 2,779 → 2,167 | **−22.0 %** |
| 2018 | 1,253 → 1,604 | **+28.0 % ADVERSE** | 2,744 → 2,194 | **−20.0 %** |
| 2019 | 1,447 → 1,752 | **+21.1 % ADVERSE** | 2,680 → 2,355 | **−12.1 %** |
| 2020 | 1,467 → 1,570 | **+7.0 % ADVERSE** | 2,559 → 2,025 | **−20.9 %** |
| 2021 | 1,591 → 1,711 | **+7.5 % ADVERSE** | 2,356 → 2,166 | **−8.1 %** |
| 2022 | 1,696 → 2,014 | **+18.8 % ADVERSE** | 2,293 → 2,148 | **−6.3 %** |
| 2023 | 1,998 → 2,129 | **+6.6 % ADVERSE** | 2,373 → 2,371 | −0.1 % |
| 2024 | 2,340 → 2,315 | −1.1 % | 2,352 → 2,344 | −0.3 % |

Commercial automobile (five-year triangle only): AY2021 1,741 → 1,789 **+2.8% adverse**, AY2022
1,939 → 2,059 **+6.2% adverse**, AY2023 2,245 → 2,272 **+1.2% adverse**, AY2024 2,544 → 2,452
−3.6%. Personal automobile: AY2021 −0.3%, AY2022 −1.5%, AY2023 −3.3%, AY2024 −3.7% favourable.

**THE FINDING, and it is the one thing the consolidated series conceals.** TRV reports net
**favourable** prior-year development in nine of ten years, $1.04bn in 2025 alone. **The
mechanism is that workers' compensation released 20-24% of eight consecutive accident years'
initial estimates, and those releases paid for general liability strengthening of 7-28% in eight
consecutive accident years plus commercial automobile strengthening plus an asbestos charge every
single year.** That is **[E2-56]**'s Pro-Am effect applied to reserves rather than to capital
allocation: *"Their marvelous core businesses … camouflage repeated failures"* — judge
line-by-line, never on the blended figure. The blended figure here is genuinely favourable; one
of its components has been wrong in the same direction for eight straight years.

**Is that dishonesty? No, and the file says so plainly.** It is the industry's shape: long-tail
casualty deteriorates under social inflation while workers' compensation has redeemed for a
decade on medical-cost moderation. And the redundancy is disclosed, line by line, in a table
anybody can read. **What it IS: a finite fuel supply.** The workers' compensation releases are
shrinking fast — 24.4% on AY2016, 8.1% on AY2021, 0.1% on AY2023 — while general liability keeps
taking. **When the workers' compensation cushion is spent, 1.6 points a year of reported combined
ratio goes with it.** That is a Q6 monitoring item and it is written as one below.

### The candor benchmark — **[E2-67]**, and TRV lands ABOVE average and BELOW the benchmark

The benchmark is Berkshire publishing a table of its own reserving errors *"so you can … judge
whether we may have some systemic bias that should make you wary of our current and future
figures"*, naming the direction: *"always presented a better underwriting picture than was truly
the case."*

**What TRV does, to its credit:**
- **It publishes the ten-year triangles** by product line, which is the reserving-error record in
  full. *(Discounted somewhat: ASU 2015-09 requires them, so this is compliance rather than
  volunteered candor. Berkshire's table was volunteered.)*
- **On asbestos it names the direction of its own error, unprompted and in plain words:** *"Over
  the past decade, the property and casualty insurance industry, **including the Company**, has
  experienced **net unfavorable prior year reserve development with regard to asbestos
  reserves**."* And it quantifies the annual charge: the in-depth reviews of Q3 2025, 2024 and
  2023 produced **$277M, $242M and $284M increases** to net asbestos reserves, on carried net
  reserves of $1.36bn. The 2023 disclosure goes further: the charge *"also included an additional
  increase to strengthen the Company's carried reserve position relative to the range of
  reasonable estimates."* **A filer that tells you it strengthened beyond the point of necessity,
  and how much, is doing the [E2-26] half-owner test properly.**
- **It names the adverse trend against itself:** *"The combined ratio continues to be impacted by
  **the tort environment, including more aggressive attorney involvement in insurance claims.**"*
- **It discloses sensitivity:** a 1% change in named risk factors, quantified for general
  liability, property, commercial multi-peril, commercial automobile and workers' compensation
  separately.
- **[E2-72] authorship:** the letter to shareholders is signed by the Chairman and CEO; nothing
  reads as prepared by a staff specialist.

**Where it falls short of the benchmark:** TRV never aggregates the triangles into the sentence
they support. It does not say "our general liability reserves have been 7 to 28% light for eight
consecutive accident years and workers' compensation has paid for it." **The reader must compute
the systemic bias that [E2-67] says the filer should name.** So: above the industry, below the
standard the corpus sets.

### STEP 2 — THE FLAGS **[E4-22, E5-15]**. *Each a prompt to read, never a verdict.*

- [ ] **weak accounting** — none found. Share-based compensation is expensed ($256M in 2025).
      Reserves are estimates by nature and the estimation methods are disclosed at length.
- [ ] **unintelligible footnotes** — the opposite. Note 8 runs to product-line triangles with
      IBNR and claim counts; the asbestos discussion names its own methodology limits
      (*"Conventional actuarial methods are not utilized to establish asbestos reserves, and the
      Company's evaluations have not resulted in a reliable method to determine a meaningful
      average asbestos defense or indemnity payment"*).
- [ ] **trumpeted earnings projections / growth targets** — **CLEAN, and checked properly.** The
      8-K of 2026-07-17, EX-99.1, contains no numeric guidance; the only occurrence of "outlook"
      is inside the forward-looking-statements legend. The one standing target is qualitative and
      is a **return** target, not an EPS target: the proxy's *"goal of achieving a core return on
      equity in the mid-teens over time."* **[E3-48]** is therefore not testable against a
      numeric outturn, because there is no published number to test. **[E5-30]**'s ratchet has not
      been started.
- [ ] **serial share issuance [E5-15]** — the inverse. Shares outstanding **353.5M (2013) →
      208.6M (2026-07-10), a 41.0% retirement.** Nothing here.
- [ ] **EBITDA / adjusted-earnings promotion [E4-29]** — **CLEAN, and checked where the CGNX
      lesson says to check.** The word EBITDA appears **zero times** in the FY2025 10-K, **zero
      times** in the 8-K EX-99.1 earnings release, **zero times** in the EX-99.2 financial
      supplement and **zero times** in the 2026 proxy. The headline non-GAAP measure is
      **"core income"**, which excludes net realized investment gains and losses — a disclosed,
      reconciled adjustment presented on a dedicated page of the supplement
      (*"Reconciliation of Net Income to Core Income and Earnings per Share to Core Income per
      Share"*, page 2). That is not the [E4-29] behaviour; depreciation is not being deleted, and
      the reconciliation is furnished rather than buried.
- [ ] **filed-figure tells [E4-30]** — **unnaturally smooth growth: NO.** Net income by year
      (2016-2025): 3,014 · 2,056 · 2,523 · 2,622 · 2,697 · 3,662 · 2,842 · 2,991 · 4,999 · 6,288.
      That is a 32% drop in 2017 and a 23% drop in 2022, published without smoothing. **Cash taxes
      as a share of reported pre-tax income:** current income tax expense over pre-tax income —
      2016 22.9% · 2017 14.5% · 2018 16.0% · 2019 17.8% · 2020 17.6% · 2021 16.4% · 2022 22.1% ·
      2023 15.0% · 2024 21.6% · 2025 16.4%. **No downward trend; the 2017-18 step is the Tax Cuts
      and Jobs Act rate change, disclosed with its own $129M provisional line.** Clean.
- [x] **ONE FLAG FIRES, and it is [E2-49]'s metric-scoping rather than [E4-22]'s list.** The pay
      metric is **adjusted** core return on equity, and the proxy states the adjustment: results
      are set so as to *"not be as volatile from year-to-year as changes in financial results due
      to catastrophe losses … executives are appropriately accountable for managing the Company's
      catastrophe losses, but are **not unduly rewarded, or disadvantaged, based on the level of
      catastrophe losses in a given year.**"* **In a business whose catastrophe load has gone from
      3.1 points of the combined ratio in 2019 to 8.4 in 2025, normalising catastrophes out of
      the pay metric removes from the scorecard the single largest adverse movement of the
      decade.** [E2-49] demands *"pre-set, long-lived and small bullseyes"*, and this bullseye is
      pre-set and long-lived — which is why it is scored as a **prompt, not a verdict**, and why
      it is [E2-49] rather than metric-switching: nothing was discarded after deteriorating.

**[E4-52] — do the flags converge?** **NO.** One prompt fires, eight read clean, and there is no
lollapalooza. This is the opposite of the converging pattern (weak accounting + trumpeted
projections + serial issuance + price-targeting) the ruling describes.

### STEP 3 — THE PRIMARY TEST **[E2-01]**. Earnings rate on equity capital employed.

| year | net income $m | average equity $m | **ROE** |
|---|---|---|---|
| 2016 | 3,014 | 23,410 | 12.9 % |
| 2017 | 2,056 | 23,476 | 8.8 % |
| 2018 | 2,523 | 23,312 | 10.8 % |
| 2019 | 2,622 | 24,418 | 10.7 % |
| 2020 | 2,697 | 27,572 | 9.8 % |
| 2021 | 3,662 | 29,044 | 12.6 % |
| 2022 | 2,842 | 25,224 | 11.3 % |
| 2023 | 2,991 | 23,240 | 12.9 % |
| 2024 | 4,999 | 26,392 | 18.9 % |
| 2025 | 6,288 | 30,379 | **20.7 %** |
| **10-year mean** | **3,369** | **25,647** | **12.94 %** |

**The denominator has to be named, per [E2-47] and [E2-43].** Two corrections run in opposite
directions and both are disclosed rather than chosen:
- **Understated equity flatters 2022-24.** Accumulated other comprehensive loss was **$(4,967)M
  at 2024-12-31** and $(2,500)M at 2025-12-31, almost all unrealised losses on a 94%
  fixed-maturity portfolio held at market. Equity fell from $28,887M (2021) to **$21,560M
  (2022)** on bond marks while nothing about the business changed. **Adding the AOCI loss back,
  2023 ROE is 2,991 ÷ ~28,600 = 10.5% rather than 12.9%, and 2024 is 4,999 ÷ ~31,700 = 15.8%
  rather than 18.9%.** The reported improvement is between a quarter and a third a denominator
  effect.
- **Goodwill overstates it the other way [E2-43].** Goodwill $4,066M and other intangibles $336M
  at 2025-12-31; on unleveraged net tangible equity of about $28.5bn the 2025 return is ~22%
  rather than 20.7%.

**So the honest statement is a ten-year mean ROE of roughly 13%, with the last two years genuinely
better (15-19% adjusted, not 19-21% reported) on a hard market and a repriced bond book.** Against
**[E5-40]**'s *"quite satisfactory"* ~12% on retained capital, that clears. Against **[E2-42]**'s
red-light test — *"Red lights should start flashing if the five-year average annual gain falls
much below the return on equity earned over the period by American industry in aggregate"* — a
13% mean does not flash.

### The half-owner test **[E2-26]** and capital allocation

**Half-owner test: PASSES, and well.** One-time items are quantified separately at every line —
catastrophe losses in dollars and in combined-ratio points by segment and by product, prior-year
development the same way, the Canadian disposal separately captioned as held for sale with its own
asset and liability lines, and the asbestos charge given its own annual number. **Nothing material
is buried inside an adjusted figure.** This is the reporting a reversed-positions owner would want.

**[E2-30] the institutional imperative — score all four:**
- [ ] resists any change in current direction — **no**: it sold the Canadian personal and most of
      the Canadian commercial business for about US$2.4bn, closing 2026-01-02, and it is letting
      800,000 personal-lines policies go rather than hold them on price.
- [ ] projects or acquisitions to soak up funds — **no.** Twelve years, $22.7bn of buybacks,
      **no large acquisition.**
- [ ] staff studies justifying the leader's craving — nothing found in the filings.
- [ ] peer behaviour mindlessly imitated — **[E3-02]**'s conformity failure mode is the one to
      test here, and TRV is on the right side of it: it shed policies through 2025 while
      competitors chased the same households.

**Buybacks — the conditions of [E5-08], scored honestly, and this is the second prompt.**
- **(1) ample funds for operations and liquidity? YES.** Holding company liquidity $2.41bn at
  2025-12-31; debt-to-total-capital 22.0%; a $1.2bn undrawn facility to 2031; $100M of commercial
  paper and the filer's own statement that *"TRV is not reliant on its commercial paper program to
  meet its operating cash flow needs."*
- **(2) at a material discount to conservatively calculated intrinsic value? NOT DEMONSTRATED.**
  TRV repurchased **$3,004M in 2025** and **$3,100M in the first half of 2026 alone** at a price
  that was 2.36x book value at 2026-06-30 ($374.62 against book value per share of $158.78) and
  2.48x at 2025 year end. **The Company publishes no intrinsic-value estimate and no repurchase
  price discipline of any kind** — which also means **[E4-31]'s THIRD condition fails**:
  *"Shareholders should have been supplied all the information they need for estimating that
  value."* Contrast **[E5-25]**, where Berkshire published **both** conditions as numbers in
  advance (the 110%-of-book limit, the $20bn liquidity floor). **CAPITAL ALLOCATION FLAG, stated
  with [E4-13]'s humility clause**: this rests on our own range, management knows the business far
  better than we do, and *"many CEOs never stop believing their stock is cheap"* **[E5-08]**. The
  flag binds position size, never the discount rate — and here there is no position to size.
- **[E5-24]**'s first law is the live question: *"what is smart at one price is dumb at another."*
  TRV bought $625M of stock in 2020 at roughly $140 and $3,004M in 2025 at roughly $290 —
  **it spent least when the stock was cheapest and most when it was dearest.** That is the pattern
  the first law warns about, and it is stated as an observation from the filed cash-flow statements
  rather than as a charge.

**[E3-54] — the retention test, five-year rolling, and it PASSES decisively.** Market value added
per dollar retained, from the filed cash-flow statements and dated closes (share counts from the
filings, prices from an aggregator and flagged as such):

| window | net income $m | dividends + buybacks $m | **retained $m** | market cap start → end $m | **$ of market value per $1 retained** |
|---|---|---|---|---|---|
| 2021-2025 (5 yr) | 20,782 | 13,703 | **7,079** | 35,429 (252.4M × $140.37) → 63,088 (217.5M × $290.06) | **$3.91** |
| 2016-2025 (10 yr) | 33,694 | 24,937 | **8,757** | 33,395 (295.9M × $112.86) → 63,088 | **$3.39** |
| 2014-2025 (12 yr) | 41,825 | 33,830 | **7,995** | 32,006 (353.5M × $90.54) → 63,088 | **$3.89** |

**TRV returned 78.5% of twelve years' net income to owners and every dollar it kept is carried at
about $3.90 of market value.** Book value per share went from roughly $70.55 (2013) to $151.21
(2025), +114% or 6.6% a year, while paying a dividend throughout and retiring 41% of the shares.
**[E2-52]**'s dividends-funded-by-issuance flag is not merely absent — it runs the other way.
**[E2-51]**'s refusal-to-repurchase tell is also absent.

**[E3-58] / [E2-56]:** no visibly outsourced allocation, no serial banker-led M&A, and the
segment-by-segment retention judgment is possible because the filer reports three segments with
their own investment-income allocation. The incremental capital has gone into the personal-lines
book at a 50.6% price increase and an 8.7% unit decline — which is a **Q2** judgment about the
business, already made, and is not re-scored here as a management failing.

**THE GUARDRAIL — checked before writing the verdict.**
- [x] Confirmed: nothing in this Q3 is used to promote the name. **[E2-37]**: *"a textile company
      that allocates capital brilliantly within its industry is a remarkable textile company — but
      not a remarkable business."* A 41% share retirement at $3.90 of market value per dollar
      retained is a remarkable **capital-allocation** record inside a business Q2 found is not a
      franchise, and **[E3-39]** governs: *averaged out, bet on the business.*
- [x] No key-person dependence found; recorded at Q2 as a non-finding rather than a strength.
- [x] No great-manager-as-the-plan case is being made.

**VERDICT: [x] IN (no disqualifier found) — RECORDED, NOT GOVERNING.** Two prompts fired
(catastrophes normalised out of the pay metric; buybacks at 2.4-2.5x book with no published
valuation discipline and [E4-31]'s third condition failed) and neither is a conduct finding.
**Per [E5-17] this is the absence of found disqualifiers and NOT a finding that the managers are
honest** — *"sincerity and empathy can easily be faked"*, and **[E5-32]**'s reminder that the filed
statement is not bedrock applies with full force to a filer whose principal liability is an
estimate. **IN never promotes, and here it cannot: Q2 already closed the file.**

---
## Q4 — WILL IT SURVIVE?
### ⚠️ RECORDED, NOT GOVERNING. Q2 closed the file OUT.

**THE SECTOR METHOD'S SUBSTITUTIONS ARE USED, NOT THE ORDINARY CONSTRUCTION.** The ordinary
owner-earnings construction is **refused here and the reason is named**: it would compute a yield
from $10,606M of 2025 operating cash flow, which contains the coupons and dividends of a $101bn
portfolio, and then count that portfolio again as component 1. **[E5-48]**: *"We exclude in the
second factor the dividends and interest from the investments we hold because including them
would produce a double-counting of value."* There is no windage that repairs that; it is an
arithmetic error, and the sector method exists to prevent exactly it. **`arith.py` computes no
operating-cash-flow yield for this name.**

### Step 2 of the method — THE COST OF FLOAT, BY YEAR **[E3-69]**

*"A comparison of underwriting loss to float developed … A low cost of funds signifies a good
business; a high cost translates into a poor business."* Float is constructed by **CONVENTION 4**
of the sector method (the WTM run's recipe, which reproduced Markel's first published float figure
to within 1.1%): *loss and LAE reserves + unearned premiums − reinsurance recoverables − premiums
receivable − deferred acquisition costs.* **A negative cost means the float was not merely free —
TRV was paid to hold it.** `arith.py` sections B and C:

| year | GAAP underwriting result $m | float, year-end $m | float, average $m | **cost of float** |
|---|---|---|---|---|
| 2016 | 1,325 | 43,346 | 43,208 | **−3.07 %** |
| 2017 | (120) | 45,087 | 44,216 | **+0.27 %** ← the one year it cost anything |
| 2018 | 90 | 46,227 | 45,657 | **−0.20 %** |
| 2019 | 173 | 48,036 | 47,132 | **−0.37 %** |
| 2020 | 639 | 51,206 | 49,621 | **−1.29 %** |
| 2021 | 837 | 54,297 | 52,752 | **−1.59 %** |
| 2022 | 584 | 57,068 | 55,682 | **−1.05 %** |
| 2023 | 144 | 60,768 | 58,918 | **−0.24 %** |
| 2024 | 2,090 | 63,778 | 62,273 | **−3.36 %** |
| 2025 | 3,307 | 65,772 | 64,775 | **−5.11 %** |
| **10-year, 2016-2025** | **9,069 total, 907 mean** | | **52,423 mean** | **−1.73 %** |

**CONVENTION 2 of the sector method requires the window to be stated: ten years, 2016-2025.**
2014-2015 are computable and are **excluded on purpose** — the reinsurance-recoverables concept
TRV tagged for 2014 returns $4,067M against $8,910M in 2015, which is a tag break rather than a
$4.8bn one-year movement, and a float series built through it would be wrong. **[E3-69]** forbids
short windows *"in either direction"* per the sector method's reading of **[E5-49]**, including a
flattering one, which is why the −5.11% of 2025 is not the reported figure and −1.73% is.

**Read against the sovereign exactly as owner earnings are:** TRV is paid **1.73%** to hold
other people's money while the 30-year Treasury pays **5.34%** to borrow. **That is a funding
advantage of about 7 percentage points on an average $52.4bn — roughly $3.7bn a year of value
created by the float mechanism alone**, and it is the single strongest economic fact in this file.
**[E3-52]** applies in full: *"liabilities without covenants or due dates attached to them … they
give us the benefit of debt … but saddle us with none of its drawbacks."*

**And float is growing, which is what makes the [E5-46] treatment applicable at all:** $43.3bn
(2016) to $65.8bn (2025), +51.8%, 4.8% a year. A shrinking insurer's float is a repayment
schedule; a growing one's is a perpetual loan.

### Step 1 of the method — INVESTMENTS AT MARKET **[E5-46]**, with the items the MKL run found missing

| | at 2026-06-30 | at 2025-12-31 |
|---|---|---|
| Fixed maturities, available for sale, at fair value | $92,922M | $89,833M |
| Equity securities, at fair value | 652 | 618 |
| Real estate investments | 884 | 900 |
| Short-term securities | 4,579 | 5,716 |
| Other investments | 4,142 | 4,115 |
| **Total investments, at market** | **$103,179M** | **$101,182M** |

- **GROSS OR NET? — the ambiguity the MKL run found worth $23.1bn there is worth NOTHING here,
  and that is the answer rather than an evasion.** TRV's consolidated balance sheet carries **no
  noncontrolling-interest line and no finance-operation borrowings offset against investments.**
  Gross equals net. **Figure used: gross at market, because it is also net.**
- **DEFERRED TAX, per [E3-71] — and the sign is the reverse of Wesco's.** Munger valued a
  deferred tax **liability** as the advantage of an interest-free loan, *"never at face and never
  at zero."* **TRV carries a net deferred tax ASSET of $1,041M at 2026-06-30** (up from $887M),
  created largely by the unrealised losses on the bond portfolio. There is no interest-free loan
  to value; there is a real asset whose realisation depends on future taxable income. **It is
  carried at its filed value and the treatment is stated rather than inherited from [E3-71],
  because [E3-71] does not reach this sign.**
- The 94%-fixed-income composition is the relevant fact for what this portfolio can earn: average
  pre-tax yield on average investments of $104,239M in 2025 was **3.80%** ($3,959M ÷ $104,239M).

### Step 3 of the method — EARNINGS FROM EVERYTHING THAT IS NOT THE PORTFOLIO **[E5-47, E5-48]**

Pre-tax, **including underwriting income** per the filer's own 2015 amendment **[E5-48]**, with
the dividends and interest of step 1 **removed** to avoid the double count, after overhead,
interest, depreciation, amortisation and minorities, before tax. Computed as *income before income
taxes less net investment income less net realised investment gains*, and cross-checked against
the components:

| year | pre-tax income $m | less net investment income | less net realised gains | **COMPONENT 2 $m** |
|---|---|---|---|---|
| 2016 | 4,053 | 2,302 | 68 | **1,683** |
| 2017 | 2,730 | 2,397 | 216 | **117** |
| 2018 | 2,961 | 2,474 | 114 | **373** |
| 2019 | 3,138 | 2,468 | 113 | **557** |
| 2020 | 3,237 | 2,227 | 2 | **1,008** |
| 2021 | 4,458 | 3,033 | 171 | **1,254** |
| 2022 | 3,354 | 2,562 | (204) | **996** |
| 2023 | 3,371 | 2,922 | (105) | **554** |
| 2024 | 6,180 | 3,590 | (30) | **2,620** |
| 2025 | 7,796 | 3,959 | (48) | **3,885** |
| **10-year mean** | **4,128** | **2,793** | | **1,305** |
| **5-year mean 2021-25** | **5,032** | **3,213** | | **1,862** |

**Cross-check, 2025:** underwriting result $3,307M + fee income $495M + other revenues $508M −
interest expense $425M = **$3,885M**, identical to the subtraction. The construction is sound.

**Component 2 has a 33-fold range across the window ($117M in 2017 to $3,885M in 2025) and a
ten-year mean of $1,305M.** **[E5-49]** applies word for word: *"underwriting in any given year
could well be unprofitable, perhaps substantially so."* Anyone valuing this name off 2025's
$3,885M is valuing the best year of twelve as the normal one.

### The third element — THE RETAINED-EARNINGS JUDGMENT **[E5-50]**, stated and not silent

*"Some companies will turn these retained dollars into fifty-cent pieces, others into two-dollar
bills … If a CEO can be expected to do this job well, the reinvestment prospects add to the
company's current value; if the CEO's talents or motives are suspect, today's value must be
discounted."*

**JUDGMENT: NEUTRAL TO MILDLY POSITIVE, and the reasoning has two halves that point opposite ways.**

- **In favour — the measured record, [E3-54]'s dollar-for-dollar test.** $3.91 of market value per
  $1 retained on the five-year rolling window, $3.39 over ten years, $3.89 over twelve. Two-dollar
  bills, on the corpus's own measurement. **And most of the capital was not retained at all**:
  78.5% of twelve years' earnings were returned, 41% of the shares retired, and no large
  acquisition was made with the rest. A company that mostly hands the money back cannot turn it
  into fifty-cent pieces.
- **Against — where the retained dollars actually went, and at what price.** The incremental
  capital financed a personal-lines book whose unit count fell 8.7% from its 2022 peak and whose
  price rose 50.6%, and $3,004M of 2025 buybacks plus $3,100M in the first half of 2026 were
  transacted at 2.4-2.5x book with **no published valuation discipline and [E4-31]'s third
  condition unmet.** The 2020-versus-2025 spending pattern — least when cheapest, most when
  dearest — is the wrong way round on **[E5-24]**.
- **So the judgment is stated as: no upward adjustment for reinvestment prospects, and no
  downward one.** The measured record earns the "no discount"; the absence of any published
  repurchase discipline forfeits the premium. **[E2-62]** is also recorded: this is not a small
  Berkshire and the licence to concentrate does not transfer.

### Great, good, or gruesome? **[E4-20]**

- [ ] great — [x] **GOOD** — [ ] gruesome
**GOOD, and [E4-43] is explicit that the good class passes:** capital-hungry growth *"may well
prove to be a satisfactory investment."* Evidence: a ten-year mean ROE of ~13% (10.5-15.8% on
AOCI-adjusted equity in the recent good years), earned also on added capital — premium grew 79%
over 2016-2025 on equity up 42%. **[E5-40]**'s ~12% on retained capital as *"quite satisfactory"*
is the right benchmark and TRV meets it. **Not great:** the return is cyclical (8.8% in 2017,
20.7% in 2025), it needs capital to write more premium, and 71% of it comes from a bond portfolio
whose yield is set by somebody else. **Not gruesome:** the cash it consumes plainly does earn a
reasonable return.

### Staying power — score all three **[E5-11]**, with the sector method's substitutions

1. **(1) A large and reliable stream of earnings — YES, and it is the most reliable thing here.**
   $3,959M of pre-tax net investment income in 2025 from a 94% fixed-income book; profitable every
   year for twelve; operating cash flow $10,606M in 2025 and positive in every year on record.
2. **(2) NOT cash on hand — read as RESERVE ADEQUACY and NET WORTH [E2-61].** *"You can be broke
   but flush … insolvent insurers don't run out of cash until long after they have run out of net
   worth."* TRV's $10.6bn of operating cash flow is therefore **not** scored as a strength.
   What is scored: **net favourable prior-year development in nine of ten years**, group-level
   reserve redundancy that has been realised rather than asserted, and **net worth of $33,121M
   against claim reserves of $67,226M** at 2026-06-30 — 2.03x, which is unexceptional for the
   line mix. **The qualification from Q3 is carried here and not softened:** the redundancy sits
   in workers' compensation, it is being spent (24.4% of AY2016 down to 0.1% of AY2023), and
   general liability has taken 7-28% for eight consecutive accident years. **PASS, with the
   cushion measurably thinning.**
3. **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — YES, and this is the one that usually
   kills.** Debt $9,068M at 2026-06-30 against $33,121M of equity, debt-to-total-capital 22.0%.
   $200M of senior notes matured 2026-04-15 and were repaid. **$100M** of commercial paper
   outstanding, with the filer's own statement that *"TRV is not reliant on its commercial paper
   program to meet its operating cash flow needs."* A $1.2bn undrawn facility runs to 2031-05-15
   and the covenant is a change-of-control test the filer confirms it complies with. Holding
   company liquidity $2.41bn. **[E2-54]**'s coverage test: interest expense $425M against $7,796M
   of pre-tax income is **19.3x**, and against the ten-year mean pre-tax income of $4,128M it is
   **10.7x** — comfortably met out of current cash flow. **[E5-39]**'s kindness of strangers is
   not depended on.

**Leverage, named and quantified — there is no ratio ceiling in this framework and the corpus
supplies none [E4-16, E3-29].** Financial debt is modest at 22.0% of capital. **The leverage that
matters is not the debt:** total assets $143,580M on equity $33,121M is **4.34x**, investments are
**3.08x** equity, and claim reserves are **2.03x** equity. **A 5% under-reserve is $3.4bn, or
10.2% of equity; a 10% under-reserve is 20.3% of it.** That is the quantification, and it is why
Q3 was a binary gate.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24]** — and model exposure, not experience **[E4-40]**

**Against `Screens/SURVIVAL SHAPES - index.md`: shape #11, THE PASS-THROUGH, is the mechanism,
with shape #7, THE LONG TAIL ON A SHORT CYCLE, as its feature. No new shape is proposed.**

- **#11 THE PASS-THROUGH** (first named by TM, 2026-09-13): *the company survives but gains are
  passed to customers and suppliers, compressing the owner's return.* In insurance the customer
  takes the gains back through the soft market, and **[E2-58]** names the machinery: *"persistent
  over-capacity without administered prices (or costs) equals poor profitability"*, long-run
  profitability set by *"the ratio of supply-tight to supply-ample years"*, and prosperity
  breeding the next glut — *"nothing fails like success."*
- **#7 THE LONG TAIL ON A SHORT CYCLE** (first named by CNR, 2026-09-13): *decades-long claims
  fixed in dollars against a years-long price cycle, the balance sheet the only buffer.* TRV's
  general liability triangles and its $1.36bn of asbestos reserves, strengthened every year for
  at least three, are that feature exactly.

**THE MECHANISM, QUANTIFIED FROM FILED FIGURES, [E3-24]'s own form.** *Consider some mathematics.*
Two things happen together, and neither is hypothetical — both have happened inside this window:

1. **The soft market returns and the current-accident-year combined ratio goes back through 100,
   as it did in 2017 (100.2).** Apply 2017's ratio to 2025's $43,914M of earned premium: the
   underwriting result becomes **−$88M against 2025's +$3,307M, a $3,395M pre-tax swing.** This is
   not a forecast; it is TRV's own realised ratio from the last soft market, and its own 2025
   filing records renewal premium changes *"lower than in 2024"* in Select Accounts, Middle
   Market and National Accounts alike.
2. **A single retention-level catastrophe.** Modelled from **exposure, not experience** [E4-40]:
   the FY2025 10-K discloses a corporate catastrophe treaty attaching at a **$3.0bn retention**
   (with a $100M per-occurrence deductible), a Northeast Property treaty at a **$2.75bn
   retention**, and a Personal Insurance treaty at a **$1.0bn retention**. **So one event inside
   the corporate retention costs up to $3.0bn net**, and TRV's own disclosure that *"approximately
   37% of its annual catastrophe losses"* arrive in the second quarter says the load is not
   diversified across the year.

**Both together: a pre-tax swing of roughly $6.4bn against 2025's $7,796M of pre-tax income and
$32,894M of equity.** Continuing net investment income of about $4.0bn means the company is
**roughly break-even to modestly profitable pre-tax, not loss-making**; equity absorbs perhaps
$1-2bn after tax; interest cover on $425M stays above 5x on investment income alone. **The
company does not die.** That is the honest conclusion and it is the conclusion **[E5-29]** demands
— risk here means impairment, never price movement.

**What dies is the owner's return, and the filed record shows exactly how much.** In 2017, the
last year this happened, TRV earned **$2,056M**, an **8.8% ROE**, and **$7.58** of diluted
earnings per share. At today's $374.62 that is a **2.0% earnings yield**, and diluted earnings per
share two-thirds below 2025's $27.43. **The third element of the death is that it need not
reverse:** the workers' compensation redundancy funding 1.6 points a year of reported combined
ratio is measurably running out (24.4% of AY2016 down to 0.1% of AY2023), and the catastrophe load
has gone from 3.1 to 8.4 points in six years. **A soft market arriving after the reserve cushion
is spent and with a doubled catastrophe load is a worse soft market than 2017's.**

**Likelihood: [ ] likely  [x] A REAL POSSIBILITY  [ ] a low-level possibility.** Stated in that
vocabulary because the pricing deceleration is already in the filings, the reserve cushion's
decline is already in the triangles, and only the catastrophe timing is unknown.

**VERDICT: [x] IN on survival — RECORDED, NOT GOVERNING.** All three **[E5-11]** strengths score,
with the reserve cushion flagged as thinning; the class is GOOD, not great **[E4-20, E4-43]**; the
cost of float is −1.73% over ten years **[E3-69]**; and the named death compresses the owner's
return without threatening the company. **This gate would have closed IN. It does not matter,
because Q2 closed the file on the business.**

---
## Q5 — COMPUTATION — NOT A CLEARANCE
### ⛔ Q2 returned OUT. Q5 IS NOT OPEN. Per operator rule 3 this arithmetic carries that heading and **may carry no entry language.**

**The price, dated, with the aggregator flagged**
- **US$374.62**, close of **2026-09-18**. Source: Yahoo Finance via `tools/sources.py:price()` —
  **an aggregator, used for the live quote only, and flagged as such.**
- **Shares: 208,575,022**, cover of the 10-Q for Q2 2026, accession 0000086312-26-000145. Both
  cover checks passed at Step 0.
- **Market capitalisation: US$78,136M.** Book value per share at 2026-06-30 was $158.78
  ($33,121M ÷ 208.6M shares), so the quote is **2.36x book**.
- **Sovereign: 5.34%**, US Treasury 30-year par yield, 2026-09-18, issuing authority.

**WHAT THE BUYER IS PAYING FOR, IN WORDS — which is what this section is for.**

At $374.62 the buyer is paying **$78.1bn** for: a **$103.2bn** securities portfolio, 94% of it
bonds yielding **3.80% pre-tax**, of which **$65.8bn is funded by policyholders at a cost of minus
1.73% a year**; plus a US property-casualty underwriting operation that has produced a mean of
**$1,305M a year pre-tax before any investment income** over ten years, ranging from $117M to
$3,885M; plus **$4.1bn of goodwill and intangibles**; less **$9.1bn of debt**. In one sentence:
**the buyer is paying 2.36 times book for a levered bond portfolio, and the underwriting business
that makes the leverage cheap earns a thin, cyclical margin of which roughly a third has been
prior-year reserve releases for ten years.**

**The two constructions disagree, and both are reported rather than one being chosen.**

**(a) The earnings-yield construction — the floor test [E4-28].** *"That's the figure we quit on."*

| basis | pre-tax income | **pre-tax yield on $78,136M** | after-tax | after-tax yield |
|---|---|---|---|---|
| 10-year mean 2016-2025 | $4,128M | **5.28 %** | $3,369M | 4.31 % |
| 5-year mean 2021-2025 | $5,032M | **6.44 %** | $4,156M | 5.32 % |
| 2025 alone, the best year of twelve | $7,796M | 9.98 % | $6,288M | 8.05 % |

**Against the ~10% floor: 5.28% on the ten-year mean and 6.44% on the five-year mean. The name
does not clear the floor on any honest multi-year construction, and clears it only on the single
best year in twelve.** Against the **5.34%** sovereign, the ten-year mean pre-tax yield of 5.28%
is **0.06 points BELOW the long bond** and the five-year mean is **1.10 points over it**.

**(b) The sector method's two-component construction [E5-46], which points the other way and must
be reported honestly.** Component 1 is **$103.2bn** of investments at market — **1.32 times the
entire market capitalisation**, before component 2 is counted at all. On Berkshire's own
arithmetic the buyer gets the $103.2bn portfolio and the underwriting business, the fee businesses
and the surety franchise for nothing, and pays 76 cents on the dollar for the securities.

**Why that is not a screamer [E4-01], and this is CONVENTION 5 of the sector method doing its
job.** **[E5-46]** licenses counting the whole portfolio *"as an element of value"* on one stated
condition — that underwriting breaks even, so the float funding it is free. **At investments of
3.08x equity, against Berkshire's 0.45x and Markel's 2.01x, essentially the entire gap between
the $103.2bn and the $33.1bn of equity rests on that condition**, which the same passage calls
*"volatile, swinging erratically between profits and losses."* TRV's ten-year record supports the
condition (current-accident-year combined ratio under 100 in nine of ten years; cost of float
−1.73%), which is why the construction is legitimate and is reported. **But a 1.32x asset-to-price
ratio built on a condition that failed once in ten years, in a portfolio carried at market and
already showing $1.86bn of unrealised losses, is not the thing [E3-65] describes** — the
Washington Post at *"about 20 percent of the value to a private owner … with the structure and the
managers aligned."* It is a modest discount to gross assets on a levered balance sheet.

**The two constructions reconcile, and the reconciliation is the answer.** They differ only in the
rate at which component 2 is capitalised. Capitalise the five-year mean pre-tax $5,032M at the
**5.34%** sovereign and the value is about **$94bn**, above the price. Capitalise it at the **10%**
floor and it is about **$50bn**, well below. **This is the same shape the BRK run of 2026-09-02
recorded and named: above the bond, below the floor.** **[E4-28]** settles which governs — *"we
don't want to buy equities where our real expectancy is below 10 percent … that's true whether
short rates are 6 percent or whether short rates are 1 percent."*

**What the price already assumes.** To justify $78.1bn at a 10% pre-tax expectancy the business
must earn **$7.8bn pre-tax, sustained** — which is 2025's figure, the best of twelve, requiring
**+55% against the five-year mean and +89% against the ten-year mean, permanently.** Against
**[E4-35]**'s base rate — *"fewer than 10 of the 200 most profitable companies … will attain 15%
annual growth in earnings-per-share over the next 20 years"* — and against **[E4-44]**'s bound
that value *"cannot over the long term grow faster than its earnings do"*, that is the Tinker Bell
assumption the corpus refuses. **State the ceiling too [E2-63]:** the upside here is capped by the
portfolio yield, because 71% of the earnings are a bond coupon, and a bond's upside is its face.

**Where certainty is priced, and it is NOT in the rate [E3-42].** Sovereign used **5.34%**, the
bare rate, **no per-name premium added**. Certainty is handled at the understanding gate and in
the end discount, once, and may not be stacked **[E4-11, E4-48]**.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — and the range is where the conclusion lives:
- **conservative: roughly $50bn** (five-year mean pre-tax capitalised at the [E4-28] floor,
  which is the construction the framework's buying rule uses)
- **optimistic: roughly $95-105bn** (five-year mean capitalised at the sovereign; or component 1
  at market with component 2 free)
- **current price: $78.1bn** — **inside the range.**

**Which bar? [x] The screamer test [E4-01].** Three outcomes, and this is the middle one:
**the price sits inside the range, so no useful conclusion can be reached, and that IS the
answer** — *"Usually, the range must be so wide that no useful conclusion can be reached."* The
normal-method bar is **not** run and no margin is applied, because Q2 already returned OUT and a
margin computed below a failed gate would be theatre.
**Windage count: ONE** — the conservative end of the Q4 component range (the ten-year rather than
the 2025 figure). Conservatism is spent once **[E4-11]**.

**VERDICT: NOT OPEN. Q2 OUT closed the file.** Had Q1-Q4 all been IN, the floor test at
**[E4-28]** would have returned **FAIL on price: 5.3-6.4% honest pre-tax expectancy against a
~10% floor — quit on, not ranked** — above the bond on the five-year mean, below the floor on
every mean, and the screamer test lands inside the range. **No ranking position is recorded,
because a name that failed Q2 is not in the opportunity set at any price [E5-35]:** *"You can turn
any investment into a bad deal by paying too much. What you can't do is turn any investment into a
good deal by paying little."*

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
### There is no position, so this records the falsifiers **[E1-02]** — what would overturn the Q2 OUT.

**The Q2 OUT is a finding about the business and [E4-19] makes it permanent. It is nonetheless
written down what would refute it**, because a verdict whose falsifier cannot be named is an
opinion. **[E4-26]**: hunt disconfirming evidence hardest for your favourite hypothesis, and the
favourite hypothesis in this file is the OUT.

**What would refute the Q2 OUT — three pre-committed, filing-checkable conditions:**
1. **TRV's current-accident-year combined ratio holds below 94 through a soft market**, measured
   the way this file measures it (reported plus favourable prior-year development), for three
   consecutive years in which the filing reports renewal premium change **decelerating**. That
   would show the 2024-25 result was position rather than the wave **[E3-51, E4-36]**.
2. **The domestic Personal Insurance policy count stops falling and turns up while premium per
   policy holds**, on the 10-K's own annual figure (8.4M at 2025-12-31 is the base) and on the
   quarterly policies-in-force lines in the furnished supplement. This is **[E4-55]**'s physical
   series and it is the honest one.
3. **The underwriting expense ratio resumes falling toward Progressive's and Allstate's 21%**, from
   28.5%. That would create the **[E2-58]** exception TRV does not currently have.

**What would confirm it — the thesis-breaking metric for anyone who reaches the opposite view:**
- **The reserve cushion runs out.** Threshold, pre-committed: **net favourable prior-year
  development below 1.0 point of the combined ratio for two consecutive years** (it has averaged
  1.6 points for ten years), or **workers' compensation favourable development on the three most
  recent mature accident years below 2%** (already 0.1% on AY2023). Source: note 8 triangles and
  the MD&A's prior-year-development points, annually.
- **The catastrophe load passes 10 points** of the combined ratio (8.4 in 2025, 3.1 in 2019).
- **General liability adverse development continues on accident years 2024 and 2025**, which are
  the years written at the top of the pricing cycle and should be the most redundant.

**Next catalyst date: the Q3 2026 earnings 8-K, expected mid-October 2026** — TRV has furnished
its third-quarter release on 2025-10-16, 2024-10-17 and 2023-10-18. **It carries the annual
in-depth asbestos review, which has produced a charge of $277M, $242M and $284M in the last three
third quarters.**

**No alert band is armed and no PORTFOLIO row is added.** Per the fold rule and the QLYS ruling of
2026-09-07: **a name that failed at Q2 failed on the BUSINESS, and a price alert on it would be a
category error.** The reversal condition is recorded in words above instead.

**VERDICT: [x] OUT, inherited from Q2.** Nothing to sell and nothing to monitor as a holding.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, **Q2 OUT — the run stops there**;
      Q3 and Q4 are written and each is headed **RECORDED, NOT GOVERNING**; Q5 carries
      **COMPUTATION — NOT A CLEARANCE** per operator rule 3 and contains no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** The competitor row
      is complete for 13 of 14 names; FFH is marked NOT COMPARABLE with the reason, and the moat
      class is **NONE**, not PROVISIONAL, so no gate rests on the missing cell.
- [x] Every UNRESEARCHED verdict names the artifact — **there are none.** Q2's OUT explicitly asks
      [E4-19]'s separating question and answers that no document is missing.
- [x] Every UNKNOWABLE verdict states what cannot be known — **there are none.**
- [x] Step 0: the filing was read with accession numbers; **two** figures cross-checked against
      the filed statements; the 8-K EX-99.1 and EX-99.2 were pulled before scoring [E4-29].
- [x] Owner earnings: **the ordinary construction is refused and the refusal is justified from
      [E5-48]**, because it would double-count a $101bn portfolio. The sector method's three
      substitutions are used instead, the float window is stated (ten years, 2016-2025, per
      CONVENTION 2), and the two excluded years are named with the tag reason.
- [x] Competitor row filled — 13 names, six of them new in this run, eight carried from the MKL
      row via the CB run, each cell sourced to a filer's own 10-K with the accession number, and
      the two comparability limits (CNA flattered, HIG segment-level) disclosed.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated 2026-09-18; the
      sector method's open FINDING 8 is checked against the filing and does not bite.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (the screamer test), not both; **windage count: one.**
- [x] Prices dated; the aggregator is used for the live quote only and is flagged twice.
- [x] **Every ledger id cited in this file was checked against `principle_ledger.csv` before
      citing it.** The file holds **267 rows**; all ids used resolve. *(CLAUDE.md said 117 until
      commit e60bcdc earlier today; the brief's warning was correct and the check was run anyway.)*
- [x] Run committed to git, in five commits with pathspecs.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** *Travelers is a well-run, honestly-reported, comfortably solvent insurer that is
  paid 1.73% a year to hold $65.8bn of other people's money — and it is not a franchise: about
  half the states must approve its rates before use, it is tenth of thirteen peers on the
  current-accident-year combined ratio and fourth of the six it actually competes with, the one
  cost-advantage exception [E2-58] allows is held seven points wide by Progressive and Allstate in
  the lines it is growing, and it has shed 800,000 personal-lines policies from its 2022 peak
  while raising price per policy 50.6%.*
- **Price US$374.62** (close 2026-09-18, aggregator flagged) · **shares 208,575,022** (10-Q cover
  2026-07-10, accession 0000086312-26-000145) · **cap US$78,136M** · **sovereign 5.34%** (US
  Treasury 30-year, 2026-09-18) · **FAIL at Q2, OUT on the business.**
- Below-gate note, not a clearance: honest pre-tax expectancy **5.3% (10-yr mean) to 6.4% (5-yr
  mean)** against the ~10% floor **[E4-28]**; above the bond on the five-year mean, below the
  floor on every mean — the BRK shape, at a much lower quality of business.

---
## DEFECTS FOUND — in the brief, the sector method, and the tooling

### 1. TOOLING — the tag-union defect, live in a second place
`tools/sources.py:annual()` carries a docstring warning that *"filers switch concepts
mid-history … A tag list is a UNION"*, added 2026-08-27 after Apple's operating-cash-flow series
was silently truncated. **The same defect bit this run twice**, in a script written fresh:
- `us-gaap:GeneralAndAdministrativeExpense` covers TRV **2007-2014 only**; from 2013 the filer
  uses `SellingGeneralAndAdministrativeExpense`.
- `us-gaap:ReinsuranceRecoverables` covers **2008-2014 only**; from 2012 the filer uses
  `ReinsuranceRecoverablesOnPaidAndUnpaidLosses`.

**The first draft of `arith.py` therefore returned a twelve-year table containing one year, 2014,
and it looked like a complete table.** It did not error and it printed a mean. **The prompt: a
single-tag read that silently returns one row is indistinguishable from a company with one year of
history**, which is the BE run's Q4 shape (survival shape #3, "too little filed history"). A
diagnostic worth adding to any run script is an assertion that the series length matches the
window requested. Recorded rather than fixed, because `tools/` is outside this run's remit.

### 2. TOOLING — the reinsurance-recoverables tag break makes 2014 unusable, and nothing says so
The union fix above produces **$4,067M for 2014** against **$8,910M for 2015** — a $4.8bn
one-year move that is a concept break, not a balance-sheet event. **A float series run through it
would show float falling $6.4bn in 2015 and would put a spurious −4.06% into the cost-of-float
table's first row.** This run excluded 2014-2015 and said why. **No tool in `tools/` detects a
level discontinuity at a tag boundary**, and one would be cheap: flag any year-over-year move
above some multiple of the series' own volatility that coincides with a change in the tag
supplying the value. *(Stated as a prompt for the operator, not built: "does it get the same
number sooner, or does it add a number?" — this removes friction from a check the run already had
to do by hand, so it qualifies.)*

### 3. SECTOR METHOD — step 1 has no rule for a deferred tax ASSET, and [E3-71] does not reach it
The second amendment says *"Step 1 had no deferred-tax rule, though [E3-71] supplies one"*, and
directs the run to value the deferred tax **liability** as an interest-free loan, *"never at face
and never at zero."* **TRV carries a net deferred tax ASSET of $1,041M**, created by unrealised
losses on a bond portfolio held at market. **The instruction has no sign.** An interest-free loan
received is worth more than face; an interest-free loan *made* is worth less — and a deferred tax
asset is closer to the second. This run carried it at filed value and said so. **This is the
mirror of FINDING 8: a gap named rather than papered over**, and a filer holding bonds at market
in a rising-rate world is the ordinary case for it, not an exotic one. **PRIME RULE 5 applies —
it needs a written case with quotes before the method is amended, so nothing is amended here.**

### 4. SECTOR METHOD — CONVENTION 5's ratio has no upper commentary, and TRV is the high case
The first amendment guards the **low** side of float ÷ investments (WTM at 22.0%) and the second
amendment introduces investments ÷ equity as the ratio that *"measures how much the answer depends
on that condition"*, with Berkshire at 0.45x and Markel at 2.01x. **TRV is 3.08x — half again
Markel's — and the document says of the ratio only "neither is a threshold and neither
disqualifies a name."** That is right as far as it goes, but the method gives a run no language for
the high end, where the [E5-46] gross-asset construction produces a number **32% above the entire
market capitalisation** and could be reported as a screamer by a run that did not stop to ask what
funds the assets. **This run wrote that language itself at Q5(b).** The prompt for the operator:
the low-side guard has a sentence and the high side does not, and the high side is where the
method can flatter rather than merely mislocate.

### 5. SECTOR METHOD — the cost of float is defined but its SIGN CONVENTION is not
**[E3-69]** speaks of *"underwriting loss to float developed"* and *"a low cost of funds."* Every
name this method has met so far has had an underwriting **loss** in at least some years. **TRV has
an underwriting gain in nine of ten**, so the ratio is negative throughout, and "a low cost" and
"a negative cost" are different claims that the method's step 2 does not distinguish. This run
adopted the convention that **negative = paid to hold the money** and stated it in the table
header. **It is not in the document and should be**, because a run that reported "cost of float
1.73%" rather than "minus 1.73%" would have inverted the single most important economic fact about
the company. *(Confessed as this run's convention, per PRIME RULE 3.)*

### 6. THE BRIEF — one instruction could not be executed as written, and the reason is a finding
The brief said, of personal lines: *"test what filed retention and renewal price change did
together."* **Neither is filed as a number.** The FY2025 10-K gives only adjectives for Personal
Insurance ("retention rates remained strong", "renewal premium changes remained positive but were
lower than in 2024"), and the furnished EX-99.2 supplement carries no retention or renewal-premium
table for any segment. The quantified series exists only in the earnings-call presentation, which
is neither filed nor furnished. **The brief assumed a disclosure that does not exist** — the same
class of error the sector method's own FINDING 1 records about float at White Mountains, where the
document *"assumed a number that most filers do not report."* **The substitute this run used is
better, not worse: the policies-in-force series, which TRV does publish annually and quarterly,
and which [E4-55] says is the honest series anyway.**

### 7. THE BRIEF — everything else in it held, and two of its warnings earned their keep
- The **fold trap** warning was correct: `## COMPLETED FROM THE QUEUE` appears twice in
  `Screens/WATCHLIST RUN QUEUE.md`, at the register heading and inside the FOLD instructions. The
  fold below anchors on a line-start regex and counts entries in the slice before and after.
- The **ledger-count** warning was correct: 267 rows, and every id was checked.
- The **MKL precedent** instruction to *extend the row, do not rebuild it* was followed, and it
  saved the run the whole specialty-peer leg. **A second finding for the queue: the row had
  already been extended once today by the CB run, and that extension was on disk and committed
  (7d1e022) before this run started.** Extending an extension worked; the provenance of every
  carried cell is recorded in `peers/row_out.md` so a third run can do it again.
- **A prior TRV session had died in this tree at about 10:43 today**, leaving fetched 10-Ks for
  2016, 2018, 2019, 2021, 2022, 2024 and 2025, the Q2 2026 supplement, the proxy, and a
  substantially complete CNA extraction (`peers/data_CNA.json`) — none of it committed, all of it
  usable, and the CNA cell of this run's competitor row rests on it. **That is the write-early
  protocol paying off across sessions rather than within one**, which the protocol does not
  currently claim and could.
