# Company Run — MasterCraft Boat Holdings, Inc. (MCFT) — 2026-09-20
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
- rate **5.34** % · date **2026-09-18** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year constant maturity**. Struck fresh in this run with
  `python tools/sources.py`; FRED DGS30 was not used and was not needed.
- FX if the quote and the earnings differ in currency: **none.** USD filer, USD quote, Nasdaq.
  11.3% of fiscal 2026 net sales were international but the registrant reports and is paid in
  USD. ADR ratio, derived: **n/a**

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **Form 10-K for the fiscal year ended June 30, 2026, filed
  2026-09-10, accession 0001193125-26-387432**, primary document `mcft-20260630.htm`.
  Also read: 10-K FY2025 (filed 2025-08-27, acc. 0000950170-25-111682); 10-Q for the quarter
  ended 2026-03-29 (filed 2026-05-07, acc. 0001193125-26-211213); the 8-K of 2026-05-15
  completing the Marine Products merger (acc. 0001193125-26-226778); the 8-K of 2026-02-05
  announcing it (acc. 0001193125-26-039497); and the 8-K EX-99.1 earnings releases.
- figure cross-checked against the filed statement (say which): **net cash provided by operating
  activities of continuing operations, fiscal 2024, $12,200 thousand.** Tagged XBRL carries two
  values for that tag at 2024-06-30 ($12,200k and $12,569k, the second from an earlier filing's
  presentation before the Aviara restatement). The FY2026 10-K's own Consolidated Statements of
  Cash Flows, read line by line, shows **12,200** for continuing operations and **12,497** for
  total operating cash flow. The tagged figure was ambiguous and the filed statement decided it.

### THE THREE LIVENESS FLAGS, RESOLVED BEFORE Q1 OPENED

**(i) `cap_flag`, "cap $389M below filed public float $236,100M, 606.94x". RESOLVED: the float
is a 1000x units error in the extractor, and the cap was stale by one corporate event.**
The FY2025 10-K cover page states, verbatim: *"The aggregate market value of the outstanding
common stock, other than shares held by persons who may be deemed affiliates of the registrant,
as of the last business day of the registrant's most recently completed second fiscal quarter,
which ended December 29, 2024 and based on the closing sale price as reported on the NASDAQ
Global Select Market system, was approximately $ 236,100,000 ."* That is **$236.1 million**, not
$236,100 million. The extractor read a figure stated in dollars as if stated in thousands. It is
the first of the two hypotheses the brief named, not the CALM and EMBC drawdown case.
**Only one class of stock.** Both covers register a single line under Section 12(b),
*"Common Stock | MCFT | NASDAQ"*, par value $0.01, and Section 12(g) *"None"*. No second class,
no tracking stock, no up-C structure. The 24,339,371 shares on the FY2026 cover are the whole
equity.
**The cap is re-struck anyway and it moves a long way**, because the screen's share count was
pre-merger: FY2026 10-K cover, **24,339,371 shares issued and outstanding as of 2026-09-04**,
against 16,306,356 as of 2025-08-22 on the FY2025 cover. The screen's $389M was the old count at
an old price. Re-struck by hand: **$482M** (inputs under Q5).

**(ii) `name_change_note`, "the registrant was MCBC Holdings, Inc. until 2018-11-02". RESOLVED:
the rebrand is cosmetic, and it is the least important perimeter fact about this filer.**
The FY2026 10-K says it under *Other Information*: *"We were incorporated under the laws of the
State of Delaware under the name MCBC Holdings, Inc. on January 28, 2000. In July 2015, we
completed an initial public offering of our common stock. Effective November 7, 2018, the name of
the Company was changed from MCBC Holdings, Inc. to MasterCraft Boat Holdings, Inc."* Same CIK
0001638290, same Commission File Number 001-37502, same EIN 06-1571747, same Delaware
incorporation, continuous 10-K history from FY2015. The NEGG test passes: the multi-year figures
are one company.
**But the perimeter broke repeatedly inside any owner-earnings window, and the screen saw none of
it.** Named and dated from the filings:

| event | date | what it does to the series |
|---|---|---|
| Crest (pontoon) acquired | October 2018 | adds a segment part-way through FY2019 |
| Aviara launched | FY2019 | a third brand, later exited |
| **NauticStar sold** | fiscal 2023 | **restated to discontinued operations for all periods presented** |
| **Aviara Transaction and Aviara Facility Sale completed** | fiscal 2025 | **restated to discontinued operations for all periods presented** |
| Balise (luxury pontoon) launched | April 2024 | organic, no perimeter break |
| **Marine Products Corporation merger completed** | **2026-05-15** | **Chaparral and Robalo acquired, a third reportable segment created, ~$284.2M of consideration, six weeks of results inside FY2026** |
| MasterCraft segment renamed Performance and Wake, Pontoon segment renamed Leisure | Q4 FY2026 | naming only; the filer states *"The segment name changes had no impact on the composition of the Company's segments"* |

The two discontinued-operations restatements are why tagged data carries two different values for
the same tag at 2023-06-30 and at 2024-06-30. **Every figure below is taken on a
continuing-operations basis from the FY2026 10-K for FY2024 through FY2026, and is labelled
as-then-reported where it is older.**

**(iii) `wc_note`, "AccountsPayable moved 62% of 2024 operating cash flow". REPRODUCED TO THE
DECIMAL, AND THE SIGN IS THE OPPOSITE OF WHAT THE FLAG SAYS.**
The flag heading in the brief reads *"ONE LINE MADE THE CASH."* It did not. From the FY2026
10-K's Consolidated Statements of Cash Flows, fiscal 2024 column, in thousands: accounts payable
**(7,594)**, a **use** of cash, against net cash provided by operating activities of continuing
operations of **12,200**. 7,594 / 12,200 = **62.2%**. The arithmetic is exact and the verb is
wrong. Accounts payable **consumed** 62% of that year's operating cash; it did not produce it.
**And, as in EMBC, the flag named the second-biggest line.** The largest working-capital line in
fiscal 2024 is **accrued expenses and other current liabilities at (12,208)**, which is **100.1%**
of that year's continuing operating cash flow, bigger than accounts payable and bigger than any
other line in the statement. The whole fiscal 2024 working-capital block as filed, in thousands:
accounts receivable +2,462 · inventories +6,067 · prepaid expenses +1,284 · income taxes (5,772)
· accounts payable (7,594) · accrued expenses and other current liabilities (12,208) ·
other, net (1,302). Net **(17,063)** against income from continuing operations of 23,243.
**Does it reverse?** Partly, and late. FY2025 accounts payable (2,017), a further use. FY2026
accounts payable **+4,490**, a source, and the filer explains that source as two timing items
rather than a trading recovery: *"Accounts payable increased due to timing of professional fee
payments related to the Marine Products Transaction and timing of purchases at the end of the
period compared to the prior-year period."*
**The question the wc_note cannot ask, answered: it is a volume collapse.** Not a financing
decision, not a supplier-terms change. Continuing-operations net sales ran $609.9M (FY2023) to
$322.4M (FY2024) to $284.2M (FY2025). A manufacturer that cuts its build rate by more than half
stops buying, and the payables balance deflates with the purchase run-rate; the accrued-expense
drawdown is the dealer-incentive and compensation accruals of a record year unwinding on the same
mechanism. **Nothing was financed into working capital. Working capital drained because the
business shrank.**

### FOUR ITEMS IN THE SCREEN ROW THAT WERE JOBS, NOT CONCLUSIONS

**`newest_filing` 2025-06-30 older than `newest_periodic` 2026-03-29: what the columns measured,
and why both are now stale.** `newest_filing` is the period end of the newest **annual** report
the screen held (FY2025 10-K, filed 2025-08-27). `newest_periodic` is the period end of the
newest **quarterly** report (Q3 FY2026 10-Q, filed 2026-05-07). They measure different things, so
the "older than" comparison the brief flagged is comparing an annual period end with a quarterly
one and means nothing on its own. **Both are superseded.** MasterCraft filed its **FY2026 Form
10-K on 2026-09-10, ten days before this run**, for the year ended 2026-06-30, accession
0001193125-26-387432. It carries the post-merger share count, the first consolidated balance
sheet including Marine Products, the fiscal 2026 impairments, and the renamed segments. The share
count for the cap comes from its cover: 24,339,371 as of 2026-09-04.

**`best_year_note`, "one year is doing heavy lifting (9-yr OCF series)". The year is FISCAL 2023,
and the metric can now be named.** The screen's nine-year total operating cash flow series,
FY2017 through FY2025, in $ thousands: 26,232 · 49,397 · 55,886 · 30,198 · 68,538 · 73,311 ·
**134,196** · 12,497 · 35,593. Mean 53,983. Delete the best year and the mean falls to 43,950, a
reduction of **18.58%**, which reproduces the screen's `best_year_dep` of **0.186** to three
figures. So `best_year_dep` is *the fraction by which the multi-year mean falls if its single best
year is deleted*, and `best_year_dep_oe` 0.209 is that same statistic computed on the owner
earnings series rather than on raw operating cash flow.

**`best_year_dep` 0.186 against `best_year_dep_oe` 0.209: which is right, and why. The owner
earnings figure, 0.209.** The two disagree because capital expenditure is not distributed like
operating cash flow across this cycle. FY2023 carried $24.6M of continuing-operations capex
against $8.1M in FY2026, so subtracting (c) *raises* the share of what remains that the single
peak year contributes. Operator rule 8 decides it: the framework's one number is owner earnings
**[E2-23]**, not operating cash flow, so the dependence statistic that counts is the one measured
on the series that carries the verdict. **0.209 is the honest figure; 0.186 understates the
concentration.** With fiscal 2026 now filed, the window rolls to FY2018 through FY2026, FY2023 is
still the best year, and the concentration is worse, not better.
**The shape of that series is itself Q2 and Q4 evidence, as the brief suspected.**
Continuing-operations net sales: FY2019 $466M · FY2020 $363M · FY2021 $526M · FY2022 $708M ·
FY2023 $610M · FY2024 $322M · FY2025 $284M · FY2026 $349M. A demand bubble and a dealer
destocking bust, **peak to trough minus 53% in two years**, in a business selling a discretionary
object priced from $33,000 to $700,000.

**`spread_caveat`: the [E4-25] rebuild was ordered, and here it RUNS.** Unlike EMBC, where the
rebuild could not run in the direction the caveat assumed because there was no standalone company
before the spin, MasterCraft has **twelve consecutive fiscal years of 10-K filings, FY2015 through
FY2026, under one CIK**. Both the corpus five-year default **[E2-42]** and a long window are
available. Both are carried at Q4, with the perimeter breaks above named beside them.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language:**
  They buy resin, fiberglass, aluminum, lumber and steel, and they buy engines, which are the
  single largest component by cost. They hand-laminate and assemble boats in three plants:
  Vonore, Tennessee (310,000 sq ft, MasterCraft); Owosso, Michigan (270,000 sq ft, Crest and
  Balise); Nashville, Georgia (1,262,000 sq ft, Chaparral and Robalo, acquired 2026-05-15). They
  sell the finished boat **wholesale to an independent dealer**, and title passes when the boat
  is handed to the carrier. **The registrant is never paid by a boat buyer.** In the filer's own
  words: *"The Company typically receives payment from the floor plan financing providers within
  5 business days of shipment."* A third-party lender pays MCFT; the dealer owes the lender.
  So a boat that leaves the Tennessee plant is revenue on the day it goes on the truck, and the
  cash is in within a week, whether or not a consumer ever wants it.

  **The retail number is somebody else's, and the filer buys it.** The 10-K's only retail
  evidence is *"March 2026 data from Statistical Surveys, Inc."* MCFT's own reported net sales
  are shipments into the channel, and the gap between shipments and registrations is dealer
  inventory, which is the swing factor that produced the cycle in section Step 0.

  **What the price actually is.** Net sales are gross wholesale price **less dealer incentives**,
  estimated at the moment of sale: wholesale rebates earned on *"purchase volume commitments and
  achievement of certain performance metrics"*; retail rebates *"that apply to boats already in
  dealer inventory"*; *"cash discounts or … reimburse its dealers for certain floor plan interest
  costs … generally ranging up to nine months"*; and other allowances. Every one of those is an
  estimate the company makes about dealer and consumer behaviour, and every one is a lever that
  moves before a price list does. **Reported net sales is therefore a net figure containing a
  discretionary promotional accrual**, which is why fiscal 2026's revenue rise is attributed in
  part to *"decreased dealer incentives"* rather than to a list price.

- **The contingent liability that belongs in Q1, not only in Q4.**
  Selling through a floor plan means MCFT has written a guarantee to the dealers' lenders. From
  Note 13, verbatim: *"Under certain conditions, the Company is obligated to repurchase new
  inventory repossessed from dealerships by financial institutions that provide credit to the
  Company's dealers … totaled approximately $ 63.5 million and $ 41.0 million as of June 30, 2026
  and June 30, 2025, respectively."* Against that, *"The Company recorded a repurchase liability
  of $ 1.5 million and $ 1.6 million as of June 30, 2026 and 2025"*, and *"We incurred no
  material impact from repurchase events during the years ended June 30, 2026, 2025, and 2024."*
  The commitment runs *"on an individual unit basis with a term from the date it is financed by
  the lending institution through the payment date by the dealer, generally not exceeding 30
  months."*
  So: a **$63.5M gross exposure, up 55% year on year**, reserved at **2.4 cents on the dollar**,
  on a business whose entire equity market value is $482M. The 2.4% reserve is an experience
  number in a period when no dealer failed. **[E4-40] is the corpus's warning about exactly this
  arithmetic:** *"focusing on experience, rather than exposure."* Recorded here; quantified at Q4.

- **The scarce input this business controls: floor space and floor-plan capacity in an
  independent dealer's showroom.**
  Not the plants, which are replaceable, and not the engines, which are bought from Ilmor,
  Mercury, Yamaha and Volvo Penta. A dealer can stock only so many brands and can borrow only so
  much against them, and the filer's own disclosure is that *"The majority of our MasterCraft
  brand dealers are exclusive to our MasterCraft product lines within the ski/wake category."*
  That exclusivity, across 83 domestic dealers at 140 locations, is the asset. **It is contracted,
  not owned**, and the 10-K describes it as re-earned every year with money: *"We have developed a
  system of financial incentives for our dealers based on achievement of key benchmarks."*
  Note the other side of the same fact: *"our other brands are generally served on a nonexclusive
  basis by their respective dealers."* Four of the five brands do not have it.

- **Concentration, as filed.** *"For fiscal 2026, the Company's top ten dealers accounted for
  approximately 34% of our net sales and none of our dealers individually accounted for more than
  10%."* Supplier side: Ilmor is the exclusive MasterCraft engine supplier and *"During fiscal
  2026, Ilmor was our largest overall supplier."* Single-site risk is acknowledged: *"Each of our
  brands is only manufactured at one of our three manufacturing facilities."*

- **Every brand and segment, and which exist today (June 30, 2026):**
  **Performance and Wake** (renamed from MasterCraft in Q4 FY2026): brand **MasterCraft**, 15
  models, 20 to 25 ft, $110k to $500k. **Leisure** (renamed from Pontoon): brands **Crest**
  (acquired October 2018) and **Balise** (launched April 2024), 9 models, $33k to $570k.
  **Recreation and Sport Fishing** (created May 2026): brands **Chaparral** and **Robalo**, 39
  models, $36k to $700k. **Gone: NauticStar** (sold fiscal 2023) and **Aviara** (the Aviara
  Transaction and Aviara Facility Sale, fiscal 2025), both now reported as discontinued operations
  for all periods presented. The registrant also owns **50% of 255 RC, LLC**, described in Note 14
  as *"a limited liability company formed for the joint ownership of a corporate aircraft"*, on the
  equity method. It is not an operating investee and there is no [E3-04] look-through to add; it
  is noted here and read again at Q3.

- **Will the fundamentals look broadly the same in ten years?** **Yes, the mechanism will; no, the
  volume will not, and the two are separable.** Boats have been hand-laid in glass and sold
  through independent dealers on floor-plan credit for sixty years, and nothing in the filing
  suggests that changes. The MasterCraft brand dates to 1968, Chaparral to 1965, Robalo to 1969,
  Crest to 1957. What is not stable is unit demand: this is a discretionary durable bought with
  credit, and its volume has halved twice inside the filed record. **That is a Q4 and Q5 problem,
  not a comprehension problem, and it is not allowed to decide this gate** (the TAIL-TRIAGE
  correction: do not let a number below decide a gate above it).

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**
  **IN.** The business is *"relatively simple and stable in character"* **[E3-31]**: buy
  components, assemble a boat, ship it to a dealer, get paid by his lender in five days, and
  guarantee the lender against the dealer's default. There is no financing arm, no float, no
  unconsolidated leverage, and the one equity-method investment is an aeroplane. I can write the
  income statement's mechanism in four sentences without using a word management chose, which is
  the test. **Recorded forward: the $63.5M repurchase guarantee, the incentive accrual as an
  earnings lever, and the fact that reported revenue is a shipment, not a sale to a boater.**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- **Needed or desired [x]** · **no close substitute [ ] FAILS** · **not price-regulated [x]**

**Criterion 2 fails on the registrant's own words, in the FY2026 10-K risk factors, verbatim:**
> *"Our industry is characterized by intense competition, which affects our sales and profits.
> The premium performance sport boat and outboard boat categories and the powerboat industry as a
> whole are highly competitive for consumers and dealers. **We also compete against consumer
> demand for used boats.** … **Competition is based primarily on brand name, price, product
> selection, and product performance.** We compete with several large manufacturers that may have
> greater financial, marketing, and other resources than we do … **In addition, certain of our
> Chaparral models compete in the wake and surf category alongside our MasterCraft brand, which
> may result in intra-company competition that could affect the sales or pricing of products
> within our portfolio.**"*

and, on the price of a substitute:
> *"our competitors could choose to reduce the price of their products, which could have the
> effect of reducing demand for our new boats."*

Three separate substitutes are named by the filer itself: a rival's new boat, **a used boat**,
and, since 2026-05-15, **its own newly acquired Chaparral**. The used-boat substitute is the
worst of the three, because every MasterCraft ever built is a permanent competitor to the next
one. This is the EMBC pattern: the filer classified its own category and the classification
decided the gate.

- **Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04]**
  **[E4-04] is not the operative test here and is not used to close this file.** Under the
  verdict form ruled 2026-09-20, [E4-04] is a **competence limit** whose failure mode is
  UNKNOWABLE at Q2, and it applies to a name that **passes [E3-03]** and whose durability cannot
  be judged. This name does not reach that door: it fails [E3-03] criterion 2 on filed evidence,
  which is a finding **about the business**. For the record, the answer to the [E4-04] question
  is that MasterCraft's advantage is defended rather than replaced (a 1968 trademark, 90 US
  patents, 130 trademarks), so [E4-04] would not have closed this file on its own.
  **What does have to be rebuilt every year is the distribution.** *"Our agreements with dealers
  in our networks typically provide for one-year terms"*, and the position inside those dealers
  is bought: *"We have developed a system of financial incentives for our dealers based on
  achievement of key benchmarks … wholesale rebates, retail rebates and promotions, other
  allowances, and floor plan interest reimbursement or cash discounts."*

- **Primary moat metric, filing-sourced, and its trend: gross margin through one full cycle,
  set beside the physical unit series [E4-55].**
  MCFT gross margin, FY2019 through FY2026: **24.3% · 20.8% · 24.7% · 23.8% · 25.6% · 19.5% ·
  20.0% · 22.9%**. Cross-checked to the filed statement: FY2026 gross profit $79,779k on net
  sales $348,903k = 22.87%. **The trend is a cycle, not a direction**, and the peak sits exactly
  where the industry's peak sits.

**[E4-55] — WHERE UNITS EXIST, MONITOR UNITS. This is the Precision Steel pattern, filed.**

| brand, units shipped to dealers | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| **MasterCraft** | 3,301 | **3,596** | 3,407 | 1,755 | 1,548 | **1,639** |
| **Crest (pontoon)** | 2,467 | **3,156** | 2,836 | 1,241 | 745 | **716** |
| net sales per unit, MasterCraft / Performance and Wake | | | $138k | $150k | $156k | **$165k** |
| net sales per unit, Crest / Leisure | | | $50k | $48k | $58k | **$62k** |

*Sources: FY2022 10-K (acc. 0001564590-22-031335), FY2024 10-K (acc. 0000950170-24-102002),
FY2026 10-K (acc. 0001193125-26-387432), MD&A unit-volume and net-sales-per-unit tables.*

**MasterCraft units are down 54% from FY2022 and Crest units are down 77%, while net sales per
unit rose 20% and 24% respectively.** That is [E4-55] word for word: *"Dollar revenue flattered
by pricing is how a shrinking franchise hides; the physical series is the honest one."* The
pontoon case is the starker one, because the physical collapse is accompanied by a **$10.1
million non-cash impairment of the Crest brand intangible assets** taken in the fiscal 2026
fourth quarter, eight years after Crest was bought. A brand whose carrying value the filer
itself has just written down is not producing evidence of a moat.

**THE COMPETITOR ROW — required [E3-28].** A moat is a claim about *relative* position.
**Same metric (gross margin and operating margin as filed), same window (the full 2019 to 2026
cycle), filing-sourced (10-K XBRL, us-gaap tags, annual periods, form 10-K only).**

| Company | metric | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | peak-to-trough net sales | source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **MCFT (subject)** | gross margin | 24.3% | 20.8% | 24.7% | 23.8% | **25.6%** | 19.5% | 20.0% | 22.9% | **$707.9M → $284.2M, −59.9%** | 10-K, CIK 1638290 |
| | operating margin | 7.1% | −7.3% | 15.0% | 16.4% | **18.3%** | 7.5% | 4.0% | **−0.3%** | | |
| **MBUU** Malibu Boats | gross margin | 24.3% | 22.9% | 25.5% | 25.5% | 25.3% | 17.7% | 17.8% | **16.0%** | $1,388.4M → $807.6M, −41.8% | 10-K, CIK 1590976 |
| | operating margin | 14.3% | 13.1% | 16.2% | 17.6% | 10.4% | −6.7% | 2.7% | 0.3% | | |
| **BC** Brunswick | gross margin | 27.3% | 27.9% | 28.5% | **28.6%** | 27.9% | 25.8% | 24.8% | n/a (Dec FY) | $6,812.2M → $5,237.1M, −23.1% | 10-K, CIK 14930 |
| | operating margin | 11.5% | 12.4% | 13.9% | 13.9% | 11.5% | 5.9% | −0.8% | | | |
| **MPX** Marine Products *(acquired by MCFT 2026-05-15)* | gross margin | 22.4% | 22.4% | 22.9% | 24.6% | 23.6% | 19.2% | 19.1% | n/a (Dec FY) | $383.7M → $236.6M, −38.3% | 10-K, CIK 1129155 |
| | operating margin | 11.7% | 10.2% | 12.2% | 13.6% | 12.8% | 7.7% | **5.7%** | | | |
| **PII** Polaris *(marine segment inside)* | gross margin | 24.3% | 24.3% | 23.7% | 22.8% | 21.9% | 20.4% | 19.1% | n/a (Dec FY) | $8,934.4M → $7,152.0M, −19.9% | 10-K, CIK 931015 |
| | operating margin | 7.1% | 7.4% | 8.7% | 9.4% | 7.8% | 4.0% | −4.9% | | | |
| **HZO** MarineMax *(retailer)* | gross margin | 26.1% | 26.4% | 32.0% | 34.9% | 34.9% | 33.0% | 32.5% | n/a (Sep FY) | $2,431.0M → $2,309.3M, −5.0% | 10-K, CIK 1057060 |
| | operating margin | 4.9% | 7.1% | 10.2% | 11.5% | 8.4% | 5.3% | 1.5% | | | |
| **ONEW** OneWater *(retailer)* | gross margin | n/a | 23.0% | 29.1% | 31.7% | 27.6% | 24.5% | 22.8% | n/a (Sep FY) | $1,936.3M → $1,772.6M, −8.5% | 10-K, CIK 1772921 |
| | operating margin | n/a | 7.7% | 12.1% | 12.5% | 0.9% | 3.7% | −4.6% | | | |

*Fiscal years are the filer's own: MCFT and MBUU end 30 June; BC, MPX and PII end 31 December;
HZO and ONEW end 30 September. The two retailers are carried because the brief named them and
because they show the channel, but their gross margin is not like-for-like with a builder's
(it carries finance and insurance income), and they are read for direction only.*

- **Peers named: 6 SEC-filing competitors, of which 4 are builders, out of an industry whose
  public builders number 4.** Buffett says eight; the powerboat industry does not have eight
  public builders, so I took every one that files, plus the two public retailers that carry the
  channel evidence, plus the acquired MPX through its final 10-K.
- **Peers unavailable, with rung and obstacle, as the ladder requires:**
  **Correct Craft / Nautique** (MasterCraft's nearest ski/wake rival) — rung *SEC EDGAR primary
  documents*, obstacle: **privately held, no SEC filings and no exchange filings**.
  **Sea Hunt Boats** and **Regal Marine Industries** — named as competitors by MCFT itself in the
  FY2026 competition risk factor — rung *SEC EDGAR*, obstacle: **privately held**.
  **Yamaha Motor Co.** and **Bombardier Recreational Products** — rung *exchange filings /
  EDINET*, obstacle: **not SEC 10-K filers; EDINET is blocked on a paid key per the evidence
  ladder.**
  **The moat class is NOT held PROVISIONAL on those absences, and here is the reason in writing:**
  the framework holds a class PROVISIONAL where missing peer data could change a *claim of a
  moat*. **No moat is being claimed.** Adding four more competitors to a market the filer already
  describes as *"intense"* and *"highly competitive"* cannot manufacture the *"no close
  substitute"* condition that criterion 2 requires; more names in the row can only widen the
  substitute set. The unreachable peers are therefore recorded, and they cannot reverse the
  finding they are missing from.

**WHAT THE ROW ACTUALLY SHOWS, INCLUDING THE PART THAT CUTS AGAINST ME [operator rule 9, E4-26].**

1. **Seven companies, three business models, one shape.** Every name in the row prints its best
   operating margin in fiscal 2021 or 2022 and its worst in fiscal 2025 or 2026, and four of the
   seven print a negative operating margin at the bottom. Builders, a diversified powersports
   manufacturer, and two retailers all did the same thing at the same time. **That is [E3-51]'s
   surfing run with the wave fully visible** — *"the advantage lives in the wave, not the
   surfer"* — and under **[E4-36]** the fourth cause of extreme success, wave-riding, is the one
   that is not ownable. A record built between fiscal 2021 and fiscal 2023 is not evidence of a
   moat; it is evidence that Americans bought boats during the pandemic.
2. **MCFT lost more revenue than anyone in the row.** Peak to trough: MCFT **−59.9%**, MBUU
   −41.8%, MPX −38.3%, BC −23.1%, PII −19.9%, ONEW −8.5%, HZO −5.0%. If a moat means anything
   on filed numbers it should mean *less* volume lost when the tide goes out. MCFT lost the most.
3. **THE DISCONFIRMING EVIDENCE, stated at full strength, because the hypothesis I like is that
   this is not a franchise.** In the *downturn* MCFT's gross margin beats Malibu's by a wide
   margin: 19.5% vs 17.7% (FY2024), 20.0% vs 17.8% (FY2025), **22.9% vs 16.0% (FY2026)**, a 6.9
   point lead over its closest ski/wake rival in the most recent year, achieved while running its
   plants at roughly half of peak volume. That is a real operating result and it is not nothing.
   **Why it does not carry the gate.** (a) It is *relative to one peer having a worse year*, not
   an absolute standard: Brunswick, the largest builder, out-earns MCFT on gross margin in
   **every one of the seven years** where both report, by 2 to 5 points. (b) The [E2-58] exception
   requires a cost advantage that is *"both wide and sustainable"*, and a lead that was absent in
   FY2019 through FY2023 and appears only in the trough is, on eight years of evidence, neither.
   (c) The same fiscal 2026 still produced a **consolidated operating loss**. A gross-margin lead
   that does not reach the operating line is a fact about mix and about Malibu, not a moat.
4. **The most profitable company in the row through the bust is the one MCFT just bought.**
   Marine Products never printed a negative operating margin, held 5.7% in its final full year,
   and lost 38% of revenue against MCFT's 60%. MCFT paid roughly $284.2 million for it. That is
   read again at Q3 as a capital-allocation fact; it is not a moat finding about MCFT.

- **Untapped pricing power — could a manager raise the return simply by raising prices, and has
  not? [E3-33] NO, and the filing gives the inverse answer.**
  **[E5-28]** scopes the class: *"If you name some business that has incredible pricing power,
  you're talking about a business that's a monopoly or a near monopoly."* MasterCraft is not
  that; its closest rival ships more boats at a higher price per boat (Malibu brand, 2,150 units
  at $184,990 average net sales per unit in FY2026, against MasterCraft's 1,639 at $165,000).
  **And [E4-37]'s inverse metric fires at full strength.** The test is *"the agony they go
  through in determining whether a price increase can be sustained."* The FY2026 10-K states the
  reflex under cost pressure in its own risk factors, verbatim:
  > *"In an effort to offset the increased interest exposure, we have offered and expect to
  > continue offering dealer incentives to pass through the additional dealer costs to us, **which
  > in turn negatively impacts our margins.**"*

  and
  > *"Deterioration in general economic conditions … may reduce our sales, **or we may decide to
  > lower pricing for our products**"*

  A business with pricing power does not volunteer to absorb its distributor's interest bill.
  **[E2-44]'s two-characteristic test fails on both limbs**: it cannot raise price when demand is
  flat and capacity is not fully utilized (it raised *net sales per unit* 5.8% in FY2026 and still
  finished 2.7 points below its FY2023 gross margin and at a consolidated operating loss), and it
  cannot grow dollar volume *"with only minor additional investment of capital"* — it grew dollar
  volume by paying $284.2 million for two more brands.
- **[E3-46], the second question about the business, is a number, and here is the series.**
  Return on average equity, from the filed statements: FY2019 **34.2%** · FY2020 **−39.7%** ·
  FY2021 **71.7%** · FY2022 **46.3%** · FY2023 **41.1%** · FY2024 **4.2%** · FY2025 **3.8%** ·
  FY2026 **−0.6%**. *"The best businesses, by definition, are going to be businesses that earn
  very high returns on capital employed **over time**."* This business earns spectacular returns
  for three years in nine and negative returns in two, and the three spectacular years are the
  three years the whole row was spectacular. **[E2-43]** is applied because the filer is
  acquisitive: the goodwill wedge is reported separately rather than buried, and it is now large.
  Goodwill $134.1M plus other intangibles $82.2M is **$216.3M against $381.3M of book equity**, so
  **57% of book equity is purchased intangibles** and unleveraged net tangible equity is $164.8M.
- **[E2-53], the dominance class, and [E5-18]'s stand-a-little-mismanagement test: both fail.**
  Position does not set the economics here; the filer says *"our profitability depends, in part,
  on our ability to spread fixed costs over a sufficiently large number of products sold and
  shipped"*, which is a scale-utilisation business, and *"Competition is based primarily on brand
  name, price, product selection, and product performance."*
- **[E2-58], the commodity-end doctrine, is the doctrine that fits.** *"persistent over-capacity
  without administered prices (or costs) equals poor profitability"*, with long-term
  profitability set by *"the ratio of supply-tight to supply-ample years"* and prosperity breeding
  the next glut. That is the filed record exactly: three supply-tight years (FY2021 to FY2023)
  produced 15% to 18% operating margins and a capacity build across the whole industry; three
  supply-ample years (FY2024 to FY2026) produced 7.5%, 4.0% and **−0.3%**. The one exception
  [E2-58] allows is *"a cost advantage that is both wide and sustainable … By definition such
  exceptions are few"*, and MCFT does not have it: Brunswick beats it on gross margin in every
  comparable year.

- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: narrowing.** Units down 54%
  and 77% by brand, a bought brand's intangibles impaired by $10.1M in the current year, a
  consolidated operating loss, and the filer disclosing that its newest acquisition competes with
  its own flagship.
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

  **OUT, on the business, on filed evidence.** MasterCraft makes a desired product that is not
  price-regulated and fails the middle criterion of **[E3-03]** outright: its own annual report
  names three classes of close substitute (rival new boats, **used boats**, and its own Chaparral)
  and states that competition is conducted *"primarily on brand name, price, product selection,
  and product performance."* The competitor row confirms it as a relative claim: an eight-year
  same-metric comparison shows MCFT below Brunswick on gross margin in every comparable year,
  with the deepest peak-to-trough revenue decline in the entire public peer set, and with every
  company in the row printing the same cycle shape at the same time, which is **[E3-51]**'s
  surfing run and **[E4-36]**'s fourth cause. The physical series **[E4-55]** is the honest one
  and it is halved. The applicable doctrine is **[E2-58]**'s commodity end, whose one exception,
  a wide and sustainable cost advantage, the row rules out.
  **Q3, Q4 and Q5 are not opened.** UNRESEARCHED and UNKNOWABLE both close a file and so does
  OUT; the hard sequence stops here. What follows below is recorded because the work was done in
  the course of reaching this verdict, and it is explicitly **NOT a verdict on any later gate.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?

⛔ **NOT OPENED. Q2 returned OUT and the hard sequence stops at the first verdict that is not
IN.** Nothing in this section is a verdict, and none of it may be read as one. It is recorded
because the work was done before Q2 closed and because the brief's standing CGNX rule required
the 8-K EX-99.1 earnings releases to be pulled, and because **operator rule 6** says a run
records what it found rather than discarding it. **No Q3 verdict box is ticked below.**

### OBSERVATIONS RECORDED, NOT SCORED

**The [E4-29] fifth flag fires, and it fires in both places.** Unlike Cognex, where the word
EBITDA was absent from the 10-K and present in the furnished release, MasterCraft promotes the
measure in **both**. The FY2026 10-K lists *"Adjusted EBITDA"*, *"Adjusted EBITDA margin"*,
*"Adjusted Net Income"* and *"Free cash flow"* among its **Key Performance Measures** in MD&A.
The 8-K EX-99.1 of 2026-09-10 (acc. 0001193125-26-387237) then headlines them against a GAAP
loss:

| | as filed (GAAP) | as promoted (non-GAAP) |
|---|---|---|
| FY2026 full year, continuing operations | **loss of $1.6 million, $(0.09) per diluted share** | *"Adjusted Net Income … was $30.2 million, or $1.76 per diluted share"* |
| FY2026 margin | **operating margin −0.3%** | *"Adjusted EBITDA margin was 13.1% for fiscal 2026, up from 8.6%"* |
| FY2026 Q4 | **loss of $7.0 million, $(0.35) per diluted share** | *"Adjusted Net Income … $13.5 million, or $0.67 per diluted share"* |

The CEO's quoted line is *"We grew net sales, expanded Adjusted EBITDA nearly 80%, and completed
the transformational combination."* **[E4-29]**: *"Trumpeting EBITDA … is a particularly
pernicious practice. Doing so implies that depreciation is not truly an expense … That's
nonsense."* Depreciation and amortisation ran **$13.7 million** in fiscal 2026 against total
capex of $8.1 million, and a large part of it is the amortisation of intangibles the company
bought. **[E5-41]**'s reverse-float mechanism applies exactly: the money was already spent.
**This is a prompt to read, never a score, and it is left unscored here.**

**A CEO claim the competitor row contradicts, recorded verbatim for whoever reopens this name.**
*"What gives me confidence is that these results were earned, not market-driven."* The row at Q2
shows six other companies printing the same cycle shape at the same time. That is a
candour observation under **[E2-26]**, not a venality finding **[E5-38]**, and it is left as an
observation.

**[E2-49], the metric-switching flag: checked, and it reads as the candour case, not the flag.**
Two yardstick changes happened in the same year. (1) The **segments were renamed** in Q4 FY2026
(MasterCraft to Performance and Wake, Pontoon to Leisure) with the filer stating *"The segment
name changes had no impact on the composition of the Company's segments or on previously
reported financial position, results of operations, cash flows, or segment operating results."*
(2) **The fiscal year end changes from June 30 to December 31, effective 2026-07-01**, announced
in June 2026 with a six-month transition report to be filed for 1 July to 31 December 2026 (8-K
of 2026-06-30, acc. 0001193125-26-290514, Item 5.03). [E2-49] fires where a switch **follows**
deterioration; this one was **announced ahead with a reason** (alignment to the acquired Marine
Products' December year end), which is the form [E2-49] itself names as the candour case.
**It is nevertheless a real cost to any future reader**: every multi-year series in this file
breaks at 2026-06-30 and must be rebuilt across a stub period.

**Capital allocation, recorded and not scored.** Buybacks fell as the shares fell: repurchase
and retirement of common stock $16,257k (FY2024), $9,767k (FY2025), $2,337k (FY2026). Then, in
May 2026, roughly **8.0 million new shares were issued** (16,406,788 at 2025-06-30 to 24,437,538
at 2026-06-30, +48.9%) plus cash, for total consideration of approximately **$284.2 million**,
to buy Marine Products. **[E5-44]** is the test that belongs here and it is left unrun:
*"The intrinsic value of the shares you give in an acquisition must not be greater than the
intrinsic value of the business you receive."* The raw arithmetic, for a future run: Marine
Products standalone produced operating cash flow of $16.5M (CY2025), $29.5M (CY2024), $56.8M
(CY2023) with capex of $1.5M, $4.6M, $10.2M and share-based compensation of $5.2M, $4.2M, $3.7M
(MPX 10-K XBRL, CIK 1129155). **No conclusion is drawn from those figures in this file.**

**Ownership and control, as filed (FY2026 10-K Item 12, as of 2026-08-28).** LOR, Inc.
**20.0%**, Coliseum Capital Management **15.2%**, Forager Capital Management 6.0%. The
Stockholders Agreement of 2026-02-05 gives the Marine Products specified stockholders the right
to nominate **two of ten directors** while they hold at least 15% of voting power, with a
standstill running to the earlier of 2028-05-15 and the date they fall below 15%. The board went
from seven to ten directors on the closing date. **Recorded, not scored.**

**One item flagged for whoever reopens this name:** Note 14 discloses that the Company
*"owns a 50 % interest in 255 RC, LLC, a limited liability company formed for the joint ownership
of a corporate aircraft."* It is immaterial to the accounts and it is **not** being scored as a
finding; it is recorded because it is the kind of item **[E2-30]** asks a reader to notice, and
because a future run should ask who the other 50% is.

**NOT RUN, and named so that the omission is visible rather than silent:** the DEF 14A pay plan
against **[E4-22]**'s third flag and **[E3-48]**'s guidance-versus-outturn test; the **[E4-30]**
cash-tax-share series; the **[E3-54]** retention test; the **[E2-30]** institutional-imperative
score; the **[E2-01]** primary test run as a full series on unleveraged net tangible assets. The
gate is closed and running them would be work on a file the framework has already stopped.
Note that Part III of the FY2026 10-K carries the compensation disclosure in full (lines for
Items 10 through 14 are inside the 10-K itself, not incorporated by reference), so the artifact
is on hand if the name is ever reopened.

---

*The template's Q3 apparatus is left unfilled below, deliberately. A ticked checkbox in a
template is not a verdict, and an unopened gate must look unopened.*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**None ticked → Q3 is a qualitative OVERLAY.** Record findings; manager quality alone does
not stop the run. **Any ticked → Q3 is a BINARY GATE and no price compensates.**
Case declared, and why: ____

**Honesty — binary, permanent, filings-based [E5-16].** *"understanding about business
mistakes; tolerance for personal misconduct is zero."* Each matter dated to when it became
PUBLIC, so the test stays point-in-time honest: ____

**STEP 2 — THE FOUR FLAGS [E4-22, E5-15].** *Accounting and disclosure, not litigation. Each
is a prompt to READ, never a verdict.*
- [ ] weak accounting — comp not expensed, fanciful pension assumptions → *"seldom just one cockroach in the kitchen"*
- [ ] unintelligible footnotes
- [ ] trumpeted earnings projections / growth targets
- [ ] serial share issuance
- [ ] EBITDA / adjusted-earnings promotion **[E4-29]** *(the fifth flag; 12+ corpus statements)*
- [ ] filed-figure tells: unnaturally smooth reported growth; cash-tax % of pretax falling **[E4-30]**
- For every box ticked, what the filing actually says: ____

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity capital employed, *without
undue leverage or accounting gimmickry* — **not** EPS growth. Multi-year series, balance
sheet before income statement.
- Years used, and the series: ____

**The half-owner test [E2-26]:** does this reporting tell me what I would want to know if the
positions were reversed? *(a one-time item quantified separately at every line passes; the
same item buried in an adjusted figure does not)* ____

**The institutional imperative — score all four [E2-30].** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [ ] resists any change in current direction
- [ ] projects/acquisitions materialise to soak up available funds
- [ ] staff studies produced to justify the leader's craving
- [ ] peer behaviour mindlessly imitated

**Capital allocation — the two buyback conditions [E5-08]:**
- (1) ample funds for operations and liquidity? ____
- (2) repurchases at a **material discount** to conservatively calculated IV? ____
  *(unquantified because the corpus leaves it unquantified)*
- If (2) fails → **CAPITAL ALLOCATION FLAG**, stated with the humility clause **[E4-13]**:
  this rests on our own IV range, and management knows the business better than we do.
  **Binds position size, never the discount rate.**
**THE GUARDRAIL — check before writing the verdict.**
- [ ] Confirmed: nothing in this Q3 is being used to **promote** the name. A strong manager
      cannot repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**.
- [ ] If this business **requires** a great manager, that is recorded at **Q2 as a moat
      defect [E4-23]** — *"the moat will go when the surgeon goes"* — not here as a strength.
- [ ] If a great manager is the reason to act: is the franchise **already intact** and the
      damage **excisable**, or is the manager the plan? **[E2-35, E2-36]** ____

- **VERDICT: [ ] IN  [ ] OUT (integrity failure is permanent)  [ ] UNRESEARCHED → ____
  [ ] UNKNOWABLE → ____**
  **NO BOX TICKED. Q3 WAS NOT OPENED** because Q2 returned OUT. The observations above are
  recorded findings, not a verdict, and nothing in them promotes or demotes this name.
  *IN = no disqualifier found. NOT a finding that the managers are honest — "sincerity and
  empathy can easily be faked" **[E5-17]**. IN never promotes.*

## Q4 — WILL IT SURVIVE?

⛔ **NOT OPENED. Q2 returned OUT.** The material below was gathered before Q2 closed and is
recorded under operator rule 6. **No box is ticked and no verdict is given.**

### OBSERVATIONS RECORDED, NOT SCORED

**The balance sheet, as filed at 2026-06-30 ($ thousands):** cash 43,865 · short-term
investments nil (50,518 a year earlier) · receivables 11,445 · inventories 82,261 · total
current assets 152,707 · PP&E net 120,563 · goodwill 134,092 · other intangibles net 82,216 ·
**total assets 500,432**. Accounts payable 24,206 · accrued expenses and other current
liabilities 73,265 · total current liabilities 97,658 · unrecognized tax positions 18,299 ·
**total liabilities 119,144** · **total equity 381,288**.
**There is no funded debt.** The term loan was repaid in fiscal 2025 ($49,500k of principal
payments); fiscal 2026 shows $25,000k drawn on the revolver and $25,000k repaid, and the
year-end balance sheet carries no debt line at all. **[E4-16]**'s mechanism (*"Whenever a bright
person … goes broke … it's because of leverage"*) has nothing to bite on here, and that is a
genuine strength recorded honestly on a file that closed OUT on the business.

**The three strengths [E5-11], scored as observations only.** (1) *A large and reliable stream
of earnings*: **the stream is large in some years and negative in others** — continuing-operations
income of $23.2M, $10.7M and **$(1.6)M** across FY2024 to FY2026, on an eight-year return-on-equity
series running from +71.7% to −39.7%. (2) *Massive liquid assets*: $43.9M of cash against a $500M
balance sheet and no debt; ample, not massive. (3) *No significant near-term cash requirements*
— **the one that usually kills** — is the interesting line, and it points at Q1's guarantee:
the **$63.5 million floor-plan repurchase obligation** reserved at **$1.5 million**, up from
$41.0 million a year earlier. **[E4-40]** is the corpus's warning about scoring that from a
loss history (*"We incurred no material impact from repurchase events during the years ended
June 30, 2026, 2025, and 2024"*) rather than from exposure: *"focusing on experience, rather
than exposure … not only useless, but actually dangerous."*

**The [E4-25] window rebuild, run because the brief ordered it and it could run here.**
This is the arithmetic only; it decides nothing and it is not a clearance.

| construction | window | mean operating cash flow | mean SBC | (c) = D&A | (c) = total capex |
|---|---|---|---|---|---|
| corpus five-year default **[E2-42]** | FY2022–FY2026 | $57,220k | $3,359k | mean $11,719k → **$42.1M** | mean $15,965k → **$37.9M** |
| long window | FY2018–FY2026 | $54,458k | $2,634k | mean $10,403k → **$41.4M** | mean $15,700k → **$36.1M** |
| the wave removed | FY2024–FY2026 | $26,198k | $3,210k | mean $11,471k → **$11.5M** | mean $11,228k → **$11.8M** |

*(All three rows use total-company operating cash flow, total-company capex and total-company
D&A, so the numerator and the denominator cover the same perimeter in each row. Sources: FY2026,
FY2024, FY2022 and FY2020 10-K consolidated statements of cash flows, with the FY2018–FY2021
years taken from XBRL as then reported and labelled as such.)*

**Combined range across both windows and both capex ends: roughly $36M to $42M.** The
**window spread is 1.7% at the D&A end and 4.8% at the capex end**, and the **capex band is 10%
to 13%**, which taken alone would read as a stable business. It is not, and the third row is
why: **delete the three years of the wave and the same arithmetic produces $11.5M to $11.8M,
about thirty cents on the dollar of the figure the long windows give.** **[E4-41]** is the
governing instruction (*normalize the mean DOWN for luck*: favourable exogenous breaks in the
window are named and removed before the mean is trusted), and **[E4-38]** names the disease the
narrow spread conceals: *"growth-rate presentations can be significantly distorted by a
calculated selection of either initial or terminal dates."* A five-year and a nine-year window
that agree to within 2% agree only because **both of them contain FY2022 and FY2023**.
**The screen's own `best_year_dep_oe` of 0.209 was pointing at this and the narrow `spread` of
0.271 was pointing away from it. The dependence statistic was the honest one.**
**Disclosed limits of this arithmetic, stated rather than buried:** (a) fiscal 2026 contains only
**six weeks** of Marine Products while the share count and the cap contain all of it, so the
trailing figure understates a pro-forma combined business; (b) fiscal 2022 and 2023 operating
cash flow is as-then-reported and includes NauticStar and Aviara, which later became
discontinued operations; (c) **(c) is a disclosed guess and must be [E2-23]** — the D&A end is
used as the corpus default **[E3-44, E2-41]** and is not treated as invalid, because boat
assembly is not the railroad or airline class **[E5-20]**, but the recent-year capex of $8.1M to
$10.5M sits below D&A of $9.6M to $13.7M largely because amortisation of purchased intangibles
is in the D&A line and is not a renewal cost, which cuts the other way and is why both ends are
shown.

**Great, good, or gruesome [E4-20]: not scored, and the reason is honest.** On the nine-year
mean it would read *good*; on the post-wave three years it would read closer to *gruesome*; and
**[E4-43]** warns against over-reading the *good* class in either direction. The gate is closed
and a class would be a conclusion drawn on a question that was never opened.

**The named way this business dies, written down because the brief asked for it and because
[E4-51] says an opinion is not earned without the argument against it.** *The mechanism:* a
consumer recession takes retail boat registrations down another 20% to 30%; dealers stop
ordering to protect their floor-plan interest bill; MCFT's shipments fall again toward the
FY2025 level; a handful of the 287 dealers fail; the floor-plan lenders foreclose and put the
repossessed units back to MCFT under the repurchase commitment. *Quantified from filed figures:*
the gross repurchase exposure is **$63.5M**, the reserve against it is **$1.5M**, and cash at
2026-06-30 is **$43.9M**. A repurchase event consuming a quarter of the gross exposure, roughly
$16M, is larger than ten times the reserve and would land in a year in which continuing
operations already lost money. *Likelihood:* **a real possibility**, not a likelihood, and
**not a solvency event**, because there is no funded debt to accelerate and the obligation is
capped: *"The Company's obligations under such floor plan agreements are subject to various
calculations and caps based on amounts currently owed by dealers to these financial
institutions."* **The argument against my own position, stated as [E4-51] requires:** no dealer
default of any size has occurred in three years, the exposure is collateralised by boats that
can be resold, MCFT carries zero debt and $43.9M of cash, and the single profitable segment
earned $21.5M of operating income in the worst retail year of the cycle. **That is a real
counter-case, and it is a Q4 counter-case; it does not reach Q2, which is where this file
closed.**
`Screens/SURVIVAL SHAPES - index.md` is not consulted for a shape, because naming a survival
shape is a Q4 output and Q4 was not opened.

---

*The template's Q4 apparatus is left unfilled below, deliberately, for the same reason as Q3.*

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** *"Using precise numbers is,
in fact, foolish; working with a range of possibilities is the better approach."* Do **not**
pick a window and defend it; carry the spread alongside the capex band.
- **Short-window mean** (window: ____ ): ____
- **Long-window mean** (window: ____ ): ____
- **Spread, conservative end:** ____ %
- **Combined range** (window spread × capex band): ____ to ____
- *Is that range too wide to reach a conclusion? If yes, **that is the verdict** **[E4-25]** —
  close the file, do not resolve it by preference:* ____
- *A wide spread is also a Q4 finding: a distorted year sits in the window (a pandemic year, an
  acquisition, a disposal), which bears on earnings reliability **[E5-11]**. Name it: ____*
- Owner earnings by year: ____
- **Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT.** D&A is the default proxy
  **[E3-44, E2-41]**; for capital-intensive businesses the D&A end is INVALID and (c) is judged
  up from total capex **[E5-20]**. Which case is this, and why: ____
- Band used ____ ; where in
  the band it sits and the reason cited from the filing: ____
- Stock compensation subtracted in full **[E5-06]**: ____
- *If the capex band changes the verdict → **UNKNOWABLE**.*

### Great, good, or gruesome? **[E4-20]**
- [ ] great — high return, rising, little capital needed
- [ ] good — attractive return, earned also on added capital
- [ ] gruesome — grows, eats capital, earns little
- Evidence: ____

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings ____
- (2) massive liquid assets ____
- (3) **no significant near-term cash requirements** ____  ← *the one that usually kills*
- Leverage, named and quantified **[E4-16, E3-29]** — *there is no ratio ceiling in this
  framework and the corpus supplies none*: ____

### Name the specific way THIS business dies **[E2-27, E3-24]**
- The mechanism: ____
- Quantified from filed figures, and the resulting outcome: ____
- Likelihood: [ ] likely [ ] a real possibility [ ] a low-level possibility
- *If no mechanism can be named at all → consider **UNKNOWABLE**.*
- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**
  **NO BOX TICKED. Q4 WAS NOT OPENED** because Q2 returned OUT. The owner-earnings arithmetic,
  the three strengths and the named death above are recorded observations, not a verdict.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

⛔ **NOT OPENED. Q1 through Q4 do not all show IN: Q2 returned OUT.** No valuation verdict is
given, no ranking position is assigned, no band is armed.

# COMPUTATION — NOT A CLEARANCE

*Produced only because the register entry in `Screens/WATCHLIST RUN QUEUE.md` requires a price, a
share count with its cover accession, a cap and a sovereign, and because the screen's cap was
wrong and the correction is owed to the reader. **It carries no entry language and it votes on
nothing.** Operator rule 3.*

**THE PRICE, FLAGGED AS AN AGGREGATOR QUOTE.**
- **$19.82**, close of **2026-09-18** (the last completed session; this run is dated Sunday
  2026-09-20). Source: **Yahoo Finance chart API, an AGGREGATOR, flagged as such under operator
  rule 5**, raw response saved at
  `Test Runs/_research 2026-09-20 MCFT/quote_MCFT_yahoo.json`. Preceding closes for context:
  19.15 (09-16), 20.13 (09-17), 19.82 (09-18).

**THE CAP, RE-STRUCK BY HAND.**
- shares: **24,339,371**, issued and outstanding **as of 2026-09-04**, from the cover page of the
  **Form 10-K for the fiscal year ended June 30, 2026, accession 0001193125-26-387432**, filed
  2026-09-10.
- second class: **none.** Section 12(b) registers Common Stock only; Section 12(g) states *"None"*.
- 24,339,371 × $19.82 = **$482,406,133**, call it **$482M**.
- *(The balance sheet at 2026-06-30 carries 24,437,538 shares issued and outstanding, 98,167 more
  than the 2026-09-04 cover count, the difference being share retirements between the two dates.
  The cover count is used because the framework's instruction is to take the share count from the
  cover of the newest periodic report. At the balance-sheet count the cap would be $484.4M, a
  0.4% difference that changes nothing.)*
- **The screen's $389M is superseded.** It was 16.3 million pre-merger shares at an earlier
  price; the merger of 2026-05-15 added roughly 8.0 million shares.

**THE SOVEREIGN.** **5.34%**, 30-year US Treasury par yield, **2026-09-18**, from the **US
Treasury daily par yield curve**, the issuing authority. FRED DGS30 not used.

**THE ARITHMETIC, for the register only.**
- owner earnings, from the Q4 observations: **$36M to $42M** on the two long windows;
  **$11.5M to $11.8M** with the three wave years removed **[E4-41]**.
- $36M to $42M ÷ $482M = **7.5% to 8.7%**. With the wave removed: **2.4%**.
- against the sovereign at 5.34%: **+2.1 to +3.4 points on the long windows, −2.9 points with
  the wave removed.**
- **The [E4-28] floor is ~10% and none of those figures reaches it.** This is the Berkshire
  configuration the operator protocol names: **above the bond and below the floor**, which under
  [E4-28] is *"the figure we quit on"* whatever the sovereign is.
- **The screen said 11.46% and −1.46% growth required.** It was 11.46% because it divided
  $45M–$57M of pre-merger owner earnings by a $389M pre-merger cap. Both numerator and
  denominator have since changed, and on the filed FY2026 figures at the re-struck cap the yield
  is **7.5% to 8.7%**, roughly three points lower.
- **THIS IS NOT A VERDICT.** The file closed at Q2 on the business. A name that fails Q2 does
  not get a price answer, and had this arithmetic come out at 20% it would have changed nothing.

# END COMPUTATION

---

*The template's Q5 apparatus is left unfilled below, deliberately. An unopened gate must look
unopened.*

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."* Honest
pre-tax expectancy at this price: ____ %. Below roughly 10%, the name is not ranked — it is
quit on, whatever the sovereign is. Above it, rank, and capital goes to rank #1 [E3-45].
**No risk premium in the discount rate [E3-42]** — certainty lives at Q1 and in Bar 1's
end discount, never in the rate.

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no
vote **[E3-34]**.

**1. THE YIELD**
- owner earnings ____ ÷ market cap ____ = **____ %** · sovereign **____ %**

**2. WHAT THE PRICE ALREADY ASSUMES**
- year-1 growth needed to justify the quote: **____ %**
- what the business has actually done: ____ %

**3. WHAT YOU ARE PAID**
- return at the current price = **____ points over the sovereign**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used ____ % — **the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — a point estimate claims precision this
method cannot support:
- conservative ____ · optimistic ____ · **current price** ____

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].** *(Corrected 2026-09-03, found by the
HHH run — this block still carried v4.0's "THERE IS NO HURDLE" heading, the SEVENTH
surviving home of the rule the framework rewrote on 2026-08-28. The floor section above at
[E4-28] already governs; this block is the ranking that applies only to what clears it.)*
- floor verdict first: honest pre-tax expectancy ____ % vs ~10% **[E4-28]** — **below →
  quit on, and the lines below are not filled in**
- points over sovereign, this name: ____
- against the rest of the opportunity set: ____
- *Take the best available, or nothing.*

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] **Normal method [E4-11]** — realistic inputs, one margin at the end.
      Margin used ____ %, and which corpus illustration it sits nearest:
      bridge ~35% **[E3-25]** · Grand Canyon 60%, the stated ceiling **[E3-26]** ·
      "closer to a dollar on the dollar" for a business you understand **[E4-12]** ·
      "dollar bills for 80 cents" **[E5-09]**
- [ ] **Screamer test [E4-01]** — does the price already clear the **conservative** case?
      No margin is added on top. Three outcomes: below the conservative case → act ·
      **inside the range → no useful conclusion, move on** · above the whole range → no.
- **Windage count** — conservatism applied at how many places? ____ *(more than one must be
  justified in writing)* **[E4-11]**

- **VERDICT: [ ] IN — RANKED, position ____  [ ] NOT IN — QUIT ON, below the ~10% floor [E4-28]  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**
  *(Box reworded 2026-09-20, decision 18 of the 09:32 audit. The old line had no way to record the
  floor's own outcome, so two runs improvised the word FAIL, 24 skipped the box, and one filled it
  in a way a reader would invert. At Q5 the rejection is [E4-28]'s* "that's the figure we quit on" *,
  a price answer and never a verdict about the business, so the box says QUIT ON, not OUT. A
  reader still reads the prose and the ranking position; the box now agrees with them.)*

  **NO BOX TICKED. Q5 WAS NOT OPENED.** The computation block above is headed as a computation
  and is not a clearance.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

⛔ **NOT OPENED. There is no position and no entry, so there is nothing to pre-commit
[E1-02].** No band is armed in `tools/alerts.json` and no `PORTFOLIO.md` row is added: a name
that failed on the **business** gets no price alert, which is the QLYS category error ruled on
2026-09-07.

**THE REVERSAL CONDITION, RECORDED IN WORDS INSTEAD, as the QLYS ruling requires.**
This file closed OUT at Q2 on the absence of a franchise. **What would have to be filed, not
merely hoped, to reopen it:**
1. **A gross-margin lead that survives a recovery.** MCFT's 6.9-point FY2026 gross-margin lead
   over Malibu appeared only in the trough and did not exist in FY2019 through FY2023. If MCFT
   still out-earns Malibu and closes on Brunswick **after industry volumes recover**, the
   [E2-58] exception (*a cost advantage both wide and sustainable*) becomes arguable on eight
   more years of evidence rather than on two.
2. **The physical series turning up and staying up [E4-55].** MasterCraft brand units above
   roughly 2,500 and Crest above roughly 1,500, held for two consecutive years, without a
   corresponding rise in dealer incentives.
3. **The filer retiring its own substitute language.** Criterion 2 of [E3-03] failed on the
   registrant's own risk factors. A 10-K that no longer names used boats, rival price cuts and
   its own Chaparral as competitors for the same customer is the document that would move this.
4. **A Chaparral-versus-MasterCraft resolution.** The FY2026 10-K discloses *"intra-company
   competition that could affect the sales or pricing of products within our portfolio."* A
   franchise does not compete with itself.
**And the honest note against my own verdict [E3-47]:** *"our most egregious mistakes fall in
the omission, rather than the commission, category … their invisibility does not reduce their
cost."* This is a debt-free, cash-generative manufacturer of an iconic 1968 brand whose single
good segment earned $21.5M of operating income in the worst retail year of the cycle, trading at
$482M. If the OUT is wrong, that is where the cost of being wrong lives, and it is written down
here so it is visible rather than invisible.

---

*The template's Q6 apparatus is left unfilled below, deliberately.*

**Pre-committed before entry [E1-02]:**
- Thesis-confirming metric: ____
- **Thesis-breaking metric and its threshold:** ____
- Next catalyst date: ____

**The sell rule [E2-28]** — two triggers, three hold conditions:
- SELL if the market judges it more valuable than the facts indicate ____
- SELL if funds are needed for something more undervalued or better understood ____
- HOLD while: return on equity capital satisfactory ____ · management competent and honest
  ____ · market does not overvalue ____
- *Price appreciation and holding period are **explicitly rejected** as reasons to sell.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring
question: is this erosion an aberrational cycle, or has the business slipped in a way that
permanently reduces intrinsic value? ____

**Do not trim winners [E5-14].** **Position size** — a judgment, stated: ____
*(sized DOWN if a capital-allocation flag is live)*

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**
  **NO BOX TICKED. Q6 WAS NOT OPENED.** There is no position and no entry, so there is nothing
  to pre-commit **[E1-02]**. The reversal condition is recorded in words above instead of as a
  price band, because the name failed on the business (the QLYS ruling, 2026-09-07).

---
## SELF-AUDIT
*A ticked box in a template is not a verdict. Each line below is answered in words.*

- [x] **Questions answered in order; no verdict skipped.** Q1 IN, Q2 OUT, and the run stopped
      there. Q3, Q4, Q5 and Q6 are headed NOT OPENED, carry no ticked verdict box, and their
      template apparatus is left blank on purpose so an unopened gate looks unopened.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** The only IN in
      this file is Q1, and every element of it is quoted from the FY2026 10-K.
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** There are no
      UNRESEARCHED verdicts in this file. Work deliberately not done inside the closed gates is
      listed by name at Q3 so the omission is visible.
- [x] **Every UNKNOWABLE verdict states what specifically cannot be known.** There are no
      UNKNOWABLE verdicts in this file. Q2 is OUT on filed evidence, not UNKNOWABLE: the
      separating question *"can I name the document that would resolve this?"* did not need to be
      asked, because the resolving document was read and it closed the gate.
- [x] **Step 0: the filing was read, with accession number; a figure was cross-checked.** FY2026
      10-K, accession 0001193125-26-387432, filed 2026-09-10. Cross-check: continuing-operations
      operating cash flow for fiscal 2024, $12,200 thousand, taken off the filed Consolidated
      Statements of Cash Flows where tagged data carried two conflicting values.
- [x] **Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.**
      Done in the Q4 observation block, on three windows, with (c) shown at both the D&A default
      **[E3-44, E2-41]** and the total-capex end, and with the perimeter limits of each row
      disclosed. **Never via a net-income proxy.** It is labelled an observation, not a verdict,
      because Q4 was not opened.
- [x] **Competitor row filled, or the moat marked PROVISIONAL and UNRESEARCHED.** Filled: six
      SEC-filing peers plus the acquired Marine Products, same metric, same window,
      filing-sourced, with the four unreachable private and foreign competitors named with rung
      and obstacle and with a written reason why their absence cannot hold the class PROVISIONAL.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** USD 5.34%,
      2026-09-18, US Treasury daily par yield curve, struck fresh in this run. FRED not used.
- [x] **Value stated as a round-number range, not a point estimate.** No value is stated at all,
      because Q5 was not opened. The computation block reports a yield range (7.5% to 8.7%) in
      round figures and is headed COMPUTATION — NOT A CLEARANCE.
- [x] **One bar chosen, not both; windage count stated.** Neither bar is used; no margin of
      safety is applied anywhere in this file. **Windage count: zero.** Conservatism is not spent
      at any point, because no valuation was performed.
- [x] **Prices dated; aggregator used for live quotes only and flagged.** $19.82 at 2026-09-18,
      Yahoo Finance, flagged as an aggregator, raw response saved to the research folder. Every
      other figure in this file comes from an SEC filing.
- [x] **Run committed to git.** Committed after Step 0, after Q1, after Q2, and at the fold, each
      time with a pathspec and a fresh message file.

**Violations found on my own file, recorded rather than silently corrected:** none found. The
one judgment call worth flagging for a reader is that **I resolved `best_year_dep` 0.186 against
`best_year_dep_oe` 0.209 in favour of the owner-earnings construction**, and I did so on operator
rule 8 plus **[E2-23]** rather than on a corpus passage about that statistic, because the corpus
contains no such statistic. If a later run disagrees, the arithmetic for both is written out at
Step 0 and can be re-derived in two minutes.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line:** MasterCraft Boat Holdings fails **[E3-03]** criterion 2 in its own FY2026 risk
  factors, which name three classes of close substitute (rival new boats, **used boats**, and
  since 2026-05-15 its own newly acquired Chaparral) and state that competition is conducted
  *"primarily on brand name, price, product selection, and product performance"*; a same-metric
  eight-year competitor row across six SEC filers shows every name printing its best operating
  margin in FY2021–22 and its worst in FY2025–26, which is **[E3-51]**'s surfing run, with MCFT
  taking the deepest peak-to-trough revenue fall in the row at **−59.9%** while its physical unit
  series **[E4-55]** halved. **Q1 IN · Q2 OUT · file closed at Q2.**
- **If UNRESEARCHED — THE WORK ORDER:** n/a.
- **If UNKNOWABLE:** n/a.
- **Price and cap, re-struck by hand:** $19.82 (2026-09-18, Yahoo Finance, aggregator, flagged)
  × 24,339,371 shares (cover of the FY2026 10-K, accession **0001193125-26-387432**, as of
  2026-09-04, one class only) = **$482M**. **Sovereign 5.34%**, 30-year US Treasury par yield,
  2026-09-18, issuing authority.
- **Reversal condition, in words, because a Q2 failure gets no price band:** see Q6 above. No
  entry in `tools/alerts.json`; no row in `PORTFOLIO.md`.
