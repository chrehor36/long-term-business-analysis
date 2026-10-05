# Company Run: Mueller Water Products, Inc. (NYSE: MWA), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before any fetch.
Working folder: `Test Runs/_research 2026-10-05 MWA/` (filings as text, `q7.py` for every derived number below).

**POSITION NOTE, declared before any verdict:** not checked. The template says to check `PORTFOLIO.md`; the brief for this
run forbids opening it (blind rule), and the blind rule was kept. Whether the operator holds MWA is unknown to this analyst.

**CONTAMINATION DECLARED.** (1) The session's git context showed commit subjects naming other v5 runs and their boxes
(CTS, MOV, DBD, RES); none concerns MWA or its industry, and none was opened. (2) Listing `Test Runs/` to confirm that no
MWA run existed showed the file names of other 2026-10-05 runs (names only; none opened). (3) For method only, I read the
growth-measurement lines of `Framework/v5/tests/A2 PG - analyst 1.md` (a Procter & Gamble test record) to apply the Q7
range CONVENTION the way the PG re-test applied it. No holding, review, queue, reading-list or resume file was opened.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $22.02 (2026-10-05 intraday, Yahoo chart API; `tools/run.py` printed $21.98 the same morning). Aggregator,
  live quote only, flagged under operator rule 5. Fifty-two-week range $20.90 to $31.00 (same source, flagged).
- **Shares by class** from the latest filing's cover: **156,125,679** common, single class (10-Q for the quarter to
  2026-06-30, filed 2026-08-06, accession `0001350593-26-000036`; `python Screens/cover_shares.py MWA`). Diluted weighted
  average for the quarter 157.3M (same 10-Q).
- **Market cap:** $22.02 x 156.13M = **$3,438M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, 30-year par yield, US Treasury daily par yield curve, dated
  2026-10-02 (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K FY2025 (year to 2025-09-30, filed 2025-11-19, `0001350593-25-000066`): Items
  1, 1A, 7, 8 and notes; 10-Q Q3 FY2026 (`0001350593-26-000036`); DEF 14A for the 2026 meeting (filed 2025-12-19,
  `0001350593-25-000069`); earnings releases (8-K `0001350593-26-000034`, ex. 99.1; 8-K `0001350593-25-000054`, ex.
  99.1); officer 8-Ks (`0001350593-23-000037` CEO departure 2023, `0001350593-25-000057` CEO succession, `0001350593-26-000014`,
  `0001350593-26-000029`); prior 10-Ks for the record: FY2024 `0001350593-24-000079`, FY2023 `0001350593-23-000060`, FY2022
  `0001350593-22-000061`, FY2021 `0001350593-21-000061`, FY2020 `0001350593-20-000066`, FY2019 `0001350593-19-000064`,
  FY2017 `0001350593-17-000062`, FY2013 `0001350593-13-000043`, FY2011 `0001350593-11-000017`, FY2009 `0001193125-09-241519`.
- **One figure cross-checked against the filed statement:** net cash from operations FY2025 **$219.3M** in the filed
  cash-flow statement (10-K FY2025, p. F-8) = $219M in `tools/run.py` = XBRL first-filed value. FY2020 to FY2022 operating
  cash, capital spending and stock pay were also read off the filed statements (10-K FY2022 p. F-8; 10-K FY2020 p. F-8).
- **`tools/run.py MWA`, arithmetic lines only** (its v4 rule text, ids and floor ignored, Part VII). Its defects checked:
  its "SBC" column (11 / 14 / 15) is the total stock pay expense of Note 10; the cash-flow add-back is 8.5 / 9.0 / 10.7,
  the difference being cash-settled awards marked to fair value each period (10-K FY2025, Summary of accounting
  policies), which are already in operating cash. I deduct the add-back. Its 2017 balance-sheet row is the first-filed
  vintage before the Anvil sale was fully restated; its cash column is blank from 2022 (tag change) and was filled from
  the filed balance sheets. Its share count matches the cover.

**Owner cash after every real cost** = operating cash flow less the stock-pay add-back less all capital spending
(filed cash-flow statements; $M; depreciation variant beside it):

| FY (Sept) | Op. cash | Stock pay add-back | Capex | Depreciation | **Owner cash** | Dep. variant | Net income |
|---|---|---|---|---|---|---|---|
| 2018 | 133.1 | 5.2 | 55.7 | 20.9 | **72.2** | 107.0 | 105.6 |
| 2019 | 92.5 | 4.3 | 86.6 | 26.0 | **1.6** | 62.2 | 63.8 |
| 2020 | 140.3 | 5.3 | 67.7 | 29.6 | **67.3** | 105.4 | 72.0 |
| 2021 | 156.7 | 8.1 | 62.7 | 31.4 | **85.9** | 117.2 | 70.4 |
| 2022 | 52.3 | 8.7 | 54.7 | 32.0 | **-11.1** | 11.6 | 76.6 |
| 2023 | 109.0 | 8.5 | 47.6 | 34.4 | **52.9** | 66.1 | 85.5 |
| 2024 | 238.8 | 9.0 | 47.4 | 39.1 | **182.4** | 190.7 | 115.9 |
| 2025 | 219.3 | 10.7 | 47.3 | 39.7 | **161.3** | 168.9 | 191.7 |
| 9M to Jun-2026 | 154.2 | 10.5 | 43.6 | 31.7 | 100.1 | | 169.6 |

Five-year average FY2021 to FY2025: **$94.3M** (depreciation variant $110.9M). Trailing twelve months to June 2026:
$165.7M. Eight-year average $76.6M. FY2019 carries the $22.0M Walter Energy tax accrual (paid FY2020) and FY2022 a $98.3M
inventory build (filed statements).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**; a maker of hydrants and buried valves passes that test of attitude easily, which is why the danger here
is the opposite one, of liking the product so much that the price is excused. The market serves: the stock has fallen
from $31.00 to $22.02 inside a year, which "just tells us prices" **[M2006-077]**; the fall is no instruction either
way. Margin of safety: "if you have to actually do it on — with pencil and paper, it’s too close to think about"
**[M1996-084]**. No macro: housing starts and municipal budgets drive a third and two thirds of sales (10-K FY2025, MD&A),
and "macro conclusions are — just never enter into the discussion" **[M2000-094]**; they enter only as a property of the
business (its cycle). Who is paid to tell you: the company's releases lead with adjusted EBITDA (8-K
`0001350593-26-000034`), and management's bonus is half adjusted EBITDA (DEF 14A); that is a seller's figure.
**Contrary evidence, written down as found [M1997-127]:** (a) the castle earns its money in only part of the company:
the metering and leak-detection unit lost money in every year it was reported separately (FY2015 to FY2021); (b) the
heavy capital programme of FY2018 to FY2023 raised tangible capital by about $317M while operating income stayed near
$112M to $132M for six years; (c) the two largest distributors take about 37% of gross sales and carry competing
products (10-K FY2025, Item 1); (d) inventory rose from 16.8% of sales (FY2017) to 23.0% (FY2025) and again by $59.9M in
nine months, with the inventory reserve provision up from $3.1M to $9.4M (10-Q); (e) "strategic reorganization and other
charges" have appeared in every year from FY2014 to FY2026 and are excluded from the adjusted figures; (f) the brass
foundry announced in FY2019 for production "late in 2022" (10-K FY2021) closed the legacy foundry only in January 2025;
(g) a CEO left abruptly in August 2023 with no reason filed; (h) the five-year owner cash is less than half of the latest
year's.

## THE STANDING RULE
The buyer's conduct, not the target's: bought outright with no borrowed money, as "borrowed money has no place in the
investor's tool kit" **[L2014-005]**, a position in this name could not ruin the buyer; nothing in the target can call
on the buyer. Passed on that assumption **[M2012-081]**.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, i.e. "where the business will be in 10 years" **[M2000-037]**.
- **What the business is** (10-K FY2025, Item 1): iron gate valves, specialty valves and service brass (Water Flow
  Solutions, 58% of FY2025 sales of $1,429.7M); fire hydrants, repair products, gas tools, meters, leak detection and
  pressure management (Water Management Solutions, 42%). Some 60% to 65% of sales go to the repair and replacement of
  municipal water systems, 25% to 30% to new residential construction, about 10% to gas utilities and industry (MD&A).
  The products "are typically specified by a water utility for use in its infrastructure system", built to AWWA
  standards and NSF/ANSI 61, and sold through waterworks distributors (Item 1).
- **The key variables and how predictable they are** **[M1998-044]**: (1) the volume of buried pipe replaced and laid,
  set by aging systems, water rates (the CPI for water and sewerage up 4.6% in the year to September 2025, MD&A) and
  housing starts; (2) price against brass ingot, scrap steel, labour and tariffs; (3) whether Mueller stays on the
  utilities' approved lists. A cast-iron hydrant and a resilient-wedge gate valve in 2036 will look like the ones of
  2026; "Many of the patents for technology underlying the majority of our products have been in the public domain for
  many years" (Item 1). The forecast is about customers who change slowly, not about technology **[M2017-019]**. The
  insiders would write it down **[M2000-105]**: the company itself publishes the end-market split every year.
- **Do the past statements tell me the future ones** **[M2008-033]**? For the valve and hydrant core, yes: the
  segment's margin can be read in every year from FY2007 (Q2). The volume path is cyclical (FY2009 Mueller Co. sales fell
  from $718.1M to $547.1M, 10-K FY2009), so "how far off we can be" **[M2011-084]** is wide year to year and narrow over
  a cycle.
- **The part that cannot be foreseen.** Meters, acoustic leak detection and pressure-management software move with
  technology, and their competitors (Sensus, Neptune, Badger Meter, Itron) are named in Item 1. Read by parts, the way the
  draft reads a holding company: the unit was $89.0M of $1,111.0M sales in FY2021, the last year reported apart (10-K
  FY2021, segment note), and it lost $13.1M. It is too small to set the value and its sign is known (a drain). Seeing that
  part dimly does not put the whole outside the circle; the doubt row **[M2002-092]** was applied to the part that sets
  the earnings, and there I have no doubt that I can say what it does and roughly what it will earn.
- **Routing.** Not a fast-changing industry for the part that matters; not a bank.
- **VERDICT: IN.** The ten-year economics of buried water valves and hydrants are foreseeable in the sense of **[M2012-065]**
  and **[M2011-014]** ("I understand the economic dynamics of the industry").

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The castle question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be
standing five, 10, 20 years from now" **[M1995-038]**. The framework names no separate "specification" or "installed
base" test (a text search of the framework for "specif" and "installed base" finds only unrelated uses); the tests below
are the draft's own, applied to a specified, installed-base product.

**What the filings say keeps it standing** (10-K FY2025, Item 1): "Most municipalities have approved a limited number
of fire hydrant brands for installation as a result of their desire to use the same tools and operating instructions
across their systems and to minimize spare part inventories"; "This large installed base also leads to recurring sales of
replacement fire hydrants and hydrant parts"; for valves, "many end users are slow to transition to brands other than
their historically preferred brands"; "Our iron gate valve and hydrant products are specified for use in the largest 100
metropolitan areas in the United States". The 2011 10-K ranked the company first in the United States and Canada in fire
hydrants and iron gate valves (`0001350593-11-000017`, Item 1). The principal competitors in both are McWane, Inc. and
American Cast Iron Pipe Company (Item 1). Transport weighs against imports: "Many of our products are big, bulky and
heavy" (Item 1A).

1. **The attacker with money** **[M2011-015]**, **[M1997-103]**. To take hydrant share a newcomer needs an iron foundry,
   AWWA and UL/FM approvals, and then a place on the approved lists of thousands of utilities whose crews keep one set of
   tools and spare parts. The money does not buy the lists. Against it: two rich, well-established rivals already hold
   lists, so the attacker exists today in the form of McWane and ACIPCO; "one competitor is frequently enough to ruin a
   business" **[M2012-108]**. What the record shows is that the three have not ruined the field (test 4).
2. **Pricing power, and the agony before a rise** **[M2005-020]**. The hardest test year is FY2009: Mueller Co.
   shipment volumes fell by $196.1M (sales $718.1M to $547.1M), yet "Lower shipment volumes ... were partially offset by
   higher sales prices of $33.0 million" and "Higher sales prices in excess of higher raw material costs increased gross
   margin by approximately 2 percentage points" (10-K FY2009, `0001193125-09-241519`). In FY2008 prices rose about $27M
   against raw materials; in FY2011 pricing of $18.9M against raw-material cost of $17.1M (10-K FY2011). The same
   company's ductile-iron pipe unit, U.S. Pipe, sold against the same two competitors, cut prices by $36.3M in FY2010 and
   ran gross losses from FY2009 to FY2011 (10-K FY2011). Same rivals, same customers, same cycle: the specified,
   installed-base product held price; the commodity pipe did not. In FY2021 to FY2023 costs ran ahead of price
   (consolidated gross margin 34.0% in FY2020, 32.3%, 29.2%, 29.7%), then price caught up (34.9% FY2024, 36.1% FY2025,
   39.4% in the June 2026 quarter; 10-Ks and 10-Q). That is "over time the businesses with strong competitive positions
   manage to pass through increases in raw material costs" with "temporary situations where, sometimes, the costs are
   increasing faster" **[M2005-017]**, though the lag was two to three years, not the "three months, six months" of
   **[M2008-014]**, and the 10-K's own words for FY2022 and FY2023 put most of it on "unfavorable manufacturing
   performance", not on price resistance.
3. **Unit volume.** Not disclosed in units. Sales of the valve and hydrant core (Infrastructure segment, ex-meters):
   $702.2M (FY2015) to $1,022.0M (FY2021), much of it price and two acquisitions (Singer 2017, Krausz 2018).
4. **The low-cost position** **[L2000-017]**, **[M1997-010]**. Not shown either way: McWane and ACIPCO are private and
   publish no costs. What can be shown is margin: the Infrastructure segment (valves, hydrants, repair, without meters)
   earned operating margins of 19.5% (FY2015), 22.3%, 22.1%, 22.0%, 20.9%, 21.1% and 20.0% (FY2021) (segment notes,
   10-Ks FY2017, FY2020, FY2021); Mueller Co. earned 20.5% in FY2007 (10-K FY2009). Through the FY2009 to FY2012 trough,
   with the then-loss-making meter business inside it, Mueller Co. stayed profitable at the operating line ($50.1M ex
   impairment in FY2009, $55.2M in FY2011). This is not the "two competitors ... beat each other’s brains out" field of
   **[M2013-052]**.
5. **The brand in the customer's mind; would the customer still choose it over the low bid** **[M2017-009]**,
   **[L2004-003]**. The customer is the utility engineer who writes the specification, and he chooses on fit with the
   installed base, tools and spare parts, not on the low bid. Against it, the filing itself: specifications often name
   more than one approved brand (it says "a limited number", not one), and among the approved brands the contractor and
   the distributor can take the low bid; "Many service brass valves are interchangeable among different manufacturers"
   (Item 1), so service brass is closer to a commodity. The distributor is the intermediary of **[M2019-041]**: the two
   largest take about 37% of gross sales, carry rival lines, and are consolidating, which the 10-K says may intensify
   "Pricing and profit margin pressure" (Item 1A).
6. **Ask the competitors.** Not possible from the record; McWane and ACIPCO file nothing. Public competitor figures
   (same metric, their own filings, operating income over revenue): Watts Water (WTS, CIK 795403) 7.5% (2009), 8.5%
   (2012), 10.4% (2016), 12.0% (2020), 15.9% (2022), 18.4% (2025; 10-K `0001104659-26-018541`); Badger Meter (BMI) 16.9%
   (2009), 10.5% (2011), 13.8% (2017), 15.3% (2020), 20.0% (2025; 10-K `0001193125-26-054739`); Zurn Elkay (ZWS, as a
   water-only company from 2021) 11.7% (2021), 8.4% (2022), 12.5% (2023), 16.4% (2025; 10-K `0001628280-26-006372`).
   Mueller consolidated: 10.0% (FY2015), 12.2% (FY2017), 12.1% (FY2020), 8.9% (FY2022), 13.8% (FY2024), 18.2% (FY2025).
   Mueller's valve and hydrant core (20% to 22%) has out-earned the plumbing-products companies through the cycle; the
   consolidated company has not, because of the meter unit and corporate cost. In meters, Badger Meter's 20% margin
   against Mueller's losses says who the winner is there **[M2012-067]**.
7. **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Widening on the evidence of margin (gross margin 32.4% in
   FY2017 to 36.1% in FY2025 and 39.4% in the latest quarter; segment operating margins at records: Water Flow 30.7% in
   the June 2026 quarter, 8-K `0001350593-26-000034`) and of new domestic foundry capacity at a time of tariffs on
   imported valves and repair products. Narrowing on the evidence of distributor consolidation and, in the specialty and
   repair lines, Israeli and Chinese production carrying tariff cost.
8. **What could destroy, modify or reduce it** **[M2000-014]**: a change of pipe material that needs no iron gate valve
   (no instance found in the filings read); a utility move to lowest-bid "or equal" specifications; a well-capitalised
   importer once tariffs lapse **[M2007-116]**. None is visible in the filings as under way.
9. **A business that has taken adversity and still done well** **[M2000-032]**: FY2009 above.

**The competitor row:** WTS, BMI, ZWS as in test 6 (XBRL first-filed values of their 10-Ks, accessions as cited); McWane
and American Cast Iron Pipe: private, no filed figures, no margin obtained (flagged).

**VERDICT: IN.** The castle is the utilities' installed base and approved lists, and it has held price in the worst
volume year of the record while the same competitors' commodity pipe did not **[M2000-032]**, **[M2005-017]**. It is a
narrow castle, held by three, with a distributor between castle and customer; the narrowness enters Q7's "how sure",
not this STOP.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital the business needs** **[M2010-090]**, **[M2011-060]** (tangible: working capital excluding
  cash and debt, plus net plant; operating income before tax; filed balance sheets): FY2018 37.7%, FY2019 28.9%, FY2020
  24.7%, FY2021 26.9%, FY2022 18.8%, FY2023 19.9%, FY2024 29.8%, FY2025 40.5%. Including the $396.5M of goodwill and
  intangibles left after the write-offs, FY2025 is about 25%.
- **To stand still and to grow** **[L1999-024]**, **[M2000-144]**. Capital spending ran well above depreciation from
  FY2018 to FY2022 ($55.7M to $86.6M against $20.9M to $32.0M) to build the Chattanooga large-casting foundry, the Kimball
  plant and the Decatur brass foundry (10-Ks FY2019 to FY2023); FY2023 to FY2025 it was $47M a year against $34M to $40M
  of depreciation, and the 10-K says spending on "our two iron foundries" will rise "over the next few years" (Item 1).
  My maintenance guess, stated as a guess **[M2000-144]**: about depreciation, $40M to $45M a year; the rest has been
  growth and modernisation.
- **What the added capital earned** **[M2001-019]**: from FY2018 to FY2023 tangible capital rose from $322.9M to $640.1M
  and operating income went from $121.7M to $127.4M: six years of "we just put way more capital into the business"
  **[M2023-081]**. In FY2024 and FY2025 operating income reached $260.6M on $644.0M; the return came, late. Acquisitions
  added capital outside this measure: Krausz $140.7M (FY2019), i2O $19.7M (FY2021), Singer (FY2017); goodwill
  impairments of $6.8M (FY2022) and $16.3M (FY2024) followed (10-Ks).
- **The growth arithmetic.** Sales grew 6.1% a year FY2015 to FY2025 (with price and acquisitions); owner cash cannot be
  carried at its endpoint rate of 17.1% a year (FY2021 $85.9M to FY2025 $161.3M), because the base years were
  "aberrational" **[L2005-003]**.
- **WEIGHS FOR.** A business that earns 20% to 40% before tax on the tangible capital it needs and can reinvest some of
  it is the second grade of **[M1998-081]**, with the caution that its last big reinvestment took six years to earn
  anything **[M2012-057]**.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, FY2017 to FY2025 and June 2026** **[M2025-032]** (filed statements; `run.py` table
  checked against them). Equity rose from $488M (FY2017) to $982M (FY2025) and $1,120M (June 2026); it is small against
  the business because an accumulated deficit of $956M (FY2017), the residue of the FY2009 write-off of $717.3M of
  goodwill and $101.4M of intangibles from the 2005 purchase by Walter Energy (10-K FY2011), has been earned back to
  $(4.6)M. Of all goodwill ever booked, $740.4M of $829.6M has been written off (10-K FY2025, Note 4): the balance sheet
  says plainly that the 2005 price, and the later bolt-on prices in part, were too high. Intangibles of $300.6M are mostly
  indefinite-lived trade names ($273.0M); amortization fell from $27.1M to $7.2M in FY2025 as the 2005 customer and
  technology intangibles ran out, which lifts reported earnings by about $20M without any change in the business. Cash
  went $362M (FY2017), $177M (FY2019, after Krausz and the capital programme), $147M (FY2022), $432M (FY2025), $495M (June
  2026). Debt has been one $450M bond for a decade (now 4.0% due June 2029). Receivables fell from 17.6% of sales (FY2017)
  to 14.8% (FY2025). Inventory rose from $139M (16.8% of sales) to $329M (23.0%) and $380M in June 2026: what the figures
  "don’t say" **[M2025-032]** is whether that is tariff stock, domestic-capacity build or slow-moving brass from the old
  foundry; the 10-Q's inventory reserve provision of $9.4M in nine months (against $3.1M) and "portfolio optimization"
  write-downs point partly to the last. This is the "inventories look out of line ... with sales" tell **[M1995-064]**,
  read twice and recorded, not explained away.
- **The real costs.** Depreciation is a true cost **[R1996-023]** and I deduct capital spending in full. Stock pay is
  deducted (Step 0). "Strategic reorganization and other charges" ran $7.2M to $16.3M in every year from FY2016 to
  FY2025 and $18.9M in nine months of FY2026, plus $5.6M of warranty and $4.1M of foundry write-downs in FY2025; the
  company's adjusted figures leave them out (DEF 14A, Exhibit A). These are "business adjustments that are necessary"
  told as "Don't count this" **[L2016-007]**, a cost "attributed to a number of years" **[L1998-031]**; I count them
  (they are inside operating cash). EBITDA is in the filer's own mouth: the releases lead with "Adjusted EBITDA" and pay
  is set on it, which **[M1998-086]** calls "utter nonsense" for a business "with significant fixed assets". The
  featured adjusted figure is the tell of **[L2016-006]**.
- **The make-the-numbers habit, tested** (the two-tell CONVENTION). Guidance is given and pay rides on it; but the record
  is not one of hitting it: FY2021 guided flat to +3%, actual +15.2%; FY2022 +4% to +8%, actual +12.3%; FY2023 +6% to
  +8%, actual +2.3%; FY2024 -3% to -8%, actual +3.1% (10-Ks FY2020 to FY2024 and their following years). No habit of
  making the number is shown **[L2002-041]**, so the featured adjusted figures and the recurring charges weigh against
  and do not reach suspicion.
- **VERDICT on confusion: IN** (the accounts are plain and the segments and cash flows can be read **[M1995-063]**).
  **WEIGHS AGAINST**, modestly: adjusted EBITDA featured and paid on, recurring charges excluded, inventory out of line.
  The recast owner cash in Step 0 feeds Q7.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **People.** CEO Paul McAndrew since 2026-02-09 (joined 2022 from Emerson as head of operations; COO from August
  2023). Predecessor Marietta Zakas (CFO 2018 to 2023, CEO 2023 to 2026). Before her, J. Scott Hall "stepped down from
  all his positions" effective the next day, 2023-08-21, with no reason filed (8-K `0001350593-23-000037`). CFO Melissa
  Rasmussen since March 2025; new chief accounting officer August 2025; chief human resources officer left September 2026
  (8-K `0001350593-26-000029`). Non-executive chair (DEF 14A), so the "also Chairman" worry of **[L2014-026]** does not
  arise.
- **The record against the hand dealt** **[M1994-008]**. The hand: a castle of hydrants and valves bought by Walter
  Energy at a peak price and spun off with debt. What was done with it: debt cut from $692M (FY2010) to $450M; U.S. Pipe
  (2012) and Anvil (2017) sold; a decade of losses in metering carried and never separated; a foundry programme that
  took six years to pay; then, under the operations-trained team since 2023, gross margin up more than 600 basis points
  and record segment margins (DEF 14A letter; 10-Ks). Ability is visible in the last three years and was not in the
  seven before them.
- **The proxy** **[M1994-009]**: FY2025 CEO summary compensation $6.9M; annual bonuses paid at 199.0% of target; the
  relative-TSR award for FY2023 to FY2025 at 198.7% (DEF 14A). Directors and officers own 1.1% together; the largest
  holders are index and fund managers.
- **Tells of dishonesty.** None found in the filings read: the 10-K states its losses, impairments, warranty charges and
  the cyber incident in plain words; no too-good-to-be-true claim; no serial issuance (shares 155.8M in FY2022, 156.1M
  now). The unexplained 2023 departure is a gap, not a tell. Integrity is applied on doubt **[M2013-088]**; I have no
  doubt of the kind the row means.
- **VERDICT on integrity: IN. Ability: UNDECIDED.** A business that "doesn’t require good management" **[M1996-037]**
  has had both an indifferent decade and three good years under the present team, which has no long record of its own
  **[M2005-039]**.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the money.** Retention test **[R1995-009]**, **[M1998-110]**: from FY2016 to FY2025 net income was $969M;
  dividends $327M and buybacks $180M were paid (filed cash-flow statements, XBRL first-filed); about $460M was kept, and
  the Anvil proceeds besides. Market value went from about $1.6B (about $9.85 in January 2015, 160M shares; aggregator,
  flagged) to $3.4B: more than a dollar of market value for each dollar kept. Against intrinsic value the test is
  less kind: owner cash averaged $67M in FY2018 to FY2020 and $94M in FY2021 to FY2025; most of the gain in value is
  the last two years. The forward question, "Can you keep using all of the capital you generate, effectively"
  **[M2010-097]**: cash has piled up to $495M against a $450M bond and no stated use; the 10-K names acquisitions and
  "international opportunities" as a strategy (Item 1), and the record of the foreign bolt-ons (Krausz, i2O; Israeli,
  British and Canadian units with $6.0M of non-U.S. pre-tax income in FY2025 and a $12.7M loss in FY2024, Note 6) is
  the record of **[L1994-015]**. Buybacks: $15.0M in FY2025 and $15.5M in nine months of FY2026, a programme of "up to
  $250.0 million" with no price named (10-K MD&A), which weighs against **[L2016-002]** unless the prices paid sit at or
  below the bottom of the Q7 range. Recorded back from Q7: FY2025 and FY2026 purchases were made at prices of roughly $23
  to $30 (aggregator, flagged), above the whole Q7 range of $10.73 to $16.76, so the CONVENTION's exception does not
  apply. No stock-paid deal; no STOP.
  **WEIGHS AGAINST**: the money kept has bought, in turn, a loss-making meter business, foreign repair and software
  bolt-ons with impaired goodwill, and buybacks above value; the capital programme, late, did pay.
- **Part B, pay, board, owners.** Bonus 50% adjusted EBITDA, 25% adjusted net sales; long-term pay 25% options, 25%
  RSUs, 25% ROIC, 25% relative TSR (DEF 14A). ROIC excludes "product liability charges" and charges approved by the
  committee (DEF 14A); pay on figures that leave out real costs is pay on what "can be easily faked" **[M1996-089]**;
  relative TSR and options pay for the market's ride **[L1997-022]**. A compensation consultant and peer group set pay
  at "the 50th percentile" (DEF 14A). New CEO: severance of 300% of salary without cause (8-K `0001350593-25-000057`).
  Directors hold little stock and what they hold is mostly granted ("assumes each grantee", DEF 14A ownership table),
  not bought **[L2019-008]**. Earnings guidance is given every quarter **[L2019-006]**.
  **WEIGHS AGAINST**, without any single item that the rows make decisive **[M2007-006]**.

## Q7: WHAT IS IT WORTH? STOP.
- **How much cash** **[R1996-018]**, **[L2021-003]**: owner cash after every real cost, five-year average FY2021 to
  FY2025, **$94.3M** (CONVENTION: the five-year average). Depreciation variant $110.9M beside it.
- **Growth shown, capped** (CONVENTION, measured on the aggregate owner cash): endpoints FY2021 to FY2025 give 17.1% a
  year, and first-two-year against last-two-year averages ($37.4M to $171.9M) give a rate that is absurd on its face;
  both rest on aberrational base years **[L2005-003]**. Capped by Q3's arithmetic at the discount rate, **5.63%**
  **[M1997-095]**, **[M1999-067]**, which is also below the 6.1% a year the decade's sales show.
- **How soon, at the long government rate.** Ten years, then no growth (zero nominal, as the CONVENTION's specifics
  say), at **5.63%** **[L2000-021]**, **[M1996-025]**.

| Case ($M; per share on 156.13M cover shares) | Value | Per share |
|---|---|---|
| No-growth: 94.3 / 0.0563 | 1,675 | **$10.73** |
| Shown growth, capped: 5.63% for ten years, then flat | 2,617 | **$16.76** |
| (beside it) depreciation variant, the same two ends | 1,970 to 3,079 | $12.62 to $19.72 |
| (beside it) FY2025 owner cash $161.3M, the same two ends | 2,865 to 4,478 | $18.35 to $28.68 |

- **How sure** **[M1999-104]**: sure of the castle (Q2), less sure of the level of cash, which in five years ran from
  -$11.1M to $182.4M, with a capital cycle and an inventory cycle inside it, a housing cycle around it, and a margin that
  is at its record in the latest quarter. The range is narrow by the CONVENTION's measure, top over bottom **1.56**, so
  not TOO HARD **[L2000-025]**, **[M2007-022]**.
- **The price against the range.** $22.02 is **above the top** ($16.76; $16.64 on diluted shares). The expected return at
  the price, solving for the rate that makes the capped shown-growth stream equal $3,438M, is **4.4% after corporate
  tax** (about 5.8% before it at the FY2025 effective rate of 24.6%); on no growth, 2.7%. On the most generous base in
  the table, FY2025 owner cash at the capped growth, it is **7.2% after tax** (about 9.5% before tax), still under the
  floor. The floor (CONVENTION) is about ten percent pre-tax, the figure stated in **[M1994-004]**, **[L2002-020]**, **[M2003-149]**,
  and "there’s just a point at which we drop out of the game" **[M2003-149]**. Even the generous case needs a pencil,
  and "if you really need a calculator ... forget about the whole exercise" **[M2009-005]**.
- **Reported at the owner's request (not a rule change):**
  - **(a) VALUE RANGE (Q7 CONVENTION): $10.73 to $16.76 a share** against $22.02.
  - **(b) FAIR PRICE: about $13.40.** The price at which the central case returns the floor. Central case (mine): base
    owner cash $127.8M, the midpoint of the five-year average ($94.3M) and FY2025 ($161.3M), because the five-year
    window carries a negative inventory year and a foundry-building cycle while FY2025 sits at a record margin; growth
    2.8% a year (half the capped rate) for ten years, then flat. Rate: **7.54% after corporate tax**, the after-tax
    equivalent of 10% pre-tax at the FY2025 effective tax rate of 24.6% (10-K FY2025, MD&A); **[L2002-020]** translated
    its own 10% as "6�-7% after corporate tax" at the tax rates of 2002 (damaged character in the row); at 7.0% the fair
    price is $14.46. Value $2,088M, **$13.37 a share**.
  - **(c) CHEAP PRICE: about $8.00.** My rule: the price at which the most conservative case needs no pencil, i.e. the
    five-year-average owner cash with **no growth at all** already earns the floor: $94.3M / 7.54% = $1,250M, **$8.01 a
    share**. It sits about 25% below the bottom of the range, in the region of "25 or 30 percent less than it was worth"
    that **[M2019-002]** names for buying one's own stock, and the margin "the more volatile the business" calls for
    **[M1997-080]**. Rule and rationale are mine, not a framework CONVENTION.
- **VERDICT: OUT.** The price is above the top of the range; the expectancy at the price is below the floor on every base
  in the table; "it’s too close to think about" **[M1996-084]**.

## Q8: IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED as a clearance; the file closed at Q7. The protocol label **"COMPUTATION — NOT A CLEARANCE"** applies, written because the brief asks for
Q8 to Q10: at $22.02 the owner cash yield is 2.7% on the five-year base and 4.7% on FY2025, against the 30-year Treasury at
5.63%. On the five-year base it loses to the bond outright **[M1997-089]**, **[M2007-095]**; on the FY2025 base it beats the
bond only by its growth, by less than the "significantly higher return" the row asks **[M2007-095]**. The comparison with
more of what the buyer owns was not made (blind rule).

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED as a clearance. Record: one $450M 4.0% note due 2029, no maintenance covenants; a $175M asset-based line,
unused but for $11.1M of letters of credit; cash $495M (10-Q; 10-K FY2025 MD&A). FY2025 operating income covers gross
interest of $20.0M thirteen times; at the FY2009 trough, Mueller Co.'s $50.1M would cover this debt's $18.0M coupon
about 2.8 times **[M1995-104]**, **[L2003-016]**. "little or no debt" in the sense of **[R1997-001]**: debt is about equal to
cash. Exposures: environmental indemnity to the buyer of U.S. Pipe for the North Birmingham Superfund site, amount
undetermined (10-K Item 1, Note 15); reliance on Tyco successors' indemnities (Item 1A); product warranty (meters $9.8M in
FY2017; $5.6M in FY2025); two distributors at 37% of gross sales. None can call for sudden large sums **[L2014-023]**.
**WEIGHS FOR.**

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. The draft would have the buyer do nothing: "The harder part is to make sure that we don’t do something when
we don’t find something that makes sense" **[M1996-006]**. A good castle at a price above its value is the case of
**[L1997-006]**: "If we swing, we will be locked into low returns." It is inside the circle, so a price near $8 to $13
would make passing it the error **[M2001-006]** names.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
Hydrants, valves and leak detection for public water systems: a story by "an unfriendly but intelligent reporter"
**[M2008-011]** would find the 2021 Albertville plant tragedy and the US Pipe Superfund indemnity, neither a matter of
how the money is made. No named business. **WEIGHS FOR.**

---
## THE BOX
**OUT at Q7.** Q1 IN, Q2 IN (a narrow castle of specified, installed-base hydrants and valves that held price in FY2009),
Q3 for, Q4 IN on confusion and against on weighing, Q5 IN on integrity, Q6 against. Value range **$10.73 to $16.76** a share
(five-year owner cash $94.3M, capped growth 5.63%, at 5.63%) against **$22.02**; expectancy at the price 4.4% after tax
(7.2% on the most generous base), under the ten percent pre-tax floor. Fair price about **$13.40**; cheap price about
**$8.00**. Not a TOO HARD: the deciding question was answered.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written top to bottom. Not committed (the brief forbids commits in this
      session), so the write-early commits after each question were not made: a deviation from the template, declared.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`; no v4 ids); every filing fact has its
      document and accession; numbers not from a filing are arithmetic on filed figures (`q7.py`) or labelled CONVENTION
      or "my rule".
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; Q8 to Q10 are labelled NOT REACHED and
      carry no entry language.
- [x] Owner cash after every real cost, from operating cash less stock pay less all capital spending, never net income
      (operator rule 5); the sovereign from the US Treasury; aggregator quotes flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (Foundations, items a to h).
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used, and its stock-pay and balance-sheet defects were resolved
      against the filings.
- [x] `python tools/check_framework.py` PASS before the end of the session (see the run notes below).
- [ ] Position note: not checked, by the blind rule (declared above).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The growth cap.** The Q7 CONVENTION carries owner cash "at the growth the business has actually shown ... capped
by the growth arithmetic of Q3: no rate that runs past the discount rate". Here the shown rate (17% at the endpoints,
absurd on the two-year averages) is an artefact of a negative inventory year and a capital cycle in the base, which
**[L2005-003]** warns against, and the CONVENTION gives no rule for an aberrational base. I capped at the discount rate
itself, the literal reading; whether "runs past" means a cap at the rate or below it, and whether sales growth may stand
in when owner cash is aberrational, should be written down. (2) **The five-year window decides the box more than any
judgment.** On the five-year average the range is $10.73 to $16.76; on the latest year it is $18.35 to $28.68 and the price
sits inside it. The CONVENTION shows the depreciation variant "beside" but says nothing about a window that straddles a
capital cycle and an inventory cycle; I applied it as written and reported the latest-year case beside it. (3) **No
specification or installed-base test.** The brief referred to "Q2's specification and installed-base tests: municipal
water standards"; the framework has no test by that name, and its only "installed base" row (**[L2003-014]**) is about
insurers lacking one. I applied tests 1, 2, 4, 5 and the adversity row **[M2000-032]**; a business whose customer is the
specifying engineer and whose buyer is a distributor fits none of the eleven tests cleanly. (4) **Order of Q6 and Q7.**
Q6's buyback CONVENTION needs the Q7 range, which comes later; recorded back as the CONVENTION's specifics allow. (5)
**The template's POSITION NOTE asks for `PORTFOLIO.md`**, which a blind run may not open; the two instructions conflict.
(6) **Hard sequence against the owner's reporting request**: the brief asks for Q8 to Q10 when Q1 to Q6 pass, but the
template marks everything after a failing STOP NOT REACHED; I wrote them as COMPUTATION, NOT REACHED.
