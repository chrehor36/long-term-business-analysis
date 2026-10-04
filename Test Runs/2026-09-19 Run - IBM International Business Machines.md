# Company Run — International Business Machines Corporation (IBM) — 2026-09-19
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
- rate **5.34 %** · date **2026-09-18** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year**, struck fresh this run by `python tools/sources.py` (not inherited
  from any brief; the RESUME STATE warns that the rate moved twice in a week).
- FX: none needed. **IBM earns in USD and quotes in USD**, but note the currency fact for
  honesty: the 10-K says the company derives *"about sixty percent of its revenues from sales
  outside the United States"* and that currency translation and hedging *"contributed
  approximately $200M in year-to-year pre-tax income growth"* in 2025. The earnings CURRENCY of
  record is USD (single reporting currency, no ADR), so USD is the sovereign; the sixty-percent
  figure is a Q4 exposure item, not an FX adjustment to the rate.

**ENTITY AND CIK — confirmed independently, not taken from the brief.** EDGAR company lookup on
CIK **0000051143** returns `INTERNATIONAL BUSINESS MACHINES CORP`, Armonk NY, SIC 3570
(Computer & Office Equipment), state of incorporation New York, fiscal year end 1231, ticker
**IBM** on the NYSE (and NYSE Texas, per the 10-K cover). File number 1-2360. The brief's CIK
is correct.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **Form 10-K for the year ended 2025-12-31, filed
  2026-02-24, accession `0000051143-26-000010`.** *IBM's 10-K carries the financial statements
  and MD&A only by incorporation by reference* — the 10-K cover says *"Portions of IBM's Annual
  Report to Stockholders for the year ended December 31, 2025 are incorporated by reference into
  Parts I, II and IV of this Form 10-K"* — so the statements were read in the filed exhibit
  `ibm-20251231_d2.htm` inside that same accession (the Annual Report to Stockholders), which is
  where the Consolidated Statement of Cash Flows (page 45), the Management Discussion and the
  notes live. Also read: **Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-23,
  accession `0000051143-26-000078`**; the **8-K of 2026-07-22, accession
  `0000051143-26-000077`, exhibit EX-99.1** (the Q2 2026 earnings release — pulled because the
  CGNX ruling makes the furnished earnings release mandatory before scoring [E4-29] and
  [E4-22]'s third flag); and the FY2022 and FY2021 Annual Report exhibits
  (`0001558370-23-002376` / `ibm-20221231xex13.htm` and `0001558370-22-001584` /
  `ibm-20211231xex13.htm`) for the Kyndryl perimeter.
- figure cross-checked against the filed statement (say which): **two.** (1) **Total revenue
  $67,535M** — read off the filed Management Discussion segment table in
  `0000051143-26-000010` / `ibm-20251231_d2.htm`, and it matches the XBRL `Revenues` fact for
  2025-12-31 in the same accession to the dollar ($67,535,000,000). (2) **Net cash provided by
  operating activities $13,193M** — read off the filed Consolidated Statement of Cash Flows
  (page 45) line by line, matching XBRL `NetCashProvidedByUsedInOperatingActivities` exactly;
  and the detail lines underneath it were transcribed rather than skipped, because one of them
  (*"Receivables (including financing receivables) (4,278)"*) is the whole financing-arm
  question at Q4.

**PRICE AND COUNT — stated here, used at Q4/Q5, and dated.**
- **Price US$229.55**, the **2026-09-18 regular-session close** (Yahoo Finance chart endpoint,
  `regularMarketPrice` with `regularMarketTime` = 2026-09-18 16:00:03 America/New_York).
  **AGGREGATOR, FLAGGED** — used for the live quote only, per operator rule 5. Prior five
  sessions for context: 249.09 (09-14), 248.37 (09-15), 237.49 (09-16), 237.75 (09-17), 229.55
  (09-18); the quote has fallen 7.8% in four sessions, which matters only in that a price band
  built on one day's close is a one-day fact.
- **Share count 942,134,390**, read off the **cover of the latest periodic filing**: Form 10-Q
  for the quarter ended 2026-06-30, accession `0000051143-26-000078`, *"The registrant had
  942,134,390 shares of common stock outstanding at June 30, 2026."* (The FY2025 10-K cover, for
  comparison, said 938,034,404 at 2026-02-10 — the count is RISING, not falling, which is a Q3
  fact.) One class of capital stock, par $0.20; no A/B split, so the BRK-B class artifact cannot
  arise here.
- **Market capitalisation US$216,267M ≈ US$216.3bn** (229.55 × 942,134,390). Stale only by any
  issuance between 2026-06-30 and today, which for IBM is employee-plan issuance of roughly
  11M shares a year, about 1.2%.
- *If the filing could not be obtained → **UNRESEARCHED**. Name the ladder rung that failed
  and the obstacle.* **Not invoked: every rung used was SEC EDGAR primary documents (rung 2).
  No rung was blocked.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** IBM is four unrelated businesses
filed as four reportable segments. FY2025, from the segment table in `0000051143-26-000010` /
`ibm-20251231_d2.htm`:

| segment | revenue | % of revenue | gross margin | segment profit | % of segment profit |
|---|---|---|---|---|---|
| Software | $29,962M | 44.4% | 83.5% | $9,920M | 60.6% |
| Consulting | $21,055M | 31.2% | 28.1% | $2,464M | 15.1% |
| Infrastructure | $15,718M | 23.3% | 58.6% | $3,458M | 21.1% |
| Financing | $737M | 1.1% | 45.3% | $521M | 3.2% |
| Other / divested | $63M | 0.1% | NM | — | — |
| **Total** | **$67,535M** | | **58.2%** | **$16,364M** | |

*Read the segment-profit column with a caveat the filing supplies: segment profit is stated
BEFORE stock-based compensation. The reconciliation in the segment note takes $1,685M of SBC
out of the $16,364M of "total reportable segment profit" to reach $10,328M of pre-tax income
from continuing operations, along with $2,166M of acquired-intangible amortisation, $653M of
workforce-rebalancing charges and $1,312M of non-Financing net interest. Every segment margin
quoted above is therefore flattered by stock pay the segments do not carry.*

**1. Software — $29,962M, and it is two different things.** Four disclosed lines: **Transaction
Processing $8,603M**, **Hybrid Cloud (Red Hat) $7,327M**, **Automation $7,733M**, **Data
$6,299M**.
- *Transaction Processing is the mainframe's own software stack* — the operating system,
  database and middleware that run only on IBM Z, licensed by installed capacity. Its revenue
  moves with how many MIPS customers install, which is why it grew 2.3% in FY2025 *"reflecting
  the benefit from our launch of IBM z17 in June 2025 and the strategic importance of this
  mission-critical software"* and fell **8%** in Q2 2026 when the z17 cycle rolled over. It is a
  toll on an installed base, not a product sold into a market.
- *Hybrid Cloud is Red Hat* — a paid subscription to a supported build of Linux, Kubernetes
  (OpenShift) and Ansible, every line of which is available free as source code. What the
  customer buys is indemnity, certification and support, not the code. Bought for **$34.8bn of
  cash on 2019-07-09** (the figure is IBM's own, in the FY2021 annual report). OpenShift ARR is
  disclosed at $1.9bn at year-end 2025, up more than 30%.
- *Automation and Data are a portfolio assembled by purchase* — HashiCorp (closed Q1 2025),
  StreamSets and webMethods from Software AG, Apptio, Turbonomic, and **Confluent, closed
  2026-03-17 for $11,268M of cash for the common stock plus $269M for equity awards** (10-Q
  `0000051143-26-000078`, note 5). Reported Software growth is therefore partly bought growth,
  and this run has to say which.
- Across Software, disclosed **annual recurring revenue $23.6bn** at year-end 2025 (up about
  $2bn), defined as the current quarter's recurring revenue multiplied by four, covering
  subscriptions, committed term licences, SaaS/PaaS and maintenance. Against $29,962M of Software
  revenue that is roughly 79% recurring and 21% transactional, and IBM's FY2024 discussion names
  both halves explicitly: *"growth in our high-value, recurring revenue base, as well as our
  transactional software revenue."*

**2. Consulting — $21,055M, 28.1% gross margin, 11.7% segment margin.** People's time, sold by
the hour or under fixed-price contracts, in two disclosed lines (Strategy and Technology
$11,537M, Intelligent Operations $9,518M). The economics are visible in the margin: of every
dollar of Consulting revenue, 72 cents is the cost of delivering it and about 88 cents is gone by
segment profit. The forward book is disclosed: **signings $21,757M in FY2025, DOWN 13.3% (14.7%
adjusted for currency)**; book-to-bill 1.03; backlog $31.9bn, up about $0.5bn.

**3. Infrastructure — $15,718M, 58.6% gross margin.** Hybrid Infrastructure $10,618M (IBM Z
mainframes plus Power and Storage) and Infrastructure Support $5,100M (the maintenance and
lifecycle contracts on the installed machines). This is a **product-cycle** business and the
filings show the cycle at both ends: **IBM Z revenue +51.7% in FY2025** on the June 2025 z17
launch, and **IBM Z revenue −42% in Q2 2026** in the release of 2026-07-22. Infrastructure
Support is flat (−0.1% in FY2025) — that is the annuity the hardware installs create.

**4. Financing — $737M of revenue, $521M of segment profit, and it is a bank.** $15,052M of
external net financing receivables ($13,192M client + $2,992M commercial, less $141M of
allowance) funded by **$15,093M of Financing segment debt "primarily comprised of intercompany
loans"**, at a disclosed **debt-to-equity ratio of 9.0 to 1** on $1,678M of equity. It earned
$705M of external interest income against $365M of interest expense on matched intercompany
loans. Its stated return on equity was **32.3%**, and the filing says why: it is *"after-tax
segment profit divided by the average of the ending equity for Financing for the last five
quarters"* — a deliberately thin equity base. This segment is separated again at Q4; it is named
here because a lender inside a technology company changes what the consolidated cash-flow
statement means.

**The scarce input this business controls.** It is **the installed base of IBM Z mainframes and
the software written for them.** Nothing else on the list is scarce in IBM's hands: Linux and
Kubernetes are other people's code; consulting skills are rented from the labour market every
year; Power and Storage compete against Dell, HPE and ODMs buying from the same suppliers; the
Automation and Data portfolios were bought, and could have been bought by someone else. The
mainframe is different for a reason the filing states plainly — *"mainframes handling 70% of the
world's transactional workflows (IBM IBV)"* — and z/OS runs on no other machine, so the switching
cost is the cost of rewriting the customer's application estate, not the cost of buying a
competitor's box. **Cited honestly: that 70% figure is IBM's own research arm (the Institute for
Business Value) quoted in IBM's own annual report. It is a self-cited statistic, not a
third-party measurement, and it is recorded as such rather than leaned on.**

**The size of the franchise, as far as the filing lets it be sized.** Transaction Processing
$8,603M + Infrastructure Support $5,100M + the IBM Z share of Hybrid Infrastructure $10,618M.
**IBM discloses IBM Z revenue in dollars nowhere** — only the percentage change, alongside
Distributed Infrastructure's −1.8% — so the split of $10,618M between IBM Z and Distributed
Infrastructure is in no filing. Treating Distributed Infrastructure as roughly flat in dollars
and IBM Z as the growth, the mainframe complex is somewhere around **$19bn to $22bn of the
$67.5bn, i.e. 28% to 33% of revenue**, and it carries more than its share of profit because
Transaction Processing sits inside an 83.5%-gross-margin segment. The remaining two thirds of
revenue — Consulting, Red Hat, Automation, Data, Distributed Infrastructure — is competed for.

**Will the fundamentals look broadly the same in ten years?** **Split answer, and the split is
the finding.**
- For the mainframe complex: **yes.** Installed bases of this kind decay slowly, the replacement
  cost is the customer's application estate rather than IBM's machine, and the filing shows the
  same architecture still being upgraded sixty-two years after System/360.
- For the other roughly 70% of revenue: **no**, and IBM says so itself. *"IBM is a globally
  integrated enterprise that participates in a highly competitive environment … we recognize
  hundreds of competitors worldwide and as we execute our hybrid cloud and AI strategy, **we are
  regularly exposed to new competitors**."* The portfolio that produced FY2025's Software growth
  contains four businesses bought in the last three years, and the 2026 releases name three new
  directions on top — Lightwell (*"a $5 billion commitment"*, July 2026), quantum (*"more than
  $10 billion … over the next five years"*), and a quantum wafer foundry with the U.S. Department
  of Commerce.

**VERDICT: [x] IN**

**Why IN and not UNKNOWABLE.** The test at Q1 is whether I can understand how the money is made
and *"how realistically [I] define what [I] don't know"* **[E3-31]**. Each of the four pieces is
legible from the filed segment disclosure: a toll on an installed base, a support subscription on
free software, a labour business with a disclosed signings and backlog series, a hardware cycle
with a disclosed launch date, and a captive lender with its own balance-sheet table. None of it
required months of study, so **[E4-46]** does not bite. The honest limits are recorded rather
than smoothed: IBM Z revenue in dollars is not disclosed anywhere; the 70%-of-transactions figure
is self-cited; and every segment margin is stated before stock pay.

**Nothing in this section is a compliment.** The durable part of the business is the minority of
revenue, and that is written down here at Q1 precisely so that Q2 cannot borrow the mainframe's
durability for the whole company. **[E4-26]** says to hunt disconfirming evidence hardest for the
favourite hypothesis, and the favourite hypothesis about IBM is the mainframe.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The three criteria, answered separately for the two halves of the company, because the filing
forces the split.**

- **Needed or desired [x]** — for every segment. Nobody disputes that enterprises need
  transaction processing, Linux support, consultants and servers.
- **No close substitute — [x] for the mainframe complex, [ ] REFUSED for the rest, and the
  refusal is in IBM's own words.** The 10-K's Competition section (`0000051143-26-000010`,
  Item 1) says: *"IBM is a globally integrated enterprise that participates in a **highly
  competitive environment** … we recognize **hundreds of competitors worldwide** and as we
  execute our hybrid cloud and AI strategy, **we are regularly exposed to new competitors**."*
  And it names its own principal methods of competition: *"technology innovation; performance;
  **price**; quality; brand; our breadth of capabilities, products and services; talent; client
  relationships and trust…"* — **price, third on the list, written by the company.** A business
  with no close substitute does not list price as one of its methods of competition. The named
  rivals, filed: Software — *"Alphabet (Google), Amazon, BMC, Broadcom, Microsoft, Oracle,
  Salesforce, SAP and Splunk, a CISCO Company"*; Consulting — *"Accenture, Capgemini,
  India-based service providers, management consulting firms, the consulting practices of public
  accounting firms…"*; Infrastructure — *"Dell Technologies, Hewlett-Packard Enterprise (HPE),
  Intel, NetApp and Pure Storage as well as original device manufacturers (ODMs)"*, plus
  *"cloud service providers … to compete with traditional providers."*
- **Not price-regulated [x]** — no price regulation of IBM's products is disclosed anywhere in
  the filing.

**The mainframe case for criterion 2, stated as strongly as it can be, because [E4-51] requires
the argument against my conclusion to be put better than its holders would put it.** z/OS runs
on no machine but IBM Z; the Transaction Processing stack ($8,603M) is licensed against installed
capacity on that architecture; the switching cost is not the price of a competitor's box but the
cost of rewriting the customer's application estate, which for a bank general ledger written in
COBOL is measured in years and hundreds of millions; Infrastructure Support ($5,100M) is the
maintenance annuity those machines create; and the filing asserts *"mainframes handling 70% of
the world's transactional workflows."* In the CEO's letter of 2026-07-14 the installed base is
quantified: *"z17 remains at nearly 130 percent program-to-program, well ahead of z16 which was
our strongest program on record, with **clients representing 85% of installed MIPs maintaining or
growing capacity**."* **On the mainframe complex, criterion 2 is satisfied, and I record it as
satisfied.** The 70% figure is IBM's own Institute for Business Value and the 85% figure is in a
furnished CEO letter rather than a periodic report; both are noted as IBM-sourced.

**And the limit of that case, which is what decides this gate: the franchise is a minority of the
company.** Sized at Q1 from the filed lines, the mainframe complex is about **$19bn to $22bn of
$67,535M, i.e. 28% to 33% of revenue.** The other two thirds is the part IBM's own Competition
section describes. **IBM does not disclose profit below the reportable-segment level**, so the
franchise's own return on capital is measurable from no filing — and I can name no document that
would resolve it, because IBM has never published sub-segment profitability. That sub-question is
**UNKNOWABLE, not UNRESEARCHED**, and it means the strongest version of the bull case cannot be
evidenced even in principle from IBM's disclosure.

### Must the moat be continuously rebuilt? **[E4-04]** — and the test is applied, not recited

The framework's own operative test: *"does a lapse in spending destroy the structure, or merely
narrow it — and does the spending defend the same advantage, or buy its replacement?"*

- **The mainframe leg PASSES [E4-04].** R&D on z16 → z17 → the next machine defends *the same*
  advantage: the same instruction-set architecture, the same customers, the same applications.
  That is the Coca-Cola-advertising case **[E3-49, E5-23]**, not the Rhodes-Ridge case. A lapse
  in spending would narrow it slowly, not destroy it.
- **The company FAILS [E4-04], because two thirds of it is held by purchase.** In five years IBM
  **sold or spun out four businesses** — Kyndryl (managed infrastructure services, spun
  2021-11-03), Watson Health (sold 2022), The Weather Company assets (sold Q1 2024), certain
  QRadar SaaS assets (sold 2024) — and **bought at least six** — Apptio, Turbonomic, StreamSets
  and webMethods from Software AG, HashiCorp (Q1 2025) and Confluent (2026-03-17, $11,268M of
  cash for the common). It **re-presented its own revenue categories in Q1 2025**, deleting
  *"Hybrid Platform & Solutions"* and *"Security"* from the Software segment. **The spending does
  not defend the same advantage; it buys the replacement.** That is the excluded class by the
  framework's own definition, and it is the Mitsui/Rhodes-Ridge analogue the document names.

**This reading does NOT rest on the contested ground, and I say so deliberately because the brief
warned against applying [E4-04] mechanically.** The operator's open question from the TSM run is
whether [E4-04]'s *rapid-and-continuous-change* exclusion should bar a leading-edge foundry whose
process node is replaced every two years — Berkshire bought TSMC, which is evidence against how
that reading was applied. **I do not need that reading here.** My [E4-04] finding is the narrower
and less contestable half of the rule: IBM's non-mainframe position is held by *businesses it
buys and sells*, so the **asset itself** is periodically replaced, not merely the process behind
it. If the operator later rules that the rapid-change exclusion is too broad, this finding
survives that ruling unchanged.

### The number the second question asks for **[E3-46]**, and the goodwill wedge **[E2-43]**

Return on equity is unusable here and the filing shows why. FY2025: net income $10,593M on
average IBM stockholders' equity of about $29,978M = **about 35%**, which is an artefact of
**$170,605M of treasury stock** bought back over three decades. **[E2-43]** requires the
denominator to be unleveraged net tangible assets with the goodwill wedge reported separately, and
for IBM the wedge swallows the equity: total equity $32,740M less goodwill $67,717M less other
intangibles $11,391M = **NEGATIVE $46,368M of tangible equity.** Tangible assets are $72,772M
against $119,139M of total liabilities. So the honest statement of IBM's returns on capital is
this: **the operating business needs very little tangible capital (capex is 1.6% of revenue), and
the capital that was actually spent to assemble it — $67.7bn of goodwill, of which $22.3bn of
cash went out in the last five years alone — earns nothing at all in the accounting.** A high
ROE here measures the buybacks, not the business.

### THE COMPETITOR ROW — required **[E3-28]**

**Metrics chosen, and why.** Four, each computable from filings for almost every peer and each
bearing directly on a criterion: **five-year revenue CAGR** (direction, **[E4-32]**), **gross
margin and its five-year change** (pricing power, **[E2-44]**), **R&D as a share of revenue**
(how much must be spent every year to stay in place, **[E4-04]**), and **stock pay as a share of
operating cash flow** (whether owners get anything after the staff, the shape-#2 test). Windows
are each filer's own five consecutive fiscal years to its latest filed annual period, stated in
the row, because forcing calendar alignment on August, October, November, January and May
year-ends would be my arithmetic rather than theirs.

| Company | window | revenue, start → latest | 5-yr CAGR | gross margin latest | Δ gross margin, 5 yr | R&D % of revenue | stock pay ÷ operating cash | source |
|---|---|---|---|---|---|---|---|---|
| **IBM (subject)** | FY2020→FY2025 | $55,179M → **$67,535M** | **4.12%** | **58.2%** | **+2.2 pts** | **12.3%** | **13.0%** | 10-K `0000051143-26-000010` |
| ServiceNow | FY2020→FY2025 | $4,519M → $13,278M | 24.06% | 77.5% | −0.6 pts | 22.3% | 35.9% | 10-K, CIK 1373715 |
| Broadcom | FY2020(Nov)→FY2025(Nov) | $23,888M → $63,887M | 21.74% | 67.8% | +11.2 pts | 17.2% | 27.5% | 10-K, CIK 1730168 |
| Microsoft | FY2020(Jun)→FY2026(Jun) | $143,015M → $331,839M | 18.33% | 67.9% | +0.2 pts | 10.7% | 6.8% | 10-K, CIK 789019 |
| Alphabet | FY2020→FY2025 | $182,527M → $402,836M | 17.15% | 59.7% | +6.1 pts | 15.2% | 15.1% | 10-K, CIK 1652044 |
| Amazon | FY2020→FY2025 | $386,064M → $716,924M | 13.18% | 50.3% | +10.7 pts | *not tagged* | 14.0% | 10-K, CIK 1018724 |
| Oracle | FY2020(May)→FY2026(May) | $39,068M → $67,357M | 11.51% | *not presented* | *n/a* | 15.3% | 15.0% | 10-K, CIK 1341439 |
| Accenture | FY2020(Aug)→FY2025(Aug) | $44,327M → $69,673M | 9.47% | 31.9% | +0.4 pts | 1.2% | 18.2% | 10-K, CIK 1467373 |
| SAP SE | FY2020→FY2025 | €27,338M → €36,800M | 6.13% | 72.9% | +1.7 pts | 18.0% | 18.5% | 20-F, CIK 1000184, **EUR** |
| Dell Technologies | FY2021(Jan)→FY2026(Jan) | $86,670M → $113,538M | 5.55% | 20.0% | **−3.2 pts** | 2.8% | 6.5% | 10-K, CIK 1571996 |
| HPE | FY2020(Oct)→FY2025(Oct) | $26,982M → $34,296M | 4.91% | *not presented* | *n/a* | 7.3% | 22.0% | 10-K, CIK 1645590 |

**Peers named: 10, against an industry that has at least the 16 IBM itself names.** *(Buffett says
eight; ten are taken, and the six omitted and why is below.)* Arithmetic in
`Test Runs/_research 2026-09-19 IBM/row.py`; inputs in `peers.py` output, every one an
`us-gaap`/`ifrs-full` fact from the filer's own annual report.

**Cells that could not be filled, named rather than guessed:**
- **Gross margin for Oracle and HPE** — neither presents a cost-of-revenue subtotal that
  companyfacts carries undimensioned, so no gross margin exists to quote. Left empty, not
  estimated. (The ORCL run of 2026-09-06 recorded the mirror-image defect on IBM itself: *"IBM's
  income statement does not present operating income at all"*, and it left that cell empty. I have
  followed the same rule in both directions.)
- **R&D for Amazon** — Amazon reports *"Technology and infrastructure"*, not R&D; the two are not
  the same line and substituting one for the other would be my arithmetic.
- **SAP is in EUR.** SAP is a 20-F filer reporting under IFRS in euro, and its USD facts in
  companyfacts are offering-document translations, not its accounts. The CAGR and the three ratios
  are currency-consistent (a growth rate and three ratios in one currency), so the row is honest;
  a dollar revenue comparison would not be. **This is the recorded non-USD IFRS limit
  (`Screens/RESUME STATE …`, the 20-F diagnosis of 2026-09-13), met again and handled by reading
  the filer's own unit rather than loosening a unit filter.**
- **Capgemini, Infosys, Tata Consultancy, NetApp, Pure Storage, Intel and Splunk/Cisco** were not
  taken. Seven more names would not change the reading, and three of them (Capgemini, and the
  India-based providers as a class) are not SEC registrants in a form this shelf reads.

### THE CELL THAT WOULD HAVE DECIDED IT DOES NOT EXIST

**The row above evidences IBM's relative position in software, consulting and infrastructure
broadly. It cannot evidence the mainframe claim, and nothing can.** The two companies that sell
mainframe software in competition with Transaction Processing are **BMC**, which is private
(owned by KKR, no SEC periodic reports), and **Broadcom**, which bought CA Technologies in 2018
and reports its mainframe business inside an *Infrastructure Software* segment with no product
disclosure. **And nobody at all sells a competing mainframe.** So:

- On the mainframe, criterion 2 is satisfied *because* the comparator set is empty, and a claim
  that rests on an empty comparator set is exactly what **[E3-28]** exists to distrust: *"I can't
  be an intelligent owner of a business unless I know what all the other businesses in that
  industry are doing"* — here there are none to know. **The mainframe moat class is therefore
  PROVISIONAL and stays PROVISIONAL**, and under the framework's own rule a PROVISIONAL class
  cannot promote a name.
- **That does not make the gate UNRESEARCHED**, and this is the distinction the run has to get
  right. The question I cannot answer is *how profitable and how durable the mainframe leg is on
  its own*. The question I **can** answer, from filed documents already in hand, is whether the
  **company** is a franchise — and the filer's own Competition section, its own acquisition and
  disposal record, and its own row position answer that. The gate is decided on evidence that is
  present, not blocked by evidence that is absent.

### Direction — and direction outranks existence **[E4-32]**

| leg | FY2024 | FY2025 | FY2025 change | Q2 2026 | reading |
|---|---|---|---|---|---|
| Transaction Processing (the franchise's software) | $8,408M | $8,603M | **+2.3%** (+0.4% ccy) | **−8%** | flat, then down |
| Infrastructure Support (the franchise's annuity) | $5,107M | $5,100M | **−0.1%** (−1.0% ccy) | −1% | **shrinking** |
| IBM Z hardware | *not disclosed in dollars* | *not disclosed* | **+51.7%** | **−42%** | one cycle, both ends |
| Consulting | $20,692M | $21,055M | +1.8% (+0.4% ccy) | flat | flat |
| Consulting signings | $25,103M | **$21,757M** | **−13.3%** (−14.7% ccy) | *"continued growth"* | the forward book fell |
| Hybrid Cloud (Red Hat) | $6,490M | $7,327M | +12.9% | +11% | growing |
| Automation | $6,558M | $7,733M | +17.9% | +4% | growing, partly bought |
| Data | $5,629M | $6,299M | +11.9% | +19% | growing, partly bought |

**The moat is not widening. The two legs that are the franchise are flat and shrinking; the legs
that are growing are the competed ones, and their growth is partly bought.** On the same filed
figures: **$22,306M of acquisition cash went out over FY2021-FY2025** (investing line, five
years) against **$12,356M of additional annual revenue** over the same span — **$1.81 of
acquisition cash per $1 of added annual revenue**, before counting the $8,316M a year of R&D.
R&D plus the five-year mean acquisition spend is **$12,777M a year, 18.9% of revenue**, to move
revenue forward by about $2.5bn a year. That is the **[E3-62]** second-step question asked of
IBM's own programme, and the answer the filing supports is that a large part of the gain does not
stay home.

**And the growth leg is paid to erode the franchise leg.** IBM's own FY2025 Consulting discussion
names its demand drivers as *"business application transformation, **application migration and
modernization**, application operations, and cybersecurity."* Migrating and modernising
applications is the one activity that destroys mainframe switching costs. IBM Consulting is not
the only firm doing it — Accenture, the India-based providers and the cloud vendors all sell it —
but IBM sells it too, and it is disclosed as a growth driver in the same annual report that calls
IBM Z *"the backbone of enterprise IT."*

### The remaining Q2 tests, run rather than skipped

- **Untapped pricing power [E3-33, E5-28]?** **No claim made.** Claiming this class is claiming
  near-monopoly **[E5-28]**, and the row would have to support it. For the mainframe complex
  something close to it may exist, but **[E4-37]**'s agony metric cannot be read from IBM's
  filings — no price series, no unit series — and the one place where filed evidence speaks, the
  Q2 2026 letter, points the other way: *"we saw clients shift their quarterly capex spend toward
  servers, storage, and memory purchases … we did not anticipate the magnitude of the capex
  reprioritization"*, and *"numerous large deals failed to close on the timelines we expected."*
  A price that customers cannot refuse is not deferred by a memory purchase. IBM's own reading is
  deferral rather than substitution (z17 still at 130% program-to-program), and I record IBM's
  reading beside mine rather than only mine.
- **The physical-unit test [E4-55] cannot be run, and that is itself a finding.** IBM discloses
  **no MIPS shipped, no installed-capacity series, no machine count, and — searched and not found
  in the FY2025 10-K — no employee headcount.** For a company a third of whose revenue is people's
  time and a third of whose profit rests on installed capacity, the honest series that would show
  whether dollar revenue is flattered by price is in no filing. Precision Steel's lesson is
  exactly this shape and IBM's disclosure does not permit the test.
- **The attacker's test [E2-45].** With ample capital I would not build a mainframe. I would fund
  the rewriting of the applications, sell the destination, and wait — which is what the cloud
  vendors and every systems integrator including IBM are doing, and which is why the franchise
  leg's revenue is flat while the company's is not.
- **The dominance class [E2-53]?** It applies to the mainframe complex and to nothing else: there
  the position rather than the execution sets the economics. It does not apply to Consulting, whose
  margin is 11.7% and whose signings fell 13.3% in one year.
- **Which of the four causes of extreme success [E4-36]?** The mainframe is an extreme max on one
  variable (switching cost). Red Hat is a wave-riding run **[E3-51]** on open-source adoption, and
  the wave is not IBM's. Consulting is none of the four. Automation and Data are purchases.
- **[E3-61]'s limit on the row, recorded:** the row shows position, not conduct. It cannot tell me
  whether IBM's software pricing behaves like *"a demented Kellogg"*; *"you'd have to know the
  people involved."*
- **Key-person dependence [E4-23]?** Not found. The mainframe moat does not depend on naming a
  CEO, which is a point in the franchise leg's favour and is recorded as such.

- Class: **[x] NONE for the company · [x] PROVISIONAL (and un-promotable) for the mainframe
  complex, ~28-33% of revenue** · Direction: **the franchise legs flat to shrinking; the growing
  legs competed and partly bought; the moat is not widening [E4-32]**
- **VERDICT: [x] OUT**

**Why OUT, and why not UNRESEARCHED or UNKNOWABLE.** OUT means the evidence is here and the
business fails the test. It is here, and it is the company's own:
1. Criterion 2 of **[E3-03]** is refused for roughly two thirds of revenue **by IBM's own
   Competition section**, which names hundreds of competitors, new competitors arriving with the
   strategy, and price as one of its own methods of competition.
2. **[E4-04]** excludes the class whose basis must be periodically replaced, and IBM's
   non-mainframe position is held by businesses it buys and sells — four sold or spun and at least
   six bought in five years, with the revenue categories themselves re-presented in 2025.
3. **[E4-32]**'s direction test, which the framework calls *"the primary criterion of a great
   business"*, reads the wrong way: the franchise legs are +2.3% then −8%, and −0.1%, while the
   bought legs grow.
4. The competitor row places IBM **last of eleven on five-year revenue growth** (4.12%), mid-pack
   on gross margin and R&D intensity, and second-best on stock pay — a slow-growing incumbent with
   recovering margins, not a widening moat.
5. The one claim that could pass — the mainframe — is a minority of revenue, is not separately
   reported for profit in any filing (**UNKNOWABLE**, no document exists), and has an **empty
   comparator set**, so it stays **PROVISIONAL** and **[E3-28]** forbids promoting on it.

**I could name a document that would change the sizing** (a filing that disclosed IBM Z revenue
and Transaction Processing profit), and if that existed the mainframe leg might well pass Q2 on
its own. **It would not change this verdict, because this verdict is about the company the share
buys**, which is the franchise plus two thirds of competed revenue plus a captive bank — and the
2026 releases add three more directions on top (Lightwell at *"a $5 billion commitment"*, quantum
at *"more than $10 billion … over the next five years"*, and a quantum wafer foundry). A file
closed at Q2 on the business is not closed for want of diligence.

**[E3-47] is the counterweight and it is taken seriously:** *"our most egregious mistakes fall in
the omission … their invisibility does not reduce their cost."* The reopening condition is written
at Q6 in words, and the single strongest fact against this verdict is recorded there too.

---
**⚠ EVERYTHING BELOW Q2 IS RECORDED, NOT GOVERNING.** The file closes at Q2. Q3, Q4, Q5 and Q6
are written because the queue's output contract requires a price and because the work was already
done; none of it can promote the name, and the Q5 arithmetic is headed
**COMPUTATION — NOT A CLEARANCE** under operator rule 3.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`* — **RECORDED, NOT GOVERNING.**
*The file closed at Q2. Nothing below can promote the name, and a Q3 IN never promotes anyway
**[E2-37, E2-38, E3-39]**. Every ledger id in this section was checked against
`principle_ledger.csv` before it was written (268 rows; zero phantom ids), because the brief
inherited a known error class — earlier briefs in this queue cited **[E4-52]** for what pay
vests on when the incentives row is **[E4-27]**.*

**STEP 1 — THE WEIGHT CASE.** *How much damage can this manager do before I can react?*
- [x] **Daily execution [E3-38, E3-43, E2-70]** — 31% of revenue is Consulting, a business bid
      and delivered contract by contract, and management says so itself in the letter of
      2026-07-14: *"These conditions require our teams to execute perfectly, and this quarter we
      faltered. We did not adapt and move quickly enough, and numerous large deals failed to
      close on the timelines we expected."* That is a have-to-be-smart-every-day statement made
      by the CEO about his own company.
- [ ] **Control [E1-16]** — no. A marketable minority holding, exitable.
- [x] **Leverage [E3-29]**, and it is quantified rather than screened, because the framework
      supplies no ratio: **total debt $61,260M at 2025-12-31 and $62.0bn at 2026-06-30**, of
      which Financing segment debt is $15,093M and $13.0bn, leaving **non-Financing debt of
      $46,167M and about $49bn** against **$8.2bn of cash, restricted cash and marketable
      securities at 2026-06-30 — down $6.3bn in six months** because $10,480M went out for
      Confluent. Debt ÷ operating cash flow is **4.64×**, which the ORCL run of 2026-09-06
      recorded as making IBM *"the only company in the row that is more levered, and IBM is not
      building data centres."* And **tangible equity is negative $46,368M** (Q2's [E2-43]
      arithmetic), so book equity absorbs nothing.

**CASE DECLARED: Q3 is a BINARY GATE, not an overlay, and no price would compensate for an
integrity failure here [E1-16, E3-29, E5-35].** Two of the three determinants are ticked.

### Honesty — binary, permanent, filings-based **[E5-16]**, each matter dated to when it became PUBLIC

**No disqualifier found, and that is the whole claim — not a finding that the managers are
honest [E5-17].** What was searched and what was found:
- **Auditor's opinion, FY2025 (`0000051143-26-000010`):** unqualified on the statements **and**
  on internal control — *"the Company maintained, in all material respects, effective internal
  control over financial reporting as of December 31, 2025."* **No material weakness. No
  restatement found in any year read (FY2021, FY2022, FY2024, FY2025).**
- **One critical audit matter, and it is the right one:** *uncertain tax positions*, because of
  *"the significant judgment by management when estimating the uncertain tax positions."* This
  is the estimate-driven area **[E2-50]** points at, and it is named by the auditor rather than
  found by me.
- **Auditor tenure: PricewaterhouseCoopers or predecessors "since 1923" — 103 years.** The
  corpus supplies no tenure rule and I am not inventing one. It is recorded because **[E5-32]**
  is on the shelf: Salomon's invented daily plug was signed by the largest audit firm in the
  country for twelve years, and *"audited does not mean true."* The cross-checks in this run
  exist for that reason.
- **Legal and regulatory:** the contingencies note says recorded liabilities for claims *"were
  not material to the Consolidated Financial Statements"* in each of 2023, 2024 and 2025. The
  one named action is an ERISA class action over joint-and-survivor annuity calculations, filed
  2022-06-02, dismissed with prejudice 2024-04-04, vacated and remanded 2025-04-03, settled and
  dismissed with prejudice **2025-12-11** with *"no material financial impact."* Environmental
  CERCLA matters, ordinary-course. **Searched and NOT found in FY2021, FY2022 or FY2025: any SEC
  enforcement matter, subpoena, investigation of revenue recognition, or grand-jury matter.**
- **[E5-22]'s calibration applied:** penalty size is not seriousness in either direction. There
  is no penalty here to mis-size, and *"they didn't act when they learned"* has nothing to
  attach to.

### STEP 2 — THE FLAGS. Each is a prompt to read, never a verdict **[E5-36]**

- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRES, and it fires exactly where the
      CGNX ruling said to look.** The word EBITDA does not appear in the FY2025 10-K or the
      Annual Report. It appears **eight times in the furnished Q2 2026 earnings release**
      (`0000051143-26-000077`, EX-99.1), which lists *"adjusted EBITDA"* and *"adjusted EBITDA
      margin"* among its non-GAAP measures and carries **two** reconciliations — *"GAAP NET
      INCOME TO ADJUSTED EBITDA RECONCILIATION"* and *"GAAP OPERATING CASH FLOW TO ADJUSTED
      EBITDA RECONCILIATION."* **Adjusted EBITDA margin 27.8% in Q2 2026 against a GAAP pre-tax
      income margin of 14.4%** — the measure is nearly double the filed one. Adjusted EBITDA
      appears five times in the Q4 2024 and Q4 2025 releases and eight times in the 2026
      releases, so **the practice is not new and it is intensifying.** [E4-29]'s mechanism
      **[E5-41]** — depreciation is *"reverse float"*, money already spent — applies with less
      force at IBM than at a capital-heavy filer, because IBM's real renewal spend is R&D
      charged above the line rather than depreciation; but the reader is still being handed a
      margin twice the filed one, and **the reason it is twice the filed one is $2,166M of
      acquired-intangible amortisation plus $2,042M of interest on the debt that bought the
      intangibles.** Deleting both is precisely what [E4-29] objects to.
- [x] **Trumpeted earnings projections / growth targets [E4-22] third flag — FIRES, and the
      guidance culture is continuous [E5-30].** IBM gives full-year revenue-growth and
      free-cash-flow guidance **every quarter**, in the furnished release. The trail, read from
      the filings rather than summarised:
      | date | guidance given | ledger |
      |---|---|---|
      | 2025-01-29 (`0000051143-25-000005`) | FY2025: *"constant currency revenue growth of at least 5 percent"*; *"about $13.5 billion in free cash flow"* | **[E3-48]** |
      | outturn, FY2025 | 6.1% constant-currency growth; **$14,734M** free cash flow | **BEATEN, both legs** |
      | 2026-01-28 (`0000051143-26-000004`) | FY2026: *"more than 5 percent"*; free cash flow *"increase by about $1 billion"* | |
      | 2026-04-22 (`0000051143-26-000036`) | *"continues to expect more than 5 percent"* | reaffirmed |
      | 2026-07-22 (`0000051143-26-000077`) | *"We **now** expect constant currency revenue growth in the range of **four-to-five percent**"* | **CUT** |
      **[E3-48]'s prescribed action is to set the company's own past guidance against outturn,
      and Buffett's stated base rate is that nine projections in ten exist to justify a decided
      course.** IBM's record on this evidence is that it **beat** both legs of its FY2025
      guidance and **cut** the revenue leg of FY2026 in July while holding the cash leg. That is
      a better record than the base rate, and it is recorded as such. **[E5-30]** is still the
      live objection and it is about the *practice*, not this year's accuracy: *"once you start
      it, it's all over … forecasting earnings, I can't imagine anything more destructive"* — a
      guidance culture is a ratchet, and IBM is on it.
- [x] **Metric-switching [E2-49] — FIRES, on the proxy's own words.** The PSU programme for
      2023-2025 carried a **Relative Return on Invested Capital modifier** against the S&P 500
      and S&P 500 Information Technology medians. *"For the 2023-2025 program, the ROIC modifier
      was 0"* — it paid nothing. For 2025 grants the Committee *"updated the performance
      modifiers"* and replaced it with a **relative TSR modifier** against the S&P 500
      percentile ranking, **in the same year IBM delivered "a total shareholder return of
      approximately 40%"** (the proxy's own figure), and **widened the leverage range from
      0-150% to 0-200%, taking the maximum from 170% to 220% of target.** [E2-49]: *"Yardsticks
      seldom are discarded while yielding favorable readings. But when results deteriorate, most
      managers favor disposition of the yardstick rather than disposition of the manager."* The
      mitigation, stated fairly: the change was **announced in advance, in the proxy, with a
      stated reason** (*"to support the focus on delivering sustainable revenue growth and free
      cash flow"*), which is the candour case [E2-49] itself carves out — except that the stated
      reason explains the revenue and cash weightings and does not explain swapping a
      capital-return modifier for a share-price modifier.
- [x] **What pay vests on [E4-27] — and it vests on the company's own adjusted numbers.** *"Never,
      ever, think about something else when you should be thinking about the power of
      incentives."* The PSU score is *"a weighted average of the results against the targets of
      **revenue (40%), operating EPS (30%) and free cash flow (30%)**."* **Operating EPS is
      non-GAAP** — it excludes acquired-intangible amortisation, acquisition charges and
      non-operating retirement costs, i.e. exactly the $2,166M and the pension items. **Free cash
      flow is IBM's own definition**, which adds back the growth of the finance book: it turned
      $13,193M of filed operating cash into **$14,734M** in FY2025. So two of the three
      financial metrics that pay management are measures management defines, and the cash metric
      is *higher* than the audited line it is reconciled to. **The mitigation, and it is real:**
      the proxy states that the results *"adjust … operating EPS for any difference between
      actual and targeted share count"* — IBM deliberately neutralises the buyback effect on the
      EPS metric, which is the game **[E2-01]** exists to warn against, removed by the company
      itself. Both halves are recorded.
- [ ] **Weak accounting [E4-22] first flag — does NOT fire, and the pension is the test.** SBC is
      expensed and is in the cash-flow statement at $1,715M. Pension assumptions are not
      fanciful: the FY2025 weighted-average **expected long-term return on U.S. plan assets is
      5.50%**, against a 5.50% U.S. discount rate and a **5.34% 30-year Treasury — sixteen basis
      points above the long bond.** (Non-U.S. plans: 4.86% expected return, 3.61% discount rate.)
      For calibration inside this project, the HON run recorded 7.25% against a 5.25% bond — 200bp
      above — and KMB 76bp above. **IBM, which was once the standard example of pension-flattered
      earnings, is now the most conservative of the three.** Non-operating retirement-related
      income/(cost) was **−$65M in 2025** and +$39M in 2023: earnings are not being flattered by
      pension credit at all.
- [ ] **Unintelligible footnotes — does NOT fire.** The reverse: the segment reconciliation
      quantifies every bridge item separately (acquired-intangible amortisation, SBC, workforce
      rebalancing, net interest ex-Financing, divested businesses), the free-cash-flow definition
      is reconciled line by line to the GAAP statement on the same page, and the Financing
      segment gets its own balance sheet, receivable-allowance table and debt-to-equity ratio.
      This is the **[E2-26]** half-owner test and IBM passes it: a one-time item is quantified at
      every line rather than buried in an adjusted figure.
- [ ] **Serial share issuance [E5-15] — does NOT fire as issuance, but the direction of the count
      is a fact.** No equity offering. Shares outstanding **rose from 938,034,404 (2026-02-10
      cover) to 942,134,390 (2026-06-30 cover)** and the count has drifted up every year since
      buybacks stopped, on employee-plan issuance of roughly 11M shares a year. Proceeds from
      issuance of shares $710M in FY2025 against $1,018M of repurchases for tax withholding — so
      **net cash went out, not in**, and **[E2-52]** (dividends funded by issuance) does **not**
      fire: the $6,255M dividend is covered 2.1× by filed operating cash.
- [ ] **Filed-figure fraud tells [E4-30] — neither fires, and one had to be read rather than
      scored.** *Unnaturally smooth growth:* refuted outright. Net income ran $1,639M (2022),
      $7,502M (2023), $6,023M (2024), $10,593M (2025) — nothing smooth about it, and FY2022's
      collapse has a disclosed non-cash cause, the **$5.9bn pre-tax pension settlement charge**
      on the transfer of about $16bn of Qualified PPP obligations to Prudential and MetLife in
      September 2022. *Cash taxes as a share of reported pre-tax income:* 29.0% (2019), 87.6%
      (2020), 43.5% (2021), 161% (2022), **18.0% (2023), 29.7% (2024), 18.9% (2025)** — noisy,
      not falling, and the two low years have a **disclosed** cause the MD&A names: *"income tax
      benefits associated with the resolution of certain tax audit matters in 2025 and 2024."*
      The flag is a prompt; the prompt was read; the cause is in the filing.
- [ ] **The restructuring-charge distortion [E3-53, E5-33] — the prompt fires on the recurrence
      and IBM's treatment PASSES.** *"Workforce rebalancing charges"* appear **every year**:
      $435M (2023), $692M (2024), $653M (2025). A charge that recurs annually is not a
      restructuring, it is a cost of doing business — and IBM treats it as one: it is inside GAAP
      pre-tax income **and** inside operating (non-GAAP) earnings, which exclude only acquisition
      charges, intangible amortisation and non-operating retirement costs. **IBM never tells
      owners to ignore it**, which is precisely what [E5-33] demands.
- [ ] **Stock-price targeting [E3-50] — a prompt, not a finding.** The rTSR modifier introduced
      for 2025 grants ties up to 20 points of PSU payout to the share price's percentile against
      the S&P 500. It is a modifier and it is relative, not the *"highest stock price possible"*
      premise [E3-50] condemns, and it is the near-universal market practice — which makes it
      **[E2-30]**(4), *peer behaviour mindlessly imitated*, rather than [E3-50] proper.
- **The auditor's-eye test [E4-34], fourth question — period-shifting.** Nothing found that moves
      revenue or expense between periods. The one candidate is the sales-type-lease residual
      adjustment inside *"Other revenue"* (−$2M in 2025, disclosed and quantified as *"reductions
      in revenue for estimated residual value less related unearned income on sales-type leases,
      which reflects the z17 launch"*) — $2M on $67,535M, disclosed with its cause.

### STEP 3 — THE PRIMARY TEST **[E2-01]**, and the denominator is the whole point

> *"The primary test of managerial economic performance is the achievement of a high earnings
> rate on equity capital employed (without undue leverage, accounting gimmickry, etc.) and not
> the achievement of consistent gains in earnings per share."*

**Return on equity, as reported, five years** (net income ÷ average IBM stockholders' equity;
equity from the filed balance sheets):

| year | net income | average equity | ROE |
|---|---|---|---|
| FY2021 | $5,743M | $19,749M | 29.1% |
| FY2022 | $1,639M | $20,423M | **8.0%** |
| FY2023 | $7,502M | $22,239M | 33.7% |
| FY2024 | $6,023M | $24,920M | 24.2% |
| FY2025 | $10,593M | $29,978M | **35.3%** |
| five-year mean | | | **26.1%** |

**And the series is unusable as written, for the reason [E2-01] itself names — "without undue
leverage" — and the reason [E2-43] names.** The denominator is held down by **$170,605M of
treasury stock** and the numerator is held up by debt: tangible equity is **negative $46,368M**.
**[E2-43]** requires unleveraged net tangible assets with the goodwill wedge separate, and the
honest statement of it is: **$67,717M of goodwill and $11,391M of other intangibles against
$32,740M of total equity.** So:
- On **[E2-73]**'s denominator — judge the operators by the return on the underlying assets, not
  on what was paid — pre-tax income from continuing operations of $10,328M on tangible assets of
  $72,772M is **14.2%**, and on the tangible *operating* asset base (excluding $14.5bn of cash and
  securities, $7,544M of prepaid pension assets and $8,610M of deferred taxes) it is far higher
  still, because the operating business runs on almost no tangible capital.
- The two statements together are the truth about IBM's returns: **the operating business earns
  very well on the tangible capital it uses, and the $67.7bn spent to assemble it earns nothing
  in the accounting at all.** A reader shown only the 35% ROE is being shown three decades of
  buybacks.

**The half-owner test [E2-26]: PASS.** Every bridge item is quantified separately; the
free-cash-flow definition is stated in words and reconciled to the GAAP line on the same page;
the Financing segment is disclosed as a lender with its own leverage ratio. I would want to know
all of this if the positions were reversed, and I am told it.

**[E3-59]'s two yardsticks.** *(1) How well do they run the business, against the hand they were
dealt and against competitors' reports?* The hand was a shrinking services conglomerate; the
record since 2021 is **industrial operating cash from $11.1bn (FY2022) to $16.4bn (FY2025), +48%**,
gross margin from 54.0% to 58.2%, and *"$4.5 billion in annual run-rate savings since 2023"*.
Against the competitor row, growth is last of eleven and margins are mid-pack. That is competent
operating management of a difficult hand. *(2) How well do they treat their owners?* The dividend
has been paid every quarter since 1916 and is covered twice; the reporting passes the half-owner
test; and the buyback question below is the one real charge.

### The institutional imperative — score all four **[E2-30]**

- [ ] **resists any change in current direction** — no. The opposite: Kyndryl spun, Watson Health
      sold, The Weather Company sold, QRadar SaaS assets sold, six businesses bought. Whatever
      else this is, it is not inertia.
- [x] **projects/acquisitions materialise to soak up available funds** — **fires, and the
      arithmetic is in the filings.** IBM suspended buybacks *"at the time of the Red Hat
      acquisition closing"* with a stated purpose: *"In order to reduce this debt and return to
      target leverage ratios within a couple of years."* It did de-lever — total debt $73.0bn
      mid-2019 to **$51,703M at 2021-12-31** — and then **re-levered, to $61,260M at 2025-12-31
      and $62.0bn at 2026-06-30**, spending **$22,306M of cash on acquisitions over FY2021-FY2025**
      and $10,480M more in H1 2026. Seven years after the buyback was suspended to cut debt, debt
      is higher than when the de-leveraging finished and **the buyback has never resumed.**
- [x] **staff studies produced to justify the leader's craving** — **recorded as a prompt, not a
      finding, and the honest label is that I cannot see inside the process.** What is visible is
      the pattern: three new multi-billion commitments announced in 2026 alone — *"Lightwell is a
      $5 billion commitment"*, quantum at *"more than $10 billion … over the next five years"*,
      and *"a letter of intent to build Anderon, the world's first pure-play quantum wafer
      foundry"* with $1bn of CHIPS incentives and *"a $1 billion cash contribution by IBM"* —
      announced by a company whose revenue grew 4.12% a year over five years. **[E3-58]** is the
      sharper id here: capital allocation is the CEO's number-one job and CEOs are neither trained
      nor selected for it.
- [x] **peer behaviour mindlessly imitated** — fires mildly: quantum, agentic AI, the rTSR
      modifier, and *"Forward Deployed Engineers"* (a job title borrowed from another company's
      playbook), all arriving on the industry's schedule.

### Capital allocation — the two buyback conditions **[E5-08]**, and the third **[E4-31]**

- **(1) Ample funds for operations and liquidity?** **Marginally.** FY2025 operating cash
  $13,193M against a $6,255M dividend and $1,617M of (c) leaves about $5.3bn; but liquidity at
  2026-06-30 was **$8.2bn, down $6.3bn in six months**, against $6,424M of short-term debt at
  year-end. IBM also has *"committed global credit facilities"* of $10.0bn — and **[E5-39]**
  says bank lines are not counted: *"We will never be dependent on the kindness of strangers."*
  On the corpus's standard IBM's liquidity is thin for its size, and that is a real answer to
  condition (1), not an excuse for failing condition (2).
- **(2) Repurchases at a material discount to conservatively calculated intrinsic value?**
  **NOT TESTED BY MANAGEMENT AT ALL, because there have been no repurchases to test.**
  **$0 of open-market buybacks in FY2020 through FY2025** — the last was $1,361M in FY2019 —
  after **$125bn** spent between FY2007 and FY2019 ($18,828M in 2007 alone, $15,375M in 2010,
  $13,859M in 2013). The only "repurchases" since are **$1,018M of share withholding for
  employee taxes**, which is payroll, not capital allocation.
- **(3) [E4-31]'s third condition — was the register given what it needs to estimate value?**
  Substantially yes on the consolidated business; **no on the franchise**, because Transaction
  Processing and IBM Z are not separately reported for profit or units.

**→ CAPITAL-ALLOCATION FLAG, and it is a two-sided one, stated with the humility clause.**
- The charge under **[E2-51]**: *"A manager who consistently turns his back on repurchases, when
  these clearly are in the interests of owners, reveals more than he knows of his motivations."*
  Six consecutive years of zero repurchase while **$22.3bn went to acquisitions and $30.3bn to
  dividends** is a revealed preference for buying other people's businesses over buying its own.
  **[E5-24]**: *"what is smart at one price is dumb at another"* — and IBM's own history is the
  proof, because the $125bn spent FY2007-FY2019 was spent at prices that produced the negative
  tangible equity above.
- The defence, stated properly: on **my own** Q5 arithmetic below, IBM is **not** at a material
  discount — the honest expectancy is 4.4%-5.7% against a ~10% floor — so **condition (2) is not
  met and a buyback would be the wrong use of the money.** A management that declines to buy its
  own stock when its stock is not cheap is obeying [E5-08], not defying it. The real charge is
  narrower and survives: the acquisitions were made anyway, and **[E5-42]** says quality is the
  capital the business needs while the investment depends on *"how much we pay for that in the
  end"* — $1.81 of acquisition cash per $1 of added annual revenue is a price, and it is high.
- **[E4-13]'s humility clause applies in full:** this rests on my own IV range, and *"they also
  know a whole lot more about them than I do."* **The flag binds POSITION SIZE, never the
  discount rate** — and here there is no position to size, because the file closed at Q2.
- **[E3-54]'s retention test is uninformative here and I say so rather than scoring it.** Over
  FY2021-FY2025 IBM earned $31,500M and paid $30,259M of dividends, so **about $1.2bn was
  retained** — the test asks for $1 of market value per $1 retained, and against $1.2bn almost
  any market-value change passes. The real allocation question is not retention; it is that the
  **acquisitions were funded by debt and disposals while essentially all of earnings went out as
  dividends.** **[E2-60]** is the id: where leverage rises to fund the payout, (c) was
  understated. Tested — and it does **not** hold: filed operating cash covers the dividend 2.1×,
  and the debt went to acquisitions, not to the dividend. **Shape #5, the self-liquidating
  distribution, is refused on the arithmetic.**
- **[E4-39]'s rare-positive tell:** searched. **No candid acquisition post-mortem found** — no
  filing revisits Red Hat, Apptio, Turbonomic, HashiCorp or the Software AG assets against the
  announcement case. That is the ordinary case (*"almost never witnessed"*), so it earns nothing
  either way.

### Candor — and this is where IBM is genuinely unusual

**[E2-72]** requires the stewardship report to come from the CEO, not a staff specialist. On
**2026-07-14, eight days before the quarter's results were released**, IBM furnished an 8-K
containing *"Arvind Krishna's Letter to IBM Investors"* with preliminary figures and this:

> *"I want to spend some time explaining what we experienced in the quarter that led to the
> Software and Infrastructure performance shortfall … **These conditions require our teams to
> execute perfectly, and this quarter we faltered. We did not adapt and move quickly enough, and
> numerous large deals failed to close on the timelines we expected, driving the majority of our
> shortfall. These are not excuses, but they are realities.**"*

That is **[E2-57]**'s test — *"'except for' should be excised from the lexicon … the real mistake
is not the act, but the actor"* — answered in the right direction, by name, ahead of the required
disclosure, with the external causes named (a customer capex reprioritisation toward memory and
servers, cybersecurity distraction) and then **explicitly subordinated to management's own
failure**. It is also **[E2-69]**'s direction test: a deviation from the normal reporting
timetable **toward** candour is not the weak-accounting flag.

**Against that, the same letter and the same release do three things a reader should see:** they
cut the revenue guidance while holding the cash guidance; they answer the shortfall with three new
multi-billion-dollar commitments; and they put *"adjusted EBITDA margin 27.8%"* in the exhibit
beside a 14.4% GAAP pre-tax margin. **Candour about the past quarter and promotion about the next
five years are not the same virtue.**

### Converging flags — **[E4-52]**, the lollapalooza, applied properly

*"Extreme consequences from confluences of psychological tendencies acting in favor of a
particular outcome."* **Five prompts fired: [E4-29] adjusted EBITDA; [E4-22]'s third flag with
[E5-30]'s ratchet; [E2-49] metric-switching; [E4-27] pay vesting on management-defined measures;
[E2-30](2) acquisitions soaking up the funds that used to buy stock.** Do they converge on one
outcome? **Partly, and the honest answer is that they converge on a NARRATIVE rather than on a
number.** Every one of them points the same way — *report the adjusted figure, target it, pay on
it, and buy the growth that makes it* — which is a reinforcing system, not a sum of five
independent prompts. **But the two tests that would turn a narrative into a misstatement both come
back clean**: the accounting is not weak (pension conservative, SBC expensed, restructuring never
excluded, clean ICFR), and the footnotes are unusually legible. **So [E4-52] is recorded as a
converging system of promotional incentives, not as an integrity finding.** **[E5-38]** is the
discipline here: a fired flag is not a venality finding, and people Buffett would trust with his
wallet *"would play games with any number that came to them."*

### THE GUARDRAIL — checked before the verdict

- [x] Confirmed: **nothing in this Q3 is used to promote the name.** The file closed at Q2 and a
      strong Q3 cannot repair it **[E2-37, E2-38, E3-39]**. *"A textile company that allocates
      capital brilliantly within its industry is a remarkable textile company — but not a
      remarkable business."*
- [x] **Key-person dependence is recorded at Q2, not here.** It was searched and **not found**:
      the mainframe moat does not require naming a CEO **[E4-23]**.
- [x] **Is a great manager the reason to act?** No, and the question does not arise. There is no
      excisable cancer **[E2-35, E2-36]** and no corporate Pygmalion on offer; there is a
      competent operator improving the margins of a slow-growing company.
- **[E5-45]'s ABCs are the live Q6 monitoring item and IBM is the corpus's own named example:**
      *"arrogance, bureaucracy and complacency. When these corporate cancers metastasize, even
      the strongest of companies can falter"* — **GM, IBM, Sears and U.S. Steel named**, whose
      *"one-time financial strength and their historical earning power proved no defense."* The
      corpus names IBM in that sentence. On the evidence read here the ABCs are **not** the
      present condition: the company sold four businesses, cut $4.5bn of run-rate cost, and its
      CEO published a letter saying he faltered. That is the opposite of complacency. It is
      carried to Q6 as the thing to watch, which is where [E5-45] belongs.
- **[E3-40]'s loss of focus is the sharper charge and it is live:** *"the management of a great
      company gets sidetracked and neglects its wonderful base business while purchasing other
      businesses that are so-so or worse … Loss of focus is what most worries Charlie and me."*
      IBM's base business — the mainframe complex — grew 2.3% and then fell 8%, while $22.3bn
      went to buying other businesses and three new multi-billion programmes were announced.
      **That is a Q2/Q6 finding, and it is recorded at Q2 as the direction test, not here as a
      compliment or an accusation.**

- **VERDICT: [x] IN — RECORDED, NOT GOVERNING**

*IN means **no disqualifier was found**. It is **not** a finding that the managers are honest —
*"sincerity and empathy can easily be faked"* **[E5-17]** — and **[E5-26]**'s calibration applies:
a decade of strong record preceded the Sokol failure, and *"it's generally a mistake to assume
that rationality is going to be perfect, even in very able people."* Five prompts fired and were
read; one capital-allocation flag is live and two-sided; the accounting and disclosure tests came
back cleaner than this project's average, and the pre-announcement letter of 2026-07-14 is one of
the better candour artifacts encountered in this queue. **IN never promotes, and this file is
already closed.***

## Q4 — WILL IT SURVIVE? — **RECORDED, NOT GOVERNING**

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

---
⛔ **Q5 DID NOT OPEN. Q1-Q4 do NOT each show IN: Q2 is OUT.** UNRESEARCHED and UNKNOWABLE both
close the file and neither is a pass; **OUT closes it permanently.** What follows is produced only
because `Screens/WATCHLIST RUN QUEUE.md` requires every run in this queue to end with a price, and
it is headed as operator rule 3 requires.

---
## COMPUTATION — NOT A CLEARANCE

**This is arithmetic, not a Q5. It carries no entry language, no ranking position, no bar, and no
margin of safety. The file closed at Q2 on the business.**

**THE PRICE, AND WHAT THE BUYER IS PAYING FOR, IN WORDS.**

**US$229.55 a share** (2026-09-18 regular-session close, Yahoo Finance `regularMarketPrice` at
16:00:03 America/New_York — **aggregator, flagged, live quote only**) × **942,134,390 shares** (Q2
2026 Form 10-Q cover, accession `0000051143-26-000078`, *"The registrant had 942,134,390 shares of
common stock outstanding at June 30, 2026"*) = **market capitalisation US$216,267M.**

**At $229.55 the buyer is paying $216.3bn for:** a mainframe franchise of about $19bn-$22bn of
revenue that no competitor can substitute and that IBM will not report profit or units for; a
$21.1bn consulting business earning 11.7% at the segment line whose forward signings fell 13.3%
last year and which is paid by its clients to migrate applications off the franchise; a $22.6bn
bought software portfolio (Red Hat, Automation, Data) assembled with $22.3bn of acquisition cash
over five years and $11.5bn more for Confluent in March 2026; a $15.1bn matched loan book levered
9 to 1; $67.7bn of goodwill and $46bn of industrial debt against $8.2bn of cash; and three new
programmes announced in 2026 — Lightwell at *"a $5 billion commitment"*, quantum at *"more than
$10 billion … over the next five years"*, and a $1bn contribution to a quantum wafer foundry. The
cash return on that price is a **2.94% dividend** (the declared $1.69 quarterly rate annualised)
and whatever the retained and borrowed capital earns.

**1. THE YIELD.**

| owner earnings | ÷ market cap | = yield | sovereign | points over the sovereign |
|---|---|---|---|---|
| **$9,486M** (band low: 4-yr FY2022-25, consolidated, renewal-D&A end) | $216,267M | **4.39%** | **5.34%** | **−0.95** |
| **$10,500M** (judged, cycle-normalised centre **[E4-41]**) | $216,267M | **4.86%** | 5.34% | **−0.48** |
| **$12,234M** (band high: 2-yr FY2024-25, industrial, capex end) | $216,267M | **5.66%** | 5.34% | **+0.32** |
| *$14,734M — IBM's own FY2025 free cash flow, for contrast only: no SBC subtracted and the finance-book build added back* | $216,267M | *6.81%* | 5.34% | *+1.47* |

**Sovereign used: 5.34% — the bare rate, no per-name premium added [E3-42].** Certainty is priced
at the understanding gate and in the end margin, never in the rate, and it is priced once
**[E4-11, E4-48]**.

**2. WHAT THE PRICE ALREADY ASSUMES.** Perpetual growth needed to lift the honest pre-tax
expectancy to the **~10% floor [E4-28]**:

| on | growth required, in perpetuity |
|---|---|
| band low | **5.61% a year** |
| judged centre | **5.14% a year** |
| band high | **4.34% a year** |

**What the business has actually done, on one perimeter:**

| series | window | rate |
|---|---|---|
| revenue (the recast continuing-operations line) | FY2020→FY2025, 5 years | **4.12% a year** |
| owner earnings, construction A, capex end | FY2022→FY2025, 3 years | **9.13% a year** |
| owner earnings, construction B, capex end | FY2022→FY2025, 3 years | **16.38% a year** |
| industrial operating cash | FY2022→FY2025 | 13.76% a year |
| IBM's own free cash flow | FY2022→FY2025 | 16.58% a year |

**3. WHAT YOU ARE PAID.** **−0.95 to +0.32 points over the sovereign**, centred on **−0.48**. At
this price a buyer receives roughly the thirty-year Treasury yield, and takes business risk,
competitive risk and $46bn of industrial leverage for it.

**THE FLOOR, AND IT IS THE WHOLE ANSWER [E4-28].** *"that's the figure we quit on … we don't want
to buy equities where our real expectancy is below 10 percent. Now, that's true whether short rates
are 6 percent or whether short rates are 1 percent."* **Honest pre-tax expectancy at this price:
4.39% to 5.66%. The floor is missed by 4.3 to 5.6 points at EVERY end of the band, in EVERY window,
on BOTH (c) ends and BOTH financing constructions.** Below the floor a name is not ranked — it is
quit on — so **no ranking position is assigned.**

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]**, on the judged $10.5bn centre:

| standard | value | per share |
|---|---|---|
| ~10% floor, no growth | ~$105bn | **~$110** |
| ~10% floor, 2% growth | ~$130bn | **~$140** |
| ~10% floor, 3% growth | ~$150bn | **~$160** |
| *bond parity, no growth — **not** a buying standard, shown to locate the price* | *~$197bn* | *~$209* |

**Round-number range: roughly $110 to $160 a share. Current price $229.55 — above the whole
range**, and above even the bond-parity figure that no buying standard endorses.

**WHICH BAR — and only one is used [E4-11 / E4-01].**
- [x] **Bar 2, the screamer test [E4-01].** Does the price already clear the **conservative** case?
      **No — it is above the whole range.** Three outcomes exist and this is the third: *price above
      the whole range → no.* **No margin is added on top, because none is needed and the corpus
      forbids stacking.**
- [ ] Bar 1, the normal method, is **not** used. No margin of safety is quoted, so none of
      **[E3-25]**'s ~35% bridge, **[E3-26]**'s 60% ceiling or **[E4-12]**'s dollar-on-the-dollar is
      invoked.
- **WINDAGE COUNT: ZERO on the price test.** Conservatism was not spent to reach this result. The
  one input judgment that runs in the conservative direction is **[E4-41]**'s cycle normalisation of
  the centre to $10.5bn — and **[E4-48]** classes that as input realism (*"be as realistic as you
  can on those numbers, but with any errors being on the conservative side"*), not as the end
  margin. **The proof that no windage was needed: at the completely un-normalised top of the band —
  the two-year window, the industrial construction, the capex end of (c), no luck removed — the
  yield is 5.66% and the floor is still missed by 4.34 points, and the value is still only ~$130 a
  share at zero growth or ~$186 at 3%.** The name fails the price test with conservatism spent
  nowhere at all.

**THE SECOND BOUND AND THE CEILING, both named [E4-44, E2-63, E4-35].**
- **[E4-44]:** *"the value of an asset … cannot over the long term grow faster than its earnings
  do."* The 5.14% perpetual growth the floor needs is a claim about earnings for ever, not about
  the next three years.
- **[E2-63]:** what bounds the upside is that IBM's revenue has compounded at 4.12% and each
  increment of revenue has cost $1.81 of acquisition cash, so growth beyond the base business
  requires capital continuously invested at a price already on the record.
- **[E4-35]'s base rate is the discipline:** fewer than 10 of the 200 most profitable companies of
  2000 achieved 15% EPS growth over twenty years. IBM does not need 15% — it needs about 5% for
  ever merely to **reach** the floor, which is a much softer claim, and that is exactly why the
  fact below is recorded as the strongest one against this file.

**THE STRONGEST SINGLE FACT AGAINST MY CONCLUSION, stated as well as its holders would state it
[E4-51].** *IBM's owner earnings have grown faster than the rate the floor requires. On one clean
perimeter, construction A's capex end went from $7,587M (FY2022) to $9,861M (FY2025) — 9.13% a
year — and construction B's from $8,287M to $13,061M, 16.38% a year; industrial operating cash rose
48% in four years; IBM's own free cash flow compounded 16.58%. The floor needs 5.14%. A holder can
therefore say, fairly, that the price assumes less growth than the company has just delivered,
that margins are still expanding on $4.5bn of realised run-rate savings, that the Software segment
is 79% recurring with ARR up $2bn, that the pension risk has been transferred twice, that the CEO
pre-announced a bad quarter in his own name, and that the mainframe franchise is a genuine
[E3-03] franchise nobody can copy.*
**Why it does not change the verdict — and this is a judgment, not a rebuttal by assertion.** (1)
The file closed at **Q2**, on the business, and **no price and no growth rate reopens a Q2**; the
growth fact is a Q5 fact arriving after the gate. (2) The base year is a trough: FY2022 was the
first post-Kyndryl year and carried the separation's cash cost. Measured from FY2023 instead,
construction A's capex end went $11,309M → $9,861M, which is **down**. Choosing FY2022 as the base
is exactly the *"calculated selection of either initial or terminal dates"* **[E4-38]** warns
against, and I have shown every window so the reader can choose. (3) The growth is **margin
recovery plus a mainframe cycle peak plus bought revenue**, and none of the three is a perpetuity:
cost programmes end, z17 has already turned (**IBM Z −42% in Q2 2026**), and bought revenue costs
$1.81 per $1. (4) Construction B's 16.38% is partly the *finance book growing*, which is lending,
not earning.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL? — **RECORDED, NOT GOVERNING**

**There is no position, so nothing here arms anything.** Q6 exists in a closed file to record the
reopening conditions in words, per the QLYS ruling of 2026-09-07: **a name that failed at Q2 failed
on the BUSINESS, and a price alert on it would be a category error.** No band is armed in
`tools/alerts.json` and no `PORTFOLIO.md` row is added.

**Pre-committed, before any entry [E1-02]** — the yardsticks are set now, in advance, so that a
future session cannot fit them to the answer:

- **Thesis-confirming metric** *(would support reopening Q2)*: **IBM begins disclosing IBM Z
  revenue in dollars and Transaction Processing segment profit**, and that disclosure shows the
  franchise complex growing in dollars and in installed capacity over a full product cycle, not
  one launch year. A physical series — MIPS installed or shipped — would matter more than any
  dollar line **[E4-55]**.
- **Thesis-breaking metric and its threshold** *(would confirm this verdict)*: **Transaction
  Processing plus Infrastructure Support declining in dollars over any trailing four quarters that
  include a mainframe launch**, and Consulting signings down a second consecutive year from
  $21,757M.
- **Next catalyst dates:** Q3 2026 results, expected late October 2026 (the pattern is an 8-K under
  Item 2.02 in the third or fourth week of the month); the FY2026 10-K expected late February 2027,
  which is the filing that will recast FY2026 for Confluent and show whether the z17 down-leg
  continued.

**THE REOPENING CONDITIONS, in words, because that is what a Q2 OUT gets.** This is a **permanent
OUT on the company as constituted**, and the framework says OUT is permanent. What would make it a
different company, and therefore a new file rather than a reversal:
1. **A structural separation** that put the mainframe complex on its own books — the way Kyndryl
   put the services business on its own books. A separately reported franchise with disclosed
   profit and units would be a **new name to run under v4**, and it would be an interesting one.
2. **A stop to the acquisition programme**, sustained over a full cycle, with the cash going to
   repurchase at a price below a conservatively calculated value — which would convert the **[E2-51]**
   charge into the **[E2-48]** superstar tell: *"these champs have made very few deals in recent
   years, and often have found repurchase of their own shares to be the most sensible employment of
   corporate capital."*
3. **Filed evidence of pricing power in both halves [E2-44]** — that IBM can raise prices when
   demand is flat and grow dollar volume with only minor additional capital — in the part of the
   company that is not the mainframe.

**The sell rule, recorded for completeness [E2-28]** — there is no holding, so each line is
notional: the two triggers (the market judging the business more valuable than the facts indicate;
funds needed for something more undervalued or better understood) and the three hold conditions
(satisfactory return on equity capital, competent and honest management, market not overvaluing).
On today's facts a holder would find condition one satisfied at the operating level, condition two
satisfied in the *no-disqualifier-found* sense of Q3, and **condition three failed** — at 4.39%-5.66%
against a 5.34% sovereign the market is not underpricing this business. **Price appreciation and
holding period are explicitly rejected as reasons to sell [E2-28]**, and are not used here.

**The real trigger is a moat downgrade and it is slow [E4-17, E3-30].** *"The question is whether
this erosion is just part of an aberrational cycle … or whether the business has slipped in a way
that permanently reduces intrinsic business values."* **For the mainframe leg this run's answer is
that Q2 2026 is an aberrational cycle, on IBM's own evidence** (z17 at 130% program-to-program, 85%
of installed MIPS maintaining or growing capacity, deals deferred rather than lost). **The
permanent slippage this file found is not in the mainframe at all; it is in the company's
composition** — two thirds of revenue competed for, held by purchase, and re-presented every few
years. That is a slow finding and **[E4-17]** says beliefs about it should change gradually, which
is why the reopening conditions above are structural rather than numerical.

**[E5-45] is the standing monitoring item, and the corpus names IBM in it:** *"arrogance,
bureaucracy and complacency … even the strongest of companies can falter"* — **GM, IBM, Sears and
U.S. Steel**, whose *"one-time financial strength and their historical earning power proved no
defense."* On the evidence read here the ABCs are **not** the present condition, and the CEO letter
of 2026-07-14 is direct evidence against complacency. Recorded as the thing to watch, not as a
finding.

**Position size: NONE. [E5-14]'s do-not-trim rule and [E3-45]'s capital-to-rank-#1 direction have
nothing to operate on.** The capital-allocation flag from Q3 would bind position size if there were
a position; there is not.

- **VERDICT: [x] OUT — RECORDED, NOT GOVERNING.** Consistent with Q2: the file is closed on the
  business, and Q6 arms nothing.

## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN → Q2 OUT → Q3, Q4, the
      computation and Q6 all written under a standing **RECORDED, NOT GOVERNING** banner placed
      immediately after the Q2 verdict.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN and Q3 IN
      and Q4 IN carry none. **The word PROVISIONAL appears once, attached to the mainframe moat
      class inside a gate whose verdict is OUT** — where a provisional class cannot promote
      anything and does not sit under an IN.
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** **There is no
      UNRESEARCHED verdict in this file**, and that was checked rather than assumed: every gate is
      IN or OUT. Two sub-questions inside Q2 are marked **UNKNOWABLE**, with what cannot be known
      stated (below).
- [x] **Every UNKNOWABLE states what specifically cannot be known.** Two, both inside Q2: (a)
      **Transaction Processing and IBM Z profitability and unit volume** — IBM has never disclosed
      profit below the reportable-segment level or any MIPS series, so **no document exists** that
      would resolve the franchise leg's own economics; (b) **the mainframe comparator set** — BMC is
      private (KKR, no SEC periodic reports), Broadcom folds its CA mainframe software into an
      undisclosed *Infrastructure Software* segment, and no one sells a competing mainframe, so the
      same-metric peer cell cannot be filled by any filing. Both are UNKNOWABLE rather than
      UNRESEARCHED because I can name no document, not because I did not look.
- [x] **Step 0: the filing was read, with accession number; a figure was cross-checked.** FY2025
      10-K `0000051143-26-000010`, filed 2026-02-24, **with the incorporated Annual Report exhibit
      `ibm-20251231_d2.htm` inside the same accession**, which is where the statements and MD&A
      live; Q2 2026 10-Q `0000051143-26-000078`; the furnished Q2 2026 release
      `0000051143-26-000077` EX-99.1 and the CEO's pre-announcement letter `0000051143-26-000070`
      EX-99.1; the FY2025, FY2024, FY2022 and FY2021 earnings releases; the 2026 proxy
      `0000051143-26-000025`; and the FY2022 and FY2021 Annual Report exhibits for the Kyndryl
      perimeter. **Two figures cross-checked** against the filed statements: total revenue
      $67,535M and operating cash flow $13,193M, both matching XBRL to the dollar. MD&A,
      cash-flow statement **including its detail lines** (the $(4,278)M receivables line is the
      whole Q4 financing question), and footnotes (segments, borrowings, retirement-related
      benefits, revenue recognition, commitments and contingencies, acquisitions) all read.
- [x] **Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.**
      Four annual windows × two (c) ends × two financing constructions, plus a TTM; the four-year
      FY2022-FY2025 mean is the longest legitimate one and **the reason the five-year default
      [E2-42] could not be met is stated and quoted** (the cash-flow statement includes Kyndryl and
      IBM published no Kyndryl cash-flow statement). (c) is disclosed as a guess **[E2-23]** at
      $1,600M-$2,000M with the raw filed D&A end refused in writing and the size of the refusal
      given ($3.1bn a year).
- [x] **Competitor row filled, or the moat marked PROVISIONAL and UNRESEARCHED.** Ten peers with
      their own stated windows, four metrics, filing-sourced. Unfillable cells named, not guessed
      (ORCL and HPE gross margin, AMZN R&D, SAP in EUR). **The mainframe sub-claim is marked
      PROVISIONAL with its comparator set shown to be empty, and it is classed UNKNOWABLE rather
      than UNRESEARCHED with the reason given** — the framework's default for an unfillable peer
      cell is UNRESEARCHED, and departing from it required naming why no document exists.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** USD 5.34%,
      2026-09-18, US Treasury daily par yield curve, **struck fresh this run** via
      `python tools/sources.py` and not inherited.
- [x] **Value stated as a round-number range, not a point estimate.** ~$110 to $160 a share.
- [x] **One bar chosen, not both; windage count stated.** Bar 2, the screamer test. **Windage
      ZERO** on the price test, with the proof that none was needed (the un-normalised top of the
      band still misses the floor by 4.34 points).
- [x] **Prices dated; aggregator used for live quotes only and flagged.** $229.55, 2026-09-18
      close, Yahoo Finance, flagged at Step 0 and again at the computation.
- [x] **Run committed to git**, in six commits with a pathspec each (template, Step 0, Q1, Q2,
      Q3, Q4, then this close and the fold).

**THINGS I GOT WRONG OR COULD NOT DO, recorded rather than smoothed:**
1. **[E3-70]'s grant-value measure of stock pay was not obtained.** No undimensioned grant-date
   total resolves for IBM in companyfacts. At 13.0% of operating cash flow SBC is under the
   50%-of-OCF threshold this project set for reading the grant table by hand, so the charge is used
   as the measure and named as the **floor** of the subtraction, not the measure.
2. **The TTM industrial construction could not be built.** IBM publishes the change in Financing
   receivables annually, in the MD&A free-cash-flow table, and not in the 10-Q. Left blank rather
   than estimated.
3. **The Kyndryl residual was not rebuilt from Kyndryl's own 10-K.** It could be attempted; the
   result would still be my subtraction rather than IBM's filed statement, and four clean years
   produced a band that does not straddle the decision. **If the answer had been close, this would
   have been the work order.**
4. **Segment-level (c) does not exist.** (c) is judged for the consolidated company; IBM discloses
   *"Depreciation/amortization of non-acquired intangibles"* by segment ($532M Software, $78M
   Consulting, $1,130M Infrastructure, $3M Financing in 2025) but no segment capex, so a
   franchise-only owner-earnings figure cannot be built.
5. **The mainframe complex's size ($19bn-$22bn) is my arithmetic, not IBM's disclosure**, and the
   run says so at Q1, Q2 and Q4 each time it is used.

---
## REGISTER
- Verdict: **[x] OUT (about the business)** — [ ] IN [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** **Q1 IN, Q2 OUT** — a genuine, unsubstitutable mainframe franchise over 28-33% of
  revenue, and for the other two thirds IBM's own Competition section names *"hundreds of
  competitors"*, *"regularly exposed to new competitors"* and price among its own methods of
  competition; **[E4-04]** excludes it because the position there is held by businesses bought and
  sold (four out, six in, five years) rather than by a defended advantage; the franchise legs are
  flat to shrinking (Transaction Processing +2.3% then −8%, Infrastructure Support −0.1%, IBM Z
  +51.7% then −42%) while the bought legs grow at $1.81 of acquisition cash per $1 of added annual
  revenue. **Price US$229.55 (2026-09-18), cap US$216,267M, sovereign USD 5.34%. FAIL.**
- **Computation, not a clearance:** owner earnings **$9,486M-$12,234M** across every window, both
  (c) ends and both financing constructions; judged centre $10.5bn; yield **4.39%-5.66%** against a
  **5.34%** sovereign, **−0.95 to +0.32 points**; the **~10% floor [E4-28] is missed by 4.3-5.6
  points at every end**; value roughly **$110-$160 a share** against a price of **$229.55**.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable. **This file is not short of any document
  it could have obtained.**
- **If UNKNOWABLE:** not the file's verdict. Two sub-questions are UNKNOWABLE and are named in the
  self-audit: the franchise leg's own profit and units, and the mainframe comparator set.
- **Survival shape (recorded at Q4, not governing):** **#10 THE CAMOUFLAGE**, with a proposed
  **feature** — the company sells the service that erodes its own franchise — offered to the
  operator and changing no register. Shapes #1, #2, #3, #4, #5 and #6 refused with arithmetic.
