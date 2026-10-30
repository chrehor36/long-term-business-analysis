
---
## RECORDED BENEATH THE CLOSE — the dispatch brief's questions, answered from the documents
**None of the following is a verdict.** Q3, Q4, Q5 and Q6 were not run and are not scored.
These are the answers the fold is owed, each with the filing behind it.

### Prior B — the working-capital flag. **REFUTED as a finding; TRUE as arithmetic.**
The screen's `wc_note` read: *"ONE LINE MADE THE CASH: AccountsPayableAndAccruedLiabilities
moved 99% of 2021 OCF."* **The single line did move 99%. It did not make the cash.** Built
from PAGP's own 10-K cash-flow detail lines (SEC XBRL, newest vintage, cross-checked against
the FY2025 filed statement, where the three lines read 207 / 96 / (337) and net to −34):

| FY | operating cash | receivables | payables & accrued | inventory | **net working-capital cash** | **OCF before working capital** |
|---|---|---|---|---|---|---|
| 2019 | 2,500 | −1,158 | +1,151 | −5 | **−12** | 2,512 |
| 2020 | 1,510 | +1,432 | −1,286 | −304 | **−158** | 1,668 |
| **2021** | **1,991** | **−2,179** | **+1,970** | −18 | **−227** | **2,218** |
| 2022 | 2,404 | +649 | −830 | −10 | **−191** | 2,595 |
| 2023 | 2,722 | +79 | −141 | +102 | **+40** | 2,682 |
| 2024 | 2,484 | +94 | −77 | +120 | **+137** | 2,347 |
| 2025 | 2,931 | +207 | −337 | +96 | **−34** | 2,965 |

**In 2021 payables released $1,970M of cash and receivables absorbed $2,179M of it. Net
working capital was a $227M DRAIN, not a source.** Both lines are the same thing seen twice:
PAA buys and sells roughly $40bn of physical crude a year, so both the payable and the
receivable scale with the crude price, and 2021 is simply the year WTI recovered from the 2020
collapse. **Operating cash before working capital is the stable series — $2.2bn to $3.0bn
across five years with no step.**

**The tooling defect this exposes (operator rule 8).** `working_capital_flag()` measures **one
line in isolation and does not net its matched counter-line.** On any commodity merchant it
will fire in every year the commodity price moved, and it will **name the wrong cause** — here
it named the year the cash was *drained* as the year the cash was *made*. This is the
tail-triage lesson of 2026-09-12 in a new place: the arithmetic was right and the description
of what it meant was wrong. **Proposed fix, not made here: where a filer tags both
`IncreaseDecreaseInAccountsAndOtherReceivables` and
`IncreaseDecreaseInAccountsPayableAndAccruedLiabilities`, the flag should report the NET
working-capital cash effect beside the single line, and refuse the "one line made the cash"
string when the counter-line offsets more than half of it.** The two tags carry **opposite
cash-sign conventions** in the standard taxonomy (an increase in receivables is a use; an
increase in payables is a source), which is the likely reason they were never netted.

### Prior E — the latest 8-K EX-99.1. **CONFIRMED, at full strength.**
Q2 2026 earnings release, 8-K **0001581990-26-000023**, furnished 2026-08-07. **"Adjusted
EBITDA" appears 43 times** in the release and 45 times in the 10-K. The second headline bullet
is *"Delivered strong second-quarter **Adjusted EBITDA attributable to PAA of $738 million**"*;
the non-GAAP table leads with Adjusted EBITDA, Adjusted net income, **"Implied DCF per common
unit"** and **"Adjusted Free Cash Flow"**. Depreciation and amortization was **$953M in FY2025
against $1,428M of operating income** — so the excluded charge is two-thirds the size of the
profit. [E4-29] is not a stray usage here; **the metric is constitutional**:
- the filer's own **targeted credit profile** is written in it — *"a leverage multiple
  averaging between 3.25x to 3.75x, which is calculated as total debt plus 50% of the value of
  preferred units, divided by **Adjusted EBITDA attributable to PAA**"* (10-K FY2025);
- the **bank covenant** is written in it — the Revolving Credit Agreement of 2026-06-12 (8-K
  **0001104659-26-075189**) *"limits Consolidated Funded Indebtedness to adjusted Consolidated
  EBITDA to no greater than 5.00 to 1.00, which increases to 5.50 to 1.00 during an
  Acquisition Period"*;
- and the release headlines *"Adjusted Free Cash Flow"* of **$4,189M for Q2 2026** against
  $348M a year earlier — a figure that is mostly the **$3.9bn of divestiture proceeds**.
**[E2-54] is the corpus's answer to an EBITDA covenant**: *"whenever someone creates a capital
structure that does not allow all interest, both payable and accrued, to be comfortably met out
of current cash flow net of ample capital expenditures — zip up your wallet"* — accrued
interest counts, cash flow is the source, and capex comes out first. Recorded, not scored.

### Prior F — the perimeter. **The screen's `deal_note` was WRONG, and three later events matter.**
`deal_note` read: *"2 8-K Item 1.01 filing(s) since 2026-02-27, none carrying a merger
agreement (EX-2.1) — most likely a credit facility or offering."* Opened, all of them:

| date | accession | what it actually is |
|---|---|---|
| 2026-03-03 | 0001104659-26-022839 | Third Amendments to the revolver and hedged-inventory facilities. Credit facility — the note's guess was right here. |
| **2026-05-12** | **0001104659-26-059512** | **Item 2.01 — COMPLETED SALE of the Canadian NGL business to Keyera for approximately CAD $5.328bn (~USD $3.883bn), ~$3.3bn net. Exhibits EX-2.2, EX-2.3 and EX-2.4 are the three amendments to the Share Purchase Agreement.** |
| 2026-06-17 | 0001104659-26-075189 | New Revolving Credit Agreement; the old revolver and the hedged-inventory facility repaid and terminated. |
| **2026-08-07** | **0001581990-26-000023** | Q2 2026 earnings release (Item 2.01 **and** 7.01 — the release is tagged 2.01). |
| **2026-09-14** | **0001104659-26-107550** | **$700M of 6.750% Series A and $800M of 7.000% Series B Junior Subordinated Notes due 2056, issued five days ago**, plus an Item 8.01 pro forma for the EPIC Crude purchases. |

**The defect in the screen inference, precisely: it searched for `EX-2.1` and this deal's
agreement exhibits are `EX-2.2` through `EX-2.4`, because the original SPA of 2025-06-17 was
filed as EX-2.1 to the Q2 2025 10-Q and only the amendments were attached to the closing 8-K.**
A deal-perimeter test keyed to one exhibit number misses every transaction whose agreement was
filed earlier and amended at closing. **This is the MRVL lesson repeating: `newest_filing
2025-12-31` while a $3.9bn divestiture, a $2.65bn acquisition and $1.5bn of new hybrid debt sat
in later filings.**

**Three perimeter events the FY2025 statements do not carry:**
1. **The Canadian NGL business is gone** (closed 2026-05-12). It is already in discontinued
   operations in the FY2025 10-K, so the continuing-operations series is the right one — but
   the FY2025 *cash-flow statement* still includes *"Cash provided by operating activities -
   discontinued operations | 484"*, i.e. **$484M of the $2,931M operating cash belongs to a
   business that no longer exists.**
2. **EPIC Crude Holdings / Cactus III was bought in two steps** (55% on 2025-10-01, the
   remaining 45% effective 2025-11-01), which is most of the **$2,651M** of FY2025 acquisition
   cash. The company's **own pro forma** (8-K 0001104659-26-107550, Item 8.01), presenting
   FY2025 as if both steps had closed on 1 January 2025, shows net income from continuing
   operations attributable to Class A shareholders falling from **$152M to $135M**, and per
   Class A share from **$0.77 to $0.68** — *the acquisition is dilutive to the Class A
   shareholder on the company's own arithmetic.* Recorded as a fact; **Q3 was not run and no
   capital-allocation verdict is written.**
3. **$1.5bn of junior subordinated notes at 6.750% and 7.000%, due 2056, issued 2026-09-14** —
   six days before this run and after the newest periodic filing. Hybrid debt priced at 6.75–7.00%
   against a 30-year Treasury of 5.34% on 2026-09-18.

### The survival shape the evidence points to — recorded, NOT a Q4 finding
Q4 was not reached, so **no shape is named as this business's death.** What the Q2 evidence
shows is the signature of **#11 THE PASS-THROUGH** (TM, 2026-09-13: the company survives but
the gains go to customers and suppliers): tariff volumes **+8%** (8,934 → 9,680 kb/d) and
Permian **+9%**, while long-haul Permian contract rates **reset to market downward** and the
five-year return on deployed capital sits at **5.6%** against a peer median of **13.7%**. The
barrels grew; the money went to the shipper. **[E3-62]'s second step answers itself here** —
*"how much is going to stay home and how much is just going to flow through to the customer"* —
and the filer's own risk factor names the reason: *"relatively low barriers to entry"* and
competitors who *"may be motivated to reduce transportation rates to levels approaching
variable operating costs."* Shapes **#5 THE SELF-LIQUIDATING DISTRIBUTION**, **#6 THE BORROWED
BALANCE SHEET** and **#28's normalisation instruction** were carried into this run as
candidates and are **untested**, because the file closed two gates before Q4.

### What I could not resolve, and the document that would resolve it
- **PAGP's own entity-level cash tax path.** PAGP carries a **$1,136M deferred tax asset**
  (2025-12-31) and pays corporate tax on income a PAA unitholder receives untaxed at the
  entity. How fast that asset is consumed, and therefore what fraction of the PAA distribution
  actually reaches a Class A shareholder over the next decade, is **not computable from the
  documents read**. *The document that would resolve it: Note 15 (Income Taxes) of the FY2025
  10-K read against the deferred-tax rollforward, plus the Section 754 / basis discussion in
  the Class A share tax summary.* **Not fetched, because the file closed at Q2 and no
  valuation was owed.**
- **The split of PAA's Crude Oil Segment Adjusted EBITDA between fee-based and merchant
  margin.** The 10-K describes both and does not disaggregate them. *The document that would
  resolve it: PAA's own investor-day materials or a supplemental disclosure; it is not in the
  10-K, the 10-Q or any 8-K read here.* Recorded as a real gap; it does not change Q2, because
  both legs fail [E3-03] — the fee leg on clause (3) and the merchant leg on clause (2).

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN, Q2 OUT, and the run stopped
      there. Q3–Q6 carry no verdict and no checkbox is ticked for them.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests
      on the 10-K and the 10-Q, both read, both cited by accession.
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** None was issued.
      The two unresolved items above are recorded *beneath the close*, with their documents
      named, and neither is a gate verdict.
- [x] **Every UNKNOWABLE verdict states what specifically cannot be known.** None was issued.
      Q2 is OUT, not UNKNOWABLE: the resolving documents exist and were read, and they say the
      business fails.
- [x] **Step 0: the filing was read, with accession number; a figure was cross-checked.** Seven
      documents listed with accession numbers. FY2025 operating cash of $2,931M checked against
      the filed Consolidated Statements of Cash Flows, including its two component lines.
- [n/a] **Owner earnings on a multi-year mean; window stated; capex band disclosed.** Q4 was
      not reached. **No owner-earnings figure is reported for this name**, and the screen's
      $1,318–1,750M is refuted at Q1 as the wrong entity's number rather than replaced by
      one of mine.
- [x] **Competitor row filled, or the moat marked PROVISIONAL and UNRESEARCHED.** Filled: ten
      peers, five years, one metric, every figure from the peer's own 10-K facts. Enbridge
      named as the excluded eleventh with its obstacle stated. The moat is **NONE**, not
      PROVISIONAL.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** USD 5.34%,
      2026-09-18, US Treasury daily par yield curve, struck this session. Nothing inherited.
- [n/a] **Value stated as a round-number range.** No value is stated. Q5 did not open.
- [n/a] **One bar chosen, not both; windage count stated.** No bar was used; no margin of
      safety was applied to anything, because nothing was valued.
- [x] **Prices dated; aggregator used for live quotes only and flagged.** PAGP $27.67 and PAA
      $25.37, both 2026-09-18, both flagged as aggregator quotes, used only for the
      security-premium fact and the cap, never for a verdict.
- [x] **Run committed to git.** Q1+Q2 at `e8a5733`; this tail and the fold in the commit named
      in the register entry.

**Two audit items tested rather than ticked**, per the 2026-09-20 finding that a match is not a
reading:
- **The SBC-of-zero check (RESUME STATE 3F).** `run.py` resolved stock compensation for all
  three years (51 / 52 / 50). Verified against the filed cash-flow statement, which reads
  *"Equity-indexed compensation expense | 50 | 52 | 51"* for 2025 / 2024 / 2023. **No silent
  zero. `ShareBasedCompensation` is not the tag this filer uses**, and the resolution came
  through another element — recorded so the next reader does not re-test it.
- **The ledger-id check.** Every id cited above was read out of `principle_ledger.csv` before
  use. **The file carries 286 data rows plus a header, not 267** — see the defect note in the
  register entry.

---
## REGISTER
- Verdict: **[x] OUT (about the business)**
- One line: **PAGP is a corporate-taxed wrapper on ~198 million PAA common units — about a
  sixth of the consolidated statements the screen priced — and the crude-oil business
  underneath fails [E3-03] on two of three clauses in the filer's own words: an overbuilt
  market with "relatively low barriers to entry" where rivals will "reduce transportation rates
  to levels approaching variable operating costs", and a "majority of our pipeline profits"
  that "remain regulated by FERC". Ten peers on the same metric, same five years, from their own
  filings: PAA earns 5.6% on deployed capital against a peer median of 13.7%, tenth of eleven.**
- Not UNRESEARCHED and not UNKNOWABLE: every document that could resolve the franchise question
  was read, and each of them answers it the same way.
