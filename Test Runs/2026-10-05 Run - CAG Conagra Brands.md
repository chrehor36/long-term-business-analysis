# Company Run: Conagra Brands, Inc. (NYSE: CAG), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template to this dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`,
so whether the operator holds CAG is unknown to the analyst. The run is written as for a name not held.

**CONTAMINATION DECLARED.** (1) The session's opening git status showed the subjects of the last five commits: the
2026-10-05 v5 runs of HOS Hornbeck Offshore (OUT at Q2) and CSW CSW Industrials (OUT at Q7), a small-cap triage screen,
a session-state note and a `run.py` change on finance leases; none names CAG or a food company. (2) Listing `Test Runs/`
to check for an earlier CAG file showed the file names (not contents) of other 2026-10-05 runs and research passes
(BN, HRB, MBUU, SONY, TBTC, AROC, ATKR, BOOT and others); no CAG file was listed and none was opened. (3) `tools/run.py`
prints v4 material; only its arithmetic lines are used (Part VII). (4) The analyst's general knowledge of Conagra up to
mid-2025 (the Pinnacle deal, the Lamb Weston spin) is background; every fact used below is from a filing with its accession.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $13.15 (2026-10-05, the live quote printed by `tools/run.py`; an aggregator, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 477,411,517 common shares, $5.00 par, one class (10-Q for the
  quarter ended 2026-08-30, filed 2026-09-30, accession `0001104659-26-112354`; `python Screens/cover_shares.py CAG`).
  The balance sheet shows 584,219,229 issued less 105,666,163 in treasury at 2026-05-31 (10-K, `0001104659-26-083905`).
- **Market cap:** $13.15 x 477.41M = **$6,278M**.
- **Debt beside it** (10-K balance sheet, 2026-05-31): notes payable $34.2M, current installments of long-term debt
  $778.2M, senior long-term debt $6,456.0M; total **$7,268M** against cash of $218.0M. After year end, $500M of 5.400%
  notes due 2031 were issued (8-K filed 2026-07-28, `0000023217-26-000032`), and $762.5M of notes mature in October 2026
  (10-K MD&A). Debt is larger than the market value of the equity.
- **Sovereign for the earnings currency (USD):** **5.63%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-02 (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for the 53-week fiscal year ended 2026-05-31, filed 2026-07-15,
  `0001104659-26-083905`; 10-Q for the quarter ended 2026-08-30, filed 2026-09-30, `0001104659-26-112354`; proxy
  (DEF 14A) filed 2026-08-11, `0000023217-26-000037`; 8-Ks of 2026-02-18 (`0000023217-26-000005`), 2026-04-13
  (`0000023217-26-000013`, chief executive replaced), 2026-06-23 (`0000023217-26-000018`), 2026-07-15
  (`0000023217-26-000022`), 2026-07-28 (`0000023217-26-000028` and `0000023217-26-000032`), 2026-09-28
  (`0000023217-26-000047`, vote results), 2026-09-30 (`0000023217-26-000052`); and the 10-Ks for FY2017 to FY2025
  (`0001628280-17-007184`, `0000023217-18-000005`, `0000023217-19-000006`, `0001564590-20-033366`,
  `0001564590-21-037738`, `0001437749-22-017530`, `0001437749-23-019879`, `0001558370-24-009764`,
  `0001558370-25-009180`) for the ten-year volume, price/mix, margin and balance-sheet record.
- **One figure cross-checked against the filed statement:** net cash from operating activities FY2026 **$1,402.1M** on
  the filed Consolidated Statement of Cash Flows (10-K `0001104659-26-083905`) against 1,402 in `tools/run.py`; also
  D&A $396.0M, stock-settled share-based payments $54.7M and additions to PP&E $423.4M, each matching.
- **`tools/run.py` arithmetic lines only** (USD millions; operating cash less stock pay less capital spending):

| FY end | OCF | stock pay | capex | D&A | OCF less SBC less capex | OCF less SBC less D&A |
|---|---|---|---|---|---|---|
| 2022-05-29 | 1,177 | 26 | 464 | 375 | 687 | 776 |
| 2023-05-28 | 995 | 79 | 362 | 370 | 554 | 546 |
| 2024-05-26 | 2,016 | 31 | 388 | 401 | 1,597 | 1,584 |
| 2025-05-25 | 1,692 | 42 | 389 | 390 | 1,261 | 1,260 |
| 2026-05-31 | 1,402 | 55 | 423 | 396 | 924 | 951 |
| **five-year mean** | | | | | **1,005** | **1,024** |

  (FY2022 and FY2023 from XBRL company facts, first-filed; `run.py` prints the five-year means 1,005 and 1,024, matching.)
  Finance-lease principal (23, 31, 31 in FY2024 to FY2026) is a further capital payment; with it the three-year mean on
  the capex basis is 1,232 (`run.py` alternate). The five-year window holds two abnormal years that pull in opposite
  directions: FY2023's cash was held down by inventory build in the inflation, and FY2024 and FY2025 were lifted by
  working-capital release and "the accelerated receipt of our outstanding receivables initiated in the second quarter of
  fiscal 2025" (10-K FY2026 MD&A, Cash Flows). See the balance-sheet reading below and the COMPUTATION section.

### The balance sheets, nine fiscal year-ends, read before the income account (written here because the file closes before Q4)
The rows ask that balance sheets be read "over an 8 or 10 year period before I even look at the income account"
**[M2025-032]**. From `tools/run.py` (first-filed XBRL), checked against the filed balance sheets of FY2018, FY2019 and
FY2026; net sales from the filed income statements (USD millions):

| year-end | assets | equity | goodwill | brands and intangibles | long-term debt (noncurrent) | retained earnings | inventory | receivables | net sales |
|---|---|---|---|---|---|---|---|---|---|
| 2018-05-27 | 10,390 | 3,676 | 4,502 | 1,284 | 3,232 | 4,745 | 997 | 583 | 7,938 |
| 2019-05-26 | 22,214 | 7,385 | 11,500 | 4,661 | 10,656 | 5,048 | 1,572 | 832 | 9,538 |
| 2020-05-31 | 22,304 | 7,876 | 11,436 | 4,316 | 8,901 | 5,471 | 1,378 | 861 | 11,054 |
| 2021-05-30 | 22,196 | 8,552 | 11,374 | 4,158 | 8,275 | 6,263 | 1,734 | 794 | 11,185 |
| 2022-05-29 | 22,435 | 8,788 | 11,329 | 3,853 | 8,088 | 6,551 | 1,940 | 867 | 11,536 |
| 2023-05-28 | 22,053 | 8,737 | 11,178 | 3,206 | 7,081 | 6,599 | 2,232 | 965 | 12,277 |
| 2024-05-26 | 20,862 | 8,440 | 10,583 | 2,708 | 7,493 | 6,276 | 2,083 | 872 | 12,051 |
| 2025-05-25 | 20,934 | 8,933 | 10,502 | 2,421 | 6,234 | 6,759 | 2,048 | 770 | 11,613 |
| 2026-05-31 | 17,274 | 6,358 | 8,119 | 1,831 | 6,456 | 4,172 | 1,905 | 658 | 11,282 |

**What the figures say.**
1. **The Pinnacle purchase doubled the balance sheet with goodwill and debt.** In FY2019 goodwill rose by $7.0 billion
   and brands by $3.4 billion; noncurrent long-term debt more than tripled. The consideration was "approximately $8.03
   billion": $5.17 billion in cash and 77.5 million shares worth about $2.82 billion issued from treasury; an
   underwritten offering of 16.3 million shares raised $555.7 million (10-K FY2019, `0000023217-19-000006`).
2. **The purchase has since been written down.** Goodwill impairments of $142M (FY2023), $526M (FY2024) and $2,382M
   (FY2026); brand impairments of $589M, $430M, $72M and $547M in FY2023 to FY2026 (filed income statements, 10-Ks of
   FY2025 and FY2026), "primarily related to brands acquired as part of the Pinnacle acquisition" (10-K FY2026,
   Critical Accounting Estimates). Accumulated goodwill impairment in Refrigerated & Frozen is $3.05 billion (10-Q
   `0001104659-26-112354`, goodwill table note).
3. **Tangible equity is negative:** equity $6,358M less goodwill $8,119M less brands $1,831M is about **minus $3.6
   billion** at 2026-05-31.
4. **Debt was paid down slowly and then re-borrowed:** noncurrent long-term debt fell from $10,656M (FY2019) to $6,234M
   (FY2025) and rose to $6,456M (FY2026); total debt is $7,268M, and $500M more was issued in July 2026. Cash is held at
   the minimum in every year ($68M to $553M).
5. **Retained earnings went backwards:** $6,759M to $4,172M in one year, the FY2026 net loss of $1,916.2M plus $670.0M
   of dividends declared (statement of stockholders' equity).
6. **Working capital moved in a way that colours the cash years:** inventory rose from 12.6% of sales (FY2018) to 18.2%
   (FY2023) in the inflation, then was released (16.9% in FY2026); receivables fell from 7.9% of sales (FY2023) to 5.8%
   (FY2026) after "the accelerated receipt of our outstanding receivables in exchange for a slightly higher prompt pay
   discount, which increased our cash flow from operations by approximately $140 million" (10-K FY2025 MD&A,
   `0001558370-25-009180`), a one-time lift. Supplier-finance programme: no instance found (text search of the FY2026
   10-K for "supplier finance" and "supply chain finance").

**What the figures do not say.** They do not show the price each brand gets against the store brand beside it: no
market-share or private-label-share figure appears in the 10-K, the 10-Q or the proxy (text search for "market share",
"dollar share", "category share" finds only risk-factor sentences). The 10-K says of its retailers that larger
retailers can "develop and market their own retailer brands" (10-K FY2026, Item 1A).

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest on this name is the margin of safety read with the foundation that a share is a business: at $13.15
the stock yields about 16% in owner cash on the five-year mean, a figure that screams, and the foundations say what a
scream is worth only after the business questions are answered. The test "if the market closed for five years"
**[M1997-109]** asks whether I would own the business, not the quotation; and the quotation, which has fallen far,
"just tells us prices" **[M2006-077]**. No macro view enters: the run judges "the average profitability of the
business over time and how strong its competitive mode is" **[M2015-016]**, not the consumer cycle. Who is paid to tell
me: the company's own presentation features free cash flow conversion of 119% and adjusted EPS (proxy,
`0000023217-26-000037`), and its impairment tests are its own appraisal of its brands; both are read as the seller's
material. The analyst's habit applied: look for what is wrong, since that is "part of investing" **[M2025-013]**, and
destroy the previous conclusion **[M2016-054]**; the analyst's prior (a cheap, cash-rich brand portfolio) is the
hypothesis to refute.

**Contrary evidence, written down as found** **[M1997-127]**:
1. (against the business) Walmart's share of net sales: 20% (FY2015), 24% (FY2017), 26% (FY2020), 28% (FY2023), 29%
   (FY2025 and FY2026); the ten largest customers about 60% (10-Ks FY2017, FY2020, FY2023, FY2025, FY2026).
2. (against) Refrigerated & Frozen organic price/mix was negative in FY2024 (-1.5%), FY2025 (-3.5%), FY2026 (-1.0%) and
   the first quarter of FY2027 (-1.5%), "primarily attributable to an increase in strategic trade investments" (10-K
   FY2025), while peers still realized price.
3. (against) Gross margin 29.9% in FY2017, 23.9% in FY2026, the lowest of the decade, after the largest price increases
   of the decade (filed income statements).
4. (against) Brand royalty rates were cut in the company's own impairment tests "due to lower-than-expected profit
   margins" (10-K FY2026 MD&A); Birds Eye was written down twice in FY2026 (10-K FY2026, Note 9).
5. (against) The dividend was halved, $0.35 to $0.175 a quarter, after FY2026 (10-K FY2026 MD&A, Equity and
   Dividends); the board removed the chief executive (8-K `0000023217-26-000013`).
6. (against) First quarter FY2027: Grocery & Snacks organic volume -5.4% on +3.4% price/mix; operating profit $268.4M
   against $347.4M, -22.7% (10-Q `0001104659-26-112354`).
7. (FOR the business) Much of the FY2026 impairment was driven by the discount rate: "a 150-basis point increase" in the
   second quarter and "a 200-basis point increase" in the fourth, with "lower market multiples in our industry", beside
   "a downward revision to our projected sales and profit margins" (10-K FY2026, Note 9). The write-downs are partly a
   rate and market event, not only an operating one.
8. (FOR) The inflation-year volume loss was industry-wide: General Mills -8 points of volume against +15 of price and
   mix (FY2023); Campbell's volume/mix -4% against +13% net price (FY2023); Kraft Heinz -3.4 pp against +13.2 pp (2022);
   Smucker -5 pp against +14 pp (FY2023). Conagra's price episode alone does not single it out (competitor row, Q2).
9. (FOR) The tangible capital the brands need is small: receivables, inventory and prepaid less payables and accruals is
   about $290M, plus net PP&E of $2,863M, about $3.15 billion, against operating profit before impairments of $1,259M
   in FY2026, about 40% pre-tax on tangible operating capital (10-K FY2026). A business with no castle at all would not
   earn that.
10. (FOR) Refrigerated & Frozen volume was +0.3% in FY2026, and FY2025's frozen volume was cut by "supply constraints"
   in chicken and vegetables rather than by demand (10-K FY2025).

## THE STANDING RULE
Owning a slice of CAG bought with the buyer's own money and sized so that its loss could be borne does not put the
buyer at risk of ruin: "always be sure you can play the next day" **[M2025-015]**; "borrowed money has no place in the
investor's tool kit" **[L2014-005]**. The company's own leverage (debt above the market value of the equity) is the
target's exposure, for Q9, not this rule. No breach.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding means "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**, with a reasonable probability of assessing
  where the business will be in ten years **[M2000-037]**.
- **The key variables**, "trying to identify the key variables in that particular business" **[M1998-044]**: (a) unit
  volume by segment; (b) net price after trade spending (price/mix); (c) input costs against the power to pass them
  through; (d) the terms the large retailers set, Walmart above all; (e) interest on $7.3 billion of debt. Each is
  reported every year (ten 10-Ks read), and the record is long enough that "the financial statements will tell me the
  information" needed to judge the future ones **[M2008-033]**.
- **Customers or technology?** The forecast is about consumer and retailer behaviour in frozen meals, shelf-stable
  goods and snacks; the rows separate this kind of analysis, "in terms of laying out what their prospective customers
  will do in the future" **[M2017-019]**, and count it among "what we think we can project out in terms of consumer
  behavior and threats to a business" **[M2023-030]**. The one change the filer names, weight-loss drugs, is a change in
  consumer behaviour that the company itself writes down and forecasts (10-K FY2026 MD&A, Trends), so the insiders do
  write this forecast down **[M2000-105]**.
- **Where it will be in ten years**, as the filings let me picture it: the same categories, sold mostly through the
  same few retailers, with unit volume flat to falling and a margin set by how much price the brands can hold against
  store brands and trade demands. A picture with a direction; whether it shows a castle is Q2's question.
- **Routing.** Not a fast-changing industry; not a financial institution. Ardent Mills (44%, equity method) is a flour
  miller whose dividends are already inside operating cash (equity earnings less than or in excess of distributions:
  +0.4, -22.1, +74.0 in FY2026, FY2025, FY2024; cash flow statement), so the Q4 convention on equity-method income is met
  by the cash figure.
- **VERDICT: IN.** The economics can be pictured ten years out from the filings; the key variables are known and
  reported **[M1998-044]**, **[M2012-065]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" and of its key factors, "how permanent are they?" **[M1995-038]**.

**The tests, each with its filing fact.**

1. **Pricing power and the agony before a rise.** The positive form is to "charge more for a product and maintain or
   increase market share" **[M2000-031]**; strength is measured "by the agony they go through" **[M2005-020]**. The
   organic record from each year's 10-K:

   | fiscal year | Grocery & Snacks volume | G&S price/mix | Refrigerated & Frozen volume | R&F price/mix |
   |---|---|---|---|---|
   | 2017 | -5% | flat | -9% | +1% |
   | 2018 | -2% | flat | +3% | flat |
   | 2019 | flat | flat | +1% | flat |
   | 2020 | +10% | -1% | +5% | +1% |
   | 2021 | +4% | +2% | +4% | +4% |
   | 2022 | -4% | +7% | -5% | +8% |
   | 2023 | -9% | +15% | -7% | +13% |
   | 2024 | -3.1% | +2.6% | -4.1% | -1.5% |
   | 2025 | -1.1% | -0.9% | -0.7% | -3.5% |
   | 2026 | -2.4% | +2.3% | +0.3% | -1.0% |
   | Q1 FY2027 | -5.4% | +3.4% | -0.1% | -1.5% |

   Compounding the reported percentages (CONVENTION of this run: the early years are reported in whole percents, so
   the product is approximate), US retail volume fell about **13% in Grocery & Snacks and about 13% in Refrigerated &
   Frozen over FY2017 to FY2026**, through a pandemic surge. The price taken in FY2022 and FY2023 stuck in shelf-stable
   goods; in frozen it was followed by three straight years of negative price/mix as the company bought volume back with
   what its 10-K for FY2025 calls strategic trade investments, and volume still did not come back. The rows' warning fits the frozen
   record: pricing "pushed" past the moat "to the point that they lost market share" **[M2001-087]**, and "too wide a
   differential" against a private label changes consumption **[M2001-088]**. The company names its own agony: it "may
   need to increase prices on certain products in fiscal 2027" and "would expect corresponding elasticity impacts" (10-K
   FY2026 MD&A, Trends); the first quarter then showed -5.4% volume on +3.4% price in Grocery & Snacks.

2. **Passing costs through over time.** "the businesses with strong competitive positions manage to pass through
   increases in raw material costs", with the allowance for "temporary situations where, sometimes, the costs are
   increasing faster" **[M2005-017]**. Gross margin (filed income statements): FY2017 29.9%, FY2018 29.6%, FY2019 27.8%,
   FY2020 27.8%, FY2021 28.4%, FY2022 24.6%, FY2023 26.6%, FY2024 27.7%, FY2025 25.9%, **FY2026 23.9%**. Operating
   profit before impairments and divestiture results (gross profit less SG&A as filed; FY2023 and FY2024 as restated in
   the FY2025 10-K): FY2022 $1,346M (11.7% of sales), FY2023 $1,833M (14.9%), FY2024 $1,846M (15.3%), FY2025 $1,466M
   (12.6%), FY2026 $1,259M (11.2%). Five years after the inflation began, the cost has not been passed through: the
   gross margin is below every pre-inflation year. **This is the single fact on which the question turns.**

3. **The brand against the retailer.** "the value of having the brand moves over to the retailer from the product
   itself" **[M2001-090]**; the narrated Kraft Heinz error was to underestimate "not what the consumer is doing so much,
   but what the retailer is", where "the brand is our protection against the intermediaries making all the money"
   **[M2019-041]**; "the retailer is going to use all the pressure" **[M2015-038]**. Filing facts: Walmart 20% of net
   sales in FY2015, 29% in FY2026, rising in eleven years without a reversal; the ten largest customers about 60%; the
   10-K's own risk factor that retailers are "more capable of resisting price increases" and can "develop and market
   their own retailer brands" (10-K FY2026, Item 1A). A competitor's filing names the shift outright: Post's FY2023
   cereal volume fell "primarily due to price elasticities and a shift towards private label products" (Post 10-K
   FY2023, `0001530950-23-000350`).

4. **Would the customer still choose it over the low bid?** See's was bought because buyers would not choose candy "for
   the low bid" **[M2017-009]**; the brand earns "better gross of margins if they ask for you by name" **[M2023-073]**.
   Conagra's gross margin is the lowest in its peer group in every year compared (row below), and its frozen brands
   needed price cuts to hold volume: on the company's own numbers, the customer took the low bid more often.

5. **Unit volume and share of mind.** "We measure it by unit cases sold" **[M1999-054]**: down about 13% in both US
   retail segments over the decade. Volume decline alone is not a fail; Duracell "will have unit declines over a period
   of time" and was held **[M2015-066]**. What makes it a fail here is that the decline came with a falling margin, not
   with a held price.

6. **The attacker.** The attacker needs no money: it is the retailer's own label on the next facing, on a shelf
   Conagra pays trade spending to hold; "one competitor is frequently enough to ruin a business" **[M2012-108]**. No
   filing gives Conagra's private-label exposure by category; that fact is not obtainable from the primary documents
   (searches recorded in Step 0).

7. **Is the moat widening or narrowing?** The question is whether it is "likely to widen further or shrink on you"
   **[M1999-108]**; whether "the competitive advantage" could "have been made stronger and more durable" is "more
   important than the P&L" **[M2000-075]**; positions grow "either weaker or stronger" **[L2005-010]**. On every measure
   the filings carry (margin, volume, customer concentration, and the company's own appraisal of its brands, whose
   royalty rates it cut "due to lower-than-expected profit margins") the position grew weaker.

8. **What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**: further retailer
   concentration, the store brand, and the weight-loss drugs the company names. "slow change can be much harder to
   perceive" **[M2014-038]**; here the change is slow and visible.

9. **Cyclical or secular?** A bad stretch may be read as "a cyclical problem, not a secular one" where the business
   "at least maintained" its superiority **[L1995-022]**. This is the strongest case for the company: the inflation of
   FY2022 to FY2026 squeezed every food maker (contrary items 7 and 8). Against it: in the competitor row Conagra's
   margin fell further than General Mills', Kraft Heinz's, Smucker's and Post's; its frozen price/mix was negative three
   years running while peers still realized price; and its dependence on Walmart rose through the whole decade, before
   and after the inflation. It did not maintain its place within the group; it lost ground inside an industry that
   itself lost ground.

**The competitor row.** Gross margin = (net sales less cost of goods sold) over net sales, from XBRL company facts
(first-filed, `data.sec.gov/api/xbrl/companyfacts/CIK<cik>.json`); volume and price from each company's 10-K MD&A;
owner-cash margin = (operating cash less stock pay less capital spending) over net sales, averaged over the years shown.

| company | gross margin, first year | gross margin, latest | inflation year: volume against price | latest year: volume against price | owner-cash margin, span average | 10-Ks read |
|---|---|---|---|---|---|---|
| **Conagra (CAG)** | 29.9% (FY2017) | **23.9%** (FY2026) | FY2023 G&S -9% / +15%; R&F -7% / +13% | FY2026 G&S -2.4% / +2.3%; R&F +0.3% / -1.0% | 9.1% (FY2017 to FY2026) | as Step 0 |
| General Mills (GIS) | 35.2% (FY2016) | 33.6% (FY2026) | FY2023 volume (tons) -8 pts / price and mix +15 pts | FY2026 organic net sales -2%; goodwill impairment $1.5B (XBRL) | 12.3% (FY2016 to FY2026) | `0001193125-23-177500`, `0001628280-26-046466` |
| Campbell's (CPB) | 34.9% (FY2016) | 28.1% (FY2026) | FY2023 volume/mix -4% / net price +13% | FY2026 volume/mix -3% / net price +1% | 9.3% (FY2016 to FY2026) | `0000016732-23-000109`, `0000016732-26-000026` |
| Kraft Heinz (KHC) | 35.8% (2016) | 33.3% (2025) | 2022 volume/mix -3.4 pp / price +13.2 pp | 2025 volume/mix -4.1 pp / price +0.7 pp | 10.4% (2016 to 2025) | `0001637459-23-000009`, `0001637459-26-000009` |
| J.M. Smucker (SJM) | 38.0% (FY2016) | 33.5% (FY2026) | FY2023 volume/mix -5 pp / price +14 pp | FY2026 volume/mix -4 pp / price +9 pp (coffee) | 10.6% (FY2018 to FY2026) | `0000091419-23-000072`, `0000091419-26-000050` |
| Post (POST) | 30.8% (FY2016) | 28.7% (FY2025) | FY2023 branded cereal volume down, private label up | FY2025 pet food volume -9%, cereal -4% | 5.3% (FY2016 to FY2025) | `0001530950-23-000350`, `0001530950-25-000260` |

(Campbell's FY2017 and FY2018 gross margins are left out: the XBRL tags give 57.0% and 51.2%, a tagging fault. Gross
margin is used across the row because it carries no impairments; General Mills' FY2026 and Kraft Heinz's 2025 operating
margins carry large ones. Fiscal years end in different months, so each year compared pairs the nearest fiscal year.)
Read over the whole span: every name lost volume when it priced in 2022 and 2023; every name's gross margin is lower now
than at the start; four of the six wrote down brands or goodwill in the last three years. Conagra has the lowest gross
margin of the six in every year compared, the second-largest fall (6.0 points, against Campbell's 6.8, Smucker's 4.5,
Kraft Heinz's 2.5, Post's 2.1, General Mills' 1.6), and an owner-cash margin below General Mills', Kraft Heinz's and
Smucker's, level with Campbell's, above Post's. The group's moats are "filling up with sand" **[M2009-106]**, and
Conagra's is among the shallowest of them.

**Why not TOO HARD.** The rows leave alone the moat that is tenuous because it cannot be valued, "therefore we leave it
alone" **[M2000-019]**; they close OUT the castle shown filling in **[M2011-015]**. The deciding facts here are in hand
from primary filings and run one way across ten years and six companies. What is missing (category-level private-label
share) would size the gap, not reverse its direction, since the company's own brand appraisals already cut royalty
rates for lower margins. Nor is this a forecast the insiders would refuse to write **[M2000-105]**: the company writes
it, and its own impairment tests read it lower. Not TOO HARD (WORK), not TOO HARD (NATURE).

**Price does not reopen it.** No one can "turn any investment into a good deal by paying little" **[M2019-015]**;
"marginal businesses purchased at cheap prices may be attractive as short-term investments" but are the wrong
foundation **[L2014-009]**; "If you really think a business is declining, most of the time you should avoid it."
**[M2012-062]**.

- **VERDICT: OUT.** The castle is shown on the evidence to be filling in. After the largest price increases of the
  decade the gross margin is the lowest of the decade (29.9% in FY2017, 23.9% in FY2026): the cost was not passed
  through **[M2005-017]**. Volume fell about 13% in both US retail segments; the frozen brands bought volume back with
  price; Walmart rose from 20% to 29% of sales **[M2001-090]**, **[M2019-041]**; and the position narrowed against the
  peers' own filings **[M1999-108]**, **[M2000-075]**. A castle being filled in closes OUT **[M2011-015]**, in the
  rows' boxes "in, out, and too hard" **[M2006-013]**.

**The file closes here.** Q3 to Q10 and Q12 are NOT REACHED. Nothing below is a clearance.

---
## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (the balance-sheet reading is in Step 0).
## Q5: WHO RUNS IT. NOT REACHED.
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7: WHAT IS IT WORTH. NOT REACHED (computation below, not a clearance).
## Q8: BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9: COULD IT RUIN US. NOT REACHED.
## Q10: THE FAT PITCH. NOT REACHED.
## Q12 (optional): PROUD OF HOW THE MONEY IS MADE. NOT REACHED.

**Facts recorded for the questions not reached, not judged** (written down as found, so a later run need not find them
again):
- *Q3:* tangible operating capital about $3.15 billion against FY2026 operating profit before impairments of $1,259M
  (contrary item 9); on the capital actually paid, goodwill and brands included, the return is far lower. FY2027
  capital spending is guided at about $550M against D&A of $396M (10-K FY2026 MD&A).
- *Q4:* restructuring charges every year (FY2025 $101.7M, FY2026 $45.7M); legacy legal items (FY2025 $88.7M charge,
  FY2026 $37.4M benefit); a $140M one-time receivables acceleration in FY2025 operating cash. The proxy features free
  cash flow conversion of 119% and adjusted EPS of $1.46 against a GAAP diluted loss of $4.00 (proxy
  `0000023217-26-000037`; 10-K). The rows say "a management that regularly attempts to wave away very real costs" by
  highlighting "adjusted per-share earnings" makes them nervous **[L2016-006]**: one tell, recorded, not judged.
- *Q5:* the board removed the chief executive (8-K `0000023217-26-000013`: "the Board has determined that Sean Connolly
  will cease to serve"); the new chief executive came from Smucker on a $1.15M salary, a $7.3M annual equity target and
  $6.0M of sign-on equity; the chief operating officer retired and the post was eliminated (8-K `0000023217-26-000028`).
- *Q6:* the $1.40 dividend (about $670M a year) was paid in full through FY2026 while debt stood above $7 billion and
  owner cash fell to $924M, then halved. Pinnacle was paid partly with 77.5 million shares at about $36.4 each ($2.82B /
  77.5M) and 16.3 million more were sold at about $34.1 ($555.7M / 16.3M), against $13.15 today. In the first quarter
  of FY2027, 2.7 million shares were bought for $44.0M, about $16.30 a share (10-Q), under an authorization that names no
  price. Performance shares pay on adjusted EPS (70%) and adjusted net sales (30%), with the FY2024 to FY2026 targets set
  "based on prior-year performance" (proxy); short-term incentive expense rose $41.6M in a year with a $1.9 billion net
  loss (10-K FY2026 MD&A). Say-on-pay passed 146,934,886 for to 142,473,328 against (8-K `0000023217-26-000047`).
- *Q9:* total debt $7,268M against a market value of $6,278M; $762.5M matures in October 2026; the revolver covenant
  caps funded debt at 4.5 times EBITDA (10-K FY2026 MD&A); unconditional purchase obligations $2.72 billion.

---
## COMPUTATION - NOT A CLEARANCE
*Operator rule 3: valuation arithmetic after a closing STOP, carrying no entry language. Reported at the owner's
request, not as a step of the run. The file closed OUT at Q2, and no price below makes the name a purchase.*

**Inputs.** Owner cash after every real cost, earnings in the rows' sense, "after interest, taxes, depreciation,
amortization and all forms of compensation" **[L2021-003]**: operating cash less stock pay less all capital spending,
five-year mean FY2022 to FY2026 **$1,005M** (D&A variant $1,024M). Operating cash is after interest, so the value is of
the equity and debt is not subtracted again. Rate 5.63% (30-year Treasury, 2026-10-02). Shares 477.41M.

**Growth shown.** On the aggregate owner cash the five years run 687, 554, 1,597, 1,261, 924; the endpoint rate (+7.7%
a year) and the log trend (+15% a year) are working-capital artifacts (inventory built in FY2022 and FY2023, released in
FY2024; receivables accelerated in FY2025): the case of "the beginning and terminal years" being "selected"
**[L2005-003]**. Under the convention's cap on a rate that traces to an absurdity, this run measures growth on the
operating profit behind the cash: $1,346M (FY2022) to $1,259M (FY2026), **-1.66% a year**. (CONVENTION of this run:
growth measured on operating profit before impairments when working capital drives the owner-cash series; rationale:
a cash series rising 15% a year while sales and operating profit fall is the absurdity the convention's own cap
forbids.) FY2024 to FY2026 alone the operating decline is -17.4% a year; the first quarter of FY2027 is -22.7%.

**VALUE RANGE** (the Q7 convention: five-year mean, carried ten years at the growth shown, then zero nominal growth, at
the sovereign):

| case | owner cash input | growth, years 1 to 10 | equity value | per share |
|---|---|---|---|---|
| shown-growth end (a decline) | $1,005M | -1.66% | $15,662M | **$32.81** |
| no-growth end | $1,005M | 0% | $17,851M | **$37.39** |

**$32.81 to $37.39 against $13.15**; top over bottom 1.14, inside the three-to-one width. (D&A variant: $33.43 to
$38.10.)

**Whole-cycle variant** (the window holds abnormal years: FY2024's $2,016M operating cash and FY2025's receivables
acceleration). Owner cash rebuilt from earnings each year so that working capital drops out: (operating profit before
impairments + about $184M of Ardent Mills dividends - net interest) x (1 - 24%) + D&A - capital spending = FY2022
$785M, FY2023 $1,230M, FY2024 $1,229M, FY2025 $939M, FY2026 $779M; mean **$992M**. At -1.66% and at no growth:
**$32.39 to $36.91**. On the FY2026 run-rate alone ($779M) at -1.66%: **$25.42**. (CONVENTION of this run: the rebuild,
the 24% rate, which is the company's guided FY2027 effective rate (10-K FY2026 MD&A), and the $184M, the mean
of distributions of $251.6M, $160.3M and $141.1M in FY2024 to FY2026 from the cash flow statement; rationale: they
remove the working-capital swings that the five-year mean cannot. FY2022 SG&A as filed may hold small brand charges.)

**What the price implies.** At $13.15 the market value of $6,278M equals the convention's arithmetic only if owner cash
falls about **13.7% a year for ten years** (on $1,005M) or **10.2% a year** (on $779M) and then holds. The last two
years' operating decline (-17.4% a year) is steeper than that; the five-year decline (-1.66%) is far gentler. The price
is a bet on which rate the next decade follows, which is the Q2 question, already answered against the business.

**FAIR PRICE** (the price at or below which the central case clears the floor). The floor is the Q7 CONVENTION, about
10% pre-tax: "a very high probability of at least 10% pre-tax returns" **[L2002-020]**, "a point at which we drop out
of the game" **[M2003-149]**. Tax treatment: owner cash is after corporate tax, so the floor is applied after tax at 10%
x (1 - 24%) = **7.6%** (CONVENTION of this run; 24% is the company's guided rate). Expected return at a price = owner-cash
yield + growth. Central case (the convention's own input and shown growth, $1,005M at -1.66%): 1,005 / (7.6% + 1.66%)
= $10,857M = **$22.74 a share**. Run-rate variant ($779M at -1.66%): **$17.62**. No-growth case: $27.70.

**CHEAP PRICE** (below which no pencil is needed). Rule of this run (CONVENTION, ours): the price at which the FY2026
run-rate owner cash ($779M), falling **10% a year forever**, still returns the 7.6% after-tax floor: 779 / (7.6% + 10%)
= $4,426M = **$9.27 a share**. Rationale: a 10% perpetual decline halves the cash in under seven years, harder than the
decade's -1.66% and than the price-implied rate on the run-rate input; below that price every case drawn from the
filings clears the floor except the last two years' -17% carried forever, so the answer would "scream at you"
**[M2009-005]** without the arithmetic.

At $13.15 the price sits below the fair price of every case and above the cheap price. The arithmetic screams; the
castle does not stand behind it. That pairing is the one the rows describe in "marginal businesses purchased at cheap
prices" **[L2014-009]**.

---
## THE BOX
**OUT**, decided at **Q2**: the castle is shown on the evidence to be filling in. Not reached: Q3 to Q10, Q12.
COMPUTATION only: value range $32.81 to $37.39 (whole-cycle $32.39 to $36.91; FY2026 run-rate $25.42); fair price
$22.74 (run-rate $17.62); cheap price $9.27; against $13.15. Not a TOO HARD, so no research pass is opened. Q11 belongs
to the holding review, not to a purchase run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written in stages (Step 0 first, then each question). **Not
      committed:** the dispatch for this run forbids commits, so the write-early commits were
      not made.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (script
      check, recorded below); every filing fact carries its accession; numbers carry a filing or a CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance; the
      computation is headed as such and carries no entry language.
- [x] Owner cash after every real cost (operating cash less stock pay less all capital spending), never a net-income
      proxy; the sovereign from the US Treasury; the price quote flagged as an aggregator's.
- [x] Contrary evidence was written down as it was found **[M1997-127]**: ten items, four of them for the business.
- [x] No row dated after the anchor: the run is dated today, not point-in-time.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 verdict text, ids and floor were ignored.
- [x] `python tools/check_framework.py` run after the file was complete; result recorded below.

**Check results (2026-10-05):** see the closing lines of this file.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The Q7 convention measures growth on aggregate owner cash, and on this name that series is a working-capital
artifact** (+15% a year by trend, +7.7% by endpoints, while sales and operating profit fell). The convention caps growth
by Q3's absurdity test but does not say what to measure instead; this run measured growth on operating profit before
impairments and confessed it. A rule is needed for which series carries the growth shown when working capital moves
the cash more than the business moved. (2) **The convention's two ends assume the shown growth is at or above zero.**
When it is negative, the shown-growth end becomes the bottom and the no-growth case the top; the text does not say so,
and a reader may take no growth as the conservative end when it is the generous one. (3) **A sovereign-rate valuation of
a declining, levered business produces a screamer by construction** ($32.81 to $37.39 against $13.15), because the
rows put no risk in the rate and leave certainty to Q1, Q2 and the margin. The hard sequence is what keeps this from
reading as a buy; a run that reached Q7 on a softer Q2 reading would find the convention saying IN. The convention would
gain from requiring the price-implied decline (here about -10% to -14% a year) to be set beside the shown rate whenever
the range sits far above the price. (4) **Q2 gives no test for separating a cyclical squeeze from a secular one** beyond
the "at least maintained" of **[L1995-022]**; this run used the competitor row for it, and the framework might say that
the competitor row is where that test is run. (5) **Operator rule 3 and the template's headings use the em dash**
("COMPUTATION" followed by an em dash), which the standing no-em-dash rule forbids; this file uses a hyphen and colons.
(6) **The write-early commits are a self-audit line, but this dispatch forbade commits;** the line says so rather than
pretending the commits were made.

---
**Check results, 2026-10-05.** `python tools/check_framework.py`: **PASS** (TEST RUNS: 1882 files, phantom ids in 0
files; output saved in `Test Runs/_research 2026-10-05 CAG/check_framework.txt`). Script check of this file
(`Test Runs/_research 2026-10-05 CAG/idcheck.py`): 61 id citations, 49 distinct, every one present in
`principle_ledger_v5.csv`; no E-ids (v4) cited; every quoted fragment standing beside an id found in that id's row
(after folding curly to straight quotes); no em dashes.

**Correction written down as found.** The first draft of the whole-cycle variant used $165M for the Ardent Mills
dividends; the mean of the three filed distributions ($251.6M, $160.3M, $141.1M) is $184.3M. The variant, the run-rate
value, the run-rate fair price, the price-implied decline on the run-rate and the cheap price were recomputed before the
file was finished: whole-cycle $31.91 to $36.37 became $32.39 to $36.91; run-rate value $24.94 became $25.42; run-rate
fair $17.29 became $17.62; implied decline 9.9% became 10.2%; cheap $9.09 became $9.27. The box does not move: the file
closed at Q2. The arithmetic is in `Test Runs/_research 2026-10-05 CAG/calc.py`.
