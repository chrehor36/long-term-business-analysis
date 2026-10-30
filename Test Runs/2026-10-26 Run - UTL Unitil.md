# Company Run — Unitil Corporation (NYSE: UTL) — 2026-10-26
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-26: the operator does not hold this name (`PORTFOLIO.md` has no UTL row).*

**Dispatch.** A purchase run of record dispatched to a blind analyst on 2026-10-26 under `Screens/_daily/_dispatch_brief.md`,
with two departures stated by the brief: the repository path is `C:\Projects\BRK`, and the lines of evidence were derived by
the analyst from the FY2025 10-K's Item 1, Item 1A and Item 7 (listed under Step 0 below). Working folder:
`Test Runs/_research 2026-10-26 UTL/` (notes, scripts, the ten-year table, the peer table, the Q7 arithmetic).

**Contamination, declared.** Seen by accident and not used: the session context showed the repository's recent commit
subjects (another company's run, TAC), a `git status` listing naming another company's research folder (ARCB) and the
`Screens/_daily/` digest files by date, and memory-index lines that name the queue's state in general terms (counts of
gate-clearers, nothing about this company). The governing framework's own text records that sixteen utilities were run on
2026-10-17 and 2026-10-18 (Q7, The regulated utility); no name or result of any of them was read. No other run file,
holding review, `PORTFOLIO.md`, register, reading list or session-state file was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $55.15 (close 2026-10-23, the last full session before the run; Yahoo chart through `tools/sources.py`,
  an **aggregator, flagged** per operator rule 5, used for the live quote only; the 2026-10-26 intraday print of $55.19
  was not used).
- **Shares by class** from the latest filing's cover: **18,236,674 common**, one class (10-Q for the quarter to
  2026-06-30, filed 2026-08-03, accession `0000755001-26-000029`; `python Screens/cover_shares.py UTL`). Checked: the same
  10-Q's balance sheet shows 18,225,964 shares outstanding at 2026-06-30; no par stock, no treasury shares, so issued equals
  outstanding; the 10,710-share difference is consistent with the at-the-market programme and the stock plan, both
  described in the 10-Q. The 8-Ks filed after the 10-Q (`0000755001-26-000031`, 2026-09-29; `0000755001-26-000033`,
  2026-10-19) report debt only. Preferred stock of $0.2M is carried and ignored as immaterial. Any ATM sales after the
  cover date are unknown (no filing yet covers them) and flagged.
- **Market cap:** $55.15 x 18,236,674 = **$1,005.7M**.
- **Sovereign for the earnings currency (USD):** **5.33%**, the 30-year par yield on the US Treasury daily par yield curve,
  dated 10/23/2026 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the 10-K for FY2025 (filed 2026-02-09, accession `0001193125-26-042983`), Items 1,
  1A, 7 and 8 in full where cited; the 10-Q for the quarter to 2026-06-30 (`0000755001-26-000029`); the proxy (DEF 14A filed
  2026-03-27, `0001193125-26-128263`); the 8-Ks of 2025-08-18 (`0001193125-25-181993`, the underwritten offering),
  2025-11-04 (`0001193125-25-264824`), 2026-02-02 (`0001193125-26-033824`), 2026-07-07 (`0000755001-26-000026`, the
  Aquarion close), 2026-09-29 and 2026-10-19 (above); the ATM prospectus supplement of 2026-02-19
  (`0001193125-26-059567`); and for the earlier years of the cycle the 10-K for FY2022 (`0000950170-23-002696`) and the
  10-K for FY2019 (`0001193125-20-019075`). **One figure cross-checked against the filed statement:** cash provided by
  operating activities, $131.3M for 2025, capital additions $185.1M and depreciation and amortization $88.7M (FY2025 10-K,
  consolidated statement of cash flows), equal to the XBRL facts; and 2021 operating cash of $107.8M in the FY2022 10-K's
  filed statement, equal to the XBRL fact.
- **`python tools/run.py UTL`:** it printed one line, "UTL: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED.", and
  no arithmetic. The arithmetic below was therefore computed by a script in the research folder
  (`scripts/table.py`, output `table_xbrl.txt`) from the SEC company facts, and every figure used in Q4 and Q7 was checked
  against the filed statements of the FY2025, FY2022 and FY2019 10-Ks. Same numbers sooner, no number added.
- **Lines of evidence chosen** (the brief's second departure), from the FY2025 10-K: Item 1, (1) the two segments,
  electric and gas distribution, gas the larger (63% of adjusted gross margin, $199.1M of $313.7M), with the Granite State
  pipeline; (2) cost-of-service regulation with decoupling in Massachusetts and New Hampshire, trackers and step
  adjustments; (3) the 2025 acquisitions of Bangor ($71.4M) and Maine Natural ($86.0M). Item 1A, (4) the regulatory risk,
  including "regulatory proceedings regarding fossil fuel use and system electrification"; (5) the need for outside
  financing; (6) customer retention and distributed generation; (7) the greenhouse-gas commitments whose costs may not
  qualify for recovery. Item 7 and the Note 8 it cites, (8) the allowed returns and capital structures in the rate orders;
  (9) the Massachusetts net-zero gas docket, the GSEP cap cuts and the Maine "Future of Gas" inquiry; (10) capital spending
  ($185.1M in 2025, $221M projected for 2026) and its funding by debt and equity; (11) the non-GAAP adjusted net income the
  MD&A features.

**The ten-year table** (US$ millions, fiscal years to 31 December; XBRL facts, the 2017-2025 operating, investing and
balance-sheet lines checked against the three filed 10-Ks named above):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 383.4 | 406.2 | 444.1 | 438.2 | 418.6 | 473.3 | 563.2 | 557.1 | 494.8 | 536.0 |
| Operating income | 70.2 | 75.4 | 71.2 | 73.1 | 71.4 | 77.8 | 80.5 | 87.1 | 90.6 | 101.2 |
| Net income | 27.1 | 29.0 | 33.0 | 44.2 | 32.2 | 36.1 | 41.4 | 45.2 | 47.1 | 50.2 |
| Operating cash | 68.3 | 86.2 | 78.5 | 104.9 | 75.7 | 107.8 | 97.7 | 107.0 | 125.9 | 131.3 |
| Capital additions | 98.1 | 119.3 | 102.4 | 119.2 | 122.6 | 115.0 | 122.1 | 141.0 | 169.9 | 185.1 |
| Acquisitions, net of cash | nil | nil | nil | nil | nil | nil | nil | nil | nil | 160.4 |
| Depreciation and amortization | 46.6 | 46.9 | 50.4 | 52.0 | 54.5 | 59.5 | 62.6 | 67.4 | 76.1 | 88.7 |
| Interest paid | | 23.0 | 24.6 | 24.1 | 23.7 | 26.0 | 26.0 | 30.9 | 31.2 | 39.3 |
| Stock issued for cash | 1.3 | 33.0 | 1.2 | 1.1 | 1.1 | 45.5 | 1.0 | 1.1 | 1.1 | 73.5 |
| Dividends paid | 20.0 | 20.4 | 21.8 | 22.1 | 22.6 | 23.6 | 25.1 | 26.2 | 27.5 | 30.1 |
| Net utility plant | 883.4 | 971.5 | 1,036.8 | 1,111.5 | 1,193.2 | 1,257.2 | 1,331.7 | 1,420.9 | 1,539.6 | 1,798.5 |
| Long-term debt incl. current | 333.6 | 406.1 | 405.8 | 457.0 | 531.6 | 506.0 | 495.8 | 514.0 | 643.3 | 670.5 |
| Short-term debt | 81.9 | 38.3 | 82.8 | 58.6 | 54.7 | 64.1 | 116.0 | 162.0 | 105.8 | 255.7 |
| Cash | 5.8 | 8.9 | 7.8 | 5.2 | 6.0 | 6.5 | 9.0 | 6.5 | 6.3 | 15.6 |
| Stockholders' equity | 293.1 | 336.8 | 351.3 | 376.8 | 389.2 | 448.5 | 467.6 | 489.3 | 512.5 | 609.6 |
| Retained earnings | 52.2 | 60.8 | 72.0 | 94.1 | 103.7 | 116.2 | 132.5 | 151.5 | 171.1 | 191.2 |
| Goodwill | nil | nil | nil | nil | nil | nil | nil | nil | nil | 4.3 |
| Retirement benefit obligations | 149.0 | 150.1 | 121.5 | 141.9 | 162.3 | 133.9 | 46.8 | 45.6 | 25.5 | 32.9 |
| Shares outstanding, year end (M) | 14.07 | 14.82 | 14.88 | 14.93 | 15.01 | 15.98 | 16.04 | 16.12 | 16.19 | 17.92 |

2019 operating cash includes the Usource divestiture's working-capital effects and 2019 net income a $13.4M pre-tax gain
on that divestiture (FY2019 10-K, `0001193125-20-019075`, cash flow statement). At 2026-06-30 (10-Q): short-term debt
$234.8M, long-term debt $680.4M plus $40.8M current, cash $9.2M, common equity $643.5M.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, and a distribution utility is the kind of asset whose cash comes from the business and not from the next
buyer, so the foundation is met in kind. The market serves and does not instruct **[M2006-077]**: the price of $55.15 is
read only against value at Q7. The margin of safety is an attitude here: "if you have to actually do it on — with pencil and
paper, it’s too close to think about" **[M1996-084]**; a regulated utility earning a set return is the textbook case where
the answer will need a pencil, and that is written down now, before the arithmetic. No macro forecast enters (the interest
rate enters only as the sovereign at Q7). Who is paid to tell you: the company sells shares continuously (an ATM programme
and an underwritten offering in 2025), so its own presentations are the speech of a seller of its stock, and I use only the
filings. **Contrary evidence, written down as found** **[M1997-127]**: (i) owner cash after all spending is negative in
every year of the window (Q4); (ii) the company has sold stock in 2017, 2021, 2025 and 2026 and debt every year, so the
dividend is paid in part from outside money; (iii) the Massachusetts regulator has cut the gas pipe-replacement tracker
cap from 3.0% to 2.5% with "likely" further cuts to 2.0% and 1.5%, and Maine has opened an inquiry into the future of gas
(FY2025 10-K, Note 8); (iv) organic gas customer additions have fallen from about 1,450 in 2018 to about 570 in 2025
(FY2019 and FY2025 10-Ks, MD&A); (v) the general counsel appointed on 2025-10-29 was a New Hampshire utility commissioner
from December 2021 to August 2024 (8-K `0001193125-25-264824`). Each is carried to the question it bears on.

## THE STANDING RULE
A purchase of a small part-interest for cash, with no borrowed money and no instrument that can call for cash, puts the
buyer at no risk of ruin: the rule forbids risking "what we have and need for what we don’t have and don’t need"
**[M2012-081]** and borrowed money, which "has no place in the investor's tool kit" **[L2014-005]**; neither is in play.
Passed, as the buyer's own conduct.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as stated.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**, "a reasonable probability of being able to asses where the business will
  be in 10 years" **[M2000-037]**. Unitil is five "wires and pipes" distribution utilities and one pipeline (FY2025 10-K,
  Item 7, Overview), regulated by three state commissions and FERC under cost-of-service rules: the regulator sets the
  revenue so that the company recovers its costs and earns "a return on their capital investment in utility assets"
  (Item 7, Regulation); energy supply is a pass-through, "the Company’s earnings are not affected by changes in the cost of
  purchased electricity and natural gas" (Item 7, Overview); Massachusetts and New Hampshire sales are decoupled.
- **The key variables and whether they are foreseeable** ("trying to identify the key variables [...] and evaluating how
  predictable they were first" **[M1998-044]**): (1) the rate base, set by the capital the company puts in (net utility
  plant $1,798.5M at end-2025 against $883.4M at end-2016); (2) the allowed return on equity and equity ratio (9.3% to 9.45%
  on about 52% equity in every order the 10-K and 10-Q report: Northern Utilities NH 9.3% and 52%, Northern Utilities ME
  9.35% and 52.01%, Fitchburg electric and gas 9.4% and 52%, Unitil Energy 9.45% in the order of 2026-05-28); (3) the lag
  between spending and rates; (4) the number of customers; (5) the policy of the three states toward natural gas. The first
  four have moved within narrow, filed bands for a decade; the past statements tell me what the future ones will look like
  in shape, which is the test **[M2008-033]**. The fifth is the one that can move the economics of the larger part, and it
  is a question about the castle, carried to Q2 (the framework gives change to Q2; Q1 points to it).
- **Would the insiders write it down?** **[M2000-105]**. For the ten-year view, yes: the companies file multi-year rate
  plans, step adjustments to 2027, a FERC settlement for Granite State running to 2028, and a capital plan; the regulator
  of Massachusetts, the strictest of the three on gas, stated in its order of 2023-12-06 that it "is not intended to
  jeopardize the rate recovery of existing investments in natural gas infrastructure by Fitchburg" (10-K Note 8). What the
  insiders do not write down is the twenty-year future of gas heating in New England; that is Q2's question.
- **Routing.** Not a fast-changing technology; not a bank; a holding company read by its parts (both regulated
  distribution, Q2 below). The doubt rule **[M2002-092]**: I do not doubt that the ten-year economics of a cost-of-service
  distribution utility are inside the perimeter.
- **VERDICT: IN.** The ten-year earning power is set by orders the filings report, and the variable that is not foreseen
  belongs to Q2 **[M2012-065]**, **[M1998-044]**, **[M2008-033]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (Q2, a business of parts; five-year operating profit 2021-2025 computed per segment as segment net
income plus income tax plus interest expense less interest income, from Note 2 of the FY2025 10-K
`0001193125-26-042983` for 2023-2025 and of the FY2022 10-K `0000950170-23-002696` for 2021-2022; US$ millions):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year | Share of the two segments | Castle | Decides |
|---|---|---|---|---|---|---|---|---|---|
| Gas distribution and Granite State pipeline | 45.7 | 50.5 | 56.5 | 61.1 | 75.4 | 289.2 | 66.5% | regulated franchise; read below | **yes** (more than half) |
| Electric distribution | 26.7 | 27.0 | 30.5 | 30.2 | 31.3 | 145.7 | 33.5% | regulated franchise, decoupled | no |

"Other" (holding company, service company, realty) loses money in every year (segment profit -1.1 to -5.7) and is a cost
centre, not a part. The water companies bought on 2026-06-30 have no filed earnings yet (10-Q: no water revenue
recognized). **The file closes on the gas part.**

**The castle questions** ("why is that castle still standing? And what’s going to keep it standing or cause it not to be
standing five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**):
- **The attacker with money** **[M2011-015]**. No rival can lay a second set of gas mains in Unitil's territories: the
  distribution utilities "deliver electricity and/or natural gas to all customers in their service territory, at rates
  established under cost of service regulation" (10-K Item 1). The franchise is "a natural franchise" of the kind the rows
  name **[M1995-037]**. The attacker who matters is not a second pipe but a substitute for the gas (electric heat pumps,
  heating oil, propane) and the state that sets the rules.
- **Pricing power and the agony before a rise** **[M2005-020]**. The company sets no price; it asks the regulator, and the
  asks are cut: Unitil Energy asked $18.5M and was granted about $13.0M (order of 2026-05-28); Fitchburg electric asked
  $6.8M, got $4.7M; Fitchburg gas asked $10.9M, got $10.1M; Northern NH asked $6.1M of temporary rates, settled at $5.5M
  (10-K Note 8; 10-Q Note 8). The prayer session is built into the business; the rows expect it of a utility: "The whole
  idea behind the utility industry is not to allow extraordinary profits" **[M2000-131]**.
- **Would the customer still choose it over the low bid?** **[M2017-009]**. For gas heat the choice is gas or another
  fuel, and customers have kept choosing gas: organic gas customer additions of about 1,450 (2018), 1,152 (2019), 1,000
  (2021), 850 (2022), 730 (2024) and about 570 in 2025 (15,930 less 15,360 acquired) (FY2019, FY2022, FY2025 10-Ks,
  MD&A). Positive every year, and falling. Weather-normalized therm sales outside the decoupled areas: up 4.2% (2019), 2.8%
  (2021), "essentially unchanged" (2022), up 3.5% in Northern Maine (2025).
- **Widening or narrowing** **[M1999-108]**. On the evidence, narrowing at the margin: the additions above have fallen by
  more than half over seven years; Massachusetts now makes a gas utility "bear the burden of demonstrating that non-gas
  pipeline alternatives (NPAs) were adequately considered" for full recovery of new investment, and cut Fitchburg's GSEP
  recovery cap from 3.0% to 2.5% with "likely" cuts to 2.0% and 1.5%; Maine opened an inquiry on 2025-05-13 into "the
  implications of Maine’s decarbonization goals for natural gas utilities" (10-K Note 8, still pending at the 10-Q). Against
  that, management is buying more gas distribution (Bangor and Maine Natural, 2025, $157.4M), and Massachusetts, the
  harshest of the three, is about 16% of gas customers (16,441 of 105,062; 10-K Item 1).
- **What could destroy, modify or reduce it five to fifteen years out** **[M2000-014]**. The regulatory climate: "the
  regulatory climate in a few states has raised the specter of zero profitability [...] it is difficult to project both
  earnings and asset values in what was once regarded as among the most stable industries in America" **[L2023-011]**. For
  Unitil the filings show the climate tightening on future gas investment and not, yet, on the return on existing
  investment; and change of this kind is slow, which "can be much harder to perceive, and can lull you to sleep easier"
  **[M2014-038]**.
- **Ask the competitors.** There are none in the territory; the comparison below is with comparable filers.

**The competitor row.** *CONVENTION of this run: the 10-K names no competitor for the distribution business (the only
competition it describes is third-party energy supply, a pass-through that does not touch the distribution margin), so I
chose three comparable SEC filers: Eversource Energy (regulated by the same NHPUC and MDPU), Chesapeake Utilities and
Northwest Natural Holding (gas-distribution-weighted utilities); rationale: the regulator's two states and the gas
business are what decide here. No named rival that does not file.* Same metrics from each filer's own XBRL facts, the
whole span (`peers_returns.txt`): net income to common over average equity, and operating income over average assets.

| Filer (latest 10-K accession) | Return on equity, each year 2016-2025 | Average | Operating income / assets, average |
|---|---|---|---|
| Unitil (`0001193125-26-042983`) | 9.4, 9.2, 9.6, 12.1 (divestiture gain), 8.4, 8.6, 9.0, 9.4, 9.4, 8.9 | 9.4% | 5.5% |
| Eversource (`0001628280-26-008461`) | 8.9, 9.1, 9.2, 7.5, 9.0, 8.5, 9.3, -3.0 (offshore wind write-off), 5.6, 10.8 | 7.5% | 4.7% |
| Chesapeake Utilities (`0001628280-26-011753`) | 11.1, 12.5, 11.3, 12.1, 11.4, 11.3, 11.2, 8.4, 9.0, 9.4 | 10.8% | 6.4% |
| Northwest Natural Holding (`0001733998-26-000012`, from 2018) | 8.6, 7.6, 8.8, 8.6, 8.2, 7.6, 5.9, 7.9 | 7.9% | 4.1% |

**The field's returns over the last full cycle, judged in words** *(the framework's CONVENTION: "ordinary" carries no
figure)*. The field earns ordinary returns, close to the allowed returns the commissions set and well short of excellent;
Unitil earns about what its orders allow (9.3% to 9.45% allowed, 9.4% earned on average), no more. A durable castle that
protects only ordinary returns would close OUT, but the framework's Q2 list names the exception in its own words (a return
set by a regulator is carried to Q3 as a second best), on two rows: the capital-heavy business entered on "reasonable
expectations of earning decent returns on the incremental sums they invest" **[L2009-012]**, and the one below. The rows
say why: "there’s no way we get rich
on our utility investments. But there’s no way we get poor, either" **[M2009-104]**; "when you get an allowed return in the
electric utility you’re almost certain of earning it, I mean, if you behave yourself" **[M2010-037]**; regulators "give us a
fair return on the assets employed" **[M2008-024]**.

**The verdict reasoning.** The castle stands for a reason that is legal, not competitive: the franchise and the compact
that lets the company earn its allowed return on what it invests. Over ten years I can judge it: the strictest regulator
has said in an order that existing investment recovery is not in jeopardy; New Hampshire, where most of Northern Utilities
and all of Unitil Energy sit, has no gas phase-out on the record I read; customers still join. Over twenty years the gas
part's castle is less certain, and the filings show it narrowing at the edges (falling additions, the NPA burden, the
tracker cap cuts, the Maine inquiry). That is a castle under slow pressure, not one shown open: no filing records a
disallowance of existing gas plant, a fall in gas customers or a commission refusing the return on equity. It is weighed,
not closed on: in Q7's certainty (no growth credited beyond what the window shows) and at Q9 (the regulatory climate)
**[L2023-011]**.
- **VERDICT: IN**, on the regulated-return exception, with the narrowing written down as contrary evidence
  **[M1995-038]**, **[M2009-104]**, **[M2010-037]**, **[M1999-108]**, **[M2014-038]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**. Operating income on average assets 5.5% over 2016-2025, never
  above 6.5% (peer table above); net income on average equity 9.4% (2019's 12.1% includes the divestiture gain). The
  return is the allowed return and no more, on a business that is two-thirds debt-and-deferral financed.
- **What the added capital earns** ("the return is not measured by the cash minus the increased capital investment we’re making. It’s measured by the
  operating earnings after depreciation" **[M2014-086]**). From end-2020 to end-2025 capital employed (long-term and short-term debt plus equity, less cash) rose
  from $969.5M to $1,520.2M, by $550.7M, and operating income rose from $71.4M to $101.2M, by $29.8M: **5.4% pre-tax on the
  added capital**. On the equity alone, net income rose by $18.0M (from $32.2M to $50.2M) on $220.4M of added equity
  (from $389.2M to $609.6M, of which $122.2M was new stock sold for cash): **8.2% after tax**. Those are decent regulated
  returns, about the orders' 9.3% to 9.45% less the lag, and nothing more.
- **To stand still and to grow** ("Every year we spend amounts equal to our depreciation charge simply to stay in the same
  economic place" **[L2000-035]**; the maintenance guess the owner is entitled to **[M2000-144]**). The filings give no split
  of capital spending into maintenance and growth. My stated guess: the provision for depreciation of plant, computed from
  the composite rates the 10-Ks state (3.29%, 3.26%, 3.33%, 3.49%, 3.45% for 2021-2025, on average depreciable plant, which
  is plant in service less construction work in progress): $52.7M, $55.1M, $59.6M, $66.3M, $72.4M, average **$61.2M**,
  against capital additions averaging **$146.6M** and reported depreciation and amortization averaging $70.9M (the
  difference is amortization of deferred regulatory costs, whose cash is already inside operating cash). So about
  **$85.4M a year** of the spending is growth, plus $160.4M of acquisitions in 2025.
- **The growth arithmetic.** The company has grown by putting in money: net plant doubled from $883.4M (2016) to $1,798.5M
  (2025), funded by debt (long-term debt from $333.6M to $670.5M, short-term from $81.9M to $255.7M) and by stock (shares
  from 14.07M to 17.92M at year end, 18.24M now). Net income rose 7.1% a year 2016-2025 and per share 4.8% a year ($1.94 to
  $2.97). "We just put way more capital into the business" **[M2023-081]**: this is the rows' utility pattern exactly, "To
  earn more, their owners must invest more" **[L2011-019]**. It is not the gruesome account, since the added money earns its
  allowed return rather than "little or no money" **[L2007-009]**; it is the second account at a rate that is decent and not "very
  satisfactory" **[M1998-081]**.
- **WEIGHS AGAINST**, mildly: the capital-heavy business the rows accept only "as the second-best choice, still a good
  choice" **[M2018-055]**, earning decent returns on the incremental sums **[L2009-012]** but needing outside money every
  year to grow, and around 8% after tax on the added equity, below the floor the purchase must earn at Q7
  **[M1998-081]**, **[L2011-019]**, **[M2014-086]**. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** ("balance sheets over an 8 or 10 year period before I even look at the income
  account" **[M2025-032]**; the table in Step 0). What moved and why:
  - *Plant and debt.* Net utility plant rose from $883.4M to $1,798.5M; total debt (long-term with current maturities plus
    short-term) from $415.5M to $926.2M, and to $956.0M at 2026-06-30. Debt grew faster than equity ($293.1M to $609.6M):
    debt to debt-plus-equity went from 59% to 60% at end-2025, and short-term debt became the swing financing, $255.7M at
    end-2025 against $54.7M at end-2020. Of that, $86.0M is a term loan for Maine Natural due 2026-10-31 and $42.6M a term
    loan for the water companies due 2027-06-30 (10-Q, financing note): acquisitions were bought with short-term money,
    later refinanced with long-term notes ($60M on 2026-09-24, $60M on 2026-10-14, the two 8-Ks).
  - *Equity against goodwill.* Goodwill is $4.3M at end-2025 ($6.8M at 2026-06-30) against $157.4M paid for Bangor and Maine
    Natural: regulated companies bought at about their regulated book, so the purchases did not fill the balance sheet with
    goodwill. Equity grew by retained earnings ($52.2M to $191.2M) and by stock sold ($33.0M 2017, $45.5M 2021, $73.5M 2025).
  - *Receivables and accrued revenue against sales.* $102.4M on $383.4M of revenue in 2016 (27%), $185.6M on $536.0M in
    2025 (35%). The ratio rose; part is the two acquired gas companies entering the winter-billing season inside 2025 and
    part the 2025 working-capital draw the MD&A ascribes to "the timing of cash receipts and disbursements in the normal
    course of business". I write it down as contrary evidence, the receivables-against-sales tell **[M1995-064]**; it is not a reserve that moves or a deferral building
    on its own, and the regulatory assets *fell* (total $164.7M in 2020 to $116.9M in 2025).
  - *Retirement obligations* fell from $162.3M (2020) to $25.5M (2024), $32.9M (2025): the rate and funding effects of
    those years; pension cost is recovered in base rates after the 2024 Fitchburg orders (10-K Note 8).
  - *What the figures cannot say* **[M2025-032]**: the value of the plant depends on the regulator continuing to allow its
    recovery; for gas plant in New England after 2035 that is a policy question no balance sheet answers (Q2).
- **The real costs.** Depreciation is a true cost **[L2015-004]**, **[R1996-023]**: the maintenance guess is the plant
  depreciation provision (Q3), and at a utility whose plant costs more to replace than it cost to build, "it costs a lot
  more money to maintain capital expenditures now in dollar terms" **[M2005-052]**, so the guess is if anything light.
  Stock pay ($1.4M to $3.3M a year, the restricted-share expense in the 10-K notes) is a real cost **[L2015-003]** and is
  deducted in Q7. Transaction costs ($0.7M in 2024, $3.1M in 2025, $1.1M in the first half of 2026, after tax as the reconciliations in
  the 10-K and 10-Q state them) recur with each deal
  and are counted, not waved away **[L2016-007]**. Deferred taxes: cash taxes paid are small ($4.9M in 2025); owner cash
  is taken after the company's cash tax, with the book-tax variant beside in Q7, since the deferral is not "a hidden form of
  equity" for a utility **[M2015-030]**. No EBITDA appears in the 10-K, the 10-Q or the proxy (text search: no instance).
- **What the accounts say of management.** The MD&A and every earnings line in the proxy feature "Adjusted Net Income" and
  adjusted EPS, which add back the acquisition transaction costs ($3.16 adjusted against $2.97 GAAP for 2025); the proxy
  sets the annual EPS target "consistent with our external guidance to investors" and pays 40% of the annual incentive on
  adjusted EPS, with a discretionary $0.04 adjustment to 2024 EPS for the same costs (DEF 14A, CD&A). These are the habits
  the framework weighs here and carries to Q5: the adjusted figure featured **[L2016-006]**, earnings guidance
  **[L2019-006]**, a declared target **[L2002-041]**. Against them, the GAAP figure is always shown first and reconciled,
  the adjustment is a single named item, and the costs are real deal costs, not operating costs relabelled.
- **VERDICT on the accounts: WEIGHS AGAINST**, mildly. No confusion: the statements reconcile, the cash flow ties to the
  balance sheets, and the tells that live in the accounts are absent (no deferrals building, no reserve releases, no
  profits that may not exist). A management "preoccupied with accounting considerations" is "a negative" but not "a total
  exclusionary factor" **[M1994-018]**; the adjusted figure and the guidance go to Q5 **[L2016-006]**, **[L2019-006]**. The
  recast owner cash (Q7): operating cash, less stock pay, less the maintenance guess.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The people.** Thomas P. Meissner, Jr., chairman and chief executive since April 2018, joined the company in 1994 as an
  engineer and ran its operations as chief operating officer from 2005 to 2018 (DEF 14A `0001193125-26-128263`). A
  lifetime inside one small utility is the record of someone who loves this business more than a bigger cheque elsewhere
  **[M2000-098]**; "people leave track records in life" **[M1998-168]**, and his is thirty-two years of it here.
- **The first yardstick, the record against the hand dealt** **[M1994-008]**. The hand is a small, regulated, capital-hungry
  utility; the record is a return on equity at the allowed level in every year (9.4% average, Q2), electric reliability the
  proxy reports as top-quartile for four years, rate cases settled near the asks, and acquisitions of gas utilities at about
  their regulated book (Q4). The peers dealt bigger hands did worse on the same metric (Eversource 7.5%, Northwest Natural
  7.9%); one did better (Chesapeake 10.8%).
- **The second yardstick, the proxy: how they treat themselves against the owners** **[M1994-009]**. Chief executive's total
  pay $3.19M for 2025, 21 times the median employee; no excise-tax gross-ups; a clawback policy; no hedging or pledging;
  executives must hold every share received as pay until they leave, and own four times salary (the CEO holds 148,738
  shares, about $8.2M at the price; directors and officers together 2.22%). Modest, and in the owners' coin.
- **Pay tied to what the person controls** **[M2003-019]**. The annual plan pays on adjusted EPS (40%), gas-leak response,
  outage minutes, customer satisfaction and cost per customer: things management controls. "you get what you reward for"
  **[M2016-083]**: the EPS leg rewards per-share earnings measured *before* the costs of the deals management chose to do
  (the 2024 discretionary $0.04 and the 2025 adjusted target), which leans toward deals; the long-term plan pays on
  three-year return on equity and growth in book value per share, and a company that sells stock above book (the 2025 offering at $46.65 against
  book of $34.01 a share at end-2025) raises its book value per share by selling stock (carried to Q6, Part B).
- **The tells of dishonesty.** Searched for in the 10-K, the 10-Q, the proxy and the 8-Ks: no restatement, no auditor
  change, no reserve released into earnings, no stock price posted as a goal **[M2004-067]**, no promise too good to be
  true. The habits carried from Q4: the adjusted figure featured, external guidance, and an EPS target. They are read with
  the rest: the targets are not "consistently" reached (GAAP EPS fell short of target in 2024 and 2025 and the proxy says so,
  "In 2024 and 2025, EPS lagged slightly behind target"), the one adjustment is named and reconciled to GAAP each time, and
  the proxy prints the GAAP figure beside the adjusted one in the same footnote. That is the "negative" of
  **[M1994-018]**, not the pattern of **[L2002-041]**. One more fact, written down **[M1997-127]**: the general counsel
  appointed 2025-10-29 was an NHPUC commissioner from December 2021 to August 2024, the commission that regulates Unitil
  Energy and Northern Utilities' New Hampshire division, and rejoined a Unitil subsidiary in December 2024 (8-K
  `0001193125-25-264824`, disclosed in full). It bears on the regulatory relationship (Q9) more than on honesty toward the
  owners; I found nothing in the filings that it touched.
- **Combined chairman and chief executive.** The board keeps the two roles together with a lead director who chaired four
  executive sessions in 2025 (DEF 14A). The rows warn how hard it is "to replace a mediocre CEO if that person is also
  Chairman" **[L2014-026]**; nothing on the record shows a mediocre chief executive, so it is a weight, not a finding.
- **VERDICT on integrity: IN.** No doubt found that would close the file under "If you’ve got doubts, forget it."
  **[M2013-088]**; the habits are read as a preoccupation, a negative **[M1994-018]**. **Ability WEIGHS FOR**: a long
  record inside the business, run at the allowed return, paid modestly and in shares held to retirement
  **[M1994-008]**, **[M1994-009]**, **[M2000-098]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- **The retention test, on the five-year rolling basis** **[R1995-009]**. Net income 2021-2025 $220.0M, dividends paid
  $132.5M, retained $87.5M. Market value: $44.27 x 15.012M shares = $664.6M at 2020-12-31; $48.44 x 17.919M = $868.0M at
  2025-12-31 (year-end closes, Yahoo, aggregator flagged; shares from the 10-K balance sheets). Of the $203.4M rise, $122.2M
  is new stock sold for cash, leaving **$81.2M of market value for $87.5M retained, about $0.93 per dollar**: just short of
  the test, on the market leg. On the intrinsic leg (Q7), the range at today's price of money brackets the 2020 price as
  it brackets today's, so no gain in value per share is shown either. Not met, narrowly.
- **What the cash is used for.** The company pays out about 60% of earnings as dividends (2025: $30.1M of $50.2M) and
  raises outside equity to fund growth in the same years: in 2025 it paid $30.1M of dividends and sold $73.5M of stock.
  The dividend is not the See's case of a business that "should be paying out its earnings" **[M2004-089]**: this business
  can use more than all of its earnings at its allowed return, and pays out a share anyway, then sells stock to replace it.
  The round trip costs the underwriting and agents' fees (the August 2025 offering raised $71.8M net on 1,602,358 shares
  at $46.65, $74.7M gross, per the 10-K).
- **Issuance and deals: value given against value got** **[R1995-010]**, **[M1995-001]**. Stock sold at $46.65 (August
  2025) and $52.14 average (ATM, first half 2026). Against the Q7 range written back from Q7 below (central, equity-only:
  **$24.57 to $49.60** a share), the 2025 offering was sold inside the range, below its top and well above its bottom, and
  the 2026 ATM sales a little above its top: the owners received at least what they gave, on these figures. The three acquisitions (Bangor $71.4M, Maine Natural $86.0M,
  the New Hampshire water companies $42.1M plus about $0.6M) were paid in cash borrowed short-term, so the all-stock STOP
  **[L2009-019]** does not arise; they were bought at about regulated book (goodwill $6.8M at 2026-06-30 against about
  $200M paid), which buys an allowed return and nothing beyond it.
- **Serial issuance** **[L2014-015]** (the candidate second STOP the framework leaves unresolved, so weighed here): stock
  sold in 2017, 2021, 2025 and continuously through an ATM since June 2025, plus forward-sale capacity added 2026-02-19
  (424B5 `0001193125-26-059567`); shares up from 14.07M (2016) to 18.24M. This is how a growing utility funds its equity
  share of rate base, and it is disclosed and modest per year (about 3% a year over the decade), but it is issuance by habit,
  and it **weighs against**.
- **Buybacks.** None to speak of: until 2024 the company bought small amounts of its stock in the open market under a
  10b5-1 plan only to supply the stock part of the directors' retainer, and the plan ended on 2024-05-31 (10-K, the
  common-stock note); there is no programme to buy below value. The buyback test has nothing to test; the bottom of the
  Q7 range is used above for the issuance instead.
- **Part A WEIGHS AGAINST**: the retention test narrowly unmet on the market leg **[R1995-009]**, dividends paid while stock
  is sold to replace them, and issuance by habit **[L2014-015]**; the deals were at book for cash, with no value given away
  that the filings show **[M1995-001]**.

**Part B, the pay, the board and the owners.**
- **Pay** (Q5): modest, in shares held to retirement; the annual plan on things management controls. Against it: the
  annual EPS leg is measured before deal costs, and the long-term plan's book-value-per-share goal is advanced by selling
  stock above book, which this company does every year: "if you have a dumb incentive system, you get dumb outcomes"
  **[M2016-083]**. A partner "in both directions" **[L1994-020]**: the restricted shares can be forfeited, and the 2026
  change holds dividends on unvested shares until they vest (8-K `0001193125-26-033824`), a move toward it.
- **The board.** Classified (three-year terms), combined chairman and chief executive with a lead director (DEF 14A);
  directors under a stock ownership and retention policy.
- **The owners as partners.** External earnings guidance (Q4), which the rows call "a totally destructive policy" when it
  becomes a catechism **[M2022-054]**; read here as a habit, not yet a catechism (Q5).
- **Part B WEIGHS AGAINST**, mildly: the pay is small and aligned in coin, but two of its measures reward deals and stock
  sales **[M2016-083]**, and guidance is given **[M2022-054]**.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
credited only "for whatever net cash is left every year" **[M1998-080]**, at the long government rate **[L2000-021]**:
5.33%. Arithmetic in `scripts/q7.py`, output `q7_output.txt`; every input is from the filed statements named in Step 0.

**The basis.** The deciding part (gas distribution, Q2) earns a return its regulators allow on its invested capital: "when
you get an allowed return in the electric utility you’re almost certain of earning it" **[M2010-037]**, and the all-equity
basis carries its own exception for "the fixed-asset commitments at our regulated utilities" **[L2017-012]**. So, by Q7, The
regulated utility: **the central figure is equity-only** (owner cash after interest and after the company's tax, against
the market value of the shares), the all-equity figure beside it.

**Owner cash, equity-only, US$ millions** (operating cash, which is after interest paid and cash tax and includes every
working-capital change, less stock pay, less the maintenance guess of Q3):

| | 2021 | 2022 | 2023 | 2024 | 2025 | Average |
|---|---|---|---|---|---|---|
| Operating cash | 107.8 | 97.7 | 107.0 | 125.9 | 131.3 | 113.9 |
| less stock pay | 1.4 | 2.1 | 1.9 | 2.4 | 3.3 | 2.2 |
| less maintenance (plant depreciation provision) | 52.7 | 55.1 | 59.6 | 66.3 | 72.4 | 61.2 |
| **Owner cash after maintenance (central)** | **53.7** | **40.5** | **45.5** | **57.2** | **55.6** | **50.5** |
| Growth spending (capital additions less maintenance) | 62.3 | 67.0 | 81.4 | 103.6 | 112.7 | 85.4 |
| Acquisitions | nil | nil | nil | nil | 160.4 | 32.1 |
| *Literal window, after all spending* | *-8.6* | *-26.5* | *-35.9* | *-46.4* | *-217.5* | *-67.0* |

Beside: maintenance taken as the full reported depreciation and amortization, average $40.9M; the book-tax variant
(deferred tax provision charged as if paid), average $40.1M.

**The specifics, one by one.**
- **(a) Cycles.** Neither end year is described by the filer as aberrational; 2022's low figure is a working-capital year
  inside the window. No cycle base; the literal window is shown above.
- **(c) Acquisitions, decided before the growth rate because it decides which growth is measured.** Purchases in the
  window, $160.4M, exceed half of owner cash before purchases ($252.5M over five years, half $126.2M), so the framework's
  serial-acquirer CONVENTION applies: **the central figure is the organic pair** (purchases left out, organic growth
  credited), the default pair beside. The filer does not report organic owner cash; it reports what Bangor and Maine
  Natural added in 2025 (gas margin $16.6M, O&M $4.2M, depreciation $3.3M, and the $1.4M rise in property taxes; 10-K MD&A).
  *CONVENTION of this run, a disclosed guess: the acquired companies' 2025 contribution to owner cash after interest is
  $16.6M less $4.2M less $1.4M, less interest on the money borrowed for them for the months held ($79.8M average at 5.5%,
  between the term-loan and note rates the filings state), less their own $3.3M of depreciation as their maintenance,
  taxed at the 2025 effective rate of 23.4%: about $2.5M. Rationale: the serial-acquirer rule needs an organic figure the
  filer does not print, and this is built only from the filer's own numbers.* Organic 2025 owner cash about $53.0M.
- **(b) Decline.** Organic growth, 2021 to 2025: ($53.0M / $53.7M) to the quarter power, **-0.33% a year**. Negative, so
  carried as negative: it makes the bottom of the range and the no-growth case is the top. (Total growth with the acquired
  contribution in: +0.84% a year; used only in the default pair.)
- **(d) Working capital** is counted: it is inside operating cash.
- **(e) Growth spending, maintenance case central.** The no-growth case charges maintenance only, $50.5M a year forever.
  The growth case charges the growth spending as well, growing with the growth carried and stopping after year ten:
  **$85.4M gross in year one, $82.9M in year ten**. The utility debt credit (Q7, The regulated utility, 2026-10-23): the
  increase in long-term debt (including current maturities; finance leases under $1M) from $531.6M at 2020-12-31 to
  $670.5M at 2025-12-31 is $138.9M, **$27.8M a year**; short-term debt and the term loans that bought the acquisitions
  are left out, and the 10-K states no securitization bonds ("do not currently use [...] securitization"). It is credited
  against the growth spending only, **capped at 48%**, the deciding part's allowed debt share: Northern Utilities New
  Hampshire 48%, Northern Utilities Maine 47.99%, Fitchburg gas 48% (10-K Note 8), together about 85% of gas customers
  (89,696 of 105,062), so the stated shares cover more than half of the part (*CONVENTION of this run: the filings state
  no rate base by company, so customers stand in for rate base in the more-than-half test and the weighting; rationale:
  the rule asks for a rate-base weight the filing does not print, and every stated share is 48% within 0.01 points, so
  the weighting cannot move the cap*); Bangor, Maine Natural and Granite State
  state none. The cap ($41.0M) does not bind. Growth spending net of the credit: **$57.6M in year one, $55.9M in year ten**
  (credit $27.8M and $27.0M). The growth that spending bought, measured organically, is nil to negative: "growth can
  destroy value if it requires cash inputs in the early years [...] that exceed the discounted value of the cash that those
  assets will generate in later years" **[L2000-023]**, and on this window it did. That inversion is the finding.
- **(f) The cap.** No positive growth is carried, so nothing to cut. Owner cash after maintenance has run at 7% to 12%
  of revenue.
- **Deals outside the window.** The New Hampshire water companies, closed 2026-06-30 for $42.1M plus about $0.6M in cash
  (8-K `0000755001-26-000026`), have no filed earnings: credited at nothing, their cost ($42.7M, borrowed on Tranche B)
  deducted, **-$2.34 a share**. Aquarion Water Company of Massachusetts, signed and not closed (MDPU approval subject to a
  rate-case moratorium; reconsideration denied 2026-03-30; 10-Q): left out of the central figure; beside, with no filed
  record of its own earnings, it would be credited at nothing and cost about $27.9M of cash ($70.0M aggregate cash less
  $42.1M paid), about **-$1.53 a share** more, before its unstated share of the $30.0M of assumed debt.

**The range, central (equity-only, organic pair, at 5.33%):**
- Top, the no-growth maintenance case: $50.5M / 5.33% = $947.3M, less $42.7M = **$49.60 a share**.
- Bottom, the organic growth case (-0.33% for ten years, growth spending net of the debt credit charged, then flat):
  $490.8M less $42.7M = **$24.57 a share**.
- Width 2.0 to 1. Beside it: the default pair (acquisitions deducted, total growth +0.84%), $18.94 to -$4.58 before the
  water deal; the growth case with no debt credit, $18.74 before the water deal; the book-tax variant's top $38.91; the
  full-D&A variant's top $39.69; the literal window after all spending, negative. **All-equity beside** (owner cash with interest paid added back after tax at
  the 2025 effective rate of 23.4%, $74.0M a year, against market value plus net debt of $946.8M at 2026-06-30: short-term debt $234.8M,
  long-term debt $680.4M plus $40.8M current, less cash $9.2M, the water-deal borrowing already in it; operating leases
  left out): $24.21 to -$12.88 a share.

**The floor, tested first** (the floor CONVENTION, about ten percent, "we don’t want to buy equities where our real
expectancy is below 10 percent" **[M2003-149]**, earned on the equity for a utility). At $55.15 the best case in the range,
the no-growth case, returns $50.5M on $1,005.8M of market value plus the $42.7M of water-deal debt: **4.8% a year, with no
growth**. The growth case returns less. On the all-equity basis the best case returns 3.8%. **No case in the range earns
the floor at the price.** The price is also above the top of the central range ($49.60). The rows expected exactly this of
a utility at a full price: "no way we get rich on our utility investments" **[M2009-104]**, and they ask only "decent
returns on the incremental sums they invest" **[L2009-012]**, which a 4.8% expectancy is not.

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent, the two averaged:
no-growth $504.9M, organic growth case $144.2M, average $324.6M, less $42.7M = **$15.46 a share, equity-only (central,
the regulated-utility basis)**; **all-equity beside: not positive (-$26.00 a share)**. Company's own cash tax; no
conversion. Growth spending (above maintenance) **$85.4M in year one, $82.9M in year ten, none after** (specific (e)).
Utility debt credit: long-term debt increase **$27.8M a year**, against growth spending only, cap **48%** (the deciding
part's allowed share, stated by the orders for Northern Utilities and Fitchburg gas), not binding.

**Q6 written back:** the bottom of the central range, $24.57, and its top, $49.60, are the figures Q6 Part A sets the
2025 offering ($46.65, inside the range) and the 2026 ATM sales ($52.14, a little above the top) against; there are no
buybacks to set against the bottom.

- **VERDICT: OUT.** No case earns the floor at the price; "there’s just a point at which we drop out of the game"
  **[M2003-149]**. Not a screamer and not near one **[M2009-005]**; the bottom boundary **[L2013-012]** is less than half
  the price.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT). See AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. See AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (and not asked by the operator for this run).

---
## THE BOX
**OUT**, decided at **Q7**: no case in the range earns the floor at the price (the best case, no growth, returns about
4.8% on the equity at $55.15). Value range, central (equity-only, the regulated-utility basis, organic pair, the water
deal deducted): **$24.57 to $49.60 a share against $55.15**; fair price **$15.46** equity-only, all-equity not positive.
Q1 IN, Q2 IN (the regulated-return exception, the gas castle narrowing at the margin), Q3 weighs against mildly, Q4 weighs
against mildly, Q5 integrity IN and ability for, Q6 weighs against.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; the box is unchanged, operator rule 2; each with its source **[M1997-127]**.)*
- **Bears on Q8 (the bond).** The 30-year Treasury yields 5.33% (US Treasury, 10/23/2026); the no-growth case's
  expectancy at the price is about 4.8% on the equity and about 3.8% on the whole business (Q7 above).
- **Bears on Q9 (debt and exposures).** Total debt $956.0M at 2026-06-30 (short-term $234.8M, of which the Maine Natural
  term loan $86.0M matures 2026-10-31 and the water term loan $42.6M on 2027-06-30; long-term $680.4M plus $40.8M current)
  against common equity $643.5M (10-Q `0000755001-26-000029`); debt was 60% of debt plus equity at end-2025. Since the
  10-Q the company has sold $60M of senior unsecured notes (5.42% 2031, 5.79% 2036; 8-K `0000755001-26-000031`) and
  Unitil Energy $60M of first mortgage bonds (5.72% 2036, 5.87% 2038; 8-K `0000755001-26-000033`). The revolving credit
  facility ($275M, to 2028-09-29) carries one financial covenant, funded debt to capitalization not above 65%; the parent's
  notes require funded debt below 70% of capitalization and earnings at least twice interest to issue more (10-K
  `0001193125-26-042983`, MD&A and Note 4). 2025 pre-tax earnings over gross interest: ($65.5M + $43.8M) / $43.8M, about
  2.5 times. The regulatory climate: the Massachusetts NPA burden and GSEP cap cuts, the Maine future-of-gas inquiry, the
  FERC transmission ROE cut to 9.57% with a $0.9M refund charge in 2026 (10-Q Note 8). The general counsel's prior
  service as an NHPUC commissioner (8-K `0001193125-25-264824`). A derivative of $17.7M at end-2025 on a long-term clean
  energy purchase contract, offset by a regulatory liability (10-K Note 7). No integrity facts are carried: Q5 was reached
  and answered.
- **Bears on Q12.** Gas and electric distribution under state regulation; none of the businesses the framework names.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      commits for Step 0 to Q1, Q2, Q3, Q4, Q5, Q6 with Q7, and the close.
- [x] Dispatched to an analyst: the brief allowed the per-question pathspec commits; the lock in `Screens/_daily/` was
      present (written by the dispatching session, not touched by this analyst); the fold into the register is the
      dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under Contamination at the top and was not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by `scripts/check_ids.py` in the research folder); every
      filing fact carries its accession; no E-ids.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost (operating cash after interest and cash tax, less stock pay, less the maintenance
      guess, with acquisitions and growth spending charged in the cases), never a net-income proxy; the sovereign from the
      US Treasury; the price and the year-end prices in Q6 from an aggregator, flagged.
- [x] Contrary evidence written down as found (Foundations, Q2, Q4, Q5, Q6); the facts for later questions are under
      AFTER THE STOP.
- [x] No row dated after the anchor: this is a run at today's date, not a point-in-time test.
- [x] Only the arithmetic lines of `tools/run.py` were to be used; it printed none (UNRESEARCHED for want of matching
      tags), and the arithmetic was done by the research-folder scripts from the filed figures.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the final commit message).
- Honest gaps: the maintenance guess is mine (the filings split no spending into maintenance and growth); the organic
  owner cash is my estimate from the filer's own figures for the acquired companies (CONVENTION above); the 2026 ATM
  sales after the 10-Q cover date are unknown; the Q3 2026 10-Q was not yet filed on the run date.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) `tools/run.py` produced nothing for a utility: it reported "no overlapping OCF/D&A/capex annual facts" although the
company tags all three (its depreciation is `UtilitiesOperatingExpenseDepreciationAndAmortization`), so every utility
run must rebuild the arithmetic by hand; the tool's tag list should be checked. (2) The serial-acquirer test compares
purchases with "owner cash before purchases" without saying on which basis: on the all-spending basis this utility's
owner cash is negative in every year and the test trips trivially; I used the central, maintenance basis ($126.2M half
against $160.4M of purchases), and it tripped there too. The organic pair then asks for "organic growth as the filer
reports it", and a utility reports organic customers and sales, never organic owner cash, so the run had to confess its
own estimate. (3) The utility debt credit takes long-term debt only and leaves out short-term borrowing, but this
company funds its acquisitions and much of its growth first with term loans classed as short-term debt ($128.6M at
2026-06-30) and refinances them later; the credit therefore depends on where in the refinancing cycle the window ends. I
followed the text. (4) The cap asks for a rate-base weighting the filings do not print; customers were used as the stand-in
(confessed). (5) A deal closed after the window "with its financing added to today's net debt" has no stated treatment on
the equity-only basis, where net debt is not used; I deducted the cash paid from the equity value, which is the same
number reached the other way. (6) Q2's regulated-return exception sends a castle with ordinary, allowed returns to Q3
rather than OUT, but says nothing of a regulated castle whose regulator's policy is turning slowly against the product
(natural gas in New England); the text routes rapid change to TOO HARD and says nothing of slow, policy-made change to a
franchise. I judged it on the ten-year record (IN, with the narrowing carried as contrary evidence); another analyst could
defensibly have closed Q2 TOO HARD (NATURE) on the twenty-year question, and the box would have been different in name
though not in what it permits.
