# COMPETITOR ROW — freight brokerage, transcribed from EDGAR primary documents
**Built 2026-09-01 for the LSTR run.** Q2 requires the competitor row because a moat is a
relative claim. This file is the evidence base; the run file carries the judgment.

**STATUS: the LSTR run was killed by a session limit before its run file was written.**
This research survives. Resume from here — the arithmetic and the competitor row are done.

---

## 0. FILING IDENTIFICATION

```
CO    CIK         ACCESSION              FILED       FYE         PRIMARY DOC
CHRW  0001043277  0001043277-26-000009   2026-02-13  2025-12-31  chrw-20251231.htm
RXO   0001929561  0001929561-26-000013   2026-02-09  2025-12-31  rxo-20251231.htm
HUBG  0000940942  *** NO FY2025 10-K EXISTS ***  (see Section 3)
      latest 10-K 0000950170-25-026866   2025-02-25  2024-12-31  hubg-20241231.htm
      NT 10-K     0001193125-26-086687   2026-03-03  2025-12-31  d16550dnt10k.htm
JBHT  0000728535  0001437749-26-005294   2026-02-24  2025-12-31  jbht20251231_10k.htm
SNDR  0001692063  0001692063-26-000013   2026-02-20  2025-12-31  sndr-20251231.htm
UBER  0001543151  0001543151-26-000015   2026-02-13  2025-12-31  uber-20251231.htm
LSTR  0000853816  0001193125-26-064756   2026-02-24  2025-12-27  d66072d10k.htm  (anchor)
```

---

## 1. THE SPREAD — the single most important item

**Each company's own verbatim label, its own number. These are NOT the same measure.**
Read the definition column before comparing.

```
CO / LABEL (verbatim)                         FY2025     FY2024     FY2023   DEFINITION
LSTR "Variable contribution"        $000    668,020    681,253    772,392
     "Variable contribution margin"            14.1%      14.1%      14.6%   rev less purch transp less AGENT COMMISSIONS
LSTR "Gross profit"                 $000    404,194    456,014    545,327
     "Gross profit margin"                      8.5%       9.5%      10.3%   GAAP; also deducts other costs of revenue

CHRW "Adjusted gross profits"       $000  2,729,410  2,765,014  2,604,608
     "Adjusted gross profit margin"            16.8%      15.6%      14.8%   rev less purch transp less purch products
CHRW "Gross profits"                $000  2,671,152  2,720,706  2,570,988
     "Gross profit margin"                     16.5%      15.3%      14.6%   GAAP; also deducts direct sw amortization
CHRW "Total adjusted gross profit margin" Transportation only: 17.5% / 16.1% / 15.2%

RXO  "Gross margin"                   $M        932        774        717
     "Gross margin as a % of revenue"          16.2%      17.0%      18.3%   rev less cost of transp less direct opex less direct D&A
RXO  "Gross margin"  Truck brokerage  $M        560        417        363
     "Gross margin as a % of revenue"          13.3%      13.8%      15.4%   truck brokerage segment only
RXO  Q4'25 truck brokerage gross margin        11.9%  (Q4'24 13.2%, Q4'23 14.8%)

JBHT "Gross profit margin" (ICS seg)           14.5%      16.1%      13.4%   company does not publish the dollar numerator

SNDR no equivalent label published. Logistics segment operating ratio 98.1% (2025) / 97.4% (2024)

UBER Freight rev less "Platform Participant
     direct transaction costs"        $M        516        489        531
     as % of Freight revenue                   10.1%       9.5%      10.1%   revenue less carrier payments
```

**Sources.** LSTR 10-K Item 7, "Gross Profit, Variable Contribution, Gross Profit Margin and
Variable Contribution Margin" reconciliation table. CHRW 10-K Item 7 OVERVIEW, "reconciliation
of gross profits to adjusted gross profits" table. **RXO: the 10-K contains NO net-revenue
line at all**; the "Gross margin" table comes from the Q4 2025 earnings release (8-K acc
0001929561-26-000006, filed 2026-02-06, Ex. 99.1 `rxoq42025pressrelease.htm`), and the FY2023
column from the Q4 2024 release (8-K acc 0001929561-25-000029, filed 2025-02-05). **Both are
FURNISHED under Item 2.02, not filed** — flagged under operator rule 4. JBHT 10-K Item 7,
"Operating Data by Segment," ICS block. UBER 10-K Note 13 Segment Information.

### Normalized to one basis: revenue less purchased transportation only (DERIVED)

This is the only line the filings support in common. **Landstar's own 14.1% is after paying
its agents; the peers pay their sales force below the gross line**, so the comparable Landstar
figure is the one below.

```
                                    FY2025   FY2024   FY2023
LSTR   (4,743,760-3,688,343)/rev     22.3%    22.3%    23.3%
CHRW   (16,232,763-12,235,163-
        1,268,190)/rev               16.8%    15.6%    14.8%
RXO    (5,742-4,611)/rev             19.7%    21.6%    24.5%
RXO truck brokerage only             13.3%    13.8%    15.4%
JBHT ICS (1,109-958)/rev             13.6%    15.3%    11.9%  (numerator incl. rents+fuel; co. says 14.5/16.1/13.4)
SNDR Logistics (1,338.9-1,057.9)/rev 21.0%    19.9%    20.5%  (cost line incl. fuel; segment incl. managed transp)
UBER Freight                         10.1%     9.5%    10.1%
HUBG (3,946,390-2,930,562)/rev         n/a    25.8%    25.2%  (majority asset-based; NOT a brokerage spread)
```

**THE TREND, PLAINLY — this is the Q2 finding.** Landstar's variable contribution margin is
**flat at 14.1%** and its purchased-transportation-only spread **flat at 22.3%**. CHRW's is the
only one clearly **rising** (14.8 → 15.6 → 16.8), attributed in its own words to *"the continued
advancement of our dynamic pricing and costing capabilities."* RXO's is **falling hard** on both
bases (18.3 → 17.0 → 16.2 total; 15.4 → 13.8 → 13.3 in truck brokerage; 11.9% in Q4 2025 with
Q1 2026 guided to 11–13%). Uber Freight sits near 10% and has **never** earned a positive
segment Adjusted EBITDA. JBHT's ICS spread is the most volatile and **the segment loses money
at every observed level.**

---

## 2. CONSOLIDATED FINANCIALS

```
                                  CHRW($000)      RXO($M)     JBHT($000)   SNDR($M)   HUBG($000, FY24)
Total revenues       FY2025      16,232,763        5,742      11,999,096    5,674.3       n/a
                     FY2024      17,724,956        4,550      12,087,204    5,290.5     3,946,390
                     FY2023      17,596,443        3,927      12,829,665    5,498.9     4,202,585
Operating income     FY2025         794,961          (79)        865,069      168.9       n/a
                     FY2024         669,141          (56)        831,225      165.2       140,291
                     FY2023         514,607           39         993,196      296.4       212,231
Net income           FY2025         587,081         (100)        598,282      103.6       n/a  (FY24: 104,043)
Total equity   FY2025 end        1,845,647        1,541       3,565,085    3,024.7       n/a
               FY2024 end        1,722,051        1,612       4,014,505    2,986.9     1,691,951
Net PP&E       FY2025 end          116,362          134       5,538,101    2,719.6       739,896 (FY24)
Total assets   FY2025 end        5,058,381        3,277       7,927,155    4,840.1     2,868,343 (FY24)
Goodwill       FY2025 end        1,457,976        1,111         134,057      337.4       814,309 (FY24)
Intangibles net FY2025 end          18,174          453          76,300       73.0       267,357 (FY24)
Total debt     FY2025 end        1,089,438      404 (a)       1,466,797      402.5 (b)   264,362 (FY24)
Operating lease liabs               305,948          266             n/d        n/d       243,156 (FY24)
CFO                  FY2025         914,519           51       1,678,272      637.4       194,419 (FY24)
Capex                FY2025      70,543 (c)           59         730,687  384.8 (d)        50,847 (FY24)
D&A                  FY2025         102,818          116         714,785      450.0       141,469 (FY24)
```
(a) RXO 10-K Item 1A: *"As of December 31, 2025, we had $408 million of outstanding debt and
finance leases"*; balance sheet shows 17 current + 387 long-term. Finance lease liabilities $3M.
(b) SNDR label "Total debt and finance lease obligations"; senior notes $50.0, delayed-draw
term loan $347.5, finance leases $5.0.
(c) CHRW: "Purchases of property and equipment" 19,628 plus "Purchases and development of
software" 50,915.
(d) SNDR: transportation equipment 352.0 plus other PP&E 32.8; company-stated "Net capital
expenditures" $289.2M after $95.6M proceeds.

Sources: consolidated balance sheets, statements of operations, and statements of cash flows
in each 10-K.

**Note for the run's asset-lightness argument**: CHRW net PP&E $116M and RXO $134M against
JBHT $5,538M and SNDR $2,720M. The asset-light structure is NOT unique to Landstar; it is
shared by its two closest brokerage peers.

---

## 3. HUB GROUP — THE FILING FAILED, AND WHY

**This is the biggest single finding of the EDGAR sweep, and it is a Q3 datum for the whole
industry, not just for Hub.**

**Hub Group has not filed a FY2025 10-K**, nor its Q1 2026 or Q2 2026 10-Qs. The rung that
failed is **the filing itself, not the retrieval.**

```
2026-02-05  8-K Item 4.02  acc 0001193125-26-039396  non-reliance
2026-03-03  NT 10-K        acc 0001193125-26-086687  late filing, FY2025
2026-03-24  8-K + PR       acc 0001193125-26-121851  Nasdaq deficiency (10-K)
2026-05-21  8-K + PR       acc 0001193125-26-234605  Nasdaq deficiency (Q1 10-Q)
2026-08-24  8-K + PR       acc 0001193125-26-363681  Nasdaq deficiency (Q2 10-Q)
```

Verbatim, 8-K of 2026-02-05, Item 4.02: *"the Company identified an error that resulted in the
understatement of purchased transportation costs and accounts payable in the first nine months
of 2025."* Ex. 99.1 the same day: *"The total amount of the reduction to accounts payable and
purchased transportation costs related to this issue that was recorded during these periods is
$77 million."* And: *"The Company expects to conclude that it did not maintain effective
disclosure controls and procedures and internal control over financial reporting for the year
ended December 31, 2025."*

**The error is in the cost line that DEFINES the brokerage spread.** By the 2026-05-21 release
the scope had widened: *"Hub Group continues to work diligently to complete the restatements of
its financial statements for the years ended December 31, 2024 and 2023 and the quarterly
periods ended March 31, 2025, June 30, 2025 and September 30, 2025."* Nasdaq's exception period
runs to **September 14, 2026**.

**Treat every HUBG number in Section 2 as subject to restatement.** They come from the FY2024
10-K, which the company now says it is restating.

Unaudited preliminary FY2025 figures Hub Group did furnish (8-K 2026-02-05, Ex. 99.1):
consolidated operating revenue ~$3.7B; ITS ~$2.2B; Logistics ~$1.6B; operating cash flow ~$194M;
capex ~$45M; cash and restricted cash ~$140M; debt ~$229M; net debt ~$116M; returned $44M to
shareholders ($30M dividends, $14M buybacks). **Q4 brokerage volumes down 10% year over year
with revenue per load down 4%.** ~6,000 employees and drivers.

---

## 4. OPERATING METRICS, HEADCOUNT, NETWORK SIZE

```
CHRW  (10-K Item 1, Human Capital; Item 7 consolidated results table)
  Employees 12/31/2025            11,855 in 37 countries
  Average employee headcount      12,733 (2025) / 14,386 (2024) / 16,041 (2023), down 11.5% and 10.3%
  Contract carriers                450,000 (2025) / 450,000 (2024) / "more than 450,000" (2023)  FLAT
  Customers                         75,000 (2025) / 83,000 (2024) / "more than 90,000" (2023)  DECLINING
  Shipments managed             ~37 million (2025) / ~37 million (2024) / ~19 million (2023)*
  Freight under management        $23 billion (2025)
  Carrier concentration: largest truck provider under 1% of total cost of transportation;
    carriers with fewer than 100 trucks moved approximately 72% of truckload shipments
  * the 2023 wording is "handled"/"processed"; the 19 to 37 million step is likely a
    definition change, not volume. FLAGGED, not used.

RXO  (10-K Item 1, Human Capital)
  Team members 12/31/2025          9,218 total = 6,906 regular employees + 2,312 temporary workers
  Carrier network                  NOT DISCLOSED in the FY2025 or FY2024 10-K.
    FY2023 10-K, verbatim: "As of December 31, 2023, we had approximately 115,000 carriers in our
    North American truck brokerage network, and access to more than 1.4 million trucks."
    *** RXO STOPPED PUBLISHING THE COUNT AFTER FY2023. That is itself the network-size datum. ***
  Q4'25 brokerage volume down 4% y/y (LTL +31%, full truckload -12%)

JBHT ICS  (10-K Item 1 ICS Segment; Item 7 Operating Data by Segment)
                                   FY2025     FY2024     FY2023
  Segment revenue ($M)              1,109      1,141      1,390
  Segment operating income ($M)       (10)       (56)       (44)   *** LOSS IN ALL THREE YEARS ***
  Gross profit margin                14.5%      16.1%      13.4%
  Loads                           553,126    609,854    764,839   DOWN 28% over two years
  Revenue per load                 $2,005     $1,872     $1,818
  Employee count (end of period)      575        590        861
  Third-party carriers (approx.)  126,400    110,000    122,100
  J.B. Hunt 360 Marketplace rev     $349.1M   $395.8M    $765.6M  DOWN 54% over two years
  Segment assets ($M)                 286        288        350
  Verbatim FY2025: "ICS's carrier base increased 15% when compared to 2024, following a decline
    in 2024 due to changes in carrier qualification requirements."
  Verbatim FY2024: "ICS's carrier base decreased 10% when compared to 2023, primarily due to
    changes in carrier qualification requirements."
  JBHT consolidated employees 12/31/2025: 31,750 (21,554 company drivers, 8,481 office,
    1,374 maintenance technicians, 341 delivery and material assistants) plus 2,350
    independent contractors

SNDR  (10-K Item 1; Note on Segments)
  Associates 12/31/2025            approximately 19,000, 70% drivers
  Verbatim: "Within our Logistics segment, our brokerage business managed over 14,000 qualified
    carrier relationships and our supply chain management business managed approximately
    $2.2 billion of third-party freight in 2025."
  Customers served in 2025         approximately 7,400, including 136 Fortune 500
  Logistics segment income from operations ($M): 25.0 (2025) / 32.7 (2024) / 45.9 (2023)

HUBG  headcount 6,471 at 12/31/2024 (5,956 at 12/31/2023); approximately 500 independent
  contractor drivers; approximately 2,300 tractors, 3,200 employee drivers, 4,700 trailers.
  No carrier count is disclosed for the brokerage business in the FY2024 10-K.

LSTR (anchor)  457 agents generated at least $1 million each in FY2025, approximately 95% of
  consolidated revenue; 77 agents generated at least $10,000,000, approximately 68% of revenue;
  *** two agencies each over 10% of revenue, in aggregate approximately $994,000,000 or 21% of
  revenue and approximately 16% of consolidated variable contribution. ***
```

**The concentration line is the one to carry into Q2 and Q4.** The network story is that ~1,100
independent agents diversify the revenue base. The filing says **two agencies are 21% of
revenue.** That is a customer-concentration fact wearing a network's clothes.

---

## 5. DIVIDENDS — the special-dividend decomposition

```
CHRW  declared per share: $2.49 (2025) / $2.46 (2024) / $2.44 (2023).  NO SPECIAL.
RXO   NONE. No dividend line in financing activities; accumulated deficit $(384)M.
JBHT  $0.44 quarterly in 2025 ($1.76), $0.43 in 2024, $0.42 in 2023; raised to $0.45 on
      2026-01-22. NO SPECIAL.
SNDR  declared $0.38/share (2025), $0.38 (2024), $0.36 (2023). NO SPECIAL declared; the 10-K
      mentions specials only as a hypothetical Board option.
HUBG  $0.125 quarterly in 2024 ($0.50). NO SPECIAL. FY2025 dividends paid approximately
      $30M per the preliminary 8-K.
LSTR  regular $1.56/share paid in FY2025 ($54,126,000) PLUS a special cash dividend of
      $2.00 per share declared 2025-12-04 ($68,117,000), and a $2.00 special declared
      2024-12-09 ($70,632,000).
```

**Landstar is the only one in the set paying special dividends. None of the five competitors
pays one.** The Stage 0 decomposition matters here: the special is **larger than the regular**,
and treating the combined figure as a yield would manufacture one — the COLM error.

---

## 6. CONVOY — why the digital broker died, and the number that overturns the popular story

### Filed EDGAR record (all that exists)
Convoy, Inc., CIK 0001754407, Seattle WA. **Two Form D filings, no financial statements, no
bankruptcy docket.**
```
Form D 2018-09-28  acc 0001754407-18-000003  offering $185,000,000  sold $177,324,953  31 investors
Form D 2019-11-14  acc 0001754407-19-000002  offering $400,000,000  sold $302,249,953  44 investors
Revenue range on both: "Decline to Disclose"
```
**There is no audited Convoy financial statement in existence.** Every Convoy margin or revenue
figure in circulation is a leak or a reporter's source. The wind-down was private, not a
bankruptcy, so nothing was ever docketed. **Everything in the rest of this section is therefore
SECONDARY SOURCE and is labelled as such — it is not filing evidence and cannot carry a Q2
judgment on its own.**

### What it did
A licensed property broker taking principal risk on the spread: it quoted the shipper a firm
price up front, then sourced the truck. No trucks owned. The digital part was four things: a
carrier-side smartphone app for self-dispatch; automated pricing and matching (Convoy claimed
100% automated brokering in top US markets by 2019, ~90% of the journey by 2022); "Automated
Reloads," bundling a follow-on load into a circuit to cut deadhead; and "Convoy Go," a leased
trailer pool for power-only drop-and-hook, ~3,000 trailers by April 2022 and ~4,000 by 2023. It
also ran fuel cards and quick-pay, fronting carrier payment before collecting from the shipper.

### Scale
Gross revenue $800M (2021), $630M (2022) against a $1B internal target, ~$500M run-rate in 2023.
Peak headcount 1,300–1,500, ~500 at closure. Network of 400,000+ drivers and 80,000 carriers per
Flexport's own memo. Over $1 billion raised including debt. Series E April 2022: $160M equity
plus $100M Hercules venture debt at a $3.8B post-money, plus a $150M JPMorgan line.

### THE NUMBER THAT OVERTURNS THE POPULAR STORY
Convoy's gross-to-net spread was **17.7% in FY2022 and 18.1% year-to-date 2023** (Craig Fuller,
FreightWaves, 2023-10-23, verbatim: *"This revenue was gained with an 18% Gross to Net revenue
margin (Shipper invoice less carrier payment), producing a net revenue run rate of $90m"*).

Set that against the filings above: **CHRW's adjusted gross profit margin in 2023 was 14.8%.
RXO's truck brokerage gross margin was 15.4%. Landstar's variable contribution margin was
14.6%.**

> **Convoy was earning a WIDER spread than the survivors and still died. The spread was not the
> problem.** Any Q2 argument that rests on Landstar's spread being defensible must survive this.

### What actually killed it — four mechanisms, each sourced
1. **Capital structure, not unit economics.** $3.8B post-money on ~$136M of net revenue is ~28x
   net revenue. No strategic acquirer could validate that, so the company required perpetual
   outside funding. Fuller: *"Convoy was a victim of two realities: a failure to control its own
   destiny by relying on investors for funding and the violence and realities of the freight
   market"* and *"There is such a thing as death by overfunding."* Investors underwrote on gross
   revenue; buyers price on EBITDA.
2. **It stopped being asset-light.** 3,000–4,000 leased trailers with daily equipment, insurance
   and maintenance cost; quick-pay working capital fronted to carriers; $100M venture debt plus
   a $150M credit line; 1,300–1,500 headcount against ~$90M of net revenue run-rate. Compare
   Hampstead on the real broker model: *"Computers and chairs don't cost much, and
   incentive-based compensation grows and contracts with market cycles."*
3. **Principal risk on fixed-rate contract freight, realized against it.** Lewis at F3, Nov 2024,
   verbatim: *"In 2019 ... we decided to go national with its trailer pool ... we took on a lot
   of contract risk right at the end of 2019 in Q3 and Q4,"* and *"with COVID hitting, that was a
   really painful decision, because the rates shot up. We had all these assets, we had all these
   contracts."*
4. **No structural moat in the first place.** Leonard Sherman (Columbia), verbatim: *"To
   successfully pull off blitzscaling, one needs factors like network effects, economies of
   scale, high customer switching costs and high barriers to entry. Sherman said freight
   brokerage is decidedly lacking in all of those areas."* **Both sides multi-home; a carrier rep
   may consult a dozen brokers a day.** And from the acquirer, Ryan Petersen's memo: chasing the
   largest shippers adds *"complexity to the system that makes it hard to scale and turn a
   profit, even with all of Convoy's incredible tech."*

There is evidence Convoy bought freight early. Rachel Premack, FreightWaves 2023-10-26, verbatim:
*"Digital freight brokers were infamous for trying to shore up market share with low rates.
Convoy appeared to do that as well... In part because of these low rates, Convoy was only able to
achieve breakeven or slightly positive margins during hot times in trucking."* Hampstead's 2019
sector model assumed digital brokers ran at ~1% gross margin against traditional brokers at
15.7%. The two facts reconcile across time: buy freight to build density, then price up. By
2022–23 it had priced up and still could not cover its cost structure.

### The founder's own statement, verbatim
Internal memo, 2023-10-19 (recovered from CDLLife; CNBC, GeekWire, Transport Topics and Supply
Chain Dive carried matching excerpts):

> *"So, what happened? In short, we are in the middle of a massive freight recession and a
> contraction in the capital markets. This combination ultimately crushed our progress at the
> same time that it was crushing our logical strategic acquirer, it was the perfect storm.*
>
> *Convoy's tech centric approach to trucking created real benefits. It also created the
> conditions for a truly scalable technology platform and business model that would have yielded
> real financial gains when market conditions improve. But in the end, market forces were too
> strong for us to withstand on our own.*
>
> *We moved all business levers possible. But we were running up the down escalator, and it kept
> speeding up.*
>
> *Alongside this unprecedented freight market collapse, the dramatic monetary tightening we've
> seen over the last 18 months has dramatically dampened investment appetite and shrunk flows
> into unprofitable late stage private companies. Add to that, amidst these freight and financial
> conditions, M&A activity has shrunk substantially and most of logical strategic acquirers of
> Convoy are also suffering from the freight market collapse, making the deal doing that much
> harder."*

**Note what Lewis names: three exogenous causes, all cyclical or capital-market. He concedes no
structural margin problem and asserts the model "would have yielded real financial gains when
market conditions improve."** That is the [E3-48] shape — read it against mechanism 4 above,
which says the opposite.

### Shutdown and disposition
Stopped accepting orders 2023-10-18; core operations closed 2023-10-19; a private wind-down,
**not a bankruptcy**, which left carrier claims unadjudicated (FreightWaves documented individual
unpaid claims including ~$156,821 for 203 loads). Goldman Sachs ran a sale process from June 2023
with initial interest from Uber Freight, Walmart, C.H. Robinson and Coyote; **C.H. Robinson was
reportedly in advanced discussions by late summer and the deal fell apart.** Flexport acquired the
technology stack and IP plus a few dozen engineers, announced 2023-11-01, terms not disclosed
(FreightWaves later reported *"$16 million, though neither company confirmed that price"*). DAT
Freight & Analytics agreed to buy the Convoy Platform from Flexport on 2025-07-28, price
undisclosed and reportedly near $250 million.

### Same window, peer set — this was a sector event, not one company's failure
Uber Freight cut ~150 brokerage jobs Jan 2023 and ~50 more in July. Transfix sold its brokerage
unit to NFI 2024-06-05 and pivoted to SaaS. Loadsmart survived but pivoted toward SaaS and managed
transportation. Flexport cut ~20% of staff in Jan 2023 and 600 more on 2023-10-13, weeks before
buying Convoy's stack. Surge Transportation, a digital brokerage, filed bankruptcy 2023-07-24.

---

## 7. UBER FREIGHT AND TQL

### Uber Freight, filed segment figures (Uber Technologies 10-K, Note 13 Segment Information)
```
$ millions                    2021     2022     2023     2024     2025
Freight revenue              2,132    6,947    5,245    5,141    5,099
Freight Segment Adj. EBITDA   (130)       0*     (64)     (74)     (33)
Freight Platform Participant
  direct transaction costs      n/d      n/d  (4,714)  (4,652)  (4,583)
Freight "Other" costs           n/d      n/d    (595)    (563)    (549)
Implied spread                  n/d      n/d    10.1%     9.5%    10.1%
```
\* The FY2023 10-K prints "--" for 2022 Freight Segment Adjusted EBITDA, i.e. zero as presented.

2021–2023 from the FY2023 10-K (acc 0001543151-24-000012). 2023–2025 from the FY2025 10-K (acc
0001543151-26-000015). **The 2021→2022 revenue jump is the Transplace acquisition**, completed
Q4 2021, which added transportation management revenue — a perimeter change, not growth.

Verbatim, FY2025 10-K: *"Freight revenue decreased primarily attributable to a 1% decrease in
Freight Gross Bookings due to lower revenue per load as a result of the challenging freight
market cycle."*

> **Uber Freight has never posted a positive segment Adjusted EBITDA in any year 2021 through
> 2025**, on a spread of ~10%, which is the thinnest in the set and roughly 40% of Landstar's
> purchased-transportation-only spread. **The best-capitalised technology entrant in the industry
> has not made the disintermediation argument work in five years of trying.**

### TQL
**No EDGAR registrant exists.** EDGAR company search returns "No matching companies" for both
"Total Quality Logistics" and "TQL". Total Quality Logistics, LLC is privately held (Ken Oaks,
Union Township, Ohio) and has never registered securities, filed a Form D, or filed a periodic
report. **There are no filed figures of any kind. Any TQL revenue or margin number is trade-press
estimate only and cannot be sourced to a filing.** Under the four-verdict test this is
UNKNOWABLE, not UNRESEARCHED: I can name no document that would resolve it.

---

## 8. WHAT COULD NOT BE OBTAINED, AND WHICH RUNG FAILED

1. **HUBG FY2025 10-K.** The filing does not exist. Failure is at the registrant, not EDGAR.
   Delinquent on the FY2025 10-K and both 2026 10-Qs; restating FY2023, FY2024 and the first
   three quarters of FY2025; Nasdaq exception to 2026-09-14. Preliminary unaudited FY2025 figures
   are **furnished (not filed)** in an 8-K Item 2.02 exhibit.
2. **RXO carrier network count for FY2024 and FY2025.** Not disclosed in either 10-K. Last
   disclosed is FY2023: ~115,000 carriers, access to more than 1.4 million trucks. **Retrieval
   succeeded; the disclosure was discontinued.** That is a Q3 candor datum.
3. **RXO net revenue in the 10-K.** The 10-K carries no such line. Sourced from 8-K earnings
   exhibits, **furnished under Item 2.02 rather than filed.** Flagged above.
4. **JBHT ICS gross profit dollar numerator.** JBHT publishes the ICS gross profit *margin*
   percentage only, never the dollar amount. The derived figure uses "Rents, purchased
   transportation, and fuel," a broader cost line, and therefore does not reconcile to the
   disclosed percentage. **Do not present the derived number as the company's.**
5. **SNDR Logistics net revenue.** No such disclosure. The segment cost line is "Purchased
   transportation, fuel, and fuel taxes," which includes fuel for Cowan's owned trucks, so the
   derived 21.0% **overstates** the true brokerage spread. SNDR's MD&A refers to *"an increase in
   net revenue per order"* but never tabulates it.
6. **HUBG brokerage carrier count.** Not disclosed in the FY2024 10-K.
7. **Convoy loads per year, and any audited Convoy financials.** Neither exists. EDGAR holds only
   the two Form D notices.
8. **EDGAR full-text search returned HTTP 500** and `cgi-bin/browse-edgar` intermittently returned
   503 under rapid sequential queries. Worked around by retry with backoff and by using
   `data.sec.gov/submissions` and `company_tickers.json`. **No data was lost to this.**
