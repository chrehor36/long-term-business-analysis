# Company Run — Dell Technologies Inc. (DELL) — 2026-09-07
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

---
## STATUS — WRITE-EARLY PROTOCOL
- [x] file created before fetching (2026-09-07)
- [ ] Step 0
- [ ] Q1
- [ ] Q2
- [ ] Q3
- [ ] Q4
- [ ] Q5 / computation
- [ ] Q6
- [ ] self-audit + fold

---
## THE SCREEN ROW AS DELIVERED — a prompt to read, never a score (operator rule 8)

```
cap_m 295522 | oe_bottom_m 3231 | oe_top_m 4652 | spread 0.44
yield_bottom 1.09% | vs_sovereign -4.15 pts | growth_required 8.91%
level_shift 1.01 "no step"          level_shift_oe n/a  "EARLY HALF STRADDLES ZERO"
best_year_dep 0.051 "none"          best_year_dep_oe 0.081
flags_disagree: FLAGS DISAGREE - one series refuses the ratio and the other does not
acq_note: NET CASH INFLOW on the acquisition line ($4,237M, 1% of cap)
newest_filing 2026-01-30
```

*(sections appended as they close)*

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.24 %** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-yr
  (the issuing authority; not FRED)**
- FX: none. Dell reports in USD; 55.6% of FY2026 revenue was United States ($63,140M of
  $113,538M) and no single foreign country reached 10%. Earnings currency is USD.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary document · date · accession:** Form **10-K for fiscal 2026 (year ended
  2026-01-30)**, filed **2026-03-16**, accession **0001571996-26-000008**
  (`dell-20260130.htm`).
- **Also read:** Form **10-Q for Q1 FY2027 (quarter ended 2026-05-01)**, filed **2026-06-09**,
  accession **0001571996-26-000030** — this is the **LATEST periodic filing** and the share
  count comes off its cover. And Form **10-K for fiscal 2023 (year ended 2023-02-03)**, filed
  **2023-03-30**, accession **0001571996-23-000007** — needed for the VMware perimeter and for
  the negative owner-earnings year.
- **Figures cross-checked against the filed statement:**
  1. The **segment note reconciles to the dollar.** ISG gross profit computed from the
     significant-expense-category table ($60,826M revenue − $45,022M cost of net revenue =
     $15,804M) less ISG SG&A $6,457M less ISG R&D $2,236M = **$7,111M**, which is exactly the
     filed ISG operating income. The same identity holds for FY2025 ($14,241 − 6,593 − 2,069 =
     $5,579M) and FY2024 ($12,942 − 6,752 − 1,904 = $4,286M). This is the arithmetic Q2 turns
     on, and it is internally consistent in the filing.
  2. Consolidated gross margin $22,707M ÷ net revenue $113,538M = **20.0%**, matching the
     MD&A's stated "decreased 220 basis points to 20.0%".

**PRICE AND SHARE COUNT — and the brief's screen row is wrong on both.**

- **Price $524.14, 2026-09-04** (aggregator — **flagged**, per the self-audit rule; used for
  the live quote only).
- **Share count, read off the cover of the LATEST periodic filing** (10-Q, accession
  0001571996-26-000030, filed 2026-06-09), verbatim:
  > "As of June 2, 2026, there were **648,107,991** shares of the registrant's common stock
  > outstanding, consisting of **324,873,640** outstanding shares of Class C Common Stock,
  > **276,744,341** outstanding shares of Class A Common Stock, and **46,490,010** outstanding
  > shares of Class B Common Stock."

**THE SHARE-CLASS RULING — `cover_shares.py` refuses to sum three classes on purpose, and
the charter says to sum them.** From Note 13 of the same 10-Q, verbatim:
  > "The Class A Common Stock, the Class B Common Stock, the Class C Common Stock, and the
  > Class D Common Stock **share equally in dividends declared or accumulated and have equal
  > participation rights in undistributed earnings.**"
  > "…any holder of Class A Common Stock or Class B Common Stock has the right to convert all
  > or any of the shares … into shares of Class C Common Stock **on a one-to-one basis.**"

The classes differ **only in votes** (A and B ten votes, C one, D none) and A/B convert into C
one-for-one at will — and did, 10 million shares of it during FY2026 and 4 million more in Q1
FY2027. **Economically equivalent; summing is correct**, and the company sums them itself on
its own cover. Class D: authorised 100 million, **zero outstanding**, so nothing to add.
No preferred is outstanding.

- **Market capitalisation = 648,107,991 × $524.14 = $339,699M.**

**DEFECT IN THE BRIEF'S SCREEN ROW (first of several).** The row carries `cap_m 295522`,
which implies **$455.98 per share** on this count — **13.0% below the 2026-09-04 quote of
$524.14**. Every derived field in the row is therefore optimistic: the true
`yield_bottom` on the row's own owner-earnings figure is **0.95%, not 1.09%**. This is the
PINS/QLYS defect class again (a stale price inside a cap), and it runs in the direction that
flatters the name.

---
## THE TWO LIVE FLAGS, ANSWERED FIRST — because the brief is right that they change the file

### FLAG 1 — `flags_disagree`. WHICH YEARS WERE NEGATIVE AT THE CAPEX END, AND WHY.

Owner earnings, every year Dell has filed as Dell Technologies, at both (c) ends
(OCF − SBC − (c)); $M; the capex line is the filed *"Capital expenditures and capitalized
software development costs"*, so capitalised software is already inside it:

| FY end | OCF | SBC | capex | D&A | **OE, capex end** | **OE, D&A end** |
|---|---|---|---|---|---|---|
| 2015-01-30 | 2,551 | 72 | 478 | 2,977 | 2,001 | (498) |
| 2016-01-29 | 2,162 | 72 | 482 | 2,872 | 1,608 | (782) |
| 2017-02-03 | 2,222 | 398 | 699 | 4,938 | 1,125 | (3,114) |
| 2018-02-02 | 6,810 | 835 | 1,212 | 8,634 | 4,763 | (2,659) |
| 2019-02-01 | 6,991 | 918 | 1,158 | 7,746 | 4,915 | (1,673) |
| 2020-01-31 | 9,291 | 1,262 | 2,241 | 6,143 | 5,788 | 1,886 |
| 2021-01-29 † | 11,407 | 1,609 | 2,082 | 5,390 | 7,716 | 4,408 |
| 2022-01-28 † | 10,307 | 1,622 | 2,796 | 4,551 | 5,889 | 4,134 |
| **2023-02-03** | **3,565** | 931 | 3,003 | 3,156 | **(369)** | **(522)** |
| 2024-02-02 | 8,676 | 878 | 2,756 | 3,303 | 5,042 | 4,495 |
| 2025-01-31 | 4,521 | 785 | 2,652 | 3,123 | 1,084 | 613 |
| 2026-01-30 | 11,185 | 723 | 2,633 | 3,029 | 7,829 | 7,433 |

† **contains VMware — see FLAG 2.**

**THE NEGATIVE YEAR IS FISCAL 2023 (ended 2023-02-03), AND IT IS ONE LINE.** From the filed
cash-flow statement in the FY2023 10-K (accession 0001571996-23-000007), the
change-in-assets-and-liabilities block for fiscal 2023 reads **accounts payable −$8,546M**.
Every other working-capital line that year was a *source* of cash (AR +113, inventories +875,
other +973, related party +649, deferred revenue +3,209). Fiscal 2023 earned $2,422M of net
income and $3,156M of D&A and still produced only $3,565M of operating cash, because
**payables ran off by $8.5bn.**

The same line, filed, across the series: **AP +5,742 (FY2022) → −8,546 (FY2023) → −498
(FY2024) → +1,703 (FY2025) → +12,665 (FY2026).** A $21.2bn swing between the worst year and
the best. **The entire distance between Dell's worst owner-earnings year (−$369M) and its
best ($7,829M) is one balance-sheet line.**

**WHY THE TWO SERIES DISAGREE — and it is a real finding, not an artifact.** The raw
operating-cash series has low ratio dispersion because it never goes negative; its floor is
$3.6bn. Owner earnings subtract a nearly **constant** $2.6–3.0bn of capex from that swinging
series, and a fixed subtraction from a volatile series raises the coefficient of variation and
pushes the trough through zero. `level_shift` on raw OCF sees a 1.01x early/late ratio and
says *"no step"*; the same test on owner earnings refuses to compute because the early half
straddles zero. **Both are correct, and the second is the informative one.** What the
disagreement points at is that **Dell's owner earnings are a working-capital series wearing an
earnings series' clothes.**

That is where **[E2-23]** constraint 3 bites: *"If the business requires additional working
capital to maintain its competitive position and unit volume, **the increment also should be
included in (c)**."* Dell's own risk factor says it does, verbatim:
> "Larger orders may also require **greater commitments of working capital**, such as for
> purchases of key components, which could adversely affect our cash flow"

Because our convention computes owner earnings through operating cash flow, the increment is
already inside the number — which is why the number swings. **The swing is the honest signal,
not noise to be averaged away.**

**THE FY2026 FIGURE IS A PAYABLES EXTENSION, QUANTIFIED [E4-41].** From the filed balance
sheet and cost of net revenue:

| | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| DSO (AR ÷ revenue × 365) | — | 39.3 | **56.5** |
| DIO (inventory ÷ COGS × 365) | — | 33.0 | **41.9** |
| **DPO (AP ÷ COGS × 365)** | ~104 | **102.3** | **135.1** |

**DPO extended 32.8 days in one year.** Holding DPO at FY2025's 102.3 days against FY2026's
actual cost of net revenue of $90,831M gives payables of $25,455M instead of the filed
$33,630M — so **$8,175M of the $11,185M of fiscal-2026 operating cash flow is a one-year
extension of supplier payment terms.** On a DPO-neutral basis, fiscal 2026 owner earnings at
the capex end are **−$346M**, not $7,829M. [E4-41] requires that a favourable break inside the
window be named and removed before the mean is trusted; this is the largest one in the file.
*(Carried as a disclosed sensitivity, not as the base case — Dell has run a negative
cash-conversion cycle for decades and part of any payables rise is simply COGS growth. What
cannot repeat is the 32.8 days on top of that: the lever is arithmetically capped at 365.)*

### FLAG 2 — THE ACQUISITION NOTE. THE FLAG IS WRONG; THE PERIMETER PROBLEM IS REAL AND RUNS THE OTHER WAY.

**What the flag says:** *"NET CASH INFLOW on the acquisition line ($4,237M, 1% of cap) — cash
acquired exceeded cash paid."*

**What the filings say — three defects, and none of them is "cash acquired".**

1. **$4,237M is a SUM OF ABSOLUTE VALUES, not a net.** `acquisition_flag()` computes
   `total = sum(abs(v) for v in vals)` over `[−3,957, 70, 126, 0, 84]`. Describing that figure
   as a "net cash inflow" mislabels its own arithmetic.
2. **The −$3,957M is the BOOMI DIVESTITURE, not an acquisition with cash acquired.** In the
   FY2022 10-K (accession **0001571996-22-000009**) Dell tagged fiscal 2022's
   `PaymentsToAcquireBusinessesNetOfCashAcquired` as **−$3,957M**, netting the $16M it paid for
   acquisitions against the $3,957M it *received* for Boomi. The filed cash-flow statement puts
   them on two separate lines (*"Acquisition of businesses and assets, net (16)"* and
   *"Divestitures of businesses, net 3,957"*).
3. **AND THE VALUE IS SUPERSEDED.** In the FY2024 10-K (accession **0001571996-24-000036**)
   Dell restated the same period's `PaymentsToAcquireBusinessesNetOfCashAcquired` to
   **+$16.0M** — the correct payments-only figure. Both values are live in companyfacts.
   `sources.annual()` writes `if x["end"] not in out`, keeping whichever value the JSON array
   presents **first**, not the one from the newest accession. It kept the withdrawn one.
   **This is the INTC defect exactly — a withdrawn input inside a screen field — and it is not
   specific to Dell.** The same pattern is visible at 2021-01-29 (−2,187, the RSA netting) and
   at 2019-02-01 (912 in one accession, −130 in another).

**THE TRUE ACQUISITION PERIMETER, rebuilt from the filed statements:** cash paid for
businesses over the five fiscal years FY2022–FY2026 is **$16 + $70 + $126 + $0 + $84 =
$296M — 0.09% of market capitalisation.** Dell has bought essentially nothing in five years.
The flag overstates the acquisition perimeter by roughly **14x** and points the wrong way.

**BUT THE PERIMETER PROBLEM IS REAL, IT IS DISPOSALS, AND THE HON PRECEDENT FIRES.**
The FY2023 10-K says so in terms, twice:
> "The Consolidated Statements of Cash Flows are presented **on a consolidated basis for both
> continuing operations and discontinued operations for all periods presented.**"
> "**Cash flows for both Fiscal 2022 and Fiscal 2021 are inclusive of cash flows attributable
> to VMware, Inc.**"

**So fiscal 2021's $11,407M and fiscal 2022's $10,307M of operating cash flow INCLUDE VMware,
a business Dell distributed to its shareholders on 2021-11-01 and does not own.** The filed
discontinued-operations note quantifies what rides inside the owner-earnings inputs for those
two years: **D&A $1,004M (FY2022) and $1,523M (FY2021); capital expenditures $263M and $329M;
stock-based compensation $814M and $1,122M.** This is the HON error, available to be made
here: a multi-year mean that INCLUDES a spun-off business, divided by a market cap that
EXCLUDES it. **Any window reaching back to FY2022 or earlier is measuring a different
company.**

**THE FULL PERIMETER LEDGER, from the business-combination and divestiture notes:**

| event | date | direction | cash | where it lands |
|---|---|---|---|---|
| **EMC Corporation** | 2016-09-07 (FY2017) | acquisition | **$37,629M** paid | the source of today's $19,547M goodwill and $4,533M intangibles, and of the negative book equity; **outside every window run here** |
| **RSA Security sold** | FY2021 | disposal | $2,187M received | inside a 6-yr window |
| **VMware spin-off** | **2021-11-01 (FY2022)** | **distribution to shareholders** | $9.3bn special dividend received by Dell; $5,052M of cash transferred out | **discontinued ops in the income statement, CONSOLIDATED in the cash-flow statement — the HON case** |
| **Boomi sold** | FY2022 | disposal | $3,957M received, $4.0bn pre-tax gain | gain removed from OCF via *"Other, net (3,130)"*, so OCF is clean of it |
| **VMware Resale terminated** | March 2024 (FY2025) | contract exit | — | Corporate & other revenue $5,624M → $3,581M → **$1,728M** |
| **Secureworks sold to Sophos/Thoma Bravo** | **2025-02-03 (FY2026)** | disposal | ~$0.9bn price, **$0.6bn to Dell**, $0.2bn gain | gain sits in *interest and other, net* — **inside net income, not inside operating cash flow** |

**RULING: the honest owner-earnings history for Dell-as-it-exists begins at fiscal 2023 (year
ended 2023-02-03), the first full year without VMware. That is FOUR years, one short of the
[E2-42] five-year default, and the shortfall is stated rather than repaired by reaching back
into a period that contains a different company.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.**

Dell buys finished components made by other people — Nvidia GPUs, Intel and AMD CPUs, memory,
drives, power supplies, sheet metal — screws them into a chassis, and sells the box. It sells
two kinds of box. **CSG** is personal computers: 50,984M of fiscal-2026 revenue at a **14.3%
gross margin**, sold mostly to corporate IT departments on a refresh cycle. **ISG** is data-
centre boxes: servers, networking and storage, $60,826M at a **26.0% gross margin**. Attached
to both is a services annuity — support contracts, deployment, extended warranty — worth
$23,133M of revenue at a **44.8% gross margin** ($10,359M of gross profit), which is where a
large share of the profit actually is. And attached to all of it is **Dell Financial Services**,
which lends the customer the purchase price and holds $16,739M of owned assets funded by
$14,646M of matched debt.

The money is made in three places and only three: **(1) a spread between what the components
cost and what the finished box sells for**, which is thin and set by competition;
**(2) the services annuity on the installed base**, which is thick and is a genuine annuity;
and **(3) the float of a negative cash-conversion cycle** — Dell collects from customers in
56.5 days, holds inventory 41.9 days, and pays suppliers in 135.1 days, so **suppliers finance
the working capital and the business runs on other people's money**. That last one is the
original Dell direct model and it is the reason the returns on tangible capital look as good as
they do. It is also the reason fiscal 2023 happened.

**The scarce input the business controls.** Not the silicon — Dell controls none of that, and
the 10-K's competition paragraph concedes that its largest customers *"often buy their
infrastructure directly from original design manufacturers."* What Dell actually controls is
**a purchasing position and a direct enterprise sales-and-service relationship at a scale only
two or three firms on earth have**: $90,831M of annual component purchasing, a global support
organisation, and an installed base that renews. That is a real asset. It is a **cost and
distribution advantage, not a product advantage** — which is the distinction [E2-58] makes when
it allows *"a cost advantage that is both wide and sustainable"* as the one exception in a
commodity business, and it is where Q2 has to do its work.

**Will the fundamentals look broadly the same in ten years?** The *mechanism* will: someone
will still assemble compute into boxes, sell them to enterprises, and support them. The
*magnitudes* will not, and the filing says so — AI-optimized servers went from **$1,873M to
$24,683M of revenue in two fiscal years**, from 2% of the company to 22%, and the 10-K names
*"the frequency of component part updates or transitions"* and *"inherent non-linearity in the
timing of demand"* as facts of the business. That is real instability, and it is recorded here
rather than waved through. But **[E3-31]** asks whether I can understand *how this makes
money*, and I can, completely, in three sentences with no management vocabulary. There is no
hidden reserve estimate, no origination model, no unconsolidated vehicle whose economics I have
to guess at. The uncertainty here is about **how much**, not about **what**, and "how much" is
Q4's and Q5's problem — it is not a claim that the business is opaque.

**One thing the filing makes easy that most do not**, and it belongs here rather than as a
compliment at Q3: Dell publishes ISG and CSG **cost of net revenue, SG&A and R&D separately**,
so segment gross margins are computable directly from the filed statement and reconcile to
segment operating income to the dollar. Most multi-segment filers do not give you this. It is
what makes Q2 decidable, and it is the reason the AMAT lesson applies here with full force:
**the segment split is available, and it kills what the consolidated numbers supported.**

- **VERDICT: [x] IN**

*Recorded, not counted against Q1: the 10-K's own risk factor — "**We are highly dependent on
the services of Michael S. Dell, our Chief Executive Officer**" — is a key-person dependence.
Per **[E4-23]** that is filed at **Q2 as a moat defect**, not here and not at Q3.*

---
## SELF-CORRECTION, ENTERED BEFORE Q2 — my own windage error, found by finishing the arithmetic

The FLAG 1 section above normalises fiscal 2026 by holding **DPO alone** at the prior year and
reports owner earnings of −$346M. **That is a one-sided normalisation and it is the error
[E4-11] names**: *"you don't try and put too much windage in at every level."* Receivables and
inventory moved against Dell in the same year and the honest normalisation holds **all three**
ratios. Completing the series with the filed FY2024 balance sheet (AR $9,343M, inventory
$3,622M, AP $19,226M):

| days | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| DSO | 38.6 | 39.3 | **56.5** |
| DIO | 19.6 | 33.0 | **41.9** |
| DPO | 104.2 | 102.3 | **135.1** |
| **cash conversion cycle** | **−46.0** | **−30.0** | **−36.7** |

**The cash conversion cycle has DETERIORATED by 9.3 days since fiscal 2024, not improved.**
Holding all three ratios at FY2025 levels against FY2026's actual revenue and cost of net
revenue: AR would be $12,224M (−$5,361M of cash), inventory $8,211M (−$2,226M), payables
$25,455M (+$8,175M) — a net **+$588M**, not +$8,175M. **Ratio-neutral fiscal-2026 owner
earnings at the capex end are $7,241M, not −$346M.** The DPO-only figure answers a narrower
question (what if suppliers alone had not extended terms) and is retained as that, clearly
labelled, rather than deleted — but it is **not** the [E4-41] normalisation and the run does
not use it as one. Recorded here rather than by editing the section above, per operator
rule 6.

The substantive finding from FLAG 1 survives the correction intact and is unchanged: **the
swing between −$369M and $7,829M is a working-capital swing, the payables line is the largest
single driver of it, and the level of owner earnings in any one year says more about the
balance sheet than about the earning power.**

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

### THE THREE CRITERIA

- **(1) needed or desired** — [x] **YES.** Enterprises need servers, storage and PCs. Not in
  question.
- **(2) no close substitute** — [ ] **NO. THIS FAILS, AND IT FAILS ON THE COMPANY'S OWN
  WORDS.** Three separate passages of the fiscal-2026 10-K, verbatim:
  > "We face ongoing product and **price competition in all areas of our business** from both
  > branded and **generic competitors**, including companies that specialize in one or more of
  > our product or service lines."

  > "We also face competition from non-traditional IT companies, including large
  > Infrastructure-as-a-Service providers, that **often buy their infrastructure directly from
  > original design manufacturers.**"

  > "ISG offers a portfolio of storage, server, and networking solutions, including
  > AI-optimized technologies, and faces **intense competition** from existing on-premises
  > competitors and increasing competitive pressures from Infrastructure-as-a-Service
  > providers."

  *"Generic competitors"* is the filer's own word for a commodity. And the second passage
  names the substitute precisely: **Dell's largest AI-server customers can and do buy the same
  Nvidia silicon in the same chassis straight from the ODM that builds Dell's own boxes.** The
  substitute is not merely close; it is the identical product with Dell's name removed.
- **(3) not subject to price regulation** — [x] **YES**, not regulated. (No credit either
  way: **[E2-59]** — regulation caps a franchise and floors a commodity business; its absence
  creates nothing.)

**Criterion (2) fails. Under [E3-03] that ends the franchise question.** What follows is the
evidence, built at full strength in both directions, because a verdict this consequential is
not carried by a definition.

### THE ARITHMETIC THAT DECIDES IT — IS THE AI REVENUE ARRIVING WITH MARGIN? **[E2-63]**

The filing discloses ISG and CSG **cost of net revenue, SG&A and R&D separately**. Segment
gross margin is therefore computable directly, and the identity closes to the dollar against
filed segment operating income in all three years (Step 0 cross-check).

| ISG ($M) | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| net revenue | 33,885 | 43,593 | **60,826** |
| cost of net revenue | 20,943 | 29,352 | **45,022** |
| **gross profit** | **12,942** | **14,241** | **15,804** |
| **gross margin** | **38.19%** | **32.67%** | **25.98%** |
| SG&A + R&D | 8,656 | 8,662 | 8,693 |
| **operating income** | **4,286** | **5,579** | **7,111** |
| **operating margin** | **12.65%** | **12.80%** | **11.69%** |
| of which AI-optimized servers | 1,873 | 9,286 | **24,683** |
| traditional servers & networking | 15,751 | 17,850 | 19,512 |
| storage | 16,261 | 16,457 | 16,631 |

**ISG gross margin fell 1,221 basis points in two years while ISG revenue grew 79.5%.** The
10-K states the cause itself, twice, without being asked:
> "Gross margin rate decreased primarily as the result of **a shift in mix towards our
> AI-optimized servers offerings.**"

**The incremental gross margin on ISG's growth:**
- FY2025 over FY2024: ΔGP $1,299M ÷ ΔRev $9,708M = **13.4%**
- FY2026 over FY2025: ΔGP $1,563M ÷ ΔRev $17,233M = **9.1%**
- two-year: ΔGP $2,862M ÷ ΔRev $26,941M = **10.6%**

**And the AI-server gross margin itself, solved from the filed figures.** Two equations, two
unknowns, assuming AI and non-AI ISG each held a constant rate across FY2025 and FY2026:

    FY2025:   9,286·m_AI + 34,307·m_other = 14,241
    FY2026:  24,683·m_AI + 36,143·m_other = 15,804
    →  m_AI = 5.37%      m_other = 40.06%

**Back-tested on the year not used to fit it**, FY2024: 1,873 × 5.37% + 32,012 × 40.06% =
**$12,923M against a filed $12,942M — an error of $19M on $12,942M, 0.14%.** A two-parameter
model that reproduces an out-of-sample year to fourteen basis points is not a fitted curve; it
is the structure.

> **AI-optimized servers run at roughly a 5% gross margin. The rest of ISG runs at 40%.
> On $22,810M of incremental AI-server revenue over two years, about $1,225M stayed home.
> Ninety-five cents of every incremental AI dollar flowed straight through.**

That is **[E3-62]**'s second step, answered from a filed statement: *"how much is going to stay
home and how much is just going to flow through to the customer."* In the one-paper town it
sticks; in a commodity business it does not. The textile-loom sentence — *"Nothing was going to
stick to our ribs as owners"* — is the fiscal-2026 ISG income statement.

**Consolidated, the same thing:** gross margin **21.6% (FY2022) → 22.2% → 23.8% (FY2024) →
22.2% → 20.0% (FY2026)**, a 383bp fall from the FY2024 peak, on revenue up 28% over the same
two years. Product gross margin specifically fell **210bp to 13.7%**. CSG gross margin fell
from **16.88% to 14.30%** over the same two years, and CSG operating margin from **7.59% to
5.56%**. **Every margin line in the company is falling, in both segments, while revenue grows.**

**Guidance for fiscal 2027 confirms the direction, in the company's own forward language:**
> "We expect margin growth, while balancing anticipated **margin rate pressure resulting from a
> continuing shift in mix towards our AI-optimized servers offerings.** We anticipate **notable
> inflation for component costs** in Fiscal 2027"

### THE PHYSICAL SERIES **[E4-55]** — where units exist, monitor units

*"Dollar revenue flattered by pricing is how a shrinking franchise hides; the physical series
is the honest one."* Dell does not print unit counts, but it prints the **decomposition**, and
it is damning in three of four product lines:

| line | FY2026 revenue | what the filing says about **units** and **price** |
|---|---|---|
| **Traditional servers & networking** | +9% (and +13% in FY2025) | *"primarily due to an increase in the average selling price … partially offset by **a decline in units sold for both periods**. The increase in the average selling price was primarily driven by **richer configurations**."* |
| **CSG commercial** | +8% | *"an increase in units sold and richer configurations, **partially offset by a decline in average selling prices**"* |
| **CSG consumer** | **−8%** | *"due to **a decline in average selling prices and units sold**"* |
| **Storage** | +1% (and +1% in FY2025) | $16,261 → $16,457 → **$16,631**: **+2.3% over two years**, below any measure of inflation |

**Traditional servers are the Precision Steel case exactly**: units DOWN in both of the last two
years, dollar revenue UP on "richer configurations." A richer configuration is not a price rise
— it is more Intel and more memory passed through at a markup. And in PCs, **average selling
prices fell in commercial and in consumer**, in the same year the company's headline revenue
grew 19%.

**[E2-44], the two-characteristic test, therefore fails on both halves:**
- *Can it raise prices even when demand is flat and capacity is not fully utilized?* **No — it
  is cutting them.** Commercial and consumer PC ASPs both declined in fiscal 2026.
- *Can it grow dollar volume with only minor additional investment of capital?* **No.** Fiscal
  2026's growth consumed **$7,022M of receivables, $3,987M of inventory and $2,740M of
  financing receivables — $13,749M of incremental working capital and financing assets in a
  single year, against $8,149M of operating income.**

**[E4-37], the inverse metric:** *"you can almost measure the strength of a business over time
by the agony they go through in determining whether a price increase can be sustained."* Dell
is not in the agony phase. It is past it: prices are already falling and the filing reports it
as a fact of the year.

### THE ONE Q2 TEST DELL PASSES, STATED AT ITS FULL STRENGTH **[E3-46], [E2-43]**

*"the best businesses, by definition, are going to be businesses that earn very high returns on
capital employed over time."* Dell does, and because book equity is **negative** the denominator
must be **unleveraged net tangible assets [E2-43]**, with the goodwill wedge reported
separately rather than hidden:

| | $M |
|---|---|
| total assets (2026-01-30) | 101,286 |
| less goodwill | (19,547) |
| less intangible assets, net | (4,533) |
| **tangible assets** | **77,206** |
| less accounts payable | (33,630) |
| less accrued and other | (8,315) |
| less short- and long-term deferred revenue | (26,930) |
| less other non-current liabilities | (3,378) |
| **unleveraged net tangible assets** | **4,953** |
| operating income $8,149M at a 21% notional tax | **6,438** |
| **return on unleveraged net tangible assets** | **≈130%** |
| *the same, netting only CURRENT non-interest-bearing liabilities* | *$21,927M → **29.4%*** |

**Both readings are high, and this is a genuine point for the business — recorded as such
[E4-26].** But read what produces it. Dell operates $101.3bn of assets on **$5.0bn of net
tangible capital** because **$72.3bn of the funding is non-interest-bearing liabilities**, of
which **$33.6bn is trade payables that ran off by $8.5bn in a single year in fiscal 2023.** A
very high return on a capital base that is mostly the suppliers' and the customers' money is a
**funding structure**, not a moat. It is also the exact structure that produced the negative
owner-earnings year, and [E2-43] chose this denominator to make operations legible, not to
license a franchise claim that criterion (2) has already refused.

### WHICH KIND OF MOAT IS BEING CLAIMED, AND WHAT THE CORPUS SAYS ABOUT IT

- **[E2-58], the commodity equation.** *"persistent over-capacity without administered prices
  (or costs) equals poor profitability."* Server and PC assembly has no administered prices.
  The single exception the corpus allows is *"a cost advantage that is both **wide and
  sustainable** … By definition such exceptions are few."* **That is the only franchise claim
  available to Dell, and it is a relative claim** — which is what the competitor row below is
  for.
- **[E3-51], surfing.** AI-optimized servers grew **+396% then +166%**. *"when a surfer gets up
  and catches the wave … he can go a long, long time. But if he gets off the wave, he becomes
  mired in shallows."* **A surfing run is not a moat; the advantage lives in the wave.**
- **[E4-36], the four causes of extreme success.** Dell's last two years are **wave-riding** —
  and wave-riding is the one of the four that is not ownable.
- **[E2-53], the dominance class.** *"Once dominant, the newspaper itself, not the marketplace,
  determines just how good or how bad the paper will be."* The inverse holds here: **the
  marketplace determined Dell's ISG gross margin and moved it 1,221bp in two years.** Position
  does not set the economics; the component cycle and the customer's alternative do.
- **[E4-32], direction outranks existence.** *"the moat widened every year"* is the primary
  criterion of a great business. Dell's measurable moat metrics — consolidated gross margin,
  ISG gross margin, ISG operating margin, CSG gross margin, CSG operating margin, commercial
  ASP, consumer ASP, traditional-server units — are **falling on every single one.** Direction
  is unambiguous and it is down.
- **[E2-45], the attacker's test.** *"how I would like, assuming I had ample capital and skilled
  personnel, to compete with it."* Buy the same Nvidia HGX boards, contract the same Taiwanese
  ODM for the same chassis, hire enterprise account managers, undercut on price. That is not a
  thought experiment: it is what Super Micro did, and the competitor row measures the result.
- **[E5-28], the pricing-power scope.** *"If you name some business that has incredible pricing
  power, you're talking about a business that's a monopoly or a near monopoly."* Not remotely
  claimable here.
- **[E3-33], untapped pricing power.** Could a manager raise the return simply by raising
  prices and has not? **No.** ASPs are falling in three of four product lines, and the fiscal-
  2027 outlook forecasts further margin-rate pressure. There is no untapped price to take.
- **[E4-23], key-person dependence — recorded HERE as a moat defect, not at Q3 as a strength.**
  The 10-K's own risk-factor heading: *"**We are highly dependent on the services of Michael S.
  Dell, our Chief Executive Officer**"*, alongside 91.7% of voting power held by the Dell and
  Silver Lake stockholders. *"the moat will go when the surgeon goes"* — a filer that names its
  CEO as a risk factor has told you where the moat is thought to live.

### THE COMPETITOR ROW — required [E3-28]. A moat is a claim about *relative* position.

Full workings, method notes, accession numbers and the four disclosed conventions are in
`Test Runs/_research 2026-09-07 DELL/competitor_row.md`. **Seven names taken** — the five real
competitors, plus the supplier whose margin is the question, plus IBM as the incumbent that
left the box business. Fiscal years are labelled by each filer's own FY and every row states
its period end; **DELL FY2026 and NVDA FY2026 end five days apart**, which is the comparison
the thesis needs.

**GROSS MARGIN, latest filed fiscal year — the row that carries the thesis:**

| | gross margin | operating margin | revenue $M | ROUNTA **[E2-43]** |
|---|---|---|---|---|
| **NVDA** FY2026 — *the supplier* | **71.07%** | **60.38%** | 215,938 | 67.99% |
| IBM FY2025 | 58.19% | 17.50% | 67,535 | 23.04% |
| HPE FY2025 | 30.26% | **(1.27)%** | 34,296 | (1.34)% |
| HPQ FY2025 | 20.60% | 5.74% | 55,295 | 68.93% ‡ |
| **DELL FY2026** | **20.00%** | **7.18%** | 113,538 | **29.36%** |
| Lenovo FY2026 § | 15.42% | 3.93% | 83,075 | n/a |
| **SMCI** FY2026 — *the attacker* | **10.82%** | 7.09% | 39,063 | 8.82% |

‡ HPQ's 68.93% is a negative-working-capital artefact on a $3,638M denominator, disclosed as
such in the research file and given no weight. § Lenovo is **not an SEC registrant** (HKEX
0992, IFRS, 31 March year end); its figures come from HKEX annual results, **evidence-ladder
rung 4**, and are flagged rather than either omitted or promoted to parity.

**THE THREE FINDINGS FROM THE ROW:**

**1. The margin sits with the supplier, and the gap is 51 points.** In fiscal years ending five
days apart, **Nvidia earned $153,463M of gross profit — 6.76× Dell's entire gross profit of
$22,707M — on revenue only 1.90× Dell's.** Nvidia's operating income of $130,387M is **16.0×
Dell's $8,149M** and **18.3× the entire ISG segment's $7,111M**. Nvidia's Data Center revenue
alone ($193,737M) is **3.19× the whole of ISG**. Per revenue dollar the supplier keeps
**71.07¢** of gross profit; the assembler keeps **20.00¢**, and ISG keeps **11.69¢** of segment
operating profit before corporate cost, amortisation and stock comp. In fiscal 2021 Dell's
revenue was **5.2× Nvidia's**; in fiscal 2026 Nvidia's is **1.90× Dell's**. **The value moved
up the stack and the filings measure the move.**

**2. AN INDEPENDENT FILER CONFIRMS THE 5% AI-SERVER MARGIN FROM ITS OWN ACCOUNTS.** Super
Micro is the purest available read on this question — it builds AI servers and nothing else,
and it carries **zero goodwill and zero intangibles**, so there is no acquired-asset layer
between revenue and the assembly economics:

| SMCI | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| revenue $M | 7,123.5 | 14,989.3 | 21,972.0 | **39,063.1** |
| **gross margin** | **18.01%** | 13.75% | 11.06% | **10.82%** |

**Revenue rose 5.48× and gross margin fell from 18.01% to 10.82% — a 39.9% relative decline.
Every incremental revenue dollar from FY2023 to FY2026 carried 9.20¢ of gross profit.** That
is arrived at from a *different company's* filings, by a different route, and it lands on the
same number as the two-equation solve of Dell's own segment note (5.4% on AI servers, 9.1%
incremental on ISG in fiscal 2026, 10.6% over two years). **Two independent filers, two
independent methods, one answer: AI-server assembly is a high-single-digit gross-margin
business.** [E3-28] exists for exactly this, and it has never returned a cleaner corroboration
in this queue.

**3. THE ATTACKER'S TEST [E2-45] IS ANSWERED WITH A FILED COST RATIO, AND DELL LOSES IT.** The
[E2-58] exception — *"a cost advantage that is both **wide and sustainable**"* — is the only
franchise claim available to a commodity assembler, and it is a relative claim. Operating
expenses as a share of revenue, latest fiscal year: **DELL 12.82%** ($14,558M ÷ $113,538M)
against **SMCI 3.73%**. **Super Micro runs a cost structure roughly one-third of Dell's**, is
already at $39.1bn of revenue, and grew **+77.8%** in its latest year against ISG's +39.5% and
Dell's +19%. Over six years SMCI compounded revenue at **+61.5%/yr** against Dell's **+5.5%**.
The attacker is not hypothetical, is not sub-scale, and is not slowing. **Dell's cost advantage
in AI servers is neither wide nor demonstrated.**

**WHAT THE ROW SAYS FOR DELL, AT FULL STRENGTH [E4-51] — and it is not nothing:**
- **Dell has the highest operating margin of any assembler in the panel (7.18%), and it has
  risen in each of six consecutive years: 4.25% → 4.60% → 5.64% → 6.12% → 6.53% → 7.18%.**
  This is the single best fact in the file for the bull case.
- **HPE, the direct ISG analogue, posted an operating LOSS of $(437)M** on 13.8% revenue growth
  (the Juniper impairment year). ISG's 11.69% segment margin is comfortably above HPE's whole
  company in any year of the six.
- **ROUNTA 29.36%** (31.16% adding back amortisation per [E2-43]) — second among the genuine
  operators and far above SMCI's 8.82%.
- **HPQ, the CSG analogue, shrank revenue at −0.5%/yr over six years** and also runs negative
  book equity. CSG grew 5% in fiscal 2026.

**AND THE ANSWER TO IT, FROM THE SAME FILINGS.** The rising operating margin is not evidence of
a widening moat; it is evidence of **harvesting**, and the two lines that produced it say so.
Dell's consolidated operating expenses **fell in absolute dollars** from $15,013M to $14,558M
while revenue rose 19%. Inside that: **SG&A fell $11,952M → $11,416M**, and **R&D as a share of
revenue fell 3.20% → 2.77%** ($3,061M → $3,142M on revenue up $17,971M). In the year the
product mix shifted hardest in the company's history, Dell spent **2.77% of revenue on R&D** —
against IBM's 12.3% — and cut selling costs. **[E5-23]** requires *"working at improving your
own moat and defending your own moat **all of the time**"*; **[E2-60]** says maintenance
includes financial strength and that under-spending it means (c) was understated. **A margin
that rises because the defence budget fell is the [E4-32] direction test failing while the
headline passes.**

**THE ROW'S LIMIT, stated [E3-61].** *"In some businesses, the participants behave like a
demented Kellogg. In other businesses, they don't … I think you'd have to know the people
involved."* The row establishes **position** — 51 points of margin gap to the supplier, a
one-third cost structure at the attacker, a 39.9% margin decline at the pure play. It cannot
establish **conduct**: whether Nvidia chooses to keep 71 cents, whether the hyperscalers keep
buying assembled rather than direct, whether Super Micro prices rationally. Those are
behavioural and the corpus says even Munger had no model for them. Nothing above rests on a
conduct prediction; all of it rests on filed outcomes.

**Peers named: 6 of the industry's real competitors, plus the supplier.** Lenovo obtained at a
lower evidence rung and flagged. **Because one peer sits below SEC parity, the moat class would
be PROVISIONAL if the verdict turned on Lenovo — it does not.** Lenovo's 15.42% gross margin
and 3.93% operating margin, at whatever rung, sit *below* Dell and *inside* the same commodity
band; obtaining them at SEC parity could only make the commodity finding stronger, never weaker.

### THE BULL CASE, BUILT AT FULL STRENGTH BEFORE IT IS ANSWERED **[E4-51]**

*"I'm not entitled to have an opinion unless I can state the arguments against my position
better than the people who are in opposition."*

1. **THE BACKLOG. Remaining performance obligations went $40bn (FY2023) → $38bn (FY2025) →
   $82bn (FY2026)** — a **116% increase in one year** — with **78% expected to convert within
   twelve months** (against 61% a year earlier). That implies roughly **$64bn of contracted
   fiscal-2027 revenue** against $113.5bn of fiscal-2026 total revenue. This is the largest and
   best-evidenced fact in Dell's favour and it is filed, not guided.
2. **Backlog is growing in the profitable line too**, not only in AI: *"during Fiscal 2026,
   demand for our traditional servers and networking offerings **outpaced supply**, resulting in
   incremental backlog growth as we exited the year."*
3. **The operating leverage is real money.** ISG operating income rose **$4,286M → $7,111M,
   +66% in two years, on operating expenses that did not move** ($8,656M → $8,693M).
4. **The services annuity is not a commodity.** Services revenue $23,133M at a **44.78% gross
   margin** produced **$10,359M of gross profit — 45.6% of the entire company's gross profit**
   — off an installed base that renews. This is the best economics in the company.
5. **Returns on tangible capital are genuinely high** (29.4%, or ~130% netting all
   non-interest-bearing liabilities), satisfying **[E3-46]**'s number.
6. **DFS credit quality is excellent**: principal charge-off rate **0.2%** in fiscal 2026,
   against 0.6% and 0.5% in the two prior years.
7. **Storage is real intellectual property**, $16.6bn of revenue, and the non-AI part of ISG
   solves to a **40.06% gross margin** — a genuinely good business hiding inside the segment.

**THE ANSWER, point by point, from the same filings.**

- **(1) and (2) are volume claims, not margin claims, and Q2 is a margin question.** At the
  5.4% solved AI gross margin, an AI-weighted $64bn of near-term backlog carries on the order of
  **$3.5bn of gross profit** — against a market capitalisation of $339.7bn. Backlog measures how
  much revenue is coming; the segment note measures what happens to it on arrival, and it is
  **95 cents flowing through**. A bigger pipe at 5 cents is still 5 cents.
- **(3) cannot repeat.** Holding operating expense flat while revenue grows 79% is a one-time
  benefit; the expense base is now 12.8% of revenue with R&D at 2.77%, and the next 79% of
  revenue growth will not come free.
- **(4) is true and it is the reason this is a Q2 finding rather than a Q1 or Q4 one — but the
  annuity is not scaling with the hardware.** Services revenue was **$24,072M (FY2024) →
  $24,147M (FY2025) → $23,133M (FY2026)**, i.e. **down 3.9%** across two years in which product
  revenue rose **40.5%** ($64,353M → $90,405M). Most of the decline is perimeter (VMware Resale
  and Secureworks, inside Corporate and other, which fell $5,624M → $1,728M), and ISG/CSG
  services did grow — but the net result stands: **the profitable annuity did not grow while
  the low-margin hardware nearly doubled.** The mix moved against the good business.
- **(5) is a funding structure**, answered in full above: $5.0bn of net tangible capital under
  $101.3bn of assets, because $72.3bn is other people's money.
- **(7) concedes the point.** That the non-AI 60% of ISG earns 40% while the AI 40% earns 5% is
  precisely the finding. **The growth is entirely in the part that does not earn**, and the part
  that earns is flat: storage **+2.3% over two years**, traditional servers **down in units in
  both years**.

### CLASS AND DIRECTION

- Class: [ ] WIDE [ ] NARROW [ ] PROVISIONAL — **[x] NONE**, on criterion (2) of **[E3-03]**.
  What Dell has is a **distribution and service position with a real annuity attached**, riding
  a wave it does not own **[E3-51]**, in a business the corpus classifies at **[E2-58]** and
  whose one exception — a wide and sustainable cost advantage — the competitor row refuses.
- **Direction: DOWN, unambiguously, on every measurable line [E4-32]:** consolidated gross
  margin 23.83% → 20.00%; ISG gross margin 38.19% → 25.98%; ISG operating margin 12.80% →
  11.69%; CSG gross margin 16.88% → 14.30%; CSG operating margin 7.59% → 5.56%; commercial PC
  ASP down; consumer PC ASP down; traditional-server units down in both of the last two years;
  R&D intensity 3.20% → 2.77%. **Not one moat metric in this filing is widening.**

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**OUT, on [E3-03] criterion (2), in the filer's own words** — *"price competition in all areas
of our business from both branded and **generic competitors**"*, and customers who *"often buy
their infrastructure **directly from original design manufacturers**"* — **corroborated
quantitatively by [E2-63]/[E3-62]** (95¢ of every incremental AI dollar flows through),
**by [E2-44]** (both halves fail: prices are falling, and growth consumed $13.7bn of working
capital and financing assets in one year), **by [E4-55]** (units down where units are
disclosed), **by [E4-32]** (every metric falling), and **by the competitor row [E3-28]** (a
51-point margin gap to the supplier, and an attacker at one-third the cost ratio growing four
times as fast).

**OUT is permanent and it is a finding about the business, not about my diligence.** It is not
a claim that Dell is a bad company — it is the best-run assembler in its panel by operating
margin, and it says so with six consecutive years of improvement. It is the claim that
**assembly is not a franchise, and Dell's own segment note is the evidence.**

⛔ **Q3, Q4, Q5 and Q6 DO NOT OPEN. The hard sequence closes the file here** (operator rule 2).
Findings gathered before the gate closed are recorded below **as observations, carrying no
verdict**, because they were already on disk and discarding evidence is not a virtue.

**ADDENDUM TO THE COMPETITOR ROW, entered after the Q2 verdict was written and changing
nothing in it.** Lenovo was ultimately obtained for all six years from its audited HKEX annual
results (rung 4; the copies came from a listed-company mirror, `doc.irasia.com`, rather than
`hkexnews.hk` — flagged, and IFRS so one rung less comparable). Its **ROUNTA is 29.52%,
against Dell's 29.36%.** So the one Q2 test Dell passes — high returns on tangible capital
**[E3-46]** — **it does not pass alone**: the largest PC vendor on earth earns the same return
on the same kind of capital. A metric matched by a direct competitor is not a moat; it is the
industry's working-capital structure. This strengthens the OUT and is recorded because it
arrived late, not because it was needed.

---
## Q3, Q4, Q5, Q6 — NOT OPENED

**Operator rule 2: no question past the first non-IN verdict is answered, and UNRESEARCHED and
UNKNOWABLE both close the file as surely as OUT.** Q2 returned **OUT**. Q3 through Q6 are
therefore **NOT REACHED** — not IN, not OUT, not UNRESEARCHED, not UNKNOWABLE. They have no
verdict, and this run does not manufacture one.

What follows was gathered before the gate closed and is recorded as **observations carrying no
verdict**, because the evidence exists and discarding it would be a loss to the register.

### OBSERVATION A — negative book equity, and what it does and does not mean

**Total Dell Technologies Inc. stockholders' equity (deficit) is $(2,470)M at 2026-01-30, and
it WIDENED from $(1,482)M** — in a year the company earned $5,936M. The cause is on the face:
treasury stock at cost of **$(14,533)M** against retained earnings of **+$3,325M**. Retained
earnings actually turned **positive** in fiscal 2026 for the first time since the EMC deal
(from $(1,160)M), so the deficit is a **buyback artefact, not an accumulated-loss artefact**.
HPQ's balance sheet has the same shape ($(346)M).

For **[E5-11] strength (3)** and **[E5-39]** this means the equity line carries no information
and must not be used: there is no cushion to measure because the cushion was distributed. The
readable numbers instead are **core debt $17,018M** (management's own definition, disclosed with
its 7:1 DFS allocation method — unusually candid) against **cash $11,528M**, i.e. **net core
debt of $5,490M** on $8,149M of operating income. **That is not a stretched balance sheet**, and
saying otherwise from the equity deficit alone would be the error.

### OBSERVATION B — the [E2-54] coverage test, run on filed figures

*"all interest, both payable and accrued, comfortably met out of current cash flow net of ample
capital expenditures."* Interest **paid**, from the supplemental cash-flow disclosures:

| | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| OCF − capex ($M) | **562** | 5,920 | **1,869** | 8,552 |
| interest paid ($M) | 1,169 | 1,438 | 1,304 | 1,354 |
| **coverage** | **0.48×** | 4.12× | **1.43×** | 6.32× |

**In two of the four perimeter-clean years, cash flow net of capital expenditure did not
comfortably meet interest, and in fiscal 2023 it did not meet it at all.** [E2-54] is the
solvency read that EBITDA-based covenants are built to avoid, and it returns a different answer
here from the headline. The counterpoint, stated: interest is bloated by **DFS-related debt of
$14,646M** matched against **$16,739M of DFS owned assets** earning interest income inside
revenue, so a share of this interest is a funding cost with a revenue offset rather than a
leverage cost. On core debt alone the picture is much better. Both readings are recorded.

### OBSERVATION C — the ORCL prior, and it is REFUTED

The brief's prior was that *"the receivables/financing book is being consolidated in a way that
flatters operating cash flow"*, on the ORCL precedent. **The filing says the opposite, and the
direction is the conservative one.** DFS **financing-receivable growth is an OPERATING outflow**
— $(2,740)M in fiscal 2026, $(951)M in fiscal 2025 — while the **DFS debt that funds it is a
FINANCING inflow**. The asset build is charged against operating cash flow and the matched
liability is not credited to it. **Dell's operating cash flow is therefore UNDERSTATED by the
growth of the finance book, not overstated.** Adding the financing-receivable growth back would
*raise* fiscal-2026 owner earnings from $7,829M to $10,569M. The prior is refuted and the
refutation runs in Dell's favour. (Credit quality supports it: principal charge-off rate
**0.2%**, against 0.6% and 0.5% in the two prior years.)

**ORCL failed Q4 on a 3.4% incremental return on ~$160bn deployed with coverage negative net of
capex. Dell is not that shape at all.** Dell deploys $2.6bn a year of capex, not $160bn, and its
incremental return on ISG's growth is 10.5% at the operating line, not 3.4%. **The two names
fail for opposite reasons: Oracle failed on the capital it deployed; Dell fails on the margin
it does not keep.** Recorded because assuming the same answer was the specific trap the brief
warned against, and the arithmetic refuses it.

### OBSERVATION D — [E5-08] on the buyback, and this prior is REFUTED TOO

Ten years of share count, from the filed balance sheets and covers:

| | FY17 | FY18 | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 | Q1 FY27 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| shares outstanding (M) | 778 | 769 | 719 | 743 | 753 | 757 | 716 | 705 | 696 | **652** | **649** |

**Down 16.2% from the post-EMC peak**, and the reduction is real, not a dilution mop-up:
fiscal 2026 alone retired **54 million shares for $6,031M**.

**And the price paid clears [E5-08] condition (2) — which I did not expect.** $6,031M ÷ 54M =
**an average of $111.69 per share** in fiscal 2026, and roughly **$147** in Q1 FY2027 (11M
shares for $1,616M). The Q4 FY2026 detail table gives the weighted average prices directly:
**$133.22, $132.34 and $118.96**. Against the value band computed below ($88–$231 at the bare
sovereign), **Dell bought its own stock at or near the bottom of the range**, which is what
[E5-08](2) asks for and what [E5-24]'s *"what is smart at one price is dumb at another"*
rewards. Condition (1) also holds: $11,528M of cash, **no** revolver borrowings and **no**
commercial paper outstanding at year end.

**The live risk is prospective, not realised.** The board authorised a further **$10bn on
2026-02-26** (leaving ~$15.2bn available) and the shares now trade at **$524.14 — 4.7× the
fiscal-2026 average repurchase price.** Continuing to buy here would fail condition (2) on the
band below, and that must be stated with the humility clause **[E4-13]**: this rests on our own
range, and management knows the business better than we do.

**But [E2-60] does fire.** Fiscal 2026 returned **$6,014M of buybacks + $1,459M of dividends +
$390M of RSU tax withholding = $7,863M, or 132% of net income**, in the same year **total debt
principal rose $6,975M and core debt rose $4,021M**, and the equity deficit widened. *"where
leverage rises to fund the payout, (c) was understated"*, and *"a company that consistently
distributes restricted earnings is destined for oblivion."* One year is not "consistently" —
recorded as a prompt, not a finding.

### OBSERVATION E — the flags that did NOT fire, recorded because absence is evidence

- **[E4-29] EBITDA promotion: DOES NOT FIRE.** A recorded sweep of the fiscal-2026 10-K finds
  **two** occurrences of the string "EBITDA" in the entire document, neither of them a headline
  measure. Dell leads on GAAP operating income and reconciles non-GAAP beside it.
- **[E5-15] serial share issuance: DOES NOT FIRE.** Proceeds from issuance of common stock were
  **$5M, $1M and $10M** in the last three years against $10.7bn of repurchases.
- **[E2-26] the half-owner test: PASSES on the segment note**, which is the reason this run was
  decidable at all. Dell publishes ISG and CSG **cost of net revenue, SG&A and R&D separately**,
  publishes the AI-optimized-server revenue line as a *new disaggregation it introduced itself*
  in Q4 FY2026, and publishes the **DFS allocated-debt method (7:1) and the core-debt
  definition**. **It disclosed the disaggregation that makes its own margin dilution visible.**
  That is candour of the kind [E2-67] describes, and it is the strongest single thing in
  management's favour in this file.
- **[E3-48] the projections flag** is not clean: the outlook section forecasts revenue and
  margin direction for the coming year. But it is **directional and it forecasts the bad news**
  — *"anticipated margin rate pressure"*, *"notable inflation for component costs"* — which is
  the opposite of the [E4-22] tell.

### OBSERVATION F — the named way this business dies **[E2-27, E3-24, E4-40]**

**The mechanism, and it is not hypothetical because it has already happened once inside the
four-year clean window.** Dell runs on a negative cash conversion cycle: it holds $10,437M of
inventory and owes $33,630M of trade payables at **135 days**. Its working capital is its
suppliers' money. When demand pauses, revenue stops but the payables keep coming due, and the
cycle unwinds violently. **Fiscal 2023 is the worked example: payables ran off $8,546M and
owner earnings went to −$369M.**

**Quantified from the fiscal-2026 balance sheet.** Payables fell roughly **31% peak-to-trough**
in the fiscal-2022 → fiscal-2023 unwind. The same 31% draw on today's $33,630M is a
**$10.4bn** cash outflow. Set against it, as of 2026-01-30:

| near-term claim | $M |
|---|---|
| debt maturing in fiscal 2027 | **7,997** |
| **purchase obligations payable within 12 months** (of $18.8bn total) | **16,800** |
| **total contractual, within 12 months** | **24,797** |
| cash and equivalents | **11,528** |

**[E4-40] — model exposure, not experience.** The 10-K names the exposure itself:
> "to date our AI solutions have been purchased primarily by **a small number of larger
> customers and cloud service providers**"

> "**Larger orders may also require greater commitments of working capital** … and expose us to
> the risk of holding excess and obsolete inventory due to **delays or cancellations**"

> "we have **increased, and expect we will continue to increase, our purchases of certain
> components** … resulting in increased purchase obligations"

**So: a two-quarter pause in AI-server demand from a handful of concentrated buyers, against
$16.8bn of non-cancelable component commitments due within twelve months, $10.4bn of payables
unwinding, $8.0bn of debt maturing, and $11.5bn of cash.** The fiscal-2023 precedent says the
company survives it — it did, with a $3.3bn buyback that year — but it says so on a base one
third the size, with no AI purchase-obligation book, and it produced negative owner earnings
while doing it.

**Likelihood: [ ] likely  [x] a real possibility  [ ] a low-level possibility** — "a real
possibility" and not lower, because *the identical mechanism fired three years ago on a smaller
balance sheet*, and because the exposure has grown faster than the buffer. This is not a
solvency call; core net debt is only $5.5bn. It is a statement about **owner earnings**: the
distribution of Dell's owner earnings has a left tail that reaches below zero and the filing
shows why.

---
## COMPUTATION — NOT A CLEARANCE

**Operator rule 3.** Q2 returned OUT; Q5 did not open. What follows is arithmetic supplied so
the queue's standing instruction — every run ends with a price and a pass/fail — is discharged.
**It carries no entry language, no recommendation, and no ranking position.**

### OWNER EARNINGS — SIX WINDOWS AND BOTH (c) ENDS

**The (c) judgment, disclosed [E2-23], [E3-44], [E5-20].** Dell is **NOT** in the
capital-intensive exception class. Capex ÷ D&A is **0.87** in fiscal 2026 — but $497M of that
D&A is **amortisation of EMC purchase intangibles**, a non-renewal charge. Stripping it,
depreciation is $2,532M against capex of $2,633M, a ratio of **1.04**. **Capex and true
depreciation are within 4% of each other**, so the [E3-44] D&A default is legitimate and the
band is unusually narrow. **(c) = total capex is the marginally more conservative end and is
used as the reported floor of the capex band; the D&A end is valid here, not invalid.**
Capitalised software is already inside the filed capex line. Stock compensation is subtracted
in full at the reported charge **[E5-06]**; SBC is 6.5% of owner earnings at its largest and
[E3-70]'s market-value uplift would not change any conclusion.

| window | capex end $M | D&A end $M | yield, capex | yield, D&A |
|---|---|---|---|---|
| FY2026 only (1 yr) | **7,829** | 7,433 | 2.30% | 2.19% |
| FY2025–26 (2 yr) | 4,456 | 4,023 | 1.31% | 1.18% |
| FY2024–26 (3 yr) | 4,652 | 4,180 | 1.37% | 1.23% |
| **FY2023–26 (4 yr — PERIMETER-CLEAN, the whole of it)** | **3,396** | **3,005** | **1.00%** | **0.88%** |
| FY2022–26 (5 yr — *contains VMware*) | 3,895 | 3,231 | 1.15% | 0.95% |
| FY2021–26 (6 yr — *contains VMware ×2*) | 4,532 | 3,427 | 1.33% | 1.01% |

**THE SPREAD CAVEAT IS CONFIRMED AGAIN — THE ELEVENTH CONSECUTIVE RUN TO FIND IT LARGER.**
Across twelve constructions the band is **$3,005M to $7,829M, a 61.6% spread**, against the
screen's published **44%**. And the screen's own two figures are **two different windows at two
different capex ends**: `oe_bottom_m 3231` is the **5-year D&A end** (VMware-contaminated) and
`oe_top_m 4652` is the **3-year capex end**. That is the INTC defect exactly, reproduced on a
different name.

*A percentage IS definable here — unlike DAL and PLPC — because every construction is positive.
But the honest headline is **dollars and a word: $3.0bn to $7.8bn, and the top of that range is
a single year in which suppliers extended terms by 33 days.***

**[E4-25]: is the range too wide to reach a conclusion?** For a *valuation* it would be. For the
question actually asked, **no** — because **every construction, at both ends, on every window,
sits between 0.88% and 2.30% against a 5.24% sovereign.** The width does not change the sign.

### THE THREE Q5 NUMBERS, computed and carrying no verdict

**1. THE YIELD.** owner earnings **$3,005M–$7,829M** ÷ market cap **$339,699M** = **0.88% to
2.30%**, against a sovereign of **5.24%**.
**Every construction is 2.94 to 4.36 points BELOW the government bond.**

**2. WHAT THE PRICE ALREADY ASSUMES.** Perpetual growth required merely to *reach* the bond:
**2.94% (on the best year ever) to 4.36% (on the perimeter-clean four-year D&A end)**. To reach
the **[E4-28] ~10% floor: 7.70% to 9.12% perpetual.**
*What the business has actually done:* owner earnings over the four perimeter-clean years are
**−369, 5,042, 1,084, 7,829** — no growth rate can be fitted to that and none is offered.
Revenue compounded **+5.5%/yr over six years**. Reported operating income did grow, **$5,411M →
$8,149M over two years**, and net income **$2,442M → $5,936M over three**. **[E4-35]** is the
relevant base rate for the floor case: fewer than 10 of the 200 most profitable companies of
2000 attained 15% for twenty years, and a claim of ~9% perpetual owner-earnings growth **in a
business whose gross margin fell 383bp in two years** carries the burden of proof against those
odds.

**3. WHAT YOU ARE PAID.** **−2.94 to −4.36 points over the sovereign.**

### THE VALUE, AS A ROUND-NUMBER RANGE [E4-01] — arithmetic, not a recommendation

| basis | value | per share |
|---|---|---|
| owner-earnings band capitalised at the **bare sovereign, 5.24%, zero growth** | ~$57bn to ~$149bn | **~$90 to ~$230** |
| the same at the **[E4-28] ~10% floor** | ~$30bn to ~$78bn | **~$45 to ~$120** |
| **the single best owner-earnings year Dell has ever filed ($7,829M), capitalised at the government bond, with no margin of safety and no discount for the 33-day payables extension inside it** | **~$149bn** | **~$230** |
| **current price, 2026-09-04 (aggregator, flagged)** | **$339,699M** | **$524.14** |

**The screamer test [E4-01] returns the THIRD outcome: the price is above the whole range**, on
every window, at both capex ends, and against the most generous single construction available.
**No margin of safety is subtracted, because none needs to be.** Windage count: **one place
only** — the perimeter cut at fiscal 2023 — and that is a correctness cut, not a conservatism
cut.

**THE PRICE, CROSS-CHECKED AGAINST A FILED FIGURE.** $524.14 is 4.8× the 52-week low of $110.22
and near the 52-week high of $534.99; the shares roughly quadrupled between February and June
2026. Because three runs have been bitten by bad quotes, the series was verified against Dell's
**own filed weighted-average repurchase prices**: $118.96–$133.22 in Q4 FY2026 (Nov 2025–Jan
2026) and ~$147 in Q1 FY2027 (Feb–May 2026), against feed closes of $127.80 (2026-01-02),
$119.16 (2026-02-02) and $210.17 (2026-05-01). **The filed prices corroborate the series.** The
quote is used for the live price only and is flagged.

---
## PASS / FAIL — the queue's standing instruction

> **FAIL. The file closed at Q2 (OUT), on [E3-03] criterion (2). Q1 IN. Q3–Q6 not opened.**
> **Price $524.14** (2026-09-04, aggregator, flagged) × **648,107,991 shares** (cover of the
> 10-Q filed 2026-06-09, accession 0001571996-26-000030) = **market cap $339,699M**, against a
> **5.24% USD sovereign** (US Treasury, 2026-09-04). Owner earnings **$3,005M–$7,829M** across
> six windows and both (c) ends; yield **0.88%–2.30%**, i.e. **2.94 to 4.36 points below the
> bond on every construction**. Value **~$90–$230/share** at the bare bond, **~$45–$120** at the
> [E4-28] floor. **No alert is armed and no PORTFOLIO row is added: the name failed on the
> BUSINESS, and a price alert on a Q2 failure is a category error** (the QLYS ruling,
> 2026-09-07).
>
> **Reversal condition, in words rather than a number:** this verdict reverses if Dell's
> **ISG gross margin stops falling while AI-optimized-server revenue keeps rising** — that is,
> if the incremental gross margin on AI servers moves durably out of high single digits — or if
> the services annuity resumes growing with the hardware. Both are readable from the same
> segment note in any future 10-K. Nothing about the price reverses it.

---
## SELF-AUDIT

- [x] Questions answered in order; stopped at the first non-IN verdict; **no verdict written for
      Q3–Q6**, which were not reached
- [x] No question marked IN carries an "unverified" or "provisional" caveat. Q1 is IN on the
      mechanism, with the magnitude instability stated and assigned to later gates
- [x] The OUT names the criterion, the corpus id, and the filed sentences it rests on
- [x] Step 0: MD&A, cash-flow statement including detail lines, and footnotes read across
      **four filings**, with accession numbers; **two figures** cross-checked against the filed
      statements (the segment identity, to the dollar, in three years; consolidated gross margin
      against the MD&A's own stated percentage)
- [x] Owner earnings on multi-year means, **six windows**, **both (c) ends**, capex band
      disclosed as a judgment with the intangible-amortisation adjustment shown
- [x] Perimeter established from the business-combination and divestiture notes, not from a
      screen field; the VMware years are excluded and the exclusion is quantified
- [x] Competitor row filled — **seven names**, filing-sourced, with method conventions and
      accession numbers in the research file; Lenovo's lower evidence rung flagged
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated
- [x] Value stated as a round-number range, not a point estimate
- [x] One bar chosen (**screamer test**, third outcome); **windage count: one**
- [x] Price dated; aggregator used for the live quote only, flagged, and **corroborated against
      a filed figure**
- [x] Share count read off the cover of the **latest periodic filing**, with the three-class
      question settled from the **charter** rather than by arithmetic
- [x] My own one-sided normalisation found and corrected in an addendum, not by editing history
- [x] `python tools/check_framework.py` run before the final commit
- [x] Run committed to git after each gate

## REGISTER

- **Verdict: OUT — about the business.**
- **One line:** Dell is the best-run assembler in its panel and assembly is not a franchise —
  its own segment note prices AI-optimized servers at a ~5% gross margin against 40% for the
  rest of ISG, and Super Micro's independent filings say 9.20¢ on the incremental dollar.
- Not UNRESEARCHED: every document that bears on the verdict was obtained and read.
- Not UNKNOWABLE: the evidence is in and it is decisive, not indeterminate.
