# Company Run — Tractor Supply Company (NASDAQ: TSCO) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. This run was dispatched under a blind rule that forbids opening
`PORTFOLIO.md`, any holding review, the two earlier TSCO run files (2026-07-15, 2026-09-04) and their research folder, the
session-state files, the run queue and the prepped reading list; none was opened. **Contamination declared:** the
session's opening context listed a recent commit message, "Session state: TSCO added to the reviews", which suggests the
name may be held or under review. I did not pursue it. The analyst also carries general prior knowledge of the company from
training, which the filings below were read to replace, not to confirm. The verdict below is not conditioned on either.

**Working folder:** `Test Runs/_research 2026-10-05 TSCO/` (filings as text, `run_py_output.txt`, `q7.py`, `peers/`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $30.80 (Yahoo chart meta, regularMarketTime 2026-10-05; **aggregator, live quote only, flagged** per operator
  rule 5). Context, same source: 52-week high $58.21, low $28.36; about $55 in February 2026, $45.02 on 2026-04-14,
  $35.59 on 2026-04-28, about $30.6 through May to July 2026.
- **Shares by class** from the latest filing's cover: **521,040,137** common shares, $0.008 par, one class
  (10-Q for the quarter ended 2026-06-27, filed 2026-08-06, accession `0000916365-26-000059`, cover as of 2026-07-25;
  `python Screens/cover_shares.py TSCO`). No preferred outstanding (FY2025 10-K balance sheet note: "no shares were issued
  or outstanding").
- **Market cap:** $30.80 x 521.04M = **$16,048M** (my arithmetic).
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, 10/02/2026
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025 (year ended 2025-12-27), filed 2026-02-19, accession `0000916365-26-000014` (Items 1, 1A, 2, 5, 7, 8: the
    statements, Notes 3 Allivet, 5 debt, 6 leases, 8 treasury stock).
  - 10-Q Q1 2026 (quarter ended 2026-03-28), filed 2026-05-07, accession `0000916365-26-000024`.
  - 10-Q Q2 2026 (quarter ended 2026-06-27), filed 2026-08-06, accession `0000916365-26-000059` (balance sheet, cash flow,
    Note 3 VIP Petcare, Note 11 impairment and restructuring, MD&A).
  - DEF 14A filed 2026-03-26, accession `0001193125-26-126620` (pay, retention award, ownership).
  - 8-Ks of 2026: Q4 2025 results 2026-01-29 (`0000916365-26-000005`); dividend and director 2026-02-11
    (`0000916365-26-000009`); Q1 2026 results 2026-04-21 (`0000916365-26-000020`); annual meeting vote 2026-05-15
    (`0000916365-26-000033`); credit agreement 2026-05-21 (`0000916365-26-000039`); VIP Petcare 2026-05-28
    (`0000916365-26-000046`); Q2 2026 results 2026-07-23 (`0000916365-26-000052`); officer change 2026-08-07
    (`0000916365-26-000063`); $500M notes 2026-08-25 (`0000916365-26-000065`).
  - Earlier 10-Ks FY2015 to FY2024 for the comparable-sales split, store counts and the Orscheln acquisition (FY2022 10-K,
    accession `0000916365-23-000045`; the others listed in `run_py_output.txt`).
- **One figure cross-checked against the filed statement:** total assets at 2025-12-27, **$10,933,679 thousand** on the
  filed Consolidated Balance Sheet (10-K, `0000916365-26-000014`), against $10,934M in the `tools/run.py` table; and net
  cash from operations FY2025 **$1,635,259 thousand** on the filed cash-flow statement against $1,635M. Both agree.
- `python tools/run.py TSCO`, **arithmetic lines only** (Part VII; its v4 ids, floor and verdict language ignored):

  | FY end | OCF | SBC | D&A | capex | owner cash, all capex (OCF − SBC − capex) | depreciation variant (OCF − SBC − D&A) |
  |---|---|---|---|---|---|---|
  | 2021-12-25 | 1,139 | 48 | 270 | 628 | 463 | 821 |
  | 2022-12-31 | 1,357 | 54 | 343 | 773 | 530 | 960 |
  | 2023-12-30 | 1,334 | 57 | 393 | 754 | 523 | 884 |
  | 2024-12-28 | 1,421 | 48 | 447 | 784 | 588 | 925 |
  | 2025-12-27 | 1,635 | 57 | 494 | 895 | 683 | 1,084 |
  | **five-year mean** | | | | | **557** | **935** |

  ($M; the 2023 to 2025 rows are the tool's; 2021 and 2022 are the same arithmetic on the XBRL of the filed 10-Ks, script
  in the research folder.) SBC is resolved and complete: it is expensed in the income statement and subtracted again here
  because the cash-flow statement adds it back. Net income over the same five years: $997M, $1,089M, $1,107M, $1,101M,
  $1,096M. **Owner cash after every real cost runs at about half of reported net income**, because capital spending has
  run at 1.6 to 2.3 times depreciation since 2021.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is **the market serves, it does not instruct** **[M2006-077]**: the quote fell from about
$55 to $31 in four months of 2026, and that fall "doesn’t tell us anything. It just tells us prices." **[M2006-077]**. The
analyst's own habit is at risk the other way, an anchor on the old price; the rule is "We really try and destroy our
previous ideas." **[M2016-054]**. **A share is a business** **[M1997-109]**: the question is whether I would be content to
own 2,463 rural stores if the market closed for five years, judged on the business. **Margin of safety** **[M1996-084]**
governs Q7. **No macro enters** **[M2000-094]**: the filings' tariff and weather paragraphs are read as properties of the
business, not forecasts. **Who is paid to tell you** **[M2020-037]**: the company's "Adjusted" earnings in the Q2 2026
release are rebuilt from GAAP lines below, and its December 2024 long-term framework was withdrawn by the company itself.

**Contrary evidence, written down as found** **[M1997-127]**:
1. Q2 2026 comparable sales −1.5%, transactions −1.7%; first half −0.6%, transactions −1.4% (10-Q `0000916365-26-000059`).
2. Guidance cut on 2026-07-23 to EPS $1.78 to $1.88 from $2.13 to $2.23, and "the Company is withdrawing the long-term
   financial framework introduced at its December 2024 Investor Day" (8-K `0000916365-26-000052`).
3. Petsense: "closure of approximately 75 stores" of 209, goodwill written to zero, $71.7M charges (10-Q Note 11).
4. "incremental investments to strengthen the Company's price-value position" (10-Q MD&A, Q2 gross margin): a retailer
   cutting price to hold traffic.
5. Inventory $3,518M at 2026-06-27 against $3,090M a year earlier, **+13.9%**, while first-half sales rose 2.9% and the
   store count 5.1% (10-Q balance sheet and MD&A); a search of the 10-Q for "inventor" found no explanation of the build.
6. Operating income flat for four years: $1,435M (2022), $1,479M, $1,468M, $1,467M (2025), while capital spending ran
   $754M to $895M a year and lease liabilities rose from $3,068M to $4,142M.
7. Revolver borrowings rose from $230M to $620M in the first half of 2026 while $253.6M was spent on buybacks
   (10-Q debt table and cash flow); $500M of 5.200% notes were sold on 2026-08-25 to repay the revolver.
8. The chief technology, digital and pet services officer resigned effective 2026-08-07 (8-K `0000916365-26-000063`).

## THE STANDING RULE
Owning this, bought for cash with no borrowed money, does not by itself put the buyer at risk of ruin; the rule binds the
buyer's financing and sizing, which this run does not see: "borrowed money has no place in the investor's tool kit"
**[L2014-005]**; "We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The business, from the 10-K (Item 1):** "the largest rural lifestyle retailer in the United States", 2,395 Tractor
  Supply stores and 207 Petsense stores at 2025-12-27 (2,463 and 209 at 2026-06-27), 15,000 to 20,000 square feet of
  inside selling space plus a side lot, "located primarily in towns outlying major metropolitan markets and in rural
  communities"; it "act[s] as a trip consolidator for numerous needs-based requirements". Sales by category FY2025:
  livestock, equine and agriculture 27%, companion animal 24%, seasonal and recreation 24%, truck, tool and hardware 15%,
  clothing, gift and décor 10%. Owned and exclusive brands about 30% of sales. Leases about 97% of its stores.
- **The key variables** **[M1998-044]**: transaction count, ticket, store count, the gross margin and the cost of a store.
  They are reported every year, and their record is long and fairly stable: comparable transactions +3.2% (2014), +3.3%,
  +2.6%, +2.2%, +2.2%, +0.3% (2019), +10.9% and +7.1% in the pandemic years, then −0.6%, −0.4%, +0.8%, +1.4% (2025) and
  −1.4% in the first half of 2026; operating margin 10.4% (2015), 10.2%, 9.5%, 8.9%, 8.9% (2019), 9.4%, 10.3%, 10.1%,
  10.2%, 9.9%, 9.5% (2025) (10-Ks FY2015 to FY2025, MD&A). The past statements do tell me something about the future ones
  **[M2008-033]**: a decade in which margins stayed between 8.9% and 10.4% through a pandemic, a tariff cycle and an
  inflation.
- **Customers or technology?** The forecast is about what rural customers will buy and where **[M2017-019]**,
  **[M2023-030]**: feed, bedding, fencing, pet food, propane, trailers. What changes fast is the channel for the part of the
  basket that ships cheaply, chiefly pet food and pet medicine.
- **Against, from the rows:** retail is the arena where the speakers say they most often misjudged their own circle: "I
  think it’s easy to sort of think you understand retail, and then subsequently find out you don’t" **[M2014-052]**; "many
  retailing businesses I can think of [...] I’m not sure I’d know where we would stand in the competitive pecking order five or 10 years from now." **[M1996-062]**;
  "the internet, in many forms of retailing, is likely to pose such a threat that we simply wouldn’t want to get into the
  business." **[M1999-013]**; "anything that can be easily bought by using a home computer [...] I think it’s terrible for most retailers." **[M2012-047]**. The same speakers bought retailers with "records [...] market positions,
  and [...] managements" they liked while calling it "a very tough business" **[M1996-102]**.
- **Reading.** Understanding means "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**. For the farm, ranch and rural half of the basket I have that fix: the goods are
  heavy, bulky and needed weekly, sold in towns that larger formats do not serve with the same assortment, and the ten-year
  record of the key variables is in the filings. For the companion-animal quarter of sales the forecast is about online
  substitution, which is a customer question, not a technology one, and its size is bounded and reported. The doubt I
  hold is about how wide the castle is, which is Q2's question, not about whether the economics can be pictured
  **[M1997-148]**.
- **VERDICT: IN, narrowly**, with **[M2012-065]**, **[M1998-044]**, **[M2008-033]**, **[M2017-019]**. The retail rows
  (**[M2014-052]**, **[M1996-062]**, **[L1995-008]**) are carried as the strongest contrary rows into Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The castle tests, each with its filing fact **[M1995-038]**:

1. **The attacker with money** **[M2011-015]**, **[M2012-106]**. Walmart is in nearly every town Tractor Supply serves and has
   the money; Amazon and Chewy have the delivery. What the filings show is the regulator's view of the local market: to buy
   Orscheln Farm and Home (166 stores, $397.7M cash), "the FTC required the Company to divest of 85 stores" to two private
   farm chains (FY2022 10-K, Note 3, `0000916365-23-000045`). The antitrust authority found that in half of Orscheln's
   towns the two farm chains were each other's competition, which says the general merchants were not treated as the
   substitute. And no listed farm-and-ranch chain exists to attack it: a sweep of the SEC ticker list for farm, rural,
   ranch, feed, co-op, cooperative, Bomgaars, Orscheln and Atwood found **no instance** of a listed farm-store retailer; the
   10-K names its rivals as "independently owned retail farm and ranch stores, numerous privately-held regional farm store
   chains and farm cooperatives" alongside general, home-center, pet and online retailers (Item 1, Competition). Since 2020
   the chain has added about 500 stores and closed none under the Tractor Supply banner (10-K FY2025 MD&A store tables).
2. **Pricing power and the agony before a rise** **[M2005-020]**, **[M2000-031]**. Gross margin rose from 34.3% (2016, 2017)
   to 36.4% (2025) while transactions grew, which is the opposite of the prayer session over the decade. But in 2026 the
   company reports "incremental investments to strengthen the Company's price-value position" and an everyday-low-price
   policy "complemented by limited and strategically planned promotions" (10-Q Q2 MD&A; 10-K Item 1). Ticket was +0.2% in
   Q2 2026. The power the decade showed is being spent, not used, this year.
3. **Unit volume and share of mind** **[M1999-054]**, **[M2000-030]**. The customers gained in 2020 and 2021 (transactions
   +10.9%, +7.1%) were largely kept (−0.6%, −0.4%, +0.8%, +1.4% after), and FY2025 transactions rose while both home
   centers' fell (row below). The first half of 2026 broke that: −1.4%. Management names "unusually adverse conditions in
   May" and "discrete headwinds"; whether it is weather or the castle is exactly what L1995-022 asks, and the answer will
   not be in the filings until 2027 **[L1995-022]**. Neighbor's Club membership is not disclosed in any filing read; the
   loyalty liability rose from $17.9M to $24.3M in 2025 (10-K Note 1), the only filed trace of it.
4. **The low-cost position** **[L2007-004]**, **[M2004-091]**. Tractor Supply is not the low-cost operator: its operating
   costs run 27% of sales (SG&A including D&A, FY2025) against Walmart's lower-margin model; its protection is the
   assortment, the location and the bulk, not the cost. In the part of the basket that is a commodity and ships cheaply
   (pet food), the low-cost and low-friction seller wins **[M1997-010]**, **[M2024-013]**, and that is where the company is
   losing (5 below).
5. **The brand in the customer's mind; would the customer still choose it over the low bid?** **[M2023-073]**,
   **[M2017-009]**. The store is the brand; 30% of sales are owned or exclusive brands. For a 50-pound feed bag, a roll of
   fence or a trailer, the nearest farm store is the practical choice; for a bag of dog food it is one of many.
6. **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Narrowing at one wall, on the evidence: companion animal "continued
   to perform below the Company average" for at least two quarters (10-Q Q1 and Q2 2026); the Petsense pet-specialty chain,
   bought in 2016, is being cut by about 75 of 209 stores with its goodwill written off ($22.2M) (10-Q Note 11); and the
   online pet seller grew its active customers 4.0% to 21.3 million and net sales 6.2% in its FY2025 (Chewy 10-K below).
   The company's answer is to buy more of the pet business (Allivet, $135.0M, December 2024; VIP Petcare, $133.8M, May
   2026). Holding at the farm walls: livestock, equine and agriculture rose from 26% to 27% of sales in 2025 and to 32% in
   Q2 2026 (10-K and 10-Q category tables); management claims share gains (8-K `0000916365-26-000005`), which the filings
   do not let me verify.
7. **What could destroy, modify or reduce it** **[M2000-014]**: delivery that makes a heavy rural basket cheap to ship
   to the farm; a general merchant that adds the farm assortment in small towns; or a slow drift of the rural hobby farmer
   to online for everything but feed. None is shown in the filings; the third is the slow change that "can lull you to
   sleep" **[M2014-038]**.
8. **Ask the competitors** **[M1999-130]**, **[M2017-091]**: no filing read names Tractor Supply (a search of the five
   peer 10-Ks for "tractor supply" found no instance); scuttlebutt is not on the public record.

**The competitor row** (latest fiscal year, each company's own 10-K XBRL and MD&A; margins and returns my arithmetic on the
filed lines; script `peers/facts.py`, output `peers/peer_table.txt`):

| Company | FY end | Revenue $M | Gross margin | Operating margin | Net income / total assets | (OCF − SBC − capex) / revenue | Comparable sales, split | Accession |
|---|---|---|---|---|---|---|---|---|
| **Tractor Supply** | 2025-12-27 | 15,524 | 36.4% | 9.5% | 10.0% | 4.4% | +1.2%: transactions +1.4%, ticket −0.2% | 0000916365-26-000014 |
| Home Depot | 2026-02-01 | 164,683 | 33.3% | 12.7% | 13.5% | 7.4% | +0.3%: transactions −1.0%, ticket +1.4% | 0001628280-26-019436 |
| Lowe's | 2026-01-30 | 86,286 | 33.5% | 11.8% | 12.3% | 8.6% | +0.2%: transactions −2.8%, ticket +3.0% | 0000060667-26-000029 |
| Walmart | 2026-01-31 | 713,163 | not tagged | 4.2% | 7.7% | 1.6% | Walmart U.S. +4.3%, "driven by growth in average ticket and transactions" | 0000104169-26-000055 |
| Chewy (pet, online) | 2026-02-01 | 12,602 | 29.8% | 2.0% | 6.6% | 2.1% | no stores; active customers +4.0% to 21.327M, net sales per active customer +2.2% | 0001766502-26-000034 |
| Petco (pet, stores) | 2026-01-31 | 5,961 | 38.7% | 2.0% | 0.2% | 2.6% | −1.6% | 0001193125-26-106114 |

What the row says: Tractor Supply's margins sit between the home centers' and the mass and pet sellers'; its gross
margin is the highest of the store chains bar Petco; its operating margin is three points under the home centers', and
its owner cash per dollar of sales is about half of theirs, because it is spending to grow. It out-traded both home
centers on transactions in their last fiscal year and lost to Walmart U.S. The two pet sellers earn 2% operating margins:
the pet aisle is a hard place to make money for anyone, which is the wall that is narrowing.

**Reading.** The castle is standing, and the evidence says why: local scale in small towns, an assortment of heavy needs-based
goods the general merchants do not carry in depth and that do not ship cheaply, and an antitrust finding that its closest
competitors are other farm stores. Ten years of 9% to 10% operating margins with rising gross margins and transaction
counts held after the pandemic are the record of a castle the attacker has not taken **[M2011-015]**. It is not "a moat
that’s tenuous in any way" **[M2000-019]** at the farm walls. At the pet wall it is being crossed, on the filings, and
the 2026 price investment and traffic loss may be the start of a wider breach or a bad May. A castle shown to be filling in
closes OUT **[M2011-015]**; this one is shown narrowing on one wall, not open. The narrowing, the retail rows ("In
retailing, to coast is to fail." **[L1995-008]**) and the 2026 traffic are carried to Q7, where they enter "the degree of certainty" **[M1999-104]**.
- **VERDICT: IN**, with **[M1995-038]**, **[M2011-015]**, **[M2000-019]**, **[L2005-010]**; narrowly, and only for the farm
  and rural walls. The companion-animal wall is recorded as narrowing **[M2001-070]**, **[M2018-042]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital needed** **[M2010-090]**, **[M2011-060]**. Tangible capital (equity + debt − cash − goodwill and
  intangibles) at 2025-12-27: $2,581M + $1,765M − $194M − $399M = **$3,753M**; pre-tax operating income $1,467M on it is
  **39%**. With the operating-lease liabilities ($4,142M) counted as capital and an interest share of rent added back at
  the filed weighted-average lease rate of 4.5% (10-K Note 6), the return is about **21%** pre-tax. Either way a high
  return on the capital the business needs; but most of the stores' capital is the landlords', and the lease view is the
  fairer one for a chain that leases 97% of its stores.
- **The incremental return, and its base years** **[M2001-019]**, **[L2005-003]**. From 2019 (pre-pandemic) to 2025:
  operating income +$724M on +$2,028M of tangible capital (36%), +$3,892M with leases (about 21%). From 2021 to 2025:
  operating income **+$160M** on **+$1,698M** of tangible capital (**9.4%**), **+$2,943M** with leases (about **7%**).
  (Lease rate applied to 2019 and 2021 is the 2025 filed rate, my approximation.) The pandemic lifted the base; since then
  the chain has added about 400 stores, a distribution centre, Allivet and remodels, and earned almost nothing more. That
  is the pattern the rows warn of: "we’re not earning a higher rate of return on capital than we were when we started. We
  just put way more capital into the business" **[M2023-081]**.
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**, **[L2000-035]**. FY2025 capital spending
  of $894.8M by the filed categories (10-K MD&A, Investing Activities): new, relocated and not-yet-opened stores $376.0M;
  existing stores $223.9M; information technology $158.1M; distribution centres $127.8M (mainly the new Nampa DC); corporate
  $9.0M. **Maintenance judgment, stated as a guess** **[M2000-144]**: existing stores, IT and corporate, about **$390M**, plus
  part of the distribution spend; against depreciation of **$494M**. So maintenance sits at or a little under depreciation,
  and "Every year we spend amounts equal to our depreciation charge simply to stay in the same economic place" **[L2000-035]**
  is the right default. Growth spending is then about $400M to $500M a year.
- **The cost of a new store against what it brings** (my arithmetic on filed figures, an estimate): new-store capital about
  $3.5M per opening ($376.0M over 99 openings and 7 relocations) before sale-leaseback proceeds, plus about $1.2M of
  inventory per store ($3,084M over 2,602 stores) and $0.18M of pre-opening cost ($17.8M over 99, 10-K Note 1). Average
  sales per store about $6.1M; at a 9.5% operating margin that is about $0.58M pre-tax on about $4.9M, about 12%, on a
  mature store, and rent is already inside the margin. A satisfactory rate, not a See's rate **[M1998-081]**.
- **The sale-leaseback.** "During fiscal 2025, the Company completed its strategically planned sale-leaseback of 41
  Tractor Supply store locations, resulting in proceeds of $252.6 million and a gain of $91.7 million" (10-K Note 6). The
  company builds stores and sells them to landlords; the proceeds recover capital and convert it into rent. The owner cash
  above deducts all capex and does not credit the proceeds.
- **WEIGHS AGAINST, narrowly.** The core returns are high **[L2009-012]**, **[M1998-081]** (the second-best business, a good
  rate on added capital), but since 2021 the added capital has earned about 7% to 9% pre-tax, and owner cash runs at half of
  reported earnings: in this model the owner earns more only by putting more in **[M2023-081]**, **[M2003-122]**.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them, before the income account** **[M2025-032]** (`tools/run.py` table, first-filed
  XBRL; filed statements read for FY2019, FY2021, FY2022, FY2025 and the 2026 quarters):

  | year-end | assets | liabilities | equity | cash | inventory | goodwill + intangibles | long-term debt | retained earnings |
  |---|---|---|---|---|---|---|---|---|
  | 2016 | 2,675 | 1,222 | 1,453 | 54 | 1,370 | 94 | 264 | 2,540 |
  | 2019 | 5,289 | 3,722 | 1,567 | 84 | 1,603 | 93 (124 filed) | 366 | 3,613 |
  | 2021 | 7,767 | 5,765 | 2,003 | 878 | 2,191 | 55 | 986 | 4,945 |
  | 2025 | 10,934 | 8,352 | 2,581 | 194 | 3,084 | 399 | 1,765 | 7,519 |
  | 2026-06-27 (10-Q) | 12,162 | 9,530 | 2,632 | 232 | 3,518 | 506 | 2,154 | 7,792 |

  What moved and why. **Equity barely moved in ten years** ($1.45B to $2.58B) while retained earnings rose by $5.0B:
  treasury stock reached $6.39B at 2025-12-27 (10-K balance sheet). The owners' capital was paid back out and the return on
  equity is therefore partly manufactured by shrinking the base **[M1998-017]**; Q3 reads returns on tangible capital for
  that reason. **Debt rose about eightfold** ($264M to $2,170M of borrowings at 2026-06-27, plus $500M of notes in August
  2026 to repay the revolver), while equity stayed flat. **Lease liabilities** arrived on the balance sheet in 2019 under the
  new standard ($2,278M) and have grown to $4,142M (2025), with $293.7M more signed and not commenced (10-K Note 6); they are
  the largest liability and the real fixed charge: rent of $675.0M in 2025 (10-K segment note). **Inventory against sales:**
  over the decade, in line ($1,370M on $6.78B of sales in 2016, 20%; $3,084M on $15.52B in 2025, 20%); in 2026, **out of
  line**, +13.9% year on year at June against first-half sales +2.9% **[M1995-064]**, with accounts payable funding part
  of it ($1,760M against $1,519M). **Goodwill** stayed small: acquisitions have been modest and paid in cash, and the Petsense
  goodwill is now gone. **Cash** is kept thin except in 2020 and 2021. What the figures cannot say: whether the 2026
  inventory is seasonal stock left by a weak May (a markdown in the second half) or stock for new stores and the Nampa DC.
- **The real costs** **[L2021-003]**, **[L2015-004]**. Depreciation $494M is a real cost and roughly the maintenance level (Q3).
  Stock pay $57M is expensed (options included; 10-K cash flow). The Petsense charges ($71.7M) and VIP Petcare deal costs
  ($9.5M) of 2026 are real costs of pet decisions and stay in. Two items flatter the reported figures: **sale-leaseback
  gains of $91.7M (2025) and $62.2M (2024) are booked inside SG&A** (10-K Note 6), 6% and 4% of operating income, recurring
  by design ("We plan to continue to leverage our sale-leaseback program", 10-K Liquidity); management calls it "a modest
  benefit" (10-K MD&A). And the 2025 cash flow was helped by deferred taxes of $61.3M from the 2025 tax act (10-K MD&A) and
  by the purchase of transferable tax credits ($168.9M paid in 2025, 10-K cash-flow note), which lower taxes for real.
  Owner cash above starts from operating cash flow, which excludes the sale-leaseback gains.
- **EBITDA in the filer's own mouth:** no instance in the releases read; the credit agreements use "consolidated EBITDAR"
  for the covenant only (10-K Note 5) **[M2002-026]**.
- **The tells.** Adjusted earnings appear for the first time in the run's window, in the Q2 2026 release ("Adjusted
  Diluted EPS of $0.81"), to strip the Petsense and VIP Petcare charges **[L2016-006]**; the GAAP figure is printed beside
  it. Inventory out of line with sales in 2026 **[M1995-064]**. The make-the-numbers habit is **not shown**: the CEO's 2025
  bonus paid 80.8% of target on 95% of target net income (DEF 14A), and 2026 guidance was cut **[L2002-041]**. Under the
  two-tell CONVENTION the STOP needs the habit plus a second tell; the habit is absent, so no suspicion.
- **Confusion?** No. The statements are plain, the categories of capital spending are disclosed, the restructuring is
  itemised **[M1994-018]**.
- **VERDICT on confusion: IN. WEIGHS AGAINST, mildly**, with **[M1995-064]**, **[L2016-006]**, **[M1998-017]**: the
  recurring sale-leaseback gains inside operating income, the 2026 inventory build and a return on equity made by buybacks
  and debt. **The recast earnings for Q7** are owner cash after every real cost, all capex deducted: five-year mean **$557M**;
  the depreciation variant $935M shown beside it.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who:** Harry A. ("Hal") Lawton III, President and CEO since January 2020, previously President of Macy's (2017 to 2019)
  (DEF 14A). Not a founder. Owns 384,999 shares directly (about $11.9M at $30.80) plus 1,164,685 options exercisable within
  60 days; all directors and officers together own less than 1% (DEF 14A ownership table). Independent chair, Edna Morris.
- **The two yardsticks** **[M1994-008]**, **[M1994-009]**. Running the business against the hand dealt: he took over a sound
  chain, kept most of the pandemic customers, accelerated store openings (80 in 2024, 99 in 2025, about 100 planned for
  2026), bought and converted Orscheln, and out-traded both home centers on transactions in 2025. Against: operating margin
  down from 10.3% (2021) to 9.5% (2025) and 8.5% to 8.8% adjusted guidance for 2026; the pet bets (Allivet, VIP Petcare) are
  his, and Petsense (bought before him) is being cut under him. Treating owners: see Q6.
- **Integrity, the tells** **[M2007-082]**, **[L2024-003]**, **[M2010-081]**. The Q2 2026 release says "While we are not
  satisfied with our performance", cut guidance, and withdrew the long-term framework rather than defend it: bad news told
  promptly. The Petsense problem was acted on with a restructuring and an impairment within the quarter it was reassessed
  **[M2017-005]**. Against: the same release leads with "The Tractor Supply business model demonstrated its strength and
  durability" in a quarter of falling traffic, and attributes the miss to "unusually adverse conditions in May". That is
  salesmanship, not a sign of dishonesty. No instance found, in the filings read, of figures obscured, reserves moved, or
  shares issued in quantity (shares outstanding fell from 532.2M diluted in 2025 to 521.8M at June 2026).
- **Love of the business or the money** **[M2000-098]**. Not knowable from the filings for a hired chief executive; the
  pay below is the only evidence, and it is weighed at Q6.
- **VERDICT on integrity: IN** (no doubt found; **[M2015-047]**, **[M2013-088]** applied on doubt and none arose).
  **Ability: WEIGHS FOR, narrowly**, with **[M1994-008]**: an able operator of a good chain whose capital decisions since
  2021 (Q3) and pet bets have not added earning power. Retail needs management that stays smart **[M1995-040]**,
  **[L1995-006]**; this one has not coasted.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[R1995-009]**, **[M1998-110]**. FY2021 to FY2025: net income $5,390M; buybacks $3,015M and
  dividends $2,059M paid (XBRL of the filed cash-flow statements), $5,074M in all. Almost nothing was retained; the growth
  in stores, the DC and the acquisitions was funded by debt (+$779M) and by landlords (lease liabilities +$1,246M). The
  market leg: about $316M retained against a market value that went from about $25.8B (113.125M shares at 2021-12-25,
  FY2021 10-K, times five for the 2024 split, at the aggregator's split-adjusted close of $45.65 on 2021-12-23, flagged)
  to $16.0B today. On so small a retention the test says little, and what it says is negative. The forward
  question **[M2010-097]**, "Can you keep using all of the capital you generate, effectively", is answered by Q3: the
  added capital since 2021 earned about 7% to 9% pre-tax.
- **Buybacks** **[L1999-023]**, **[L2016-002]**, **[L2011-003]**. The programme names no price: "The timing and amount of any
  shares repurchased under the program will depend on a variety of factors, including price" (10-K Item 7), with a
  fixed-sum plan, "Our projected share repurchases for fiscal 2026 are currently estimated to be in a range of
  approximately $375.0 million to $450.0 million" (10-K Item 7). Average prices paid: $43.71 (2023), $53.02 (2024),
  $54.53 (2025), $40.86 (first half 2026), $34.92 (Q2 2026) (10-K Note 8; 10-Q Note 8). They were funded in 2026 with
  borrowing while operating cash fell (contrary evidence 7): "available funds -- cash plus sensible borrowing capacity
  -- beyond the near-term needs of the business" **[L1999-023]** is a question the board did not visibly ask. The
  CONVENTION reads the prices paid against the bottom of the Q7 range; that check is made at Q7 below and recorded back
  here: **every price paid since 2023 is above the bottom ($19.00); the 2024 and 2025 prices are above the top
  ($42.65).** Not rescued.
- **Issuance and deals** **[M1995-001]**, **[L2009-019]**, **[L2014-015]**. All deals for cash: Orscheln $397.7M less $69.4M of
  forced divestitures and a $10M property sale; Allivet $135.0M; VIP Petcare $133.8M. No stock deal; no serial issuance
  (shares fell). Value given against value got: Petsense, bought in 2016, has been written down to zero goodwill and a
  third of its stores closed; the two pet acquisitions are too new to grade.
- **Part B, pay** **[M2003-019]**, **[L1994-019]**, **[M1995-010]**, **[M2016-083]**. CEO 2025 total $32.3M in the summary table
  (salary $1.34M; stock awards $26.9M, of which a one-time "Retention Equity Award" with "a targeted grant value of $20
  million"; options $2.3M; bonus $1.6M) (DEF 14A). The annual bonus pays on net income, net sales and three strategic
  initiatives; the regular PSUs on "growth in net sales and growth in earnings per diluted share", and "The earnings per
  diluted share target also includes an assumption of share repurchase activity" (DEF 14A). No charge for capital
  anywhere in the plan: a batting average "that does not include a cost of capital is a phony batting average"
  **[M1995-010]**, and per-share earnings can be grown by buying shares with borrowed money **[M1998-017]**. The retention
  PSUs pay on relative total shareholder return against the S&P 500 constituents over 2026 to 2030; relative TSR removes
  part of the market's ride **[M2000-062]** but pays for a price, not a business result. The board is independent with a
  separate chair; 13.9% of votes cast went against say-on-pay in May 2026 (8-K `0000916365-26-000033`: 61.1M against,
  376.3M for). The person matters more than the plan **[M2007-006]**.
- **Part A WEIGHS AGAINST**: little retained, buybacks at prices above value with borrowed money and no stated price,
  growth capital earning less each year **[L2016-002]**, **[L1999-023]**, **[M2023-081]**. **Part B WEIGHS AGAINST**: pay on
  sales and buyback-assisted EPS with no capital charge, and a $20M retention grant in the year before the guidance was
  cut **[M1995-010]**, **[M2016-083]**.

## Q7 — WHAT IS IT WORTH? STOP.
Reached: Q1 IN, Q2 IN, Q3 weighed, Q4 IN and weighed, Q5 IN and weighed, Q6 weighed.

- **How much, how sure, how soon, at the long government rate** **[L2000-021]**, **[M1996-025]**. The CONVENTION range (Part
  VI): five-year mean owner cash after every real cost, $557.4M (FY2021 to FY2025, all capex deducted) **[L2021-003]**,
  **[L2005-003]**; carried ten years at the growth shown, then at zero nominal growth, discounted at 5.63%. Growth shown on
  the aggregate owner cash, endpoint to endpoint: $463M (2021) to $683M (2025), **10.2% a year**. The base year is low
  (2021's capex doubled from $294M to $628M), and over the same years operating income grew 2.9% a year, so the shown rate
  flatters **[L2005-003]**. The rate also runs past the discount rate; the CONVENTION caps growth by Q3's arithmetic **[M1997-095]**,
  **[M1999-067]**, and the result is shown both ways. Script `q7.py`.

  | Case | Owner cash base | Growth, years 1 to 10 | Value $M | Per share (521.04M) |
  |---|---|---|---|---|
  | No growth (bottom) | 557.4 | 0% | 9,901 | **$19.00** |
  | Shown growth (top) | 557.4 | 10.2% | 22,223 | **$42.65** |
  | Shown growth capped at the discount rate | 557.4 | 5.63% | 15,475 | $29.70 |
  | Depreciation variant, no growth | 934.8 | 0% | 16,604 | $31.87 |
  | Depreciation variant, shown growth | 934.8 | 7.2% | 29,377 | $56.38 |

  Owner cash is after interest, so the equity value is read directly; the debt is carried as rolled, which Q9 would test.
- **How sure** **[M1999-104]**. Sure of the level within a band (five years of owner cash between $463M and $683M, of
  operating income between $1.31B and $1.48B); unsure of the growth, for the reasons in Q2 and Q3: a pet wall narrowing,
  traffic falling in 2026, and added capital earning less each year. The range is **2.24 to one**, under the
  CONVENTION's three-to-one, so it is not TOO HARD on width **[L2000-025]**, **[M2007-022]**.
- **The floor (CONVENTION), about ten percent pre-tax** **[M1994-004]**, **[L2002-020]**, **[M2003-149]**. The expected return at
  $30.80 on the owner-cash stream: **3.5%** with no growth and **7.5%** with the shown growth carried ten years; on the
  depreciation variant 5.8% and 9.6%. These are after-tax cash yields set against a pre-tax floor, which favours the
  name; it still does not clear the floor on any case. The value at a 10% expectancy on the shown-growth stream is $21.71
  a share ($29.46 on the depreciation variant).
- **The price against the range.** $30.80 sits **inside** the range, about 62% above its bottom; on the capped reading it is
  above the top; on the depreciation variant it is just below the bottom. In every reading it is a case that needs a
  pencil, and "if you have to actually do it on — with pencil and paper, it’s too close to think about." **[M1996-084]**;
  "So if you really need a calculator [...] forget about the whole exercise. Just go onto something that shouts at you."
  **[M2009-005]**. The buy is made only at "a reasonable price in relation to the bottom boundary of our estimate"
  **[L2013-012]**, and the price is not near that.
- **The price that would need no pencil** (my arithmetic, not a rule): the no-growth case alone yields the ten percent floor at
  about **$10.70** a share on the all-capex cash ($17.94 on the depreciation variant). Somewhere around $11, a third of
  today's quote and well under the $19.00 bottom, the case would scream; nothing between $19 and $43 does.
- **Q6's buyback check, recorded back:** the prices paid ($34.92 to $54.53 since 2023) all sit above the $19.00 bottom.
- **Value range:** **$19.00 to $42.65 a share against $30.80.** **Closes:** OUT. The range is narrower than three to one, the
  price sits inside it (not a screamer), and the expectancy at the price is under the floor: "there’s just a point at which
  we drop out of the game." **[M2003-149]**.
- **VERDICT: OUT**, with **[M2003-149]**, **[M2009-005]**, **[M1996-084]**, **[L2013-012]**, **[M2006-013]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED** (the run closed at Q7).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED** (the run closed at Q7). The facts are recorded under COMPUTATION below.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED** (the run closed at Q7).

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED**; not asked by the operator.

---
## COMPUTATION — NOT A CLEARANCE
Facts gathered for the questions after the closing STOP. They carry no entry language and change nothing above.
- **The bond (Q8's first filter) at today's price** **[M1997-089]**: owner-cash yield 3.5% (all capex) to 5.8% (depreciation
  variant) against the 30-year Treasury at 5.63%. On the conservative measure the bond yields more, today, with no
  growth needed.
- **The debt and exposures (Q9's facts)** **[M1995-104]**, **[L2014-023]**, **[L2012-002]**. Borrowings $2,170M at 2026-06-27
  (5.25% notes $750M; 1.75% notes $650M; 3.70% notes $150M; revolver $620M), then $500M of 5.200% notes due 2032 sold
  2026-08-25 to repay revolver borrowings. Operating-lease liabilities $4,142M (2025) plus $293.7M signed and not
  commenced; rent $675M a year. Coverage, pre-tax earnings over interest: about $1,398M over $70M of interest in 2025, about
  20 times; with rent as a fixed charge, (operating income + rent) over (interest + rent) is about 2.9 times (my arithmetic
  on 10-K figures). Ratings Baa1 and BBB, stable, at 2026-02-19 (10-K Item 7). The new revolver ($1.30B, unsecured, five
  years) carries a leverage covenant of "not greater than 4.00 to 1.00" (8-K `0000916365-26-000039`). Change-of-control
  puts at 101% on the notes. No collateral calls, no deposits, no cash-out features found. Self-insurance reserves for
  workers' compensation $89.7M and general liability $63.5M with stop-loss cover (10-K Note 1). For a whole business
  offered, "little or no debt" **[R1997-001]** would be the question; the debt itself is serviceable, the leases are the
  weight.
- **Twelve-month owner cash to June 2026** (a check on the five-year base, not an input): first-half operating cash flow
  fell to $653M from $1,003M, mainly from the timing of tax-credit purchases, and capex rose to $436M from $352M (10-Q cash
  flow); the trailing figure is distorted by that timing and is not used.

---
## THE BOX
**OUT**, decided at **Q7**. Value as a range: about $557M a year of owner cash after every real cost (five-year mean), sure
in level and unsure in growth, worth **$19.00 to $42.65 a share** at the 30-year Treasury rate of 5.63%, against a price of
**$30.80**. The price sits inside the range, not so far below it that it needs no pencil, and the expected return at the
price (3.5% to 7.5% on owner cash) is under the ten percent floor. Q8 to Q10 NOT REACHED. Not TOO HARD: Q1 and Q2 were
answered IN on the filings, and the range is narrower than three to one. Q11 (has the business changed, or only its price)
belongs to the holding review, not to a purchase run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template was copied before `tools/run.py` or any EDGAR request).
      [ ] **Committed after each question: NO.** The dispatching instruction for this run forbade commits; the file was
      written whole after the reading, not question by question. Declared, not ticked.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`; no E-ids); every filing fact has its
      accession; derived figures are arithmetic on filed figures, shown, with scripts in the research folder.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance (Q8 to Q10 NOT
      REACHED; the later facts sit under COMPUTATION with no entry language).
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority (US Treasury par curve); the aggregator quote flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (eight items under the foundations, before the
      verdicts).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; the anchor is today.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its v4 floor, ids and "points over the sovereign"
      lines were ignored.
- [x] `python tools/check_framework.py` **PASS** on 2026-10-05 after this file was written (TEST RUNS: phantom ids in 0
      files; v5 ledger verbatim 4279/4279). No commit made, at the dispatcher's instruction.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **The growth cap in the Q7 range CONVENTION is ambiguous for a ten-year term.** It says the shown growth is
"capped by the growth arithmetic of Q3: no rate that runs past the discount rate", citing M1997-095, whose point is that a
rate above the discount rate *carried forever* gives infinity; carried ten years and then flat, a 10.2% rate gives a finite
value. I could not tell whether 10.2% must be cut to 5.63%; I showed both ($42.65 and $29.70 tops), and the box is OUT
either way, but for a closer name the cap would decide it. (2) **"The growth shown" does not say endpoint or fit**, and the
endpoint is hostage to the base year the rows warn about (L2005-003): TSCO's owner cash rose 10.2% a year endpoint to
endpoint while operating income rose 2.9%, because 2021's capex doubled. (3) **Sale-leaseback proceeds are not
addressed.** The CONVENTION deducts "all capital spending"; a retailer that builds stores and sells them to landlords
recovers part of that spending as proceeds that are really lease financing. Crediting the proceeds would move the
five-year base from $557M to $655M and the shown growth to 19.3%, a range of $22.32 to $101.48 that is **4.55 to one,
TOO HARD on width**; so the treatment of one line can move the box between OUT and TOO HARD. I followed the CONVENTION's
words (all capex, proceeds not credited, since they create rent that already sits in operating cash flow) and record the
sensitivity. (4) **The template's position note conflicts with a blind dispatch**: it says "check `PORTFOLIO.md`", which the
blind rule forbids; I recorded the conflict and the contamination instead. A smaller point already raised by earlier runs
remains: Q6's buyback CONVENTION needs the bottom of the Q7 range, which the hard sequence computes later; I recorded the
check at Q7 and wrote it back into Q6.
