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

