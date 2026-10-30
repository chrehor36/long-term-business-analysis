# Company Run: PPL Corporation (NYSE: PPL), 2026-10-26
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied to this dated name before any fetch (commit
14564e1d). Dispatched blind run; working folder `Test Runs/_research 2026-10-26 PPL/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-26: the operator does not hold this name (`PORTFOLIO.md` has no PPL row).*

**Contamination, declared and not used.** (1) The session opened with a git status and five recent commit subjects
(an NRG v5 re-run fold and two automation commits); none names PPL. The status listing showed one other company's
research folder name (`_research 2026-09-27 ARCB`), not opened. (2) The memory index loaded into the session carries
counts of gate-clearers and a queue position; none names PPL. Nothing of either was used. No other run file, holding
review, register, reading list or `PORTFOLIO.md` was opened, listed or searched.

**Lines of evidence chosen from the 10-K for 2025 (Item 1, Item 1A, Item 7), as the brief asks.** (a) The allowed and
earned returns in the three jurisdictions and the outcome of the 2025 to 2026 rate cases (Item 7, Rate Case
Proceedings; Note 7; the 8-Ks of 2026-08-17 and 2026-08-27). (b) The capital programme and the data-centre load it is
built for (Item 1A, first risk under B; Item 7, Forecasted Uses of Cash), with the Blackstone joint venture outside the
regulated plan. (c) The Kentucky coal fleet under environmental rules and its replacement (Item 1, Power Supply; Item
1A, C). (d) The holding company's financing: debt, the at-the-market programme, the equity units, the exchangeable
notes (Item 1A, A; Note 7 of the 10-Q). (e) The 2021 sale of the U.K. business and the 2022 purchase of Rhode Island,
which sit inside the five-year window (Note 9 of the 10-K for 2023). (f) The non-GAAP "Earnings from Ongoing
Operations" featured in Item 7 and used for pay (Item 7, Reconciliation; proxy, CD&A).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $35.13 (2026-10-26, live quote as printed by `tools/run.py`; aggregator, flagged per operator rule 5).
- **Shares:** 752,544,841 common shares outstanding at 2026-07-31, cover of the 10-Q for the quarter to 2026-06-30
  (accession 0000922224-26-000044, filed 2026-08-07). `python Screens/cover_shares.py PPL` printed this count beside
  three subsidiary counts (PPL Electric 66,368,056; LG&E 21,294,223; KU 37,817,878); the cover says each of those is
  "all held by" a wholly-owned subsidiary of PPL, so they are not classes of PPL stock and are not added. Check: the
  10-Q balance sheet note gives 771,335 thousand issued and 752,369 thousand outstanding at 2026-06-30 (issued less
  treasury, about 18,966 thousand), consistent with the cover. No later 8-K reports an issuance that changes the
  count. **Not in the count, stated:** forward sale contracts under the at-the-market programme for about 27.4 million
  shares at a blended initial forward price of about $35.90, unsettled at 2026-06-30 (10-Q, Note 7); 23 million equity
  units of $50 whose purchase contracts oblige holders to buy common stock by 2029-02-15 (10-Q, Note 7); and the
  exchangeable senior notes due 2028 and 2030 (10-Q, Note 4).
- **Market cap:** 752.5M x $35.13 = **$26,437M**.
- **Sovereign for the earnings currency (USD):** **5.33%**, US Treasury daily par yield curve, 30-year, 2026-10-23
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for 2025, filed 2026-02-20, accession 0000922224-26-000008 (Items 1, 1A,
  7, 8 and notes 7, 12); 10-K for 2023, accession 0000922224-24-000008 (cash flows 2021 to 2023, Note 9 on the Rhode
  Island purchase, the Talen and billing matters); 10-K for 2021, accession 0000922224-22-000005 (2021 segment
  figures); 10-Q for the quarter to 2026-06-30, accession 0000922224-26-000044; proxy (DEF 14A) filed 2026-04-01,
  accession 0001193125-26-135991; 8-Ks of 2026-08-07 (0000922224-26-000042, the second-quarter release, Exhibit 99.1),
  2026-08-17 (0000922224-26-000046, the Kentucky rehearing order) and 2026-08-27 (0000922224-26-000048, the Rhode
  Island rate decision).
- **Figures cross-checked against the filed statement:** net cash provided by operating activities for 2025, $2,629M,
  printed by `tools/run.py` from XBRL, equals the filed Consolidated Statement of Cash Flows (0000922224-26-000008);
  long-term debt at 2025-12-31, $17,990M, equals the filed balance sheet.
- **`tools/run.py PPL`, arithmetic lines only** (output kept at `_research 2026-10-26 PPL/run_py_output.txt`; its
  2021 operating cash, $2,270M, includes the discontinued U.K. business and is replaced below by the filed
  continuing-operations figure, $1,544M):

| FY | Op. cash (continuing) | Stock pay | Depreciation | Capital spending | OCF - SBC - depreciation | OCF - SBC - capex |
|---|---|---|---|---|---|---|
| 2021 | 1,544 | 37 | 1,082 | 1,973 | 425 | -466 |
| 2022 | 1,730 | 37 | 1,181 | 2,155 | 512 | -462 |
| 2023 | 1,758 | 33 | 1,254 | 2,390 | 471 | -665 |
| 2024 | 2,340 | 46 | 1,279 | 2,805 | 1,015 | -511 |
| 2025 | 2,629 | 49 | 1,312 | 4,030 | 1,268 | -1,450 |
| mean | | | | | **738** | **-711** |

  USD millions; sources: 10-K 2025 and 10-K 2023 cash-flow statements. Stock pay is resolved (one line, "Stock
  compensation expense"); no finance-lease principal of size (one line of $1M in 2024). Operating cash is after
  interest and income taxes actually paid, so this is the equity-only owner cash. Acquisition cash outside capital
  spending: Rhode Island (Narragansett Electric) $3,660M net of cash acquired in 2022; sale proceeds: the U.K.
  business $10,560M in 2021 (discontinued) and Safari Holdings $146M in 2022.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: a regulated utility is bought for the cash its rate base yields, and the
question is whether that cash, not the next buyer, justifies $35. The market serves and does not instruct
**[M2006-077]**; the price is read only against Q7. No macro view enters **[M2000-094]**: the data-centre boom that the
company's plan rests on is a forecast of demand, recorded as a fact about the plan, not used as a reason. Who is paid to
tell you **[M2011-083]**: the company's own 6% to 8% EPS growth target and its "ongoing" figure are the seller's
projection of what it sells, and are not consulted as inputs **[M1995-050]**. **Contrary evidence, written down as
found** **[M1997-127]**: (1) the earned return on book equity was 5.1% over 2021 to 2025, the lowest of the four
utilities compared at Q2; (2) owner cash after all capital spending was negative in every year of the window; (3) the
three 2026 rate orders granted less than asked in each state and the FERC cut the New England transmission return
retroactively; (4) the company excluded about $1.3B of after-tax costs from its featured earnings over 2022 to 2025 and
pays its officers on the adjusted figure; (5) it is issuing equity by three routes at once.

## THE STANDING RULE
Nothing in the purchase as a part-interest bought for cash, unlevered and sized within the buyer's means, risks what
the buyer has and needs **[M2012-081]**; the rule binds the buyer's financing, and no margin, collateral or option
position is contemplated **[L2014-024]**. The target's own debt is weighed at Q9.

---
## Q1: CAN I UNDERSTAND IT? STOP.
- **The test.** Understanding is "a reasonable probability of being able to asses where the business will be in 10
  years" **[M2000-037]**, the key variables identified and their predictability judged **[M1998-044]**.
- **What the business is** (10-K 2025, Item 1, 0000922224-26-000008): a holding company for four regulated utilities.
  Kentucky Regulated (LG&E and KU: generation, transmission, distribution; 1.4M customers; 2025 revenue $3.8B, net
  income $674M; capitalization $13.6B), Pennsylvania Regulated (PPL Electric: transmission and distribution only, no
  generation; 1.5M customers; $3.1B, $639M; rate base $11.1B), Rhode Island Regulated (RIE: electric and gas
  delivery; 0.8M customers; $2.2B, $85M; rate base $4.3B). Corporate and Other lost $217M in 2025 (holding-company
  interest and unallocated costs).
- **The key variables.** (1) Rate base, set by the capital the regulators approve; (2) the allowed return and how much
  of it is earned; (3) the regulatory climate in Kentucky, Pennsylvania, Rhode Island and at the FERC; (4) in Kentucky,
  the cost and permission to keep or replace a coal fleet (generation 2025: LG&E 10,331 GWh coal of 12,172; KU 14,738
  of 19,754); (5) the cost of the debt and equity the programme needs.
- **Are they foreseeable?** The mechanics are written down by the regulators each year: base rates as a return on rate
  base (Item 1, Rates), formula transmission rates under FERC, riders that earn a return (DSIC, smart meter, the
  Kentucky PGR). The insiders do write the forecast down: a three-year capital plan of $17.35B for 2026 to 2028 (Item 7,
  Forecasted Uses of Cash) and fully projected test years in Pennsylvania and Kentucky. That passes test 5
  **[M2000-105]**. The financial statements tell me what the next ones will look like in outline, since revenue
  follows rate base and allowed return **[M2008-033]**.
- **What weighs against.** Item 1A names the plan's dependence on data centres, "the increased concentration of
  business within a single industry based on emerging technologies" (Item 1A, B); the regulated return shields the
  return on what is built but not the volume of what is built. The rows say an allowed return in the electric utility
  is one "you’re almost certain of earning" only "if you behave yourself" **[M2010-037]**, and that the compact can
  break **[L2023-011]**. Those bear on the castle (Q2) and the value (Q7), not on whether the economics can be pictured.
- **VERDICT: IN.** The ten-year economics are a regulated return on a rate base whose size and pricing are set in
  public proceedings and filed; a reasonable fix on earning power and position can be had **[M2012-065]**; no doubt
  that it sits inside the circle **[M2002-092]**.

## Q2: WHY IS THE CASTLE STILL STANDING? STOP.
- **The parts table** (segment net income, the filer's segment measure, USD M; 2021 from 10-K 2021, 0000922224-22-000005,
  on the presentation then used; 2022 to 2025 from 10-Ks 2023 and 2025):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year | share of the three | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| Kentucky Regulated | 468 | 549 | 552 | 620 | 674 | 2,863 | 49.3% | regulated franchise, vertically integrated | **yes (largest)** |
| Pennsylvania Regulated | 445 | 525 | 519 | 574 | 639 | 2,702 | 46.5% | regulated delivery franchise | no |
| Rhode Island Regulated | n/a | -44 | 96 | 109 | 85 | 246 | 4.2% | regulated delivery franchise | no |

  No part carries more than half, so the largest, Kentucky, decides (Q2, A business of parts). Kentucky's 2021 figure is
  on the pre-2023 presentation, which charged LKE financing to the segment; on the later presentation it would be
  higher and Kentucky's share larger. Pennsylvania is close behind and has the same kind of castle; the reading below
  holds for both.
- **The castle tests.**
  - *Why is it still standing* **[M1995-038]**: a legal franchise. "There are currently no other electric public
    utilities operating within the electric service areas of LG&E and KU"; PPL Electric "operates a regulated
    distribution monopoly in its service area"; "There are currently no other electric or gas public utilities
    operating within the service area of RIE" (10-K 2025, Item 1, Competition).
  - *The attacker with money* **[M2011-015]**: an attacker cannot build a second grid in a franchised territory; the
    attack the filing names is narrower: FERC Order 1000 lets non-incumbents bid for some PJM transmission ("Increased
    competition can result in lower rate base growth", Item 1A, D), bills for customer choice or distributed generation
    in the Kentucky General Assembly (none adopted), and large gas customers who can bypass LG&E (Item 1).
  - *Pricing power and the agony before a rise* **[M2005-020]**: the business has none of its own; every rise is a
    rate case before a commission. The 2026 outcomes: Kentucky asked $391M at a 10.95% ROE and got $233M at 9.775%
    (orders of 2026-02-16, about $7M more on rehearing, 8-K 0000922224-26-000046); Pennsylvania asked $356M at 11.3%
    and settled at $275M with no stated ROE (10-Q, Note 6); Rhode Island asked $181M at 10.75% and got $137.8M at
    9.275%, its second rate year refused (8-K 0000922224-26-000048). The FERC cut the New England transmission base
    ROE to 9.57% retroactive to 2014 (10-Q, Note 6). This is the agony, institutionalised.
  - *The low-cost position and the low bid* **[L2004-003]**: the delivery customer cannot take the low bid; in
    Pennsylvania 40% of residential and 98% of large commercial load buys its energy from competitive suppliers, but the
    supply cost is a pass-through and "its financial results are not impacted" (Item 1, PLR).
  - *Widening or narrowing* **[M1999-108]**: allowed returns held near 9.3% to 9.8% in the 2026 orders; Kentucky moved
    from a return on capitalization to a return on rate base from 2026-01-01; Kentucky added a pilot generation recovery
    clause and a high-load tariff with minimum payments and collateral. Against it: affordability is now in the orders
    (Rhode Island winter bill credits and paused charges, the hold-harmless credits of about $170M, the Pennsylvania
    low-income terms). On the filings the franchise is neither widening nor visibly filling in.
  - *What could destroy it* **[M2000-014]**: a regulatory climate turning against the owner, the case the 2023 letter
    narrates of other states **[L2023-011]**; the Kentucky coal fleet's environmental rules (Item 1A, C); and, for the
    capital plan only, data-centre demand that does not arrive.
- **The competitor row.** The 10-K names no rival company: each segment's Competition paragraph says there is no other
  utility in its service area. **CONVENTION of this run:** the rivals compared are FirstEnergy (CIK 1031296; Pennsylvania
  utilities under the same commission), American Electric Power (CIK 4904; Kentucky Power under the same Kentucky
  commission, a coal-heavy integrated fleet) and Eversource (CIK 72741; New England electric and gas delivery beside
  Rhode Island). Rationale: the filing names none, and these three sell the same regulated service under the same
  regulators. Same metric, from each company's own 10-K XBRL (accessions 0001031296-26-000046, 0000004904-26-000013,
  0001628280-26-008461, 0000922224-26-000008), 2021 to 2025, whole span:

| Company | Net income to common / average equity, by year | five-year | capex / depreciation | OCF less capex, five years ($M) |
|---|---|---|---|---|
| PPL (2021 continuing ops) | 0.1, 5.5, 5.3, 6.3, 8.1% | **5.1%** | 2.19 | -3,352 |
| FirstEnergy | 16.1, 4.3, 10.7, 8.5, 8.2% | 9.3% | 2.36 | -3,954 |
| AEP | 11.6, 10.0, 9.0, 11.4, 12.3% | 10.9% | 2.36 | -7,906 |
| Eversource | 8.5, 9.3, -3.0, 5.6, 10.8% | 6.3% | 2.97 | -7,310 |

  (Working in `_research 2026-10-26 PPL/scripts/peer_calc.py` and `peers_table.txt`. AEP capital spending is its
  "construction expenditures" line; Eversource's depreciation line is used, not its D&A line, which carries
  regulatory amortization. PPL's book equity carries $2,247M of goodwill, $1,585M of it from Rhode Island.)
- **The field's returns over the whole span, judged in words.** The four earn returns on book equity that are fair at
  best and ordinary in the plain sense, and every one spends more than it generates, year after year. PPL earned the
  least of the four over the span; in 2025 it reached 8.1%, still below the 9.3% to 9.8% its regulators allow, the gap
  being regulatory lag, the holding company's debt and the Rhode Island goodwill on which no regulator allows a return
  (RIE "will exclude all goodwill from the ratemaking capital structure", 10-K 2023, Note 9). Under Q2's list a durable
  castle that protects only ordinary returns closes OUT, but the framework's same item excepts a return set by a
  regulator and carries it to Q3 as a second best (the framework's wording, paraphrased; its rows are the utility
  rows, the "decent returns on the incremental sums they invest" of **[L2009-012]** and the "guaranteed return" of
  **[M2009-104]**). This is that exception.
- **VERDICT: IN.** The castle stands because the law grants it and the regulators keep it **[M1995-038]**; nothing in
  the filings shows it being filled in; the return it protects is a regulated, fair-not-rich one, "there’s no way we
  get rich on our utility investments" **[M2009-104]**, and is carried to Q3 and Q7. The compact's fragility
  **[L2023-011]** and the gap between allowed and earned returns are carried forward, not decided here.

## Q3: HOW MUCH CAPITAL MUST GO IN, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**: net income to common on average book equity 5.1% over
  2021 to 2025, 8.1% in 2025 (Q2 table); on equity less the $2,247M of goodwill, 2025 is about 9.6% (1,179 on an
  average of about 12.2B). The regulators allow 9.275% (Rhode Island, 52% equity, 8-K 0000922224-26-000048) to
  9.775% (Kentucky base rates) on the equity they recognise. The business, read on the capital it needs, earns about
  what it is allowed; the owner of PPL earns less, because the holding company carries debt and goodwill the
  regulators do not reward.
- **To stand still and to grow** **[L2000-035]**: capital spending ran 1.8 to 3.1 times depreciation (1,973 against
  1,082 in 2021; 4,030 against 1,312 in 2025), and the filed plan is $17.35B for 2026 to 2028, $5.1B to $6.2B a year
  (10-K 2025, Item 7, Forecasted Uses of Cash), more than four times the 2025 depreciation charge. The filing gives no
  maintenance figure; depreciation is the guess, "not inappropriate in most companies to use as a proxy for required
  capital expenditures" **[M1998-127]**, and the owner is entitled to that guess **[M2000-144]**.
- **What the added capital earns.** Maintenance-only owner cash rose from 425 (2021) to 1,268 (2025), while capital
  spending above depreciation summed 7,245 over the five years and long-term debt rose about 6.2B net of the Rhode
  Island debt assumed (Q7). The incremental return is the allowed return on the added rate base, with lag; the rows'
  measure is "the operating earnings after depreciation" **[M2014-086]**, and the regulated return is fair, not rich:
  "deploy large sums at fair returns" **[L2005-005]**. "To earn more, their owners must invest more." **[L2011-019]**.
  This is the second account of **[L2007-010]**, never the first, and the rows accept it as a second best
  **[M2018-055]**.
- **WEIGHS AGAINST, mildly.** A second-best business by the rows' own grading **[M1998-081]**, whose growth is bought
  with compulsory capital at a regulated return; on the owner's equity the earned return has run below the allowed
  return for the whole window. The "little or no debt" test is applied at Q9.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten year-ends** **[M2025-032]** (`tools/run.py` table, first-filed XBRL, accessions
  0000922224-17-000010 to 0000922224-26-000008; read against the filed balance sheets of 2025, 2023 and 2021):
  - 2016 to 2020, with the U.K. business: assets 38.3B to 48.1B; equity 9.9B to 13.4B, helped by share issuance
    (proceeds of common stock 453M in 2017, 698M in 2018, 1,167M in 2019); long-term debt 17.8B to 21.6B; goodwill
    about 3.1B to 3.3B.
  - 2021, the sale: assets fall to 33.2B, cash rises to 3,571M, goodwill falls to 716M (Kentucky only), long-term debt
    halves to 10.7B (4,606M retired, with a 395M loss on extinguishment), retained earnings fall from 5,315M to 2,572M
    (net loss 1,480M, the discontinued U.K. business; dividends 1,279M; 34.8M shares bought back for 1,003M).
  - 2022, the purchase: Rhode Island for 3.8B cash plus 1.5B of debt assumed; goodwill to 2,248M; cash back to 356M.
  - 2023 to mid-2026: long-term debt (with current maturities) 15.6B, 16.5B, 18.9B, then 20.3B at 2026-06-30 (10-Q);
    equity 13.9B, 14.1B, 14.9B, 15.0B, raised as much by stock reissued (401M in 2025) as by retained earnings
    (2,710M to 3,207M); construction work in progress 2,390M to 3,437M in 2025.
  - Receivables (customer) against revenue: 583M on 5,783M in 2021 (10.1%), 1,108M on 9,042M in 2025 (12.3%);
    fuel, materials and supplies 322M to 551M (5.6% to 6.1% of revenue). Moved, not out of line.
  - What the figures cannot say: whether the regulatory assets (2,092M noncurrent at 2025) and the plant will earn the
    allowed return. What they say plainly: debt has risen faster than equity every year since 2021.
- **The real costs.** Depreciation is charged and is real **[R1996-023]**; no EBITDA appears in the 10-K, the release
  or the proxy (search: no instance of "EBITDA" in the three documents). Stock pay is expensed (49M in 2025) and is
  deducted from owner cash. Amortization (104M in 2025) is left in the costs; it is largely regulatory-asset and
  debt-cost amortization, not purchased intangibles.
- **The featured adjusted figure, recorded and carried to Q5.** Every Item 7 segment discussion and every earnings
  release leads with "Earnings from Ongoing Operations", which management also uses "in measuring achievement of
  certain corporate performance goals, including targets for certain executive incentive compensation" (10-K 2025,
  Item 7). The special items excluded (after tax): about 285M in 2022, 443M in 2023, 362M in 2024, 163M in 2025
  (10-Ks 2023 and 2025, Reconciliation of Earnings from Ongoing Operations); ongoing 4,818M against GAAP 3,565M over
  2022 to 2025. The items recur: acquisition integration in each of 2022 to 2025, IT transformation in 2024 and 2025,
  the PPL Electric billing issue in 2023 and 2024, strategic and centralisation initiatives, office relocation. The
  rows: "a management that regularly attempts to wave away very real costs by highlighting "adjusted per-share
  earnings" makes us nervous" **[L2016-006]**; telling owners year after year not to count necessary business
  adjustments "is misleading" **[L2016-007]**. Guidance is given and reaffirmed (2026 ongoing EPS $1.90 to $1.98; 6%
  to 8% EPS growth "through at least 2029", Exhibit 99.1 of 0000922224-26-000042), the habit the rows call "the
  scourge of earnings "guidance"" **[L2019-006]**.
- **Confusion or suspicion?** None found in the accounts themselves. Every special item is listed by line, by segment,
  with its tax, and reconciled to GAAP net income; the press release states GAAP earnings first in its body; no
  prepaid or deferred account builds out of line, no reserve moves suspiciously, receivables and inventories track
  revenue **[M1995-064]**. The habit is "a negative" but not "a total exclusionary factor" **[M1994-018]**.
- **VERDICT on the accounts: WEIGHS AGAINST.** Not a STOP: the statements can be read and recast. The recast earnings
  for Q7 are owner cash after depreciation, stock pay, interest and tax, on GAAP cash flows, with no special item added
  back. The adjusted figure, its use for pay and the guidance go to Q5 **[M2004-067]**.

## Q5: WHO RUNS IT? STOP on integrity; WEIGHING on ability.
- **The two yardsticks** **[M1994-008]**: how they run the business against the hand dealt, and how they treat the
  owners. The chief executive since 2020 (Vincent Sorgi, proxy 0001193125-26-135991) inherited a U.K.-and-U.S. group,
  sold the U.K. business for $10.56B in 2021, bought Rhode Island for $5.3B in 2022, and runs a capital plan that has
  more than doubled annual spending since 2021. Earned return on equity stayed the lowest of the four compared (Q2).
- **The habits carried from Q4, read with the integrity record.** (1) The ongoing figure, excluding recurring costs
  (about 1.25B after tax over 2022 to 2025), featured and used for pay **[L2016-006]**, **[L2016-007]**. (2) Guidance
  and a multi-year EPS growth target reaffirmed each quarter **[L2019-006]**, **[L2000-039]**. (3) Targets met: the
  2025 cash-incentive EPS target was $1.79 and the "actual corporate EPS" was $1.81, paying 125% (proxy, Corporate
  Financial Goal Performance), against GAAP diluted EPS of $1.59. Consistency in beating declared targets over many
  years was not shown by the documents read: no instance found, in the filings read, of a record of hitting every
  declared target, which is what makes the rows "downright incredulous" **[L2002-041]**.
- **The rest of the integrity record, from the filings.** (a) Talen: the spun-off generator (PPL Energy Supply,
  renamed Talen) and its affiliates sued PPL over the 2015 spin-off; PPL settled in December 2023 for $115M and the
  claims were dismissed, "This matter is now concluded" (10-K 2023, Talen Litigation; 0000922224-24-000008). (b) The
  PPL Electric billing event of December 2022 to January 2023: estimated bills from a technical fault, a PAPUC
  investigation, a settlement with a $1M civil penalty, remedial work, and an agreement not to recover the
  extraordinary costs (10-K 2023, Note 7). The company acted when it learned of the problem, the test of
  **[M2017-005]**; the costs were then excluded from the featured figure. (c) The Rhode Island acquisition commitments
  were kept as filed: rate stay-out, forgone transition cost recovery, goodwill excluded from rates, the hold-harmless
  credits finally set at about $170M (8-K 0000922224-26-000048). (d) The board has an independent chair; officers and
  directors are barred from hedging and pledging (proxy).
- **Judgment on integrity.** The rows separate the promoter's habits, which make them "nervous" **[L2016-006]** and
  are "a negative" **[M1994-018]**, from the doubt that closes the file, "If you’ve got doubts, forget it."
  **[M2013-088]**. I read the record as habits shared with the industry and fully disclosed, not as dishonesty: the
  reports tell an owner what a full owner would want to know about each item **[M1998-036]**, the GAAP figure is given
  first and reconciled, the two legal matters ended in settlement with disclosure, and nothing found shows the numbers
  being made up to meet a target. Professed integrity proves nothing **[M2010-069]**, and industry custom is no excuse
  **[M2009-013]**; those weigh against, and the pay on the adjusted figure is weighed at Q6, Part B. A second analyst
  could read the same record as doubt; the rows do not draw the line between the two (see the last section).
- **VERDICT on integrity: IN, narrowly. Ability WEIGHS AGAINST, mildly:** the hand was played into a lower return on
  the owners' equity than the peers earned, and a $5.3B purchase whose segment earned $85M to $109M of GAAP net income
  in its three full years (see Q6).

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[R1995-009]**: little is retained. Dividends against GAAP net income: 787M on 756M
  (2022), 704M on 740M (2023), 747M on 888M (2024), 794M on 1,181M (2025). Retained earnings rose 0.5B over four years
  while the equity the capital plan needs comes from issuance: treasury stock reissued for 401M in 2025, an
  at-the-market programme of up to $2B (forward contracts for about 27.4M shares at about $35.90 outstanding at
  2026-06-30), $1.15B of equity units committing holders to buy common stock by 2029, $1.15B of 3.000% exchangeable
  notes due 2030 issued 2025-11-24, and the 2023 exchangeable notes due 2028 (10-Q, Notes 4 and 7). Paying out the
  earnings and selling new shares to fund the plan is the policy.
- **Buybacks.** 34.8M shares for $1.0B in 2021, about $28.7 a share, under a $3B authority that named no price (10-K
  2021, Share Repurchases) **[L2016-002]**. The test against the bottom of the Q7 range is written back below.
  *Written back from Q7 and committed with it:* the bottom of the central Q7 range is $18.20 a share (equity-only, the
  regulated-utility basis). The 2021 purchases at about $28.7 sit well above it, so the programme with no stated price
  weighs against **[L1999-023]**, **[L2011-003]**. The issuance of 2025 and 2026 at about $35 to $36 sits at about twice
  the top of the range ($18.40): on this computation the new shares are sold above value, which does not harm the
  continuing owners **[M1996-013]**, and the serial-issuance weight above stands.
- **Issuance and deals.** The issues are at about $35 to $36; whether that gives less in value than it gets is decided
  by Q7 **[M1995-001]**: issuing below value harms continuing owners **[M1996-013]**, issuing above it does not. The
  volume and variety of issuance is the behaviour the rows name, "hell-bent on issuing shares" **[L2014-015]**, a
  candidate second STOP the framework leaves unresolved (section VI); weighed here, heavily, against. No all-stock deal
  in the window (the Rhode Island price was cash and assumed debt), so the one STOP of Part A does not arise
  **[L2009-019]**. The Rhode Island deal: $5.3B of enterprise value given, $3.8B of it cash from the U.K. sale, for a
  segment that earned net income of 96M, 109M and 85M in 2023 to 2025 and is allowed 9.275% on 52% equity from 2026;
  the cash price alone yields about 2.5% on that income, and $1,585M of the price is goodwill no regulator will reward.
  Value given exceeded value got on the evidence so far **[M1995-001]**, **[L1997-031]**.
- **Part B, pay, the board, the owners.** Annual cash incentive 65% on "Corporate EPS" from ongoing operations, a
  figure management defines (proxy); long-term units 50% on three-year TSR against a utility index and a peer group,
  25% on growth of ongoing EPS, 25% on sustainability goals; the 2023 to 2025 units paid 161%, 152% and 146% of
  target. Chief executive's 2025 total: $13,221,331 (Summary Compensation Table); pay ratio 74:1. Pay is not tied to
  what the person controls when half the long-term award rides on relative share price **[M2003-019]**, and the
  annual award is measured on a figure that leaves out costs the owners bore **[L2016-007]**. Directors must hold five
  times the retainer, met largely by deferred stock units granted, not shares bought with savings **[L2019-008]**.
  Independent chair; executive officers and directors together hold under 1% of the stock (proxy).
- **WEIGHS AGAINST.** Part A: the earnings are paid out while new shares, units and exchangeable notes are sold to
  fund a programme of compulsory capital, and the one large deal of the window gave more than it got. Part B: pay on an
  adjusted figure and on relative share price.

## Q7: WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life"
**[R1996-018]**, credited only with "whatever net cash is left every year" **[M1998-080]**, at the long government
rate **[L2000-021]**, as a range **[L2000-024]**. Arithmetic in `_research 2026-10-26 PPL/scripts/q7.py`, output in
`q7_output.txt`; USD millions unless a per-share figure.

- **The basis.** Q2 found the deciding part (Kentucky) earning a return a regulator allows, so Q7, The regulated
  utility, governs: the central figure is equity-only, owner cash after interest and after the company's own tax
  against the market value of the shares, with the long-term debt raised for the fixed assets credited against the
  growth spending, and the all-equity figure beside **[L2017-012]**, **[M2010-037]**.
- **The cash input.** Owner cash after every real cost, equity-only, maintenance-only (specific (e)): operating cash
  of continuing operations (after interest and income tax paid) less stock pay less depreciation as the maintenance
  guess **[M1998-127]**, **[M2000-144]**: 425, 512, 471, 1,015, 1,268 for 2021 to 2025; **five-year mean 738**. The
  all-spending series (capital spending in full) is negative every year, mean **-711**, shown beside. No special item
  is added back.
- **The window, (a).** No cycle in a regulated delivery business; 2021 is aberrational on the filer's own description
  (the U.K. sale, a $395M loss on extinguishment, Rhode Island not yet owned) and 2022 holds Rhode Island for seven
  months. The literal window is used, with the growth measured as below; no cycle base exists to substitute.
- **Acquisitions, (c).** Net purchases over the window: Rhode Island $3,660M less Safari $146M = $3,514M, more than
  half of owner cash before purchases ($3,691M over five years), so the serial-acquirer rule makes the **organic pair
  central** (purchases left out, organic growth), with the default pair (purchases deducted, total growth credited)
  beside. **CONVENTION of this run:** the U.K. sale proceeds ($10,560M, 2021) are left out of net purchases, because
  the U.K. business's cash flows are discontinued operations and are outside every year of the window; counting the
  proceeds while excluding the earnings would credit the window with a business it does not contain. The filer reports
  no organic growth; **CONVENTION of this run:** organic growth is the company's sales growth between 2023 and 2025,
  the only years with Rhode Island owned in full at both ends, 4.30% a year (8,312 to 9,042). Total growth for the
  default pair is sales growth 2021 to 2025, 11.82% a year (5,783 to 9,042).
- **The cap, (f).** The shown growth of owner cash, 425 to 1,268, is 31.4% a year; carried ten years from the mean it
  would reach about 11,350 a year, above 2025 sales of 9,042 and far above the highest share of sales owner cash has
  reached (14.0%, 2025). It traces to an absurdity **[M1999-067]** and is cut to sales growth as above; both are
  written down. A base year in which the cash was poor produces a "breathtaking, but meaningless, growth rate"
  **[L2005-003]**.
- **Growth spending, (e), and the utility debt credit.** Capital spending above depreciation: 891, 974, 1,136, 1,526,
  2,718; mean 1,449. Long-term debt (noncurrent plus current maturities; finance leases immaterial; short-term debt
  and cash left out; no securitization bonds found) rose from 11,140 at 2021-12-31 to 18,894 at 2025-12-31; less the
  1,510 of Rhode Island debt assumed in the purchase (not raised for fixed assets), the increase is 6,244 over four
  years, **1,561 a year** (CONVENTION of this run: measured from the window's first year-end, since the 2020 balance
  sheet still carried the U.K. debt). The cap: the filings state an allowed capital structure for Rhode Island only
  (48% debt, 8-K 0000922224-26-000048), not for Kentucky, the deciding part; Pennsylvania's settlement "does not
  stipulate a return on equity or capital structure" (10-Q, Note 6). With an allowed share stated for less than half
  of the deciding part's rate base, the cap is the business's own long-term debt share of long-term capital at the
  latest filed date: 20,258 of 35,303 at 2026-06-30, **57.4%**. Credit = the lesser of 1,561 and 57.4% of 1,449 =
  **832 a year**; equity-funded growth spending **617**. In the growth case the growth spending grows with the growth
  and stops at year ten: gross **$1,511M in year one, $2,207M in year ten**; credit $867M to $1,267M; equity-funded
  $644M to $941M; none after year ten. The maintenance guess (depreciation) is charged in full to the equity every
  year **[L2000-035]**, **[M2014-086]**.
- **The cases, equity-only, discounted at 5.33%, then zero nominal growth after year ten:**

| Case | Value | Per share | Return at the price ($26,437M) |
|---|---|---|---|
| Organic, no growth (central top) | 13,850 | **$18.40** | 2.79% |
| Organic, growth 4.30%, growth spending net of credit (central bottom) | 13,696 | **$18.20** | 3.25% |
| Default pair, no growth (purchases stop) | 13,850 | $18.40 | 2.79% |
| Default pair, growth 11.82%, Rhode Island deducted, purchases stop at year ten | 16,568 | $22.02 | 4.20% |
| Literal shown growth 31.4%, uncut (shown beside only; cut by (f)) | 131,645 | $174.93 | 13.55% |
| All spending charged, no growth | -13,336 | -$17.72 | none |
| All-equity, organic, no growth (less net debt 19,991 at 2026-06-30) | 1,278 | $1.70 | 2.44% on EV |
| All-equity, organic, growth | -3,703 | -$4.92 | 2.66% on EV |

  The growth case values below the no-growth case: the growth bought, at the window's spending and the window's
  return, is worth a little less than its cost at the long rate, so the no-growth case is the top and the growth case
  the bottom, the inversion specific (e) names, "growth can destroy value" **[L2000-023]**. Net debt for the all-equity
  line: short-term debt 65 plus long-term debt 20,258 less cash 332 at 2026-06-30 (10-Q); operating leases left out.
  The 27.4M forward shares and the equity units are not in the share count; counting them would lower every
  per-share figure. The 2025 year alone, 1,268 at no growth, would be $31.61 a share at the long rate and a 4.80%
  return at the price: still below the price and below the floor.
- **Value range (central, equity-only): $18.20 to $18.40 a share against $35.13.** Width 1.01 to 1.
- **The floor, tested first.** No defensible case earns about ten percent at the price: the best, the default pair's
  growth case, returns 4.20%; the central cases 2.79% to 3.25%, below the 5.33% bond itself. "we don’t want to buy
  equities where our real expectancy is below 10 percent" **[M2003-149]**. The one case above ten percent is the
  uncut 31.4% growth, which the cap excludes as an absurdity **[M1999-067]**. The price is also above the top of the
  range, which closes OUT however wide the range.
- **Fair price (a reporting figure, never a verdict; Part VII): $8.39 a share**, equity-only (the regulated-utility
  central basis), after the company's own tax: the no-growth case at ten percent $9.81, the growth case at ten percent
  $6.97, averaged. All-equity beside: $-11.50 and $-20.88, averaged **$-16.19**, not positive. Default pair beside:
  $6.23 equity-only. No cheap price is reported.
- **VERDICT: OUT.** The price does not clear the floor on any case the filings support, and sits at about twice the
  top of the range. Not a close call needing a pencil **[M2009-005]**; the arithmetic is shown only because the
  regulated basis has to be built to be stated.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT). Facts below, under AFTER THE STOP.

## Q9: COULD IT RUIN US? WEIGHING.
NOT REACHED. Facts below.

## Q10: IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (not asked by the operator for this run).

---
## THE BOX
**OUT at Q7** (the floor: no case the filings support earns about ten percent at $35.13; the central equity-only
range is $18.20 to $18.40 a share, the price about twice its top). Q1 IN, Q2 IN (Kentucky decides; regulated
franchise, carried to Q3 as a second best), Q3, Q4 and Q6 weigh against, Q5 integrity IN narrowly. Reporting figures:
value range $18.20 to $18.40; fair price $8.39 (equity-only, central), $-16.19 all-equity beside.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Bears on Q8 (the bond).** The 30-year Treasury yields 5.33% (2026-10-23); the equity-only cases return 2.79% to
  4.20% at the price (Q7 table).
- **Bears on Q9 (debt and exposures).** Long-term debt 20,258M and short-term debt 65M against equity 15,045M at
  2026-06-30 (10-Q); long-term debt due within one year 469M. Pre-tax earnings plus interest over interest: 2022
  (915 + 513) / 513 = 2.8 times; 2023 (924 + 666) / 666 = 2.4 times; 2024 (1,116 + 738) / 738 = 2.5 times; 2025
  (1,472 + 808) / 808 = 2.8 times (10-Ks 2023 and 2025). PPL is a holding company whose debt is structurally
  subordinated to its subsidiaries' (Item 1A, A). Earnings come from three states and four regulated companies, the
  diversity the rows prefer to a single utility **[L2005-019]**. The plan needs $17.35B of capital over 2026 to 2028
  against operating cash of $2.6B in 2025, funded by debt, hybrids and equity (Item 7, Liquidity). The Kentucky
  high-load tariff carries minimum payments and collateral from data-centre customers; the Blackstone joint venture
  (Invitium Energy, 51%) has signed no energy services agreement and is outside the business plan (Exhibit 99.1,
  0000922224-26-000042). The "little or no debt" criterion **[R1997-001]** is stated for whole businesses.
- **Bears on Q12.** No business the rows name (casinos, tobacco, loading schemes) is carried on; the Kentucky
  generation is mostly coal (25,069 of 31,926 GWh in 2025, Item 1).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 14564e1d); written question by question; committed after Q2,
      after Q6, and with Q7 and the close (write-early).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the dispatching session holds the lock in
      `Screens/_daily/` (not touched by this analyst); the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident
      (commit subjects, one research folder name, the memory index) is declared under contamination at the top and
      not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row
      (`_research 2026-10-26 PPL/scripts/check_ids.py`); no E-ids. Every filing fact carries its accession or names
      its filing.
- [x] The order was kept; Q7 was the first STOP to fail and closed the run; Q8 to Q12 are NOT REACHED; nothing after
      Q7 is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy: operating cash less stock pay less depreciation
      (maintenance) and less capital spending (all-spending case); the sovereign from the US Treasury; the price is an
      aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations, and at each question); the facts found for Q8, Q9 and Q12
      are under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its 2021 operating cash (with the discontinued U.K.
      business) was replaced by the filed continuing-operations figure.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The line between "nervous" and "doubt" at Q5.** Q4 carries guidance and a featured adjusted figure to Q5, where
the framework closes the file on doubt, "If you’ve got doubts, forget it." **[M2013-088]**; the rows themselves call the habit something that makes them "nervous"
**[L2016-006]** and "a negative" that cannot be "a total exclusionary factor" **[M1994-018]**. Nothing says when a
disclosed, reconciled, industry-wide habit, used for pay, becomes doubt about the people. I closed Q5 IN narrowly and
said so; a second analyst could close it OUT on the same record, and the box would move from Q7 to Q5 with no change of
facts. (2) **The utility debt credit's cap where the deciding part's regulator states no capital structure.** The
fallback is "the business's own long-term debt share of long-term capital"; the text does not say whether "the
business" is the consolidated company (which carries holding-company debt the regulators never allowed) or the deciding
part. I used the consolidated company (57.4%), which gives the larger credit; the deciding part's own share would be
lower and the value lower still. (3) **The serial-acquirer rule fired on one deal.** One cash purchase in a five-year
window exceeded half of owner cash before purchases, so the organic pair became central; the rule's name suggests a
habit, its text a threshold. (4) **Organic growth "as the filer reports it"** where the filer reports none: I used the
sales growth between the two years-ends at which the same businesses were owned (2023 to 2025), a CONVENTION of this
run. (5) **The long-term debt increase over a window that opens with a divestiture.** The 2020 year-end carried the
U.K. debt, so the increase was measured from 2021-12-31 over four years and the acquired Rhode Island debt was taken
out; the text names neither adjustment. None of the five moves the box: every defensible case is below the floor at
the price.

