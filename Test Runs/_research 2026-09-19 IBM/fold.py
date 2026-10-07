# -*- coding: utf-8 -*-
"""The six-step fold for the IBM run, done as ONE read-modify-write per file because
concurrent runs share this tree (KO by a scheduled cycle, DIS and others in parallel)."""
import io, re, sys

QUEUE = 'Screens/WATCHLIST RUN QUEUE.md'
LIST = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'

# ---------------------------------------------------------------- count helper
def register_slice(text):
    """Text between the LAST line that is exactly the COMPLETED heading and the
    THE WRITE-EARLY PROTOCOL heading."""
    lines = text.split('\n')
    hidx = [n for n, l in enumerate(lines) if l.strip() == '## COMPLETED FROM THE QUEUE']
    assert hidx, 'COMPLETED heading not found'
    h = hidx[-1]
    widx = [n for n, l in enumerate(lines) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
    assert widx, 'WRITE-EARLY heading not found'
    w = widx[0]
    assert w > h, 'headings out of order'
    return h, w, lines

def count_entries(lines, h, w):
    """A register entry starts a line with '- **'."""
    return sum(1 for l in lines[h + 1:w] if l.startswith('- **'))

q = io.open(QUEUE, encoding='utf-8').read()
h, w, lines = register_slice(q)
before = count_entries(lines, h, w)
print('register entries BEFORE:', before)

ENTRY = """- **IBM (International Business Machines Corporation), 2026-09-19 - FAIL at Q2 (OUT ON THE BUSINESS: a real, unsubstitutable mainframe franchise over
  roughly a THIRD of the revenue, and bought growth over the rest). **WAVE 6**, one of the eleven the 2026-09-01 triage dropped with no reason recorded
  anywhere on disk; read as unlabelled, and the gate that closed it was not predictable from the label's absence. **CIK 0000051143 confirmed
  independently** from the EDGAR company lookup (INTERNATIONAL BUSINESS MACHINES CORP, Armonk NY, SIC 3570, New York incorporation, file number 1-2360), not
  taken from the brief. **Q1 IN**: four filed segments - Software $29,962M at an 83.5% gross margin and $9,920M of segment profit, Consulting $21,055M at
  28.1% and $2,464M, Infrastructure $15,718M at 58.6% and $3,458M, Financing $737M and $521M - with the caveat the filing itself supplies, that segment
  profit is stated BEFORE the $1,685M of stock pay the reconciliation removes, so every segment margin quoted is flattered. Transaction Processing $8,603M is
  the mainframe's own stack, +2.3% in FY2025 on the June 2025 z17 launch and **-8% in Q2 2026**; IBM Z itself **+51.7% in FY2025 and -42% in Q2 2026**. The
  scarce input is the installed IBM Z base; **IBM discloses IBM Z revenue in dollars nowhere**, so the mainframe complex is sized at **28-33% of revenue
  ($19-22bn)** with the arithmetic shown, and the *"mainframes handling 70% of the world's transactional workflows"* figure is flagged as IBM's own Institute
  for Business Value, self-cited. The ten-year answer is split - yes for the mainframe, no for the other ~70% on IBM's own words - and that split was written
  down AT Q1 so Q2 could not borrow the mainframe's durability for the whole company. **Q2 OUT**: [E3-03] criterion 2 is satisfied for the mainframe and
  REFUSED for the rest by IBM's own Competition section (*"highly competitive environment"*, *"hundreds of competitors worldwide"*, *"we are regularly exposed
  to new competitors"*, and **price listed third among its own principal methods of competition**); **[E4-04] applied rather than recited** - the mainframe
  leg PASSES (R&D on z16-z17 defends the same architecture, the Coca-Cola case [E3-49, E5-23]) and the COMPANY fails because two thirds of it is held by
  purchase: Kyndryl spun 2021-11-03, Watson Health, The Weather Company and QRadar SaaS assets sold, Apptio, Turbonomic, StreamSets/webMethods, HashiCorp and
  **Confluent (closed 2026-03-17, $11,268M cash for the common plus $269M for equity awards)** bought, and the Software revenue categories re-presented in Q1
  2025 with *"Hybrid Platform & Solutions"* and *"Security"* deleted. **The run deliberately does NOT rest on the contested rapid-change reading the TSM run
  flagged for the operator**: its finding is the narrower half - the ASSET is replaced, not the process - and it survives whatever the operator rules on
  [E4-04]'s scope. Direction [E4-32] reads the wrong way: the two franchise legs are +2.3%-then--8% and -0.1% while the bought legs grow, Consulting signings
  fell **13.3%** to $21,757M, and **$22,306M of acquisition cash FY2021-25 bought $12,356M of added annual revenue - $1.81 per $1** before $8,316M a year of
  R&D (R&D plus mean acquisition spend = 18.9% of revenue). **And the growth leg is paid to erode the franchise leg**: Consulting's own disclosed demand
  drivers include *"application migration and modernization"*. **The competitor row: ten peers** (MSFT, GOOGL, AMZN, ORCL, ACN, SAP, DELL, HPE, AVGO, NOW),
  each on its own five consecutive fiscal years, four metrics - revenue CAGR, gross margin and its 5-year change, R&D % of revenue, stock pay / operating cash
  - and **IBM is LAST of eleven on revenue CAGR at 4.12%**, mid-pack on margin (58.2%, +2.2 pts) and R&D (12.3%), second-best on stock pay (13.0%). Unfillable
  cells named, not guessed: no gross margin for ORCL or HPE (no cost-of-revenue subtotal undimensioned - the mirror of the limit the ORCL run recorded on IBM,
  whose `OperatingIncomeLoss` is untagged), no R&D for AMZN (it reports *"Technology and infrastructure"*), **SAP read in EUR as a 20-F IFRS filer** (the
  recorded non-USD limit, handled by reading the filer's own unit rather than loosening a filter). **THE CELL THAT WOULD HAVE DECIDED THE MAINFRAME DOES NOT
  EXIST**: BMC is private (KKR), Broadcom folds CA's mainframe software into an undisclosed *Infrastructure Software* segment, and nobody sells a competing
  mainframe - so that class is **PROVISIONAL and un-promotable [E3-28]**, and Transaction Processing profit is disclosed in no filing, which is **UNKNOWABLE,
  not UNRESEARCHED**. [E2-43]: **tangible equity is NEGATIVE $46,368M** ($67,717M goodwill + $11,391M intangibles against $32,740M of equity), so the 35%
  FY2025 ROE measures **$170,605M of treasury stock**, not the business; on [E2-73]'s denominator pre-tax income is 14.2% of tangible assets. **Q3 IN,
  RECORDED NOT GOVERNING** - declared a **BINARY GATE** (daily execution ticked on the CEO's own *"this quarter we faltered"*; leverage ticked and quantified
  at non-Financing debt $46,167M rising to about $49bn, debt/OCF 4.64x, negative tangible equity; control not ticked). No disqualifier found: clean PwC opinion
  on the statements AND on internal control, one critical audit matter (uncertain tax positions), no restatement, no material weakness, no SEC matter found in
  FY2021/FY2022/FY2025, the single named action an ERISA suit dismissed with prejudice 2025-12-11 with no material impact; PwC or predecessors *"since 1923"*
  recorded beside [E5-32] without inventing a tenure rule. **Five prompts FIRED and all five were read**: [E4-29] - EBITDA absent from the 10-K and **eight
  times in the furnished Q2 2026 release**, adjusted EBITDA margin **27.8% against a 14.4% GAAP pre-tax margin**, with TWO reconciliations including operating
  cash to adjusted EBITDA (the CGNX ruling found exactly where to look, and the practice runs back through the FY2024 release); [E4-22]'s third flag with
  [E5-30]'s ratchet - quarterly full-year revenue and free-cash-flow guidance, and the trail read from the filings rather than summarised: FY2025 guidance
  (*"at least 5 percent"*, *"about $13.5 billion"*) **BEATEN on both legs** (6.1%, $14,734M), FY2026 reaffirmed in April and **CUT on 2026-07-22** from
  *"more than 5 percent"* to *"four-to-five percent"*; [E2-49] metric-switching - the PSU relative-ROIC modifier that *"was 0"* replaced for 2025 grants by a
  relative-TSR modifier in a year of about 40% TSR, with the leverage range widened from 0-150% to **0-200%** and the maximum from 170% to 220% of target,
  mitigated by being announced in advance with a reason; **[E4-27]** (checked against the ledger, because earlier briefs in this queue cited [E4-52] for this)
  - PSUs vest on revenue 40%, **non-GAAP operating EPS** 30% and **IBM's own free cash flow** 30%, the last being the definition that turns $13,193M of filed
  operating cash into $14,734M, mitigated by IBM's own share-count adjustment to the EPS metric, which removes the game [E2-01] warns about; [E2-30](2) -
  buybacks suspended at the Red Hat close *"in order to reduce this debt"*, debt duly cut to $51,703M by 2021-12-31 and then **back to $62.0bn**, $22.3bn spent
  on acquisitions, and **$0 of open-market repurchase in FY2020-FY2025** after $125bn in FY2007-FY2019. Prompts that did NOT fire, each tested rather than
  assumed: **pension expected return 5.50% against a 5.34% long bond - sixteen basis points, the most conservative of the three calibrated in this project
  (HON 200bp, KMB 76bp)**, and non-operating retirement cost was -$65M, so earnings are not pension-flattered at all; footnotes unusually legible (every
  bridge item quantified, the FCF definition reconciled on the same page, the Financing segment given its own balance sheet); [E2-52] refused - the $6,255M
  dividend is covered 2.1x by filed operating cash and net share cash went OUT; [E4-30] both tells refuted - reported growth is not smooth ($1,639M to
  $10,593M of net income, FY2022's collapse being the disclosed $5.9bn NON-CASH pension settlement on transferring ~$16bn of Qualified PPP obligations to
  Prudential and MetLife) and cash tax / pre-tax income is noisy not falling (18.0%, 29.7%, 18.9%) with the low years' cause disclosed as tax-audit
  settlements; [E3-53]/[E5-33] PASS - *"workforce rebalancing charges"* recur every year ($435M, $692M, $653M) and IBM includes them in its OWN adjusted
  measure. **The candour artifact is one of the better ones in this queue**: the 8-K of **2026-07-14**, eight days before results, carried *"Arvind Krishna's
  Letter to IBM Investors"* pre-announcing the miss - *"These conditions require our teams to execute perfectly, and this quarter we faltered... These are not
  excuses, but they are realities"* - which is [E2-72] authorship and [E2-57] answered in the right direction. **[E4-52] recorded as a converging system of
  PROMOTIONAL incentives, not an integrity finding**, because the two tests that would turn narrative into misstatement both come back clean. One live
  **capital-allocation flag**, two-sided and stated with [E4-13]'s humility clause: [E2-51]'s turned-back-on-repurchases charge against the fact that on this
  run's own arithmetic the stock is NOT at a material discount, so declining to buy it obeys [E5-08] rather than defying it - the surviving charge is that
  $22.3bn was spent on acquisitions instead, at a disclosed price of $1.81 per $1. [E3-54] retention is uninformative and said to be (about $1.2bn retained
  against $30,259M of dividends over five years). [E5-45] noted: **the corpus names IBM itself in the ABCs sentence**, and on this evidence the ABCs are not
  the present condition; carried to Q6. **Q4 IN, RECORDED NOT GOVERNING. THE KYNDRYL PERIMETER IS THE WORK**: the revenue line WAS recast to continuing
  operations for FY2019 onward, and **the CASH-FLOW statement was NOT** - the FY2021 annual report says the statement *"include[s] the cash flows of
  discontinued operations"* and footnotes **one aggregate figure per year ($1.6bn, $4.4bn, $4.5bn for 2021, 2020, 2019)** with no Kyndryl cash-flow statement,
  so the CNR rule's *"nothing is estimated; the pro forma is addition"* condition fails and **FY2019-FY2021 are REFUSED, not adjusted**. Clean perimeter
  **FY2022-FY2025 plus the TTM**, and the five-year default [E2-42] is short by one year with the quoted reason. **THE FINANCING ARM IS SEPARATED THE GM/F/TM/HMC
  WAY, and IBM files the separation itself**: Financing segment debt **$15,093M** *"primarily comprised of intercompany loans"* at a disclosed **9.0 to 1**
  against $15,052M of external receivables (78% investment-grade, 0.9% reserved), non-Financing debt **$46,167M**, and the MD&A's own *"Less: change in
  Financing receivables"* line. **IBM's published free cash flow ADDS BACK the loan-book build**, taking $13,193M of filed operating cash to $16,393M and
  printing **$14,734M of "free cash flow" - larger than the audited line it reconciles to**. That is NOT the [E4-41] flag (the reconciliation is on the same
  page and *"Change in total debt 2.9"* sits two lines below it), but DELL's counter-precedent decides the direction, so both are carried as a Ford-style
  ladder: **A = consolidated OCF as filed (conservative), B = IBM's own industrial line (generous)**, and a look-through construction is explicitly NOT
  attempted with the reason stated, so no reader adds the $521M of segment profit twice. **(c) DECOMPOSED, and the raw D&A end REFUSED with the size of the
  refusal given**: not the capital-intensive class (capex 1.6% of revenue), so [E3-44]'s default is available in direction, but **$900M of operating-lease ROU
  amortisation is excluded because the rent is already inside operating cash (the CRM precedent) and $2,166M of acquired-intangible amortisation is excluded
  because $8,316M a year of R&D above the line already renews the technology (HON/UNH/EFX)**; (c) judged at **$1,600M-$2,000M** as a disclosed guess [E2-23],
  against a raw filed D&A of $5,021M that would print a **2.99% yield** and is $3.1bn a year too conservative for two named reasons. Not the CVX inversion.
  **SBC RESOLVES** (undimensioned annual USD every year FY2007-25, so the BE zero-substitution defect cannot arise) **and is COMPLETE** (the BA defect searched
  for: one stock line in the statement, no 401(k)-in-treasury-shares line, and a disclosed $30M difference to the segment figure in the acquisition-charge
  direction); [E3-70]'s grant value is not obtainable undimensioned and, at 13.0% of operating cash, is recorded as a limit with the charge named as the floor.
  **BAND across every window, both (c) ends and both constructions: $9,486M to $12,234M**, 29.0% of the low end - **NOT too wide, because it straddles
  nothing**, and the width comes from the finance book ($3.2bn in FY2025, $1.2bn the other way in FY2023) rather than from a $338M capex band. [E4-41]
  normalisation DOWN for luck names **FY2025 as a mainframe cycle PEAK** against Q2 2026's -42%, plus $200M of currency and the tax-audit settlements; judged
  centre **$10.5bn**. **GOOD, not great [E4-20, E4-43]** - excellent returns on the capital in place ($5,899M of net plant) and far less on the added capital
  ($1.81 per $1); emphatically not gruesome. [E5-11]: **(1) YES** (industrial cash $11.1bn to $16.4bn in four years; **$20,372M of deferred income read as
  [E3-52] float and the exact INVERSE of shape #4**), **(2) NO** ($8.2bn of liquidity at 2026-06-30, **down $6.3bn in six months** on Confluent, against
  $62.0bn of debt, and [E5-39] refuses to count the $10bn of undrawn facilities amended out to 2029/2031), **(3) MOSTLY YES** scored from the filed
  Contractual Obligations table - $11,995M of 2026 contractual claims plus the $6,255M dividend and $1,617M of (c) = **$19,867M against $21.4bn, a ratio of
  0.93**, with a well-spread ladder ($437M rest-of-2026, $6,713M 2027, $6,001M 2028, $5,583M 2029, $4,448M 2030, $39,894M thereafter). **[E2-54] coverage 5.7x
  on interest paid and 4.9x on interest paid AND accrued**, the strict construction; covenants certified *"well within the required levels"*, no ratings
  trigger. **THE PENSION, stated because the brief required it: net underfunded $2,283M and FALLING $374M**; qualified plans in SURPLUS (US Personal Pension
  Plan *"137 percent funded"*, worldwide qualified *"116 percent funded"*, a $7,544M prepaid pension asset), the $9,828M underfunded liability mostly
  non-qualified US promises ($3,472M against $5M of assets) and non-US plans; and *"In 2026, we are not legally required to make any contributions to the U.S.
  defined benefit pension plans"*, with mandated non-US funding of *"approximately $0.8 billion in the next five years"*. **The pension is not the claim.**
  **Shape #10 THE CAMOUFLAGE**, with a proposed **feature** offered to the operator and changing no register: **the company sells the service that erodes its
  own franchise**. Quantified without modelling, because Q2 2026 already is the quantification (IBM Z -42%, Transaction Processing -8%, Infrastructure -7%,
  GAAP pre-tax income -5%, guidance cut, and three new programmes announced in the same six weeks); on the slow version, a 5%-a-year decline in the $13,703M
  of disclosed franchise revenue at a 70% incremental margin is **-$2.2bn of segment profit, 13% of the $16,364M total**, costing about **$5.6bn of
  acquisition cash to replace** at the revealed $1.81 per $1. Likelihood **a real possibility** (not *likely*: z17 is at *"nearly 130 percent
  program-to-program"* with *"85% of installed MIPs maintaining or growing capacity"*, and IBM's own reading is deferral, not substitution). **Shapes refused
  with arithmetic: #1** (purchase obligations **$4,817M total, $1,958M in 2026**, against ORCL's $260bn of leases not yet commenced - IBM *could* stop),
  **#2** (SBC 13.0% of operating cash), **#5**, **#4** (inverted), **#6** (a feature of the Financing segment only), **#3** (only just, and said so). **Q5 DID
  NOT OPEN.** Price headed **COMPUTATION - NOT A CLEARANCE** under operator rule 3: yield **4.39%-5.66%** against the sovereign, **-0.95 to +0.32 points**, the
  **~10% floor [E4-28] missed by 4.3-5.6 points at EVERY end of the band, in every window, on both (c) ends and both constructions**, so **no ranking position
  is assigned**; growth required in perpetuity merely to REACH the floor **4.34%-5.61%** against a 4.12% five-year revenue CAGR; value **roughly $110 to $160
  a share** against a price of $229.55, which is above the whole range and above even the $209 bond-parity figure that no buying standard endorses. **Bar 2
  (screamer), outcome three. WINDAGE ZERO, with the proof**: at the completely un-normalised top of the band the yield is 5.66% and the floor is still missed
  by 4.34 points. **The strongest single fact against the file, stated as well as its holders would state it [E4-51]: IBM's owner earnings have grown FASTER
  than the floor requires** - 9.13% a year at construction A's capex end and 16.38% at B's, FY2022 to FY2025, industrial cash up 48%, against a required
  5.14% - and the four answers are given without assertion: the file closed at Q2 and no growth rate reopens a Q2; **FY2022 is a trough and measured from
  FY2023 construction A is DOWN, $11,309M to $9,861M**, which is exactly [E4-38]'s selected-base-year warning, so every window is published; the growth is
  margin recovery plus a cycle peak plus bought revenue and none of the three is a perpetuity; and part of B's 16.38% is the finance book GROWING, which is
  lending, not earning. **Q6 arms NOTHING** - the QLYS ruling of 2026-09-07: a Q2 failure is a failure on the BUSINESS and a price alert would be a category
  error, so **no `tools/alerts.json` band and no `PORTFOLIO.md` row**. Reopening conditions recorded in words: a structural separation putting the mainframe
  complex on its own books (**a new name to run under v4, not a reversal of this one**), a sustained stop to the acquisition programme with repurchase below a
  conservatively calculated value ([E2-48]'s superstar tell), or filed [E2-44] pricing-power evidence outside the mainframe; thesis-breaking metric and
  threshold pre-committed [E1-02]. **WAVE 6, the third of the eleven and the third of the five ordinary businesses.** **Register entry 118**, counted from this
  file's heading line to `## THE WRITE-EARLY PROTOCOL` (117 line-start entries before it, no duplicate ticker, IBM not previously entered).
  `Test Runs/2026-09-19 Run - IBM International Business Machines.md` (template `cbad2c4`, Step 0 `19b4523`, Q1 `d2c4233`, Q2 `917cf00`, Q3 `43cfd89`, Q4
  `35c6371`, computation/Q6/audit/register `4379b00`, fold in the fold commit), `check_framework.py` **PASS**. **THE PAIR.** Price **US$229.55** (2026-09-18
  regular-session close, Yahoo Finance chart `regularMarketPrice` with `regularMarketTime` 16:00:03 America/New_York, **aggregator flagged**; the four prior
  sessions were 249.09, 248.37, 237.49 and 237.75, so the quote fell 7.8% in four sessions and a one-day close is a one-day fact) x **942,134,390** x 1.0 =
  cap **US$216,267M**. **Count:** the Q2 2026 Form 10-Q cover, accession **`0000051143-26-000078`** (filed 2026-07-23), *"The registrant had 942,134,390
  shares of common stock outstanding at June 30, 2026"* - one class of capital stock, par $0.20, so no A/B artifact is possible; the FY2025 10-K cover said
  938,034,404 at 2026-02-10, i.e. **the count is RISING**, on employee-plan issuance of roughly 11M shares a year since buybacks stopped. **Sovereign USD
  5.34%** (2026-09-18, US Treasury daily par yield curve, struck fresh this run by `python tools/sources.py`, not inherited from the brief). **Filing:** FY2025
  Form 10-K **`0000051143-26-000010`** (filed 2026-02-24), whose statements and MD&A live in the incorporated Annual Report exhibit `ibm-20251231_d2.htm`
  inside the same accession - *"Portions of IBM's Annual Report to Stockholders ... are incorporated by reference into Parts I, II and IV"* - plus 10-Q
  `0000051143-26-000078`, the furnished Q2 2026 release `0000051143-26-000077` EX-99.1, the CEO's pre-announcement `0000051143-26-000070` EX-99.1, the
  FY2024/FY2025 releases `0000051143-25-000005` and `0000051143-26-000004`, the 2026 proxy `0000051143-26-000025`, and the FY2022 and FY2021 Annual Report
  exhibits `0001558370-23-002376` and `0001558370-22-001584` for the Kyndryl perimeter. Two figures cross-checked to the dollar against the filed statements:
  total revenue $67,535M and operating cash flow $13,193M. **PASS/FAIL: FAIL - closed at Q2, OUT on the business.**"""

lines.insert(h + 1, ENTRY)
q2 = '\n'.join(lines)

# step 2 - strike IBM in the WAVE 6 table
old_row = '| IBM | International Business Machines | ordinary | **RUN** |'
new_row = '| ~~IBM~~ | International Business Machines | ordinary | **RUN 2026-09-19 - struck. FAIL at Q2, OUT on the business: a real mainframe franchise over ~28-33% of revenue and bought growth over the rest. Price US$229.55, cap US$216,267M. See COMPLETED.** |'
assert old_row in q2, 'WAVE 6 IBM row not found in the expected form'
q2 = q2.replace(old_row, new_row, 1)

h2, w2, lines2 = register_slice(q2)
after = count_entries(lines2, h2, w2)
print('register entries AFTER:', after)
assert after == before + 1, 'register count moved by %d, not 1' % (after - before)
io.open(QUEUE, 'w', encoding='utf-8').write(q2)
print('queue written; IBM struck in WAVE 6')
