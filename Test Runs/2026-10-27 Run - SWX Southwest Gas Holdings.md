# Company Run: Southwest Gas Holdings, Inc. (NYSE: SWX), 2026-10-27
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied to this dated name before any fetch (commit
407a2b85). Dispatched blind run; research folder `Test Runs/_research 2026-10-27 SWX/` (notes, `calc.py` for every
figure in Q3 and Q7, `fetch.py`, `xbrl.py`, the `tools/run.py` output; filings cached under `cache/`, gitignored).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-27: the operator does not hold this name (`PORTFOLIO.md` has no SWX row).*

**Contamination, declared.** (1) A directory listing of `Test Runs/` filtered for "SWX", run to confirm this file's own
name, showed by name a file `2026-10-18 Run - SWX Southwest Gas Holdings.md` and a folder `_research 2026-10-18 SWX`.
Neither was opened, read or searched; nothing in them is known to me or used. (2) The session context showed recent
commit subjects about another company's v5 re-run (a gas utility, OGS, "OUT at Q7"). Not opened, not used; for that
reason I did not choose that company as a peer. (3) The user memory index loaded with the session names counts of
gate-clearers and a queue state; it names no company and was not used.

**Departures stated by the brief and carried here:** the repository path is `C:\Projects\BRK`; the lines of evidence
and the competitors were derived by me from the filings (see Step 0 and Q2).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $92.02 (2026-10-27 intraday, about 10:00 Eastern; Yahoo chart feed via `tools/sources.py` /
  `tools/run.py`; **aggregator, live quote only, flagged** per operator rule 5). Year-end closes from the same feed,
  used only for the retention test at Q6: 2020 $60.75, 2025 $80.02 (aggregator, flagged).
- **Shares by class:** one class, common, $1 par. 72,445,853 shares as of 2026-07-31 on the cover of the 10-Q for the
  period ended 2026-06-30, filed 2026-08-05, accession `0001692115-26-000112` (`python Screens/cover_shares.py SWX`).
  Checked: the 10-Q balance sheet shows 72,443,899 shares "issued and outstanding" at 2026-06-30, so no treasury
  stock; the 8-Ks filed after that 10-Q (2026-08-05 results, accession `0001692115-26-000109`; 2026-10-20 an officer's
  retirement, accession `0001193125-26-426703`) record no issuance. The 2026 dividend reinvestment plan issues small
  amounts (256,000 shares in 2025, 10-K Item 7).
- **Market cap:** 72.446M x $92.02 = **$6,666.5M**.
- **Sovereign for the earnings currency (USD):** **5.31%**, US Treasury daily par yield curve, 30-year, 2026-10-26
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the 10-K for 2025, filed 2026-02-25, accession `0001692115-26-000062` (Items 1,
  1A, 7, 8 and 9A in the parts cited; both registrants' statements, Southwest Gas Holdings and Southwest Gas
  Corporation, are in it); the 10-K for 2024, accession `0001692115-25-000082`, and for 2023, `0001692115-24-000038`
  (utility balance sheets); the annual-report exhibits holding the utility's statements for 2020 to 2022
  (`swx-20221231_d2.htm`, accession `0001692115-23-000056`), 2018 to 2020 (`swx-20201231_d2.htm`,
  `0001692115-21-000008`), 2017 to 2019 (`swx123119ex1301.htm`, `0001692115-20-000016`) and 2015 to 2017
  (`d513923dex1301.htm`, `0001193125-18-063850`); the 10-Q to 2026-06-30, `0001692115-26-000112`; the proxy, DEF 14A
  filed 2026-03-23, `0001692115-26-000080`; the 8-Ks of 2025-08-12 (`0001193125-25-178542`, Centuri sale and
  deconsolidation), 2026-01-09 (`0001692115-26-000004`, Item 4.02 non-reliance), 2026-02-12 (`0001193125-26-047540`,
  Icahn cooperation agreement terminated), 2026-08-05 and 2026-10-20.
- **One figure cross-checked against the filed statement:** `tools/run.py` (XBRL) gives 2025 capital spending 808 and
  depreciation and amortization 331 ($M); the filed Southwest Gas Corporation cash-flow statement in the 10-K for 2025
  shows "Capital expenditures and property additions (807,866)" and "Depreciation and amortization 330,724" ($000).
  They agree.
- **`python tools/run.py SWX`, arithmetic lines only** (output in the research folder). Its owner-earnings lines are
  Holdings' consolidated figures with Centuri inside them in 2023 and 2024 and are not used; its debt line "d1" is the
  tag CapitalizationLongtermDebtAndEquity, which includes equity, and is not used. Every figure below is read from the
  utility's own filed statements. **Owner cash after every real cost, all spending (the literal window, 2021 to 2025):
  average -$217.4M a year**; after maintenance only: **+$233.8M** (Q4 and Q7 show the build). Capital spending averaged
  $740.3M against depreciation of $289.1M; stock pay averaged $8.0M and is deducted (it is added back inside operating
  cash).
- **Which business is valued.** Since the deconsolidation of Centuri in August 2025 and the sale of the last Centuri
  shares on 2025-09-05, "the business is solely comprised of the Natural Gas Distribution segment" (10-K 2025, Item 1).
  The run values that business from the statements of Southwest Gas Corporation, the subsidiary that is the segment,
  plus the holding company's cash and costs.
- **The lines of evidence I chose, from Item 1, Item 1A and Item 7:** (1) the regulated return: allowed against
  earned return on equity, and the rate cases that set it (Item 7, Rates and Regulatory Proceedings); (2) customer and
  margin growth against the capital it takes (Item 1 and Item 7: customers, first-time meter sets, operating margin,
  capital expenditures); (3) the competitive and policy threat: electric utilities at the point of installation, and
  electrification and decarbonization policy, sharpest in California (Item 1 Competition and Environmental Matters;
  Item 1A "Our operations are subject to increased competition" and the climate-legislation risk); (4) purchased-gas
  cost pass-through and its cash swings (Item 1 and Item 7, PGA); (5) the accounts: the state-tax error, the
  restatement of two 10-Qs, the material weakness and its remediation (Item 1A, Item 9A, Note 3); (6) the capital plan,
  including the Great Basin 2028 expansion (Item 7, Capital Expenditures; 10-Q 2026-06-30).

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the margin of safety: a regulated business whose return is set by commissions
is a case where "if you have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**,
and the arithmetic below is a pencil exercise on a narrow band. A share is a business **[M1997-109]**: the question is
what the regulated network will hand its owners, not where the quotation goes; the quotation has risen from $60.75 at
the end of 2020 to $92.02, and appreciation "is never a reason to buy it" **[L2013-007]**. No macro forecast enters
**[M2000-094]**: the run makes no forecast of gas prices or interest rates; inflation enters only as a property of the
business **[M2011-054]**. Who is paid to tell you **[M2020-037]**: the company publishes net-income and rate-base growth
guidance (8-K 2026-01-09, accession `0001692115-26-000004`), and the run does not use it **[M1995-050]**.
**Contrary evidence, written down as found** **[M1997-127]**: (a) the utility has earned 6.0% to 8.5% on its year-end
equity in every year 2018 to 2025, below every return its commissions allowed (Q2, Q3); (b) operating cash has covered
capital spending in one year of eight (2024, and then only through the recovery of gas costs); (c) the 2025 10-K
revised the utility's statements back to 2017 for a state deferred-tax error and Holdings restated two 10-Qs (Q4);
(d) shares outstanding rose from 48.2M (cover, February 2018) to 72.4M, about half again, to fund the capital plan and
acquisitions later reversed (Q6); (e) the 2026 to 2030 capital plan of $6.3B, about $1.3B a year, is near twice the
window's average spending (Q3).

## THE STANDING RULE
The buyer's own conduct: a part-interest bought for cash, without borrowed money, sized so that a fall of half or more
changes nothing, would not "risk what we have and need for what we don’t have and don’t need" **[M2012-081]**; "borrowed
money has no place in the investor's tool kit" **[L2014-005]**. Nothing in the target can call on the buyer. The rule
is met on those terms; the target's own debt is weighed at Q9 if reached.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**, and the economics, not the product, are what
  must be foreseen **[M2000-104]**.
- **What the business is** (10-K 2025, Item 1): a regulated distributor of natural gas to about 2,281,000 customers
  (1,224,000 in Arizona, 849,000 in Nevada, 208,000 in California at 2025-12-31), "over 99%" residential and commercial;
  53% of 2025 operating margin earned in Arizona, 35% in Nevada, 12% in California; 85% of margin from residential and
  small commercial customers. Rates are set by the ACC, PUCN and CPUC on "rate base, cost of service, and cost of
  capital"; Great Basin, an interstate pipeline in northern Nevada, is regulated by FERC. Rates in all three states are
  "decoupled" from volume, and gas costs pass through by PGA clauses that "affect cash flows, but have no direct impact
  on margin".
- **The key variables and how predictable they are** **[M1998-044]**: (1) rate base, which grows with the capital
  spent and is visible in the filings (gross gas plant $6,193.8M at 2016-12-31 to $11,517.0M at 2025-12-31); (2) the
  allowed return on equity and the equity share of capital in each state, stated in each rate decision (Arizona 9.84% on
  48.5% equity, decided March 2025; Nevada 9.5% on a hypothetical 50% equity, rates effective April 2024; California
  11.16% authorized, a proposed decision of June 2026 recommending 10.0% on 50% equity); (3) how much of the allowed
  return is actually earned, the regulatory lag, read from the accounts; (4) customer growth, 2,047,000 (10-K 2018) to
  2,281,000 (10-K 2025), about 1.6% a year; (5) the policy threat to gas use. The first four have moved slowly and
  visibly for eight years. The fifth is the one a forecaster could get wrong, and it is a question of the castle (Q2,
  test 11), not of whether the economics can be read.
- **Would the insiders write it down?** **[M2000-105]**. They do: the company files a five-year construction plan
  ($6.3B for 2026 to 2030, Item 7) and its commissions publish multi-year rate decisions and, in Nevada, a triennial
  resource plan under SB 281. The plan is not used as a projection **[M1995-050]**; its existence shows the industry
  writes the ten-year picture down, unlike the tech field of the row.
- **Change.** "We view change as more of a threat into the investment process than an opportunity" **[M1999-063]**.
  The change here is policy, slow and visible in statute: Arizona bars municipalities from banning gas service; Nevada's
  SB 281 "reinforces natural gas’ role"; California's AB 1207 "contemplates the transition of gas utilities’ free
  allowances to electric utilities" (Item 1, Competition and Environmental Matters). California is 12% of margin. This
  is not a technology whose ten-year economics cannot be seen; it is a threat the castle questions must weigh.
- **Doubt about the perimeter** **[M2002-092]**: none that the economics can be read. The bank and holding-company
  doors do not apply: since September 2025 Holdings owns one business (Item 1).
- **VERDICT: IN.** The ten-year economics are those of a rate-regulated network whose return, rate base and customer
  count are each stated in the filings and have moved slowly; this is a business where one can have "a pretty good idea
  where it’s going to be in ten years" **[M1997-021]**. The electrification threat goes to Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now." **[M1995-038]**

- **The parts table** (section B). The filer reported two segments until August 2025 and one since: "After the
  deconsolidation of Centuri in August 2025, the business is solely comprised of the Natural Gas Distribution segment"
  (10-K 2025, Item 1). The interstate pipeline bought at the end of 2021 (MountainWest) was sold in February 2023
  (Holdings income statement 2023: "Goodwill impairment and loss on sale" $71.2M). What a buyer gets today is one part:

  | Part | Share of five-year operating profit of what is owned now | Castle | Decides |
  |---|---|---|---|
  | Natural gas distribution (Southwest Gas Corporation, including Great Basin, FERC rate base about $191M per the 10-Q) | 100% (operating income 2021 to 2025: $318.6M, $307.7M, $349.7M, $412.7M, $482.4M) | a regulated franchise, read below | yes |

- **Test 3, the money test** **[M2011-015]**: could a rival with money build a second gas network under the streets of
  Las Vegas, Phoenix and Tucson? The commissions grant the service territories, and a second network would recover only
  what its rates allowed; no attacker of the distribution business is named in the filing. The attackers the 10-K names
  are of two kinds: "Electric utilities are the principal competitors of Southwest Gas for the residential and small
  commercial markets", competing "at the initial installation phase", and interstate pipelines (El Paso, Kern River,
  Transwestern, Tuscarora, Ruby) that pose "a potential bypass threat" to large users near them (Item 1, Competition;
  Item 1A). On the money test the castle stands.
- **Test 1, the key factors and how permanent they are** **[M1995-038]**: the franchise plus the installed appliance:
  "The customer will generally continue to use the chosen energy source for the life of the equipment", and Southwest
  Gas "provided natural gas to a large majority of the new homes constructed during the year in the major metropolitan
  markets" (Item 1). Its permanence depends on state law, which the filings show moving in opposite directions:
  protective in Arizona (municipal gas bans barred) and Nevada (SB 281 "reinforces natural gas’ role"), adverse at the
  margin in California (AB 1207, free allowances to move to electric utilities; Item 1).
- **Test 2, would it stand without the lord** **[M1996-037]**: yes. Margin is decoupled from volume, gas costs pass
  through, and "approximately 93% of our margin is fixed each year" (proxy 2026, compensation section). These are
  "pass-through organizations. They need to be operated efficiently in order to achieve their rate of return"
  **[M2012-013]**.
- **Test 4, pricing power and the agony before a rise** **[M2005-020]**: the business has none of its own. Every price
  is set in a contested rate case, and the window shows the agony: Arizona asked $125.6M at 10.15% and was granted
  $80.2M at 9.84% (March 2025); Nevada asked $74.0M and was granted $59.1M at 9.5% (April 2024); California asked $43.7M
  at 11.35% and settled the revenue at $39.5M with the return litigated, the proposed decision recommending 10.0% (10-K
  Item 7; 10-Q 2026-06-30). The return is "more or less — within a range, anyway — a guaranteed return" **[M2009-104]**,
  not a return the business can raise.
- **Test 5, unit volume and share of mind** **[M1999-054]**: customers grew from 2,047,000 (10-K 2018) to 2,281,000
  (10-K 2025), higher every year; first-time meter sets were 41,000 in 2024 and 37,000 in 2025 (a 1.6% rate). Transport
  throughput for large users fell from 92.7 million dekatherms in 2024 to 83.7 million in 2025 (Item 1), on 11% of
  margin. The unit that matters, the customer, grows slowly and steadily.
- **Test 6, the low-cost position** **[M2018-043]**: against electricity at installation, the company claims "the
  abundance, low cost, resiliency, and reliability of natural gas" as its advantage (Item 1). The filing gives no
  delivered-cost comparison with the electric utilities, so the claim is the company's, not shown.
- **Test 8, would the customer choose it over the low bid** **[M2017-009]**: the residential customer cannot take
  another distributor's bid; the large user can, and the filing says the company keeps such customers by "negotiated
  transportation contract rates" and "special long-term contracts" (Item 1), that is, by cutting price where the
  alternative is real.
- **Test 9, ask the competitors.** No competitor's statement about Southwest Gas is on the public record I read.
- **Test 10, widening or narrowing** **[M1999-108]**: on customers, slowly widening; on policy, a stand-off, two states
  protective and one adverse; and Great Basin's open seasons drew precedent agreements for "just under 1 Bcf/d" for 2028
  and "further expressions of incremental capacity interest for an additional 1.8 Bcf/d" (10-Q 2026-06-30), demand
  evidence for the pipeline.
- **Test 11, what could destroy, modify or reduce it** **[M2000-014]**: (a) electrification mandates, or the loss of new
  construction to all-electric homes, starting where the law is adverse (California, 12% of margin); (b) a regulatory
  climate that turns, which the speakers narrate as their own mistake: "I did not anticipate or even consider the
  adverse developments in regulatory returns" **[L2023-011]**; (c) disallowance of costs already in plant (Item 1A, "Our
  regulated operations plant and other assets may be subject to impairment"). "slow change can be much harder to
  perceive, and can lull you to sleep easier" **[M2014-038]**. None of these is shown on the evidence to be filling in
  the moat today; each is a threat named in the filing.
- **The competitor row** (rivals the 10-K names, from their own filings). Of the named rivals, one files with the SEC
  today: **Northwest Pipeline LLC** (CIK 110019; named in Item 1 among Great Basin's rivals as "Northwest Pipelines").
  Named rivals that do not file: El Paso Natural Gas (last 10-K 2012), Kern River, Transwestern, Tuscarora (its former
  owner TC PipeLines LP last filed a 10-K in 2021), Ruby, Pinyon Pipeline, Prospector Pipeline; the electric utilities
  are named only as a class. Because the one named filer competes only with the small pipeline part, I add as a
  **CONVENTION of this run** one peer for the distribution business, **Atmos Energy** (CIK 731802), the largest
  pure-play gas distributor filing with the SEC. Rationale: Q2 section C asks for the field's returns and the 10-K names
  no gas distributor; I chose it before reading its figures. Metric: net income over year-end equity, from the filers'
  own statements (XBRL transcription), over the whole span read:

  | Year | SWX utility (Southwest Gas Corp.) | Atmos Energy (FY to Sept.) | Northwest Pipeline LLC |
  |---|---|---|---|
  | 2018 | 7.8% | 12.6% | 11.7% |
  | 2019 | 8.1% | 8.9% | 12.4% |
  | 2020 | 7.1% | 8.9% | 13.2% |
  | 2021 | 7.4% | 8.4% | 12.2% |
  | 2022 | 6.0% | 8.2% | 12.3% |
  | 2023 | 7.2% | 8.1% | 15.9% |
  | 2024 | 8.1% | 8.6% | in Williams' combined 10-K, not read |
  | 2025 | 8.5% | 8.8% | in Williams' combined 10-K, not read |

  Sources: SWX from the utility's filed statements (Step 0 accessions; 2024 equity as revised in the 2025 10-K); Atmos
  10-Ks, latest accession `0000731802-25-000056`; Northwest Pipeline 10-Ks `0000110019-21-000003` to
  `0000110019-24-000003`. Southwest Gas earned less on its equity than the distribution peer in every year of the span,
  and less than any return its commissions allowed (9.5% to 11.16%) in every year.
- **The field's returns over the last full cycle** (section C): regulated gas distribution earns about 8% to 9% on
  equity at the peer and 6% to 8.5% at Southwest Gas, across a span that held the 2021 to 2022 gas-price spike and its
  recovery. These are ordinary returns. The section's own exception governs: "A return set by a regulator is the
  exception, carried to Q3 as a second best" (the framework's words), on **[M2009-104]** and **[L2009-012]**. The
  ordinary return does not close the file here; it is weighed at Q3.
- **VERDICT: IN.** The castle stands: a regulated franchise no attacker with money could duplicate **[M2011-015]**,
  whose customers grow slowly every year and whose margin is fixed by decoupling. It protects a return the regulator
  sets, not the "excellent returns" of the moat row **[L2007-004]**, and that is carried to Q3. The threats
  (electrification, the regulatory climate) are named in the filing and not shown to be filling the moat in today
  **[M2000-014]**.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
Figures from the utility's filed statements (Step 0 accessions), computed in `calc.py`.
- **Return on the capital actually needed** **[M2010-090]**: net income over year-end equity 7.8%, 8.1%, 7.1%, 7.4%,
  6.0%, 7.2%, 8.1%, 8.5% for 2018 to 2025 (Q2 table). Against its own allowed returns (9.5% Nevada, 9.84% Arizona,
  11.16% California authorized), it has under-earned every year. The proxy's own long-term pay target is a three-year
  average utility return on equity of 7.77% at target (threshold 7.27%, maximum 8.28%; DEF 14A 2026,
  `0001692115-26-000080`): the board plans for an under-earned return. "if you have a business that’s earning 5 or 6
  percent on equity and you hold it for a long time, you are not going to do well in investing" **[M1998-006]**; this one
  earns 6% to 8.5%.
- **What the added capital earned**, measured as the row measures it, "by the operating earnings after depreciation"
  **[M2014-086]**: net regulated plant rose from $6,176.1M (2020-12-31) to $8,690.5M (2025-12-31), $2,514.5M added;
  operating income rose from $302.6M (2020) to $482.4M (2025), $179.8M: **7.2% before tax on the added plant**. On the
  equity: equity rose $1,291.5M and net income $141.2M, 10.9%; but "Other income (deductions)" moved from -$6.6M (2020)
  to +$52.4M (2025) (interest income and the cash surrender value of company-owned life insurance, Item 7 and Note 1);
  without that swing, after tax at 21%, the added equity earned about 7.3%. These are "decent returns on the
  incremental sums" **[L2009-012]** only at the low end.
- **To stand still, and to grow** **[L1999-024]**: depreciation averaged $289.1M a year over 2021 to 2025 against
  capital spending of $740.3M, 2.6 times. The filing gives no split of spending into maintenance and growth, so the
  maintenance guess is the depreciation charge, which "is not inappropriate in most companies to use as a proxy for
  required capital expenditures" **[M1998-127]**; the bias is stated: the filing says "Significant replacement
  activities are expected to continue well beyond the next few years" (Item 7), and for utilities "your depreciation
  charges are inadequate and you’re kidding yourself as to your real economic profits" **[M2015-049]**, so true
  maintenance may sit above the charge. The spending above depreciation, $451.2M a year, buys about 1.6% a year in
  customers and rate-base growth that the commissions price.
- **How it is funded.** Operating cash covered capital spending in one year of eight (2024, through the recovery of
  gas costs under-collected in 2021 to 2023). Over 2021 to 2025 the utility added $1,069.8M of long-term debt and received
  $752.6M of equity from its parent (cash-flow statements: $202.6M, nil, $530.0M, nil, $20.0M), which the parent raised
  by issuing shares ($213.6M, $461.8M, $251.8M, $8.9M, $19.7M; Holdings XBRL `ProceedsFromIssuanceOfCommonStock`, 10-K
  accessions above) and in 2025 from the Centuri sale. The plan for 2026 to 2030 is $6.3B of construction, "approximately
  $1.3B" a year in 2026 and 2027 and $1.8B in 2028, with operating cash to provide "approximately 60% of the funding for
  total construction expenditures, and dividend requirements" (Item 7). "To earn more, their owners must invest more"
  **[L2011-019]**; this is "compulsory reinvestment" **[M1997-016]** in the plain sense: the commissions require the
  safety and replacement programs, and growth in rate base is the only road to growth in earnings.
- **The growth arithmetic and its caps** **[M1998-081]**: the second-best business "takes more money, but the rate at
  which you invest — reinvest — the money to get that growth is a very satisfactory rate". Here the rate is the regulated
  rate less the lag, about 7% to 8.5% on equity, and the speakers' own grade for it is "as the second-best choice, still
  a good choice" **[M2018-055]**, conditional on the return: "cash-consuming businesses, by their nature, are
  unattractive unless the cash they consume gets to earn a reasonable return" **[M2012-057]**.
- **WEIGHS AGAINST.** A capital-heavy regulated business that must take in outside debt and equity every year to grow,
  earning on its equity less than its commissions allow and less than the field's peer, with a return on added plant of
  about 7% before tax; a second best **[M2018-055]** at the low edge of "decent" **[L2009-012]**. ("Little or no debt" is
  for Q9.)

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them, before the income account** **[M2025-032]**: Southwest Gas Corporation,
  $M, read from the filed statements (Step 0 accessions; 2016 and 2017 from the FY2017 report as recast without
  Centuri; 2024 as revised in the 2025 10-K).

  | Year-end | Gross gas plant | Equity | Long-term debt incl. current | Short-term debt | Retained earnings | Cash | Deferred purchased gas, net (+ owed by customers, - owed to them) |
  |---|---|---|---|---|---|---|---|
  | 2016 | 6,193.8 | 1,667.9 | 1,400.1 | 0 | 767.1 | 19.0 | not extracted |
  | 2017 | 6,629.6 | 1,610.0 | 1,521.0 | 191.0 | 659.2 | 37.9 | not extracted |
  | 2018 | 7,134.2 | 1,782.5 | 1,818.7 | 152.0 | 717.2 | 32.0 | -74.8 |
  | 2019 | 7,813.2 | 2,005.2 | 2,116.3 | 194.0 | 782.1 | 40.5 | -16.3 |
  | 2020 | 8,384.0 | 2,233.5 | 2,438.2 | 57.0 | 835.1 | 41.1 | -52.6 |
  | 2021 | 8,901.6 | 2,527.9 | 2,715.6 | 250.0 | 906.8 | 38.7 | +291.1 |
  | 2022 | 9,453.9 | 2,569.2 | 3,251.3 | 225.0 | 935.4 | 51.8 | +450.1 |
  | 2023 | 10,140.4 | 3,183.6 | 3,501.5 | 0 | 1,018.5 | 71.2 | +552.9 |
  | 2024 | 10,844.9 | 3,235.5 | 3,504.5 | 0 | 1,059.8 | 311.1 | -239.6 |
  | 2025 | 11,517.0 | 3,525.0 | 3,508.0 | 0 | 1,314.9 | 56.4 | -304.9 |

  **What moved and why.** Plant nearly doubled (+86%); equity more than doubled (+111%), but mostly by paid-in capital
  from the parent (additional paid-in capital $1,065.2M at 2018 to $2,195.5M at 2025), not by retained earnings; debt
  rose 2.5 times; long-term debt over long-term debt plus equity went from 46% (2016) to 52% (2020) to 50% (2025).
  Goodwill is trivial ($11.2M). Receivables run near 9% to 10% of revenue throughout (2018 $140.1M on $1,357.7M; 2025
  $170.5M on $1,942.5M), no build. The one large swing is purchased gas: customers owed the utility $552.9M at the end of
  2023 for gas bought in the 2021 to 2023 price spike, financed with debt, recovered in 2024, and by 2025 the utility
  owed customers $304.9M. Retained earnings fell from $767.1M to $659.2M in 2017, the year the holding company was formed.
  **What the figures can't say** **[M2025-032]**: whether the regulatory assets will be allowed. The filing states the
  rule: "If rate recovery is no longer probable, due to competition or the actions of regulators, the related
  regulatory asset is required to be written off" (Note 1).
- **The real costs.** Depreciation is charged at about 2.7% of original cost (2.3% for transmission and distribution
  plant, Note 1), a 40-year-plus life; it is a true cost **[L2015-004]** and, for the reason given at Q3, may be short of
  the true maintenance need **[M2015-049]**. Stock pay is expensed ($13.0M in 2025) and is deducted from owner cash here
  **[L2021-003]**. Pensions: discount rate 5.75% both years (Item 7). No EBITDA is featured in the 10-K; the company
  features "utility gross margin" and "operating margin" (non-GAAP, Item 7) and pays on "utility adjusted net income"
  ($273.9M in 2025 against GAAP utility net income of $300.3M; proxy 2026).
- **The tells** **[M1995-064]**. (1) **Restatement and revision.** On 2026-01-09 the Audit Committee concluded that the
  10-Qs for the periods ended 2025-06-30 and 2025-09-30 "should no longer be relied upon" (8-K Item 4.02,
  `0001692115-26-000004`): state deferred-tax apportionment rates were not updated after the Centuri share sales. For
  the utility "the errors date back to the formation of Southwest Gas Holdings in 2017"; they were judged not material
  to any period, but the 2025 10-K revised the history "due to the magnitude of the cumulative effect" ($36.4M off 2024
  equity) and "also revised the historical financial statements to correct other previously identified immaterial
  errors" (Note 3; 2024 revenue +$7.8M, net income +$0.9M). A material weakness was reported in the 10-K (Item 1A, Item
  9A) and declared remediated at 2026-06-30 (10-Q, Item 4). "There is seldom just one cockroach in the kitchen"
  **[L2002-039]**: here there were two sets of errors, one a control failure over eight years. (2) **A deferred account
  building.** "Prepaid and other current assets" rose from $140.9M to $234.0M in 2025; the filing names the cause, a
  regulatory asset for Arizona decoupling (revenue recognized and not yet billed) of $91.1M against $32.4M (Note 1). It
  is explained, not hidden, and it is the kind of account the row says to "look twice" at **[M1995-064]**. (3)
  **Guidance.** The company publishes guidance for net income and for compound growth in utility net income and rate
  base for 2025 to 2029, and reaffirmed it in the non-reliance 8-K itself: "The Company reaffirms its guidance for 2025
  net income" (8-K 2026-01-09). Earnings guidance **[L2019-006]** and an adjusted figure in pay **[L2016-006]** are
  recorded here as a weighing against **[M1994-018]** and carried to Q5.
- **Is it confusion or suspicion?** No. The error is identified, quantified, explained, non-cash ("The Company does not
  expect any impact on previously reported operating margin, cash flows", 8-K 2026-01-09) and its control declared
  fixed; the decoupling asset is named and explained. The figures can be read. "if I don’t understand it, I figure it’s
  probably because the management doesn’t want me to understand it" **[M2003-029]** does not apply: I understand it. The
  weak control is a weight against, not a STOP.
- **The recast earnings for Q7.** Owner cash is built from the utility's operating cash, which already deducts interest
  and the company's taxes paid and includes working capital (specific (d)), less stock pay, less capital spending (all
  spending, or the maintenance guess). Two adjustments, both stated: (i) in 2025 the utility lent its parent $105.6M
  ("Receivable from parent", inside operating cash); that cash stayed in the group, so it is added back; (ii) the holding
  company's own costs are deducted, at $6.0M a year before tax, $4.7M after tax at 21% (**CONVENTION of this run**:
  the corporate operating costs in the 2025 and 2024 Holdings income statements were $6.4M and $5.9M above the utility's,
  Item 8; earlier years carried the Icahn contest and Centuri, which no longer exist; rationale: the ongoing cost of the
  business as it now stands). Year by year, $M:

  | Year | Operating cash | Capital spending | Stock pay | Depreciation | Owner cash, all spending | Owner cash, maintenance only |
  |---|---|---|---|---|---|---|
  | 2021 | 25.2 | 602.0 | 6.4 | 253.4 | -583.1 | -234.5 |
  | 2022 | 284.4 | 683.1 | 5.8 | 263.0 | -404.5 | 15.6 |
  | 2023 | 391.5 | 762.1 | 4.9 | 295.5 | -375.4 | 91.2 |
  | 2024 | 1,253.0 | 846.6 | 10.0 | 303.1 | 396.4 | 939.9 |
  | 2025 | 618.8 (+105.6) | 807.9 | 13.0 | 330.7 | -96.5 | 380.7 |
  | Average, less holding-company cost | 535.7 | 740.3 | 8.0 | 289.1 | **-217.4** | **233.8** |

  The yearly figures swing with purchased gas (2021 -$343.7M, 2024 +$715.0M in the operating-cash line "Deferred
  purchased gas costs"); the working-capital lines net to -$6.0M a year over the window, so the average is not carried
  by them. Two figures are shown beside, not used centrally: with the window's net build of gas-cost over-collection
  owed to customers taken out ($252.3M over five years, $50.5M a year), owner cash after maintenance is $183.4M; with
  deferred income taxes taken out (average $81.8M; of utility deferred taxes the row says "I don’t think I would look at
  that as a hidden form of equity" **[M2015-030]**), it is $152.0M.
- **VERDICT on the accounts: WEIGHS AGAINST.** Not a STOP: nothing confuses and the one suspicious-looking account is
  explained. Against: a restatement, a revision reaching back to 2017, a material weakness, published guidance, and pay
  on an adjusted figure, carried to Q5 **[M2013-088]**.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who runs it now.** The chief executive since 2022, Karen Haller, gave notice on 2026-02-19 and left the post on
  2026-05-08; she stays as an advisor through 2026-12-31 at "a monthly salary of $95,000", with her "existing equity and
  cash incentive awards" continuing to vest (8-K 2026-02-25, `0001193125-26-071537`). Her successor is Justin Brown,
  President of Southwest Gas, appointed from inside, with a "one-time performance stock unit (“PSU”) award with a target
  value equal to $3.1 million" (same 8-K). The chief financial officer left on 2025-12-01 with $1,568,400 in cash under a
  separation agreement (8-K 2025-11-05, `0001193125-25-266887`); the investor-relations vice president and treasurer
  since 2023-2024 was made chief financial officer (8-K 2025-11-26, `0001193125-25-300528`). The chief administrative
  officer will retire by June 2027 (8-K 2026-10-20). The board chair is a non-executive director (proxy 2026). The
  Icahn Group held board seats under cooperation agreements from 2022 (proxy 2026) until both sides ended the last one on
  2026-02-11 (8-K 2026-02-12, `0001193125-26-047540`); three of its designees remain directors.
- **The first yardstick, how well they run the business, against the hand dealt** **[M1994-008]**: the hand is a
  growing, decoupled, regulated territory. The record: the utility earned 6.0% to 8.5% on equity against allowed returns
  of 9.5% and above in every year 2018 to 2025 (Q2, Q3), and the long-term pay plan sets the target at a 7.77% average
  (proxy). The capital-allocation record at the holding company: two acquisitions for cash in 2021 ($2,354.3M paid for
  businesses, net of cash acquired; Holdings XBRL, 10-K 2023 accession `0001692115-24-000038`), one of them, the
  MountainWest pipeline, written down by a "pre-tax goodwill impairment loss of $449.6 million in the fourth quarter of
  2022" and sold in February 2023 "for $1.5 billion in total enterprise value" (10-K 2023); the other inside Centuri,
  which was floated in 2024 and sold out by September 2025. That is the work of the earlier management and board as
  much as this one; the current team's record is the unwinding.
- **The second yardstick, how they treat the owners** **[M1994-009]**: read in the proxy and below at Q6, Part B: chief
  executive pay of $10,029,409 in 2025 (Summary Compensation Table) on utility net income of $300.3M; special
  performance units for the chief executive in 2024 and 2025 for the "transformation"; pay set against the 50th
  percentile of a peer group benchmarked by Aon; incentive pay on "utility adjusted net income" and adjusted earnings
  per share.
- **The habits carried from Q4**: guidance, reaffirmed in the very 8-K that withdrew reliance on two 10-Qs; an adjusted
  figure in pay; and accounting errors found three times in four years (a $21M misstatement of the 2022 MountainWest loss
  "identified" in the first quarter of 2023, 10-K 2023; the state deferred-tax apportionment error from 2017 to 2025;
  "other previously identified immaterial errors", 10-K 2025 Note 3). Each was found and disclosed by the company itself,
  before an outside party forced it; the non-reliance 8-K came six weeks before the 10-K; the weakness was declared
  remediated within six months, and its cause is named in plain words in the 10-Q.
- **The tells of dishonesty** (Q5's list): no "too good to be true" claim found; the reports explain the errors rather
  than "dancing around" them; no sign of a management fixed on the stock price beyond the ordinary guidance; mistakes are
  named in the filings (the restatement, the material weakness). "Never deal with a rascal under the expectation that
  you can prevent him from cheating you" **[L2023-003]**, and the rule is applied on doubt: "If you’ve got doubts, forget
  it." **[M2013-088]**. I found errors of control and costly decisions, not deceit.
- **Love of the business, and after the cheque**: the outgoing chief executive leaves with an advisory salary and
  continued vesting; the incoming one is a 2026 promotion from inside the utility. No evidence either way on love of the
  business beyond tenure.
- **VERDICT on integrity: IN** (no fact found that raises doubt about honesty; the accounting errors are carried as a
  weight on ability and on the accounts, not as deceit) **[M2015-047]**. **Ability WEIGHS AGAINST**: a regulated
  business that has under-earned its allowed return every year for eight years, a board that planned for that, an
  acquisition written down within a year, and a turnover of the chief executive and chief financial officer within
  three months of a restatement **[M1994-008]**, **[M2021-042]**.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
- **The retention test** **[R1995-009]**, **[M1998-110]**, at Holdings over 2021 to 2025: net income attributable
  $200.8M, -$203.3M, $150.9M, $198.8M, $439.8M, total $787.0M; common dividends paid $138.2M, $160.6M, $174.6M, $177.6M,
  $178.5M, total $829.5M (Holdings XBRL, 10-K accessions above). Nothing was retained: dividends exceeded earnings by
  $42.5M, and the 2025 earnings include a $200.3M gain in discontinued operations from the Centuri sale. Meanwhile
  $955.8M of new shares were sold (Q3). Market value: 57,225,776 shares (cover, February 2021) at $60.75 = $3,476.5M;
  72,269,125 shares (cover, February 2026) at $80.02 = $5,783.0M (prices aggregator, flagged). The market leg rose
  $2,306.5M on $913.3M of capital put in, so it passes in market value; but the row's correction says the market leg
  alone misleads **[R2009-002]**, and against value per share the record is a written-down acquisition and a book value
  per share that moved from $46.8 (2020) to $54.8 (2025).
- **Issuance and deals.** "Only if we receive less in value than we give" **[M1995-001]**: MountainWest was bought for
  cash at the end of 2021 and the company wrote off $449.6M of goodwill on it within a year (Q5), value given above value
  got. Both 2021 deals were paid in cash, so they are acquisitions, not mergers in the framework's usage, and the Part A
  STOP (an all-stock deal in undervalued stock) does not arise. Shares outstanding went from 48,159,162 (cover, February
  2018) to 72,445,853 (cover, July 2026), about 50% more, through the at-the-market programme and the dividend
  reinvestment plan; $340.0M remains available under the at-the-market programme (Item 7), though the company "does not
  expect to issue equity in 2026" (10-Q). "we have never invested in companies that are hell-bent on issuing shares"
  **[L2014-015]**: the issuance funded a regulated rate base, which is the common shape of the industry, and stopped in
  2024; it is weighed here, as the framework carries that row (a candidate STOP, unresolved, section VI).
- **Buybacks.** No repurchases in the window (no repurchase line in the cash-flow statements 2021 to 2025). *(Written
  back from Q7, committed with Q7:)* the test of prices paid against the bottom of the Q7 range does not arise; for the
  record, the bottom of the range is $63.70 a share on the central case (no-growth alone) and $63.23 with the growth case
  shown beside, against a price of $92.02, so a repurchase at today's price would sit above it **[L2016-002]**.
- **Dividends and the use of cash.** The dividend has been $2.48 a share a year since 2022 (Holdings XBRL), paid while
  the utility cannot fund its own construction: operating cash will provide "approximately 60% of the funding for total
  construction expenditures, and dividend requirements" (Item 7), and the Centuri proceeds are to fund "future dividend
  payments to stockholders that would otherwise be funded by Southwest Gas" (Item 7). The row's test is the reverse case:
  a dividend is right for "a company that expects to regularly earn more than it can profitably employ" **[M2004-089]**;
  this one earns less than it employs and borrows and issues to pay. The policy is "clear, consistent" **[L2012-015]**;
  whether it is rational at a company that sells shares in the same years is doubtful.
- **Part A WEIGHS AGAINST**: a cash acquisition that destroyed value, a half-again share count, and a dividend paid out of
  issuance and debt; the 2025 sale of Centuri for about $1.3B, applied to debt and the utility's plan, is the one clear
  return of value.

### Part B: the pay, the board and the owners
- **Pay tied to what the person controls** **[M2003-019]**: the annual plan pays on utility adjusted net income (40%),
  customer satisfaction, cost per customer and safety measures; the long-term plan on three-year adjusted utility
  earnings per share (60%) and average utility return on equity (40%, target 7.77%), with a relative-return modifier.
  The measures are the utility's own and mostly within management's reach; but the earnings measure is an adjusted
  figure, and the return target is set below what the commissions allow.
- **Who designs it** **[M1994-009]**: a compensation committee benchmarking to the 50th percentile of the relevant
  market with Aon (proxy). "comp committees have become slaves to comparative data" **[L2005-015]**; "we do not bring
  in compensation consultants" **[M2004-016]**.
- **The extras**: special performance units for the chief executive in 2024 and 2025, a $3.1M one-time unit for the
  successor, $1.57M to the departing financial officer, an advisory salary of $95,000 a month and continued vesting for
  the departing chief executive, and "above-market" deferred-compensation earnings reported for executives (proxy,
  Summary Compensation Table notes). "The acid test for reform will be CEO compensation" **[L2002-029]**. These are
  weighed below the question of the person **[M2007-006]**.
- **The board**: a non-executive chair, so the chief executive does not also chair **[L2014-026]**; a board reshaped by
  an activist's designees from 2022 to 2026.
- **Part B WEIGHS AGAINST**, mildly: ordinary utility pay practice, benchmarked, with special grants around each
  transition.

## Q7: WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is
the risk-free interest rate" **[L2000-021]**. All figures from `calc.py` in the research folder; $M unless per share.

- **The basis: equity-only, central** (Q7, The regulated utility). The whole business earns a return its regulators
  allow on invested capital, the row's own exception for "the fixed-asset commitments at our regulated utilities"
  **[L2017-012]**; "when you get an allowed return in the electric utility you’re almost certain of earning it"
  **[M2010-037]** (this company has not, Q3). Owner cash is after interest and after the company's tax, against the
  market value of the shares. The holding company's own cash at 2026-06-30 is added: consolidated cash $270.5M less the
  utility's $58.9M = **$211.6M** ($2.92 a share); the holding company has had no debt since the 2025 repayments (10-K
  Item 7; 10-Q). No subsequent event stated in the 10-Q changes it.
- **The cash input** (Q4's recast): five-year average 2021 to 2025, owner cash after maintenance only **$233.8M**;
  after all spending, **-$217.4M** (the literal window, shown beside). The maintenance guess is the depreciation charge,
  $289.1M a year (Q3); the filing allows the guess only through the charge, said so **[M2000-144]**, **[L1999-024]**.
- **The six specifics.** (a) **Cycles**: the window holds one full purchased-gas cycle, the under-collection of 2021 to
  2023 and its recovery in 2024; the filer describes no year as aberrational in its earnings, and the working-capital
  lines net to -$6.0M a year over the window, so the window is the base; the yearly literal figures are in Q4. (b)
  **Growth**: the recast series, owner cash after maintenance with working capital, runs -$234.5M, $15.6M, $91.2M,
  $939.9M, $380.7M. It changes sign, so the growth is measured between halves: 2021-2022 average -$109.5M, 2024-2025
  average $660.3M, a rate from a negative base, meaningless. **By (b), the central range is the no-growth case alone,
  said so.** Shown beside: the growth of the same series before working-capital swings, $139.2M in 2021 to $382.4M in
  2025, 28.7% a year. (c) **Acquisitions**: none at the utility in the window; the holding company's 2021 purchases were
  sold (2023, 2025) and are not in the business valued. (d) **Working capital**: counted, inside operating cash. (e)
  **Growth spending** (beside case only): capital spending above depreciation averaged $451.2M; in the growth case it
  grows at the growth carried and stops at year ten: **$475.1M in year one, $756.9M in year ten, none after.** (f) **The
  cap**: 28.7% carried ten years would put owner cash at $4,777M against sales of $3,576M at the business's own sales
  growth, far above the highest share of sales owner cash has reached in the filings read (19.7%, 2025): an absurdity
  **[M1999-067]**. The rate is cut to the business's sales growth over the window, 6.3% a year (regulated revenue
  $1,521.8M in 2021 to $1,942.5M in 2025; operating margin grew 7.3%), and by (f) to no more than the discount rate:
  **5.31%** for ten years, zero nominal growth after **[M1997-095]**.
- **The utility debt credit** (beside growth case only; Q7, The regulated utility, 2026-10-23). Long-term debt
  including current maturities: $2,438.2M at 2020-12-31, $3,508.0M at 2025-12-31 (short-term debt, nil at both dates,
  and cash left out; no securitization bonds; finance-lease principal is paid inside an "Other" financing line of a few
  million a year and its balance is not separately stated, said so): **increase $1,069.8M, $214.0M a year**, credited
  against the growth spending only. The cap: the allowed debt shares the filing states are Arizona 51.5% (equity 48.5%),
  Nevada 50% (a hypothetical 50/50 structure), California 50% (the 2026 proposed decision's 50.0% equity layer); Great
  Basin's FERC settlement states a pre-tax return, not a structure. The filing states no rate base by state; weighting by
  the share of operating margin (53%, 35%, 12%, Item 7) as the stand-in for rate base is a **CONVENTION of this run**
  (rationale: the only stated weight; the states with stated shares carry well over half of it, so the fallback does not
  apply): **cap 50.8%** of growth spending, $229.2M, above the $214.0M increase, so the credit is $214.0M, growing with
  the growth spending: **net growth spending $249.8M in year one, $398.0M in year ten.** (The business's own long-term
  debt share of long-term capital at 2025-12-31 is 49.9%, for comparison.) The assets are "funded by large amounts of
  long-term debt" **[L2010-012]**, and the return on added capital is "measured by the operating earnings after
  depreciation" **[M2014-086]**.
- **The rate: 5.31%**, the US Treasury 30-year par yield of 2026-10-26, "use the government bond rate" **[M1996-025]**.
- **The value range, equity-only, per share** (72.446M shares; holding-company cash added):

  | Case | Value | Per share |
  |---|---|---|
  | **No growth, maintenance only (the central range, by (b))** | $233.8M / 5.31% = $4,403.2M, + $211.6M | **$63.70** |
  | Beside: growth case, 5.31% for ten years, net growth spending charged, zero growth after | $4,369.1M, + $211.6M | $63.23 |
  | Beside: no growth, with the window's build of gas-cost over-collection owed to customers taken out (base $183.4M) | | $50.58 (growth case $43.15) |
  | Beside: no growth, with deferred income taxes taken out (base $152.0M) | | $42.44 |
  | Beside: the literal window, all spending (-$217.4M a year) | no positive value | n/a |
  | **All-equity basis, beside**: owner cash before interest $345.6M (interest averaged $141.5M, $111.8M after tax at 21%), less net debt at 2026-06-30 of $3,239.3M (long-term debt $3,409.9M + current maturities $100.0M - cash $270.5M; operating leases left out, said so) | | no growth $45.11; growth case with all growth spending charged and no credit $30.53 |

  The growth case sits just below the no-growth case: the growth carried equals the discount rate, so each year's
  growth adds no present value and the spending that buys it is a cost; "growth can destroy value" **[L2000-023]**, and
  the inversion is the finding, not an error. Width: $63.23 to $63.70 with the beside case, about one to one.
- **The floor is tested first** (2026-10-10). At $92.02 the market value of the shares less the holding-company cash is
  $6,454.9M. The no-growth case returns **3.62%** a year on it; the growth case's internal rate of return at the price is
  **4.06%**; every other beside case is lower. **No case in the range earns the floor of about ten percent at the
  price**, and the price sits above the top of every case: "So, there’s just a point at which we drop out of the game"
  **[M2003-149]**. The width test does not arise.
- **Fair price (a reporting figure, never a verdict; Part VII):** each end case valued with its own cash at ten percent
  instead of the sovereign, the two averaged, per share, after the company's own tax. The central range has one end (by
  (b)): $233.8M / 10% = $2,338.1M + $211.6M = **$35.19 a share, equity-only, the central basis for a regulated
  utility**. With the beside growth case as a second end ($1,485.2M at 10%), the average is **$29.31**. **All-equity,
  beside: $2.98** on the no-growth case alone, **-$11.22** with the growth case (not positive). No cheap price is
  reported.
- **VERDICT: OUT.** Valued, and the price does not clear the floor on any case: the expected return at $92.02 is about
  3.6% to 4.1% a year against a floor of about ten percent and a long bond at 5.31%. "there’s no way we get rich on our
  utility investments" **[M2009-104]**; at this price the owner would not earn the bond.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9: COULD IT RUIN US? WEIGHING.
NOT REACHED.

## Q10: IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7**: valued (equity-only, the regulated-utility basis) at **$63.70 a share** on the central range (no-growth
alone, by specific (b)), $63.23 with the growth case beside, against **$92.02**; no case earns the floor of about ten
percent at the price (3.6% to 4.1%). Fair price $35.19 equity-only ($29.31 with the growth case beside; all-equity $2.98
and -$11.22). Q1 IN, Q2 IN (regulated return carried to Q3), Q3 weighs against, Q4 weighs against (not a STOP), Q5
integrity IN with ability weighing against, Q6 weighs against.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; the box is unchanged (operator rule 2) **[M1997-127]**.
- **Q8 (the bond):** the 30-year Treasury yields 5.31% (2026-10-26); owner cash after maintenance is 3.62% of the
  market value of the shares less the holding-company cash at $92.02 (Q7).
- **Q9 (debt and exposures):** long-term debt $3,409.9M plus $100.0M current at 2026-06-30, all at the utility; the
  holding company has none (10-Q). "$1.5 billion of long-term debt maturing" in 2026 to 2030, including "$75.0 million 8%
  senior unsecured debenture due in 2026" (Item 7). 2025 utility pre-tax income $353.1M plus interest $181.7M covered
  interest 2.94 times (the pre-tax measure, not EBITDA). Unsecured ratings "investment grade" at Moody's, S&P and Fitch
  (Item 7). The $6.3B construction plan for 2026 to 2030 is about 60% internally funded with dividends, so roughly
  $2.5B must come from debt, parent equity and the remaining Centuri proceeds (Item 7; my arithmetic, not the filing's).
  The Great Basin expansion alone is "approximately $1.7 billion" over three years and "could increase" by "$0.6
  billion" (10-Q), against utility equity of $3,848.9M at 2026-06-30. Purchased-gas swings are financed by a $400M
  credit facility; the 2021 to 2023 under-collection reached $552.9M (Q4). Pension plan discount rate 5.75% (Item 7).
  Company-owned life insurance cash value $165.6M moves earnings with markets (Item 1A, Note 1).
- **Q10:** nothing found beyond the above.
- **Q12:** a gas distributor; no business named in Q12's list. The filing reports greenhouse-gas obligations under
  California's Cap-and-Invest programme (Item 1).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 407a2b85, before the first `tools/run.py` call); written
      question by question. **Departure:** Q1, Q2, Q3, Q4 and Q7 each had their own commit; Q5 and Q6 were written in
      one sitting and committed together (commit 3d299de6), and the box, the after-the-stop facts and this audit go in
      the closing commit.
- [x] Dispatched: the brief allowed per-question pathspec commits of my two paths only, and states that the dispatching
      session holds the lock and folds the run. I committed nothing else and did not push.
- [x] Blind rule: no other run file, holding review, `PORTFOLIO.md`, resume-state file, the run queue or the prepped
      reading list was opened or searched. **Declared under contamination** (top of file): a `ls "Test Runs" | grep SWX`
      run to confirm my own file name showed the names of a 2026-10-18 SWX run file and research folder, not opened;
      commit subjects in the session context named another gas utility's re-run, not opened, and that company was not
      used as a peer.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row (checked
      by `check_ids.py` in the research folder, final result below); no E-ids. Every filing fact carries its document
      and accession; the 2021 acquisition payment and Holdings' issuance, dividends and net income are XBRL
      transcriptions from the 10-Ks named, flagged as such.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 NOT REACHED; nothing after Q7 is a
      clearance.
- [x] Owner cash after every real cost from operating cash, stock pay and capital spending, never a net-income proxy
      (operator rule 5); the sovereign from the US Treasury; the price and year-end closes are aggregator quotes,
      flagged.
- [x] Contrary evidence written down as found (Foundations, and at each question); facts for later questions under
      AFTER THE STOP. Integrity facts were judged at Q5 (it was reached), so no flag is needed in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used; its owner-earnings lines (consolidated with Centuri) and
      its "d1" debt line (a tag that includes equity) were read and not used, said so in Step 0.
- [x] `python tools/check_framework.py` run before the closing commit (result below).
- **Weak points I know of:** the maintenance guess is the depreciation charge, with no filing split; the holding-company
  cost is my figure ($6.0M a year); the rate-base weights for the debt-credit cap are operating-margin shares; Atmos is
  a peer of my choosing; Northwest Pipeline's 2024 and 2025 figures were not read (they sit in Williams' combined 10-K);
  the 2016 and 2017 utility purchased-gas balances were not extracted; the prior 10-K's 2021 exhibit (purchase prices
  of the 2021 acquisitions) was not read, so the 2021 purchase price is the XBRL total of $2,354.3M for both deals.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Specific (b) and pass-through cash.** A gas distributor's operating cash swings by hundreds of millions with gas
costs it passes through at no margin (2021 -$343.7M, 2024 +$715.0M here). Owner cash "as Q4 recasts it" then changes
sign, and (b) sends the range to the no-growth case alone, although customers, plant and operating margin grew in every
year of the window. The text does not say whether the series that measures growth may exclude pass-through working
capital the way (a) lets a cycle set the base. I applied (b) as written and showed the growth case on the series before
working capital beside it; both close OUT, but a utility nearer the line would turn on this. (2) **Specific (f) at the
discount rate.** Cutting the absurd rate to the sales growth "never above the discount rate" leaves a utility whose
sales grow faster than the long bond with growth carried exactly at the discount rate, at which growth is worth nothing
by construction and the growth case, once its spending is charged, always falls below the no-growth case. That may be
intended (growth bought at the bond rate is worth no more than it costs); the text does not say so. (3) **The debt-credit
cap** asks for allowed shares "weighted by rate base"; this filing states allowed structures by state but no rate base
by state, and the text gives no stand-in. I used operating-margin shares and called it a convention. (4) **The
maintenance guess** for a utility: much of the spending replaces old pipe under safety programmes and earns a return
like growth spending; the line between "to stand still" and "to grow" that (e) and the debt credit both rest on is not
drawn by the filing, and depreciation was used. (5) **Holding-company cash** under the equity-only utility basis: the
text says what is added for net debt on the all-equity basis but not whether a holding company's own cash is added on
the equity-only basis; I added it ($2.92 a share). (6) **Q2's regulated-return exception** carries "a return set by a
regulator" to Q3; it does not say what to do with a company that has earned well below its allowed return in every year
of the span, which is closer to the "ordinary returns" OUT than to a set return. I carried it to Q3 as written. (7)
**The template's Q7 line** asks for the growth spending in year one and year ten and the utility credit even where, as
here, the central range is the no-growth case alone; I reported them for the beside case.
