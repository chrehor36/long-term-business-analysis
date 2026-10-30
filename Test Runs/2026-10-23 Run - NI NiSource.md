# Company Run, NiSource Inc. (NYSE: NI), 2026-10-23
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind
run under `Screens/_daily/_dispatch_brief.md` as the brief departs from it (the brief says where: the lines of evidence
are derived by the analyst, not written by the dispatcher). Filled top to bottom, each question committed as it closed.
Working folder: `Test Runs/_research 2026-10-23 NI/` (notes, scripts and their printed output; raw filings in its
gitignored `cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-26: the operator does not hold this name (`PORTFOLIO.md` has no NiSource row).*

**CONTAMINATION, declared and not used.** (1) The session opened with a repository status and commit list in its
context: the five latest commit subjects concern another utility's v5 re-run (NEE), including its box, its deciding
question and its computed figures. I read them before starting; I did not open that run file, and nothing in this run
rests on them. Because that subject line names a Q5 close for a utility, I state here that the Q5 judgment below was
made on NiSource's own filings and argued both ways in the text. (2) The same status list showed untracked research
folder names of other companies (AYI, ARCB); names only. (3) The memory index loaded with the session carries one-line
summaries of the queue (counts of gate-clearers, "nothing buyable", holding reviews owed); no company names bearing on
NI; not used. No other run file, holding review, `PORTFOLIO.md` or blind-listed file was opened, listed or searched.

**The lines of evidence this name needs (derived by the analyst from the 10-K's Item 1, Item 1A and Item 7, as the
brief requires).** Chosen because the 10-K says the company "derives substantially all of its revenues and earnings
from the operating results of these rate-regulated businesses" (FY2025 10-K, Item 1): (i) the regulated return: allowed
ROE by jurisdiction, the earned return over a full span, and the regulatory climate (Item 1 rate-case table; Item 1A
"Most of our revenues are subject to regulation"; the Indiana ROE and tracker investigations in the Q2 2026 10-Q);
(ii) the capital programme and how it is funded (Item 7 capex tables, $28.6 billion 2026-2030 plan; the ATM programme;
the Blackstone minority sales), because owner cash for a utility is decided by spending against debt and equity raised;
(iii) the data-center business, GenCo and the ADS (Amazon) and Alphabet contracts, the one part whose economics are new
(Item 1, Item 7, 8-K of 2026-10-16); (iv) the gas business's long-run demand (Item 1 energy-efficiency and Maryland
electrification text) because the castle of a gas distributor depends on gas staying in the house; (v) the safety and
integrity record, the Greater Lawrence Incident of 2018 and its criminal resolution (FY2020 10-K, the DPA and plea
exhibits of 8-K 0001193125-20-051063), because Item 1A names "inherent hazards and operating risks, including potential
public safety risks" and the company's own history is the largest instance; (vi) the debt, since Item 1A says "We have
substantial indebtedness". The 10-K names no rival company (see Q2).

---
## STEP 0, THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $43.69 (close 2026-10-22, aggregator quote via `tools/run.py`, flagged per operator rule 5: live quote only).
- **Shares by class** from the latest filing's cover: one class, 479,560,100 common shares as of 2026-07-29 (10-Q for
  the period ended 2026-06-30, filed 2026-08-05, accession `0001111711-26-000088`; `python Screens/cover_shares.py NI`).
  Checks: issued less treasury at 2025-12-31, 482,395 thousand less 3,963 thousand = 478,432 thousand, equal to the
  balance-sheet count (FY2025 10-K statement of equity); 479,498,053 outstanding at 2026-06-30 (10-Q balance sheet).
  After the 10-Q: no 8-K or prospectus found that issues common shares (8-Ks of 2026-08-18, a $750M junior subordinated
  note, and 2026-10-16, a battery tolling agreement; 424B2/424B5 of 2026-08-13/14 for the note). **Forward sales not yet
  settled** (10-Q Note 6): 2,390,057 + 2,200,000 + 2,151,874 = 6,741,931 shares, about $298.9M of proceeds at the
  forward prices; for the per-share figures below they are treated as settled (CONVENTION of this run: the company
  states it expects full physical settlement, so the shares and their cash are both counted), giving 486.302M shares.
- **Market cap:** $20,952M at the cover count ($21,247M with the forward shares, less $299M of proceeds to come).
- **Sovereign for the earnings currency (USD):** 5.29%, 30-year par yield, US Treasury daily par yield curve,
  2026-10-22 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025 (filed 2026-02-11, `0001111711-26-000027`): Items 1, 1A, 3, 7,
  the statements, Notes 4, 6, 8, 12, 19, 21 and the tax note; 10-Q for Q2 2026 (`0001111711-26-000088`); proxy DEF 14A
  filed 2026-03-30 (`0001140361-26-011851`); 8-Ks of 2025-10-31 (`0001193125-25-259392`, ATM), 2025-12-11
  (`0001193125-25-316004`, revolver), 2026-05-18 (`0001193125-26-228913`, senior notes), 2026-08-05 (`0001111711-26-000087`,
  Q2 release, exhibit 99.1), 2026-08-18 (`0001193125-26-355564`, junior notes), 2026-10-16 (`0001193125-26-423375`,
  tolling agreement); the cycle's 10-Ks for FY2018 (`0001111711-19-000008`), FY2020 (`0001111711-21-000010`), FY2021
  (`0001111711-22-000007`), FY2022 (`0001111711-23-000006`), FY2023 (`0001111711-24-000011`), FY2024
  (`0001111711-25-000008`); the DPA and plea agreement filed as exhibits 10.1 and 10.2 to the 8-K of 2020-02-27
  (`0001193125-20-051063`).
  **One figure cross-checked against the filed statement:** net cash from operating activities 2025, $2,362.3M on the
  filed Statement of Consolidated Cash Flows (FY2025 10-K), equal to the $2,362 `tools/run.py` transcribed from XBRL.
  **A transcription error found:** `tools/run.py` printed a "debt" column d3 tagged `CapitalizationLongtermDebtAndEquity`
  ($27,118M at 2025-12-31). That tag is total capitalization (equity plus long-term debt) on NI's balance sheet; long-term
  debt excluding current maturities is $15,457.8M (FY2025 10-K and 10-Q balance sheets). The run.py debt sums are not
  used; the debt below is computed as total capitalization less total equity, checked against the 10-K's own figure of
  "total consolidated indebtedness of $16,213.5 million" (Item 1A).
- `python tools/run.py NI` arithmetic lines (saved as `run_py_output.txt`): OCF 2023-2025 $1,935M, $1,782M, $2,362M;
  stock pay $34M, $44M, $51M; capex as tagged $2,646M, $2,614M, $2,782M; D&A $908M, $1,043M, $1,168M; owner earnings on
  the capex basis negative every year (mean -$697M), on the D&A basis $944M. These lines leave out four capital outflows
  the filed statements carry (cost of removal; milestone payments to renewable developers, $1,098.7M in 2025; advanced
  deposits, $373.8M in 2025; a developer obligation paid in financing, $347.2M in 2023), so the owner cash below is built
  from the filed statements, not from these lines. Only the arithmetic lines were used; run.py's v4 material ignored.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is whether I would be content to own this regulated network if the
market closed. The foundation that bears hardest is "Who is paid to tell you": the company's own communications lead with
a guided non-GAAP figure and a growth rate to 2033, a seller's projection of what is being sold; the speakers say "we’ve
never looked at a projection in connection with either a security we’ve bought or a business we’ve bought" **[M1995-050]**,
and the guidance is not used in any figure below. No macro view enters **[M2000-094]**: interest rates, data-center demand and
gas prices are not forecast. **Contrary evidence, written down as found** **[M1997-127]**: (1) the Q2 2026 GAAP EPS of
$0.09 against an adjusted $0.16 (8-K exhibit 99.1); (2) the admitted "pattern of flagrant organizational indifference"
in the 2020 statement of facts (DPA exhibit 10.1); (3) the capital spending is about 3.6 times depreciation over five
years and owner cash after all spending is negative in four of five years; (4) the Indiana commission opened
investigations into the authorized ROE and the trackers in July 2026 (10-Q Note 9); (5) shares outstanding rose from
323.2M (2016) to 478.4M (2025); (6) run.py's debt column was total capitalization (corrected above). Each is carried to
its question.

## THE STANDING RULE
The run is a part-interest bought for cash, unlevered, at whatever size the operator sets; nothing in the purchase gives
anyone a call on the buyer: "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**. The
rule is met by the buyer's conduct, and the target's own debt is weighed at Q9.

---
## Q1, CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**. NiSource is two regulated businesses and a new one:
  Columbia Operations, gas distribution to about 2.4 million customers in five states; NIPSCO Operations, gas (about 0.9
  million customers) and electric (about 0.5 million customers) in northern Indiana; and GenCo, generation being built to
  serve data-center load under the ADS (Amazon) contract and a later Alphabet contract, its costs reported in Corporate
  and Other (FY2025 10-K, Item 1 and Note 21). Operating income 2023-2025 by segment: Columbia $738.3M, $728.7M,
  $895.1M; NIPSCO $541.7M, $719.8M, $938.1M; Corporate and Other $15.5M, $7.0M, $2.1M (Note 21; 2023 corporate by
  difference from the consolidated $1,295.5M).
- **The key variables and whether they are foreseeable** **[M1998-044]**: the rate base (what is invested and admitted
  to rates), the allowed return on equity and the share of it actually earned, and the regulatory climate in six states.
  The rate base is set by the company's spending and the commissions' approvals; the allowed ROEs in force run 9.60% to
  10.00% (Item 1 rate-case table: Pennsylvania 10.00%, Maryland 9.80%, Kentucky and Virginia 9.75%, Ohio 9.60%, NIPSCO gas
  and electric 9.75%). These are the variables the rows name for a utility, "when you get an allowed return in the
  electric utility you’re almost certain of earning it, I mean, if you behave yourself" **[M2010-037]**, and the past
  statements do tell the future ones in kind **[M2008-033]**: a tariff, a tracker, a rate case.
- **What is less foreseeable, and whether it decides.** GenCo's data-center generation is new (contract signed 2025;
  first assets under construction) and carries construction, cost-recovery and counterparty risk the filings name ("our
  ability to recover our investments and realize our expected return under our current and any future data center
  contracts", Q2 2026 release). It contributed no operating income in the window, so by the business-of-parts paragraph
  (a part "matters" when it carries more than half of five-year operating profit, or else is the largest) it does not
  decide; the deciding parts are Columbia and NIPSCO, each about half. The gas distribution business's long-run demand
  is the second uncertainty (Maryland's net-zero and electrification policy, declining use per customer, Item 1); the
  rows' test is whether it is "important and knowable" **[M2006-076]**: its direction is stated in the filings and
  regulators recover the cost of the network through fixed charges in several states (Ohio's straight fixed variable
  design, Item 1), so it is a risk to the castle, carried to Q2, not a fog over the economics.
- **Would the insiders write it down?** **[M2000-105]**: utilities file ten-year integrated resource plans and five-year
  capital plans with their regulators (NIPSCO's 2024 IRP, Item 1); the insiders do write it down.
- **VERDICT: IN.** The deciding parts are rate-regulated distribution and integrated utility businesses whose earning
  power is the allowed return on a rate base the filings state; the definition of understanding is met "where the
  business will be in 10 years" **[M2000-037]**, in the sense of a range, not a point. The doubt rule was weighed
  **[M2002-092]**: the doubt I have is about the regulatory climate and the company's own record, which are questions of
  the castle and the people, not of whether the economics can be read.

## Q2, WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
- **The castle.** A franchise granted by the state: "Our NIPSCO Electric utility generally has exclusive service areas
  under Indiana regulations and retail electric customers in Indiana do not have the ability to choose their electric
  supplier" (Item 1). In gas, customers may buy the commodity from marketers (34.9% of Columbia's residential customers,
  6.8% of NIPSCO's, did so at 2025-12-31) but the gas still moves through the utility's pipe for a tariff (Item 1). The
  "why is that castle still standing" question **[M1995-038]** has a plain answer: no one can lay a second distribution
  network beside 37,300 miles of Columbia main and 18,100 miles of NIPSCO main.
- **The money test** **[M2011-015]**: could an attacker with a hundred billion dollars take it? Not by building; the
  franchise is the commission's to give. The attack that can work is the one the rows name for utilities, a regulator's:
  "the regulatory climate in a few states has raised the specter of zero profitability or even bankruptcy" **[L2023-011]**.
- **Pricing power and the agony before a rise** **[M2005-020]**: none of its own. Prices are set in rate cases, and the
  company received less than it asked in every case listed: Pennsylvania $55.6M of $110.4M asked; Ohio $68.3M of $221.4M;
  NIPSCO electric $257.0M of $368.7M; NIPSCO gas $120.9M of $161.9M (Item 1 rate-case table). The prayer session is
  institutional here: it is the rate case.
- **Would the customer choose it over the low bid?** In electricity in Indiana, the customer has no choice. In gas, the
  substitute is electric heat; the filing claims "customer preference for natural gas" (Item 1) and names the threat:
  Maryland's plan to "transition gas furnaces to electric heat pumps" and proposed rules that new customers "pay the full
  cost of extending service" (Item 1). Maryland is Columbia's smallest state by approved incremental revenue (Item 1 table).
- **Ask the competitors** **[M1999-130]**: the 10-K names no rival company. It names classes: "investor-owned, municipal,
  and cooperative electric utilities", pipelines, "alternate fuels, such as propane and fuel oil", and, for data centers,
  "utilities and other energy sources across the United States and abroad" (Item 1). **The competitor row is therefore a
  CONVENTION of this run**: three SEC-filing utilities chosen as the nearest in business mix, Atmos Energy (ATO, pure gas
  distribution, fiscal year to September; 10-K `0000731802-25-000056`), ONE Gas (OGS, pure gas distribution; 10-K
  `0001587732-26-000009`) and CenterPoint Energy (CNP, gas distribution plus an electric utility in Indiana and Texas;
  10-K `0001130310-26-000008`); rationale: they are what a gas-and-electric distributor in the Midwest would be measured
  against, and none is a rival for NI's customers, which is itself the finding.
- **The competitor row** (net income to common over average common equity, XBRL first-filed values from each company's
  10-Ks; `peers.py`, printed in `peers_output.txt`):

  | | 2015-2025 mean | 2021-2025 mean | worst year in span |
  |---|---|---|---|
  | NI | 6.0% | 9.2% | 2018, -1.3% (Greater Lawrence); 2020, -1.2% (sale of the Massachusetts business) |
  | ATO | 10.0% | 9.0% | 2023, 8.7% |
  | OGS | 8.3% | 8.5% | 2015, 6.5% |
  | CNP | 8.7% | 10.9% | 2015, -17.3%; 2020, -11.4% (both non-utility impairments) |

- **The parts table** (Note 21, operating income 2023-2025, the only years on the current segment basis; the 2021-2022
  segments were reported as gas and electric and are not comparable):

  | part | share of 2023-2025 operating income | castle | decides |
  |---|---|---|---|
  | Columbia Operations (gas distribution, five states) | 51.0% | state franchise, regulated return | yes (more than half) |
  | NIPSCO Operations (gas and electric, Indiana) | 48.5% | exclusive electric territory, regulated return | yes (largest of the rest, near half) |
  | Corporate and Other incl. GenCo | 0.5% | not yet a business | no |

  On the five-year test the span is shorter than five years on this basis; I treat both regulated segments as deciding,
  since together they are all of the operating profit and each is near half.
- **The field's returns over the last full cycle.** The field earns what its regulators allow, about 8% to 10% on book
  equity across the four filers and eleven years, and NI earned less than the field over the whole span (6.0% mean) because
  of its own losses in 2018 and 2020, and about the field in 2021-2025 (9.2%). That is an ordinary return protected by a
  durable castle, which Q2's list (What it rules OUT) sends OUT except where the return is set by a regulator, a case the
  framework carries to Q3 as a second best. The rows' own words for it: "there’s no way we get rich on our utility investments. But there’s
  no way we get poor, either" **[M2009-104]**; "the industry offers owners the opportunity to deploy large sums at fair
  returns" **[L2005-005]**.
- **Widening or narrowing?** **[L2005-010]**: narrowing at the edges. The gas franchise is under policy pressure in one
  state; Indiana opened "formal investigations related to authorized return on equity and the future use of regulatory
  trackers" in July 2026 (10-Q Note 9). Widening in electric load: two hyperscale customers contracted (Q2 2026 release).
- **What could destroy it, five to fifteen years out** **[M2000-014]**: a regulatory climate that turns, the case of
  **[L2023-011]**; a second catastrophic gas incident, since "A catastrophic event can render a single utility insolvent"
  **[L2005-019]** and NI has already had one; electrification of heat ending the gas network's growth; and data-center
  generation built ahead of contracts that fail.
- **VERDICT: IN**, on the regulated exception: the castle is a franchise that stands, the returns it protects are set by
  regulators and are fair, not excellent, and Q2's text carries that case to Q3 rather than closing it. The regulatory
  climate is the castle's weak wall and is weighed at Q9 as the framework directs.

## Q3, HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital needed.** Operating income after depreciation over net plant: 2025 $1,835.3M on $28,688M net
  PP&E at year-end, 6.4% before tax; 2021 $1,006.9M on $17,882M, 5.6% (10-K statements; XBRL net PP&E). On common equity,
  9.2% average 2021-2025 (Q2 row). The measure the rows set for a utility's added capital: "It’s measured by the
  operating earnings after depreciation" **[M2014-086]**. Operating income rose $828.4M from 2021 to 2025 while net PP&E
  rose $10,806M: about 7.7% pre-tax on the increment, before interest on the debt that paid for most of it.
- **Reinvestment to stand still and to grow.** All capital spending (capex, cost of removal, developer milestone payments,
  deposits, finance-lease principal, contract and developer payments in financing) averaged $3,378M a year 2021-2025
  against depreciation of $938M (`q7_compute.py`): 3.6 times. The filer's own "Maintenance" lines plus cost of removal and
  lease principal averaged $1,070M, above depreciation (MD&A capex tables, FY2021-FY2025 10-Ks). The rows on the class:
  "To earn more, their owners must invest more" **[L2011-019]**; the capital-heavy business is "the second-best choice,
  still a good choice" **[M2018-055]** on the condition of "decent returns on the incremental sums they invest"
  **[L2009-012]**.
- **The growth arithmetic and its caps.** The plan is $28.6 billion 2026-2030, "including $21.0 billion of base capital
  investments and $7.6 billion of strategic data center infrastructure investments", for "9%-11% consolidated rate base
  growth" (Q2 2026 release). Owner cash cannot fund it: owner cash after all spending was negative in every year 2021-2025
  before any debt credit (Q7). It is funded by debt (total debt $9,746M at 2020-12-31 to $16,213.5M at 2025-12-31), by
  shares (Q6), and by selling minority stakes (19.9% of NIPSCO Holdings II to a Blackstone affiliate for $2,161.9M in
  2023; 19.9% of Generation Holdings II in 2025; statements of cash flows and Note 4).
- **WEIGHS UNDECIDED, leaning AGAINST.** The added capital earns about what regulators allow, which the rows accept as a
  second best **[M2018-055]**, **[L2009-012]**; against it, the company has earned below its allowed returns over the
  full span, and the growth is bought with outside money on every side, "cash-consuming businesses, by their nature, are
  unattractive unless the cash they consume gets to earn a reasonable return" **[M2012-057]**. The "little or no debt"
  criterion is applied at Q9.

## Q4, DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** **[M2025-032]** (FY2016-FY2025 10-Ks via XBRL first-filed values, checked
  against the filed 2025 and 2026-06-30 balance sheets; USD millions):

  | year-end | equity (NI) | minority | goodwill | net PP&E | total debt | debt share of capital | receivables / revenue | retained earnings | shares (M) |
  |---|---|---|---|---|---|---|---|---|---|
  | 2016 | 4,071 | 0 | 1,691 | 13,068 | 7,909 | 66.0% | 18.9% | -972 | 323.2 |
  | 2017 | 4,320 | 0 | 1,691 | 14,360 | 9,002 | 67.6% | 18.4% | -1,073 | 337.0 |
  | 2018 | 5,751 | 0 | 1,691 | 15,543 | 9,133 | 61.4% | 20.7% | -1,399 | 372.4 |
  | 2019 | 5,987 | 0 | 1,486 | 16,912 | 9,643 | 61.7% | 16.5% | -1,371 | 382.1 |
  | 2020 | 5,752 | 86 | 1,486 | 16,620 | 9,746 | 62.5% | 16.9% | -1,765 | 391.8 |
  | 2021 | 6,947 | 326 | 1,486 | 17,882 | 9,802 | 57.4% | 16.9% | -1,581 | 405.3 |
  | 2022 | 7,575 | 326 | 1,486 | 19,843 | 11,316 | 58.9% | 17.8% | -1,214 | 412.1 |
  | 2023 | 8,270 | 1,867 | 1,486 | 22,275 | 14,128 | 58.2% | 15.7% | -967 | 447.4 |
  | 2024 | 8,684 | 1,984 | 1,486 | 25,454 | 13,960 | 56.7% | 17.7% | -712 | 469.8 |
  | 2025 | 9,450 | 2,210 | 1,486 | 28,688 | 16,214 | 58.2% | 18.0% | -315 | 478.4 |

  (Total debt = total capitalization less total equity, plus current maturities and short-term borrowings; debt share =
  debt over debt plus total equity including the minority. Equity 2018-2024 includes preferred stock and equity units.)
  **What moved and why.** Net plant more than doubled; debt doubled; NI's equity more than doubled, and **all of the equity
  growth came from issuing shares**, since retained earnings were a deficit in every one of the ten years: dividends and
  the 2018 and 2020 losses exceeded the decade's earnings, and the deficit only began closing in 2021. Goodwill fell once,
  in 2019 (the Massachusetts impairment). Receivables track revenue (16% to 21%); no build-up. Cash is small except at
  2023 year-end, when the Blackstone proceeds sat in cash before redeeming preferred stock and paying down debt. The
  minority line, nil in 2019, is $2,210M in 2025: owners of NI common now own about 80% of NIPSCO's equity, not all of it.
  What the figures cannot say: the value of regulatory assets ($2,225M noncurrent at 2025-12-31) depends on future rate
  orders; the capital spending's return depends on commissions not yet asked.
- **The real costs.** Depreciation is real **[R1996-023]**, and here it understates the spending to stand still: the filer's
  own maintenance spending plus cost of removal ran above depreciation every year (Q3), "merely spending their depreciation
  expense will not keep them in the same place" being the railroad row's case **[M2016-092]** that the utility's figures
  repeat in small. Stock pay is $24M to $51M a year (cash-flow statement, "Stock compensation expense and 401(k) profit
  sharing contribution") and is charged in owner cash. The recurring "one-time": the 2026 adjusted figure removes
  "Workplace continuity" ($21.4M) and a "Value Captured initiative" ($5.4M) in Q2 2026, and the 2025 proxy defines
  Adjusted EPS as GAAP "adjusted for certain items, such as fluctuations in weather and other significant unusual events"
  (DEF 14A). Cash taxes are near nil ($9.4M, $4.3M, $3.3M paid 2023-2025, 10-K supplemental cash-flow schedule) against
  tax expense of $139.5M to $203.8M, because of accelerated depreciation and a federal loss carryforward of $1,192.0M that
  does not expire (tax note). Of deferred taxes in a utility the rows say "I don’t think I would look at that as a hidden
  form of equity" **[M2015-030]**: the regulator returns the benefit to customers.
- **EBITDA in the filer's own mouth.** No instance found in the Q2 2026 release or the 10-K MD&A of EBITDA featured
  (text search of both). The featured figure is "non-GAAP consolidated adjusted EPS", which leads the release's headline
  bullets ahead of GAAP, with a guidance range for 2026 ($2.02-$2.07) and a guided growth rate "of 9%-10% from 2026-2033"
  (8-K exhibit 99.1). The adjustment runs both ways (2025 adjusted EPS $1.90 per the proxy against GAAP diluted EPS
  $1.95), so it is not a one-way flattering of costs; it is a habit of guidance and of a featured adjusted figure.
- **What the accounts say of management's character.** The statements are readable and agree with themselves (the OCF,
  debt and share cross-checks above). None of the account tells of the list in Q4 was found: no prepaid or deferred
  accounts building out of line (prepayments $149M to $246M), no reserve that moves with an offering, no profit that may
  not exist. The guidance habit and the featured adjusted figure are the make-the-numbers habit's public face:
  "Managers that always promise to "make the numbers" will at some point be tempted to make up the numbers"
  **[L2002-041]**; "the scourge of earnings "guidance" and the desire of CEOs to "hit the number."" **[L2019-006]**.
- **VERDICT on the accounts: no STOP; WEIGHS AGAINST.** The accounts neither confuse nor raise suspicion; owner cash can be
  built from them. Against: depreciation short of the spending to stand still, the adjusted figure featured, and guidance
  to 2033, which "makes us nervous" in the rows' words **[L2016-006]**; recorded as a weighing **[M1994-018]** and carried
  to Q5. The recast earnings feed Q7.

## Q5, WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who runs it.** President and CEO Lloyd M. Yates since February 2022 (director since March 2020; before that Duke
  Energy, retired 2019); CFO Shawn Anderson since March 2023; COO and Chief Safety Officer William Jefferson Jr. since
  2022; every executive officer listed in the FY2025 10-K took his or her present office in 2022 or later (Item 1,
  Information about our executive officers). Board of twelve, chaired by Kevin T. Kabat (director since 2015); five
  directors served before the Greater Lawrence Incident of September 2018 (Jesanis 2008, Henretta 2015, Kabat 2015,
  Altabef 2017, Butler 2017) and one joined in 2018 (Bunting); a former chair of the National Transportation Safety Board
  joined in 2019 (Hersman) (DEF 14A).
- **The integrity record, read whole.** On 2018-09-13 over-pressurization of a low-pressure system of Columbia Gas of
  Massachusetts caused fires and explosions in Lawrence, Andover and North Andover; one fatality, injuries, about 7,500
  meters cut off (FY2020 10-K, Note 20-C). In February 2020 the subsidiary pleaded guilty to violating the Natural Gas
  Pipeline Safety Act and paid a criminal fine of $53,030,116; NiSource entered a deferred prosecution agreement for three
  years, sold the Massachusetts business, and recorded about $1,036M of claims, fines and settlements (FY2020 10-K). The
  statement of facts in the DPA (8-K `0001193125-20-051063`, exhibit 10.1) says the subsidiary, "through a pattern of
  flagrant organizational indifference, knowingly and willfully violated a minimum safety standard"; that its employees
  knew from a 2015 NiSource operational notice that a disrupted control line could cause a "catastrophic event"; that a
  field-engineering manager "made clear to CMA employees that meeting GSEP mileage goals was directly connected to company
  earnings"; and that an "urgent" request for more regulator-station staff in October 2017 was not met before the event.
  NiSource acknowledged in the DPA that "the Government has sufficient basis to allege that NiSource is responsible for
  CMA's conduct". The probation ended 2021-06-23 (FY2022 10-K); the DPA period ran to 2023-02-26 and no instance was found
  of an extension or breach (text search of the FY2022 and FY2023 10-Ks; the FY2023 10-K no longer mentions it). A
  shareholder derivative suit over the board's safety oversight and proxy safety disclosures was dismissed in federal
  court in March 2021 (federal claims with prejudice) and refiled in the Delaware Chancery Court (FY2021 10-K); no instance
  found of it in the FY2022 10-K's legal note; outcome not read.
- **What is current.** In November 2025 the Indiana commission opened an investigation into NIPSCO's gas-meter accuracy
  after "NIPSCO's disclosure of a latent issue with a small percentage of the meter indexes" found during a meter rollout;
  hearing scheduled for October 2026 (10-K Note 12; 10-Q Note 9). The company found and disclosed it: "tell us the bad
  news immediately" **[M1998-039]**. No other legal proceeding is called material (10-K Note 19-C).
- **The two yardsticks** **[M1994-008]**. Running the business: since 2022 the regulated segments' operating income rose
  from $1,280.0M (2023) to $1,833.2M (2025) (Note 21); the earned return on common equity rose from 8.3% (2021) to 10.3%
  (2025); rate cases were settled in Indiana and decided in Pennsylvania; the proxy reports zero serious injuries or
  fatalities and zero PHMSA-reportable incidents due to operations or process failure in 2025; two hyperscale contracts
  signed. Treatment of owners: CEO total pay $13.2M in 2025 ($9.2M in 2023), 106 times the median employee; the proxy
  ("how they treat themselves versus how they treat the shareholders" **[M1994-009]**) shows 50% of performance shares and
  the short-term plan's financial measure on Adjusted EPS, stock ownership guidelines of six times salary for the CEO, a
  hedging and pledging ban, and 97% say-on-pay support (DEF 14A).
- **The habits carried from Q4.** Guidance on adjusted EPS for the year and a growth rate to 2033; the 2025 proxy
  reports results that "exceeded our adjusted EPS guidance range"; executive pay paid on the same adjusted figure. Read with
  the integrity record: the rows warn that a CEO's forecasts can make "really decent people misbehave because they felt
  that there was a loyalty to their CEO to present certain numbers" **[M2015-033]**, and the DPA's facts are a case of
  that warning, in safety rather than accounting, in the old organization.
- **The case for OUT, stated as strongly as I can** **[M2016-055]**. Integrity is applied on doubt, not on proof:
  "If you’ve got doubts, forget it." **[M2013-088]**. The organization admitted a knowing and willful crime with a death
  in it, the facts tie it to earnings-linked capital goals, and the board chair and four other directors oversaw that
  organization then and oversee this one now. The present plan is the same engine at a larger size: capital spending
  converted into rate base and earnings, a guided growth rate, pay on the adjusted figure. The rows say culture is hard
  to change, "it’s a lot easier to build a new organization around a culture than it is to change the culture of an
  existing organization" **[M2010-021]**, and that an organization's norms travel down, "they adopt the norms of what they
  think is happening up above them" **[M2000-154]**. The front-page test **[M2016-033]** was failed in the most literal way.
- **The case for IN, and why it carries.** The STOP is on the integrity of who runs it, and the rows' tells are tells of
  people (reports that dance **[M1995-111]**, figures obscured on purpose **[M2003-029]**, the too-good-to-be-true
  **[M2002-028]**), and no instance of them was found in the filings read; the record against the officers now in charge
  shows no dishonesty toward owners, regulators or courts: the parent did not contest the facts, met the
  DPA, sold the business as required, settled the class action, and now discloses its own defects before the regulator
  finds them. The officers who ran the company in 2018 are gone from the list of executive officers; none of the present
  officers is named in the statement of facts. The admitted conduct was indifference to safety, a failure the rows weigh
  under culture and ability, not a lie to owners. "people leave track records in life" **[M1998-168]**: this management's
  four-year track record is clean in the filings. The doubt I have is about the culture the board and the plan still
  carry, and the rows give the place for that: management enters "as to the degree of certainty that we attribute to the
  stream of income" **[M1999-104]**, which is a weighing.
- **VERDICT on integrity: IN** (the closest call of the run; see What in the framework was wrong or unclear).
  **Ability: WEIGHS FOR, with the guidance habit and the incentive architecture against.** The present team has improved
  the earned return and the safety record on the evidence; against it, pay and public promises rest on a guided adjusted
  EPS, "the scourge of earnings "guidance"" **[L2019-006]**, in a company whose own history shows what earnings goals can
  do to field decisions.

## Q6, WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[R1995-009]**, five years 2021-2025. Net income to common $3,609.7M; common dividends
  $2,151.6M; retained $1,458.1M (10-K statements). Owners also put in new money: common issued $1,391.5M and equity units
  $839.9M (2021, converted to common in 2023) (cash-flow statements). Market value of the common rose from $8,988M
  (391.8M shares at $22.94 on 2020-12-31) to $19,978M (478.4M at $41.76 on 2025-12-31; year-end closes from the
  aggregator, flagged): $10,990M of market value against $3,689.5M retained and put in. The market leg passes. The
  intrinsic leg, read against Q7's range ($29.20 to $32.83 a share, equity-only at the sovereign), shows the market price
  above the range, so the market leg flatters the test; the speakers rewrote the test because the market leg alone can mislead
  **[R2009-002]**. Weighed, not decided.
- **Buybacks.** None in the window; no repurchase programme (cash-flow statements 2021-2025). Q6's buyback test has
  nothing to read; written back from Q7: not applicable.
- **Issuance.** Shares outstanding 323.2M (2016) to 478.4M (2025), up 48%, through the ATM programmes, equity units and
  forward sales; a $1.5 billion ATM opened 2025-10-31 with $1.15 billion of capacity left at 2026-06-30 (8-K
  `0001193125-25-259392`; 10-Q Note 6). The rows on the serial issuer: "we have never invested in companies that are
  hell-bent on issuing shares" **[L2014-015]**, which the framework carries as a candidate second STOP, unresolved (section
  VI), so it is weighed here and not applied as a stop. What was received: ATM prices of $39.71 to $46.47 a share in
  2025-2026 (10-K MD&A; 10-Q Note 6), above the top of Q7's range, so on this run's range the issuance did not give more
  value than it got: "We will issue common stock only when we receive as much in business value as we give" **[R1995-010]**.
  The minority sales: 19.9% of NIPSCO Holdings II for $2,161.9M in 2023, a price implying about $10.9 billion for all of
  NIPSCO's equity when the whole company's common was worth about $11.9 billion at that year-end (447.4M shares at $26.55),
  so the stake was sold at a high price relative to the market's price for the whole. No all-stock acquisition; Q6's STOP
  **[L2009-019]** does not apply.
- **Dividends while issuing.** The company pays out about 55% to 60% of GAAP earnings (dividends $530.4M against $929.5M in
  2025) while selling new shares at commissions of up to 2% (8-K of 2025-10-31) to fund the plan: a dividend paid and
  partly taken back. The rows' test is whether the dollar retained could earn more than a dollar **[M2004-089]**; here the
  company says it could (it is raising outside equity), which argues for retaining more and issuing less.
- **Part B, pay, board, owners.** Performance shares: 50% three-year cumulative Adjusted EPS, 30% relative total
  shareholder return, 10% operational excellence and safety, 10% workforce and sustainability; short-term plan 70% Adjusted
  EPS, 2025 result $1.90 against a $1.88 target, paid at 167% of target on that measure (DEF 14A). Pay on a per-share
  earnings figure that grows with capital spent, with no capital charge in the plan, in a capital-intensive business, is
  the arrangement the rows warn of: "In a capital-intensive business, you have to have something that — you have to have
  a factor in the compensation arrangement that includes a capital cost element" **[M2009-081]**; "you get what you reward
  for" **[M2016-083]**. A safety measure is in both plans, which the old plan's facts make the right addition. Chair and CEO
  are separate. The compensation discussion and tables take more than half of the proxy's text as extracted (the CD&A opens at line
  4,984 and the pay-versus-performance section closes after line 11,791 of 13,033), the length test of **[M2009-087]**. Guidance is given, which inverts **[M2022-054]**.
- **WEIGHS AGAINST** (Part A): serial issuance with a dividend paid alongside, though at prices above this run's range and
  with the minority stakes sold well. **WEIGHS AGAINST** (Part B): pay on a guided adjusted EPS with no capital charge in a
  business where capital spent is the earnings engine.

## Q7, WHAT IS IT WORTH? STOP.
All arithmetic in `q7_compute.py`, printed in `q7_output.txt`. The question is the speakers' "How certain are you that
there are indeed birds in the bush?" **[L2000-021]**, with "are you going to have to put more cash into after you buy
it?" **[M2014-068]** asked first, because for this business the answer is yes, every year.

- **The basis.** NI's deciding parts earn a return a regulator allows, so Q7's regulated-utility paragraph governs: the
  central figure is equity-only (owner cash after interest and the company's tax, against the market value of the
  shares), the debt raised over the window for the fixed assets credited against the spending it funded up to the debt
  share, the all-equity figure beside. The exception is the row's own, "the fixed-asset commitments at our regulated
  utilities" **[L2017-012]**. Merchant generation stays all-equity: GenCo has no operating earnings in the window and its
  spending (deposits, part of the 2025 capex) is inside the spending below.
- **Owner cash, by year (USD millions; filed cash-flow statements, FY2025 10-K for 2023-2025, FY2023 10-K for 2021-2022):**

  | | 2021 | 2022 | 2023 | 2024 | 2025 | average |
  |---|---|---|---|---|---|---|
  | net cash from operations (working capital inside it) | 1,217.9 | 1,409.4 | 1,935.1 | 1,781.5 | 2,362.3 | 1,741.2 |
  | stock pay and 401(k) stock contribution | -24.3 | -24.9 | -33.5 | -43.6 | -50.9 | -35.4 |
  | all capital spending (a) | -2,266.7 | -2,803.8 | -4,015.6 | -3,314.0 | -4,491.5 | -3,378.3 |
  | of which the filer's maintenance (b) | -715.3 | -867.5 | -1,043.2 | -1,201.5 | -1,524.3 | -1,070.4 |
  | preferred dividends, minority and tax-equity distributions, net of their contributions (c) | +189.4 | -39.9 | +183.0 | +24.9 | +142.6 | +100.0 |
  | **owner cash after maintenance only** | 667.7 | 477.1 | 1,041.4 | 561.3 | 929.7 | **735.4** |
  | owner cash after all spending, before any debt credit | -883.7 | -1,459.2 | -1,931.0 | -1,551.2 | -2,037.5 | -1,572.5 |
  | the same, with the debt credit | 409.8 | -165.7 | -637.5 | -257.7 | -744.0 | -279.0 |

  (a) capex, cost of removal, milestone and final payments to renewable-generation developers, advanced deposits, other
  investing, the 2023 developer obligation paid in financing ($347.2M), contract-liability payments, finance-lease
  principal (2021-2022 the combined line with debt repayments, taken whole). (b) the filer's own "Maintenance" capex lines,
  including Corporate and Other maintenance (MD&A capex tables, FY2021-FY2025 10-Ks; segment basis), plus cost of removal
  and lease principal. (c) excludes the $2,161.9M received in 2023 for 19.9% of NIPSCO Holdings II, a sale of part of the
  business, not cash from it; includes the minority's later contributions, which pay its share of the spending
  (CONVENTION of this run: the minority's cash in and out is what separates our share of the consolidated cash; rationale:
  our share of free cash equals the consolidated figure less the minority's net receipts).
- **The debt credit.** Total debt rose from $9,746.1M (2020-12-31) to $16,213.5M (2025-12-31): $6,467.4M raised net over
  the window. No regulator-allowed capital structure is stated in the filings read (text search of the 10-K and 10-Q for
  "capital structure" found only rating and covenant text), so the rule's fallback is used: the business's own debt share
  of capital at the latest filed date, $17,403.0M of debt over $17,403.0M plus $11,894.4M of equity including the
  minority at 2026-06-30, 59.4% (the revolver covenant ratio, 51.0% at 2025-12-31 on its own definition, is shown beside
  and not used). Cap: 59.4% of $16,891.6M of spending = $10,033.8M; the credit is the lesser, $6,467.4M, $1,293.5M a year.
  **CONVENTION of this run: net, not gross.** The debt raised is taken net of repayments, since a refinancing funds no new
  asset; rationale: the gross figure would credit the same dollar of plant twice.
- **Where the credit belongs.** The debt raised funded the rate-base growth (net plant $17,882M to $28,688M), not the
  replacement: in a no-growth steady state the debt does not grow, so the maintenance-only case carries no credit, and the
  credit goes to the growth spending it paid for (CONVENTION of this run; rationale as stated, and the text does not say).
  The rule's words, read alone, would also credit debt against maintenance spending; that reading is shown beside.
- **The specifics, in order.** Four of the PG re-test: growth measured on aggregate owner cash (yes); all spending deducted
  with the maintenance judgment stated (the filer labels its maintenance, so (e) applies and the maintenance-only case is
  central); zero nominal growth after year ten (yes); a price above the top closes OUT (applies). And (a) to (f): (a) no
  end year is aberrational on the filer's own description; the literal five-year window is the window used. (b) the
  all-spending series changes sign (2021 positive, 2022-2025 negative, halves $122.0M to -$500.9M with the credit), so its
  compound rate is meaningless; growth is measured on the maintenance-only series instead, 2021 to 2025 $667.7M to
  $929.7M, 8.63% a year (halves $572.4M to $745.5M). (c) no business acquired; the developer payments are purchases of
  generation assets under build-transfer agreements and are counted as capital spending; no merger; the signed battery
  tolling agreement of 2026-10-15 (8-K `0001193125-26-423375`: about $2.2 billion of storage payments over about twenty and
  a half years, a finance lease, effective only if its conditions are met by 2027-01-31) is left out of the central figure
  and noted beside: it would add a lease liability and its payments to the spending. (d) working capital is inside the cash
  from operations. (e) the maintenance-only case is central; the growth case charges the growth spending net of its debt
  credit, -$1,014.5M a year at the window average, against the growth it buys; maintenance-only cash and net growth
  spending are both carried at 8.63% for ten years and both stop after year ten (CONVENTION of this run, following the
  framework's purchases-stop-after-year-ten rule for acquisitions: growth spending stops with the growth). (f) 8.63% is
  above the 5.29% discount rate, so it is carried only inside the ten years; the absurdity test passes: maintenance-only
  owner cash in year ten, about $1,679M, would be about 14% of sales grown at the business's own 7.9% (revenue $4,899.6M
  to $6,642.2M, 2021-2025), below the highest share it has earned in the window (18.9%, 2023).
- **Value range (equity-only, at the 5.29% sovereign, per share on 486.302M shares with $298.9M of forward proceeds):**
  maintenance-only, no growth: **$29.20**; growth case: **$32.83**. Range **$29.20 to $32.83** against **$43.69**. At ten
  percent the growth case falls below the no-growth case ($8.59 against $15.74): the growth bought is worth less than its
  cost at the floor rate, "growth can destroy value if it requires cash inputs in the early years" **[L2000-023]**.
  Beside, not deciding: the literal-credit reading (debt credited against maintenance too), $53.92 no-growth at the
  sovereign, $28.81 at ten percent; owner cash charged with book tax instead of cash tax (deferred taxes added back,
  $161.3M a year, removed; the federal loss carryforward does not expire, so the framework's statutory-rate convention for
  short-lived carryforwards does not bind), $22.93 at the sovereign, $12.42 at ten percent; the all-equity basis (owner
  cash before interest, interest shielded at the 21% statutory rate, against market value plus net debt of $17,333.0M at
  2026-06-30; the $750M junior notes of 2026-08-18 are after that filing and not added): no-growth $6.93, growth case
  -$7.81 at the sovereign.
- **Closes. The floor is tested first.** At $43.69 no case earns about ten percent: valued at ten percent, the central
  cases give $15.74 and $8.59 a share, the literal-credit reading $28.81, the book-tax case $12.42, the all-equity cases
  -$12.83 and -$39.04; every one is below the price. The owner-cash yield at the price is 3.5% on the central case (6.5%
  on the literal-credit reading). "there’s just a point at which we drop out of the game" **[M2003-149]**. The price also
  sits above the top of the range, which closes OUT by the same floor. The width test does not arise (the range is about
  1.1 to one).
- **Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and averaged, after
  the company's own tax: **$12.17 a share on the equity-only basis (central, the regulated-utility basis)**; **-$25.93 on
  the all-equity basis beside**. No cheap price is reported.
- **VERDICT: OUT.** The price does not clear the floor on any case the filings support. The business is understood and
  its castle stands; the rows' own line on such a business: "there’s no way we get rich on our utility investments"
  **[M2009-104]**; and on such a price, "some utilities have sold at extraordinary prices. And we can’t pay them"
  **[M2017-095]**.

Q8, Q9, Q10 and Q12: **NOT REACHED** (operator rule 2; the Q7 STOP closed the file).

---
## THE BOX
**OUT at Q7** (the floor, tested first): value range $29.20 to $32.83 a share (equity-only, regulated-utility basis, at
the 5.29% sovereign) against $43.69; no case earns about ten percent at the price. Fair price $12.17 equity-only
(central), -$25.93 all-equity (beside).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged.)* **[M1997-127]**
- **Q8.** The bond: the 30-year Treasury yields 5.29% (2026-10-22); the central case's owner-cash yield at the price is 3.5%.
- **Q9.** Total debt $17,403.0M at 2026-06-30 (10-Q), plus $750M of 6.25% junior subordinated notes issued 2026-08-18
  (8-K); pre-tax earnings plus interest over interest 3.07, 3.64, 2.66, 2.94, 2.90 times in 2021-2025 (10-K income
  statements; the coverage of **[L2012-002]**, pre-tax earnings over interest, read with interest added back to the
  numerator); ratings BBB+ (S&P), Baa2 (Moody's), BBB (Fitch), all stable; $153.9M of collateral would be called on a
  downgrade below investment grade (10-Q); the revolver covenant caps debt to capitalization at 70% (51.0% at
  2025-12-31); the 2026-10-15 tolling agreement would add a finance-lease obligation behind about $2.2 billion of
  payments; NI is a holding company dependent on its subsidiaries' cash (Item 1A); the "little or no debt" criterion of
  **[R1997-001]** is not met by a utility so financed; the rows' cover test for utilities is earning power that "even
  under very adverse business conditions, amply covers their interest requirements" **[L2010-012]**; one catastrophic
  incident (2018) has already cost about $1 billion; Indiana's ROE and tracker investigations are open (10-Q Note 9).
- **Q10.** Nothing to record beyond the box.
- **Q12.** The company operates gas and electric networks and builds generation for data-center customers; no business of
  the kind the rows name. The Greater Lawrence record (Q5) bears on the newspaper test and is recorded there.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `9d8e5a46`); written question by question. **Departure:** Q1 to
  Q4 were committed together in one commit (`7b1ec2d5`) rather than one commit each; Q5, Q6 and Q7 were each committed on
  closing. The Q7 script was written during Q4's work (to read the debt and spending the balance sheets showed) and was
  committed with Q4; a header "COMPUTATION, NOT A CLEARANCE" was added to it before Q5's commit; no entry language in it.
- [x] Dispatched: the brief allowed per-question commits; the lock is held by the dispatching session (not touched).
  The run binds only once folded into the register by the dispatcher.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident (the
  session's commit list naming another utility's run and box, other companies' research-folder names, the memory index
  lines) is declared under CONTAMINATION and not used.
- [x] Every v5 id resolves and every quoted fragment beside an id is in that row (`check_ids.py`, result in
  `check_ids_output.txt`); no E-ids; every filing fact carries its accession or names its filing; aggregator prices
  flagged; the CONVENTIONs of this run confessed where used (forward shares treated as settled; the competitor set; the
  minority's cash flows separating our share; the debt credit net of repayments; the credit kept with the growth
  spending; growth spending stopping after year ten).
- [x] The order was kept; Q7 was the first STOP that failed; Q8 to Q12 are not reached and nothing after Q7 is a clearance.
- [x] Owner cash after every real cost, built from the filed statements, never a net-income proxy; the sovereign from the
  US Treasury; aggregator quotes flagged.
- [x] Contrary evidence written down as found (the Foundations line, six items, each carried to its question); facts for
  later questions under AFTER THE STOP. No integrity flag in the box line: Q5 was answered, not left behind a STOP.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used, and one of them (the debt column) was found to be total
  capitalization and replaced from the filed balance sheets.
- [x] `python tools/check_framework.py` PASS before the commits of this file.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
**(1) Q5 and an organization's admitted crime under former officers.** The integrity STOP is applied "on doubt", and the
rows' tells are tells of persons; the framework does not say whether a criminal plea and a deferred prosecution
agreement, with a statement of facts tying safety failures to earnings-linked capital goals, made under officers who have
since left but overseen by directors who remain, is doubt about who runs it now or a weighing on culture and ability. I
read it as the latter and said why; a second analyst could close at Q5 on the same facts with **[M2013-088]**. The box
would be OUT either way here, but not for every name. A sentence in Q5 on the reach of the integrity STOP in time and
across a change of officers would settle it. **(2) The regulated-utility credit and the maintenance case.** Q7's utility
paragraph credits the debt raised against "the capital spending it funded", and specific (e) makes maintenance-only
central. Read together literally, debt raised to grow the rate base is credited against replacement spending, which in a
no-growth perpetuity assumes borrowing forever; I kept the credit with the growth spending and showed the literal reading
beside ($53.92 against $29.20 no-growth at the sovereign, a large difference, though both fail the floor). The text should
say which spending the credit is set against when (e) applies. **(3) Net or gross debt raised.** The paragraph says "the
long-term debt raised over the window"; gross issuance and the net increase differ; I used net and confessed it.
**(4) Minority interests in a consolidated utility.** Nothing in Q7 says how to take a 19.9% minority's share out of
consolidated owner cash, or whether the price received for a stake sale is owner cash; I used the minority's net cash
flows and excluded the stake sale, confessed. **(5) The tool.** `tools/run.py`'s debt table for this filer printed total
capitalization under a "debt" heading; a run that took it would have overstated debt by the whole of the equity.
**(6) Growth when the all-spending series changes sign.** Specific (b) moves to halves and then to "the no-growth case
alone"; for a utility whose all-spending owner cash is negative by design, growth has to be measured on the maintenance
series with the growth spending charged separately, which (e) implies and (b) does not say.
