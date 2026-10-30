# Company Run — MGE Energy, Inc. (Nasdaq: MGEE) — 2026-10-23
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. The dispatching session
fills it at the fold. **Filled at the fold (2026-10-23, after the run was committed): not held** (`PORTFOLIO.md` read for MGEE only).

**Dispatch:** a dispatched blind purchase run of record under the canonical brief `Screens/_daily/_dispatch_brief.md`, with
the brief's one stated departure (the lines of evidence derived by the analyst from the 10-K, and competitors taken from the
10-K). Working folder `Test Runs/_research 2026-10-23 MGEE/` (notes, scripts, the ledger rows read, the arithmetic); raw
filings are kept in its `cache/` subfolder, which is gitignored.

**Contamination, declared and not used.** (1) A directory listing of `Test Runs/` made to check for a same-day file name
showed the names of ten other run files dated 2026-10-23 (EDN, ENIC, ES, ETR, EVRG, FE, FTS, HE, IDA, KEP) and their
research folders; I did not open them. (2) The session's opening context showed recent commit subjects for a KEP v5 re-run
(box OUT at Q2, its comparators and figures) and research folders for AYI and ARCB in the working-tree status. (3) The
memory index loaded with the session carries lines on the queue state and a count of gate-clearers. None of this concerns
MGEE and none of it was used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $74.24 (close 2026-10-22; Yahoo Finance chart API through `tools/sources.py price()`; an **aggregator, flagged**
  per operator rule 5, used for the live quote only).
- **Shares by class** from the latest filing's cover: **37,784,012** MGE Energy common shares outstanding as of 2026-07-31
  (10-Q for the quarter to 2026-06-30, filed 2026-08-05, accession `0001193125-26-333969`; `python Screens/cover_shares.py
  MGEE`). The tool's second line, 17,347,894 shares, is Madison Gas and Electric Company's own common stock, all held by
  MGE Energy (the combined filing's cover says so); it is not a second class of MGEE and is not added. Check against the
  equity note of the same 10-Q: 37,780,751 shares at 2026-06-30 (36,541,849 at 2025-12-31, plus 990,099 sold in the
  2026-05-06 offering, plus the Stock Plan and the ATM: 154,321 ATM shares to 2026-06-30). **The forward sale agreements of
  2026-05-06:** 2,310,232 shares sold forward to Morgan Stanley, Bank of America and JPMorgan at an initial forward price of
  $72.9094, settleable through January 2028, expected net proceeds about $168.4M on full physical settlement (10-Q, Footnote
  6.c; 8-K of 2026-05-08, accession `0001193125-26-214717`). They are not outstanding and are not in the count; on full
  settlement the count would be 40,094,244 and net debt would fall by about $168.4M. Since the forward price ($72.91) is
  within 2% of the price used, settlement is nearly neutral to every per-share figure below; the diluted figure is shown
  beside where it matters.
- **Market cap:** 37,784,012 × $74.24 = **$2,805.1M**.
- **Sovereign for the earnings currency (USD):** **5.29%**, US Treasury daily par yield curve, 30-year, 10/22/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-24, accession `0001193125-26-067036` (Items 1, 1A, 2,
  5, 7, 8 with Footnotes 9, 14, 22; the combined MGE Energy and MGE report); 10-K for FY2022, accession
  `0000950170-23-003632` (segment table for 2020 to 2022 only); 10-Q for the quarter to 2026-06-30, accession
  `0001193125-26-333969` (cover, balance sheet, equity statement, Footnote 6 on equity); proxy (DEF 14A) filed 2026-04-02,
  accession `0001161728-26-000005`; 8-Ks of 2026-05-08 (`0001193125-26-214717`, the offering and forwards), 2026-08-05
  (`0001193125-26-334011`, earnings), 2026-08-21 (`0001193125-26-360327`, dividend), 2026-10-05 (`0001193125-26-414025`,
  credit agreements amended and extended to 2031-10-01, one MGE facility raised from $90M to $210M). Ten years of annual
  figures from SEC XBRL company facts (CIK 0001161728), each carried with the accession of the 10-K that filed it, in
  `_research 2026-10-23 MGEE/xbrl_table.py` and its output in the notes file.
- **One figure cross-checked against the filed statement:** cash provided by operating activities FY2025 **$263,234K** in
  the filed Consolidated Statement of Cash Flows (10-K page 59) equals the XBRL fact
  NetCashProvidedByUsedInOperatingActivities for 2025 (accession `0001193125-26-067036`). Also checked: net income FY2025
  $135,889K, capital expenditures $343,220K, depreciation and amortization $114,324K, all equal.
- `python tools/run.py MGEE`: **it failed** ("no overlapping OCF/D&A/capex annual facts. UNRESEARCHED."), because MGE
  Energy tags depreciation as UtilitiesOperatingExpenseDepreciationAndAmortization, which the tool does not read. No line
  of it was used. The arithmetic below was made from the SEC company facts and the filed statements by my own script
  (`xbrl_table.py`), which reads filed numbers and adds none.

**The ten years of annual figures** (USD millions; XBRL, each year from the latest 10-K that filed it):

| Year | Revenue | Net income | Op. cash (OCF) | Capex | D&A | ATC contributions | LT debt issued | LT debt repaid | Dividends paid | Common issued |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 544.7 | 75.6 | 147.9 | 83.7 | 44.6 | 3.0 | 0.0 | 4.3 | 41.8 | 0.0 |
| 2017 | 563.1 | 97.6 | 131.4 | 108.1 | 53.1 | 11.1 | 70.0 | 34.4 | 43.7 | 0.0 |
| 2018 | 559.8 | 84.2 | 153.0 | 212.2 | 56.4 | 5.9 | 100.0 | 24.5 | 45.8 | 0.0 |
| 2019 | 568.9 | 86.9 | 130.5 | 164.0 | 71.6 | 7.8 | 50.0 | 4.6 | 47.8 | 0.0 |
| 2020 | 538.6 | 92.4 | 172.4 | 203.1 | 74.2 | 5.6 | 19.3 | 39.0 | 51.7 | 79.6 |
| 2021 | 606.6 | 105.8 | 137.5 | 153.2 | 77.0 | 4.0 | 100.0 | 4.8 | 54.8 | 0.0 |
| 2022 | 714.5 | 111.0 | 153.7 | 175.0 | 85.5 | 5.2 | 25.0 | 4.9 | 57.5 | 0.0 |
| 2023 | 690.4 | 117.7 | 237.6 | 222.1 | 100.4 | 7.0 | 139.3 | 54.3 | 60.4 | 0.0 |
| 2024 | 676.9 | 120.6 | 277.8 | 236.9 | 108.6 | 4.8 | 50.0 | 5.1 | 63.6 | 31.6 |
| 2025 | 743.7 | 135.9 | 263.2 | 343.2 | 114.3 | 9.5 | 50.0 | 5.3 | 67.6 | 3.75 |

Finance-lease principal paid was $0.9M to $1.5M a year from 2019 (XBRL FinanceLeasePrincipalPayments). Stock pay expensed
was $1.0M to $4.5M a year (AllocatedShareBasedCompensationExpense), a part of it equity-settled (the equity statement's
"Equity-based compensation plans and other": $0.9M in the first half of 2025, $1.1M in the first half of 2026); it is
inside the expenses that make net income and operating cash, and the cash-settled part is paid in operating cash.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would own this regulated utility if the market closed for five years
**[M1997-109]**, and the answer turns on the regulated return and the capital it demands, not on the quote. The market
serves and does not instruct **[M2006-077]**: the price of $74.24 says nothing about value until the facts are read. No
macro forecast enters **[M2000-094]**: I do not forecast rates, gas prices or data-centre demand; the 30-year Treasury
enters only as the yardstick of Q7. Margin of safety **[M1996-084]**: if the case needs pencil and paper it is too close.
Who is paid to tell you: the company's own compensation consultant and the "EPS and assets five-year growth of 7%" line in
the proxy are the company's case for itself, read as such. **Contrary evidence, written down as found** **[M1997-127]**:
(1) owner cash after all capital spending is negative in six of the last ten years; the business has paid its dividend
from borrowing and share issuance, not from cash left over; (2) the 2026 offering and forward sales add 3.3 million shares
(about 9% of the count) within a year, and the capital plan of $1.9B for 2026 to 2030 is larger than the whole
property account was in 2020; (3) the earned return on equity (about 10.7%) is a little below the two Wisconsin
co-owners' (Alliant about 10.9%, WEC about 11.6%); (4) the 2025 PSCW settlement allowed only a 0.15% electric increase for
2026, a reminder that the regulator, not the company, sets the price.

## THE STANDING RULE
Owning a minority stake in a listed utility bought with cash and without borrowing does not put the buyer at risk of ruin;
the rule binds the buyer's financing and sizing, "never going to risk what we have and need for what we don’t have and don’t
need" **[M2012-081]**, **[L2023-005]**. Nothing in the target can call on the buyer. Checked: no buyer leverage is assumed.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**Lines of evidence chosen, and from which Item** (the brief's departure): from **Item 1** (business and segments): the five
segments, the service territory (264 square miles of Dane County for electric, 1,722 square miles in seven counties for
gas), the generation mix and the coal exit, the leased nonregulated plants, the 3.6% ATC stake; from **Item 1A** (risks):
regulatory recovery and the "excess revenue test" on fuel, the earnings-sharing band, customer self-supply and storage, data
centres and the Madison moratorium, tax-credit risk under the IRA and OBBBA, capital-project overruns above PSCW-approved
levels, the holding company's dependence on MGE's dividend under a 55% equity-ratio restriction; from **Item 7** (MD&A):
segment net income, the authorized rate base and ROE by test year, the 2026 to 2030 capital forecast and the project
list, cash flows and the financing plan, the capitalization ratios, the dividend restrictions and covenants.

- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.
  The key variables **[M1998-044]** are three and each is in the filing: (1) the rate base, set by the PSCW in two-year
  test periods (electric average rate base $1,241.5M for 2025, $1,346.3M for 2026, $1,537.9M for 2027; gas $341.4M,
  $375.6M, $393.6M; 10-K Item 7, Rate Matters); (2) the authorized return on common equity (9.7% for 2025, 9.8% for 2026 and
  2027) on an equity component of about 56%; (3) the capital the plan requires ($395M, $580M, $300M, $310M, $315M for 2026
  to 2030, 10-K Item 7, Capital Expenditures) and how it is financed. Earnings are roughly rate base × equity share × allowed
  ROE, plus the leased plants and ATC; the statements tell me what the future statements will look like **[M2008-033]**.
  The speakers' own reading of the field: "when you get an allowed return in the electric utility you’re almost certain of
  earning it, I mean, if you behave yourself" **[M2010-037]**.
- **What could put the ten years out of reach.** Customer self-supply (rooftop solar and batteries) is named in Item 1A,
  but its effect is on volume and rate design under an obligation to serve, not on whether the regulator lets the company
  earn on its rate base; data-centre load is named as an upside and a risk, not part of the base case; the coal exit
  (Columbia, Elm Road to gas by 2032) is a capital programme the PSCW approves project by project. None is a forecast the
  industry's insiders would refuse to write down **[M2006-076]**: the filing itself writes down rate base and return two
  years ahead. The business is not one of rapid technological change in the sense of **[L1993-023]**; it is a slow-changing
  franchise whose economics are set by a commission.
- **Routing.** Not a bank. A holding company read by its parts: electric utility (about 62% of 2021 to 2025 segment net
  income), gas utility (about 13%), the nonregulated energy segment (about 19%, plant leased to MGE on PSCW-approved terms),
  ATC (about 7%). Every part that matters is a regulated or regulator-approved return and is understood on the same tests.
- **VERDICT: IN.** The ten-year economics are a regulated return on a growing rate base, written down in the filing two
  years ahead, inside the circle **[M2012-065]**, **[M2000-037]**, **[M2010-037]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**Competitors.** The FY2025 10-K names **no rival company**: a text search of the 10-K for "compet" finds only the two
interstate pipelines' competition for MGE's gas transport (Item 1, Gas supply). MGE is the franchised distributor in its
territory. **Comparators are therefore a CONVENTION of this run**: WEC Energy Group (CIK 0000783325) and Alliant Energy
(CIK 0000352541), the two Wisconsin utility holding companies under the same regulator (the PSCW) that the 10-K names as
MGE's co-owners and plant operators (Columbia with WPL and WPSC, Elm Road with WEC, West Riverside with WPL; Item 2).
Rationale: the same commission sets their returns, so their filings show what the field earns under this regulator.
Wisconsin Power and Light files with the SEC only inside Alliant's combined report and has no standalone XBRL facts, so it is
read through Alliant; WPPI Energy (an Elm Road co-owner) is a municipal power agency and does not file with the SEC.

- **Test 1, what keeps it standing** **[M1995-038]**: a legal franchise. MGE is the public utility for 264 square miles of
  Dane County (electric, about 170,000 customers) and 1,722 square miles of seven counties (gas, about 180,000); the PSCW
  regulates "rates; terms and conditions of service; [...] financing; the closure of generating facilities" (Item 1A).
  How permanent: as permanent as the franchise and the regulatory compact; MGE was organized in 1896 (Item 1).
- **Test 3, the attacker with money** **[M2011-015]**: no one can build a second distribution grid in Madison; this is
  the railroad case, not the airline case, "You really couldn’t create another railroad" **[M2013-054]**. The real attacker
  is not a rival utility but customer self-supply (rooftop solar, batteries, micro turbines), named in Item 1A; it erodes
  volume, not the franchise, and the filing says the obligation to serve continues.
- **Test 4, pricing power** **[M2005-020]**: the company has no price of its own; every rise goes through a rate case. The
  record of rate cases is the evidence: 4.17% electric for 2025 approved (reduced to 2.63% by the fuel plan); in the
  2026/2027 settlement 0.15% electric for 2026 and 3.63% for 2027, gas 2.77% and 2.04%; authorized ROE 9.7% then 9.8%;
  equity component about 56% (10-K Item 7, Rate Matters). An earnings-sharing band returns earnings above the authorized
  ROE (MGE keeps the first 15 basis points, half of the next 60 goes back, all above that goes back). The ceiling on the
  return is written into the order.
- **Test 5, unit volume**: electric retail sales 3,220.6 million kWh in 2025 against 3,153.8 million in 2024 (+2.1%,
  partly weather), residential customers growing; gas retail therms +14.3% on an 18% colder year (Item 7). Volume is
  weather-driven and slowly growing; no decline found in the years read.
- **Test 6, the low-cost position**: the filing gives no rate comparison with other utilities and I found none; not
  judged. A franchised utility's customer does not choose it on cost.
- **Test 10, widening or narrowing** **[M1999-108]**, **[L2005-010]**: the rate base is widening (electric $1,241.5M for
  2025 to $1,537.9M for 2027) and the authorized return is steady at 9.7% to 9.8%; that is growth of what the walls
  enclose, not of the walls.
- **Test 11, what could destroy, modify or reduce it** **[M2000-014]**: (a) the regulatory climate; Buffett's own
  narrated utility error is exactly this, "I did not anticipate or even consider the adverse developments in regulatory
  returns" **[L2023-011]**; in Wisconsin the record read shows full rate cases approved or settled unanimously and a 55%
  equity ratio required as a dividend condition, nothing like the California or Hawaii cases that row names; (b) customer
  self-supply and storage (Item 1A), the slow change that "can lull you to sleep easier" **[M2014-038]**; (c) capital
  projects above PSCW-approved cost, which "we may not be able to recover" (Item 1A), with three projects already flagged
  as expected to exceed approved levels (Item 7 project table, note (f)); (d) the coal units, 21% (Columbia) and 11% (Elm
  Road) of summer capacity, to be converted or replaced under PSCW approval. None of these is shown by the filings to be
  filling the castle in today.
- **The competitor row** (same metric, own filings, SEC XBRL): return on average common equity, net income to common over
  the average of opening and closing equity.

| Company (CIK) | Years | ROE by year (%) | Average | Accession (latest 10-K read) |
|---|---|---|---|---|
| MGE Energy (1161728) | 2016 to 2025 | 10.7, 13.0, 10.6, 10.4, 10.1, 10.6, 10.5, 10.6, 10.2, 10.7 | 10.7% | `0001193125-26-067036` |
| Alliant Energy (352541) | 2016 to 2025 | 9.5, 11.1, 11.7, 11.4, 11.3, 11.3, 11.2, 10.8, 10.0, 11.3 | 10.9% | `0000352541-26-000007` |
| WEC Energy Group (783325) | 2016, 2017, 2020 to 2025 | 10.6, 13.0, 11.5, 11.9, 12.4, 11.2, 12.3, 11.6 | 11.6% | `0000783325-26-000018` |

  WEC's 2018 and 2019 could not be computed (its common-equity tag stops at 2017 and the tag that replaces it includes
  noncontrolling interest from 2020, which understates its ROE slightly); flagged. All three earn about 10% to 12% on
  equity in every year of the decade, the 2017 spike in two of them being the year of the federal tax-rate change. Over the
  same decade MGE's capital spending was 1.05 times its operating cash (sum $1,901.6M against $1,805.0M), WEC's 1.07 times
  for 2016 to 2022 (its capex tag changes after 2022; not read further); Alliant's ratio from XBRL is distorted by a
  classification I did not read and is not used. MGE earns a little less on equity than its two neighbours.
- **The parts table** (segment net income, the measure the filer reports by segment, 2021 to 2025; 10-K FY2022 and FY2025,
  Footnote 22; **CONVENTION of this run**: segment net income stands in for operating profit because the filer reports no
  segment operating income; rationale: the section B threshold needs a profit share and this is the only one filed):

| Part | Share of five-year segment net income | Castle | Decides |
|---|---|---|---|
| Electric utility | $365.3M of $591.0M, 61.8% | franchise, regulated return | **yes, more than half** |
| Gas utility | $77.8M, 13.2% | franchise, regulated return | no |
| Nonregulated energy (Elm Road, WCCF leased to MGE) | $114.8M, 19.4% | lease to MGE on PSCW-approved terms | no |
| Transmission (ATC 3.6%, ATC Holdco 4.4%) | $39.6M, 6.7% | FERC-regulated transmission | no |
| All other | -$6.6M | n/a | no |

- **The field's returns over the last full cycle, judged in words.** The durable players in this field (MGE and the two
  Wisconsin co-owners) earned ordinary returns on equity, about ten to twelve percent, in every year of the decade, on the
  evidence of their own filings. The rows send a standing castle that protects only ordinary returns to OUT, with one
  named exception, a return set by a regulator, carried to Q3 as a second best (Q2, What it rules OUT), on the rows
  "there’s no way we get rich on our utility investments. But there’s no way we get poor, either" **[M2009-104]** and "We
  expect only that these businesses have reasonable expectations of earning decent returns on the incremental sums they
  invest" **[L2009-012]**. This castle's return is set by the PSCW (authorized 9.7% to 9.8%), so it is the exception, not
  an OUT; the weighing goes to Q3.
- **VERDICT: IN.** The deciding part's castle (the electric franchise) stands on law and on the impossibility of a second
  grid **[M2013-054]**; its returns are ordinary and set by a regulator, the stated exception carried to Q3 as a second
  best **[M2009-104]**, **[L2009-012]**; the regulatory climate is the threat to watch **[L2023-011]**, and on the record
  read it is not filling the castle in.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M1995-051]**: on equity, 10.1% to 10.7% in every year 2016 to 2025 except
  2017 (13.0%, the tax-rate change), against an authorized 9.7% to 9.8%. On total capital (net income plus interest after
  tax at a 27.2% combined federal and Wisconsin statutory rate, over long-term debt plus short-term debt plus equity):
  2025, $135.9M + $33.8M × 0.728 = $160.5M over average capital of about $2,140M, **about 7.5%**. A fair return, not a high
  one; the regulator sets it so **[M2009-104]**.
- **Reinvestment to stand still and to grow** **[L1999-024]** is the question this business answers worst. Capital
  spending exceeded depreciation by a wide margin in every year read (2025: $343.2M against $114.3M, three times), and
  over 2016 to 2025 capital spending ($1,901.6M) exceeded the whole of operating cash ($1,805.0M) before a dollar of
  dividends. The plan for 2026 to 2030 is $1,900M, about $380M a year against operating cash of $263M in 2025 (Item 7).
  This is the class the 2011 letter names: of "our regulated utilities, for example", it says they "fail it because
  inflation places heavy capital requirements on them" **[L2011-019]**. The spending is not optional
  under an obligation to serve and a coal exit approved project by project.
- **What the added capital earns** **[M2014-086]** ("measured by the operating earnings after depreciation"): from 2020 to
  2025 net income rose $43.5M ($92.4M to $135.9M) while common equity rose $327.9M ($976.0M to $1,303.9M): **about 13%
  on the added equity**. On added total capital: net income plus after-tax interest rose from about $110M to $160.5M (+$51M)
  while long-term plus short-term debt plus equity rose from $1,548M to $2,190M (+$643M): **about 8% on the added
  capital**. The added sums earn a decent, regulated return; that is the condition the rows set for a capital-heavy business
  **[L2009-012]**.
- **The growth arithmetic and its caps.** Earnings growth is bought, not free: each dollar of growth needs new capital at
  about the regulated return, roughly half of it borrowed and the rest retained or issued. The rows grade this business
  second, "as the second-best choice, still a good choice" **[M2018-055]**;
  the growing utility's reinvestment figures are liked where "we have such confidence that the reinvested money is
  going to do exceptionally well" **[M2014-088]**, while the best business is the one that needs little capital to grow
  **[M1998-081]**.
- **WEIGHS FOR, as a second best and not as the best:** the added capital earns a decent regulated return (about 8% on
  total capital, about 13% on added equity), which is what the rows ask of a capital-heavy business **[L2009-012]**,
  **[M2018-055]**; against it, the reinvestment is compulsory and consumes all the operating cash **[L2011-019]**. (The
  "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them, before the income account** **[M2025-032]** (USD millions, year end; SEC XBRL,
  each year from the latest 10-K that filed it; 2025 and 2024 read on the filed balance sheet, 10-K page 60):

| Year end | Total assets | PP&E net incl. CWIP | Regulatory assets (noncurrent) | Cash | Receivables | LT debt incl. current | Short-term debt | Common equity | Retained earnings | Debt / (debt + equity) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 1,801.1 | 1,282.1 | 158.5 | 96.0 | 39.9 | 387.1 | 0.0 | 724.1 | 373.0 | 35% |
| 2017 | 1,855.2 | 1,341.4 | 142.6 | 108.0 | 42.3 | 422.6 | 4.0 | 778.2 | 426.9 | 35% |
| 2018 | 1,988.6 | 1,509.4 | 145.4 | 83.1 | 43.6 | 497.9 | 13.0 | 816.6 | 465.7 | 38% |
| 2019 | 2,081.7 | 1,642.7 | 134.3 | 23.5 | 40.5 | 543.4 | 0.0 | 855.7 | 504.7 | 39% |
| 2020 | 2,253.7 | 1,769.4 | 142.5 | 44.7 | 41.4 | 524.1 | 52.5 | 976.0 | 545.4 | 37% |
| 2021 | 2,371.9 | 1,878.8 | 107.5 | 17.4 | 46.2 | 619.1 | 5.5 | 1,027.5 | 596.4 | 38% |
| 2022 | 2,517.6 | 1,971.1 | 103.9 | 11.6 | 55.4 | 639.6 | 70.5 | 1,081.7 | 649.9 | 40% |
| 2023 | 2,675.5 | 2,128.2 | 81.6 | 11.1 | 46.7 | 724.0 | 38.0 | 1,140.1 | 707.2 | 40% |
| 2024 | 2,828.0 | 2,287.3 | 36.8 | 21.3 | 51.3 | 769.0 | 0.0 | 1,230.1 | 764.1 | 38% |
| 2025 | 3,155.4 | 2,572.9 | 42.8 | 5.7 | 57.6 | 813.8 | 94.5 | 1,303.9 | 832.4 | 41% |

  What moved and why: property grew from $1,282M to $2,573M (doubled in nine years) and was paid for by debt (long plus
  short from $387M to $908M) and equity (from $724M to $1,304M, of which retained earnings $459M and new shares about $115M
  in 2020, 2024 and 2025). The cash pile of 2016 and 2017 (about $100M) was spent by 2019 and the company now runs on
  commercial paper. The noncurrent regulatory assets fell from $158M to $43M, so less of the balance sheet is a claim on
  future rates than ten years ago, a good sign. Receivables moved with revenue (about 7% to 8% of revenue each year). No
  goodwill (the company has bought plant interests, never companies). The prepaid pension asset was $165.0M at 2025 (plans
  overfunded; the 10-K says no required contributions for 2026). What the balance sheet says plainly: the business does not
  fund its growth from its own cash; debt and new shares carry it, at a steady debt share of about 35% to 41%. At
  2026-06-30 (10-Q): long-term debt $879.1M plus current $20.5M plus short-term $34.8M, cash $16.6M, equity $1,440.5M after
  the May offering.
- **The real costs** **[L2015-004]**: depreciation is a true cost here, and capital spending has run at two to three times
  it in every recent year; depreciation is taken as the maintenance proxy only where Q7 needs a maintenance case
  **[M1998-127]**, said so there. Stock pay is small ($1.0M to $4.5M a year, expensed). No restructuring charges. **AFUDC
  equity** is non-cash income booked during construction ($6.2M in 2025, $5.7M in 2024; XBRL
  PublicUtilitiesAllowanceForFundsUsedDuringConstructionCapitalizedCostOfEquity), about 4% to 5% of net income; operating
  cash does not contain it, which is one reason owner cash, not net income, is used at Q7. **Tax-credit transfers**: $18.5M
  (2024) and $10.9M (2025) of operating cash came from selling renewable tax credits to other taxpayers (Item 7, cash
  flows); the OBBBA phases such credits out (Item 1A), so this cash is not permanent. **Deferred taxes** are not hidden
  equity: "I don’t think I would look at that as a hidden form of equity" **[M2015-030]**; the regulator passes their benefit
  to the customer (same row).
- **EBITDA in the filer's mouth**: no instance of "EBITDA" in the 10-K, the 10-Q, the proxy or the 8-Ks read (text search),
  and no adjusted earnings figure. No earnings guidance found in the filings read (search of the 10-K, 10-Q and the
  earnings 8-K for "guidance"; the 8-K's press-release exhibit was not read). EPS is one pay metric (20% of the annual
  incentive, target $3.43, actual $3.72; proxy), carried to Q5 and Q6 as a pay design fact, not as public guidance.
- **What the accounts say of management's character**: plain, conservative presentation; segment results reconcile to the
  consolidated statement; the noncontrolling-interest structure of the leased plants is explained in the filing itself;
  PwC has audited since 1993 with one critical audit matter (regulatory assets and liabilities), the expected one.
- **VERDICT on the accounts: no confusion, no suspicion; WEIGHS FOR.** The figures can be read **[M2025-032]**; the real
  costs are in them and the non-cash items (AFUDC equity, tax-credit sales) are disclosed and can be taken out. The recast
  earnings feed Q7 as owner cash from the cash-flow statement, not as net income.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** Jeffrey M. Keebler, Chairman, President and CEO since 2018-10-01, an officer for fourteen years and with the
  company for almost three decades (10-K, executive officers; proxy); CFO Jared J. Bushek since 2023-03-01, an officer for
  ten years. An inside, long-tenured management of a single-territory utility.
- **The two yardsticks** **[M1994-008]**. (1) How well they run it, against the hand dealt: the hand is a regulated
  franchise in a growing college-and-government city; the record is an earned ROE at or slightly above the authorized
  return in every year read (10.1% to 10.7% against 9.7% to 9.8% authorized), electric reliability and gas safety in the
  top decile of the national survey and customer satisfaction 4.62 and 4.64 of 5 (proxy, 2025 incentive table), and two
  rate cases settled or approved without a reported fight (the 2026/2027 settlement was unanimous). Against the two
  Wisconsin co-owners under the same regulator it earns a little less on equity (10.7% against 10.9% and 11.6%; Q2). (2) How
  they treat the owners: read in the proxy, "see how they treat themselves versus how they treat the shareholders"
  **[M1994-009]**: CEO total pay $3.61M in 2025 ($2.13M in 2024), a pay ratio of 25.5 to 1, no options, no related-person
  transactions since 2025-01-01 (proxy, Related Person Transactions).
- **The tells of dishonesty** (Q5's list): no too-good-to-be-true claims found; no adjusted earnings, no EBITDA, no
  earnings guidance found in the filings read (Q4); the reports state the bad news in the risk factors in plain terms
  (projects expected to exceed approved cost, the excess-revenue test on fuel, the earnings-sharing band that returns
  excess earnings to customers). The CEO's letter is promotional in tone (fifty years of dividend increases, "nearly $2
  billion in projected capital investment") but says nothing the filings contradict. The make-the-numbers habit carried
  from Q4: EPS is a pay target (20% of the annual incentive; target $3.43, actual $3.72) and cumulative EPS and average
  ROE drive the performance units; this is a pay design, not public guidance, and is weighed at Q6. Integrity is applied
  on doubt alone **[M2013-088]**; I found nothing that raises a doubt.
- **Love of the business.** The officers are career utility people promoted from inside; the CEO's own holding is small
  (8,991 shares owned outright, about $0.67M at $74.24, plus 22,974 restricted units and 4,829 deferred units; proxy), a
  little under one year's pay. A holding of
  less than a year's pay is weak evidence either way.
- **Ability** enters as a weight on value, not as a gate **[M1999-104]**, and the business needs less of it than most:
  "If you have a big enough moat, you don’t need as much management." **[M1999-106]**. The weight is modest here because
  the regulator sets the return and the plan; the place management can fail is cost control on the capital projects (three
  already flagged above approved cost) and the regulatory relationship.
- **VERDICT on integrity: IN** (no tell found; nothing in the habits carried from Q4 leaves a doubt) **[M2013-088]**,
  **[M2005-003]**. **Ability WEIGHS FOR, modestly:** a clean regulated record and top-decile reliability, a return a little
  below the neighbours', in a business that needs ordinary management **[M1994-008]**, **[M1999-106]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- **The retention test** **[R1995-009]**, **[M1998-110]**, market leg. Five years, 2020-12-31 to 2025-12-31: retained
  earnings rose $287.0M ($545.4M to $832.4M) and new shares brought in $35.4M (2024 and 2025), $322.4M kept or added; the
  market value rose from $2,532.5M (36,163,370 shares on the 2021-01-31 cover × $70.03) to $2,865.6M (36,541,849 shares ×
  $78.42), +$333.1M: **about $1.03 of market value per dollar kept**. Ten years, 2016-12-31 to 2025-12-31: retained
  earnings +$459.4M and new shares about $115.0M (2020, 2024, 2025), $574.4M; market value $2,263.9M (34,668,370 × $65.30)
  to $2,865.6M, +$601.7M: **about $1.05 per dollar**. Year-end closes are the aggregator's (flagged). The test is passed by
  a hair on the market leg and the result swings with the end dates (from the 2021 year-end close of $82.25 it fails). The
  intrinsic leg needs Q7 and is written back there.
- **Buybacks**: none. The company does not repurchase its stock (no repurchase in the cash-flow statements read; in 2025
  the Stock Plan bought shares in the open market for participants, which is not a company buyback; 10-K Item 7). Nothing
  to test against **[L1999-023]**; the line Q6 owes to Q7's bottom is therefore moot. *(Written back from Q7, committed
  with it: the bottom of the range is $57.93 a share; no repurchase exists to set against it. The 2026 shares were sold at
  about $72.91 to $73, above the top of the central range ($68.46), so on that range they were sold above value.)*
- **Issuance and deals** **[M1995-001]**. New shares: $79.6M in 2020, $31.6M in 2024, $3.75M in 2025; in 2026 an
  underwritten offering (990,099 shares, net about $72.2M), forward sales of 2,310,232 shares (about $168.4M expected),
  the ATM ($11.5M to 2026-06-30) and the Stock Plan; shares outstanding from 34.67M (2016) to 37.78M (2026-07-31), 40.09M
  if the forwards settle in full, about **+16% in ten years**. Issuance is planned with the regulator's capital structure (the
  PSCW sets a 56% equity component and restricts MGE's dividends below a 55% equity ratio), so it funds the rate base rather
  than promotion; but the serial-issuer row is plain, "we have never invested in companies that are hell-bent on issuing
  shares" **[L2014-015]**, and section VI carries serial issuance as an unresolved candidate STOP. I weigh it against, not
  as a STOP: the pace is about 1.5% a year and the purpose is stated and regulated. Whether the shares were sold above or
  below value is read at Q7: shares sold at about $73 are good for the remaining owners if value is below that, and bad if
  above **[M1995-001]**. **Deals**: no company bought, no stock deal; the RockGen purchase (33.4% of an existing gas plant,
  about $203M, cash, pending PSCW approval, expected close 2027) is a plant purchase inside the capital plan. The one Part A
  STOP (an all-stock deal in undervalued stock **[L2009-019]**) does not arise.
- **Dividends and the use of cash.** Fifty consecutive years of increases (proxy); dividends of $67.6M in 2025, about half
  of net income, paid in years when owner cash after all capital spending was negative, while the company borrowed and sold
  shares. The rows' test is whether a retained dollar becomes more than a dollar **[M1998-033]**, not a payout ratio, "the
  idea of paying out 20 percent of your earnings, or 10 percent, or 30 percent of earnings in dividends strikes us as nuts"
  **[M2000-051]**; a company that pays out half its earnings and then issues shares to replace the money pays its owners
  with their own capital and an underwriter's fee in between. Weighs against, mildly: in a regulated utility the dividend is
  the convention of the field and the regulator's capital structure governs the mix.

**Part B, the pay, the board and the owners.**
- **Pay tied to what the person controls** **[M2003-019]**: the annual incentive is 40% metric-specific (EPS 20%,
  residential and commercial satisfaction 5% each, electric reliability and gas safety 5% each), 30% corporate goals, the
  rest individual, capped at 150% of target; the long-term plan is half performance units (50% average ROE, 50% cumulative
  EPS, a relative TSR modifier, 2025 to 2027) and half time-based restricted units (proxy, CD&A). "you get what you reward
  for" **[M2016-083]**: cumulative EPS in a regulated utility rises with the capital put in at the allowed return, so half of
  the performance units reward growth of the rate base whatever it costs the owners in new shares; the ROE half and the
  reliability and satisfaction metrics are things the managers control. A compensation consultant (FW Cook) and a peer group
  set the levels (proxy). Weighs mildly against.
- **The board**: ten directors, eight independent, a Lead Independent Director (since 2009 on the board), the chairman is
  the CEO. "I've seen how hard it is to replace a mediocre CEO if that person is also Chairman." **[L2014-026]**: weighs
  against, mildly, since I have no evidence that the CEO is mediocre.
- **Owners as partners**: directors and executive officers as a group own 73,906 shares outright (about $5.5M at $74.24,
  about 0.2% of the company), with 69,369 restricted units on top (proxy, beneficial ownership); the three newest directors
  own 734 to 924 shares each; directors receive an annual equity grant worth $85,000. The rows prefer directors who bought
  "with their savings, rather than simply having been the recipients of grants" **[L2019-008]**; the proxy does not say
  which shares were bought and which granted. No guidance, no selective disclosure found.
- **WEIGHS: Part A AGAINST, mildly** (retention barely a dollar for a dollar on the market leg, steady issuance while
  paying out half the earnings; no buyback to test; no stock deal) **[R1995-009]**, **[L2014-015]**, **[M2000-051]**.
  **Part B AGAINST, mildly** (EPS-weighted pay in a business where EPS grows by adding capital; combined chairman and CEO;
  small insider ownership) **[M2016-083]**, **[L2014-026]**, **[L2019-008]**.

## Q7 — WHAT IS IT WORTH? STOP.
Q1 to Q4 are IN and Q5 to Q6 recorded; Q7 is reached. Script and output: `_research 2026-10-23 MGEE/q7_value.py` and
`q7_output.txt` (filed inputs only, USD millions).

**The basis.** The deciding part (electric, Q2 parts table) earns a return the PSCW allows on its invested capital, so
Q7's text for the regulated utility governs: the central figure is the **equity-only** basis, owner cash after interest
and after the company's own tax, against the market value of the shares ($2,805.1M), with the long-term debt raised over
the window to fund the fixed assets credited against the spending it funded, up to the regulator's allowed debt share
**[L2017-012]**, **[L2010-012]**, **[M2014-086]**. Allowed debt share: 43.94% (one minus the 56.06% common-equity
component of the 2025 test year; 10-K Item 7, Rate Matters). The **all-equity** figure is shown beside and never decides.
The tax is the company's own as filed (see the note on credits below).

**The cash input** (five-year window 2021 to 2025, owner cash as the cash-flow statement gives it, never net income):
| | 2021 | 2022 | 2023 | 2024 | 2025 | Average |
|---|---|---|---|---|---|---|
| Owner cash after all spending (OCF less capex, ATC contributions and finance-lease principal, plus other investing) | -20.9 | -27.7 | 6.2 | 35.0 | -88.8 | **-19.2** |
| Owner cash after maintenance only (OCF less depreciation and lease principal, plus other investing) | 59.3 | 67.0 | 134.9 | 168.1 | 149.6 | **115.8** |
| Growth spending (capex less depreciation, plus ATC contributions) | 80.2 | 94.7 | 128.7 | 133.1 | 238.4 | 135.0 |

- **(e), the maintenance case central.** The filing gives no split of maintenance and growth spending, but it lists the
  growth projects by name (new solar, wind, battery, the RockGen purchase), and depreciation is the rows' accepted proxy for
  the spending that keeps a business in place, "not inappropriate in most companies to use as a proxy for required capital
  expenditures" **[M1998-127]**; for a utility, spending equal to book depreciation holds the rate base flat, which is the
  no-growth case. So the central case is owner cash after maintenance only, $115.8M a year, and the growth spending is
  charged against the growth it buys; the all-spending case is shown beside.
- **The debt credit.** Long-term debt issued over the window $364.3M, repaid $74.4M, **net raised $289.9M**. Against all
  capital spending the cap is 43.94% × $1,130.4M = $496.7M (not binding); against the growth spending alone the cap is
  43.94% × $644.6M = $283.2M (binding). In the growth case the credit is $283.2M, so the **equity-funded growth spending is
  $78.4M a year** ($135.0M less $56.6M). In the all-spending case the credit is the net $289.9M ($58.0M a year); the gross
  $364.3M is shown beside. Short-term debt rose by $42.0M over the window and is not credited (the rule names long-term
  debt; MGE refinanced $90M of it into notes in January 2026).
- **(a), cycles.** The first year is touched by an event the filer names: 2021's $36.5M working-capital draw is tied in the
  FY2022 10-K to the February 2021 gas-price spike ("Natural gas costs increased significantly [...] in February 2021
  related to extreme weather conditions"; accession `0000950170-23-003632`). Its recovery falls inside the same window
  (2023 and 2024 operating cash), so the five-year average carries both the draw and its reversal and the literal window is
  kept; the variant with the draw added back is shown beside. The end-to-end growth of owner cash is distorted by it, which
  is one reason the shown rate is absurd (next line).
- **(b) and (f), the growth.** Owner cash after maintenance grew 26.1% a year from 2021 to 2025 end to end; carried ten
  years it would need about $1,173M a year, against $307M at the highest share of sales the business earned in the window
  (24.8%, 2024) applied to sales grown ten years: an absurdity **[M1999-067]**. The rate is cut to the business's own
  sales growth over the window, **5.23% a year** ($606.6M to $743.7M), below the discount rate, carried ten years, then zero
  nominal growth with the growth spending stopping **[M1997-095]**. Net-income growth (6.47%) is shown beside. The
  all-spending series changes sign, so by (b) that case is the no-growth case alone, said so.
- **(c), (d).** No acquisition of a business in the window; the plant interests bought (West Riverside 2023 and 2024) are
  inside capital spending. The RockGen purchase (an asset purchase agreement signed in February 2026 for 33.4% of an
  existing gas plant, about $203M in cash, pending PSCW approval, expected to close in 2027) is a plant interest, capital
  spending under (c) and inside the 2026 to 2030 forecast; it falls after the window and is not valued beside, since it
  enters the rate base at the return the regulator sets. Working capital is inside operating cash, so it is counted.
- **Whose tax.** The company's effective rate is low (13.3% in 2025, 8.1% in 2024) because of renewable production and
  investment tax credits, and $18.5M (2024) and $10.9M (2025) of operating cash came from selling credits. I apply owner
  cash at the tax as filed, not at the statutory rate, because in a regulated utility the credits reduce the customer's
  rates rather than enlarge the owner's return ("that helps our customer and it doesn’t help us, basically", said of a
  utility's deferred taxes, **[M2015-030]**); the variant without the credit-sale cash is shown beside. This reading is
  confessed under "What in the framework was wrong or unclear".

**The range (equity-only, central), discounted at 5.29%:**
| Case | Value | Per share | Expected return at $74.24 |
|---|---|---|---|
| No growth, owner cash after maintenance $115.8M forever | $2,189M | **$57.93** | 4.13% |
| Growth at 5.23% ten years, equity-funded growth spending $78.4M charged (growing with it), then no growth | $2,587M | **$68.46** | 4.97% |

**Value range: $57.93 to $68.46 a share against $74.24.** Width 1.18 to 1. Beside (none decides):
- all-spending case with the net debt credit, owner cash $38.7M, no growth (sign changes): $19.38 a share, a 1.38% return;
  with the gross issuance credited, $26.82;
- growth at the net-income rate (6.47%) instead of sales: top $76.61 a share, a 5.42% return at the price;
- the 2021 working-capital draw added back: $61.58 to $74.02, a 5.28% return in the growth case;
- without the tax-credit sale cash: $54.97 to $63.97;
- all-equity basis (owner cash before interest, after-tax interest at 27.24% added back, less net debt of $937.3M:
  long-term debt $899.6M and short-term $34.8M less cash $16.6M at 2026-06-30, plus finance leases $19.6M at 2025 year end;
  operating leases left out): $43.97 (no growth, maintenance) and $45.96 (growth, all growth spending charged, no credit);
  all-spending all-equity owner cash is $2.4M a year and the value is negative, -$23.58 a share;
- the literal net-income window (not used, operator rule 5): average net income $118.2M at 5.29% is $59.12 a share.

**The floor is tested first** **[M2003-149]**. No case in the range, and no case beside it, earns the floor of about ten
percent at $74.24: the central cases return 4.13% and 4.97%, the most generous variant 5.42%. "we don’t want to buy equities
where our real expectancy is below 10 percent" **[M2003-149]**. The price is also above the top of the central range,
which closes OUT through the same floor convention. The width test does not arise. The bond comparison belongs to Q8, but
the arithmetic is plain here: the best case barely exceeds the 30-year Treasury's 5.29%, and "if government bond rates were
2 percent, we’re not going to buy a business to earn 3 or 3 1/2 percent expectancy over the years" **[M2007-095]**.

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and the two averaged:
no-growth $30.64, growth $28.29, **fair price $29.47 a share** on the equity-only basis (central for a regulated utility,
debt raised for the fixed assets credited up to the 43.94% allowed debt share), after the company's own tax. Beside it, on
the **all-equity basis, $6.01 a share** (no-growth $11.58, growth $0.45). With the forward sales settled in full (2,310,232
more shares, $168.4M more cash) the equity-only fair price is $31.97. No cheap price is reported. That the growth case is
worth less than the no-growth case at ten percent (but more at 5.29%) says the growth bought earns between the two rates on
the owners' money, as Q3 found.

**Written back to Q6 (the line Q6 owes to Q7).** Buybacks: none, so there is nothing to test against the bottom of the
range ($57.93). Issuance: shares sold in 2026 at about $72.91 to $73 (the offering and the forward price) are above the top
of the central range, so on this range they were sold above value, which by the rows' own test favours the remaining owners
**[M1995-001]**; it does not change Q6's weighing, which rests on the payout-then-issue pattern.

- **VERDICT: OUT.** The floor tested first: no case of the range earns about ten percent at $74.24 (central 4.1% to 5.0%,
  the most generous variant 5.4%) **[M2003-149]**, and the price is above the top of the range ($68.46) **[L2013-012]**;
  nothing here screams **[M2009-005]**. "no way we get rich on our utility investments" **[M2009-104]**, and at this price
  the owner would not earn the floor either.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT). Facts found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT at Q7** (the floor tested first): the equity-only value range is **$57.93 to $68.46 a share** at the 30-year
Treasury's 5.29%, against **$74.24**; no case of the range earns about ten percent at the price (4.1% to 5.0% centrally,
5.4% at the most generous variant). Q1 IN, Q2 IN (franchise castle, regulator-set ordinary returns carried to Q3 as a second
best), Q3 WEIGHS FOR as a second best, Q4 WEIGHS FOR, Q5 integrity IN and ability WEIGHS FOR modestly, Q6 AGAINST mildly in
both parts. Reporting figures: fair price **$29.47** equity-only (central for a regulated utility), **$6.01** all-equity
beside.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged; operator rule 2 **[M1997-127]**.)*
- **Q8 (the alternatives).** The 30-year Treasury yields 5.29% (10/22/2026, Treasury); the central cases of Q7 return 4.13%
  and 4.97% at the price, the most generous variant 5.42%. The dividend yield at the price is 2.74% ($0.5083 a quarter,
  8-K of 2026-08-21, accession `0001193125-26-360327`).
- **Q9 (debt and exposures).** Long-term debt $899.6M at 2026-06-30 (including $20.5M current), commercial paper $34.8M,
  cash $16.6M (10-Q). Maturities at 2025 year end: $21.6M within one year, $80.6M in two to three years, $62.0M in four to
  five years, $653.8M after five (10-K, contractual obligations). Interest cover in 2025, pre-tax earnings plus interest over
  interest: ($156.7M + $33.8M) / $33.8M, about 5.6 times. Credit agreements amended and extended to 2031-10-01, one MGE
  facility raised from $90M to $210M (8-K, `0001193125-26-414025`); covenant ceiling 65% debt to capitalization, actual
  41.1% (MGE Energy) and 44.5% (MGE) at 2025 year end; no borrowing defaults or accelerates on a rating downgrade (10-K
  Item 7). Derivative collateral posted $1.8M at 2025 year end. Firm purchase obligations $718.0M and construction
  obligations $296.9M (10-K). A single-territory utility: the rows' warning that "A catastrophic event can render a single
  utility insolvent" applies to its shape **[L2005-019]**. MGE's dividends to MGE Energy are barred if its equity ratio
  falls below 55% (58.0% at 2025 year end). Common equity is about 59% of capitalization (10-K): not "little or no debt" in
  the acquisition-criteria sense **[R1997-001]**, a criterion the rows state for whole businesses.
- **Q12 (how the money is made).** Coal remains a material fuel (Columbia 21% and Elm Road 11% of summer capacity; coal
  1.75 million MWh of 3.73 million MWh delivered in 2025, 10-K Item 1), with conversion to gas planned by 2030 to 2032. None
  of the businesses Q12 names (casinos, tobacco, distributor-loading schemes, gambling dressed as investing) is involved.
- **Integrity (Q5)** was reached and answered IN; no integrity fact is carried unjudged.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template copy and the research folder were made before the first
      tool or EDGAR call); written question by question; committed after each question with a pathspec of my two paths
      (commits 033db7d6 Step 0 to Q1, 07b98d80 Q2, b1d8e6a7 Q3, af1c38b3 Q4, 4e1fe9d4 Q5, 2df62d33 Q6, 4f94a1bd Q7, and the
      close). One append attempt for Q2 failed in the shell and wrote nothing; it was redone from a draft in the research
      folder.
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's. The fold into the
      register is the dispatcher's (operator rule ten); this run binds nothing until it is in the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One `ls` of `Test Runs/` filtered to
      2026-10-23 showed ten other same-day file names; commit subjects and a memory index line were in the session context.
      All declared under contamination at the top; none used.
- [x] Every v5 id resolves (`_research 2026-10-23 MGEE/check_ids.py`, run before the close commit; see its output in the
      notes); every filing fact carries its accession; numbers are filed or computed from filed numbers, or are labelled.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 are NOT REACHED; nothing after it is a
      clearance.
- [x] Owner cash from the cash-flow statement after every real cost, never a net-income proxy (the net-income window is
      shown once, labelled "not used"); the sovereign from the US Treasury; the price and the year-end closes are an
      aggregator's, flagged.
- [x] Contrary evidence written down as found (foundations); facts for later questions are under AFTER THE STOP; no
      integrity fact is left unjudged.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` produced nothing usable (it failed on the depreciation tag); none of its output was used. The
      arithmetic came from my own scripts reading filed numbers.
- [x] `python tools/check_framework.py` PASS before the close commit (result recorded in the notes file).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The regulated-utility rule and specific (e) do not say how they combine.** The utility paragraph credits long-term
   debt "against the capital spending it funded"; (e) makes the maintenance-only case central and charges growth spending
   against the growth it buys. I applied the credit to the growth spending only (capped at the allowed debt share of
   capex less depreciation), on the reading that a flat rate base needs no new debt; the credit against all spending is shown
   beside. The two readings give $78.4M and $77.0M of equity-funded growth spending a year, a small difference here, but
   the text should say which. 2. **Whose tax, for a utility with tax credits.** The carryforward convention computes owner
   cash at the statutory rate where credits run out inside ten years; in a regulated utility the credits pass to customers
   through rates, so restating at the statutory rate would understate the owner's cash. I used the tax as filed and showed
   the case without the credit-sale cash beside; the text does not address this. 3. **"Net" or "gross" debt raised.** The
   utility paragraph says "the long-term debt raised over the window"; refinancing raises debt that funds no new asset. I
   credited the net ($289.9M) and showed the gross ($364.3M) beside. 4. **The allowed debt share for a holding company with
   a nonregulated segment.** The PSCW's 56.06% equity component applies to MGE; MGE Energy's consolidated debt also carries
   the leased plants' secured notes. I used the regulator's share for the whole, as the text directs, and say so. 5.
   **`tools/run.py` fails on utilities** that tag depreciation as UtilitiesOperatingExpenseDepreciationAndAmortization; the
   tool reported UNRESEARCHED, which is a tool gap, not a fact about the company. 6. **The comparator when the 10-K names no
   rival.** The brief and the template assume named rivals; a franchised utility has none, so the comparators were a
   CONVENTION of the run, chosen as the co-owners under the same regulator.
