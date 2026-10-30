# Company Run: Boise Cascade Company (NYSE: BCC), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`, so
the analyst does not know whether the operator holds BCC. The run is written as a purchase run of record.

**CONTAMINATION DECLARED.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`, the run queue, the
prepped reading list, any other `Test Runs/` file about BCC (a listing of `Test Runs/` filtered for "bcc" returned nothing
before this file was made), any 2026-10-05 or 2026-10-06 run or research file of another company, and the unadopted
small-cap gaps case. Seen without opening: (a) folder names in `Test Runs/` (research folders dated 2026-10-05 and
2026-10-06 for other tickers, among them ADT, BTU, GPOR, HRMY, NSIT, PTEN); (b) the session's git status and five commit
subjects, two of which state other companies' boxes (BTU and PTEN, both OUT at Q2, with their fair and cheap prices) and
two of which describe fixes to `tools/run.py` and `Screens/cover_shares.py`; (c) the memory index carried into the
session, which names the queue state and the number of gate-clearers. None of it concerns BCC. The two Q2 OUTs in the commit
subjects are a possible anchor toward OUT at Q2 for a cyclical producer; that anchor is named here so that the Q2 verdict
below can be read against it, and the Q2 verdict rests on BCC's own filings and its competitors' filings only.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $74.84 (close 2026-10-05, as printed by `python tools/run.py BCC`; **aggregator, live quote only, flagged** per
  operator rule 5).
- **Shares by class** from the latest filing's cover: one class, Common Stock $0.01 par, **34,891,351** as of 2026-07-31
  (Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-03, accession `0001328581-26-000027`;
  `python Screens/cover_shares.py BCC`). No second class; no charter note needed.
- **Market cap:** $74.84 x 34.891M = **$2,611M**.
- **Net debt (cash and funded debt only), 2026-06-30:** $450.0M senior notes principal (carried at $448.4M net) less
  $304.8M cash = **$145.2M** (same 10-Q). At 2025-12-31 it was $450.0M less $477.2M cash, a net cash position of $27.2M
  (10-K FY2025); the difference is the seasonal build of receivables (trade receivables $507.1M at June against $315.9M at
  December). Leases are outside this figure: operating lease minimum payments $73.7M and finance lease $26.5M at
  2025-12-31 (10-K FY2025, Liquidity).
- **Enterprise value used below:** $2,611M + $145.2M = **$2,756M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, the 30-year par yield on the US Treasury daily par yield
  curve, 10/05/2026 (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4), all from SEC EDGAR, CIK 1328581, saved as text in
  `Test Runs/_research 2026-10-06 BCC/`:
  - 10-K FY2025, filed 2026-02-24, `0001328581-26-000006` (Business, Risk Factors, MD&A, statements, Notes 8, 12, 15).
  - 10-Q Q2 2026, filed 2026-08-03, `0001328581-26-000027` (statements, MD&A, the risk factor on the decking supplier).
  - Proxy DEF 14A filed 2026-03-17, `0001104659-26-029440` (CEO succession; pay mix headings only, Q5 not reached).
  - 8-K 2026-08-03, `0001328581-26-000025` (Item 8.01: ten-year exclusive distribution agreement with James Hardie);
    8-K 2026-07-30, `0001328581-26-000023` (quarterly dividend $0.23).
  - Back to the IPO and before it: S-1 filed 2012-11-15, `0001047469-12-010624` (selected data 2007-2011, segment tables
    2007-2011, the 2009-2011 cash flows); 10-K FY2012 `0001328581-13-000015`, FY2013 `0001328581-14-000010`, FY2014
    `0001328581-15-000032`, FY2015 `0001328581-16-000155`, FY2016 `0001328581-17-000012`, FY2017 `0001328581-18-000012`,
    FY2018 `0001328581-19-000025`, FY2019 `0001328581-20-000024`, FY2020 `0001328581-21-000011`, FY2021
    `0001328581-22-000017`, FY2022 `0001328581-23-000020`, FY2023 `0001328581-24-000018`, FY2024 `0001328581-25-000010`.
- **One figure cross-checked against the filed statement:** net cash provided by operations FY2025 is $254,148 thousand in
  the filed 10-K's Sources and Uses table (`0001328581-26-000006`), equal to the $254.1M `tools/run.py` transcribed from
  XBRL; capital spending $241.4M in the 10-K's Investment Activities text equals the run.py figure. Sales FY2025 $6,404.6M
  in the filed income statement equals the XBRL figure.
- **`tools/run.py BCC`, arithmetic lines only** (its rule, id and floor lines ignored under Part VII). Owner cash after every
  real cost = operating cash flow less stock pay less capital spending (USD M): 2023 456.6, 2024 193.3, 2025 0.6
  (three-year mean 216.8); depreciation basis 539.6, 278.7, 83.8. Five-year mean (2021-2025) **423.7** on the capex basis,
  **481.6** on the depreciation basis; run.py flags a +95% divergence between the three- and five-year windows, the spike
  of 2021-2022 being inside the second. Stock pay resolved by year from the ShareBasedCompensation tag (2023 15.4, 2024
  15.5, 2025 12.1); finance-lease principal (1.4 to 2.0 a year) shown as an alternate, immaterial.
- **The seventeen-year table**, built in the research folder (`owner_cash.py`) from the S-1 for 2009-2011 and the 10-K
  cash-flow statements for 2012-2025 (USD M):

| Year | OCF | Stock pay | Capex | D&A | Owner cash (capex) | Owner cash (D&A) | Acquisitions | Sales | Owner cash / sales |
|---|---|---|---|---|---|---|---|---|---|
| 2009 | -35.2 | 0 | 21.4 | 40.9 | -56.6 | -76.1 | 0 | 1,973.3 | -2.9% |
| 2010 | 10.3 | 0 | 35.8 | 34.9 | -25.5 | -24.6 | 0 | 2,240.6 | -1.1% |
| 2011 | -43.0 | 0 | 39.3 | 37.0 | -82.3 | -80.0 | 5.8 | 2,248.1 | -3.7% |
| 2012 | 77.6 | 0 | 27.4 | 33.4 | 50.2 | 44.2 | 2.4 | 2,779.1 | 1.8% |
| 2013 | 33.4 | 2.9 | 45.8 | 38.0 | -15.3 | -7.5 | 103.0 | 3,273.5 | -0.5% |
| 2014 | 101.8 | 5.9 | 61.2 | 51.4 | 34.7 | 44.5 | 0 | 3,573.7 | 1.0% |
| 2015 | 80.3 | 5.8 | 87.5 | 55.6 | -13.0 | 18.9 | 0 | 3,633.4 | -0.4% |
| 2016 | 151.9 | 8.2 | 83.6 | 72.8 | 60.1 | 70.9 | 215.9 | 3,911.2 | 1.5% |
| 2017 | 151.6 | 9.7 | 75.5 | 80.4 | 66.4 | 61.5 | 0 | 4,432.0 | 1.5% |
| 2018 | 163.6 | 8.8 | 80.0 | 146.8 | 74.8 | 8.0 | 25.5 | 4,995.3 | 1.5% |
| 2019 | 245.6 | 8.0 | 82.7 | 80.1 | 154.9 | 157.5 | 15.7 | 4,643.4 | 3.3% |
| 2020 | 294.5 | 7.8 | 79.4 | 95.2 | 207.3 | 191.5 | 0 | 5,474.8 | 3.8% |
| 2021 | 667.0 | 7.9 | 106.5 | 80.8 | 552.6 | 578.3 | 0 | 7,926.1 | 7.0% |
| 2022 | 1,041.2 | 11.9 | 114.1 | 101.6 | 915.2 | 927.7 | 515.2 | 8,387.3 | 10.9% |
| 2023 | 687.5 | 15.4 | 215.4 | 132.5 | 456.7 | 539.6 | 162.8 | 6,838.2 | 6.7% |
| 2024 | 438.3 | 15.5 | 229.6 | 144.1 | 193.2 | 278.7 | 10.2 | 6,724.3 | 2.9% |
| 2025 | 254.1 | 12.1 | 241.4 | 158.2 | 0.6 | 83.8 | 33.4 | 6,404.6 | 0.0% |

  Notes on the table. 2011 operating cash is the S-1's audited -$43.0M (the FY2012 10-K's XBRL carries -$43.6M; immaterial).
  Stock pay was nil before the 2013 IPO (units were held at the parent, Boise Cascade Holdings). 2018 depreciation includes
  $55.0M of accelerated depreciation for the Roxboro LVL curtailment (10-K FY2019, Note 6), so the D&A basis understates
  2018. Operating cash is after cash taxes and interest; it moves with working capital, which fell in the 2009-2011
  trough and rose in the 2021-2022 spike. Pooled over 2009-2025, owner cash was **3.24% of sales** (capex basis), 3.55% on the
  depreciation basis, and **1.87% after the cash paid for acquisitions** (about $1.09 billion over the span).
- **Balance sheets first, 2011 to 2025, read in Step 0 because the file closes before Q4** (`tools/run.py` table, the
  filed balance sheets behind it, and the XBRL facts for 2011-2016; USD M). The rule is the meetings': "balance sheets
  over an 8 or 10 year period before I even look at the income account" **[M2025-032]**.

| Year-end | Assets | Equity | Cash | Inventory | Goodwill + intangibles | Long-term debt | Retained earnings | PP&E net |
|---|---|---|---|---|---|---|---|---|
| 2011 | 897 | 283 | 176 | n/t | n/t | n/t | n/t | n/t |
| 2012 | 828 | 98 | 46 | 326 | 21 | 275 | -38 | 266 |
| 2013 | 1,104 | 452 | 118 | 383 | 32 | 302 | 111 | 361 |
| 2016 | 1,439 | 580 | 104 | 433 | 71 | 438 | 281 | 569 |
| 2019 | 1,693 | 701 | 285 | 498 | 78 | 441 | 357 | 477 |
| 2020 | 1,966 | 851 | 405 | 503 | 77 | 444 | 452 | 461 |
| 2021 | 2,573 | 1,353 | 749 | 661 | 75 | 445 | 949 | 495 |
| 2022 | 3,241 | 2,058 | 998 | 698 | 299 | 444 | 1,646 | 770 |
| 2023 | 3,459 | 2,196 | 950 | 712 | 361 | 445 | 1,780 | 933 |
| 2024 | 3,369 | 2,151 | 713 | 803 | 345 | 446 | 1,928 | 1,047 |
| 2025 | 3,242 | 2,075 | 477 | 796 | 345 | 445 | 1,504 | 1,157 |

  (n/t = not tagged that year-end in the facts read; 2014, 2015, 2017 and 2018 are in `tools/run.py` output and the
  research folder and move between their neighbours.) **What the figures are saying.** (1) Equity is mostly two events: the
  owners' capital went from $283M to $98M in 2012 when the company paid $228.3M of distributions to its private-equity
  parent before the IPO (10-K FY2012, `0001328581-13-000015`), was rebuilt by the IPO's $262.5M net proceeds less a $100.0M
  repurchase from the parent in July 2013 (10-K FY2013), and then rose from $851M to $2,058M in the two spike years
  2021-2022. Everything before 2020 added about $50M to $100M a year. (2) Goodwill and intangibles are small against
  equity (about 17% in 2025) and came almost entirely from the Coastal Plywood purchase of 2022 ($515.2M cash) and BROSCO
  in 2023 ($162.8M). (3) Debt has been held at $438M to $446M since 2016 while equity tripled; there is no leverage story
  here. (4) Cash peaked at $998M in 2022 and has been spent down to $305M by June 2026 on special dividends ($2.00 and
  $3.00 in 2021, $2.50 and $1.00 in 2022, $3.00 and $5.00 in 2023, $5.00 in 2024), buybacks ($194.9M at $128.81 a share
  in 2024, $181.4M at $86.31 in 2025, $108.3M at $77.08 in the first half of 2026; 10-K FY2025 Note 12, 10-Q Q2 2026),
  capital spending above depreciation, and acquisitions. (5) The capital base more than doubled after the spike: PP&E net
  went from $461M (2020) to $1,157M (2025), depreciation from $95M to $158M; the business now has to earn on a much larger
  plant than the one that produced the pre-2020 record. (6) Inventory rose from $712M to $803M in 2024 and stayed at $796M
  in 2025 while sales fell from $6,838M to $6,404M; read against **[M1995-064]**, "inventories look out of line, you know,
  with sales", the filer's explanation is early-buy programmes with vendors, new door and millwork locations and log
  inventory (10-K FY2025, Operating Activities); a second tell was not found, so it is recorded and not weighed as
  suspicion. (7) Retained earnings fell $424M in 2025 because the board retired about 7 million treasury shares and charged
  the $341.9M excess over par to retained earnings (10-K FY2025, Note 12); an accounting reclassification, not a loss.
  **What they do not say and cannot say** **[M2025-032]**: whether the 2021-2022 earnings that built the equity were a cycle
  or a new level, and what the enlarged plant will earn through the next trough. The balance sheet is conservative; it
  says nothing about the castle.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would own this "if the market closed for five years" **[M1997-109]**, which
for BCC means owning a cyclical distributor and wood-products maker through a full housing cycle, not a quotation. No
macro forecast enters: the filer's own outlook ("generational tailwinds and an undersupply of housing units", 10-K
FY2025 MD&A) is set aside, since macro conclusions "just never enter into the discussion" **[M2000-094]**; what counts is
"the average profitability of the business over time and how strong its competitive mode is" **[M2015-016]**, which is why
this run reads seventeen years and not the last five. Who is paid to tell you: the growth narrative is the company's own
and the S-1's "Low-Cost Manufacturing and Distribution Footprint" heading was written to sell shares in 2012. The analyst's
habits: look for "what you’re missing" **[M2025-013]**, and state the other side's case better than its holder
**[M2016-055]** (done at the end of Q2). **Contrary evidence, written down as found** **[M1997-127]**:
1. Found at the S-1: Building Materials Distribution earned a segment profit in every year of the housing collapse
   (2007 $51.8M, 2008 $19.5M, 2009 $8.0M, 2010 $11.6M, 2011 $2.0M), while Wood Products and BlueLinx lost money.
2. Found at the price tables: LVL realizations rose from $14.92 a cubic foot (2009) to $18.66 (2019) and $24.90 (2025);
   I-joists from $895 per thousand feet (2009) to $1,270 (2019) and $1,755 (2025). EWP did not fall back to its 2019 price
   after the spike, unlike plywood ($213, $266, $334).
3. Found at the competitor margins: BMD's segment margin exceeded BlueLinx's operating margin in 15 of the 17 years
   2009-2025 (not in 2021 and 2022).
4. Found at Weyerhaeuser's filings: in the trough BCC's Wood Products lost much less on its sales (2009 -14.0%, 2010 -1.2%,
   2011 -2.1%) than Weyerhaeuser's Wood Products segment (-35.7%, -14.3%, -10.8%).
5. Found at the balance sheet: debt flat at about $445M for a decade, net cash at the 2025 year-end, no pension
   overhang left (funded status -$4M in 2021 against -$192M in 2012).
These are weighed at Q2.

## THE STANDING RULE
Owning BCC shares bought with the buyer's own money and sized so that a halving cannot force a sale puts the buyer at no
risk of ruin; the rule binds the buyer's financing and size, not the target: "We are never going to risk what we have and
need for what we don’t have and don’t need." **[M2012-081]**. No borrowing to buy is assumed. Nothing in this name changes
that.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.
- **The key variables and whether they are foreseeable** ("trying to identify the key variables in that particular
  business, and evaluating how predictable they were first" **[M1998-044]**): (1) US single-family starts, the demand
  driver the filer names first (943.0 thousand in 2025, 10-K FY2025); (2) the price of EWP (LVL, I-joists) and of plywood;
  (3) BMD's gross margin (15.1% in 2025, 15.3% in 2024) and its mix (commodity 35.0%, general line 45.2%, EWP 19.8% of BMD
  sales in 2025); (4) the cost of logs, about 80% of wood fiber cost. Variables (1) and (2) are cyclical and their timing
  cannot be foreseen; their **pattern** can, because seventeen years of statements show it twice (the 2008-2011 trough and
  the 2021-2022 spike).
- **Do the past statements tell me the future ones?** "the financial statements will tell me the information that’s useful
  to me" **[M2008-033]**: yes in kind. The product line (I-joists, LVL, plywood, two-step distribution) is the one the
  S-1 described in 2012; the industry changes slowly (truss substitution, slab-on-grade foundations, a fire-code change on
  I-joists over basements, mass timber), and none of it is fast technology. "I understand the economic dynamics of the
  industry" **[M2011-014]** is answerable: the 10-K says in plain words where the prices come from and who competes.
- **Is it important and knowable?** "If something’s important but unknowable, forget it." **[M2006-076]**. What is unknowable
  is the date of the next trough. What is knowable, and decides the file, is whether the business has a castle that
  carries it through the cycle; that is Q2's question and can be answered from the record.
- **Doubt test.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. The
  analyst has no doubt that the business can be read; the doubt is about its quality, which is not this question.
- **VERDICT: IN.** A wood-products maker and building-materials wholesaler whose economics can be read from its own
  filings over two full cycles; not fast-changing; no financial-institution opacity. Filing fact: the 10-K FY2025
  (`0001328581-26-000006`) describes the same two segments, products and customers as the S-1 (`0001047469-12-010624`).

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" and "how permanent are they?" **[M1995-038]**. BCC is two businesses
under one roof, and the filer itself puts a large part of both inside the commodity class. The commodity rule and its
exception are applied first, then the castle tests.

**The commodity reading, in the filer's words** (10-K FY2025, MD&A, "Commodity Nature of a Portion of Our Products"): OSB,
plywood and lumber "are commodities that are widely available from multiple sources, with prices and volumes determined
frequently in an auction market based on participants' perceptions of short-term supply and demand factors", and "the price
for any one or more of the products we distribute or produce may fall below our purchase or cash production costs". In
2025 commodities were 35.0% of BMD sales (51.6% in 2021) and plywood was 31% of Wood Products sales. The row that defines
the class is the customer's indifference: "most insureds don't care from whom they buy" **[L2004-003]**. The policy: "We’re
going to be investors in businesses, not commodities, by and large." **[M2007-131]**.

**The one exception, tested: is BCC the low-cost operator?** "Another way to prosper in a commodity-type business is to be
the low-cost operator." **[L2004-007]**; "being the low-cost producer is all-important" **[L2000-017]**; and against the
textile mill, "The guy who could sell it cheaper than we could made it risky for us." **[M1997-010]**.
- **Wood Products: no, on the filer's own word.** Every 10-K read that carries the risk factors says it: "Certain mills
  operated by our competitors may be lower-cost manufacturers than the mills operated by us." (10-K FY2013
  `0001328581-14-000010`, FY2019 `0001328581-20-000024`, FY2025 `0001328581-26-000006`). The same 10-K adds "we may not be
  able to maintain our costs at a level sufficiently low for us to compete effectively", and that western log costs are
  higher than southern. In 2018 the company curtailed LVL at Roxboro after concluding "we would be unable to reduce
  manufacturing costs to an acceptable level" ($55.0M accelerated depreciation; 10-K FY2019). In plywood the 10-K names
  Georgia-Pacific "the largest manufacturer in North America" and South American imports. The S-1's claim that two
  Douglas fir plywood mills are "among the lowest cost" producers (2012) is a selling document's claim for two mills in one
  species; in the 10-Ks searched for the phrase (FY2013, FY2019, FY2025) the claim made is for "low-cost, internal veneer
  manufacturing" (FY2013), never for the segment against its rivals. "In an unregulated commodity business, a
  company must lower its costs to competitive levels or face extinction." **[L1994-035]**.
- **Building Materials Distribution: relatively efficient, not shown to prosper.** BMD's segment margin beat BlueLinx's
  operating margin in 15 of 17 years (contrary evidence 3 above), and it stayed in profit through 2009-2011. But the margin
  it kept in the trough was 0.5%, 0.7% and 0.1% of sales (2009-2011), and its pooled margin over 2009-2025 is 4.1% with 2.0%
  or less in every year before 2014. The exception's verb is "prosper" **[L2004-007]**; the evidence shows a distributor that
  survived the trough better than its weakest rival, not one that prospered through it. The copper picture asks for "a
  copper producer whose costs are $2.50 a pound with a copper producer whose costs are $1 a pound" **[M2009-059]**; the gap
  here is about one to two points of sales against BlueLinx and none against UFP Industries (below).
- **The company as a whole: no.** Consolidated operating losses in each of 2008, 2009, 2010 and 2011 (-$24.5M, -$83.4M,
  -$13.2M, -$27.0M) and net losses in each (-$63.0M, -$98.5M, -$33.3M, -$46.4M) (S-1, Selected Historical Consolidated
  Financial Data); owner cash negative in all three of 2009-2011 (Step 0 table). The low-cost operator welcomes the hard
  market **[L1997-021]**; this one lost money in it four years running.

**The castle tests, each with its filing fact.**
1. **Key factors and permanence** **[M1995-038]**. The filer names its advantages: the integrated model (BMD takes about 75%
   of Wood Products' EWP volume and 51% of its plywood volume), the national footprint (40 distribution facilities), the EWP
   sales force's design software and job-pack systems (10-K FY2025, Business). The integration is a captive channel inside
   one company, not a reason an outside customer pays more; the footprint is copyable, per test 3.
2. **The money test** **[M2011-015]**. In distribution, the filer: "the barriers to entry for local competitors are
   relatively low" (10-K FY2025, Risk Factors). In EWP, a funded attacker need not build an LVL mill: the filer reports "an
   increase in floor truss capacity by some of our dealer customers" and the spread of slab-on-grade construction, either
   of which "could negatively impact our I-joist market share and net sales prices" (same). Builders FirstSource, named by
   BCC as one of its two largest customers, describes its own floor and roof trusses and "engineered wood that we design and
   cut" as "factory-built substitutes for job-site framing" (BLDR 10-K FY2025, `0001193125-26-054643`). The largest
   customer makes a substitute. "there are some industries that are just never going to have barriers to entry"
   **[M2012-106]**.
3. **Pricing power and the agony before a rise** **[M2005-020]**: "a prayer session before you raise your prices a penny".
   The filer: Wood Products "provides financial incentives, including temporary price protection, to various parties along
   the supply chain (including wholesale distributors, dealers, and homebuilders)", so "the full effects of announced price
   increases may be delayed or reduced"; customer consolidation "could increase buying power which would create demand
   pressure on our financial incentives and compress our margins" (10-K FY2025, Risk Factors); EWP sales are reported "net of
   the cost of all EWP rebates and sales allowances provided at various stages of the supply chain" (10-Q Q2 2026, Note 11).
   Prices: LVL -11% and I-joists -10% in 2025, then LVL -6% and I-joists -7% in the first half of 2026, with volumes down
   both years. That is the prayer session in the filer's own description.
4. **Unit volume** **[M1999-054]** in kind: I-joist sales volume 290 million equivalent lineal feet in 2021, 215 million in
   2025; LVL 18.2 and 18.9 million cubic feet (10-K FY2025, capacity table). LVL capacity 36.3 million cubic feet against 27.2
   produced in 2025. Flat to falling volume into a lower price.
5. **The low-cost position**: tested above; not held in manufacturing on the filer's own word.
6. **The brand in the customer's mind.** BCC's EWP trademarks carry $8.9M on the balance sheet (10-Q Q2 2026, Note on
   intangibles). In distribution the brands belong to the suppliers, and the filer says so: for general line products "brand
   preference and product performance characteristics can have a high degree of influence on our customers' purchasing
   decisions" (10-Q Q2 2026, Risk Factors). On July 13, 2026 its primary composite decking supplier terminated the
   distribution relationship, and the filer expects "some customers will shift purchases to competitors to retain access
   to our former composite decking offering" (same); on July 31, 2026 BMD signed a ten-year agreement making it James
   Hardie's sole full-line national distributor, committing to buy those products exclusively and not to stock specified
   competing products at designated branches (8-K `0001328581-26-000025`). Where the brand sits with the maker, "the brand
   is our protection against the intermediaries making all the money" **[M2019-041]**, and here BCC is the intermediary.
7. **Would the customer still choose it over the low bid?** "it wouldn’t be a question of people buying candy for the low
   bid" **[M2017-009]** is the test; the filer lists BMD's competitive factors beginning with "pricing and availability of
   product", and Wood Products competes "primarily on the basis of price, quality, availability" (10-K FY2025, Business).
8. **Ask the competitors** **[M1999-130]**. BlueLinx's 10-K FY2025 (`0001628280-26-011136`) uses the same words: the
   industry is "highly fragmented and competitive, and the barriers to entry for local competitors are relatively low".
   Weyerhaeuser's 10-K FY2025 (`0001193125-26-051422`) shows EWP press capacity of 42 million cubic feet against BCC's 36.3
   million, so the EWP field has two large makers, and both cut EWP prices in 2025 (Weyerhaeuser: solid section and
   I-joists each "a 7 percent decrease in sales realizations"). Fewness does not cure it: "you can have only two
   competitors and they’re still terrible businesses, they beat each other’s brains out" **[M2013-052]**.
9. **Widening or narrowing** **[M2000-075]**: "could the competitive advantage have been made stronger and more durable".
   For: BMD's mix moved from commodities toward general line (30.2% to 45.2% of BMD sales, 2021-2025). Against: truss and
   slab substitution rising; a fire-code change on I-joists over unfinished basements; Wood Products segment income from
   $575.2M (2022) to $5.8M (2025) on sales of $1,613.4M; the decking supplier lost in 2026. Narrowing on the evidence.
10. **What could destroy, modify or reduce it** **[M2000-014]**: a further shift of floor framing to trusses made by the
    dealer customers, and a supplier choosing another distributor or selling direct ("certain suppliers to our distribution
    business also sell and distribute their products directly to our customers", 10-K FY2025).

**The competitor row** (same metric, operating income over sales, from each company's own 10-K filings via its XBRL
financial data; accessions of the 2025 figures: BXC `0001628280-26-011136`, BLDR `0001193125-26-054643`, LPX
`0000060519-26-000012`, UFPI `0001104659-26-019567`, WY `0001193125-26-051422`; of the 2009 figures: BXC
`0001193125-12-082075`, BLDR `0001193125-12-094395`, LPX `0001504337-12-000010`, UFPI `0001140361-12-015431`, WY
`0001193125-10-041278`; BCC 2009-2010 from the S-1; the computation is `peerser.py` in the research folder):

| Company | 2009 | 2010 | 2011 | 2015 | 2018 | 2019 | 2021 | 2022 | 2024 | 2025 | Mean 2009-25 | Loss years |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BCC (consolidated) | -4.2% | -0.6% | -1.2% | 2.8% | 1.4% | 2.9% | 12.3% | 13.8% | 7.3% | 2.9% | 4.0% | 2009-2011 |
| BlueLinx (two-step distributor) | -1.0% | -1.3% | -0.5% | 0.9% | -0.5% | 1.3% | 10.2% | 9.9% | 3.0% | 1.1% | 2.1% | 2009-11, 2013, 2018 |
| UFP Industries (wood products) | 2.6% | 1.6% | 0.7% | 4.7% | 4.5% | 5.5% | 8.5% | 9.9% | 7.4% | 5.8% | 5.0% | none |
| Builders FirstSource (dealer, BCC's customer) | -8.9% | -9.1% | -4.8% | 2.5% | 4.8% | 5.4% | 12.0% | 16.6% | 9.7% | 5.2% | 3.9% | 2009-2012 |
| Louisiana-Pacific (OSB, branded siding) | -12.6% | -0.5% | -10.3% | -3.3% | 18.6% | -0.9% | 40.1% | 32.4% | 18.0% | 7.7% | 9.6% | 2009-11, 2014-15, 2019 |
| Weyerhaeuser (consolidated, includes timberlands) | -8.1% | 7.1% | 9.6% | 13.0% | 18.6% | 9.9% | 35.7% | 30.2% | 9.6% | 10.6% | 14.2% | 2009 |

Segment against segment, from the competitors' own segment tables: **Wood Products**, BCC segment income over segment
sales against Weyerhaeuser's Wood Products net contribution over its net sales (WY 10-Ks FY2011 `0000106535-12-000016`,
FY2015 `0000106535-16-000046`, FY2019 `0001564590-20-004822`, FY2022 `0000950170-23-003217`, FY2025): 2009 -14.0% vs
-35.7%; 2011 -2.1% vs -10.8%; 2015 5.0% vs 6.7%; 2019 4.3% vs 7.6%; 2022 27.2% vs 31.9%; 2025 0.4% vs 1.1%. BCC lost less in
the trough and earned less in every other year sampled; Weyerhaeuser's segment also holds lumber and OSB, so this is the
nearest comparison the filings allow, not an exact one. Pooled over 2009-2025, BCC's Wood Products earned 9.3% of sales,
**4.1% outside the three spike years 2021-2023**. **Distribution**, BMD segment margin against BlueLinx operating margin:
higher in 15 of 17 years; BMD pooled 4.1%. Against UFP Industries, which has no loss year in the span, BCC's consolidated
mean margin is lower (4.0% against 5.0%) and its trough deeper.

**The other side's case, stated as strongly as the analyst can** **[M2016-055]**. EWP is a near-duopoly in which BCC is
the second maker and the largest captive channel; its realizations have risen faster than inflation since 2009 and did not
fall back to 2019 levels after the spike; the distributor has beaten its listed rival in fifteen of seventeen years and
never lost money even in 2009; the mill modernisations (Oakdale) and the Thorsby I-joist line are bought out of a debt-light
balance sheet; and 2025-2026 is a trough in single-family starts, not a broken business. **Why it does not carry the file.**
The exception asks for the low-cost operator, and the filer says in three 10-Ks a decade apart that competitors' mills may
cost less than its own; it is the high-cost side's case **[M1997-010]**. Two large makers cut EWP prices together in 2025
and kept cutting in 2026 through rebates paid down the chain to homebuilders, which is "they beat each other’s brains out"
**[M2013-052]** in a business the filer calls not subject to auction pricing. The distributor's edge is relative to its
weakest peer and does not appear as prosperity in either trough; the filer and that peer both say entry is easy; and the
general-line growth that the bull case rests on depends on suppliers' brands, one of which left in July 2026. The castle
is not shown to be standing; it is shown to be open, which is how the business earned nothing in 2009-2011 and $0.6M of
owner cash in 2025 after spending $241.4M on plant.

**The routing.** This is not a castle "whose future cannot be judged" (TOO HARD **[M2000-019]**); the evidence runs one way
and comes from the filer's own risk factors and price tables and the competitors' filings: a commodity field **[L2004-003]**,
a manufacturer that is not the low-cost producer **[L1994-035]**, **[M1997-010]**, a distributor in a field with low barriers
**[M2012-106]**, and a pricing record that is the prayer session **[M2005-020]**. "If the answer had been yes, we wouldn’t
have done it." **[M2011-015]**, and price does not reopen it: "What you can’t do is turn any investment into a good deal by
paying little" **[M2019-015]**.

- **VERDICT: OUT.** The castle is shown open on the evidence (`0001328581-26-000006`, Risk Factors and MD&A;
  `0001047469-12-010624`, Selected Data). The file closes here, in the "out" box of "three boxes at the company: in, out,
  and too hard" **[M2006-013]**. Q3 to Q10 and Q12 are NOT REACHED and nothing below is a clearance.

## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
(Recorded for the owner only: capital spending was $215.4M, $229.6M and $241.4M in 2023-2025 against depreciation of
$132.5M, $144.1M and $158.2M, and the company guides $150M to $170M for 2026 (10-K FY2025, Investment Activities); the
maintenance share is not separated in the filing. Not weighed.)

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED.
(The balance-sheet reading is in Step 0. One note for a later reader: the filer presents segment EBITDA in its segment tables
and explains its limitations; not weighed.)

## Q5: WHO RUNS IT. NOT REACHED.
(Fact only: Nate Jorgensen retired as CEO on 2026-03-02 and Jeff Strom became CEO on 2026-03-03; proxy
`0001104659-26-029440`.)

## Q6: WHAT WILL THEY DO WITH THE MONEY. NOT REACHED.
(Facts only, for the owner: special dividends "in each of the last five years" to 2024 (10-K FY2024, Item 5), none in 2025; buybacks under an authorisation that names no price,
at average prices of $128.81 (2024), $86.31 (2025) and $77.08 (first half 2026). Set against the computation below, all
three averages sit above the whole-cycle central fair price and the 2024 average sits above the top of the whole-cycle
range. Not weighed, since Q6 is not reached.)

---
## COMPUTATION - NOT A CLEARANCE
*(Written at the owner's request, after the closing STOP at Q2. It carries no entry language and clears nothing. The
protocol's heading joins its two halves with a long dash; it is written here with a hyphen under the standing no-dash rule.)*

**(a) The value range under the Q7 convention, and why it fails here.** The convention takes the five-year average of
owner cash, carried at the growth shown, ten years, then no growth, at the sovereign. Five-year average (2021-2025):
**$423.7M** (capex basis), $481.6M (depreciation basis). No-growth end at 5.66%, less net debt: **$210.37** a share (capex),
$239.72 (depreciation). The growth shown on aggregate owner cash from 2021 to 2025 is **-81.8% a year** ($552.6M to $0.6M),
so the shown-growth end is below zero (-$1.64 a share). The range is therefore wider than three to one and the convention
would close it TOO HARD. The cause is the window: it opens on the spike, and "a base year in which earnings were poor can
produce a breathtaking, but meaningless, growth rate" **[L2005-003]** works in reverse when the base year is a peak; the
window's average is the kind of figure the meetings warn may reflect "a cyclical peak in earnings" **[L1994-009]**.

**(a') The whole-cycle variant** (CONVENTION of this run, confessed: the five-year window holds the spike and the trough
of 2009-2011 is outside it, so the cash input is taken as the pooled owner-cash margin over 2009-2025, one full bust and one
full boom, applied to 2025 sales of $6,404.6M; held at no growth, at the sovereign, less net debt; the rate convention is the
framework's). Owner cash is after the company's taxes, interest, depreciation-equivalent capital spending and stock pay,
the figure "calculated after interest, taxes, depreciation, amortization and all forms of compensation" **[L2021-003]**.

| Case | Owner-cash margin | Owner cash | Yield on EV at $74.84 | Value at 5.66% | Fair price (10% on EV) | Cheap price (20% on EV) |
|---|---|---|---|---|---|---|
| Low: 2009-2025 without the 2021-2022 spike | 1.75% | $112.2M | 4.1% | $52.65 | $28.00 | $11.92 |
| After cash paid for acquisitions, 2009-2025 | 1.87% | $119.6M | 4.3% | $56.41 | $30.12 | $12.98 |
| **Central: 2009-2025, capex basis** | **3.24%** | **$207.5M** | **7.5%** | **$100.90** | **$55.30** | **$25.57** |
| High: 2009-2025, depreciation basis | 3.55% | $227.0M | 8.2% | $110.81 | $60.91 | $28.38 |

Whole-cycle value range at the sovereign: **$52.65 to $110.81 a share** (2.1 to 1), against **$74.84**. The price sits
inside the range, near its lower half; under the convention's second close that is OUT as well, a case that is not a
screamer, "it’s too close to think about" **[M1996-084]**.

**(b) Fair price.** The price at or below which the central case clears the floor, about ten percent (the framework's Q7
CONVENTION, from "a very high probability of at least 10% pre-tax returns" **[L2002-020]** and "there’s just a point at which
we drop out of the game" **[M2003-149]**): **$55.30 a share**. Treatment stated: (i) the floor is applied to **equity plus
net debt** (enterprise value), net debt $145.2M at 2026-06-30, cash and notes only, leases excluded; (ii) the central case is
held at **no growth**, because the shown growth over the span is the acquisitions' and the spike's and the business shows
no organic growth in owner cash that Q3 would let through; (iii) **tax**: the owner cash is already after the company's
income taxes, and the floor is read as the buyer's return before the buyer's own tax, which is how the letter's figure is
stated ("10% pre-tax returns" that then "translate" to a lower figure "after corporate tax", **[L2002-020]**, Berkshire's own
tax). On the alternative reading, the business's pre-tax earnings at a 25% tax rate set against the price, the fair price
would be $75.12, about today's price; the stricter reading is used because the framework's floor speaks of "the price paid"
and the cash an owner can take out is after the company's taxes.

**(c) Cheap price.** The price below which no pencil is needed: **$25.57 a share**, the price at which the central
whole-cycle owner cash yields twice the floor (20%) on enterprise value. Rule (CONVENTION of this run, confessed): a business
whose owner cash halved from 2008 to 2011 and from 2022 to 2025 must still clear the floor after a halving, and the meetings
widen the margin as volatility rises ("the more volatile the business is", "the larger the margin of safety"
**[M1997-080]**) and take it as "a big discount from that present value calculated using the risk-free interest rate"
**[M1997-126]**; the scale of discount in the meetings' own example is about a third of value ("I didn’t need to know whether
it was worth 97 billion or 103 billion if I was buying it at 35 billion" **[M2008-068]**), and $25.57 is about a quarter of
the central value at the sovereign ($100.90). None of this reopens Q2: a lower price does not cure an open castle
**[M2019-015]**.

**Against the price, in one line:** $74.84 is above the central fair price ($55.30) by about 35%, inside the whole-cycle
range ($52.65 to $110.81), and about three times the cheap price ($25.57). At today's price the central whole-cycle owner cash
yields 7.5% on enterprise value, below the floor.

---
## Q7 to Q10, Q12. NOT REACHED.
The file closed OUT at Q2. The computation above is reporting at the owner's request and answers none of these questions.

---
## THE BOX
**OUT, at Q2.** The castle is shown open on the filer's own evidence: commodity products priced at auction, a Wood Products
segment whose 10-Ks say competitors' mills may be lower-cost, EWP prices cut through rebates in a two-maker field and a
largest customer that makes the substitute, a distribution business in which entry is easy by the filer's and its rival's
words, and consolidated losses in each of 2008-2011. For the owner's reporting only (COMPUTATION): whole-cycle range $52.65
to $110.81, central fair price $55.30, cheap price $25.57, against $74.84. Not TOO HARD, so no research pass is opened.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the copy was the first action after reading the framework and template).
  Written in order, question by question, in this one file; **not committed after each question**, because the operator's
  instruction for this run forbids any commit. Write-early was kept in substance, not in commits.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, see below); every filing fact carries its
  document and accession; every number has a filing or a CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; the valuation lines after it are headed
  COMPUTATION and carry no entry language.
- [x] Owner cash after every real cost (operating cash less stock pay less all capital spending, with the depreciation
  variant beside it), never a net-income proxy; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (five items under the Foundations) and weighed at Q2.
- [x] No row dated after the anchor: the run is dated today and every row cited is from 2025 or earlier.
- [x] Only the arithmetic lines of `tools/run.py` were used; its yield-versus-sovereign line and anything it prints as a rule
  were ignored.
- [x] `python tools/check_framework.py`: PASS on 2026-10-06 after this file was written (not committed, per the run's instruction).
- Fragment check: a Python script (`Test Runs/_research 2026-10-06 BCC/check_ids.py`) confirms no v4 E-id appears, every
  M/L/R id is in the v5 ledger, and every quoted fragment set immediately before an id is a substring of that row.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The Q7 range convention breaks on a cyclical name whose five-year window holds a spike.** The window 2021-2025 opens on
the best year in the company's history and closes on a year of $0.6M owner cash; the "growth shown" is -82% a year, the
shown-growth end is below zero, and the convention mechanically returns TOO HARD on width while its no-growth end ($210)
is nearly three times the price. The framework has no rule for normalising across a full cycle; this run confessed its own
(the pooled 2009-2025 margin on current sales). A ruling is needed on whether the five-year window may be replaced by a
whole-cycle window when the filer itself calls its results cyclical. (2) **Q2 for a two-segment company.** Q1 has a by-parts
rule for a holding company; Q2 has none. Here one part (distribution) shows a relative cost edge over its weakest listed
rival while the other (manufacturing) is admitted by the filer to be higher-cost in places. The run judged the castle of the
whole, because the earnings, the cash and the capital are shared and the integration is the filer's own stated strategy;
that choice is ours and should be ruled on. (3) **"Prosper" in the low-cost exception is undefined.** L2004-007's exception
asks for the low-cost operator and says it prospers; it does not say against whom the cost is measured when the only listed
rival is weak, or whether surviving a trough with a 0.1% margin is prospering. The run read "prosper" as earning a return
through the trough, and recorded the relative edge as contrary evidence. (4) **The floor's tax basis is ambiguous.**
L2002-020 states the ten percent as the investor's pre-tax return; M2011-062 states it as the business's "pretax earnings on
what we pay" for whole businesses. For BCC the two readings move the fair price from $55.30 to $75.12, the whole distance to
the price. The run used the first for a marketable purchase and showed the second; the framework should say which. (5) **The
protocol's computation heading (operator rule 3) is written with a long dash** and the operator's standing rule forbids
them; the heading was written with a hyphen. (6) **Write-early versus no commits.** The template's
self-audit asks for a commit after each question; this run's instruction forbids commits; the box was ticked in substance
and the conflict is recorded.
