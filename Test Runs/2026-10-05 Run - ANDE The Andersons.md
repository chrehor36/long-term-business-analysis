# Company Run: The Andersons, Inc. (NASDAQ: ANDE), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Every judgment
cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run
and later questions are marked NOT REACHED. Copied from `Test Runs/_TEMPLATE - Company Run.md` before any fetch.
Working folder: `Test Runs/_research 2026-10-05 ANDE/` (filings as text, the XBRL facts, the scripts `fetch.py`,
`xb.py`, `owner_cash.py`, `value.py`, and their outputs).

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is barred by this run's blind rule, so the
analyst does not know whether the operator holds the name.

**CONTAMINATION DECLARED.** No file about ANDE was seen or opened. Seen by name only, not opened: the session-start git
status listing untracked run files dated 2026-10-05 for LCII, LKQ and SLVM; a directory listing of `Test Runs/` that
matched "2026-10-05 Run - SXI Standex International.md" on the letters "ande" inside "Standex"; recent commit subjects
naming SCSC ScanSource (OUT at Q2), KSS Kohl's (OUT at Q2), AMR Alpha Metallurgical (OUT at Q2) and a session-state
commit about an S&P 600 screen; and the memory index line saying the queue held "57 gate-clearers, nothing buyable". The
three Q2 outs in commit subjects are a prior that this kind of run tends to close at Q2; it is declared so the reader can
weigh it. None of the barred files was opened.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $66.84 (2026-10-05, from `tools/run.py`; aggregator, live quote only, flagged per operator rule 5).
  For scale only: the 2026 proxy values director RSUs granted on 2025-08-22 at "$40.95 per share, the closing price on
  the date of issuance" (DEF 14A, 2026-03-11, accession `0001104659-26-026341`), so the price is up about 63% in
  thirteen months.
- **Shares by class** from the latest filing's cover: one class, common, 33,975,570 shares (10-Q for the period ended
  2026-06-30, filed 2026-08-04, accession `0000821026-26-000122`; `python Screens/cover_shares.py ANDE`). Issued
  34,211 thousand less 194 thousand treasury at 2026-06-30 on the balance sheet of the same 10-Q, 34.017M, close to the
  cover count of 2026-07-31.
- **Market cap:** $66.84 x 33.976M = $2,271M.
- **Sovereign for the earnings currency (USD):** 5.63%, US Treasury daily par yield curve, 30-year, 10/02/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-18, `0000821026-26-000010`), Items 1, 1A, 2, 7 and 8 in
  part; 10-Q Q2 2026 (filed 2026-08-04, `0000821026-26-000122`), statements and MD&A; DEF 14A 2026 (filed 2026-03-11,
  `0001104659-26-026341`), pay measures and ownership table; 8-K of 2025-08-04 (`0000821026-25-000147`, the TAMH
  buyout); 8-K of 2026-03-25 (`0000821026-26-000048`, the credit agreement amendment). For the segment history: 10-Ks
  FY2012 (`0000821026-13-000005`), FY2015 (`0000821026-16-000068`), FY2018 (`0000821026-19-000026`), FY2019
  (`0000821026-20-000011`), FY2021 (`0000821026-22-000050`), FY2022 (`0000821026-23-000068`), FY2023
  (`0000821026-24-000071`), FY2024 (`0000821026-25-000050`). The 8-K of 2026-08-03 (`0000821026-26-000120`, the Q2
  release) was listed, not read; the 10-Q it summarises was read.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $176,998
  thousand on the filed Consolidated Statement of Cash Flows (10-K FY2025, page 34), against $177.0M in the
  `tools/run.py` XBRL transcription. Agrees.
- **`python tools/run.py ANDE`, arithmetic lines only** (output saved as `run_py_output.txt`): OCF 946.8 / 331.5 / 177.0
  (2023 / 2024 / 2025, $M); SBC 12.9 / 13.6 / 17.0; D&A 125.1 / 127.8 / 133.3; capex 150.4 / 149.2 / 233.1. Its
  "owner earnings" are OCF less SBC less capex, so they carry the working-capital swings: 783.4 in 2023 is grain
  inventory liquidated (inventories released $572.2M and receivables $469.0M that year on the filed cash-flow statement),
  not earnings. Its printed "yield" of 12.90% rests on that 2023 figure and is not used. Owner cash is rebuilt below on a
  consistent basis.

### Owner cash, rebuilt on a consistent basis (operator rule 5)
**How.** Net income from continuing operations (including the noncontrolling share) + depreciation and amortization of
continuing operations + non-cash asset impairments - capital spending of continuing operations. Working-capital changes
are left out because they are the grain and fertilizer price cycle passing through inventory, receivables, payables and
margin deposits, financed by seasonal short-term lines; over 2016 to 2025 operating cash summed $2,045M against $2,193M
of cash earnings so measured, so working capital absorbed about $148M in ten years (and the LTG purchase of 2019 brought
its working capital in through the acquisition, not through operating cash). Stock pay stays deducted (it is an expense
inside net income). The noncontrolling share is kept because ANDE has owned 100% of the four ethanol plants since
2025-07-31; the $425.0M paid for that 49.9% is charged a carrying cost (below). Rail, sold in 2021 and 2022, is removed
using the filed discontinued-operations lines. Source: XBRL company facts transcribed from the 10-Ks above, checked to
the FY2025 filed statements (2025: 119.3 + 133.3 + 18.1 - 233.1 = 37.6).

| FY | NI cont. | D&A cont. | impairment | capex cont. | owner cash (capex basis) | owner cash (NI + impairment, D&A as capex) | pretax cont. |
|---|---|---|---|---|---|---|---|
| 2016 | 14.5 | 84.3 | 9.1 | 77.7 | 30.2 | 23.6 | 21.4 |
| 2017 | 42.6 | 86.4 | 10.9 | 34.6 | 105.3 | 53.5 | -20.5 |
| 2018 | 41.2 | 90.3 | 6.3 | 142.6 | -4.8 | 47.5 | 53.2 |
| 2019 | 3.9 | 112.0 | 41.2 | 58.1 | 99.0 | 45.1 | 13.0 |
| 2020 | -16.2 | 153.1 | 0.0 | 45.0 | 91.9 | -16.2 | -27.1 |
| 2021 | 131.5 | 157.2 | 8.9 | 67.1 | 230.6 | 140.5 | 160.8 |
| 2022 | 155.0 | 134.7 | 11.8 | 76.8 | 224.7 | 166.8 | 194.6 |
| 2023 | 132.5 | 125.1 | 87.2 | 150.4 | 194.3 | 219.7 | 169.6 |
| 2024 | 170.7 | 127.8 | 0.0 | 149.2 | 149.3 | 170.7 | 200.8 |
| 2025 | 119.3 | 133.3 | 18.1 | 233.1 | 37.6 | 137.4 | 141.5 |

($M. 2016 to 2018 still include Rail, which the filings of those years did not separate; the 2023 impairment is the
$87.2M ELEMENT write-off, capital spent in 2018 and 2019 and lost.)

- **Five-year mean, 2021 to 2025:** $167.3M (capex basis), $167.0M (D&A basis). Less the after-tax carrying cost of the
  $425.0M TAMH payment, CONVENTION of this run ($425.0M x 5.63% sovereign = $23.9M pre-tax, $18.9M after 21% tax;
  rationale: the five years earned interest on cash of up to $644M and carried less debt, and the payment that replaced
  the minority's share took that cash; the sovereign is used because the framework names no other rate): **$148.4M, or
  $4.37 a share after tax; $175.0M, or $5.15 a share, pre-tax** (pretax income + impairment + D&A - capex - $23.9M).
- **Seven-year mean, 2019 to 2025** (the first year the present structure existed: LTG fully owned from 2019-01-02, TAMH
  formed 2019): $146.8M capex basis, $123.4M D&A basis; after the same charge, $127.9M and $104.5M; pre-tax $145.2M
  ($4.27 a share).
- **Capex against D&A:** 2019 to 2025 capex $779M against D&A $943M; but 2025 capex $233.1M against D&A $133.3M and H1
  2026 capex $127.3M against D&A $68.7M (10-Q). Maintenance is not split out in the filings; the five-year capex and D&A
  bases agree within $0.3M, so the choice does not move the five-year figure.

### The balance sheets, ten year-ends (read in Step 0 because the file closes before Q4)
"balance sheets over an 8 or 10 year period" **[M2025-032]**, from the `tools/run.py` table, checked to the FY2025 and
FY2024 filed balance sheets ($M):

| year-end | equity (ANDE) | goodwill | intangibles | cash | inventory | LT debt | retained |
|---|---|---|---|---|---|---|---|
| 2016 | 774 | 64 | 106 | 63 | 683 | 397 | 609 |
| 2019 | 974 | 135 | 175 | 55 | 1,171 | 1,016 | 643 |
| 2021 | 1,072 | 129 | 117 | 216 | 1,815 | 600 | 703 |
| 2023 | 1,283 | 128 | 86 | 644 | 1,167 | 563 | 883 |
| 2024 | 1,366 | 128 | 69 | 562 | 1,287 | 608 | 971 |
| 2025 | 1,245 | 128 | 64 | 98 | 1,365 | 560 | 1,039 |
| 2026-06-30 | 1,319 | (in other assets) | | 67 | 961 | 563 | 1,115 |

What the figures say:
- **Equity grew slowly and partly by issuance.** ANDE equity $774M to $1,245M in nine years; retained earnings $609M to
  $1,039M. 4.4 million shares were issued on 2019-01-02 as 38.9% of the LTG consideration (10-K FY2019). Tangible equity
  at 2025 year-end about $1,053M ($1,245M less goodwill $128M and intangibles $64M); price to book 1.72 at June 2026
  equity of $38.77 a share ($1,318.7M over 34.017M shares).
- **The 2025 fall in equity is the TAMH premium.** Additional paid-in capital fell from $385.6M to $208.4M: $425.0M was
  paid for a minority interest carried at about $246M (NCI $246.1M at 2025-06-30 on the 10-Q), the difference charged to
  equity. The 8-K says the $425.0M was "inclusive of $40.0 million of working capital".
- **Inventory and debt move together.** Inventory $683M (2016) to $1,171M (2019, LTG consolidated) to $1,815M (2021, high
  grain prices) to $961M (June 2026, seasonal low). Short-term debt ranges $22M to $502M across the years; at 2026-06-30
  short-term debt $314.4M, current long-term $22.9M, long-term $563.5M, against cash $66.5M. Inventory against sales:
  17% in 2016, 12% in 2025 (sales $11,009M).
- **Cash was a boom residue, now spent.** $644M (2023) and $562M (2024) came from inventory liquidation and the ethanol
  boom; $425.0M went to Marathon's stake in July 2025.
- **What they don't say.** Receivables of $652.5M at 2025 year-end are after $243.9M sold without recourse under
  factoring in 2025 ($201.7M in 2024), so receivables and operating cash are both flattered by the program as it grows;
  the allowance for doubtful accounts is $42.6M (2025) and $48.3M (2024), and bad-debt expense was $17.6M in 2024 (10-K
  FY2025). Readily marketable grain inventories are marked to market through cost of sales, so reported inventory and
  gross profit move with exchange prices.
- **Liabilities that can be called.** The FY2025 10-K: "Our futures, options, and over-the-counter contracts are subject
  to margin calls", and some borrowings "require minimum levels of working capital and equity". The revolver was cut from
  $1.55B to $1.30B and extended to 2031 (8-K, 2026-03-25).

## THE FOUNDATIONS (not a gate)
Three bear on this name. A share is a business: the question is whether I would own this business "if the market closed
for five years" **[M1997-109]**, and the 63% rise since August 2025 counts for nothing, since appreciation "is never a
reason to buy it" **[L2013-007]**. The market serves: the price is information only, "the market is there to serve you
and not to instruct you" **[M2006-077]**. No macro enters: corn, crush spreads, tariffs and the Renewable Fuel Standard
are the weather of this business, and what counts is "the average profitability of the business over time" **[M2015-016]**,
which is why the run reads fifteen years and not the strong first half of 2026.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the Renewables segment earned $139.5M (2024) and
$140.1M (2025) pre-tax on identifiable assets of $680.5M and $617.3M, above 20%; (2) H1 2026 pre-tax income $101.2M
against $28.0M a year earlier, with Q2 the segment's "highest second quarter results to date" (10-Q); (3) the plants
produce "consistently well in excess" of a 405 million gallon nameplate (10-K FY2025); (4) the trade business earned a
steady $87.9M to $96.2M pre-tax a year from 2021 to 2024 after the LTG purchase; (5) the filer's own focus is "leading
the industry in margins per bushel", a low-cost claim. Each is weighed at Q2.

## THE STANDING RULE
A cash purchase of a marketable common stock, unlevered and sized so that its loss would not touch what the buyer needs,
puts the buyer at no risk of ruin; the rule binds the financing: "Anything can happen anytime in markets." **[L2014-005]**,
and the buyer is "never going to risk what we have and need" **[M2012-081]**. No conflict for this name if bought that
way. The target's own margin calls belong to Q9.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**. The product chemistry need not be known; what
  is needed is to "understand the economic dynamics of the industry" **[M2011-014]**.
- **The key variables** ("trying to identify the key variables in that particular business" **[M1998-044]**): in
  Agribusiness, bushels handled, the basis and the carry between futures months earned on 270.8 million bushels of
  storage in the US and Canada (10-K FY2025, Item 2: Kansas 74.2M, Ohio 38.6M, Michigan 27.2M, Texas 23.9M, Louisiana
  23.3M, Canada 21.2M among others), and fertilizer margins; in Renewables, the crush spread (ethanol and co-products less
  corn and gas) at four plants (Indiana 110M, Iowa 55M, Michigan 130M, Ohio 110M gallons nameplate), plus federal credits.
- **Are they foreseeable?** Their level is not, year to year; their nature is. Grain origination, storage and fertilizer
  are old trades with slow change; the filer's own description of how money is made (basis appreciation, spread, storage
  fees) is the one the FY2012 10-K gave for its "Space income" (basis, spread, storage fees). What I can foresee for ten years is that this is a
  price-taking handler and processor of commodities whose returns follow the cycle; that is a fix on the economics, which
  is what the test asks, even though it is not a flattering one. The past statements do tell me what the future ones will
  look like in kind: "the financial statements will tell me the information" **[M2008-033]**, provided fifteen years and
  not five are read.
- **The doubt, recorded.** Ethanol's ten-year economics depend on government (the Renewable Fuel Standard; the Section
  45Z credit, which "applies to qualifying fuel produced after December 31, 2024, and sold through December 31, 2029",
  10-K FY2025 Item 1A) and on gasoline demand. That is a forecast insiders would decline to write down for the level of
  margins **[M2000-105]**, but it is not a fast-changing technology; the variable is "important and knowable" **[M2006-076]**
  in its direction (a policy-made margin that can be withdrawn), and the direction is enough for Q2. It is carried to Q2
  as a threat to the castle, not used to close the file here.
- **VERDICT: IN.** The economics of grain handling, fertilizer and ethanol are understood in their dynamics
  **[M2011-014]**, and the earning power and competitive position can be fixed in kind for ten years **[M2012-065]**; the
  understanding is what lets Q2 decide whether there is a sustainable edge **[M1997-148]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
- **The filer's own description of the competition** (10-K FY2025, Item 1, Agribusiness): "The Company competes in the
  sale of commodities and nutrient inputs with other public and private grain brokers, farm retailers, elevator operators
  and farmer owned cooperatives. Some of the Company's competitors are also its customers. Competition is based primarily
  on price, service and reliability." And Item 1A: "The markets for our products in both of our business segments are
  highly competitive. While we have substantial operations in certain regions where we operate, some of our competitors
  are significantly larger, compete in wider markets, have greater purchasing power, and have considerably larger
  financial resources." The price itself is set elsewhere: "Futures prices are determined by worldwide supply and demand."
  Fertilizer is bought "from a small number of suppliers".
- **The commodity test.** The marks the rows give are all present. The product is standard and the customer buys on
  price: the rows' commodity is one where "They sell a commodity-like product" and so "price competition [...] is usually
  fierce" (the insurance row, **[L2004-003]**, by analogy). The rival sets the price: "whatever he charged for gas was my
  price" **[M2012-109]**; "he determined our profit, because we looked at his price every day" **[M2023-079]**; here the
  exchange and the larger merchants set it. Improvements pass to the customer: "the improvement you get one day, your
  competitor gets the next day" **[M2004-053]**. ANDE buys commodities and sells commodities; the formula the rows praise
  is "Buy commodities, sell brands" **[L2011-008]**, and ANDE has no brand to sell.
- **Would the customer still choose it over the low bid?** No evidence of it: the filer says competition is "primarily
  on price", the opposite of "people buying candy for the low bid" **[M2017-009]**, which See's escaped.
- **The attacker with money.** "could I do it?" **[M2011-015]**: elevators, fertilizer terminals and ethanol plants are
  bought and built by cooperatives, ADM, Bunge, Cargill and private plants; ANDE itself bought its way in (LTG in 2019,
  four ethanol plants in stages ending with Marathon's 49.9% for $425.0M in 2025, a price per gallon of capacity that a
  rival with money can also pay). "one competitor is frequently enough to ruin a business" **[M2012-108]**.
- **The one exception: is ANDE the low-cost operator?** The rows allow a commodity business through on cost: "being the
  low-cost producer is all-important" **[L2000-017]**; "Another way to prosper in a commodity-type business is to be the
  low-cost operator" **[L2004-007]**; otherwise "the low-cost producer can put you out of business" **[M1997-010]**, and
  "the guy with the lower cost comes in and kills you" **[M2001-013]**. The cost is relative: "Those are two different
  kinds of businesses" **[M2009-059]**. No unit cost is disclosed by ANDE or its rivals in a comparable form, so the test
  is run on what a low-cost operator must show over a whole cycle: higher returns than the field. The competitor row:

| company (filing) | metric | 2011 to 2025 avg | 2016 to 2025 avg | 2021 to 2025 avg | note |
|---|---|---|---|---|---|
| **ANDE** (10-Ks above; XBRL facts) | pre-tax income / beginning total equity | **11.4%** | **6.8%** | 12.5% | losses or near-zero in 2015, 2016, 2017, 2019, 2020 |
| ADM (10-Ks, latest `0000007084-26-000011`) | same | 12.5% | 12.1% | 14.5% | never below 5.7% in the span; includes a 2012 transition period |
| Bunge (Bunge Ltd to FY2022, latest `0001144519-23-000010`; Bunge Global from FY2023, latest `0001628280-26-009842`) | same | 12.7% | 15.0% | 24.3% | one loss year (2019) |
| REX American (10-Ks, latest in the facts `0000930413-25-001069`, fiscal years to Jan 2025; FY Jan 2026 10-K `0000930413-26-000937` opened for gallons only) | same | 13.6% | 10.4% | 12.6% | pure ethanol, holds large cash, so its equity return understates its plants |
| Green Plains (10-Ks, latest `0001309402-26-000019`) | same | 0.1% | -8.0% | -9.2% | the weak ethanol producer |
| CHS Inc. (10-Ks, latest `0000823277-25-000038`; fiscal years to August) | same | 14.2% | 9.0% | 12.7% | FLAGGED: a cooperative with patronage and oil refining; not comparable on tax or mix |
| Scoular | none | none | none | none | FLAGGED: private, no SEC filings |

  (Script `peers_avg.txt`; values are the latest-filed XBRL value for each fiscal year, transcribed from the filers' own
  10-Ks.) Pre-tax margin on sales, same span: ANDE -0.6% to 3.2% (2013 to 2015 not computed, the revenue tag was unusable), 1.1%
  to 1.8% in 2021 to 2025; ADM 1.6% to 5.2%.
  Segment returns (ANDE 10-Ks): Trade earned pre-tax -$17.3M, $24.7M, $87.9M, $95.2M, $96.2M, $91.4M in 2019 to 2024 on
  identifiable assets of $2.0B to $3.2B, about 2.5% a year; Agribusiness (trade plus nutrient) $56.6M on $2,848M in 2025,
  2.0%. Renewables earned $47.7M, -$47.3M, $81.2M, $108.2M, $91.2M (after the $87.2M ELEMENT impairment), $139.5M,
  $140.1M in 2019 to 2025 on assets of $617M to $836M, about 11% a year before the minority's share; the 2025 figure
  includes $35.0M of Section 45Z credits, and H1 2026 includes $50.4M more.
- **Reading the row.** Over fifteen years ANDE earned less on its equity than ADM, Bunge and REX, and more than Green
  Plains. Over the last ten it earned about half of what ADM and Bunge did. For the low-cost operator "a tough market helps"
  **[L1997-021]**; ANDE lost money or nearly so in five of the fifteen. Its strongest stretch, 2021 to 2025, is
  the stretch every grain merchant and every efficient ethanol plant also enjoyed, and it still trailed ADM and Bunge. The
  contrary evidence written at the foundations is real (Renewables above 20% on assets in 2024 and 2025; trade steady since
  2021), but it coincides with the ethanol boom of 2021 to 2023, then the 45Z credits from 2025, and does not survive the
  whole-span comparison. The "margins per bushel" claim is the filer's; the returns do not show it against REX, the one
  pure-ethanol peer with a long record.
- **What could destroy, modify or reduce it** **[M2000-014]**: the Section 45Z credit ends with fuel sold through
  2029-12-31; ethanol demand rides on the 10% blend and the RFS ("much of the blending is done to meet the RFS standard by
  adding 10% ethanol", 10-K); tariffs and trade disputes on export grain (Item 1A); and the larger rivals named by the
  filer. The failed ELEMENT plant (built 2019, $87.2M impaired in 2023, placed in receivership 2023-04-18, litigation
  settled in principle in Q2 2026, with about $11 million of added litigation expense in 2026, 10-Q) shows the cost of a plant without a cost edge.
- **Widening or narrowing?** Neither shown. The trade business grew by purchase (LTG), not by an advantage that widened;
  the ethanol margin of 2024 to 2026 is a policy-and-cycle margin that every plant shared.
- **VERDICT: OUT.** The castle is shown open on the filer's own evidence: competition "primarily on price", prices set by
  the exchanges, rivals "significantly larger" with "greater purchasing power", and fifteen years of returns that do not
  show the low-cost operator the one exception requires **[L2000-017]**, **[M1997-010]**. This is the business whose price the rival sets, the gas station of the rows, "whatever he charged for gas was my
  price" **[M2012-109]**, and a castle shown open on the evidence goes to OUT, not TOO HARD
  **[M2011-015]**: the future is not unjudgeable, it is judged to be the commodity average. A low price would not reopen
  it: you cannot "turn any investment into a good deal by paying little" **[M2019-015]**, and "marginal businesses
  purchased at cheap prices may be attractive as short-term investments" **[L2014-009]** only.

---
## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED (Q2 closed OUT).
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED. (The balance sheets were read in Step 0, above.)
## Q5: WHO RUNS IT. NOT REACHED.
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
Facts gathered while reading, recorded for whoever reopens the file, not weighed: dividends paid $26.8M in 2025 ($0.20 a
quarter declared in 2026); buybacks $15.4M in 2025 and $4.6M in H1 2026, with no stated price limit found; stock pay
$17.0M in 2025 (10% of net income attributable of $95.7M); no options granted since 2015; the proxy names "Adjusted
Pretax Income", "Adjusted EPS", "Return on Invested Capital (ROIC)", "Relative TSR" and net income as the pay measures,
and the filer presents adjusted EBITDA; the TAMH stake was bought for cash at 1.73 times its carrying value; the LTG stake
was bought in part with 4.4 million new shares in January 2019.
## Q7: WHAT IS IT WORTH. NOT REACHED as a clearance. See the COMPUTATION below.
## Q8: BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9: COULD IT RUIN US. NOT REACHED.
## Q10: THE FAT PITCH. NOT REACHED.
## Q12 (optional): NOT ASKED.

---
## COMPUTATION: NOT A CLEARANCE
*(Reported at the owner's request, not a rule change. Q2 closed OUT; nothing below is entry language, and no figure
below reopens the file.)*

**Method.** The Q7 CONVENTION of `Framework/THE FRAMEWORK v5.md`: five-year average owner cash after every real cost
("a figure calculated after interest, taxes, depreciation, amortization and all forms of compensation" **[L2021-003]**;
depreciation as "almost always true costs" **[L2015-004]**), carried ten years at the growth shown, then no nominal
growth, discounted at the 5.63% sovereign. Script `value.py`, output `value.txt`.

**Growth shown.** On the aggregate owner cash of 2021 to 2025: the D&A basis moved from $140.5M to $137.4M, -0.6% a year;
the capex basis from $230.6M to $37.6M, -36% a year. The capex-basis rate is capex timing (2021 capex $67M, 2025 $233M),
an absurdity the convention's Q3 cap excludes, so -0.6% is the shown rate and the no-growth case is the top end (the
convention never carries growth above what was shown).

**(a) VALUE RANGE (convention, five years 2021 to 2025, $148.4M after tax):** **$73.99 to $77.59 a share** (capex
basis; D&A basis $73.84 to $77.43), against **$66.84**. Width 1.05 to 1, so not TOO HARD on width; the price sits about
10% below the bottom, just below a narrow range, a case that would need a pencil: "It should scream at you."
**[M2009-005]**. A 2.1% growth case (pre-tax
income 2010 to 2025, $104.1M to $141.5M, the whole span including acquisitions) would give $91.63; it is outside the
convention and shown only to say how much the answer depends on the input.

**(a') WHOLE-CYCLE VARIANT (2019 to 2025, the trough of 2019 and 2020 and the boom of 2021 to 2023 both inside):**
capex basis $127.9M after tax, **$63.75 to $66.85**; D&A basis $104.5M, **$52.11 to $54.64**; with the 2.1% case, $78.96
and $64.54. The price sits at the top of the whole-cycle range on the capex basis and above it on the D&A basis. A
ten-year variant (2016 to 2025, Rail still in 2016 to 2018) gives $48.32 to $50.66 (capex) and $39.86 to $41.80 (D&A).

**(b) FAIR PRICE** (the price at or below which the central case clears the ~10% pre-tax floor; the floor is the
speakers' "at least 10% pre-tax returns" **[L2002-020]**, below which "we drop out of the game" **[M2003-149]**). Tax
treatment: pre-tax means before corporate income tax; pre-tax owner cash = filed pretax income from continuing operations
+ impairment + D&A - capex - the $23.9M pre-tax carrying cost of the TAMH payment. The Section 45Z credits are inside
filed pretax income and are not taxed, which flatters the pre-tax figure against the after-tax one. Central case: $5.15 a
share pre-tax (five-year), no growth: **fair price $51.51**; at the shown -0.6%, $48.58. On the whole-cycle base ($4.27):
$42.73. At $66.84 the expected pre-tax return is 7.7% on the five-year base and 6.4% on the whole-cycle base, below the
floor either way.

**(c) CHEAP PRICE** (below which no pencil is needed). Rule, CONVENTION of this run: half the lowest bottom among the
ranges computed (the whole-cycle D&A-basis bottom, $52.11), because the rows ask for "a big discount from that present
value" **[M1997-126]** and their example is a price about a third of the value, so that "I would know they were fat"
**[M2008-068]**; and checked that at that price even the weakest base (ten years with Rail, $3.03 a share pre-tax) still
clears the 10% floor (11.6%). **Cheap price about $26.** The price is about 2.6 times it.

**Summary against the price:** value range $73.99 to $77.59 (five-year), $52.11 to $66.85 (whole cycle); fair $51.51;
cheap about $26; price $66.84. Even had Q2 passed, the file would have closed OUT at Q7 on the floor.

---
## THE BOX
**OUT, decided at Q2** (a commodity castle shown open on the filer's own evidence, with no low-cost edge in fifteen years
of returns against ADM, Bunge and REX). Not a TOO HARD, so no research pass is opened. For reference only (COMPUTATION,
not a clearance): value range $73.99 to $77.59 (five-year convention) and $52.11 to $66.85 (whole cycle), fair $51.51,
cheap about $26, against $66.84.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Written section by section; **not committed**, at the dispatcher's
      instruction ("Do not commit"), so the write-early commit after each question did not happen.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, below); every filing fact has its accession;
      the numbers come from the filings or the scripts in the working folder, the conventions are labelled.
- [x] The order was kept; Q2 closed the run OUT; nothing after it is a clearance, and the value figures are headed
      COMPUTATION: NOT A CLEARANCE. (The heading uses a colon where the protocol prints a dash, by the no-dash rule.)
- [x] Owner cash after every real cost on a consistent basis, never a net-income proxy: net income plus non-cash charges
      less capex, stock pay kept as a cost, working capital excluded and its ten-year total stated; the sovereign from the
      Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]**, at the foundations, and weighed at Q2.
- [x] No point-in-time anchor; not applicable.
- [x] Only the arithmetic lines of `tools/run.py` were used; its "yield" and "points over the sovereign" lines rest on
      working-capital swings and were set aside.
- [x] `python tools/check_framework.py` run (result recorded below).

**Check results (2026-10-05):** see the last lines of this file.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Owner cash for a business whose working capital is the commodity price.** The template and `tools/run.py` build
owner cash from operating cash flow, which for a grain merchant swings by hundreds of millions with prices (2023: $947M
of operating cash against about $194M of owner cash); the run.py "yield" of 12.9% was an artefact. Neither the framework
nor the template says when working capital is excluded; this run excluded it and stated the ten-year total, but that is
a choice. (2) **A minority bought out inside the five-year window.** The Q7 convention averages five years of a company
whose ownership of its largest earner changed from 50.1% to 100% in year five; no rule says how. This run used
whole-company figures less a carrying cost on the price paid at the sovereign, a CONVENTION of its own. (3) **The
low-cost exception has no test for a firm that discloses no unit costs.** Q2 asks whether the business is the low-cost
operator; for a merchandiser and processor no comparable cost per bushel or per gallon is filed, so this run used
whole-span pre-tax returns on equity against the peers as the evidence a low-cost operator would leave. The framework does
not name that proxy, and returns on equity mix leverage and cash holdings (REX's cash depresses its figure). (4) **"Growth
shown" is unmeasured.** The convention does not say endpoints or a fitted rate, nor which basis; on the capex basis the
five-year rate here is -36% a year from capex timing alone. This run used the D&A-basis endpoints and said why.
(5) **Pre-tax floor and untaxed credits.** The floor is "pre-tax", and the Section 45Z credits are pre-tax income that
bears no tax; a business earning tax credits looks better against a pre-tax floor than its after-tax cash justifies. The
framework is silent. (6) **Policy-made economics between Q1 and Q2.** The routing rule sends fast technology to Q1 TOO
HARD and an open castle to Q2 OUT; it says nothing of an industry whose margin is set by a statute with an end date
(the RFS, 45Z to 2029). This run treated it as a Q2 threat; another analyst could send it to Q1 TOO HARD (NATURE) on
test 5, and the box would differ.

---
**Check results, 2026-10-05.** `python tools/check_framework.py`: PASS. `Test Runs/_research 2026-10-05 ANDE/check_run.py`:
no em or en dashes; no E-ids; every M, L and R id cited in this file is a row of `principle_ledger_v5.csv`; every quoted
fragment placed beside an id is found in that id's row (after normalising curly and straight quotes and splitting at
`[...]`).
