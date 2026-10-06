# Company Run — The Home Depot, Inc. (NYSE: HD) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. The rule forbids opening
`PORTFOLIO.md`, any holding review, any earlier HD run file or research folder, the session-state files, the run queue, the
prepped reading list and `tools/alerts.json`; none was opened. **Contamination declared:** none from the repository noticed
at the time of writing. The analyst carries general prior knowledge of the company from training (a large US home-improvement
retailer, a recent large distribution acquisition), which the filings below were read to replace, not to confirm.

**Working folder:** `Test Runs/_research 2026-10-06 HD/` (notes, `run_py_output.txt`, scripts; raw filings under `cache/`,
gitignored).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** **$281.15** (close 2026-10-05, as printed by `python tools/run.py HD`; **aggregator, live quote only, flagged**
  per operator rule 5).
- **Shares by class** from the latest filing's cover: **997,689,626** common shares, $0.05 par, one class (10-Q for the
  quarter ended 2026-08-02, filed 2026-08-25, accession `0001628280-26-058715`, cover as of 2026-08-18;
  `python Screens/cover_shares.py HD`). The 10-K cover lists one class registered (common stock, NYSE); no preferred
  outstanding on the balance sheet.
- **Market cap:** $281.15 x 997.69M = **$280,500M** (my arithmetic; the tool prints $280.50B).
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`python tools/sources.py`; issuing authority). Output saved as `sources_output.txt`.
- **Filings read** (operator rule 4):
  - 10-K FY2025 (52 weeks ended 2026-02-01), filed 2026-03-18, accession `0001628280-26-019436`: Item 1, Item 5 (repurchase
    table and the pause), Item 7 (results, ROIC table, liquidity, debt, leases, cash flows), Item 7A, Item 8 statements,
    the segment note (Primary and "Other", i.e. SRS) and the GMS acquisition (Note 13, as summarised in Item 7).
  - 10-Q Q2 FY2026 (quarter ended 2026-08-02), filed 2026-08-25, accession `0001628280-26-058715`: statements, segment
    note, Note 10 acquisitions (Mingledorff's, about $1.1B, closed 2026-05-11), commercial paper, share repurchases (still
    paused), IEEPA tariff refunds (about $730M received).
  - DEF 14A filed 2026-04-07, accession `0000354950-26-000090`: MIP and performance-share design, Summary Compensation
    Table, ownership guidelines, beneficial ownership, director pay.
  - 8-K Q2 FY2026 results, filed 2026-08-18, accession `0000354950-26-000145`, EX-99.1 (the non-GAAP habit read here
    before any judgment on it).
  - 8-K filed 2026-08-12, accession `0000354950-26-000141` (Item 5.02 and EX-99.1: the chair and CEO, Edward Decker, on
    "temporary medical leave"; an office of the CEO of Ann-Marie Campbell and Richard McPhail; the CFO designated interim
    principal executive officer; the lead director chairs the board).
  - 8-K filed 2026-08-21, accession `0000354950-26-000148` (Item 5.02: $500,000 restricted stock grants to three EVPs on
    expanded portfolios).
  - Competitors: Lowe's Companies 10-K FY2025 (year ended 2026-01-30), filed 2026-03-23, accession `0000060667-26-000029`;
    Floor & Decor Holdings 10-K FY2025 (year ended 2025-12-25), filed 2026-02-19, accession `0001628280-26-009770`
    (via its XBRL; see Q2).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025
  **$16,325M** on the filed Consolidated Statement of Cash Flows (10-K `0001628280-26-019436`) against $16,325M in the
  `tools/run.py` table; total assets at 2026-02-01 **$105,095M** on the filed balance sheet against $105,095M in the tool's
  ten-year table. Both agree. One small difference found and resolved: the tool's SBC tag
  (AllocatedShareBasedCompensationExpense: 524, 444, 382) differs by $2M a year from the cash-flow statement's
  "Stock-based compensation expense" (522, 442, 380); the run uses the filed cash-flow line.
- `python tools/run.py HD`, **arithmetic lines only** (Part VII; its v4 ids, floor and verdict language ignored), extended
  to five years from the same XBRL (`history.py`, `peers.py`; outputs in the research folder):

  | FY (ends) | OCF | SBC | D&A | capex | owner cash, all capex (OCF − SBC − capex) | depreciation variant (OCF − SBC − D&A) | net earnings |
  |---|---|---|---|---|---|---|---|
  | FY2021 (2022-01-30) | 16,571 | 399 | 2,862 | 2,566 | 13,606 | 13,310 | 16,433 |
  | FY2022 (2023-01-29) | 14,615 | 366 | 2,975 | 3,119 | 11,130 | 11,274 | 17,105 |
  | FY2023 (2024-01-28) | 21,172 | 380 | 3,247 | 3,226 | 17,566 | 17,545 | 15,143 |
  | FY2024 (2025-02-02, 53 wks) | 19,810 | 442 | 3,336 | 3,485 | 15,883 | 16,032 | 14,806 |
  | FY2025 (2026-02-01) | 16,325 | 522 | 3,514 | 3,679 | 12,124 | 12,289 | 14,156 |
  | **five-year mean** | | | | | **14,062** | **14,090** | 15,529 |

  ($M.) SBC is resolved and complete: expensed in the income statement and subtracted again here because the cash-flow
  statement adds it back. D&A here includes amortization of acquired intangibles (FY2025: $607M, 10-K segment note). Finance
  lease principal payments sit in financing, not capex ($271M, $380M, $327M in FY2023 to FY2025, tool's alternate column);
  deducting them would lower the three-year mean by about $326M. **Owner cash swings with working capital** (inventory
  built in FY2022 and released in FY2023; a federal tax payment deferred from FY2024 into FY2025; the OBBBA's expensing
  lowered FY2025 cash taxes), which is why the five-year mean, not any one year, is the base. Over the five years owner cash
  averaged about 91% of net earnings; capex ran close to depreciation and amortization (0.9 to 1.05 times).
- **Ten-year balance sheets** (tool's table, first-filed XBRL; read before the income account at Q4).

## THE FOUNDATIONS (not a gate)
**A share is a business** **[M1997-109]**: the question is whether I would be content to own 2,359 home-improvement stores
and about 1,340 trade-distribution branches if the market closed for five years. **The market serves, it does not
instruct** **[M2006-077]**: the quote is used only as a price. **No macro enters** **[M2000-094]**: the filings blame
"a persisting high interest rate environment" for soft demand (10-K Item 7); that is read as a fact about the last three
years' results, not a forecast of housing. **Who is paid to tell you** **[M2020-037]**: the company's "Adjusted" earnings
add back only acquired-intangible amortization (8-K EX-99.1 `0000354950-26-000145`), and its ROIC is its own non-GAAP
measure; both are rebuilt from GAAP lines below. **Margin of safety** **[M1996-084]** governs Q7. The analyst's own risk is
the prior: a famous, admired retailer, which invites a confirmation read; "destroy our previous ideas" **[M2016-054]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. The core business has not grown for four years: Primary-segment (store) net sales $152,669M, $153,108M (53 weeks),
   $151,966M in FY2023 to FY2025; Primary operating income $21,689M, $21,313M, $20,574M (10-K segment note
   `0001628280-26-019436`). Comparable sales −3.2%, −1.8%, +0.3%; comparable transactions −2.9%, −1.0%, −1.0% (10-K Item 7).
2. Operating margin fell every year: 15.3% (FY2022), 14.2%, 13.5%, 12.7% (FY2025) (`peers_output.txt`, from filed XBRL).
3. Owner cash fell from $17,566M (FY2023) to $12,124M (FY2025); net earnings fell four years running from $17,105M.
4. The growth bought instead: SRS for $17,644M of acquisition cash in FY2024, GMS for about $5.5B in FY2025, Mingledorff's
   for about $1.1B in 2026. The "Other" segment (all of SRS and GMS) earned **$316M of operating income on $12,717M of
   sales** in FY2025, after $398M of intangible amortization (10-K segment note): about $714M before that amortization on
   some $23B of purchase price (my arithmetic).
5. ROIC as the company states it fell from 36.7% (FY2023) to 31.3% to 25.7% (10-K Item 7 table), and 24.8% trailing at Q2
   FY2026 (10-Q).
6. Buybacks paused since March 2024 "as we seek to reduce our outstanding debt"; debt on the face of the balance sheet rose
   from $23,601M (FY2016) to $55,772M (FY2025) (tool's table, 10-K Item 7).
7. The chair and CEO went on medical leave on 2026-08-12 with an office of the CEO in his place (8-K
   `0000354950-26-000141`); two named executive officers were terminated without cause in 2025 (DEF 14A).
8. The 10-K's own competition paragraph: "Online and other digital capabilities, as well as AI tools, facilitate competitive
   entry, price transparency, and comparison shopping, increasing the level of competition we face." (Item 1).

## THE STANDING RULE
A purchase of a marketable stake, paid in cash, without borrowing, and sized so that a fall of half or more could be
borne without a forced sale, carries no ruin to the buyer **[M2012-081]**, **[L2014-005]**. The target's own debt is
weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test** **[M2012-065]**: "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years", and "how the industry will develop and where the company will stand within the industry".
- **What the business is, from the 10-K** (`0001628280-26-019436`, Item 1 and the segment note): two parts. (a) The
  **Primary segment**, 2,359 home-improvement stores in the US, Canada and Mexico with their websites, HD Supply (MRO) and
  installation and rental services: $151,966M of FY2025 sales, $20,574M of operating income. Customers are DIY
  homeowners, do-it-for-me homeowners and Pros; about 30,000 to 40,000 items a store; online 15.9% of sales, "approximately
  50% of our U.S. online orders were fulfilled through a store". (b) **"Other"**, the SRS trade-distribution group (roofing
  and building products, interior and construction products from GMS, landscape, pool, and from 2026 HVAC from
  Mingledorff's): $12,717M of sales and $316M of operating income in FY2025, over 1,340 locations at Q2 FY2026.
- **The key variables and how predictable they are** **[M1998-044]**: (1) demand for repair and remodelling of an existing
  housing stock, which moves with housing turnover and rates but does not go away (three years of negative comparable
  sales, FY2023 −3.2%, FY2024 −1.8%, then +0.3%, are a cycle in the variable, not a change in its nature); (2) HD's cost and
  share position against Lowe's and a fragmented field (read at Q2 from both companies' 10-Ks); (3) whether the internet
  displaces the store. On (3) the filings show the store as the fulfillment node for half the online orders and online
  sales growing 10.4% on a comparable-week basis inside HD, not around it; the forecast is about what customers will do
  with bulky, project-based goods, not about a technology race **[M2017-019]**, **[M2023-030]**. (4) What the
  distribution group will earn on the money put into it: knowable in kind (distribution of building products is a plain
  business), not yet shown in its results (see Q3 and Q6).
- **Do the past statements tell me the future ones** **[M2008-033]**: for the store business, yes in level: Primary
  operating income stayed between $20.6B and $21.7B over FY2023 to FY2025 on flat sales, and the ten-year table shows the
  same business at larger size. For the distribution group, two years of results that include purchase accounting.
- **The retail warning, applied to myself** **[M2014-052]**: "it’s easy to sort of think you understand retail, and then
  subsequently find out you don’t"; and of "many retailing businesses", "I’m not sure I’d know where we would stand in the
  competitive pecking order five or 10 years from now" **[M1996-062]**. Retail must "stay smart" **[M1995-040]**; the
  internet "in many forms of retailing, is likely to pose such a threat" **[M1999-013]**. Against these: the pecking order in
  this industry has been the same two names for the whole ten-year table, and the two together run the store base the
  online channel fulfils from. I can name where HD will stand (first, by scale) with more confidence than I can name its
  margin.
- **Doubt test** **[M2002-092]**: I have no doubt that the store business is inside the perimeter in kind; I do have doubt
  about the level of its margin in ten years, which is a Q2 and Q7 question (how sure, how much), not a question of
  whether the economics can be pictured at all.
- **Routing:** not a fast-changing technology business **[M1998-008]**; not a bank; not a holding company. The distribution
  group is a part that matters to the future more than to the present earnings (1.5% of FY2025 operating income, 7.7% of
  sales) and is understood in kind.
- **VERDICT: IN**, narrowly, with **[M2012-065]**, **[M1998-044]**, **[M2008-033]**, **[M2017-019]**. The retail rows
  (**[M2014-052]**, **[M1996-062]**, **[M1995-040]**) are carried forward to Q2 as the reason the castle must be shown, not
  assumed.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The 1995 question **[M1995-038]**, asked of the store business first (98% of operating income), then of the distribution
group. Arithmetic in `q2_arith.py` / `q2_arith_output.txt`.

- **What keeps it standing: scale and the low-cost position** **[M1995-039]** ("a retailer that just has huge advantages in
  terms of buying cheaper and enjoying higher sales per square foot"), **[M2018-043]**, **[M2004-091]**. The filings show it:
  HD's Primary segment sold about **$619 per square foot** of store (FY2025 Primary sales $151,966M over about 245.3M square
  feet, 2,359 stores times the 10-K's "approximately 104,000 square feet" average; the Primary figure also carries HD Supply's
  MRO sales, so this overstates the store figure somewhat) against **Lowe's $440** ($86,286M over 196M square feet of
  selling space, Lowe's 10-K `0000060667-26-000029`; Lowe's figure carries a few months of its own acquisitions). Sales per
  store $64.4M against $49.1M. The same fixed store, distribution and buying costs spread over about 40% more sales is
  the cost advantage, and the gross margins are almost identical (HD 33.3%, Lowe's 33.5%), so the advantage shows up in
  operating cost, not in price: the rows' form of the castle, "not to widen our profit margin but rather to enlarge the
  price advantage" **[L1996-016]**.
- **The money test** **[M2011-015]**: could a well-funded attacker take it? The best-funded attacker for thirty years has been
  Lowe's, with the same format, the same suppliers and ex-Home Depot executives in four of its senior roles (Lowe's 10-K,
  executive officers). It remains at 57% of HD's Primary sales on 80% of its selling space. Floor & Decor, the specialist
  attacker, earns a 5.8% operating margin on $4,684M of sales (its 10-K XBRL, `0001628280-26-009770`). No new national
  entrant appears in either 10-K's competition paragraph; the named threat is "online" and "AI tools" that "facilitate
  competitive entry, price transparency, and comparison shopping" (HD 10-K Item 1).
- **Pricing power and the agony before a rise** **[M2005-020]**, **[M2005-017]**: weak, as for any retailer of largely
  branded and commodity goods (lumber, building materials). What the filings show is pass-through, not power: tariffs in
  FY2025 were offset by "diversification efforts and some price increases" with gross margin held at 33.3% (10-K Item 7).
  The castle is the cost position, not the price.
- **Unit volume and share of mind** **[M1999-054]**: transactions fell: comparable transactions −2.9%, −1.0%, −1.0% in FY2023
  to FY2025 and −1.2% in the first half of FY2026 (10-K Item 7; 8-K EX-99.1 `0000354950-26-000145`), with ticket rising.
  Against the nearest rival, the share held: comparable sales HD −3.2%, −1.8%, +0.3% against Lowe's −4.7%, −2.7%, +0.2%;
  Lowe's comparable transactions −2.8% in FY2025 against HD's −1.0% (Lowe's 10-K, Other Metrics table). Volume fell for
  the industry; HD lost less of it.
- **Would the customer still choose it over the low bid** **[M2017-009]**, **[L2004-003]**: the DIY customer can compare
  prices, and the 10-K says so. The Pro customer buys on delivery, credit, job-lot depth and location (10-K Item 1), which
  the scale of the store and fulfilment network supplies; this is the part of the custom HD is spending to deepen.
- **The competitor row** (same metric, each company's own 10-K):

  | Company, fiscal year | Net sales $M | Operating margin | Comparable sales | Sales per sq ft | Owner cash / sales (5-yr) | Accession |
  |---|---|---|---|---|---|---|
  | Home Depot, FY2025 (Primary segment) | 151,966 | 13.5% | +0.3% | ~$619 | 9.0% (whole company) | `0001628280-26-019436` |
  | Lowe's, FY2025 | 86,286 | 11.8% (12.1% before $321M acquisition costs) | +0.2% | $440 | 7.9% | `0000060667-26-000029` |
  | Floor & Decor, FY2025 | 4,684 | 5.8% | (not computed) | (not computed) | negative to 5.2% by year | `0001628280-26-009770` |

  (Owner cash / sales is the five-year mean of OCF − SBC − capex over sales, `peers_output.txt`.)
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**, **[M2000-075]**: **narrowing, on the evidence, and I write it
  down** **[M1997-127]**. HD's operating margin against Lowe's: FY2021 15.2% against 12.6% (a 2.6-point gap); FY2023 Primary
  14.2% against 13.4%; FY2024 13.9% against 12.5%; FY2025 13.5% against 12.1% before Lowe's acquisition costs (1.4 points).
  The gap has roughly halved in four years while both margins fell. Part of the fall is the demand cycle the rows tell the
  analyst to separate from the castle ("you should view last year's figures as reflecting a cyclical problem, not a secular
  one", said of a bad year in which "we at least maintained [...] our competitive superiority" **[L1995-022]**), and HD's comparable sales held better than Lowe's in
  each of the three bad years. Part is cost: Primary SG&A rose from $26,598M to $28,885M (FY2023 to FY2025) on flat sales,
  "higher payroll and related costs" (10-K Item 7). The rival closing half the margin gap is the fact that would, if it
  continued, show the castle filling in; it has not closed it.
- **What could destroy, modify or reduce it** **[M2000-014]**: the internet is the named threat **[M1999-013]**,
  **[M2012-047]** ("anything that can be easily bought by using a home computer"). Much of HD's assortment cannot easily be
  bought that way (lumber, building materials, appliances needing installation, job-lot Pro orders), and half its own online
  orders are filled from the store; the threat is real at the small-item, price-comparable end of the assortment and not, on
  this evidence, at the project end. Retail "you have to stay smart" **[M1995-040]**: the castle depends on continued
  execution, which is why Q5 matters more here than for a See's.
- **The distribution group (SRS, GMS, Mingledorff's)**: a castle not yet shown. Specialty building-products distribution is
  fragmented and competitive (10-K Item 1); the group earned an operating margin of 2.5% in FY2025 after amortization, 5.6%
  before it (`q2_arith_output.txt`). It is a small part of today's earnings and is weighed at Q3 and Q6 as capital
  allocation, not as the castle that carries the company.
- **VERDICT: IN**, narrowly, with **[M1995-038]**, **[M1995-039]**, **[M2011-015]**, **[M2018-043]**, **[M1999-108]**: the
  store castle stands on a cost and scale position the competitor row shows, held through three years of falling volume;
  it is narrower than it was, which is recorded and carried into "how sure" at Q7 **[M1999-104]**. It is not shown open
  (no rival has crossed it) and its future can be judged (no fast technological change in the core goods), so neither OUT
  nor TOO HARD **[M2000-019]**, **[M2006-013]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
Arithmetic in `q3_arith.py` / `q3_arith_output.txt`, on the filed balance sheets and the tool's ten-year table.
- **Return on the capital the business needs** **[M2010-090]**, **[M2011-060]** (forget purchased goodwill when judging the
  business; include it when judging the allocation). Net tangible operating assets at 2026-02-01 (receivables, inventory,
  other current assets, property, lease right-of-use assets and other assets, less payables, accrued pay, sales tax,
  deferred revenue, income tax payable, other accrued and other long-term liabilities; 10-K balance sheet) were
  **$46,946M**; operating income before acquired-intangible amortization was $21,497M, a **45.8% pre-tax** return (53.8% in
  FY2024). On the cruder measure the tool's table allows across ten years (equity plus debt on the face, less cash, less
  goodwill and intangibles, leases left out), the pre-tax return on tangible capital was 57.6% in FY2016, 66.1% in FY2019 and
  62.3% in FY2025. The store business earns very high returns on the tangible capital it needs **[M1995-051]**,
  **[M1998-081]**, and they are not the product of a cyclical peak, a monopoly price or leverage in the operating assets
  **[L1994-009]**: they held through FY2023 to FY2025 on flat sales.
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**: capex ran 0.9 to 1.05 times depreciation
  and amortization over FY2021 to FY2025 and is guided at "approximately 2.5% of projected fiscal 2026 net sales", about
  $4B, covering "building new stores and maintaining existing stores" (10-K Item 7); the plan is about 80 new stores over
  five years from FY2023 (10-K Item 1), against 2,359 existing. The filing does not split maintenance from growth capex; my
  stated guess is that maintenance sits near depreciation **[M1998-127]**, and the Q7 convention deducts all capex anyway.
  Inventory rose from $12,549M (FY2016) to $25,817M (FY2025), from 13% to 16% of sales (tool's table), and receivables from
  $2,029M to $5,597M as the Pro and distribution business grew: working capital is the store business's real growth cost.
- **What the added capital has earned** **[M2001-019]**, **[M2023-081]**, written down as found **[M1997-127]**. Total
  capital including goodwill (equity plus debt on the face, less cash) rose from $25,396M (FY2016) to $67,196M (FY2025);
  operating income rose $7,463M, an **incremental pre-tax return of 17.9%** over nine years. Split at FY2021: FY2016 to FY2021
  added $10,651M of capital and $9,613M of operating income (the pandemic boom and the HD Supply purchase); **FY2021 to
  FY2025 added $31,149M of capital and operating income fell $2,150M**. Most of that capital is the distribution group:
  $24,387M of acquisition cash from FY2024 to the first half of FY2026 (SRS, GMS, Mingledorff's; cash-flow statements),
  which earned $714M before amortization in FY2025 (5.6% of its sales, about **3.1% pre-tax** on the FY2024 and FY2025
  purchase cash) and $507M in the first half of FY2026 (10-Q segment note `0001628280-26-058715`). GMS was owned only from
  2025-09-04 and SRS's results are seasonal, so a full year will read higher; even doubled, the return on the purchase
  money would be a single-digit pre-tax figure, below the 5.66% bond after tax. This is the "worst" grade of
  **[M1998-081]** applied to the added capital, not to the business: growth bought at "a very low rate of return".
- **The growth arithmetic and its caps** **[M2003-120]**, **[M1997-095]**, **[M1999-067]**: the store business throws off
  far more cash than it can reinvest at its own high rate (80 stores over five years, capex near depreciation), which is
  the "great business" pattern of **[M2003-120]**: "They do not generate lots of opportunities to earn high returns on
  incremental capital." The surplus has gone, since 2024, to dividends, to debt repayment and to distribution
  acquisitions at low returns rather than to buybacks (Q6). Primary-segment sales were flat over FY2023 to FY2025, so no
  growth rate above about zero is shown for the core (Q7).
- **WEIGHS FOR on the capital the store business needs, AGAINST on what the added capital has earned; overall
  UNDECIDED**, with **[M1998-081]**, **[M2010-090]**, **[M2011-060]**, **[M2001-019]**, **[M2003-120]**: a business that needs
  little capital to stand still, whose recent added capital earns little.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten year-ends, FY2016 to FY2025** **[M2025-032]** (tool's table from first-filed XBRL; the
  FY2025 and FY2024 columns read on the filed 10-K balance sheet, `0001628280-26-019436`). What moved and why:
  - **Equity against the buybacks.** Equity went from $4,333M to −$1,878M (FY2018) and −$3,116M (FY2019), back to $3,299M,
    −$1,696M (FY2021), and up to $12,813M (FY2025). Retained earnings rose every year, $35,519M to $94,537M; the swings are
    treasury stock, $95,971M at cost for 806M shares at 2026-02-01 (filed balance sheet), against 1,802M issued. Equity
    rose from FY2024 only because buybacks stopped in March 2024. Return on equity is therefore not a measure here
    **[M1998-017]**, **[M2001-054]**; the run uses returns on operating capital (Q3).
  - **Goodwill and intangibles against equity.** Goodwill $2,093M to $22,344M and intangibles to $10,329M, almost all in
    FY2021 (HD Supply) and FY2024 to FY2025 (SRS, GMS). Together $32,673M, against equity of $12,813M: every dollar of
    book equity and more is purchased intangibles.
  - **Cash** is small throughout ($1,389M to $3,760M, except $7,895M in FY2020), $1.0B of the FY2025 figure held abroad
    (10-K Item 7). The company runs on commercial paper ($4,464M at year-end, peak $5.8B in FY2025, $6.2B in the first half
    of FY2026).
  - **Receivables and inventory against sales.** Sales rose 74% from FY2016 to FY2025 ($94,595M to $164,683M); inventory rose
    106% ($12,549M to $25,817M) and receivables 176% ($2,029M to $5,597M). Inventory turns fell to 4.4 from 4.7 (10-K Item 7);
    first-half FY2026 inventory $26,847M against $24,843M a year earlier, +8.1%, with sales +5.3% and the acquisitions
    explaining part (10-Q). Receivables follow the Pro and distribution mix, which sells on trade credit. Neither builds out
    of line with an explanation the filing gives; I note the trend, not a tell **[M1995-064]**.
  - **Debt** on the face $23,601M to $55,772M; it financed buybacks to FY2023 and the acquisitions after.
  - What the figures "can’t say" **[M2025-032]**: what the distribution group will earn in a normal year; the split of
    capex between maintenance and growth.
- **The real costs.** Depreciation is charged and capex has run at about depreciation **[R1996-023]**, **[L2015-004]**.
  Stock pay of $522M is expensed and is subtracted again in owner cash **[L2015-003]**, **[L2021-003]**. No recurring
  restructuring charges in FY2023 to FY2025 found in the income statements; the one non-recurring item named is a
  "non-recurring legal-related benefit recognized during fiscal 2024", a gain, not a charge (10-K Item 7). Self-insurance
  reserves are booked undiscounted on actuarial estimates (10-K Note 1). No defined-benefit pension found in a text search
  of the 10-K for "pension" and "defined benefit".
- **EBITDA in the filer's own mouth** **[M1998-086]**, **[M2002-026]**: not in the earnings release, the 10-Q or the proxy
  (text search, zero hits); once in the 10-K, as a target in performance-share awards granted to SRS employees (10-K
  stock-compensation note). Carried to Q6 Part B.
- **Adjusted figures** **[L2016-006]**, **[L2012-003]**: the release leads with GAAP net earnings and EPS, then gives an
  "Adjusted" EPS that adds back only acquired-intangible amortization ($4.92 against $4.79 GAAP in Q2 FY2026; 8-K EX-99.1
  `0000354950-26-000145`). Amortization of acquired customer relationships in a distribution business is closer to a real
  expense than not **[L2012-003]**; owner cash here is computed from operating cash flow and is unaffected. The company's
  ROIC divides NOPAT by long-term debt and equity and leaves out commercial paper and leases (10-K Item 7 definition), which
  flatters it a little; the run does not use it.
- **The make-the-numbers habit** **[L2002-041]**, **[L2000-037]**: the company gives annual guidance (FY2026: sales growth
  about 2.5% to 4.5%, EPS "approximately flat to 4.0%", reaffirmed 2026-08-18) and its Q2 release says "Our second quarter
  results exceeded our expectations". That is one tell. A second was looked for and not found: reserves that move, prepaid
  or deferred accounts building, profits on both sides of a contract. Under the two-tell CONVENTION (framework Q4, ours),
  it weighs against and is not suspicion.
- **Clear speech** **[M1994-018]**: the 10-K explains the fall in operating cash flow (vendor timing, inventory, the
  deferred tax payment, OBBBA), the pause in buybacks and why ROIC fell ("higher average equity due to our ongoing pause in
  share repurchases") in plain terms.
- **The recast earnings for Q7**: owner cash after every real cost, five-year mean **$14,062M** (STEP 0), depreciation
  variant $14,090M; both after interest, taxes and stock pay.
- **VERDICT on confusion: IN** (the accounts can be read and nothing in them confused me **[M1995-063]**, **[M2003-029]**).
  **WEIGHS AGAINST, mildly**, with **[L2002-041]**, **[L2016-006]**: annual guidance, an adjusted EPS, and an EBITDA target
  in one subsidiary's pay; none is a second tell.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stake the speakers read rather than meet **[M2007-081]**; what follows is read from the filings.
- **Who.** Edward P. Decker, chair, president and CEO (CEO since March 2022, chair since October 2022, earlier president and COO and EVP
  U.S. stores; DEF 14A `0000354950-26-000090`), on "temporary
  medical leave" since 2026-08-12; the company "expects Decker to return within the next few months" (8-K
  `0000354950-26-000141`). In his place an office of the CEO: Ann-Marie Campbell, senior EVP, who "began her career with the
  Company in 1985 as a cashier", and Richard McPhail, EVP and CFO since 2019, with the company since 2005 and now the
  interim principal executive officer; the independent lead director, Gregory Brenneman, chairs the board. No change to
  the two executives' pay for the added duties (same 8-K).
- **Yardstick one, the record against the hand dealt** **[M1994-008]**: the hand since FY2022 was falling housing turnover
  and high rates (10-K Item 7). Against the same hand Lowe's comparable sales were worse in each of FY2023 to FY2025 and
  its transactions fell faster in FY2025 (Q2). HD's operating margin fell 2.6 points in four years with flat Primary sales,
  partly from wage investment the 10-K names. The operators held the store business's position; they did not hold its
  margin.
- **Yardstick two, how they treat the owners** **[M1994-009]**: the proxy shows CEO total compensation of $16,191,127 for
  FY2025 (Summary Compensation Table) against $14,156M of net earnings, about 0.1%; his base salary "remained unchanged since his appointment" in 2022, held "At Mr. Decker’s request"; the MIP paid 95% of target in a year
  of results between threshold and target. The CEO holds stock worth 34.8 times salary against a 6 times guideline;
  hedging and pledging are prohibited (DEF 14A). Directors and executive officers as a group hold 0.08% (769,244 shares plus
  418,247 deferred units). Nothing in the proxy shows the managers treating themselves better than the owners in a way
  that stands out; Part B of Q6 weighs the design.
- **The tells of dishonesty** (**[M2002-028]**, **[M1995-111]**, **[M2004-067]**, **[M2007-082]**), looked for in the 10-K,
  the 10-Q, the release and the proxy: none found. The key figures of the industry (comparable sales, transactions, ticket)
  are reported every quarter, bad years included; the ROIC fall is explained in plain words; the fall in operating cash
  flow is explained line by line. The one legal matter disclosed is an EPA lead-safe consent decree in the installation
  business, terminated in FY2025 after about $1.7M of stipulated penalties that the company "collected [...] from our
  third-party installers" (10-K Item 3). The proxy's independent-chair proposal (a shareholder's text, not the company's)
  cites three missed quarters and a lowered FY2025 outlook; a management that lowers its outlook is missing its numbers,
  not making them.
- **How they talk about mistakes** **[L2024-003]**: no instance found of "mistake" or "fell short" in the 10-K, the proxy or
  the Q2 release (text search); the documents describe headwinds, not errors. A weak point, common to large companies; the
  acquisitions' returns (Q3) are not discussed against the prices paid **[L2014-013]**.
- **Love of the business** **[M2000-098]**: the senior people are long-tenured insiders (Campbell from cashier in 1985,
  McPhail since 2005, Decker CEO after earlier HD roles), the culture is described in the 10-K as the "inverted pyramid", and
  the founders' values are invoked in every filing; I cannot test love from filings beyond that tenure. Two named
  executives were terminated "without cause" in 2025 (EVP U.S. stores; CIO) with no reason given (DEF 14A).
- **What ability shows in** **[L1995-006]**, **[M1995-040]**: retail needs management that stays smart; the record of keeping
  share in a bad cycle weighs for; the acquisitions' returns (Q3, Q6) weigh against the capital half of ability, which Q6
  carries. The CEO's leave adds a short-term uncertainty, and "the number one risk factor is that this business gets the
  wrong management" **[M2021-042]**; the stand-ins are insiders of twenty and forty years.
- **VERDICT on integrity: IN** (applied on doubt **[M2013-088]**, **[M2015-047]**; no doubt found). **Ability: WEIGHS FOR,
  narrowly**, with **[M1994-008]**, **[M1995-040]**: operators who held the position against the nearest rival through three
  bad years, under a leader now on leave.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
Arithmetic in `q6_arith.py` / `q6_arith_output.txt` (filed XBRL of the 10-Ks).

**Part A, the money.**
- **The stated order of uses** (10-K Item 1 and Item 7): reinvest in the business, then a quarterly dividend, then
  "return excess cash to our shareholders through share repurchases"; repurchases paused "In March 2024 [...] in
  connection with the SRS acquisition" with no plan to resume in FY2026 "as we seek to reduce our outstanding debt". The
  order is the rows' order **[L2012-011]**, **[L2021-005]**; what matters is the price paid at each step.
- **The retention test** **[R1995-009]**, **[M1998-110]**, **[M2011-072]**. Over FY2021 to FY2025 net earnings were
  $77,643M; dividends took $41,238M (53%) and buybacks $30,105M (39%), leaving about $6,300M kept, while $24,989M went to
  acquisitions, the difference borrowed. The market's verdict on the five years, in the company's own performance graph
  (10-K Item 5): $100 in HD at the end of FY2020 became $156.25 with dividends, against $164.12 for the S&P 500 Retail index
  and $200.82 for the S&P 500. The intrinsic leg: operating income fell from $23,040M to $20,890M while total capital rose
  $31,149M (Q3). On both legs the money kept and borrowed since FY2021 has not yet shown a dollar of value for a dollar
  spent; the span is short for the acquisitions **[M1998-110]**.
- **Deals: value given against value got** **[L1994-015]**, **[M2007-123]**, **[L2014-012]**: all paid in cash, so the
  all-stock STOP **[L2009-019]** does not arise, and there is no serial issuance of shares **[L2014-015]** (diluted shares
  fell from 1,078M to 995M, FY2020 to FY2025). But the cash bought, in FY2025, $714M of pre-amortization operating income
  on about $23B (Q3), which is value given well above value got unless the distribution group's earnings rise several-fold.
  The 10-K presents the deals as strategy ("to accelerate the vision of becoming a leading, multi-category building
  materials distributor") with no post mortem against the price **[L2014-013]**; a third purchase (Mingledorff's, about
  $1.1B) followed in 2026, and an "Office of Pro Acceleration" now coordinates the acquired businesses (8-K
  `0000354950-26-000148`). The rows' warning about the forces that "push toward deals" applies **[M2014-076]**.
- **Buybacks** **[L1999-023]**, **[L2016-002]**, **[L2011-003]**: the authorization ($15.0B, August 2023, about $11.7B unused)
  names no price and "does not have a prescribed expiration date" (10-K Item 5). Average prices paid, approximate from
  dollars and shares tagged in the 10-Ks (shares in whole millions): about $181 (FY2018), $219 (FY2019), $333 (FY2021),
  $310 (FY2022), $311 (FY2023), $300 (FY2024). Under the buyback CONVENTION (framework Q6, ours) a programme with no stated
  price weighs against unless the prices paid sit at or below the bottom of the Q7 range; the check is run at Q7 and
  recorded back here. The buybacks to FY2023 were also partly borrowed: debt on the face rose from $31,483M to $44,111M
  over FY2019 to FY2023 while equity stayed near zero (tool's table); the rows' first condition is funds "beyond the
  near-term needs of the business", counting "sensible borrowing capacity" **[L1999-023]**.
- **Dividends** **[M2004-089]**, **[L2012-015]**: paid every quarter since 1987, raised in February 2026 to $2.33 a quarter
  (10-K Item 5 and Item 7); $9,152M in FY2025, 65% of net earnings and 75% of owner cash. A business that cannot reinvest its
  own cash at its own high rate should pay out, and this one does; the policy is clear and consistent. For.
- **Part A: WEIGHS AGAINST**, with **[L1994-015]**, **[M2007-123]**, **[L2016-002]**, **[M1998-110]**: a sound dividend, but
  the money not paid out has gone since 2021 to buybacks at prices not tested against value and to about $24B of
  acquisitions earning a low pre-tax return on their price so far.

**Part B, the pay, the board, the owners.**
- **Pay tied to what the person controls** **[M2003-019]**, **[M2016-083]**: the FY2025 cash bonus (MIP) was weighted 50%
  on sales (raised from 40% "to more closely align the MIP structure with drivers of shareholder value creation in recent
  years"), 30% on operating profit, 10% on inventory turns and 10% on a Pro sales goal (DEF 14A). Acquired sales are removed
  only in "the year of acquisition or disposition"; after that year bought sales count toward the largest weight. "you get
  what you reward for" **[M2016-083]**: half the bonus rewards revenue regardless of the capital used to get it, in a
  company that has just bought about $24B of revenue-producing businesses at low returns. Against this, the performance
  shares (50% of equity) pay on three-year average ROIC and operating profit, and ROIC charges for the capital
  **[L1994-019]**, **[M1995-010]**.
- **The bar** **[L1996-019]**: for the FY2025 to FY2027 performance shares "each year’s target [is] determined by applying the
  pre-established rate of change to the prior year’s actual results", so a bad year lowers the next year's bar; the FY2023
  to FY2025 award paid 70.1% on results between threshold and target, and the FY2025 MIP paid 95% of target with every
  financial measure between threshold and target (DEF 14A). A plan that resets on actuals leans toward "heads I win, tails
  you lose" **[L1994-020]** more than a fixed bar does; the FY2026 MIP raised the sales threshold to 95% and cut threshold
  pay to 25%, a move the other way.
- **Options** **[L1994-021]**, **[M1997-043]**: 20% of executive equity is fixed-price options vesting over five years, with no
  step-up for retained earnings; the cost is expensed **[L1998-028]**. A flaw the rows name, small in weight.
- **EBITDA in pay** **[M1998-086]**: SRS employees' performance shares pay partly on "SRS earnings before interest, taxes,
  depreciation and amortization" and sales targets (10-K stock-compensation note); the capital charge is absent where the
  capital was largest.
- **The board** **[L2014-026]**, **[L2019-008]**, **[M2009-086]**: chair and CEO combined, with an independent lead director
  since 1998; shareholders rejected an independent-chair proposal in 2025 with 73% of votes against (DEF 14A). Directors'
  own holdings are small and mostly deferred units received as fees (none to 10,065 shares owned outright for ten of the
  eleven non-employee directors listed; the lead director 66,043); the retainer is at least two-thirds equity. Pay is set
  with an outside consultant (Pay Governance) and a retail peer group **[M2004-016]**, **[L2005-015]**.
- **The owners** **[L1994-023]**, **[M2022-054]**: full quarterly disclosure of the industry's key measures; annual earnings
  guidance given.
- **Part B: WEIGHS AGAINST, mildly**, with **[M2016-083]**, **[L1994-021]**, **[L1996-019]**, **[L2014-026]**: modest pay for
  the size, high ownership by the CEO, no pledging, but a bonus that pays half on revenue, a bar that resets on actual
  results, plain options, and an EBITDA target in the acquired business.

## Q7 — WHAT IS IT WORTH? STOP.
Reached: Q1 IN, Q2 IN, Q3 weighed, Q4 IN and weighed, Q5 IN and weighed, Q6 weighed. Script `q7.py`, output `q7_output.txt`.

- **How much, how sure, how soon, at the long government rate** **[L2000-021]**, **[M1996-025]**. The CONVENTION range
  (framework Q7 and Part VI, ours): five-year mean owner cash after every real cost, **$14,062M** (FY2021 to FY2025, all
  capex deducted) **[L2021-003]**, **[L2005-003]**; carried ten years at the growth shown on the aggregate owner cash, never
  above it, then at zero nominal growth, discounted at **5.66%**.
- **The growth shown.** Endpoint to endpoint, $13,606M (FY2021) to $12,124M (FY2025): **−2.84% a year**. A log-linear fit
  through the five years gives **+1.26%**, because the middle years (FY2023, FY2024) were high on working-capital release.
  The convention does not say which (the same gap TSCO's run reported); both are shown. Either flatters the business:
  FY2024 and FY2025 owner cash include the earnings of SRS and GMS, bought for about $23B of acquisition cash that the
  convention's owner cash does not deduct; and the core (Primary segment) showed no sales growth over FY2023 to FY2025 and
  falling operating income (Q2, Q3). No positive growth rate is shown for the business without the purchases.

  | Case | Owner cash base | Growth, years 1 to 10 | Value $M | Per share (997.69M) | Expected return at $281.15 |
  |---|---|---|---|---|---|
  | Shown growth, endpoint (bottom) | 14,062 | −2.84% | 198,619 | **$199.08** | 3.9% |
  | No growth (top) | 14,062 | 0% | 248,442 | **$249.02** | 5.0% |
  | Shown growth, log-fit (shown for the gap) | 14,062 | +1.26% | 274,429 | $275.06 | 5.5% |
  | Depreciation variant, endpoint / no growth / log-fit | 14,090 | −1.98% / 0% / +1.94% | 213,030 / 248,940 / 290,335 | $213.52 / $249.52 / $291.01 | 4.3% / 5.0% / 5.9% |

  Owner cash is after interest, so the equity value is read directly; the debt is carried as rolled, which Q9 would test.
  Deducting finance-lease principal (about $326M a year in FY2023 to FY2025) would lower every value by about 2%.
- **How sure** **[M1999-104]**, **[L2005-001]**. Sure of the level of the store business's earnings within a band (Primary
  operating income $20.6B to $21.7B over FY2023 to FY2025; owner cash $11.1B to $17.6B by year, the swings working capital
  and tax timing, Step 0). Unsure of the direction: a castle narrower than it was against Lowe's (Q2), and $24B of added
  capital earning about 3% pre-tax so far (Q3). The range is **1.25 to one** ($199.08 to $249.02; 1.38 to one with the
  log-fit top), far inside the CONVENTION's three to one, so it is not TOO HARD on width **[L2000-025]**, **[M2007-022]**.
- **The floor (CONVENTION), about ten percent pre-tax** **[M1994-004]**, **[L2002-020]**, **[M2003-149]**, qualified as
  the speakers qualified it **[M2003-151]**, **[M2016-078]**. The expected return at $281.15 on the owner-cash stream is
  **3.9% to 5.5%** across every case shown, 5.0% with no growth; these are after-tax cash yields set against a pre-tax
  floor, which favours the name, and the name still does not clear it on any case. At the price, the owner-cash yield
  (5.01%) is **below the 30-year Treasury (5.66%)**; the price needs owner cash to grow about 1.5% a year for ten years
  merely to return the bond, and about 10% a year for ten years to return the floor.
- **The price against the range.** $281.15 sits **above the top** of the range ($249.02 with no growth; $275.06 even on the
  log-fit reading, which is above the shown endpoint growth). Under the CONVENTION's fourth specific, "a price above the
  top of the range closes OUT through the floor convention above, the expected return at the price then being below the
  minimum". It is the opposite of a case that "ought to just kind of scream at you" **[M1996-084]**; the purchase is made
  only at "a reasonable price in relation to the bottom boundary of our estimate" **[L2013-012]**.
- **The prices that would change the answer** (my arithmetic, not a rule): no-growth owner cash yields the ten percent
  floor at about **$140.94** a share ("cheap"); the shown-growth cases clear it at **$116.55** (endpoint) to **$153.50**
  (log-fit) ("fair" on the central readings). Even $141 would be a case that needs a pencil unless the store castle's
  margin had stopped narrowing; at half today's quote it would start to shout **[M2009-005]**.
- **Q6's buyback check, recorded back:** the prices paid in FY2021 to FY2024 (about $300 to $333) all sit above the $199.08
  bottom and above the $249.02 top; under the buyback CONVENTION the no-price programme weighs against, as Q6 recorded.
- **Value range:** **$199.08 to $249.02 a share against $281.15.** **Closes:** OUT. The range is narrower than three to one,
  the price sits above it, and the expectancy at the price is under the floor and under the bond: "there’s just a point at
  which we drop out of the game." **[M2003-149]**.
- **VERDICT: OUT**, with **[M2003-149]**, **[L2013-012]**, **[M1996-084]**, **[M2009-005]**, **[M2006-013]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED** (the run closed at Q7). The bond fact is recorded under COMPUTATION below.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED** (the run closed at Q7). The facts are recorded under COMPUTATION below.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED** (the run closed at Q7).

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED**; not asked by the operator.

---
## COMPUTATION — NOT A CLEARANCE
Facts gathered for the questions after the closing STOP. They carry no entry language and change nothing above.
- **The bond (Q8's first filter) at today's price** **[M1997-089]**: owner-cash yield 5.01% (all capex; 5.02% on the
  depreciation variant) against the 30-year Treasury at 5.66%. On the five-year owner cash the bond yields more today, with
  no growth needed and no business risk.
- **The debt and exposures (Q9's facts)** **[M1995-104]**, **[L2014-023]**, **[L2012-002]**, **[L2010-020]**. At 2026-08-02:
  short-term debt (commercial paper) $4,248M, current installments of long-term debt $4,697M, long-term debt $43,951M,
  together **$52,896M**; operating-lease liabilities $9,671M (10-Q balance sheet `0001628280-26-058715`). At 2026-02-01:
  senior notes $48.8B, $4.6B payable within 12 months; future interest on them $25.4B; about 11% floating after swaps
  (+1 point costs about $54M a year); lease obligations $15.9B remaining, $2.2B within 12 months (10-K Item 7 and 7A).
  Coverage, pre-tax earnings plus interest over interest, FY2025: ($18,602M + $2,412M) / $2,412M, **about 8.7 times**
  (10-K income statement). The company funds itself in part on commercial paper ($11.0B program, peak $6.2B in the first
  half of FY2026) backed by $11.0B of bank facilities, part of them 364-day lines; maturities are assumed to roll, which
  **[L2010-020]** warns is "usually valid" and occasionally not. Indentures carry no financial-ratio covenants (10-K Item 7).
  Self-insured for general and product liability, workers' compensation and medical, with catastrophe cover above
  retentions (10-K Item 1A and Note 1). No collateral calls, deposits or cash-out features found. For a whole business
  offered, "little or no debt" **[R1997-001]** would not be met; for a marketable stake the debt is serviceable on present
  earnings and would be the weight at Q9.
- **First half FY2026** (a check on the base, not an input): operating cash flow $11,422M against $8,968M a year earlier,
  helped by working capital (+$570M against −$1,821M) and about $730M of IEEPA tariff refunds the company calls "the vast
  majority of our expected refunds" (10-Q); capex $1,724M. Not used in the base; it does not change the close.

---
## THE BOX
**OUT**, decided at **Q7**. Value as a range: about $14,062M a year of owner cash after every real cost (five-year mean,
FY2021 to FY2025), sure in level and unsure in direction, worth **$199.08 to $249.02 a share** at the 30-year Treasury rate
of 5.66% (to $275.06 on the most generous growth reading), against a price of **$281.15**. The price sits above the range;
the expected return at the price (3.9% to 5.5% on owner cash) is under the ten percent floor and under the bond. Q8 to Q10
NOT REACHED. Not TOO HARD: Q1 and Q2 were answered IN on the filings, and the range is far narrower than three to one.
What would reverse it: a price near $141 or below (no-growth owner cash then clears the floor), together with evidence
that the store castle's margin gap over Lowe's has stopped narrowing and that the distribution acquisitions earn more
than the bond on their price. Q11 (has the business changed, or only its price) belongs to the holding review, not to a
purchase run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (template copied and committed, `71dacad`, before `tools/run.py` or any
      EDGAR request); written question by question; committed after Step 0, Q1, Q2, Q3, Q4, Q5, Q6 and Q7 (write-early).
- [x] Every v5 id resolves (each grepped in `principle_ledger_v5.csv` before it was written; no E-ids); every filing fact
      carries its document and accession; derived figures are arithmetic on filed figures, shown in the scripts of the
      research folder.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance (Q8 to Q10 NOT
      REACHED; the later facts sit under COMPUTATION with no entry language).
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): OCF − SBC − all capex, with the
      depreciation variant beside it; the sovereign from the issuing authority (US Treasury par curve, 10/05/2026); the
      aggregator quote flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (eight items under the foundations before any
      verdict; the narrowing margin gap at Q2 and the incremental-return finding at Q3 written where found).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; the anchor is today.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its v4 floor, "points over the sovereign" and
      verdict lines were ignored.
- [x] `python tools/check_framework.py` PASS before each commit (last run before the final commit: PASS).
- [x] Blind rule kept: no earlier HD run file or research folder, `PORTFOLIO.md`, holding review, session-state file, run
      queue, prepped reading list or `tools/alerts.json` was opened. Other companies' 2026-10-05 run (TSCO) was read for
      form only.
- [x] No raw filing text or HTML staged: downloads and text dumps sit under `cache/` (gitignored), checked with
      `git status --short` before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Five things. (1) **The range CONVENTION breaks when the growth shown is negative.** It says owner cash is carried "at the
growth the business has actually shown [...] never above it" and that the range's two ends are "the no-growth case and
the shown-growth case". For HD the endpoint growth is −2.84% a year, so the no-growth end is itself above the growth
shown; I used it as the top of the range, but the rule as written forbids it. (2) **"The growth shown" still does not say
endpoint or fit** (TSCO's run raised the same point): HD's endpoint is −2.84% and a log fit is +1.26%, and the two tops
differ by $26 a share; the box is OUT either way here, but a closer name would turn on the choice. (3) **Acquisitions are
not addressed by the owner-cash definition.** "All capital spending" is deducted, but cash paid for businesses is not,
while the bought businesses' earnings enter owner cash and the growth shown. For HD, $24B of acquisition cash since
FY2024 sits outside the base while SRS's and GMS's earnings sit inside it; a serial acquirer's growth is flattered, and
the convention says nothing on whether acquisition outlays are a real cost of the stream (I recorded the effect at Q3 and
Q7 and did not deduct them). (4) **"Fair" has no defined central case.** The dispatch asked for the price at which the
central case clears the floor; the framework defines the two ends, not a centre; I reported the shown-growth readings
($116.55 to $153.50) beside the no-growth "cheap" price ($140.94). (5) Two known form conflicts recur: the template's
position note says to check `PORTFOLIO.md`, which the blind rule forbids (recorded as "not checked"); and Q6's buyback
CONVENTION needs the bottom of the Q7 range, which the hard sequence computes later (run at Q7 and recorded back).
**Tool defects:** `tools/run.py` reads stock pay from `AllocatedShareBasedCompensationExpense` (524, 444, 382), which differs
by $2M a year from the filed cash-flow line "Stock-based compensation expense" (522, 442, 380); immaterial here, but the
cash-flow tag (`ShareBasedCompensation`) is the one owner cash should subtract. Its default window is three years, not the
five the v5 range CONVENTION uses (it prints a five-year line separately), and it still prints v4 floor and "points over
the sovereign" lines, ignored per Part VII. Its ten-year table shows intangibles as untagged ('-') before FY2021.
