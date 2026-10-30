# Company Run: Vistra Corp. (NYSE: VST), 2026-10-27
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch** (commit eda4478c).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-27: the operator does not hold this name (`PORTFOLIO.md` has no VST row).*

**Dispatch.** A dispatched purchase run under `Screens/_daily/_dispatch_brief.md`, with the departures the brief states (new
repository path; the analyst derives the lines of evidence from the 10-K). Research folder: `Test Runs/_research 2026-10-27 VST/`
(scripts, tool outputs, computations; raw filings in its ignored `cache/`).

**Contamination, declared.** The session context showed recent commit subjects of this repository (folds and audits of other
names: VGNT, PPL, TAC); none concerns this company, none was opened, nothing of them is used. No other run file, holding review,
`PORTFOLIO.md` or blind-listed file was opened, listed or searched.

**Lines of evidence, chosen by the analyst from the FY2025 10-K's Item 1, Item 1A and Item 7** (accession 0001692819-26-000006):
(1) how the wholesale price is set and where the fleet sits on the cost curve (Item 1, Market Discussion; Item 7, Factors
Affecting); (2) the field's record over a full cycle: Winter Storm Uri in 2021 and the bankruptcies in the field, from the filer's
and the rivals' filings (Item 1A); (3) retail competition and customer counts (Item 1, Retail Operations; Item 1A); (4) the
large-load contracts, the claimed change for the better (Item 7, highlights: AWS and Meta PPAs); (5) capital: maintenance against
growth spending, and the acquisitions (Energy Harbor, Lotus, Cogentrix, the Vistra Vision buyout) (Item 7; Note 21); (6) debt,
liquidity and collateral (Item 1A, $20.7 billion of indebtedness; margin deposits); (7) hedging without hedge accounting and the
non-GAAP figures the filer features (Item 1A; Note 21; the earnings releases); (8) market design and subsidy (PJM capacity price
cap, ERCOT co-optimization, the 45U nuclear PTC) (Item 1; Item 7).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $141.73 (close 2026-10-26; aggregator quote printed by `tools/run.py`, flagged per operator rule 5: live quote only).
- **Shares by class** from the latest filing's cover: 335,635,195 common, single class (10-Q for the period ended 2026-06-30,
  filed 2026-08-10, accession 0001692819-26-000019; `python Screens/cover_shares.py VST`). Cross-checks: the 10-Q balance sheet
  shows 335,961,328 shares outstanding at 2026-06-30 (issued less 220,121,017 treasury shares), consistent with buybacks after the
  quarter end. Filings after the 10-Q read for share changes: 8-Ks of 2026-09-24 (junior subordinated notes) and 2026-10-05 (credit
  amendment), the 424B5 of 2026-09-10 (listed, not opened); none issues common stock. The Cogentrix deal would issue 5,000,000 shares
  at closing; not closed (Q7).
- **Market cap:** 335.635M x $141.73 = **$47,570M**.
- **Sovereign for the earnings currency (USD):** **5.31%**, US Treasury daily par yield curve, 30-year, 10/26/2026 (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-27, 0001692819-26-000006): Items 1, 1A, 7, the statements, Notes 21
  (segments), income taxes, litigation; 10-K FY2024 (2025-02-28, 0001692819-25-000013); 10-K FY2023 (2024-02-29, 0001692819-24-000012);
  10-K FY2022 (2023-03-01, 0001692819-23-000005); 10-K FY2020 (2021-02-26, 0001692819-21-000004), each for its cash-flow statement,
  segment note and MD&A capital tables; 10-Q Q2 2026 (2026-08-10, 0001692819-26-000019); proxy DEF 14A (2026-03-18,
  0001628280-26-019029); 8-Ks: 2025-10-28 (0001193125-25-253608, Lotus closing), 2026-01-05 (0001193125-26-002589), 2026-07-14
  (0001140361-26-028454, PJM auction), 2026-08-07 with the Q2 2026 earnings release (0001692819-26-000017), 2026-09-24
  (0001140361-26-037577), 2026-10-05 (0001140361-26-038468). Rivals: NRG 10-K FY2025 (0001013871-26-000004) and FY2018
  (0001013871-19-000007); Constellation 10-K FY2025 (0001868275-26-000032); Talen 10-K FY2025 (0001622536-26-000017); and the four
  companies' XBRL company facts (transcription, used for the field table only).
- **One figure cross-checked against the filed statement:** cash provided by operating activities FY2025, $4,070M in `tools/run.py`
  (XBRL) and $4,070M on the filed consolidated statement of cash flows (10-K FY2025); also 2024 $4,563M and 2023 $5,453M, both agree.
  Pre-tax income FY2025 $1,123M (XBRL) agrees with Note 21's "Total consolidated income before income taxes $ 1,123".
- `python tools/run.py VST`, arithmetic lines only (`Test Runs/_research 2026-10-27 VST/run_py_output.txt`): OCF 5,453 / 4,563 / 4,070
  (2023 to 2025); SBC 77 / 100 / 113; capex 1,676 / 2,078 / 2,752; D&A 1,956 / 2,631 / 2,950. The tool's alternate "other capital
  payment" of 1,071 / 1,226 / 1,189 is the **purchases of environmental allowances** line of the investing section (checked against the
  statement); it is a real recurring cost and is charged below, net of allowance sales. The tool's three-year means (2,430 capex
  basis, 2,086 D&A basis) leave out the allowances, the 2021 and 2022 years, and interest and tax treatment; they are not used.
  Its five-year window (1,024 capex basis) is closer to the recast below. SBC is complete in the statement (one line). No
  securities inside operating cash; nuclear decommissioning trust purchases and sales net to about -$23M a year and are charged.
- **Owner cash, recast from the filed cash-flow statements** (`Test Runs/_research 2026-10-27 VST/scripts/q7.py`, output
  `q7_output.txt`; USD millions). All-equity basis: operating cash plus interest paid (net of capitalized) plus income taxes paid,
  less stock pay, all capital spending (capex including nuclear fuel and LTSA prepayments, net environmental allowance purchases,
  net decommissioning-trust investment, less proceeds of asset sales, insurance recoveries of damaged plant and transferable ITC
  sales), less tax at 23% on pre-tax income before interest and before unrealized commodity marks (CONVENTION of this run: 21%
  federal plus about 2% state, the filer's reconciliation showing state at 2.0% to 3.6%; rationale: "Whose tax" asks for the
  statutory rate where carryforwards shelter the company, and the marks reverse), with the 45U nuclear PTC revenue (2024 $545M,
  2025 $220M) taken out and priced separately:

  | year | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|---|---|
  | owner cash, all spending, before interest, after 23% tax | 1,986 | 1,746 | -817 | -568 | 3,344 | 2,059 | 953 |
  | growth spending (MD&A "Growth and development expenditures"; 2025 Note 21 basis) | 104 | 401 | 440 | 475 | 698 | 800 | 648 |
  | equity-only (after interest at 77% and preferred dividends), all spending | 1,591 | 1,374 | -1,168 | -1,144 | 2,732 | 1,185 | -40 |

  Five-year average 2021-2025, all spending: **$994M**; maintenance only (latest-filing growth basis): **$1,418M**. Acquisitions and
  noncontrolling-interest purchases are not in these figures (Q7, specific (c)).

## THE FOUNDATIONS (not a gate)
Two foundations bear here. A share is a business: the test is whether I would be content to own this "if the market closed for five
years" **[M1997-109]**, and for a business whose net income swung from a loss of $1,264M (2021) to a profit of $2,812M (2024) on
the marks of its hedges and the weather, the answer rests on the business's cash over a cycle, not on its quotation. The market
serves, it does not instruct: the stock's rise since 2022 "just tells us prices" **[M2006-077]**; it is no evidence of value. No macro
forecast enters: the filer's own narrative of data-center load growth is a forecast of demand, and "macro conclusions are — just
never enter into the discussion" **[M2000-094]**; it is weighed only as a claim about the business at Q2. Who is paid to tell you:
the filer features "Ongoing Operations Adjusted EBITDA" and its guidance, and its executives are paid on adjusted figures (Q4, Q6).
**Contrary evidence, written down as found** **[M1997-127]**: (i) 2021 owner cash was negative by about $0.8 billion and 2022 by
about $0.6 billion; (ii) the filer's predecessor completed a Chapter 11 reorganization on 2016-10-03 (10-K FY2025 glossary,
"Effective Date"); (iii) $20.7 billion of total indebtedness at 2025-12-31 (Item 1A); (iv) price formation is set by the marginal
unit for all generators (Item 1); (v) total retail customers fell from about 4.5 million (10-K FY2020) to about 3.5 million (10-K
FY2022) before acquisitions restored about 5 million.

## THE STANDING RULE
Owning a part-interest bought with the buyer's own money, unlevered and sized within the buyer's means, puts the buyer at no risk
of ruin: the rule binds the buyer's conduct, "never going to risk what we have and need for what we don’t have and don’t need"
**[M2012-081]**. The target's own exposure to "sudden demands for large sums" **[L2014-024]** (collateral calls) is the target's,
weighed at Q9, not the buyer's.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The business, from the filing.** An integrated retail electricity seller (about 5 million customers, 2.6 million in Texas) and
  merchant generator (43,641 MW: gas 62%, coal 20%, nuclear 15%, solar and batteries 3%), selling into ERCOT, PJM, ISO-NE, NYISO,
  MISO and CAISO (10-K FY2025, Item 1). Generation sells at a market price: "all generators receive the same price for energy based
  on the bid price of the last MWh needed to balance supply and demand" (Item 1). Retail buys from the generation segments
  "at market prices" (Note 21) and sells to households and businesses that can switch.
- **The key variables and how predictable they are** **[M1998-044]**: the wholesale power price and the market heat rate (set by the
  marginal gas unit, and by renewables when they are abundant, Item 1 and Item 7); capacity prices (PJM's auction, under an
  administrative price cap for 2026-2027 and 2027-2028 that PJM proposes to extend, Item 1); fuel costs; extreme weather (Uri); the
  retail margin; and the market rules. None of the price variables is predictable to the speakers: "We don’t think we can predict
  commodity prices." **[M2016-025]**. But the framework's commodity paragraph governs the routing: dependence on a commodity price "is
  never by itself a STOP at Q1 or Q2"; Q1 asks whether the business can be understood from its figures, and the price level enters at
  Q7. The figures can be read: the segments, the hedges, the cash-flow statement and the capital tables are all filed and reconcile.
  The physical business (plants that burn fuel or split uranium, a retail book) does not change fast in its technology; its market
  rules change, and that is a question of the castle (Q2).
- **Test 3, do the past statements tell me the future ones?** They tell me the range of outcomes over a cycle (2019 to 2025 includes
  a scarcity loss, a collateral drain and a boom), which is what Q7 needs; they do not tell me the price path, which no one is asked
  to forecast **[M2008-069]**: "if you can’t make a decision on something like PetroChina off the figures, forget about going further".
- **The doubt, written down** **[M2002-092]**: "if you have doubts about something being into your circle of competence, it isn’t."
  The doubt here is about the ten-year earning power **[M2012-065]**, "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years", which the market rules and the scarcity events make wide. It is a doubt
  about the castle and the value, not about what the business is or how it makes money **[M2011-014]**: "What is important is that I
  understand the economic dynamics of the industry. Is there — are there competitive moats? Is there ease of entry?" Those questions
  can be put to the filings, so the file goes on to Q2, where the commodity paragraph places them.
- **VERDICT: IN**, with the doubt carried to Q2 and Q7. Filing fact: 10-K FY2025 Item 1, price formation and fleet; Note 21, segments.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (section B; "lumping them together [...] impedes analysis" **[L2008-005]**). Segment net income, five years
2021-2025, USD millions, from Note 21 of the 10-Ks FY2023 (2021-2022, the segmentation then in force, with a Sunset segment) and
FY2025 (2023-2025); and the same less the unrealized hedge marks each segment carries, from the Adjusted EBITDA reconciliations in
Item 7 of the 10-Ks FY2022, FY2023, FY2024 and FY2025 (the filer: the generation segments and Retail carry opposite marks on the
same forward contracts, so the marks move profit between parts without cash). Arithmetic in `Test Runs/_research 2026-10-27 VST/NOTES.md`.

| part | 5-yr net income as filed | share | 5-yr net income less unrealized hedge marks | share | castle | decides |
|---|---|---|---|---|---|---|
| Retail | 6,284 | 79% | 5,376 | 52% | standing, on thin evidence (below) | **yes** (more than half on both measures) |
| Texas generation | 1,008 | 13% | 3,301 | 32% | open (commodity, below) | no |
| East generation | 1,125 | 14% | 1,890 | 18% | open | no |
| West | 737 | 9% | 655 | 6% | open | no |
| Sunset (2021-2022 only) | -367 | | -56 | | retired | no |
| Asset Closure | -841 | | -788 | | closing | no |
| total of segments | 7,946 | | 10,378 | | | |

Retail decides. The file closes on Retail's castle; the generation parts, which do not decide, are carried to Q7 as ordinary at
no growth (section B). The generation segments together (Texas, East, West) carry more than Retail on the second measure
(5,846 against 5,376); the convention reads reported parts, and the unclear point is recorded at the end.

**Retail's castle, the tests with their filing facts.**
- *What keeps it standing, and how permanent* **[M1995-038]**: "why is that castle still standing? And what’s going to keep it
  standing or cause it not to be standing five, 10, 20 years from now." The filer's answer: the TXU Energy brand, "used to sell
  electricity to customers in the competitive retail electricity market in Texas for over 20 years" (Item 1), customer service,
  and the integrated supply that hedges the retail book with the company's own generation (Item 7, Factors).
- *Unit volume*: Texas customers about 2.4 million (10-K FY2020; again FY2022), 2.5 million (FY2023), 2.6 million (FY2024 and
  FY2025); "our total retail customer counts increased approximately 3%, 3% and 1% in 2022, 2021 and 2020" by meters (10-K FY2022,
  Item 7). Against it: total customers about 4.5 million (FY2020), 3.5 million (FY2022), 4 million (FY2023), 5 million (FY2024,
  after the Energy Harbor retail book was bought); outside Texas the book shrank and was bought back. The two FY2022 statements
  (counts up by meters; headline count down a million) are not reconciled in the filing read; recorded as found **[M1997-127]**.
- *The record through the cycle*: Retail earned a profit in every year of 2021-2025, including the Uri year ($2,196M as filed,
  $793M less marks), when the company as a whole lost $1,264M.
- *The money test and the low bid*: the filer's own words are against the castle: "with retail competition, it is easier for
  residential customers where we serve load to switch" and "We operate in a very competitive retail market where our retail
  operation faces significant competition for customers" (Item 1A). The product is the same electricity over the same wires.
  The rows' failing answer is "most insureds don't care from whom they buy" **[L2004-003]**; the passing answer is customers who
  do not buy on "the low bid" **[M2017-009]**. No retail price data were found in the filings read, so whether TXU holds its
  customers at a premium cannot be shown from them; what is shown is that the Texas book held its size and its margin for five
  years in an open market.
- *Widening or narrowing* **[M1999-108]**: "whether it’s likely to widen further or shrink on you". In Texas, holding to slightly
  widening by count; outside Texas, narrowing then bought.
- *What could destroy it* **[M2000-014]**: "destroy, or modify, or reduce the economic strengths". A scarcity event with the supply
  unhedged: the retail book came through 2021 because the generation side bore the loss (Texas segment -$2,512M as filed).
- *The returns it protects*: not computable from the filing: "A measure of assets is not applicable, as segment assets are not
  regularly reviewed by the CODM" (Note 21, 10-K FY2025). Retail goodwill was $2.461 billion (10-K FY2023, critical estimates).
- **Judged in words** **[M1999-108]**: a standing castle in Texas on five years of evidence (count held, profit in every year
  including the worst one), with the switching risk and the dependence on the company's own supply written against it.

**The generation parts (do not decide), and the field.** A commodity business is judged at Q2 by its cost position (the commodity
paragraph): "we would measure it, probably, more by cost of production than we would by whether copper was selling for $2.00 a
pound or a dollar a pound" **[M2006-004]**. The fleet is a price-taker: all generators "receive the same price for energy based on
the bid price of the last MWh needed" (Item 1), the condition of the business whose price another sets, "whatever he charged for
gas was my price" **[M2012-109]**. The fleet is not the low-cost producer as a whole: nuclear (15%) sits low on the dispatch order,
but coal (20%) is being retired as uneconomic ("We have retired, announced planned retirements of, and may be forced to retire or
idle additional underperforming generation units", Item 1A; impairments of Zimmer 2021, Miami Fort 2022 and Kincaid 2023 for
falling projected margins, 10-K FY2023 Note 22), and subsidized renewables lower the price when abundant (Item 7). "commodity
businesses have risk unless you’re the low-cost producer" **[M1997-010]**.

**The competitor row and the field's returns over the last full cycle.** The 10-K names no rival by name (it lists "regulated
utilities, industrial companies, non-utility generators, competitive subsidiaries of regulated utilities, independent power
producers, REPs, and other energy marketers", Item 1). Chosen by the analyst, three that file with the SEC: NRG Energy (CIK
1013871, integrated retail and generation, Texas and East), Constellation Energy (CIK 1868275, nuclear-led), Talen Energy (CIK
1622536, PJM merchant). Rivals in the filer's categories that do not file as SEC equity registrants (private generators, municipal
and cooperative utilities, private REPs) are flagged and not compared. Metric, the same for all: operating income after a 21%
tax (CONVENTION of this run, the federal rate; rationale: one tax for all so that the comparison is of the businesses) over average
tangible capital (equity plus debt less cash, goodwill and intangibles), from first-filed XBRL annual values (transcription, not
checked line by line against each rival's statements; `Test Runs/_research 2026-10-27 VST/peers_xbrl.txt`,
`Test Runs/_research 2026-10-27 VST/field_returns.txt`):

| company | span | after-tax operating income / tangible capital, span total | worst year | best year | reorganization in the field, from the filings |
|---|---|---|---|---|---|
| Vistra | 2017-2025 | 7.5% | 2021: -9.5% | 2024: 23.5% | predecessor's Chapter 11 completed 2016-10-03 (10-K FY2025, glossary, "Effective Date") |
| NRG | 2015-2025 | 6.8% | 2015: -14.2% | 2024: 45.0% (capital shrunk by buybacks and impairments) | GenOn and subsidiaries filed Chapter 11 on 2017-06-14 (NRG 10-K FY2018) |
| Constellation | 2020-2025 | 7.7% | 2021: -1.8% | 2024: 19.5% | none found in the filing read |
| Talen | 2015, 2022, 2024-2025 (gaps in the tagged data) | 1.3% | 2025: -1.3% | 2022: 5.0% | Chapter 11 May 2022, emerged 2023-05-17 (Talen 10-K FY2025) |

Judged in words, as the convention asks: over the cycle the field's durable players earned ordinary returns on tangible capital,
negative in the scarcity and collateral years and high only in 2023-2025, and the field's history in the filings read includes
three reorganizations. "A truly great business must have an enduring "moat" that protects excellent returns on invested capital"
**[L2007-004]**; the generation parts show no such protection over the cycle. The 2023-2025 improvement (higher realized and
capacity prices; the 20-year AWS and Meta nuclear PPAs signed 2025-2026, delivery from late 2026 to 2034, Item 7) is a change for
the better that has not been through a downturn; it is credited only on a full cycle **[M2017-026]**, **[L1995-022]**. Because the
generation parts do not decide, this is recorded and carried to Q7 (no growth), not boxed.

- **VERDICT: IN** on the deciding part, Retail, whose castle stands on the five-year evidence, judged in words; the generation
  parts are open and are carried to Q7 as ordinary at no growth.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**: "we’re defining it in terms of the capital actually needed in the
  business." After-tax operating income on average tangible capital, 2017-2025 (Q2 table): 7.5% over the span, from -9.5% (2021)
  to 23.5% (2024). That is the return of the whole; Retail's own capital is not reported (Note 21).
- **Reinvestment to stand still** **[L2000-035]**: "Every year we spend amounts equal to our depreciation charge simply to stay in
  the same economic place". The filer's own maintenance figure ("capital expenditures, including nuclear fuel and excluding growth
  expenditures", Note 21, 10-K FY2025): $1,471M (2023), $1,727M (2024), $2,104M (2025), against depreciation and amortization on the
  cash-flow statement of $1,956M, $2,631M and $2,950M (these include nuclear fuel amortization and, in 2025, about $400M written off
  at Moss Landing). Beside the plant, a recurring cash cost of staying in business sits in investing: net purchases of
  environmental allowances of $571M, $453M and $914M. The stand-still cost is therefore about $2.0 to $3.0 billion a year, the same
  order as the whole owner cash (Step 0). The filer's maintenance definition moved between filings: the FY2024 10-K put 2024 growth
  and development spending at $800M, the FY2025 10-K's segment note implies $351M for the same year; the run uses the latest filing
  where it reaches (Q7) and records the change.
- **Reinvestment to grow, and what it earns.** Growth has come chiefly by purchase, paid in cash and debt: Energy Harbor ($3,065M
  cash, 2024), the Vistra Vision minority ($1,748M in 2024, $703M in 2025, $613M due currently at 2026-06-30, plus $180M of
  dividends to the minority in 2024), Lotus ($1,140M cash and about $800M of assumed debt, 2025), and Cogentrix signed ($2.3B cash,
  $1.5B assumed debt, 5,000,000 shares; not closed). Purchases 2021-2025: $6,836M, against five-year owner cash before purchases of
  about $4,970M. What the largest purchase returned cannot be isolated from the filings read: the East segment, which holds the
  Energy Harbor nuclear plants, earned $826M and $922M (less marks) in 2024 and 2025 against $163M in 2023, a rise that also carries
  the PJM capacity-price increase and the nuclear PTC. The test is the speakers': "whether that’s good or bad depends on what we
  earn on that incremental $130 million over time" **[M2001-019]**; on the evidence here the answer is not shown.
- **The grade** **[M1998-081]**: "The second-best business is a business that also gives you more and more money. It takes more
  money, but the rate at which you invest — reinvest — the money to get that growth is a very satisfactory rate." The rows accept a
  capital-heavy business on "decent returns on the incremental sums they invest" **[L2009-012]**; a field return of about 7.5% after
  tax across the cycle, with a stand-still cost near the whole of owner cash, does not show it.
- **WEIGHS AGAINST**: a capital-heavy business whose maintenance and allowance spending consume most of its cash over the cycle, and
  whose growth has been bought at returns the filings do not isolate **[M2012-057]**: "cash-consuming businesses, by their nature,
  are unattractive unless the cash they consume gets to earn a reasonable return." (The "little or no debt" criterion is applied at Q9.)

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, eight to ten years** **[M2025-032]** ("balance sheets over an 8 or 10 year period before I even look at
the income account"). From `tools/run.py`'s ten-year table (first-filed XBRL), checked against the filed balance sheets of the
10-Ks FY2020, FY2023 and FY2025 and the 10-Q of 2026-06-30 (USD millions):

| year-end | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026-06 |
|---|---|---|---|---|---|---|---|---|---|
| stockholders' equity (incl. preferred from 2021) | 7,863 | 7,959 | 8,371 | 8,291 | 4,902 | 5,307 | 5,570 | 5,097 | 5,482 |
| goodwill | 2,068 | 2,553 | 2,583 | 2,583 | 2,583 | 2,583 | 2,807 | 2,810 | 2,810 |
| intangibles | 2,493 | 2,748 | 2,446 | 2,146 | 1,958 | 1,864 | 2,213 | 2,435 | 2,286 |
| debt on the face (long-term, current, short-term) | 11,065 | 10,729 | 9,330 | 10,731 | 12,621 | 14,402 | 16,298 | 18,843 | 19,595 |
| cash | 636 | 300 | 406 | 1,325 | 455 | 3,485 | 1,188 | 785 | 435 |
| trade receivables | 1,087 | 1,365 | 1,279 | 1,397 | 2,059 | 1,674 | 1,982 | 2,323 | 2,293 |
| retained earnings (deficit) | -1,449 | -764 | -399 | -1,964 | -3,643 | -2,613 | -454 | -12 | 1,076 |

What moved and why. Debt doubled from 2020 to mid-2026 (to $19.6 billion on the face, plus $300M of receivables financing and the
$613M forward repurchase obligation) while equity fell from $8.4 billion to $5.5 billion, of which $2.476 billion is preferred stock
issued from 2021 (the $2.0 billion issue of 2021 followed Uri, cash-flow statement FY2021); the common equity is therefore about
$3.0 billion, after treasury stock of $7.6 billion: the buybacks were financed by borrowing. Goodwill and intangibles together
($5.1 billion) exceed the common equity, so tangible common equity is negative. Receivables rose with sales (sales $9.1 billion in
2018, $17.7 billion in 2025), about 12% to 13% of sales throughout: nothing out of line. Cash is thin except at 2023, when margin
deposits came back. The deficit closed only in 2025-2026. Prepaid expense and other current assets rose from $205M (2020) to $654M
(2025) and $832M (2026-06), from about 1.8% to 3.7% of sales; the filings read do not break it down, and it is recorded as found
**[M1995-064]**: "if some prepaid expense, deferred asset accounts start building up suspiciously high [...] you want to look twice".
Off the debt line but real: asset retirement obligations of $4.2 billion (nuclear decommissioning and coal closure), set against
investments of $5.3 billion that are mostly decommissioning trusts; derivative assets of $3.7 billion and liabilities of $4.9
billion (current, 2026-06). What the figures cannot say **[M2025-032]**: what the hedge book is worth in the next scarcity event, and
how much collateral it will then demand.

**The real costs.** Depreciation is real **[L2015-004]**, and here the stand-still spending is close to it (Q3). Stock pay is small
($113M in 2025) and is charged. The recurring "one-time": Winter Storm Uri (2021), Winter Storm Elliott (2022), the Martin Lake fire
(2024, about $384M to restore), the Moss Landing fires (2025, about $400M written off and a $155M impairment), and the Asset Closure
segment's losses in every year (-$841M over five years as filed); the filer's featured "Ongoing Operations" figures exclude Asset
Closure, a cost that recurs. The environmental allowances are a recurring cash cost in investing (Q3).

**EBITDA in the filer's own mouth.** The chief operating decision maker "primarily focuses on Adjusted EBITDA" (Note 21); the Q2 2026
release (8-K 2026-08-07) leads its highlights after GAAP net income with "Ongoing Operations Adjusted EBITDA", reaffirms guidance
ranges for 2026 Adjusted EBITDA ($6.8 to $7.6 billion) and "Adjusted FCFbG" ($3.925 to $4.725 billion), and states a 2027 midpoint
opportunity range. The rows: "The one figure we regard as utter nonsense is the so-called EBITDA." **[M1998-086]**; guidance is "the
scourge of earnings "guidance"" **[L2019-006]**; an adjusted figure featured to wave away real costs "makes us nervous" **[L2016-006]**.
In the filer's favour: the release states GAAP net income first, with the unrealized hedge loss named beside it, and the 10-K
explains the opposite marks between segments in plain words; "If you find a management that doesn’t care about the accounting but
does explain to you in clear terms what’s going on, I think you should regard that as a plus" **[M1994-018]**. The featured
"free cash flow before growth" differs from the owner cash of Step 0 mainly by what it leaves out (allowances, collateral swings,
growth spending, acquisitions); the run uses its own recast.

**Confusion or suspicion?** The accounts are long but they reconcile: net income, the marks, the segment tables and the cash-flow
statement agree with one another, and the owner cash could be recast from them. No confusion that closes the file **[M1995-063]**.
The tells that live in the accounts: the prepaid line (above) and the moving maintenance definition (Q3), both recorded, neither
enough for suspicion on its own.

- **VERDICT on the accounts: WEIGHS AGAINST** (adjusted figures featured, guidance given and reaffirmed, a recurring closure cost
  excluded from the featured figure, the moving maintenance definition, the prepaid line), carried to Q5; not a STOP. The recast
  earnings (Step 0) feed Q7.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**: "how well they run the business [...] You have to have some understanding of the hand they
  were dealt [...] And then the second thing you want to figure out is how well that they treat their owners."
  *Running the business*: the 2021 loss was operational as well as dealt: "supply challenges were among the primary drivers of the
  significant loss experienced in 2021 as a result of Winter Storm Uri" (10-K FY2023, Item 1A); two fires followed (Martin Lake,
  2024; Moss Landing, 2025, with a battery facility written off). Against those: commercial availability of 97% or greater in the
  2026 summer heat (release, 8-K 2026-08-07), S&P's upgrade to investment grade in December 2025 (10-K FY2025, Item 7), and the
  20-year nuclear contracts. No rival's Uri record was read, so the hand dealt cannot be set against the competitors' play.
  *Treatment of owners*: the proxy (DEF 14A 2026-03-18): chief executive James A. Burke's total pay $15,989,188 (2025), $12,236,044
  (2024), $10,453,376 (2023); annual incentive weighted on "Adjusted EBITDA", "Adjusted FCFbG" and total cost; PSUs on "Adjusted
  FCFbG per share" with a relative TSR modifier against the S&P 500; his stock ownership 128 times base salary against a 6 times
  requirement; the chairman's role separate from the chief executive's. Read the proxy for "how they treat themselves versus how
  they treat the shareholders" **[M1994-009]**: pay rose about half in two years, on adjusted figures, while owners' per-share
  figures were lifted by debt-funded buybacks; the chief executive's own large holding pulls the other way.
- **The integrity record, as found** (10-K FY2025, litigation note): the Illinois Attorney General's complaint against Illinois Gas &
  Electric, a Crius subsidiary bought in 2019, alleging improper marketing and overcharging, "The vast majority of the conduct in
  question occurred prior to our acquisition"; a grand-jury subpoena to Energy Harbor in July 2020 in the Ohio HB6 investigation,
  before Vistra owned it (2024); the Dorrell antitrust suit (2025) against 28 companies, Vistra and Luminant among them, alleging an
  exchange of nuclear-staff pay information since at least 2003, at the motion stage; the Uri investigations, to which the company responded. Disclosure controls effective (Item 9A,
  FY2025); no restatement found in the filings read. None of these is a finding against the present management.
- **The habits carried from Q4**, read with the record: guidance given and reaffirmed each quarter, adjusted EBITDA featured, pay
  on adjusted figures. The rows' sharper test is the habit of always hitting the number, "we become downright incredulous if they
  consistently reach their declared targets" **[L2002-041]**; the guidance record across years was not read, and 2021 missed it by
  the Uri loss, so the habit of always hitting is not shown. "things that they do in public in relation to their investors and the
  promises they make" **[M2004-067]**: the promises here are dated ranges with their GAAP reconciliation, not a stock price posted in
  the lobby.
- Doubt closes the file, "If you’ve got doubts, forget it." **[M2013-088]**. On the record read, the doubts are about judgment and
  emphasis (adjusted figures, pay), not about honesty: the accounts reconcile, the GAAP figure comes first, and the allegations are
  of other owners' conduct or are industry-wide and unproven. "trustworthiness is more important than the brains" **[M2015-047]**;
  nothing read shows a want of it.
- **VERDICT on integrity: IN.** Ability **WEIGHS AGAINST**, narrowly: the operational losses of 2021, 2024 and 2025 against the
  recovery and the contracts since.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- *Retention.* Over 2021-2025 the company kept nothing net: net income summed to $2,774M (cash-flow statements) while it paid
  $5,959M for its own shares, $1,516M of common dividends and $666M of preferred dividends; debt on the face rose from $9.3 billion
  (2020) to $18.8 billion (2025). The retention test **[R1995-009]**, "whether retention, over time, delivers shareholders at least
  $1 of market value for each $1 retained", has nothing retained to test; the question is the reverse one, whether the cash paid
  out and borrowed was spent below value.
- *Buybacks.* About $6.5 billion since November 2021 and about 30% of the shares retired (release, 8-K 2026-08-07); "~$1.2 billion
  of the share repurchase authorization remained available, which we expect to complete no later than year-end 2027": a sum and a
  date, no price. The rows: value is "entirely purchase-price dependent" and announcements "almost never refer to a price above which
  repurchases will be eschewed" **[L2016-002]**. Prices paid: in 2025, 6.6 million shares for about $1.0 billion (10-K FY2025, Item 7),
  about $150 a share. **Against the bottom of the Q7 range** (written back from Q7, committed with it): the no-growth value is $26.02 a
  share on the central case and -$5.82 on the literal window with all spending (all-equity basis), so the prices paid sit far above
  the bottom of the range, and the no-stated-price programme **weighs against**. The first condition is not met either: the funds
  were not "beyond the near-term needs of the business" but borrowed, and the stock was not "below its intrinsic value,
  conservatively-calculated" **[L1999-023]** on this run's figures.
- *Deals: value given against value got* **[M1995-001]**: "Only if we receive less in value than we give. That’s the key to it."
  Energy Harbor and Lotus were paid in cash and assumed debt; Cogentrix, signed and not closed, is $2.3 billion of cash, $1.5 billion
  of assumed debt and 5,000,000 shares "at a mutually agreed-upon value of $185 per share" (10-K FY2025, Item 7): by the larger part
  an acquisition, not a merger. The one STOP of Part A, an all-stock deal in undervalued stock **[L2009-019]**, is not engaged: the
  deal is not all-stock, and on this run's Q7 the shares given are valued well below $185, not above. What the purchases returned is
  not shown in the filings read (Q3); the programme of buying, $6.8 billion in five years against owner cash before purchases of
  about $5.0 billion, weighs against as a use of the money **[L2011-003]**: "what is smart at one price is dumb at another."
- **Part A WEIGHS AGAINST**: debt-funded buybacks at prices far above the Q7 range, with no stated price, and a serial programme of
  purchases whose returns are not shown.

**Part B: the pay, the board, the owners.**
- Pay tied to what the person controls **[M2003-019]**: "tying performance to what is actually under the reasonable control of the
  person that’s being measured." The annual plan pays on adjusted EBITDA, adjusted free cash flow before growth and total cost; the
  PSUs pay on adjusted free cash flow before growth *per share*, a figure raised by buying shares with borrowed money, and are moved
  up to 25% either way by relative total shareholder return, a stock-price figure outside the executive's control; the rows shun
  arrangements "whose ultimate value [...] is totally out of the control of the person whose behavior we would like to affect"
  **[L1996-018]**. In the owners' favour: the chief executive's holding of 128 times salary, payouts capped at target if absolute
  TSR is negative, and a chairman separate from the chief executive (proxy).
- **Part B WEIGHS AGAINST**, narrowly.

## Q7: WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon: value is "the discounted value of the cash that can be taken out of a business during its
remaining life" **[R1996-018]**, at the long government rate **[L2000-021]**, 5.31% (Step 0). Computation in
`Test Runs/_research 2026-10-27 VST/scripts/q7.py`, output `Test Runs/_research 2026-10-27 VST/q7_output.txt`.

**The base, by the specifics.**
- *(a) Cycles.* The window's first year is aberrational on the filer's own description ("supply challenges were among the primary
  drivers of the significant loss experienced in 2021 as a result of Winter Storm Uri", 10-K FY2023, Item 1A; owner cash -$817M) and
  so is 2022 (-$568M, the collateral drain: margin deposits -$1,874M). The base is the last full cycle, peak to peak in owner cash:
  2019 ($1,986M) to 2023 ($3,344M), averaged over 2019-2023 **[L2005-003]**. The literal window 2021-2025 is shown beside.
- *(b) Decline and growth.* The window's series changes sign, and between its halves (2021-2022 average -$693M; 2024-2025 average
  $1,506M) it changes sign again: the growth rate is meaningless. Growth between successive cycles cannot be measured: the company
  in its present form dates from the 2018 Dynegy merger, and the filings read hold one full cycle. **The range is therefore the
  no-growth case alone, said so.**
- *(c) Acquisitions.* Purchases 2021-2025, $6,836M (Energy Harbor, the Vistra Vision minority with its dividends, Lotus), exceed half
  of owner cash before purchases ($4,970M): the serial-acquirer convention makes the organic pair central, purchases left out and
  organic growth as the filer reports it. The filer reports no organic growth figure, so none is credited; the no-growth case
  stands. Beside it, the default pair: purchases deducted (window average $1,367M a year) with total growth credited (none
  measurable): the literal base becomes negative. Cogentrix, signed and not closed by the price date, is valued beside: no earnings
  of it are filed, so it is credited at nothing, and its financing ($2.3 billion cash, $1.5 billion assumed debt) is added to net
  debt and its 5,000,000 shares to the count.
- *(d) Working capital* is inside operating cash: margin deposits net -$902M over the window, trade receivables -$1,636M.
- *(e) Growth spending.* The filing allows the maintenance guess (the filer's growth and development spending, Step 0 table), so the
  central case is owner cash after maintenance only; the all-spending case is beside. In the no-growth case no growth spending is
  charged: **growth spending $0 in year one, $0 in year ten**.
- *(f) The cap* is not engaged: no growth is carried.
- *Whose tax.* Owner cash is after a 23% tax on pre-tax income before interest and marks (Step 0), the statutory rate the
  convention asks for where carryforwards shelter the company: federal NOLs of $3.8 billion "will begin to expire in 2031" (10-K
  FY2025, income taxes), and the 45U nuclear PTC runs 2024-2032. Both shelters are priced separately at the long rate: the PTC at its
  window average of $153M a year for 2026-2032, the NOL deferred tax asset of $1,078M over about three years: $1,873M together.
- *On what the floor is earned.* Merchant generation and retail, priced by a market: the all-equity basis is central (the regulated
  utility paragraph keeps "Merchant generation and unregulated renewables, priced by a market" on it). Net debt at the latest filed
  date, 2026-06-30 (10-Q): long-term debt $17,719M, current portion $1,876M, receivables financing $300M, forward repurchase
  obligation $613M, less cash $435M: **$20,073M**; preferred stock $2,476M added (CONVENTION of this run: preferred counted with net
  debt; rationale: its $192M a year is paid ahead of the common out of owner cash struck before interest): **$22,549M**. Left out
  and said so: operating leases; restricted cash; the $438M margin-deposit financing with an affiliate, matched by $438M of deposits
  posted under it; asset retirement obligations, set against the decommissioning trusts. The junior subordinated notes of 2026-09-24
  ($1.5 billion) came after the 10-Q and are not stated in it; they raise cash and debt alike until spent. Enterprise value at the
  price: $47,570M + $22,549M = **$70,119M**.

**The values (no growth, perpetual, all-equity unless said; per share on 335.635M shares).**

| case | owner cash a year | value per share at 5.31% | value per share at 10% | owner cash yield at the price |
|---|---|---|---|---|
| **central**: cycle 2019-2023, maintenance only | $1,562M | **$26.02** | -$15.65 | 2.23% |
| literal window 2021-2025, maintenance only | $1,418M | $17.95 | -$19.94 | 2.02% |
| literal window 2021-2025, all spending | $994M | -$5.82 | -$32.56 | 1.42% |
| cycle 2019-2023, all spending | $1,138M | $2.25 | -$28.27 | 1.62% |
| beside: central with Cogentrix as if closed (credited at nothing) | $1,562M | $14.48 | | |
| for information only, not a case: 2023-2025, maintenance only | $2,520M | $79.78 | $12.90 | 3.59% |
| equity-only, central (after interest and preferred) | $1,101M | $67.34 | $37.80 | 2.31% |
| equity-only, literal window, all spending | $313M | $23.15 | $14.33 | 0.66% |

**The floor, tested first** **[M2003-149]**: "we don’t want to buy equities where our real expectancy is below 10 percent." At
$141.73, no case earns it: the central case yields 2.23% before any growth; the best three years of the record, taken alone, yield
3.59%. For the central base to earn 10% at the price, owner cash would have to grow about 21% a year for ten years, to about $10.6
billion, with no growth spending charged for it; the record shows no growth rate at all. The price sits far above the top of the
range, which "closes OUT however wide the range, by the floor convention". The width test is not reached. Nor would a close case
pass: "It should scream at you." **[M2009-005]**.

- **Value range:** the no-growth case alone, **$26.02 a share** on the central case (literal window beside: $17.95 maintenance
  only, -$5.82 all spending), against **$141.73**. **Closes OUT**: no case earns the floor at the price.
- **Fair price (a reporting figure, never a verdict; Part VII):** the range being one case, the fair price is that case valued at
  ten percent: **-$15.65 a share on the all-equity basis (not positive)**, after the company's own tax at the statutory rate with the
  shelters added; **equity-only beside: $37.80**. No cheap price is reported. Growth spending $0 in year one and year ten (no growth
  case). Utility debt credit: not applicable (not a regulated utility).
- **VERDICT: OUT** **[M2003-149]**, at the floor.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT**, decided at **Q7** (the floor): the no-growth value is **$26.02 a share** on the central case (all-equity; literal window
beside $17.95 maintenance only, -$5.82 all spending) against a price of **$141.73**; no case earns about ten percent at the price.
Fair price (reporting figure): not positive on the all-equity basis (-$15.65); $37.80 equity-only. Re-look under an alert at the
top of the computed range, like any OUT (Part VII).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.)*
- **Q8, the bond.** The 30-year Treasury at 5.31% (2026-10-26) against an owner cash yield of 2.23% on the central case and 3.59% on
  the best three years (Q7 table).
- **Q9, the debt and the sudden demands.** Total indebtedness about $20.7 billion and about $19.9 billion net of cash at 2025-12-31
  (10-K FY2025, Item 1A); on the face at 2026-06-30, $19,595M of debt plus $300M of receivables financing and $613M of forward
  repurchase obligation, against $435M of cash (10-Q); $1.5 billion of junior subordinated notes added 2026-09-24 (8-K). Collateral:
  margin deposits drained $1,000M (2021) and $1,874M (2022) and returned $1,899M (2023) (cash-flow statements); the 10-K's own words,
  "increased collateral posting requirements" in Uri (10-K FY2023, Item 1A), and a downgrade "could trigger liquidity demands
  pursuant to contractual arrangements" (10-K FY2025, Item 1A). A commodity-linked revolving facility whose borrowing base moves with
  prices ($1.75 billion limit; amended 2026-09-30, 8-K 2026-10-05). Liquidity $6,295M at 2026-06-30 (release). S&P BBB- since
  December 2025. Asset retirement obligations $4.2 billion. Nuclear operations (six units) and their accident risk (Item 1A). The
  "little or no debt" criterion, stated for a whole business, is not met on these facts.
- **Q9, aggregation.** One weather event (Uri) produced the 2021 loss across Texas generation; ERCOT relies on "energy-market price
  signals" without a capacity market (Item 1).
- **Q12.** Coal 20% of capacity, with retirements and gas repowering announced (Item 1); no business named in Q12's list.
- No integrity facts beyond those judged at Q5.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit eda4478c); committed after each question (Q1 9e160df8, Q2 d423c561, Q3
      8cabb8db, Q4 ae17ea71, Q5 39c3a9ff, Q6 and Q7 together f6f0ff37, as the brief asks for Q6's buyback line). **Departure from
      write-early, confessed:** most of the filing research for Q1 to Q7 (cash flows, segments, rivals, proxy) was done before the
      Q1 section was written, and each section was then written and committed in order; the sections were not each written as
      their own research closed. The judgments were made in question order, but the evidence for later questions was in view
      when earlier ones were written.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's. The run binds nothing
      until it is folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; the commit subjects seen in the session
      context are declared under Contamination and not used.
- [x] Every v5 id resolves (`Test Runs/_research 2026-10-27 VST/scripts/check_ids.py`: every id in `principle_ledger_v5.csv`,
      every quoted fragment beside an id found in that row, no E-ids); every filing fact carries its document and accession (Step 0
      lists them; the text names the document).
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); sovereign from the Treasury; the price is an
      aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations; Q2's customer counts; Q4's prepaid line); facts for later questions
      under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its three-year means were not used and the reason is given in Step 0.
- [x] `python tools/check_framework.py` PASS before the final commit (run 2026-10-27: "PASS — every number resolves to a
      verbatim source or a confessed convention"); the run's own id check: 57 distinct ids, 62 citations, 0 problems.
- Conventions of this run, confessed: the 23% tax (21% federal plus about 2% state) on owner cash; the 21% tax in the field table;
  preferred stock counted with net debt; the cycle base set peak to peak in owner cash, 2019-2023. Figures not obtained: Retail's
  own capital (not reported); retail prices against rivals; the rivals' figures beyond tagged XBRL (not checked line by line); the
  guidance record across years; income taxes paid for 2021 and 2022 (taken as nil; the effect is small against the totals).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The business of parts, applied to a vertically integrated company.** Q2's convention reads reported segments, but here the
Retail segment buys from the generation segments "at market prices" and the two carry opposite hedge marks on the same contracts,
so the split of profit between them is an internal transfer price, and the marks alone moved Retail's five-year share from 52% to
79%. Retail decided on both measures, but the three generation segments together out-earned it on the measure less marks; the text
does not say whether segments that share one fleet and one hedge book should be read as one part. The run applied it as written.
(2) **A range of one case.** Where growth is meaningless the range "is the no-growth case alone", but the fair price is defined as the
average of two end cases; the run valued the one case at ten percent, and reported the template's growth-spending line as $0. (3)
**Preferred stock** is not named in the net-debt definition (borrowings and finance leases); the run counted it with net debt and
confessed the convention. (4) **A credit taken as revenue.** "Whose tax" prices carryforwards and credits "that run out inside ten
years", which reads as income-tax credits; the 45U nuclear PTC is recognized as revenue and runs to 2032; the run took it out of the
base and priced it beside, and the text does not say whether that is required. (5) **A maintenance figure that moves between
filings.** The FY2024 10-K put 2024 growth spending at $800M and the FY2025 10-K implies $351M for the same year; specific (e) does
not say which filing governs; the run used the latest filing where it reaches and the older series before it. (6) **No rivals
named.** The brief asks for the rivals the 10-K names; this 10-K names only categories, so the run chose three and said so.
