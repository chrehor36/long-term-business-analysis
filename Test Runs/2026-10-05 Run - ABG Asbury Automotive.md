# Company Run: Asbury Automotive Group, Inc. (NYSE: ABG), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Template:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch. Working folder:
`Test Runs/_research 2026-10-05 ABG/` (the filings as text, `q7.py`, `gpu.py`, `peers/peers.py`, `ledger_rows.txt`).
Every judgment cites a v5 ledger id in bold; every filing fact carries its accession. No em dashes are used in this
file, so operator rule 3's heading is written "COMPUTATION - NOT A CLEARANCE".

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbade opening `PORTFOLIO.md`,
so whether the operator holds ABG is unknown to the analyst. Berkshire owns Berkshire Hathaway Automotive; the rows on
auto dealing are read below as evidence, never as a reason to like this name.

**CONTAMINATION, declared:** (1) a directory listing of `Test Runs/` showed the file name
`2026-07-16 Run - Auto Dealers 5-pack (ABG LAD AN GPI PAG).md`. It was not opened; its name says a v3-era run of
these dealers exists and nothing about its outcome. (2) The session's opening context listed recent commit subjects
(HOS, CSW, KLXE, a small-cap screen) and the git status listed other 2026-10-05 run files by name (CAG, GIII). None
concerns ABG; none was opened. (3) `tools/run.py` printed v4 material; only its arithmetic lines were used (Part VII).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $171.62 (2026-10-05, Yahoo chart feed via `tools/sources.py`; AGGREGATOR, live quote only, flagged under
  operator rule 5). It is the twelve-month low; the twelve-month high in the same feed is $256.03.
- **Shares by class** from the latest filing's cover: 17,951,917 common, $0.01 par, as of 2026-07-29 (10-Q for the
  quarter ended 2026-06-30, filed 2026-07-31, accession 0001144980-26-000094; `python Screens/cover_shares.py ABG`).
  One class only. Balance-sheet check: 40,099,276 issued less 22,147,927 in treasury = 17,951,349 at 2026-06-30.
- **Market cap:** $171.62 x 17.952M = **$3,081M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, 2026-10-02
  (the issuing authority, read by `tools/run.py` through `tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025 (filed 2026-02-20, accession 0001144980-26-000051), Items 1, 1A,
  3, 7, 7A and 8; 10-Q for Q2 2026 (filed 2026-07-31, 0001144980-26-000094), statements, MD&A, debt note, Items 3, 4
  and Part II; DEF 14A 2026 (filed 2026-03-24, 0001144980-26-000070), ownership, CD&A, summary compensation table;
  8-Ks of 2026-07-28 (Q2 release, 0001144980-26-000089), 2026-08-19/25 (0001144980-26-000096), 2026-08-31
  (0001144980-26-000098), 2026-02-04 (0001144980-26-000003) and 2025-12-08 (0001144980-25-000155); and every 10-K
  income statement and MD&A unit table from FY2007 to FY2024 (accessions in `gpu.py` and the table at Q2; FY2008
  10-K 0001193125-09-055555 for the 2008 going-concern paragraph).
- **One figure cross-checked against the filed statement:** cash provided by operating activities FY2023, $313.0M,
  printed by `tools/run.py` from XBRL, equals the filed cash-flow statement in the FY2025 10-K (0001144980-26-000051).
  FY2025 OCF $775.2M likewise equals the filed statement.
- **`tools/run.py ABG`, arithmetic lines only:** OCF less SBC less capex was $1,073M (2021), $581M (2022), $147M (2023);
  its window stopped at 2023 because later capex and D&A tags were missing. Those lines are on the wrong basis for a
  dealer (see Q4: they swing with how floor-plan debt is classified) and are not used. Owner cash is rebuilt below from
  the filed statements on one consistent basis.

### Owner cash, rebuilt on a consistent floor-plan basis (USD millions)
**The basis.** Asbury classifies floor-plan debt owed to a lender affiliated with the car maker (Ford Credit) as
"trade" and its change runs through operating cash flow; floor-plan debt owed to its bank syndicate is "non-trade" and
runs through financing (10-K FY2025, "Classification of Cash Flows Associated with Floor Plan Notes Payable"). The new
vehicle inventory itself always runs through operating cash. So reported OCF swings by hundreds of millions with the
mix (2021 $1,163.7M, 2023 $313.0M). The consistent basis used here treats **all new-vehicle floor plan as operating**
(it is the supplier credit that finances the inventory), treats **cash parked in the floor-plan offset account as
cash** (not as a repayment), and treats **used-vehicle floor plan and floor plan assumed or repaid in acquisitions and
divestitures as financing**. That is the company's own "adjusted cash flow provided by operating activities", whose
reconciliation lines are in each 10-K; I re-added them for FY2025: 775.2 - 57.2 - 9.1 - 57.4 = 651.5 (filed 651.4),
and checked the -57.2 against the gross lines (non-trade borrowings 10,382.0 less repayments 10,214.9 = 167.1, less
the used-vehicle facility's net 650.0 - 425.7 = 224.3, gives -57.2). Owner cash = that figure less stock pay less all
capital spending excluding real estate. Real-estate purchases (2021 $224.9M, 2024 $157.5M, H1 2026 $51.9M) are left
out: they replace rent, which already sits in the earnings. Acquisitions are left out and judged at Q3 and Q6.

| Year | Adjusted OCF | SBC | Capex ex real estate | **Owner cash** | D&A variant (less D&A, not capex) | Source 10-K |
|---|---|---|---|---|---|---|
| 2019 | 282.3 | 12.5 | 57.6 | 212.2 | 233.6 | FY2021, 0001144980-22-000079 |
| 2020 | 442.6 | 12.6 | 46.5 | 383.5 | 391.5 | FY2021 |
| 2021 | 632.1 | 16.2 | 74.2 | **541.7** | 574.0 | FY2023, 0001144980-24-000076 |
| 2022 | 987.0 | 20.6 | 94.6 | **871.8** | 897.4 | FY2023 |
| 2023 | 705.4 | 23.5 | 142.3 | **539.6** | 614.2 | FY2023 |
| 2024 | 688.4 | 26.7 | 162.6 | **499.1** | 586.7 | FY2025 |
| 2025 | 651.4 | 27.7 | 186.0 | **437.7** | 541.3 | FY2025 |
| H1 2026 | 305.2 | 17.2 | 117.4 | 170.6 (x2 = 341) | | 10-Q Q2 2026 |

**Five-year average 2021-2025: $578.0M** (capex basis), $642.7M (D&A variant). Shown growth on the aggregate,
2021 to 2025: **-5.2% a year** (capex basis), -1.5% (D&A). Capital spending ran at 2.3x depreciation in 2025 and is
guided to "approximately $250.0 million" for 2026 (10-Q); the filing does not split maintenance from growth, so all of
it is deducted. Three of the five years (2021-2023) are the vehicle-shortage peak; see Q7 for the whole-cycle variant.

---
## THE FOUNDATIONS (not a gate)
A share is a business: "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**. For
ABG the answer turns on the debt, not on the quote: an owner who cannot be forced to sell can wait out a cycle, but the
company itself has once been at the mercy of its lenders (Q9 record). The market's $171.62, a twelve-month low, "just
tells us prices" **[M2006-077]**; no macro view on car sales, rates or tariffs enters: "we just don’t
get into the macro factors" **[M2000-094]**. The margin of safety is an attitude here and an arithmetic at Q7; if the case needs pencil
and paper, "it’s too close to think about" **[M1996-084]**.
**Contrary evidence, written down "in the first 30 minutes"** **[M1997-127]**: (1) 2008 10-K: the auditor's going-concern paragraph and
lender waivers (written at Q9 the hour it was read). (2) The 2023-2025 franchise-rights impairments, $407.7M, on
"underperformance of certain stores" (Q3, Q4). (3) The FTC enforcement action of 2024-08-16 over add-on products
(Q5). (4) Adjusted EPS in the headline with recurring exclusions (Q4). (5) Same-store new-vehicle gross profit down
24% in Q2 2026 (Q2). (6) The speakers' own dealership yardstick, "a 10 or 12 times multiple of a bad year" **[M2015-079]**, which the
price does not clearly meet on an all-equity basis (Q7).

## THE STANDING RULE
Owning ABG does not by itself put the buyer at risk of ruin if it is bought with the buyer's own money and sized as
the standing rule requires: "borrowed money has no place in the investor's tool kit" **[L2014-005]**; "if you hold it
on borrowed money, you know, you could have been cleaned out" **[M2020-022]**. The leverage inside the company is the
target's, weighed at Q9, not the buyer's.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, "a reasonable probability of being able to asses where the business will
  be in 10 years" **[M2000-037]**.
- **What the business is** (10-K FY2025, Item 1): 223 franchises at 171 locations in 15 states at year-end (202 at 158
  locations in 14 states by 2026-06-30 after divestitures), 36 brands; four lines: new vehicles (52.8% of 2025
  revenue, 20.2% of gross profit), used (29.1%, 8.4%), parts and service (13.9%, 47.9%), finance and insurance (4.3%,
  23.4%), the last including Total Care Auto (TCA), its own service-contract and GAP underwriter (2025 TCA revenue
  after eliminations $91.1M, gross profit $38.6M).
- **The key variables, "and evaluating how predictable they were first"** **[M1998-044]**: (a) new-vehicle gross profit per unit: cyclical
  and set by supply; nineteen years of filings show its range ($1,516 to $5,583, table at Q2); (b) parts and service
  gross profit: grew in every year but 2020, and fell only 6% from 2008 to 2009; (c) F&I per vehicle: about $1,002 in 2010 (F&I revenue $116.4M over
  116,156 new and used retail units, FY2010 10-K) to $2,214 in 2025 (MD&A); (d) the cost of money on $5.3B of debt
  and floor plan; (e) the prices paid for acquisitions; (f) two structural variables, the state franchise laws and the
  electric-vehicle share of the car park.
- **Do the past statements tell the future ones?** For (a) to (e), yes: the same four lines and the same unit tables run
  through every 10-K since 2007, and each line's behaviour in the 2008-09 and 2021-23 extremes is on the record. The product is opaque to me in its
  technology and need not be; the economic role (sell, finance and service a maker's vehicles inside a territory the
  law protects) has not changed in the span read.
- **The doubts, carried and not settled by preference.** The speaker who owns a dealership group says: "We like our
  dealership operation, but I don’t think I can tell you what the auto industry will look like five or ten years from
  now." and adds "you won’t see anybody that owns the market because they changed the vehicle" **[M2023-100]**. The
  first half is about the industry; the speaker separates his dealerships from it, and the same rows call dealing "a
  very good business. It’s a local business." **[M2015-011]**. And retail is the speakers' named example of a thing one
  only thinks one understands: "it’s easy to sort of think you understand retail, and then subsequently find out you
  don’t" **[M2014-052]**. The variables (f) are important; whether they are "important and knowable" **[M2006-076]** is the castle's
  question and is taken at Q2, where the routing sends a castle whose future cannot be judged.
- **VERDICT: IN.** The ten-year economics are a cyclical vehicle margin around a service business, both visible in the
  filings for nineteen years; the doubt on the structural variables is real and is carried to Q2. A stricter reader of
  "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]** could close here
  TOO HARD; I did not, because the doubt is about the castle's future, which Q2 owns.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**

**The castle tests, each with its filing fact.**
1. **The attacker with money** ("if I had a hundred million dollars and I wanted to go in and take on See’s Candy,
   could I do it?" **[M2011-015]**): a rival cannot open a Toyota store beside Asbury's Toyota store. State
   franchise laws make it "unlawful for a manufacturer to terminate or not renew a franchise unless "good cause"
   exists" and restrict competitors from "relocating their stores or establishing new stores of a particular vehicle
   brand within a specified area" (10-K FY2025, Item 1). The attacker must buy a store, and pays for the castle in the
   price: Asbury carried $4,360M of goodwill and franchise rights at 2026-06-30 (10-Q). Against that, the agreement is
   "non-exclusive", rivals with other brands and other same-brand dealers in the metro sell the same cars, and "certain
   electric vehicle manufacturers have been permitted to circumvent the state automotive franchise laws of several
   states" (Item 1).
2. **Pricing power and the agony before a rise** ("a prayer session before you raise your prices a penny"
   **[M2005-020]**): none on vehicles. Rival dealers "generally obtain new
   vehicle inventory from vehicle manufacturers on the same terms as us" (Item 1). The price is set by the rival:
   "he determined our profit, because we looked at his price every day" **[M2023-079]**. In service, gross margin
   excluding reconditioning rose from 46.9% to 48.3% in 2025 (MD&A), so labour rates are passed on.
3. **Unit volume:** 2025 same-store new units +3%, used retail units -7% ("affordability headwinds", MD&A); Q2 2026
   same-store new units -6% (10-Q).
4. **The low-cost position:** "Another way to prosper in a commodity-type business is to be the
   low-cost operator." **[L2004-007]**. Asbury's operating margin averaged 4.2% of revenue in 2010-2019 against AutoNation 4.0%, Lithia
   3.9%, Group 1 3.0%, Penske 2.8%, Sonic 2.5% (competitor row below). After interest the edge narrows: pretax margin
   2010-2019 Asbury 3.1%, AutoNation 3.2%, Lithia 3.2%. The speakers deny a scale advantage in exactly this field:
   "There are not any huge advantages of scale, at least that I’m aware of, in owning lots of dealerships."
   **[M2015-011]**; "I don’t think we’re going to get significant benefits of scale as we buy more units in the auto
   field." **[M2015-078]**. Asbury's strategy names scale ("Leverage scale and cost structure", Item 1).
5. **The brand in the customer's mind:** the brand is the maker's, sold under seventeen local group names; the
   customer asks for a Toyota, not for Asbury.
6. **Would the customer still choose it over the low bid?** ("it wouldn’t be a question of people buying candy for
   the low bid" **[M2017-009]**): for a new car, no; the gross-profit-per-
   unit history below shows buyers taking the low bid as price information spread. For warranty and recall work the
   customer has no choice: "manufacturer policies requiring that warranty and recall related repairs be performed at a
   franchised dealership" (Item 1); warranty gross profit was $226.4M in 2025, +21%.
7. **Widening or narrowing** ("could the competitive advantage have been made stronger and more durable"
   **[M2000-075]**): the vehicle half narrowed for twelve straight years before the shortage,
   the newspaper's "lost still another notch" **[L1995-023]**; the service half widened (its share of gross profit
   rose from 39.9% in 2007 to 47.9% in 2025, 49.7% in Q2 2026).
8. **Would it stand without the lord?** Partly. "In retailing, to coast is to fail." **[L1995-008]**; "retailing is a
   good case of a business where you have to stay smart" **[M1995-040]**. The 2023-2025 impairments were booked "due
   to the underperformance of certain stores" (MD&A), and the speakers' own dealer group runs on local managers "that
   have skin in the game of their own" **[M2015-078]**. Good local managers, not a superstar.
9. **What could "destroy, or modify, or reduce the economic strengths"** **[M2000-014]**: repeal or erosion of the
   franchise laws ("many states have recently passed or introduced legislation to permit direct to consumer sales of
   electric vehicles by certain companies, such as Tesla and Rivian", Item 1A); fewer service hours per electric
   vehicle; maker-set facility programmes; and, on the F&I line, regulators (the FTC action at Q5).

**The vehicle margin over nineteen years** (computed from each year's filed income statement and unit table, own-year
10-K except 2007-2009 from the FY2009 10-K, 0001193125-10-044910; `gpu.py`):

| Year | New GP per unit | Used GP per retail unit (incl. wholesale) | New gross margin | Parts and service share of gross profit |
|---|---|---|---|---|
| 2007 | $2,234 | $2,112 | 7.2% | 39.9% |
| 2008 | 2,095 | 1,939 | 6.7% | 45.7% |
| 2009 | 2,111 | 1,899 | 6.8% | 50.6% |
| 2010 | 2,062 | 1,969 | 6.6% | 45.8% (reconditioning reclassified from 2010; not comparable with 2009) |
| 2012 | 2,068 | 1,804 | 6.4% | 42.9% |
| 2014 | 2,075 | 1,699 | 6.1% | 42.6% |
| 2016 | 1,828 | 1,606 | 5.2% | 45.7% |
| 2018 | 1,569 | 1,574 | 4.4% | 46.8% |
| 2019 | 1,516 | 1,514 | 4.1% | 47.8% |
| 2020 | 2,296 | 1,944 | 5.8% | 44.4% |
| 2021 | 4,463 | 2,740 | 9.9% | 38.0% |
| 2022 | 5,583 | 2,333 | 11.5% | 37.2% |
| 2023 | 4,701 | 2,071 | 9.2% | 41.7% |
| 2024 | 3,697 | 1,629 | 7.2% | 45.8% |
| 2025 | 3,433 | 1,810 | 6.5% | 47.9% |

(The full 2007-2025 series is in `gpu.py`; the computed new GP per unit matches the filed figure where the filing
states one: 2019 $1,516, 2020 $2,296, 2022 $5,583, 2024 $3,697, 2025 $3,432.) Q2 2026: same-store new-vehicle gross
profit -24%, luxury -21%, domestic -33% (10-Q MD&A).

**The competitor row** (each company's own 10-K XBRL facts, 2010-2025; `peers/peers.py`, `peers/peers2.py`; latest
10-K accessions: AutoNation 0001628280-26-007800, Lithia 0001023128-26-000015, Group 1 0001031203-26-000064, Penske
0001628280-26-012830, Sonic 0001628280-26-010570, Asbury 0001144980-26-000051). Operating income before floor-plan
interest over tangible capital is computed as operating income / (equity + long-term debt incl. current - goodwill -
franchise rights); peers' debt tags differ, so that column is indicative only.

| | Op. margin 2010-19 | Op. margin 2020-25 | Pretax margin 2010-19 | Pretax margin 2020-25 | Op. income / tangible capital, 2013-2019 range |
|---|---|---|---|---|---|
| **Asbury** | **4.2%** | **6.3%** | 3.1% | **5.5%** | 24-28% (from the filings, after floor-plan interest: 2019 22.7%) |
| AutoNation | 4.0% | 5.5% | 3.2% | 4.7% | 27-45% |
| Lithia | 3.9% | 5.6% | 3.2% | 4.6% | 23-36% |
| Group 1 | 3.0% | 5.2% | 1.9% | 4.2% | 24-39% |
| Penske | 2.8% | 4.5% | 2.4% | 4.9% | 20-32% |
| Sonic | 2.5% | 2.6% | 1.5% | 1.6% | 15-29% |

What the row says: every franchised group earned 15-45% on tangible capital in every year of 2013-2019, years with no
shortage; the castle is the industry's (the law and the warranty rule), not Asbury's alone; Asbury is among
the better operators, not a different kind of business.

**The reading.** The castle is still standing because the law closes the territory and the maker sends its warranty
work there; it has stood through 2008-09 (service gross profit $329.5M to $309.9M while total gross profit fell 15%)
and through the decade of shrinking vehicle margins, with returns on tangible capital well above any cost of capital
for all six groups. Inside the walls the vehicle trade is a commodity: "most insureds don't care from whom they buy"
**[L2004-003]** is true of the new-car buyer, the rival sets the price, "he determined our profit" **[M2023-079]**, and
there is no scale moat, "There are not any huge advantages of scale" **[M2015-011]**. The future question, the laws and the electric car over ten to twenty years, is real; the evidence of
the span is that the law has held against fifteen years of direct-sale campaigns and that service has widened. That
is a judgment, not a measurement; the rows leave the moat alone "when we see a moat that’s tenuous in any way" **[M2000-019]**.
I judge the service-and-territory castle not tenuous over ten years and unknowable over twenty, and the vehicle trade
no moat at all.
- **VERDICT: IN, narrowly.** The castle shown is the franchised dealer's legal territory and its service bay, shared
  with every franchised competitor, not Asbury's own; the vehicle margin is a commodity and is narrowing back from the
  shortage. A castle shown open would close OUT; this one is not shown open on the evidence of nineteen years. Its
  twenty-year future is carried as the largest doubt of the run.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed:** "we’re defining it in terms of the capital actually
  needed in the business. Whether it’s a good investment for us depends on how much we pay for that in the end."
  **[M2010-090]**.
  Operating income less floor-plan interest over tangible capital (equity + debt - goodwill - franchise rights):
  22.7% (2019), 27.8% (2024), 24.9% (2025), with the inventory financed by makers' floor plan and the makers' floor-plan
  assistance ($113.4M in 2025) exceeding floor-plan interest ($91.2M). "Has it earned high returns on capital?"
  **[M1995-051]**: on the capital the stores need, yes, in good years and ordinary ones. The 2015-2016 returns on equity
  of 45-56% (XBRL) were made by shrinking equity through buybacks, which the rows discount: "if you keep the equity low
  enough by buying shares back, why, you could make return on equity whatever you want" **[M1998-017]**; and the
  2021-2023 figures were "a cyclical peak in earnings" **[L1994-009]**.
- **Reinvestment to stand still.** Capital spending ex real estate was 2.3x depreciation in 2025 ($186.0M vs $82.4M)
  and is guided to about $250M in 2026; the makers' agreements list "failure to complete facility upgrades required by
  the manufacturer" among the grounds for termination (Item 1). That is compulsory spending of the kind the speakers
  avoid: "we have tried to avoid places where there was a lot of compulsory reinvestment just in order to stand still"
  **[M1997-016]**.
- **What the added capital earned.** Growth since 2019 was bought. Acquisitions 2019-2025: $8,096M (Park Place 2020,
  Larry H. Miller 2021, Koons 2023, Herb Chambers 2025); divestitures 2019 to H1 2026: $2,095M; net about $6.0B, plus
  $666.9M of new shares in 2021 (cash-flow statements). Pretax income excluding divestiture gains and impairments rose
  from $239.3M (2019) to $723.0M (2025), +$484M on the net $6.0B, about 8% pretax, and that 2025 figure still carries a
  new-vehicle gross profit per unit of $3,433 against $1,516 in 2019. Pretax return on all capital including the
  goodwill paid for fell from 18.1% (2019) to 10.3% (2025). For capital allocation "you have to include goodwill,
  because we paid for it" **[M2011-060]**; "whether that’s good or bad depends on what we earn on that incremental
  $130 million over time" **[M2001-019]**. The 2023-2025 franchise-rights impairments ($117.2M, $149.5M, $141.0M) are
  the filing's own admission that some of what was bought is earning less than was paid.
- **WEIGHS AGAINST.** The stores earn well on the tangible capital they need, but the growth arithmetic is the second
  savings account at best and, on the acquired capital, close to the third: it "requires you to keep adding money at
  those disappointing returns" **[L2007-010]**; the earnings rose because "We just put way more capital into the
  business as we went along" **[M2023-081]**.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first:** "balance sheets over an 8 or 10 year period before I even look at the
income account" **[M2025-032]**. Filed balance sheets (10-Ks FY2017, FY2019, FY2021, FY2023, FY2025, 10-Q Q2 2026), USD millions:

| Year-end | Equity | Goodwill | Franchise rights | Tangible equity | Debt ex floor plan | Floor plan | Inventory | Cash | Retained earnings | Treasury stock |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 279.7 | 128.1 | 48.5 | 103.1 | 926.7 | 781.8 | 894.9 | 3.4 | 611.5 | (879.5) |
| 2017 | 394.2 | 160.8 | 49.6 | 183.8 | 875.5 | 732.1 | 826.0 | 4.7 | 750.3 | (919.1) |
| 2018 | 473.2 | 181.2 | 65.8 | 226.2 | 905.3 | 966.1 | 1,067.6 | 8.3 | 922.7 | (1,023.4) |
| 2019 | 646.3 | 201.7 | 121.7 | 322.9 | 939.4 | 788.0 | 985.0 | 3.5 | 1,094.5 | (1,028.6) |
| 2020 | 905.5 | 562.2 | 425.2 | (81.9) | 1,201.8 | 702.2 | 875.2 | 1.4 | 1,348.9 | (1,033.7) |
| 2021 | 2,115.5 | 2,271.7 | 1,335.7 | (1,491.9) | 3,582.6 | 564.5 | 718.4 | 178.9 | 1,881.3 | (1,044.1) |
| 2022 | 2,903.5 | 1,783.4 | 1,800.1 | (680.0) | 3,301.3 | 51.0 | 959.2 | 235.3 | 2,610.1 | (1,063.0) |
| 2023 | 3,244.1 | 2,009.0 | 2,095.8 | (860.7) | 3,206.1 | 1,785.7 | 1,768.3 | 45.7 | 2,961.5 | (1,067.3) |
| 2024 | 3,502.1 | 2,044.7 | 1,911.7 | (454.3) | 3,138.6 | 1,694.7 | 1,978.8 | 69.4 | 3,218.9 | (1,079.2) |
| 2025 | 3,891.9 | 2,281.3 | 2,097.6 | (487.0) | 3,572.0 | 2,027.0 | 2,135.8 | 40.4 | 3,616.2 | (1,092.8) |
| 2026-06 | 3,923.2 | 2,269.7 | 2,090.4 | (436.9) | 3,457.7 | 1,839.5 | 2,108.6 | 30.4 | 3,657.3 | (1,104.0) |

What the figures are saying: equity grew fourteenfold, but by retained earnings, a $666.9M share issue in 2021 and
acquisitions; goodwill and franchise rights rose from $177M to $4,360M and have exceeded equity since 2020, so the
book is the price of bought stores, not tangible capital. Debt outside floor plan rose from $0.9B to $3.5B, mostly real
estate loans and the 2029/2032 notes issued for Larry H. Miller. Inventory has been rebuilt from the 2021-2022
trough (52 days' supply of new vehicles at 2025 year-end, which the MD&A calls "well below historical levels"; 38 used). Cash is nearly nil by design: spare cash sits in the floor-plan offset
account ($150.7M at 2025 year-end) and the revolver. Retained earnings understate earnings since 2023, when retired
treasury shares began to be charged to them ($251.1M, $173.0M, $94.7M, $122.5M+$138.8M). What they cannot say: what the
franchise rights are worth if the territory laws weaken, or what a store bought at the peak will earn at a normal margin. The 2022 near-zero floor plan (the offset account held the cash) and its 2023 return show why
reported operating cash flow cannot be read raw.
- **The real costs.** Depreciation is real ("almost always true costs" **[L2015-004]**) and here understated against
  capex (Q3). Stock pay ($27.7M) is deducted. Impairments: $7.1M (2019), $23.0M (2020), $117.2M, $149.5M, $141.0M
  (2023-2025), $4.2M (Q2 2026): a recurring "non-cash" item that is the delayed cost of acquisitions.
- **EBITDA and adjusted earnings in the filer's own mouth.** The Q2 2026 release puts "adjusted EPS, a non-GAAP measure,
  of $6.82" beside GAAP $6.25 in its headline, excluding Tekion implementation expenses (also named in the 2025 SG&A discussion),
  impairments (every year), weather losses and duplicative DMS costs; it reports "Transaction adjusted EBITDA" and a
  "transaction adjusted net leverage ratio" of 3.4x (8-K 0001144980-26-000089). The bonus is paid on "earnings before
  non-floor plan interest, income taxes and depreciation and amortization" (DEF 14A). The rows: "a management that
  regularly attempts to wave away very real costs by highlighting "adjusted per-share earnings" makes us nervous"
  **[L2016-006]**; telling owners year after year not to count such costs, "when management is simply making business
  adjustments that are necessary, is misleading" **[L2016-007]**; "does management think the tooth fairy pays for
  capital expenditures?" **[L2000-036]**; "where people are talking about EBITDA, is going to be about zero"
  **[M2002-026]**. The 10-K's own MD&A uses GAAP figures and explains the floor-plan classification "in clear terms",
  with a reconciliation each year: "we can’t afford to use it as a total exclusionary factor" **[M1994-018]**.
- **Make-the-numbers habit:** no earnings guidance found in the release or 10-K; no habit found. 2024 material weakness
  (IT general controls at a vendor's DMS used by the acquired Koons stores) was remediated in 2025 (10-K Item 9A text in
  Item 1A); a control lapse, not a tell of purpose.
- **VERDICT on confusion: IN** (the accounts are understood once the floor-plan basis is rebuilt; nothing is obscure
  on purpose, "when the accounting confuses you, I would just tend to forget about it as a company" **[M1995-063]** does
  not apply). **WEIGHS AGAINST** on the featured adjusted earnings, the EBITDA-paid bonus and the recurring impairments.
  Recast earnings for Q7: the owner cash table in Step 0.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks:** the record against "the hand they were dealt" **[M1994-008]**: since 2020 the managers took a
  $7B-revenue group to $18B and kept the highest operating margin of the six (competitor row), in a shortage that lifted
  every dealer. The capital half of the record is Q6's and weighs against.
- **The proxy:** "see how they treat themselves versus how they treat the shareholders" **[M1994-009]**. Perquisites
  small (a demonstrator car and a car allowance); hedging and pledging banned; clawback; double-trigger severance; an
  independent non-executive chair until May 2026, then the outgoing CEO as executive chairman with a lead independent
  director (8-K 0001144980-25-000155). CEO pay $10.7M (2025) against beneficial ownership of 55,420 shares ($9.5M at
  today's price); the new CEO owns 3,816 shares; all fifteen directors and officers together 145,318 shares, under 1%
  (DEF 14A). Pay and ownership are read at Q6, Part B.
- **The letters and reports**, "whether the management is telling us about the things that we would want to know about
  if we owned a hundred percent of the company" **[M1998-036]**: the 10-K explains the floor-plan cash-flow split, the impairments and the
  Tekion conversion plainly; the releases lead with adjusted figures (Q4).
- **The doubt, written down.** On 2024-08-16 the FTC began an administrative enforcement action against the Company,
  three David McDavid dealerships and one general manager, alleging violations of Section 5 of the FTC Act and the Equal
  Credit Opportunity Act "in connection with the sale of add-on products" (10-K Item 3; 10-Q Part I, Note 13). Asbury
  "vigorously disputed" the allegations and sued the FTC on constitutional grounds; both remain pending and no range of
  loss is given. It is an allegation, unadjudicated, about sales practice at three of about 160 stores; it names no
  officer. The rows make doubt enough: "If you’ve got doubts, forget it." **[M2013-088]**; "we wouldn’t hire
  anybody, no matter how able, if we didn’t trust them" **[M2015-047]**; and the front-page test of a course of action
  "which, if put on the front page, you know, would make you very unhappy" **[M2016-033]**.
- **VERDICT on integrity: IN, with the doubt recorded.** No tell of dishonesty toward the owners was found in the proxy,
  the 10-Ks or the releases; the doubt is about store-level selling practice alleged by a regulator, and I read the
  integrity STOP as a judgment on the people who run the company, which the record does not impeach. A reader who takes
  the pending action as doubt about the company itself would close the file here OUT; the box below does not change.
  **Ability WEIGHS FOR** on operations (margins), **AGAINST** on capital (Q3, Q6).

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test:** "at least $1 of market value for each $1 retained", on "a five-year
  rolling basis" **[R1995-009]**. 2021-2025: net income $3,054.5M; returned by buybacks $892.0M; kept $2,162.5M, plus $666.9M raised in
  2021: $2,829.4M put to work. Market value went from $2,811M (2020-12-31, $145.74 x 19.29M shares; aggregator close,
  flagged) to $3,081M today: +$270M. Intrinsic leg: owner cash per share $19.89 (2020) to $22.76 (2025), and $19.45 on
  the whole-cycle base (Q7). The test fails on the market leg and barely moves on the intrinsic leg: "if after three or
  four years, you’ve found that the dollars we’ve retained hasn’t created more of that in value, then the presumption
  becomes very strong" **[M1998-110]**.
- **Issuance and deals.** The 2021 issue: $666.9M of new stock, roughly $171 to $176 a share (shares issued rose from
  41.13M to 45.05M in 2021, of which a small part was employee awards; FY2021 10-K), to help pay for Larry H. Miller; since 2023 the company has bought back stock at $196 (2023),
  $220 (2024), $231 (2025) and $206 (H1 2026) (shares and dollars from the 10-Ks and 10-Q). Issued at about $171 to $176,
  bought back at $196 to $231: "they sell low and then they buy high" **[M1998-027]**; issuing below value harms owners "just
  as if you issue shares beneath that figure, you are harming your shareholders" **[M1996-013]**. The deals were for
  cash and debt, not all stock, so the one STOP of Part A does not arise. No post-mortem of any acquisition against
  its projections was found in the 10-Ks: "Post mortems of acquisitions, in which reality is honestly compared to the
  original projections, are rare in American boardrooms." **[L2014-013]**. Debt-financed deals flatter per-share
  earnings: "even a high-priced deal will usually boost per-share earnings if it is debt-financed" **[L2017-004]**.
- **Buybacks.** The programme names no price: "corporate repurchase announcements almost never refer to a price above
  which repurchases will be eschewed" **[L2016-002]**; $372.7M of authority remained at 2026-05-31 (10-Q Part II).
  Under the framework's convention the prices paid are read against the bottom of the Q7 range: the 2023-H1 2026
  averages ($196-$231) sit at or below the whole-cycle bottom of $230 (Q7), so the purchases are not counted against
  on price. They were made at 3.2-3.4x "transaction adjusted net leverage", with the revolver drawn and $447.7M of debt due within a year (10-Q); whether the
  funds are "cash plus sensible borrowing capacity -- beyond the near-term needs of the business" **[L1999-023]** is
  doubtful.
- **Part B, pay, board, owners.** The bonus (80% weight) is paid on adjusted EBITDA scaled to the national new-car
  sales rate; the performance shares on one-year adjusted EPS and EPS growth relative to five dealer peers; the
  strategic objectives reward "integration of large acquisitions", the Tekion conversion and "operating margin
  relative to its peers" (DEF 14A). No charge for the $6B of capital put in, no step-up, one-year measurement periods;
  a consultant and a peer group set the levels. The rows: pay tied "to what is actually under the reasonable control of
  the person that’s being measured" **[M2003-019]**; "comp committees have become slaves to comparative data"
  **[L2005-015]**; "ratchet, ratchet, and bingo" **[M2012-095]**. Directors and officers own under 1%; the largest
  holders are index funds and three activist funds (Abrams 11.0%, Impactive 6.5%, Eminence 5.0%).
- **WEIGHS AGAINST** (Part A: retention fails, issuance low and buybacks higher, acquisitions earning about 8% pretax
  on a peak-margin year). **WEIGHS AGAINST** (Part B: paid on EBITDA and one-year adjusted EPS, no capital charge,
  little ownership).

## Q7: WHAT IS IT WORTH? STOP.
**The method and its conventions.** Value is the cash taken out, at the long government rate, as a range: "What is the
risk-free interest rate (which we consider to be the yield on long-term U.S. bonds)?" **[L2000-021]**; "working with a
range of possibilities is the better approach" **[L2000-024]**. The framework's CONVENTION: five-year average of owner
cash, carried at the growth shown (capped by Q3) for ten years, then no growth, at 5.63%; ends = no-growth and
shown-growth cases; TOO HARD if top/bottom > 3:1; OUT if the price sits inside or just below a narrower range; IN only
if no pencil is needed. Floor CONVENTION: about 10% pre-tax, "a very high probability of at least 10% pre-tax returns"
**[L2002-020]**, below which "there’s just a point at which we drop out of the game" **[M2003-149]**. Tax treatment:
owner cash is after corporate tax; 10% pre-tax is taken as 7.43% after tax at Asbury's 2025 effective rate of 25.7%
(10-K MD&A).

**Why the five-year window cannot stand alone here (PRIME RULE 2, the text wins).** Three of the five years are the
shortage peak (new GP per unit $4,463 to $5,583 against $1,516 to $2,296 before). The rows on growth bases: "If either
year was aberrational, any calculation of growth will be distorted." **[L2005-003]**; and the speakers' own rule for
this industry: "if we’re going to be in the car business forever, we’re going to have some good years and we’re going
to have some bad years. And we would rather buy at a 10 or 12 times multiple of a bad year than buy at an eight times
multiple of a good year." **[M2015-079]**. So the whole-cycle variant, which the owner asked for as reporting, is the
range this run decides on; the convention's range is reported beside it.

**Whole-cycle base (CONVENTION of this run, confessed).** Owner cash averaged 12.6% of gross profit in 2015-2019 (owner
cash $37.2M, $167.1M, $139.7M, $130.8M, $212.2M on gross profit $1,060.8M-$1,168.9M; 2015-2018 on the company's older
adjusted-OCF definition, which adds back only new-vehicle non-trade floor plan, from the FY2016 and FY2018 10-Ks,
0001144980-17-000063 and 0001144980-19-000053). Trailing twelve months' gross
profit to 2026-06-30 is $3,075.6M, of which new vehicles $585.5M; restating new-vehicle gross profit to the 2015-2019
mean per unit ($1,704 on 181,204 units = $309M) and used to its pre-peak level (about -$30M) gives whole-cycle gross
profit of $2,769M; x 12.6% = **$349M**. Cross-check: H1 2026 owner cash annualised is $341M (Step 0). Rationale: the
pre-peak conversion of gross profit into owner cash applied to today's store base with the vehicle margin restored to
its pre-peak level; it carries today's higher debt cost only through the ratio, which flatters it slightly (other
interest was 4.7% of gross profit in 2019 and 6.1% in 2025).

**COMPUTATION - NOT A CLEARANCE until the verdict line** (`q7.py`; values per share on 17.952M shares):

| Case | Base | Growth 10 yrs, then flat | Equity value | Per share |
|---|---|---|---|---|
| Convention, no growth | $578.0M | 0% | $10,266M | $572 |
| Convention, shown growth | $578.0M | -5.2% | $6,830M | $380 |
| Convention, D&A variant | $642.7M | 0% / -1.5% | $11,416M / $10,176M | $636 / $567 |
| **Whole-cycle, no growth** | $349M | 0% | $6,202M | **$345** |
| **Whole-cycle, shown decline** | $349M | -5.2% | $4,126M | **$230** |
| Whole-cycle, central (half the decline) | $349M | -2.6% | | $282 |

- **(a) VALUE RANGE: $230 to $345 a share (whole-cycle), width 1.5 to 1, against $171.62.** Convention range on the
  five-year base: $380 to $572 (width 1.5 to 1). Neither is wider than three to one, so TOO HARD by width does not arise.
- **(b) FAIR PRICE: $216.** The price at which the central whole-cycle case (base $349M, half the shown decline for ten
  years, then flat) returns 7.43% after tax, about 10% pre-tax at the 25.7% rate. On the convention's five-year base
  the same rule gives $358.
- **(c) CHEAP PRICE: $163.** My rule (CONVENTION of this run): the price at which the bottom case (whole-cycle base,
  the full shown decline) still earns the ~10% pre-tax floor after the stress the speakers name, "if interest rates go
  up another hundred basis points or 200 basis points, we’re still happy with what we’ve bought" **[M2007-096]**:
  +200bp on the $2.09B of floating-rate debt (10-Q Item 3: $20.9M a year per 100bp) cuts owner cash by $31M after tax
  to $318M. Without the stress the same rule gives $179. Rationale: below $163 even the worst whole-cycle case clears
  the floor under a rate shock, so no estimate of the normal vehicle margin decides the matter.
- **Returns at $171.62:** whole-cycle no growth 11.3% after tax (15.3% pre-tax); central 9.5% (12.8% pre-tax); bottom
  7.8% (10.5% pre-tax). The price clears the floor in every case shown, and the bottom case clears it by half a point.
- **The speakers' own dealership yardstick, on an all-equity basis** ("we evaluate acquisitions on an all-equity
  basis" **[L2017-004]**): enterprise value $6,539M (market
  cap plus $3,457.7M of debt outside floor plan, 10-Q) over whole-cycle unlevered owner cash of $489M ($349M plus
  after-tax other interest of $139M) is **13.4x after tax, 9.9x pre-tax**, against "a 10 or 12 times multiple of a bad
  year" **[M2015-079]**, and $349M is a normal year, not a bad one (2009, the last bad one, earned $38.6M pretax on
  gross profit of $613.0M). On one reading of that row (after tax) the enterprise is priced above what the speakers
  said they would pay for a dealership; on the other (pre-tax) about at it.
- **The close.** The price sits 25% below the bottom of the whole-cycle range and $8.62 above the cheap price; the
  bottom case earns the floor by half a point; the all-equity check puts the enterprise at or above the speakers' own
  multiple for dealers on a year that is not a bad one; and the business is levered 3.4x and cyclical, where "the
  larger the margin of safety" **[M1997-080]** is asked. Reaching each of these numbers took a pencil: "If you need to
  use a computer or a calculator to make the calculation, you shouldn’t buy it." **[M2009-005]**; the price should be
  "a reasonable price in relation to the bottom boundary of our estimate" **[L2013-012]**, and here it is below the
  bottom only by a margin that depends on the normal vehicle margin, which is the estimate least sure.
- **VERDICT: OUT.** Valued, the price below the bottom of the whole-cycle range, but not a screamer: the case needs a
  pencil and the speakers' own dealer yardstick does not shout. Under the convention's five-year base alone the price
  would look far below value; that base is three-fifths shortage years and is set aside under PRIME RULE 2 as stated
  above. Alert levels for the file: fair $216 (re-look), cheap $163 (no pencil needed); both are levels at which the
  file would be re-opened, not buy signals.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed OUT). For the record only: at $171.62 every case shown beats the 5.63% bond on cash yield
("one opportunity cost of buying the stock is to compare it with a bond" **[M1997-089]**); the ranking against what the operator already owns could not be done under the blind rule.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED as a clearance; the facts found are recorded because they bear on any re-look.
- **2008-09.** "Our independent public accounting firm included an explanatory paragraph in its audit report for our
  2008 financial statements that indicated there is uncertainty that we will remain in compliance with certain
  covenants in our debt agreements, and that this uncertainty raises substantial doubt about our ability to continue as
  a going concern"; the paragraph was itself a default under the revolver, the used-vehicle floor plan and the GMAC
  floor plan, cured by lender waivers and reduced credit lines (FY2008 10-K, 0001193125-09-055555). The business
  (service) held; the capital structure depended on "the kindness of strangers" **[L2008-019]**.
- **Today.** Debt outside floor plan $3,457.7M (senior notes 2028 $405M, 2029 $800M, 2030 $445M, 2032 $600M; real-estate
  loans and mortgages $1,148.6M; revolver $70.0M; 10-Q Note 9), current portion $447.7M (not itemised in the 10-Q);
  floor plan $1,839.5M due as each car is sold; Ford Credit's floor plan "can be terminated by either the Company or
  Ford Credit with a 30-day notice period" (10-K MD&A); cross-defaults across facilities; transaction-adjusted net
  leverage 3.4x against a stated target of 2.5x-3.5x. Coverage, "pre-tax earnings/interest, not EBITDA/interest" **[L2012-002]**: 4.5x on
  other interest in 2025 (4.9x before gains and impairments), 3.4x including floor-plan interest; lower on a
  whole-cycle year. "credit is like oxygen" **[L2010-020]**; "no significant near-term cash requirements"
  **[L2014-023]**. The criterion "Businesses earning good returns on equity while employing little or no debt"
  **[R1997-001]** is a STOP for a whole business only; for a stock it
  would weigh heavily against.

## Q10: IS IT THE FAT PITCH? WEIGHING.
NOT REACHED. What the draft would have the buyer do: nothing. "You wait for the fat pitch." **[M2003-070]**; at $171.62 this is not one.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Noted for any re-look: the FTC action on add-on products is the "story [...] written by an unfriendly but
intelligent reporter" **[M2008-011]** that the newspaper test asks about; F&I is 23.4% of gross profit.

---
## THE BOX
**OUT at Q7.** Value range $230 to $345 a share on a whole-cycle base ($380 to $572 on the convention's five-year base,
which is three-fifths shortage years) against $171.62; fair price $216, cheap price $163. Q1 IN, Q2 IN narrowly (the
castle is the franchised dealer's legal territory and service bay, shared with every rival; the vehicle trade is a
commodity), Q3, Q4 and Q6 weigh against, Q5 IN on integrity with the FTC doubt recorded.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Not written question by question with a commit after each: the
      instructions for this run forbade committing, and the file was written in one pass after the reading. Declared.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, and every quoted fragment beside an
      id checked inside that row); every filing fact carries its accession or the 10-K it came from; peer figures from
      their own 10-K XBRL facts with accessions.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 are marked NOT REACHED and their
      facts are recorded, not cleared. Q7's arithmetic is headed as computation until its verdict line.
- [x] Owner cash after every real cost, rebuilt from filed operating cash flow on one floor-plan basis, never a
      net-income proxy; the sovereign from the US Treasury; the price and the 2020 close flagged as aggregator.
- [x] Contrary evidence written down as found (Foundations list).
- [x] No point-in-time anchor applies (a live run); no row dated after the anchor issue arises.
- [x] Only the arithmetic lines of `tools/run.py` were used, and those lines were then replaced (wrong basis for a
      dealer).
- [x] `python tools/check_framework.py`: PASS on 2026-10-05 after this file was written (TEST RUNS: phantom ids in 0
      files). No commit made, as instructed.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The Q7 five-year convention has no rule for a window dominated by an aberrational peak.** Here three of five
years are the shortage, and the convention's range ($380-$572) would make a levered cyclical a screamer at $171.62;
I set it aside under PRIME RULE 2 on rows L2005-003 and M2015-079 (quoted at Q7) and decided on a whole-cycle base of my own
construction, confessed as a CONVENTION. Two analysts could close this name IN and OUT on that choice alone; the
framework should say when the five-year average yields to a cycle-average and how the cycle base is built. (2)
**Q7 values levered owner cash at the risk-free rate.** For a company with $3.5B of debt outside floor plan that
inflates equity value; the corpus's own correction is the all-equity view (row L2017-004, quoted at Q7), which the convention does
not apply. (3) **EBITDA talk: STOP or WEIGHING?** The framework's Q4 paragraph on why confusion is a STOP treats
the EBITDA row M2002-026 as a stop stated as a count, while Q4's heading makes the STOP confusion or suspicion only. I read EBITDA talk as a weighing
because the 10-K itself is clear; the framework should say. (4) **Q5, doubt alone, and a pending regulator's
allegation.** The framework applies the integrity STOP on doubt; it does not say whether an unadjudicated
enforcement action against the company and a store manager, naming no officer, is doubt about the people who run it.
I read it as not, and recorded the doubt; a stricter reading closes at Q5 with the same box. (5) **Q1 and Q2 share
the structural doubt** (franchise laws, electric vehicles): Q1's doubt rule (row M2002-092, quoted at Q1) would close at Q1 what
Q2's routing sends to Q2; I followed the routing. (6) **[M2015-079]'s "multiple of a bad year"** does not say pre-tax
or after tax; the all-equity check reads 9.9x or 13.4x depending on which. (7) **Operator rule 3's heading contains an
em dash**, which the operator's standing style rule forbids; written here as "COMPUTATION - NOT A CLEARANCE". (8) The
template's write-early and commit-after-each step conflicts with a run instructed not to commit; declared in the
self-audit.
