# Company Run — Salesforce, Inc. (CRM) — 2026-09-07
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

---
## STATUS OF THIS FILE
*Written incrementally under the write-early protocol. Sections appear as they close.*

- [x] Step 0 — the rate and the filing
- [x] The acquisition perimeter (above Q1, AVGO method)
- [x] **Q1 — IN** (narrow)
- [x] **Q2 — IN** · class NARROW · direction flat to narrowing *(+ a marked addendum completing the competitor row)*
- [x] **Q3 — IN** · no disqualifier found · live capital-allocation flag · [E4-52] convergence
- [x] **Q4 — IN** · GOOD, not great · 3 of 3 on [E5-11]
- [x] **Q5 — NOT IN** · quit on at the [E4-28] floor, not ranked
- [x] **Q6 — IN** as a pre-committed monitoring register
- [x] Self-audit
- [x] Defect register — tooling and brief
- [x] `python tools/check_framework.py` → **PASS** · 0 phantom citations across 106 ledger ids
      cited in this file, checked against all 266 ledger rows

**COMMIT PROVENANCE, recorded because the record should be readable.** This run was written under
the write-early protocol and committed section by section: `41a5cea` (Step 0 and the perimeter),
`6db44b2` (Q1), `37aa2c6` (Q2), `fcf9470` (Q2 addendum and Q3), `b2033a9` (Q4, Q5, Q6,
self-audit). A **concurrent DAL run in this same working tree** then swept the final two edits —
the defect register and this status block — into commit `c62b779`, which carries a DAL message.
No content was lost or altered; the run file on disk is byte-identical to HEAD. Recorded so a
later reader looking for "the commit that closed CRM" is not misled by the message on it.

**THE ANSWER IN ONE LINE: all four business gates clear; the name is quit on at the price.
Honest pre-tax expectancy 6.22%–9.62% against a ~10% floor, and no construction out of 33
yields as much as the 5.24% sovereign. Judged value roughly $80 to $240 against $259.23.**

---
## THE SCREEN ROW AS INHERITED — a prompt to read, never a score [operator rule 8]

```
cap_m 213659 | oe_bottom_m 3549 | oe_top_m 8952 | spread 1.522
yield_bottom 1.66% | vs_sovereign -3.58 pts | growth_required 8.34%
level_shift 2.70  STEP UP - normalize down [E4-41]
best_year_dep 0.256
acq_note: acquisitions are $27,399M inside the window (13% of cap)
newest_filing 2026-01-31
```

**Every line of this row is treated as a question, not an input.** What follows is the
rebuild.

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.24%** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-year,
  from the issuing authority** (`tools/sources.py`, which reads Treasury first and FRED only
  as fallback per CLAUDE.md as corrected 2026-09-02).
- FX: none required. Salesforce reports in USD and 65% of FY2026 revenue was United States
  (10-K, Note 2, geographic disaggregation). The earnings currency and the quote currency
  are the same. No ADR ratio.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary document · 10-K for fiscal 2026** (year ended **2026-01-31**), filed
  **2026-03-02**, accession **0001108524-26-000060**, document `crm-20260131.htm`.
- **Also read, and it changes the answer · 10-Q for the quarter ended 2026-07-31**, filed
  **2026-08-27**, accession **0001108524-26-000190**, document `crm-20260731.htm`. The
  brief's mandatory correction 5 is why this was pulled, and it fired. See below.
- **Figures cross-checked against the filed statement** (Consolidated Statements of Cash
  Flows, 10-K p.61, and Condensed Consolidated Balance Sheets, 10-Q p.3):
  - FY2026 net cash provided by operating activities **$14,996M** — matches XBRL.
  - FY2026 depreciation and amortization **$3,631M** — matches XBRL.
  - FY2026 stock-based compensation **$3,509M** — matches XBRL.
  - FY2026 capital expenditures **$(594)M** — matches XBRL, and it is a **single line**.
  - FY2026 business combinations, net of cash acquired **$(9,268)M** — matches XBRL.
  - 2026-07-31 noncurrent debt **$39,288M** against **$10,439M** at 2026-01-31.

### THE SHARE COUNT — CORRECTION 5 FIRED, AND IT IS THE LARGEST ERROR ON THE ROW

`tools/run.py` reported **956.0M shares** and a market cap of **$247.82B**. It says so itself
in its own warning line: the basis is `WeightedAverageNumberOfDilutedSharesOutstanding`,
*"a WEIGHTED AVERAGE, not a cover-page count."*

The cover page of the **latest periodic filing** says otherwise, verbatim:

> "As of August 20, 2026, there were approximately **823 million** shares of the Registrant's
> Common Stock outstanding." — 10-Q, accession 0001108524-26-000190, cover page

The full cover-page series, from `dei:EntityCommonStockSharesOutstanding`:

| cover date | form | shares (M) | accession |
|---|---|---|---|
| 2025-02-28 | 10-K | 961 | 0001108524-25-000006 |
| 2025-05-22 | 10-Q | 956 | 0001108524-25-000030 |
| 2025-08-28 | 10-Q | 952 | 0001108524-25-000088 |
| 2025-11-28 | 10-Q | 937 | 0001108524-25-000238 |
| 2026-02-25 | 10-K | 923 | 0001108524-26-000060 |
| **2026-05-21** | **10-Q** | **819** | 0001108524-26-000127 |
| **2026-08-20** | **10-Q** | **823** | **0001108524-26-000190** |

**104 million shares — 11.3% of the company — left the register in a single quarter**, and
then the count went back UP by 4 million in the next one. Both halves of that are findings
and both are worked at Q3.

**Market cap used throughout this run: 823.0M × $259.23 = $213,346M**, price dated
**2026-09-04** (aggregator, live quote only, flagged per operator rule 5). run.py's
$247.82B is **16.2% too high**. The inherited screen row's `cap_m 213659` is right, which
means the screen path and the run path disagree — recorded as a tooling defect at the end.

---
## THE PERIMETER — READ THIS BEFORE ANY NUMBER BELOW

*Method from `2026-09-06 Run - AVGO Broadcom.md`, which put this section above Q1 for the
same reason.*

The inherited row says acquisitions are **$27,399M inside the five-year window, 13% of cap —
"small against the cap but LARGE IN ABSOLUTE TERMS."** Both halves of that sentence are
wrong, and they are wrong in the same direction.

**Why the flag cannot see the real number.** `acquisition_flag()` reads the investing-section
line `PaymentsToAcquireBusinessesNetOfCashAcquired`. Salesforce's two largest acquisitions in
history were paid **substantially or entirely in its own stock**, and stock consideration never
touches the investing section. The CERT run found this defect at a $145M scale. Here it is
two orders of magnitude larger.

**The investing line, ten years (10-K cash-flow statements, $M):**

| FY | business combinations, net of cash acquired |
|---|---|
| 2017 | 3,193 |
| 2018 | 25 |
| 2019 | 5,115 |
| 2020 | 369 |
| 2021 | 1,281 |
| 2022 | 14,876 |
| 2023 | 439 |
| 2024 | 82 |
| 2025 | 2,734 |
| 2026 | **9,268** |

The five-year window FY2022–FY2026 sums to **$27,399M** and reproduces the row exactly. It is
the cash half only.

**What the flag missed, from the business-combination notes.** *(Filled at Q4 below with the
Slack and Tableau notes; the shape is already visible: FY2020 shows $369M of investing cash
in the year Tableau closed, because Tableau was an all-stock deal.)*

**The one piece of good news, and it is real: Salesforce filed the pro forma.** The Broadcom
finding was that where the filer files it, the perimeter work is done for you. Salesforce did,
for Informatica, in the FY2026 10-K, Note 4 — verbatim:

> "The following pro forma financial information summarizes the combined results of operations
> for the Company and Informatica, as though the companies were combined as of the beginning of
> the Company's fiscal 2025."

| combined perimeter, $M | FY2026 | FY2025 |
|---|---|---|
| Total revenues | 42,853 | 39,535 |
| Pretax income | 9,335 | 6,969 |
| Net income | 7,382 | 5,864 |

**On the combined perimeter, revenue grew 8.39%, not the headline 9.58%.** The MD&A says the
same thing in its own words: *"The acquisition of Informatica in November 2025 contributed
approximately $399 million of revenue."* Backing that out of the as-reported figures gives
**8.53% organic**. Two independent constructions, both filed, both land at ~8.4–8.5%.

**This matters at Q5 before Q5 opens**, so it is recorded here rather than there: the row's
`growth_required 8.34%` and the business's filed organic growth of 8.4–8.5% are the same
number. That coincidence is the whole file, and it is worked properly at Q5 — *if* Q1–Q4 get
there.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** A company rents a hosted database
of its own customer records, plus the workflow software that reads and writes to it, at a price
per employee per month, on a contract of one to three years, **paid in advance**. Salesforce
bills the year up front, banks the cash, and recognises the revenue ratably as the months pass.
The unrecognised balance sits on the liability side as unearned revenue — **$24,317M at
2026-01-31** — which is why operating cash flow ($14,996M) is nearly twice reported operating
income ($8,331M) and why the business needs almost no capital of its own. **The customers fund
the working capital.**

Of FY2026's $41,525M of revenue, **$39,388M (94.9%) is subscription and support** and $2,137M
is professional services, which *fell* 4%. The 10-K states the split itself: *"Subscription and
support revenues accounted for approximately 95 percent of our total revenues for fiscal 2026."*

Where the money goes, FY2026, as filed (Consolidated Statements of Operations, p.58):

| line | $M | % of revenue |
|---|---|---|
| Total revenues | 41,525 | 100.0 |
| Cost of revenues | 9,270 | 22.3 |
| **Gross profit** | **32,255** | **77.7** |
| Research and development | 5,993 | 14.4 |
| **Sales and marketing** | **14,345** | **34.5** |
| General and administrative | 3,000 | 7.2 |
| Restructuring | 586 | 1.4 |
| **Income from operations** | **8,331** | **20.1** |

The single largest cost in this business is **not** building the software. It is selling it.
Sales and marketing is 2.4x research and development, and it has been 2.2x–2.7x for a decade.
That fact is the hinge of Q2 and it is recorded here because it is a *description*, not yet a
judgment.

**The scarce input this business controls.** Not the code — the code has close analogues from
six large firms. What it controls is **the customer's own operational data plus the accumulated
configuration around it**: the objects, fields, permission model, workflow rules, reports and
third-party integrations a customer's own staff built over years inside the tenant. That artifact
is the customer's, not Salesforce's, but it is only executable inside Salesforce's runtime.
Salesforce controls the runtime. Second, it controls a **distribution ecosystem** — the system
integrators and AppExchange ISVs whose consulting revenue depends on the platform continuing to
be chosen.

**Will the fundamentals look broadly the same in ten years?** The revenue *mechanism* almost
certainly will: enterprises will keep paying a subscription to keep customer records in a
governed, hosted system, and they have been doing so through Salesforce for 26 years. What is
genuinely in motion is **the metering unit**. Salesforce has renamed its entire product line
Agentforce, and its own 10-K names the change as a risk to the metric it sells on:

> "Our attrition rates may increase or fluctuate as a result of various factors, including …
> pricing increases or changes, such as **the increased prevalence of consumption-based pricing
> models** and economic downturns." — 10-K FY2026, Item 1A

> "the markets and monetization strategies for certain offerings, including **Agentforce and
> Data 360, remain relatively new and uncertain**" — same

A seat business repricing itself as a consumption business is a change in the revenue equation,
not a marketing exercise, and where AI does more work per seat the seat count is the thing at
risk. **[E3-31]** asks whether the business is *"relatively simple and stable in character"*.
The **simple** half is unambiguously satisfied: two revenue lines, one segment, one cash-flow
statement I can read end to end. The **stable in character** half is where the doubt lives, and
it is a doubt about the *rate*, not about the *mechanism*.

**The verdict is IN, and it is IN narrowly and for a stated reason.** I can write the equation:
*seats × price × renewal, less an ~8% annual leak, less the cost of replacing that leak.* Every
term of it is a filed number. The uncertainty about the metering unit is uncertainty about
**growth**, which is a Q5 input, not about **comprehension**, which is what Q1 asks. Framework
**[E4-46]** is the discipline here: a named filing inside an understood business is a work order,
a business needing months of study is Q1 OUT. This needed the 10-K, the 10-Q and ten years of
MD&A. It did not need months.

**One thing recorded now so it cannot be smuggled in later.** The consolidated entity is
comprehensible; the **acquisition accounting is where the complexity actually sits**, and the
run keeps that at Q4 where it belongs rather than letting it fail Q1. Goodwill and acquired
intangibles are **$65,392M against total assets of $109,620M at 2026-07-31 — 59.7% of the
balance sheet.** That is a fact about how the company was assembled, not about whether I can
read the income statement.

- **VERDICT: [x] IN** · narrow, on comprehension of the revenue equation; the metering-unit
  question is carried forward to Q2 (moat direction) and Q5 (growth), not resolved here.

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

- **Needed or desired [x]** — 94.9% of revenue is subscription, remaining performance
  obligation is **$72.4bn** at FY2026 against $63.4bn (+14.2%), and the attrition rate is ~8%.
  Customers renew.
- **No close substitute [~]** — **contested, and this is where the run does its work.**
- **Not price-regulated [x]** — trivially satisfied.

### THE FILED ANSWER TO THE PRICING TEST, AND IT IS THE SAME EVERY YEAR

**[E2-44]** asks whether the business can raise prices *"even when product demand is flat and
capacity is not fully utilized."* **[E4-37]** says you can *"almost measure the strength of a
business over time by the agony they go through in determining whether a price increase can be
sustained."* Salesforce answers both questions itself, in its own MD&A, in **six of the last
seven 10-Ks**, in words that barely change:

> "The increase in subscription and support revenues … was primarily caused by **volume-driven
> increases** from new business … **Pricing was not a significant driver of the increase in
> revenues for the period.**" — FY2026 10-K, MD&A (accession 0001108524-26-000060)

The same sentence appears in the FY2020, FY2022, FY2023, FY2024 and FY2025 10-Ks. And the risk
factor names the reason:

> "Our attrition rates may increase or fluctuate as a result of various factors, including …
> **pricing increases or changes**, such as the increased prevalence of consumption-based
> pricing models" — FY2026 10-K, Item 1A

**Six consecutive years of filed testimony that price contributes essentially nothing.** That
is the agony end of **[E4-37]**'s metric, disclosed by the company. It also disposes of the
untapped-pricing-power class **[E3-33]** in the negative: **[E5-28]** scopes that class to *"a
monopoly or a near monopoly"*, and the competitor row below will not support such a claim.

### WHAT SALESFORCE'S OWN COMPETITION SECTION SAYS

This is Item 1, the business description, not a risk factor, and it is the CERT shape:

> "The market for our service offerings is highly competitive, rapidly evolving and fragmented,
> and subject to changing technology with **low barriers to entry** …
> - **AI-native companies and emerging startups** … offering highly specialized, autonomous, or
>   automated solutions that **may bypass traditional business process workflows or displace
>   established user interfaces**;
> - software companies that **provide their product or service free of charge** as a single
>   product or when bundled with other offerings …
> - **would-be customers who may develop enterprise applications for internal use.**"
> — FY2026 10-K, Item 1, Competition

Free substitutes, in-house build, and AI-native displacement, all named by the filer. **CERT
closed at Q2 on exactly this evidence.** It does not close Salesforce, and the reason is the
next section: at Certara the disclosed retention was *falling* (108.8% to 101.5%) and confirmed
the boilerplate. Here the disclosed metric contradicts it.

### THE PRIMARY MOAT METRIC — TEN VINTAGES, AND THE PRIOR WAS REFUTED

The brief asked whether the attrition disclosure was ever withdrawn or replaced with words
**[E2-49]**. **It was not.** It survives in all ten years, and the FY2026 10-K still carries a
number. This is the second consecutive run (after QLYS) where the withdrawal prediction was
refuted by the filings.

| FY | attrition rate | what is excluded from the calculation |
|---|---|---|
| 2017 | 8–9% | Marketing and Commerce Cloud |
| 2018 | 8–9% (also "<10%" incl. Marketing Cloud) | Marketing and Commerce Cloud |
| 2019 | <10% | Commerce Cloud, integration (MuleSoft) |
| 2020 | <9% | Commerce, Integration, Salesforce.org, Tableau |
| 2021 | **9.0–9.5%** | Integration, Salesforce.org, Tableau |
| 2022 | **7.0–7.5%** | MuleSoft, Salesforce.org, Tableau, **Slack** |
| 2023 | <7.5% | MuleSoft, Tableau, Slack |
| 2024 | ~8% | Slack |
| 2025 | ~8% | Slack self-service |
| 2026 | ~8% | Slack self-service **and current-year acquisitions** |

**Three readings, and they point in different directions.**

**First, and it is the candor pole [E2-49].** The FY2023 10-K pre-announced a change that it
expected to make its own number *worse*, with the reason, a year ahead:

> "**Beginning in the first quarter of fiscal 2024, Mulesoft and Tableau will be included in our
> attrition rate calculation, which we expect to slightly increase our attrition rate going
> forward.**" — FY2023 10-K

And it did: below 7.5% became ~8%. **[E2-49]** distinguishes the switch that *follows*
deterioration from the one *"announced ahead with reasons (as Berkshire's own 1982 switch
was)"*, and calls the second the candor case. This is the second. The metric-switching flag
**does not fire**.

**Second, the perimeter is nonetheless never like-for-like.** It moved in nine of ten years, and
the standing rule — *"In general, we exclude service offerings from acquisitions from our
attrition calculation until they are fully integrated into our customer success organization"* —
means that in a company that acquires continuously, the newest and least-proven revenue is
**permanently** outside the metric. Slack has been excluded in some form for **five consecutive
years**. The rule is disclosed and applied consistently, which is why this is a caveat and not a
flag, but **[E2-49]**'s demand is for *"pre-set, long-lived and small bullseyes"* and this
bullseye moves.

**Third, precision degraded.** FY2021 and FY2022 gave decimal ranges. FY2024, FY2025 and FY2026
give *"approximately eight percent"* three years running — a reading that cannot be falsified at
the first decimal place.

**And the level itself is the Q2 number.** ~8% attrition on $39,388M of subscription revenue is
roughly **$3.2bn of annualised contract value lost every year** that must be replaced before a
dollar of growth appears. Subscription revenue grew $3,709M in FY2026. **Gross new business had
to be on the order of $6.9bn to net $3.7bn.** That is the treadmill this franchise runs, and it
is what the $14,345M sales-and-marketing line buys.

**Where units exist, monitor units [E4-55].** Salesforce discloses **no unit series at all** — no
seat count, no customer count, no dollar-based net revenue retention. Attrition is the only
unit-adjacent metric it publishes, and it is a value rate, not a volume. Recorded as a
disclosure gap, not as a flag.

### THE COMPETITOR ROW — REQUIRED **[E3-28]**

*A moat is a claim about relative position and cannot be evidenced from one company's numbers.*
**Eight companies, which is the number Buffett names.** Metrics are the latest completed fiscal
year for each, filing-sourced.

| Company | FY end | Revenue $M | rev growth | **S&M % of rev** | R&D % of rev | GAAP op margin | SBC ÷ OCF |
|---|---|---|---|---|---|---|---|
| **Salesforce (CRM)** | 2026-01-31 | **41,525** | **9.6% (8.4% organic)** | **34.5%** | 14.4% | **20.1%** | **23.4%** |
| Microsoft (MSFT) | 2026-06-30 | 331,839 | n/a here | not disclosed separately | n/a here | 46.8% | 6.8% |
| Oracle (ORCL) | 2026-05-31 | 67,357 | n/a here | not disclosed separately | n/a here | 30.6% | 15.0% |
| SAP SE (EUR, unconverted) | 2025-12-31 | 36,800 | n/a here | not on this basis | n/a here | 26.1% | 18.5% |
| Adobe (ADBE) | 2025-11-28 | 23,769 | 10.5% | **27.3%** | tag absent | **36.6%** | 19.4% |
| ServiceNow (NOW) | 2025-12-31 | 13,278 | **20.9%** | 33.0% | 22.3% | 13.7% | 35.9% |
| Workday (WDAY) | 2026-01-31 | 9,552 | 13.1% | 27.4% | 28.0% | 7.5% | 55.3% |
| HubSpot (HUBS) | 2025-12-31 | 3,131 | 19.2% | **44.1%** | 28.9% | 0.2% | 69.4% |

**Sources.** MSFT, ORCL and SAP cells are reused from
`_research 2026-09-06 ORCL/competitor_row.md` (MSFT accession 0001193125-26-323660; ORCL
0001193125-26-277521; SAP 20-F 0001104659-26-020058) rather than rebuilt, per the brief. ADBE,
NOW, WDAY and HUBS are from SEC XBRL 10-K facts pulled here
(`_research 2026-09-07 CRM/peers/*.json`). **Flagged honestly: those four cells are tagged data,
not read filings.** They are used for *relative position*, which is what the row is for; no
verdict in this run rests on a peer cell alone, and the subject company's filing was read in full
per operator rule 4.

**Cells I could not fill, and why.** Microsoft does not break out Dynamics 365 revenue or its
sales-and-marketing line separately; Oracle does not disclose a cloud-applications segment
margin (the ORCL run recorded the same absence). SAP is EUR, unconverted, and its expense
captions do not map to a US-GAAP S&M line. Adobe does not tag `ResearchAndDevelopmentExpense` on
this basis. **Per [E3-28] those are named, not guessed.**

**What the row actually says, and it is not what the brief expected.**

1. **Salesforce spends more of its revenue on selling than every peer except HubSpot** — 34.5%
   against Adobe's 27.3% and Workday's 27.4%, and *above* ServiceNow's 33.0%. The largest,
   oldest, most entrenched company in the category has the second-highest selling intensity in
   the row. **[E2-45]**'s attacker's test is answered by that number: an attacker with capital
   does not have to out-build Salesforce, only out-sell it, and Salesforce's own cost structure
   states what that costs.
2. **Salesforce has the lowest GAAP operating margin of the four large peers** — 20.1% against
   Microsoft 46.8%, Adobe 36.6%, Oracle 30.6%, SAP 26.1%. After 26 years and $69bn of
   acquisitions it converts less of a dollar of revenue into operating profit than any of them.
3. **Salesforce is the slowest-growing pure-play application vendor in the row** — 8.4% organic
   against ServiceNow 20.9%, HubSpot 19.2%, Workday 13.1%. The category is growing; the leader
   is growing at less than half the rate of its two nearest challengers.
4. **The SBC comparison is a genuine point in Salesforce's favour and it is recorded as one.**
   23.4% of operating cash flow against ServiceNow 35.9%, Workday 55.3%, HubSpot 69.4%, and
   against CrowdStrike's 68.0% which contributed to closing that file. It is *better* than
   Qualys's 24.9%, which was explicitly cleared of the charge. Worked in full at Q4.

**The row's stated limit [E3-61].** Position is not conduct. *"In some businesses, the
participants behave like a demented Kellogg. In other businesses, they don't … I think you'd
have to know the people involved."* The row shows that Salesforce sells harder and earns less
per dollar than its peers. It cannot show whether Microsoft will choose to bundle Dynamics into
an existing enterprise agreement at a price Salesforce cannot match. That is a conduct question
and the corpus says even Munger had no model for it.

### THE [E4-04] TEST — MUST THE MOAT BE CONTINUOUSLY REBUILT?

The framework's test: *does a lapse in spending destroy the structure, or merely narrow it — and
does the spending defend the same advantage, or buy its replacement?*

**It merely narrows it.** The evidence is the core product lines' own disclosed revenue
(10-K Note 2, subscription revenue by service offering, $M):

| | FY2026 | FY2025 | FY2024 | FY26 growth |
|---|---|---|---|---|
| Agentforce Sales | 9,028 | 8,322 | 7,580 | +8.5% |
| Agentforce Service | 9,818 | 9,054 | 8,245 | +8.4% |

The system-of-record core is **growing, not shrinking**, at roughly the company rate. A year
without acquisitions would slow growth; it would not destroy the installed base, because the
base is held by the customer's own configuration, not by this year's spending. That is the
Coca-Cola-advertising side of the line, not the Rhodes-Ridge side. **[E4-04] does not fail.**

**Does success depend on a great manager? [E4-23]** No. The moat here is switching cost inside
the customer's own tenant, and it would survive the founder's departure. Recorded as **not** a
moat defect. Whether the founder-CEO is *the reason for the capital allocation* is a different
question and it belongs at Q3.

### CLASS AND DIRECTION

- **Class: NARROW.** Criterion (2) passes on revealed behaviour — 92% of contract value renews
  every year, for a decade, and RPO grew 14.2% — but it passes as a **switching-cost moat with
  no pricing power**, which is the weaker form. A product with truly no close substitute can
  take price; this one says every year that it does not.
- **Direction [E4-32]: FLAT TO NARROWING, and that is the primary criterion of a great business
  going the wrong way.** Attrition 7.0–7.5% (FY2022) to ~8% (three years running); price
  contribution nil for six years; organic growth 24.7% to 8.4% in four years; share of the
  applications market lost to two faster challengers. **The one genuinely widening line** is
  selling efficiency — sales and marketing fell from 47% of revenue (FY2017) to 34.5% (FY2026)
  — and that came from a headcount reduction under external pressure, which is worked at Q3, not
  from a wider moat.

- **VERDICT: [x] IN** · class **NARROW** · direction **flat to narrowing**. Not PROVISIONAL: the
  row is filled with eight companies and the four unfillable cells are named rather than guessed.

---
### ⟦ADDENDUM TO Q2 — 2026-09-07, same session, added before Q3 closed⟧

*Operator rule 6: corrections go in a marked addendum, never by editing history. The row above
was written with four cells marked "not disclosed separately" for Microsoft, Oracle and SAP.
Those cells **are** obtainable and were filled after the row was committed. The verdict does not
change; the evidence for it gets stronger and one new finding appears that the first row could
not see.*

**THE COMPLETED ROW.** Latest completed fiscal year each; **window caveat stated: fiscal ends
span seven months** (MSFT Jun-2026 and ORCL May-2026 run five to seven months ahead of the
Nov/Dec-2025 filers). SAP is EUR, unconverted. Sources: MSFT `0001193125-26-323660` · ORCL
`0001193125-26-277521` · SAP 20-F `0001104659-26-020058` · ADBE `0000796343-26-000003` ·
NOW `0001373715-26-000007` · HUBS `0001193125-26-046646` · WDAY `0001327811-26-000014` ·
CRM `0001108524-26-000060`. Full worksheet:
`_research 2026-09-07 CRM/COMPETITOR ROW CRM 2026-09-07 computed.csv`.

| | FYE | Revenue $M | YoY | 5y CAGR | **S&M / rev** | R&D / rev | GAAP op margin | SBC ÷ OCF | GW+intang % of assets |
|---|---|---|---|---|---|---|---|---|---|
| **Salesforce** | Jan-26 | 41,525 | **9.6%** | 14.3% | **34.5%** | **14.4%** | 20.1% | 23.4% | **57.7%** |
| Microsoft | Jun-26 | 331,839 | 17.8% | 14.6% | **8.0%** | 10.7% | 46.8% | 6.8% | 18.2% |
| Oracle | May-26 | 67,357 | 17.3% | 10.7% | **12.4%** | 15.3% | 30.6% | 15.0% | 25.0% |
| SAP (EUR) | Dec-25 | 36,800 | 7.7% | 6.1% | 24.1% | 18.0% | 26.1% | 18.5% | 44.5% |
| Adobe | Nov-25 | 23,769 | 10.5% | 13.1% | 27.3% | 18.1% | 36.6% | 19.4% | 45.3% |
| ServiceNow | Dec-25 | 13,278 | 20.9% | 24.1% | 33.0% | 22.3% | 13.7% | 35.9% | 18.0% |
| Workday | Jan-26 | 9,552 | 13.1% | 17.2% | 27.4% | 28.0% | 7.5% | 55.3% | 32.7% |
| HubSpot | Dec-25 | 3,131 | 19.2% | 28.8% | **44.1%** | 28.9% | 0.2% | 69.4% | 8.5% |

**What the completed cells add, and it sharpens the Q2 finding rather than softening it.**

1. **The selling-intensity gap against the two firms that can actually take Salesforce's seats is
   enormous.** Microsoft spends **8.0%** of revenue on sales and marketing and grew 17.8%. Oracle
   spends **12.4%** and grew 17.3%. Salesforce spends **34.5%** and grew 9.6%. Salesforce spends
   **4.3x Microsoft's proportion of revenue on selling and grows at half its rate.** That is
   **[E2-45]**'s attacker's test answered by the attacker's own cost structure.
2. **Salesforce has the LOWEST research intensity of the seven software peers** — 14.4%, below
   Oracle's 15.3%, SAP's 18.0%, Adobe's 18.1%, ServiceNow's 22.3%, Workday's 28.0%. It is the
   one that buys, rather than builds, and the perimeter section quantifies what that cost.
3. **The goodwill wedge is the largest in the row by twelve points** — 57.7% of total assets
   against Adobe's 45.3% and SAP's 44.5%. HubSpot at 8.5% is the only near-organic filer.

**THE NEW FINDING THE FIRST ROW COULD NOT SEE — the retention comparison.**

| | disclosed metric, verbatim caption | value | comparable to CRM? |
|---|---|---|---|
| **Salesforce** | "attrition rate" (TTM, value-based, exclusions listed above) | **~8%** → implies ~92% gross value retention | — |
| ServiceNow | "Renewal rate." (ACV-based) | **98%** | roughly |
| Workday | "Gross Revenue Retention Rate" | **~97%** (was ~98% in FY2025) | roughly |
| HubSpot | "Net Revenue Retention" (includes upsell) | 103.5% | **no** — a net metric |
| Microsoft / Oracle / SAP | none | — | — |
| Adobe | 9.9% "total attrition rate" — **an EMPLOYEE metric**, Human Capital section | — | **no** |

**On the nearest-comparable disclosed measures, Salesforce retains less of its contract value
each year than either Workday or ServiceNow.** ~92% against ~97% and 98%. The metrics are **not
like-for-like** — Salesforce's excludes Slack self-service and current-year acquisitions,
ServiceNow's excludes price and user changes and has been pinned at exactly 98% for eight
consecutive years, Workday's excludes expansion — and that caveat is carried, not buried. But
the direction of the gap is consistent with everything else in this row: the incumbent leaks
more, sells harder, researches less, and grows slower than the challengers.

**The Adobe cell is a trap and is recorded as one.** Adobe's numeric 9.9% "total attrition rate"
is *employee* turnover in Item 1's Human Capital section, not customer churn. SAP's old FY2020
20-F "Retention Rate of 95.3%" was the same trap and no longer appears. A screen matching on the
word "attrition" would have put Adobe's staff turnover in a moat row.

**Microsoft's Dynamics cannot be isolated, and the gap is structural.** Note 18 gives one
blended dollar line, *"Dynamics products and cloud services"* — **$9,006M (FY2026)**, $7,827M,
$6,831M, $5,796M — which the filing states explicitly mixes cloud and on-premises: *"including
Dynamics 365 … and on-premises ERP and CRM applications"*, and *"driven by growth in Dynamics
365, offset in part by a decline in Dynamics on-premises products."* The two move in opposite
directions and the split is never quantified. Dynamics 365 alone appears only as a growth rate
(18% in FY2026) with no base to apply it to, and Microsoft states it is *"impracticable"* to
identify amortization and depreciation by segment. There is exactly one Dynamics member in the
inline XBRL. **This is UNKNOWABLE from the filings, not UNRESEARCHED** — no document exists that
would resolve it.

**Q2 VERDICT UNCHANGED: IN, class NARROW, direction flat to narrowing.** The addendum makes
NARROW the clearly right call rather than the cautious one.

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

### STEP 1 — THE WEIGHT CASE. Nothing below counts until this is filled in.

*How much damage can this manager do before I can react?*

- [ ] **Daily execution [E3-38, E3-43, E2-70]** — **NOT TICKED.** The root of this test is *"their
  only products are promises"*. Salesforce's product is delivered software under a signed
  multi-year contract with $24.3bn of cash already collected in advance and $72.4bn of
  contracted revenue not yet recognised. A bad year of execution shows up as slower bookings,
  not as a hole in the balance sheet. **[E5-18]** is satisfied: this business will stand a little
  mismanagement.
- [ ] **Control [E1-16]** — **NOT TICKED.** Marketable security, exit available daily.
- [ ] **Leverage [E3-29]** — **NOT TICKED, and this is the close call, so the reasoning is
  written out.** The capital structure changed character in one quarter: debt principal went
  **$8,500M (FY2025) → $14,500M (FY2026) → $39,500M (2026-07-31)**, equity **$61,173M → $38,378M**,
  and **tangible book equity is negative $27,014M** ($38,378M of equity against $65,392M of
  goodwill and acquired intangibles). Against that: debt is **2.6x** operating cash flow;
  **[E2-54]**'s coverage test passes with room — FY2026 OCF of $14,996M less capex of $594M is
  $14,402M against interest running at roughly $1,900M a year, **7.6x** — the first maturity is
  **March 2028** and the whole FY2029 wall is about $6.0bn; and the filing states *"The Company
  was in compliance with all debt covenants as of July 31, 2026."* **[E3-29]**'s test is that
  *small asset errors destroy equity*. Here the assets that could be mis-stated are goodwill,
  and a goodwill write-down does not touch the cash that services the debt. **Not the leverage
  class — but it is closer than it was six months ago, and if the buyback continues on borrowed
  money this box gets ticked at the next look.**

**CASE DECLARED: none ticked → Q3 is a qualitative OVERLAY.** Findings are recorded and they
bind position size; manager quality alone does not stop this run. **[E5-18]**

### HONESTY — binary, permanent, filings-based **[E5-16]**

*"We are understanding about business mistakes; our tolerance for personal misconduct is zero."*
Each matter dated to when it became **public**.

**No disqualifier found, and the control record is genuinely clean:**

| test | finding |
|---|---|
| ICFR conclusion, FY2023 / FY2024 / FY2025 / FY2026 | *"was effective"* in all four; EY audited and concurred each year |
| Material weakness, any year | none disclosed |
| Restatement for error | none. The FY2019 revenue restatement is the **full retrospective adoption of ASC 606** — an accounting-standard change, and the filing says so |
| Auditor | Ernst & Young LLP — *"We have served as the Company's auditor since 2002."* 24 years, no change; ratified 2026 at 93.0% |
| Late filings | **none.** No NT 10-K or NT 10-Q in the entire filing history: 12 10-Ks and 37 10-Qs, all timely |
| SEC enforcement / Wells notice / subpoena | none found in Item 3 or the legal-proceedings note, FY2023–FY2026 |
| Pledging / hedging | *"Executive Officers and directors are not permitted to pledge our securities"*; hedging and short sales prohibited |

**One optics matter, dated and recorded rather than scored.** 8-K filed **2026-06-02**
(accession 0001108524-26-000138): the incoming Chief Accounting Officer *"served as the Company's
**Lead Audit Engagement Partner on behalf of EY**, the Company's independent auditor"* from 2016
to 2021. It is legal under the one-year cooling-off period and it is disclosed. It is also the
audit partner who signed off on this filer's statements taking the principal accounting officer's
chair at the same filer. **[E5-32]** is the reason it is written down at all — *"Audited does not
mean true"*; Salomon's floating plug survived twelve years of the largest audit firm in the
country. This is not a finding of anything. It is a note that one of the independent checks on
these statements is now less independent than it was, and it belongs on the page.

### STEP 2 — THE FLAGS **[E4-22, E5-15, E4-29, E4-30]**
*Each is a prompt to READ, never a verdict.* **[E5-36, E5-38]**

- [ ] **weak accounting** — **does not fire.** Stock compensation is expensed. Business
      combinations disclose the full consideration split, the intangible lives, and ASC 805 pro
      formas. Revenue recognition is conventional.
- [ ] **unintelligible footnotes** — **does not fire.** The notes are among the clearest this
      queue has read. The business-combination note gave up the whole perimeter in one table.
- [x] **trumpeted earnings projections / growth targets — FIRES, HARD.**
- [x] **serial share issuance [E5-15] — FIRES.**
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRES, with one real mitigant.**
- [ ] **filed-figure tells [E4-30]** — **does not fire, and the reason is now documented.**
- [x] **the restructuring charge [E3-53] — FIRES.**
- [ ] **metric-switching [E2-49]** — worked at Q2. Does **not** fire: the change was
      pre-announced a year ahead, with the reason, and in the direction that made the company's
      own number worse. That is the candor case the row names.
- [ ] **dividends funded by issuance [E2-52]** — does not fire. The $1,587M dividend is 11% of
      operating cash flow.

**FLAG 1 — TRUMPETED TARGETS. The action the corpus prescribes is to pull the company's own past
guidance and set it against outturn [E3-48]. Done.**

The target is in a filed document — 8-K filed **2022-09-21, accession 0001108524-22-000047**,
Item 7.01, Exhibit 99.1, the September 2022 investor presentation. Slide 24 is headed
**"Path to $50B"**:

> "$31B FY23 Guidance … **$50B FY26 Target** … **17% CAGR**"

Slide 39 restates it with the commitments attached: *"FY26 Revenue Target … $50B … **25%+ FY26
Non-GAAP Operating Margin** … Average Free Cash Flow Return 30-40% … $10B Share Repurchase
Authorization."*

**The outturn, from the FY2026 income statement: $41,525M. Short by $8,475M — 17.0%.** And
$399M of what was delivered came from Informatica, bought after the target was set, so on the
target's own portfolio basis the miss is larger. Delivered CAGR FY2023→FY2026 was about **9.8%
against the 17% promised**. The margin half of the same slide was **beaten decisively** — 34.1%
non-GAAP against "25%+" — and that is recorded as a point in management's favour, because
**[E3-48]** asks for the record of the people who made the projections, and the record is one
half badly missed and one half comfortably beaten.

**What happened next is the part that fires the flag.** The target was **replaced, not
reconciled.** 8-K filed **2025-10-16** (accession 0001108524-25-000168): *"Salesforce Announces
New FY30 Revenue Target of $60B+, 10% organic FY26-FY30 CAGR"* — issued **three and a half
months before the FY26 target period closed**, when the shortfall was already arithmetically
certain. Four months later it was raised again, to $63bn including Informatica. The same October
release introduced a *"Profitable Growth Framework, **50 by FY30**"* — subscription
constant-currency growth plus non-GAAP operating margin summing to 50 — which is **the identical
construct as the CEO's Margin & Growth PRSU metric**, currently running at 43.5.

**And the audited document carries no record of any of it.** The string "50 billion" appears
**zero times in all ten 10-Ks, FY2017 through FY2026**. The 10-K acknowledged obliquely in
FY2023–FY2025 that *"long-term targets"* existed; in **FY2026, the year the target came due
short, the phrase "long-term target" disappears from the 10-K entirely.**

**[E5-30]** is why this is weighted as a ratchet rather than as one bad year: *"once you start
it, it's all over. You can't quit … And forecasting earnings, I can't imagine anything more
destructive."* A missed target replaced by a longer-dated target announced before the first one
expired is that mechanism working. And **[E4-35]** prices the new promise: *"fewer than 10 of the
200 most profitable companies in 2000 will attain 15% annual growth in earnings-per-share over
the next 20 years."* The company that just delivered 9.8% against a 17% promise has published a
10% organic four-year CAGR. It is at least a promise sized to what the business has actually done,
which the last one was not.

**FLAG 2 — SERIAL SHARE ISSUANCE [E5-15].** *"one of the surest indicators of a promotion-minded
management, weak accounting, a stock that is overpriced and — all too often — outright
dishonesty."* The flag fires on the arithmetic. **The venality half of that sentence is expressly
NOT found** — **[E5-38]**: the flag reads the accounting; **[E5-16]**'s binary judges the person,
and it found nothing.

| | diluted weighted-average shares (M) | buyback that year ($M) |
|---|---|---|
| FY2017 | 700.2 | 0 |
| FY2018 | 734.6 | 0 |
| FY2019 | 775 | 0 |
| FY2020 | 850 | 0 |
| FY2021 | 930 | 0 |
| FY2022 | 974 | 0 |
| FY2023 | **997 — the peak** | 4,000 |
| FY2024 | 984 | 7,620 |
| FY2025 | 974 | 7,829 |
| FY2026 | 956 | 12,596 |
| Q2 FY2027 | 821 | 27,332 (H1, of which $25,000 debt-funded ASR) |

**Six consecutive years with no repurchase programme at all, during which the diluted count rose
39%.** The word "repurchase" appears in the FY2017–FY2022 10-Ks only in debt-covenant
boilerplate. The programme did not exist until **August 2022** — which is to say, until after an
activist arrived.

**Where the shares went. [E5-44] is the governing test: *"The intrinsic value of the shares you
give in an acquisition must not be greater than the intrinsic value of the business you
receive."*** Stock consideration paid for acquisitions, from the business-combination notes:

| deal | closed | total consideration $M | **paid in stock $M** | what the filing says it delivered |
|---|---|---|---|---|
| MuleSoft | FY2019 | 6,425 | 1,178 | no separate pro forma filed |
| Datorama | FY2019 | 766 | 537 | — |
| **Tableau** | FY2020 | **14,845** | **14,552** *(cash: $1M)* | stub revenue $689M, **pretax loss $(503)M** |
| ClickSoftware | FY2020 | 1,386 | 663 | — |
| **Slack** | FY2022 | **27,068** | **11,064** | FY2022 revenue $592M, **pretax loss $(1,105)M** |
| **stock total** | | | **$27,994M** | |

**$28.0bn of Salesforce stock was issued to buy businesses, and the investing section of the
cash-flow statement never saw a dollar of it.** Tableau is the pure case: **$14,845M of
consideration, of which cash was one million dollars**, in a fiscal year whose "business
combinations, net of cash acquired" line reads **$369M**. The consideration is in the equity
statement instead: *"Shares issued related to business combinations — 102 [million shares] —
$15,588."*

**FLAG 3 — ADJUSTED-EARNINGS PROMOTION [E4-29].** The FY2026 bridge, from the earnings release
(8-K accession 0001108524-26-000056, Exhibit 99.1):

| | FY2026 $M |
|---|---|
| GAAP income from operations | **8,331** |
| + amortization of purchased intangibles | 1,687 |
| + stock-based compensation | 3,480 |
| + restructuring and acquisition-related costs | 658 |
| **Non-GAAP income from operations** | **14,156** |
| GAAP operating margin | **20.1%** |
| **Non-GAAP operating margin** | **34.1%** |

**The bridge is $5,825M — 70% of GAAP operating income and 14.0 margin points.** Non-GAAP diluted
EPS is $12.52 against GAAP $7.80, a 60% uplift. The stated rationale for the largest add-back is
the one the corpus refuses outright:

> "**Stock-Based Compensation Expense:** … It is principally aimed at aligning their interests
> with those of our stockholders and at long-term employee retention, **rather than to motivate
> or reward operational performance for any particular period.** Thus, stock-based compensation
> expense varies for reasons that are generally unrelated to operational decisions and
> performance in any particular period."

**[E5-06]**: *"To say 'stock-based compensation' is not an expense is even more cavalier."* And
the asymmetry the paragraph creates is visible on this company's own cash-flow statement: SBC is
removed from earnings on the ground that it is not pay for the period's performance, while
**$22.6bn of it over ten years diluted the count 36.5%** and **$59.4bn of shareholder cash has
since been spent buying shares back.**

**THE ONE REAL MITIGANT, and it is a genuine one.** The word *"non-GAAP"* appears **zero times
in every Salesforce 10-K from FY2017 through FY2026** and zero times in every recent 10-Q —
verified string by string across ten annual reports. So does "free cash flow", and so does "ARR".
**The audited annual report is clean of the promotion entirely.** The whole non-GAAP apparatus
lives in Exhibit 99.1 of furnished 8-Ks. Under **[E2-26]**'s half-owner test that is a
meaningfully better posture than burying the adjustment inside the 10-K's own MD&A, and it is
recorded as such. **It becomes a problem only when you ask what the CEO is paid on** — which is
the next section, and where the two facts collide.

**FLAG 4 — THE RESTRUCTURING CHARGE [E3-53].** Announced 8-K **2023-01-04** (accession
0001108524-23-000003), Item 2.05: *"a reduction of the Company's current workforce by
approximately 10 percent"*, with an estimate of *"approximately $1.4 billion to $2.1 billion in
charges."*

| FY | charge $M | as described in the filing |
|---|---|---|
| 2023 | 828 | "$683 million relates to employee transition, severance … $145 million … office space reductions" |
| 2024 | 988 | "$541 million … severance … $447 million … office space reductions" |
| 2025 | 461 | "primarily related to employee transitions, severance payments and employee benefits" |
| 2026 | 586 | "primarily related to employee transitions, severance … as well as select data center exits" |
| **total** | **2,863** | **$763M above the top of the announced range, across four consecutive years** |

The FY2024 10-K said *"We do not expect to incur significant additional charges in connection
with our initiatives in the near term."* It then charged $461M, said it again, charged $586M, and
says it a third time. The FY2026 10-K has dropped the defined term "Restructuring Plan" for a
standing posture — *"We have undertaken **various restructuring initiatives**"* — and the
non-GAAP reconciliation now carries **"Restructuring and acquisition-related costs" as a
permanent line**, present every quarter and inside FY2027 guidance. **[E5-33]**: *"to tell owners
year after year, 'Don't count this' … is misleading."* **A charge excluded as non-recurring in
four consecutive years, with a fifth guided, is recurring.** It is left inside operating cash
flow and therefore inside owner earnings at Q4, exactly as **[E5-33]** requires.

**FLAG 5 — THE FILED-FIGURE TELLS [E4-30]. Tested and it does NOT fire. The work is shown
because the brief asked for it and because the FY2026 number looks alarming until you read the
note.**

*Unnaturally smooth reported growth:* **absent.** Growth ran 24.7% → 18.3% → 11.2% → 8.7% → 9.6%.
Nobody smoothing anything produces that series.

*Cash taxes falling as a share of reported pretax income:* the headline looks like the tell.

| FY | pretax $M | provision % | **cash taxes paid $M** | **cash % of pretax** |
|---|---|---|---|---|
| 2024 | 4,950 | 16.4% | 1,027 | 20.7% |
| 2025 | 7,438 | 16.7% | 2,061 | 27.7% |
| 2026 | **9,520** | **21.5%** | **1,282** | **13.5%** |

Cash taxes fell **38% in absolute dollars while pretax income rose 28%.** **The resolving
document was named and has been read** — FY2026 10-K, income-tax note, the ASU 2023-09
disaggregation, which Salesforce adopted in Q4 FY2026:

| income taxes paid, net of refunds ($M) | FY2026 | FY2025 |
|---|---|---|
| Federal | **658** | 1,091 |
| State | 132 | 276 |
| Ireland | 92 | 139 |
| Israel | **0** | 287 |
| Other foreign | 400 | 268 |
| **total** | **1,282** | **2,061** |

The fall is Federal (−$433M), Israel (−$287M) and State (−$144M). The mechanism is on the face of
the deferred-tax table in the same note: the **"Capitalized research & development" deferred tax
asset fell from $2,431M to $1,944M**, a $487M unwind — the Section 174 capitalisation reversing —
which is a **timing and legislative** effect, not a divergence between book and cash earnings.
**And the decisive point is the direction of the book number: the provision RATE ROSE, 16.7% →
21.5%.** **[E4-30]**'s tell is cash taxes falling *while the reported number is being pushed up*.
Here the reported tax burden rose and the cash burden fell for a reason the filing states. **The
flag does not fire, and this is recorded as a refutation, not as a pass.**

### THE CONVERGENCE — [E4-52], AND IT IS THE CENTRAL Q3 FINDING

*"extreme consequences from **confluences** of psychological tendencies acting in favor of a
particular outcome … it dominates life."* Four flags fired. They are not four prompts to be
summed. **They point at one thing.**

**THE PAY METRICS ARE NOT FILED NUMBERS — the Broadcom finding replicated, and worse.**
(DEF 14A filed 2026-04-16, accession 0001108524-26-000085.)

| what the CEO is paid on | weight | is that exact metric a filed number? |
|---|---|---|
| **Non-GAAP Income from Operations** | 50% of the annual bonus | **NO.** "non-GAAP" appears **zero times in ten consecutive 10-Ks** and zero times in every recent 10-Q |
| **Non-GAAP operating margin** ("Margin & Growth") | half the PRSUs | **NO.** No operating-margin figure, GAAP or non-GAAP, is quantified anywhere in the 10-K |
| **"Agentforce & Data 360 ARR"** | 33% of the FY2026 equity grant — **and it vested at 200%** | **NO.** The string appears **zero times in any filed report**; "ARR" and "Annual Recurring Revenue" also appear zero times, all ten years |
| Subscription and support revenue | 50% of the annual bonus | the GAAP line is filed — but the plan uses it **"on a constant currency basis, as discussed in Exhibit 99.1 to the Company's Form 8-K"** |
| Relative TSR vs the Nasdaq-100 | half the PRSUs | yes, market-based and verifiable |

The plan's own definition concedes the gap in writing:

> "'Non-GAAP Income from Operations' is defined as … **further excluding the impact of adjustments
> to the bonus payout percentage** … and **as may be further adjusted for other impacts of certain
> acquisitions. As a result, these financial metrics may differ from the financial results we
> report in our quarterly earnings release materials.**"

Not "may differ from our audited statements" — **may differ from the earnings release**, which is
already the unaudited document. **Three different values of "non-GAAP income from operations"
circulate for fiscal 2026**: $14,156M in the proxy's own Appendix A reconciliation (matching the
earnings release), **$14,216M** in the bonus scorecard, and a PRSU margin of 33.9% against the
reconciliation's 34.1%.

**And the one clean GAAP metric that was in the plan was removed.** Operating cash flow was a
bonus metric in FY2024 and FY2025. **It was dropped for FY2026.**

**Every pay metric except relative TSR is sourced to Exhibit 99.1 of an 8-K — furnished, not
filed, outside the auditor's opinion and outside Section 18 liability.**

**This is the confluence.** The non-GAAP apparatus is kept out of the audited report (which
reads as candour), and the executive scorecard is then built entirely on that same
out-of-the-audited-report apparatus (which is the opposite). Growth is bought with stock that the
cash-flow statement cannot see; the resulting amortisation is added back to reach the number the
CEO is paid on; the dilution is then repurchased with borrowed cash; and the missed revenue
target is replaced rather than reconciled. **[E4-52]** is the right lens: these are not four
independent prompts, they are one reinforcing system pointing at a scoreboard that no auditor
signs.

**The corpus's own caution applies at full strength [E5-38]:** people Buffett would trust with
his wallet *"would play games with any number that came to them."* **This is not a venality
finding. It is an accounting-and-disclosure finding, and it binds position size, not the
discount rate.**

**And the shareholders have said the same thing in a filed vote.** Say-on-pay, computed from the
Item 5.07 8-Ks:

| meeting | % for | 8-K accession |
|---|---|---|
| 2023-06-08 | 82.11% | 0001108524-23-000029 |
| **2024-06-27** | **45.60% — FAILED** | 0001108524-24-000014 |
| 2025-06-05 | 76.85% | 0001108524-25-000033 |
| 2026-05-28 | 80.75% | 0001108524-26-000131 |

The 2025 proxy states the cause in the company's own words: *"The overwhelming majority of
stockholders expressed disfavor for the **one-time supplemental off-cycle equity grant** awarded
to our CEO outside our annual compensation program, with the majority noting it was **the primary
driver of their 2024 say-on-pay vote**."* The grant: a $15M annual award in Q1 FY2024, then *"a
second fiscal 2024 long-term equity incentive award … total target value of $20 million"* near
year-end. **The corrective cycle that followed raised the bonus funding cap from 100% to 150%
and set the FY2027 CEO target at $48M** — against a **filed** company TSR of **$94.12 per $100
invested versus a peer group's $256.61**, and a Compensation Actually Paid figure for FY2026 of
**negative $49.2M**. Benioff remains combined Chair and CEO; independent-chair proposals drew
22.6% and 21.6%. The Lead Independent Director, Robin Washington, **left that seat in March 2025
to become an executive officer of the company she had been the independent check on.**

### STEP 3 — THE PRIMARY TEST **[E2-01]**

*"The primary test of managerial economic performance is the achievement of a high earnings rate
on equity capital employed … and not the achievement of consistent gains in earnings per share."*
Multi-year series, balance sheet before income statement.

| FY | net income $M | ending equity $M | **ROE** |
|---|---|---|---|
| 2017 | 323 | 8,230 | 3.9% |
| 2018 | 360 | 10,376 | 3.5% |
| 2019 | 1,110 | 15,605 | 7.1% |
| 2020 | 126 | 33,885 | 0.4% |
| 2021 | 4,072 | 41,493 | 9.8% |
| 2022 | 1,444 | 58,131 | 2.5% |
| 2023 | 208 | 58,359 | 0.4% |
| 2024 | 4,136 | 59,646 | 6.9% |
| 2025 | 6,197 | 61,173 | 10.1% |
| 2026 | 7,457 | 59,142 | **12.6%** |

**Ten-year mean ROE on ending equity: 5.7%. Nine of the ten years are below 10%.** FY2026 is the
first year above 12% in the decade, and part of how it got there was the denominator: $12.6bn of
buyback drove equity **down** $2.0bn in a year the company earned $7.5bn.

**[E2-42]** sets the reference: *"Red lights should start flashing if the five-year average annual
gain falls much below the return on equity earned over the period by American industry in
aggregate."* The five-year mean here is **6.5%**. The light is on.

**[E2-43] — the acquisitive-filer denominator, with the goodwill wedge reported separately and
never hidden in book equity.**

| FY | equity $M | goodwill $M | intangibles $M | **GW+intang** | **tangible equity** |
|---|---|---|---|---|---|
| 2022 | 58,131 | 47,937 | 8,978 | 56,915 | +1,216 |
| 2023 | 58,359 | 48,568 | 7,125 | 55,693 | +2,666 |
| 2024 | 59,646 | 48,620 | 5,278 | 53,898 | +5,748 |
| 2025 | 61,173 | 51,283 | 4,428 | 55,711 | +5,462 |
| **2026** | 59,142 | 57,941 | 6,815 | **64,756** | **−5,614** |
| **2026-07-31** | **38,378** | **59,250** | **6,142** | **65,392** | **−27,014** |

**The wedge is larger than the entire equity account.** Everything Salesforce owns that is not
goodwill or a purchased intangible is worth **less than nothing** against its liabilities.

**A return on unleveraged net tangible assets is computable and is deliberately NOT ranked on.**
At FY2026 it reads 74.6% and at 2026-07-31 it would read higher still. That is arithmetically
true and economically empty: the ratio is large because the denominator has been consumed by
acquisition premia and a debt-funded buyback, not because a small tangible base throws off large
earnings. The competitor row makes the point cleanly — **Microsoft (38.8%) and SAP (37.5%) are
the only peers in the row that earn a high return on a positive, unsubsidised tangible base.**

**[E2-73]** says pick the denominator by the question asked, and there are two questions here with
two different answers:
- *What return do the operators earn on the assets they work with?* **High.** The CRM business
  needs almost no tangible capital: $594M of capex on $41,525M of revenue.
- *What return do owners earn on the capital actually committed?* **5.7% mean over ten years**,
  because the capital committed includes **$69.4bn paid for other people's businesses.**

**Both go on the page. That gap is the whole of Q3.**

### THE HALF-OWNER TEST **[E2-26]**

*Does this reporting tell me what I would want to know if the positions were reversed?*

**Where it passes, and it passes well.** The attrition rate is disclosed for ten straight years,
with the perimeter named each time and a worsening change pre-announced a year ahead. Every
acquisition's consideration is split cash-versus-stock in the notes. **Three ASC 805 pro formas
were filed — Tableau, Slack and Informatica — and all three are unflattering**, which is the
disclosure a management with something to hide would not volunteer. Restructuring charges are
quantified separately at every line. The FY2020 10-K even volunteered *why* its attrition number
looked good: *"Our attrition rate for fiscal 2020 **benefited, in part**, from the ongoing shift
in our business mix to enterprise and international markets which have longer customer contract
term durations."*

**Where it fails.** The 10-K contains no ARR, no net revenue retention, no customer count, no
free cash flow, no non-GAAP reconciliation, one reporting segment, and — in the year the target
came due 17% short — **no mention that a $50bn target was ever set.** A shareholder who reads only
the audited annual report cannot find the scoreboard the CEO is actually paid on, cannot find the
promise that was missed, and cannot decompose the single segment.

### THE INSTITUTIONAL IMPERATIVE — SCORE ALL FOUR **[E2-30]**
*Not a fraud test: "institutional dynamics, not venality or stupidity."*

- [ ] **resists any change in current direction** — **NOT ticked, and the evidence is against it.**
  January 2023: a 10% workforce cut, a hard margin pivot, and a rewritten 10-K vocabulary
  ("restructuring" 0→46 mentions, "profitable growth" 0→4, "share repurchase" 0→26, "activist"
  0→1, all from six consecutive years of zero). GAAP operating margin went 3.3% → 20.1% in three
  years. **This management changed direction violently.** What it did not do is change direction
  *by itself* — the change followed the activist, which is the next box.
- [x] **projects/acquisitions materialise to soak up available funds** — **TICKED, and it is the
  largest fact in this run.** **$69.4bn of total acquisition consideration over ten years against
  $39.7bn of cumulative owner earnings at the most generous construction — 1.75x.** Then, having
  paid $9.6bn cash for Informatica in November 2025, the company **borrowed $31bn four months
  later** to buy its own stock. Both directions used the funds; neither left any.
- [ ] **staff studies produced to justify the leader's craving** — **not ticked, and I cannot
  evidence it from filings.** Named as unevidenced rather than assumed. **[E3-58]**'s outsourcing
  variant does not fire either: capital allocation here is visibly the founder's own, not a
  banker's or a consultant's.
- [x] **peer behaviour mindlessly imitated** — **ticked with a caveat that matters.** The
  January-2023 playbook — mass layoff, margin target, buyback authorisation, first-ever dividend
  — is precisely what every large software company ran in that quarter. **[E2-30]** says this is
  institutional dynamics, not stupidity, and here the imitation **worked**: margin 3.3% → 20.1%.
  Ticked because the behaviour is the behaviour; noted because the outcome was good.

### CAPITAL ALLOCATION — THE BUYBACK, AND THE DILUTION QUESTION ATTACHED

**[E5-08]**'s two conditions, plus **[E4-31]**'s third.

**(1) Ample funds for operations and liquidity?** Operations, yes. **But the buyback was not made
from ample funds — it was made from borrowings.** In March 2026 Salesforce issued **$25.0bn of
senior notes plus a $6.0bn term loan** and *"used the net proceeds from the March 2026 Notes to
fund an accelerated share repurchase program of its common stock."* Cash and securities had
already fallen from $14,032M to $9,565M over FY2026. **[E5-25]** is the standard: Berkshire
published its liquidity floor **as a number, in advance** — *"financial strength that is
unquestionable takes precedence over all else."* Salesforce publishes no such floor.

**(2) At a material discount to conservatively calculated intrinsic value?** The ASR bought
**~103 million shares at an average price of $198.34**, plus 11M at $192.00 in the open market.
The money to buy them cost **4.24% to 6.70%** — the long tranches price at 6.40% (2046), 6.55%
(2056) and **6.70% (2066)**.

Against that, owner earnings per share at $198.34, on the constructions built at Q4 below and on
823M shares:

| construction | OE $M | per share | **yield at $198.34** |
|---|---|---|---|
| 5-year window, corpus default [E2-42], (c) = total D&A | 3,549 | $4.31 | **2.2%** |
| 5-year window, (c) = capex | 6,479 | $7.87 | 4.0% |
| 3-year window, (c) = capex — the most generous multi-year | 8,952 | $10.88 | 5.5% |
| TTM to 2026-07-31, (c) = capex — the single most generous number in this run | 11,489 | $13.96 | 7.0% |

**Borrowing at 4.2%–6.7% to buy an asset yielding 2.2%–7.0%, where the conservative end of the
range is a third of the cost of the money.** **[E4-50]** licenses exactly this behaviour —
Munger's wiser board buys *"very aggressively, using up all cash on hand **and also borrowing
funds**"* — but it licenses it **on the discount**: *"the discount does the licensing, never the
borrowing."* On this run's arithmetic there is no discount at the conservative end. **CONDITION
(2) FAILS → CAPITAL-ALLOCATION FLAG.**

**Stated with the humility clause, and it is not a formality here [E4-13, E5-08].** *"it is
natural for CEOs to be optimistic about their own businesses. They also know a whole lot more
about them than I do"*; *"many CEOs never stop believing their stock is cheap."* This flag rests
entirely on **my** owner-earnings range. Management bought at $198 and the quote today is
$259 — **on the only scoreboard available so far, they were right and I am the one being
second-guessed.** The flag binds **position size, never the discount rate.**

**(3) [E4-31]'s third condition — *"Shareholders should have been supplied all the information
they need for estimating that value."*** Weakly met at best: one segment, no ARR, no net
retention, no customer count, no reconciliation inside the audited report.

**THE DILUTION QUESTION, ANSWERED PLAINLY, BECAUSE THE BRIEF ASKED FOR A PLAIN ANSWER.**

*"A buyback that only offsets dilution is not a return of capital — it is a payroll expense
settled in cash. State plainly which it is."*

**It is both, in three distinct phases, and the phases must not be blended.**

- **FY2017–FY2022 — pure dilution, no buyback.** Diluted shares 700.2M → 974M, **+39%**, with
  **zero** repurchases in six years and $10.9bn of SBC expensed.
- **FY2023–FY2026 — overwhelmingly a payroll expense settled in cash.** $32,045M spent; diluted
  weighted-average shares 997M → 956M, **−41M, −4.1%.** That is **$782M of cash per million net
  diluted shares retired**, against an average repurchase price around $222–254. **Roughly
  three-fifths to two-thirds of that $32bn bought back stock the company had just issued to its
  own staff.** Over the same four years SBC ran $12,758M.
- **H1 FY2027 — a genuine return of capital, and it was borrowed.** $27,332M retired ~114M shares
  gross; cover-page count 929M → **823M**, a real 11.4% reduction. This one is not a payroll
  offset. **It is $31bn of 4.2%–6.7% debt converted into stock at $198.**

**And the register began re-inflating the moment the ASR stopped.** Cover-page shares went
**819M (2026-05-21) → 823M (2026-08-20)** with **zero** open-market repurchases in Q2 FY2027. The
mechanism is in the 10-Q's own equity note: restricted stock outstanding went **26M units
(2026-01-31) → 39M units (2026-07-31)** in six months, because 22M RSUs were granted at a
weighted-average **$191.68** against a prior book at **$265.64**. **A falling share price means
more shares granted per dollar of pay.** Remaining SBC to be recognised at 2026-07-31: **$8,324M.**

**The ten-year statement, which is the one that matters.** Diluted weighted-average shares went
**700.2M → 956.0M, +36.5%.** Cover-page shares outstanding went **707.5M (2017-01-31) → 823M
(2026-08-20), +16.3%.** After $59.4bn of cumulative repurchases and $22.6bn of stock
compensation, **an owner of Salesforce owns a smaller fraction of it than a decade ago.**

**[E3-54] — THE CORPUS'S OWN SCORED TEST, AND IT IS FILED.** At least $1 of market value per $1
retained, five-year rolling. Salesforce's own Pay-versus-Performance table reports **company TSR
at $94.12 per $100 invested, against a peer group at $256.61.** Over that period the company
retained the great majority of roughly $40bn of earnings. **Less than a dollar of market value
per dollar retained — a good deal less. The test fails, on the company's own filed number.**

**[E2-56] — the Pro-Am effect, and it is the diagnosis.** *"Their marvelous core businesses …
camouflage repeated failures in capital allocation elsewhere."* Salesforce reports **one
segment**, so segment-level retention cannot be judged from the filings. But the filed pro formas
do the job the segments will not, and **all three point the same way**:

| deal | filed ASC 805 pro forma | reported actual | direction |
|---|---|---|---|
| Tableau, FY2020 | net **loss** $(292)M | net income $126M | **a profit becomes a loss** |
| Slack, FY2022 | net income $1,127M | $1,444M | **−22%** |
| Informatica, FY2026 | net income $7,382M | $7,457M | **−1%** |

**Every acquisition Salesforce filed a pro forma for reduced combined net income on a
like-for-like basis.** The company disclosed this itself, three times, unprompted — which is the
half-owner test passing and the capital allocation failing, in the same document.

**[E4-39] — the rare-positive tell is ABSENT.** *"A candid acquisition post-mortem is almost
never witnessed."* The Washington Post reviewed every deal three years on. Salesforce publishes
no post-mortem, and it replaced the $50bn target rather than reconciling it. Recorded as an
absence, not as a flag.

### THE GUARDRAIL — checked before writing the verdict

- [x] **Confirmed: nothing in this Q3 is being used to promote the name.** **[E2-37, E2-38,
      E3-39]** — the January-2023 turnaround was a genuinely impressive piece of operating work
      (margin 3.3% → 20.1% in three years), and *"a textile company that allocates capital
      brilliantly within its industry is a remarkable textile company — but not a remarkable
      business."* It repairs nothing at Q2 and substitutes for nothing at Q4.
- [x] **Key-person dependence was recorded at Q2 [E4-23]**, where it was found **absent**.
- [x] **Is a great manager the reason to act? No.** **[E2-35, E2-36]** is not engaged; there is no
      excisable cancer and no Pygmalion here.
- **[E3-40]'s two vectors, tested.** *"Loss of focus is what most worries Charlie and me … the
  management of a great company gets sidetracked and neglects its wonderful base business while
  purchasing other businesses that are so-so or worse."* **This is the closest thing in the corpus
  to a description of Salesforce's ten-year record**, and it is a **Q6 exit trigger**, not an
  engagement plan **[E4-24, E4-49]**. Against it, and it must be weighed: the base business was
  **not** neglected — Agentforce Sales grew 8.5% and Agentforce Service 8.4% in FY2026, and the
  margin repair was done to the core, not to the acquisitions.

### VERDICT

- **VERDICT: [x] IN** — meaning **no disqualifier found**, which is all this gate can ever mean.
  **[E5-17]**: *"People are not that easy to read. Sincerity and empathy can easily be faked."*
  **[E5-26]**: a decade of strong record preceded Sokol. This is **not** a finding that the
  managers are honest; it is a finding that four flags fired on the accounting and disclosure, the
  binary integrity test found nothing, and the control record is clean.
- **LIVE: a CAPITAL-ALLOCATION FLAG on [E5-08] condition (2)**, and an **[E4-52] convergence**
  of four flags on a single scoreboard that no auditor signs. **Both bind position size. Neither
  touches the discount rate [E4-13].**
- **IN NEVER PROMOTES.** Nothing above improves Q2's NARROW or advances Q4.

---
## Q4 — WILL IT SURVIVE?

### THE (c) JUDGMENT — THE AVGO/CVX INVERSION IS LIVE, AND IT RESOLVES TO A THIRD NUMBER

**[E2-23]**: *"(c) the average annual amount of capitalized expenditures for plant and equipment,
etc. that the business requires to fully maintain its long-term competitive position and its
unit volume"* … *"**(c) must be a guess**."* **[E3-44]** makes D&A the corpus default;
**[E5-20]** names the exception class where D&A *understates* renewal. **Salesforce is in
neither class, and the run says so rather than defaulting.**

**Step 1 — decompose the D&A line, because it is a composite and the filing says so.** FY2026
cash-flow statement, footnote (1) to the statement itself: *"Includes amortization of intangible
assets acquired through business combinations, depreciation of fixed assets and amortization and
impairment of right-of-use assets."*

| FY2026 D&A of $3,631M | $M | share | is it renewal capital? |
|---|---|---|---|
| Amortization of **acquired** intangibles (income-statement footnote: $692M in cost of revenues + $995M in sales and marketing) | **1,687** | **46.5%** | **No** — see step 3 |
| Depreciation and amortization of **fixed assets** (10-K property-and-equipment note: *"totaled $1.2 billion, $1.0 billion and $1.1 billion during fiscal 2026, 2025 and 2024"*) | **~1,200** | 33.0% | **Yes** |
| Amortization and impairment of **right-of-use assets** (residual) | **~744** | 20.5% | **No** — already inside OCF as rent |

**Step 2 — the physical half is settled, and capex ALONE understates it by half.** Fixed-asset
depreciation is **$1,200M against capital expenditures of $594M — 2.02x.** That looks like the
**[E5-20]** railroad exception until you find the missing cash: **"Principal payments on
financing obligations" of $584M sits in the FINANCING section**, not investing. It is the
repayment leg of build-to-suit and finance-lease obligations on data centres and offices — real
cash, spent on real assets, that the investing line never sees. **[E3-52]** is the instruction
to read the terms rather than the caption.

> **capex $594M + financing-obligation principal $584M = $1,178M, against fixed-asset
> depreciation of $1,200M. A ratio of 0.98x.**

Two independent routes to the same number. **This is squarely the [E3-44] / [E2-41] DEFAULT
class** — *"capital expenditures that over time roughly approximate depreciation"* — once the
whole cash outflow is counted. The MSFT and ORCL runs found the opposite shape (capex 3.4x and
7.3x depreciation); Salesforce is the CERT/AVGO shape at the physical level and the default
class at the same time.

**Step 3 — the intangible half is a cost already paid, and its renewal is already inside
operating cash flow.** The ruling established at AVGO and applied at CERT governs:
**acquisition amortisation renews nothing that R&D above the OCF line does not already renew.**
The $1,687M is the run-off of purchase prices settled in FY2020, FY2022 and FY2026 — Tableau's
$14,845M, Slack's $27,068M, Informatica's $9,636M. What keeps that technology current is
**research and development, expensed above the operating-cash-flow line at $5,993M, 14.4% of
revenue**. To deduct the amortisation as well would charge the renewal twice.

**Step 4 — the right-of-use amortisation is rent, and rent is already netted inside OCF.** The
cash-flow statement adds back the ROU amortisation and subtracts *"Operating lease liabilities
(567)"*. Putting the add-back into (c) as well would charge the rent twice.

> ### **(c) = capital expenditures + principal payments on financing obligations.**
> **FY2026: $1,178M. Five-year mean: $1,179M.**

**DIRECTION DISCLOSED, because the framework requires it.** Choosing $1,178M over the corpus
default of $3,631M is **the generous choice**. It raises FY2026 owner earnings by **$2,453M**.
It is also the *correct* choice on the filed decomposition, and the D&A end is carried in every
table below so that no later reader inverts it. **Windage: this run's one (c) adjustment is
spent in the COMPANY's favour, not the analyst's. There is no conservative windage anywhere in
this file, and the count is stated again at Q5.**

**THE THIRD READING, PUT ON THE PAGE RATHER THAN SUPPRESSED.** **[E2-23]**'s *"etc."* and *"its
unit volume"* support a reading in which **acquisitions are maintenance capital** at this filer,
because Salesforce has the **lowest R&D intensity in the competitor row (14.4%)** and every
product category beyond the original Sales and Service clouds was bought rather than built.
On that reading:

> five-year mean acquisition consideration **$8,282M/yr** against a five-year mean (OCF − SBC)
> of $7,179M → **owner earnings of −$1,103M. Negative.**

**It is not adopted, and here is the reason, stated so it can be argued with.** **[E2-23]** asks
what is required to *fully maintain* the existing position and unit volume, not what is required
to grow. The filed evidence is that the core maintains itself: **Agentforce Sales grew 8.5% and
Agentforce Service 8.4% in FY2026** without a purchase in either line. The acquisitions bought
**new revenue categories** — analytics, integration, messaging, data management — which is growth
capital. **[E2-60]**'s third dimension (*"its financial strength"*) is the part that does bite,
and it is carried to staying power below, where the debt-funded buyback belongs.

### OWNER EARNINGS — EVERY WINDOW PUBLISHED **[E4-38]**, BOTH ENDS AND THE JUDGED END

**Per year ($M), all from filed statements and footnotes.** OCF, SBC, D&A, capex and financing
obligations from the consolidated statements of cash flows; acquired-intangible amortisation
from the income-statement footnote in each year's 10-K.

| FY | OCF | SBC | OCF−SBC | D&A | acq. amort. | capex | fin. oblig. | **(c) judged** |
|---|---|---|---|---|---|---|---|---|
| 2017 | 2,162 | 820 | 1,342 | 632 | 228 | 464 | 98 | 562 |
| 2018 | 2,738 | 997 | 1,741 | 784 | 288 | 534 | 106 | 640 |
| 2019 | 3,398 | 1,283 | 2,115 | 982 | 447 | 595 | 131 | 726 |
| 2020 | 4,331 | 1,785 | 2,546 | 2,135 | 792 | 643 | 173 | 816 |
| 2021 | 4,801 | 2,190 | 2,611 | 2,846 | 1,121 | 860 | 103 | 963 |
| 2022 | 6,000 | 2,779 | 3,221 | 3,298 | 1,624 | 717 | 156 | 873 |
| 2023 | 7,111 | 3,279 | 3,832 | 3,786 | 1,951 | 798 | 419 | 1,217 |
| 2024 | 10,234 | 2,787 | 7,447 | 3,959 | 1,869 | 736 | 629 | 1,365 |
| 2025 | 13,092 | 3,183 | 9,909 | 3,477 | 1,651 | 658 | 603 | 1,261 |
| **2026** | **14,996** | **3,509** | **11,487** | **3,631** | **1,687** | **594** | **584** | **1,178** |

**Owner earnings over EIGHT windows and FOUR (c) constructions — 32 constructions, plus TTM.**
Yields are on the hand-built market cap of **$213,346M** (823.0M cover-page shares × $259.23).

| window | **(c)=capex** *[most generous]* | **(c)=capex+fin** *[JUDGED]* | (c)=D&A less acq. amort. | (c)=total D&A *[corpus default]* |
|---|---|---|---|---|
| 3yr FY2024-26 | 8,952 · 4.20% | **8,346 · 3.91%** | 7,661 · 3.59% | 5,925 · 2.78% |
| 4yr FY2023-26 | 7,472 · 3.50% | **6,914 · 3.24%** | 6,245 · 2.93% | 4,456 · 2.09% |
| **5yr FY2022-26 — the corpus default [E2-42]** | 6,479 · 3.04% | **6,000 · 2.81%** | 5,305 · 2.49% | 3,549 · 1.66% |
| 6yr FY2021-26 | 5,691 · 2.67% | **5,275 · 2.47%** | 4,569 · 2.14% | 2,918 · 1.37% |
| 7yr FY2020-26 | 5,150 · 2.41% | **4,769 · 2.24%** | 4,088 · 1.92% | 2,560 · 1.20% |
| 8yr FY2019-26 | 4,696 · 2.20% | **4,346 · 2.04%** | 3,774 · 1.77% | 2,382 · 1.12% |
| 9yr FY2018-26 | 4,308 · 2.02% | **3,986 · 1.87%** | 3,493 · 1.64% | 2,223 · 1.04% |
| 10yr FY2017-26 | 3,965 · 1.86% | **3,665 · 1.72%** | 3,238 · 1.52% | 2,072 · 0.97% |
| FY2026 alone | 10,893 · 5.11% | **10,309 · 4.83%** | 9,543 · 4.47% | 7,856 · 3.68% |
| **TTM to 2026-07-31** | 11,489 · 5.39% | **10,919 · 5.12%** | 10,158 · 4.76% | 8,163 · 3.83% |

TTM is FY2026 + H1 FY2027 − H1 FY2026: OCF $15,750M, SBC $3,665M, D&A $3,922M, acquired-intangible
amortisation $1,995M, capex $596M.

**THE SPREAD CAVEAT WAS LIVE AND IT FIRED — a ninth consecutive time.**

- **Published:** `spread 1.522`, from `oe_bottom_m 3549` to `oe_top_m 8952` — **four
  constructions**, and the "band" is in fact the 5-year D&A end against the 3-year capex end.
- **Rebuilt:** the true range across eight windows and four (c) ends is **$2,072M to $8,952M —
  a width of 4.32x**, against a published 2.52x on the two cells actually shown and a `spread`
  cell of 1.52. Including the TTM construction the top is $11,489M and the width is **5.54x.**
- **The published row could not see this** because it never built a window longer than five
  years and never built the two middle (c) constructions at all.

**IS THAT RANGE TOO WIDE TO REACH A CONCLUSION [E4-25]? No — and the reason matters.** A 4.3x
width would normally close the file. Here the width is **not dispersion and not a distorted
year**; it is a **level shift**, and it is the *good* kind. The screen row flagged it correctly:
`level_shift 2.70  STEP UP - normalize down [E4-41]`. GAAP operating margin went **2.1% (FY2022)
→ 20.1% (FY2026)** after a 10% workforce reduction, and every window that reaches back before
FY2024 is averaging a company that no longer exists. **[E3-55]** is the scope: the spread measures
uncertainty about the *level*, and here the mechanism of the level change is known, disclosed and
completed. So the range is carried in full, and the run does **not** close on width — it closes,
if it closes, on the floor.

**[E4-41] NORMALISED DOWN, as the rule requires.** The favourable exogenous break in the window
is named and removed: **FY2026 net income of $7,457M includes $1,017M of gains on strategic
investments**, and Q2 FY2027 alone carried **$2,613M** of such gains against $2,331M of operating
income. Those are marks on a venture portfolio, not earnings from selling software. **They are
already outside owner earnings** — the cash-flow statement backs them out of OCF at the
*"(Gains) losses on strategic investments, net"* line — so no further adjustment is made, but any
reader working from net income must remove them.

**Stock compensation subtracted in full [E5-06], and the measure is stated [E3-70].** $3,509M in
FY2026 is subtracted at 100%. **[E3-70]** says the reported charge is the **floor**, not the
measure, where SBC is material. It is material here in dollars and the floor is understated for
a specific, filed reason: **Informatica's assumed awards carried a $330M fair value of which
$294M was allocated to future services** and will be expensed later; Slack's equivalent figure
was **$1.5bn of $1.7bn**. Purchase accounting routes a slice of the acquisition price through
future SBC. No upward adjustment is made — that would be a second windage — but the direction is
recorded.

**SBC ÷ OCF, the comparable the brief asked for, computed to the dollar against the filed
cash-flow statement** (numerator: the SBC add-back line; denominator: *"Net cash provided by
operating activities"*):

| FY | SBC $M | OCF $M | **SBC ÷ OCF** |
|---|---|---|---|
| 2020 | 1,785 | 4,331 | 41.2% |
| 2021 | 2,190 | 4,801 | 45.6% |
| 2022 | 2,779 | 6,000 | 46.3% |
| 2023 | 3,279 | 7,111 | 46.1% |
| 2024 | 2,787 | 10,234 | **27.2%** |
| 2025 | 3,183 | 13,092 | 24.3% |
| **2026** | **3,509** | **14,996** | **23.4%** |

Against the comparable set: **CrowdStrike 68.0%** (which contributed to closing that file),
Tenable 71.9%, Rapid7 67.8%, HubSpot 69.4%, Workday 55.3%, ServiceNow 35.9%, Certara 34.3%,
**Qualys 24.9%** (explicitly cleared of the charge), Adobe 19.4%, Oracle 15.0%, **Microsoft 6.8%**.

**The brief's prior is CONFIRMED on the ratio and CONFIRMED on the dollars, and the ratio wins.**
23.4% is better than Qualys's cleared 24.9% and less than a third of CrowdStrike's. The trend is
the strongest single data point in the file: **46.3% → 23.4% in four years, halved.** The dollars
are indeed large — $3,509M a year, $22.6bn over ten years — but the brief's framing that *"the
dollar amount matters more than the ratio when the buyback exists to offset it"* is answered at
Q3, where the buyback arithmetic was done, not here. **On the [E5-06] test as this framework runs
it, Salesforce passes comfortably.**

### GREAT, GOOD, OR GRUESOME? **[E4-20]**

- [ ] great — high return, rising, little capital needed
- [x] **good** — attractive return, earned also on deposits that are added
- [ ] gruesome — grows, eats capital, earns little

**The evidence, computed the way the ORCL run computed it.**

| | capital deployed $M | owner earnings (c=capex) then → now | increment | **return on deployed capital** |
|---|---|---|---|---|
| FY2022–FY2026 | **47,306** (acquisitions 41,412 + capex/financing obligations 5,894) | 1,751 → 10,893 | +9,142 | **19.3%** |
| FY2017–FY2026 | **79,033** (acquisitions 69,432 + capex/financing obligations 9,601) | 878 → 10,893 | +10,015 | **12.7%** |

**This is the finding I least expected and it must be stated first because it runs against the
prior [E4-26].** Salesforce deployed **$79bn over ten years** — 1.75x its own cumulative owner
earnings at the most generous construction — and owner earnings rose by **$10.0bn**. That is
**12.7% pre-tax on everything deployed over a decade**, and **19.3%** over five. **[E5-40]** puts
*"quite satisfactory"* at about 12% on retained capital. **[E4-43]** is explicit that the *good*
class **passes**: *"nothing shabby about earning $82 million pre-tax on $400 million of net
tangible assets."*

**Three honest qualifications, none of which moves it to gruesome.**
1. **Attribution is not provable from the filings.** Salesforce reports **one segment**. Most of
   the owner-earnings increment came from the margin repair — a headcount reduction — not from
   the acquisitions. The 12.7% is what the consolidated numbers show; **[E2-56]** warns that a
   marvellous core camouflages allocation failures elsewhere, and with one segment the
   camouflage cannot be lifted.
2. **The three filed pro formas each point the other way** (Q3): Tableau turned a reported
   profit into a pro-forma loss, Slack cut combined net income 22%, Informatica 1%.
3. **It is not great.** *The great one "pays an extraordinarily high interest rate that will rise
   as the years pass."* Salesforce's return on deployed capital **fell** from 19.3% over five
   years to 12.7% over ten because the ten-year figure includes Tableau and Slack. And the rate
   is not rising: **the company's own FY2027 guidance is a GAAP operating margin of 20.1% — flat
   to FY2026 — with operating cash flow growing 4–5% against revenue of 11–12%.**

**GOOD. It passes Q4's business test, and it ranks below great at Q5. That is all [E4-43] permits
this finding to mean.**

### STAYING POWER — SCORE ALL THREE **[E5-11]**

**(1) A large and reliable stream of earnings — PASSES, and it is the strongest in the file.**
94.9% of revenue is subscription. **$24,317M of cash was collected in advance** at FY2026 and
sits as unearned revenue. **Remaining performance obligation is $72.4bn**, up 14.2%, of which
cRPO $35.1bn. Operating cash flow has risen every single year for a decade, including 2020.
**[E5-37]** says the metric set is chosen by business type first; for a prepaid subscription
business the right metric is contracted backlog, and it is large and growing.

**(2) Massive liquid assets — PASSES, WEAKENED, AND THE DIRECTION IS WRONG.** Cash and
marketable securities were **$14,032M (FY2025) → $9,565M (FY2026) → $11,403M (2026-07-31)**
against **$39,500M of debt principal**. Net debt is roughly **$28.1bn**, against a position that
was net *cash* eighteen months ago. The absolute liquidity is ample against a $594M capex bill
and no near-term maturity; it is no longer "massive" against the balance sheet.

**(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — PASSES. This is the one that usually kills and
it does not kill here.**

| requirement | amount | when |
|---|---|---|
| Debt, current, at 2026-07-31 | **$0** | — |
| First maturities: March 2028 $3,500M · April 2028 $1,500M · July 2028 $1,000M | $6,000M | FY2029 |
| 2026 Term Loan | $6,000M | March 2031 |
| Interest, run rate (Q2 FY2027 expense $473M) | ~$1,900M/yr | ongoing, rising |
| Dividend | ~$1,500M/yr | discretionary |
| Operating lease liabilities | $2,455M | laddered |
| ASR final settlement | **share delivery, cash already paid** | Q3 FY2027 |
| Contentful and Fin acquisitions | **terms not in any filing read** | Q3 FY2027 |

Against operating cash flow of roughly **$15bn a year**. **[E2-54]**'s coverage test — *"all
interest, both payable and accrued, comfortably met out of current cash flow net of ample
capital expenditures"* — reads **$14,996M − $1,178M = $13,818M against ~$1,900M of interest,
7.3x**, and it passes on the judged (c) as well as the generous one. **This is not the Oracle
shape**, where the same test came out negative.

**[E3-52] — read the terms, not just the quantity.** The largest liability in this business is
**unearned revenue: $18,787M at 2026-07-31.** It is customer-prepaid, carries no covenants and no
due dates, and is discharged by delivering software rather than by paying cash. That is precisely
the *"liabilities without covenants or due dates … the benefit of debt … with none of its
drawbacks"* class. The $39.5bn of senior notes is the opposite class, and the filing confirms
*"The Company was in compliance with all debt covenants as of July 31, 2026."*

**[E5-39] — the kindness of strangers, and this is where the honest scoring hurts.** *"We will
never be dependent on the kindness of strangers … cash is a lot like oxygen."* Salesforce is not
**dependent** on lenders for operations — the business funds itself several times over. But in
March 2026 it **chose** to borrow $31bn from strangers to buy its own stock, converting a net-cash
balance sheet into a $28bn net-debt one, and **$22.9bn of repurchase authorisation remains**. The
strength that **[E2-64]** describes as an offensive asset — *"the most attractive opportunities
may present themselves at a time when credit is extremely expensive"* — has been spent on the
register rather than kept for the opportunity. **Strength (3) passes on the facts and the
direction is recorded against it.**

**Leverage, named and quantified [E4-16, E3-29]** — *there is no ratio ceiling in this framework
and the corpus supplies none*: debt principal $39,500M; debt ÷ OCF **2.6x**; debt ÷ equity
**1.03x**; **tangible book equity −$27,014M**; interest coverage on OCF-less-(c) **7.3x**;
weighted coupon on the March 2026 notes running **4.50%–6.70%**, with the long tranches at 6.40%,
6.55% and 6.70%.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**

**Model exposure, not experience [E4-40].** Salesforce's loss history is benign — it has never had
a down year of revenue. That history is *"not only useless, but actually dangerous"* as a guide.
What follows comes from what the filing shows the business is **exposed** to.

**THE MECHANISM: the seat stops being the right unit, and Salesforce cannot take price to
compensate.** Salesforce sells per-user subscriptions to a system of record. Its filed position
is that (a) *"Pricing was not a significant driver of the increase in revenues"* — six years
running, so growth is seats — and (b) *"the increased prevalence of consumption-based pricing
models"* is named in its own risk factors as a driver of attrition, and *"the markets and
monetization strategies for certain offerings, including Agentforce and Data 360, remain
relatively new and uncertain."* If AI agents do the work that sales representatives and service
agents do today, the customer's seat count falls **while its usage of Salesforce rises**, and a
company with no demonstrated pricing power cannot convert the second into the first.

**QUANTIFIED FROM FILED FIGURES.** Base case, FY2026 as filed:

- Subscription revenue **$39,388M**; attrition ~**8%** → roughly **$3,151M of annualised contract
  value lost every year** before any growth.
- Subscription revenue grew **$3,709M**, so gross new business was on the order of **$6,860M**,
  bought with **$14,345M** of sales and marketing.

**The scenario, and every input is a move smaller than one already observed in this window:**

- Attrition rises **8% → 12%**. That is a 4-point move; the disclosed metric already moved
  2.5 points (7.0–7.5% → ~8%) between FY2022 and FY2024 on a perimeter change alone. Annual
  loss becomes **$4,727M**, up $1,576M.
- Gross new business held flat at $6,860M → net subscription growth falls from $3,709M to
  **$2,133M**, i.e. **growth of 5.4% instead of 9.4%.**
- Sales and marketing rises 3 points of revenue to hold that gross figure — the **[E2-27]**
  mechanism exactly, *"viewed individually, each company's capital investment decision appeared
  cost-effective and rational; viewed collectively, the decisions neutralized each other"* —
  costing **$1,246M**. Operating income falls from $8,331M to roughly **$7,085M.**
- **The outcome is not insolvency. It is a business growing 5% with a flat margin, at a price
  that needs 4.9%–7.2% of perpetual owner-earnings growth to pay 10%.** Interest coverage would
  still be about 6x. Nothing defaults. **The equity simply is not worth $259.**

**LIKELIHOOD: a real possibility.** Not *likely*: the core lines still grew 8.4–8.5% in FY2026 and
92% of contract value renews. Not a *low-level possibility* either: the company's own FY2027
guidance already has GAAP operating margin flat and operating cash flow growing 4–5%, which is
the first half of this scenario arriving on schedule.

**THE SECOND MECHANISM, quantified and then dismissed as a death.** Goodwill is **$59,250M
against $38,378M of equity, in one reporting unit**. A 25% impairment is **$14.8bn** and takes
book equity to **$23.6bn**. It would be the largest write-off in the company's history and it
would change **nothing** about the cash: the notes are unsecured, the covenants are complied
with, and impairment is a non-cash charge. **Recorded as an accounting event, not a death.**

**THE THIRD MECHANISM, and the one a bear should actually lead with — Microsoft.** Dynamics grew
18% in FY2026 from a $9,006M blended base while Salesforce grew 8.4%, and **Microsoft spends 8.0%
of revenue on selling against Salesforce's 34.5%.** If Microsoft chooses to put Dynamics into
enterprise agreements at an incremental price Salesforce cannot match, 8% attrition becomes 15%
and no amount of sales spending outruns it. **[E3-61]** is the honest limit: the competitor row
shows position, and this is **conduct** — *"I think you'd have to know the people involved"* —
and Microsoft has had this option for fifteen years without exercising it at that intensity.
**Likelihood: a real possibility.**

**THE BEAR CASE STATED SO ITS HOLDERS WOULD ACCEPT IT [E4-51], AND THEN THE OTHER SIDE AT FULL
STRENGTH.** The case against the business is above and it is serious. **The case for it, which
Q4 exists to test, is this**: Salesforce collected **$24.3bn of cash before delivering anything**,
holds **$72.4bn of contracted revenue**, generates **$15.0bn of operating cash on $594M of
capex**, renews **92% of contract value every year for a decade**, has an interest bill covered
7.3x, has no debt due for eighteen months, and has been forecast to be destroyed by open source,
by Microsoft, and now by AI in every one of the last fifteen years while compounding revenue at
**14.3% over five years**. **Q4 asks whether it will survive. On the filed evidence the answer is
emphatically yes.**

- **VERDICT: [x] IN** · **GOOD**, not great · 3 of 3 on **[E5-11]**, with strength (2) weakening
  and the direction recorded · named death is a **margin-and-growth compression, a real
  possibility**, not a solvency event.

---
⛔ **Q1–Q4 each show IN. Q5 opens.**

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**Sovereign: 5.24% USD, 2026-09-04, US Treasury daily par yield curve, 30-year, from the issuing
authority.** The bare rate. **No per-name risk premium is added [E3-42]** — *"mathematical
gibberish."*

**Market cap: $213,346M** = **823.0M** cover-page shares (10-Q, accession 0001108524-26-000190,
*"As of August 20, 2026"*) × **$259.23** (2026-09-04, aggregator, live quote only, flagged).
**Not** run.py's 956.0M weighted average, which overstates the cap by 16.2%.

### THE FLOOR, BEFORE THE RANKING **[E4-28, E3-13]**

*"that's the figure we quit on … that's true whether short rates are 6 percent or whether short
rates are 1 percent."*

**Honest pre-tax expectancy = the owner-earnings yield the buyer actually receives, plus the
growth in that stream.** The growth input is not mine: it is **the company's own FY2027 guidance
of 4–5% operating-cash-flow growth** (8-K accession 0001108524-26-000187, 2026-08-26), taken at
its midpoint of 4.5%.

| construction, judged (c) | owner-earnings yield | **+ 4.5% guided growth = honest expectancy** | vs the ~10% floor |
|---|---|---|---|
| 10-year window | 1.72% | **6.22%** | **fails** |
| **5-year window — the corpus default [E2-42]** | **2.81%** | **7.31%** | **fails** |
| 3-year window | 3.91% | **8.41%** | **fails** |
| FY2026 alone | 4.83% | 9.33% | **fails** |
| **TTM to 2026-07-31 — the single most generous number in this file** | **5.12%** | **9.62%** | **fails** |

**Every construction fails the floor. The most generous one, built on a single trailing twelve
months at the most generous (c) this run could justify, reaches 9.62%.**

**And the growth input is charged twice in the company's favour to get even that.** The 4.5% is
guided while revenue grows 11–12% *including acquisitions*; sustaining it requires the
**$8.3bn a year of acquisition spending that (c) deliberately excludes.** A reader who puts that
spending back into (c) gets **negative owner earnings** and no expectancy at all.

> ### **FLOOR VERDICT: below ~10% on every construction. The name is QUIT ON, not ranked.**
> **[E4-28]** — *"we don't want to buy equities where our real expectancy is below 10 percent."*

### 1. THE YIELD

- owner earnings **$6,000M** (5-year window, judged (c), the corpus default window) ÷ market cap
  **$213,346M** = **2.81%** · sovereign **5.24%**
- full range across all constructions: **0.97% to 5.39%**
- **Not one of the 32 window-by-(c) constructions, nor the TTM construction, yields as much as
  the 30-year Treasury.** The best is 5.12% against 5.24% — **0.12 points short of the risk-free
  rate before a single risk is priced.**

### 2. WHAT THE PRICE ALREADY ASSUMES

| construction | perpetual owner-earnings growth needed to pay the ~10% floor |
|---|---|
| 10-year | **8.28%** |
| **5-year (corpus default)** | **7.19%** |
| 3-year | **6.09%** |
| TTM | **4.88%** |

**What the business has actually done:** revenue growth **24.7% → 18.3% → 11.2% → 8.7% → 9.6%**,
of which FY2026's 9.6% is **8.4% on the filed Informatica pro forma** and **8.5% backing the
disclosed $399M contribution out of the reported line**. FY2027 guidance is 11–12% headline of
which *"slightly above 3pts"* is Informatica, i.e. **~8% organic** — and **operating cash flow is
guided to grow 4–5%.**

**[E4-35] prices the belief the price requires**: *"fewer than 10 of the 200 most profitable
companies in 2000 will attain 15% annual growth in earnings-per-share over the next 20 years."*
The corpus default window needs **7.19% forever**. That is inside the base rate — it is not a
15% claim — which is precisely why this name is a **near miss rather than an absurdity**, and why
the file closes on the floor rather than on ridicule.

**[E2-63] — the revenue × margin decomposition, and the KLAC finding replicates.** GAAP operating
margin went 2.1% (FY2022) → 20.1% (FY2026), which is where almost all of the owner-earnings
increment came from. **The company's own FY2027 guidance puts GAAP operating margin at 20.1% —
exactly flat — and non-GAAP at 34.3% against 34.1%, up 0.2 points.** **The margin lever is spent,
and Salesforce says so in its own guidance.** What is left is revenue growth of ~8% organic
converting into operating-cash-flow growth of 4–5%. **[E2-63]**'s ceiling clause governs: most
operating businesses are capped *"unless more capital is continuously invested"* — and here the
capital that would be invested is acquisition capital that this run has already excluded from (c).

### 3. WHAT YOU ARE PAID

| construction | points over the sovereign |
|---|---|
| 10-year, judged (c) | **−3.52** |
| 5-year, judged (c) — corpus default | **−2.43** |
| 3-year, judged (c) | **−1.33** |
| FY2026 alone | −0.41 |
| TTM to 2026-07-31 | **−0.12** |
| widest, across all 32 constructions | **−4.27 to −0.12** |

**You are paid nothing over the sovereign at any construction. You are paid less than the
sovereign at every one.**

### WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE **[E3-42]**

- Sovereign used: **5.24% — the bare rate, no per-name premium added.**
- Certainty was handled twice and neither place is the rate: at the **understanding gate**, where
  Q1 passed narrowly and recorded the metering-unit doubt; and in the **discount to value
  demanded at the end**, which is never reached because the floor disposes of the name first.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**

Judged owner earnings capitalised at the **10% floor less the company's guided 4.5% growth**
(5.5%), on 823.0M shares:

| construction | value $M | **per share** |
|---|---|---|
| 10-year window | 66,636 | **~$81** |
| **5-year window — corpus default** | 109,098 | **~$133** |
| 3-year window | 151,752 | **~$184** |
| TTM to 2026-07-31 | 198,527 | **~$241** |

- **conservative ≈ $80** · **optimistic ≈ $240** · **centre ≈ $150** · **current price $259.23**
  (2026-09-04)

Round numbers, as the rule requires. **The price is above the entire judged range**, including
the construction built from the single best trailing twelve months at the most generous
maintenance-capex guess this file could defend.

### WHICH BAR **[E4-01, E4-11]**

- [x] **Screamer test [E4-01].** *"Take the conservative end of the range and ask whether the
      price already clears it. No margin is added on top."* This is also **[E5-34]**'s routine
      verbatim: *"we will buy the stock … if it sells at a reasonable price in relation to **the
      bottom boundary of our estimate**."* Bottom boundary: **~$81.** Price: **$259.23.**
      **Outcome: price above the whole range → no.**
- [ ] Normal method [E4-11] — not used; no end margin is applied, because none is needed.

**WINDAGE COUNT: ZERO conservative adjustments, and ONE adjustment in the company's favour.**
The (c) judgment took $1,178M rather than the corpus default of $3,631M, raising owner earnings
by $2,453M a year; the growth input is the company's own guidance rather than the run's estimate;
the sovereign carries no per-name premium; no end margin is applied. **Conservatism was not spent
once — it was not spent at all, and the name still fails.** That is stated so no reader can
attribute this verdict to stacked windage **[E4-11, E4-48]**.

- **VERDICT: [ ] IN.** **NOT IN — quit on at the [E4-28] floor.** Ranking position: **not
  ranked.** Below roughly 10% honest expectancy a candidate is not ranked, it is quit on,
  whatever the sovereign is doing.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

*The name is not owned and is not being entered. Q6 is written as the pre-committed monitoring
register **[E1-02]** — "I believe in establishing yardsticks prior to the act" — so that a future
look is judged against yardsticks set today rather than against yardsticks chosen then.*

**Pre-committed, before entry:**

- **Thesis-confirming metric (would make me wrong to have quit):** **operating cash flow growth
  above 8% for two consecutive fiscal years** while GAAP operating margin holds at or above 20%.
  Guidance today is 4–5%. If OCF compounds at 8%+ while the margin holds, the TTM construction's
  5.12% yield plus 8% growth clears the floor and the file reopens on the arithmetic alone.
- **Thesis-breaking metric and its threshold:** the **disclosed attrition rate above 9%**, or any
  fiscal year in which the attrition disclosure is **dropped or replaced with words**. It has
  survived ten years and three years at "approximately eight percent"; a move to 9%+ on a
  perimeter that is not simultaneously widened would mean the switching-cost moat is going.
- **Second breaking metric:** **sales and marketing rising back above 37% of revenue.** The one
  genuinely improving line in this file is selling efficiency (47% → 34.5%); a reversal means the
  gross-new-business treadmill has steepened.
- **The price at which the arithmetic changes:** at the 5-year corpus-default construction the
  floor is cleared at roughly **$133**; on the 3-year construction at roughly **$184**. **A
  quotation below about $130 puts this name back on the page** at the corpus's own default window.
- **Next catalyst dates:** Q3 FY2027 results, late November 2026 — which will carry the **final
  ASR settlement** (the remaining ~20% of the $25bn programme) and the **first disclosure of
  terms for the Contentful and Fin acquisitions**, neither of which is in any filing read here.

**The sell rule [E2-28]** — two triggers, three hold conditions. Not owned, so recorded as the
standard that would apply:
- SELL if the market judges it more valuable than the underlying facts indicate — **this is the
  current condition**, on every construction in this file.
- SELL if funds are needed for something more undervalued or better understood — not engaged.
- HOLD while: return on equity capital satisfactory (**ten-year mean ROE 5.7%; five-year 6.5% —
  [E2-42]'s red light is on**) · management competent and honest (**Q3 found no disqualifier and
  one live capital-allocation flag**) · market does not overvalue (**fails**).
- *Price appreciation and holding period are explicitly rejected as reasons to sell.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring question:
*is this erosion an aberrational cycle, or has the business slipped in a way that permanently
reduces intrinsic business value?* **On today's evidence it is neither yet.** Attrition is flat
at ~8%, RPO grew 14.2%, and the core product lines grew 8.4–8.5%. What has changed is the
**growth rate**, from 24.7% to 8.4% in four years, and **[E4-32]**'s direction test reads flat to
narrowing. *"Those beliefs change quite gradually"* — this one has not finished changing, and the
counter-trigger **[E2-40]** is noted for the day it does: once the view crystallizes, delay is
the graver error.

**[E3-40] is the standing watch item.** *"Loss of focus is what most worries Charlie and me …
the management of a great company gets sidetracked and neglects its wonderful base business while
purchasing other businesses that are so-so or worse."* Ten years, $69.4bn, three filed pro formas
each showing the acquisition reducing combined net income. If a fourth large acquisition is
announced before the FY2030 targets are tested, that is the **[E4-24]** exit trigger, not an
engagement plan — the corpus rates its own record at persuading managements *"worse than poor."*

**Position size — a judgment, stated: ZERO.** The name is quit on at the floor **[E4-28]**, and
a live capital-allocation flag would size it down even if it had cleared **[E4-13]**.

- **VERDICT: [x] UNKNOWABLE is NOT the answer here, and neither is UNRESEARCHED. Q6 is [x] IN**
  as a monitoring register: the metrics, thresholds, price and catalyst date are all named and
  all obtainable from the next 10-Q.

---
## SELF-AUDIT

- [x] Questions answered in order; no verdict skipped. **Q1 IN → Q2 IN → Q3 IN → Q4 IN → Q5 NOT
      IN (quit on at the floor) → Q6 written as a monitoring register.**
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q2 is explicitly
      **not** PROVISIONAL: eight companies in the row and four unfillable cells named.
- [x] Every UNRESEARCHED verdict names the artifact — **there are none.** The one item that would
      have been UNRESEARCHED (the FY2026 cash-tax fall) was resolved inside this run by reading
      the named document, the ASU 2023-09 disaggregation in the FY2026 income-tax note.
- [x] Every UNKNOWABLE states what cannot be known. **One is recorded, at Q2:** Microsoft's
      Dynamics 365 revenue cannot be isolated from Note 18's blended cloud-plus-on-premises line,
      and **no document exists that would resolve it** — Microsoft states segment amortisation is
      *"impracticable"* to identify and does not allocate assets to segments.
- [x] Step 0: the filing was read — 10-K accession **0001108524-26-000060** (filed 2026-03-02) and
      10-Q accession **0001108524-26-000190** (filed 2026-08-27) — MD&A, cash-flow statement
      including detail lines, and footnotes. **Six figures cross-checked against the filed
      statements**, listed at Step 0.
- [x] Owner earnings on a multi-year mean; **eight windows published**; capex band disclosed as a
      judgment with **four (c) constructions** and the adopted one argued from the filed
      decomposition.
- [x] Competitor row filled — **eight companies**, plus a marked addendum completing the four
      cells the first pass left open.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 2026-09-04.
- [x] Value stated as a round-number range: **~$80 to ~$240, centre ~$150.**
- [x] One bar chosen — the **screamer test [E4-01]** — not both. **Windage count: zero
      conservative adjustments; one adjustment in the company's favour, disclosed.**
- [x] Prices dated; the aggregator was used for the live quote only and is flagged.
- [x] Run committed to git, section by section, under the write-early protocol.

---
## REGISTER

- **Verdict: [x] IN at Q1–Q4 (about the business) · NOT IN at Q5 (about the price).** The
  business clears all four business gates. The name is **quit on at the [E4-28] floor**, not
  ranked, and it is not an OUT about the business.
- **One line:** *A narrow switching-cost moat with no pricing power, a good — not great —
  business that turned $79bn of deployed capital into $10bn of owner earnings over a decade, run
  by managers with a clean control record who are paid on numbers that appear zero times in any
  filed report, priced at $259 against a judged value of roughly $80 to $240 and an honest
  expectancy of 6.2%–9.6% against a 10% floor.*
- **The seventeenth name in this queue to clear all four business gates and fail on price.**

### THE FOUR-VERDICT LINE

| | verdict | one line |
|---|---|---|
| **Q1** | **IN** (narrow) | Seats × price × renewal, less an 8% leak, less the cost of replacing it. Every term is a filed number. |
| **Q2** | **IN** — class **NARROW**, direction **flat to narrowing** | 92% of contract value renews; price has contributed nothing for six straight years by the company's own MD&A. |
| **Q3** | **IN** — no disqualifier found; **live capital-allocation flag**; **[E4-52]** convergence | Clean controls, 24-year auditor, no restatement. Four flags fire, and they point at one scoreboard no auditor signs. |
| **Q4** | **IN** — **GOOD**, 3 of 3 on **[E5-11]** | 12.7% pre-tax on $79bn deployed over ten years; $72.4bn of contracted revenue; interest covered 7.3x. |
| **Q5** | **NOT IN — quit on at the floor** | Honest expectancy 6.22%–9.62% against ~10%. No construction out of 33 yields as much as the 5.24% sovereign. |
| **Q6** | **IN** as a monitoring register | Reopens below roughly $130, or on two years of 8%+ OCF growth with the margin held. |

---
## DEFECTS FOUND — IN THE TOOLING AND IN THE BRIEF
*Operator rule 8: tools fetch and compute and are forbidden to conclude. Every item below is a
place where a tool concluded something and was wrong, or where a prompt-to-read did not fire.*

### A. TOOLING

**A1 — `tools/run.py` uses a WEIGHTED AVERAGE share count and the market cap is 16.2% too high.
This is the largest single error in the row and it is not a rounding matter.**
run.py reported **956.0M shares** and **$247.82B** of market cap; the cover page of the latest
periodic filing says **823 million** (10-Q accession 0001108524-26-000190, *"As of August 20,
2026"*). The hand-built cap is **$213,346M**. run.py prints its own warning — *"a WEIGHTED
AVERAGE, not a cover-page count"* — and then computes the yield from it anyway, so every
owner-earnings yield it printed for CRM is **16.2% too low**. **The screen path got this right**
(`cap_m 213659` reconciles to 823M × ~$259.6), so **the two owner-earnings paths disagree on the
denominator as well as on (c)**. That is the CERT finding generalising: a fix applied on one path
and not the other is worse than no fix, because it looks applied.
**Suggested fix:** run.py should read `dei:EntityCommonStockSharesOutstanding` from the newest
periodic filing and refuse to print a yield when only a weighted average resolves.

**A2 — `da_annual()`'s max-across-elements rule is CORRECT here and would have been WRONG under
the CERT-style patch.** Salesforce tags both `DepreciationDepletionAndAmortization` ($1,200M,
FY2026) and `DepreciationAndAmortization` ($3,631M). The first is **fixed-asset depreciation
only**; the second is the cash-flow-statement total. Taking the max resolves to $3,631M, which is
the right total. **The brief's warning to print the raw series and eyeball it was followed and it
paid**: the series has a real 2.17x discontinuity at FY2020 (982 → 2,135), which is **not** a
tag-semantics artifact — it is ASC 842 pulling right-of-use amortisation into the caption plus
Tableau and MuleSoft amortisation arriving. Recorded because the CERT defect class would have
flagged it as broken and it is not.

**A3 — `best_year_dep 0.256` is real, not an artifact, and it is the wrong shape of finding.**
The window's dependence on a single best year is genuine, but the diagnosis is a **level shift**,
not single-year dependence: GAAP operating margin went 2.1% → 20.1% between FY2022 and FY2026 and
stayed. `level_shift 2.70 STEP UP` caught it correctly. **The two flags disagreed and the
level-shift one was right.**

**A4 — `acquisition_flag()` understates the perimeter by $14,013M, or 51%, and it understates the
percentage of cap as well.** The flag reads the investing line only and reported
**$27,399M, 13% of cap**. Total consideration from the business-combination notes over the same
five years is **$41,412M, 19.4% of the hand-built cap**. The gap is stock consideration, which
never touches investing: Slack's **$11,064M** of common stock, and — across the ten-year window —
Tableau's **$14,552M against $1M of cash**. Ten-year total consideration is **$69,432M** against
a ten-year investing line of $29,624M. **The CERT finding replicates at 100x the scale.**
**Suggested fix:** where `PaymentsToAcquireBusinessesNetOfCashAcquired` is non-trivial, the flag
should also read `StockIssuedDuringPeriodValueAcquisitions` and print both, or print a
prompt-to-read naming the business-combination note. It must not report a percentage of cap from
the cash line alone.

**A5 — the `spread` cell is still not a capex band, a ninth consecutive time.** `spread 1.522`
with `oe_bottom_m 3549` / `oe_top_m 8952` is the **5-year D&A end against the 3-year capex end** —
two windows and two different (c) ends, mixed. The true range across eight windows and four (c)
constructions is **$2,072M to $8,952M, 4.32x**, or **5.54x** including the TTM construction.

**A6 — `PaymentsToAcquirePropertyPlantAndEquipment` alone understates capital consumed by half at
this filer, and no existing flag catches it.** Salesforce's capex line is $594M against
fixed-asset depreciation of $1,200M. The missing cash is **"Principal payments on financing
obligations" of $584M, sitting in the FINANCING section** — build-to-suit and finance-lease
repayments on data centres and offices. `lease_capex_flag()` reads `FINLEASE_FLAG_TAGS` and did
not fire. **Suggested fix:** add `RepaymentsOfLongTermCapitalLeaseObligations` /
`FinanceLeasePrincipalPayments` to the prompt-to-read set whenever depreciation exceeds cash
capex by more than ~1.5x. The generalisable rule this run used: **when depreciation is far above
capex, look in financing before concluding the filer is under-investing.**

**A7 — the capitalised-software port of 2026-09-07 does not bite here, and that is worth
recording rather than assuming.** All four `SOFTWARE_CAP` tags —
`PaymentsToDevelopSoftware`, `PaymentsForSoftware`, `PaymentsToAcquireSoftware`,
`PaymentsForCapitalizedInternalUseSoftware` — are **absent from Salesforce's XBRL in all ten
years**. The cash-flow statement carries a single caption, *"Capital expenditures"*, throughout.
Salesforce **does** capitalise internal-use software, and said so through FY2020 (*"we believe we
have larger capitalized costs as compared to traditional enterprise software companies"*, with
$64.6M of amortisation disclosed in FY2017) — but **the policy note was dropped after FY2020 and
no amount has been disclosed since.** So the spend is inside `capex` and cannot be separated.
**This is UNKNOWABLE, not UNRESEARCHED** — there is no document that would resolve it.

### B. THE BRIEF

**B1 — correction 1 does not apply to this filer, and checking it was still right.** Salesforce
capitalises software but reports no separate line and has disclosed no amount since FY2020. The
capitalised-software fix is inert here; the (c) question turned on financing obligations instead.

**B2 — the SBC prior is CONFIRMED on the ratio and the framing about dollars is answered
elsewhere.** SBC ÷ OCF is **23.4%**, below Qualys's cleared 24.9% and roughly a third of
CrowdStrike's 68.0%, and it **halved in four years** from 46.3%. The dollars are large ($3,509M)
but the buyback arithmetic that the brief attached to them belongs at Q3, where it was done, not
inside the owner-earnings subtraction.

**B3 — the attrition-withdrawal prior is REFUTED, for the second consecutive run.** The metric was
never withdrawn; it appears in all ten 10-Ks and the FY2026 one still carries a number. **And the
one change that did occur is the candor case, not the flag**: the FY2023 10-K pre-announced a
year ahead that adding MuleSoft and Tableau *"would slightly increase our attrition rate"*, and it
did. **[E2-49]** does not fire. The real finding is softer and had to be built by hand: the
perimeter moved in nine of ten years and now excludes *"current year acquisitions"* as a
self-renewing category.

**B4 — the Q2 prior is CONFIRMED in shape and the outcome is the opposite of CERT's.** Criterion
(2) is genuinely contestable — Salesforce's own Item 1 names free substitutes, in-house build and
AI-native displacement, exactly the language that closed CERT — but the **revealed behaviour
contradicts the boilerplate**: 92% of contract value renews, for a decade, and RPO grew 14.2%.
NARROW, not OUT.

**B5 — "acquisitions are small against the cap" is wrong, and it is wrong by construction.**
See A4. The true five-year perimeter is 19.4% of cap and the ten-year total consideration is
$69,432M — **1.75x cumulative ten-year owner earnings at the most generous construction.**

**B6 — the AVGO/CVX inversion applies but resolves to a THIRD number, not to either end.**
The brief said not to default. Following that instruction, the D&A line decomposed to 46.5%
acquisition amortisation (excluded — R&D above the OCF line already renews it), 20.5%
right-of-use amortisation (excluded — already inside OCF as rent), and 33.0% fixed-asset
depreciation (included). The adopted (c) is **capex + financing-obligation principal = $1,178M**,
which independently equals the $1,200M of fixed-asset depreciation. **Neither the capex end nor
the D&A end was the right answer.**

**B7 — the growth prior is CONFIRMED and the margin prior is CONFIRMED, and the second one is the
Q5 finding.** Filed organic growth is **8.4–8.5%** on two independent constructions, against the
row's `growth_required 8.34%`. And **[E2-63]**'s decomposition leaves the margin lever spent by
the company's own admission: **FY2027 guidance is a GAAP operating margin of 20.1%, exactly flat
to FY2026, with operating cash flow growing 4–5% against revenue of 11–12%.** The KLAC finding
replicates.

**B8 — the [E4-30]/[E4-52] pay prior is CONFIRMED, and it is worse than Broadcom's.** At Broadcom
one metric appeared zero times in any filed report. At Salesforce the string **"non-GAAP" appears
zero times in ten consecutive 10-Ks and in every recent 10-Q**, yet 50% of the CEO's bonus and
half the PRSUs vest on non-GAAP measures; **"Agentforce & Data 360 ARR"** — 33% of the FY2026
equity grant, which vested at **200%** — appears **zero times in any filed report**; and the only
clean GAAP metric in the plan, **operating cash flow, was dropped for FY2026.**

**B9 — one prior in the brief was mis-specified and it matters.** The brief asked whether the
buyback "only offsets dilution." The answer is **phase-dependent and blending the phases gives
the wrong answer either way**: FY2017–FY2022 was pure dilution with no buyback at all
(+39% shares, zero repurchases); FY2023–FY2026 was overwhelmingly a payroll expense settled in
cash (**$782M of cash per million net diluted shares retired**); and H1 FY2027 was a genuine
11.4% reduction **paid for with $31bn of 4.2%–6.7% debt.** A single verdict on "the buyback"
misdescribes all three.
