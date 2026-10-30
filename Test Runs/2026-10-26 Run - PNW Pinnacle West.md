# Company Run — Pinnacle West Capital Corporation (NYSE: PNW) — 2026-10-26
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run. The brief departs from the canonical brief in one stated way only: the repository path is
C:\Projects\BRK (moved 2026-10-25). Template copied before any fetch (commit 8fb67eb5). Working folder:
`Test Runs/_research 2026-10-26 PNW/` (notes, fetch and arithmetic scripts, the run.py output, the peer table, the Q7 script
and its output; raw filings are cached under its ignored `cache/`).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-26: the operator does not hold this name (`PORTFOLIO.md` has no PNW row).*

**Contamination, declared.** (1) `CLAUDE.md`, loaded automatically, names `Screens/RESUME STATE 2026-09-12 ...` and
`Screens/WATCHLIST RUN QUEUE.md` by file name and describes `PORTFOLIO.md`; none was opened. (2) The first `git status`
of the run printed one path belonging to another analyst's research folder, `Test Runs/_research 2026-09-27 ARCB/_logmsg_dispatch.txt`
(a file name only, another company). (3) `CLAUDE.md` also says that a Berkshire Hathaway Energy subsidiary is PNW's 50/50
partner in TransCanyon; that fact is in PNW's own 10-K and is used only as a filing fact. Nothing seen was used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $105.88 (close 2026-10-23, the last close printed by `tools/run.py`; **aggregator, live quote only, flagged**
  per operator rule 5).
- **Shares by class:** one class of common stock. 121,197,234 shares outstanding at 2026-07-28 (cover of the 10-Q for the
  quarter to 2026-06-30, filed 2026-08-04, accession `0000764622-26-000041`). `python Screens/cover_shares.py PNW` printed
  a second line of 71,264,947 shares: that is Arizona Public Service's common stock, all held by Pinnacle West (combined
  filing), not a PNW class, and is not added. **Check against issued less treasury:** 121,238,487 issued less 46,968
  treasury = 121,191,519 at 2026-06-30 (10-Q balance sheet), within 6,000 shares of the cover count (stock pay).
  **Check against later filings:** none of the 8-Ks filed after the 10-Q (2026-08-04 Item 1.01, `0001104659-26-090108`;
  2026-08-07, 2026-09-04, 2026-09-30, investor handouts) reports a settlement. **Forward equity not yet issued:** 4,426,350
  shares left on the February 2024 forward (about $62.8 a share), 8,306,132 shares on thirteen ATM forwards at a weighted
  $97.38 (10-Q Note 13), and one more ATM forward of $84 million gross effective 2026-07-06 (about 0.8 million shares at
  about $103): about **13.55 million shares for about $1,171 million**, roughly 11% more shares. A new $500 million ATM with
  forward option was opened 2026-08-04 (8-K above; prospectus `0001104659-26-090107`). The $525 million 4.75% convertible
  notes due June 2027 convert at about $92.30 (10.8338 shares per $1,000; the excess over principal may be paid in shares).
- **Market cap:** 121.197M x $105.88 = **$12,832M** (on the cover count; the forward shares are shown beside in Q7).
- **Sovereign for the earnings currency:** **5.33%**, US Treasury daily par yield curve, 30-year, 2026-10-23
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-25, `0000764622-26-000011` (MD&A, Notes 1, 5, 7, 8, 9,
  14, 16 in the parts cited, the statements); 10-Q for Q2 2026, filed 2026-08-04, `0000764622-26-000041` (MD&A regulatory
  section, balance sheet, cash flows, Note 13); proxy DEF 14A filed 2026-04-03, `0001628280-26-023516`; 8-K 2026-08-04
  earnings release exhibit 99.1, `0000764622-26-000040`; 8-K 2026-08-04 Item 1.01 (ATM); 424B5 2026-06-02
  `0001104659-26-069513` (a $500 million note issue); the cycle filings: 10-K FY2017 `0000764622-18-000018`, FY2019
  `0000764622-20-000017`, FY2021 `0000764622-22-000014`, FY2023 `0000764622-24-000016`, FY2024 `0000764622-25-000023`.
  FY2016 to FY2022 statement lines were taken from the XBRL facts of each year's own 10-K (accessions in the peer table).
  **One figure cross-checked against the filed statement:** net cash from operating activities FY2025, $1,805,095 thousand on
  the filed cash-flow statement (10-K `0000764622-26-000011`, page 95) against $1,805M printed by `tools/run.py`: agrees.
- `python tools/run.py PNW`, arithmetic lines only (output saved as `_research 2026-10-26 PNW/run_py_output.txt`): owner
  cash after all capital spending (its "OE capex") 2023 -656, 2024 -663, 2025 -847 ($M); on depreciation 336, 630, 808.
  **Two defects found in its lines and corrected from the filing.** (a) Its capital spending is gross: it omits the
  contributions in aid of construction that customers paid in ($181M, $311M, $306M in 2023 to 2025), the borrowed AFUDC shown
  in investing, the Palo Verde lease buy-in ($199M, 2025, a financing line) and the payments to the Palo Verde lessors (the
  minority partners, $18M to $21M a year). The run's own owner-cash table in Q4 uses the whole investing total and those
  lines. (b) Its debt table double-counts 2023: it tags $875M under both LongTermDebtCurrent and OtherLongTermDebtCurrent
  and sums $9,900M; the filed figure is $7,541M long-term plus $875M current plus $610M short-term. As the brief warned, every
  debt figure in this run is taken from the balance sheets, not from that table. SBC is resolved (stock compensation $17M to
  $27M a year, deducted).

## THE FOUNDATIONS (not a gate)
Two foundations bear on this name. *A share is a business* **[M1997-109]**: PNW is a regulated monopoly whose cash comes from
what the Arizona Corporation Commission (ACC) lets it earn on what it spends, so the question is the cash the owner keeps
after the spending, not the dividend. *Margin of safety* **[M1996-084]**: a regulated return set near the cost of equity
leaves little room for a price that screams. *Who is paid to tell you* **[M2011-083]**: the company publishes an EPS outlook
each year and every rate case asks for far more than it gets; neither is evidence of value. **Contrary evidence, written down
as found** **[M1997-127]**: (1) owner cash after all capital spending was negative in nine of the last ten years (Q4 table);
the dividend has been paid out of new debt and new shares; (2) the 2021 rate order cut the allowed return on equity to 8.70%
against 10.15% asked, with a $215.5M disallowance, later reversed in part by the courts; (3) the company spent in the 2014
ACC elections that chose its own regulators, a matter that drew federal grand jury subpoenas (closed) and four years of
subpoena fights with a commissioner; (4) the share count will rise about 11% on forwards already signed, at prices below
today's; (5) net income grew about 4% a year over 2016 to 2025 while common equity grew about 4.3% and debt about 10%: the
growth is bought, not earned.

## THE STANDING RULE
A purchase in cash of a listed share, unlevered and sized by the buyer, puts the buyer at no risk of ruin from the target
**[M2012-081]**, **[L2023-005]**; the target's own debt is Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it** **[M2000-037]**, **[M2012-065]**: a reasonable fix on earning power and competitive
  position in ten years. PNW "derive[s] essentially all of our revenues and earnings from our principal subsidiary, APS"
  (10-K FY2025, MD&A overview, `0000764622-26-000011`); retail electric revenue was 95% of operating revenue in 2025. APS is
  the vertically integrated monopoly supplier to about 1.4 million retail customers in 11 of Arizona's 15 counties, operator
  and 29.1% owner of Palo Verde, 63% owner of Four Corners Units 4 and 5.
- **Key variables** **[M1998-044]**: (1) rate base growth (original-cost rate base $8.87B asked in the 2019 case, $10.5B in
  the 2022 case, $12.5B in the 2025 case: about 6% a year); (2) the allowed return on equity and equity layer, and the lag
  before spending enters rates; (3) customer and load growth (customers +2.2% a year 2023 to 2025; weather-normalized sales
  +3.9% a year; the company projects +5% to +7% a year through 2030, of which data centers and large manufacturers are 4 to
  6 points); (4) Palo Verde's licence and operation (renewal of all three units to the mid-2060s announced March 2026, 10-Q);
  (5) the ACC's composition and climate. Each is read from the filings, and the insiders write the forecast down: a 15-year
  Integrated Resource Plan every three years, a three-year capital plan ($2.60B, $2.65B, $2.70B for 2026 to 2028), a sales
  forecast through 2030 **[M2000-105]**.
- **Do the past statements tell the future ones?** **[M2008-033]** Largely yes: the business is a return on a growing
  regulated asset base, with weather and the regulator as the swing factors. The variable hardest to foresee is political (an
  elected five-member commission), but it is knowable in kind from the record of four rate orders over the cycle, and it is
  read at Q2 and Q3 as a property of the castle, not as a macro forecast **[M2006-076]**.
- **Routing:** not a fast-changing industry in the Q1 sense **[M1998-008]**; distributed solar and storage are read at Q2.
- **VERDICT: IN** **[M1995-051]**. The economics ten years out (a larger rate base earning a regulated return, financed by
  debt and new shares) can be pictured from the filings.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question **[M1995-038]**: why is the castle still standing, and what keeps it standing "five, 10, 20 years from now".
- **The attacker with money** **[M2011-015]**: no rival can string a second set of wires to APS's 1.4 million customers; the
  service territory is granted by the state, and the capital plan alone is $2.6B to $2.7B a year. On this test the castle
  stands. The attackers that exist are of other kinds: rooftop solar (the export price paid to rooftop customers has been cut
  10% a year, 2023 to 2025, to $0.06171 per kWh; 10-K Note 8), large customers seeking other supply, and the regulator.
- **Pricing power and the agony before a rise** **[M2005-020]**: APS cannot raise a price; it asks, and is granted part.
  Every case in the cycle, from the filings (ask against grant):

  | case | filed | asked | granted | order |
  |---|---|---|---|---|
  | 2016 | 2016-06-01 | +$165.9M base | +$94.6M; ROE 10.0% on 55.8% equity (settlement) | 2017-08-15/18 (10-K FY2017 `0000764622-18-000018`) |
  | 2019 | 2019-10-31 | +$184M total (+$69M net); ROE 10.15% on 54.7% equity | -$4.8M a year; ROE 8.70% (9.16% recommended, then a 20 bp penalty); $215.5M Four Corners SCR disallowed | 2021-11-02 (10-K FY2021 `0000764622-22-000014`) |
  | 2019, after appeal | | | Court of Appeals vacated the SCR disallowance 2023-03-06; joint resolution restored ROE to 8.9% and $215.5M, plus $59.6M lost revenue by surcharge | 2023-06-21 (10-K FY2023 `0000764622-24-000016`) |
  | 2022 | 2022-10-28 | +$460M net; ROE 10.25% on 51.93% equity | +$491.7M base revenue requirement (after adjustor transfers); ROE 9.55% | 2024-02-22, final 2024-03-05 (10-K FY2025) |
  | 2025 | 2025-06-13 | +$579.5M net (later +$608.7M); ROE 10.70% on 52.35% equity; formula rate (FRAM) | pending; ACC Staff 9.55% to 9.80%, RUCO 9.00% to 9.20%; hearing closed 2026-07-07; decision expected by year end | 10-Q Q2 2026 `0000764622-26-000041` |

  The agony is the business model: the "price" is a return on capital the regulator sets each three years or so, and it was
  cut by 130 bp in 2021 before courts restored part of it. Rates did rise faster than in the past: the company says average
  residential rates rose 16.2% from 2018 to 2024 against Phoenix CPI of 32.1% (10-K FY2025, MD&A).
- **Unit volume** **[M1999-054]**: customers +2.4% in 2025, +2.2% a year 2023 to 2025; weather-normalized kWh +5.0% in 2025,
  +3.9% a year 2023 to 2025; forecast +5% to +7% a year to 2030 (10-K FY2025). Volume is rising, and the large-load queue
  "far exceed[s] available generation and transmission resource capacity in the Southwest region for the foreseeable future".
- **Low cost, brand, low bid** **[L2007-004]**, **[M2017-009]**: not the castle here; the customer cannot choose.
- **Widening or narrowing** **[M1999-108]**: the cycle shows both. Narrowing 2019 to 2021 (the 2019 rate review of rate-plan
  complaints, the 2019 disconnection moratorium, the 2021 order at 8.70%); widening 2023 to 2026 (court reversals, 9.55%,
  a December 2024 ACC policy statement allowing formula rates, a December 2024 financing order allowing yearly equity
  infusions, the May 2025 state wildfire law that ties the standard of care to an approved mitigation plan, approved
  2026-05-07). The formula-rate policy is itself under court challenge (Court of Appeals remand 2025-11-21; petitions pending
  at the Arizona Supreme Court), and on 2026-06-16 the Court of Appeals found the 2024 grid access charge on solar customers
  imposed without adequate notice (10-Q).
- **What could destroy, modify or reduce it** **[M2000-014]**: the regulatory compact, which the rows name as the one moat
  that broke for Berkshire's own utilities, "I did not anticipate or even consider the adverse developments in regulatory
  returns" **[L2023-011]**; wildfire (a "catastrophic event can render a single utility insolvent" **[L2005-019]**); Palo
  Verde as a single site holding 29.1% of three units. None of these is shown on the filings to be filling the moat in now.
- **Ask the competitors:** not done (no access); the rival filings below stand in for it.
- **The competitor row** (FY2016 to FY2025, from each filer's XBRL facts of its own 10-Ks; table and accessions in
  `_research 2026-10-26 PNW/peers.md`):

  | company | 10-yr average ROE on average common equity | allowed ROE, last order (FY2025 10-K) | capex / D&A, 10 yrs | sum of OCF less capex, 10 yrs | revenue CAGR |
  |---|---|---|---|---|---|
  | PNW (APS, ACC) | 9.5% (8.1% to 10.7%) | 9.55% (2024) | 2.17x | -$4,216M | 4.8% |
  | IDACORP (Idaho Power) | 9.5% | 9.6% (Dec 2025) | 2.66x | -$772M | 4.1% |
  | Portland General (PGE) | 8.1% | 9.34% (2025) | 1.95x | -$1,885M | 7.1% |
  | Xcel Energy (NSP-MN) | 10.4% | 9.25% on 52.5% equity (2023) | 2.53x | -$17,550M | 3.1% |
  | Tucson Electric Power (ACC, Fortis) | 9.3% | not stated in its 10-K | 2.43x | -$570M | 3.5% |

  Accessions of the FY2025 10-Ks: PNW `0000764622-26-000011`, IDA `0001057877-26-000028`, POR `0001193125-26-052750`, XEL
  `0000072903-26-000009`, TEP `0000100122-26-000006`. PNW earned what its peers earned over the whole span, including TEP
  under the same commission, and never less than 8.1%.
- **The parts table:** one reportable segment, regulated electricity, essentially all operating income (10-K FY2025). The
  other subsidiaries (PNW Power: the TransCanyon joint venture and two wind minority stakes; El Dorado: about $70M of venture
  commitments) are immaterial; Bright Canyon Energy was sold in 2024 ($84M received in 2024, $23M in 2023). **APS decides.**
- **The field's returns over the cycle, in words:** ordinary. The castle protects a return near 9% to 10% on book equity,
  set by the regulator. The framework's Q2 list sends the standing castle that protects only ordinary returns to OUT and
  excepts a regulator-set return, which it carries to Q3 as a second best. The rows behind the exception: "there’s no way we
  get rich on our utility investments. But there’s no way we get poor, either." **[M2009-104]**; "decent returns on the
  incremental sums they invest" **[L2009-012]**; "when you get an allowed return in the electric utility you’re almost
  certain of earning it" **[M2010-037]**. PNW's record bears the last out within about a point, in both directions.
- **VERDICT: IN**, on the regulator's exception **[M2009-104]**, **[L2009-012]**: the castle is legal, it stood through a
  hostile commission and was partly repaired by the courts, and its returns are ordinary by design. The regulatory compact is
  carried to Q3 and Q9 as the thing that could break it **[L2023-011]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital needed** **[M1995-051]**: net income to common on average common equity averaged 9.5% over
  FY2016 to FY2025 (peer table, Q2). On total capital (equity plus all borrowings) it is lower: FY2025 net income $617M plus
  after-tax cash interest of about $292M on about $17.6B of capital, roughly 5%.
- **What the added capital earned** **[M2001-019]**, measured as the rows measure it, on earnings and not on cash **[M2014-086]**
  (three-year averages at each end, from the filed statements, so that no single year sets the result **[L2005-003]**):

  | | FY2016 to 2018 average | FY2023 to 2025 average | added |
  |---|---|---|---|
  | net income to common ($M) | 480 | 576 | +96 |
  | interest paid ($M) | 194 | 353 | +159 (about +119 after tax) |
  | common equity, year end ($M) | 5,011 | 6,659 | +1,648 |
  | total borrowings, year end ($M) | 4,835 | 9,672 | +4,837 |
  | capital employed ($M) | 9,846 | 16,331 | +6,485 |

  The added equity earned about **5.8%** (96 on 1,648), and the added capital about **3.3%** after tax before interest
  (215 on 6,485). End to end, FY2016 to FY2025: net income +$175M on equity +$2,242M, **7.8%**. The company gives the reason
  itself: "the Company will continue to be challenged with regulatory lag" (proxy 2026, CEO letter); $1.65B sat in
  construction work in progress at 2025 year end, and the 2017 tax law and the 2021 order cut rates while the base grew. A
  decision on the 2025 case (asked +$608.7M of revenue) would lift the end figure; it is pending and is not credited here.
- **Reinvestment to stand still and to grow** **[L2000-035]**, **[L1999-024]**: capital spending was 2.17 times depreciation
  over the decade, and owner cash after all of it was negative in nine of ten years (Q4 table). The spending is compulsory
  in the rows' sense: "Securing a reliable grid requires ongoing infrastructure investments in addition to investments to
  support new customer growth" (10-K FY2025, MD&A), an obligation to serve that the company cannot decline. Inflation adds to
  it: "To earn more, their owners must invest more." **[L2011-019]**. Customers' contributions in aid of construction have
  grown ($64M in 2016, $306M in 2025) and the 2025 case asks that "growth pays for growth"; that offsets part of the bill.
- **The growth arithmetic** **[M1998-081]**: the rows grade three businesses. PNW is not the first (it gives back no free
  cash). It is the second, "It takes more money", only if "the rate at which you invest — reinvest — the money to get that
  growth is a very satisfactory rate" **[M1998-081]**; on the filed record the added capital earned 3% to 8% depending on the
  measure, below the 9.55% allowed, while the business is "forced to grow to stay in the game at all" **[M1998-081]**. The
  rows also say the utility's capital is "capital-intensive businesses that are good businesses" and "the second-best
  choice, still a good choice" **[M2018-055]**, "if they earn a decent return on capital" **[M2007-112]**.
- **Caps for Q7:** owner cash cannot grow faster than the rate base and the allowed return let it; sales grew 8.85% a year
  FY2021 to FY2025 (fuel pass-through included), rate base about 6% a year.
- **WEIGHS AGAINST**, narrowly: a regulated second best **[M2018-055]**, **[L2009-012]**, whose added capital over the cycle
  earned less than the regulator allowed and less than the rows' "decent returns on the incremental sums they invest"
  **[L2009-012]** asks, for a reason (lag) the company names. The "little or no debt" test **[R1997-001]** is Q9's.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** **[M2025-032]** ($M, year end; consolidated; equity is common shareholders'
  equity; long-term debt includes current maturities; first-filed XBRL of each 10-K, the 2024 and 2025 columns checked
  against the filed balance sheet in `0000764622-26-000011`; `tools/run.py` debt sums not used, see Step 0):

  | year | total assets | common equity | retained earnings | cash | intangibles | long-term debt incl. current | short-term borrowings | debt / (debt + equity) |
  |---|---|---|---|---|---|---|---|---|
  | 2016 | 16,004 | 4,804 | 2,256 | 9 | 90 | 4,147 | 177 | 47% |
  | 2017 | 17,019 | 5,007 | 2,443 | 14 | 257 | 4,872 | 95 | 50% |
  | 2018 | 17,664 | 5,223 | 2,641 | 6 | 263 | 5,138 | 76 | 50% |
  | 2019 | 18,479 | 5,431 | 2,838 | 10 | 291 | 5,633 | 115 | 51% |
  | 2020 | 20,020 | 5,634 | 3,025 | 60 | 283 | 6,314 | 169 | 54% |
  | 2021 | 22,003 | 5,906 | 3,265 | 10 | 274 | 7,064 | 292 | 55% |
  | 2022 | 22,723 | 6,049 | 3,360 | 5 | 259 | 7,792 | 341 | 57% |
  | 2023 | 24,661 | 6,178 | 3,466 | 5 | 267 | 8,416 | 610 | 59% |
  | 2024 | 26,103 | 6,754 | 3,667 | 4 | 591 | 8,859 | 568 | 58% |
  | 2025 | 30,032 | 7,046 | 3,851 | 7 | 576 | 9,806 | 757 | 60% |
  | 2026-06-30 | 32,577 | 7,035 | 3,842 | 9 | n/r | 10,551 | 819 | 62% |

  **What moved, and why.** Debt rose 2.5 times (from $4.3B to $10.6B with short-term) while equity rose 1.5 times, so the
  borrowed share of capital went from 47% to 60% (62% at June 2026); the covenant ceiling is 65% (10-K FY2025, debt
  provisions: "approximately 60% for Pinnacle West and 50% for APS"), so about ten points of the consolidated leverage sit
  at the holding company, above APS. Retained earnings grew $1.6B over nine years against about $4.9B of net income (FY2017 to FY2025): the rest
  went out as dividends. Equity was topped up by share sales from 2024 ($369M in 2024, $110M in 2025, plus about $1.17B of
  forwards still to settle). Cash is a working balance only. Intangibles are mostly software, amortized (a real cost
  **[L2012-003]**). Two items the table does not show and the filing does: **operating lease liabilities** for battery-storage
  and power contracts rose from $1.6B (2024) to $3.7B (2025) to $5.1B (June 2026), fixed obligations recovered through the
  fuel adjustor and left out of net debt by the framework's rule, said so here and weighed at Q9; and **customer advances**
  rose from $569M to $853M (data-center and large-load prepayments). What the figures cannot say: what the ACC will allow on
  the $12.5B rate base in the pending case, and whether the advances are refundable if loads do not arrive.
- **Owner cash after every real cost** **[L2021-003]**, **[L2015-004]** (equity-only, after interest and the company's own
  tax, as the utility basis requires; $M; script `_research 2026-10-26 PNW/q7.py`): operating cash, less stock pay, less all
  net investing (capital spending net of customer contributions, borrowed AFUDC, decommissioning-trust funding, the BCE sale
  proceeds as a negative purchase), less payments to the Palo Verde lessors (minority partners), less the 2025 Palo Verde
  lease buy-in. Beside it, the maintenance case: depreciation and amortization including nuclear fuel taken as the
  maintenance guess **[M2000-144]**, since "the depreciation charge is not inappropriate in most companies to use as a proxy
  for required capital expenditures" **[M1998-127]** and the filing gives no maintenance figure of its own.

  | year | operating cash | stock pay | net investing | D&A incl. nuclear fuel | owner cash, all spending | owner cash, maintenance only | growth spending | maintenance owner cash / sales |
  |---|---|---|---|---|---|---|---|---|
  | 2016 | 1,023 | 19 | 1,252 | 565 | -271 | 416 | 687 | 11.9% |
  | 2017 | 1,118 | 21 | 1,429 | 611 | -355 | 463 | 818 | 13.0% |
  | 2018 | 1,277 | 20 | 1,193 | 651 | 41 | 583 | 542 | 15.8% |
  | 2019 | 957 | 18 | 1,131 | 664 | -215 | 252 | 467 | 7.3% |
  | 2020 | 966 | 18 | 1,278 | 686 | -353 | 239 | 592 | 6.7% |
  | 2021 | 860 | 18 | 1,387 | 719 | -566 | 102 | 668 | 2.7% |
  | 2022 | 1,241 | 16 | 1,618 | 818 | -414 | 386 | 800 | 8.9% |
  | 2023 | 1,208 | 17 | 1,694 | 854 | -524 | 316 | 840 | 6.7% |
  | 2024 | 1,610 | 24 | 1,934 | 956 | -369 | 609 | 978 | 11.9% |
  | 2025 | 1,805 | 27 | 2,379 (+199 buy-in) | 970 | -818 | 790 | 1,608 | 14.8% |
  | **avg 2021-25** | | | | | **-538** | **441** | **979** | |

  Lessor payments ($18M to $23M a year) are deducted in both owner-cash columns. Reported net income to common over the
  same five years averaged $566M, so the maintenance-case owner cash ($441M) runs about a fifth below it: AFUDC equity
  income ($39M to $61M a year) is non-cash, and working capital, chiefly fuel and purchased power deferred under the power
  supply adjustor, absorbed cash in 2021 to 2023 (operating cash $860M in 2021).
- **The real costs.** Depreciation is real and short of what is spent **[L2015-004]**: capital spending ran 2.17 times it.
  Stock pay is deducted. Pensions: projected obligation $2.8B, pension plans $180M underfunded and retiree-medical plans
  $399M overfunded at 2025 year end; no contribution required for three years; the $723M pension regulatory asset is
  recovered in rates. The rows warn that pension accounting is "The real lollapalooza" **[M2003-110]**; here the net position
  is about level, and the non-service pension credit added $12M to $49M a year to pre-tax income, which owner cash does not
  count. Deferred taxes ($2.5B) are not treated as equity **[M2015-030]**. Restructuring charges: none recurring found. No
  EBITDA in the company's mouth in the documents read.
- **What the accounts say of management.** The results are reported in GAAP, with no adjusted figure featured in the
  Q2 2026 release (`0000764622-26-000040`, exhibit 99.1). An annual EPS outlook is published: "For 2026, the Company
  continues to estimate its consolidated earnings will be within a range of $4.55 to $4.75 per diluted share on a
  weather-normalized basis." That is earnings guidance, which weighs against here and is carried to Q5 **[L2019-006]**,
  **[M1994-018]**. Regulatory accounting (deferrals, regulatory assets of $1.75B and liabilities of $1.95B) is explained
  item by item in Note 8 and was readable; nothing confused, and no tell from the list in the accounts **[M1995-064]**.
- **VERDICT on the accounts: WEIGHS AGAINST** **[M1994-018]**: no confusion and no suspicion **[M1995-063]**, **[M1995-065]**;
  against, the guidance habit (carried to Q5) and a recast that shows owner cash after all spending negative in nine of ten
  years, the dividend paid with borrowed and newly issued money. The recast feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**The integrity record, from the filings, in date order** (each a filing fact, not a press report):
1. **The 2014 ACC elections.** "Pinnacle West previously received grand jury subpoenas issued in connection with an
   investigation by the office of the United States Attorney for the District of Arizona. The subpoenas sought information
   principally pertaining to the 2014 statewide election races in Arizona for Secretary of State and for positions on the
   ACC. The subpoenas requested records involving certain Pinnacle West officers and employees, including the Company's
   former Chief Executive Officer, as well as communications between Pinnacle West personnel and a former ACC
   Commissioner. Pinnacle West understands the matter is closed." (10-K FY2019, `0000764622-20-000017`, Other Information).
   No charge is recorded in any filing read.
2. **Resisting disclosure, 2016 to 2020.** A sitting commissioner subpoenaed records of "political contributions" and
   payments to "501(c)(3) and (c)(4) nonprofits" for 2011 to 2016; APS and Pinnacle West moved to quash and sued for a
   declaratory judgment that the subpoenas were "contrary to law"; the matter ran from September 2016 to March 2020
   (10-K FY2017 `0000764622-18-000018`; 10-K FY2021 `0000764622-22-000014`). The same commissioner sought to vacate the
   2017 rate order for "alleged issues of disqualification and bias on the part of the other Commissioners"; the Arizona
   Supreme Court declined jurisdiction (10-K FY2017).
3. **2019.** Two further commission dockets "to investigate campaign expenditures and political participation of APS and
   Pinnacle West"; the companies responded voluntarily (10-K FY2019). In the same year the commission's rate review of the
   2017 order, opened on complaints that the increase "was much more than anticipated", ordered APS to show each customer
   the bill on "their most economical rate" and to fund education for customers whose bills rose more than 9% and who were
   not on the cheapest plan; and APS suspended disconnections for non-payment, after which the commission made the summer
   moratorium a rule (10-K FY2019).
4. **2021.** The rate order carried a "20 basis point penalty reduction to the return on equity"; it was reversed in the
   2023 joint resolution after the Court of Appeals decision (10-K FY2021, FY2023).
5. **The remedy, and its term.** "Mr. Guldner committed to the ACC that during his tenure, Pinnacle West and APS, and any of
   their affiliated companies, will not participate in ACC campaign elections through financial contributions or in-kind
   contributions." (10-K FY2019). His tenure as chief executive ended on 2025-03-31 (proxy 2026, `0001628280-26-023516`).
   No filing read renews the commitment under the present chief executive. The board's governance committee "Reviews and
   assesses the Company's Political Participation Policy" (proxy 2026). The policy itself is on the company's website, not
   in a filing; read through a summarizing fetch tool (**not a primary-filing read; flagged**), the version "Updated April
   2026" bars "corporate contributions to political candidates for, or office holders in, [...] the Arizona Corporation
   Commission" and was reported to say nothing about independent expenditures, or payments to groups that make them, in
   commission races. The 2014 matter concerned exactly elections for commission seats.
6. **Present management.** Theodore Geisler, Chairman, President and CEO since 2025-04-01, joined in 2001 and was CFO 2020
   to 2022 and President of APS 2022 to 2025 (proxy 2026). No filing read ties him to the 2014 spending. One director,
   Richard Fox, has served since 2014 (proxy 2026).
7. **Carried from Q4:** an annual EPS outlook ($4.55 to $4.75 for 2026), weather-normalized; whether it is habitually met
   was not tested.

**Judged.** The rows apply integrity "on doubt, not on proof" (the framework's words); "If you’ve got doubts, forget it."
**[M2013-088]**; "we wouldn’t hire anybody, no matter how able, if we didn’t trust them." **[M2015-047]**; "you can’t make a
good deal with a bad person" **[M1995-084]**; "people leave track records in life." **[M1998-168]**. The track record here
is an institution that, by its own filings, was investigated over the election of its own regulators, fought for four years
against a regulator's demand to disclose its political spending, and then gave a promise not to repeat it that was bounded,
in its own words, by one man's "tenure", which has ended. The test the rows give for such conduct is the front page: "a
course of action which, if put on the front page, you know, would make you very unhappy, you can get in a lot of trouble.
It may take a while." **[M2016-033]**. Against the doubt: no filing shows the conduct recurring after 2019, the present
chief executive is not tied to it, disclosure is now made yearly, and the board oversees a written policy. Those facts
narrow the doubt; they do not remove it, because the one safeguard that addressed the 2014 conduct by name has lapsed on its
own terms and the written policy, as read, does not close the channel used. The rows accept the cost of such a refusal:
"we rule out 90 percent of the times. And we may be wrong about a fair number that we’re ruling out." **[M2007-092]**.
A second reader who confines Q5 to the persons now in office, and gives no weight to the website reading, could close it IN;
the box would not change, since the COMPUTATION below puts the price above the top of the range.
- **Ability** (recorded, not weighed further): earned returns matched the peers and TEP under the same commission over the
  whole span (Q2), and the 2023 court-and-settlement recovery of the $215.5M SCR disallowance and the 20 bp penalty shows a
  management that defends the rate base; the 2019 to 2021 customer record (rate-plan migration, disconnections) cost it the
  penalty in the first place.
- **VERDICT on integrity: OUT, on doubt** **[M2013-088]**, **[M2015-047]**. The file closes here. Q6 to Q12 are NOT
  REACHED; Q7 is shown below as COMPUTATION, NOT A CLEARANCE, for the reporting figures the brief asks for.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED (the file closed at Q5). Facts found are under AFTER THE STOP. The buyback line Q6 would need: PNW bought back
no shares in the window (treasury purchases are tax withholding on awards only); the issuance prices are set against the
COMPUTATION range below, in AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
**COMPUTATION, NOT A CLEARANCE** (operator rule 3; the file closed at Q5). Script and output:
`_research 2026-10-26 PNW/q7.py`, `q7_output.txt`.
- **Basis.** The deciding part, APS, earns a return the ACC allows on its invested capital, so the equity-only basis is
  central and the all-equity basis is shown beside (Q7, The regulated utility; **[L2017-012]**, **[M2010-037]**). The
  company's own tax; owner cash is after it; no conversion.
- **Cash input** (Q4 table): five-year average FY2021 to FY2025 of owner cash after maintenance only, **$441M** (specific
  (e); the guess is depreciation and amortization including nuclear fuel, **[M2000-144]**, **[M1998-127]**); growth spending
  above maintenance averaged **$979M**. The literal window, all spending deducted, averages **-$538M**, on which no value can
  be built at any rate (shown beside). Specific (a): FY2021 (owner cash $102M, fuel deferrals) is a weak first year, but the
  filing does not call it aberrational; the robustness line below uses FY2025 alone instead.
- **Growth shown.** End to end ($102M to $790M) is meaningless; between the halves (FY2021-22 average $244M, FY2024-25
  average $700M) it is 42% a year, which carried ten years would need owner cash of 118% of sales against a best-ever 15.8%
  (FY2018). Cut under specific (f) to the business's own sales growth over the window, **8.85%** a year (FY2021 $3,804M to
  FY2025 $5,340M), with zero nominal growth after year ten **[M1999-067]**, **[M1997-095]**.
- **Growth spending (specific (e))**: $979M grown at 8.85%: **$1,065M in year one, $2,288M in year ten**, none after.
- **Utility debt credit**: long-term debt including current maturities rose from $6,314M (2020) to $9,806M (2025), **$698M a
  year** (no finance leases or securitization bonds found; commercial paper and term loans left out). Credited against growth
  spending only, growing and stopping with it. **Cap 60.0%**: the 10-K does not state the allowed capital structure of the 2024
  order (only the 2017 order's 44.2% debt and the 2025 request's 47.65%), so the cap is PNW's own long-term debt share of
  long-term capital at the latest filed date, 2026-06-30: $10,551M / ($10,551M + $7,035M). The credit (71% of growth spending)
  is held to the cap, so equity cash in years one to ten is owner cash less 40% of growth spending.
- **Value range (equity-only, central), at the 5.33% sovereign:** no-growth **$68.2** a share; growth case **$99.6**;
  **$68.2 to $99.6 against $105.88**, width 1.46 to 1. With the 13.55 million forward shares and their $1,171M counted:
  $70.0 to $98.3.
- **Floor tested first** **[M2003-149]**: at $105.88 (market cap $12,832M) the no-growth case returns 3.43% and the growth
  case 5.11%. **No case earns the floor of about ten percent.** Robustness: FY2025's single-year maintenance owner cash
  ($790M) valued at ten percent is $65.2 a share; a debt-credit cap at the 2025 request's 47.65% lowers the growth case at the
  floor to $27.1. The price also sits above the top of the range.
- **Fair price (a reporting figure, never a verdict; Part VII):** each end valued at ten percent (no-growth $4,406M, $36.4;
  growth $4,429M, $36.5), averaged: **$36.45 a share, equity-only, central** ($41.48 with the forward shares and their cash).
  **All-equity basis, beside:** owner cash plus after-tax cash interest ($259M a year: interest paid plus borrowed AFUDC, at a
  24.9% combined rate), less net debt at 2026-06-30 of $11,360M (long-term $10,551M, short-term $819M, less $9M cash;
  operating leases of $5.1B left out, said so): at ten percent no-growth -$36.0 and growth -$63.6, average **-$49.8 a
  share**; at the sovereign $14.5 to $28.9. Growth spending charged $1,065M in year one, $2,288M in year ten. Utility debt
  credit $698M a year, against growth spending only, cap 60.0% (own share; the filing states no allowed share). No cheap
  price is reported.
- **VERDICT (computation only, not a box):** had Q7 been reached it would close **OUT**: no case earns the floor at the
  price **[M2003-149]**, and the price sits above the top of the range.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts under AFTER THE STOP.

---
## THE BOX
**OUT**, decided at **Q5 on integrity doubt** **[M2013-088]**. Q1 IN; Q2 IN on the regulator's exception; Q3 and Q4 weigh
against. COMPUTATION beside the price: value range $68.2 to $99.6 a share (equity-only, utility basis) against $105.88; fair
price $36.45 (equity-only, central), all-equity -$49.8 beside; no case earns the floor, so Q7 would also close OUT.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.
- **Q6, the money.** Dividends paid $274M (2016) to $423M (2025), about 70% of net income (indicated $3.64 a share against
  2025 diluted EPS $5.05), while owner cash after all spending was negative; the gap was filled by debt (+$5.7B long-term) and
  shares. **Issuance against the COMPUTATION range:** the February 2024 forward at $64.51 (11.24M shares; 6.81M settled at
  $62.82 to $64.17) sits below the bottom of the range ($68.2); the ATM forwards of November 2024 to June 2026 at $88.69 to
  $103.00 (8.31M shares, weighted $97.38) sit inside it. About 20 million new shares since 2024 on about 113.5 million, to be
  read beside the framework's candidate second STOP on serial issuance **[L2014-015]**. No buybacks. Bright Canyon Energy,
  the unregulated venture of 2014, was sold in 2024 for about $108M received, after a 2022 full impairment of one wind stake
  (Clear Creek). 4CA's 7% of Four Corners went to the Navajo Transitional Energy Company; Pinnacle West still guarantees
  certain of its obligations to the other owners (10-K FY2025, Note 14). The 2021 order required $10M to the Navajo Nation and
  smaller payments to Hopi and Navajo County communities for the coal exits, recoverable in rates.
- **Q6, pay and board.** Annual incentive 50% earnings; performance shares (70% of long-term pay) on relative TSR 40%, EPS
  40% and "Clean Megawatts Installed" 20% (replaced in 2026 by a reliability and affordability measure); RSUs 30%. No capital
  charge in any measure. The chief executive is also chairman (since 2025-04-01), with a lead independent director.
  Say-on-pay support 96.6% in 2025 (proxy 2026).
- **Q9, debt and exposures.** Borrowed share of capital 60% (2025), 62% (June 2026); covenant ceiling 65%; ratings
  Baa2/BBB+/BBB (PNW) and Baa1/BBB+/BBB+ (APS), stable, no rating triggers; the $525M convertible due June 2027 is classified
  current; $5.1B of operating-lease obligations for storage and power contracts; the ACC bars APS dividends that would take
  its equity ratio below 40% (52% at 2025 year end). Interest paid $184M (2016) to $389M (2025) against operating income
  $856M to $1,068M. Single-site nuclear (Palo Verde, 29.1%, licence renewal to the mid-2060s planned); wildfire exposure
  under a 2025 state law and an approved mitigation plan; a captive cell for excess liability; an industry-wide nuclear wage
  class action (2025). Pension plans $180M underfunded, retiree medical $399M overfunded.
- **Q12.** Coal: Cholla burned its last coal in March 2025 (gas conversion planned, up to $440M); Four Corners runs to 2031,
  with "the potential extension of coal beyond 2031" now stated (10-K FY2025). Customers: the 2019 disconnection moratorium
  and rate-plan review (Q5, item 3).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (8fb67eb5); written question by question; committed after each with the
      two-path pathspec (Step 0 and Q1, Q2, Q3, Q4, Q5, the close).
- [x] Dispatched: the brief allowed per-question commits; the lock and the fold are the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` opened, listed or searched; `Test Runs/` was never listed (the
      template was opened by its path). Accidental sightings declared under Contamination at the top. A helper agent fetched
      the peer figures under the same blind rule, writing only into this run's research folder.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `_research 2026-10-26 PNW/check_cites.py`; every quoted
      fragment beside an id checked in that row; no E-ids. Filing facts carry accessions.
- [x] The order was kept; Q5 closed the file; Q7 is headed COMPUTATION, NOT A CLEARANCE and carries no entry language.
- [x] Owner cash after every real cost, never a net-income proxy; the sovereign from the Treasury; the price an aggregator
      quote, flagged.
- [x] Contrary evidence written down as found (Foundations); facts for later questions under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor date.
- [x] Only the arithmetic lines of `tools/run.py` used; its gross capex and its 2023 debt double count corrected from the
      filing.
- [x] `python tools/check_framework.py` run before the closing commit.
- **Honest weak points.** (1) The Q5 close leans partly on the company's website policy read through a summarizing fetch
  tool, not a filing; the filed part of the doubt (a commitment bounded by a tenure that has ended, never renewed in a filing
  read) stands without it. (2) The maintenance guess is depreciation; the filing gives none of its own. (3) FY2016 to FY2022
  statement lines are XBRL facts of each year's 10-K, checked against the filed statement only for FY2023 to FY2025. (4)
  Whether the EPS outlook is habitually met was not tested. (5) The ACC's present composition and the 2026 commission
  elections are in no filing read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q5 and time.** The integrity STOP is applied on doubt, but the text does not say whether doubt attaches to an
institution's past conduct under earlier officers or only to the persons now in office; here the answer decided which
question closed the file (Q5 rather than Q7). I read it to reach a lapsed safeguard against the institution's own conduct and
said that a second reader could close Q5 IN, with the same box. (2) **Website documents.** The protocol ranks filings over
aggregators but says nothing of a company's own website (here, the political participation policy the proxy points to); I
used it, flagged, as secondary. (3) **The utility debt-credit cap** falls back to the business's own debt share where the
filing states no allowed share; for a holding company with debt above the utility (60% consolidated against APS's 50%) the
fallback rewards holding-company leverage with a larger credit; the 47.65% sensitivity is shown. (4) **Specific (a)** makes a
year aberrational only on the filer's own description; utilities describe fuel-deferral swings without calling a year
aberrational, so FY2021 stays in the base. (5) **Specific (f)** cuts absurd growth to sales growth, but a utility's sales
carry fuel passed through at cost, so the cut rate partly carries the gas price; rate-base growth (about 6%) would be the
business's own measure, and the text does not offer it.
