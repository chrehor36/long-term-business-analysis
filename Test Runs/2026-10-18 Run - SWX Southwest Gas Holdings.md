# Company Run — Southwest Gas Holdings, Inc. (NYSE: SWX) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (ce330c6c): `PORTFOLIO.md` read for this one ticker; the operator does not hold SWX (no line names SWX, Southwest Gas or Centuri).*

**Contamination, declared before any verdict.** (1) To find whether today's run file already existed, a directory listing
of `Test Runs/` filtered to the date 2026-10-18 was run before the template was copied; it showed the names of six other
run files of today and their research folders (HOKCY, MDU, NJR, NWN, OGS, XNGSY). None was opened. (2) The session context
supplied, unasked, the subjects of the last five commits, which describe the fold of the OGS run (ONE Gas, a gas
distributor): "OUT at Q7, on the floor", "Q2 IN as the regulated exception [...] TOO HARD (NATURE) named as the other
reading", "Q3 and Q6 against", "peer-set dividend while issuing stock". These were seen before any SWX filing was read.
They are another company's verdicts and are not used; where this run reaches a like reading, it reaches it from the
SWX filings and the framework text, and the self-audit says so. (3) Two ledger-memory lines in the session context name
counts of runs and a "queue state"; nothing in them names SWX.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $87.45 (close 2026-10-16, printed by `tools/run.py`; aggregator, live quote only, flagged per operator
  rule 5). The 10-K's Item 5 gives $86.64 at February 18, 2026 (0001692115-26-000062).
- **Shares by class:** one class, common stock $1 par. **72,445,853** shares on the cover of the 10-Q for the quarter
  ended 2026-06-30, filed 2026-08-05, as of 2026-07-31 (accession `0001692115-26-000112`; `python Screens/cover_shares.py
  SWX`). Checked against the balance sheet of the same 10-Q: issued and outstanding 72,443,899 at 2026-06-30; issued equals
  outstanding (no treasury stock, `tools/run.py` balance-sheet issued count 72.444M). Filings after the 10-Q, by the EDGAR
  submission list read 2026-10-18: Forms 4 and 144 only (2026-09-28, 2026-09-29); no 8-K, prospectus or 424B after it.
  The ATM program had $340.0M of stock available at 2025-12-31 and no issuance in 2025 (10-K, MD&A, Liquidity).
- **Market cap:** 72.445853M x $87.45 = **$6,335.4M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 10/16/2026
  (issuing authority; printed by `tools/run.py` from `tools/sources.py`).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-25, `0001692115-26-000062` (combined filing of Southwest Gas Holdings, Inc. and Southwest
    Gas Corporation): Items 1, 1A, 3, 5, 7, 8 (both registrants' statements, Note 3 revision, Note 13 dispositions, Note 14
    restatement, the tax note), 9A.
  - 10-Q for 2026-06-30, filed 2026-08-05, `0001692115-26-000112`: balance sheet, debt note, segment results, MD&A.
  - DEF 14A filed 2026-03-23, `0001692115-26-000080`: compensation discussion, related-person transactions, board.
  - 8-Ks: 2026-01-09 Items 2.02, 4.02, 7.01 (`0001692115-26-000004`); 2026-02-25 Item 5.02, CEO resignation and successor
    (`0001193125-26-071537`); 2026-02-11 Item 5.02 (`0001193125-26-045442`); 2026-01-02 Item 5.02 (`0001193125-26-000920`);
    2025-10-14 Item 1.01, Icahn cooperation agreement (`0001193125-25-239100`); earnings releases furnished 2026-02-25
    (`0001692115-26-000060`) and 2026-08-05 (`0001692115-26-000109`).
  - The cycle: 10-K FY2023 (`0001692115-24-000038`), FY2022 financial-statements document (`0001692115-23-000056`),
    FY2021 (`0001692115-22-000005`), FY2020 (`0001692115-21-000008`), FY2019 Exhibit 13.01 (`0001692115-20-000016`).
  - Rivals: Williams combined 10-K FY2025 including Northwest Pipeline LLC (`0000107263-26-000006`); Berkshire Hathaway
    Energy combined 10-K FY2025 (`0001081316-26-000003`) and FY2022 (`0001081316-23-000005`), for Nevada Power Company and
    Sierra Pacific Power Company; Northwest Pipeline LLC XBRL company facts 2015 to 2023 (SEC API, transcription).
- **One figure cross-checked against the filed statement:** Holdings' 2025 operating cash flow, `tools/run.py` 556 against
  the filed statement of cash flows $556,076 thousand; capital expenditures 808 against $807,866 thousand; long-term debt
  3,433 against $3,433,012 thousand (10-K FY2025). All agree.
- **`tools/run.py` arithmetic lines used:** price, share counts, the sovereign, the Holdings ten-year balance-sheet table
  and its OCF/capex/D&A lines. Not used: its owner-earnings means (Holdings consolidated, which mix Centuri's discontinued
  operations and the gas-cost swings into one series) and its debt table, whose first column is
  `CapitalizationLongtermDebtAndEquity`, a tag that includes equity, so its "sum" is not debt. The run builds owner cash
  from Southwest Gas Corporation's own filed statements instead (Q4, Q7).

**The lines of evidence chosen, and why.** From Item 1 (one segment since August 2025, three states, rate regulation,
decoupling, purchased-gas pass-through, competition from electric utilities and interstate pipelines), Item 1A
(regulation, rate lag, electrification policy, the material weakness, the activist history) and Item 7 (results, rate
cases, capital plan, liquidity), the run reads: (1) **Southwest Gas Corporation's own statements**, filed in every 10-K of
the window, as the record of the business that remains; (2) **the divestitures**: MountainWest (Questar Pipelines, bought
2021-12-31 for $1.576B, sold 2023-02-14) and Centuri (IPO 2024-04-22, deconsolidated August 2025, last shares sold
2025-09-05) are treated as businesses no longer owned: their earnings are left out of the window, and what they returned is
in today's cash and debt; their purchase and sale are weighed at Q5 and Q6 as uses of the owners' money; (3) **the
purchased-gas (PGA) balances**, because the 2021-2023 gas-price spike and its recovery swing operating cash by hundreds of
millions a year; (4) **the rate cases** (allowed and earned returns); (5) **the capital plan** (2026-2030 $6.3B, the Great
Basin expansion); (6) **debt, leases, share issuance, the ATM and DRIP, dividends**; (7) **stock pay and the proxy**;
(8) **the restatement, the Note 3 revision and the material weakness**; (9) **litigation** (Item 3: none material in
management's opinion); (10) **the rivals' own filings** for Q2.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the regulated network will produce for its owners, not where the quote goes
**[M1997-109]**. No macro forecast enters: the gas price, the rate level and the national electrification debate are not
forecast; they enter only as properties of this business (the gas price is passed through; the cost of capital is set by
regulators) **[M2000-094]**. Who is paid to tell you: the company publishes earnings-per-share and rate-base growth
guidance and an "adjusted" earnings figure, and pays its officers on an adjusted figure (Q4, Q5, Q6); the projections are
not used **[M1995-050]**. The analyst's habits: hunt what is wrong **[M2025-013]**. **Contrary evidence, written down as
found** **[M1997-127]**: (a) owner cash after all capital spending was negative in every year of the window (Q3, Q7);
(b) the earned return on equity sat below every allowed return in every year read (Q2, Q3); (c) the business has needed
new money from its parent in most years and the parent issued about $1.65B of stock from 2017 to 2025 while paying about
$1.37B of dividends (XBRL, Holdings; Q6); (d) the 2025 interim statements were declared unreliable and a material weakness
was found (Q4); (e) the CEO resigned in February 2026, a year after a special retention award, and the CFO changed in
December 2025 (Q5); (f) the company bought a pipeline business for $1.576B at the end of 2021 and recorded a $449.6M
goodwill impairment on deciding to sell it within a year (Q5, Q6); (g) California's and Nevada's policies on gas use and
the free carbon allowances move against gas distribution (Q2).

## THE STANDING RULE
Nothing in a purchase of SWX common stock for cash puts the buyer at risk of ruin; the rule binds the buyer's financing
and sizing, not the target **[M2012-081]**, **[L2014-005]**. The target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The business, from Item 1 (0001692115-26-000062).** Southwest Gas buys, distributes and transports natural gas to
  about 2,281,000 customers in Arizona (1,224,000), Nevada (849,000) and California (208,000); 37,000 first-time meters in
  2025 (1.6%). Rates are set by the ACC, the PUCN and the CPUC on rate base, cost of service and cost of capital; all
  three states decouple margin from volume; gas cost is passed through under PGA clauses "without markup" (MD&A). 85% of
  operating margin comes from residential and small commercial customers, 11% from transportation. Great Basin, an
  interstate pipeline under FERC, is a subsidiary; its 2028 expansion is now estimated at about $2.3B (earnings release
  2026-08-05, `0001692115-26-000109`).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) rate base, which is the plant the company
  builds and the regulators admit, growing about 7% a year in the window (gas plant $8,384M at 2020 to $11,517M at 2025,
  Q4); (2) the allowed return on equity (9.5% Nevada, 9.84% Arizona, MD&A) and the gap between it and the earned return
  (regulatory lag); (3) customer growth in Phoenix, Tucson and Las Vegas; (4) the cost of the debt and equity that must be
  raised; (5) state policy on new gas connections. The first four are written down by the industry itself, five years out,
  in the company's own guidance and in rate filings; they are the kind of forecast insiders do write, the inverse of
  **[M2000-105]**. The fifth is a policy forecast; it is weighed at Q2, test 11, where the framework puts what could
  destroy or reduce the castle **[M2000-014]**.
- **Understanding, as the rows define it.** A "reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**: earning power here is allowed return times equity in rate base, less
  the lag; the competitive position is a franchise network whose rival is the electric utility at the moment of
  installation. The chemistry of gas is not needed, "What is important is that I understand the economic dynamics of the
  industry" **[M2011-014]**. A holding company read by its parts: since August 2025 there is one part, the Natural Gas
  Distribution segment (Item 1), so the parts rule decides nothing.
- **Doubt, tested** **[M2002-092]**. The 2023 letter warns that "the regulatory climate in a few states" makes it "difficult
  to project both earnings and asset values" **[L2023-011]**, naming California. California is 12% of SWG's 2025 operating
  margin (MD&A). The warning is weighed at Q2 test 11 (what could reduce the castle) rather than here, because it bears on
  the castle's returns, not on whether the economics can be pictured; a row about named companies decides no STOP alone
  (Q2, a row about one company).
- **Routing.** Not a business of fast-changing technology; not a bank; one operating part.
- **VERDICT: IN.** The economics of a decoupled, rate-regulated gas distributor can be pictured ten years out within a
  range: rate base, allowed return, lag and customer growth are written in the filings **[M2000-037]**, **[M2012-065]**;
  what cannot be forecast (state policy on gas) is a threat to be weighed at Q2, not a reason the economics cannot be
  understood **[M2006-076]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**

**The castle tests, each with its filing fact** (10-K FY2025, `0001692115-26-000062`, unless stated):
- **The attacker with money** **[M2011-015]**. Nobody can lay a second gas network under Phoenix, Tucson and Las Vegas
  and take the customers: the service territories are granted and regulated by the three commissions (Item 1, "Rates
  and Regulation"); the 10-K names no rival distributor in its territory. The attacker that exists is the electric
  utility, which competes "at the initial installation phase when the customer/builder typically makes the decision";
  after that "the customer will generally continue to use the chosen energy source for the life of the equipment"
  (Item 1, Competition). Against that attacker the filing reports that in 2025 Southwest Gas "provided natural gas to a
  large majority of the new homes constructed during the year in the major metropolitan markets" of its territories.
  The second attacker is bypass: large customers near the interstate pipelines (El Paso, Kern River, Transwestern,
  Tuscarora, Ruby), met by negotiated rates; transportation is 11% of operating margin.
- **Pricing power and the agony before a rise** **[M2005-020]**. There is no pricing power in the rows' sense: every
  price is a rate case. In the window the company asked and got less each time: Arizona asked $125.6M and a 10.15% ROE
  and was granted $80.2M and 9.84% (decision March 2025); Nevada asked $74.0M and was granted $59.1M at 9.5% (MD&A, Rates
  and Regulatory Proceedings). The agony is institutional, and by this test the business is not strong; the framework
  sends a return set by a regulator to Q3 as a second best rather than to OUT (What it rules OUT, the standing castle
  that protects only ordinary returns).
- **Unit volume and share of mind** **[M1999-054]**. Customers rose to 2,281,000 (37,000 first-time meters in 2025,
  41,000 in 2024); decoupling makes margin independent of volume per customer. Throughput is not the measure here; the
  count of connected customers is, and it rose every year read.
- **The low-cost position** **[M2004-091]**. Against electricity for space and water heating the 10-K claims "the
  abundance, low cost, resiliency, and reliability of natural gas"; the filing gives no cost comparison by state, so the
  claim is the filer's and is weighed lightly.
- **The brand / the low bid** **[M2017-009]**. Not applicable in the usual sense: a residential customer cannot buy gas
  delivery from anyone else at the meter.
- **Ask the competitors** **[M1999-130]**. Not available on the public record beyond the filings below.
- **Widening or narrowing** **[M1999-108]**. The earned return on equity rose from 6.0% (2022) to 8.5% (2025) on
  year-end equity (competitor row below), still below every allowed return; the company itself states the aim as
  "improvements in our achieved returns" through formula ratemaking (earnings release 2026-02-25). Nevada passed SB 281
  (2023), a three-year planning process for gas utilities with pre-approval of certain investments; Arizona bars
  municipal bans on gas service (Item 1). These widen the moat in two states.
- **What could destroy, modify or reduce it** **[M2000-014]**: (1) **state policy on gas**: California's cap-and-invest
  law AB 1207 "contemplates the transition of gas utilities’ free allowances to electric utilities", which "may result
  in higher costs for natural gas utilities over time" (Item 1, Environmental Matters); California is 12% of 2025
  operating margin, Nevada 35%, Arizona 53% (MD&A); (2) **the regulators' returns**: "I did not anticipate or even
  consider the adverse developments in regulatory returns" **[L2023-011]**; the speakers' own utility mistake is exactly
  this; (3) **a catastrophe**: "A catastrophic event can render a single utility insolvent" **[L2005-019]**: a gas network
  in three states, with pipeline-safety rules (MD&A, Pipeline Safety), carries that risk; it is weighed at Q9.

**The competitor row.** The 10-K names its rivals as the electric utilities (not named by name) and the interstate
pipelines El Paso, Kern River, Transwestern, Tuscarora and Ruby (Item 1, Competition), and, for Great Basin, Ruby,
Tuscarora, Northwest Pipeline, Pinyon and Prospector. Named rivals that file with the SEC: **Northwest Pipeline LLC**
(named as NWPL and "Northwest Pipelines"); and **Nevada Power Company and Sierra Pacific Power Company** (d/b/a NV Energy,
named as an LDC on Great Basin and the electric utility of Southwest Gas' Nevada territory, so a named party and the
electric rival in the 35% of margin earned in Nevada). Named rivals that do not file: El Paso Natural Gas (last 10-K
2012-02-27), Kern River, Transwestern, Tuscarora, Ruby, Pinyon, Prospector. The Arizona electric utilities are not named in
the 10-K and are not used. Metric: net income over year-end equity, as each filed it (a reporting basis of this run; the
filers' own ROE definitions differ).

| Year | Southwest Gas Corp. | Nevada Power | Sierra Pacific Power | Northwest Pipeline |
|---|---|---|---|---|
| 2016 | n/r | n/r | n/r | 13.1% (180 / 1,377) |
| 2018 | 7.8% (138.8 / 1,782) | n/r | n/r | 11.7% (131 / 1,121) |
| 2019 | 8.1% (163.2 / 2,005) | n/r | n/r | 12.4% (143 / 1,153) |
| 2020 | 7.1% (159.1 / 2,233) | n/r | n/r | 13.2% (151 / 1,140) |
| 2021 | 7.4% (187.1 / 2,528) | 10.0% (303 / 3,030) | 8.1% (124 / 1,535) | 12.3% (136 / 1,109) |
| 2022 | 6.0% (154.4 / 2,569) | 8.9% (298 / 3,354) | 5.8% (118 / 2,048) | 12.4% (137 / 1,108) |
| 2023 | 7.2% (228.4 / 3,184) | n/r | n/r | 15.9% (180 / 1,133) |
| 2024 | 8.1% (262.1 / 3,235) | 7.8% (349 / 4,448) | 4.0% (85 / 2,100) | 15.5% (180 / 1,163) |
| 2025 | 8.5% (300.3 / 3,525) | 5.3% (247 / 4,690) | 4.9% (146 / 2,981) | 12.7% (181 / 1,427) |

Sources: Southwest Gas Corporation statements in the 10-Ks listed at Step 0 ($M; 2023 net income as adjusted in the FY2025
10-K); Nevada Power and Sierra Pacific from the BHE combined 10-Ks `0001081316-26-000003` (2023 to 2025 income, 2024 and
2025 equity) and `0001081316-23-000005` (2020 to 2022 income, 2021 and 2022 equity); Northwest Pipeline from XBRL company
facts (2015 to 2023, transcription) and the Williams combined 10-K `0000107263-26-000006` (2023 to 2025). n/r = not read.
Northwest Pipeline's 2017 figure (a loss of $28M) carried the 2017 tax-law charge and is left out of the table and said so.

**The parts table.** One part since August 2025: Natural Gas Distribution (Southwest Gas, including Great Basin), 100%
of operating profit after the separations. Centuri and MountainWest are not owned and are not read as parts. The part
decides.

**The field's returns over the last full cycle, judged in words.** The window crosses the 2021-2023 gas-price spike and
its unwinding (Q4) and a full round of rate cases in all three states, so it is taken as a cycle. The distributors and
electric utilities of this territory earned single-digit returns on equity throughout, 4% to 10%, and Southwest Gas sat in
the middle of that band and below its own allowed returns every year. The FERC pipeline earned 12% to 16%. The field is a
standing castle that protects ordinary returns, not excellent ones **[L2007-004]**; but the return is set by a regulator,
which the framework names as the exception carried to Q3 as a second best: "there’s no way we get rich on our utility
investments. But there’s no way we get poor, either." **[M2009-104]**; capital-heavy businesses are entered on "decent
returns on the incremental sums they invest" **[L2009-012]**.

**The other reading, stated.** A castle whose future cannot be judged is TOO HARD **[M2000-019]**: whether California and
Nevada will restrict new gas connections within ten to twenty years is a policy forecast the industry's insiders would not
write down. Against it: Arizona, 53% of margin, has barred municipal restrictions by statute; the filer won most new homes
in its metros in 2025; Nevada's 2023 law sets up pre-approval of gas investments rather than a phase-out. The threat is
real and slow **[M2014-038]**, and it is weighed, not found decisive, on the evidence read.

- **VERDICT: IN**, as the regulated exception: the franchise network stands and no rival with money can duplicate it
  **[M2011-015]**; the returns it protects are ordinary and regulator-set, carried to Q3 as a second best **[M2009-104]**,
  **[L2009-012]**. The policy threat in California and Nevada is recorded as the strongest evidence against the castle
  **[M2000-014]**, **[L2023-011]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
Southwest Gas Corporation, $M, from its own filed statements (Step 0). Return on all capital = (net income + interest
paid x (1 - 0.24)) / (year-end equity + all borrowings); the 24% marginal tax on interest is a CONVENTION of this run
(21% federal plus about 3% state, from the FY2025 rate reconciliation; rationale: the all-equity figure needs the tax the
interest saves, and the effective rate is pulled down by excess-deferred-tax amortization that has nothing to do with
interest).

| Year | Net income | Interest paid | Equity (YE) | Borrowings (YE) | Return on all capital | Return on equity (YE) | Capex | D&A | Capex / D&A |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | 187.1 | 90.2 | 2,528 | 2,966 | 4.7% | 7.4% | 602.0 | 253.4 | 2.4x |
| 2022 | 154.4 | 108.0 | 2,569 | 3,476 | 3.9% | 6.0% | 683.1 | 263.0 | 2.6x |
| 2023 | 228.4 | 139.7 | 3,184 | 3,502 | 5.0% | 7.2% | 762.1 | 295.5 | 2.6x |
| 2024 | 262.1 | 157.0 | 3,235 | 3,504 | 5.7% | 8.1% | 846.6 | 303.1 | 2.8x |
| 2025 | 300.3 | 177.0 | 3,525 | 3,508 | 6.2% | 8.5% | 807.9 | 330.7 | 2.4x |

- **What it earns on the capital it needs** **[M2010-090]**, **[M2011-060]**: 3.9% to 6.2% after tax on all capital, against
  a 30-year Treasury of 5.43% today; on equity, 6.0% to 8.5%, below every allowed return (9.5% Nevada, 9.84% Arizona).
  2025 includes a $16.4M state tax benefit from the apportionment change, which the company itself removes in its adjusted
  figure (earnings release 2026-02-25).
- **To stand still and to grow** **[L1999-024]**, **[M2000-144]**. Capital spending ran 2.4 to 2.8 times depreciation.
  The filing says "the majority" of 2025's $840.2M of construction "represented costs associated with replacement of
  existing transmission and distribution plant to fortify system integrity and reliability" (MD&A, 2025 Construction
  Expenditures). So the spending needed to stay in place is above the depreciation charge, as at the railroad "BNSF must
  annually spend more than its depreciation charge to simply maintain its present level of business" **[L2023-009]**;
  the difference here is that the regulator lets the replacement into rate base and pays a return on it. The guess
  (Q7): maintenance between depreciation ($289M a year average) and half of capital spending ($370M); depreciation is
  taken as the generous end and said so.
- **Compulsory reinvestment.** Pipe replacement under integrity-management rules and franchise requirements is spending
  the business must do "the same way if it’s unattractive" **[M1998-128]**; the speakers "tried to avoid places where
  there was a lot of compulsory reinvestment just in order to stand still" **[M1997-016]**. And of utilities in
  inflation: "To earn more, their owners must invest more." **[L2011-019]**
- **Is there ever any cash** **[M2003-122]**, **[M2008-036]**. Owner cash after all capital spending was negative every
  year (Q7 table: about -$206M to -$346M a year on the all-equity basis). The gap was filled by the parent: contributions of
  $202.6M (2021), $530.0M (2023) and $20.0M (2025), while the utility paid the parent dividends of $651.7M over the five
  years; and by borrowings, up from $2,495M (2020) to $3,508M (2025). For 2026 to 2030 the company expects operating cash
  to provide "approximately 60% of the funding for total construction expenditures, and dividend requirements" (MD&A,
  Capital Expenditures), against $6.3B of planned spending before the Great Basin estimate rose to $2.3B.
- **What the added capital earned.** All capital rose from $4,728M (2020: equity 2,233, borrowings 2,495) to $7,033M
  (2025), +$2,305M; net income plus after-tax interest rose from $232.6M (2020: 159.1 + 96.7 x 0.76) to $434.8M, +$202.2M,
  about 8.8% on the added capital (about 8.1% without the 2025 tax benefit). That is a decent return on the incremental
  sums in the rows' sense **[L2009-012]**, and above today's Treasury rate; it is below the floor of about 10% that Q7
  applies.
- **Second best, named.** "as the second-best choice, still a good choice, the answer is yes. It’s not as good as the best
  choice." **[M2018-055]**; "cash-consuming businesses, by their nature, are unattractive unless the cash they consume gets
  to earn a reasonable return" **[M2012-057]**; a growing utility is liked because "the reinvested money is going to do
  exceptionally well" **[M2014-088]**, which here it has not: the earned return sat below the allowed return in every year.
- **WEIGHS AGAINST.** A second best whose incremental capital earns about 8% to 9% after tax and whose owners must keep
  putting money in, with returns on all capital of 4% to 6% and no year of positive owner cash after spending
  **[L2011-019]**, **[M2003-122]**, **[M2012-057]**; the regulated return keeps it from being the "worst business"
  **[M1998-081]**, since the added capital earns more than the bond. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, before the income account** **[M2025-032]**. $M, year-end.

Southwest Gas Holdings (consolidated; `tools/run.py` first-filed XBRL, checked against the FY2025 and FY2023 statements):

| | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| Total assets | 7,358 | 8,170 | 8,736 | 12,765 | 13,197 | 11,870 | 12,024 | 10,429 |
| Equity (Holdings) | 2,252 | 2,506 | 2,675 | 2,954 | 3,059 | 3,310 | 3,504 | 3,961 |
| Goodwill | 359 | 343 | 345 | 1,781 | 787 | 790 | 781 | 11 |
| Long-term debt (non-current) | 2,107 | 2,300 | 2,732 | 4,116 | 4,403 | 4,610 | 4,348 | 3,433 |
| Retained earnings | 944 | 1,039 | 1,068 | 1,114 | 747 | 739 | 759 | 1,023 |
| Shares outstanding (M) | 53 | 55 | 57 | 60 | 67 | 72 | 72 | 72 |

Southwest Gas Corporation (the business that remains; its own filed balance sheets, Step 0 accessions):

| | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| Net plant | 5,093 | 5,685 | 6,176 | 6,547 | 7,025 | 7,518 | 8,109 | 8,691 |
| Equity | 1,782 | 2,005 | 2,233 | 2,528 | 2,569 | 3,184 | 3,235 | 3,525 |
| of which paid-in capital | 1,065 | 1,229 | 1,410 | 1,619 | 1,623 | 2,157 | 2,165 | 2,195 |
| of which retained earnings | 717 | 782 | 835 | 907 | 935 | 1,018 | 1,060 | 1,315 |
| Borrowings (long-term, current, short-term) | 1,971 | 2,310 | 2,495 | 2,966 | 3,476 | 3,502 | 3,504 | 3,508 |
| PGA balance, receivable (+) / payable (-) | n/r | -16 | -53 | 291 | 450 | 553 | -242 | -305 |

What the balance sheets say. (1) **The plant grew $3.6B in seven years and the owners paid for it mostly with new money.**
The utility's equity rose $1,743M, of which $1,130M was paid-in capital from the parent and $598M retained earnings;
borrowings rose $1,537M. At Holdings, retained earnings were $944M in 2018 and $1,023M in 2025: in seven years almost
nothing was kept for the owners, while shares outstanding rose from 53M to 72M. (2) **Goodwill tells the deal history**:
$345M in 2020, $1,781M after the 2021 purchases of Questar Pipelines and Riggs Distler, $787M after the 2022 impairment of
$449.6M on deciding to sell MountainWest (FY2022 10-K), $11M once Centuri was gone. (3) **The gas-cost balance swung from a
$553M receivable (2023, the old definition) to a $305M payable (2025)**: the 2021-2023 spike was paid out of the
company's pocket and then recovered from customers, so operating cash was depressed in 2021-2022 and inflated in 2024;
the payable is money owed back to customers through lower rates. (4) Holdings' cash of $577M at 2025 (and $271M at
2026-06-30) is the residue of the Centuri sales, not of the utility.

**The real costs** **[L2021-003]**, **[L2015-004]**:
- **Depreciation** is real and short: replacement spending is "the majority" of a construction budget that runs 2.4 to
  2.8 times the depreciation charge (Q3) **[L2015-004]**.
- **Stock pay** ($4.9M to $13.0M a year at the utility) is expensed in net income; the run removes its add-back from
  operating cash (Q7) **[L2015-003]**.
- **Deferred taxes.** The utility paid almost no cash income tax in the window ($0 in 2023 and 2024, $1.0M in 2025, refunds
  in 2020 and 2021) because of accelerated tax deductions and a net operating loss (Holdings: federal NOL $599.4M and
  state NOLs $435.7M on a return basis; NOL deferred tax asset $146.3M at 2025). The run charges tax at the income
  statement's provision and counts the NOL as a separate shelter (Q7, Whose tax).
- **Pensions.** Assumed long-term return 7.00%, discount rate 5.75% (MD&A, Critical Accounting Policies); the defined
  benefit plan is closed to hires after 2021. Not fanciful on their face **[L2002-039]**.
- **EBITDA in the filer's own mouth:** not found in the 10-K or the two earnings releases read; the releases feature
  "operating margin", "adjusted net income" and "adjusted utility ROE".

**What the accounts say of management's character** **[M1995-064]**:
- **The restatement.** On 2026-01-09 the Audit Committee concluded that the interim statements for 2025-06-30 and
  2025-09-30 "should no longer be relied upon" (8-K Item 4.02, `0001692115-26-000004`): income tax expense and net deferred
  tax liabilities were understated by $27.3M (six months to June) and $35.1M (nine months to September), because state
  apportionment rates were not updated after the Centuri share sales of May and August 2025; a further $75.0M of current
  debt maturities had been classified as long-term at 2025-09-30 (10-K Note 14). No effect on the annual results.
- **The revision.** The same error ran at Southwest Gas Corporation back to the holding company's formation in 2017; it
  was judged not material to any prior year but the prior statements were revised for its cumulative size, "to correct
  other previously identified immaterial errors" as well (Note 3).
- **The material weakness.** Holdings' internal control over financial reporting was not effective at 2025-12-31 (a review
  control over state apportionment rates); disclosure controls were found not effective as of the two restated quarters
  after first being found effective; PwC's report on Holdings' controls says the same; the utility's controls were found
  effective (Item 9A).
- **Reclassification.** $294.9M (2023) and $74.3M (2024) of accrued purchased gas costs were moved between operating-cash
  lines; totals unchanged (Note 2).
- **Guidance and an adjusted figure.** The company gives annual EPS guidance ($4.17 to $4.32 for 2026), a five-year EPS
  growth range (12% to 14%) and a rate-base growth range, and headlined that 2025 "Exceeded Top End of 2025 Net Income
  Guidance Range" (earnings release 2026-02-25). The adjusted utility figure for 2025 ($283.9M) was **below** GAAP
  ($300.3M), removing a tax benefit; the proxy's incentive figure ($273.9M) was lower still. Guidance and a featured
  adjusted figure weigh against here **[L2019-006]**, **[L2016-006]**, and are carried to Q5 (section A of the gaps case).

**Why this is not the STOP.** The STOP falls on accounts that confuse or raise suspicion **[M1995-063]**, **[M2003-029]**.
The errors here are named, quantified, dated and traced to one cause (an estimate not updated after a change in the
group's structure); the company found them itself in its year-end review and filed the 4.02 before the 10-K; the
direction of the interim error flattered two quarters, but the annual figures were unaffected and the adjusted figure
that management features ran below GAAP rather than above it. None of the account-level tells is present: no prepaid or
deferred accounts building without explanation (the deferred charges and regulatory balances are tied to named
mechanisms in the regulatory assets and liabilities table of the 10-K), no reserves moving with a stock sale, no profits that may not exist **[M1995-064]**. Two errors and
a weakness in one review control are a cockroach count to be weighed **[L2002-039]**, not a confusion that cannot be read.
- **VERDICT on the accounts: IN (no STOP); WEIGHS AGAINST**: a restatement of two quarters, a revision back to 2017 and a
  material weakness in the year the business was reshaped **[L2002-039]**; guidance and a featured adjusted figure carried
  to Q5 **[L2019-006]**, **[L2016-006]**, **[M1994-018]**. The recast owner cash (Southwest Gas Corporation, gas-cost
  swings removed, stock pay and deferred tax charged) feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**The people in the window.** Karen S. Haller, President and CEO through 2025, resigned on 2026-02-19, effective
2026-05-08; Justin L. Brown, President of Southwest Gas, succeeded her (8-K `0001193125-26-071537`). The CFO, Robert J.
Stefani, left by agreement effective 2025-12-01 (8-K `0001193125-25-266887`, filed 2025-11-05: "not a result of any
disagreement with the Companies’ independent auditors or any member of management"); a new CFO started 2025-12-01. The
board chair is an independent director, E. Renae Conley (DEF 14A). The Icahn Group, a holder of more than 5% in 2025,
designated four directors under cooperation agreements from 2022; one resigned on 2025-12-31 and was not replaced
(8-K `0001193125-26-000920`).

**The two yardsticks** **[M1994-008]**.
- **How they ran the business, against the hand dealt.** The hand: a decoupled franchise in the fastest-growing
  territories of the Southwest, 37,000 to 41,000 new meters a year. The play: earned returns on equity of 6.0% to 8.5%
  against allowed returns of 9.5% and above in every year read (Q2, Q3); rate cases settled for less than asked in each
  state (Q2); S&P upgraded both companies to BBB+ (earnings release 2026-02-25); the Centuri proceeds repaid $709.0M of
  debt (10-K, MD&A). **Capital allocated over time**: Questar Pipelines bought for $1.576B on 2021-12-31 with a 364-day term
  loan (FY2021 10-K), a $449.6M goodwill impairment recorded in the fourth quarter of 2022 on deciding to sell, sold
  2023-02-14 with a further $50.0M of impairment and loss on sale in 2023 (FY2025 10-K, Corporate and Administrative);
  Riggs Distler bought by Centuri on 2021-08-27 (FY2021 10-K); Centuri taken public in April 2024 and sold down through
  September 2025 for about $1.3B of 2025 proceeds and a $343.1M gain on deconsolidation (FY2025 10-K, MD&A). The proxy speaks
  of "our investors’ directive to rapidly separate Centuri" (DEF 14A, compensation discussion). The pipeline purchase lost
  about half a billion dollars in fourteen months.
- **How they treat their owners** **[M1994-009]**: weighed at Q6 Part B (pay, board, owners).

**Integrity, the STOP** **[M2005-003]**, **[M2013-088]**. The tells the rows name, read against the record:
- **Reports that dance** **[M1995-111]**: the 10-K explains the restatement, the revision and the weakness in plain terms
  with the amounts (Q4); the 4.02 was filed on 2026-01-09, before the 10-K. No dancing found.
- **Too good to be true** **[M2002-028]**: the long-range EPS growth range of 12% to 14% a year for 2026 to 2030
  (earnings release 2026-08-05) is ambitious for a utility, but it is tied in the release to a named project (the Great
  Basin expansion, with contracted demand stated) and a rate-base growth range of 9.5% to 11.5%, not to unexplained
  margin gains.
- **A management fixed on its stock price** **[M2004-067]**: no instance found in the documents read (the 10-K, both
  releases and the proxy were searched for stock-price targets; the proxy's relative TSR modifier on one special award is
  the nearest).
- **The habits carried from Q4**: annual EPS guidance, a headline that net income "Exceeded Top End" of guidance, and a
  featured adjusted figure **[L2002-041]**, **[L2019-006]**, **[L2016-006]**. Read with the rest of the record: the
  adjusted utility figure was below GAAP in 2025 (it removed a tax benefit), and the incentive figure lower still; the
  habit is guidance, not making the numbers by adjustment. It weighs against; it does not raise a doubt about honesty.
- **How they talk about mistakes** **[L2024-003]**: no instance found of the MountainWest loss or the restatement called a
  mistake (a text search for "mistake" in the FY2025 10-K, the FY2023 and FY2022 10-K statements, both releases and the
  proxy found none); the MountainWest sale is described as simplifying the company. A weight against candour, not a tell
  of dishonesty.
- **A sequence recorded and not read as a tell.** The CFO who signed the June and September 2025 quarterly reports left by
  agreement, announced 2025-11-05; the errors in those quarters were found later, "in connection with the preparation of
  this Form 10-K" (Item 9A). The filings give no link between the two, and the 8-K says the departure was not the result of
  a disagreement with the auditors. Written down as found **[M1997-127]**; no inference drawn.
- **Related persons.** 5,490,882 Centuri shares were sold to the Icahn Group in private placements in 2025 "at prices ranging
  from $17.50 to $20.75 per share, the same prices available to the public", approved by the nominating committee (DEF 14A,
  Related Person Transactions). Disclosed and at the public price.

**Love of the business and ability** **[M2000-098]**, **[M1999-104]**. A hired management of a regulated utility; the
after-the-sale test does not apply to a market purchase **[M2007-081]**. The departing CEO keeps a salary and her awards' vesting as an advisor through
2026 (Q6 Part B). Ability weighs against on the capital record (the MountainWest round trip) and on the earned-return
gap; for, on the rate cases now in progress in all three states and the credit upgrade.

- **VERDICT on integrity: IN.** No tell of dishonesty found on the record read; the errors were found, quantified and
  disclosed by the company **[M1995-111]**, **[M2013-088]**. **Ability WEIGHS AGAINST**: half a billion dollars lost on a
  pipeline bought and sold within fourteen months, returns below the regulators' allowance throughout, and turnover at the
  top in 2025 and 2026 **[M1994-008]**, **[M2021-042]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
- **The retention test** **[R1995-009]**, **[M1998-110]**. Little was retained. At Holdings, retained earnings were $944M
  at 2018 and $1,023M at 2025 (Q4); the earnings of the years went out as dividends ($1,365M paid 2017 to 2025, XBRL
  `PaymentsOfDividendsCommonStock`) or were lost on MountainWest. The money that built the plant was new money: stock
  issued for $1,649M of proceeds from 2017 to 2025 (XBRL `ProceedsFromIssuanceOfCommonStock`: 41, 354, 158, 139, 214, 462,
  252, 9, 20) and $1.5B more of utility borrowings (Q4). The test is therefore less "was a dollar kept worth a dollar" than
  "was a dollar raised worth a dollar"; on Q7's computation (below) the value per share is far below the price at which
  the stock was sold, which hurts the buyers of the new shares, not the holders who sold them, and says the owners' money
  went into plant that earns a regulated return under the floor.
- **Serial issuance** **[L2014-015]**: shares outstanding rose from 47M (2016) to 72M (2025), +54%, with stock sold in every
  year from 2017 to 2023 and through the DRIP since (2025: 256,000 shares for $19.2M); $340.0M remains under the ATM program
  and the 2026-2030 plan expects operating cash to fund only about 60% of spending and dividends (Q3). The framework
  carries serial issuance as a candidate second STOP, unresolved (section VI); here it is weighed heavily against. For a
  regulated utility the issuance is how rate base is financed at the commission's equity ratio, which is the reader's
  explanation, not a row's.
- **Dividends** **[M2004-089]**, **[M2000-051]**: paid every year since 1956 and raised 4% for 2026 to $2.58 a year; the
  board sets it considering, among other factors, "the competitiveness of the dividend yield" (10-K Item 5). A dividend set
  against peers' yields while the company sells stock to fund its spending is the ratio approach the rows call "nuts"
  **[M2000-051]**, applied in the reverse direction: the owners are paid out and then asked back in, less the costs.
- **Buybacks**: none found (10-K Item 5 reports none; no repurchase tag in the XBRL facts read). The test of a buyback
  against the bottom of the Q7 range does not arise; the bottom is written back here for the record: **-$35.65 a share on
  the all-equity basis** (Q7).
- **Issuance and deals, value given against value got** **[M1995-001]**, **[L1994-015]**. Questar Pipelines: $1.576B given
  at 2021-12-31, sold 2023-02-14 for $1.5B "as adjusted for indebtedness", with $449.6M of goodwill written off in 2022 and
  $50.0M more in 2023; financed first by a $1.6B term loan, then by debt and the 2022 stock issue. Centuri: Riggs Distler
  bought in 2021, Centuri sold down in 2024-2025 for about $1.3B of 2025 proceeds and a $343.1M gain on deconsolidation;
  the proceeds repaid $709.0M of debt and paid dividends (10-K). **The one STOP in Part A**, an all-stock deal in
  undervalued stock **[L2009-019]**: no all-stock deal found in the window; both purchases were paid in cash and borrowings.
  Not triggered.
- **Part A WEIGHS AGAINST**: the retention test cannot be passed by a business that retains almost nothing and raises its
  growth capital by selling stock **[L2014-015]**; a $1.6B purchase reversed at a half-billion-dollar loss **[M1995-001]**;
  a dividend set by yield competitiveness **[M2000-051]**.

### Part B: the pay, the board and the owners
- **Pay tied to what the person controls** **[M2003-019]**: the annual incentive pays only if 80% of target "utility
  adjusted net income" is reached, which carries a 40% weight; performance shares pay 60% on cumulative adjusted utility
  EPS and 40% on three-year average utility ROE (DEF 14A). Net income and EPS rise with rate base whether or not the added
  capital earns its cost; the ROE leg is the one charge for capital in the design **[L1994-019]**. The committee keeps "a
  policy on permitted incentive plan adjustments" and in 2025 approved adjustments that included the gain on the sale of
  the company's plane and a deferred-tax true-up (DEF 14A, note to the annual incentive table) **[M1997-041]**.
- **The special award and the departure** **[L1994-020]**: in February 2025 the CEO received a special grant of 25,456
  target performance shares, vesting 2026-12-31, "to encourage retention" (DEF 14A); she resigned a year later, and the
  board agreed she would serve as "an employee and advisor" through 2026-12-31 at "a monthly salary of $95,000", with her
  "existing equity and cash incentive awards" continuing to vest (8-K `0001193125-26-071537`). A retention award that vests
  after the person has resigned is upside without the condition it was granted for. Her 2025 realized pay was $8,578,022
  (DEF 14A). The successor's terms: $900,000 salary, 110% target bonus, a one-time $3.1M performance share award.
- **The board** **[M2007-120]**: an independent chair (a plus by inversion of **[L2014-026]**); a large holder's designees
  on the board since 2022 (owner-orientation in the rows' sense **[M2006-011]**); board chair pay raised to $400,000 for
  2026 by reference to the peer group (DEF 14A) **[L2005-015]**.
- **The owners as partners** **[L1994-023]**: candour on the restatement is adequate (Q4, Q5); earnings guidance is given,
  which Berkshire's own rule rejects **[M2016-002]** (by inversion).
- **Part B WEIGHS AGAINST**: pay on adjusted earnings and EPS that grow with capital put in **[M2003-019]**, **[L1994-019]**,
  and a retention award left to vest after resignation **[L1994-020]**; the independent chair and the owner-designated
  directors are the weights for.

## Q7 — WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is
the risk-free interest rate" **[L2000-021]**. The arithmetic is `calc.py` in the research folder, its output `calc_out.txt`;
every input there carries its accession.

**The cash, as Q4 recasts it** (Southwest Gas Corporation, $M). Operating cash as filed, less the stock-pay add-back, less
the gas-cost (PGA) swing, less the deferred-tax add-back (tax charged at the income-statement provision), plus interest
paid after a 24% tax (the all-equity basis); then less depreciation (the maintenance guess, Q3) or less all capital
spending.

| Year | PGA swing removed | All-equity cash before capex | after D&A (maintenance) | after all capex | Equity-only, after D&A | NI + interest x 0.76 |
|---|---|---|---|---|---|---|
| 2021 | -343.7 | 377.9 | 124.5 | -224.1 | 55.9 | 255.7 |
| 2022 | -159.0 | 477.3 | 214.2 | -205.9 | 132.2 | 236.4 |
| 2023 | -102.8 | 523.8 | 228.3 | -238.3 | 122.1 | 334.6 |
| 2024 | +792.5 | 500.8 | 197.8 | -345.7 | 78.4 | 381.4 |
| 2025 | +65.3 | 502.6 | 171.9 | -305.3 | 37.4 | 434.8 |
| **Average** | | | **187.3** | **-263.8** | **85.2** | **328.6** |

Average capital spending $740.3M, depreciation $289.1M; growth spending (capital spending less the maintenance guess)
$451.2M a year.

**The conventions of this run, confessed** (PRIME RULE 3; each is ours):
- **CONVENTION (the PGA swing):** the purchased-gas balance is a pass-through on which the company neither earns nor loses
  margin (Item 1), so its swing is removed from owner cash; the window total is the change in the filed PGA balance, from
  -$52.6M (2020, FY2021 10-K) to -$304.9M (2025, FY2025 10-K), +$252.3M; by year the filed cash-flow lines are used (2023 as
  first filed, before the reclassification of $294.9M of accrued gas costs) and 2024 is the residual. The FY2025 table
  includes accrued purchased gas costs and the 2020 table does not say whether it does; the seam is recorded. Rationale:
  the swing of the 2021-2023 spike would otherwise set the base. **And** the over-collected balance at 2026-06-30
  ($286.8M payable, 10-Q) is counted with net debt, since it is owed back to customers through lower rates; the figure
  without it is shown beside.
- **CONVENTION (deferred tax):** tax is charged at the income-statement provision, not at the cash paid (nearly nil, Q4);
  the NOL shelter ($146.3M deferred tax asset at 2025) is added at its present value at the Treasury rate, used evenly
  over three years: $131.7M. Rationale: the framework's Whose-tax convention prices a shelter separately; the deferred tax
  of a growing utility is a growth artifact that a no-growth case would not keep.
- **CONVENTION (the tax on interest):** 24% (Q3).

**The six specifics, applied.**
- (a) **Cycle.** The window 2021-2025 holds the gas-price spike and its recovery; with the PGA swing removed, no end year is
  aberrational on the filer's description of it. The literal window (as filed: PGA swing and deferred tax left in, all
  capital spending deducted) is shown beside: average all-equity owner cash after all spending -$131.6M (as-filed
  cash before capex $608.7M less $740.3M).
- (b) **Decline.** No negative growth; not applied.
- (c) **Acquisitions.** The business that remains made none in the window; MountainWest and Centuri are not owned and their
  proceeds are in today's cash and debt (Step 0, lines of evidence). Not applied.
- (d) **Working capital.** Counted, inside operating cash, except the PGA swing (above).
- (e) **Growth spending.** The filing allows the guess (Q3), so the central case is owner cash after maintenance only,
  $187.3M, with the growth spending of $451.2M a year charged against the growth it buys. The growth bought is worth less
  than its cost at both rates: the growth case falls below the no-growth case, so the no-growth case is the top of the
  range and the growth case the bottom, "growth can destroy value" **[L2000-023]**.
- (f) **The cap.** The shown growth of owner cash, 8.39% a year end to end (2.95% between the halves of the window),
  carried ten years gives $419.2M in year ten, 11.7% of sales carried at the business's own sales growth (6.29% a year,
  2021-2025), above the highest share earned in the window (11.1%, 2022). The cut applies: growth is carried at the sales
  growth, not above the discount rate, so at 5.43%. Both are shown.
- Ten years, then no growth (zero nominal), growth spending stopping with it; the long Treasury rate throughout
  **[M1996-025]**.

**The basis** (Q7, On what the floor is earned). Net debt at the latest filed date, 2026-06-30 (10-Q): borrowings $3,509.9M
(long-term $3,409.9M plus current $100.0M) less cash $270.5M = **$3,239.3M**; with the PGA over-collection, **$3,526.2M**.
Subsequent events stated in that filing: the $75.0M debenture was repaid on 2026-08-03 (cash and debt both fall; net debt
unchanged); the commercial-paper program was raised to $100M (no borrowing stated). Operating leases are left out; finance
lease balances are not separately stated in the documents read (principal payments $3.8M to $4.7M a year), left out and
said so. Market value $6,335.4M; all-equity value at the price **$9,729.8M** (with the NOL shelter deducted).

**Value range at 5.43%, all-equity, per share** (central):

| Case | Whole business | Per share |
|---|---|---|
| No growth, maintenance only (top) | $3,450M | **$0.77** |
| Growth at 5.43% (the cut), growth spending charged (bottom) | $812M | **-$35.65** |
| beside: growth at the shown 8.39%, growth spending charged | $1,468M | -$26.60 |
| beside: literal window, all spending, no growth | -$4,859M | -$113.93 |
| beside: generous, net income + after-tax interest ($328.6M), no growth, nothing for growth spending | $6,052M | $36.68 ($40.64 without the PGA in net debt) |
| Equity-only (owner cash after interest, against the market value) | | -$27.04 to $23.48 |

**The floor, tested first** (CONVENTION, Q7). The expected return at $87.45 on every case: the central owner cash is a
1.93% yield on the all-equity value; the generous earnings figure, 3.38%; the internal rate of return of the generous case
grown at 9.99% a year for ten years with its growth spending charged, 4.73%; and of the most generous case the run can
build, the same growth with no growth spending charged at all, 7.18%. No case earns the floor of about ten percent
**[M2003-149]**: "there’s just a point at which we drop out of the game." The file closes OUT whatever the width; the width
test is not reached (the range crosses zero, so its ratio has no meaning).

**The screamer.** Not reached; the price sits far above the top of every range, so nothing about it shouts **[M2009-005]**.

**Fair price (a reporting figure, never a verdict; Part VII).** Each end case valued at ten percent, the two averaged, less
net debt: **-$39.99 a share on the all-equity basis** (central, growth cut to 5.43%; -$39.58 at the shown 8.39%; -$36.03
without the PGA counted as debt); **-$8.60 a share equity-only** (-$10.54 at the shown growth). Not positive on either
basis. Tax: the company's own provision, no conversion; the NOL shelter added. No cheap price is reported.

- **VERDICT: OUT** at Q7: valued, and the price does not clear the floor on any case **[M2003-149]**; the price $87.45 sits
  above the top of the range ($0.77 a share all-equity at the Treasury rate), which closes OUT through the floor
  convention; the range is "the bottom boundary of our estimate" **[L2013-012]** read against a price that no defensible
  case reaches.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (No business named in Q12's list is involved.)

## THE BOX
**OUT at Q7, on the floor.** Southwest Gas Holdings, a regulated gas distributor in Arizona, Nevada and California
since the Centuri separation; Q1 IN; Q2 IN as the regulated exception (a franchise network protecting ordinary,
regulator-set returns, carried to Q3 as a second best; state gas policy recorded as the strongest evidence against);
Q3 against; Q4 no STOP, against (restated 2025 interim quarters, revision to 2017, material weakness); Q5 integrity IN,
ability against; Q6 against. Value range **-$35.65 to $0.77 a share** on the all-equity basis at the 5.43% Treasury rate,
against **$87.45**; no case earns the floor (best case 7.18%). Fair price **-$39.99** all-equity, not positive;
**-$8.60** equity-only.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; the box is unchanged (operator rule 2) **[M1997-127]**.
- **Q9 (debt and exposures).** Borrowings $3,509.9M at 2026-06-30, all at Southwest Gas Corporation; Holdings has none
  drawn (10-Q). Pre-tax earnings over interest at the utility, 2025: ($353.1M + $181.7M) / $181.7M = 2.9 times (the
  coverage measure of **[L2012-002]**). No credit-rating triggers in any debt instrument; a leverage-ratio cap with about
  $4.7B of headroom at the utility and $5.7B at Holdings; a minimum net worth covenant on the 6.1% notes due 2041 (10-K,
  MD&A). Maturities: $75.0M repaid 2026-08-03, $25.0M due June 2027. Undrawn: $400.0M utility facility and $300.0M
  Holdings facility, both to August 2029; commercial paper program $100M. Spending of $6.3B planned for 2026 to 2030 before
  the Great Basin estimate rose by about $0.6B, with operating cash expected to fund about 60% of spending and dividends
  (Q3): the rest is new debt and stock. One utility in three states carries the single-catastrophe exposure the rows name
  **[L2005-019]**. Pension: assumed return 7.00%, discount rate 5.75%.
- **Q10, Q12.** Nothing found that bears on them.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). Q6 and
      Q7 were committed together, as the brief asks, because Q6's buyback line needs Q7's bottom. **Slip declared:** a
      directory listing of `Test Runs/` for today's date was run before the copy, to see whether the file existed; it
      exposed six other run names (declared under contamination at the top).
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session; the run is folded into the register before the dispatcher moves on (operator rule ten). For the
      dispatcher to tick. *Ticked by the dispatching session (overnight cycle of 2026-10-18): the brief granted the
      pathspec commits, the cycle's lock was held throughout, and the run is folded in the same cycle before any other name.*
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched, except the date-filtered listing
      above; the commit subjects of the OGS fold were seen in the session context. Declared, not used. Where this run's
      Q2 reading (the regulated exception) and Q3/Q6 weights resemble those subjects, they were reached from the SWX filings
      and the framework's own text (Q2, What it rules OUT, the regulated exception); the analyst cannot prove the absence
      of an anchoring effect and says so.
- [x] Every v5 id resolves and every quoted fragment beside an id is the row's own (`idcheck.py` in the research folder,
      output in `idcheck_out.txt`); every filing fact has its accession; no number without a row, a filing or a
      CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): the central figure is built from the
      filed cash-flow statement. **Declared:** a "generous" variant on net income plus after-tax interest is shown beside
      the range at Q7, labelled, only to show that the floor fails even on the most favourable reading; it sets no end of
      the range and no reporting figure.
- [x] The sovereign from the issuing authority (US Treasury par curve, 2026-10-16); the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations, items a to g); facts for Q9 written under AFTER THE STOP.
      No integrity facts are left unjudged (Q5 was reached and answered).
- [x] No row dated after the anchor is cited in a point-in-time run (not a point-in-time run).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its owner-earnings means and its debt table were
      set aside, and why is stated at Step 0.
- [x] **Slip declared (operator rule 3):** `calc.py` and its output `calc_out.txt`, which hold the Q7 valuation arithmetic,
      were written and committed in the research folder (commit `6a8c78cc`, with Q1) before Q2 to Q4 had closed, without
      the heading COMPUTATION, NOT A CLEARANCE. They carry no entry language; the run file reported no Q7 figure before
      Q4 closed except the bottom of the range written back into Q6 in the same commit as Q7. The heading is added to the
      script's output from the final commit on; the earlier commit stands as the record.
- [x] `python tools/check_framework.py` PASS before the final commit (result at the foot of this file).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Pass-through balances.** Specific (d) counts working capital and (a) treats an aberrational year, but a regulated
utility's purchased-gas balance swung by about $800M across three years of a commodity spike and its recovery, on which
the company earns no margin and pays or receives carrying charges; the text has no rule for a pass-through balance, nor
for whether an over-collection owed back to customers is net debt (Q7's net-debt definition names only borrowings and
finance leases). The run confessed two conventions (remove the swing; count the over-collection as debt) and showed the
figures without them. (2) **Specific (e)'s mechanics.** "The growth spending charged against the growth it buys" does not
say whether the spending grows with the business or stays flat, nor whether it stops at year ten; the run grew it with the
business and stopped it at year ten, by analogy with the acquisition clause in (c). (3) **The cap's "sales" for a utility.**
GAAP revenue includes gas cost passed through at cost and swung from $1.5B to $2.5B and back within the window; operating
margin (non-GAAP) is the honest base. Either growth rate (6.29% and 7.28%) is above the 5.43% discount rate, so the cut
lands at 5.43% on either base here; another utility could differ. (4) **Whose tax and deferred tax.** The convention prices "carryforwards or credits that run
out inside ten years"; a growing utility's deferred tax comes mostly from accelerated and repairs deductions, which are
neither, and its NOL is federal and indefinite; the run charged the book provision and priced the NOL as a shelter, a
convention of its own. (5) **The retention test for a business that retains nothing.** Part A's test asks whether a dollar
kept became a dollar of value; SWX keeps almost nothing and raises its growth money by selling stock. The framework's
nearest rule, serial issuance, is still a candidate STOP left unresolved in section VI; a run on a utility cannot apply it
either way. (6) **The regulated exception.** Q2 passes any castle whose ordinary returns are regulator-set to Q3, and Q3 is
a weighing, so for every regulated utility the only gate between Q1 and Q7 is integrity; the decision then falls entirely
on the floor at Q7. That may be right, "there’s no way we get rich on our utility investments" **[M2009-104]**, but the
text does not say that it intends the floor to be the utility's only gate.


---
**Checks before the final commit (2026-10-18):** `python tools/check_framework.py` PASS (TEST RUNS: phantom ids in 0 files;
POINTERS: 0 missing). `idcheck.py`: 93 distinct ids, 128 citations, 20 quoted fragments checked against their rows, 0
problems; no E-ids.
