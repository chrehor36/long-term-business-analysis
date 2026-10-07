import io
p = 'Test Runs/2026-09-19 Run - IBM International Business Machines.md'
s = io.open(p, encoding='utf-8').read()
start = "## Q2 — IS IT A FRANCHISE? **[E3-03]**"
end = "## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?"
i, j = s.index(start), s.index(end)
new = """## Q2 — IS IT A FRANCHISE? **[E3-03]**

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

"""
s = s[:i] + new + s[j:]
io.open(p, 'w', encoding='utf-8').write(s)
print('q2 written')
