# Company Run — McDonald's Corporation (NYSE: MCD) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. The rule forbids opening
`PORTFOLIO.md`, any holding review, any earlier run file or research folder for this ticker, the session-state files, the
run queue, the prepped reading list and `tools/alerts.json`; none was opened. **Contamination declared:** (1) listing
`Test Runs/` to find the 2026-10-05 runs for form showed the file name of an earlier MCD run dated 2026-09-03; it was not
opened, and its verdict is unknown to me. (2) Rows of the v5 ledger name McDonald's directly, including Buffett's sale of
the stock in 1998 and his later verdict that the sale was a mistake (**[L1998-019]**, **[M1999-123]**); they are the
speakers' words about the business in their time and are cited as such, not as a verdict on today's price. (3) I carry
general knowledge of the company from training; the filings below were read to replace it, not to confirm it. The verdict
is not conditioned on any of the three.

**Working folder:** `Test Runs/_research 2026-10-06 MCD/` (`run_py_output.txt`, `cover_shares_output.txt`,
`sources_output.txt`, `series.py` and `series_output.txt`, `q7.py` and its output, `peers.md`; raw filings under `cache/`,
gitignored).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $233.04 (close 2026-10-05, as printed by `python tools/run.py MCD`; **aggregator, live quote only, flagged**
  per operator rule 5). Context from the filings: the company bought its own stock at an average $304.62 in April 2026,
  $283.71 in May and $280.21 in June (10-Q Part II Item 2, accession `0000063908-26-000073`).
- **Shares by class** from the latest filing's cover: **707,641,531** common shares, $0.01 par, one class (10-Q for the
  quarter ended 2026-06-30, filed 2026-08-07, accession `0000063908-26-000073`; `python Screens/cover_shares.py MCD`).
  Preferred: authorized 165.0 million, issued none (10-K balance sheet).
- **Market cap:** $233.04 x 707.64M = **$164,908M** (my arithmetic; `tools/run.py` prints $164.91B).
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`python tools/sources.py`; issuing authority). About 68% of operating income is earned outside the US (10-K, Liquidity
  and Uses of Cash), but the reporting and the debt are dollar-led and the earnings currency of the filings is the dollar.
- **Filings read** (operator rule 4), all from SEC EDGAR:
  - 10-K FY2025 (year ended 2025-12-31), filed 2026-02-24, accession `0000063908-26-000035`: Business, MD&A (Outlook,
    Cash Flows, the capital-expenditure-by-type chart on page 21, Financing and Market Risk), Risk Factors, Legal
    Proceedings, the four statements, notes on Franchise Arrangements, Leasing, Restructuring, Equity Method, Debt.
  - 10-K FY2023, filed 2024, accession `0000063908-24-000072`: the cash-flow statement for 2021 and 2022.
  - 10-Q Q2 2026 (quarter ended 2026-06-30), filed 2026-08-07, accession `0000063908-26-000073`: balance sheet, cash
    flow, restructuring note, MD&A, Part II Item 2 (repurchases).
  - DEF 14A filed 2026-04-07, accession `0001193125-26-145548` (pay, board, ownership).
  - 8-K 2026-08-04, accession `0000063908-26-000067`, EX-99.1, Q2 2026 results (read before judging non-GAAP habits).
  - 8-K 2026-08-04, accession `0000063908-26-000069`, EX-99.1, President of McDonald's USA replaced.
  - 8-K 2026-09-23, accession `0000063908-26-000076`, EX-99.1, Investor Day: "McDonald's > NEXT" targets and the
    franchisee partnering support.
  - 8-K 2026-02-10, accession `0000063908-26-000028`, EX-99.1 (a director elected); 8-K 2026-02-11, accession
    `0000063908-26-000032`, EX-99.1 (Q4 2025 results).
- **One figure cross-checked against the filed statement:** cash provided by operations FY2025 **$10,551M** on the filed
  Consolidated Statement of Cash Flows (10-K `0000063908-26-000035`, page 42), against $10,551M in the `tools/run.py`
  table; total assets at 2025-12-31 **$59,515M** on the filed balance sheet against $59,515M in the tool's ten-year table.
  Both agree. One tag does not: the XBRL element the series script first read as depreciation and amortization carries
  only the SG&A line ($457M in 2025) after 2017; total D&A ($2,199M in 2025) is taken from the filed cash-flow statements.
- `python tools/run.py MCD`, **arithmetic lines only** (Part VII; its v4 ids, floor and verdict language ignored), with
  2021 and 2022 from the FY2023 10-K's filed cash-flow statement:

  | FY | OCF | SBC | capex | D&A | restaurants bought less sold | "Other" investing | **A: OCF−SBC−capex** | B: A less the two investing lines | C: OCF−SBC−D&A |
  |---|---|---|---|---|---|---|---|---|---|
  | 2021 | 9,142 | 139 | 2,040 | 1,868 | 178 | 54 | **6,962** | 6,730 | 7,134 |
  | 2022 | 7,387 | 167 | 1,899 | 1,871 | 361 | 457 | **5,321** | 4,503 | 5,349 |
  | 2023 | 9,612 | 175 | 2,357 | 1,978 | 246 | 676 | **7,079** | 6,157 | 7,459 |
  | 2024 | 9,447 | 172 | 2,775 | 2,097 | 358 | 498 | **6,500** | 5,644 | 7,178 |
  | 2025 | 10,551 | 165 | 3,365 | 2,199 | 8 | 579 | **7,021** | 6,434 | 8,187 |
  | **five-year mean** | | | | | | | **6,577** | **5,894** | **7,061** |

  ($M.) SBC is resolved and complete: expensed in the income statement, added back in operations, subtracted again here.
  Lease payments of about $1.7B a year are almost all inside operations (10-K, Leasing Arrangements). The "restaurants
  bought less sold" column is "Purchases of restaurant businesses" less "Sales of restaurant and other businesses"; the
  "Other" investing outflow is not explained anywhere in the 10-K (a search of the text for the line and for "investing
  activities" found no breakdown); capitalized software, a real cost, rose from $836M to $1,061M over 2023 to 2025 (10-K,
  Capitalized Software), so part of the line is probably software, and column B takes the whole line out to be safe.
  The 2024 purchase of an equity stake in Grand Foods Holding (China), $1,837M, is an acquisition and is not in any
  column. **Owner cash after every real cost runs at about 77% of reported net income** (A, five-year mean $6,577M against
  net income of $7,545M, $6,177M, $8,469M, $8,223M, $8,563M, mean $7,795M).
- **The capital spending split, from the filing** (10-K page 21, "Capital expenditures by type"):

  | FY | new restaurants | existing restaurants | other | total | D&A |
  |---|---|---|---|---|---|
  | 2023 | 1,217 | 1,044 | 96 | 2,357 | 1,978 |
  | 2024 | 1,564 | 1,106 | 105 | 2,775 | 2,097 |
  | 2025 | 2,247 | 1,040 | 78 | 3,365 | 2,199 |

  Spending on existing restaurants plus "other" runs at $1.1B to $1.2B a year, about half of depreciation. A maintenance
  variant on those three years (OCF − SBC − existing − other): $8,297M, $8,064M, $9,268M, mean $8,543M. It is shown, not
  used: the 2026-09-23 Investor Day adds "approximately $8.5 billion in total NEXT partnering support through 2036,
  including approximately $5 billion through 2030, through a combination of rent relief and capital support" to
  franchisees (8-K `0000063908-26-000076`), which is a cost of keeping the existing system standing and is not in any
  year above.

## THE FOUNDATIONS (not a gate)
**A share is a business** **[M1997-109]**: the question is whether I would be content to own a landlord and licensor to
45,356 restaurants if the market closed for five years, judged on what the restaurants pay it, not on the quote.
**The market serves, it does not instruct** **[M2006-077]**: the quote is $233 against the $280 to $305 the company itself
paid in the second quarter; that fall "doesn’t tell us anything. It just tells us prices." **[M2006-077]**. **Margin of
safety** **[M1996-084]** governs Q7. **No macro enters** **[M2000-094]**: the 10-K's "more discerning consumer spending"
and weight-loss medications are read as properties of the business, not forecasts. **Who is paid to tell you**
**[M2020-037]**: the company features non-GAAP earnings that leave out a restructuring charged every year since 2023, and
its Investor Day targets are a seller's projection of what it sells **[M2011-083]**; both are rebuilt from the filed
statements below. **The analyst's habits**: the speakers' own rows about this company pull in both directions (the sale
called a mistake **[M1999-123]**; food called less certain than razor blades **[M1997-001]**), and the worst anchor "is
always your previous conclusion" **[M2016-054]**, here the speakers' conclusion as well as my own prior.

**Contrary evidence, written down as found** **[M1997-127]**:
1. U.S. comparable sales +0.8% in Q2 2026, "driven by positive check growth, including favorable product mix, partly
   offset by negative comparable guest counts" (8-K `0000063908-26-000067`; 10-Q MD&A). Fewer visits, higher checks.
2. The President of McDonald's USA, in the job almost seven years, "decided to leave"; the chief executive says "we see an
   opportunity to raise the bar in the U.S. and accelerate performance in our largest market" (8-K
   `0000063908-26-000069`, `0000063908-26-000067`).
3. $8.5B of "NEXT partnering support through 2036 [...] through a combination of rent relief and capital support" to
   franchisees (8-K `0000063908-26-000076`): the landlord is cutting the rent and paying for the tenants' equipment.
4. "Accelerating the Organization" restructuring charges in every year: $250M (2023), $221M (2024), $226M (2025), $98M in
   the first half of 2026, "approximately $250 million" expected for 2026, completion "during 2027", $795M so far (10-K
   Restructuring note; 10-Q note). The non-GAAP figures leave them out.
5. Shareholders' equity negative every year since 2016 (−$2,204M to −$1,791M at 2025, low −$8,210M at 2019); long-term
   debt up from $25,878M (2016) to $39,973M (2025) (the ten 10-Ks listed in `run_py_output.txt`).
6. The company's own after-tax return on invested capital fell: 25.2% (2023), 21.8% (2024), 20.3% (2025) (10-K, Total
   Assets and Return), while capital spending rose 43% from 2023 to 2025.
7. Owner cash (column A) was $6,962M in 2021 and $7,021M in 2025: flat over four years in which systemwide restaurants
   rose and capital spending rose by $1.3B.

## THE STANDING RULE
Owning a marketable stake bought for cash, unlevered and sized within what the buyer can lose without being forced to
sell, does not put the buyer at risk of ruin **[M2012-081]**, **[L2023-005]**; the rule binds the buyer's conduct, and the
target's own debt of $40.0B and derivative collateral (10-K: "$79 million of collateral" posted) are weighed at Q9, not
here. Borrowed money to own it would be ruled out **[L2014-005]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the company is, from the filing.** "The Company is primarily a franchisor"; of 45,356 restaurants at 2025 year-end,
  43,317 were franchised and 2,039 company-operated (10-K Business and the Nature of Business note, `0000063908-26-000035`).
  Under a conventional franchise "the Company generally owns or secures a long-term lease on the land and building" and the
  franchisee pays "rent and royalties based upon a percent of sales, with specified minimum rent payments", "generally for
  a period of 20 years"; developmental licensees and affiliates pay a royalty and supply their own capital. 2025 franchised
  revenues were $16,548M: rents $10,442M, royalties $6,018M, initial fees $88M (Franchise Arrangements note). Future
  minimum rents already contracted: $31,451M (same note). So the cash is a share of what 45,000 restaurants sell, most of
  it as rent on property the company controls.
- **The key variables, and how predictable** **[M1998-044]**: (1) systemwide sales, $139.4B in 2025 (10-K MD&A), which is
  restaurants open times sales per restaurant, the latter guest counts times check; (2) the rent and royalty taken on
  those sales, fixed by 20-year contracts; (3) the capital the company must put into the real estate and now into the
  franchisees; (4) the franchisees' own health, since "you have to have a good business for the franchisee to, over time,
  have a good business for the parent company" **[M1998-164]**. (1) and (2) are slow-moving and contractual; (3) and (4)
  are where the filings of 2026 move (Step 0, contrary evidence 3).
- **Where it will be in ten years** **[M2000-037]**, **[M2012-065]**: a landlord and licensor to a larger number of
  restaurants selling hamburgers, chicken, fries and drinks in the same 100-odd countries, paid a percent of their sales.
  The forecast is about customers and their habits, not about a technology **[M2017-019]**, **[M2023-030]**: the
  digital, delivery and loyalty programmes the 10-K describes are channels to the same counter. The speakers themselves
  framed the McDonald's question as one of competition, the franchise arrangement and whether people keep eating
  hamburgers (**[M2007-045]**, the row's note on the stand that precedes it), which is a consumer question.
- **Do the past statements tell me the future ones?** **[M2008-033]** Largely yes: the franchise revenue line rose every
  year shown (15,437, 15,715, 16,548), and the company's model "is designed to generate stable and predictable revenue,
  which is largely a function of franchisee sales" (10-K). What the past statements do not yet show is the cost of the
  2026 partnering support, which is announced, sized ($8.5B through 2036) and therefore knowable.
- **The speakers on this industry.** Food gives no "total certainty of dominance" because "People move around in the food
  business" **[M1997-001]**; "convenience is a huge factor" **[M1997-139]**, with Buffett's gloss in the row's note: "So
  it’s no knock on McDonald’s at all. It’s just the nature of the kind of industry they’re in." That bears on the castle
  (Q2), not on whether the economics can be foreseen. Munger: "the net returns on capital McDonald’s has earned all these
  years are high, even though they have owned a lot of their real estate" **[M1998-171]**.
- **What could put the forecast out of reach.** The 10-K's own risk factor names "changes to dietary guidelines or use of
  weight-loss medications" and says some changes in consumer acceptance "can occur rapidly". **Contrary evidence written
  down** **[M1997-127]**: this is the one variable in the filings that a reader cannot size. I judge it a slow change of
  the kind "much harder to perceive" **[M2014-038]**, to be weighed at Q2 under what could reduce the castle, not a fast
  technological change that would put the ten-year economics out of reach at Q1 **[M1998-008]**: the product and the
  habit are seventy years old, and the industry's insiders do write ten-year forecasts down (the company published 2030
  targets on 2026-09-23), which is the test of **[M2000-105]**, though their forecasts are not relied on **[M1995-050]**.
- **Do I doubt it is inside?** **[M2002-092]** No, for the economics: a percent of sales, rent on owned and leased
  property, and the capital that goes in are all readable from the filings. The judgment of whether those economics are
  improving or eroding is Q2's.
- **VERDICT: IN.** The ten-year economics can be pictured from the filings: rent and royalty on systemwide sales under
  20-year contracts, plus the capital that must go in **[M2012-065]**, **[M2000-037]**; the forecast concerns consumer
  behaviour **[M2023-030]**, not fast technology **[L1993-023]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The competitor row** (each company's own filings; detail and accessions in `peers.md`): US comparable sales.

| | FY2025 | Q2 2026 | H1 2026 |
|---|---|---|---|
| McDonald's US (10-K `0000063908-26-000035`, 10-Q `0000063908-26-000073`) | +2.1% | +0.8%, guest counts negative | +2.3% |
| Burger King US (RBI 10-K `0001618756-26-000017`, 10-Q `0001618756-26-000045`) | +1.6% | **+8.5%** | +7.2% |
| Popeyes US (same RBI filings) | −2.9% | −5.2% | −5.8% |
| Wendy's US (10-K `0000030697-26-000009`, 10-Q `0000030697-26-000116`) | −5.6% | −7.0% | −7.4% |
| Taco Bell Division, 86% US (Yum 10-K `0001041061-26-000084`, 10-Q `0001041061-26-000160`) | +7% | +7% | +8% |

1. **What keeps it standing, and how permanent** **[M1995-038]**. From the filings: (a) the sites. "the Company generally
   owns or secures a long-term lease on the land and building"; it owns "approximately 56% of the land and approximately
   80% of the buildings for restaurants in its consolidated markets"; net property under franchise arrangements $22.8B
   including land of $7.1B (10-K, MD&A and Franchise Arrangements note). (b) The drive-thru network: "nearly 29,000 drive
   thru locations globally, including over 95% of the approximately 13,700 locations in the U.S." (10-K Strategic
   Direction). (c) The franchise system: 20-year agreements, franchisees who "generally" are not "passive investors", and
   $31,451M of minimum rent already contracted. (d) The brand and the menu, "seventeen unique billion-dollar brands" (10-K).
   These are physical and contractual, built over seventy years; they do not "depend on the genius of the lord in the
   castle" **[M1995-038]**.
2. **Would it stand without the lord?** **[L2007-006]**, **[M1996-037]** Yes on the evidence: 95% of restaurants are run by
   independent operators; the company's chief executive was replaced in 2019 and its US president in August 2026 (8-K
   `0000063908-26-000069`) and the system kept opening restaurants (2,276 in 2025, 10-K).
3. **The money test** **[M1997-103]**, **[M2011-015]**: could a well-funded attacker rebuild 13,700 US corner sites, 95%
   with drive-thrus, and 30,000-odd licensed restaurants abroad? Not with money alone; the sites and the franchisees came
   over decades **[M2002-048]**. But the money test does not settle the restaurant fight, because the attackers already
   exist and are standing: Burger King, Wendy's, Taco Bell and Popeyes have fought on the same corners for fifty years.
   The test the rows add, "one competitor is frequently enough to ruin a business" **[M2012-108]**, has not been met in
   that half-century.
4. **Pricing power and the agony before a rise** **[M2005-020]**. **Weighs against, written down as found**
   **[M1997-127]**: US sales growth comes from "positive check growth [...] partly offset by negative comparable guest
   counts" (10-Q); the 10-K speaks of "industry-wide challenges associated with more discerning consumer spending" and a
   marketing strategy "that highlights value at every tier of the menu"; the 2026 strategy is built on "dedicated value
   leadership" (8-K `0000063908-26-000076`). Fewer visits at higher checks is the pattern the rows warn of, pricing pushed
   to "the point that they lost market share without [...] having — the moat that they thought they had" **[M2001-087]**.
   It is not yet a loss of share across the field (Wendy's and Popeyes fell further), but it is a prayer session, not a
   price rise taken in stride **[M2005-020]**.
5. **Unit volume and share of mind** **[M1999-054]**, **[M1997-099]**: restaurants 41,822 (2023), 43,477 (2024), 45,356
   (2025), with 2,600 openings planned for 2026 (10-K Outlook); systemwide sales $139.4B, +5% in constant currency in
   2025; "nearly 220 million" 90-day active loyalty users (8-K `0000063908-26-000067`). Unit volume across the world is
   rising; US visits per restaurant are falling (item 4).
6. **The low-cost position** **[M2018-043]**, **[L2007-004]**: SG&A expected at "about 2.2% of Systemwide sales" in 2026
   (10-K Outlook), on a base of $139.4B of sales; the largest buyer in its industry. Scale is a cost advantage
   **[M1995-039]**; but the rows put the low-cost moat in passing costs to customers **[L1996-016]**, and the US check
   growth runs the other way.
7. **The brand** **[M2008-075]**, **[M2023-073]**: asked for by name; the speakers name it among the brands that travel,
   "McDonalds travels" **[M1997-068]**, and the filings show it: International Operated Markets comparable sales +3.2% and
   Developmental Licensed +4.6% in 2025 (10-K), and positive in every segment in Q2 2026 (8-K `0000063908-26-000067`).
8. **Would the customer still choose it over the low bid?** **[M2017-009]** The speakers' own answer for this industry:
   "People move around in the food business [...] they may favor McDonald’s but they will go to different places at
   different times" **[M1997-001]**, and "a great many of the decisions on fast food, as to where you eat, is simply based on
   which one you see. I mean, convenience is a huge factor." **[M1997-139]**. Convenience is what the sites and drive-thrus
   own (item 1), so the castle is in the location more than in the customer's loyalty; the 2026 swing to Burger King and
   Taco Bell is the customer moving around, as the row says he does.
9. **Ask the competitors** **[M1999-130]**, **[M2025-043]**: their filings answer for them. Wendy's 10-K announces "Project
   Fresh" to "increase traffic"; RBI's Burger King segment grew comparable sales while its restaurant count shrank 0.8%
   (fewer, better units). None of them reports a unit growth rate near McDonald's 4.5% net (10-K Strategic Direction).
10. **Widening or narrowing** **[M1999-108]**, **[L2005-010]**: abroad, widening (unit growth, positive comparable sales in
    all regions, an increased stake in the China business in 2024). In the US, narrowing in the first half of 2026 against
    Burger King and Taco Bell, widening against Wendy's and Popeyes. The company's own answer is to cut the rent and fund
    the franchisees' equipment, $8.5B through 2036 (8-K `0000063908-26-000076`); the rows tie the franchisor's castle to
    the franchisee's business **[M1998-164]**, **[M1998-165]**, so a landlord forced to subsidise tenants is a notch, not a
    breach **[L1995-023]**. Whether the support restores US traffic is not knowable today; its cost is (Q3, Q7).
11. **What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**: (a) weight-loss medications
    and dietary change (10-K risk factor), a slow change **[M2014-038]**; (b) the delivery intermediary taking the customer,
    the "value of having the brand moves over to the retailer" **[M2001-090]**; the company's answer is its own app, a
    target of 30% of delivery sales from it by end-2027 (10-K); (c) the franchisee's economics (item 10). Would it be started
    today? A drive-thru landlord on the best corners would be; none of the three is a technology that obsoletes the corner
    **[M2006-065]**.
- **VERDICT: IN.** The castle stands for a reason that is physical and contractual, the sites under 20-year rent and the
  drive-thrus on them, plus a brand that travels **[M1997-068]**, and the money test is met **[M1997-103]**; its weakness is
  the one the speakers named for the whole industry, a customer who moves around **[M1997-001]**, **[M1997-139]**, now shown
  in falling US guest counts and a rival's 8.5% quarter. That is a castle losing a notch at home while widening abroad,
  not one shown open **[M2011-015]**; the cost of defending it is carried to Q3 and Q7.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, **[M2011-060]** (`q3.py`, `q3_output.txt`; net tangible
  operating capital = total assets less goodwill, cash and non-debt current liabilities, the lease asset shown in and
  out; pre-tax operating income from the filed income statements):

  | year-end | net tangible operating capital | of which lease right-of-use | operating income | on all of it | without the leased-site asset |
  |---|---|---|---|---|---|
  | 2021 | 43,048 | 13,552 | 10,356 | 24.1% | 35.1% |
  | 2023 | 44,549 | 13,514 | 11,647 | 26.1% | 37.5% |
  | 2025 | 51,720 | 14,606 | 12,393 | 24.0% | 33.4% |

  ($M; 2023 to 2025 lease figures from the filed balance sheets, the XBRL tags being absent.) About 24% pre-tax on every
  dollar of tangible capital including the leased sites is a high return for a business that owns much of its real
  estate, as Munger said of it **[M1998-171]**; it is not made by shrinking equity **[M1998-017]**, since the measure is
  on operating capital, not on the negative book equity.
- **What the added capital earned.** 2021 to 2025: operating income +$2,037M on +$8,672M of net tangible operating
  capital, **23.5% pre-tax on the increment** (`q3_output.txt`), close to the average. But owner cash did not follow:
  column A was $6,962M in 2021 and $7,021M in 2025 (Step 0), because capital spending rose from $2,040M to $3,365M, most of
  it for new restaurants ($2,247M of $3,365M in 2025, 10-K page 21), and new units pay rent with a lag. The company's own
  after-tax ROIC fell from 25.2% to 20.3% over 2023 to 2025 (10-K) **[M2023-081]**: "We just put way more capital into
  the business".
- **To stand still, and to grow** **[L1999-024]**, **[M2000-144]**: spending on existing restaurants plus other was
  $1,140M, $1,211M and $1,118M in 2023 to 2025 against depreciation of $1,978M to $2,199M (Step 0), so on the filing the
  company maintains its existing estate for about half of its depreciation, because "Franchisees are responsible for
  reinvesting capital in their businesses over time" (10-K). That cheapness is now being given back: from 2027 to 2030
  "about $3 billion of annual baseline capital expenditures plus $1.5 billion to $2 billion of cumulative capital partnering
  support", and "$8.5 billion in total NEXT partnering support through 2036 [...] through a combination of rent relief and
  capital support" (8-K `0000063908-26-000076`). The rows' test is whether the outlay keeps the competitive position or
  grows it **[L1999-024]**; on the company's own words the partnering money is for the first, the franchisees' modernisation
  and "value leadership", and its return to the owner is the rent it protects, not new rent.
- **The growth arithmetic** **[M2001-019]**, **[L2007-010]**: unit growth is bought with the company's capital in the US and
  International Operated Markets (about 750 openings planned in 2026) and with the licensees' capital elsewhere ("more than
  1,800 restaurant openings", 10-K Outlook), the second kind costing the company nothing. So part of the growth is See's
  and part is the "good" savings account **[L2007-010]**. It is not the gruesome kind: the increment still earns about 23%
  pre-tax.
- **WEIGHS FOR**, qualified: a high return on the capital the business actually needs, kept on the increment
  **[M1995-047]**, **[L2009-012]**; against it, a rising capital need (capital spending up 43% in two years, partnering
  support of $8.5B announced) that has kept owner cash flat for four years **[M2008-036]**, **[M2023-081]**. (The "little
  or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** **[M2025-032]** (`run_py_output.txt`, first-filed XBRL, read against the filed
  FY2023 and FY2025 balance sheets):

  | year-end | assets | equity | cash | goodwill | long-term debt | retained earnings |
  |---|---|---|---|---|---|---|
  | 2016 | 31,024 | −2,204 | 1,223 | 2,336 | 25,878 | 46,223 |
  | 2019 | 47,511 | −8,210 | 898 | 2,677 | 34,118 | 52,930 |
  | 2021 | 53,854 | −4,601 | 4,709 | 2,782 | 35,623 | 57,535 |
  | 2025 | 59,515 | −1,791 | 774 | 3,354 | 39,973 | 70,282 |

  What moved and why. (a) Assets jumped from $32.8B to $47.5B in 2019: the lease right-of-use asset arrived with the lease
  standard (about $13.5B at 2023 to 2025), an accounting change, not a purchase. (b) Retained earnings rose $24.1B in nine
  years while equity stayed negative: treasury stock at cost reached $79,316M at 2025 (10-K balance sheet), so the company
  has paid out more than it earned and borrowed part of the difference; long-term debt rose $14.1B. That is what the
  figures say. (c) Goodwill is small ($3.4B) and grew only with refranchising and buy-backs of restaurants; no large
  acquisition sits in the accounts. (d) Cash is kept low ($774M) against a $5.0B commercial paper programme and a $4.0B
  committed line (10-K). (e) Receivables $2,466M against revenues of $26,885M, inventory $61M: nothing building up out of
  line with sales **[M1995-064]**. What they do not say: the market value of the land and buildings (carried at cost, land
  $7.1B in the franchise estate), and what the franchisees earn, on which everything rests **[M1998-164]**. What they
  cannot say: whether the $8.5B partnering support restores the US traffic.
- **The real costs.** Depreciation is a real cost **[R1996-023]**, **[L2015-004]**; here maintenance spending on existing
  restaurants runs at about half of it because the franchisees carry most of the reinvestment (Q3), so column A (all
  capital spending deducted) is the conservative base and the depreciation variant is shown beside it (Step 0). Stock pay
  $165M, expensed and deducted **[L2015-003]**. Equity-method income ($190M in 2025, 10-K) is counted as the dividends the
  affiliates pay: the company records dividends from equity investees "within the cash provided by operations" (10-K,
  Equity Method note), and the share of profit is removed from operations as non-cash, so column A already follows the
  framework's convention for equity-method income.
- **The recurring "one-time"** **[L1998-031]**, **[L2016-007]**: "Accelerating the Organization" restructuring charges of
  $250M, $221M, $226M and $98M (first half of 2026), "approximately $250 million" expected for 2026 and "completion during
  2027" (10-K and 10-Q notes): a five-year programme of about $1.05B. The company's non-GAAP earnings leave them out (Q2 2026
  release: GAAP EPS $3.32, non-GAAP $3.38), and "Management [...] bases incentive compensation plans on these results"
  (10-K MD&A). They are a cost of running the business and stay in owner cash (they are in operating cash already).
- **EBITDA in the filer's mouth** **[M1998-086]**, **[M2002-026]**: no instance found; a search of the FY2025 10-K, the Q2 2026
  10-Q, the Q4 2025 and Q2 2026 releases, the Investor Day release and the proxy for "EBITDA" returned nothing.
- **The tells** **[M1995-064]**: (1) adjusted earnings featured beside GAAP, with a recurring charge excluded and pay
  measured on the adjusted figure **[L2016-006]**; GAAP is printed first in every release read, and the adjustment is
  small (2% of net income in 2025: $178M after tax on $8,563M). (2) No earnings guidance is given; the Investor Day sets
  2030 targets (operating margin, free cash flow conversion), so the habit of making a quarterly number **[L2002-041]** is
  not evidenced. One tell, not two: by the two-tell line (framework Q4, CONVENTION) it weighs against and does not make
  suspicion.
- **Clear speech** **[M1994-018]**: the 10-K explains in plain terms how the money is made (rent, royalty, initial fees,
  the minimum rents contracted) and prints the capital spending by type; the accounts are not confusing.
- **VERDICT on confusion: IN** (not confusing, not suspect **[M1995-063]**, **[M2003-029]**); **WEIGHS AGAINST**, mildly,
  for the adjusted figures that pay management and exclude a cost repeated every year **[L2016-006]**, **[L2016-007]**. The
  recast earnings for Q7 are owner cash column A, $6,577M a year on the five-year mean, with column B ($5,894M) and the
  depreciation variant ($7,061M) beside it.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
Extracts in `notes - proxy and SEC 2023.md`. This is a marketable stake, so the yardsticks and the reading tests carry the
weight, not the after-the-sale test **[M2007-081]**.
- **The first yardstick, the record against the hand dealt** **[M1994-008]**: Christopher Kempczinski has been chief
  executive since 2019 and chairman since 2024 (DEF 14A `0001193125-26-145548`). Over 2019 to 2025 operating income rose
  from $9,070M to $12,393M (`series_output.txt`, XBRL of the filed 10-Ks; 2025 checked to the filed statement), through a
  pandemic year, and restaurants from 41,822 to 45,356 over 2023 to 2025 (10-K); against the competitor row, Wendy's US sales fell 5.6% in 2025 and
  Burger King shrank its restaurant count (Q2). The hand was a strong one **[M1996-037]**; the record is that of a
  management that did not spoil it, and the 2026 US slippage is on its watch.
- **The second yardstick, how they treat the owners** **[M1994-009]**, read in the proxy: the chief executive's pay was
  $20.6M in 2025, $18.2M in 2024 and $19.2M in 2023, about 0.24% of 2025 net income; his short-term bonus paid 76.4% of
  target because "2025 operating income and Systemwide sales results were below target", and the 2023 performance units
  vested at 82.2% (DEF 14A). Pay fell when results fell. The design is weighed at Q6, Part B.
- **The tells of dishonesty** **[M1995-111]**, **[M2007-082]**, applied on doubt alone **[M2013-088]**. **Contrary evidence
  written down** **[M1997-127]**: on 2023-01-09 the SEC found that McDonald's "failed to disclose that the company exercised
  discretion in treating Easterbrook’s termination as without cause in conjunction with the execution of a separation
  agreement valued at more than $40 million" and that it "violated Section 14(a) of the Exchange Act"; the company consented
  without admitting or denying, and "The Commission determined not to impose a financial penalty on McDonald’s in light of
  the substantial cooperation it provided" (SEC press release 2023-4, from the issuing authority). Read whole, the record is
  a board that let a fired chief executive keep his equity and did not say it had chosen to, then, on its own internal
  investigation in July 2020, found the further misconduct, and cooperated fully. The first half is a report that danced
  around the figure that mattered **[M2007-082]**; the second is the act the rows ask for when bad news arrives, "the main
  problem was they didn’t act when they learned about it" **[M2017-005]**, here inverted: they acted. The man who concealed
  was the predecessor, not the present chief executive. I do not find in it a doubt about the honesty of the people now
  running the company; I record it as the one integrity mark in the documents read, six years old.
- **The letters and reports** **[M1998-036]**, **[M2007-083]**: the 10-K is plain and gives the owner what he would want
  (capital spending by type, minimum rents, the restaurant counts by structure). The releases are another matter: "McDonald’s
  > NEXT", "Make It Golden", "fan truths", "brand fandom" (8-K `0000063908-26-000076`; 10-K) read as "a standardized bunch
  of popular jargon" **[M1998-038]**. Weighs against, lightly.
- **How they talk about mistakes** **[L2024-003]**: the US president's departure is presented as "a deliberate leadership
  transition plan", and the chief executive speaks of "an opportunity to raise the bar in the U.S." (8-Ks
  `0000063908-26-000069`, `0000063908-26-000067`); no document read uses "mistake" or "wrong" of the US result. No instance
  found of a plain admission; a search of the two releases and the Investor Day release for "mistake" and "wrong" found
  none.
- **Love of the business** **[M2000-098]**: the new US president has "more than 26 years of McDonald’s experience"
  (8-K `0000063908-26-000069`); the chief executive holds 869,034 shares including vested options (DEF 14A) against an
  ownership requirement of six times salary. Hired managers, long in the system; nothing in the documents argues either
  way on love against money **[M2016-066]**.
- **VERDICT on integrity: IN.** No doubt about the honesty of the present management is raised by the documents read; the
  2019 disclosure failure belonged to the board's handling of a predecessor and was followed by investigation and
  cooperation **[M2017-005]**, **[M2015-047]**. **Ability WEIGHS FOR**: a record kept against a strong hand and against
  competitors who did worse **[M1994-008]**, **[M2012-089]**, with the 2026 US slippage and the jargon set against it.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test** **[M1994-061]**, **[R1995-009]**, **[M1998-110]**: there is little to test, because the company
  does not retain. Over 2016 to 2025 it paid $39.3B in dividends and $39.6B for its own stock against net income of
  $65.5B (`series_output.txt`, XBRL of the ten filed 10-Ks; the 2025 figures, $5,115M and $2,056M, checked to the filed
  cash-flow statement), about 120% of earnings, and long-term debt rose $14.1B over the same years (Q4). Its stated order
  is "(i) invest in opportunities to grow the business [...] (ii) prioritize our dividend and (iii) repurchase shares with
  remaining free cash flow over time" (10-K Strategic Direction), the order the rows give **[L2012-011]**, **[L2021-005]**.
  A company that "expects to regularly earn more than it can profitably employ in its business, should be paying out
  dividends" **[M2004-089]**; it does, 50 consecutive years of increases (10-K), and "clear, consistent and rational"
  **[L2012-015]**.
- **Buybacks** **[L1999-023]**, **[L2011-003]**: the programme is "$15.0 billion [...] with no specified expiration date"
  and names no price (10-K; 10-Q Part II Item 2), the form the rows describe as never referring "to a price above which
  repurchases will be eschewed" **[L2016-002]**. **The prices paid, read against the bottom of the Q7 range (recorded here
  from Q7, as the framework directs):** $3,105M for 11.1M shares in 2023 ($280), $2,826M for 10.1M in 2024 ($280),
  $2,016M for 6.7M in 2025 ($301) (10-K statement of shareholders' equity), and $288.62 average in Q2 2026 (10-Q). The
  bottom of the Q7 range is **$164**, the top $195 (Q7). Every purchase in the record read was made at 1.4 to 1.8 times
  the bottom and above the top: "If you’re repurchasing shares above a rationally calculated intrinsic value, you are
  harming your shareholders" **[M1996-013]**; "if you buy it for $1.10, you are doing them no favor at all" **[M2014-008]**.
  Part of it was paid for with borrowed money (above). And the pay plan reaches into it: the performance-unit EPS targets
  were set with "the planned level of share repurchases" built in (DEF 14A), a buyback planned as a quantity, not as a
  price **[M2016-049]**. By the convention (framework Q6, buyback with no stated price), **weighs against**.
- **Issuance and deals** **[M1995-001]**, **[L2014-012]**: none in stock. The 2024 increase in the China stake ($1,837M,
  cash; 10-K) and the restaurant buy-backs from franchisees were paid in cash. The STOP for an all-stock deal by an
  undervalued acquirer **[L2009-019]** does not arise; no serial issuance **[L2014-015]** (share count fell from 723M to 711M
  over 2023 to 2025, 10-K).
- **Part A WEIGHS AGAINST**: the payout is honest and the dividend sound, but the buybacks, part-borrowed, have been made
  with no stated price at prices above any value this run can support **[L2016-002]**, **[M1996-013]**.

**Part B: the pay, the board and the owners.**
- **Pay tied to what the person controls** **[M2003-019]**: the 2025 bonus measures operating income growth (40%),
  systemwide sales growth (30%), new restaurant openings (15%) and a scorecard (15%) (DEF 14A). Operating income and sales
  are under management's hand; restaurant openings reward capital spent, not the return on it, and "you get what you
  reward for" **[M2016-083]**: a bonus on openings at a time when capital spending rose 43% in two years is a bonus on the
  input. The pay is measured on results "excluding [...] impairment and other charges" (10-K), which leaves out the
  restructuring charged every year (Q4).
- **Options** **[L1998-028]**, **[L1994-021]**: half the long-term award is stock options ($8.0M of the chief executive's
  $20.6M in 2025), at a fixed price with no step-up for retained earnings, the "royalty on money that you left with me"
  **[M1997-043]**; the proxy does not name the dividend conflict of a fixed-price option, as **[L2005-014]** says such
  proxies do not. The performance units carry a relative-TSR modifier and a cap when absolute TSR is negative, which is a
  partner "in both directions" in part **[L1994-020]**.
- **Who designs it** **[M1997-041]**: an outside consultant (Semler Brossy) and an "Annual compensation peer group review"
  (DEF 14A), the ratchet the rows warn of **[M2004-016]**, **[L2005-015]**.
- **The board** **[M2007-120]**: chairman and chief executive combined since 2024, with a Lead Independent Director; the
  board opposed a shareholder proposal to separate the roles (DEF 14A). The rows find a mediocre chief executive who also
  chairs hard to replace **[L2014-026]**; the chief executive here is not judged mediocre (Q5), so this is a structure to
  watch, not a finding. A director was added in 2026, the serving chief executive of Ford Motor Company (8-K
  `0000063908-26-000028`); no evidence either way on directors who bought with their savings **[L2019-008]**.
- **The owners as partners** **[L1994-023]**: no quarterly earnings guidance; long-range targets published at the 2026
  Investor Day. Disclosure of the business is full in the 10-K (Q4).
- **Part B WEIGHS AGAINST**, mildly: pay partly on inputs and adjusted figures, half in fixed-price options, set against a
  peer group; mitigated by pay that fell when results fell and a TSR cap **[M2007-006]** (the person outranks the plan).
- **Q6 WEIGHS AGAINST** on both parts; no STOP arises.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, **[M2009-004]**; the cash is what comes out
net of what must go back in **[M1998-080]**, **[M2014-068]**. Arithmetic in `q7.py`, output in `q7_output.txt`.
- **The cash.** Owner cash after every real cost, column A (OCF − SBC − all capital spending), five-year mean **$6,577M**
  **[L2021-003]**, **[L2015-004]** (Step 0, Q4). Interest is already paid out of it, so it is the owners' cash and is
  discounted to an equity value directly; the $40.0B of debt is assumed to roll, which Q9 weighs.
- **The growth shown** (CONVENTION, framework Q7: measured on the aggregate owner cash, 2021 to 2025): endpoint 0.21% a
  year ($6,962M to $7,021M); log-trend through the five years 2.19% (2022, the year of the Russia exit charge, is the low
  point). Both are inside Q3's cap: no rate near the discount rate **[M1997-095]**. I take the log-trend as the
  shown-growth end because the endpoint rate is held down by a strong first year; this choice raises the top of the
  range and works against an OUT, not for it.
- **The rate:** 5.66%, the 30-year Treasury, 10/05/2026, no risk premium added **[M1996-024]**, **[M1998-151]**.
- **The range** (CONVENTION, framework Q7: ten years at the growth shown, then zero nominal growth, discounted at the
  sovereign; the ends are no growth and shown growth):

  | case | value, $M | per share | expected return at $233.04, after tax |
  |---|---|---|---|
  | no growth | 116,196 | **$164.20** | 3.99% |
  | shown growth, endpoint 0.21% | 118,142 | $166.95 | 4.06% |
  | shown growth, log-trend 2.19% | 138,230 | **$195.34** | 4.77% |
  | beside it, column B no growth (restaurant purchases and the unexplained investing line also deducted) | 104,130 | $147.15 | 3.57% |
  | beside it, depreciation variant, log-trend 5.86% | 198,472 | $280.47 | 6.70% |

  **Value range: $164 to $195 a share against $233.04.** Width 1.19 to 1, well inside three to one, so TOO HARD by width
  does not arise **[L2000-025]**.
- **The floor** (CONVENTION, framework Q7: about ten percent pre-tax **[M1994-004]**, **[L2002-020]**, **[M2003-149]**,
  qualified by **[M2003-151]** and **[M2016-078]**). Owner cash is after corporate tax, so the run converts the floor at the
  company's 2025 effective rate of 21.4% (10-K) to **7.86% after tax** (CONVENTION of this run, the form a 2026-10-05
  sibling run used; rationale: the floor is stated pre-tax and the cash is after tax, and the filer's own rate is the least
  invented converter). At $233.04 the expected return is 3.99% to 4.77% after tax across the range, about 5.1% to 6.1%
  pre-tax: below the floor in every case. Even the depreciation variant at its own shown growth returns 6.70% after tax,
  and the sensitivities in `q7_output.txt` (the 2016 to 2025 growth of 6.14% carried ten years: 6.41%; five percent for ten
  years: 5.91%) all fall short. The price sits above the top of the range, which "closes OUT through the floor convention
  above, the expected return at the price then being below the minimum" (framework Q7, the four specifics).
- **The prices the arithmetic implies** (COMPUTATION, NOT A CLEARANCE; no entry language): the price at which the
  shown-growth case (log-trend) earns the 7.86% after-tax floor, **"fair" = $138.83**; the price at which the no-growth
  case earns it, **"cheap" = $118.24** (`q7_output.txt`). Neither is a screamer threshold: at either price the case would
  still need a pencil, and a screamer is a price "so far below" that it does not **[M2009-005]**, **[M1996-084]**.
- **How sure** **[M1999-104]**: the castle stands and the people are honest (Q2, Q5), which supports the narrowness of the
  range; the announced $8.5B of partnering support through 2036 (about $5B by 2030), not in any year of the record, would
  lower the cash if it is not repaid in rent, and so sits against the top of the range, not the bottom.
- **VERDICT: OUT.** The price is above the top of a narrow range; the expected return at $233.04 is about half the floor,
  "a point at which we drop out of the game" **[M2003-149]**; "You can turn any investment into a bad deal by paying too
  much" **[M2019-015]**. This is a verdict on the price, not on the business **[M2010-090]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the run OUT). For the record only, not a clearance: the expected return at the price, 3.99% to
4.77% after tax, is below the 5.66% the 30-year Treasury pays before tax, so the stock would not pass the bond as the first
filter either **[M1997-089]**.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts gathered on the way, unweighed: long-term debt $39,973M, 97% fixed-rate, weighted rate 4.0%, BBB+ and
Baa1, "no provisions in the Company’s debt obligations that would accelerate repayment of debt as a result of a change in
credit ratings", $79M of derivative collateral posted, $85M of guarantees for the System (10-K Financing and Market Risk;
Material Cash Requirements); operating income $12,393M against interest $1,582M in 2025 (filed income statement).

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (not asked; the operator did not choose it for this run).

---
## THE BOX
**OUT, at Q7.** Q1 IN, Q2 IN, Q4 IN on confusion, Q5 IN on integrity; Q3 weighs for (qualified), Q4 weighs against
(mildly), Q6 weighs against. **Value range $164 to $195 a share against $233.04** (no-growth to shown-growth owner cash,
five-year mean $6,577M, at 5.66%); expected return at the price 4.0% to 4.8% after tax, below the ~10% pre-tax floor
(7.86% after tax). Prices the arithmetic implies, not entry language: the shown-growth case earns the floor at $138.83, the
no-growth case at $118.24. **What would reverse it:** the price, or the cash. A quote at or below about $139 brings the
shown-growth case to the floor (and still needs a pencil); or five-year owner cash after every real cost rising enough,
with the partnering support paid, that the no-growth case clears the floor at the quote (about $13.0B a year at $233; it
was $7.0B in 2025). The business is not the reason for the box; the price is.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      commits for Step 0, Q1, Q2, Q3, Q4, Q5, Q6, Q7 and this close.
- [x] Every v5 id resolves (`idcheck.py` against `principle_ledger_v5.csv` before each commit: none missing); every filing
      fact has its accession; one figure is labelled as unchecked memory and was removed (the 2019 restaurant count).
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 and Q9 carry facts marked NOT REACHED, not
      clearances.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): OCF − SBC − all capital spending, with
      a stricter column and the depreciation variant beside it; the sovereign from the US Treasury; the price flagged as an
      aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]**: seven items under the foundations, and at Q1,
      Q2 (items 4, 8, 10), Q3, Q5.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; the run date is
      today and no row postdates it.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII): its v4 ids, floor and verdict language were
      ignored.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **"The growth shown" has no stated measure.** The Q7 convention says the growth is measured on aggregate
owner cash over the five years but not whether by endpoints or by trend; here the endpoint rate is 0.21% and the
log-trend 2.19%, so the top of the range moves from $167 to $195. I took the higher, against the OUT; it did not change the
box, but on a closer name it would. (2) **The floor is pre-tax and the cash is after tax.** The convention says "about ten
percent pre-tax" and the cash input is after corporate tax; the framework gives no converter. I used the filer's effective
rate (21.4%) to get 7.86% after tax, following a sibling run's form, and confessed it as a convention of this run. (3)
**A known, sized future cost has no place in the convention.** The $8.5B of franchisee partnering support announced on
2026-09-23 (rent relief and capital support, about $5B by 2030) is in no year of the five-year record, so the convention's
base ignores it; I kept it out of the arithmetic and set it against the top of the range in words. A rule is wanted for an
announced cost of this size. (4) **All capital spending deducted, with growth measured on the result.** When two-thirds of
capital spending is for new units (here $2,247M of $3,365M in 2025), deducting it all while measuring growth on the
residual can understate both ends; the depreciation variant is the check, and here it also fails the floor, so the box
holds. Smaller: Q5 gives no rule on whether a board's disclosure failure about a predecessor (the 2023 SEC order) is a
doubt about the present management; I judged it was not and wrote down why. **Tool notes:** `tools/run.py` printed the
right total D&A and a five-year window; the one wrong D&A tag (the SG&A-only line after 2017) was in this run's own
`series.py`, caught at the cross-check and replaced by the filed figures. `tools/run.py`'s balance-sheet table has no lease
line, so the 2019 jump in assets (the lease standard) is unexplained in its output until the filing is read; and it does not
flag the unexplained "Other" investing outflow ($579M in 2025), which the operator may want it to show as a line.
