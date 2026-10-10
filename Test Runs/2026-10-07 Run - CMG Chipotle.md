# Company Run — Chipotle Mexican Grill, Inc. (NYSE: CMG) — 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Dispatched run.** Brief: `Screens/_daily/_dispatch_brief.md` with the dispatcher's slots (run file, working folder
`Test Runs/_research 2026-10-07 CMG/`, lines of evidence, competitors CAVA, SG, MCD, YUM, WING). Lock: `Screens/_daily/_overnight.lock`
was present when this run started (held by the dispatching session; not written or touched by this analyst).

**CONTAMINATION, declared as found (not used):** (1) the session context showed the last five commit subjects of the
repository before any work: a batch fold naming AVGO, BMI, CB and CHD with their boxes and alert prices, and four CB run
commits; and a `git status` listing showing untracked research folders for AYI, BDC, CHD and ARCB. (2) The session context
carried a memory index line describing the queue (counts of gate-clearers, holding reviews owed). None of it concerns
Chipotle; none of it is used. No other Chipotle run file was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $30.90 (close 2026-10-06; `tools/run.py` live quote; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **1,265,418,000** as of 2026-07-24
  (10-Q for the quarter ended 2026-06-30, filed 2026-07-31, accession `0001058090-26-000066`; `python Screens/cover_shares.py CMG`).
  Check against issued less treasury: the 10-Q balance sheet shows 1,267,838 thousand issued at 2026-06-30 and no treasury
  stock (the company retires every repurchased share, Note 7 of the 10-K); the 2.4M gap is the July buying. **The 2024
  split:** the charter amendment raising authorized shares from 230 million to 11.5 billion "in connection with a 50-for-one
  stock split" was approved at the annual meeting of 2024-06-06 (8-K filed 2024-06-07, accession `0001058090-24-000024`),
  49 additional shares per share to holders of record 2024-06-18, trading split-adjusted from 2024-06-26. The 10-K cover
  counts read 27,421,169 (2024-02-02) and 1,355,337,000 (2025-01-31): 27.42M x 50 = 1,371M before a year of buybacks, so
  the post-split count agrees with the split. No 8-K filed after the 10-Q issues shares (8-Ks of 2026-08-05 and 2026-09-14
  read: a salmonella statement and a director's election); the 8-K of 2026-07-29 adds a $1.3 billion repurchase
  authorization, so the count will keep falling.
- **Market cap:** 1,265.418M x $30.90 = **$39,101M**.
- **Net cash at the latest filed date (2026-06-30, 10-Q `0001058090-26-000066`):** cash $228.2M + current investments
  $449.7M + long-term investments $97.1M = $775.0M; borrowings nil (the $500M revolver of 2025-06-24 is undrawn; 8-K
  `0001058090-25-000047`); no finance leases. Restricted cash ($35.6M) left out. Operating lease liabilities $5,419.2M
  (current $317.0M + long-term $5,102.2M) **left out of net debt and said so**, as Q7's basis rule directs; their cash
  cost runs through operating cash flow.
- **Sovereign for the earnings currency (USD):** **5.64%**, US Treasury daily par yield curve, 30-year, 10/06/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-04, `0001058090-26-000009`); 10-Q Q2 2026 (filed
  2026-07-31, `0001058090-26-000066`); proxy DEF 14A (filed 2026-04-28, `0001140361-26-017294`); 8-Ks of 2024-06-07,
  2024-08-13, 2024-08-28, 2025-06-26, 2025-08-26, 2025-09-05, 2025-11-25, 2026-01-12, 2026-07-08, 2026-07-29, 2026-08-05,
  2026-09-14; and the 10-Ks FY2014 to FY2024 for the cycle (accessions in the research folder's `filings.md`).
  **Cross-check:** operating cash flow FY2025 $2,113,926K in the filed cash-flow statement of the 10-K equals the
  `tools/run.py` figure of 2,114 (USD millions).
- `python tools/run.py CMG` arithmetic lines only (its rules and floor ignored, Part VII): OCF − SBC − capex 2023 $1,099M,
  2024 $1,380M, 2025 $1,328M; OCF − SBC − D&A 2023 $1,340M, 2024 $1,638M, 2025 $1,633M; 5-year capex-basis mean $1,043M.
  SBC: 2023 $124.0M, 2024 $131.7M, 2025 $119.5M (cash-flow add-back; total expense incl. capitalized $121.4M in 2025).
  The ten-year table and its reading are under Q4.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own a piece of these 4,186 restaurants "if the
market closed for five years" **[M1997-109]**, and the price of $30.90, down from the 2024 split-adjusted highs the 10-K's
return table shows (the $100 of 2020 was worth $217 at the end of 2024 and $134 at the end of 2025), tells nothing about
value: "it doesn’t tell us anything. It just tells us prices." **[M2006-077]**. No macro view enters ("macro conclusions are
— just never enter into the discussion." **[M2000-094]**), so the 2026 consumer slowdown the 10-Q describes is read only for
what it shows about the business. The analyst's habit that bears hardest here is to look for "what’s wrong in things"
**[M2025-013]**: a popular brand with a famous recovery invites the reader to rest on the recovery story.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the 2015-2016 food-borne illness collapse: comparable
sales fell 14.6% in Q4 2015, 30% in December 2015, over 36% in January 2016 and 20.4% for 2016, with transactions down
14.4% (10-K FY2015 `0001058090-16-000058`; 10-K FY2016 `0001058090-17-000009`); operating margin went from 17.0% (2015)
to 0.9% (2016) and did not regain 2015's level until 2024 (`series.md`). (2) Average restaurant sales fell from $2.532M
(2015-09-30) to $1.868M (2016) and were back above the 2015 figure in nominal dollars only by 2021 ($2.641M). (3) In 2025
comparable sales fell 1.7% with transactions down 2.9%, and average restaurant sales fell 3.4% to $3.104M (10-K FY2025),
after the CEO credited with the recovery left in August 2024. (4) A new salmonella statement on 2026-08-05: jalapeños from a
common lot removed from restaurants (8-K `0001058090-26-000069`), and the 10-Q's own words, "recent U.S. food safety
concerns", among the causes of "low-single-digit headwinds" to comparable sales. (5) Executive turnover: the chief
accounting officer resigned 2025-08-25 with no successor named for ten days; the marketing chief and the general
counsel "transitioned out" on 2026-01-12 (8-Ks `0001058090-25-000067`, `0001058090-26-000002`). (6) Restaurant margin
fell from 26.8% in H1 2025 to 24.3% in H1 2026 (10-Q). (7) Build cost per restaurant rose from about $835,000 (2017) to
about $1.5 million (2025) while average restaurant sales rose from $1.940M to $3.104M (10-Ks FY2017, FY2025): sales per
dollar of build cost fell from about 2.3 to about 2.1.

## THE STANDING RULE
Bought for cash, sized so that a fall of half or more is borne without a forced sale ("you don’t want to put yourself in a
position where you have to sell" **[M2020-007]**), and with no borrowed money ("borrowed money has no place in the
investor's tool kit" **[L2014-005]**), owning this puts the buyer at no risk of ruin. The buyer's financing and sizing are
the operator's and are not seen by this blind run; nothing in the target raises a demand on the holder.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, with the key variables named and judged for predictability first, "because
  that is the first step" **[M1998-044]**. The business is one segment: company-owned restaurants (4,042 at 2025-12-31,
  4,186 at 2026-06-30) selling burritos, bowls, tacos and salads, revenue "derived from sales by our restaurants", no
  franchising in the US and 15 partner-operated restaurants abroad (10-K FY2025 Item 1; 10-Q). The key variables, from
  the filings: (1) restaurant count, growing 304 to 334 a year (2024-2025) with 350 to 370 planned for 2026; (2) average
  restaurant sales, the product of transactions and check; (3) restaurant margin, set by food (29.6% of revenue 2025),
  labor (25.1%), occupancy (5.2%) and other operating costs (14.7%); (4) the cost to build, about $1.5M gross a unit in
  2025; (5) food safety, which the 10-K names first among its risk factors and says may be higher than at "some of our
  competitors because we use fresh, unprocessed produce, handle raw chicken in our restaurants".
- **Foreseeable?** Variables (1), (3) and (4) are read from twelve years of 10-Ks and moved slowly except in 2016. The
  forecast is about customers, not technology: what people eat and where, the kind of analysis the rows call
  "consumer behavior and threats to a business" **[M2023-030]**, **[M2017-019]**. The product has been the same since
  1993. Variable (2) is the uncertain one: the rows warn that "in the food business, you would never get the total
  certainty of dominance" and "People move around in the food business" **[M1997-001]**, and that "it’s easy to sort of
  think you understand retail, and then subsequently find out you don’t" **[M2014-052]**. Variable (5) is not forecastable
  in its timing; its effect once it happened is on the record (2016: comps −20.4%, operating margin 0.9%).
- **Do the past statements tell me the future ones?** **[M2008-033]**: for a single-segment, debt-free, company-owned
  chain, yes in kind: the statements carry the unit count, the four cost lines and the build cost, and a reader can see
  what moved them. What they cannot tell is the size and date of the next disruption to transactions.
- **Would the insiders write it down?** **[M2000-105]**: the filer writes down its restaurant openings for the year and
  its comparable-sales expectation ("about flat" for 2026, 10-K FY2025 MD&A); the industry is not one whose ten-year
  economics its insiders call too hard.
- **Routing.** Not an industry of rapid technological change; not a start-up; not a financial institution; one segment.
  The doubt I hold is about the size of variable (2), the castle's question, which Q2 owns; it is not doubt that the
  economics can be read **[M2002-092]** (the rows ask "a feel for it", not "four decimal places" **[M2015-086]**).
- **VERDICT: IN.** The earning power of a company-owned restaurant chain can be fixed within a range for ten years from
  its unit count, unit sales, four cost lines and build cost, all filed, and the forecast is one of customer behaviour
  **[M2012-065]**, **[M1998-044]**, **[M2023-030]**. Carried to Q2 as a warning, not a STOP: food is a business in which
  customers "move around" **[M1997-001]**, and retail is the arena the speakers name for thinking one understands
  **[M2014-052]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. The competitor rows are in
`Test Runs/_research 2026-10-07 CMG/comp.md`; the filer's twelve-year series in `series.md` in the same folder.
- **1. The key factors.** On the filings: (a) scale in one format, 4,186 company-owned restaurants (no US franchising), the
  largest in its cuisine among the filers read; (b) the unit economics: average restaurant sales $3.104M (2025) against
  about $1.5M gross build cost, and a restaurant margin of 25.4%; (c) a brand built on "Food with Integrity", whose own 10-K
  says it can be eroded by "actual or perceived food safety or food-borne illnesses"; (d) convenience: Chipotlanes in 257 of
  334 openings in 2025 and "around 80%" planned for 2026, digital 36.7% of food and beverage revenue (2025). The rows say
  what kind of factor (d) is in this trade: "a great many of the decisions on fast food, as to where you eat, is simply
  based on which one you see. I mean, convenience is a huge factor." **[M1997-139]**.
- **2. Without the lord.** The test is whether "a business requires a superstar" **[L2007-006]**. The recovery from the 2016
  collapse is associated in the filings with a change of chief executive (Niccol, 2018 to August 2024; 8-K
  `0001058090-24-000035`), and the first full year after he left shows comparable sales −1.7% and transactions −2.9% while
  Taco Bell (+7%), CAVA (+4.0%) and McDonald's US (+2.1%) grew and Sweetgreen (−7.9%) and Wingstop (−3.3%) fell. One year
  cannot separate the lord from the weather. The restaurant economics did not leave with him: restaurant margin 25.4% in 2025
  is within about a point of the 2023-2024 peak, and the business ran at 26 to 27% under its founders before 2015. Weighed,
  not decided: the rows call the really great business one "that doesn’t require good management" **[M1996-037]**, and a
  restaurant chain sits nearer the retailer, of whom the rows say "a retailer must stay smart, day after day" **[L1995-008]**.
- **3. The money test** **[M2011-015]**. Could a rival with money take it? The rivals with money are on the record: CAVA,
  funded through its 2023 offering, grows units in another cuisine and earned a 4.7% operating margin in 2025; Sweetgreen
  has lost money in every year filed (2021-2025); Taco Bell is larger but sells at a lower price point and is mostly
  franchised. No filer read shows a rival taking Chipotle's category. Against: "one competitor is frequently enough to ruin
  a business" **[M2012-108]**, and the nearest thing to that competitor in this history was the company's own kitchens
  (2015-2016).
- **4. Pricing power and the agony** **[M2005-020]**. Through the last inflation the price went up and the customers stayed:
  menu price increases gave an 8.5% benefit in 2021 with transactions +10.3%, 5.2% in 2023 with transactions +5.0%, 2.9% in
  2024 with transactions +5.3% (10-Ks FY2021 and FY2024), and restaurant margin rose from 22.6% (2021) to 26.7% (2024): the
  pass-through of "businesses with strong competitive positions" **[M2005-017]**. The agony shows after it: 2.1% of price in
  2025 with transactions −2.9%, and the filer's own risk factor that "our higher menu prices may cause some guests to shift
  their purchases to other restaurants" (10-K FY2022). Price pushed "too far to the point that they lost market share"
  **[M2001-087]** is a live question here, not a finding.
- **5. Unit volume and share of mind.** Transactions: −14.4% (2016), +7% (2019), +10.3% (2021), +5.0% (2023), +5.3% (2024),
  −2.9% (2025), +1.0% (Q2 2026). Average restaurant sales: $2.532M (September 2015), $1.868M (2016), $2.641M (2021),
  $3.213M (2024), $3.104M (2025).
- **6. The low-cost position.** Not the low-cost producer: food is 29.6% of revenue, the cost of its ingredient standard.
  The castle is the brand and the convenience of the unit, not cost.
- **7. The brand; 8. the low bid.** The decisive evidence is the kind the rows name: "if you see a business take a lot of
  adversity and still do well, that tells you something about the underlying strength of the business" **[M2000-032]**, as
  with the card nobody quit after a scandal **[M2018-073]**. Here the customers did quit: comparable sales −30% in December
  2015, worse than −36% in January 2016, −20.4% for 2016 (10-Ks FY2015, FY2016). They came back, slowly: operating margin
  regained its 2015 level only in 2024, nine years later. The brand survived a test that would have closed most restaurant
  chains, but it failed the salad-oil form of the test, in which nobody quit. Against the brand, the rows' reading of the
  trade: "you would never get the total certainty of dominance [...] People move around in the food business"
  **[M1997-001]**.
- **9. Ask the competitors** **[M1999-130]**: not available from filings; not used.
- **10. Widening or narrowing** **[M2000-075]**. Over the full cycle 2015 to 2024, widened: 1,994 restaurants at the end of
  2015 (1,971 US and 23 abroad, 10-K FY2015) to 3,726 at the end of 2024, margin back to its peak, digital and drive-through
  formats added. Over the last six quarters, narrowing on the evidence: average restaurant sales −3.4% (2025), restaurant
  margin from 26.8% (H1 2025) to 24.3% (H1 2026), while Taco Bell and CAVA grew same-store sales. Six quarters is not a cycle.
- **11. What could destroy, modify or reduce it** **[M2000-014]**: a second food-safety failure (the 10-K: "We may have
  higher risk for food safety incidents than some of our competitors because we use fresh, unprocessed produce, handle raw
  chicken in our restaurants"; a salmonella statement was filed 2026-08-05); a rival in its own cuisine at its own scale
  (none found among filers); labor rules (the wage, scheduling and termination laws named in the risk factors); price past the moat
  **[M2001-087]**.
- **The parts table.** One reportable segment, the US, 97.9% of 2025 revenue ($11,679M of $11,926M, Note 14); Canada,
  Europe and partner-operated restaurants are below the reporting thresholds. No parts reading is needed.
- **The field's returns over the last full cycle** (section C). The company-owned rivals earn little: Sweetgreen lost money
  every year it has filed; CAVA earned a 4.7% operating margin in 2025 on a restaurant-level margin near Chipotle's.
  Chipotle's operating margin ran 17.0% (2015), 0.9% (2016), 7.9% (2019), 16.9% (2024), 16.2% (2025). The franchisors (MCD,
  YUM, WING) earn franchisor returns on a different model **[M1998-164]**. The durable company-owned player in this field
  earns excellent returns over the full cycle outside the outbreak years; this is not section C's case of a standing castle
  that protects only ordinary returns, since here the returns protected are excellent, and a moat is what "protects
  excellent returns on invested capital" **[L2007-004]**; and the change for the better
  after 2016 has been seen through a full cycle (trough 2016, peak 2024), so section C's TOO HARD (WORK) for an uncredited
  change does not apply.
- **VERDICT: IN**, with the weight stated. The castle stands on brand and convenience at a scale no filer in its cuisine
  matches; it fell once, by its own hand, and was rebuilt over a full cycle to its prior returns, while rivals with money
  have not taken its category **[M1995-038]**, **[M2011-015]**, **[M2000-032]**, **[M2005-017]**. It is not a Coca-Cola castle:
  in food, customers "move around" **[M1997-001]**, its customers did quit once, and the last six quarters narrow it. I do
  not read it as a moat "tenuous in any way" **[M2000-019]** (its returns and its survival of the worst event in its history
  are on the record), but it is not one a reader can call permanent; that doubt is carried to Q7 as the width of the range
  and to the margin asked, "the more volatile the business is [...] the larger the margin of safety" **[M1997-080]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, measured on tangible assets **[M2011-060]** (goodwill is $21.9M,
  immaterial). Net tangible operating assets at 2025-12-31 (10-K): property and equipment $2,679M plus receivables, inventory
  and prepaids $326M less payables, accruals, payroll and unearned revenue $885M = **$2,120M**, against operating income of
  $1,936M: about 91% pre-tax. That figure counts the leased real estate as free. With the operating lease assets ($4,463M)
  added to capital and the lease interest put back (5.48% weighted rate x $5,076M of lease liabilities, about $278M; Note 9),
  the return is about $2,214M on $6,583M, **about 34% pre-tax** (computed). The same lease-inclusive measure, computed from
  the filed balance sheets: about 16% (2019), 22% (2021), 33% (2023), 36% (2024). In 2016 operating income was $34.6M on
  about $1.15B of net tangible assets before leases: about 3%. Return on equity (2025: $1,536M on $2,831M, 54%) is not used:
  equity has been shrunk by buybacks, the case in which "you could make return on equity whatever you want" **[M1998-017]**.
- **To stand still.** "Every year we spend amounts equal to our depreciation charge simply to stay in the same economic
  place" **[L2000-035]**. The maintenance guess **[M2000-144]**, **[L1999-024]**: the filer plans $834.1M of capital
  spending for 2026, of which $531.8M is new restaurants (before landlord reimbursements), $266.9M "investments in existing
  restaurants including remodeling and similar improvements, new equipment and hardware, and technology", and the rest
  (about $35M) corporate (10-K FY2025 MD&A). My best guess for maintenance is depreciation, $361.4M in 2025 (about $390M
  annualised from H1 2026), above the filer's own $302M for existing restaurants and corporate, because the depreciation
  includes the units built in 2017 to 2025 whose remodels are still ahead. Maintenance is about 3% of revenue.
- **To grow.** The growth spending is new units: 334 in 2025 at about $1.5M gross, $1.3M net of landlord reimbursements
  (10-K FY2025); 350 to 370 planned for 2026. The build cost has risen from about $835,000 (2017) to about $1.5M (2025), faster
  than average restaurant sales ($1.940M to $3.104M). **New-unit return, computed from company averages because the filer
  files no first-year sales or payback for new units:** $3.1M of sales at a 25% restaurant margin (after rent) is about
  $0.78M a year before tax on $1.3M of net build cost, about 60% pre-tax cash on cash, a payback near two years. New units
  sell below the average in their first year and the 10-K warns that openings "may negatively impact the profitability of
  existing restaurants that are located nearby"; the computed figure is the top of what a new unit earns, not a filed fact.
- **The incremental test** **[M2001-019]**. From 2021 to 2025 lease-inclusive capital rose by about $2.0B and operating income
  before lease interest by about $1.2B: about 61% pre-tax on the added capital, flattered by the recovery of margin from the
  pandemic year. Even halved for that, it is "a very satisfactory rate" on reinvested money, the second-best business of
  **[M1998-081]**, not the first: growth here requires capital (about $1.3M plus a lease per unit), it does not come free.
- **The caps.** The filer states "our long-term goal of 7,000 restaurants in the U.S. and Canada" (10-K FY2025; "in North
  America" in the 10-K FY2024), against 4,042 company-owned at 2025-12-31 (3,938 in the US; the Canada count is not filed)
  *(corrected during the run, before the close: this line quoted the goal as "in the U.S.", a truncated read)*: about 75% more units, at 350 a year about nine years. Unit growth near 8 to 9% a year for
  ten years is therefore the filer's own written ceiling, not a projection of mine. Average restaurant sales growth on top
  of it is not capped by any filing; the decade 2015 to 2025 shows $2.53M to $3.10M, about 2% a year compounded through an
  outbreak and an inflation. "Most of the great businesses generate lots of money. They do not generate lots of
  opportunities" **[M2003-120]**: this one has generated the opportunity for twenty years, but the 7,000 goal says where it ends,
  and growth in owner cash much above unit growth plus a few points of average-sales growth is where "you bump into absurdities"
  **[M1999-067]** once the margin is at its peak, as it is.
- **WEIGHS FOR.** The capital actually needed earns about a third pre-tax with the leases counted and more without them, and
  the added units earn a high return on about $1.3M each, so retained money has been reinvested at "a very satisfactory
  rate" **[M1998-081]**, **[L2009-012]**; against, growth needs capital every year, the build cost is rising faster than unit
  sales, and the filer's own 7,000 goal caps the runway **[M2003-120]**.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** **[M2025-032]** (`tools/run.py` table, first-filed vintages 2016-2025, read
  against the filed statements of the 10-Ks FY2016, FY2019, FY2023 and FY2025 and the 10-Q of 2026-06-30). What moved and why:
  - *Debt:* none in any year. The only facility is a $500M revolver, undrawn throughout (Note 12; 8-K `0001058090-25-000047`).
  - *Leases:* total assets jump from $2,266M (2018) to $5,105M (2019) and liabilities from $824M to $3,422M because the
    lease standard put the restaurant leases on the balance sheet; by 2025 operating lease liabilities are $5,076M against
    property of $2,679M. The real obligation of the business is its rent, $520M paid in 2025 (Note 9), not any borrowing.
  - *Goodwill and intangibles:* goodwill $21.9M in every year; no acquisitions. Equity is not padded by purchased assets.
  - *Cash and investments:* cash plus current and long-term investments about $1,860M (2023), $2,291M (2024), $1,246M (2025),
    $775M (2026-06-30). The pile built through 2024 is being spent on buybacks: $2,425.5M in 2025 and $1,354.9M in H1 2026
    against operating cash flow of $2,113.9M and $1,332.0M.
  - *Equity and retained earnings:* equity $1,402M (2016), $3,656M (2024), $2,831M (2025), $2,200M (2026-06-30). In 2024 the
    company retired $5,194M of treasury stock against retained earnings ($5,189M) and paid-in capital, and since then charges
    repurchases straight to retained earnings, which stood at a deficit of $(67.2)M at 2026-06-30. The fall in equity is the
    buyback, not losses.
  - *Receivables, inventory, prepaids against sales:* receivables $40M (2016) to $156M (2025), 1.0% to 1.3% of revenue
    (delivery-partner and gift-card receivables); inventory $15M to $50M, 0.4% of revenue throughout; prepaids $44M to $120M,
    1.1% to 1.0% of revenue. No account is "building up suspiciously high" against sales **[M1995-064]**.
  - *Taxes:* deferred tax liabilities $46M (2024), $126M (2025), $163M (2026-06-30), and income taxes paid fell to $423M (2025)
    and $83M in H1 2026 (of which $93M bought transferable energy credits): the 2025 federal tax law's accelerated
    deductions defer tax; the filer names "the timing of tax-related payments, including the impacts of H.R.1" as a lift to
    2025 operating cash flow. A timing benefit, not a lasting one: the 2025 and H1 2026 cash flows are flattered by it.
  - What the figures cannot say: the value of the brand, and the probability of the next food-safety event.
- **The real costs.** Depreciation is charged ($361.4M, 2025) and is a fair proxy for maintenance (Q3). Stock pay is
  expensed in GAAP ($121.4M in 2025, about 1% of revenue; $134.6M in 2024 including the retention grants), and the cash
  used to settle withholding on vested awards ($49.5M in 2025, $49.4M in H1 2026) is a further cost of stock pay paid
  through financing; owner cash below deducts stock pay as **[L2021-003]** requires ("all forms of compensation"). Recurring
  "one-time" items: impairment, closure costs and asset disposals $38.4M (2023), $26.9M (2024), $27.5M (2025), $23.6M in H1
  2026; legal contingencies in every year (an accrued liability of $11.4M at 2025 year-end; legal costs moved labor 0.2 points
  in H1 2026); restructuring under "Recipe for Growth" from 2026. All are inside GAAP operating income and are left there
  **[L2016-007]**. No pension. EBITDA: the filer does not feature it in the releases read.
- **The tells.** The press releases (8-K exhibits 99.1 of 2026-02-03 and 2026-07-29, accessions `0001058090-26-000007`,
  `0001058090-26-000063`) put "Adjusted diluted earnings per share" in the highlights beside the GAAP figure, removing
  restaurant and corporate impairments, legal matters "that we expect to exceed typical costs", restructuring, and stock pay
  for the 2024 retention grants (after-tax total $15.4M in Q2 2026, about 4% of net income): a featured adjusted figure
  **[L2016-006]** that removes recurring costs and a form of stock pay **[L2015-003]**. Earnings guidance is given every year
  (comparable sales "about flat" for 2026 in the 10-K; raised to "low single digit" in the July release, headlined
  "CHIPOTLE RAISES FULL YEAR COMPARABLE SALES GUIDANCE"). The rows name the practice: "the scourge of earnings "guidance""
  **[L2019-006]**. Both are recorded as a WEIGHING against and carried to Q5. Against that, the filings explain each cost line
  in plain words with its causes in tenths of a point (10-K MD&A), "in clear terms what’s going on" **[M1994-018]**, a plus.
- **Growth-rate check** **[L2005-003]**: the five-year window 2021-2025 begins in a year the filer itself describes as
  affected by the pandemic ("The COVID-19 pandemic has had and is likely to continue to have a significant impact on our
  business and results of operations", 10-K FY2021), and the decade's base year 2016 is the outbreak trough; neither base
  can carry a growth rate unadjusted. Carried to Q7.
- **VERDICT on the accounts: WEIGHS FOR.** No confusion and no suspicion: no debt, no acquisitions, working-capital accounts
  steady against sales, costs explained line by line **[M1994-018]**, **[M1995-064]**. Weighs against, carried to Q5: the
  featured adjusted EPS **[L2016-006]** and annual guidance **[L2019-006]**. The recast earnings for Q7: operating cash flow
  less stock pay less capital spending (all-spending case) and less depreciation (maintenance case), less the after-tax
  interest on the cash pile for the all-equity basis.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The people.** Chief executive Scott Boatwright (interim from August 2024, chief executive from November 2024; joined May
  2017 from 18 years at Arby's; chief operating officer before) (proxy `0001140361-26-017294`; 8-K `0001058090-24-000035`).
  Chief financial officer Adam Rymer from October 2024. Independent chairman Scott Maw since August 2024 (the chief
  executive and chairman roles were split when the former chairman and chief executive left). The 8-K of 2026-07-08 moved Mr.
  Maw off the audit committee to meet Rule 10A-3 independence requirements, without a reason stated; I did not find one in
  the filings read and record it as an open fact.
- **The two yardsticks** **[M1994-008]**. *Running the business against the hand dealt:* the management in place since 2024
  inherited a business at its peak margin and has produced comparable sales −1.7% (2025) and +1.4% (H1 2026), and a
  restaurant margin down from 26.8% to 24.3% in H1 2026, in a year when Taco Bell and CAVA grew and Sweetgreen and Wingstop
  shrank. As chief operating officer from 2017 he ran the restaurants through the recovery (comparable sales positive every
  year 2017 to 2024). *Treatment of owners:* "read the proxy statements, see [...] how they treat themselves versus how they
  treat the shareholders" **[M1994-009]**: chief executive pay $15.46M (2025) and $17.50M (2024, including an $8.0M
  retention grant and a $3.5M bridge grant); median employee $17,446; ratio 886 to 1 (proxy). Pay fell with results in 2025:
  the company factor of the annual bonus paid 40% because comparable sales (−1.7% against a 2.0% threshold) and restaurant
  cash flow margin were below threshold, and the chief executive's individual factor was set at 90% (proxy). Pay is Q6's
  subject; here it is read for character, and the 2025 bonus cut is a plus.
- **The integrity record, every fact found:**
  1. *The Deferred Prosecution Agreement (April 2020)*: to settle a criminal investigation "into company-wide food safety
     matters that occurred in our restaurants dating back to January 1, 2013", the DOJ filed a two-count misdemeanor
     information "charging Chipotle with adulterating and causing food to be adulterated"; the company paid a fine ($25M
     reserved, 10-K FY2019) and was required to run a compliance program for three years ending April 2023 (10-Ks FY2020-FY2022).
     The FY2023 and later 10-Ks no longer carry it as a risk; the dismissal itself was not found in the filings read. The
     incidents ran through 2018 (Sterling, Virginia, July 2017; Powell, Ohio, August 2018, 10-Ks FY2017-FY2018), after the
     2015 outbreaks and after Mr. Boatwright joined (May 2017) to run restaurant operations. This is a record of failed operations, and
     the company's conduct when it learned of the problem is the test the rows give, "the CEO has to act" **[M2017-005]**:
     it acted (a food safety program, an independent advisory council, a food-safety modifier that can cut every executive's
     bonus by up to 20%, proxy), but the failures recurred twice in the following three years.
  2. *Labor-law matters*: a settled New York City Fair Workweek and Earned Safe and Sick Time complaint (2022) and "several
     audits of our compliance with employment law requirements, which could result in additional liabilities" (10-Ks FY2022-
     FY2024); legal contingencies charged in every year and a labor cost line raised 0.2 points by "costs related to certain
     legal proceedings" in H1 2026 (10-Q). Amounts of the individual settlements were not found in the 10-Ks read.
  3. *Securities claims*: Stradford v. Chipotle (2024) alleges false statements about portion sizes and improper insider
     trading by the former chief executive and the former finance chief; dismissed with leave to amend on 2025-12-18; a
     second amended complaint filed 2026-01-20; a derivative suit stayed behind it (Note 11; 10-Q). Earlier class actions
     over the 2015-2017 food-safety disclosures (Ong; the Sterling class) are named in the 10-K FY2017. Allegations, not
     findings.
  4. *Executive departures*: the chief accounting and administrative officer resigned "effective immediately" on 2025-08-25
     "to pursue a new professional opportunity", with the filer's statement that it was "not the result of any dispute or
     disagreement [...] including with respect to any matters relating to Chipotle’s accounting practices"; a controller was
     made principal accounting officer ten days later (8-Ks `0001058090-25-000067`, `0001058090-25-000070`). The marketing
     chief and the general counsel "transitioned out" on 2026-01-12 with severance-plan benefits (8-K `0001058090-26-000002`).
  5. *Carried from Q4*: a featured adjusted figure **[L2016-006]**, adjusted diluted EPS beside GAAP EPS in every release
     read, removing recurring impairments, outsized legal matters and the retention stock pay; and annual guidance
     **[L2019-006]** on comparable sales: for 2025 "growth in the low to mid-single digit range" (10-K FY2024) against −1.7%
     actual, a miss the proxy states ("fell below expectations"); for 2026 "about flat", raised in July under a headline in
     capitals.
     Not the habit of "consistently" reaching declared targets that makes the rows "downright incredulous" **[L2002-041]**:
     the 2025 targets were missed, said so, and the bonus fell.
  6. *Candour*: the 10-K explains each cost line by its causes in tenths of a point, and the 2015 10-K named the company's
     own "failure to meet those expectations" in the outbreak; the proxy says 2025 "fell below expectations". I did
     not meet the taboo the rows distrust, in which "mistake" or "wrong" were forbidden words **[L2024-003]**; nor did I find a
     full post-mortem.
- **Love of the business.** Not testable from outside for a hired management of a widely held company **[M2007-081]** (the
  rows read rather than meet for marketable stocks). The chief executive owns 289,162 shares (about $8.9M at $30.90) plus
  475,100 exercisable SOSARs, against $15.46M of 2025 pay; the directors other than one early investor (Albert Baldocchi,
  3.2M shares) own little; all directors and officers 0.45% (proxy). Their stake is mostly granted, not bought.
- **VERDICT on integrity: IN.** The record holds a corporate criminal food-safety settlement under the prior management, two
  recurrences after it, labor-law penalties and live securities allegations; it holds no finding of dishonesty by the present
  management in the figures or the filings, the accounts are clear (Q4), and the one habit carried from Q4 (featured adjusted
  EPS and guidance) is small in amount, reconciled in the same release, and was not used to hide a miss: the 2025 miss was
  stated and paid for in the bonus. I have weighed whether these facts leave doubt, "If you’ve got doubts, forget it."
  **[M2013-088]**: the doubt they leave is about the operation (food safety recurs) and about pay, which Q2 and Q6 carry, not
  about whether these people tell the owners the truth **[M2015-047]**. **Ability WEIGHS FOR, weakly**: a long operating record
  in the recovery as chief operating officer, a short and weak record as chief executive in a hard year, and a business whose
  economics, by the rows' own ranking, matter more than its management **[M1996-037]**, **[M1999-104]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[R1995-009]**, **[M1998-110]**. No dividend has ever been paid (10-K Item 5). Over 2021-2025
  net income was $5,850.7M (652.98 + 899.10 + 1,228.74 + 1,534.11 + 1,535.76; 10-Ks FY2022 and FY2025) and buybacks took
  $5,316.0M of cash: about 91% of the earnings went back to sellers of the stock, not into the business. What the business
  kept, it reinvested in units at the returns found in Q3 (about a third pre-tax on lease-inclusive capital), which passes
  the forward question, "Can you keep using all of the capital you generate, effectively, for a very long time?"
  **[M2010-097]**, for the capital the units need. The test that matters here is therefore the buyback.
- **Buybacks** **[L1999-023]**. No programme names a price: each authorization (July 23, September 15 and December 8, 2025;
  June 11, 2026, $1.3B) "may be modified, suspended, or discontinued at any time" and names no ceiling (10-K Item 5; 8-K
  `0001058090-26-000063`), the form **[L2016-002]** finds "puzzling". By the convention (Q6, the buyback with no stated price),
  the purchases are then read against the bottom of the Q7 range: $18.00 a share on the all-equity basis (Q7, central
  construction). Prices paid (split-adjusted): $36.55 (2023, $589.8M), $57.21 (2024, $995.8M), $42.54 (2025, $2,417.7M),
  $34.35 (H1 2026, $1,331.6M; $32.55 in Q2) (10-K Note 7; 10-Q). Every year's average sits above the bottom of the range and
  above its top ($31.52), so the $5.3B spent since 2023 was spent above value on this run's arithmetic; "If you’re
  repurchasing shares above a rationally calculated intrinsic value, you are harming your shareholders" **[M1996-013]**. The
  cash and investments fell from about $2.29B (2024) to $0.78B (2026-06-30) to do it, and the authorizations were topped up
  three times in eleven months after the price fell, the pattern of buying "to "show confidence"" **[L1999-028]** rather than
  at a stated discount. **Weighs against.**
- **Issuance and deals.** No acquisitions; goodwill $21.9M unchanged. No share issuance except stock pay (ESPP 134
  thousand shares in 2025; awards net-settled). Shares outstanding fell from about 1,551M split-adjusted (31.02M at
  2015-01-30) to 1,265M (2026-07-24). No STOP here.
- **Part B, pay tied to what the person controls** **[M2003-019]**, **[L1994-019]**. The annual bonus (proxy) pays on
  comparable sales (40%), restaurant cash flow margin (40%) and "site assessment requests" (20%, "a measure of our inventory
  for new restaurants over the next 18 – 24 months"): the first two are under the managers' control and paid zero in 2025;
  the third rewards a pipeline count with no return attached and paid 200%. The long-term grant is 60% PSUs on three-year
  restaurant cash flow dollars and new restaurant openings, and 40% SOSARs or RSUs: dollars and openings grow with capital
  put in, and no capital charge is made, the "batting average that does not include a cost of capital" **[M1995-010]**; the
  2023-2025 PSUs paid 273% of target on $7.843B of restaurant cash flow and 923 openings. The SOSARs are seven-year
  fixed-price options with no step-up for retained earnings **[L1994-021]**. The 2024 retention grants ($8.0M each to the
  interim chief executive and the president, $7.0M to two others) vest on service alone, pay that pays "no matter what
  happens" **[M1999-018]**. In favour: the bonus fell to 40% of the company factor when the business missed, a food-safety
  modifier can cut it by 20%, clawback and stock-ownership guidelines exist (proxy). *The board:* an independent chairman
  separate from the chief executive since 2024, the arrangement the rows prefer for replacing a mediocre chief executive
  **[L2014-026]**; directors' holdings are small and, but for one early investor, granted rather than bought with savings
  **[L2019-008]**; an independent compensation consultant and a peer group set pay levels (proxy). **Weighs against**, on the
  options, the uncharged growth metrics and the service-only grants; the 2025 bonus cut weighs for.
- **WEIGHS AGAINST.** Part A: the retained money earns well in new units, but nearly all earnings since 2021 went to
  buybacks at prices above this run's whole value range, under programmes with no stated price **[L2016-002]**,
  **[M1996-013]**. Part B: pay rewards growth in dollars and openings with no charge for the capital that buys it, through
  fixed-price options and service-only grants **[M1995-010]**, **[L1994-021]**, **[M1999-018]**; an independent chairman and
  a bonus that fell with results are the credits.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
at the long government rate **[L2000-021]**: 5.64% (Step 0). Arithmetic in `Test Runs/_research 2026-10-07 CMG/q7calc.py`,
output in `q7calc.out` beside it.
- **Owner cash after every real cost** (Q4): operating cash flow (after cash taxes, working capital and rent) less stock
  pay less capital spending; the all-equity basis also removes the after-tax interest earned on the cash pile, since net
  cash is added back separately (Q7, On what the floor is earned). USD millions, all-spending / maintenance-only (spending
  set at depreciation, Q3's guess): 2021 656.9 / 844.7 · 2022 729.9 / 922.3 · 2023 1,051.3 / 1,292.6 · 2024 1,308.2 /
  1,566.8 · 2025 1,271.8 / 1,576.7. **Five-year averages: $1,003.6M all-spending, $1,240.6M maintenance-only**
  (equity-only, interest left in: $1,043.2M and $1,280.2M). No acquisitions (specific (c) does not arise); working capital
  is inside operating cash flow (d); the company's own tax, no conversion; no carryforward shelter (section E does not arise).
  The 2025 cash flow carries a tax-timing benefit (deferred tax +$79.5M) that is left in and said so.
- **The window and the cycle** (specific (a)). The window's first year, 2021, is aberrational on the filer's own words ("The
  COVID-19 pandemic has had and is likely to continue to have a significant impact on our business and results of
  operations", 10-K FY2021). The rows warn that "a base year in which earnings were poor can produce a breathtaking, but
  meaningless, growth rate" **[L2005-003]**: the literal growth 2021 to 2025 is 18.0% a year (all-spending; 16.9%
  maintenance), most of it margin recovered after the pandemic and the outbreak. Specific (a) then asks for the last full
  cycle's average and growth between successive cycles' averages. On the owner-cash series the last full cycle runs peak to
  peak, 2015 to 2024 (trough 2016), and its average is $506.8M, half of what the business earns today, because the
  business doubled inside the cycle; and no earlier full cycle is in the filings read, so growth between cycle averages
  cannot be measured. **CONVENTION of this run** (rationale: specific (a) was written for a business that cycles about a
  level, and gives no workable base for one that grew through a company-specific collapse): the base stays the five-year
  average, which keeps 2021 at its low level and so errs low, and the growth is measured peak to peak, 2015 to 2024, the
  same point in successive cycles: **15.3% a year all-spending** (13.8% maintenance). The literal window is shown beside.
- **The cap** (specific (f), Q3). Both shown rates trace to an absurdity **[M1999-067]**: revenue growing at the filer's own
  unit runway (3,938 US units toward the 7,000 goal, 5.9% a year, with average restaurant sales at their 2015-2025 rate of
  2.1%, together 8.1% a year) reaches about $26.0B in ten years, and owner cash grown at 15.3% would be about $4.2B (16% of
  that revenue), at 18.0% about $5.3B (20%). The highest owner-cash margin in the record is 11.6% all-spending and 13.9%
  maintenance-only (2024), at the peak restaurant margin of 26.7%. Owner cash above the maintenance-only record per dollar
  of sales, while still spending to grow, is not a result the business has ever shown. The growth is cut back to **8.1%**,
  the rate at which owner cash grows at today's margin on the filer's own unit goal and the decade's average-sales growth
  (CONVENTION of this run in its arithmetic; the cap's principle is **[M1999-067]**, and the unit goal is the filer's).
- **The construction** (specific (e)): the central case is maintenance-only owner cash, with growth spending charged
  against the growth it buys. **Bottom:** maintenance-only owner cash, no growth: $1,240.6M / 5.64% = $22.0B, plus net cash
  $775.0M, over 1,265.4M shares = **$18.00**. **Top:** all-spending owner cash growing 8.1% a year for ten years, then no
  growth, no growth spending and maintenance-only cash: **$31.52**. Width 1.75 to one.
- **Beside it, for the record** (all-equity, per share): literal window, all-spending both ends, 18.0%: $14.67 to $58.26
  (3.97 to one); literal growth on construction (e): $18.00 to $68.27 (3.79 to one); peak-to-peak growth uncapped on (e):
  $18.00 to $55.42 (3.08 to one); latest year (2025) as base instead of the average, capped: $22.70 to $39.86.
  Equity-only, capped: $17.94 to $31.96.
- **The price against it.** $30.90 sits inside the central range, near its top. The growth the price implies at the
  sovereign is 7.9% a year for ten years, about the whole of the capped case. Expected return at $30.90 (the discount rate
  at which the case's cash stream is worth the market value less net cash): no growth 3.2%; capped 8.1% growth 5.7%;
  peak-to-peak 15.3% uncapped 8.9%; literal 18.0% uncapped 10.3%. Below the floor of about ten percent in every case but
  the one this run cuts back as absurd, and there only at the floor, not past it **[M2003-149]**.
- **Value range:** **$18.00 to $31.52** a share (all-equity basis, central construction) against **$30.90**. **Closes OUT**:
  the range is narrower than three to one and the price sits inside it, near the top, so the expected return is below the
  floor ("there’s just a point at which we drop out of the game" **[M2003-149]**) and the case is nowhere near one that
  would "scream at you" **[M2009-005]**. Were the cut-back refused, the uncapped ranges run 3.1 to 4.0 to one, wider than
  three to one, and the file would close TOO HARD on width **[L2000-025]**; on no construction does the price clear the
  floor by a margin, so on none is it IN.
- **Fair price (a reporting figure, never a verdict; Part VII):** **$13.02** a share on the all-equity basis (central
  figure): the midpoint of the range, $24.76, corresponds to owner cash growing 5.1% a year on the central construction,
  and that cash stream, after the company's own tax, discounted at the floor of 10% plus net cash of $775.0M, is worth
  $13.02 a share. **Equity-only: $12.84.** Beside them, on the uncapped literal construction, the same figure would be
  $21.23. No cheap price is reported.
- **Q6's buyback test**, run here and recorded there: the bottom of the range is $18.00; every year's average repurchase
  price since 2023 ($36.55, $57.21, $42.54, $34.35) sits above the range's top.
- **VERDICT: OUT** at Q7, by the floor: a narrower-than-three-to-one range with the price inside it near the top
  **[M2003-149]**, **[M2009-005]**, **[L2013-012]**. Q8, Q9, Q10 and Q12 are NOT REACHED.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED: the file closed OUT at Q7. Facts found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED: the file closed OUT at Q7. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED: the file closed OUT at Q7.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED: the file closed OUT at Q7. Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT at Q7, by the floor**: value range **$18.00 to $31.52** a share (all-equity basis, central construction, 1.75 to
one) against **$30.90**, the price inside the range near its top; expected return at the price 3.2% (no growth) to 5.7%
(growth capped at 8.1%). Fair price (reporting figure) **$13.02** all-equity, **$12.84** equity-only. Q1 IN, Q2 IN with
the weight stated, Q3 weighs for, Q4 weighs for on the accounts, Q5 integrity IN and ability weighs for weakly, Q6 weighs
against. Not a TOO HARD; were Q7's growth cut-back refused, the uncapped ranges (3.1 to 4.0 to one) would close TOO HARD on
width, never IN.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Q8 (the bond).** The 30-year Treasury yields 5.64% (2026-10-06). Owner cash at the price, all-equity basis: the
  five-year maintenance-only average $1,240.6M is 3.2% of the enterprise value of $38,326M; the all-spending average
  $1,003.6M is 2.6%; 2025's maintenance-only figure $1,576.7M is 4.1% (`q7calc.out`).
- **Q9 (debt and exposures).** No borrowings at any year-end 2016-2025 or at 2026-06-30; a $500M revolver, undrawn, with
  covenants of total leverage at most 3.0x and fixed-charge coverage at least 1.5x (8-K `0001058090-25-000047`; Note 12).
  Operating lease liabilities $5,419.2M at 2026-06-30, cash rent paid $520.3M in 2025; legally binding leases signed but not
  commenced $834.4M; purchase obligations $1,887M at 2025-12-31 (Note 9; MD&A). Cash and investments $775.0M at 2026-06-30,
  down from about $2.29B at 2024 year-end after buybacks. "Certain key ingredients are purchased from a small number of
  suppliers" (10-K Item 1). One event's size on the record: the 2015 outbreaks took comparable sales down 20.4% for 2016
  and operating income from $763.6M to $34.6M; the company did not borrow through it.
- **Q12 (how the money is made).** Not a named business of the section. Facts for the newspaper test: the 2020 Deferred
  Prosecution Agreement for adulterating food (two misdemeanor counts, fine paid); the 2022 New York City Fair Workweek
  settlement and other employment-law audits (10-Ks FY2020-FY2024); a food-safety modifier in executive bonuses (proxy).
- **Q10.** No position is taken by a blind run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `768687a9`, made after `tools/run.py` and `cover_shares.py` had
      run but after the copy; see the note below); written question by question; committed after each with a pathspec of
      the run file and the research folder only (write-early).
- [x] Dispatched: the brief allowed the per-question commits; the lock `Screens/_daily/_overnight.lock` was present when
      the run began and was not touched by this analyst; the fold is the dispatcher's (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched by me. Seen by accident and
      declared at the top: commit subjects and untracked-folder names in the session context, and a memory index line. The
      acceptance test, which the brief requires, reads every run file (its check 5); I viewed only the tail of its output,
      which names framework files only.
- [x] Every v5 id resolves: `python "Test Runs/_research 2026-10-07 CMG/check_run.py"` reports 119 citations (85 distinct),
      none missing, no E-ids, every quoted fragment standing before an id found in that row. Every filing fact carries its
      document and accession here or in `filings.md` and `comp.md`.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 NOT REACHED; nothing after it is a
      clearance. No figure was reported as a clearance before Q1-Q4 closed IN (operator rules 2 and 3).
- [x] Owner cash after every real cost: operating cash flow less stock pay less capital spending (or depreciation for the
      maintenance case), never a net-income proxy (operator rule 5); the sovereign from the US Treasury; the price an
      aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations, seven items) **[M1997-127]**; facts for later questions under
      AFTER THE STOP. Integrity facts were judged at Q5 (reached), so the box line carries no integrity flag.
- [x] No row dated after the anchor is cited: this is not a point-in-time run (anchor today).
- [x] Only the arithmetic lines of `tools/run.py` were used; its rule text, ids and floor were ignored (Part VII).
- [x] `python tools/check_framework.py` PASS before the closing commit.
- **Declared departures.** (1) `tools/run.py` and `Screens/cover_shares.py` ran a minute before the first commit of the
  copied template; the copy itself was made before any fetch. (2) Two passages were corrected inside this run before its
  close and the corrections are visible: Q3's quotation of the unit goal ("in the U.S." was a truncated read of "in the
  U.S. and Canada", marked in place), and six sentences in Q2, Q4, Q5 and Q7 restructured so that no id stands beside a
  filing quotation or the framework's own wording (found by the brief's check script; the quotations themselves were
  unchanged). (3) Two CONVENTIONS of this run, confessed in Q7: the peak-to-peak growth reading in place of specific (a)'s
  cycle averages, and the cut-back of growth to 8.1% computed from the filer's unit goal and the decade's average-sales
  growth. (4) The new-unit return in Q3 is computed from company averages; the filer files no new-unit sales or payback.
  (5) Competitor data are thin before 2021 for the company-owned rivals (CAVA and Sweetgreen file from their IPOs) and some
  MCD and Taco Bell years were not extracted (`comp.md`, gaps line).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Specific (a), cycles, fails for a grower whose cycle was its own collapse.** The window's first year (2021) is
aberrational on the filer's own words, so (a) sends the base to the last full cycle's average and the growth to successive
cycles' averages. The owner-cash cycle runs peak to peak 2015-2024; its average ($506.8M) is half of today's earning power
because the business doubled inside the cycle, and no earlier full cycle exists in the filings, so the growth step cannot be
run. I kept the five-year base and measured growth peak to peak, confessed as a CONVENTION of this run. (2) **Specific
(f), the cut-back, has no target.** "Any result that traces to an absurdity is cut back" says to cut, not to what. Here the
cut decides the box: capped at 8.1% the range is 1.75 to one and the file closes OUT; uncapped (15.3% or 18.0%) the range
is 3.1 to 4.0 to one and closes TOO HARD on width. Two analysts could split OUT and TOO HARD on this name exactly as Test A'
did before the range convention. I cut to growth at today's margin on the filer's own unit goal; the framework should say
what the cut-back lands on. (3) **Specific (e) is silent on year eleven.** When growth spending is charged against the
growth for ten years and growth then stops, does the cash after year ten return to the maintenance-only figure? I assumed
yes (it raises the top); the text does not say. (4) **The fair price's "midpoint".** Midpoint of the range in dollars, but
the floor must be applied to a cash stream; I mapped the dollar midpoint to the growth rate that produces it on the central
construction and discounted that stream at 10%. A second reading (the midpoint of the two ends' growth rates) would give a
different figure. (5) **All-equity basis for a net-cash company.** The text defines owner cash "before interest" with net
debt added; for a company that earns interest on cash, the after-tax interest income must come out of owner cash or the cash
is counted twice. I removed it; the text does not say so. (6) **Q2 test 9, ask the competitors**, cannot be run from filings
by a blind analyst; recorded as not available. (7) **Section C's "full cycle" for a change for the better** was
satisfied here by one trough-to-peak span; the text does not say whether a company-specific collapse and recovery counts as
the "cycle" the convention means.
