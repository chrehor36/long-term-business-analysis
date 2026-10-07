import io
p = 'Test Runs/2026-09-19 Run - IBM International Business Machines.md'
s = io.open(p, encoding='utf-8').read()
start = "## Q4 — WILL IT SURVIVE?"
end = "---\n⛔ **Q5 does not open unless Q1-Q4 each show IN.**"
i, j = s.index(start), s.index(end)
new = """## Q4 — WILL IT SURVIVE? — **RECORDED, NOT GOVERNING**

### THE PERIMETER, FIRST — and the Kyndryl spin is the whole reason this section is short

**The CNR rule: no mean crosses the spin unless it is rebuilt on one perimeter.** For IBM the spin
cuts the cash-flow statement in a way the income statement does not, and the filing says so in
words:

> *"Our cash flows from operating, investing and financing activities, as reflected in the
> Consolidated Statement of Cash Flows … **include the cash flows of discontinued
> operations.**"* — FY2021 Annual Report, `0001558370-22-001584` / `ibm-20211231xex13.htm`,
> with the footnote *"**Includes cash flows of discontinued operations of $1.6 billion, $4.4
> billion and $4.5 billion in 2021, 2020 and 2019, respectively.**"*

So:
- **The REVENUE line was recast** to continuing operations for FY2019 onward (*"the historical
  results of Kyndryl are presented as discontinued operations and, as such, have been excluded
  from continuing operations and segment results for all periods presented"*). That is why Q2's
  five-year revenue CAGR from FY2020's $55,179M is legitimate — it is a continuing-operations
  figure throughout.
- **The CASH-FLOW statement was NOT recast.** FY2019, FY2020 and FY2021 operating cash each
  contain Kyndryl, and IBM published **one aggregate discontinued-cash number per year, not a
  Kyndryl cash-flow statement.** The CNR rule's first condition — *"both predecessors filed
  complete audited cash-flow statements for every year used … Nothing is estimated; the pro
  forma is addition"* — **is not met**, because subtracting $4.5bn from an operating-cash total
  when the disclosure does not say how much of it was operating would be my estimate, not IBM's
  addition.
- **Therefore: FY2019, FY2020 and FY2021 are REFUSED, not adjusted. The clean perimeter is
  FY2022-FY2025 plus the trailing twelve months, and the five-year default window [E2-42] is
  short by one year and says so.** Kyndryl Holdings files its own 10-K and I could in principle
  build the subtraction from it; I have not, because the residual would still be my arithmetic
  rather than IBM's filed statement, and the four clean years plus the TTM already produce a band
  narrow enough to conclude.
- **A second perimeter event sits inside the TTM and is named: Confluent, closed 2026-03-17 for
  $11,268M of cash plus $269M for equity awards** (10-Q `0000051143-26-000078`, note 5, with
  $3,834M of acquired intangibles added in Q1 2026). H1 2026 operating cash therefore includes
  about a quarter and a half of Confluent, bought for 5.3% of the market capitalisation. The TTM
  row carries it and is flagged.

### THE FINANCING ARM — separated the way GM, F, TM and HMC did it, and IBM files the separation

The lineage rule from those runs is *"both belong to the finance company or neither does, and
taking one without the other is the error."* IBM is easier than GM and harder than Dell, for one
reason: **the separation is published by IBM itself**, in the Management Discussion, as a named
line item.

| what is separated | figure, FY2025 | where it is filed |
|---|---|---|
| Financing segment revenue | $737M | segment table |
| Financing segment profit | $521M *(includes intercompany activity eliminated in consolidation)* | segment table, note (1) |
| External net financing receivables | **$15,052M** ($13,192M client + $2,992M commercial, less $141M allowance) | Financing segment tables, page 38 |
| **Financing segment debt** | **$15,093M**, *"primarily comprised of intercompany loans"*, **debt-to-equity 9.0 to 1** on $1,678M of equity | Debt table, page 25-26 |
| **Non-Financing debt** | **$46,167M** | Debt table, page 25 |
| Financing external interest income / matched interest expense | $705M / $365M | segment note, *Other Reportable Segment Items* |
| **The cash-flow effect — IBM's own line** | *"Less: change in Financing receivables"* **$(3.2)bn in 2025**, $(0.4)bn 2024, **+$1.2bn 2023**, $(0.7)bn 2022 | free-cash-flow table, page 32 |

**What IBM's own free-cash-flow definition does, in plain words, and it is disclosed:** *"We
define free cash flow as net cash from operating activities **less the change in Financing
receivables** and net capital expenditures … management considers Financing receivables as a
profit-generating investment, not as working capital that should be minimized."* So IBM **adds
back** the cash consumed by growing its loan book, taking $13,193M of filed operating cash to
**$16,393M** of *"net cash from operating activities, excluding Financing receivables"*, then
deducts $1.6bn of net capital expenditure to publish **$14,734M of free cash flow — a figure
LARGER than the audited operating-cash line it is reconciled to.**

**[E4-41]'s test is whether a pro-forma discloses earnings too high, and this one is the mirror
image of Berkshire's: it discloses cash too high, and it discloses exactly how.** The
reconciliation is printed on the same page, the offsetting debt appears two lines below it as
*"Change in total debt 2.9"*, and the Financing segment's 9.0:1 leverage is published separately.
**So this is not the [E4-41] flag; it is a disclosed definition whose direction I have to correct
for myself.** And DELL's counter-precedent says which way: the receivable build is an **operating**
outflow while the debt that funds it is a **financing** inflow, so consolidated operating cash is
**understated** by the growth of the finance book — and IBM's own adjustment is legitimate in
substance but incomplete, because it credits the asset build back without charging the $2,977M of
extra Financing segment debt that paid for it.

**The answer is Ford's answer: a ladder of named constructions, not one number.**

- **Construction A — CONSOLIDATED operating cash exactly as filed, less SBC, less (c).** This
  charges the whole growth of the finance book against the owner. It is the **conservative** end
  and it is the DELL reading.
- **Construction B — INDUSTRIAL operating cash (IBM's own filed ex-Financing-receivables line),
  less SBC, less (c).** This is the Ford "filed sector column" reading, and it is the
  **generous** end. It is legitimate only if the reader also holds in view that the finance book
  is funded by $15,093M of matched debt at 9.0:1 — which is scored separately below, never netted
  against the receivables.
- **Not attempted: a look-through construction.** Ford's (C) and (D) add the finance sub's
  distributions or its net income. **For IBM neither is available and neither is needed**: IBM
  Financing is not a separate SEC registrant, its debt is intercompany, and its segment profit is
  stated *including* intercompany activity that is *"eliminated in IBM's consolidated financial
  results"* — so adding $521M on top of consolidated operating cash would double-count. The
  external economics of the arm are already inside constructions A and B through $705M of interest
  income. **Stated so no reader adds it twice.**

### (c) — a DISCLOSED JUDGMENT with the corpus default decomposed **[E2-23, E3-44, E2-41, E5-20]**

**Which case is IBM?** **Not the capital-intensive exception class.** Capex is **1.6% of revenue**
($1,091M of plant + $647M of software on $67,535M) and the filing describes no renewal programme
that depreciation understates. **[E5-20]**'s railroad/airline carve-out does not apply, so
**[E3-44]**'s D&A default is available in direction. But the D&A **line** cannot be used as filed,
for two reasons that must be taken out one at a time:

| component of filed D&A, FY2025 | amount | treatment | reason |
|---|---|---|---|
| Depreciation, total | $2,284M | | |
| — of which operating-lease ROU amortisation | **$(900)M** | **EXCLUDED** | the rent is **already inside operating cash flow**; including it charges the same rent twice (the CRM precedent) |
| — fixed-asset depreciation | $1,384M | **INCLUDED** | real plant renewal |
| Amortisation of capitalised software and acquired intangibles | $2,737M | | |
| — of which **acquired**-intangible amortisation | **$(2,166)M** | **EXCLUDED** | it renews nothing. **$8,316M a year of R&D — 12.3% of revenue — is charged above the operating-cash line and already pays for the technology.** (The HON/UNH/EFX precedent; EFX's words: *"Purchased-intangible amortization is an acquisition artifact, not renewal spend"*) |
| — capitalised-software amortisation | ~$571M | **INCLUDED** | *"a data company's capitalized software development IS its product renewal"* — and IBM's cash software investment of $647M sits within $80M of it, which is the cross-check |

**The three (c) constructions, $M, all filed-sourced:**

| year | (c) capex end | (c) renewal-D&A end | (c) RAW filed D&A |
|---|---|---|---|
| FY2022 | 1,861 | 2,155 | 4,802 |
| FY2023 | 1,489 | 1,869 | 4,396 |
| FY2024 | 1,128 | 1,937 | 4,667 |
| FY2025 | **1,617** | **1,955** | **5,021** |
| TTM 2026H1 | 1,703 | 1,972 | 5,202 |

**The raw filed D&A end is REFUSED, with the reason and the size of the refusal stated.** At
$5,021M it would put FY2025 owner earnings at $13,193 − $1,715 − $5,021 = **$6,457M, a 2.99%
yield** — and it is wrong twice over: it charges $900M of rent that operating cash already paid,
and it charges $2,166M of acquisition artifact as though R&D were not already charged. **That is
the number a mechanical screen would print, and it is $3.1bn a year too conservative for a stated
reason, not for a preference.** *(Direction note: at IBM the raw D&A end is the LOW end, so this is
**not** the CVX inversion the AVGO run named; it is the ordinary direction with an invalid
magnitude.)*

**(c) is judged at ~$1,600M-$2,000M, and I disclose it as a guess [E2-23]: "(c) must be a
guess."** The band is narrow — $338M wide in FY2025, 0.5% of revenue — because IBM's physical
renewal genuinely is small. **The real width in this file is not the capex band at all; it is the
construction (the finance book) and the window.** Saying so is the point of carrying both
**[E4-25]**.

**The working-capital increment [E2-23] constraint 3 is inside both constructions**, because
operating cash flow nets the working-capital change from one audited line — and for IBM that line
matters enormously: *"Receivables (including financing receivables) (4,278)"* in FY2025 is the
single largest reconciling item in the statement, which is exactly why the two constructions exist.

**SBC RESOLVES and is COMPLETE, checked deliberately against the two defects this queue has
found.** (1) *RESOLVES:* `ShareBasedCompensation` carries an undimensioned annual USD value for
every year FY2007-FY2025 — the BE defect (SBC tagged only by expense line, so `sbc.get(e, 0.0)`
silently substitutes zero) **does not arise**. (2) *COMPLETE:* the BA defect — SBC that resolves
but is incomplete because a second form of stock pay sits on another cash-flow line — was searched
for. IBM's cash-flow statement carries **one** stock line, *"Stock-based compensation"*
($1,715M FY2025, $1,004M H1 2026), and the segment reconciliation carries $1,685M *"Stock-based
compensation … Excludes certain acquisition-related charges"* — a $30M difference, disclosed, in
the acquisition-charge direction. **No 401(k)-in-treasury-shares line and no separate equity
contribution exists in IBM's statement.** SBC is subtracted **in full [E5-06]**.
**[E3-70]'s grant-value measure is the one thing I could not do and I say so:** the corpus asks
for *"what the company could have realized by publicly selling options of like quantity and
structure"*, and no undimensioned grant-date total resolves for IBM. At **13.0% of operating cash
flow** SBC is well under the 50% threshold this project set for reading the grant table by hand
(second-lowest in the eleven-name row), so the charge is used as the measure and the floor is
noted. **This is a recorded limit, not a gap in diligence.**

### OWNER EARNINGS — every valid window, both (c) ends, both constructions

*All figures $M. Arithmetic: `Test Runs/_research 2026-09-19 IBM/oe.py`.*

**By year:**

| year | filed OCF | industrial OCF (ex-Financing receivables) | SBC | A: capex end | A: renewal-D&A end | B: capex end | B: renewal-D&A end |
|---|---|---|---|---|---|---|---|
| FY2022 | 10,435 | 11,135 | 987 | 7,587 | 7,293 | 8,287 | 7,993 |
| FY2023 | 13,931 | 12,731 | 1,133 | 11,309 | 10,929 | 10,109 | 9,729 |
| FY2024 | 13,445 | 13,845 | 1,311 | 11,006 | 10,197 | 11,406 | 10,597 |
| FY2025 | 13,193 | 16,393 | 1,715 | 9,861 | 9,523 | **13,061** | **12,723** |
| TTM 2026H1 | 14,888 | *not available* | 1,877 | 11,308 | 11,039 | — | — |

*The TTM industrial row is blank because **IBM publishes the change in Financing receivables
annually, not quarterly** — the 10-Q gives no such line. Recorded as a source limit, not
estimated.*

**By window:**

| construction | window | capex end | renewal-D&A end |
|---|---|---|---|
| A consolidated | 2-yr FY2024-25 | 10,434 | 9,860 |
| A consolidated | 3-yr FY2023-25 | 10,725 | 10,216 |
| A consolidated | **4-yr FY2022-25** | **9,941** | **9,486** |
| A consolidated | TTM | 11,308 | 11,039 |
| B industrial | 2-yr FY2024-25 | 12,234 | 11,660 |
| B industrial | 3-yr FY2023-25 | 11,525 | 11,016 |
| B industrial | **4-yr FY2022-25** | **10,716** | **10,260** |

**COMBINED RANGE across every window, both (c) ends and both constructions: $9,486M to
$12,234M** — a width of $2,748M, **29.0% of the low end.**

- **Is that range too wide to reach a conclusion [E4-25]? NO — and the reason is that the whole
  range sits on one side of the decision.** At the 2026-09-18 cap of $216,267M the range is
  **4.39% to 5.66%**. The ~10% floor **[E4-28]** is not reached at either end, not in any window,
  not on either (c) end, not on either construction. The ORCL run's formulation applies exactly:
  *"width closes a file only when it straddles the decision, and this one straddles nothing."*
- **The wide spread is also a Q4 finding [E5-11], and the distorted years are named:**
  **FY2022** is the low year in every construction, and its cause is disclosed and non-cash — the
  **$5.9bn pre-tax pension settlement charge** on transferring about $16bn of Qualified Personal
  Pension Plan obligations to Prudential and MetLife in September 2022 depressed earnings, not
  cash; the cash weakness was the post-separation year itself. **FY2025** is the high year in
  construction B and the low year in construction A, entirely because of one line: the finance
  book grew $3.2bn. **The two constructions disagree by $3.2bn in FY2025 and by $1.2bn in the
  opposite direction in FY2023** — that is the single largest source of width in this file, and it
  is a financing question, not a capex question.
- **[E3-55]'s scope test applied:** is the spread noise around a certain mechanism, or uncertainty
  about the level? **Mostly the level.** Industrial operating cash rose $11.1bn → $12.7bn →
  $13.8bn → $16.4bn across the four clean years, which is a trend, not a bounce — so the
  conservative end is a stale reading of a business whose cash generation genuinely improved, and
  I say so against my own interest.
- **[E4-41] — normalise the mean DOWN for luck, and the items are named and quantified:**
  1. **FY2025 is a mainframe cycle PEAK.** z17 launched June 2025, IBM Z revenue +51.7%,
     Infrastructure segment profit +41.2%. **Q2 2026 shows the other side: IBM Z −42%,
     Transaction Processing −8%, Infrastructure −7%.** A mean whose latest and largest year is a
     product-cycle peak is a favourable break, and the corpus says to remove it before trusting
     the mean.
  2. **Currency:** *"Currency translation and hedging contributed approximately $200M in
     year-to-year pre-tax income growth"* in FY2025.
  3. **Tax-audit settlements** in 2024 and 2025 reduced cash tax — cash tax was 18.9% of pre-tax
     income in FY2025 against a 29.0% FY2019 reading.
  **Taken together I judge the honest, cycle-normalised centre of owner earnings at roughly
  $10bn-$11bn, nearer the four-year means than the TTM**, and I am choosing the lower half of my
  own range on purpose.
- **[E3-04] look-through:** searched. IBM has no material equity-method or unconsolidated
  minority stakes disclosed; *"expense resulting from basis differences on equity method
  investments"* appears in the non-GAAP definition but no material investee earnings exist to add.
  **Nothing to add; recorded so the omission is not read as an oversight.**
- **For comparison only, IBM's own free cash flow**, which is **not** owner earnings because no
  SBC is subtracted: $9.3bn (FY2022), $11.2bn (FY2023), $12.7bn (FY2024), **$14,734M (FY2025) =
  6.81% of the cap.** The gap between IBM's 6.81% and my 4.39%-5.66% is, almost exactly, **stock
  pay plus the finance-book adjustment** — which is the whole of what this framework adds to the
  company's own headline number.

### Great, good, or gruesome? **[E4-20]**

- [ ] great — [x] **GOOD** — [ ] gruesome

**Why GOOD and not great.** On the capital in place the returns are excellent: about $10bn-$11bn
of normalised owner earnings against **$5,899M of net plant** and total tangible assets of
$72,772M, in a business whose maintenance capex is 1.6% of revenue. That is the great class's
*shape*. **It is not the great class, because the added capital earns much less than the capital in
place**, and the filings price it: **$22,306M of acquisition cash FY2021-FY2025 for $12,356M of
additional annual revenue — $1.81 per $1** — at consolidated margins well under 100%, so the
incremental return on the money actually deployed for growth is a fraction of the return on the
installed base. **[E4-43]** is explicit that the good class **passes**: *"nothing shabby about
earning $82 million pre-tax on $400 million of net tangible assets"*, and the good class *"may
well prove to be a satisfactory investment."* **[E5-40]**'s ~12%-on-retained-capital benchmark is
the right comparator and IBM's retained capital is near zero, because essentially all of earnings
goes out as dividends and the acquisitions are debt-funded. **GOOD ranks below great at Q5 and
that is all it does [E4-43].**

**It is emphatically not gruesome.** Gruesome is *"grows rapidly, requires significant capital to
engender the growth, and then earns little or no money."* IBM grows at 4%, requires little
physical capital, and earns $10bn+. The cash-consuming test has nothing to bite on.

### Staying power — score all three **[E5-11]**

**(1) A large and reliable stream of earnings — YES, and it is the strongest of the three.**
Industrial operating cash $11.1bn → $16.4bn over four years, every year positive, never below
$10.4bn even in the post-spin year. Revenue is 79% recurring inside Software (ARR $23.6bn),
Infrastructure Support is a maintenance annuity, Consulting carries a $31.9bn backlog, and
**deferred income is $20,372M** ($16,101M current + $4,271M noncurrent) — customers' money held in
advance. **[E3-52]** is the right reading of that $20.4bn: liabilities *"without covenants or due
dates attached to them"*, discharged by delivering software and support at high margin. **This is
the inverse of shape #4** (BA's customer advances discharged at a negative margin) and it is worth
saying explicitly, because the same balance-sheet line kills one company and funds another.

**(2) Massive liquid assets — NO. This is the weak leg and the corpus's standard is strict.**
$14.5bn of cash, restricted cash and short-term marketable securities at 2025-12-31, and **$8.2bn
at 2026-06-30 — down $6.3bn in six months**, because $10,480M went out for Confluent, against
**$62.0bn of total debt.** IBM has $10bn of committed revolving facilities, amended 2026-06-22 out
to 2029 and 2031, **undrawn** — and **[E5-39]** refuses to count them: *"We will never be
dependent on the kindness of strangers … cash is a lot like oxygen."* **Scored on the corpus's
standard, IBM fails strength (2), and it fails it by choice**, having spent the liquidity on an
acquisition.

**(3) No significant near-term cash requirements — MOSTLY YES, and this is the leg that usually
kills, so it is scored from the filed table rather than asserted.** The FY2025 Contractual
Obligations table, payments due in **2026**:

| claim | 2026 |
|---|---|
| Long-term debt obligations | $6,146M |
| Interest on long-term debt | $2,078M |
| Finance lease obligations | $279M |
| Operating lease obligations | $935M |
| **Purchase obligations** | **$1,958M** |
| Minimum mandated defined-benefit pension funding | **$50M** |
| Excess Savings Plan | $238M |
| Long-term termination benefits | $311M |
| **contractual subtotal** | **$11,995M** |
| dividend (not contractual, but it has been paid every quarter since 1916) | $6,255M |
| (c) | $1,617M |
| **total twelve-month claim** | **$19,867M** |

Against **$13,193M of filed operating cash plus $8.2bn of liquidity = $21.4bn: a ratio of 0.93.**
Tight in the arithmetic and comfortable in reality, because $6,146M of it is refinancing at A-/A3
and $6,255M of it is discretionary. The **maturity ladder is well spread** — $437M for the rest of
2026, $6,713M (2027), $6,001M (2028), $5,583M (2029), $4,448M (2030), $39,894M thereafter — with
no wall.

**THE PENSION, stated as the brief required.** **Net underfunded position $2,283M at 2025-12-31**,
*down* $374M year on year on higher discount rates. Decomposed: total **overfunded** plans have
$35,383M of assets against $27,839M of obligations, a **$7,544M prepaid pension asset** on the
balance sheet; total **underfunded** plans have $9,437M of assets against $19,264M of obligations,
**$9,828M** recognised as a liability — of which $3,472M is US plans (almost entirely
**non-qualified**, with $5M of assets, i.e. an unfunded promise, not a funding shortfall) and
$6,356M non-US. **The qualified plans are in surplus: *"our qualified defined benefit pension
plans were well funded"*, the U.S. Personal Pension Plan *"was 137 percent funded"*, and worldwide
qualified plans *"116 percent funded at December 31, 2025."*** **The cash demand is
de-minimis and it is disclosed: *"In 2026, we are not legally required to make any contributions
to the U.S. defined benefit pension plans"***, mandated non-US contributions of *"approximately
$0.8 billion in the next five years"* and *"approximately $0.1 billion"* in 2026; all
retirement-related contributions about $1.4bn in 2026 against $13bn+ of operating cash. **The
pension is not a claim on this business** — the same finding the CNR run reached about a different
company (*"the pension is not the claim"*). And the risk-reduction programme is on the record: the
2022 transfer of ~$16bn of obligations to Prudential and MetLife and the 2024 transfer behind the
$3.1bn settlement charge have both **shrunk** the exposure.

**LEVERAGE, named and quantified — there is no ratio ceiling in this framework and the corpus
supplies none [E4-16, E3-29, E1-18].**
- Total debt **$61,260M** (2025-12-31) and **$62.0bn** (2026-06-30).
- **Financing segment debt $15,093M / $13.0bn**, matched to $15,052M of external financing
  receivables at 9.0:1, and *"the terms of the intercompany loans are set by the company to
  substantially match the term, currency and interest rate variability underlying the financing
  receivable."* **Matched-book debt against receivables 78% investment-grade** (up 4 points),
  0.9% reserved.
- **Non-Financing debt $46,167M / about $49bn** — the industrial obligation, against $8.2bn of
  liquidity and $10bn-plus of annual industrial operating cash.
- **[E2-54]'s coverage test, run the way it is written** — all interest, payable and accrued, out
  of current cash flow **net of ample capital expenditure**: ($13,193M − $1,617M) ÷ $2,042M of
  interest paid = **5.7×**, or **4.9×** on interest paid *and accrued* (about $2,350M a year, from
  the 10-Q's *"Total interest paid and accrued"* of $1,177M for six months). **Passes, and passes
  on the strict construction.** Covenants: a consolidated net interest expense ratio *"which
  cannot be less than 2.20 to 1.0"*, secured indebtedness capped at 10% of consolidated net
  tangible assets, cross-default at $500M — **and IBM certifies compliance and says the covenants
  *"are well within the required levels."*** No ratings trigger in the debt.
- **[E3-52]'s terms test, both ways.** $20,372M of deferred income is covenant-free and
  customer-prepaid — the good kind. $46bn of non-Financing notes and debentures is the covenanted
  kind, dated, and its interest bill rose from $1,401M (FY2022) to $2,042M (FY2025) **while total
  debt rose $9.6bn**.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24]**

**Shape: #10 THE CAMOUFLAGE** (first named by SONY, 2026-09-13) — *"cash from the strong legs is
recycled into legs that must re-win a race each cycle; the company lives, the owner's return does
not."* Scored against `Screens/SURVIVAL SHAPES - index.md`, and the fit is exact, with one
refinement below.

**The mechanism, in one sentence.** The mainframe complex — about 28-33% of revenue and a
disproportionate share of the profit — is a slowly decaying annuity whose decay is accelerated by
the very migration-and-modernisation work IBM's Consulting segment sells; the cash it throws off
is spent, at **$1.81 of acquisition cash per $1 of added annual revenue**, buying competed
businesses that must re-win their markets every cycle; essentially all of reported earnings goes
out as a dividend that has been paid every quarter since 1916 and cannot be cut without a
reputational event; so the purchases are funded with debt, and **the company survives indefinitely
while the owner's return converges on the dividend yield plus whatever the bought growth is
actually worth.**

**Quantified from filed figures — and the quarter that quantifies it has already happened.** I do
not have to model the down-leg of the mainframe cycle, because **Q2 2026 is it**:
- IBM Z revenue **−42%**, Transaction Processing **−8%**, Infrastructure **−7%**, in one quarter
  (`0000051143-26-000077`).
- GAAP pre-tax income **−5%**, GAAP pre-tax margin **−0.9 points to 14.4%**, GAAP diluted EPS
  **−2%** — while *operating* (non-GAAP) pre-tax income rose 3%.
- Full-year constant-currency revenue guidance **cut** from *"more than 5 percent"* to
  *"four-to-five percent"*.
- And the response, announced in the same six weeks: **three new programmes** — Lightwell at *"a
  $5 billion commitment"*, quantum at *"more than $10 billion … over the next five years"*, and
  a *"$1 billion cash contribution by IBM"* to a quantum wafer foundry.

**Now the arithmetic of the slow version.** Transaction Processing plus Infrastructure Support are
$13,703M of *disclosed* revenue, and Software's segment margin on the Transaction Processing half
is far above the company average. Suppose that block declines **5% a year** for five years — the
rate Q2 2026 already exceeded — at a **70% incremental margin**: that is about **−$3.1bn of
revenue and −$2.2bn of segment profit, 13% of FY2025's $16,364M of total reportable segment
profit, and roughly 20% of owner earnings.** To replace $3.1bn of revenue at IBM's own revealed
price of $1.81 per $1 would cost about **$5.6bn of acquisition cash** — a little over half of one
year's owner earnings, every five years, on top of a dividend that already consumes $6.3bn and
$8.3bn a year of R&D. **The company pays for it, and the owner's yield does not rise.**

**Likelihood: [x] a real possibility.** Not *likely*, because the installed base is genuinely
durable and IBM's own evidence points to deferral rather than substitution (*"z17 remains at nearly
130 percent program-to-program"*, *"clients representing 85% of installed MIPs maintaining or
growing capacity"*). Not *a low-level possibility*, because it is already visible in one filed
quarter and the replacement price is already on the record.

**[E4-40] — model exposure, not experience, which is the failure mode this section exists to
avoid.** The exposure, independent of what has happened: **two thirds of revenue is competed for by
Microsoft, Amazon, Alphabet, Oracle, SAP, Salesforce, Broadcom, Accenture, Dell, HPE and hundreds
of others by IBM's own count**; the franchise third depends on customers choosing *not* to rewrite
applications, a decision they take one at a time and that IBM itself is paid to help them take;
and $46bn of industrial debt sits against $8.2bn of cash. A benign recent record — four years of
rising industrial cash — is *"not only useless, but actually dangerous"* as a guide to that.

**Shapes explicitly REFUSED, with the arithmetic:**
- **#1 CONTRACTED NOT TO STOP (ORCL) — REFUSED.** IBM's total **purchase obligations are $4,817M**,
  $1,958M of it in 2026, against $67.5bn of revenue. Oracle's comparable exposure was **$260bn of
  leases not yet commenced**, 8.13× its operating cash flow. IBM's quantum and Lightwell numbers
  are *announced intentions*, not signed commitments, and the contractual-obligations table proves
  it. **The distinction the ORCL run drew — *"a company that could stop and a company that has
  contracted not to"* — puts IBM firmly in the first class.**
- **#2 EARNS NOTHING AFTER PAYING ITS PEOPLE — REFUSED.** SBC is **13.0% of operating cash flow**,
  second-lowest of the eleven-name row.
- **#5 THE SELF-LIQUIDATING DISTRIBUTION — REFUSED on the arithmetic**, tested at Q3: filed
  operating cash covers the dividend **2.1×**, and the debt increase funded acquisitions, not the
  payout. **[E2-60]** does not bite.
- **#4 THE CASH IS SPENT UNDOING PAST WORK — REFUSED, and inverted.** IBM's $20,372M of deferred
  income is discharged at software and support margins, which is float, not BA's negative-margin
  advance.
- **#6 THE BORROWED BALANCE SHEET — REFUSED for the industrial business**, where $46bn of
  investment-grade term debt with no ratings trigger and a well-spread ladder is leverage, not
  dependence on rolling other people's money. It is a **feature** of the Financing segment alone,
  which is 9.0:1 against a matched, 78%-investment-grade receivable book.
- **#3 TOO LITTLE FILED HISTORY — REFUSED, but only just, and for a reason worth recording.** Four
  clean post-Kyndryl years plus a TTM is *enough* to reach a conclusion here because the range
  does not straddle the decision. It would not have been enough if the answer had been close.

**A refinement of #10 proposed, not a new shape.** SONY's camouflage has *strong legs whose cash
is recycled into legs that must re-win a race*. IBM adds a mechanism SONY did not have: **the
company sells the service that erodes its own franchise**, and books it as growth. Whether that
deserves its own number is for the operator; it is proposed as a **feature of #10**, not as shape
#22, and no register is changed by this note.

- **VERDICT: [x] IN — RECORDED, NOT GOVERNING.** The business survives: a good business
  **[E4-20, E4-43]**, coverage 4.9×-5.7× on the strict test, a de-minimis pension demand, a clean
  maturity ladder, and a rising industrial cash stream. **Strength (2) of [E5-11] fails on the
  corpus's standard and is recorded as failing.** None of this promotes the name; the file closed
  at Q2.

"""
s = s[:i] + new + s[j:]
io.open(p, 'w', encoding='utf-8').write(s)
print('q4 written')
