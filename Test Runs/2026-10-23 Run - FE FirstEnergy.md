# Company Run — FirstEnergy Corp. (NYSE: FE) — 2026-10-23
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, 2026-10-23, after the run was committed (fa9667d5): `PORTFOLIO.md` read for this one ticker; **not held**.*

**CONTAMINATION, declared before any verdict.** (1) A directory listing of `Test Runs/` made to confirm the dated name was
free showed five run files and research folders dated today for other names (EDN, ENIC, ES, ETR, EVRG); none was opened.
(2) The session context showed recent commit subjects, which include the fold of the ES run of today (its box, its range
and its fair price). ES is another utility; its figures are not used here and no comparison is drawn from them. (3) The
brief itself names Q7's regulated-utility paragraph. Nothing else of the blind-listed files was seen. No other `Test Runs/`
file about FirstEnergy was opened, listed or searched.

**Dispatch.** Dispatched by an unattended overnight cycle under `Screens/_daily/_dispatch_brief.md` as amended in the brief
(lines of evidence and competitors derived by the analyst from the 10-K). Write-early kept: template copied before any
fetch; one commit per closed question, pathspec of this file and `Test Runs/_research 2026-10-23 FE/` only.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $46.49 (close 2026-10-22, as printed by `tools/run.py`; an aggregator quote, live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: **578,639,932** common, $0.10 par, as of June 30, 2026 (10-Q for the
  quarter ended 2026-06-30, filed 2026-07-28, accession `0001031296-26-000123`). `Screens/cover_shares.py FE` also printed
  13,628,447 shares: those are Jersey Central Power & Light's common, a co-registrant on the combined 10-Q, "all held by
  FirstEnergy Corp." (cover page); they are not added. Checked against the filed balance sheet of the same 10-Q: "578,639,932
  and 577,851,052 shares outstanding as of June 30, 2026, and December 31, 2025"; FE shows no treasury line (shares under the
  ICP 2020 "are issued from authorized but unissued common stock", FY2025 10-K Note 5). No 8-K or prospectus after the 10-Q
  changes the count (the EDGAR submissions list, fetched today, shows no filing after 2026-07-28).
- **Market cap:** 578.64M x $46.49 = **$26,901M**.
- **Sovereign for the earnings currency (USD):** **5.29%**, 30-year par yield, US Treasury daily par yield curve, 10/22/2026
  (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025 (filed 2026-02-18, `0001031296-26-000046`): Items 1, 1A, 7, the
  statements of Item 8, Notes 5 (stock-based pay), 13 (regulatory matters), 14 (contingencies) and 15 (segments); 10-Q for the
  quarter ended 2026-06-30 (filed 2026-07-28, `0001031296-26-000123`); proxy DEF 14A (filed 2026-04-01,
  `0001193125-26-138029`); 8-K of 2026-07-28 with its Ex. 99.1 news release (`0001031296-26-000122`); 8-K of 2026-02-12
  (`0001031296-26-000020`, a director not standing again); for the window and the history, the 10-Ks for FY2024
  (`0001031296-25-000006`), FY2023 (`0001031296-24-000008`), FY2021 (`0001031296-22-000013`), FY2020
  (`0001031296-21-000020`) and FY2019 (`0001031296-20-000008`). **Cross-checked against the filed statement:** net cash
  provided from operating activities 2025 = $3,700M in `tools/run.py` (XBRL) and $3,700M on the filed FY2025 cash-flow
  statement; total assets 2025-12-31 = $55,904M in both.
- `python tools/run.py FE`, arithmetic lines only (output in `Test Runs/_research 2026-10-23 FE/run_py_output.txt`): OCF
  1,387 / 2,891 / 3,700 (2023-2025); capital investments 3,356 / 4,030 / 4,705; three-year mean of OCF less capex -1,371,
  of OCF less D&A 1,091; the five-year window -791 and 1,145. Read against the filing: (a) stock pay is "n/f" in XBRL; the
  filing gives it (Note 5: total stock-based costs $85M / $86M / $83M for 2025 / 2024 / 2023, of which $39M / $43M / $44M
  expensed net of capitalization) and the equity statements give the stock actually issued under the plans, $50M / $98M /
  $89M / $74M / $60M for 2021-2025, which this run deducts; (b) `run.py`'s capex omits "Asset removal costs" ($226M / $213M /
  $274M / $305M / $376M for 2021-2025), a separate investing line, which this run counts as capital spending; (c) the
  depreciation `run.py` prints for 2023-2025 (1,461 / 1,581 / 1,664) is the segment note's "Depreciation", not the
  cash-flow statement's "Depreciation and amortization" (1,255 / 1,446 / 1,607); (d) finance-lease principal is $2M to $8M a
  year, immaterial. Owner cash is built at Q7 from the filed statements (`q7.py` in the research folder).
- **Lines of evidence chosen, from Items 1, 1A and 7, and why.** (1) *The regulated return and the regulatory climate*:
  Item 1 shows every price and return set by six state commissions and FERC (the allowed-ROE table), and Item 1A's second
  group of risks is state and federal rate regulation; this decides Q2 and Q3. (2) *HB 6 and what followed*: the first risk
  factor of Item 1A and a long section of Item 7 (the DPA, the SEC order, the PUCO audits, the securities class action, the
  indictment of two former officers); this decides Q5 and bears on Q9. (3) *The capital program and how it is paid for*:
  Item 7 (Energize365, $36 billion for 2026 to 2030, "expected to be funded with a combination of organic cash flows, the
  issuance of debt, including hybrid securities, and the issuance of common equity"); this bears on Q3, Q6 and Q7. (4) *The
  debt*, including "approximately $6.8 billion of external FE holding company debt" (Item 1) and the 2.50 times
  interest-coverage covenant (10-Q); Q9. (5) *The transmission part and its minority owner*: Item 1 records that Brookfield
  owns 49.9% of FET; Q2's parts, Q6 and Q7.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what six million customers' wires and the transmission grid will
pay their owners, not where the quotation goes. No macro forecast enters **[M2004-102]**: data-centre demand, PJM capacity
prices and interest rates appear in the filing and are read only as properties of this business. The market serves and
does not instruct **[M2006-077]**; the earnings releases feature "Core Earnings (non-GAAP)" and a growth target of "6% to
8%", and projections are not used **[M1995-050]**. Margin of safety **[M1996-084]**: if the case needs a pencil it is too
close. **Contrary evidence, written down as found** **[M1997-127]**: (i) the company itself, by its DPA, agreed to the
filing of a criminal information charging it with one count of conspiracy to commit honest services wire fraud and paid a
$230M penalty (FY2025 10-K, Item 7); (ii) in the five years 2021-2025 the business spent more on its assets than its
operations produced plus the long-term debt it raised, and sold 49.9% of its transmission holding company and $1B of common
stock to cover the gap (cash-flow statements, FY2023 and FY2025 10-Ks); (iii) earnings attributable to FE were $1,283M in
2021 and $1,020M in 2025 after $17.4B of capital investments over the five years (same); (iv) the PUCO cut the Ohio
companies' ROE to 9.63% and a $352M impairment for disallowances was recorded in 2025 (Item 7); (v) of the securities class
action, "FE believes that it is probable that it will incur a loss", the amount not estimable (10-Q,
`0001031296-26-000123`).

## THE STANDING RULE
A part-interest bought for cash with no borrowing, and sized so that its loss cannot touch what the buyer has and needs, does
not risk ruin; the buyer's conduct is the rule's subject **[L2014-024]**, and the target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**. FE is a regulated wires
  business: distribution in six states, high-voltage transmission in PJM, and 3,610 MW of regulated generation in West
  Virginia (FY2025 10-K, Item 1). Its earnings are a regulated return on a rate base ("a total rate base of approximately
  $21.3 billion" for the electric companies, plus $5.4 billion FirstEnergy-owned in Stand-Alone Transmission, Item 1).
  **The key variables** **[M1998-044]**: the size of the rate base, the allowed return and capital structure each
  commission grants, how fast and how fully costs are recovered, and customer demand. Each is on the public record (the
  allowed-ROE table of Item 1; the rate-case record of Item 7). They are not a technology forecast: the load forecast is
  about customers **[M2017-019]**, and the commissions' orders are filed.
- **Important and knowable** **[M2006-076]**; **would the insiders write it down** **[M2000-105]**? The regulators do write
  it down: each rate order states the return and the capital structure (the PUCO's order of 2025-11-19, "a return on equity
  of 9.63% and a hypothetical capital structure of 48.8% debt and 51.2% equity", Item 7). What is not knowable is the
  regulatory mood ten years out; that is a question about the castle and is carried to Q2.
- Routing: not a fast-changing industry; not a bank; FE is a holding company read by its parts, all three of which are
  regulated electric utilities of the same kind (Q2's parts table).
- **VERDICT: IN.** The economics can be pictured from the figures **[M2008-069]**, and the first question **[M1995-051]** is
  passed: a cost-of-service utility whose ten-year earning power is a rate base times an allowed return, both on file.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now" **[M1995-038]**.
- **The attacker with money** **[M2011-015]**, **[M2012-106]**. "Within FirstEnergy’s Electric Companies' distribution
  business, including JCP&L, there generally is no competition for electric distribution service in the Electric Companies’
  respective service territories" (FY2025 10-K, Item 1, Competition). The barrier is a legal franchise, not a cost or a
  brand: no sum of money buys the right to string a second set of wires to six million customers. The one breach the filing
  names is in transmission: under FERC Order No. 1000 "non-incumbent developers can compete for certain PJM transmission
  projects in the service territories" of FE's companies, which "has resulted in additional competition to build
  transmission facilities" (same), while FE also bids outside its territory (Valley Link, FET's share "approximately $1
  billion"; Grid Growth, "approximately $448 million", Item 1).
- **Pricing power and the agony before a rise** **[M2005-020]**. FE has none of its own: every rate is set in a rate case.
  The record of the last cycle is the agony made formal. Ohio asked for "approximately $190 million" with "a return on
  equity of 10.8%" and was granted "approximately $34 million, with a return on equity of 9.63%" (PUCO, 2025-11-19, Item 7),
  followed by a "$352 million (pre-tax) impairment charge ... related to disallowances in the Ohio base rate case" (Item 7);
  Ohio's legislature repealed the statute for the electric security plans (HB 15, 2025); FERC's transmission ROE lost its 50
  basis point RTO adder by a Sixth Circuit ruling of January 2025 (Item 1, note (1) to the ROE table). On the other side,
  base rate cases were implemented in New Jersey, West Virginia and Pennsylvania (Item 7, results 2025 against 2024).
- **Unit volume** **[M1999-108]**: peak demand rose at six of the seven companies from 2023 to 2025 (FE PA 10,058 to 10,505
  MW; OE 5,192 to 5,744 MW; Item 1, System Demand); the release of 2026-07-28 speaks of data-centre demand "contracted ... at 6.4
  GW" (Ex. 99.1, a company projection, not used as a figure). **The low-cost position** and **the brand** do not apply to a
  franchised monopoly; the customer has no low bid to take.
- **Widening or narrowing** **[M1999-108]**: in Ohio, narrowing over the last cycle (the ESP repeal, the ROE cut, the
  disallowance, $275M of restitution and refunds ordered on 2026-01-07, Item 7); in New Jersey, West Virginia and
  Pennsylvania, held. **What could destroy, modify or reduce it** **[M2000-014]**: not a competitor, a regulator. Item 1A
  names the path: PJM capacity prices "can result in material increases in retail customers’ monthly electric utility
  bills", and "customer resistance to the resulting market driven increases ... could lead to increased pressure for state
  and federal utility regulators to limit" recovery. The speakers name the same failure: "the regulatory climate in a few
  states has raised the specter of zero profitability or even bankruptcy" and "I did not anticipate or even consider the
  adverse developments in regulatory returns" **[L2023-011]**.
- **Ask the competitors**: the 10-K names no competitor (distribution has none; the transmission developers are not named).
  **The competitor row is therefore a CONVENTION of this run** (rationale: the filing names none, and the nearest
  comparison is other PJM wires utilities in the same states): American Electric Power (CIK 4904; the Ohio and PJM
  transmission neighbour), PPL (CIK 922224; Pennsylvania distribution), Exelon (CIK 1109357; PJM distribution in
  Pennsylvania, Maryland and New Jersey). Metric: net income attributable to common over average common equity, each from
  its own 10-K XBRL (`roe.py` in the research folder):

  | ROE | 2021 | 2022 | 2023 | 2024 | 2025 | five-year mean | latest 10-K |
  |---|---|---|---|---|---|---|---|
  | **FE** | 16.1% | 4.3% | 10.7% | 8.5% | 8.2% | 9.6% | `0001031296-26-000046` |
  | AEP | 11.6% | 10.0% | 9.0% | 11.4% | 12.3% | 10.9% | `0000004904-26-000013` |
  | PPL | -10.9% | 5.5% | 5.3% | 6.3% | 8.1% | 2.9% | `0000922224-26-000008` |
  | EXC | 5.1% | 7.3% | 9.2% | 9.3% | 9.9% | 8.2% | `0001109357-26-000018` |

  Read in words: PPL's 2021 carries its loss on the UK sale and Exelon's 2021 carries its generation arm before the 2022
  separation; FE's equity is small for its size because of the accumulated deficit left by its 2018 generation exit, which
  flatters its ratio (its "aggregate actual ROE ... as determined for regulatory purposes" for 2025 is 9.8%, Item 1). Over
  the whole span the field earns returns in the regulated band, FE inside it and below AEP.
- **The parts table** (CONVENTION of the business of parts, Q2; the filer reports its present three segments for 2023-2025
  only, so the shares are of three years, the filer's own restated figures, FY2025 10-K Note 15):

  | part | earnings attributable to FE 2023 / 2024 / 2025 ($M) | share of the three-year total of the parts | castle | decides |
  |---|---|---|---|---|
  | Distribution (Ohio Companies, FE PA) | 587 / 624 / 363 | 39% | state franchise, rate base $11.1B | yes, the largest part |
  | Integrated (JCP&L, MP, PE) | 300 / 535 / 588 | 35% | state franchise plus regulated generation in WV, rate base $10.2B | no |
  | Stand-Alone Transmission (FE's share of FET, KATCo) | 399 / 294 / 357 | 26% | FERC formula rates; Order 1000 competition for new projects; Brookfield owns 49.9% of FET | no |

  No part carries more than half; the largest, Distribution, decides. Its castle is the exclusive franchise and stands.
  Corporate/Other lost $163M / $475M / $288M (holding-company interest, the HB 6 penalties).
- **The field's returns over the last full cycle**, judged in words: regulated, in a band set by commissions; a durable
  castle protecting ordinary returns would close OUT, but "A return set by a regulator is the exception, carried to Q3 as a
  second best" (Q2's list), on the rows "there’s no way we get rich on our utility investments. But there’s no way we get
  poor, either" **[M2009-104]** and "decent returns on the incremental sums they invest" **[L2009-012]**.
- **VERDICT: IN.** The castle stands as a legal monopoly on the wires; it is not shown open by any attacker **[M2011-015]**.
  Its weakness is the lord who sets its rents, the regulator **[L2023-011]**, which is carried to Q3, Q7 and Q9.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **What it earns on the capital it needs.** The regulated measure: "aggregate actual ROE ... as determined for regulatory
  purposes" 9.8% for 2025 against allowed returns of 9.5% to 12.7% (FY2025 10-K, Item 1). On the filed totals for 2025:
  earnings attributable to FE $1,020M, income to the minority $251M and interest expense $1,217M (Note 15) against
  tangible assets of $50,286M (total assets $55,904M less goodwill $5,618M) give about 4.4% on tangible assets before
  interest, with interest taken after tax at the 21% federal rate (arithmetic on the filing; the 21% is the statutory rate,
  not FE's own, and is said so). "Return on tangible assets" is the measure the rows use **[M2011-060]**.
- **To stand still and to grow.** Over 2021-2025 capital investments were $17,426M and asset removal costs $1,394M, against
  depreciation of $7,383M (FY2021, FY2023 and FY2025 10-Ks): spending of 2.5 times depreciation. The filing does not split
  maintenance from growth in dollars; it lists "Base distribution projects to address aging infrastructure" and
  "Generation maintenance projects" among the uses of Energize365 without amounts (Item 7). The next five years are planned
  at $36 billion, "approximately 25% higher than the previous" plan (Item 7). "To earn more, their owners must invest more"
  **[L2011-019]**.
- **What the added capital earned.** Earnings attributable to FE were $1,283M in 2021 and $1,020M in 2025; in between $406M
  (2022), $1,102M (2023), $978M (2024) (10-K XBRL, accessions in `roe.py`'s output). Over the same years the business put
  $18.8B into its assets, common equity rose from $8,675M to $12,510M, the long-term debt on the face of the balance sheet
  rose from $23,854M to $26,556M (`tools/run.py`'s balance-sheet table, filed vintages), and 49.9% of FET was sold. The owners'
  earnings did not rise with the capital: "We just put way more capital into the business" **[M2023-081]**, said of a
  utility whose earnings did rise; here they did not. Part of the gap is the regulator's (the Ohio disallowance and ROE
  cut, Q2) and part is the dilution from the FET sale ("The dilutive effect of the FET Equity Interest Sale that closed in
  March 2024", Item 7).
- **The capital-heavy business as a second best**: accepted where it earns "decent returns on the incremental sums they
  invest" **[L2009-012]**; the second-best grade asks that the reinvestment rate be "a very satisfactory rate"
  **[M1998-081]**. The low-return business held long does not do well "Even if you buy it cheap to start with"
  **[M1998-006]**.
- **WEIGHS AGAINST.** A capital-heavy regulated business whose incremental $18.8B over five years left the owners'
  earnings lower than at the start, and which needed equity sales to fund it; the second best **[L2009-012]** is not shown.
  (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** **[M2025-032]** (`tools/run.py` table, first-filed XBRL vintages, accessions
  listed there; the 2024 and 2025 columns checked against the filed FY2025 balance sheet):

  | $M, year-end | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|---|---|---|---|---|
  | common equity | 6,241 | 3,925 | 6,814 | 6,975 | 7,237 | 8,675 | 10,166 | 10,437 | 12,455 | 12,510 |
  | goodwill | 5,618 | 5,618 | 5,618 | 5,618 | 5,618 | 5,618 | 5,618 | 5,618 | 5,618 | 5,618 |
  | retained earnings | -4,532 | -6,262 | -4,879 | -3,967 | -2,888 | -1,605 | -1,199 | -97 | 43 | 35 |
  | debt on the face | 22,552 | 22,497 | 19,504 | 20,998 | 24,477 | 23,854 | 21,654 | 24,910 | 24,023 | 26,556 |
  | cash | 199 | 589 | 367 | 627 | 1,734 | 1,462 | 160 | 137 | 111 | 57 |
  | shares outstanding (M) | 442.3 | 445.3 | 511.9 | 540.7 | 543.1 | 570.3 | 572.1 | 574.3 | 576.6 | 577.9 |

  **What moved and why.** Common equity doubled while retained earnings went from a deficit of $4.5B to $35M: the equity is
  paid in, not earned and kept. The steps are issuances: the "$2.5 billion equity issuance" of January 2018 ("$1.62
  billion in mandatorily convertible preferred equity ... and $850 million" of common, FY2019 10-K); "Common stock issuance"
  of $1,000M in 2021 (FY2023 10-K cash-flow statement); "Proceeds from FET minority interest sale, net of transaction costs"
  $2,348M in 2022 (same) and "Proceeds from FET Equity Interest Sale" $3,500M in 2024, of which $1,934M was credited to paid-in
  capital (FY2025 10-K equity statement). Shares outstanding rose 31% over the nine years. Goodwill, unchanged at $5,618M, is
  45% of 2025 common equity. Debt rose by $4.0B over the ten years and reached $28,983M at 2026-06-30 (10-Q: currently
  payable long-term debt $505M, short-term borrowings $1,376M, long-term debt and other long-term obligations $27,102M).
  Cash is held near nothing; receivables ($1,726M) and materials ($577M) move with the business. **What the figures cannot
  say**: the securities class action carries no accrual because the loss "cannot yet reasonably" be estimated (10-Q); the
  regulators' future treatment of the $56B of plant is not in any figure.
- **The real costs.** Depreciation $1,664M in 2025 against capital investments of $4,705M and removal costs of $376M: the
  depreciation is a real cost **[R1996-023]**, and here it falls far short of the spending that keeps and grows the plant
  **[L2015-004]**. Stock pay: $85M of stock-based costs in 2025 (Note 5), $60M of stock issued under the plans (equity
  statement). **The recurring "one-time"**: every year of the window carries a special item of the same family. 2021: the
  $230M DPA penalty; 2024: "the $100 million civil penalty resulting from the SEC investigation and the $19.5 million
  settlement with the OAG’s office", a $200M ARO charge, a $62M impairment of the Akron office; 2025: "A $352 million
  (pre-tax) impairment charge" for Ohio disallowances and "A $275 million (pre-tax) charge ... resulting from the Ohio
  Companies' PUCO-approved settlement" (Item 7, both years). These are costs of the business as it is run: "we do not ask you
  to forget about those costs" **[M1999-023]**; telling owners year after year to ignore them "is misleading"
  **[L2016-007]**. Pensions are marked to market each year ("Pension and OPEB mark-to-market adjustments" of -$253M / $22M /
  $78M, cash-flow statement), and the company funded the plan with a $750M "Pension trust contribution" in 2023.
- **EBITDA in the filer's own mouth**: no instance found in the FY2025 10-K's MD&A by a text search for "EBITDA". **The
  adjusted figure featured**: the release of 2026-07-28 leads with "Core Earnings (non-GAAP)", "Reaffirms 2026 Core Earnings
  guidance range of $2.62 to $2.82 per share" and "Core Earnings compound annual growth near the top end of 6% to 8% from 2026
  to 2030" (8-K, `0001031296-26-000122`, Ex. 99.1), while GAAP earnings for 2025 were $1.77 per basic share (Item 7). A
  management "that regularly attempts to wave away very real costs by highlighting "adjusted per-share earnings" makes us
  nervous" **[L2016-006]**; guidance and the desire to "hit the number." **[L2019-006]**. Recorded here as a weighing
  against and carried to Q5 **[M1994-018]**.
- **Confusion or suspicion from the statements themselves?** The statements are readable: regulated revenues, a stated
  rate base, segment results reconciled (Note 15). The tells of the accounts **[M1995-064]** are not present in the current
  statements (no building prepaid or deferred accounts out of line; materials flat against sales). The history does carry
  one: the FY2020 10-K's auditor found "a material weakness in internal control over financial reporting existed as of that
  date related to its senior management failing to set an appropriate tone at the top" (`0001031296-21-000020`); the FY2021
  report carries no such finding. That fact is about people and is carried to Q5.
- **VERDICT on the accounts: WEIGHS AGAINST** (no STOP: not confusing **[M1995-063]**, and the suspicion the record raises is
  about the people, not about the present statements **[M1995-065]**). The recast earnings feed Q7 as owner cash, with every
  special item kept in.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**The integrity record, from the filings** (each with its source):
1. **The company's own admission.** "FE agreed to the filing of a criminal information charging FE with one count of
   conspiracy to commit honest services wire fraud" and paid "a criminal monetary penalty totaling $230 million" (DPA of
   2021-07-21; FY2025 10-K, Item 7, Other Legal Proceedings). The DPA's obligations run on until the prosecution of "two
   former FirstEnergy senior officers", charged on 2025-01-17 "with one count of participating in a Racketeer Influenced
   and Corrupt Organizations Act conspiracy", concludes (same).
2. **What the board itself found in 2020.** The board's committee terminated the CEO and two senior vice presidents, who
   "violated certain FirstEnergy policies and its code of conduct"; "certain former members of senior management did not
   reasonably ensure that relevant information was communicated within our organization and not withheld from our
   independent directors, our Audit Committee, and our independent auditor"; the matters included "a payment of
   approximately $4 million made in early 2019" to "an entity associated with an individual who subsequently was appointed
   to a full-time role as an Ohio government official directly involved in regulating the Ohio Companies"; the chief legal
   officer and the general counsel and chief ethics officer were separated "due to inaction and conduct that the Board
   determined was influenced by the improper tone at the top" (FY2020 10-K, `0001031296-21-000020`). The auditor reported
   a material weakness for "senior management failing to set an appropriate tone at the top" (same).
3. **The consequences, still arriving.** SEC settlement of 2024-09-12: "a civil penalty of $100 million and to cease and
   desist" (FY2024 10-K, `0001031296-25-000006`); the Ohio attorney general's $19.5M settlement (FY2025 10-K); the PUCO's
   audit of "53 payments totaling approximately $75 million made in support of the passage of HB 6 and subsequent
   referendum efforts", its "approximately $250 million in monetary penalties" of 2025-11-19, replaced on 2026-01-07 by
   "restitution and refunds totaling approximately $275 million" (FY2025 10-K, Item 7); the securities class action,
   class recertified on 2026-04-30, "probable" loss not estimable (10-Q, `0001031296-26-000123`).
4. **Who runs it now.** Brian X. Tierney, CEO since 2023 and chairman since 2025, from Blackstone Infrastructure Partners
   and AEP (FY2025 10-K, executive officers): the chief executive also chairs **[L2014-026]**. K. Jon Taylor, CFO since
   2020, was FE's "Vice President, Controller and Chief Accounting Officer" until 2018 and "President, Ohio Operations" in
   2018-2019 (FY2020 10-K). Jason J. Lisowski has been "Vice President, Controller and Chief Accounting Officer" since 2018
   (FY2019 10-K, `0001031296-20-000008`; FY2025 10-K). No filing read accuses either of them of anything; no filing read
   says what either knew of the payments recorded and the Ohio regulator paid during their tenure. Of the ten director
   nominees of 2026, three have served since 2017 or 2018 (Demetriou and O'Neil 2017, Turner 2018; DEF 14A,
   `0001193125-26-138029`), through the years in which the board was, by its own later finding, kept uninformed.
5. **The habits carried from Q4**: Core Earnings featured, guidance "reaffirmed", growth "near the top end" of a stated
   range (Ex. 99.1 of 2026-07-28). And the pay yardstick moved mid-course: on 2025-06-17 the board "approved a
   modification to one of the key performance indicators (“KPI”) for certain outstanding awards", replacing "the Operating
   EPS KPI with the Core EPS KPI" for the 2023-2025 and 2024-2026 cycles, after "our non-core earnings from pension and
   Signal Peak ... decreased significantly – by over 50%" (DEF 14A; the cumulative-EPS payout was capped at 100% of target
   in the same change). The CEO's 2025 total compensation was $13,452,559 (DEF 14A, Summary Compensation Table).

**The other side's case, stated as well as I can** **[M1997-127]**: the people who did it were removed by the board itself
in 2020 and two of them are under federal indictment; the CEO is an outsider hired in 2023; seven of ten directors joined
in 2021 or later; FE completed the DPA's three-year term ("As of July 22, 2024, FirstEnergy had successfully completed the
obligations required within the three-year term of the DPA", FY2025 10-K), cooperated with the SEC, paid restitution in Ohio,
and no new misconduct is reported in any filing read. A reader could say the rascals are gone.

**The judgment.** The test is the people who will run it, and it is applied on doubt, not proof: "If you’ve got doubts,
forget it." **[M2013-088]**; "we rule out 90 percent of the times. And we may be wrong about a fair number that we’re ruling
out. The important thing is whether the ones we’re ruling in we’re right about." **[M2007-092]**. The doubt here has four
roots, each in the filings. (a) The wrong was the institution's, not one man's: it was found in the "tone at the top", it
reached the legal and ethics officers, and information was kept from the directors and the auditor; "people know it
throughout the organization. And they adopt the norms of what they think is happening up above them." **[M2000-154]**.
(b) The two officers who keep the books today held the books, and the Ohio presidency, while the payments were made; the
filings are silent on what they knew, and silence is not evidence of behaviour **[M1998-166]**. (c) A new chief executive
three years in has not yet left a track record here **[M1998-168]**, and he also chairs the board that judges him
**[L2014-026]**. (d) The present management's public habits are the ones the rows tie to culture: an adjusted figure
featured **[L2016-006]**, guidance and the number to hit **[L2019-006]**, and a pay yardstick changed for awards already
running when the old one moved against it; "I hate, with a passion, rewarding anything that can be easily faked"
**[M1996-089]**; these are "things that they do in public in relation to their investors and the promises they make"
**[M2004-067]**. The rows do not buy an organization in order to watch it change: "we really don’t believe in buying into
organizations to change them" **[M2000-152]**, and "it’s a lot easier to build a new organization around a culture than it
is to change the culture of an existing organization" **[M2010-021]**. Professing integrity settles nothing ("everybody
mouths the integrity, even when it’s lacking" **[M2010-069]**; the MD&A opens "FirstEnergy is dedicated to integrity").
None of this proves a present officer dishonest. It leaves a doubt that the filings cannot remove, and the rule is the
doubt.

- **Ability** (the two yardsticks **[M1994-008]**): the hand dealt includes a regulatory climate partly of the company's own
  making (the Ohio penalties and disallowances, Q2); the record of the last five years is flat owners' earnings on rising
  capital and half the transmission holding sold (Q3, Q6 facts below). **WEIGHS AGAINST.**
- **VERDICT on integrity: OUT** (doubt **[M2013-088]**). The file closes here. Q6 to Q10 and Q12 are NOT REACHED; what was
  found for them is under AFTER THE STOP, and Q7's figures are COMPUTATION, NOT A CLEARANCE.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED (Q5 closed the file). Facts found are under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The reporting figures are computed under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q5, integrity, on doubt** **[M2013-088]**. Q1 IN, Q2 IN, Q3 weighs against, Q4 weighs against; Q6 to Q12 not
reached. COMPUTATION beside the price (not a clearance): the value range is the no-growth case alone, **-$14.77 a share**
on the equity-only basis (central for a regulated utility), against **$46.49**; fair price **-$7.81** equity-only and
**-$57.55** all-equity. No case of the range, nor any variant shown beside it, earns the floor at the price, so the file
would have closed OUT at Q7 had it reached it.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.

**Q6, the money and the owners.**
- Retention: retained earnings were $-1,605M at 2021-12-31 and $35M at 2025-12-31; common dividends paid 2021-2025 were
  $4,632M against earnings attributable to FE of $4,789M (cash-flow statements and XBRL, FY2023 and FY2025 10-Ks). Over the
  same years FE raised $6,848M of equity: $1,000M of common stock in 2021, $2,348M net from the sale of 19.9% of FET in 2022,
  and $3,500M from the sale of a further 30% of FET in 2024 (same). The 10-K plans further common equity "averaging
  approximately 1% of its now current market capitalization in each year" of 2026-2030 (Item 7). Shares outstanding rose
  from 442.3M (2016) to 578.6M (2026-06-30), 31% (XBRL; 10-Q cover).
- Buybacks: none in 2021-2025 (no repurchase line in the financing sections, FY2023 and FY2025 10-Ks). The bottom of the
  Q7 range below is -$14.77 a share, so no price paid could have sat at or below it. *(The Q6 buyback line the brief asks
  to write back with Q7: no buyback to test.)*
- Issuance and deals: 49.9% of FET, the transmission holding company of the Stand-Alone Transmission segment, is now
  Brookfield's (Item 1); FE receives its share through FET's distributions and its special interest in MAIT's Class B
  distributions (Item 1). The serial-issuer row **[L2014-015]** is the candidate second STOP of Q6, unresolved in the
  framework's section VI. No all-stock acquisition in the window.
- Part B: CEO total compensation for 2025 $13,452,559 (DEF 14A); the CEO chairs the board; the mid-cycle change of the LTIP
  KPI from Operating EPS to Core EPS (Q5, item 5).

**Q7, COMPUTATION, NOT A CLEARANCE** (script and output: `q7.py`, `q7_output.txt` in the research folder).
- **Basis.** The deciding part (Distribution, Q2's parts table) earns a return a regulator allows on its invested capital,
  so the equity-only basis is central and the all-equity basis is beside (Q7, The regulated utility, **[L2017-012]**,
  **[M2010-037]**). Owner cash after interest and after the company's own tax: operating cash flow (cash taxes and interest
  already paid), less stock issued under the plans, less capital investments and asset removal costs, less distributions
  to the FET minority, plus the long-term debt raised over the window to fund the fixed assets, capped at the regulator's
  allowed debt share.
- **The window**, 2021-2025, from the filed statements (2021-2022: FY2023 10-K `0001031296-24-000008`; 2023-2025: FY2025
  10-K `0001031296-26-000046`), $M:

  | | 2021 | 2022 | 2023 | 2024 | 2025 | sum |
  |---|---|---|---|---|---|---|
  | operating cash flow | 2,811 | 2,683 | 1,387 | 2,891 | 3,700 | 13,472 |
  | less Ohio restitution accrued in 2025, paid 2026 | | | | | -275 | -275 |
  | less stock issued under the plans | -50 | -98 | -89 | -74 | -60 | -371 |
  | less capital investments | -2,487 | -2,848 | -3,356 | -4,030 | -4,705 | -17,426 |
  | less asset removal costs | -226 | -213 | -274 | -305 | -376 | -1,394 |
  | less distributions to the FET minority | 0 | -21 | -72 | -86 | -100 | -279 |
  | plus net long-term debt raised (issued less redeemed) | 1,568 | -2,305 | 2,613 | -660 | 2,796 | 4,012 |
  | **equity-only owner cash** | **1,616** | **-2,802** | **209** | **-2,264** | **980** | **-2,261** |

  The credit: net long-term debt raised over the window $4,012M, against a cap of $9,184M (48.8% of the $18,820M of capital
  investments and removal costs). 48.8% is "a hypothetical capital structure of 48.8% debt" in the PUCO's order of
  2025-11-19, the only allowed debt share the 10-K states for any jurisdiction; FE's own debt share of capital at 2026-06-30
  is 67% ($28,983M of borrowings against $14,426M of total equity, 10-Q). The cap does not bind under either. The 2025
  restitution is charged in the year it was recognized because the cash left in 2026 (10-Q, H1 operating cash flow), the one
  adjustment to the filed operating cash flow; the 2021 DPA penalty, the 2023 $750M pension contribution and the 2024 SEC and
  Ohio settlements are left in their years as real costs of the business as run (Q4).
- **Central: -$452M a year, -$0.78 a share** (window mean, debt credited at the window total).
- **The specifics, in order.** (a) Cycle base: neither end year is described by the filer as aberrational; the literal window
  is the base, and is the only one shown. (b) Decline and sign: the series changes sign; between halves (2021-2022 mean
  -$593M, 2024-2025 mean -$642M) no compound rate has meaning; **the range is the no-growth case alone, said so**. (c)
  Acquisitions: none in the window; the 2025 sale of the Signal Peak stake ($47.5M at book) is immaterial. The FET minority
  sales are the filer's financing and equity transactions and are treated as equity issued, not as businesses sold
  (CONVENTION of this run; rationale: they are sales of a share of the deciding business's sister segment, booked by the
  filer as equity, and crediting $5.85B of one-time proceeds as negative capital spending would carry a sale that cannot
  recur into ten years of value, the absurdity **[M1999-067]** names). No signed unclosed deal; no deal after the window.
  (d) Working capital: inside operating cash flow as filed. (e) Maintenance: the filing names maintenance projects but gives
  no amounts, so the guess is not allowed in dollars; the depreciation variant is shown beside. (f) Cap: no growth is
  carried, so nothing to cut. The four PG specifics: the series is aggregate, not per share; all spending is deducted;
  zero growth after year ten is moot; a price above the top closes OUT.
- **The floor, tested first** (Q7): at $46.49 the floor needs about $2,690M a year of owner cash on the equity (10% of
  $26,901M). No case earns it. **Value range: -$14.77 to -$14.77 a share** (the no-growth case at the 5.29% sovereign,
  equity-only), against $46.49: OUT by the floor whatever the width.
- **Beside, never deciding.** (i) The debt credited each year at the allowed share instead of the debt actually raised:
  $582M a year, $1.01 a share, worth $19.02 at the sovereign and $10.06 at ten percent; about 2.2% at the price. (ii)
  Depreciation in place of all capital spending, no debt credit: $1,033M a year, $1.78 a share; halves growth 1.28% a year;
  worth $33.74 (no growth) to $37.39 (that growth) at the sovereign, $17.85 to $19.47 at ten percent; about 3.8% to 5.2% at
  the price. (iii) A stricter minority charge (the minority's $251M share of 2025 income in place of the $100M it was paid)
  would lower every case. (iv) **All-equity basis**: owner cash before interest (interest paid $5,169M over the window,
  added back after tax at the 21% federal rate, a statutory rate and said so) is -$438M a year; net debt at 2026-06-30
  $28,920M ($28,983M of borrowings, finance leases inside "other long-term obligations", less $63M of cash; restricted cash
  and operating leases left out); value at the sovereign -$64.28 a share.
- **The two reporting figures** (a reporting convention, not a rule; nothing here is a verdict or entry language): **(a)
  value range -$14.77 to -$14.77 a share** (the no-growth case alone, equity-only, central for a regulated utility); **(b)
  fair price -$7.81 a share equity-only (central)**, with **-$57.55 a share on the all-equity basis** beside; each end case
  valued at ten percent and the two averaged (here one case), after the company's own tax.

**Q8.** The sovereign pays 5.29%; the central equity-only owner cash yields -1.7% at the price, the most generous variant
about 5.2% **[M1997-089]**.

**Q9, debt and exposures.**
- Borrowings $28,983M at 2026-06-30 against common equity of $12,935M (10-Q); "approximately $6.8 billion of external FE
  holding company debt" at 2025-12-31 (Item 1); a $750M term loan "with a maturity date of April 27, 2027" drawn to repay
  short-term borrowings, short-term borrowings of $1,376M, and a covenant "to maintain a consolidated interest coverage
  ratio of not less than 2.50 times" (10-Q). On the rows' definition, pre-tax earnings over interest **[L2012-002]**: 2025
  income before tax $1,559M (net income $1,271M plus income taxes $288M) and interest expense $1,217M give (1,559 + 1,217)
  / 1,217 = 2.3 times (FY2025 10-K).
- Exposures: the securities class action, probable loss not estimable (10-Q); a failure to comply with the DPA "may also result
  in a breach of certain covenants contained in our credit agreements and could result in an event of default" (Item 1A); the PJM capacity-price pressure on bills and on regulators (Item 1A).
- The "little or no debt" criterion **[R1997-001]** is not met (it is a STOP for a whole business only).

**Q12.** The filings read describe HB 6 as legislation FE lobbied for, and the money as "53 payments totaling approximately
$75 million made in support of the passage of HB 6 and subsequent referendum efforts" (PUCO audit, FY2025 10-K); the
front-page test is the row's **[M2016-033]**. Recorded, not weighed.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `4da61af1`); written question by question; committed after each
      (Step 0 to Q1, Q2, Q3, Q4, Q5, the close).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's; the run binds
      only once folded into the register by that session (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; one listing of `Test Runs/` to
      confirm the dated name was free showed five other names' file names, and the session context showed commit subjects
      about the ES run; both are declared under CONTAMINATION at the top and were not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`; every quoted fragment beside an id is in its row
      (`check_ids.py` in the research folder); every filing fact carries its document and accession; no E-id.
- [x] The order was kept; Q5 was the first STOP that failed and closed the run; everything after it is NOT REACHED or
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay, removal costs, the minority's cash, the HB 6 penalties and settlements
      kept in), never a net-income proxy; the sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (THE FOUNDATIONS, Q5's other side); the facts for later questions are under
      AFTER THE STOP.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its stock pay ("n/f"), its capex (without removal costs) and its
      depreciation were each read against the filing (Step 0).
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The regulated utility's debt credit** says "the long-term debt raised over the window to fund the fixed assets" but
not whether that is gross or net of redemptions, nor how to treat debt repaid out of equity proceeds. At FE the equity sales
of 2022 and 2024 ($5.85B for 49.9% of FET) repaid debt, so the net debt raised ($4,012M) is far below the allowed share of the
spending ($9,184M) and the central owner cash is negative; crediting at the allowed share instead (variant (i)) gives $582M a
year. I used the window's net long-term debt, as the words read most naturally, and showed the other beside; the box does
not turn on it, since neither earns the floor. (2) **Specific (c)** names businesses bought and sold, not a sale of a
minority stake in a consolidated subsidiary; I treated FE's FET sales as equity issued (the filer's own classification) and
confessed it as a CONVENTION of this run. (3) **Q5 and successor management**: the framework applies integrity "on doubt
alone" but says nothing of how far an institution's admitted crime attaches to the managers who follow, or of when such a
record is spent; I judged the doubt from the filings (officers then in place still in place, three directors from the
period, present habits) and stated the other side's case, but another analyst could weigh the 2020 dismissals more heavily
and pass Q5; the box would then have been decided at Q7, also OUT. (4) **The parts table** asks for five-year shares, but
FE re-cut its segments in 2024 and reports the present three for 2023-2025 only; I used three years. (5) The template's
box line clause "integrity facts recorded, not judged" covers a file closed before Q5 and has no wording for a file closed
at Q5 itself; I gave none.

