# Company Run - USANA Health Sciences, Inc. (USNA) - 2026-09-21

**STATUS: CLOSED 2026-09-21 - VERDICT Q2 OUT.** Written as it went (write-early protocol);
Q3 through Q6 are recorded beneath the close and govern nothing.
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
- rate **5.34%** - date **2026-09-18** - source **US Treasury daily par yield curve, 30-year,
  from the issuing authority** (`python tools/sources.py`). FRED DGS30 not used; no fallback needed.
- FX: not applicable to the quote. **But note the earnings currency is only nominally USD** -
  91.1% of Core Nutritional net sales were made outside the United States in H1 2026 (10-Q,
  2026-07-04), and China alone was 41.3% of FY2025 consolidated net sales. USD is the reporting
  currency; the sovereign is read as the reporting currency of the filer, and this mismatch is
  recorded rather than adjusted for, because the corpus prices the currency the business earns in
  and offers no method for a basket. Recorded as a limit of this run.

**The filing was read** - not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary document - date - accession no.:**
  - **Form 10-K, FY ended 2026-01-03 (a 53-week year), filed 2026-03-16, accession
    `0000896264-26-000021`**, primary document `usna-20260103.htm`.
  - **Form 10-Q, quarter ended 2026-07-04, filed 2026-08-13, accession `0000896264-26-000056`**,
    primary document `usna-20260704.htm`. *(This is the newest periodic filing - the `newest_periodic`
    field on the screen row, 2026-07-04, is correct.)*
  - **DEF 14A, filed 2026-04-07, accession `0000896264-26-000026`.**
  - **8-K of 2026-08-04, accession `0000896264-26-000050`** (Items 2.02, 7.01, 9.01) - the Q2 2026
    earnings release, pulled for **[E4-29]** and **[E4-22]**'s third flag, standing since the CGNX run.
- **Figures cross-checked against the filed statement** (Consolidated Statements of Cash Flows and
  of Comprehensive Income, 10-K accession `0000896264-26-000021`): FY2025 **net cash provided by
  operating activities $22,349 thousand**, **equity-based compensation expense $13,828**,
  **depreciation and amortization $32,562**, **purchases of property and equipment $13,823**. All
  four match the XBRL series used at Q4 below to the dollar. FY2025 **net sales $925,257** and
  **earnings from operations $37,432** cross-checked against the filed income statement.

---
## THE CAP FLAG - RESOLVED BEFORE ANY YIELD IS COMPUTED (operator rule 4)

The screen row's loudest field said: *"CAP BELOW FILED PUBLIC FLOAT - cap $263M against a filed
float of $328M (1.25x) as of 2025-06-27. A cap cannot be smaller than a subset of itself.
RE-STRIKE THE CAP BY HAND before using any yield on this row."*

**Neither input is wrong. The comparison is.** Read from the 10-K cover page, accession
`0000896264-26-000021`:

> "The aggregate market value of common stock held by non-affiliates of the registrant **as of
> June 27, 2025**, was approximately $ 328 million **based on a closing market price of $31.13
> per share**."

> "There were **18,456,935** shares of the registrant's common stock outstanding **as of March
> 13, 2026**."

And from the 10-Q cover page, accession `0000896264-26-000056`:

> "As of **August 11, 2026** , th ere were **18,476,534** outstanding shares of the registrant's
> common stock, $0.001 par value." *(the spacing artifact is the filer's; PRIME RULE 1 forbids
> smoothing it)*

The $328 million is a **dollar amount struck at a $31.13 price fifteen months before the cap was
measured.** The closing price on 2025-06-27 was **$31.13** - the price series agrees with the
cover page to the cent, which is the cross-check. The price on 2026-09-21 is **$14.40**, a
**53.7% fall**. The non-affiliate share count implied by the cover is 328/31.13 = **about 10.5
million shares**, against roughly 19 million outstanding, which is consistent with the 10-K's own
statement that *"Gull Global, Ltd., an entity that is solely owned and controlled by our founder,
Dr. Myron Wentz, owned approximately 40.0% of our outstanding common stock at January 3, 2026."*

**So the float is a proper subset of the cap at every single date; the screen compared two
different dates.** This is a **TOOLING DEFECT**, recorded in the fold: `cap_flag` sets a live
market cap against the cover-page non-affiliate market value, which by SEC rule is struck at the
last business day of the registrant's most recently completed second fiscal quarter and can be up
to eighteen months stale. In a stock that has halved it fires with a false claim of arithmetic
impossibility. **The flag was still worth obeying** - it sent a reader to the cover page, which is
exactly where operator rule 4 wanted them. It is a false positive with a true instruction.

**THE CAP, RE-STRUCK BY HAND:**

| | |
|---|---|
| shares outstanding | **18,476,534** |
| share basis | **10-Q cover page, as of 2026-08-11, accession `0000896264-26-000056`** |
| price | **$14.40** |
| price date | **2026-09-21** *(aggregator - live quote only, flagged, operator rule 5)* |
| **market cap** | **$266.1 million** |

No split has occurred between the measurement date and the anchor, so the split-invariance rule
is satisfied trivially; the cover count and the balance-sheet count (18,463 thousand shares issued
and outstanding at 2026-07-04) agree to within the quarter's equity-award issuance. The screen's
$263M differed only by the price used.

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.**

USANA makes vitamin pills, protein powder and face cream, and sells them to the people who sell
them. There is one customer type that matters: a person who signs up, buys a monthly box of
supplements largely for their own use, and is paid a commission if they recruit others who do the
same. The filing calls them Brand Partners and Preferred Customers and adds them together as
*"active Customers"*; it counts as active anyone who bought at any time in the most recent three
months. Revenue is therefore **customers times average spend**, and the company says so itself:
*"we increase our sales by increasing the number of our active Customers, the amount they spend
on average, or both."*

The cost structure is the tell. Of FY2025's $925.3M of net sales (filed income statement): gross
profit 78.3%, then **Brand Partner incentives of $336.2M - 43.3% of core nutritional net sales** -
paid back out to the customers themselves for selling and recruiting. Roughly forty-three cents of
every core dollar returns to the distributor network as commission, and after SG&A of $337.4M what
was left was **$37.4M of operating earnings on $925.3M of sales, or 4.0%**. This is not a
product-margin business. It is a **recruitment-margin business**: the gross margin is high because
the distributor, not the company, carries the selling cost, and the distributor is then paid out of
that same gross margin. The economics live or die on the size of the network, and the network is
counted in the filing, in people.

Since December 2024 there is a **second business**: Hiya, a children's vitamin subscription sold
direct to consumers online, bought for **$206.1 million in cash** for a 78.85% controlling interest
(Note B, 10-K). That is a different animal - no distributors, no commissions, paid advertising to
acquire a subscriber, lower gross margin (the 10-K attributes the 280 basis point consolidated
gross-margin fall to Hiya's mix). Plus Rise (protein bars, retail) and Oola, both acquired 2022.
Two reportable segments and an "other".

**The scarce input this business controls.** There is none that the company controls. It does not
control the distributor: *"Our Brand Partners may terminate their services at any time and, like
most direct selling companies, we experience a high turnover among new active Customers from year
to year."* It does not control its largest market - China is **41.3% of net sales and 49.9% of core
active Customers**, conducted through BabyCare, under a regulatory regime Item 1A devotes pages to.
It does not control manufacture of nearly half its output - **third-party suppliers and
manufacturers accounted for approximately 44% of product sales in 2025.** The formulations, the
trademarks and the Salt Lake City plant are owned; none of them is scarce. **What the company
actually owns is a list of people who can leave on any day, and the right to pay them forty-three
cents of every dollar they bring in.**

**Will the fundamentals look broadly the same in ten years?** The mechanism will. Someone will sell
supplements to someone else on commission in 2036. Whether *this* network exists at the size that
supports this cost base is a different question, and it belongs at Q2 and Q4, not here. The business
is **relatively simple** in [E3-31]'s sense: two segments, one revenue identity, one cash-flow
statement, no financial leverage to speak of, no derivatives book, no float. There is no part of it
I cannot follow from the filing.

**The Hiya complication is real and does not close Q1.** A direct-to-consumer subscription vitamin
business is also simple. It is a second business bolted onto the first, and the 10-K reports it as a
separate segment with its own net sales, its own subscriber count (181,700 active Monthly Subscribers
at 2026-01-03) and its own goodwill. Two simple businesses reported separately is still
understandable; what the bolting-on does to the **earnings series** is a Q4 perimeter finding,
recorded there, and it is not used to duck the verdict here.

**VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

*Reason for IN, and its limit: the unit economics are legible from one page of the income statement
and one table of customer counts, and both are filed. [E4-46] governs the alternative - a business
that would take months of study is Q1 OUT and no fetch repairs it; this one took one filing.
Nothing in this verdict is a judgment about whether the business is good.*

## Q2 - IS IT A FRANCHISE? **[E3-03]**

**The three conditions, scored against the filing.**

| [E3-03] condition | verdict | evidence |
|---|---|---|
| (1) needed or desired | **passes** | 387,000 people bought in the last three months of FY2025; product returns are 0.8% of net sales (10-K) |
| (2) thought by its customers to have **no close substitute** | **FAILS** | the company's own words, below |
| (3) not subject to price regulation | **passes** | prices are set by the company; regulation here is of claims, labelling and the selling method, not price |

**Condition (2) fails on the registrant's own sentence.** From Item 1, "Competition", 10-K
accession `0000896264-26-000021`:

> "Our business through USANA, Hiya, and Rise is **very competitive and the barriers to entry
> are not significant.** We compete with manufacturers, distributors, and retailers of
> nutritional products in many channels, including global direct selling, direct-to-consumer,
> specialty retail stores, wholesale stores, e-commerce businesses such as Amazon, and the
> internet generally. We also compete with other public and privately owned direct sellers for
> distributor talent, including for example Amway, Herbalife, and Nu Skin. On both fronts,
> compared to USANA, Hiya, and Rise, **many of our competitors are significantly larger, have a
> longer operating history, higher visibility and name recognition, and greater financial
> resources.**"

That is a company telling its owners it has no moat, in the section of the annual report set
aside for saying so. **[E3-03]** requires all three conditions; one of them is denied by the
subject.

**And [E3-03]'s own demonstration test fails in both halves.** The row says the existence of the
three conditions *"will be demonstrated by a company's ability to **regularly price its product
or service aggressively and thereby to earn high rates of return on capital**."*

- **Pricing.** USANA did raise prices in FY2025 - the 10-K attributes part of the core gross-margin
  improvement to *"price increases"*, and average spend per active Customer rose **4.4%**. In the
  same year **active Customers fell 14.8%**. Under **[E2-44]**'s first characteristic - the ability
  to raise prices *"without fear of significant loss of either market share or unit volume"* - this
  is a fail, and it is the fail in its most legible form.
- **Returns on capital.** Computed from the filed series (see Q3's [E2-01] table): return on
  equity ran **28-33% every year from FY2010 to FY2021**, then **16.0% / 12.8% / 7.9% / 2.0%**.
  Operating margin ran **15.6% (FY2020) to 4.0% (FY2025)**. High returns were real and they are gone.

**[E4-55] - where units exist, monitor units. They exist here, the company publishes them, and
they are the whole story.** Munger's Precision Steel row is the template: *"In 2006, Precision
Steel's service center volume was 46 million pounds, down from 69 million pounds sold as recently
as 1999. This decline in physical volume is a serious reverse, not likely to disappear in some
'bounce back' effect. Nor do we expect another sharp rise in prices like the approximately 40%
rise that recently occurred, holding dollar volume roughly level despite a precipitous drop in
physical volume."*

**USANA's physical series, each figure read from the 10-K of that year:**

| fiscal year end | active Customers | source |
|---|---|---|
| 2016-12-31 | 471,000 *(then called "active Associates")* | 10-K FY2016 |
| 2017-12-30 | 565,000 | 10-K FY2017 |
| **2018-12-29** | **616,000 - the peak** | 10-K FY2018 |
| 2019-12-28 | 586,000 | 10-K FY2019 |
| 2021-01-02 | 599,000 | 10-K FY2020 |
| 2022-01-01 | 560,000 | 10-K FY2021 |
| 2022-12-31 | 490,000 | 10-K FY2022 |
| 2023-12-30 | 483,000 | 10-K FY2023 |
| 2024-12-28 | 454,000 | 10-K FY2025 comparative table |
| **2026-01-03** | **387,000** | 10-K FY2025, acc. `0000896264-26-000021` |
| 2026-07-04 | **384,000** | 10-Q, acc. `0000896264-26-000056` |

**616,000 to 387,000 is minus 37% in seven years**, and the decline is in every region without
exception: Greater China (15.4%), Southeast Asia Pacific (18.2%), North Asia (7.9%), Americas and
Europe (12.9%) in FY2025 alone. The 10-K's own forward-looking-statements list concedes it in the
first bullet: *"our core business ... has declined in net sales, net income and active Customers
over the last few years."* The consolidated **net sales line rose 8.3% in FY2025** - and it rose
only because $130.0 million of purchased Hiya revenue was added. **Dollar revenue flattered by an
acquisition and by price is precisely how [E4-55] says a shrinking franchise hides.**

**A second, independent statement of the same thing, from Item 1A** (same accession), found
after the verdict above was written and recorded here because it goes the same way:

> "Entry to market is **not particularly capital intensive or otherwise subject to high barriers**
> and as a result, **new competitors can enter easily and compete with us for customers and
> distributors, including our Brand Partners.** Our product offerings in each product category are
> also relatively small, compared to the wide variety of products offered by many of our
> competitors."

The registrant makes the no-moat statement twice, in two different Items, in the same annual
report.

---
### THE COMPETITOR ROW - required [E3-28]

**Specification, stated before the row was built:** every listed company whose primary business is
selling nutrition, wellness or weight-management product through a commissioned distributor or
coach network, measured on **(a) net sales and (b) operating margin, from its own
SEC-filed annual accounts, on the same calendar-year window FY2018-FY2025**, newest vintage. Source
for every cell: that company's own `companyfacts` US-GAAP annual facts drawn from its 10-K filings,
cross-read against the newest 10-K text for HLF, NUS, MED and NHTC.

**Net sales, $ millions, from each company's own 10-K:**

| Company | FY2018 | FY2021 | FY2023 | FY2025 | peak-to-FY2025 |
|---|---|---|---|---|---|
| **USANA (consolidated)** | 1,189.2 | 1,186.5 | 921.0 | **925.3** *(incl. $132.0 bought Hiya)* | **-22%** |
| **USANA (core nutritional only)** | 1,189.2 | ~1,186 | ~921 | **775.5** | **-35%** |
| Herbalife (HLF) | 4,891.8 | 5,802.8 | 5,062.4 | 5,037.5 | -13% |
| Nu Skin (NUS) | 2,679.0 | 2,695.7 | 1,969.1 | 1,485.2 | **-45%** |
| Medifast (MED) | 501.0 | 1,526.1 | 1,072.1 | 385.8 | **-76%** |
| Natural Health Trends (NHTC) | 191.9 | 60.0 | 43.9 | 39.8 | **-79%** |
| Mannatech (MTEX) | 173.6 | 159.8 | 132.0 | 108.0 | **-38%** |
| LifeVantage (LFVN, June FY) | 203.2 | 220.2 | 213.4 | 182.6 *(FY2026)* | **-21%** |
| BODi / Beachbody (BODI) | - | 873.6 | 527.1 | 251.7 | **-71%** |

**Operating margin, same source, same window:**

| Company | FY2018 | FY2021 | FY2023 | FY2025 |
|---|---|---|---|---|
| **USANA** | **15.8%** | **14.3%** | 10.1% | **4.0%** |
| Herbalife | 14.0% | 12.7% | 7.0% | 9.5% |
| Nu Skin | 9.0% | 8.7% | 2.5% | 4.4% |
| Medifast | 13.8% | 14.2% | 11.8% | **-3.7%** |
| Natural Health Trends | 17.6% | 2.6% | -3.8% | **-4.5%** |
| Mannatech | -0.1% | 5.7% | -0.7% | **-0.4%** |
| LifeVantage | 5.1% | 8.0% | 2.0% | 3.3% *(FY2026)* |
| BODi | - | -34.0% | -26.7% | 2.2% |

**Peers named: 7, from an industry with roughly a dozen participants of scale, of which the three
largest by revenue - Amway, Mary Kay and Melaleuca - are private and file nothing.** Buffett asks
for eight **[E3-28]**; seven were taken because seven is every listed one I could find that meets
the specification. **Three of the largest participants are unavailable**, which under the template
would normally hold the moat class PROVISIONAL and make the verdict UNRESEARCHED. **It does not
here, and the reason must be stated plainly: the missing companies could only make the case
worse.** Amway and Mary Kay are the named larger competitors in USANA's own Competition paragraph;
their absence removes evidence of *competitive pressure*, never evidence of a moat. A row that is
unanimous across seven filers, and whose three missing members are the ones cited against the
subject by the subject, does not become provisional by their absence. **The verdict below does not
rest on the row alone in any case** - it rests on [E3-03] condition (2) being denied in the
registrant's own words.

**What the row shows, and its limit [E3-61].** Seven of seven listed participants are smaller in
FY2025 than at their peak in the window; five of seven are down more than a third; three of seven
lost money at the operating line in FY2025. The unit series says the same at the peers, from their
own filings: Nu Skin's FY2025 10-K - *"Customers decreased 10%, Paid Affiliates decreased 11% and
Sales Leaders decreased 19% compared to the prior year"*; Natural Health Trends' - *"We had 14%
fewer active members at December 31, 2025 as compared to the end of 2024, and 5% fewer active
members at the end of 2024 as compared to the end of 2023 ... These losses in the number of active
members were a significant factor contributing to the decrease in our recent year-over-year
sales"*; Medifast's - *"The year-over-year decline in revenue was primarily driven by a decrease in
the number of active earning coaches."* **[E3-61]** caps what the row can prove - it shows position,
never conduct, and *"you'd have to know the people involved"* - so the row is used here for what it
can carry: **USANA's decline is not an execution failure peculiar to USANA.** That matters in
exactly one direction, and it is the wrong one for the owner: a franchise is a *relative* claim,
and being no worse than an industry that is collectively shrinking is the absence of a moat, not
the presence of one.

**USANA was the best operator in the row and that is now spent.** In FY2018 its 15.8% operating
margin led every listed peer. In FY2025 its 4.0% sits below Herbalife's 9.5% and barely above Nu
Skin's 4.4%. **[E4-32]** asks for the direction - *"we want the moat widened every year ... that
does not necessarily mean that the profit is more this year than last year"* - and the direction
here is negative on every filed measure the framework asks for: units, margin, return on capital,
and relative position within the row.

---
### THE REST OF THE Q2 TESTS

- **[E5-23] / [E4-04] - is the moat rebuilt or defended?** The question does not reach the ruling,
  because there is no moat to classify. For the record of the attempt: the distributor network must
  be *replaced*, not merely defended - the 10-K says *"we experience a high turnover among new
  active Customers from year to year"*, and the company spent FY2025 rolling out an *"enhanced Brand
  Partner Compensation Plan"* to re-buy the network's loyalty, which is the paying-for-a-replacement
  case, not the defending-the-same-trademark case. Recorded, not relied on.
- **[E4-36] - which of the four causes of extreme success produced the record?** USANA's 2010-2021
  record of 28-33% returns on equity was real. Read against [E4-36]'s list it is the fourth kind -
  *"Catching and riding some sort of big wave"* - and **[E3-51]** names what happens next: *"when a
  surfer gets up and catches the wave and just stays there, he can go a long, long time. But if he
  gets off the wave, he becomes mired in shallows."* The wave was the two-decade expansion of
  network-marketed supplements, most of all in China. **The competitor row is the evidence that it
  is the wave and not the surfer**, because all seven surfers came off it within the same four years.
  A surfing run is not a moat; the advantage lived in the wave.
- **[E2-45] - the attacker's test.** With ample capital and skilled personnel, competing with USANA
  requires: a contract manufacturer (USANA itself uses third parties for 44% of product sales), a
  commission schedule more generous than 43%, and a website. The company states the barrier itself
  and states that it is *"not significant"*. Compare *"I'd rather wrestle grizzlies than compete
  with Mrs. B and her progeny"* - this is the opposite pole.
- **[E3-33] / [E5-28] - untapped pricing power?** No. The pricing power was tapped in FY2025 and the
  customer count fell 14.8% in the same year. **[E5-28]** scopes the class - *"If you name some
  business that has incredible pricing power, you're talking about a business that's a monopoly or
  a near monopoly"* - and a company that names Amway, Herbalife and Nu Skin as larger rivals in its
  own Competition paragraph is not claiming near-monopoly. **[E4-37]**'s inverse metric points the
  same way: the measure of a business is *"the agony they go through in determining whether a price
  increase can be sustained"*, and the filed evidence of the agony is the simultaneous compensation-plan
  rebuild, the Q4 FY2025 cost realignment and the 14.8% unit loss.
- **[E2-53] - the dominance class?** Not applicable. USANA is not dominant in any channel it names;
  it is, by its own account, smaller than several rivals in the one channel it was built for.
- **[E3-46] - the second question, and it is a number.** *"the best businesses, by definition, are
  going to be businesses that earn very high returns on capital employed over time."* Over the last
  four filed years: 16.0%, 12.8%, 7.9%, 2.0% on equity. Not this one, not now.
- **[E3-43] - so what class is it?** *"'a business' earns exceptional profits only if it is the
  low-cost operator or if supply of its product or service is tight."* Supply of nutritional
  supplements is not tight. USANA is not the low-cost operator - it manufactures in Utah and pays
  43% of core revenue in commissions, against competitors with *"greater financial resources"*. It
  is **"a business"** in [E3-43]'s sense, and the row's last sentence is the one that binds:
  *"a business, unlike a franchise, can be killed by poor management."*

- Class: [ ] WIDE [ ] NARROW [x] **NONE** [ ] PROVISIONAL - Direction: **narrowing on every filed
  measure - units, margin, return on capital, and rank within the competitor row**
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**Why OUT and not UNKNOWABLE.** The [E4-04] ruling of 2026-09-20 sends to **UNKNOWABLE at Q2** a
name that *passes* [E3-03] and whose durability cannot be judged from filings - the perimeter
close. **This name does not pass [E3-03].** Condition (2) is denied by the registrant in its own
Competition paragraph, and the row's demonstration test - aggressive pricing producing high
returns on capital - fails in both halves on filed figures. That is *"the evidence is here and the
business fails"*, which is the definition of OUT. **[E4-19]**'s separating question was asked
aloud: *can I name the document that would resolve this?* There is no document that would; the
documents are in, and they say what they say.

**STOP. Operator rule 2: the run closes here.** Q3 through Q6 below are **RECORDED, NOT
GOVERNING** - no verdict box is ticked in any of them, and nothing in them may be read as a
verdict about this company.

---
## Q3 - ARE THEY HONEST, AND ARE THEY RATIONAL?
### RECORDED, NOT GOVERNING - the file closed at Q2. No verdict box is ticked.
*Operator rule 2: UNRESEARCHED and UNKNOWABLE both close a file and neither is a pass; an OUT
closes it permanently. What follows was gathered before and during Q2 and is written down because
the operator asked for the proxy, the 8-K EX-99.1s and the ownership question to be worked. None
of it is a verdict, and none of it may be cited as one.*

**The weight case, declared as the template requires.** Daily execution: **HIGH** - **[E3-38]**'s
have-to-be-smart-every-day class, and **[E3-43]** classifies this filer as *"a business"*, which
*"can be killed by poor management."* Control: no (public minority). Leverage: no - $0 drawn on
the credit facility at 2026-07-04. **One determinant high, so Q3 would have been a binary gate had
the file reached it.** It did not reach it.

**Ownership and control.** DEF 14A, accession `0000896264-26-000026`, beneficial ownership table:
**Gull Global, Ltd. holds 7,408,345 shares, 40.1%** - the 10-K adds that it is *"an entity that is
solely owned and controlled by our founder, Dr. Myron Wentz"*, who *"is no longer active in the
management of USANA and is an emeritus member of our Board of Directors"*, and that the holding
*"could also have the effect of delaying, deterring, or preventing a change in control that might
otherwise be beneficial to shareholders."* The next three holders are index and quant funds
(Renaissance 6.2%, Pzena 6.1%, Vanguard 5.1%). **Every named executive officer and director
combined holds well under 1%**: the current CEO 47,067 shares, the CFO 6,754, the COO 9,256, the
former CEO 17,453. **Control sits with a founder who no longer runs the business and does not sit
on the operating side; the operators own almost none of it.** Recorded; not scored.

**The primary test [E2-01] - the earnings rate on equity capital employed, multi-year, and it is
the collapse.** Computed from the filed statements, newest vintage:

| FY end | operating margin | return on equity | cash taxes / pretax |
|---|---|---|---|
| 2018-12-29 | 15.8% | 32.3% | 36.9% |
| 2019-12-28 | 13.8% | 28.6% | 36.5% |
| 2021-01-02 | 15.6% | 28.2% | 29.8% |
| 2022-01-01 | 14.3% | 29.5% | 34.9% |
| 2022-12-31 | 10.8% | 16.0% | 42.2% |
| 2023-12-30 | 10.1% | 12.8% | 41.3% |
| 2024-12-28 | 7.8% | 7.9% | 52.9% |
| 2026-01-03 | **4.0%** | **2.0%** | **89.5%** |

**The [E4-30] cash-tax tell does NOT fire, and the honest record is that it fires the other way.**
The corpus's fraud tell is *cash taxes falling as a share of reported pretax income*. Here cash
taxes **rise** to 89.5% of pretax, and the filing gives the reason: an effective book rate of
72.4% caused by *"an unfavorable shift in the jurisdictional mix ... such that losses generated in
certain markets are not producing a corresponding income tax benefit"*, with the deferred-tax
valuation allowance built from $156.1M to **$178.7M** in FY2025 (Schedule II). That is a company
whose profitable jurisdictions are taxed while its losing ones get no relief - an economic
deterioration, not a disclosure one. **A test that does not fire is recorded as not firing.**

**[E4-29] and [E4-22]'s third flag, scored against the 8-K EX-99.1 earnings releases and not only
the 10-K - standing for every Q3 since the CGNX run. Both fire, and hard.**

The word EBITDA appears 20 times in the Q4/FY2025 release (acc. `0000896264-26-000014`), 17 times
in Q1 2026 (acc. `0000896264-26-000030`) and 15 times in Q2 2026 (acc. `0000896264-26-000050`).
**Adjusted EBITDA and Adjusted diluted EPS are headline lines in the Key Financial and Operating
Results table at the top of every one**, beside GAAP. The FY2025 spread:

| FY2025 headline | GAAP | the promoted figure |
|---|---|---|
| net earnings / Adjusted EBITDA | **$10.8M** | **$101.3M** |
| diluted EPS / Adjusted diluted EPS | **$0.58** | **$1.93** |

**[E4-29]**: *"Trumpeting EBITDA ... is a particularly pernicious practice. Doing so implies that
depreciation is not truly an expense, given that it is a 'non-cash' charge. That's nonsense."*
FY2025 D&A was **$32,562 thousand** - the largest single item deleted, and most of it is
amortisation of the intangibles bought with the shareholders' $206.1 million. **[E5-41]**'s
reverse-float reading applies exactly: the money was already spent, in cash, in December 2024.

**And the measure is not merely promotional here - it is contractual.** Note O: the price USANA
must pay for the remaining 21.15% of Hiya under the Put Right *"is based on Hiya's **Adjusted
EBITDA** (as defined in the LLC Agreement) for the calendar year immediately prior to the year in
which such right is exercised, multiplied by the Company Value Reference Amount."* A non-GAAP
measure sets a real cash obligation.

**The projections flag [E4-22], and [E3-48]'s prescribed action performed on the record.**
[E3-48] says pull the company's own past guidance and set it against outturn. Fiscal 2026 guidance,
three dated points from the furnished releases:

| metric | issued 2026-02-17 | reaffirmed 2026-05-05 | **cut 2026-08-04** |
|---|---|---|---|
| consolidated net sales | $925M - $1.0bn *(flat to +8%)* | reaffirmed *"across all metrics"* | **$910M** |
| net earnings | **$20.3M - $26.6M** | reaffirmed | **$(11)M** |
| diluted EPS | $1.11 - $1.45 | reaffirmed | **$(0.61)** |
| Adjusted diluted EPS | $1.95 - $2.29 | reaffirmed | **$0.76** |
| Rise Wellness net sales | $65M - $80M | reaffirmed | **$35M** |
| Hiya net sales | $140M - $155M | reaffirmed | **$125M** |

**A profit forecast of +$20M to +$27M became a loss of $(11)M in under six months, and was
reaffirmed in full at the halfway point.** [E5-30] is the reason this is not just a bad quarter:
*"once you start it, it's all over. You can't quit ... And forecasting earnings, I can't imagine
anything more destructive."* Recorded, not scored.

**[E3-53] and [E5-33] - the restructuring charge.** FY2025 carried a **$6,463 thousand "Cost
realignment"** charge on its own income-statement line, *"primarily related to employee
severance"*, plus a **$6,967 impairment** line; Q2 2026 added a **$29,137 goodwill impairment** of
the Hiya reporting unit. **[E5-33]** governs the treatment: these are real costs and they belong in
the owner-earnings mean - *"to tell owners year after year, 'Don't count this' ... is misleading."*
The Adjusted diluted EPS bridge excludes them. **Note the timing**: $29.1M of the $127.3M of Hiya
goodwill was written off **eighteen months after the acquisition closed**, on *"current
lower-than-expected financial performance and changes in the near-term forecast."*

**[E5-08] and [E5-24] - the buyback conditions, and this is the sharpest allocation finding in the
file.** Repurchases, from the filed cash-flow statements:

| FY | repurchases | approximate price context |
|---|---|---|
| 2021-01-02 | $57.0M | |
| **2022-01-01** | **$177.8M** | the year the shares closed at **$101.20** |
| 2022-12-31 | $25.4M | |
| 2023-12-30 | $11.6M | |
| 2024-12-28 | $9.4M | |
| **2026-01-03** | **$27.5M** | 927,000 shares retired for $27,738 thousand = **$29.92 a share** |

**$281.7 million of stock was bought back in six years. The whole company is now worth $266.1
million.** The FY2025 tranche was struck at $29.92 in the same fiscal year that active Customers
fell 14.8%; the shares are $14.40 today - a **52% loss inside twelve months**. **[E5-24]**: *"what
is smart at one price is dumb at another."* Condition (1) of **[E5-08]** was met - ample funds.
Condition (2) - *"selling at a material discount to the company's intrinsic business value,
conservatively calculated"* - was not, on the company's own subsequent disclosure. **[E4-13]**'s
humility clause is stated as the framework requires: this rests on our range and *"it is natural
for CEOs to be optimistic about their own businesses. They also know a whole lot more about them
than I do"* - and **[E5-08]** itself allows that *"many CEOs never stop believing their stock is
cheap."* **The flag binds position size, never the discount rate** - and there is no position.

**[E3-54] - the retention test, five-year rolling: at least $1 of market value per $1 retained.**
No dividend has ever been paid (`PaymentsOfDividendsCommonStock` resolves to nothing in any year).
Net earnings attributable to USANA, FY2021 through FY2025: **$116.5 + $69.3 + $63.8 + $42.0 + $10.8
= $302.4 million**. Over the same five years the market value went from roughly **$1.94 billion**
(19.2M shares at the 2021-12-31 close of $101.20) to **$266.1 million**. **The test fails by more
than a billion and a half dollars; every dollar retained or spent produced negative market value.**
Recorded with **[E2-56]**'s caution about blended series and with [E4-13]'s clause; it is an
observation about outcome, not a finding about a person.

**[E2-30] - the institutional imperative, scored as the template asks.** Not a fraud test:
*"Institutional dynamics, not venality or stupidity."*
- (2) **acquisitions materialising to soak up available funds: FIRES.** Cash stood at $330.4M at
  FY2023 year end and $206.1M of it went into Hiya in December 2024, into a channel the company had
  no prior experience of, and $29.1M of the goodwill was written off eighteen months later.
- (4) **peer behaviour mindlessly imitated: FIRES on the filed record.** Herbalife ran a
  "Transformation Program" (2021-2024) and then a "Restructuring Program" (2024-2025), per its own
  10-K; Nu Skin, Medifast and BODi have each restructured in the window; USANA's Q4 FY2025 "cost
  realignment" is the same move at the same point in the same cycle.
- (1) resistance to change and (3) staff studies justifying a craving: **not established from the
  filings.** The opposite of (1) is arguably visible - the company changed channel, changed the
  compensation plan and changed CEO. Recorded as not established rather than as clean.

**Management turnover, from the proxy.** Kevin Guest was CEO from November 2016, became Executive
Chairman on 2023-07-01 when Jim H. Brown succeeded him, and **on 2026-01-08 Mr Brown stepped down
and Mr Guest reassumed the CEO role while remaining Chairman.** The Board re-combined the Chairman
and CEO functions at the same time. A 2.5-year CEO tenure ending mid-strategy, with the predecessor
returning, is a fact; **[E3-61]** is the limit on reading conduct from structure, and it is applied.

**The honesty binary [E5-16].** **No integrity finding of any kind was made.** No restatement, no
late filing, no auditor change (KPMG, Auditor Firm ID 185, stands), no SEC enforcement matter found
in the filings read, no related-party dealing disclosed beyond the founder's passive holding.
**[E5-17]** caps the whole exercise - *"People are not that easy to read. Sincerity and empathy can
easily be faked"* - and a Q3 pass would in any case have been *"the absence of found disqualifiers,
not a finding that the managers are honest."* **No verdict is written here.**

**THE GUARDRAIL, checked as the template requires.** Nothing in this section is used to promote or
to demote the name. **[E2-37]**, **[E2-38]** and **[E3-39]** govern: *"a good managerial record ...
is far more a function of what business boat you get into than it is of how effectively you row."*
The boat is the finding; the rowing is not. **[E5-18]** is the fair reading of the operators here -
the business would not stand a little mismanagement, which is a fact about the business, and it was
recorded at Q2 where it belongs.

- **VERDICT: NOT TAKEN. The file closed at Q2.** No box ticked.

---
## Q4 - WILL IT SURVIVE?
### RECORDED, NOT GOVERNING - the file closed at Q2. No verdict box is ticked.

### THE PERIMETER - what the screen's $210M acquisition note actually is

The screen said *"acquisitions are $210M, 80% of cap, inside the window - the numerator and
denominator may be different companies."* **Established from the filings, and it is two events,
not one:**

| event | closed | consideration | what it is |
|---|---|---|---|
| **Rise (and Oola)** | during FY2022 | **$6,532 thousand**, `Payments to acquire businesses`, FY2022 cash-flow statement | protein bars and drinks, sold through retail; a personal-development direct seller |
| **Hiya Health Products, LLC** | **2024-12-23** | **$206,074 thousand cash** for **78.85%**, final after the working-capital adjustment (Note B, 10-K acc. `0000896264-26-000021`) | children's chewable vitamins, direct-to-consumer subscription |

**$209.9 million in total - the screen's $210M is right, and it is 78.9% of the re-struck $266.1M
cap.** The Hiya purchase price allocation: identifiable net assets $132,980, of which **intangibles
$124,200**; redeemable non-controlling interest $54,170; **goodwill $127,264**. Almost the entire
purchase was intangibles and goodwill.

**The perimeter breaks in the owner-earnings series, counted:**
1. **FY2022** - Rise and Oola. Immaterial: $6.5M of consideration against $103.9M of operating cash
   that year. **Not a break in substance.**
2. **FY2025 (year ended 2026-01-03)** - **a real break.** It is the first full year of Hiya:
   $131,971 of net sales added, 14.3% of consolidated, with no Brand Partner incentives, lower
   gross margin, and the amortisation of $124.2M of acquired intangibles running through SG&A. The
   D&A line more than doubles, **$14,539 to $32,562**, almost entirely on that account.
3. **FY2025 is also a 53-week year** (2024-12-29 to 2026-01-03), which the 10-K names as a
   contributor to the core net-sales comparison. A third, smaller discontinuity in the same year.

**So the numerator and the denominator are the same company - the cap and the newest year both
include Hiya - but the SERIES spans a perimeter break at 2024-12-23 and only at that date.** Every
year before FY2025 is the core direct-selling business plus a rounding error. **[E4-25]** is the
governing instruction and it is followed below: run more than one window and carry the spread.

### THE SPREAD, REBUILT ACROSS EVERY WINDOW THE FILINGS SUPPORT

The screen's `spread_caveat` said the width was *"4-construction width only (3y/5y x two capex
ends): CANNOT see variation older than the 5-year window; rebuild it [E4-25]."* **Rebuilt.** The
filed history reaches back to FY2009 in `companyfacts` from the filer's own 10-Ks - **seventeen
annual periods**. Construction is the framework's confessed convention: **owner earnings = operating
cash flow, less share-based compensation in full [E5-06], less the (c) guess**, with (c) run at both
ends of its band - the **D&A default [E3-44, E2-41]** and **total capex**.

**Owner earnings by year, $ millions** *(OCF, SBC, D&A and capex all from each year's own filed
cash-flow statement; FY2025's four figures cross-checked against the filed statement in Step 0)*:

| FY end | OCF | SBC | D&A | capex | **OE, (c)=D&A** | **OE, (c)=capex** |
|---|---|---|---|---|---|---|
| 2010-01-02 | 32.5 | 8.9 | 7.1 | 4.1 | 16.5 | 19.5 |
| 2011-01-01 | 66.1 | 10.4 | 7.9 | 4.2 | 47.8 | 51.5 |
| 2011-12-31 | 70.1 | 10.5 | 8.5 | 10.6 | 51.1 | 49.0 |
| 2012-12-29 | 92.8 | 10.2 | 8.8 | 8.4 | 73.8 | 74.2 |
| 2013-12-28 | 98.9 | 7.6 | 9.0 | 8.1 | 82.3 | 83.2 |
| 2015-01-03 | 105.2 | 9.8 | 8.8 | 20.4 | 86.6 | 75.0 |
| 2016-01-02 | 111.5 | 11.1 | 10.0 | 23.7 | 90.4 | 76.7 |
| 2016-12-31 | 136.9 | 16.5 | 13.5 | 32.7 | 106.9 | 87.7 |
| 2017-12-30 | 123.8 | 15.5 | 16.1 | 13.2 | 92.2 | 95.1 |
| 2018-12-29 | 152.1 | 15.0 | 16.8 | 11.4 | 120.3 | 125.7 |
| 2019-12-28 | 126.7 | 15.5 | 14.7 | 16.6 | 96.5 | 94.6 |
| **2021-01-02** | 160.4 | 14.4 | 13.7 | 15.1 | **132.3** | **130.9 - the peak** |
| 2022-01-01 | 121.2 | 14.3 | 13.0 | 12.8 | 93.9 | 94.1 |
| 2022-12-31 | 103.9 | 13.3 | 13.4 | 10.4 | 77.2 | 80.2 |
| 2023-12-30 | 70.6 | 14.6 | 12.7 | 14.5 | 43.3 | 41.5 |
| 2024-12-28 | 61.0 | 14.6 | 14.5 | 10.1 | 31.9 | 36.3 |
| **2026-01-03** | 22.3 | 13.8 | 32.6 | 13.8 | **-24.1** | **-5.3** |

**Every window ending FY2025, both (c) ends, against the re-struck $266.1M cap:**

| window | OE range, $M | implied yield |
|---|---|---|
| 3-year | 17.0 - 24.2 | 6.40% - 9.08% |
| 4-year | 32.1 - 38.2 | 12.05% - 14.35% |
| **5-year (the corpus default [E2-42, E1-03])** | **44.4 - 49.4** | **16.70% - 18.55%** |
| 6-year | 59.1 - 62.9 | 22.20% - 23.66% |
| 7-year | 64.4 - 67.5 | 24.21% - 25.36% |
| 8-year | 71.4 - 74.8 | 26.84% - 28.09% |
| 10-year | 77.0 - 78.1 | 28.95% - 29.34% |
| 12-year | 77.7 - 79.0 | 29.20% - 29.67% |
| 15-year | 75.9 - 77.0 | 28.53% - 28.93% |
| 17-year (all filed history) | 71.2 - 71.7 | 26.75% - 26.94% |

**THE FULL REBUILT RANGE: $17.0 million to $79.0 million of owner earnings - a 4.6-fold spread -
which is 6.40% to 29.67% on the re-struck cap.** The screen's reported width, built on 3-year and
5-year windows only, was $17M to $49M. **The rebuild widens the top end by 61%**, exactly as
[E4-25] predicted it would: *"CANNOT see variation older than the 5-year window."*

**[E4-25] answers its own question here**: *"Usually, the range must be so wide that no useful
conclusion can be reached."* A range whose top end is 4.6 times its bottom end is that range. **And
[E4-38] forbids resolving it by choosing a window** - *"growth-rate presentations can be
significantly distorted by a calculated selection of either initial or terminal dates"* - so every
window is published above, which is the corpus's own remedy.

### WHERE THE LEVEL STEP FALLS - and the screen mis-specified its shape

The screen carried three step findings: `level_shift` 0.39 on operating cash, `level_shift_oe` 0.23
on owner earnings, `level_shift_full` 0.48, each captioned *"STEP DOWN - the series has changed
level."* **The ratios are right and the word STEP is wrong.** A step implies a level change at a
date. What the filings show is a **slide, running six consecutive years, in every measure at once:**

| FY end | active Customers | net sales | operating margin | OCF | OE (capex end) |
|---|---|---|---|---|---|
| 2021-01-02 | 599,000 | 1,134.6 | 15.6% | 160.4 | 130.9 |
| 2022-01-01 | 560,000 | 1,186.5 | 14.3% | 121.2 | 94.1 |
| 2022-12-31 | 490,000 | 998.6 | 10.8% | 103.9 | 80.2 |
| 2023-12-30 | 483,000 | 921.0 | 10.1% | 70.6 | 41.5 |
| 2024-12-28 | 454,000 | 854.5 | 7.8% | 61.0 | 36.3 |
| 2026-01-03 | 387,000 | 925.3 *(incl. bought Hiya)* | 4.0% | 22.3 | -5.3 |

The rolling five-year owner-earnings mean, which is how the framework would read it, falls in every
single anchor: **$108M (to FY2021) → $105M → $89M → $77M → $44M.** No two consecutive windows agree,
and the direction never reverses.

**If a date must be named, there are two hinges, and the filings give a reason for each:**
1. **FY2022** - net sales -15.8%, units -12.5%, operating margin 14.3% to 10.8%. The end of the
   pandemic-era surge in at-home supplement buying and in virtual recruitment, with China leading
   down. FY2021 was the all-time high in both revenue and owner earnings.
2. **FY2025** - units -14.8%, operating margin 7.8% to 4.0%, OCF -63%. **Four distinct causes, all
   in one year**: continued unit erosion; the first full year of Hiya (lower margin plus $18M of
   incremental D&A, mostly acquired-intangible amortisation); the $6.5M cost realignment and the
   $7.0M impairment; and a **72.4% effective tax rate** from foreign losses that generate no benefit.
   On top of that, operating cash absorbed a **$34,685 thousand inventory build**.

**The consequence for the mean, stated plainly.** A mean taken across FY2010-FY2025 describes a
business that no longer exists: 599,000 customers, 15.6% margins, $130M of owner earnings. A mean
taken across FY2023-FY2025 describes one that earns $17-24M. **These are not two estimates of one
number. They are one number for each of two businesses**, and [E4-25]'s verdict - that no useful
conclusion can be reached - is the honest report, not a failure of effort.

### MAINTENANCE CAPEX - the (c) judgment, disclosed [E2-23, E3-44, E2-41, E5-20]

- **Does the company publish its own maintenance-capital figure? [E5-20] asks first.** **No.**
  The MD&A, the liquidity section and the contractual-obligations table were read; capital
  expenditure is discussed only in total. Under **[E2-09]** and **[E3-44]**, (c) is therefore a
  **disclosed guess** and never a substitute number - PRIME RULE 3's clause of 2026-09-20 forbids a
  CONVENTION label licensing what operator rule 5 bans, and no net-income proxy is used anywhere in
  this file.
- **Which [E5-20] class is this?** **Not the capital-intensive class.** Capex has run $10-33M a year
  against $855M-$1,189M of revenue - roughly 1.1% to 3.3% of sales - in a business whose assets are
  one Utah manufacturing plant, distribution centres and IT. The railroad/airline exception does not
  apply and the **D&A default [E3-44, E2-41] is legitimate here**, so both ends of the band stand.
- **But the D&A end is distorted upward from FY2025 onward and the direction must be stated.** D&A
  more than doubled to $32,562 because of the amortisation of $124.2M of Hiya intangibles. **That is
  not a renewal cost**; it is the accounting unwind of a price already paid in cash in December 2024.
  Using it as (c) charges the business twice for one outlay. It happens to be the **conservative**
  end, so using it understates rather than overstates owner earnings, which is the safe direction
  when the question is whether to buy - **but it is not the right number, and the run says so
  rather than letting the band pretend to two equally legitimate answers.**
- **The working-capital increment [E2-23] constraint 3.** Operating cash is used precisely because
  it nets the working-capital change from one audited line. FY2025's OCF of $22,349 is after a
  **$34,685 inventory build** and a **$14,218 reduction in other liabilities**; H1 2026 reversed
  $9,421 of the inventory. Recorded so a reader can see it, not adjusted out - taking it out would
  be spending conservatism in the wrong direction.
- **Stock compensation subtracted in full [E5-06]**: $13,828 in FY2025, $14.6M and $14.6M before
  that. SBC has run 13-14% of a shrinking operating cash flow and **62% of FY2025's**. **[E3-70]**
  notes the reported charge is the floor of the correct subtraction, not the measure; no grant-date
  total resolves undimensioned here, which is the known source limit recorded in the resume state,
  so the charge is used and the understatement is flagged.

### GREAT, GOOD, OR GRUESOME? **[E4-20]**

- [ ] great  [ ] good  [x] **it is none of the three as the test is written, and the reason matters**

[E4-20]'s three savings accounts all assume a business that is *adding* deposits. This one is
**shrinking and buying its growth**: capital went out at $206.1M for Hiya and $281.7M for its own
stock over six years, and the interest rate on the remaining account went from 28% on equity to
2.0%. It is not *gruesome* in [E4-20]'s literal sense - gruesome *"grows rapidly, requires
significant capital to engender the growth, and then earns little or no money"*, and USANA is not
growing. **[E4-43]** warns against over-reading the test, so it is not over-read: the honest label
is **a shrinking former-great**, and the shrinkage is in units, which is the series [E4-55] says to
trust.

### STAYING POWER - all three, from the 10-Q balance sheet at 2026-07-04 **[E5-11]**

1. **A large and reliable stream of earnings: FAILS ON RELIABLE, not on large.** Operating cash of
   $22.3M in FY2025 against $160.4M five years earlier; $33.1M in H1 2026 against $27.7M in H1 2025,
   so the half-year is up. Six consecutive years of decline is the record.
2. **Massive liquid assets: PASSES, and it is the strongest fact in the file.** **Cash and cash
   equivalents $168,560 thousand** at 2026-07-04 - **63% of the entire $266.1 million market cap** -
   against total liabilities of $132,237 and **zero drawn on the credit facility** ($14,000 at
   FY2025 year end, repaid). Equity attributable to USANA $526,306.
3. **No significant near-term cash requirements: PASSES, with one named item.** No debt, no
   maturities, no dividend. The one obligation is the **Hiya Put Right** (Note O): the holders of the
   21.15% may put **half** of it from **2028-04-30** and the rest from **2030-04-30**, priced on
   Hiya's Adjusted EBITDA times a contractual reference amount. It is carried in the mezzanine at
   **$44,667 thousand** at 2026-07-04, down from $53,168 - and the direction is the point: a
   deteriorating Hiya **reduces** the obligation, so the liability shrinks with the asset. It is not
   due for nineteen months and it is not a covenant. **[E3-52]** is the right reading - a liability
   with no covenant and a long date is a different animal from bank debt due next year.
- **Leverage, named and quantified [E4-16, E3-29]:** **none.** $0 drawn; $663 thousand of interest
  paid in all of FY2025. The framework supplies no ratio ceiling and none is needed.
- **[E2-55]**'s design principle - *"acceptable long-term results under extraordinarily adverse
  conditions"* - is met on the balance sheet and not on the earnings.

### THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**

**Model exposure, not experience [E4-40].** The benign fact - $168.6M of cash and no debt - is the
useless guide; the exposure is the compounding of the network.

**The mechanism.** A direct-selling network is a recruiting machine whose output is its own input.
Brand Partner incentives are 43.3% of core net sales, so a Partner's income is a fixed share of the
volume they and their downline generate. When the network shrinks, the top of it earns less; when
the top earns less, the business opportunity is less attractive to recruit into; the enhanced
Compensation Plan of Q3 2025 is the filed evidence that the company knows this and is paying to
arrest it. Meanwhile the fixed cost base - a Utah manufacturing plant, 25 country organisations, IT
- does not shrink at the same rate, which is what turned a 14.8% unit decline into a 49% fall in
operating earnings and a 63% fall in operating cash in one year.

**Quantified from filed figures.** Core nutritional net sales were $775.5M in FY2025 with a
consolidated operating margin of 4.0%, or $37.4M. Hold everything else and run the company's own
FY2026 core guidance of a 0-5% decline forward. Core net sales at a continued **8% annual decline**
reach roughly **$655M by FY2028**; at the FY2025 gross margin, and with SG&A shrinking only half as
fast as revenue - which is what the filed FY2025 experience shows, core SG&A fell 2.5% on an 8.3%
sales fall - **consolidated operating earnings cross zero somewhere between FY2027 and FY2028.**
Against that: $168.6M of cash, no debt, and $33.1M of operating cash in H1 2026, so **the company
does not run out of money; it runs out of profit.** The death is not insolvency. It is the arrival
at a point where the business is worth its net cash and nothing more.

**Likelihood: [x] a real possibility.** Not *likely*, because H1 2026 operating cash was up
year-on-year and the balance sheet is unencumbered; not *a low-level possibility*, because six
consecutive years of decline, a 37% fall in units, a cut-in-half guidance and seven of seven peers
pointing the same way are not a cycle that has shown any sign of turning. **[E4-51]**'s prescription
- state the arguments against your position better than the people in opposition - requires the
counter-case in writing, and it is: **$168.6M of cash inside a $266.1M cap, no debt, positive and
rising half-year operating cash, a founder-controlled register unlikely to sell into weakness, and
a core business the company guides to only a 0-5% decline in FY2026.** That case is real. It is a
**balance-sheet case, not a franchise case**, and Q2 is where this file closed.

- **VERDICT: NOT TAKEN. The file closed at Q2.** No box ticked.

---
## Q5 - WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?
# COMPUTATION — NOT A CLEARANCE
### RECORDED, NOT GOVERNING. Operator rules 2 and 3.
*Q5 did not open and cannot open: Q2 returned OUT. The arithmetic below is published only so the
operator can see what the re-struck cap does to the screen's yield, and it carries **no entry
language**. Nothing here is a verdict, a ranking or a recommendation.*

- Owner earnings, **full rebuilt range across all seventeen filed years and both (c) ends**:
  **$17.0M to $79.0M**
- Market cap, re-struck by hand: **$266.1M** (18,476,534 shares at $14.40, 2026-09-21)
- **Implied yield range: 6.40% to 29.67%**, against a **5.34% USD sovereign** (US Treasury daily par
  yield curve, 2026-09-18)
- Five-year window, the corpus default **[E2-42]**: **16.70% to 18.55%**
- Three-year window, the business as it is now: **6.40% to 9.08%** - **below the ~10% floor
  [E4-28]** at both ends
- Newest single year, FY2025: owner earnings **negative at both (c) ends**, $(24.1)M to $(5.3)M

**What this shows and what it cannot.** The whole disagreement between "cheap" and "not cheap" is
the disagreement about which business is being bought, and [E4-25] says that width **is** the
answer: *"Usually, the range must be so wide that no useful conclusion can be reached."* A name
whose honest owner-earnings range spans 4.6-fold, and whose newest filed year is negative, is not
ranked and not quit-on - **it never reached the floor test at all, because the business gate
closed first.** **[E5-42]** is the ordering that makes this correct: business quality is judged at
Q2-Q4, *"whether it's a good investment for us depends on how much we pay for that in the end"* -
and the price question is never reached when the business question has answered.

- **VERDICT: NOT TAKEN - Q5 DID NOT OPEN.** No box ticked.

## Q6 - WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
### RECORDED, NOT GOVERNING - there is no position and no entry, so there is no exit to pre-commit.

**[E1-02]** requires the yardstick *"prior to the act"*, and there is no act. What is recorded
instead is **the reversal condition in words** - the QLYS ruling of 2026-09-07 bars a price alert on
a name that failed on the business, and this one failed on the business.

**What would reopen this file** - all three would have to be true together, because any one alone
is noise:
1. **The unit series turns.** Active Customers rising year-on-year for **four consecutive
   quarters**, not average spend, not dollars, not constant currency - the count, which the company
   publishes every quarter. It was 616,000 at FY2018, 387,000 at FY2025 and 384,000 at 2026-07-04.
2. **The competitor row stops being unanimous.** At least two of Herbalife, Nu Skin, Medifast,
   Mannatech, LifeVantage, NHTC and BODi growing units and revenue in the same window - which would
   be the first evidence in this file that the wave **[E3-51]** has not simply broken.
3. **A statement in a filed 10-K that contradicts the two in the FY2025 one** - that barriers to
   entry *are* significant, or that the products are thought to have no close substitute. **[E3-03]**
   condition (2) was denied by the registrant; only the registrant's own filing can undeny it.

**No band is armed in `tools/alerts.json` and no `PORTFOLIO.md` row is written**, per fold step 4
and the QLYS ruling. A price alert on a business-gate failure is a category error: the price is not
the thing that was wrong.

- **VERDICT: NOT TAKEN. The file closed at Q2.** No box ticked.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **The run stopped at the first non-IN
      verdict (Q2 OUT) and Q3-Q6 carry no verdict boxes.**
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the only IN.
- [x] Every UNRESEARCHED verdict names the artifact - **none was returned.**
- [x] Every UNKNOWABLE verdict states what cannot be known - **none was returned.**
- [x] Step 0: the filing was read, with accession numbers; four figures were cross-checked against
      the filed cash-flow statement and two against the filed income statement.
- [x] Owner earnings on a multi-year mean; **every window from 3 to 17 years published [E4-38]**;
      capex band disclosed as a judgment with the [E5-20] class named and the D&A distortion stated.
      **No net-income proxy anywhere** (operator rule 5, PRIME RULE 3).
- [x] Competitor row filled - **7 listed peers, same metric, same window, each from its own
      SEC-filed accounts**; the three private participants named and their absence reasoned about
      rather than papered over.
- [x] Sovereign is for the reporting currency, from the issuing authority, dated; **the
      earnings-currency mismatch is disclosed in Step 0 as a limit of this run.**
- [x] No value range was stated, because Q5 did not open. The computation carries its rule-3 heading.
- [x] One bar chosen: **neither** - no bar applies to a file closed at Q2. **Windage count: zero.**
      No conservatism was spent anywhere, because no valuation was reached.
- [x] Prices dated; the aggregator used for the live quote only and flagged, and cross-checked
      against the 10-K cover page at 2025-06-27 ($31.13, exact).
- [x] Every judgment carries a ledger id (operator rule 8).
- [x] Run committed to git.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** **USNA - Q2 OUT.** The 10-K says twice, in Item 1 and Item 1A, that its barriers to
  entry are not significant and that new competitors can enter easily; [E3-03] condition (2) is
  denied by the registrant, and the row's demonstration test fails in both halves - prices were
  raised in FY2025 and active Customers fell 14.8%, while return on equity went 28% to 2.0%. Units
  616,000 to 387,000 in seven years, and seven of seven listed direct sellers are below their
  in-window peak: a broken wave [E3-51], not a moat. **Price $14.40 at 2026-09-21; 18,476,534
  shares from the 10-Q cover, accession 0000896264-26-000056; cap $266.1M; sovereign USD 5.34% at
  2026-09-18 (US Treasury).**
