# Company Run - INSTEEL INDUSTRIES INC (IIIN) - 2026-09-21
**Wave 7, name 20 of 218. Unattended overnight cycle.** Run under `Framework/THE FRAMEWORK v4.md`
(v4.1) and the operator protocol in `CLAUDE.md`. Research folder:
`Test Runs/_research 2026-09-21 IIIN/`.

**STATUS: CLAIMED 2026-09-21. Filling top to bottom; each question committed as it closes.**

**THE SCREEN ROW, CARRIED UNLABELLED** from `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv` -
a machine's output and the thing being tested, not an input to any verdict:

```
IIIN,INSTEEL INDUSTRIES INC,588,40,57,0.441,$40M to $57M,,,,"ONE LINE MADE THE CASH: AccountsPayableAndAccruedLiabilities moved 71% of 2025 OCF. Operating cash is not owner earnings when one balance-sheet line produced it (DELL, INOD). Read the 2025 cash-flow statement and liquidity note.",0.0674,0.0139,0.0326,2.13,STEP UP - normalize down [E4-41],0.238,"ONE YEAR CARRIES THE WINDOW - a tight spread here is arithmetic, not knowledge; re-price on a wi (9-yr OCF series)",n/a,EARLY HALF STRADDLES ZERO - the pre-window years run from $-12.7M to $,0.328,FLAGS DISAGREE - one series refuses the ratio and the other does not; read the filing [E4-25],n/a,17,WINDOW DISAGREE - 9yr and the full 17yr series give different KINDS of answer; the 9yr base may already contain the wave [E4-41],"acquisitions are $72M, 12% of cap, inside the window.",,4-construction width only (3y/5y x two capex ends): CANNOT see variation older than the 5-year window; rebuild it [E4-25],2025-09-27,2026-06-27
```

**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS - every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order - not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation - it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 - THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** - the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **2026-09-18** (the newest published print; 2026-09-21 is a Monday) ·
  source (issuing authority) **US Treasury daily par yield curve, 30-year par yield**, struck
  fresh this run through `tools/sources.py`. **FRED DGS30 was not used and is the fallback,
  not the source.**
- FX: none. Insteel earns in USD. The FY2025 10-K, Item 1: *"We sell our products nationwide
  across the U.S. and, to a much lesser extent, into Canada, Mexico and Central and South
  America."* Non-US sales are disaggregated in Note 15 and are immaterial to the currency choice.

**THE PRICE - AGGREGATOR, FLAGGED, LIVE QUOTE ONLY (operator rule 5).**
- **$29.66**, close of **2026-09-18**, Yahoo Finance chart API via `tools/sources.py`. Raw
  response saved to `Test Runs/_research 2026-09-21 IIIN/price_raw_aggregator.json`
  (`regularMarketPrice 29.66`, `currency USD`, `fullExchangeName NYSE`). **This is the only
  number in the file that comes from an aggregator.**

**THE SHARE COUNT AND THE CAP - STRUCK BY HAND OFF THE COVER OF THE NEWEST PERIODIC FILING.**
- Cover of the **Form 10-Q for the quarterly period ended June 27, 2026**, filed 2026-07-16,
  **accession 0001437749-26-023682**, verbatim: *"Common Stock (No Par Value)"* …
  **"19,358,247"** … *"Number of Shares Outstanding as of July 15, 2026"*.
- **ONE CLASS ONLY.** The FY2025 balance sheet reads *"Preferred stock, no par value Authorized
  shares: 1,000 None Issued"* and *"Common stock, $ 1 stated value Authorized shares: 50,000
  Issued and outstanding shares: 2025, 19,420 ; 2024, 19,452"* (thousands). **Insteel is the ADM
  shape, not the BELFB shape**: single class, current cover, count falling slowly on buybacks.
  The dual-class cover-tag defect that made BELFB's screen cap wrong by 6.29x cannot arise here,
  and it was checked rather than assumed.
- **Splits after the measurement date: none.** `split_factor_after('IIIN','2026-07-15')` returns
  **1.0**. `cap = close(anchor) × shares(measurement) × splits AFTER measurement`
  = 29.66 × 19,358,247 × 1.0 = **$574.2M**, on `close`, never `adjclose`.
- **Against the screen's 588, the screen is 2.4% high.** This is not the BELFB or FC defect
  class - it is a stale price, not a wrong count: 588 ÷ 19,358,247 implies $30.37, which sits
  inside the range the 10-K itself discloses, *"During fiscal 2025 our common stock traded as
  high as $41.64 and as low as $22.49."* **The cap used everywhere below is the hand-struck
  $574.2M.**

**The filing was read** - not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **Form 10-K for the fiscal year ended September 27, 2025**, filed 2025-10-23,
    **accession 0001437749-25-031597** (`iiin20250927_10k.htm`) - the newest ANNUAL filing.
  - **Form 10-Q for the quarter ended June 27, 2026**, filed 2026-07-16,
    **accession 0001437749-26-023682** - the newest PERIODIC filing.
  - **DEF 14A filed 2026-01-02, accession 0001308179-26-000001** (read at Q3).
  - **8-K / EX-99.1 earnings releases** of 2025-10-16 (acc. 0001437749-25-031106), 2026-01-15
    (0001437749-26-001309), 2026-04-16 (0001437749-26-012485) and 2026-07-16
    (0001437749-26-023670); plus the EX-99.1 of **2026-08-21** (0001437749-26-028729, the Upper
    Sandusky closure) and **2026-08-11** (0001437749-26-027019, the dividend declaration).
- **FY2026 HAS NOT CLOSED AND NO 10-K FOR IT EXISTS.** Insteel's year ends on the Saturday
  nearest 30 September; FY2025 ended 2025-09-27 and FY2026 ends **2026-10-03**, twelve days
  after this run. The newest periodic filing is therefore the **third quarter of FY2026** (period
  ended 2026-06-27), exactly as the screen row's `newest_periodic` says. Checked against the
  submissions index, not assumed.
- **figure cross-checked against the filed statement - three, by hand, against the filed
  statements and not against XBRL:**
  1. **FY2025 operating cash flow $27,163 thousand**, read off the filed Consolidated Statements
     of Cash Flows (*"Net cash provided by operating activities 27,163"*), equal to the
     companyfacts figure used in the series below.
  2. **Shareholders' equity recomputed from A − L** *(the [E5-32] cross-check: Salomon's books
     carried an invented number for twelve audited years, so audited does not mean true)*: total
     assets **$462,650** less total current liabilities **$66,009** less other liabilities
     **$25,109** = **$371,532**, which is the filed *"Total shareholders' equity 371,532"* to
     the dollar.
  3. **FY2025 net sales $647,706 thousand** on the filed Consolidated Statements of Operations,
     against the MD&A's *"Net sales increased 22.4% to $647.7 million in 2025 from $529.2 million
     in 2024"* - the two agree and the percentage is arithmetic on them.

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language:** Insteel buys hot-rolled carbon
  steel wire rod by the ton, draws and welds it into two products - seven-wire prestressing
  strand, and welded wire sheets and rolls - and sells them by the ton to the people who cast
  concrete. **The whole business is one arithmetic line: tons shipped × (price per ton less rod
  cost per ton), less conversion cost, less freight.** Nothing else moves the result. The filing
  writes the same equation without disguising it (FY2025 10-K, Item 1, Raw Materials):
  *"Selling prices for our products tend to be correlated with changes in wire rod prices.
  However, the timing and magnitude of the relative price changes vary depending upon market
  conditions and competitive factors. Ultimately, the relative supply - demand balance in our
  markets and competitive dynamics determine whether our margins expand or contract during
  periods of rising or falling wire rod prices."* FY2025 is that equation worked: gross profit
  rose $43.8M, and the MD&A attributes *"higher spreads between average selling prices and raw
  material costs ($36.1 million)"* - **82% of the improvement was spread, not volume.**
- **The scarce input this business controls:** **on the evidence, none.** The rod is bought, not
  made - *"which we purchase from both domestic and foreign suppliers and can generally be
  characterized as a commodity product"* - and imports were *"approximately 27% and 15%"* of
  total wire rod purchases in FY2025 and FY2024. What Insteel actually holds is **freight
  geometry**: eleven owned plants *"all located in the U.S. in close proximity to our customers
  and raw material suppliers"*, in a product whose value-to-weight ratio makes long hauls
  uneconomic. It claims its buying scale as an advantage - *"We believe that our substantial
  wire rod requirements, desirable mix of sizes and grades and strong financial condition
  represent a competitive advantage by making us a relatively more attractive customer to our
  suppliers"* - and that claim is tested at Q2 against the vertically integrated competitors the
  same section names. It is not a scarce input owned, and Q1 does not credit it as one.
- **Will the fundamentals look broadly the same in ten years?** Yes. Concrete has been reinforced
  with drawn steel wire for a century, the product is written into building codes and into
  *"Buy America"* melt-and-cast rules, and the 10-K's own list of what moves the result - rod
  price, construction activity, import competition, freight - is the same list it would have
  carried in 2009. This is **[E3-31]**'s *"relatively simple and stable in character"*, not a
  business *"complex or subject to constant change"*. **The volatility is in the numbers, not in
  the character of the business**, which is the distinction **[E3-55]** draws: *"If we have a
  business about which we're extremely confident as to the business result, we would prefer that
  it have high volatility than low volatility."*
- **The five-minute test [E4-46]:** *"if we can't make a decision in five minutes, we can't make
  it in five months. You know, we're not going to learn enough in the **followings** five months
  to make up for the fact that we went in deficient in the first place."*
  **Transcript artifact flagged, not smoothed (PRIME RULE 1):** the ledger row reads
  *"followings five months"*, and `Framework/THE FRAMEWORK v4.md` quotes the same passage as
  *"following five months"*, dropping the *"You know,"* as well. **The corpus wins (PRIME RULE 2),
  so this run quotes the row. Reported as a finding, not repaired by this run, because the
  framework is a governing document and editing one to match a run is the wrong direction.** Nothing here needed five months: one
  reportable segment, two product lines, no debt, no float, no equity-method stakes, no foreign
  subsidiaries of substance, and a cash-flow statement of sixteen lines.

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____
  *IN on understanding only. Understanding a commodity converter is not a finding that it is a
  good business - that is Q2's question, and the commodity doctrine at **[E2-58]** is where it
  gets asked.*

## Q2 - IS IT A FRANCHISE? **[E3-03]**

**The definition, applied line by line, quoted from the ledger row:** *"An economic franchise
arises from a product or service that: (1) is needed or desired; (2) is thought by its customers
to have no close substitute and; (3) is not subject to price regulation. The existence of all
three conditions will be demonstrated by a company's ability to regularly price its product or
service aggressively and thereby to earn high rates of return on capital."* **[E3-03]**, 1991
letter. **Note the row's second sentence, which the test above is usually read without: the
three conditions are demonstrated by regular aggressive pricing and high returns on capital.
Insteel's filings evidence neither.**

- **Needed or desired [x]** - yes, and without qualification. Reinforced concrete cannot be
  poured without it, and the products are written into building codes and into federal and state
  *"Buy America"* melt-and-cast rules (FY2025 10-K, Item 1).
- **No close substitute [ ] - THIS IS WHERE IT FAILS, AND IT FAILS ON THE COMPANY'S OWN
  WORDS.** Three separate statements in the FY2025 10-K, Item 1:
  1. *"Our markets are highly competitive based on price, quality and service."*
  2. Seven named makers of the identical products: *"Our primary competitors for WWR products
     are Wire Mesh Corporation, Concrete Reinforcements, Inc., National Wire Products, Davis
     Wire Corporation and Oklahoma Steel & Wire Co., Inc. Our primary competitors for PC strand
     are Sumiden Wire Products Corporation and Wire Mesh Corporation."* Plus imports:
     *"Import competition is also a significant factor in certain segments of the PC strand and
     SWWR markets that are not subject to 'Buy America' requirements."*
  3. **Its own flagship product is sold AS a substitute for something else** - ESM *"is an
     engineered made-to-order product that is used as the primary reinforcement for concrete
     elements or structures, frequently serving as a lower cost reinforcing solution than
     hot-rolled rebar."* A product whose sales pitch is that it undercuts the incumbent
     alternative is in a substitution relationship, and substitution runs both ways.
- **Not price-regulated [x]** - no rate regulation. But see the **[E2-59]** reading below: what
  Insteel has instead of a franchise is a *trade* regime, and that is the opposite case.

**One of three criteria fails, so [E3-03] is not satisfied. The rest of this question is the
work of establishing that the failure is the real thing and not a reading error.**

### The commodity doctrine, which is the class this business is in [E2-58]

> *"persistent over-capacity without administered prices (or costs) equals poor profitability"*,
> with long-term profitability set by *"the ratio of supply-tight to supply-ample years"*, and
> the one exception being *"a cost advantage that is both **wide and sustainable** … By
> definition such exceptions are few."* - **[E2-58]**

The 10-K puts the business inside that equation itself: *"The primary raw material used to
manufacture our products is hot-rolled carbon steel wire rod … can generally be characterized as
a commodity product"*, and *"Ultimately, the relative supply - demand balance in our markets and
competitive dynamics determine whether our margins expand or contract."*

**And the ratio of supply-tight to supply-ample years is on the record, published by the company
itself.** The 2026 proxy prints fifteen years of return on capital as calculated under its own
incentive plan (DEF 14A 2026-01-02, acc. 0001308179-26-000001):

| FY | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ROC (ROCICP) | 5.1% | 1.4% | 7.7% | 10.4% | 11.1% | 23.1% | 12.5% | 16.6% | 1.8% | 9.7% | 36.9% | 47.6% | 9.1% | 6.3% | 14.1% |

Fifteen-year mean **14.2%**; **strip the two steel-spike years 2021-22 and the remaining thirteen
average 9.9%**, with three years under 2%. That is *"the ratio of supply-tight to supply-ample
years"* rendered as a table by the company's own compensation committee. **[E3-46]** asks the
second question about the business as a number - *"the best businesses, by definition, are going
to be businesses that earn very high returns on capital employed over time"* - and a
thirteen-year ex-spike mean near ten is not that.

### Is the exception present - a cost advantage both wide and sustainable?

**No, and the filing says why.** Insteel's stated strategy is *"operating as the lowest cost
producer in our industry"*, but the same Item 1 concedes the structural problem in one sentence:
*"Some of our competitors, such as Wire Mesh Corporation, Nucor Corporation and Oklahoma Steel
and Wire, are **vertically integrated companies that produce both wire rod and concrete
reinforcing products** and offer multiple product lines over broad geographic areas."*

**Wire rod is not a component of Insteel's cost - it is essentially the whole of it.** FY2025
cost of sales was **$554,268** thousand on net sales of **$647,706** thousand (filed Consolidated
Statements of Operations), **85.6% of sales**, and the MD&A attributes the year's entire margin
swing to *"higher spreads between average selling prices and raw material costs ($36.1
million)"*. **The competitors named above own the input that sets 85% of Insteel's costs;
Insteel buys it, 27% of it from abroad in FY2025.** That is the reverse of a wide and sustainable
cost advantage, and the competitor row below shows it has not produced one.

### THE COMPETITOR ROW - required [E3-28]

> *"I can't be an intelligent owner of a business unless I know what all the other businesses in
> that industry are doing."* - **[E3-28]**

**Same metric, same window, filing-sourced.** Metric: **return on shareholders' equity, net
income ÷ year-end shareholders' equity**, computed identically for every row from each filer's
own 10-K facts, **FY2010 through FY2025, sixteen consecutive years**. Equity is the right
denominator here because none of these filers is an acquisition vehicle with a large goodwill
wedge and Insteel carries **no debt at all**, so its ROE is its return on capital employed with
no leverage flattering it - **the [E2-01] test run in the subject's favour.**

| Company | metric | window | 16-yr mean | min | max | source |
|---|---|---|---|---|---|---|
| **INSTEEL (IIIN)** | net income ÷ year-end equity | FY2010–FY2025 | **9.9%** | −0.3% (FY2011) | 32.1% (FY2022) | own 10-K facts, CIK 764401; FY2025 figures hand-checked against the filed statements above |
| Nucor (NUE) | same | FY2010–FY2025 | **14.6%** | 1.1% (2015) | 48.7% (2021) | Nucor 10-K facts, CIK 73309 |
| Steel Dynamics (STLD) | same | FY2010–FY2025 | **17.7%** | −5.4% (2015) | 51.0% (2021) | Steel Dynamics 10-K facts, CIK 1022671 |
| Commercial Metals (CMC) | same | FY2010–FY2025 | **8.9%** | −16.4% (FY2010) | 37.0% (FY2022) | Commercial Metals 10-K facts, CIK 22444 |

**The row is cross-checked against a peer's own words, not left on tagged data.** Nucor's FY2025
10-K (filed 2026-02-25, accession 0001193125-26-071575) states in its MD&A: *"Return on average
stockholders' equity was 8.5% and 9.8% in 2025 and 2024, respectively."* My identically
constructed figures are 8.3% and 10.0% - the gap is average-equity versus year-end-equity and
nothing else, so the row's construction reproduces a filer's own disclosure to within a fraction
of a point.

**Peers named: 7 of the 7 real competitors the subject's own filing names, plus 2 substitute
producers. Peers OBTAINABLE: 1 of the 7, and even that one unsegmented.**

| Named in Insteel's Item 1 | status | disclosed |
|---|---|---|
| Wire Mesh Corporation (WWR **and** PC strand - named in both lines, the only one that is) | private | **UNOBTAINABLE** - EDGAR company search returns *"No matching companies"* |
| Concrete Reinforcements, Inc. | private | **UNOBTAINABLE** - same search, no matching companies |
| National Wire Products | private | **UNOBTAINABLE** - same |
| Davis Wire Corporation | private (Heico Companies) | **UNOBTAINABLE** - neither name files |
| Oklahoma Steel & Wire Co., Inc. | private | **UNOBTAINABLE** - same |
| Sumiden Wire Products Corporation (PC strand) | foreign parent, unsegmented | **UNOBTAINABLE** - no SEC filer |
| Nucor Corporation | public, **unsegmented for wire/reinforcement** | in the row, at the company level only |
| *(substitute producers, not named by Insteel)* Steel Dynamics, Commercial Metals | public, unsegmented | in the row for the rebar substitute |

**This incompleteness is disclosed and it changes nothing about the verdict, for a reason worth
stating plainly.** The framework's rule is that an unavailable peer holds the **moat class
PROVISIONAL**, which is UNRESEARCHED - and that rule exists to stop a run **crediting** a moat it
has not checked against the field. **It does not license a run to withhold a negative finding
that rests on the subject's own filing.** Nothing a private competitor's accounts could show
would convert *"Our markets are highly competitive based on price, quality and service"* and a
product sold as the cheaper alternative to rebar into *"no close substitute"* **[E3-03]**. The
class recorded below is **NONE**, and the missing rows could only make it worse, never better.

**And the row's limit is stated [E3-61]:** identical structures produce opposite conduct - *"In
some businesses, the participants behave like a demented Kellogg. In other businesses, they
don't … **I think you'd have to know the people involved.**"* The row shows Insteel earning the
lowest sixteen-year return of the four, unlevered; it cannot show whether the private half of the
industry is disciplined or demented. On the filed evidence of FY2024 - below - it has been
behaving like the latter.

### The physical series, which is the honest one [E4-55]

> "In 2006, Precision Steel's service center volume was 46 million pounds, down from 69 million
> pounds sold as recently as 1999. **This decline in physical volume is a serious reverse, not
> likely to disappear in some ""bounce back'' e?ect.** Nor do we expect another sharp rise in
> prices like the approximately 40% rise that recently occurred, holding dollar volume roughly
> level despite a precipitous drop in physical volume." - **[E4-55]**, 2006 Wesco letter
>
> *(The ledger row carries OCR damage: doubled opening quotation marks and a replacement
> character in "e?ect". Reproduced, flagged, and not smoothed, PRIME RULE 1.)*

**Insteel does not disclose tons.** The physical series exists only as year-over-year percentages
in each 10-K's MD&A, and that is a stated limit of the source, not a finding. Chained from the
filings:

| FY | shipments | average selling price | net sales | 10-K MD&A, verbatim |
|---|---|---|---|---|
| 2016 | **+2.6%** (+4.8% pro-forma 52 weeks) | −8.8% | −6.5% | *"as a 2.6% increase in shipments was offset by an 8.8% reduction in average selling prices"* |
| 2019 | **−7.1%** | +8.1% | +0.6% | *"an 8.1% increase in average selling prices partially offset by a 7.1% decrease in shipments"* |
| 2021 | **−0.6%** | +25.7% | +25.0% | *"a 25.7% increase in selling prices partially offset by a 0.6% decrease in shipments"* |
| 2022 | **−7.8%** | +51.9% | +40.0% | *"a 51.9% increase in selling prices partially offset by a 7.8% decrease in shipments"* |
| 2023 | **−5.3%** | −17.1% | −21.5% | *"a 17.1% decrease in selling prices along with a 5.3% decrease in shipments"* |
| 2024 | **~flat** | down | −18.5% | *"driven entirely by a decrease in average selling prices as shipments remained relatively flat"* |
| 2025 | **+14.8%** | +6.7% | +22.4% | *"a 14.8% increase in shipments and a 6.7% rise in average selling prices … primarily due to incremental volume generated from our acquisitions"* |

**Read it in that order and it is the Precision Steel shape exactly.** FY2022's headline is net
sales up 40%; the tons moved **down 7.8%**. Across FY2021–FY2024 the physical series runs −0.6%,
−7.8%, −5.3%, flat - **roughly thirteen per cent fewer tons over four years** - and the one
growth year, FY2025, is **bought**: the MD&A attributes it to *"incremental volume generated from
our acquisitions."* **Organic FY2025 tonnage is not separable from acquired tonnage in any filed
document**, which is recorded here as a limit rather than guessed at. **[E4-32]**'s direction test
- the moat *"widened every year"* being *"the primary criterion of a great business"* - returns
the wrong sign: the share is being purchased, not won.

### The pricing tests

- **[E2-44], the two-characteristic test - can it raise prices *"even when product demand is flat
  and capacity is not fully utilized"*? FAILS, on the filing.** FY2024: *"Net sales decreased
  18.5% … driven entirely by a decrease in average selling prices as shipments remained
  relatively flat. The decrease in average selling prices was driven by persistent competitive
  pricing pressures in our welded wire reinforcing markets, the impact of low-priced PC strand
  and a decline in raw material costs."* Flat demand, and price went **down**. The second half of
  [E2-44] - grow dollar volume *"with only minor additional investment of capital"* - also fails:
  FY2025's growth cost **$72.1 million of cash** for two competitors.
- **[E4-37], the inverse metric - the agony of a price increase.** The FY2025 10-K, Impact of
  Inflation: *"our ability to raise our selling prices depends on market conditions and
  competitive dynamics, and there may be periods during which we are unable to fully recover
  increases in our costs."* And the risk factors: *"we may be unable to fully recover increased
  rod costs during weaker market environments."* That is the agony end of the scale, in the
  company's own hedged language, and it is a permanent feature of the filings rather than a bad
  year's confession.
- **[E3-33] untapped pricing power - NOT PRESENT, and the scope rule [E5-28] is why the claim is
  not even attempted.** *"If you name some business that has incredible pricing power, you're
  talking about a business that's a monopoly or a near monopoly"* **[E5-28]**. Insteel is the
  largest producer in a market with six named direct rivals and live import competition. Claiming
  the [E3-33] class here would be claiming near-monopoly, and the competitor row refuses it.

### The trade regime - [E2-59], and this is the sharpest finding in the question

> "Businesses in industries with both substantial over-capacity and a "commodity" product
> (undifferentiated in any customer-important way by factors such as performance, appearance,
> service support, etc.) are prime candidates for profit troubles. **These may be escaped, true,
> if prices or costs are administered in some manner and thereby insulated at least partially
> from normal market forces. This administration can be carried out (a) legally through
> government intervention** (until recently, this category included pricing for truckers and
> deposit costs for financial institutions), (b) illegally through collusion, or (c)
> "extra- legally" through OPEC-style foreign cartelization" - **[E2-59]**, 1982 letter
>
> *(quoted from the ledger row's own `quote_verbatim`, not from the framework's summary of it.
> The row carries the source's spacing artifact "extra- legally", reproduced rather than
> smoothed, PRIME RULE 1.)*

**The brief asked whether trade remedies are doing the work a moat is being credited with. They
are, and the 10-K says so four times in one paragraph** - the same clause after each petition:

> *"The DOC ruled in our favor and imposed anti-dumping duties ranging from 12% up to 119%,
> **which had the effect of limiting the participation of these countries in the domestic
> market**."* (2003, five countries)
> *"final countervailing duty margins ranging from 9% to 46% and anti-dumping margins ranging
> from 43% to 194%, **which had the effect of limiting the continued participation of Chinese
> producers in the domestic market**."* (2010)
> *"the DOC ruled in our favor and imposed anti-dumping duties ranging from 4% to 194%, **which
> had the effect of limiting the participation of these countries in the domestic market**."*
> (2020–21, fifteen countries)
> *"the DOC ruled in our favor and imposed final countervailing duty margins ranging from 23% to
> 110%, **which had the effect of limiting the continued participation of Mexican producers in
> the domestic market**."* (SWWR, 2021)

**Whatever floor exists under PC strand and standard welded wire pricing is administered, and
the administrator is the Department of Commerce, not Insteel.** [E2-59]'s rule then applies
without adjustment: regulation *floors* a commodity business, and the moat belongs to the regime.
The risk factors concede the dependence in terms: *"**Trade law enforcement is critical to our
ability to maintain our competitive position against foreign PC strand and SWWR producers**"*,
and *"Such actions may be costly and may not be successful."*

**And the regime is demonstrably porous, which is the strongest available evidence that it is not
a moat at all.** Duties had been in force against five countries since 2003, China since 2010 and
fifteen more since early 2021 - and FY2024's price decline is attributed in the MD&A to *"the
impact of low-priced PC strand"* imports, with shipments *"adversely impacted by weaker market
conditions, increasing volumes of PC strand imports"*. FY2019 is the same story with the tariff
running the other way: *"Shipments for the current year were unfavorably impacted by an increase
in low-priced import competition spurred by the Section 232 tariff on imported steel"* - **a
trade measure aimed at helping the industry raised Insteel's rod cost and let finished imports in
underneath it.** A protection that has to be re-petitioned every decade and still lets the price
be set from abroad in the weak years is [E2-59]'s regime, not [E3-03]'s franchise.

### The remaining Q2 tests, each answered

- **[E2-53], the dominance class** - *"Once dominant, the newspaper itself, not the marketplace,
  determines just how good or how bad the paper will be. Good or bad, it will prosper."* **The
  inverse holds here.** Insteel *is* dominant by its own description - *"the nation's largest
  manufacturer of steel wire reinforcing products"* - and the marketplace still determines its
  economics completely: FY2024 return on capital of 6.3% and a 29%-of-target bonus, in the same
  plants, with the same position, as FY2022's 47.6%. **Dominance without pricing control is not
  the dominance class.**
- **[E2-45], the attacker's test** - *"how I would like, assuming I had ample capital and skilled
  personnel, to compete with it."* I would like it a great deal, and the filings say how: buy or
  build wire-drawing capacity near a metro market, buy rod on the same world market Insteel buys
  it on, and undercut. **Insteel has just demonstrated the entry cost: $72.1 million bought two
  going concerns with plants, equipment, customers and inventory, about 12.6% of its own market
  capitalisation.** A moat you can step over for a tenth of the incumbent's value is not a moat.
- **[E4-36], which of the four causes of extreme success** - the FY2021-22 result was
  **wave-riding**: a raw-material spike that lifted selling prices 25.7% and then 51.9% while
  **tons fell**. **[E3-51]**: *"when a surfer gets up and catches the wave and just stays there,
  he can go a long, long time. But if he gets off the wave, he becomes mired in shallows."* The
  wave broke in FY2023 and the 2024 return on capital was 6.3%. **The advantage lived in the
  wave, not in the surfer.**
- **[E4-04] is NOT the ground of this verdict, and that is deliberate.** Under the ruling of
  2026-09-20, [E4-04] is applied as a **competence limit**, never as a fourth franchise
  criterion, and a name that *passes* [E3-03] but whose durability cannot be judged closes
  UNKNOWABLE. **Insteel does not reach that door**: it fails [E3-03] criterion 2 on filed
  evidence, which is an OUT about the business, decided before [E4-04] is consulted. **Nor is
  [E4-23] used** - this business does not require a superstar; it requires a steel cycle.

- Primary moat metric, filing-sourced, and its trend: **gross margin, 17 years** - FY2009 −6.6%,
  then 8.5, 9.4, 6.2, 10.8, 11.9, 13.0, 20.4, 15.4, 15.6, 6.6, 11.8, 20.6, **23.9 (FY2022 peak)**,
  10.1, 9.4, **14.4 (FY2025)**. Computed from each year's filed gross profit and net sales.
  **Trend: none - a saw-tooth between 6% and 24% with no drift.** That is a spread business, and
  a spread is what a franchise does not have to live on.
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: units shrinking, share
  purchased, spread set by the steel cycle and by the DOC.**

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

**⛔ THE FILE CLOSES HERE.** Q2 is OUT on the business: **[E3-03]** criterion 2 fails on the
subject's own Item 1, the business sits squarely in **[E2-58]**'s commodity class without its
*wide and sustainable* exception, and what floor exists belongs to the trade regime under
**[E2-59]**, not to the company. Per operator rule 2, **no verdict box is ticked below this
line**, and any arithmetic that follows is headed **COMPUTATION - NOT A CLEARANCE**.

*Notes for Q3 and Q4 are recorded beneath the close because the work was done before the verdict
was written and because it bears on the reversal condition at the end of the file. They carry no
verdicts.*

## Q3 - ARE THEY HONEST, AND ARE THEY RATIONAL?
### ⛔ NOTES BENEATH THE CLOSE. NO VERDICT IS TICKED. The file closed at Q2.
*Recorded because the work was done before the Q2 verdict was written, because operator rule 2
permits notes below a close, and because these facts bear on the reversal condition at the end.*

**THE WEIGHT CASE, declared** *(a note, not a gate, since the file is closed)*:
- [x] **Daily execution [E3-38]** - **ticked.** The product is undifferentiated by the filing's
  own account and the year's result is made by rod-buying timing, inventory positioning and the
  willingness to push price. FY2022 is the proof: **inventories absorbed $118.6 million of cash**
  and FY2023 released **$97.6 million** of it, a $216 million swing on management's positioning
  in a company with a $574M market value. That is have-to-be-smart-every-day.
- [ ] Control [E1-16] - no, a marketable minority stake.
- [ ] Leverage [E3-29] - no. **Total debt $0** at FY2025 and at 2026-06-27; the FY2025 MD&A's own
  table reads *"Total debt - "* and *"Shareholders' equity … 100 %"* of total capital.
- **Had the file remained open, one box ticked makes Q3 a binary gate and no price compensates.**

**Honesty - no disqualifier found in the documents read.** *Written as [E5-17] requires:*
**a Q3 pass is the absence of found disqualifiers, not a finding that the managers are honest.**
Legal proceedings are boilerplate ordinary-course; auditor Grant Thornton LLP, *"has served as
our auditor since its appointment in 2002"* (DEF 14A 2026), so no auditor churn. No restatement
appears in the filings read.

**THE FLAGS [E4-22, E5-15, E4-29, E4-30] - each checked, most clean, and the clean reads matter
because they were taken in the place the CGNX run proved they must be taken.**

- [ ] **weak accounting** - one item to record rather than to score: the FY2025 10-K states
  *"We have reviewed our accounting estimates, and none were deemed to be considered critical
  for the accounting periods presented."* A filer declaring **no** critical accounting estimate
  is an absence claim inside a filing. On this business it is plausible - no reserves, no
  percentage-of-completion, no pension asset-return assumption driving income - but it is
  recorded as an oddity, not waved through.
- [ ] unintelligible footnotes - no. Twenty notes, plain English, tables that foot.
- [ ] **trumpeted earnings projections / growth targets - DOES NOT FIRE, and it was checked in
  the 8-K EX-99.1 releases, not only in the annual report.** Four quarterly releases read
  (2025-10-16, 2026-01-15, 2026-04-16, 2026-07-16). **No numeric earnings, EPS, margin or
  growth guidance appears in any of them.** The only forward number of any kind is capital
  spending, and the one revision to it is explained as timing: *"The revised outlook reflects
  the timing of certain projects rather than any change in our planned investment activities,
  with a portion of the related expenditures now expected to be incurred in fiscal 2027."*
  The outlook language is adjectival - *"cautiously optimistic"*, *"Favorable outlook for the
  remainder of fiscal 2026"* - which **[E5-30]** does not reach; the ratchet it warns about is
  forecasting earnings, and no earnings are forecast.
- [ ] **serial share issuance [E5-15]** - does not fire. Shares issued and outstanding ran
  **17,609k (FY2011) → 19,420k (FY2025)**, about **+0.7% a year**, all of it option and RSU
  settlement; the cash raised from option exercises across the whole 17-year series never
  exceeded $5.1 million in a year and was **$62 thousand** in FY2025. Nothing here resembles
  *"one of the surest indicators of a promotion-minded management."*
- [ ] **EBITDA / adjusted-earnings promotion [E4-29] - CLEAN, and this is a real finding rather
  than an absence of looking.** The string *"EBITDA"* appears **zero times** in the FY2025 10-K,
  **zero times** in the Q3 FY2026 10-Q, **zero times** in the 2026 proxy, and **zero times in
  any of the six 8-K exhibits read**, as do *"non-GAAP"* and *"adjusted earnings"*. The company's
  public narrative is built on GAAP net earnings, GAAP diluted EPS and return on capital. Under
  **[E5-41]** - depreciation as *"reverse float"*, the expense already paid being exactly the one
  EBITDA deletes - a capital-intensive filer that never reaches for it is making the honest
  choice at the point where the temptation is largest.
- [ ] **filed-figure tells [E4-30]** - neither fires. *Unnaturally smooth growth*: the opposite;
  net earnings ran −22.1, 0.5, −0.4, 1.8, 11.7, 16.6, 21.7, 37.2, 22.6, 36.3, 5.6, 19.0, 66.6,
  125.0, 32.4, 19.3, 41.0 ($M, FY2009–FY2025). *Cash taxes as a share of reported pretax income*:
  45.0%, n/m, 6.5%, 14.8%, 31.3%, 23.7%, 34.1%, 27.2%, 18.2%, 23.4%, 7.9%, 19.5%, 25.7%, 18.8%,
  13.2%, 20.0% - noisy with the cycle and with no downward drift, and **the two best years paid
  19.5% and 25.7%**, which is the wrong direction for the tell.
- **[E2-49] metric-switching - MY OWN PRIOR WAS TESTED AND DID NOT FIRE. The count is
  UNCHANGED at six fires and six failures; IIIN is not a seventh fire.** *"Yardsticks seldom are
  discarded while yielding favorable readings. But when results deteriorate, most managers favor
  disposition of the yardstick rather than disposition of the manager"* - demand *"pre-set,
  long-lived and small bullseyes"* **[E2-49]**. Insteel's annual incentive has been **return on
  capital, and only return on capital, for at least fifteen consecutive years**, and the 2026
  proxy prints the whole series including the years it paid nothing: *"we do not apply subjective
  factors to adjust compensation during periods where our failure to meet our return on capital
  targets may be due to factors outside the control of our executive officers"*, with payouts of
  **0.0% in 2011, 0.0% in 2012, 0.0% in 2019 and 29.0% in 2024**. **Publishing your own worst
  readings in a table is the [E2-67] positive pole** - Berkshire published its reserving errors so that readers could
  *"judge whether we may have some systemic bias that should make you wary of our current and
  future figures"* - transposed to a compensation
  disclosure. The CEO's own non-equity incentive fell from **$1,500,000 (FY2025, 200% of target)
  to $204,673 (FY2024, 29% of target)** and back; the pay moved with the number.

**THE PRIMARY TEST [E2-01] - a number, multi-year, balance sheet before income statement.**
Net income ÷ year-end shareholders' equity, FY2010–FY2025, **unlevered because there is no
leverage**: 0.3, −0.3, 1.2, 7.3, 9.3, 10.8, 16.6, 10.1, 15.0, 2.3, 7.2, 22.1, 32.1, 8.5, 5.5,
11.0 - **sixteen-year mean 9.9%**. The company's own ROCICP series (NOPAT ÷ invested capital)
means **14.2% over fifteen years and 9.9% over the thirteen years excluding the 2021-22 spike**.
**[E2-42]**'s red light - *"Red lights should start flashing if the five-year average annual gain
falls much below the return on equity earned over the period by American industry in
aggregate"* - is the test this series should be read against, and it is recorded here without a
verdict because the file is closed.

**The half-owner test [E2-26] - this reporting mostly passes, and the sharpest instance is an
admission against interest.** On the acquisition the 10-K says: *"Following the EWP Acquisition,
net sales of the former EWP facilities in 2025 were approximately $ 59.3 million. The actual net
sales specifically attributable to the EWP Acquisition, however, cannot be quantified due to our
integration efforts … we have determined that the presentation of EWP's earnings is impracticable
for 2025."* It then **publishes the pro forma anyway**, and the pro forma is unflattering:
FY2024 combined **net earnings $17,510 thousand against the $19,305 thousand actually reported**
- **the acquired business, at FY2024 industry conditions, would have REDUCED earnings by $1.8
million on $93.3 million of additional sales.** Restructuring is quantified by category
(separation $251k, relocation $340k, closure $492k, impairment $895k) rather than buried, which
is what **[E5-33]** asks for and **[E3-53]** warns about.

**THE INSTITUTIONAL IMPERATIVE [E2-30] - one of four observable, and it is not a fraud test.**
- [ ] resists any change in current direction - no; it has closed plants and redeployed equipment.
- [x] **projects or acquisitions materialise to soak up available funds** - the shape is present.
  Cash peaked at **$125.7M (FY2022) → $111.5M (FY2024) → $38.6M (FY2025)** and was spent on
  **$72.1M of acquisitions plus a $48.6M special dividend the year before and a $19.4M special
  dividend the year after.** Recorded as [E2-30]'s *"Institutional dynamics, not venality or
  stupidity"*, not as an accusation - a cash pile in a cyclical with no debt is exactly the
  condition the passage describes.
- [ ] staff studies to justify the leader's craving - nothing in the filings.
- [ ] peer behaviour mindlessly imitated - nothing in the filings; the consolidation is
  idiosyncratic rather than industry-wide in the documents read.

**CAPITAL ALLOCATION - recorded, with the humility clause [E4-13] attached.**
- **Buyback condition (1), ample funds [E5-08]:** met - no debt, $98.7M of the $100M revolver
  available at FY2025 year end.
- **Buyback condition (2), a material discount to conservatively calculated IV:** **not
  evidenced either way.** Repurchases are token and continuous - $2.3M (FY2023), $1.8M (FY2024),
  $2.3M (FY2025) against dividends of $41.3M, $50.9M and $21.8M - and no filing states a
  value test. **[E2-51]**'s *"A manager who consistently turns his back on repurchases … reveals
  more than he knows of his motivations"* does not cleanly apply, because the cash is returned,
  just through dividends. **[E5-31]**'s ordering test - business needs first, then acquisitions
  versus repurchases **by per-share value added at the price** - is the one the record cannot
  answer from the filings, and that is a limit, not a finding. **The humility clause [E4-13]:**
  *"it is natural for CEOs to be optimistic about their own businesses. They also know a whole
  lot more about them than I do."*
- **The retention test [E3-54] - BOTH WINDOWS PUBLISHED, because [E4-38] forbids choosing one.**
  *"growth-rate presentations can be significantly distorted by a calculated selection of either
  initial or terminal dates"* **[E4-38]**.

  | window | retained (NI − dividends) | market value, start → end | $ of market value per $1 retained |
  |---|---|---|---|
  | **FY2021–FY2025**, to the FY2025 year-end close | $98.0M | $366.7M → $747.5M | **$3.89 - passes** |
  | **FY2021–FY2025**, to 2026-09-18 | $98.0M | $366.7M → $574.2M | **$2.12 - passes** |
  | **FY2017–FY2025 (nine years)**, to the FY2025 close | $129.4M | $687.7M → $747.5M | **$0.46 - fails** |
  | **FY2017–FY2025 (nine years)**, to 2026-09-18 | $129.4M | $687.7M → $574.2M | **−$0.88 - fails** |

  **The corpus's own test is five-year rolling, and on that window it passes.** The five-year
  window begins at the **October 2020 trough** and the nine-year window begins at a **2016
  peak**, which is precisely the artifact [E4-38] names. The honest statement is that **the
  retention test on this name measures the steel cycle more than it measures the allocator**,
  and both numbers are printed so that nobody has to take my word for which window I preferred.
- **Tenure, and what it implies [E3-58]:** *"Mr. Woltz has served as our Chief Executive Officer
  since 1991 and as Chairman of the Board since 2009"* (DEF 14A 2026). **Thirty-five years.**
  [E3-58]'s arithmetic - a CEO of long tenure has allocated an enormous share of all the capital
  the business has ever had - applies at close to its maximum here. Against it: allocation is
  visibly **not** outsourced; there is no serial banker-led M&A programme (two deals in
  seventeen years of filings) and no consultant-driven capital programme in the documents read.
- **The one allocation fact that deserves to be written plainly, without an accusation
  attached.** The $67.0M EWP purchase bought two production facilities, **Upper Sandusky, Ohio
  and Warren, Ohio.** Warren was closed in **November 2024, within weeks of closing the deal**
  (*"Production at the Warren facility ceased in November 2024"*, $2.3M of FY2025 restructuring,
  the building sold at a $0.5M impairment). Upper Sandusky's closure was announced on
  **2026-08-21**, twenty-two months after purchase, with *"restructuring charges of approximately
  $4.6 million"* and *"the elimination of up to 65 positions"*. **Both acquired plants closed
  within two years.** The stated logic is coherent and is in the release - the remaining WWR
  plants *"have ample open capacity to accommodate additional volumes"* and *"We do not expect
  this action to affect the Company's revenue"* - which is buying volume and killing the
  capacity, a rational consolidation move. **It is also, in the same sentence, the company's own
  testimony that its industry has ample open capacity**, which is [E2-58]'s *"persistent
  over-capacity"* stated by the subject.
- **[E5-33] applies to the charges:** *"to tell owners year after year, 'Don't count this' … is
  misleading."* The FY2025 $2.3M and the FY2026 $4.6M are real costs of owning this business and
  are inside the owner-earnings series below by construction, not annualized away.

**THE GUARDRAIL - checked.**
- [x] Confirmed: nothing in this Q3 is used to promote the name. It could not be: **the file
  closed at Q2, and [E2-37]/[E2-38]/[E3-39] say a good jockey does not repair the horse.** *"a
  textile company that allocates capital brilliantly within its industry is a remarkable textile
  company - but not a remarkable business"* **[E2-37]**. That sentence is the whole of this Q3.
- [x] Key-person dependence is recorded at **Q2 as a moat question, not here as a strength**
  **[E4-23]** - and the Q2 finding was that this business does not need a superstar, it needs a
  steel cycle.

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE - NO VERDICT. THE FILE CLOSED AT
  Q2 AND TICKING A BOX HERE WOULD BREACH OPERATOR RULE 2.**

## Q4 - WILL IT SURVIVE?
### ⛔ NOTES BENEATH THE CLOSE. NO VERDICT IS TICKED.

# COMPUTATION - NOT A CLEARANCE

*Everything from here to the end of the file is arithmetic produced after a closed gate. It
carries no entry language and no verdict, per operator rule 3.*

### The owner-earnings rebuild, over EVERY filed year - what the five-year window hides

**Construction (the confessed CONVENTION, section VI):** owner earnings = operating cash flow
− stock-based compensation − the (c) guess, with the working-capital increment already netted
inside operating cash flow as **[E2-23]** constraint 3 requires. Two ends for (c): **D&A**, which
is the corpus default **[E3-44, E2-41]**, and **total capital expenditure**. No net-income proxy
is used anywhere (operator rule 5; PRIME RULE 3's clause of 2026-09-20).

| FY | OCF | SBC | D&A | capex | **OE (c)=D&A** | **OE (c)=capex** |
|---|---|---|---|---|---|---|
| 2010 | 12.88 | 2.26 | 7.00 | 1.49 | **3.62** | **9.13** |
| 2011 | −2.91 | 2.92 | 9.57 | 7.94 | **−15.40** | **−13.76** |
| 2012 | 13.14 | 2.21 | 9.76 | 8.07 | **1.17** | **2.87** |
| 2013 | 36.83 | 2.16 | 9.83 | 5.03 | **24.83** | **29.64** |
| 2014 | 29.23 | 2.66 | 10.27 | 8.96 | **16.30** | **17.62** |
| 2015 | 35.77 | 2.30 | 11.93 | 7.15 | **21.54** | **26.32** |
| 2016 | 56.25 | 2.44 | 11.54 | 12.98 | **42.27** | **40.84** |
| 2017 | 20.84 | 2.25 | 11.65 | 20.57 | **6.95** | **−1.98** |
| 2018 | 53.97 | 2.08 | 12.82 | 18.45 | **39.07** | **33.44** |
| 2019 | 6.61 | 2.06 | 13.55 | 10.51 | **−9.00** | **−5.96** |
| 2020 | 56.22 | 2.03 | 14.26 | 7.11 | **39.94** | **47.08** |
| 2021 | 69.88 | 1.99 | 14.52 | 17.50 | **53.37** | **50.39** |
| 2022 | 5.67 | 2.43 | 14.49 | 15.90 | **−11.25** | **−12.66** |
| 2023 | 142.20 | 2.42 | 13.30 | 30.70 | **126.47** | **109.07** |
| 2024 | 58.21 | 3.07 | 15.41 | 19.15 | **39.72** | **35.99** |
| 2025 | 27.16 | 3.49 | 18.39 | 8.21 | **5.28** | **15.46** |

*(FY2009 is excluded from the means: its D&A does not resolve undimensioned in companyfacts, so
only one end could be computed. Stated rather than filled in.)*

**THE WINDOWS, ALL OF THEM PUBLISHED [E4-25, E4-38]:**

| window | OE, (c)=D&A | OE, (c)=capex |
|---|---|---|
| **3 years, FY2023–25** | **$57.2M** | **$53.5M** |
| **5 years, FY2021–25** *(the corpus default [E2-42])* | **$42.7M** | **$39.7M** |
| **9 years, FY2017–25** | **$32.3M** | **$30.1M** |
| **16 years, FY2010–25 - every filed year the data supports** | **$24.1M** | **$24.0M** |
| **TTM to 2026-06-27** *(FY2025 less 9M FY2025 plus 9M FY2026)* | **−$20.5M** | **−$13.3M** |

- **Short-window mean** (window: 5 years, FY2021–25): **$39.7M–$42.7M**
- **Long-window mean** (window: 16 years, FY2010–25): **$24.0M–$24.1M**
- **Spread, conservative end:** the long window is **44% below** the five-year window, and the
  three-year window is **2.4×** the sixteen-year one.
- **Combined range** (window spread × capex band): **−$20.5M to $57.2M.**
- **Is that range too wide to reach a conclusion? YES, and [E4-25] says that IS the conclusion.**
  *"Usually, the range must be so wide that no useful conclusion can be reached."* A band running
  from **negative twenty** to **plus fifty-seven** on a $574M market value cannot rank anything.
  **This is a second, independent ground on which the file does not proceed** - and it was
  reached from the filings, not from the screen.
- **The distorted year, named [E5-11, E4-41]: FY2023, and it is not a small distortion.**
  **FY2023 alone is 59.2% of the five-year window's total owner earnings at the D&A end.** And
  **FY2023's cash was not earnings**: the filed cash-flow statement shows working capital
  *providing* **$97.6M** of the year's $142.2M of operating cash - **68.6%** - of which
  **$94.3M was the inventory line alone**, unwinding the $118.6M build of FY2022 as steel prices
  fell. Strip the working-capital swing and FY2023's owner earnings are **about $29M, not
  $126M**. **[E4-41]** is the corpus's own instance of doing exactly this, and it is
  quoted from the ledger row rather than from the framework's gloss of it: *"We've yet to see a
  pro-forma presentation disclosing that audited earnings were somewhat high. So let's make a
  little history: Last year, on a pro-forma basis, Berkshire had lower earnings than those we
  actually reported. That is true because two favorable factors aided our reported figures."*
  The favourable factor here is the 2021-22 steel spike and its unwind. The break here is the
  2021-22 steel spike and its unwind, and it is the whole of the short window's advantage.
- **The step-up the screen reported is real and it is a wave, not a level.** On the nine-year
  operating-cash series the recent three years mean **$75.9M** against the earlier six's
  **$35.5M**, a ratio of **2.13** - which reproduces the screen's figure exactly. The sixteen-year
  owner-earnings series says what that ratio is made of: **[E3-51]**'s surfer.

### Maintenance capex - a DISCLOSED JUDGMENT, and the corpus default holds here

**(c) "must be a guess"** **[E2-09]**. **The guess, stated:** **~$15–18M a year**, i.e. at the
**D&A end**, and here is the reasoning rather than a computation.
- **[E3-44]**'s default - *"by and large, the depreciation charge is not inappropriate in most
  companies to use as a proxy for required capital expenditures"* - and **[E2-41]**'s *"At 95% of
  American businesses, capital expenditures that over time roughly approximate depreciation are a
  necessity."* **Insteel is visibly inside the 95%: over FY2010–FY2025 D&A averaged $12.39M and
  capital expenditure averaged $12.48M, a ratio of 1.01.** Sixteen years of the two lines
  matching to one per cent is as clean a case for the default as the corpus's own wording asks
  for, and it is why the two owner-earnings ends converge on the long window ($24.1M vs $24.0M)
  and diverge only on short ones.
- **[E5-20]**'s exception class - railroads, airlines, anything whose own filing says depreciation
  understates renewal - **is argued by the filing but refuted by the series.** The 10-K's risk
  factors do say *"Our operations are capital intensive and require substantial recurring
  expenditures for the routine maintenance of our equipment and facilities"*, and FY2026 capital
  spending is guided *"up to approximately $20.0 million"* against FY2025 D&A of $18.4M. But the
  same MD&A says the spending is **not** all renewal - *"Capital expenditures for both years
  focused on cost and productivity improvement initiatives in addition to recurring maintenance
  requirements"* - and, decisively, *"Our investing activities are largely discretionary,
  providing us with the ability to significantly curtail outlays should future business
  conditions warrant"*, which is the opposite of a railroad's position. **So the D&A end is valid
  here, and it is the conservative end in the recent years** (FY2025: D&A $18.4M against capex
  $8.2M).
- **[E4-47]**, the inflation conditioner, is noted and not spent twice: replacement cost of
  wire-drawing and welding equipment in current dollars runs ahead of depreciation charged on
  older dollars, which argues the true (c) sits at the **upper** end of $15–18M rather than the
  lower. That judgment is applied once, inside the guess, and not again as a margin.
- **Stock compensation subtracted in full [E5-06]:** yes, every year, at the cash-flow add-back.
  **[E3-70]**'s stricter market-value measure is not reached for: SBC is **$3.49M on $27.2M of
  operating cash** in FY2025 and averages **$2.4M a year**, and the resume-state threshold for
  hand-reading the grant table is SBC/OCF above 50%. Recorded, not skipped.

### THE SCREEN ROW, TESTED LINE BY LINE - what survived and what did not

| screen field | value | verdict after the hand rebuild |
|---|---|---|
| `cap_m` | **588** | **2.4% HIGH.** Hand cap **$574.2M** on 19,358,247 cover shares × $29.66. Stale price, not a share-count defect. |
| `oe_bottom_m` / `oe_top_m` | **40 / 57** | **REPRODUCED EXACTLY** - 3y and 5y means × two capex ends give **$39.7M, $42.7M, $53.5M, $57.2M**. The arithmetic is right. |
| `wc_note` | *"ONE LINE MADE THE CASH: AccountsPayableAndAccruedLiabilities moved 71% of 2025 OCF"* | **ARITHMETIC RIGHT, DIRECTION INVERTED - the BELFB failure repeated.** $19,260 ÷ $27,163 = **70.9%**, correct. But the line was a **source** inside a working-capital block that was a **net drain of $35.7M, −131% of operating cash.** The MD&A says so in words: *"**Working capital used $37.6 million of cash** due to a $36.5 million increase in inventories and a $20.4 million increase in accounts receivable **partially offset by** a $19.3 million increase in accounts payable and accrued expenses."* **The payable did not make the cash; it softened the loss of it.** |
| `level_shift` / `level_note` | **2.13**, *"STEP UP - normalize down [E4-41]"* | **REPRODUCED AND CORRECT AS ARITHMETIC** (recent 3 = $75.9M, earlier 6 = $35.5M on the 9-year OCF series) - **and the instruction was right**: it is a wave, and the mean does need normalizing down. |
| `best_year_dep` | **0.238** | **REPRODUCED** on the 9-year OCF series. **But it understates the problem by more than half**: on the series the framework actually values, **FY2023 is 59.2% of the five-year owner-earnings window**, not 23.8%. |
| `level_shift_oe` / `level_note_oe` | refused, *"EARLY HALF STRADDLES ZERO … $-12.7M"* | **REPRODUCED EXACTLY** - the 9-year capex-end series runs −$1.98M, $33.44M, −$5.96M, $47.08M, $50.39M, **−$12.66M**, so the refusal is correct and the **$-12.7M is FY2022**. |
| `flags_disagree` | *"one series refuses the ratio and the other does not"* | **EXPLAINED.** The **operating-cash** series' early half has one small negative and a positive mean, so the guard passes it and it prints 2.13; the **owner-earnings** series' early half straddles zero properly, so the guard refuses. **The refusing series is the right one** - a ratio across a sign change is not a ratio, and operating cash simply hides the sign changes that netting capex reveals. |
| `window_disagree` | *"the 9yr base may already contain the wave"* | **CONFIRMED, and worse than stated.** Not only does the 9-year base contain the wave; **the 5-year base is 59% made of one year of inventory liquidation.** |
| `spread_caveat` | *"4-construction width only … CANNOT see variation older than the 5-year window; rebuild it"* | **THE INSTRUCTION WAS RIGHT AND THE REBUILD CHANGED THE ANSWER.** Sixteen filed years give **$24.0–24.1M**, against the published **$40–57M**. **The long-window mean is 41% of the published band's midpoint.** |
| `acq_note` | *"acquisitions are $72M, 12% of cap, inside the window"* | **CONFIRMED, at 12.6% of the hand cap**, and the perimeter is worse than the note implies - see below. |
| `growth_required` 0.0326, `yield_bottom` 0.0674, `vs_sovereign` 0.0139 | | **All three are computed on a band the rebuild refutes and on a cap 2.4% high.** No Q5 number is reported; the file closed at Q2. |
| `newest_filing` 2025-09-27 / `newest_periodic` 2026-06-27 | | **BOTH CORRECT.** FY2026 closes 2026-10-03 and no 10-K for it exists. |

### THE AGGREGATE WORKING-CAPITAL CHECK - computed by hand, as the ADM defect requires

**The standing check after ADM:** `working_capital_flag()` tests **single** lines against a 30%
threshold, so it missed a **50.7% aggregate** at ADM. Insteel is the mirror image - the note fires
on a **combined** tag - so the net block was computed by hand for every year, as
**cash = −ΔAR − ΔInventories + ΔAP&accrued − ΔOther**, reconciled to the filed statement in FY2025
and FY2023.

| FY | net WC cash | as % of OCF | the line that did it |
|---|---|---|---|
| 2021 | **−$13.2M** | −18.9% | inventories building as prices rose |
| **2022** | **−$135.8M** | **−2,395%** of $5.7M of operating cash | **inventories absorbed $118.6M** |
| **2023** | **+$97.6M** | **+68.6%** | **inventories released $94.3M** |
| 2024 | +$17.6M | +30.2% | inventories $14.5M |
| **2025** | **−$35.7M** | **−131.5%** | inventories −$36.5M and receivables −$20.4M, **AP +$19.3M an offset** |
| 9M FY2026 | **−$18.6M** | −103% of $18.0M | inventories −$29.1M, **AP +$13.7M an offset** |

**Three things follow, and none of them is in the screen row.**
1. **Insteel's operating cash IS a working-capital series**, in both directions, and in FY2022 and
   FY2023 the working-capital line was larger than the operating cash itself.
2. **The flagged line is an offset in both of the two most recent periods.**
3. **The unflagged line is the one that matters.** In FY2023 the inventory release was **66.3% of
   operating cash**, over the flag's 30% threshold, in the flag's own five-year window - and
   **the flag never saw it.**

### TOOLING DEFECTS FOUND - reported, not patched *(a tool may remove friction, never add a step)*

1. **`WC_TAGS` contains no inventory tag and no receivables tag.** The list is
   `IncreaseDecreaseInAccountsPayableAndAccruedLiabilities`, `IncreaseDecreaseInAccountsPayable`,
   `IncreaseDecreaseInContractWithCustomerLiability`, `IncreaseDecreaseInDeferredRevenue` - all
   four are **liability** lines. **A working-capital flag that cannot see inventories is blind to
   every inventory-cycle business there is**, which is most of industrials, distribution and
   retail. Insteel tags `IncreaseDecreaseInInventories` and `IncreaseDecreaseInAccountsReceivable`
   in every year, so the data was present and the test did not ask for it. **This is the same
   defect class the queue keeps finding: a guard that reads one side of the series while the
   defect lives on the other.**
2. **The flag reports only the single largest line and stops.** FY2025's payable at 70.9% beat
   FY2023's inventory release at 66.3%, so only the payable was printed - **and the payable was
   an offset while the inventory release carried the whole published band.** Reporting the maximum
   is not the same as reporting the material one; the honest output is every line over the
   threshold, in every year of the window, with its sign.
3. **The direction defect is now confirmed twice.** BELFB found it and IIIN reproduces it: the
   note's sentence *"ONE LINE MADE THE CASH"* asserts a direction the function never tests. It
   computes `abs(v)/abs(o)` and then prints a directional claim. **Two runs, two inversions -
   this is no longer a one-off.**
4. **A note, not a defect, about the band:** `oe_bottom`/`oe_top` are constructed from 3- and
   5-year windows only, and on this name the sixteen-year mean sits **$16M below the published
   bottom**. The `spread_caveat` says this in words and the CSV's own columns then carry the
   narrow band as if it were the answer.

### The acquisition perimeter [the standing check]

- **$72.1M of cash out in FY2025** - EWP $67.0M (2024-10-21) and OWP $5.1M (2024-11-26) - against
  a hand cap of $574.2M: **12.6%.**
- **The acquired operations' cash is inside the operating-cash series from 2024-10-21 onward and
  the purchase price is nowhere inside maintenance capex.** Eleven and a half months of acquired
  operating cash sit in FY2025's $27.2M; the $72.1M sits in investing. **Any owner-earnings
  series that spans the deal is comparing two different companies**, which is why the sixteen-year
  mean is the honest one and the three-year mean is not.
- **The tested source limit applies and was not re-attempted** (resume state, section 5):
  **stock consideration does not resolve undimensioned in companyfacts.** It does not bite here -
  **both deals were all cash** (*"The EWP Acquisition was funded with cash on hand"*), read from
  the filing rather than inferred from a tag.
- **What the filing will not tell anyone**: *"the presentation of EWP's earnings is impracticable
  for 2025."* The **pro forma is the only quantification that exists**, and it says the
  acquisition would have **cut FY2024 net earnings by $1.8M**. $25.9M of the $67.0M became
  **goodwill**; FY2025 goodwill rose $9.7M → $37.8M and intangibles $5.3M → $16.6M.

### Great, good, or gruesome? **[E4-20]**

- [ ] great · [ ] good · [x] **gruesome, on the sixteen-year record, and the test is [E4-43]'s
  boundary rather than a slur.** *"The worst sort of business is one that grows rapidly, requires
  significant capital to engender the growth, and then earns little or no money."* Insteel does
  not grow rapidly, which is the one respect in which it is not the airline. But **[E4-43]** says
  the *good* class passes on the strength of *"nothing shabby about earning $82 million pre-tax on
  $400 million of net tangible assets"* - roughly **20% pre-tax on tangible capital** - and
  Insteel's sixteen-year unlevered ROE is **9.9%** while the working capital that funds the volume
  has to be **re-lent to the cycle at every upturn**: $118.6M of it in FY2022 alone, on a business
  whose equity was then $390M. **The savings-account image decides it**: the deposits added in
  FY2022 earned nothing, and the account only looked good in FY2023 when the deposit was
  withdrawn. **[E5-40]**'s ~12% *"quite satisfactory"* return-on-retention benchmark is not
  reached on the long window either.

### Staying power - score all three **[E5-11]**

1. **A large and reliable stream of earnings - LARGE, NOT RELIABLE.** Net earnings over seventeen
   filed years: −$22.1M to +$125.0M. **[E5-29]** is honoured - volatility is not risk - but
   [E5-11] asks for *reliable*, and the FY2019 and FY2022 owner-earnings years are negative.
2. **Massive liquid assets - YES, AND RECENTLY HALVED AND HALVED AGAIN.** Cash $125.7M (FY2022)
   → $111.5M (FY2024) → **$38.6M (FY2025)** → **$14.9M at 2026-06-27**, plus an undrawn $100M
   revolver ($98.7M available at FY2025 year end, $1.3M of letters of credit). **No debt at any
   date read.**
3. **No significant near-term cash requirements - THE ONE THAT USUALLY KILLS, AND IT IS THE ONE
   TO WATCH HERE.** The FY2025 commitments note: *"we had $ 92.3 million in non-cancelable
   purchase commitments for raw material extending as long as approximately 60 days"*, against
   **$38.6M of cash**. The gap is covered by the revolver and by the receivables those purchases
   turn into - but **[E5-39]**'s standard is *"We will never be dependent on the kindness of
   strangers"*, and a borrowing base *"calculated based upon a percentage of eligible receivables
   and inventories"* is exactly the facility that shrinks when the cycle turns, because the
   collateral shrinks with it. **That is the structural weakness in an otherwise conservative
   balance sheet, and it is not visible in the debt-to-capital ratio of zero.**
- **Leverage, named and quantified [E4-16, E3-29]:** **none.** Total debt $0; other liabilities
  $25.1M (operating leases and the supplemental retirement plan). **[E3-52]**'s reading - covenant
  terms matter more than quantity - finds nothing covenanted and nothing due. **On leverage this
  is among the cleanest balance sheets the queue has read.**

### Name the specific way THIS business dies **[E2-27, E3-24]**

**The mechanism: the spread inverts and the inventory is on the wrong side of it.** Insteel buys
rod on monthly pricing (*"most recently monthly for domestic suppliers"*) and sells into a market
where *"we may be unable to fully recover increased rod costs during weaker market environments"*
and where, when rod falls, *"our financial results would be negatively impacted if the selling
prices for our products decrease to an even greater extent **and if we are consuming higher cost
material from inventory**."* The kill is the second clause: a cost shock that cannot be passed
on, landing on an inventory bought at the old price.

**Quantified from filed figures - and the company quantifies it itself.** Q3 FY2026 10-Q, Item 3:

> *"Based on our shipments and average wire rod cost reflected in cost of sales for the first nine
> months of 2026, **a 10% increase in the price of wire rod would have resulted in a $33.1 million
> decrease in our pre-tax earnings** (assuming there was not a corresponding change in our selling
> prices)."*

**Nine-month pre-tax earnings were $28,104 thousand.** So **a 10% rod move with no price response
erases 118% of the year's pre-tax earnings** - more than all of it. The second, slower form is the
inventory whipsaw already on the record: **$118.6M absorbed in FY2022 and $94.3M released in
FY2023**, a swing of 38% of the current market value inside two years, on a decision about when to
buy steel.

**The exposure, not the experience [E4-40].** *"all of us in the industry made a fundamental
underwriting mistake by focusing on experience, rather than exposure."* The experience is
reassuring - seventeen years, no debt, never a loss year after 2009. **The exposure is $33.1M of
pre-tax earnings per 10% of rod price, a 50% Section 232 tariff on the steel content of its own
product (*"recently increased to 50% from 25%"*), 27% of rod purchased abroad, and a trade regime
in its finished markets that has to be re-petitioned each decade.**

**Likelihood: [x] a real possibility** for a year of negative owner earnings - it has happened in
**FY2011, FY2019 and FY2022** within the sixteen years read, which is roughly one year in five.
**[ ] likely** is not claimed for permanent impairment: with no debt and a discretionary capex
budget, the mechanism above produces **bad years, not death**. **The honest statement is that this
business is very hard to kill and quite easy to make worthless as a compounder** - which is Q2's
finding arriving at Q4 by another road.

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE - NO VERDICT. THE FILE CLOSED AT
  Q2.** *Note for the record: had it reached here, **[E4-25]**'s too-wide-a-range rule would have
  closed it independently - the combined range runs from −$20.5M to $57.2M.*

---
## Q5 - WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### ⛔ Q5 DOES NOT OPEN. Q2 is OUT. **No yield, no value range, no ranking, no floor verdict.**

**One line is recorded and it is a statement about the screen, not about the price.** The screen
ranked this name on a yield of **6.74%** computed from a band of **$40M–$57M** over a cap of
**588**. On the hand-struck cap of **$574.2M** and the **sixteen-year** owner-earnings mean of
**$24.0–24.1M**, the same arithmetic gives **4.2%**, against a sovereign of **5.34%** - *below the
bond, before any judgment about the business is made at all.* **This is COMPUTATION, NOT A
CLEARANCE**, it is reported only to record what the rebuild did to the screen's input, and
**[E4-28]**'s floor is not adjudicated because the question is not open.

- **VERDICT: NOT OPENED. Q2 closed the file.**

## Q6 - WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

### ⛔ No position, no entry, no exit metric. **NO PRICE ALERT - the QLYS ruling.**

**A name that failed on the BUSINESS gets no price band.** **[E5-35]**: *"You can turn any
investment into a bad deal by paying too much. **What you can't do is turn any investment into a
good deal by paying little.**"* Arming a price alert on IIIN would assert the opposite.

**THE REVERSAL CONDITION, IN WORDS, PRICE EXCLUDED.** This file reopens only if the **business**
changes, and the change would have to be visible in filings as one of these:

1. **A structural change in the industry's supply**, not a cyclical one - filed evidence that the
   named competitors' capacity has permanently left the market, such that the FY2025 statement
   *"our remaining welded wire reinforcement production facilities … have ample open capacity"*
   ceases to be true industry-wide. **[E2-58]**'s equation turns on over-capacity, and only its
   removal turns it back.
2. **Pricing conduct that survives a flat-demand year** - a fiscal year in which shipments are
   flat or down and **average selling prices rise**, reported in the MD&A in those terms. That is
   **[E2-44]**'s test, and FY2024 is the filed counter-example.
3. **A physical series that grows without being bought** - shipments up on an organic basis, with
   the MD&A separating organic from acquired tonnage, for three consecutive years. **[E4-55]**.
4. **Backward integration into wire rod**, which would be the only visible route to the *"wide and
   sustainable"* cost advantage **[E2-58]** names as its single exception - and would itself be a
   new business needing its own run.

**None of these is a price. [E4-17]**'s *"beliefs change quite gradually"* governs the formation
of this view, and nothing above would be read from one quarter.

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE - NO VERDICT. THE FILE CLOSED AT
  Q2.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **Q1 IN, Q2 OUT, and the file stops
      there.** Q3 to Q6 carry notes with **no verdict box ticked**, per operator rule 2.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the only
      IN in this file and it rests on Item 1 of a filing read in full.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives. **There is no
      UNRESEARCHED verdict in this file.** The one place the framework would ordinarily produce
      one - an incomplete competitor row - is discussed at Q2 and does not apply, because the
      verdict is OUT on the subject's own filing and six of the seven named competitors file
      nothing anywhere, so no artifact could be named.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known. **There is no
      UNKNOWABLE verdict in this file.**
- [x] Step 0: the filing was read, with accession number; **three figures were cross-checked
      by hand against the filed statements** (FY2025 operating cash $27,163k; equity recomputed
      from A - L to $371,532k; FY2025 net sales $647,706k against the MD&A's own 22.4%).
- [x] Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.
      **Five windows published (3y, 5y, 9y, 16y, TTM), both ends of (c) on every one.**
- [x] Competitor row filled, **and its incompleteness disclosed name by name**, with the reason
      the incompleteness does not rescue the class recorded in the open.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated. **5.34%, US
      Treasury 30-year par yield, 2026-09-18, struck fresh this run. FRED not used.**
- [x] Value stated as a round-number range, not a point estimate. **No value is stated at all:
      Q5 did not open.** The only Q5-adjacent arithmetic is headed COMPUTATION - NOT A CLEARANCE.
- [x] One bar chosen, not both; windage count stated. **Neither bar was used - no valuation was
      performed. Windage count: ZERO.** Conservatism was not spent, because no margin was taken.
      The one judgment made, (c) at the D&A end, is stated once and not re-applied as a margin.
- [x] Prices dated; aggregator used for live quotes only and flagged. **$29.66, close of
      2026-09-18, Yahoo Finance chart API, raw response saved to the research folder.**
- [x] Run committed to git, **in five commits: the claim, Step 0 + Q1, Q2, the notes beneath
      the close, and the fold.**

**Extra audit item this run added for itself, because the brief made it a standing check:**
- [x] **Every screen-row field tested against the filings and the result recorded, pass or
      fail.** Twelve fields, of which one (`cap_m`) is 2.4% high, one (`wc_note`) has the right
      arithmetic and the wrong direction, four reproduce exactly, and one (`spread_caveat`)
      issued an instruction that changed the answer when obeyed.
- [x] **No net-income proxy anywhere** (operator rule 5 and PRIME RULE 3's clause of
      2026-09-20). Owner earnings run off operating cash flow in every window.
- [x] **Every quotation checked against `principle_ledger.csv`'s own `quote_verbatim` field,
      not against the framework's rendering of it.** Six were corrected on that check, and two
      source artifacts are reproduced and flagged rather than smoothed.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line:** *The nation's largest maker of steel wire for concrete is a converter of a
  commodity it does not own, selling into a market its own 10-K calls "highly competitive based
  on price, quality and service" against six named rivals and imports, with whatever floor
  exists under its prices administered by the Department of Commerce rather than by the company
  - **[E3-03]** criterion 2 fails on the filing, **[E2-58]** supplies the class and **[E2-59]**
  supplies the regime, so Q2 is OUT and Q3 to Q6 are notes.*
- **If UNRESEARCHED - THE WORK ORDER:** not applicable; the verdict is OUT, not UNRESEARCHED.
- **If UNKNOWABLE:** not applicable.

---
## WHAT THIS RUN FOUND THAT THE SCREEN DID NOT

1. **The published owner-earnings band is 41% too generous once every filed year is read.**
   $40M-$57M from 3- and 5-year windows; **$24.0M-$24.1M across the sixteen years the filer has
   actually filed.**
2. **One year carries the band, and that year's cash was inventory, not earnings.** FY2023 is
   **59.2%** of the five-year window, and **68.6%** of FY2023's operating cash was a
   working-capital release, **$94.3M of it the inventory line alone**, unwinding FY2022's
   $118.6M build.
3. **The working-capital note's direction is inverted, for the second time in four cycles.**
   The MD&A says *"Working capital used $37.6 million of cash"*; the flagged payable was the
   offset.
4. **`WC_TAGS` cannot see inventories or receivables.** A working-capital flag built only from
   liability tags is blind to every inventory-cycle business, and on this name the line it could
   not see is the one that carries the valuation.
5. **The trailing twelve months of owner earnings are negative at both ends** (-$20.5M and
   -$13.3M to 2026-06-27), which no annual-only screen can see.
6. **`principle_ledger.csv` holds 311 rows, not the 267 that `CLAUDE.md` and every brief still
   state.** Counted from the file, as the standing instruction says to. The growth is traceable:
   267 at commit `9d38c16`, 286 at `b7e84ca`, **311 at `0eaeadd`**, both of the latter dated
   2026-09-20, with the key-files table never updated. **Reported, not edited: `CLAUDE.md` is
   the operator's document.**
7. **`Framework/THE FRAMEWORK v4.md` smooths a transcript artifact in [E4-46]**, printing
   *"the following five months"* where the ledger row reads *"the followings five months"*, and
   dropping a *"You know,"*. PRIME RULE 1 says flag artifacts and never smooth them, and PRIME
   RULE 2 says the corpus wins. **Reported, not edited.**
8. **A post-balance-sheet event that no annual screen carries:** on **2026-08-21** Insteel
   announced the closure of Upper Sandusky, Ohio, *"restructuring charges of approximately $4.6
   million"* and *"the elimination of up to 65 positions"* - **the second of the two plants the
   FY2025 acquisition bought, both now closed within twenty-two months.**
