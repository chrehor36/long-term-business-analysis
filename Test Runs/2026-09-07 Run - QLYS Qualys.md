# Company Run — Qualys, Inc. (QLYS) — 2026-09-07
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
## STEP 0 — THE RATE, THE COVER, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- rate **5.24 %** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-yr
  (issuing authority; not the FRED fallback)**
- FX: none. Qualys reports in USD. International revenue is disclosed but not separately
  currency-denominated in the segment note; the reporting and earnings currency is USD.

**STAGE 0 — THE COVER COUNT, BY HAND. AND THE SCREEN ROW'S COUNT IS STALE BY 1.1M SHARES.**

- **10-Q cover, verbatim, accession `0001107843-26-000035`, filed 2026-08-04, period
  2026-06-30:** *"The number of shares of the registrant's common stock outstanding as of
  **July 22, 2026** was **34,595,001**."* Single class, $0.001 par, NASDAQ. No split in the
  filing history; the split feed returns none after the measurement date.
- **The published screen row's `cap_m 6124` back-solves to 35,676,668 shares** at the $171.65
  quote. **That is the 10-K cover count**, and the 10-K cover reads: *"outstanding as of
  **February 11, 2026** was **35,675,926**"* (35,675,926 × $171.65 = $6,123.75M, i.e. the row
  to four figures). **The row used a correct source, six months stale.** Qualys retired
  1,080,925 shares — **3.0%** — between the two cover dates, so the row's market cap is 3.1%
  too high and its yield 3.1% too low. Direction of the error: **against** the company.

  > **CORRECTION, recorded in place per operator rule 6 rather than silently edited.** This
  > line first read *"The 10-K balance sheet count at 2025-12-31 was 35,681 thousand … the row
  > used the year-end balance-sheet count."* **Both halves were wrong.** The filed
  > balance-sheet count at 2025-12-31 is **35,730 thousand**, not 35,681; and the row's
  > implied count matches the **10-K cover (35,675,926 at 2026-02-11)**, not the balance
  > sheet. Found by re-deriving the count from XBRL and the cover after the section was
  > committed. **No downstream figure changes**: the market cap used throughout this run has
  > been $5,938M on the 10-Q cover count of 34,595,001 from the start, and the correction only
  > re-attributes which stale source the screen took.

- **price $171.65 · 2026-09-04 · aggregator, FLAGGED, live quote only** (operator rule 5)
- **shares 34,595,001** (10-Q cover, 2026-07-22, single class)
- **MARKET CAP = $171.65 × 34,595,001 = $5,938M**

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: FY2025 10-K, FYE 2025-12-31, filed 2026-02-20, accession
  `0001107843-26-000008`.**
- Vintages also read for the disclosure-history tests: FY2024 `0001107843-25-000009`,
  FY2023 `0001107843-24-000008`, FY2022 `0001437749-23-004384`, FY2021 `0001437749-22-004075`,
  FY2020 `0001437749-21-003648`, FY2019 `0001628280-20-001963`, FY2018 `0001628280-19-002099`,
  FY2017 `0001107843-18-000003`.
- 10-Qs read: `0001107843-26-000035` (2026-06-30), `0001107843-26-000015` (2026-03-31),
  `0001107843-25-000038` (2025-09-30).
- Proxy: DEF 14A filed 2026-04-22, accession `0001140361-26-016101`.
- **Figure cross-checked against the filed statement:** XBRL returns FY2025 operating cash
  flow of $309,400k. The filed Consolidated Statements of Cash Flows shows **"Net cash
  provided by operating activities 309,400"** — agrees to the dollar. Second cross-check,
  because (c) decides the width of this run: XBRL `PaymentsToAcquirePropertyPlantAndEquipment`
  FY2025 = $4,990k; the filed investing section shows **"Purchases of property and equipment
  ( 4,990 )"** — agrees to the dollar, and it is **the only capital line in the entire
  investing section.**

---
## THE SCREEN ROW — REPRODUCED, AND IT IS THE EIGHTH CONSECUTIVE SPREAD DEFECT

**The published row:**

    QLYS, cap_m 6124 · oe_bottom_m 145 · oe_top_m 183 · spread 0.265 ·
    yield_bottom 2.36% · vs_sovereign −2.88 pts · growth_required 7.64% ·
    level_shift 1.64 "STEP UP - normalize down [E4-41]" · best_year_dep 0.072 ·
    acq_note: (none) · newest_filing 2025-12-31

**BOTH ENDS REPRODUCE TO THE DOLLAR, AND THE WIDTH BETWEEN THEM IS TWO DIMENSIONS
COLLAPSED INTO ONE NUMBER.** Rebuilt by hand from the filed cash-flow statements:

- `oe_bottom 145` = the **5-year** (2021–25) mean of (OCF − SBC − **D&A**) = **$144.6M**
- `oe_top 183` = the **3-year** (2023–25) mean of (OCF − SBC − **capex**) = **$182.9M**

**The window moved AND the capex end moved, in the same direction, in one number.** The
framework requires the capex band to be the (c) judgment **[E2-23], [E3-44], [E5-20]** and
the window spread to be carried *alongside* it **[E4-25]**. The row varies both at once and
reports neither, so the "26.5% spread" cannot be attributed to either cause.

**THE OPERATOR'S CORRECTION 2 IS REFUTED FOR THIS FILER, AND THAT MATTERS.** The brief
warned that `da_annual()` returned **empty** on CRWD, so both "ends" were secretly the same
capex end. **It does not return empty here.** `DepreciationDepletionAndAmortization` resolves
for every one of the sixteen filed years, and it reconciles to the filed statement:
XBRL 2025 = $14,491k; the filed cash-flow statement shows **"Depreciation and amortization
expense 14,491"**. So the D&A end of the band was genuinely computed for Qualys. The defect
here is not a missing end — it is the **conflation** of the window axis with the capex axis.

**THE OPERATOR'S CORRECTION 3 IS ALSO REFUTED, AND I checked it the way CRWD's was missed.**
Qualys has **no separately-tagged capitalized-software cash line.** The entire investing
section of the FY2025 10-K is four lines: purchases of marketable securities, sales and
maturities of marketable securities, **"Purchases of property and equipment ( 4,990 )"**, and
the net. `CapitalizedComputerSoftwareGross` exists as a *balance-sheet* tag ($3.4M at
2025-12-31, $1.2M at 2024-12-31) but it sits **inside** the PP&E note as *"Computer software
26,237"* against total gross PP&E of $263,657k, and there is no corresponding cash line to
omit. Recorded sweep of the FY2021–FY2025 investing sections: **no instance found** of a
second capital line in any of them. **The CRWD failure mode does not exist here.**

**THE SPREAD CAVEAT IS LIVE, AND THE TRUE WIDTH IS 2.10x, NOT 1.26x.** Rebuilt over nine
windows and both (c) ends, the range is **$108.3M – $227.4M — a 110% width against the
published 26.5%.** Full grid at Q4.

**THE STEP FLAG POINTS AT THE RIGHT END OF THE SERIES THIS TIME, AND THE OPERATOR'S PRIOR
IS REFUTED.** `level_shift 1.64 "STEP UP — normalize down"` is computed on operating cash
flow, and on CRWD it pointed at a series that had already peaked and halved. **Qualys is the
opposite case: owner earnings are at their all-time high in the newest filed year, at both
ends of the band.** OE at the capex end: $130.1M (2022) → $166.7M (2023) → $154.6M (2024) →
**$227.4M (2025)**. The instruction to normalise down is nonetheless *correct here*, for a
reason the flag cannot see and which this run had to find in the tax note — see the
[E4-41] section at Q4, where **$25M of the 2025 step is a named legislative tax break.**

**`growth_required 0.0764` reproduces**: the screen solves `FLOOR − oe/cap` =
0.10 − 145/6,124 = 0.07632. It is a **perpetual** Gordon growth rate at a 10% discount rate,
not a fading ten-year rate. Both forms are stated at Q5. **On the corrected market cap and
the corrected windows the requirement is 6.17% to 8.18%, not a single 7.64%.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words, without management's language.** Qualys sells a
subscription to a scanning service. A customer tells Qualys which of its machines, web
applications, containers and cloud accounts it wants watched; Qualys runs software in
fifteen rented data centres that interrogates those assets, compares what it finds against a
catalogue of known software defects, and returns a ranked list of what is broken and how to
fix it. The customer pays a fee per year, sized by how many assets are in scope and how many
of the separately-priced modules are switched on. **The customer pays for the whole year up
front, at the start of the term**: the FY2025 10-K says *"We generally invoice our customers
for the entire subscription amount at the start of the subscription term."* That is why
deferred revenue is **$401.1M current** against $669.1M of annual revenue, and why the
business has never needed outside capital.

Where the money goes is unusually plain, and the plainness is the point:

| FY2025 | $M | % of revenue |
|---|---|---|
| Revenues | 669.1 | 100% |
| Cost of revenues | 114.8 | 17.2% |
| Research and development | 117.3 | 17.5% |
| Sales and marketing | 143.5 | 21.4% |
| General and administrative | 71.6 | 10.7% |
| **Operating income** | **222.0** | **33.2%** |
| Net income | 198.3 | 29.6% |
| Operating cash flow | 309.4 | 46.2% |
| **Capital expenditure** | **5.0** | **0.75%** |

**Gross margin is 82.9% and capital expenditure is three-quarters of one percent of
revenue.** Gross property and equipment is $263.7M against **$240.5M of accumulated
depreciation — the owned asset base is 91% written down** and net PP&E is $23.2M on a
$5,938M company. This is about as close to a business that requires no capital as a filer in
this queue gets.

**The scarce input this business controls.** Not the scanners and not the cloud — both are
rented, from third parties, on agreements the 10-K says run *"through 2030."* The scarce
input is **the vulnerability signature library and the scan logic built on top of it**: a
twenty-six-year accumulation of checks for specific software defects on specific versions of
specific products, plus the deployed sensor and appliance estate that already has credentialed
access inside customers' networks. A new entrant can buy the compute; it cannot buy the
back-catalogue of checks or the credentialed position, and the customer cannot easily
re-establish either. Note what is *not* scarce: the platform runs on somebody else's
hardware, in somebody else's buildings, under contracts with an end date.

**Two structural facts carried forward because they decide Q4 and Q5:**
- **Customers fund the entire business.** Total assets $1,095.1M, of which cash and
  marketable securities are **$696.8M** and goodwill $7.4M — leaving $390.9M of operating
  assets against $533.9M of liabilities that are overwhelmingly deferred revenue. **Operating
  capital employed is negative.** The liability is covenant-free and has no due date
  **[E3-52]**. There is no debt of any kind.
- **Stock compensation is a quarter of operating cash flow, and it is not rising.** $77.0M
  against $309.4M — **24.9%**. The ten-year band is 21.7% to 33.7% with no trend. This is the
  single sharpest contrast with the CRWD file, where the same ratio was **68.0% and rising in
  each of three years**, and where it decided the run.

**Will the fundamentals look broadly the same in ten years?** The revenue mechanism — pay
per year for a scanning subscription, pay more per module — is simple and I expect it to
survive. Whether *Qualys* is the one collecting it is the Q2 question and I do not waive it
here. R&D at 17.5% of revenue is materially lower than CrowdStrike's 28.8%, which cuts both
ways and is adjudicated at Q2 under **[E4-04]**. Qualys's own risk factors say the market is
*"characterized by rapid technological advances, **customer price sensitivity**, short product
and service life cycles, intense competition"* — a filed statement, repeated verbatim in every
one of the eight vintages read, that goes directly to [E3-03] criterion (2) and to
[E2-44]'s first half. It is recorded here and decided at Q2.

**Q1 asks whether I can understand how the money is made, and I can. It is a rented-compute
subscription with 83% gross margins, no capital, no debt, and customers who pay a year in
advance.**

- **VERDICT: [x] IN**
  *Recorded and carried forward: the filing's own "customer price sensitivity" language and
  the [E3-31] constant-change clause are live and are decided at Q2, not waived here.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** — yes. Vulnerability scanning is a compliance requirement, not a
  preference: PCI-DSS, FedRAMP and most regulated-industry regimes mandate periodic scanning.
- No close substitute **[ ]** — **FAILS. The evidence is below and it is the company's own.**
- Not price-regulated **[x]** — no price regulation.

### THE FILED METRIC, EVERY VINTAGE — AND THE OPERATOR'S FIRST PRIOR IS **REFUTED**

*The brief's instrument: "net dollar expansion/retention rate over every vintage it was
filed, and whether it was ever withdrawn or replaced with words **[E2-49]**."* **It was
never withdrawn and never replaced with words. Not once, in eighteen consecutive filings.**

| period | filing | net dollar expansion rate, as filed |
|---|---|---|
| FY2021 | 10-K 2023-02-23 (comparative) | **108%** |
| Q1 2022 | 10-Q 2023-05-04 (comparative) | **110%** |
| Q2 2022 | 10-Q 2023-08-03 (comparative) | **110%** |
| Q3 2022 | 10-Q 2023-11-02 (comparative) | **111%** ← peak |
| FY2022 | 10-K 2023-02-23 | **109%** |
| Q1 2023 | 10-Q 2023-05-04 | **109%** |
| Q2 2023 | 10-Q 2023-08-03 | **108%** |
| Q3 2023 | 10-Q 2023-11-02 | **106%** |
| FY2023 | 10-K 2024-02-22 | **105%** |
| Q1 2024 | 10-Q 2024-05-07 | **104%** |
| **Q2 2024** | 10-Q 2024-08-06 | **102%** ← **trough, published as a number** |
| Q3 2024 | 10-Q 2024-11-05 | **103%** |
| FY2024 | 10-K 2025-02-21 | **103%** |
| Q1 2025 | 10-Q 2025-05-06 | **103%** |
| Q2 2025 | 10-Q 2025-08-05 | **104%** |
| Q3 2025 | 10-Q 2025-11-04 | **104%** |
| FY2025 | 10-K 2026-02-20 | **103%** |
| Q1 2026 | 10-Q 2026-05-05 | **104%** |
| **Q2 2026** | **10-Q 2026-08-04** | **105%** |

**Three findings, and the first two run FOR the company.**

1. **[E2-49] DOES NOT FIRE. It fires the other way.** *"Yardsticks seldom are discarded while
   yielding favorable readings. But when results deteriorate, most managers favor
   **disposition of the yardstick rather than disposition of the manager**"* — and the demand
   is for *"pre-set, long-lived and small bullseyes."* Qualys **introduced** this metric in
   the 10-K filed 2023-02-23, at the top of the series, and then **published every falling
   quarter of it as an integer, including the 102% trough.** Set beside CrowdStrike — which
   replaced *"above 120%"* with *"our benchmark"* 91 days after the published number stopped
   being met — this is the candid case, and the contrast is the sharpest single difference
   between the two files. It is recorded as a **credit**, at Q3.
2. **THE DIRECTION HAS TURNED UP. The operator's prior that criterion (2) "fails here too,
   and possibly harder than CRWD" is REFUTED on its own instrument.** The trough was Q2 2024
   at 102%; the last four filed quarters read 103, 104, 104, 105. **[E4-32]** says direction
   outranks existence, and over the last eight quarters the direction is positive.
3. **AND THE LEVEL IS STILL THE PROBLEM, AND IT IS WHY THIS GATE FAILS.** 103–105% net
   dollar expansion means **the existing customer cohort pays 3 to 5 percent more each
   year** — at or barely above inflation, on a subscription that bills annually and where
   Qualys controls the list price. CrowdStrike, which failed this gate, was at **115%**.
   A business *"thought by its customers to have no close substitute"* **[E3-03](2)** does
   not extract three points a year from a base it has already sold. **The metric was kept
   honestly and it says the same thing an abandoned metric would have said.**

### **[E2-44] — BOTH HALVES, AND THEY SPLIT**

*Can it raise prices "even when product demand is flat and capacity is not fully utilized",
and grow dollar volume "with only minor additional investment of capital"?*

**HALF TWO PASSES, AND IT PASSES BETTER THAN ALMOST ANYTHING IN THIS QUEUE.** Total capital
expenditure was **$4,990k on $669,051k of revenue — 0.75%** — and the company guides
2026 capex to *"a range of $8.0 million to $12.0 million."* Working capital is a **source**:
deferred revenue rose $21.7M in 2025 and the current balance is $401.1M. Operating capital
employed is negative. Dollar volume grows on essentially no incremental capital. This half is
not a marginal pass; it is close to the ideal case the corpus describes.

**HALF ONE CANNOT BE EVIDENCED AS A PASS, AND THREE FILED SERIES POINT AGAINST IT.**

- **Qualys files no ASP, no price list, no per-asset price and no unit count of any kind.**
  Recorded sweep across all eight 10-K vintages (2018–2025): **no instance found** of an
  average selling price, a per-scanned-asset price, a seat price or any physical series.
  **[E4-55]** — *"where units exist, monitor units"* — cannot be run, because the units were
  never filed.
- **The one customer-count disclosure has been FROZEN for five consecutive years.** Item 1
  reads *"over 10,000 customers worldwide"* in the 10-Ks for FY2021, FY2022, FY2023, FY2024
  **and FY2025** — identical wording, identical floor, five vintages. (The pre-2021 series was
  on a different basis and is not comparable: *"over 12,200 customers and active users"*
  (FY2018), *"over 15,700"* (FY2019), *"over 19,000 customers, **including active subscribers
  of our free services**"* (FY2020).) A round-number floor repeated five times is not a
  series; it is the absence of one, and it is the [E4-55] hiding-place in its exact form —
  *"dollar revenue flattered by pricing is how a shrinking franchise hides"*, except here we
  cannot even see the pricing.
- **A customer-quality claim was quietly narrowed, and it is datable.** The FY2021 and FY2022
  10-Ks say the customer base includes *"a majority of each of the **Forbes Global 100 and
  Fortune 100**."* The FY2023 10-K, filed **2024-02-22**, says *"a majority of the Forbes
  Global 100."* Recorded sweep: **"Fortune 100" appears twice in each of the FY2021 and
  FY2022 10-Ks and zero times in the FY2023, FY2024 and FY2025 10-Ks.** No announcement, no
  reason given. It is a marketing sentence rather than a key metric and I am not going to
  inflate it — but it is the only customer-quality series filed, and it was cut without a word.

**THE PRICE EVIDENCE THAT DOES EXIST, AND IT IS IN THE REVENUE BRIDGE.** Qualys decomposes
its revenue increase every year — a genuinely above-average disclosure, credited at Q3 under
**[E2-26]** — and the decomposition carries the finding:

| of the annual revenue increase | 2023 | 2024 | 2025 | H1 2026 |
|---|---|---|---|---|
| from customers existing at the start | 80% | 69% | 76% | 91% |
| from new customers | 20% | 31% | 24% | 9% |
| **direct** | 46% | 20% | **20%** | **7%** |
| **through partners** | 54% | 80% | **80%** | **93%** |
| direct share of TOTAL revenue | 57% | 54% | **51%** | — |

**And the revenue-recognition footnote says what a partner sale is worth:** *"Sales to channel
partners are made **at a discount** and revenues are recorded at this discounted price over
the subscription terms."* **Four-fifths of the 2025 revenue increment, and 93% of the H1 2026
increment, arrived through the discounted channel while the direct share of total revenue fell
57% → 54% → 51%.** That is a realised-price mix shift downward, disclosed by the company, and
it is the closest thing to a price series this filer publishes. **[E4-37]** supplies the
inverse metric — *"you can almost measure the strength of a business over time by the agony
they go through in determining whether a price increase can be sustained"* — and there is no
filed evidence of a price increase attempted, taken or held in any of the eight vintages.

**STATED FAIRLY, AND THIS IS THE DIFFERENCE FROM CROWDSTRIKE.** CrowdStrike's MD&A said in
terms that customers *"have included discounting"* and that this *"[has] resulted, and [is]
expected to continue to result, in increased contraction."* **Qualys's MD&A says no such
thing.** What Qualys has is a *risk factor* — *"Larger competitors with more diverse product
and service offerings may reduce the price of products or subscriptions that compete with ours
or **may bundle them with other products and subscriptions** … which could increase pricing
pressure on our solutions and cause **the average sales price for our solutions to decline**"*
— and recorded sweep shows **that language is verbatim identical in the FY2019, FY2022 and
FY2025 10-Ks.** It is boilerplate. **It does not date a deterioration and I will not use it as
if it did.** The evidence that Qualys's realised price is under pressure is the channel-mix
shift and the 103% expansion rate, not the risk factor.

### **[E4-04] — MUST THE MOAT BE CONTINUOUSLY REBUILT?**

*The test: does a lapse in spending destroy the structure, or merely narrow it — and does the
spending defend the same advantage, or buy its replacement?*

**This is where Qualys reads BETTER than CrowdStrike and still does not clear.** R&D is
**$117.3M, 17.5% of revenue**, against CrowdStrike's 28.8%; and unlike CrowdStrike, Qualys has
made **essentially no acquisitions** — the last was Blue Hexagon in October 2022, whose
$1.5M escrow holdback was paid in 2024, and goodwill has been static at **$7.4M since 2019**.
Nothing here is buying a replacement moat. The spending defends the same asset: a
twenty-six-year vulnerability-signature library and the scan logic on top of it. That is the
Coca-Cola shape, not the Mitsui shape, and it is a real point for the company.

**But the structure it defends sits on rented ground.** The 10-K: *"We currently host
substantially all of our solutions from **third-party** shared cloud platforms located in the
United States, Canada, Switzerland, the Netherlands, United Arab Emirates, Australia, United
Kingdom, Italy, the Kingdom of Saudi Arabia and India … Our shared cloud platform agreements
have varying terms **through 2030**"* — and, in the risk factors, *"our existing shared cloud
platform providers have **no obligations to renew their agreements with us on commercially
reasonable terms, or at all**."* The **[E2-45]** attacker's test — *"how I would like, assuming
I had ample capital and skilled personnel, to compete with it"* — has an uncomfortable answer
here that it does not have for CrowdStrike: **the largest named competitors are the same
companies, or the customers of the same companies, that own the infrastructure Qualys rents.**

**Key-person dependence, recorded at Q2 as a moat defect [E4-23], not at Q3 as a strength:**
founder Philippe Courtot ceased to be CEO on 2021-03-19 and Sumedh Thakar has been CEO since
2021-04-27. **The moat survived the founder's departure** — revenue has grown every year since
and owner earnings are at a record. That is genuine [E4-23] evidence *in the company's favour*:
this is not a business whose moat goes when the surgeon goes.

### THE COMPETITOR ROW — REQUIRED **[E3-28]**

*"I can't be an intelligent owner of a business unless I know what all the other businesses in
that industry are doing."* Full working, with **thirty accession numbers** and verbatim quotes,
in `Test Runs/_research 2026-09-07 QLYS/COMPETITOR_ROW.md`.

**Peers named: 2 of the 2 head-on SEC-registered pure-plays**, plus CrowdStrike from its own
completed run of today's date. Buffett says eight; **standalone vulnerability management has
exactly two other US-listed pure-plays**, and every other competitor Qualys names is either
private (Invicti, Tanium, Wiz) or does not file a security-revenue line (Microsoft — the
blocked rung established by the CRWD run, where a recorded sweep of two Microsoft 10-K
vintages found **no filed security revenue figure at all**). **All three pure-plays have
December year ends, so the window is genuinely identical.**

| same metric, FY2025 (all FYE 2025-12-31) | **QLYS** | **TENB** | **RPD** |
|---|---|---|---|
| Revenue | $669.1M | $999.4M | $859.8M |
| Revenue growth | +10.1% | +11.0% | **+1.9%** |
| Gross margin | **82.9%** | 78.1% | 70.3% |
| **GAAP operating margin** | **+33.2%** | **(0.9)%** | **+1.3%** |
| GAAP net income | **$198.3M** | **$(36.1)M** | $23.4M |
| Operating cash flow | $309.4M | $266.8M | $153.8M |
| OCF as % of revenue | **46.2%** | 26.7% | 17.9% |
| Share-based compensation | $77.0M | $191.8M | $104.3M |
| **SBC ÷ operating cash flow** | **24.9%** | **71.9%** | **67.8%** |
| Total capex (both capital lines) | $5.0M | $16.6M | $23.7M |
| **OCF − SBC − capex** *(owner earnings, capex end)* | **$227.4M** | **$58.4M** | **$25.8M** |
| Goodwill | **$7.4M** | $697.9M | $593.3M |
| **Debt (principal)** | **NONE** | $358.1M term loan, matures 2028-07-07 | $900.0M convertibles, 2027 and 2029 |
| Cash + investments | **$696.8M** | $298.2M | $702.6M |
| **Net cash / (net debt)** | **+$696.8M** | **($59.9M)** | **($197.4M)** |
| Retention metric filed **today**? | **YES — 103% FY2025, 105% at Q2 2026** | YES — 106% FY2025 and Q2 2026 | **NO — withdrawn** |
| Retention direction | 111 → **102** → **105** *(bottomed, rising)* | 117 → 111 → 108 → **106** *(falling)* | 122 → 120 → 108 → 103 → **withdrawn** |
| Restructuring charges, last 3 years | **NONE, in any vintage** | 2023 $4.5M, 2024 $6.1M, 2025 $3.1M, **H1 2026 $3.1M** | 2023 **$22.2M / 16% of workforce**; new **12% cut approved 2026-08-07** |
| Shares outstanding, direction | **34,595,001, −12% in 5½ yrs** | 110,139,983, falling | **67,400,640, rising** |
| **EV ÷ owner earnings (capex end)** | **23.0x** | **65.6x** | **36.4x** |

**THIS ROW IS THE STRONGEST EVIDENCE IN THE FILE AND IT RUNS FOR QUALYS. I am going to state
it at full strength before I use anything against it [E4-51, E4-26].**

- **Qualys earns 3.9x Tenable's owner earnings on two-thirds of Tenable's revenue, and 8.8x
  Rapid7's.** On the same product, in the same market, in the same twelve months.
- **[E3-46]'s question is answered decisively.** *"the best businesses, by definition, are
  going to be businesses that earn very high returns on capital employed over time."* Qualys:
  33.2% operating margin on **negative** operating capital, no debt, $7.4M of goodwill in
  twenty-six years. Tenable: a GAAP loss, $697.9M of goodwill and a secured amortising term
  loan at 6.78–7.22%. Rapid7: a 1.3% operating margin, $900M of convertibles, a $957.5M
  accumulated deficit, and **ARR that has stopped moving — $839,819k (2024) to $839,850k
  (2025), +0.004%, and $824,020k at 2026-06-30, down 2.0% year on year.**
- **[E2-58]'s single named exception is present here.** *"The one exception is a cost
  advantage that is both **wide and sustainable** … By definition such exceptions are few."*
  A **34-point** GAAP operating-margin gap over the closest head-on peer, held and widened
  across six years (Qualys 26.6% in 2020 to 33.2% in 2025 while Tenable stayed at or below
  zero), on an identical product category, is as wide and as well-evidenced a cost advantage
  as a filed peer row in this queue has produced. **It is real, I am not discounting it, and
  it is why this name is priced where it is.**
- **[E4-32] direction, against the head-on peers: Qualys is the only one of the three whose
  moat metric is rising.** Its expansion rate bottomed at 102% and has printed six
  consecutive readings at or above 103, ending at **105%**. Tenable's has fallen from 117% to
  106% and is still falling. Rapid7 **withdrew** its renewal rate in the 10-K filed
  2022-02-24 after it went 122% → 103% and has filed nothing since — the [E2-49] case Qualys
  did not commit.
- **[E2-45]'s attacker's test, run on the peers' own conduct.** Tenable names *"Qualys"* in
  the competition section of **every vintage read, including the latest**. Rapid7 named
  Qualys in the FY2019 through FY2022 10-Ks and **deleted the named-competitor list in the
  10-K filed 2024-02-26** — a company that stops naming its competitors while its ARR goes
  flat. Neither peer has taken a pound of flesh out of Qualys's margin.
- **And neither peer has ever had to cut staff, while both of Qualys's competitors have.**
  Tenable has taken restructuring charges in four consecutive periods including H1 2026;
  Rapid7 cut 16% of its workforce in 2023 and its board approved a further **12% reduction on
  2026-08-07**. **Recorded sweep of all eight Qualys 10-K vintages for a restructuring
  charge, a workforce reduction or an impairment: no instance found.**

**THE ROW'S LIMIT, STATED [E3-61].** *"In some businesses, the participants behave like a
demented Kellogg. In other businesses, they don't … I think you'd have to know the people
involved."* And two limits specific to this row. First, **it is a row of the wrong three
companies for the actual threat.** The competitors that matter to the Q2 question are the ones
Qualys names in its own filing and that this row cannot contain: CrowdStrike, Palo Alto
Networks, Microsoft and Wiz — the last now acquired by Google. Microsoft's rung is blocked, as
the CRWD run established; **the platform-bundling question is therefore unresolvable from
filings, and the Q2 verdict below does not rest on it.** Second, **winning a shrinking pool is
not the same as owning one.** Rapid7's ARR is flat and Tenable's expansion rate is decaying
toward Qualys's; the row shows Qualys is the best of three, and says nothing about whether
three is the right number.

**THE STRONGEST FACT AGAINST QUALYS IN THE ROW, AND IT IS ONE THE ROW MAKES POSSIBLE TO SEE.**
Tenable serves **"over 40,000 customers"** and Rapid7 **11,674**, against Qualys's **"over
10,000."** Tenable has four times the customer count and one and a half times the revenue.
**Customers demonstrably buy the substitutes**, in very large numbers, and Qualys's own
customer count has not been given a new number in five years. Qualys's superiority in this row
is a superiority of **margin**, not of **position** — and [E3-03] criterion (2) is a question
about position.

**AND THE ROW SOFTENS TWO OF MY OWN CRITICISMS, WHICH IS WHY IT WAS BUILT [E4-26].**
- **The frozen customer count is an industry habit, not a Qualys habit.** Tenable filed
  *"approximately 43,000"* (FY2022) and *"approximately 44,000"* (FY2023 **and** FY2024), then
  **loosened it to *"over 40,000"* in the FY2025 10-K filed 2026-02-27** — a *less* precise
  disclosure than the one it replaced, in the same direction as Qualys's five-year *"over
  10,000."* Rapid7's customer count **fell for the first time** in FY2025 (11,727 → 11,674).
  Qualys's frozen count is still a real defect at [E4-55]; it is not evidence that Qualys is
  worse than its peers on disclosure. On the metric that matters most — the expansion rate —
  Qualys is the most forthcoming of the three.
- **How bad the alternative is, in one filed number.** At $11.00 on 2026-09-04, **Rapid7's
  entire market capitalisation of $741.4M is less than the $900.0M principal of its own
  convertible notes**, and its 2027 Notes were reclassified to current at 2026-03-31. This is
  the industry Qualys is winning, and its condition is part of why Qualys's margin gap has
  been allowed to persist.

### THE Q2 VERDICT

- **Untapped pricing power [E3-33] / [E5-28]? NO, and the class is foreclosed.** *"If you name
  some business that has incredible pricing power, you're talking about a business that's **a
  monopoly or a near monopoly**"* **[E5-28]** — claiming the class is claiming near-monopoly,
  and the row does not support it. Qualys is roughly a quarter of the filed revenue of the
  three pure-plays and has a quarter of Tenable's customer count.
- Class: **NARROW.** · Direction: **rising against the two head-on peers, unmeasurable against
  the platform bundlers, and negative on realised price mix.**
- **VERDICT: [x] OUT — on [E3-03] criterion (2).**

**AND THIS IS THE CLOSEST Q2 CALL THIS QUEUE HAS PRODUCED. I am going to say what would make
it wrong, because it very nearly is.**

**The case for IN, stated as well as I can state it [E4-51]:**

> Qualys earns a **33.2% GAAP operating margin and 82.9% gross margin on negative operating
> capital**, in a year in which its two head-on competitors earned **(0.9)%** and **1.3%** and
> both were cutting staff. That gap is 34 points wide, it has been held for six years, and it
> has *widened*. **If customers genuinely regarded Tenable and Rapid7 as close substitutes at
> the price, that gap could not persist — price would have converged.** It has not. Margin
> persistence against named, funded, listed, head-on competitors is the substitute test run on
> filed data rather than on adjectives, and Qualys passes it. Its expansion rate bottomed two
> years ago and has risen for six straight readings while Tenable's fell and Rapid7's was
> withdrawn. It has published every falling quarter of that metric as an integer. It has no
> debt, $696.8M of cash, $7.4M of goodwill in twenty-six years, no restructuring charge ever,
> no litigation, no investigation, and a 12% smaller share count than five years ago. **On
> [E2-58]'s one named exception — "a cost advantage that is both wide and sustainable" — this
> is the exception.**

**Why it still does not carry the gate, and the reasoning is narrow enough to be attacked:**

1. **[E2-58] offers that exception as a rescue for PROFITABILITY, not as a route into the
   franchise class, and it says so in its own terms.** The equation it belongs to is
   *"persistent over-capacity without administered prices (or costs) equals poor
   profitability"*; the wide-and-sustainable cost advantage is what lets a participant escape
   the poor profitability. **It does not make the market's substitutes stop existing.** And
   **[E3-62]'s second step** asks the question that decides which way a cost advantage runs:
   *"how much is going to stay home and how much is just going to flow through to the
   customer."* Qualys's advantage is staying home **today** at a 33% margin. The channel-mix
   shift — direct revenue 57% → 54% → **51%** of the total, and **93% of the H1 2026 revenue
   increment arriving through a channel the filing says is sold "at a discount"** — is that
   question being answered in real time, in the wrong direction.
2. **[E3-03](2) asks what customers think, and the filed answers are the company's own.**
   Qualys names **seven** competitors in a market it calls *"highly fragmented and
   competitive"*; its risk factors, in every one of eight vintages, describe a market
   *"characterized by … **customer price sensitivity**"*; and the substitutes are bought at
   scale — Tenable serves four times as many customers. A product *"thought by its customers
   to have no close substitute"* does not sit in a market its own vendor describes that way.
3. **The installed base pays three to five percent more a year, and that is the whole answer
   to [E2-44] half one.** 103–105% net dollar expansion, filed eighteen times. **[E4-37]**
   gives the inverse metric — *"you can almost measure the strength of a business over time by
   the agony they go through in determining whether a price increase can be sustained"* — and
   there is **no filed evidence of a price increase attempted, taken or held in any vintage.**
   Half two of [E2-44] passes emphatically; half one cannot be evidenced at all, and the one
   proxy that exists says the answer is "roughly inflation."
4. **[E4-55] cannot be run, and the absence is not neutral.** *"Where units exist, monitor
   units … dollar revenue flattered by pricing is how a shrinking franchise hides; the
   physical series is the honest one."* Qualys files **no ASP, no per-asset price, no seat
   count and no unit series of any kind**, and its one customer disclosure has read *"over
   10,000 customers worldwide"* in five consecutive 10-Ks. The honest series does not exist,
   and the framework does not let an unmeasurable moat be graded IN.

**WHAT WOULD FLIP THIS VERDICT, NAMED IN ADVANCE SO IT IS FALSIFIABLE.** Any one of:
**(a)** the net dollar expansion rate filed at **110% or above for four consecutive
quarters**; **(b)** a filed customer count that moves — any new number replacing *"over
10,000"*, in either direction, so that a unit series exists again; **(c)** a filed statement
of a list-price increase taken and held, or the restoration of the direct share of revenue
above 57%; or **(d)** the disclosure of actual bookings, which would let the register compute
the leading indicator management pays itself on. **Each is a document I can name, so this
verdict is reviewable — but it is OUT and not UNRESEARCHED, because the documents that exist
have all been read and they answer the question as it stands.**

**Q2 CLOSES THE FILE. Everything below this line is recorded because the operator's brief
asked for it and because a closed file still owes the register its findings. None of it is a
verdict, and per operator rule 2 none of it can promote the name.**

---

## Q3 ITEMS — RECORDED. **[E2-01, E2-26, E2-49, E3-48, E4-22, E4-29, E4-31, E5-08]**

**STEP 1 — THE WEIGHT CASE, DECLARED. Nothing below counts until this is filled in.**

- **Daily execution [E3-38, E2-70]** — **[x] TICKED.** Qualys runs credentialed scanning
  agents and appliances *inside* customers' networks and ships signature updates
  continuously. The 10-K's own risk factors name *"defects, errors or vulnerabilities"* and
  the possibility that the platform *"may be used to gain unauthorized access"*. This is the
  [E2-70] shape — the product is a promise, renewed daily — and one bad update on one day
  is the CrowdStrike precedent in the same industry. **Q3 is a BINARY GATE for this
  business, not an overlay, and no price compensates [E1-16, E3-29, E5-35].**
- Control **[ ]** — not ticked. Marketable minority position, exit available.
- Leverage **[ ]** — not ticked. **Zero debt of any kind.**

**HONESTY BINARY [E5-16] — RECORDED SWEEP, AND IT IS CLEAN.** The FY2025 10-K Legal
Proceedings note reads in full: *"As of December 31, 2025, there has not been at least a
reasonable possibility that the Company has incurred a material loss from any ongoing legal
proceedings, individually or taken together."* Recorded sweep of all eight 10-K vintages and
twelve 10-Qs for a Department of Justice inquiry, an SEC investigation or subpoena, a
securities class action, a derivative suit, a restatement or a material weakness: **no
instance found.** The auditor is **Grant Thornton LLP**, and the audit report states *"We
have served as the Company's auditor since 2005"* — twenty-one consecutive years, no auditor
change to date. **This is the single largest contrast with the CRWD file, which carries an
open DOJ and SEC information request into revenue recognition and ARR.** Under [E5-17] this
is *the absence of found disqualifiers, not a finding that the managers are honest.*

**STEP 2 — THE FLAGS. Each is a prompt to READ, never a verdict [E5-36, E5-38].**

- **weak accounting [ ]** — does not fire. Stock compensation is expensed in full and shown
  on the face of the cash-flow statement as *"Stock-based compensation, net of amounts
  capitalized"*; no pension; no material estimates outside tax. No restatement, no revision,
  no identified error in any vintage read.
- **unintelligible footnotes [ ]** — does not fire. The notes are short and plain; the
  revenue-recognition note states the channel-discount mechanism in one sentence.
- **trumpeted earnings projections / growth targets [x] FIRES — see the proxy findings
  below [E3-48, E5-30].**
- **serial share issuance [ ]** — does not fire, and fires **inverted [E5-15]**. Shares
  outstanding: **39.3M (2020-12-31) → 39.1M → 37.4M → 36.9M → 36.5M → 35.7M (2025-12-31) →
  34,595,001 (10-Q cover, 2026-07-22).** A **12.0% net reduction in five and a half years**
  after all option, RSU and ESPP issuance. There is no issuance flag here to read.
- **EBITDA / adjusted-earnings promotion [x] FIRES, AND IT IS THE FIFTH FLAG IN ITS EXACT
  FORM [E4-29].** *"Trumpeting EBITDA … is a particularly pernicious practice. Doing so
  implies that depreciation is not truly an expense, given that it is a 'non-cash' charge.
  That's nonsense."* Adjusted EBITDA is the **headline non-GAAP metric of the 10-K itself**,
  in a section titled *"Key Operating and Non-GAAP Financial Performance Metrics"*, in every
  one of the eight vintages read (13 to 15 occurrences of "EBITDA" per filing). **$313.4M of
  Adjusted EBITDA against $222.0M of GAAP operating income and $198.3M of net income — a
  41% and 58% uplift.** And it is not only reported: **"Adjusted EBITDA Margin" is one of
  the four measures the company names in Item 402(v) as most important for linking pay to
  performance, and it is one of the two PRSU vesting metrics.** *(Stated fairly, and this is
  the strongest mitigation available: the 10-K prints the full reconciliation from net
  income, and lists the limitations itself, including — remarkably — the exact objection
  [E4-29] makes: "Adjusted EBITDA excludes depreciation and amortization of property and
  equipment and amortization of intangible assets, although these are non-cash charges,
  **the assets being depreciated and amortized may have to be replaced in the future**."
  That is the company arguing the corpus's case against its own metric, in its own filing.
  The flag still fires — [E5-41]'s reverse-float mechanism is unaffected by disclosure — but
  the disclosure conduct is candid and is credited.)*
- **filed-figure tells [E4-30] — one half fires and one half does not.**
  - *Unnaturally smooth reported growth:* **does not fire.** Revenue growth by year:
    16.6%, 20.8%, 15.3%, 12.9%, 13.3%, 19.1%, 13.2%, **9.6%, 10.1%**. Net income fell in
    2021 ($91.6M → $71.0M). Neither series is smooth.
  - *Cash taxes falling as a share of reported pretax income:* **fires as a prompt, and the
    reading resolves it.**

| FY | pretax income | cash taxes paid, net | **cash tax %** |
|---|---|---|---|
| 2019 | $80.0M | $3.0M | 3.8% |
| 2020 | $102.0M | $8.1M | 7.9% |
| 2021 | $89.4M | $35.1M | **39.2%** |
| 2022 | $133.7M | $39.7M | 29.7% |
| 2023 | $178.7M | $34.9M | 19.5% |
| 2024 | $209.8M | $60.6M | 28.9% |
| **2025** | **$246.8M** | **$40.9M** | **16.6%** |

  The series is not monotone and the 2025 fall has a named, dated, public legislative cause
  which the filing states: *"On July 4, 2025, the One Big Beautiful Bill Act (OBBBA) was
  signed into law … Beginning in 2025, the OBBBA provides an **elective deduction for
  domestic research and development expenses** and a reinstatement of elective 100%
  first-year bonus depreciation."* **The flag was right to fire and reading it produced the
  single most important adjustment in this run — not a Q3 finding but a Q4 one, at [E4-41].**

**[E2-49] METRIC-SWITCHING — DOES NOT FIRE ON DISCLOSURE, FIRES ONCE ON PAY.** The
disclosure half is the credit recorded at Q2: eighteen consecutive filings of the net dollar
expansion rate, through a nine-point decline, never withdrawn and never replaced with an
adjective. On pay, one change is on the record and the proxy dates it itself: *"For each of
the three equally-weighted metrics, the payout percentage was capped at 125% of target.
**In 2023 and previous years, the payout percentage overall and for each metric was capped at
100% of target.**"* The cap was raised, with a stated reason (*"to incentivize top-end
performance"*) — announced-with-reasons is the candid form [E2-49] itself distinguishes, and
the raise came in growing years, not deteriorating ones. Recorded, not scored against.

**[E3-48] THE PROJECTIONS FLAG — IT FIRES, AND THE PROXY SHOWS WHERE THE BULLSEYES WERE
DRAWN.** *"pull the company's own past guidance and set it against outturn."* The 2025
Corporate Bonus Plan, as filed in the DEF 14A of 2026-04-22:

| 2025 quarterly bonus metric | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| Revenue growth **target** | 9.1% | 10.1% | 10.3% | 9.2% |
| Revenue growth **actual** | 9.7% | 10.3% | 10.4% | 10.1% |
| payout | 125% | 105% | 103% | 117% |
| Non-GAAP EPS **target** | $1.51 | $1.44 | $1.55 | $1.60 |
| Non-GAAP EPS **actual** | **$1.67** | **$1.68** | **$1.86** | **$1.87** |
| payout | **125%** | **125%** | **125%** | **125%** |
| Bookings growth target | 6.5% | 9.4% | 11.4% | 9.1% |
| Bookings growth **actual** | **not disclosed** | **not disclosed** | **not disclosed** | **not disclosed** |
| payout | 125% | 125% | 80% | 121% |
| **Weighted payout** | **125%** | **119%** | **102%** | **121%** |

Three findings, in ascending order of seriousness:

1. **The non-GAAP EPS leg paid the 125% maximum in all four quarters of 2025**, beating
   target by 11%, 17%, 20% and 17%. A bullseye hit at the cap four times out of four is not
   *"pre-set, long-lived and small"* **[E2-49]**; it is a floor dressed as a target.
2. **Two of the four quarterly revenue-growth targets were set BELOW the prior full year's
   actual.** 2024 revenue growth was **9.6%**; the Q1 2025 target was **9.1%** and the Q4
   2025 target was **9.2%**. This is the target-below-actual test that has now replicated
   across this queue, hit here on two of four quarters — weaker than the CRWD hit (which was
   on the 70%-weighted metric) but present. *(Stated fairly: the Q2 and Q3 targets were set
   above prior-year actual, and the company beat all four.)*
3. **THE SHARPEST FINDING IN THE PROXY, AND IT IS A DISCLOSURE FINDING, NOT A PAY ONE.**
   One-third of the entire executive cash bonus is paid on **bookings growth**, and the
   proxy states: *"With respect to actual bookings growth rate … this is an internal measure
   that **we do not disclose** for several reasons, including our belief that disclosure
   would result in **competitive harm** to the Company."* **The targets are published; the
   results are withheld.** Shareholders are told what management was aimed at and are not
   told whether it was hit, on a metric that is one of the four the company itself names as
   most important. Under **[E2-26]** — *"tell you the business facts that we would want to
   know if our positions were reversed"* — this fails. Under **[E4-31]** it does more than
   that: see the buyback section below.

**[E4-52] — DO THE FLAGS CONVERGE?** Three fire: EBITDA promotion, the projections/targets
flag, and the withheld bookings result. **They point at one thing, and it is the same thing:
the company's public scorecard is built out of measures that delete depreciation, delete
stock compensation from EPS, and withhold the leading indicator.** That is a confluence in
[E4-52]'s sense and it is read as one system, not three prompts. **What it is NOT is the
CrowdStrike lollapalooza**, which added metric-withdrawal, serial issuance and an open DOJ
inquiry on top. Here the register can still check the company: GAAP is complete, the retention
metric is filed every quarter, the share count falls, and nothing is under investigation.

**STEP 3 — THE PRIMARY TEST [E2-01].** *"a high earnings rate on equity capital employed
(without undue leverage, accounting gimmickry, etc.) and not the achievement of consistent
gains in earnings per share."*

| FY | net income | average equity | **ROE** | operating margin |
|---|---|---|---|---|
| 2019 | $69.3M | $372.4M | 18.6% | 22.5% |
| 2020 | $91.6M | $395.6M | 23.1% | 26.6% |
| 2021 | $71.0M | $420.6M | 16.9% | 21.3% |
| 2022 | $108.0M | $362.9M | 29.8% | 26.7% |
| 2023 | $151.6M | $328.7M | **46.1%** | 29.4% |
| 2024 | $173.7M | $422.6M | **41.1%** | 30.8% |
| 2025 | $198.3M | $519.1M | **38.2%** | **33.2%** |

**The number is high and rising and it must be read with two corrections, one in each
direction.**
- **Against the company:** equity is being shrunk by buybacks, which mechanically lifts ROE.
  The denominator fell from $436.7M (2021) to $289.1M (2022) because $317.3M of stock was
  retired. Part of the 46.1% in 2023 is arithmetic, not performance.
- **For the company, and it is the larger correction [E2-43, E3-46]:** the honest denominator
  is *unleveraged net tangible assets*, and it is **negative**. Total assets $1,095.1M, less
  cash and marketable securities $696.8M, less goodwill $7.4M, leaves **$390.9M of operating
  assets against $533.9M of liabilities that are overwhelmingly customer prepayments.**
  **Operating capital employed is roughly negative $143M.** [E3-46]'s question — *"the best
  businesses, by definition, are going to be businesses that earn very high returns on
  capital employed over time"* — is answered as emphatically as it can be: **$222.0M of
  operating income on negative operating capital.** This run declines to print a ratio with a
  negative denominator, exactly as the CRWD run did, and states the finding in words instead.

**THE HALF-OWNER TEST [E2-26] — MIXED, AND THE POSITIVE HALF IS UNUSUAL.** Qualys publishes,
every year, a decomposition of its revenue *increase* into existing versus new customers,
United States versus foreign, and direct versus partner. Very few filers in this queue do
that, and it is the disclosure that produced the sharpest **negative** finding in this run
(the channel-mix shift at Q2). A company that publishes the number that damages its own case
is meeting [E2-26]. **Set against that: the bookings actuals are withheld, no ARR is filed,
no unit count, no ASP, and the customer count has been "over 10,000" for five years.**

**THE INSTITUTIONAL IMPERATIVE — SCORE ALL FOUR [E2-30].** *Not a fraud test.*
- **[x] resists any change in current direction** — the "over 10,000 customers" sentence, the
  identical risk-factor language across seven years, and a strategy statement unchanged since
  2018. Fires, mildly.
- **[ ] projects/acquisitions materialise to soak up available funds** — **does not fire, and
  the absence is the strongest capital-allocation fact in the file.** Goodwill has been
  **$7.4M since 2019**; one small acquisition (Blue Hexagon, October 2022) in seven years;
  $696.8M of cash left uninvested rather than spent. This is the opposite of the imperative.
- **[ ] staff studies produced to justify the leader's craving** — no instance found.
- **[ ] peer behaviour mindlessly imitated** — **does not fire, and again the absence is
  notable.** The entire peer group has been acquiring platforms and withdrawing metrics;
  Qualys has done neither.

**CAPITAL ALLOCATION — THE BUYBACK, AND ALL THREE CONDITIONS [E5-08, E4-31, E5-24].**

| FY | cash repurchased | shares retired | **average price** |
|---|---|---|---|
| 2018 | $85.0M | — | — |
| 2019 | $86.4M | — | — |
| 2020 | $126.7M | — | — |
| 2021 | $130.0M | — | — |
| 2022 | $317.3M | — | — |
| 2023 | $170.8M | 1,342k | **$127.59** |
| 2024 | $139.9M | 993k | **$141.77** |
| 2025 | $183.4M | 1,361k | **$135.14** |
| Q4 2025, monthly | — | 328,162 | $128.13 / $140.46 / **$143.10** |
| H1 2026 | **$131.4M** | — | — |

Cumulative 2018–2025: **$1,239.5M of cash returned**, against an aggregate authorisation
raised to **$1.6bn on 2026-02-05**.

- **Condition (1) — ample funds for operations and liquidity? YES, and it is not close.**
  $696.8M of cash and marketable securities, **zero debt**, $309.4M of operating cash flow,
  and total named near-term requirements of roughly $50M (2026 lease payments $11.0M, 2026
  purchase commitments $28.1M, guided capex $8–12M).
- **Condition (2) — a material discount to conservatively calculated intrinsic value?**
  **This one is answered against the run's own Q5 range and it does not pass.** Every
  repurchase in the last three years was struck between **$127.59 and $143.10**; the
  conservative end of the value range computed below is **roughly $50 to $65 a share** at the
  [E4-28] floor. On my own numbers the company has been buying at roughly twice the
  conservative case, and above the top of the whole floor-based range at 5% growth ($85–93).
  **CAPITAL-ALLOCATION FLAG, stated with the humility clause [E4-13]:** *"it is natural for
  CEOs to be optimistic about their own businesses. **They also know a whole lot more about
  them than I do.**"* This rests entirely on my own range; **the flag binds position size,
  never the discount rate.** And it must be stated the other way too, because [E5-24] governs
  — *"what is smart at one price is dumb at another"* — **every one of those repurchases was
  struck 17% to 26% below today's $171.65 quote.** Against the market, management's timing has
  been good; against value, it has not. Both are true and the second is the one the framework
  scores.
- **Condition (3), the earliest full statement [E4-31] — "Shareholders should have been
  supplied all the information they need for estimating that value." IT FAILS, AND THE PROXY
  SAYS SO IN TERMS.** The company withholds actual bookings — one of the four measures it
  names as most important, one-third of the executive cash bonus — on the stated ground of
  *"competitive harm"*; files no ARR; files no customer count beyond a five-year-frozen
  *"over 10,000"*; and files no price or unit series of any kind. **A $1.24bn buyback has been
  executed against a register that cannot compute the leading indicator management pays
  itself on.** This is the cleanest [E4-31] failure this queue has produced.

**THE GUARDRAIL — CHECKED BEFORE ANY VERDICT [E2-37, E2-38, E3-39].**
- [x] Confirmed: nothing in this Q3 is used to promote the name. The clean legal record, the
  unbroken metric disclosure and the shrinking share count are real and **cannot repair Q2.**
  *"betting on the quality of a business is better than betting on the quality of
  management"* **[E3-39]**.
- [x] Key-person dependence was recorded **at Q2** as a moat item **[E4-23]**, and it was
  recorded as evidence *for* the moat: the founder left in 2021 and the business kept
  compounding.
- [x] No great-manager exception is being claimed **[E2-35, E2-36]**. The franchise question
  is decided on the franchise.

---

## Q4 ITEMS — RECORDED. **[E2-23, E4-25, E4-38, E4-41, E5-11, E2-54, E3-52]**

### OWNER EARNINGS, BY YEAR AND BY WINDOW — EVERY WINDOW PUBLISHED **[E4-38]**

*OE = OCF − SBC − (c), from the filed cash-flow statements. Figures $M.*

| FY | OCF | SBC | OCF−SBC | capex | D&A | **OE @ (c)=capex** | **OE @ (c)=D&A** | revenue | SBC÷OCF |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 69.3 | 20.1 | 49.2 | 23.2 | 17.0 | 25.9 | 32.2 | 197.9 | 29.1% |
| 2017 | 107.6 | 27.0 | 80.7 | 37.8 | 20.6 | 42.9 | 60.0 | 230.8 | 25.0% |
| 2018 | 125.5 | 30.1 | 95.4 | 22.8 | 28.9 | 72.6 | 66.5 | 278.9 | 24.0% |
| 2019 | 160.6 | 34.9 | 125.7 | 27.6 | 31.2 | 98.1 | 94.5 | 321.6 | 21.7% |
| 2020 | 180.1 | 40.0 | 140.1 | 30.0 | 32.8 | 110.0 | 107.2 | 363.0 | 22.2% |
| 2021 | 200.6 | 67.6 | 133.0 | 24.4 | 35.9 | 108.6 | 97.1 | 411.2 | 33.7% |
| 2022 | 198.9 | 53.4 | 145.4 | 15.4 | 34.6 | 130.1 | 110.8 | 489.7 | 26.9% |
| 2023 | 244.6 | 69.1 | 175.5 | 8.8 | 27.0 | 166.7 | 148.5 | 554.5 | 28.2% |
| 2024 | 244.1 | 77.1 | 167.0 | 12.3 | 18.5 | 154.6 | 148.4 | 607.6 | 31.6% |
| **2025** | **309.4** | **77.0** | **232.4** | **5.0** | **14.5** | **227.4** | **217.9** | **669.1** | **24.9%** |

**Sixteen consecutive years of positive owner earnings at both ends of the band.** There is
no loss year anywhere in the filed history.

**THE WINDOW GRID — NINE WINDOWS, BOTH (c) ENDS [E4-25, E4-38]**

| window | OE @ (c)=capex | OE @ (c)=D&A |
|---|---|---|
| 2025 only | 227.4 | 217.9 |
| 2023–2025 (3yr) | 182.9 | 171.6 |
| 2022–2025 (4yr) | 169.7 | 156.4 |
| **2021–2025 (5yr — the corpus default [E2-42])** | **157.5** | **144.6** |
| 2020–2025 (6yr) | 149.6 | 138.3 |
| 2019–2025 (7yr) | 142.2 | 132.1 |
| 2018–2025 (8yr) | 133.5 | 123.9 |
| 2016–2025 (10yr) | 113.7 | 108.3 |
| 2020–2024 (5yr, ending one year earlier) | 134.0 | 122.4 |
| 2019–2023 (5yr, ending two years earlier) | 122.7 | 111.6 |

**THE TRUE RANGE IS $108.3M – $227.4M — a 2.10x width (110%), against the published 26.5%.
The operator's spread caveat is CONFIRMED for the eighth consecutive run**, and the width
here comes almost entirely from the **window**, not from the capex band. The two axes,
separated:
- **Window axis, holding (c) constant at capex:** $113.7M (10yr) to $227.4M (2025) — **2.00x.**
- **Capex axis, holding the window constant at five years:** $144.6M to $157.5M — **1.09x.**

**THAT IS THE OPPOSITE OF THE USUAL CASE AND IT IS ITSELF THE FINDING.** For most filers in
this queue the capex band is the source of width. For Qualys the (c) judgment is nearly
irrelevant — **the whole distance between "maintenance capex" and "D&A" is $9.5M on a base of
$232.4M, four percent** — because the business consumes almost no capital. The width is the
**level shift**, and the level shift is what [E4-41] is written for.

### **(c) — THE DIRECTION TEST [E3-44, E2-41, E5-20], AND [E5-20] INVERTS HERE**

**Which case is this?** The corpus default is that D&A is a fair proxy for (c) **[E3-44,
E2-41]**; the exception class is the business whose own filing shows depreciation understates
renewal **[E5-20]**. **Qualys is in neither. It is the mirror of [E5-20]: depreciation
OVERSTATES cash renewal, and has for four consecutive years.**

| FY | total capex | total D&A | capex ÷ D&A |
|---|---|---|---|
| 2020 | $30.0M | $32.8M | 0.91x |
| 2021 | $24.4M | $35.9M | 0.68x |
| 2022 | $15.4M | $34.6M | 0.45x |
| 2023 | $8.8M | $27.0M | 0.33x |
| 2024 | $12.3M | $18.5M | 0.67x |
| **2025** | **$5.0M** | **$14.5M** | **0.34x** |

**Why, from the filing and not from inference.** Gross property and equipment is $263,657k
against **$240,491k of accumulated depreciation — 91% written down** — and gross PP&E grew
only $2.5M in 2025. The renewal has moved off the balance sheet: the platform runs on
**third-party** shared cloud facilities under agreements *"through 2030"*, and the company
took on **$14,559k (2025) and $30,639k (2024) of new operating-lease right-of-use assets**
against $121k in 2023. **The cash cost of that renewal is already inside operating cash flow**
— *"Cash payments included in the measurement of lease liabilities $12,336"* in 2025, plus
$60.2M of non-cancelable cloud-infrastructure purchase obligations of which $13.2M falls
within twelve months, all paid out of operations. **So the band is not distorted by an
off-cash-flow renewal channel, and neither end is invalid.**

**RECORDED SWEEP ON THE FINANCE-LEASE DEFECT** (the class found by the COST and HD runs,
addendum 2026-09-01): the PP&E note says property and equipment *"includes assets under
finance leases"*, so the tag was checked. **The FY2025 financing section contains no finance-
lease principal-payment line, the lease maturity table is headed "operating lease
liabilities" only, and no finance-lease liability is separately disclosed.** No instance
found; the defect does not bite here.

**(c) IS DISCLOSED AS A JUDGMENT AND THE JUDGMENT IS: SIT AT THE D&A END.** The corpus
default governs **[E3-44]** — *"by and large, the depreciation charge is not inappropriate in
most companies to use as a proxy for required capital expenditures"* — and here it is also
the conservative end, so no windage is being spent to choose it. Two supporting filed facts:
the company guides 2026 capex **up** to *"a range of $8.0 million to $12.0 million"* from
$5.0M, and D&A is still falling toward capex, so the two ends are converging. **The 2025
capex of $5.0M is the lowest in nine years and is not a maintenance level I would project.**

### **[E4-41] — NORMALIZE THE MEAN DOWN FOR LUCK. THE 2025 STEP IS 40% LEGISLATED.**

> *"Favourable exogenous breaks in the window are named and removed before the mean is
> trusted."* — the corpus's only pro-forma that disclosed earnings too **high**. **[E4-41]**

**The screen's `level_shift 1.64 "STEP UP — normalize down"` is right, and it is right for a
reason computed on operating cash flow that cannot see the cause.** Operating cash flow rose
**$65.3M** in 2025, from $244.1M to $309.4M — 27% growth against 10.1% revenue growth. The
cash-flow statement itself supplies the bridge:

| driver of the 2025 OCF increase | $M |
|---|---|
| net income | +24.6 |
| **deferred income taxes** (2024 −19.5 → 2025 +8.4) | **+27.9** |
| depreciation and amortization | −4.0 |
| working-capital movement | +13.2 |
| other | +3.6 |
| **total** | **+65.3** |

**Forty-three percent of the entire 2025 step is one line: the deferred-tax swing.** The
10-K names its cause and dates it: *"On July 4, 2025, the One Big Beautiful Bill Act (OBBBA)
was signed into law … Beginning in 2025, the OBBBA provides an **elective deduction for
domestic research and development expenses** and a reinstatement of elective 100% first-year
bonus depreciation."* Cash taxes paid **fell from $60.6M to $40.9M while pretax income rose
from $209.8M to $246.8M** — a cash tax rate of **16.6% against a five-year mean of 26.8%.**

**THE ADJUSTMENT, DISCLOSED AS A JUDGMENT.** Restoring 2025 cash taxes to the five-year mean
rate (26.8% × $246.8M = $66.1M) removes **$25.2M** from operating cash flow. The independent
cross-check — the deferred-tax swing itself — gives **$27.9M**. The two bracket each other,
and this run takes **$25M**, at the smaller end. *(Why not more: OBBBA's R&D expensing is a
permanent regime change, so part of the benefit does recur. Why not zero: 2025 also carries
the catch-up of previously capitalised domestic R&D, which does not recur, and $25M of a
$65M step is the conservative attribution. This is one place where conservatism is spent —
see the windage count at Q5.)*

**THE NORMALIZED GRID:**

| window | OE @ (c)=capex | **OE @ (c)=D&A** |
|---|---|---|
| 2025 only, normalized | 202.2 | 192.7 |
| 2023–2025 (3yr) | 174.5 | 163.2 |
| **2021–2025 (5yr — corpus default)** | **152.4** | **139.5** |
| 2019–2025 (7yr) | 138.6 | 128.5 |
| 2016–2025 (10yr) | 111.2 | 105.8 |

**NORMALIZED TRUE RANGE: $105.8M – $202.2M, a 1.91x width.** The published row's $145–183M
sits inside it and represents neither end.

**AND THE SECOND HALF OF THE LEVEL QUESTION, WHICH THE FLAG ALSO CANNOT SEE.** Owner earnings
at the capex end grew from $108.6M (2021) to $227.4M (2025) — **20.3% a year**, which looks
like a growth business. It is not, and the decomposition says why:

| source of the $118.8M increase in OE @ capex, 2021 → 2025 | $M | share |
|---|---|---|
| growth in OCF − SBC | +99.4 | 84% |
| **capex falling from $24.4M to $5.0M** | **+19.4** | **16%** |

**The capex tailwind is exhausted** — capex cannot fall below zero and the company guides it
up — and **at the D&A end the same exhaustion is larger**, because D&A fell from $35.9M to
$14.5M and contributed $21.4M of the increase. **On the honest underlying measure, OCF − SBC
normalized for the tax break, the four-year growth rate is 11.7% a year, not 20.3%** — and
that is the number Q5 must use, not the headline.

### GREAT, GOOD, OR GRUESOME? **[E4-20]**

- **[x] GREAT — high return, little capital needed.** *"The great one pays an extraordinarily
  high interest rate that will rise as the years pass."* $222.0M of operating income on
  **negative** operating capital employed; 82.9% gross margin; 33.2% operating margin; capex
  0.75% of revenue; sixteen straight profitable years. On the [E4-20] test this is a great
  business and I am not going to hedge it.
- **With the ceiling [E2-63] stated, because it decides Q5.** The great savings account
  **will not take further deposits.** Qualys retains nothing: it earns $198.3M and returns
  $183.4M of it in buybacks, because there is nothing inside the business to spend it on.
  [E5-40]'s return-on-retention question therefore has no denominator here. **A great
  business that cannot redeploy is a bond with a growing coupon, and it is valued like one** —
  which is exactly what Q5 does below.

### STAYING POWER — SCORE ALL THREE **[E5-11]**

- **(1) a large and reliable stream of earnings — PASS, emphatically.** Sixteen consecutive
  years of revenue growth and positive owner earnings. **$401.1M of current deferred revenue
  and $518.0M of total remaining performance obligations** already contracted at 2025-12-31,
  of which $323.0M is scheduled to be recognised in 2026 — **48% of next year's revenue is
  already sold and largely already collected.** No customer above 10% of revenue in any of
  the last three years, filed.
- **(2) massive liquid assets — PASS, emphatically.** **$696.8M of cash and marketable
  securities** against a $5,938M market capitalisation — **11.7% of the company, and 104% of
  a year's revenue.** Held in *"money market funds, fixed-income U.S. Treasury and government
  agency securities, commercial paper, corporate bonds and asset-backed securities."*
- **(3) no significant near-term cash requirements — PASS, and this is the one that usually
  kills.** Total named 2026 requirements: operating lease payments **$11.0M**, purchase
  commitments **$28.1M**, guided capex **$8–12M**. **Roughly $50M against $309.4M of operating
  cash flow and $696.8M of liquidity.** [E5-39]'s test — *"We will never be dependent on the
  kindness of strangers"* — is met without qualification: **there is no revolver, no
  commercial paper, no debt, and nothing depended on.**
- **Leverage, named and quantified [E4-16, E3-29]: ZERO.** Total liabilities of $533.9M
  consist of $401.1M current deferred revenue, $47.0M noncurrent deferred revenue, $52.3M of
  operating lease liabilities and accruals. **[E3-52] applies in full:** these are
  *"liabilities without covenants or due dates attached to them"* — customer prepayments and
  leases, not covenanted bank debt. **[E2-54]'s coverage test is trivially satisfied: there is
  no interest, payable or accrued.**
- **[E2-60] — the restricted-earnings test.** Does the payout cost the business its unit
  volume, competitive position or financial strength? $1,239.5M of buybacks over eight years
  while cash rose from $86.6M (2017) to $696.8M and revenue trebled. **No.**

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**

**MODEL EXPOSURE, NOT EXPERIENCE [E4-40].** Qualys has never had a losing year, never had a
restatement, never had a breach disclosed in a filing and never had a customer above 10% of
revenue. **That record is "not only useless, but actually dangerous" as a guide**, because the
exposure is not in the history.

**THE MECHANISM, NAMED:** **standalone vulnerability management is absorbed into platforms
that are already installed for another reason, and the realised price per scanned asset falls
faster than the asset count rises.** Qualys states the mechanism itself, in its own competition
paragraph: *"We compete with large and small public companies, such as **CrowdStrike, Palo
Alto Networks, Rapid7, and Tenable Holdings**, as well as privately held security providers
including Invicti, Tanium, and **Wiz (which has announced a pending acquisition by Google)**"*
— and in its risk factors: *"Larger competitors with more diverse product and service
offerings may reduce the price of products or subscriptions that compete with ours or **may
bundle them with other products and subscriptions**."* **Approximately 100% of Qualys's
revenue is one product category, and three of the named competitors have a reason to give
that category away to sell something else.**

**QUANTIFIED FROM FILED FIGURES [E3-24].** *"Consider some mathematics."* The observable
input is the company's own net dollar expansion rate, which **fell nine points in seven
quarters (111% in Q3 2022 to 102% in Q2 2024) with no company-specific event.** Take that
observed slope, not a forecast, and apply it once more from today's 105%:

| scenario | NDR | base contribution | new-customer contribution (held at the 2025 $14.8M) | net revenue change |
|---|---|---|---|---|
| today | 105% | +$33.5M | +$14.8M | **+7.2%** |
| one more observed slope | 96% | −$26.8M | +$14.8M | **−1.8%** |
| bundled-away | 92% | −$53.5M | +$14.8M | **−5.8%** |

**At −5.8% a year for five years, revenue falls from $669.1M to roughly $497M.** Holding the
2025 cost base of $447.1M flat in nominal terms — an assumption that *favours* the company,
since it assumes no cost growth at all — **operating income falls from $222.0M to about $50M,
a 78% decline**, and owner earnings fall to roughly the level of stock compensation. **The
company does not fail: $696.8M of cash and no debt means it cannot be forced.** What is
destroyed is the equity value, not the entity.

**LIKELIHOOD: [x] A REAL POSSIBILITY.** Not "likely" — the metric has turned back up and the
compliance mandate is real. Not "a low-level possibility" — nine points of the move have
already happened and are on file.

**AND THE ARGUMENT AGAINST MY OWN POSITION, STATED AT FULL STRENGTH [E4-51].**
*"I'm not entitled to have an opinion unless I can state the arguments against my position
better than the people who are in opposition."*

> Vulnerability scanning is not bought because a vendor is liked; it is bought because
> PCI-DSS, FedRAMP and every regulated-industry regime require it, and the scanner of record
> inside a large enterprise is embedded in audit evidence, ticketing workflow and change
> control. Qualys has been that scanner for twenty-six years. The bundling thesis has been
> available to state at every point since 2020, and over that window Qualys's revenue went
> from $363.0M to $669.1M, operating margin from 26.6% to **33.2%**, gross margin to an
> all-time-high **82.9%**, and the share count fell 12%. **The net dollar expansion rate
> bottomed at 102% two years ago and has printed 103, 104, 104, 103, 104, 105 since.** Q2
> 2026 revenue grew **11%**, faster than any of the three preceding full years. The company
> has $696.8M of cash, no debt, no litigation, no investigation, one $7.4M goodwill balance
> in twenty-six years, and an auditor of twenty-one years' standing. Nothing here is
> deteriorating; a decelerating growth rate at a 33% operating margin with a 12%-shrinking
> share count is what a mature franchise harvesting looks like, and the market has priced
> five years of nothing into it — **a $100 investment at end-2020 was worth $109.05 at
> end-2025 while the peer index returned $258.44.**

**That case is real and it is why this name reached the top of the queue on price. What it
does not do is answer [E3-03] criterion (2), which is the gate — and it does not change the
arithmetic at Q5, which is done below.**

---

# COMPUTATION — NOT A CLEARANCE

**⛔ Q5 did not open. Q2 is OUT, so per operator rule 2 and rule 3 everything in this section
is arithmetic produced below a closed gate. It carries NO entry language, NO ranking position
and NO verdict. It is here because the operator asked for the price and the value band, and
because the arithmetic is the sharpest single fact in the file.**

### 1. THE YIELD — owner earnings against the bond

- **Sovereign: 5.24%**, US Treasury 30-year par yield, 2026-09-04, issuing authority. **The
  bare rate. No per-name premium is added [E3-42]** — *"It may look mathematical. But it's
  mathematical gibberish in my view."*
- **Market capitalisation $5,938M** = $171.65 × 34,595,001.

| owner-earnings figure | OE | **yield** | **vs sovereign** | perpetual g needed for the [E4-28] floor |
|---|---|---|---|---|
| 10yr (2016–25) @ (c)=D&A, normalized | $105.8M | 1.78% | **−3.46 pts** | 8.22% |
| **5yr (2021–25) @ (c)=D&A, normalized — THE HEADLINE [E2-42, E3-44]** | **$139.5M** | **2.35%** | **−2.89 pts** | **7.65%** |
| 5yr @ (c)=capex, normalized | $152.4M | 2.57% | −2.67 pts | 7.43% |
| 3yr (2023–25) @ (c)=capex, normalized | $174.5M | 2.94% | −2.30 pts | 7.06% |
| **best case: 2025 alone @ (c)=capex, normalized** | **$202.2M** | **3.41%** | **−1.83 pts** | **6.59%** |
| best case, un-normalized (the screen's own view) | $227.4M | 3.83% | −1.41 pts | 6.17% |

**Every construction in the grid — nine windows, both capex ends, normalized and raw — yields
less than the government bond.** The best of eighteen figures is 3.83%, and that one is a
single un-normalized year.

**EX-CASH CROSS-CHECK, because $696.8M of the market cap is securities.** Interest and other
income was $24.9M pretax in 2025, roughly $20M after tax, and it sits inside operating cash
flow — so owner earnings already contain the return on the cash pile and adding the cash
separately would double-count. Stripping both: operating owner earnings of ~$119.5M against
an ex-cash capitalisation of $5,241M = **2.28%.** The split does not change the answer.

### 2. WHAT THE PRICE ALREADY ASSUMES — stated in both forms

- **Perpetual form (the screen's form).** At the [E4-28] floor of 10%, the quote requires
  **7.43% to 7.65% growth in owner earnings, forever**, on the five-year default window.
- **Fading form, run as an ENGINE only [E3-34, E4-42] — it casts no vote.** A ten-year fade
  to a 3% terminal rate, discounted at 10%, requires **year-1 growth of 27.8% (capex end) or
  30.2% (D&A end)**, decaying linearly to 3%.
- **What the business has actually done.** Revenue growth **10.1%** in 2025 and **11.0%** in
  Q2 2026, decelerated from 19.1% in 2022. **OCF − SBC, normalized for the tax break, has
  compounded at 11.7% a year over four years** — and of the headline 20.3% owner-earnings
  growth over that span, **16% came from capex falling from $24.4M to $5.0M, which cannot
  repeat.** The net dollar expansion rate says the installed base contributes **3 to 5%**.
- **[E4-35] applies, and it applies gently.** *"fewer than 10 of the 200 most profitable
  companies in 2000 will attain 15% annual growth in earnings-per-share over the next 20
  years."* **7.5% perpetual is well under that wager's threshold and I will not pretend
  otherwise — this is not a heroic growth requirement.** What makes it fail is not the growth
  rate; it is that **7.5% forever is required merely to reach the floor**, with nothing left
  over, on a business whose own moat metric says the base grows 3–5%. **[E4-44]'s second
  bound governs the rest:** *"the value of an asset, whatever its character, cannot over the
  long term grow faster than its earnings do."*
- **[E2-63] — STATE THE CEILING.** The upside here is capped by something structural: **there
  is nowhere to put the money.** Qualys earns $198.3M and returns $183.4M, because capex is
  0.75% of revenue and goodwill has been $7.4M since 2019. Owner earnings can grow only as
  fast as revenue times margin expansion, and margin is already 33.2% with 1.7 of the last 3.8
  points coming from depreciation roll-off that is nearly complete.

### 3. WHAT YOU ARE PAID

**−2.89 points against the sovereign** on the five-year default construction; **−1.83 points**
on the single most favourable normalized construction in the whole grid.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**

**Against the [E4-28] floor of 10%**, on the five-year normalized owner-earnings band of
$139.5M to $152.4M:

| perpetual growth assumed | value | per share |
|---|---|---|
| 3% *(the rate the filed expansion metric supports)* | $2.05–2.24bn | **roughly $60 to $65** |
| 5% *(half of current revenue growth, sustained)* | $2.93–3.20bn | **roughly $85 to $95** |
| 7% *(current revenue growth, sustained forever)* | $4.98–5.44bn | **roughly $145 to $155** |

- **conservative: roughly $60 · optimistic: roughly $95 · current price $171.65**

**AND THE ONE PLACE THE TWO STANDARDS DISAGREE, WHICH IS WORTH RECORDING [E4-28].** Against
the **bare sovereign of 5.24%** with no floor applied, the same owner earnings at 3% perpetual
growth are worth **$6.4bn to $7.0bn, or $185 to $203 a share** — *above* today's quote.
**Qualys is the Berkshire case named in the operator protocol: above the bond, below the
floor.** The framework resolves it explicitly and it resolves it against the name — *"A
candidate whose honest pre-tax expectancy sits below roughly 10% is not ranked — it is quit
on, however it compares with the bond of the day"* **[E4-28]**, whose basis is *guessed future
opportunity cost*, not today's rate. **This is the single most important sentence in this
run's arithmetic, and it is the reason the "best-priced unrun name in the queue" still fails.**

### WHICH BAR **[E4-01, E4-11]**

- [x] **Screamer test [E4-01].** *Does the price already clear the conservative case?* The
  conservative case is roughly $60 a share and the price is $171.65. **The price is above the
  whole range: outcome three, "no."** No margin is added on top — *"startlingly low" is what
  you observe, not what you subtract*, and nothing here is startlingly low.
- **Windage count: ONE, and it is disclosed.** Conservatism is spent once **[E4-11, E4-48]**,
  at the **[E4-41] normalization of the 2025 tax break** ($25M, the smaller of two
  independent derivations). It is **not** spent again in the discount rate (the bare sovereign
  and the corpus's own 10% floor are used, with no per-name premium **[E3-42]**), **not** in
  the (c) judgment (the corpus default D&A end is also the conservative end, so the choice
  costs nothing extra), and **not** in an added end margin (the screamer test adds none). *If
  the $25M normalization were reversed entirely, the five-year yield would be 2.44% rather
  than 2.35% and no conclusion in this section would change.*

**VERDICT: NONE. The gate closed at Q2. No ranking position is assigned.**

---

## Q6 ITEMS — RECORDED, NOT A VERDICT. **[E1-02, E2-28, E4-17, E3-30]**

**There is no position, so there is no sell rule to pre-commit [E1-02].** What follows is the
**re-open trigger**, written now so that it is *"prior to the act"* and cannot be
retro-fitted.

**Thesis-breaking metrics — the conditions under which this OUT should be re-examined**
(these are the Q2 flip conditions restated, plus the price):
1. **Net dollar expansion rate filed at 110% or above for four consecutive quarters.** Watch
   the 10-Q, first week of May / August / November / late February.
2. **A filed customer count that moves** — any number replacing *"over 10,000 customers
   worldwide"*, restoring a unit series **[E4-55]**.
3. **Disclosure of actual bookings growth**, which would close the **[E4-31]** failure.
4. **Price.** At the five-year normalized band, the [E4-28] floor is cleared at roughly
   **$60 to $95 a share** depending on the growth assumption — a **45% to 65% fall** from
   $171.65. A price in that region on unchanged fundamentals is a reason to run the file
   again, not a reason to buy on this one.

**Thesis-confirming metric (that the OUT is right):** the direct share of total revenue,
filed annually in MD&A — 57% (2023), 54% (2024), **51% (2025)**. Continued decline is the
realised-price erosion this run identified, compounding.

**Next catalyst date:** Q3 2026 10-Q, expected early November 2026.

**The monitoring question [E3-30, E4-17]:** *is this erosion an aberrational cycle, or has the
business slipped in a way that permanently reduces intrinsic value?* **Honestly: it is not yet
possible to say, and beliefs on this one should change gradually [E4-17].** The expansion rate
has turned up; the price mix has turned down; the two point in opposite directions and two
years is not enough of either.

**Position size: ZERO.** No position is taken and none is recommended. **[E3-45]** directs
capital to rank #1, and a name yielding 2.35% against a 5.24% sovereign is not on the list at
any size. *(The capital-allocation flag raised at [E4-31] would in any case bind size
downward, per the template's rule.)*

---

## SELF-AUDIT

- [x] Questions answered in order; no verdict skipped. **Stopped at Q2. Q3, Q4, Q5 and Q6
      material is recorded below the closed gate and is explicitly labelled as not a verdict.**
- [x] No question marked IN carries an "unverified" or "provisional" caveat. **Q1 is the only
      IN, and the caveats it records (the "customer price sensitivity" language, the
      constant-change clause) were carried forward to Q2 and adjudicated there, not waived.**
- [x] Every non-IN verdict states what resolves it. **Q2's OUT names four falsifiable flip
      conditions, each a document that can be pointed at.**
- [x] Step 0: the filing was read, with accession number; **two figures cross-checked to the
      dollar** (operating cash flow $309,400k; capex $4,990k).
- [x] Owner earnings on a multi-year mean; **nine windows published [E4-38]**; capex band
      disclosed as a judgment with the corpus default [E3-44] cited and the [E5-20] exception
      class explicitly tested and found to invert.
- [x] Competitor row filled from peer filings; **2 of the 2 head-on SEC-registered
      pure-plays**, same metric, same window (all three are December year-ends). The blocked
      rung (Microsoft's unsegmented security revenue) is named, and **the Q2 verdict does not
      rest on it.**
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 2026-09-04.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (screamer test), not both; **windage count stated: ONE**, and its
      immateriality demonstrated.
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] `python tools/check_framework.py` run before the final commit.
- [x] Run committed to git, section by section, per the write-early protocol.

**ONE THING THIS RUN DID NOT DO, RECORDED HONESTLY.** The platform-bundling threat that the
death mechanism turns on **cannot be sized from filings**, because Microsoft files no security
revenue line, Wiz is private and being acquired, and Palo Alto's FY2026 10-K is not yet filed.
That question is **UNRESEARCHED-becoming-UNKNOWABLE**, exactly as the CRWD run found. **The Q2
OUT does not rest on it** — it rests on Qualys's own filed expansion rate, its own channel-mix
disclosure and its own description of its market.

## REGISTER

- **Verdict: [x] OUT (about the business), at Q2, on [E3-03] criterion (2).**
- **One line:** Qualys is a genuinely excellent business — 33.2% operating margins on negative
  operating capital, no debt, $696.8M of cash, a clean twenty-one-year audit record and a
  retention metric it has published honestly through a nine-point decline — that sits in a
  market its own filing calls *"highly fragmented and competitive"* with seven named
  substitutes, whose installed base pays only 3–5% more each year, and whose incremental
  revenue increasingly arrives through a channel sold at a discount; **and at $171.65 it
  yields 2.35% against a 5.24% sovereign, so even if the gate had opened the price would have
  closed it.**
- **The four-verdict line:** Q1 **IN** · Q2 **OUT** · Q3–Q6 **not reached** (material recorded).
- **This was the closest Q2 call in the queue.** The reasoning is set out at full strength on
  both sides and the four documents that would reverse it are named.
