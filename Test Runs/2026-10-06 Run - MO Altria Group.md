# Company Run — Altria Group, Inc. (NYSE: MO) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template to this dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, the holding
reviews, the session-state files, the register and `tools/alerts.json` were not opened, so whether the operator holds MO
is unknown to the analyst. The run is written as for a name not held.

**CONTAMINATION DECLARED.** (1) To find peer runs for form, `Test Runs/` was listed filtered to file names dated
2026-10-05; no MO file appeared in that filtered list and no earlier MO run or research folder was opened (whether one
exists was not checked). One peer run (CAG, 2026-10-05) was read for form only. (2) `tools/run.py` prints v4 material;
only its arithmetic lines are used (Part VII). (3) A text search of `principle_ledger_v5.csv` for "tobacco",
"cigarette" and "smok" returned the rows the speakers gave on tobacco companies; they are v5 rows and are used as such.
(4) The analyst's training memory of Altria up to mid-2025 (Marlboro, the JUUL and NJOY purchases, the ABI stake) is a
prior; every fact used below is from a filing with its accession.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $67.88 (2026-10-05, the live quote printed by `tools/run.py`; an aggregator, flagged per operator rule 5).
  Cross-reference from the filer: the company bought its own shares in the first half of 2026 at an average of $62.78
  (8-K EX-99.1 of 2026-07-30, `0000764180-26-000093`).
- **Shares by class** from the latest filing's cover: **1,669,743,926** common shares, one class, as of 2026-07-22 (10-Q
  for the quarter ended 2026-06-30, filed 2026-07-30, accession `0000764180-26-000094`; `python Screens/cover_shares.py MO`).
  The balance sheet at 2025-12-31 shows 2,805,961,317 issued less 1,131,643,020 repurchased (10-K `0000764180-26-000017`).
- **Market cap:** $67.88 x 1,669.74M = **$113,342M**.
- **Debt beside it** (10-K balance sheet, 2025-12-31): long-term debt $24,140M plus current portion $1,569M = **$25,709M**,
  against cash of $4,474M. Dividends payable $1,782M; accrued settlement charges $2,178M.
- **Sovereign for the earnings currency (USD):** **5.66%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-05 (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-25, `0000764180-26-000017` (Item 1, Item 1A, MD&A
  segment results, the statements, Notes 14 and the stock-compensation note); 10-Q for the quarter ended 2026-06-30, filed
  2026-07-30, `0000764180-26-000094` (cover); 8-K of 2026-07-30 with EX-99.1, the second-quarter release,
  `0000764180-26-000093`; proxy (DEF 14A) filed 2026-04-02, `0001104659-26-038900` (fetched; not reached, see Q5);
  earlier 10-Ks for the ten-year volume and share record: FY2022 `0000764180-23-000020`, FY2019 `0000764180-20-000018`,
  FY2016 `0000764180-17-000028`. Competitors: British American Tobacco 20-F for 2025, filed 2026-02-13,
  `0001303523-26-000017`; Philip Morris International 10-K for 2025, filed 2026-02-06, `0001628280-26-005939`.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025
  **$9,290M** on the filed Consolidated Statement of Cash Flows (10-K `0000764180-26-000017`) against 9,290 in
  `tools/run.py`; also capital expenditures $216M and depreciation and amortization $266M, each matching.
- **`tools/run.py` arithmetic lines and the filed notes** (USD millions; owner cash = operating cash less stock pay less
  capital spending; stock pay is not a line on the cash-flow statement, `run.py` found none in XBRL and printed the
  warning, so it is taken from the stock-compensation note, RSU plus PSU pre-tax expense; script and output in
  `Test Runs/_research 2026-10-06 MO/owner_cash.py` and `owner_cash_output.txt`):

| FY | OCF | stock pay | capex | D&A | OCF less SBC less capex | OCF less SBC less D&A |
|---|---|---|---|---|---|---|
| 2021 | 8,405 | 40 | 169 | 244 | 8,196 | 8,121 |
| 2022 | 8,256 | 50 | 205 | 226 | 8,001 | 7,980 |
| 2023 | 9,287 | 58 | 196 | 272 | 9,033 | 8,957 |
| 2024 | 8,753 | 56 | 142 | 286 | 8,555 | 8,411 |
| 2025 | 9,290 | 62 | 216 | 266 | 9,012 | 8,962 |
| **five-year mean** | | | | | **8,559** | **8,486** |

  Three things the owner-cash line carries that a reader must know. (a) Operating cash includes the dividends from ABI
  ($208M, $139M, $163M in 2025, 2024, 2023), which is how the framework counts equity-method income (Q4, CONVENTION);
  the equity-method profit itself is not counted. (b) Cash taxes paid fell from $2,657M (2022) to $1,874M, $1,709M and
  $1,695M (2023 to 2025): the 2023 return claimed "a $ 4.0 billion ordinary loss" on the former JUUL investment (10-K
  FY2025, Note 14), and transferable tax credits reduced cash taxes in each year (cash-flow footnote). At the 21% federal
  statutory rate the loss is worth about $840M of tax (arithmetic; the filing does not state the cash effect by year);
  spread over the window it would take the five-year mean to about $8,391M. (c) Guidance for 2026 capital expenditure
  is "$375 million to $450 million" for a plant consolidation (EX-99.1), about twice the 2021 to 2025 run.

### The balance sheets, ten year-ends, read before the income account (written here because the file closes before Q4)
The rows ask that balance sheets be read "over an 8 or 10 year period before I even look at the income account"
**[M2025-032]**. From `tools/run.py` (first-filed XBRL; the FY2025 column checked against the filed balance sheet):

| year-end | assets | equity | goodwill | intangibles | LT debt + current | retained | cash | inventory |
|---|---|---|---|---|---|---|---|---|
| 2016 | 45,932 | 12,770 | 5,285 | 12,036 | 13,881 | 36,906 | 4,569 | 2,051 |
| 2017 | 43,202 | 15,377 | 5,307 | 12,400 | 13,894 | 42,251 | 1,253 | 2,225 |
| 2018 | 55,638 | 14,787 | 5,196 | 12,279 | 13,042 | 43,962 | 1,333 | 2,331 |
| 2019 | 49,271 | 6,222 | 5,177 | 12,687 | 28,042 | 36,539 | 2,117 | 2,293 |
| 2020 | 47,414 | 2,839 | 5,177 | 12,615 | 29,471 | 34,679 | 4,945 | 1,966 |
| 2021 | 39,523 | -1,606 | 5,177 | 12,306 | 28,044 | 30,664 | 4,544 | 1,194 |
| 2022 | 36,954 | -3,973 | 5,177 | 12,384 | 26,680 | 29,792 | 4,030 | 1,180 |
| 2023 | 38,570 | -3,540 | 6,791 | 13,686 | 26,233 | 31,094 | 3,686 | 1,215 |
| 2024 | 35,177 | -2,238 | 6,945 | 12,973 | 24,926 | 35,516 | 3,127 | 1,080 |
| 2025 | 35,017 | -3,502 | 5,787 | 11,876 | 25,709 | 35,452 | 4,474 | 1,070 |

**What the figures say.** The 2018 assets jump is the JUUL investment, financed by "$12.8 billion of short-term
borrowings used to finance Altria’s investment in JUUL in 2018" (10-K FY2019, `0000764180-20-000018`); those borrowings
were termed out in 2019, when long-term debt doubled (13.0 to 28.0 billion). The investment was then written down
(equity-method losses of $5,979M in 2021 and $2,186M in 2022 in XBRL), which is the fall in retained earnings. Equity has been negative since 2021: dividends and buybacks above earnings, financed by
the 2019 debt. Goodwill rose in 2023 with NJOY (bought for cash, $2,751M net, in the FY2023 cash-flow statement) and fell
by $1,158M in 2025 when NJOY's goodwill was impaired, with a further $978M of asset impairment and exit costs that year.
Inventory has fallen by half since 2018 while volume fell by half. What the figures do not say: whether the cigarette
cash stream behind the debt will last; that is the castle question.

### COMPUTATION — NOT A CLEARANCE
Owner-cash yield at the price: $8,559M / $113,342M = **7.55%** (capex basis), 7.49% (D&A basis), against the sovereign
at 5.66%. Aggregate owner cash grew at 2.40% a year from 2021 to 2025 on the capex basis, inside a window that holds the
JUUL tax relief. No value range is drawn here; Q7 is not reached.

## THE FOUNDATIONS (not a gate)
Two bear on this name. A share is a business: the question is what the cigarette and oral businesses will produce, not
what the next buyer pays **[M1997-109]**; the stock's yield invites the opposite habit. And the analyst's habits: the
corpus's own speakers, asked about tobacco companies, said they had no special insight into how government and society
would treat the product, and the speakers' later record on this very industry is the contrary evidence a reader must
weigh against that **[M1994-022]**, **[M1999-119]**; state the other side's case at its best **[M2016-055]** and look for
"what you’re missing" **[M2025-013]**. No macro enters: the consumer-income pressure the filer describes is not used as a
forecast **[M2000-094]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) since 2016 cigarette
shipments halved (122,930 to 61,752 million sticks, 10-Ks `0000764180-17-000028` and `0000764180-26-000017`) while
operating income before the 2025 impairments rose from $8,762M to $12,035M; a castle under "serious" legislative threat
in 1999 kept earning for a quarter century. (2) The menthol ban was withdrawn from OMB in January 2025 (10-K FY2025,
Potential Product Standards). (3) The industry decline rate fell from about 8% (2025) to about 5% (first half 2026,
EX-99.1). Each is carried into Q2.

## THE STANDING RULE
A marketable stake bought for cash, unlevered and sized so that its loss does not touch what the buyer has and needs,
puts the buyer at no risk of ruin **[M2012-081]**, **[L2023-005]**; borrowed money to own it is ruled out **[L2014-005]**.
The target's own debt is Q9's subject.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The business, from the filing.** Altria sells nicotine in the United States: cigarettes through PM USA (Marlboro,
  "the largest-selling cigarette brand in the United States for over 50 years"), large cigars (Black & Mild), moist
  smokeless (Copenhagen, Skoal), nicotine pouches (on!) and e-vapor (NJOY); it holds equity stakes in ABI and Cronos
  (10-K FY2025 Item 1, `0000764180-26-000017`). The smokeable segment earned adjusted OCI of $11,064M of the company's
  total on revenues net of excise of $17,443M, a 63.4% margin; oral earned $1,835M at 67.9% (MD&A segment results).
- **The key variables and how predictable they are** **[M1998-044]**: (1) the industry's cigarette volume decline rate,
  (2) the price realised per pack, (3) Marlboro's share and the discount segment's share, (4) settlement and FDA user-fee
  payments, which the filing ties to volume and inflation ("$3.0 billion on average for the next three years"), (5)
  migration to pouches and e-vapor, and (6) federal product standards. Variables 1 to 4 have a thirty-year record in the
  filings and the past statements do describe the shape of the future ones **[M2008-033]**: volume down, price up,
  margins held. Variables 5 and 6 are the castle's threats, not the mechanism of the business.
- **The understanding test as the rows state it.** "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**. The product, the distribution and the cost structure
  are plain; a cigarette is not a fast-moving technology, and the company's cigarette economics have behaved for a decade
  as the filings say they would. The question the rows separate from this is "the predictability of the economics of
  the situation 10 years out" **[M2000-104]**, and here the predictability turns on two things outside the mechanism:
  what government does to the product and how fast smokers move to substitutes. The rows give those to the castle
  question, "what can happen — say five, 10, 15 years from now — that will destroy, or modify, or reduce the economic
  strengths" **[M2000-014]**, and the routing of the framework sends rapid change in an industry to Q1 only where the
  business itself cannot be foreseen **[M1998-008]**. The cigarette business can be: its earning mechanism is known, its
  record long, and its competitive position inside the cigarette category is the strongest in it.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. The
  doubt here is not whether the business is understood but whether its castle will stand against a regulator and a
  substitute; that doubt is carried to Q2 and decided there, not waived.
- **VERDICT: IN.** The economics of the business are understood, its key variables are named and on the record, and
  the questions that make its future uncertain are castle questions **[M2012-065]**, **[M1998-044]**, **[M2000-014]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. Altria has two
castles of very different strength, and the filings show both.

- **Pricing power, and the agony before a rise** **[M2005-020]**, **[M2000-031]**. The strongest evidence in the file.
  PM USA raised the Marlboro list price four times in 2024 and four times in 2025 ($0.15 to $0.20 a pack each time) and
  again on 2026-01-18 ($0.20) (10-K FY2025, Pricing Actions). In 2025 higher pricing added $1,680M to smokeable revenue
  against $2,426M lost to volume, and adjusted OCI still rose 1.3% with the margin up from 61.6% to 63.4%; in the second
  quarter of 2026 the margin was 64.8% (EX-99.1). "If you name some business that has incredible pricing power, you’re
  talking about a business that’s a monopoly or a near monopoly." **[M2010-092]**. Against it, written down as found
  **[M1997-127]**: the filer says each year's pricing gain "includes higher promotional investments", the first sign of
  the price rise being paid for in discounts **[M2005-020]**.
- **Unit volume and share of mind** **[M1999-054]**, **[M1997-099]**. Cigarette shipments: 122,930 million sticks (2016),
  101,799 (2019), 84,678 (2022), 61,752 (2025): half in nine years, -7.36% a year compounded (10-Ks `0000764180-17-000028`,
  `0000764180-20-000018`, `0000764180-23-000020`, `0000764180-26-000017`; arithmetic in `owner_cash_output.txt`). Volume
  decline is not by itself a fail: the battery "will have unit declines over a period of time, but I think we’ll do fine"
  **[M2015-066]**. But the rows also say "If you really think a business is declining, most of the time you should avoid
  it" **[M2012-062]**, and the share of mind is slipping as well as the category: Marlboro's share of all cigarettes
  44.0% (2016), 43.1% (2019), 42.5% (2022), 40.5% (2025), 39.5% (second quarter 2026); PM USA's total 51.4% (2016) to
  45.2% (2025).
- **Would the customer still choose it over the low bid?** **[M2017-009]**. Inside premium, yes: Marlboro's share of the
  premium segment was 59.4% in 2025 and 59.6% in the second quarter of 2026, unchanged. But the low bid is taking the
  category: discount share 24.2% (2019), 26.9% (2022), 31.8% (2025), 33.8% (second quarter 2026). The filing names the
  attacker's weapon: discount makers "have cost advantages because they are not parties to settlements" (10-K Item 1A).
  Premium shipments fell from 95.9% to 93.6% of PM USA's own cigarette volume in a year as it moved into discount itself.
- **The money test and the attacker** **[M2011-015]**, **[M2012-108]**. No well-funded entrant has built a premium
  cigarette brand against Marlboro in the record read; inside cigarettes the castle stands. The attack comes from outside
  the category, in substitutes the customer moves to rather than rival cigarettes, and there Altria is the one losing:
  - **Oral.** The nicotine pouch reached 59.9% of the oral category in the second quarter of 2026 (51.8% a year
    earlier); Altria's oral retail share fell from 37.3% to 31.9% in 2025, Copenhagen from 19.0% to 15.4%, and on!'s share
    of the pouch category from 18.8% to 15.4% (2025) and was 14.4% in the second quarter of 2026 (10-K; EX-99.1). A Skoal
    trademark impairment of $354M was taken in 2024.
  - **E-vapor.** NJOY, bought for $2,751M net in 2023, had its principal product barred from import and sale by an ITC
    exclusion order; 2025 carried a $1,158M goodwill impairment and further intangible impairments in the e-vapor unit
    because of the ITC orders and "our expectation that effective enforcement against illicit flavored disposable
    e-vapor products would occur more gradually than initially anticipated" (10-K Item 1A). Flavored disposables, "the
    majority of which we believe have evaded the regulatory process", are about 70% of e-vapor (MD&A).
  - **Heated tobacco.** "there are no products in the U.S. marketplace from the joint venture" (10-K Item 1, as of
    2026-02-25).
- **The competitor row** (same metrics from the competitors' own filings):

| company | metric | 2025 | source |
|---|---|---|---|
| Altria (PM USA) | US cigarette shipments; industry estimate | -10.0% reported (-9.5% calendar-adjusted); industry about -8% | 10-K `0000764180-26-000017` |
| BAT (Reynolds) | US combustibles volume; price/mix; industry | -7.7%; +12.3%; industry -7.4%; "volume share was down 10 bps while value share was up 30 bps" | 20-F `0001303523-26-000017` |
| Altria (Helix, on!) | US pouch volume; share of pouch category | 177.8M cans (+10.9%); 15.4%, down 3.4 points | 10-K `0000764180-26-000017` |
| BAT (Velo) | US Modern Oral volume; category volume share | volume up 249%; 18.0%, up 11.6 points, "the number 2 position" | 20-F `0001303523-26-000017` |
| PMI (ZYN) | oral shipments, Americas | 930M cans, +29.4%, "predominantly driven by ZYN nicotine pouches in the U.S." | 10-K `0001628280-26-005939` |

  Asked which competitor they would shoot **[M1999-130]**, the competitors' filings answer by where they spend: both
  attack the pouch, where on! is third behind ZYN and Velo. BAT also names the cigarette's own enemy: "adult nicotine
  consumer migration to alternative nicotine products", with poly-usage among combustible smokers at 53%. The cigarette
  pricing the row shows is industry-wide, not Marlboro's alone (BAT price/mix +12.3%).
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Narrowing in share in every category the company sells,
  for nine years in cigarettes and sharply in oral; widening in margin. The rows put the moat ahead of the year's P&L
  **[M2000-075]**, so the margin does not settle it.
- **What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**. Two things, and both are aimed
  at the product, not at its price. (1) The regulator: "In January 2025, the FDA proposed a tobacco product standard
  that would establish a maximum nicotine level in cigarettes [...] with the aim of making such products minimally or
  non-addictive. The public comment period [...] closed in September 2025 [...] We believe the rulemaking process for
  this proposed product standard will take multiple years to complete." (10-K FY2025, Potential Product Standards). If it
  became final and were upheld it "could have a material adverse effect" (same section). (2) The substitute: the company
  has withdrawn its own forecast for it: "we continue to reassess our smoke-free goals and expect to provide updated
  goals when we have more clarity on how the legitimate e-vapor market may evolve" (MD&A, Vision and 2028 Goals). The
  2006 letter's test, would the business be started today against its substitutes **[L2006-008]**, has no answer in the
  filings, because the substitutes' legal status is itself undecided.
- **What the speakers said of this industry.** "You have to come to a conclusion as to how society is going to want to
  treat — and the present administration for that matter. And the economics of the business may be fine, but that
  doesn’t mean it has a great future." **[M1994-022]**; the same row's note records Buffett saying he had no special
  insights on it. In 1999 Buffett separated a political threat to pricing from one to the product: "the problems of the
  tobacco companies are of a far different order than the problems of the pharmaceutical companies" **[M1999-119]** (the
  row's note records Munger, just before, calling the legislative threat serious and beyond his power to predict). The
  nicotine standard is that second kind.
- **Contrary evidence, written down** **[M1997-127]**: the 1994 and 1999 doubts were followed by a quarter century in
  which the cigarette castle kept its pricing and its owners were well paid; the speakers' doubt did not prove the castle
  open, only that its future could not be judged by them, and the box is not a judgment of quality **[M2000-038]**. The
  menthol standards were withdrawn from OMB in January 2025, and the cigarette decline rate eased to about 5% in the
  first half of 2026. None of this answers the deciding question: none says whether a maximum-nicotine rule will be
  finalised, or where the substitutes and their enforcement will stand in ten years.
- **The routing.** The castle is not shown open on the evidence: inside cigarettes it stands and prices, so this is not
  OUT **[M2011-015]**. Its future cannot be judged, because it turns on a federal rule aimed at the product and on the
  pace of migration to substitutes whose legal status is unsettled: "In some businesses that’s very — it’s impossible —
  to figure [...] and then we just — we don’t even think about it then." **[M2000-014]**; "We don’t know how to valuate
  that, and therefore we leave it alone." **[M2000-019]**. The verdict is "too hard" **[M2006-013]**.
- **Which cause.** NATURE. The deciding question is a forecast the industry's insiders do not write down **[M2000-105]**:
  the filer gives "multiple years" for the rulemaking and no outcome, and has withdrawn its own smoke-free goals until it
  has "more clarity"; neither competitor filing read forecasts the rule or the substitutes' settlement either. It is
  important and not knowable from the documents **[M2006-076]**, and it is the case the rows name where study does not
  help: "the nature of the industry would be the roadblock" **[L1993-023]**. A lower price does not reopen it
  **[M2000-038]**.
- **VERDICT: TOO HARD (NATURE).** The cigarette castle stands and prices today; whether it stands in ten years depends on
  a regulator's rule aimed at the product and on substitutes the company is losing, and that cannot be judged
  **[M2000-014]**, **[M2000-019]**, **[M1999-119]**, **[M1994-022]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
(The filed figures are at Step 0: capital spending of $142M to $216M a year against operating cash near $9 billion; not
weighed, because the file closed at Q2.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED.
(Recorded for a later reader, not judged: the balance sheets are read at Step 0; the company features adjusted diluted
EPS, recast in 2025 for "amortization of intangibles that were not previously identified as special items and that are
now excluded from our adjusted financial measures" (10-K MD&A), guides adjusted EPS each year and to 2028, and states a
debt-to-Consolidated EBITDA target of "approximately 2.0x".)

## Q5 — WHO RUNS IT. NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
(Recorded, not judged: dividends paid $6,960M and buybacks $1,000M in 2025 against owner cash of $9,012M; a $2 billion
programme with no stated price, first-half 2026 purchases at an average $62.78 (EX-99.1); the JUUL and NJOY purchases and
their write-downs are at Step 0.)
## Q7 — WHAT IS IT WORTH. NOT REACHED.
## Q8 — BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 — COULD IT RUIN US. NOT REACHED.
## Q10 — THE FAT PITCH. NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT REACHED.
(Noted for the operator: tobacco is a named business in the rows. Had the run reached here, the framework makes it a
STOP only for a whole business bought and run **[M2005-097]**, **[M2016-064]**, **[M2021-013]**, and a WEIGHING for a
marketable stake, where the speakers would own the stock **[M2005-096]**, **[M2004-075]**, while Munger's later line runs
against investing in sellers of things bad for people **[M2021-059]**; that pull is OPEN in the framework.)

---
## THE BOX
**TOO HARD (NATURE), decided at Q2.** The cigarette castle stands and prices (Marlboro 59.6% of premium, four list
increases a year, adjusted OCI margin 64.8%), but its ten-year future turns on the FDA's proposed maximum-nicotine
standard and on migration to pouches and e-vapor in which Altria is losing share, and neither the filer nor its
competitors write that forecast down. Q7 not reached; no value range. Price $67.88 (aggregator), market cap $113,342M,
five-year owner cash $8,559M a year (7.55% of the price, a computation, not a clearance). The box reopens only on a change
in the facts, not in the price: the proposed nicotine standard withdrawn or struck down, and the substitutes' legal
status settled with Altria's place in them shown in the filings.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      Step 0 through Q1 were committed together (`53b9a95`) because the Step 0 reading ran into the Q1 facts; Q2 and the
      close in the next commit.
- [x] Every v5 id resolves (each grepped in `principle_ledger_v5.csv` before writing); every filing fact has its
      accession; the arithmetic is in `Test Runs/_research 2026-10-06 MO/owner_cash.py`.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance; the Step 0
      computation is headed as operator rule 3 requires.
- [x] Owner cash after every real cost, stock pay taken from the note because XBRL had none; never a net-income proxy
      (operator rule 5); the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, Q2 pricing, Q2 contrary paragraph).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its v4 lines (the growth the price assumes, the
      owner-earnings label) were not used.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **Regulation aimed at the product has no test of its own.** Q2's eleven tests ask about attackers,
price, volume, brand and change; a proposed federal standard that would make the product "minimally or non-addictive"
fits only test 11 **[M2000-014]**, and the rows that speak to it directly (**[M1994-022]**, **[M1999-119]**) are in the
ledger but not cited anywhere in Q2. The run used test 11 and those rows; a named test ("how will society and government
treat the product itself?") would keep two analysts from differing on whether this belongs at Q1 or Q2. (2) **The Q1 and
Q2 routing for an understood business with an unjudgeable threat.** The routing sends fast industry change to Q1 and "a
castle whose future cannot be judged" to Q2; a business whose mechanism is plain but whose future is set by a regulator
and by substitutes could be closed at either. This run chose Q2 because the doubt is about the castle, not the
mechanism, and says so. (3) **Declining volume with intact pricing.** **[M2012-062]** stands in Q2's OUT list ("declining
business") and **[M2015-066]** says unit declines are not a fail; the framework gives no line between them. The run did
not need one, but a run that reached Q7 would. (4) **Temporary cash-tax relief inside the five-year owner-cash
average.** The Q7 CONVENTION fixes the five-year average but not whether a one-off tax benefit (here the JUUL ordinary
loss, about $840M at the statutory rate) is taken out; the run showed both figures. Also: some ledger rows carry a second
speaker's words in their evolution note (Munger's line before **[M1999-119]**); the framework does not say whether a run
may quote a note, so this run only reported it. No tool defect found: `tools/run.py` found no stock pay in XBRL and said
so, as designed.
