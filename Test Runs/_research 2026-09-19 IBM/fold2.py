# -*- coding: utf-8 -*-
"""Step 3 of the fold: the narrative fold into the prepped reading list, plus the
overnight-log line.  One read-modify-write per file, because the tree is shared."""
import io, os, datetime

LIST = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
LOG = 'Screens/_daily/OVERNIGHT LOG.md'

NARRATIVE = u"""
---

## IBM (International Business Machines Corporation) - run 2026-09-19 - Q1 IN, Q2 OUT
*WAVE 6. CIK 0000051143, confirmed from the EDGAR company lookup rather than from the brief.*

**WHY THIS NAME HAD NEVER BEEN RUN, and the answer is still that nothing on disk says.** IBM is one
of the eleven the 2026-09-01 triage dropped silently and the operator's screenshots recovered on
2026-09-19. It was read as unlabelled. **The gate that closed it could not have been guessed from
the absence of a label**, and the run's own finding is that the interesting half of IBM passes the
franchise test and the other two thirds fail it - which is exactly the kind of answer a label would
have flattened in either direction.

**THE FINDING, in one paragraph.** IBM contains a real franchise. z/OS runs on no machine but IBM
Z; the Transaction Processing software stack ($8,603M) is a toll on installed mainframe capacity;
Infrastructure Support ($5,100M) is the maintenance annuity those machines create; the switching
cost is the customer's application estate, not IBM's box. **That franchise is 28-33% of revenue, and
IBM discloses its profit and its units nowhere**, so the strongest version of the bull case cannot
be evidenced even in principle. For the other two thirds, **the refusal of [E3-03] criterion 2 is
written by IBM**: *"highly competitive environment"*, *"hundreds of competitors worldwide"*, *"we are
regularly exposed to new competitors"*, and **price listed third among its own principal methods of
competition.** [E4-04] then excludes the company because that two thirds is held **by purchase** -
Kyndryl spun, Watson Health, The Weather Company and QRadar SaaS assets sold, Apptio, Turbonomic,
StreamSets/webMethods, HashiCorp and Confluent bought, the Software revenue categories re-presented
in Q1 2025 - while the franchise legs are flat to shrinking. **Price US$229.55, cap US$216,267M,
sovereign USD 5.34%. FAIL at Q2.**

**REFUTED PRIORS - four of them, and three were the brief's own hypotheses:**
1. **"The mainframe cycle and its attach revenue"** was offered as a Q1 item and turned out to be
   the **Q2 direction test [E4-32]**, because the filings show both ends of one cycle: **IBM Z
   +51.7% in FY2025** on the June 2025 z17 launch and **-42% in Q2 2026**, with Transaction
   Processing +2.3% then **-8%**. A moat whose revenue does that in five quarters is not widening.
2. **"The long record of buybacks funded partly by debt"** is a record that ENDED. IBM spent about
   **$125bn on repurchase between FY2007 and FY2019** and **$0 in FY2020-FY2025**; the only
   "repurchases" since are $1,018M of share withholding for employee taxes, which is payroll. The
   live charge is the opposite of the brief's: **six years of buying other people's businesses
   instead of its own**, $22,306M of acquisition cash FY2021-25 plus $11.5bn for Confluent, at a
   revealed **$1.81 of cash per $1 of added annual revenue**. And [E2-51]'s
   turned-back-on-repurchases charge is only half true, because on this run's own arithmetic the
   stock is not at a material discount, so declining to buy it **obeys** [E5-08].
3. **"The pension is large"** - it is large and it is **not a claim**. Net underfunded **$2,283M and
   falling**; the qualified plans are in **surplus** (US Personal Pension Plan *"137 percent
   funded"*, worldwide qualified *"116 percent funded"*, a $7,544M prepaid asset); the $9,828M
   underfunded liability is mostly **non-qualified** US promises ($3,472M against $5M of assets) and
   non-US plans; and the filing says *"In 2026, we are not legally required to make any
   contributions to the U.S. defined benefit pension plans."* **More striking: the company that was
   once the standard example of pension-flattered earnings now has the most conservative expected
   return on plan assets of any name calibrated in this project - 5.50% against a 5.34% long bond,
   sixteen basis points, against HON's 200bp and KMB's 76bp** - and non-operating retirement cost
   was **minus** $65M in FY2025, so there is no pension credit in earnings at all.
4. **"Free-cash-flow definitions against the filed cash-flow statement [E4-41]"** - IBM's definition
   produces a number **LARGER than its audited operating cash flow** ($14,734M against $13,193M),
   because it adds back the growth of its own loan book. That looks like the flag and **is not**:
   the reconciliation is printed on the same page, the offsetting *"Change in total debt 2.9"* two
   lines below it, and the Financing segment's 9.0:1 leverage disclosed separately. **The
   [E4-41]-shaped finding at IBM is elsewhere** - FY2025 is a mainframe cycle peak, and the mean has
   to be normalised down for it.

**WHAT THE FILE ADDS TO THIS PROJECT'S METHOD:**
- **A perimeter case the CNR rule had not met before: the income statement was recast and the
  cash-flow statement was not.** IBM presented Kyndryl as discontinued operations *"for all periods
  presented"* in revenue and segments, so the five-year revenue CAGR is legitimate from FY2020 -
  **but the FY2021 annual report says in words that the cash-flow statement *"include[s] the cash
  flows of discontinued operations"* and footnotes one aggregate figure a year ($1.6bn/$4.4bn/$4.5bn
  for 2021/2020/2019) with no Kyndryl cash-flow statement.** So FY2019-FY2021 operating cash is
  **refused, not adjusted**, the clean perimeter is FY2022-FY2025 plus the TTM, and the five-year
  default [E2-42] is short by one year with the reason quoted. **Standing lesson: "was it recast?"
  is a per-statement question, not a per-filer one.** A run that checks only the revenue line will
  believe a spin-off perimeter is clean when the cash-flow statement is not.
- **A captive-finance separation that the FILER publishes, and the direction that has to be
  corrected anyway.** The GM/F/TM/HMC lineage had to find the separation in segment notes or a
  finance subsidiary's own 10-K. IBM prints it in the MD&A as *"Less: change in Financing
  receivables"*. But DELL's counter-precedent decides which way it runs: the receivable build is an
  **operating** outflow while the debt that funds it is a **financing** inflow, so consolidated
  operating cash is understated by the loan book's growth and IBM's own adjustment is right in
  substance and incomplete, because it credits the asset build back without charging the $2,977M of
  matched Financing segment debt that paid for it. **The run therefore carries a Ford-style ladder -
  A consolidated (conservative), B industrial (generous) - and explicitly refuses a look-through
  construction, with the reason stated so no later reader adds the $521M of segment profit twice.**
  The two constructions differ by **$3.2bn in FY2025 and $1.2bn the other way in FY2023**, which is
  the largest single source of width in the file. **A captive lender inside a technology company
  moves owner earnings more than the capex band does.**
- **A (c) decomposition where the filed D&A line is wrong in TWO independent places at once.** The
  raw D&A end of $5,021M charges **$900M of operating-lease ROU amortisation** whose rent operating
  cash has already paid (the CRM precedent) **and $2,166M of acquired-intangible amortisation** that
  renews nothing, because $8,316M a year of R&D above the line already does (the HON/UNH/EFX
  precedent). Take both out and (c) is **$1,955M**, against a capex end of $1,617M - a $338M band on
  a $67.5bn company. **The screen's number would have printed a 2.99% yield; the refusal is worth
  $3.1bn a year and is stated in writing with its size.** This is NOT the CVX inversion: the raw
  D&A end is still the low end, it is just an invalid magnitude.
- **The CGNX ruling earned its keep again.** *EBITDA does not appear in IBM's 10-K or annual
  report.* It appears **eight times in the furnished Q2 2026 earnings release**, with **adjusted
  EBITDA margin 27.8% against a 14.4% GAAP pre-tax margin** and two reconciliations, one of them
  **operating cash flow to adjusted EBITDA**. A run that read only the annual report would have
  scored [E4-29] clean on a company whose quarterly narrative carries the measure. **Third
  consecutive confirmation of the ruling.**
- **A guidance test where the company BEAT its own numbers, and the flag still fires on the
  practice.** [E3-48]'s prescribed action was performed from the filings: FY2025 guidance
  (*"at least 5 percent"* constant-currency revenue, *"about $13.5 billion"* of free cash flow) was
  **beaten on both legs** (6.1%, $14,734M); FY2026 was reaffirmed in April and **cut on 2026-07-22**
  from *"more than 5 percent"* to *"four-to-five percent"*. So the outturn record is **better** than
  Buffett's stated nine-in-ten base rate, and **[E5-30]** still bites, because it is about the
  ratchet rather than this year's accuracy. **Recording both halves is the point**: a run that only
  scores the flag misses that the company told the truth, and a run that only scores the outturn
  misses that quarterly guidance is a commitment it cannot now abandon.
- **[E2-49] found in a compensation modifier, which is a new location for that flag in this
  project.** The PSU **relative-ROIC** modifier *"was 0"* for the 2023-2025 programme - it paid
  nothing - and for 2025 grants the Committee replaced it with a **relative-TSR** modifier, in a
  year of about 40% total shareholder return, **while widening the leverage range from 0-150% to
  0-200%** and the maximum from 170% to 220% of target. *"Yardsticks seldom are discarded while
  yielding favorable readings."* The mitigation is real and is recorded: it was announced in
  advance, in the proxy, with a reason - though the stated reason explains the revenue and cash
  weightings and not the swap of a capital-return modifier for a share-price one.
- **A candour artifact worth keeping as a calibration case.** On **2026-07-14, eight days before the
  quarter's results**, IBM furnished an 8-K carrying *"Arvind Krishna's Letter to IBM Investors"*
  with preliminary figures and this: *"These conditions require our teams to execute perfectly, and
  this quarter we faltered. We did not adapt and move quickly enough, and numerous large deals
  failed to close on the timelines we expected, driving the majority of our shortfall. **These are
  not excuses, but they are realities.**"* That is **[E2-57]** answered in the right direction and
  **[E2-72]** authorship, ahead of the required disclosure. **It belongs in the same drawer as
  Berkshire's own reserving-error table [E2-67]** as an example of what the positive pole looks like
  when it is real - and it sits in the same six weeks as three new multi-billion-dollar programme
  announcements, which is why **[E4-52]** is recorded here as a converging system of *promotional*
  incentives rather than as an integrity finding.
- **[E2-43]'s goodwill wedge at its most extreme so far: tangible equity is NEGATIVE $46,368M.**
  $67,717M of goodwill plus $11,391M of other intangibles against $32,740M of equity, and $170,605M
  of treasury stock in the denominator. **A 35% return on equity here measures three decades of
  buybacks.** On [E2-73]'s denominator - the return on the underlying assets, not on what was paid -
  pre-tax income is 14.2% of tangible assets, and the honest two-sentence statement is that the
  operating business earns very well on the tangible capital it uses while the $67.7bn spent to
  assemble it earns nothing in the accounting at all.
- **Shape #10 THE CAMOUFLAGE, with a feature proposed and no register changed: the company sells the
  service that erodes its own franchise.** IBM Consulting's disclosed demand drivers include
  *"application migration and modernization"* - the one activity that destroys mainframe switching
  costs - in the same annual report that calls IBM Z *"the backbone of enterprise IT."* SONY's
  camouflage recycles strong-leg cash into legs that must re-win a race; IBM adds a leg that is paid
  to shorten the strong one. **Offered to the operator as a feature of #10, not as shape #22.**
- **Shape #1 REFUSED with the arithmetic, and the refusal is informative.** IBM's **total purchase
  obligations are $4,817M**, $1,958M of it in 2026, against $67.5bn of revenue; Oracle's comparable
  exposure was **$260bn of leases not yet commenced, 8.13x its operating cash flow.** The quantum
  *"more than $10 billion"* and Lightwell *"$5 billion"* figures are **announced intentions**, and
  the contractual-obligations table proves it. The ORCL distinction - *"a company that could stop
  and a company that has contracted not to"* - puts IBM firmly in the first class, and that is the
  cleanest test of the shape yet run.

**THE STRONGEST FACT AGAINST THE VERDICT, because [E4-51] requires it to be stated better than its
holders would.** **IBM's owner earnings have grown faster than the ~10% floor requires.** On the
clean perimeter, construction A's capex end went $7,587M (FY2022) to $9,861M (FY2025) - **9.13% a
year** - and construction B's $8,287M to $13,061M, **16.38%**; industrial operating cash rose 48% in
four years; IBM's own free cash flow compounded 16.58%. **The floor needs 5.14% in perpetuity.** A
holder can say fairly that the price assumes less growth than the company has just delivered, on
$4.5bn of realised run-rate savings, with Software 79% recurring and ARR up $2bn, the pension risk
transferred twice, and a CEO who pre-announced a bad quarter in his own name. **Four answers, none
by assertion:** the file closed at **Q2**, on the business, and no growth rate reopens a Q2;
**FY2022 is a trough and measured from FY2023 construction A is DOWN, $11,309M to $9,861M**, which
is precisely the *"calculated selection of either initial or terminal dates"* **[E4-38]** warns
against, so every window is published; the growth is margin recovery plus a cycle peak plus bought
revenue and none of the three is a perpetuity; and part of B's 16.38% is **the finance book
growing**, which is lending, not earning.

**TOOLING AND BRIEF DEFECTS FOUND (five):**
1. **`tools/run.py` and `floor_screen.py` cannot price IBM's (c) correctly, for a reason no guard can
   detect.** IBM's D&A add-backs are `Depreciation` (which *includes* $0.9bn of operating-lease ROU
   amortisation, disclosed only in a footnote to the cash-flow statement) and
   `AmortizationOfIntangibleAssets` (which is *"Amortization of capitalized software **and acquired
   intangible assets**"* combined). **A screen at the D&A end therefore charges rent twice and
   charges an acquisition artifact as renewal, and prints a (c) of $5,021M against a defensible
   $1,955M - a 2.99% yield against 4.4%-5.7%.** Neither error is visible from the tag name. **This
   is the same class as the ELF finding** (the D&A end triple-counting on filers who capitalise into
   other assets) and the same remedy applies: only a reader sees which class a filer is in.
2. **`OperatingIncomeLoss` is untagged for IBM** - the limit the ORCL run recorded from the other
   side, met again from IBM's own side. The cell was left empty in the competitor row rather than
   filled with my arithmetic, in both directions.
3. **The non-USD IFRS limit is still live and was met again.** SAP's companyfacts carries `Revenue`
   in EUR and in USD, and the USD facts are offering-document translations, not its accounts. The
   row reads SAP in **EUR**, using a growth rate and three ratios that are currency-consistent, and
   says so. **Recorded, not worked around**: the RESUME STATE's judgment that a currency guard must
   be designed in rather than a unit filter loosened still stands.
4. **The brief said the register held 117; it held 118 by the time this run folded**, because the KO
   cycle folded in between. The count-before-and-after protocol caught it and the entry is numbered
   **119**. **The protocol works and briefs should stop quoting a count at all** - they should say
   *count it*, which this one did also say.
5. **The brief's Q3 framing - "the perimeter and the accounting history are the work here" - was
   half right and the half that was wrong is worth recording.** The perimeter work turned out to
   belong to **Q4** (the cash-flow statement was not recast), and Q3's sharpest material was not
   accounting history at all but **a compensation modifier ([E2-49]) and a furnished earnings
   release ([E4-29])**. The brief was right to name [E3-48], [E4-41], [E4-27] and [E4-52] as the
   ids and right to tell the run to check every id against the ledger - **[E4-52] is indeed the
   lollapalooza row and [E4-27] the incentives row**, and the check took one command.
"""

s = io.open(LIST, encoding='utf-8').read()
assert 'IBM (International Business Machines Corporation) - run 2026-09-19' not in s, 'already folded'
if not s.endswith('\n'):
    s += '\n'
io.open(LIST, 'w', encoding='utf-8').write(s + NARRATIVE)
print('narrative fold appended,', len(NARRATIVE), 'chars')

LOGLINE = (
 u"- 2026-09-19 10:16 EDT | IBM | "
 u"Q1 IN / **Q2 OUT** (on the business; Q3, Q4, the price computation and Q6 recorded, not governing). "
 u"[E3-03] criterion 2 HOLDS for the mainframe complex (~28-33% of revenue: Transaction Processing $8,603M "
 u"+2.3% FY2025 then -8% in Q2 2026, IBM Z +51.7% then -42%, Infrastructure Support -0.1%) and is REFUSED for "
 u"the other two thirds by IBM’s own Competition section (hundreds of competitors, regularly exposed to new "
 u"competitors, price third among its own methods of competition); [E4-04] excludes the company because that two "
 u"thirds is held by PURCHASE - four sold or spun and six bought in five years, $22,306M of acquisition cash for "
 u"$12,356M of added annual revenue, $1.81 per $1; ten-peer row puts IBM LAST of eleven on five-year revenue growth "
 u"at 4.12%; the mainframe comparator cell does not exist (BMC private, Broadcom undisclosed, no competing mainframe) "
 u"so that class stays PROVISIONAL and un-promotable, and Transaction Processing profit is UNKNOWABLE, not "
 u"UNRESEARCHED. Kyndryl perimeter: the revenue line WAS recast and the CASH-FLOW statement was NOT, so FY2019-21 "
 u"are refused not adjusted; clean perimeter FY2022-25 + TTM. Financing arm separated the GM/F/TM/HMC way and IBM "
 u"files the separation itself (segment debt $15,093M at 9.0:1, non-Financing debt $46,167M); both constructions "
 u"carried, look-through explicitly refused. (c) $1,617M-$1,955M after excluding $900M of lease ROU amortisation and "
 u"$2,166M of acquired-intangible amortisation; the raw D&A end of $5,021M refused in writing. Owner earnings "
 u"$9,486M-$12,234M over every window and both (c) ends = 4.39%-5.66%, the ~10% floor missed by 4.3-5.6 points "
 u"everywhere; value roughly $110-$160 a share. Five Q3 prompts fired and were read ([E4-29] adjusted EBITDA margin "
 u"27.8% vs 14.4% GAAP pre-tax, furnished release only; [E4-22]/[E5-30] quarterly guidance, FY2025 BEATEN on both "
 u"legs and FY2026 CUT on 07-22; [E2-49] a relative-ROIC modifier that was 0 swapped for relative TSR with the range "
 u"widened to 0-200%; [E4-27] pay on non-GAAP operating EPS and IBM’s own free cash flow; [E2-30](2) six years of "
 u"zero buyback while $22.3bn went to acquisitions) against a clean accounting read (pension expected return 5.50% vs "
 u"a 5.34% long bond, net underfunded $2,283M and falling, no 2026 US DB contribution required) and the CEO’s own "
 u"pre-announcement letter of 2026-07-14. Shape #10 THE CAMOUFLAGE with a proposed feature (the company sells the "
 u"service that erodes its own franchise); #1 refused on $4,817M of total purchase obligations against ORCL’s "
 u"$260bn. Nothing armed - a Q2 failure is a failure on the business (the QLYS ruling): no alerts.json band, no "
 u"PORTFOLIO row. Register 119 (the brief said 117; KO folded in between and the count-before-and-after protocol "
 u"caught it) | "
 u"$229.55 (2026-09-18 close, Yahoo regularMarketPrice 16:00:03 ET, aggregator flagged) x 942,134,390 (Q2 2026 10-Q "
 u"cover, 0000051143-26-000078) = cap $216,267M; sovereign 5.34% USD (US Treasury 30Y, 09/18/2026, struck fresh) | "
 u"PASS | see fold commit")

if os.path.exists(LOG):
    l = io.open(LOG, encoding='utf-8').read()
else:
    l = u'# OVERNIGHT LOG\n'
if not l.endswith('\n'):
    l += '\n'
io.open(LOG, 'w', encoding='utf-8').write(l + LOGLINE + '\n')
print('overnight log appended')
