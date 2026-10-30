# Company Run - Cal-Maine Foods, Inc. (CALM) - 2026-09-20
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
- rate **5.34%** · date **09/18/2026** · source **US Treasury daily par yield curve, 30-year
  constant maturity, from the issuing authority (home.treasury.gov).** Struck fresh this
  session: the cached copy `tools/_cache/sov_USD_treasury.csv` was deleted before the call and
  the file re-fetched. **No rate was inherited from the brief or from any other run.** FRED
  DGS30 was not used and was not needed. The 09/17/2026 row of the same file reads 5.29, so the
  series is live rather than stale.
- FX: **none arises.** Cal-Maine is a Delaware corporation reporting in USD, sells "throughout
  much of the U.S.", and the quote is in USD on Nasdaq. No foreign segment is reported. One
  sovereign, and it is the USD one.

**The filing was read** - not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: Form 10-K for the 52 weeks ended 2026-05-30 ("fiscal 2026"), filed 2026-07-22,
  accession `0001562762-26-000080`** (document `calm2026053010K.htm`).
- **Newest periodic: the same document.** Cal-Maine's fiscal year ends on the Saturday closest
  to May 31; the fourth quarter is not separately reported on Form 10-Q, and the first quarter
  of fiscal 2027 (ending 2026-08-29) was not filed as of this session. The most recent 10-Q is
  for the quarter ended 2026-02-28, accession `0001562762-26-000046`, filed 2026-04-01 - older
  than the 10-K. **So the screen's `newest_filing` and `newest_periodic` of 2026-05-30 are both
  correct and neither is stale.** That is a date, not a defect: the screen was cut 2026-09-02
  and nothing periodic has been filed since.
- Also read: the **10-Q for the quarter ended 2025-11-29, accession `0001562762-26-000004`**
  (for the share count at the float measurement date); the **8-K of 2026-09-02, accession
  `0001562762-26-000102`** (Items 1.01, 2.03, 9.01 - the `deal_note` filing); and the **8-K of
  2026-07-22, accession `0001562762-26-000078`** (Item 2.02, the fiscal 2026 earnings release).
- **Figures cross-checked against the filed statements, not the tagged data:**
  1. **Share count.** The 10-K cover reads *"As of July 22, 2026, `46,917,080` shares of the
     registrant's Common Stock, $0.01 par value, were outstanding."* The Consolidated Statements
     of Stockholders' Equity in the same document read, at May 30, 2026, **75,061** thousand
     shares issued and **28,080** thousand treasury shares: 75,061 - 28,080 = **46,981** thousand
     outstanding at the balance-sheet date. The cover count is 64 thousand lower because the
     company kept buying between 2026-05-30 and 2026-07-22. **The two agree.**
  2. **Operating cash flow and net income.** The filed Consolidated Statements of Cash Flows read
     *"Net cash provided by operating activities 479,753"* for fiscal 2026 (in thousands), and
     *"Net income $ 318,112"*; the tagged `NetCashProvidedByUsedInOperatingActivities` and
     `ProfitLoss` for the year ended 2026-05-30 read 479,753,000 and 318,112,000. **The tags are a
     transcription of the filed lines, which is why the filed lines were opened.**

**PRICE, SHARES AND CAP - RE-STRUCK BY HAND, as the screen's `cap_flag` orders.**
- **Price US$72.89**, close of **2026-09-18**, aggregator (Yahoo via `tools/sources.py`),
  **FLAGGED as an aggregator quote** and used for nothing but the cap, per operator rule 5.
- **Shares 46,917,080**, read off the **cover of the newest periodic filing**, which here is the
  10-K itself, accession **`0001562762-26-000080`**, as of 2026-07-22. `Screens/cover_shares.py`
  returns the same figure from the same accession.
- **No share classes to sum, and the charter question is closed by the filing.** Cal-Maine had
  two classes until last year. Note 11 - Equity: *"On April 14, 2025, all `4.8` million shares of
  Class A Common Stock were converted into Common Stock. Upon the conversion of the Class A
  Stock, the Company was no longer a controlled company under the rules of The Nasdaq Stock
  Market."* The Statements of Stockholders' Equity show the mechanics on one line - *"Conversion
  of Class A Shares 4,800 48 (4,800) (48)"* - and Note 12 confirms *"All shares of Class A Common
  Stock were converted into Common Stock on April 14, 2025."* **There is now one class, it is the
  class that trades, and the cover count is the whole company.** No summing was done and none was
  available to do.
- **Split factor after the measurement date: 1.0.** `close`, never `adjclose`.
- **MARKET CAP US$3,419.8 million** = 46,917,080 × $72.89.

**THE `cap_flag` CONTRADICTION, RESOLVED FROM THE DOCUMENTS - and it is the screen's, not the
company's.** The flag says *"cap $3,763M against a filed float of $3,825M (1.02x) as of
2025-11-28. A cap cannot be smaller than a subset of itself."*
- The float figure is real and I have the accession: the **10-K cover, accession
  `0001562762-26-000080`**, reads *"The aggregate market value, as reported by The Nasdaq Global
  Select Market, of the registrant's Common Stock, $0.01 par value, held by non-affiliates at
  November 28, 2025, which was the date of the last business day of the registrant's most
  recently completed second fiscal quarter, was $`3,825,418,582`."*
- **The two numbers are struck nine months apart, at two different prices, on two different
  share counts.** The close on 2025-11-28 was **$83.32**; the close on 2026-09-02, the day the
  screen was cut, was **$78.82**. The implied non-affiliate share count at the float date is
  3,825,418,582 ÷ 83.32 = **45,912,369 shares**. The 10-Q filed for that very quarter, accession
  `0001562762-26-000004`, says *"There were 47,654,046 shares of Common Stock, $0.01 par value,
  outstanding as of January 7, 2026"* - so **affiliates held on the order of 1.7 million shares,
  about 3.6% of the company**, which is what a float of 96%-odd of the cap looks like.
- **Put both on the same date and the contradiction disappears.** Those same 45,912,369
  non-affiliate shares at the 2026-09-02 close are worth **$3,619M against the screen's cap of
  $3,763M** - 96.2% of it. At this session's price they are worth **$3,347M against the
  re-struck cap of $3,420M** - 97.9% of it. **Float has been a proper subset of the cap
  throughout.**
- **DEFECT FOUND IN THE SCREEN, reported to the fold.** `cap_flag` compares a cap struck at
  today's price against a float struck at the prior half-year end and calls the difference
  arithmetically impossible. It is not impossible; it is a falling share price. The flag fires on
  **any** name that has dropped more than the affiliate percentage since its last float
  measurement date, and it fired here on a 12.5% drawdown. It is a prompt to read, and reading
  discharges it. *(Operator rule 8: a tool may not conclude. This one did, and it was wrong.)*
- *If the filing could not be obtained → **UNRESEARCHED**. Name the ladder rung that failed
  and the obstacle.* **Not invoked: every document named above was obtained from EDGAR.**

**THE `deal_note`, OPENED.** The screen flags *"1 8-K Item 1.01 filing(s) since 2026-07-22, none
carrying a merger agreement (EX-2.1)."* Opened: **8-K of 2026-09-02, accession
`0001562762-26-000102`**, Items 1.01 and 2.03. It is a **Second Amended and Restated Credit
Agreement with BMO Bank N.A., a senior unsecured revolving facility of up to $250 million**,
maturing 2031-08-31, with a $250M accordion; *"As of September 1, 2026, no amounts were borrowed
under the Credit Facility and $5.9 million in standby letters of credit were issued."* Covenants:
total funded debt to capitalization no greater than 50%, and minimum tangible net worth of $1.5
billion plus 50% of positive net income less permitted restricted payments. **No merger, no
EX-2.1, no live deal. The quote is an owner-earnings price, not a spread** - the ROKU finding does
not bite here.

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language.** Cal-Maine keeps about 50 million
  hens alive and laying, feeds them corn and soybean meal it mills itself, and sells the eggs by
  the dozen to about three buyers of consequence. In fiscal 2026 it sold **approximately 1.2
  billion dozen shell eggs** and took **$2,911.6 million** of revenue - roughly **$2.43 a dozen**
  in, against a cost of sales the segment tables put at $1,059.2M on conventional and $777.9M on
  specialty. The margin is the gap between a price it does not set and a cost it only partly
  controls. Feed is *"the largest element of our shell egg production cost, typically exceeding
  50% of our total farm production costs"*; the company milled **2.1 of the 2.2 million tons** of
  finished feed it used. Of the eggs it sold, **92.1% it produced itself** and the rest it bought
  from others at market. **90.0% of its production came from Company-owned facilities and 10.0%
  from contract producers**, under an arrangement where Cal-Maine *"own[s] the flock, furnish[es]
  all feed and critical supplies, own[s] the shell eggs produced and assume[s] market risks."*
  Growth comes from buying other egg farms: *"Since 1989, we have acquired and integrated `28`
  businesses."*
- **The scarce input this business controls.** There is not one. Hens, corn, soybean meal, land
  and labour are all purchasable by anyone with capital, and the filing says so about the two
  that matter: egg prices *"fluctuate widely and are outside our control"*, and of feed *"we do
  not have control over the prices of the ingredients we"* buy. What Cal-Maine does control is
  **scale and vertical integration** - the largest flock in the U.S., its own hatcheries, pullet
  farms, feed mills and in-line processing - which is a cost position, not a scarce input. Whether
  that cost position is **wide and sustainable** in **[E2-58]**'s sense is a Q2 question and is
  answered there.
- **Will the fundamentals look broadly the same in ten years?** Yes, and that is not a
  compliment. People will eat eggs; *"shell egg household penetration was approximately 97%"* and
  demand *"increases basically in line with the overall U.S. population growth."* The business of
  converting grain into eggs will be recognisably the same business. **This is "relatively simple
  and stable in character"** **[E3-31]** in the way the framework asks: I can state the unit
  economics without management's language and I do not need to predict a technology.
- **VERDICT: [x] IN**
  *The business is understood. Nothing here is an endorsement; [E3-31] asks whether I can follow
  the money, and I can. The three changes inside the ten years a reader should hold - the
  cage-free conversion, the prepared-foods build, and HPAI - are changes in the mix and the
  weather, not in what the company is.*

## Q2 - IS IT A FRANCHISE? **[E3-03]**

**The three criteria, scored one at a time from the registrant's own filing.**

- **(1) needed or desired - [x] YES.** *"shell egg household penetration was approximately 97%"*;
  per-capita consumption ran **260 to 286 eggs** a year between 2021 and 2025. Eggs are wanted.
- **(2) thought by its customers to have NO CLOSE SUBSTITUTE - [ ] NO. THIS IS WHERE THE FILE
  CLOSES.** The filing says the opposite of criterion (2) in four separate places, and each is the
  registrant's own words:
  - *"The production, processing, and distribution of shell eggs is an intensely competitive
    business, which has traditionally attracted large numbers of producers in the U.S. **Shell egg
    competition is generally based on price, service and product quality.** The shell egg
    production industry remains highly fragmented."* (Item 1, Competition)
  - *"The production and sale of fresh shell eggs, **which accounted for 84.6% to 94.3% of our net
    sales in our last three fiscal years**, is intensely competitive. We compete with a large
    number of competitors that may prove to be more successful than we are in producing, marketing
    and selling shell eggs. We cannot provide assurance that we will be able to compete
    successfully with any or all of these companies. Increased competition could result in price
    reductions, greater cyclicality, reduced margins and loss of market share."* (Item 1A)
  - *"**Competitive pressures may also restrict our ability to increase prices**, including in
    response to commodity and other input cost increases."* (Item 1A)
  - *"Our operating results are materially impacted by market prices for eggs and feed grains
    (corn and soybean meal), which are **highly volatile, independent of each other, and out of
    our control**."* (Item 7, Company Overview)

  The mechanism of substitution is on the face of the pricing disclosure: *"We sell our shell eggs
  at prices based on formulas that take into account, in varying ways, one of the independently
  quoted regional wholesale market prices for shell eggs"* - Urner Barry or the USDA - and
  *"Almost all of our conventional shell eggs are priced and sold under market-based pricing
  frameworks or the hybrid models described above, split almost evenly between such frameworks."*
  **A product whose price is set by reference to a published quote for the identical product from
  anybody else is the definition of a close substitute.** And the company says plainly that it does
  not reach the consumer: *"We do not sell eggs directly to consumers or set the prices at which
  eggs are sold to consumers."*
- **(3) not subject to price regulation - [x] PASSES, and it is the only one that does.** Egg
  prices are not administered. Note that this is the clause **[E2-59]** warns about from the other
  side: regulation *floors* a commodity business and *caps* a franchise, and neither creates the
  class. Here there is no floor either.

**[E3-03] requires all three. Criterion (2) fails on the registrant's own words. That is OUT on
the business, not a perimeter close.**

**Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04]** -
**not reached, and deliberately not used.** Under the verdict form ruled 2026-09-20, [E4-04] is a
**competence limit** and closes a file UNKNOWABLE, never OUT on the business. This file does not
need it: [E3-03] criterion (2) fails on filed evidence, which is an OUT the corpus supports
directly. Recorded so that no reader mistakes the route.

**THE COMMODITY DOCTRINE IS THE RIGHT FRAME, AND THE FILER WROTE IT OUT.** **[E2-58]**:
*"persistent over-capacity without administered prices (or costs) equals poor profitability"*,
long-term profitability set by *"the ratio of supply-tight to supply-ample years"*, and prosperity
breeding the next glut - *"nothing fails like success."* Item 1A says it in the company's voice:

> *"During times when prices are high, the egg industry has typically produced more eggs,
> primarily by increasing the number of layers, which historically has ultimately resulted in an
> oversupply of eggs, leading to periods of lower prices."*

**THE ONE EXCEPTION [E2-58] ALLOWS, TESTED RATHER THAN ASSUMED** - *"a cost advantage that is both
wide and sustainable … By definition such exceptions are few."* Cal-Maine has the best claim to it
of any egg producer in the United States: the largest flock, its own feed mills, in-line
facilities, 28 acquisitions since 1989. **It fails the test on its own filed record**, and the
reason is the shape of the record rather than its level.

**[E2-01]'s primary test, run as a multi-year series - the earnings rate on equity capital
employed, balance sheet before income statement:**

| fiscal year | net income ($m) | stockholders' equity ($m) | **ROE** |
|---|---|---|---|
| 2011 | 60.8 | 418.9 | 14.5% |
| 2012 | 89.7 | 479.1 | 18.7% |
| 2013 | 50.4 | 517.7 | 9.7% |
| 2014 | 109.2 | 593.8 | 18.4% |
| 2015 | 161.3 | 703.6 | 22.9% |
| **2016** | **316.0** | 915.3 | **34.5%** |
| **2017** | **-74.3** | 842.7 | **-8.8%** |
| 2018 | 125.9 | 953.3 | 13.2% |
| 2019 | 54.2 | 986.6 | 5.5% |
| 2020 | 18.4 | 1,009.7 | 1.8% |
| 2021 | 2.1 | 1,012.8 | 0.2% |
| 2022 | 132.7 | 1,104.6 | 12.0% |
| **2023** | **758.0** | 1,611.1 | **47.1%** |
| 2024 | 277.9 | 1,800.1 | 15.4% |
| **2025** | **1,220.0** | 2,560.6 | **47.6%** |
| 2026 | 316.7 | 2,632.7 | 12.0% |

*(`NetIncomeLoss` and `StockholdersEquity`, 10-K vintages, newest restatement, SEC companyfacts;
fiscal 2026's two lines cross-checked against the filed statements in Step 0.)*

- **Sixteen-year mean ROE: 16.6%.** Strip the three supply-shock years - **2016** (the year after
  the 2015 HPAI depopulation), **2023** and **2025** (the outbreaks that started in 2022, in which
  *"40.2 million and 45.2 million commercial layer hens and pullets were depopulated due to HPAI"*
  in 2024 and 2025) - and **the mean of the other thirteen years is 10.4%.** That is at or about
  the return on equity earned by American industry in aggregate, which is exactly where
  **[E2-42]** says *"red lights should start flashing."*
- **A wide and sustainable cost advantage does not produce a -8.8% year.** Fiscal 2017 is the
  glut that followed the 2016 spike: net loss $74.3 million, and **operating cash flow of minus
  $45.9 million.** Fiscal 2021 is the second: ROE 0.2%. **The low-cost producer in a commodity
  still loses money when the cycle turns** - which is [E2-58]'s point, not a refutation of it.
- **The excess is dated, and it is dated to the disease.** Conventional shell egg prices rose
  **99.7%** in fiscal 2025 and fell **50.9%** in fiscal 2026, on the filer's own variance table,
  with *"Volumes for conventional shell eggs … relatively flat"* in both directions. Conventional
  segment income went **$213.7M → $1,290.0M → $216.6M**. **The windfall was a price the company
  did not make, and it left on the same terms.** This is **[E4-41]** in its own home: a favourable
  exogenous break, named and removed before the mean is trusted.
- **[E3-46]**'s number, asked about the business before the manager - *"the best businesses, by
  definition, are going to be businesses that earn very high returns on capital employed over
  time"* - is answered by the thirteen-year 10.4%, not by the two spikes.

**[E3-62]'S SECOND STEP - WHO DO THE GAINS FLOW TO? - IS ANSWERED BY THE FILER'S OWN PRICING
DISCLOSURE, AND THE ANSWER IS THE CUSTOMER.** The corpus's question is *"how much is going to stay
home and how much is just going to flow through to the customer"*. Cal-Maine has written the answer
into its contracts:
- *"**The majority of our specialty shell eggs are priced and sold under frameworks that are based
  on cost of production**"* - a cost-plus contract passes every efficiency gain to the buyer by
  construction, and specialty was **$1,070.5M, 36.8% of fiscal 2026 net sales.**
- On the conventional half the price is a published third-party quote, so a cost saving lands in
  the margin only until the industry's next round of capacity says otherwise - and Item 1A adds
  that even the cost-based contracts leak in the other direction: *"customers may seek to
  renegotiate the terms of their arrangements during periods of sustained low prices."*
- And the counterparty has the weight to ask. **Walmart Inc. (including Sam's Club) was 30.0% of
  consolidated net sales in fiscal 2026; the top three customers were 43.1%.**

**THE COMPETITOR ROW - required [E3-28].** *A moat is a claim about relative position and cannot
be evidenced from one company's numbers.* Same metric (**[E2-01]**'s earnings rate on equity
capital employed), same window (the last eight filed fiscal years of each registrant), each figure
from that registrant's own 10-K filings.

| Company | metric | same window - eight filed fiscal years | mean | source |
|---|---|---|---|---|
| **CAL-MAINE FOODS (CALM)** | ROE | FY19 5.5 · FY20 1.8 · FY21 0.2 · FY22 12.0 · FY23 47.1 · FY24 15.4 · FY25 47.6 · FY26 12.0 | **17.7%** | 10-K, CIK 0000016160 |
| **Vital Farms (VITL)** - pasture-raised shell eggs, the only other listed pure-play | ROE | FY19 27.9 · FY20 6.2 · FY21 1.6 · FY22 0.8 · FY23 13.3 · FY24 19.8 · FY25 18.9 *(seven filed)* | **12.6%** | 10-K, CIK 0001579733 |
| **Post Holdings (POST)** - owner of Michael Foods, the largest US egg-products business | ROE | FY18 15.3 · FY19 4.3 · FY20 0.0 · FY21 6.1 · FY22 23.3 · FY23 7.8 · FY24 9.0 · FY25 8.9 | **9.3%** | 10-K, CIK 0001530950 |
| **Pilgrim's Pride (PPC)** - the nearest listed commodity-protein comparable | ROE | FY18 12.3 · FY19 18.1 · FY20 3.7 · FY21 1.2 · FY22 26.3 · FY23 9.7 · FY24 25.6 · FY25 29.4 | **15.8%** | 10-K, CIK 0000802481 |
| **Tyson Foods (TSN)** - the largest US protein producer | ROE | FY18 23.2 · FY19 14.2 · FY20 13.5 · FY21 17.2 · FY22 16.4 · FY23 -3.6 · FY24 4.4 · FY25 2.6 | **11.0%** | 10-K, CIK 0000100493 |

- **Peers named: 4, of an industry whose ten largest producers held `57%` of table-egg layer hens
  at calendar year-end 2025** (10-K, citing *Egg Industry Magazine*). **The rest of that ten are
  private and file nothing with the Commission** - Rose Acre Farms, Versova, Daybreak, Hillandale,
  MPS and the others leave no primary document to read. The evidence-ladder note the framework asks
  for: **the rung is "competitor filings" and the obstacle is that the competitors are not
  registrants.**
- **What the row shows, and what it cannot.** Cal-Maine's mean sits highest, and it is *supposed*
  to - it is the largest and the most integrated. But **every name in the column has the same
  shape**: two or three spike years carrying a mean the median year does not support. Pilgrim's ran
  1.2% in FY21 and 26.3% in FY22; Tyson ran -3.6% in FY23; Vital Farms ran 0.8% in FY22. **Identical
  structure, identical signature.** That is the commodity equation showing up five times in one
  table, and it is why a higher mean here is a better position *inside* the class rather than an
  exit from it. **[E3-61]**'s limit is recorded as the framework requires: the row shows position;
  it cannot show conduct.
- **The row is NOT the reason for the verdict**, and it is not held PROVISIONAL as a way of
  avoiding one. The verdict rests on [E3-03] criterion (2), which fails on Cal-Maine's own filed
  words about its own product. The row is here because the framework requires it and because it
  **corroborates** that reading from five independent registrants.

**UNTAPPED PRICING POWER - could a manager raise the return simply by raising prices, and has not?
[E3-33]** - **No, and the claim is not available to make.** **[E5-28]** scopes the class: *"If you
name some business that has incredible pricing power, you're talking about a business that's a
monopoly or a near monopoly."* Cal-Maine is the largest of a field in which the **top ten hold 57%**
and it holds roughly a sixth of the national flock (**50.0 million layers and 14.5 million pullets
and breeders** at 2026-05-30, *"the largest in the U.S."*, in an industry that depopulated 45.2
million hens in 2025 alone without the market clearing for long). The inverse metric **[E4-37]**
points the same way and the filing supplies the reading: *"Competitive pressures may also restrict
our ability to increase prices."* **That is agony-pricing, written by the filer.**

**THE BRANDED LEG, TESTED SEPARATELY BECAUSE IT IS THE STRONGEST DISCONFIRMING CASE [E4-26].** The
specialty segment is 36.8% of sales and carries names - *"Eggland's Best®, Land O'Lakes®, Farmhouse
Eggs®, 4Grain®"*. If a franchise lives anywhere in this company it lives there. It does not, and the
filing says why: **the two brands that matter are rented.** They come *"from our cooperative
membership in Eggland's Best, Inc."*, Cal-Maine pays **franchise fees** for them, and the fee is the
co-op's to set - *"In fiscal 2025, the higher prices for conventional shell eggs compared to
specialty shell eggs diminished the need to promote specialty shell eggs, during which time, EB
temporarily reduced the related franchise fees for certain specialty shell egg brands"*, and those
fees came back in fiscal 2026 as **a $4.7 million increase.** A brand whose licensor reprices it
against the licensee's own cycle is **shape #13 THE TENANT** by construction, not a moat. And the
segment did not behave like one: **specialty segment income fell 45.6%, from $333.6M to $181.5M**,
on a **2.4% increase** in dozens sold and a **9.5% decrease** in price.

**A SECOND DISCONFIRMING TEST, AND IT CUTS THE SAME WAY.** The nearest thing to an administered
price this industry ever had was the **United Egg Producers animal-welfare guidelines**, whose
supply effect the Egg Products Plaintiffs attacked directly: on **December 1, 2023 a jury returned
a decision awarding … $17.8 million in damages**, and on **November 6, 2024 the court entered final
judgment against the Company and other defendants, jointly and severally, totalling $43.6 million
after trebling**, on the allegation that the defendants violated the Sherman Act *"by agreeing to
limit the production of eggs and thereby illegally to raise the prices that plaintiffs paid for
processed egg products."* Cal-Maine also settled a DOJ and 17-state antitrust investigation on or
about **June 25, 2026**, denying wrongdoing, with **no fines or penalties**, **$1.5 million** to the
settling states and **30 million eggs** donated; Washington State did not join and its investigation
continues. **[E2-59]** is the row: administered pricing can floor a commodity business, but the moat
belongs to the **regime**, and *"That day is gone"* is how it ends. **Here the regime is being
dismantled in court.** This is recorded as Q2 evidence about the *class* of the business. **It is
NOT scored as a Q3 finding, because Q3 is not reached** - the run stops here, and scoring a gate the
sequence never opens is the violation the operator protocol exists to prevent.

- Class: [ ] WIDE [ ] NARROW [x] **NONE** [ ] PROVISIONAL · Direction: **the two moat-shaped things
  in the file are both weakening.** The licensed specialty brands repriced against Cal-Maine in
  fiscal 2026 (+$4.7M of fees into a -45.6% segment income), and the industry's supply-side
  coordination sits under a $43.6M judgment and a settled federal investigation.
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**WHY OUT AND NOT UNKNOWABLE.** The separating test, asked aloud **[E4-19]**: *can I name the
document that would resolve this?* There is nothing left to name. The document is already in hand
and it is the registrant's own Form 10-K, which says the product is sold into an *"intensely
competitive"* and *"highly fragmented"* industry at prices *"outside our control"* set off a
published third-party quote, against competitors it *"cannot provide assurance"* it can beat.
**The evidence is here and the business fails criterion (2). That is OUT** - the permanent,
about-the-business verdict - and no fetch repairs it.

---
## Q3 - ARE THEY HONEST, AND ARE THEY RATIONAL?

**NOT REACHED. THE FILE CLOSED AT Q2 (OUT).** Operator rule 2: the sequence is a hard block, and no
later question may be scored. What was seen in passing while reading Q2's documents is recorded in
**FINDINGS NOT SCORED** below, explicitly as unscored evidence for a future run, and it is **not** a
Q3 verdict.

## Q4 - WILL IT SURVIVE?

**NOT REACHED.** No survival shape is named, and `Screens/SURVIVAL SHAPES - index.md` takes no new
row from this run. The owner-earnings series below was built because the brief ordered the width
rebuilt over every window and both (c) ends, and because the screen's own caveats had to be
discharged. **It is headed as the protocol requires and it carries no entry language.**

### COMPUTATION — NOT A CLEARANCE

*Produced before Q1-Q4 all showed IN, and therefore reported under operator rule 3 as a
computation. It votes on nothing. It is here to discharge four of the screen's caveats -
`spread_caveat`, `window_disagree`, `level_shift`/`level_shift_oe`, and `flags_disagree` - and to
leave the next reader of this name a series that does not have to be rebuilt.*

**Construction.** Owner earnings = operating cash flow - stock compensation - (c) **[E2-23]**, the
confessed CONVENTION of `THE FRAMEWORK v4.md` section VI. **(c) is a disclosed judgment and is shown
at both ends**: the D&A default **[E3-44, E2-41]** and total capex. All four input series are taken
from the filed Consolidated Statements of Cash Flows across **the whole filed history, seventeen
years, fiscal 2010 to fiscal 2026** - not the five the screen could see. Fiscal 2026's lines were
cross-checked against the filed statement in Step 0. **No net-income proxy is used anywhere in this
run** (operator rule 5; PRIME RULE 3 as amended 2026-09-20).

**SBC RESOLVES FOR EVERY ONE OF THE SEVENTEEN YEARS, and it was checked rather than assumed** (the
BE defect). `ShareBasedCompensation` resolves only from fiscal 2019; the earlier years resolve under
`AllocatedShareBasedCompensationExpense` (the footnote figure, rounded to $0.1M) and
`AdjustmentsToAdditionalPaidInCapital…RequisiteServicePeriodRecognition` (the equity-statement
figure). The two agree to the rounding. **No year had zero silently substituted for it.**
**Materiality, stated so the [E3-70] grant-value question is closed rather than deferred:** stock
compensation was **$5.757 million in fiscal 2026, 1.2% of operating cash flow**, and **89,867
restricted shares were granted in the year**. At any plausible grant price that is under $10 million
against $480 million of operating cash. **Neither the charge nor the grant value can move this
series enough to matter - the opposite of the ARM/CALX finding, and recorded as such.**

| FY | OCF | SBC | D&A | capex | **OE, (c)=D&A** | **OE, (c)=capex** |
|---|---|---|---|---|---|---|
| 2010 | 116,668 | 218 | 31,785 | 20,786 | 84,665 | 95,664 |
| 2011 | 62,310 | 218 | 30,754 | 20,742 | 31,338 | 41,350 |
| 2012 | 98,058 | 0 | 30,752 | 26,845 | 67,306 | 71,213 |
| 2013 | 57,538 | 292 | 34,173 | 26,290 | 23,073 | 30,956 |
| 2014 | 123,920 | 1,274 | 37,203 | 59,188 | 85,443 | 63,458 |
| 2015 | 195,330 | 2,268 | 40,708 | 82,263 | 152,354 | 110,799 |
| 2016 | 388,437 | 3,071 | 44,592 | 76,125 | 340,774 | 309,241 |
| **2017** | **-45,918** | 3,427 | 49,113 | 66,657 | **-98,458** | **-116,002** |
| 2018 | 200,415 | 3,467 | 54,026 | 19,671 | 142,922 | 177,277 |
| 2019 | 115,085 | 3,619 | 54,650 | 67,989 | 56,816 | 43,477 |
| 2020 | 73,609 | 3,617 | 58,103 | 124,178 | 11,889 | **-54,186** |
| **2021** | 26,136 | 3,778 | 59,477 | 95,069 | **-37,119** | **-72,711** |
| 2022 | 126,209 | 4,063 | 68,395 | 72,399 | 53,751 | 49,747 |
| 2023 | 863,010 | 4,205 | 72,234 | 136,569 | 786,571 | 722,236 |
| 2024 | 451,398 | 4,358 | 80,241 | 147,116 | 366,799 | 299,924 |
| **2025** | 1,224,734 | 4,527 | 94,021 | 161,255 | **1,126,186** | **1,058,952** |
| 2026 | 479,753 | 5,757 | 124,342 | 151,220 | 349,654 | 322,776 |

*(thousands of dollars)*

**THE WIDTH, REBUILT OVER EVERY WINDOW AND BOTH (c) ENDS.**

| window | mean OE, (c)=D&A | mean OE, (c)=capex |
|---|---|---|
| 3 years, FY2024-26 | **$614.2M** | $560.6M |
| 5 years, FY2022-26 *(the corpus default **[E2-42]**)* | $536.6M | $490.7M |
| 5 years, FY2021-24 + FY2026 *(same count, fiscal 2025 removed)* | $303.9M | $264.4M |
| 9 years, FY2018-26 | $317.5M | $283.1M |
| 10 years, FY2017-26 | $275.9M | $243.1M |
| 8 years, FY2010-17 *(the early half the screen could not see)* | $85.8M | $75.8M |
| 13 years, FY2010-22 *(the record before the current HPAI cycle)* | $70.4M | **$57.7M** |
| **17 years, FY2010-26 - the whole filed history** | $208.5M | $185.5M |

**THE FULL COMBINED RANGE IS $57.7M TO $614.2M - a factor of 10.6.** The screen published
**$491M to $614M** and said in its own `spread_caveat` that it was *"4-construction width only
(3y/5y x two capex ends): CANNOT see variation older than the 5-year window; rebuild it [E4-25]."*
**The screen was right about its own blindness.** Rebuilt over seventeen years, its published bottom
is not the bottom - it is the top of the second-best window, and the true bottom is **one-eighth of
it.**

**A WORD WHERE THE BOTTOM SITS NEAR OR BELOW ZERO, as the brief requires.** It does, three times.
**Fiscal 2017 is negative on both ends** (-$98.5M and -$116.0M) and its operating cash flow itself
is negative. **Fiscal 2021 is negative on both ends.** **Fiscal 2020 is negative on the capex end**
and $11.9M on the D&A end. **In three of seventeen filed years - 18% of the record - this business
returned nothing to an owner, and in one of them it consumed cash.** The screen's `level_note_oe`
field, truncated in the CSV, was reporting exactly this and the truncation hid the half that
mattered: *"EARLY HALF STRADDLES ZERO - the pre-window years run from $-72.7M to $"*. Rebuilt, the
early half runs from **-$116.0M (FY2017, capex end) to +$340.8M (FY2016, D&A end).** The truncated
string pointed at a true finding; the brief's instruction to treat truncation as a missing string and
rebuild from the filings was the right call, because the rebuilt figure says more than the sentence
did.

**`level_shift` AND `level_shift_oe`, READ FROM THE FILINGS [E4-41].** The screen fired both - 3.07
and 0.343 - with the note *"STEP UP - normalize down [E4-41]"*. **Read the row, read the filer's own
explanation, and the normalisation is owed.** The filer's variance table says conventional shell egg
prices rose **99.7%** in fiscal 2025 and fell **50.9%** in fiscal 2026, with volumes *"relatively
flat"* both ways, because **40.2 million and 45.2 million commercial layer hens and pullets were
depopulated due to HPAI** in 2024 and 2025 - **rivals' hens, overwhelmingly, not Cal-Maine's.**
Cal-Maine lost about **352,000 pullets** to a single Maryland outbreak on 2026-03-14 and *"operations
have fully resumed."* **A price rise caused by the destruction of competitors' inventory is the
definition of a favourable exogenous break**, and [E4-41] says name it and remove it before the mean
is trusted. **The normalised level, taken from the record rather than from an adjustment of my own
devising: the thirteen years before the current HPAI cycle, fiscal 2010 to fiscal 2022, mean $57.7M
to $70.4M of owner earnings.** The business has since been enlarged by roughly $667 million of
acquisitions (below), so that figure is a floor read on the old perimeter and not a forecast for the
new one. **The screen's flag was right here. It has been wrong elsewhere in this project; it was
checked, not assumed.**

**`flags_disagree` - "one series refuses the ratio and the other does not; read the filing
[E4-25]".** Read. The two series disagree because **owner earnings go negative where net income does
not**: fiscal 2017 has net income of -$74.3M and owner earnings of -$98.5M to -$116.0M, and fiscal
2021 has net income of **+$2.1M** and owner earnings of **-$37.1M to -$72.7M**. **A ratio taken
across a sign change is not a ratio**, which is the same defect the Opus session fixed in
`level_shift` for ARM. **The disagreement is the finding, and the finding is that this business has
years in which it earns an accounting profit and no owner earnings at all.**

**`window_disagree` - "9yr and the full 17yr series give different KINDS of answer; the 9yr base may
already contain the wave [E4-41]."** Confirmed from the filings, and the screen understated it. The
nine-year base (FY2018-26) contains **both** HPAI cycles and misses **both** of the troughs that
frame them; the seventeen-year base contains one full peak-to-glut round trip (FY2016 +$340.8M →
FY2017 -$98.5M) the nine-year base cannot see at all. **[E4-38]** is the instruction followed here:
publish every window rather than defend one.

**THE ACQUISITION PERIMETER - every event in the window, dated from the filings.** The screen said
*"acquisitions are $643M, 17% of cap, inside the window - the numerator and denominator may be
different compani[es]"*. Rebuilt from the filed investing section and Note 2 - Acquisitions:

| effective date | fiscal year | event | consideration |
|---|---|---|---|
| Q1 FY2025 | 2025 | **ISE America** - ~4.7M layers (1.0M cage-free), 1.2M pullets, feed mills, ~4,000 acres, MD/NJ/DE/SC | within FY2025's $116.2M |
| Q2 FY2025 | 2025 | **MeadowCreek Foods LLC** - remaining interests acquired, becomes wholly owned | within FY2025's $116.2M |
| Q2 FY2025 | 2025 | **Crepini Foods LLC** - 51% JV, ~$6.75M cash contributed | within FY2025's $116.2M |
| Q3 FY2025 | 2025 | **Deal-Rite Foods** - two feed mills, storage, NC | within FY2025's $116.2M |
| **2025-06-02** | 2026 | **Echo Lake Foods LLC** - prepared foods, ~$289.5M | within FY2026's $427.8M |
| **2025-10-10** | 2026 | **Clean Egg LLC** - 677k brown cage-free / free-range layers and pullets, ~$23.7M | within FY2026's $427.8M |
| **2026-03-02** | 2026 | **Creighton Brothers / Crystal Lake** - 3.2M layers, 865k pullets, feed mill, 1,007 acres, egg-products and hard-cooked facility, ~$129.3M | within FY2026's $427.8M |
| **2026-05-12** | 2026 | **Van's Foods** (from Sara Lee Frozen Bakery) - ~$24.8M | **$24.8M, tagged on its own line** |

- **Five-year total, filed investing cash: $44.8M (FY22) + $0 (FY23) + $53.7M (FY24) + $116.2M (FY25)
  + $452.6M (FY26) = $667.3 million, 19.5% of the re-struck cap.** The screen's $643M omitted the
  separately-tagged Van's line; the correct figure is **higher**, not lower.
- **Which years are pre- and post-perimeter: fiscal 2010-2024 are pre-perimeter; fiscal 2025 is the
  first part-year of ISE, MeadowCreek, Crepini and Deal-Rite; fiscal 2026 is the first full year of
  those and the first part-year of Echo Lake, Clean Egg, Creighton and Van's.** **Fifteen of the
  seventeen years in the table above are a different company from the one the price buys**, and every
  long-window mean is therefore the mean of a smaller business.
- **The tested source limit is noted rather than re-attempted** (`RESUME STATE`, section 5): stock
  consideration in an acquisition perimeter does not resolve undimensioned in companyfacts on any of
  the four names tested, so **the investing-cash line is the floor of the number, not the number.**
  Here it is close to the whole of it - the share count fell in every year of the window and treasury
  purchases ran $1.7M → $50.4M → $131.1M over FY2024-26, so nothing material was bought with paper.

**IS THE RANGE TOO WIDE TO REACH A CONCLUSION? [E4-25]** *"Usually, the range must be so wide that no
useful conclusion can be reached."* **$57.7M to $614.2M against a $3,419.8M cap is a yield of 1.7%
to 18.0%.** On this evidence no useful conclusion could be reached at Q5 even if Q5 were open, and
**[E3-55]**'s carve-out does not rescue it: that exception is for a business *"about which we're
extremely confident as to the business result"* whose yearly figure merely bounces. Here the *level*
is what is unknown, and three of seventeen years have no owner earnings at all. **Recorded, unranked,
and not used as a verdict - the verdict was reached at Q2, on the business, not on the price.**

---
## Q5 - WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**NOT OPENED.** Q2 returned OUT. ⛔ The sequence is a hard block; no Q5 output may be reported. **The
sovereign is recorded in Step 0 for the register entry only, and no yield is struck against it.**

## Q6 - WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**NOT REACHED** - there is no position and no entry. **The reversal condition is recorded in words
instead**, per the QLYS ruling of 2026-09-07, and no price band is armed in `tools/alerts.json`,
because a price alert on a name that failed on the business is a category error.

**WHAT WOULD REOPEN THIS FILE.** Not a price. A change in the **structure** of the industry, and
there are only two shapes it could take, both visible in a filing:
1. **A durable narrowing of the field** - the 10-K's own *"the ten largest producers owned
   approximately `57%` … of industry table egg layer hens"* moving far enough, for long enough, that
   Cal-Maine's realised price stops tracking the Urner Barry quote. The metric to watch is the one
   the filer publishes itself: the split between market-based and cost-based pricing frameworks,
   today *"split almost evenly"* on conventional.
2. **The mix crossing over** - prepared foods and **owned** (not licensed) branded products growing
   from today's remainder into a majority of segment income, with pricing that does not reference a
   published quote. Shell eggs were **84.6% to 94.3% of net sales in the last three fiscal years**;
   the announced expansions add *"more than 30 percent"* of prepared-foods capacity from mid-2027
   through 2028. **That would be a different company and would need a new run, not a revision of
   this one.**

---
## FINDINGS NOT SCORED - seen while reading Q2's documents, recorded for a future run

*These are **not** verdicts. Q3 and Q4 were never opened, and nothing below was scored against any
gate. They are written down so a later run does not have to rediscover them, and so this file cannot
be read as having scored a gate it did not open.*

- **Antitrust, on the record rather than alleged.** Jury decision 2023-12-01 awarding **$17.8
  million**; final judgment 2024-11-06 against the Company and other defendants, joint and several,
  **$43.6 million after trebling**; a bond of approximately **$23.9 million** posted 2024-12-17
  pending appeal, another defendant posting the remainder. DOJ and 17-state settlement on or about
  **2026-06-25** - **no fines or penalties**, **$1.5M** to the settling states, **30 million eggs**
  donated, antitrust compliance and reporting measures agreed, **wrongdoing denied**; **Washington
  State did not join** and its investigation continues, with management *"unable to estimate the
  amount or range of potential losses, if any, at this time."* New putative class actions were
  consolidated by the Judicial Panel on Multidistrict Litigation on **2026-02-10** into the Western
  District of Wisconsin, with **no discovery yet taken**. **[E5-16]**'s binary is the right
  instrument and **this run did not apply it.**
- **Customer concentration.** Walmart (including Sam's Club) **30.0%** of consolidated net sales in
  fiscal 2026, **33.6%** in 2025, **34.0%** in 2024; top three **43.1% / 49.2% / 49.0%.**
- **Segment reporting changed in the fourth quarter of fiscal 2026**, from one reportable segment to
  three, with *"All prior fiscal year periods … recast to reflect the new reportable segments."*
  **[E2-49]**, the withdrawn-yardstick prior, is the row that asks whether a yardstick was disposed
  of as results deteriorated. **This run did not score it.** What a future run needs, stated both
  ways so the brief does not smuggle in a conclusion: the change was made **in the year conventional
  segment income fell 83.2%**, which is the pattern [E2-49] describes; against that, the new segments
  **disaggregate** rather than blend, prior periods were recast so the comparison survives, and the
  prepared-foods build supplies an operating reason. **Six fires and five failures is where this
  prior stands in the project; it is flagged here, not resolved.**
- **A variable dividend that tracked the windfall down.** *"Dividends ($`8.319` per share)"* in
  fiscal 2025 against *"($`2.458` per share)"* in fiscal 2026; cash dividends paid $330.3M → $231.6M
  while treasury purchases rose $54.0M → $131.1M. **[E2-52]**'s issuance-funded-dividend flag does
  **not** fire: the share count fell in every year of the window and no equity was sold.
- **Balance sheet, for whoever opens Q4 next**: no borrowings under the new $250M revolver as of
  2026-09-01, $5.9M of standby letters of credit; cash, cash equivalents and restricted cash
  **$113.5M** at 2026-05-30, down from $500.4M, with $648.9M of investments purchased and $745.2M
  sold during the year; total equity **$2,640.5M**; a covenant floor of $1.5bn tangible net worth.
- **A defect in the screen, reported to the fold**: `cap_flag` compares a cap struck at today's price
  against a float struck at the prior half-year end and declares the gap arithmetically impossible.
  It is not; it is a share price that fell 12.5% in nine months. See Step 0.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **Q1 IN, Q2 OUT, and the run stopped there.**
      Q3, Q4, Q5 and Q6 are marked NOT REACHED and carry no verdict.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the only IN
      and it rests on the filed 10-K read this session.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives. **None was returned.**
- [x] Every UNKNOWABLE verdict states what specifically cannot be known. **None was returned.**
- [x] Step 0: the filing was read, with accession number; **two** figures were cross-checked against
      the filed statements (the share count against the equity statement; operating cash flow and net
      income against the cash-flow statement).
- [x] Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.
      **Eight windows and both (c) ends, over the whole seventeen-year filed history** - and the whole
      block is headed **COMPUTATION — NOT A CLEARANCE** under operator rule 3, because it was produced
      before Q1-Q4 all showed IN, which they never did. **No net-income proxy anywhere.**
- [x] Competitor row filled. **Four registrants, same metric, same window, each from its own 10-K
      filings**, with the industry's private majority named as a ladder-rung obstacle. **The moat class
      is NONE, not PROVISIONAL**: the verdict rests on the subject's own filed words about its own
      product, not on the completeness of the row.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated. **5.34%, 09/18/2026,
      US Treasury daily par yield curve.** Cache deleted and struck fresh this session; nothing
      inherited from the brief.
- [ ] Value stated as a round-number range, not a point estimate. **N/A - Q5 not opened.**
- [ ] One bar chosen, not both; windage count stated. **N/A - Q5 not opened. Conservatism was spent
      nowhere; there was no valuation to spend it on.**
- [x] Prices dated; aggregator used for live quotes only and flagged. **$72.89, 2026-09-18, Yahoo via
      `tools/sources.py`, flagged, used only for the cap.**
- [x] Run committed to git.

**Two further checks this run owed and performed:**
- [x] **Every ledger id cited above was verified against `principle_ledger.csv` before it was
      written**, by line-start match, as the brief requires. The file carries **311 rows** (312 lines
      with the header); `CLAUDE.md`'s "267 rows" line is stale and this run did not edit it.
- [x] **[E4-26] applied to my own preferred answer.** The reading ran toward OUT early, so the two
      strongest disconfirming cases were built out rather than skipped: the **[E2-58]** cost-advantage
      exception (tested against a sixteen-year ROE series and failed at -8.8% in fiscal 2017 and +0.2%
      in fiscal 2021), and the **branded specialty leg** (tested against the Eggland's Best
      franchise-fee disclosure and found rented). Both strengthened the verdict rather than weakening
      it. Recorded so the reader can check that the hunt was made. *"you must not fool yourself, and
      you're the easiest person to fool"* **[E3-41]**.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **Q2 OUT - the largest egg producer in the United States sells a commodity at prices set
  off a published third-party quote, in an industry its own 10-K calls "intensely competitive" and
  "highly fragmented", so [E3-03]'s criterion (2) fails on the registrant's own words; the [E2-58]
  cost-advantage exception was tested against a sixteen-year ROE series and failed at -8.8% in fiscal
  2017 and +0.2% in fiscal 2021.**
- **If UNRESEARCHED - THE WORK ORDER:** n/a.
- **If UNKNOWABLE:** n/a.
