# Company Run — ONE Gas, Inc. (NYSE, NYSE Texas: OGS) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch. Dispatched blind run under the canonical brief
`Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure (lines of evidence and comparators derived by the
analyst from the 10-K). Every judgment cites a v5 ledger id in bold; every filing fact carries its accession.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (04279b52): `PORTFOLIO.md` read for this one ticker; the operator does not hold OGS (no line names OGS, ONE Gas or Oklahoma Natural Gas).*

**Contamination, declared and not used.** (1) The session context showed the repository's recent commit subjects, which
describe a v5 run of another gas distributor (Northwest Natural, NWN) that closed TOO HARD (NATURE) at Q2 on state climate
policy, with its computation figures. That run was not opened. It is a different company in different states; nothing of its
reasoning or figures is used here, and when the 10-K's peer group named Northwest Natural among comparators I chose others
(Q2) so as not to lean on it. (2) The session context also carried a memory index line on the queue state (wave 7, holding
reviews owed, a count of gate-clearers); none of it names this company. (3) **A slip of my own:** before copying the template,
I ran a directory listing of `Test Runs/` filtered for "OGS|ONE Gas" to check that the dated file name was free. The blind
rule forbids listing `Test Runs/` for this company's files. It returned no file at all; nothing was opened or read. Declared
here and in the self-audit.

**Lines of evidence chosen (the brief's departure), and from which items of the FY2025 10-K
(accession 0001587732-26-000009):**
1. *The regulatory compact* (Item 1, Regulatory Overview; Item 7, Regulatory Activities): authorized returns, rate base, the
   interim mechanisms (PBRC, GSRS, GRIP), regulatory lag, Texas House Bill 4384.
2. *The substitute, not the rival* (Item 1, Competition; Item 1A, climate and environmental legislation; Item 7,
   forward-looking factors): gas against electricity at the point of installation; customer counts and new connections.
3. *The capital the business consumes* (Item 7, capital expenditures, liquidity, equity issuance): capex against depreciation,
   the equity raised each year, the 2026 capital plan and its split.
4. *The one-time event* (Item 1A, gas price spikes; Note 17 and Item 7 on securitization): Winter Storm Uri, its costs and
   their recovery, which deform the cash-flow window.
5. *The debt and the liquidity* (Item 1A, access to capital; Item 7, Liquidity): commercial paper, the term loan, covenants,
   ratings.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $75.60 (close 2026-10-16, the last close before this Sunday run date; Yahoo chart via `tools/run.py`;
  **aggregator, flagged per operator rule 5, live quote only**). Cross-check of the aggregator's history against a filing:
  the proxy (DEF 14A, 2026-04-01, accession 0001193125-26-137922) states "$77.25 per share on December 31, 2025"; the
  aggregator's 2025-12-31 close is $77.25.
- **Shares by class:** one class, common stock, par $0.01. Cover of the 10-Q for the quarter ended 2026-06-30 (filed
  2026-08-05, accession 0001587732-26-000035): **62,856,270 shares** as of 2026-07-24 (`python Screens/cover_shares.py OGS`).
  Check: the 10-Q balance sheet shows 62,797,154 shares "issued and outstanding" at 2026-06-30 and no treasury line (issued
  equals outstanding); the 59,116 difference is consistent with the at-the-market and plan issuance the 10-Q describes.
  **After the last 10-Q:** the 424B5 of 2026-08-12 (accession 0001193125-26-347036) and the 8-K of 2026-08-13 (accession
  0001193125-26-349155) are a debt issue ($375 million of 5.45% notes due 2036, proceeds to repay the $250 million term loan
  and commercial paper), not an equity issue. Unsettled forward sales of 506,607 shares (net proceeds about $41.5 million) are
  outstanding under the 10-Q's table; they are left out of the count and named here.
- **Market cap:** 62.856 million × $75.60 = **$4,751.9M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-16
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-19, accession 0001587732-26-000009), Items 1, 1A, 5, 7, the
  four statements and Notes on debt, securitization and legal matters; 10-Q Q2 2026 (filed 2026-08-05, accession
  0001587732-26-000035), balance sheet, equity program; proxy DEF 14A (filed 2026-04-01, accession 0001193125-26-137922),
  pay tables, STI and PSU design, ownership; 8-Ks of 2025-12-18 (0001587732-25-000064, the WFEC pipeline), 2025-12-29
  (0001193125-25-335291, forward settlements), 2026-02-18 (0001587732-26-000006, results and 2026 guidance), 2026-07-13
  (0001193125-26-302034, a director added), 2026-08-04 (0001587732-26-000033, results, guidance raised), 2026-08-13
  (0001193125-26-349155, notes); 424B5 of 2026-08-12 (capitalization table at 2026-06-30). For the cycle: 10-K FY2022
  (0001587732-23-000015), 10-K FY2021 (0001587732-22-000019), 10-K FY2019 (0001587732-20-000017), 10-K FY2016
  (0001587732-17-000011), cash-flow statements and balance sheets.
- **One figure cross-checked against the filed statement:** cash provided by operating activities FY2025, $578,833 thousand on
  the filed cash-flow statement of the 10-K; `tools/run.py`'s XBRL series carries $578.8M for 2025. Also capital expenditures
  FY2025, $707,226 thousand filed; XBRL $707.2M.
- **`python tools/run.py OGS`, arithmetic lines only:** its owner-earnings window stops at 2023 (it found D&A tagged only as
  intangible amortization, a warning it prints) and its 2022 and 2023 operating cash includes the Oklahoma securitization
  proceeds ($1,331M and $197M, "ogs:ProceedsFromSecuritizationBondsOperatingActivities"). Its owner-earnings lines are
  therefore not used; the owner cash below is built from the filed statements (Q4, Q7). Its ten-year balance-sheet table is
  used as transcription and checked against the filed balance sheets (Q4). SBC resolved: share-based compensation expense
  $10.5M to $14.8M a year (2021 to 2025, filed cash-flow statements), treated as a cost and not added back.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this utility "if the market closed for five years"
**[M1997-109]**, and the market's quote "just tells us prices" **[M2006-077]**. The foundation that bears hardest here is
the margin of safety as an attitude: a regulated business priced near its regulated value is the case where "if you have to
actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**. No macro forecast enters: no view
on gas prices or rates is taken; "macro conclusions are — just never enter into the discussion" **[M2000-094]**. Who is paid
to tell me: the company's own five-year "outlook" and its adjusted earnings figure are management's numbers, read as such
**[M2020-037]**. **Contrary evidence, written down as found** **[M1997-127]**: (a) the business has needed new equity every
year since 2020 (equity issued $19.4M in 2020 rising to $252.4M in 2024 and $212.2M in 2025, filed cash-flow statements);
(b) its own risk factors name electricity as the substitute chosen "at initial installation" and climate legislation that
could "impose costs or restrictions on end users of natural gas" (10-K Item 1 and 1A); (c) from February 2026 the company
features an adjusted net income figure and guides on it (8-K 2026-02-18, accession 0001587732-26-000006). Each is carried to
the question it bears on. Scuttlebutt is not available to a blind run; its purpose, "to possibly reject your original
hypothesis" **[M1998-144]**, is served by the competitors' filings at Q2.

## THE STANDING RULE
The buyer's conduct, not the target's: nothing in this run proposes borrowed money or a size that could ruin the buyer;
"borrowed money has no place in the investor's tool kit" **[L2014-005]**, and the rule is "Never risk permanent loss of
capital" **[L2023-005]**. No position is taken in a run. Passes as a statement of conduct.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as written:** understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.
- **What the business is (10-K Item 1 and Item 7, accession 0001587732-26-000009):** "a 100-percent regulated natural gas
  distribution utility" with "approximately 2.3 million customers" in Oklahoma, Kansas and Texas; one reportable segment.
  Revenue is set by regulators "based on the revenue requirements needed to achieve our authorized rates of return"; the gas
  itself is passed through "at cost" and "operating income is not affected by fluctuations in the cost of natural gas" (Item 7
  and 7A). Fixed charges were about 91, 52 and 66 percent of sales revenue less gas cost in Oklahoma, Kansas and Texas in
  2025 (Item 1).
- **The key variables, and how predictable** **[M1998-044]**: (1) rate base, which grows with capital spent and approved
  (Oklahoma $2,453M, Kansas $1,468M, Texas $1,887M, Item 1 table); (2) the allowed return, ROE 9.40%, 9.60% and 9.80% with
  equity ratios of 59% and 60% where stated (Item 1 table, actions of June 2025, August 2025 and January 2026); (3) regulatory
  lag, narrowed by PBRC, GSRS, GRIP and Texas House Bill 4384 (Item 1, Item 7); (4) customer count, 2,295 thousand average in
  2025 against 2,281 thousand in 2024, with "23,000 new customer connections in each year" (Item 7); (5) the long-run use of
  gas for heating against electricity (Item 1, Competition). The first four are written down by the company and its regulators
  years ahead: an Oklahoma rate case is required "on or before June 30, 2027" (Item 1), and the company states a capital plan
  of "approximately $800 million in 2026" (8-K 2026-02-18). The insiders would write the ten-year forecast down
  **[M2000-105]**; utilities' own financial statements tell what the next ones will look like **[M2008-033]**. The speakers
  call such utilities "pass-through organizations" that "need to be operated efficiently in order to achieve their rate of
  return" **[M2012-013]**, and of an allowed return, "you’re almost certain of earning it, I mean, if you behave yourself"
  **[M2010-037]** (said of the electric utility; the gas distributor's compact in the filing is the same in form).
- **The fifth variable** is the one that is hard: whether gas heat holds against electricity in these three states over ten
  to twenty years. It is a question about customers and policy, not technology that changes fast; Q1's routing sends a fast-
  changing industry to TOO HARD here, and this is not that: the filings show slow, measurable data (customer counts, new
  connections, the states' own legislation). Rapid change is owned by Q2, and the durability question is taken there.
- **Doubt about the perimeter** **[M2002-092]**: I have none about how the economics work; the doubt is about the castle's
  future, which is Q2's question.
- **VERDICT: IN.** A regulated gas distributor whose earnings are rate base times an allowed return; its key variables are
  stated in its filings and its regulators' orders **[M2012-065]**, **[M1998-044]**, **[M2012-013]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now" **[M1995-038]**. Filing facts from the 10-K FY2025 (accession 0001587732-26-000009) unless stated.

- **The attacker with money.** The castle is a franchise network: 43,200 miles of distribution main and 2,200 of transmission
  (Item 2), serving "approximately 89 percent, 72 percent, and 13 percent of the natural gas distribution customers in
  Oklahoma, Kansas, and Texas" (Item 1). A rival with money would have to lay a second network under the same streets and win
  a franchise to do it; the test is the See's question, "could I do it? And I came to the conclusion, no" **[M2011-015]**, and
  the railroad's: "You really couldn’t create another railroad" **[M2013-054]**. The 10-K names one place it is not exclusive:
  "In Texas, we are also subject to competition from other local distribution companies" (Item 1), and large industrial
  customers near "a competitive pipeline" may get "Reduced-rate transportation service" (Item 1). The money test passes for
  the residential and commercial core.
- **Pricing power and the agony before a rise.** The company has no pricing power of its own: every rate is set in a filed
  proceeding, the speakers' "prayer session before you raise your prices a penny" written into law **[M2005-020]**. The
  record of the prayers, 2025 (Item 7): Oklahoma asked $41.5 million and settled at $41.1 million; Texas asked $41.1 million
  on a 10.4% ROE and received a $14.5 million increase (the administrative law judge's recommendation, adopted) on a 9.8% ROE;
  Kansas asked $7.2 million and received it. New rates added $116.0 million to 2025 operating income. The return is what the
  regulator allows, not what the castle could charge: "The whole idea behind the utility industry is not to allow
  extraordinary profits" **[M2000-131]**.
- **Unit volume and share of mind; the low bid.** The customer cannot buy gas delivery from a rival in most of the territory,
  so the low-bid test is put against the substitute: "Significant energy usage competition occurs between natural gas and
  electricity in the residential and small commercial markets. Customers and builders typically make the decision on the type
  of equipment, and therefore the energy source, at initial installation" (Item 1). The evidence of the choice is the customer
  count: average customers 2,295 thousand in 2025 against 2,281 thousand in 2024, net growth in all three states, with 23,000
  new connections in each of 2024 and 2025 (Item 7); 2026 plans $230 million for "extensions to new customers" (8-K
  2026-02-18, accession 0001587732-26-000006); and a new 43-mile pipeline for an electric cooperative's gas-fired plant, about
  $120 million of ONE Gas investment, to be completed by the third quarter of 2028 (8-K 2025-12-18, accession
  0001587732-25-000064). Volumes are weather driven and flat: sales volumes 157,330 MMcf in 2025 against 156,606 in 2023;
  transportation volumes 216,955 against 227,875 (Item 7). Builders in these states still choose gas on the filed evidence.
- **The low-cost position.** A distributor is not a commodity seller; the gas is passed through at cost. The relevant cost is
  the delivered cost of heat against electricity, which no filing read states. Recorded as a gap, not filled.
- **Ask the competitors.** The 10-K names no rival company. Its competitors are electricity in general and, in Texas, "other
  local distribution companies", unnamed. **CONVENTION of this run:** the comparators are Atmos Energy (ATO) and Spire (SR),
  both in the 10-K's own Item 5 peer group and both predominantly regulated gas distributors that file with the SEC;
  rationale: without a named rival, the castle question for a regulated distributor is answered by what its regulated peers
  earn over the same span. (Northwest Natural is in the same peer group and was not chosen; see the contamination note.)
- **Widening or narrowing** **[M1999-108]**. Widening on the regulatory side: Texas House Bill 4384, signed June 2025,
  "allowing gas utilities in Texas to defer, and later recover, specific costs related to property, plant and equipment placed
  in service, but not yet reflected in base rates" (Item 7); the Texas service areas consolidated into one statewide division
  effective January 2026; trackers for pensions and ad-valorem taxes; weather normalization in all service areas (Item 1).
  Narrowing: Texas granted about a third of what was asked in 2025, and Oklahoma's PBRC filings were required "for each of the
  years 2021 through 2025", after which a full rate case is due by June 30, 2027 (Item 1); the mechanism's renewal is not
  stated.
- **What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**. (1) *Policy against gas in
  buildings.* The 10-K's risk factor is general: "Various states and municipalities have adopted or are considering adopting
  legislation" on greenhouse gases, which "could also incentivize alternative energy sources, impose costs or restrictions on
  end users of natural gas" (Item 1A); it names no such measure adopted in Oklahoma, Kansas or Texas, and the one state law it
  describes (House Bill 4384) runs the other way. The speakers name this kind of threat to utilities: "the regulatory climate
  in a few states has raised the specter of zero profitability" **[L2023-011]**, and of their own loss, "It was an
  extrapolation of a societal trend" **[M2025-045]**; regulators are less inclined to let a stranded asset into rate base for
  "rank foolishness" than "where societal demands are just changing" **[M2017-094]**. (2) *The regulators themselves*:
  "railroads, utilities, insurance companies, are all very much affected by the political process" **[M2012-074]**. (3) *One
  event*: in February 2021 Winter Storm Uri produced extraordinary gas costs that the company carried as a regulatory asset
  (current and noncurrent regulatory assets and liabilities moved by $1,929.8 million on the 2021 cash-flow statement, 10-K
  FY2022, accession 0001587732-23-000015) and recovered through state securitizations: $1,330.6 million in 2022 and $197.4
  million in 2023 of Oklahoma proceeds inside operating cash, and $335.9 million of Kansas bonds, which are non-recourse to ONE
  Gas (10-K FY2022 cash-flow statement; 10-K FY2025, Note 17). The castle held through it because the regulators allowed
  recovery. (4) *Slow change*: "slow change can be much harder to perceive, and can lull you to sleep easier" **[M2014-038]**.
  The filed evidence on (1) is that customers are still being added and a gas-fired power customer has just been contracted;
  on (2), the ROEs renewed in 2025 and 2026 in all three states.
- **The parts table.** One reportable segment (Item 7). The three divisions have the same economics (a franchise under a state
  regulator) and are read together; by rate base, Oklahoma 42%, Texas 32%, Kansas 25% of $5,808 million (Item 1 table).
- **The competitor row** (return on average equity: net income over the average of opening and closing stockholders' equity,
  from each filer's XBRL company facts, first-filed values; the last year checked to the latest 10-K):

| fiscal year | ONE Gas (Dec) | Atmos Energy (Sep) | Spire (Sep) |
|---|---|---|---|
| 2016 | 7.5% | 10.5% | 8.6% |
| 2017 | 8.5% | 10.8% | 8.6% |
| 2018 | 8.6% | 13.9% (tax-reform year) | 10.1% |
| 2019 | 9.0% | 9.7% | 7.7% |
| 2020 | 9.0% | 9.6% | 3.5% |
| 2021 | 9.0% | 9.1% | 10.5% |
| 2022 | 9.0% | 8.9% | 8.1% |
| 2023 | 8.6% | 8.7% | 7.6% |
| 2024 | 7.6% | 9.1% | 8.2% |
| 2025 | 8.1% | 9.3% | 8.2% |
| ten-year average | 8.5% | 10.0% | 8.1% |
| capex over D&A, last year | 2.2x | 4.8x | 3.1x |

  Sources: ONE Gas 10-K FY2025 (0001587732-26-000009; net income $264.2M, equity $3,440.1M and $3,104.5M); Atmos 10-K FY2025
  (0000731802-25-000056; net income $1,198.8M; capital spending $3,561M, D&A $734.7M); Spire 10-K FY2025
  (0001193125-25-282583; net income $271.7M; capex $922.4M, D&A $298.2M). Earlier years from the same filers' 10-Ks via the
  XBRL company facts, transcription (`Test Runs/_research 2026-10-18 OGS/comp.py`).
- **The field's returns over the last full cycle, judged in words:** the three regulated gas distributors earned high single
  digits on book equity in every year of the decade except Spire's 2020, with ONE Gas in the middle and steady (7.5% to
  9.0%). These are ordinary returns, ordinary because a regulator sets them. The framework's list of what Q2 rules OUT
  names this as its exception (a return set by a regulator is carried to Q3 as a second best). The speakers on the field: "the industry offers owners the opportunity to deploy large sums at fair
  returns" **[L2005-005]**; "there’s no way we get rich on our utility investments. But there’s no way we get poor, either"
  **[M2009-104]**.
- **Judgment.** The castle stands because a rival cannot rebuild it and because the three state compacts were renewed in 2025
  and 2026 at 9.4% to 9.8% on equity; it is kept standing by builders still choosing gas in these states and by regulators
  still allowing recovery, including of a two-billion-dollar storm. What could take it down is a change in what those states
  want, which the filings show moving, if anything, toward gas (House Bill 4384, the WFEC pipeline), and which would come
  slowly **[M2014-038]**. The bet is the one the speakers describe for their own utilities: "the bet we are making is that
  regulatory authorities will treat us fairly in the future" **[M2014-087]**. I judge the castle standing for the regulated
  return, no more: not shown open, and its future judgeable on the filings for what the castle protects, a fair return on rate
  base, not an excellent one **[L2007-004]**.
- **VERDICT: IN**, as the regulated exception: a franchise castle standing on the filings, protecting a fair, regulator-set
  return, carried to Q3 as a second-best business (**[M2011-015]**, **[M2013-054]**, **[M2009-104]**, **[L2009-012]**). The
  policy threat to gas in buildings is the strongest contrary evidence and is carried forward.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
The speakers' question: "does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**.
The test the brief fixes for a capital test is the one the speakers use for their own utilities: "the return is not measured by
the cash minus the increased capital investment we’re making. It’s measured by the operating earnings after depreciation"
**[M2014-086]**, set against the capital employed.

- **Return on the capital actually needed.** After-tax operating earnings before interest (net income plus interest expense
  after the company's effective tax rate) against capital employed (equity plus debt less cash, less goodwill; the Kansas
  securitization bonds left out with their charges, see Q7):

| | 2016 | 2025 | change |
|---|---|---|---|
| net income | $140.1M | $264.2M | |
| interest expense, after the year's effective tax rate | $43.7M × (1 − 37.8%) = $27.2M | $142.8M × (1 − 17.8%) = $117.4M | |
| after-tax operating earnings | $167.3M | $381.6M | +$214.3M |
| capital employed | $1,888.3M equity + $1,337M debt − $14.7M cash − $158.0M goodwill = $3,052.6M | $3,440.1M + $3,120.1M − $10.6M − $158.0M = $6,391.6M | +$3,339.0M |
| return | 5.5% | 6.0% | 6.4% on the added capital |

  Sources: 10-K FY2016 (0001587732-17-000011) and 10-K FY2025 (0001587732-26-000009), statements of income, balance sheets;
  2016 debt as long-term debt $1,192M plus commercial paper $145M (`tools/run.py` transcription of the filed balance sheet);
  2025 debt $2,133.0M other long-term debt plus $249.7M current maturities plus $737.4M notes payable. On book equity the
  return is 7.5% to 9.0% a year (Q2 table).
- **Reinvestment to stand still and to grow.** Capital expenditures were $309.1M against D&A of $143.8M in 2016 and $707.2M
  against $317.3M in 2025, about 2.1 to 2.2 times depreciation throughout, plus asset removal costs of $47M to $62M a year
  inside operating cash (filed cash-flow statements 2014 to 2025). The 2026 plan is "approximately $800 million", of which
  "approximately $230 million" is for extensions to new customers and the rest "primarily targeted for system integrity and
  replacement projects" (8-K 2026-02-18, accession 0001587732-26-000006). The replacement spending is compulsory in the sense
  that the safety rules require it, and it is also what the regulator lets the company earn on: it raises rate base. This is
  the utility case the speakers describe: "To earn more, their owners must invest more" **[L2011-019]**; "you have to keep
  putting more and more money into a public utility. And you’d better hope that the rate of return allowed is commensurate"
  **[M2005-052]**; "we have forced capital investment to essentially keep in the same place" **[M2022-050]**.
- **Whose money.** Operating cash has not covered capital spending and dividends: equity issued was $744.1M from 2017 to 2025
  (filed cash-flow statements, "Issuance of common stock"), against $748.0M of earnings retained over the same years (net
  income $1,864.6M less dividends paid $1,116.6M); total debt (ex the Kansas securitization bonds) rose from about $1.34
  billion at the end of 2016 to $3.12 billion at the end of 2025. Rising earnings alone prove nothing: "we’re not earning a
  higher rate of return on capital than we were when we started. We just put way more capital into the business"
  **[M2023-081]**, which describes this record (6.0% in 2025 against 5.5% in 2016 on capital doubled).
- **The growth arithmetic.** Operating income rose from $310.3M (2021) to $457.5M (2025), 10.2% a year, net income 6.4% a
  year, on capital that rose about as fast. Growth here is the second grade of the 1998 passage at best, "It takes more money,
  but the rate at which you invest — reinvest — the money to get that growth is a very satisfactory rate" **[M1998-081]**,
  and whether 6.4% after tax on all capital is "very satisfactory" depends on what it is set against: it is above the 5.43%
  bond, and below the floor of Q7. The speakers accept such businesses as a second best: "as the second-best choice, still a
  good choice, the answer is yes. It’s not as good as the best choice" **[M2018-055]**; "they’re good enough" **[M2018-056]**,
  on the condition of "decent returns on the incremental sums they invest" **[L2009-012]**; but "cash-consuming businesses,
  by their nature, are unattractive unless the cash they consume gets to earn a reasonable return" **[M2012-057]**, and a
  utility's return is "in effect, a bond-like return" **[M2011-054]**.
- **WEIGHS AGAINST**, admitted as a second best: the business consumes more capital than it earns, raises equity every year,
  and earns about 6% after tax on all its capital and 6.4% on the capital added, a bond-like return a little above the
  government rate **[L2011-019]**, **[M2012-057]**, **[M2011-054]**; it is not barred, since the rows admit regulated returns
  as "good enough" **[M2018-056]**, **[L2009-012]**. The "little or no debt" criterion is applied at Q9.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten year-ends, before the income account** **[M2025-032]** ($ millions; `tools/run.py`
  transcription of first-filed XBRL, accessions 0001587732-17-000011 through 0001587732-26-000009; checked against the filed
  balance sheets for 2016, 2024 and 2025):

| year-end | total assets | equity | cash | receivables | goodwill | long-term debt (non-current) | notes payable | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2016 | 4,943 | 1,888 | 15 | 291 | 158 | 1,192 | 145 | 161 |
| 2017 | 5,207 | 1,960 | 14 | 299 | 158 | 1,193 | 357 | 246 |
| 2018 | 5,469 | 2,043 | 21 | 295 | 158 | 1,285 | 300 | 321 |
| 2019 | 5,708 | 2,129 | 18 | 260 | 158 | 1,286 | 516 | 403 |
| 2020 | 6,029 | 2,233 | 8 | 293 | 158 | 1,582 | 418 | 484 |
| 2021 | 8,402 | 2,350 | 9 | 342 | 158 | 3,683 | 494 | 565 |
| 2022 | 7,776 | 2,584 | 10 | 554 | 158 | 2,662 | 552 | 652 |
| 2023 | 7,771 | 2,766 | 19 | 348 | 158 | 2,160 | 88 | 738 |
| 2024 | 8,426 | 3,105 | 58 | 408 | 158 | 2,385 | 915 | 810 |
| 2025 | 8,853 | 3,440 | 11 | 462 | 158 | 2,356 | 737 | 909 |

  **What moved and why.** Equity rose $1,552M in nine years: $748M from retained earnings and about $800M of paid-in capital
  from share issuance (paid-in capital $2,530.1M at 2025). Goodwill is unchanged at $158M from the separation: no acquisitions.
  Receivables moved with gas prices, not with credit (20% of revenue in 2016, 19% in 2025; the 2022 peak was the year of high
  gas prices). Cash is held near zero; the business runs on commercial paper ($737.4M at 2025, $770.8M at 2026-06-30). The
  2021 spike in long-term debt ($3,683M) was Winter Storm Uri: $2.5 billion of notes issued in 2021, $1,627M repaid in 2022 and
  $773M in 2024 as the securitization proceeds came in (10-K FY2022 and FY2025 cash-flow statements). Debt other than the
  Kansas securitization bonds roughly doubled while the network grew (net property $7,122.2M at 2025). Deferred income taxes
  ($963.9M) and regulatory liabilities ($508.9M, including the excess deferred taxes owed back to customers) are large and are
  liabilities to the regulatory process, not hidden equity: "I don’t think I would look at that as a hidden form of equity"
  **[M2015-030]**. **What the figures do not say:** whether the $305.7M of regulatory assets and the plant in service awaiting
  rates will be allowed; that is a regulatory judgment, read at Q2.
- **The real costs.** Depreciation ($317.3M in 2025) is a true cost **[R1996-023]**, and here it falls short of what keeps the
  network in place: replacement spending runs above it (Q3), the case where "your depreciation charges are inadequate"
  **[M2015-049]** and where one "should also subtract something" **[L2015-004]**; the owner cash in Q7 therefore deducts
  capital spending, not depreciation, with depreciation shown only as a variant. Stock pay is expensed ($14.8M, 2025) and is
  not added back. Asset removal costs ($52.3M, 2025) are inside operating cash and stay deducted. The income tax line is
  lowered by credits for excess deferred taxes ($17.6M in 2025, $25.7M in 2024), which the 10-K says are matched by credits in
  customers' rates (Item 7, EDIT). No restructuring charges, no recurring "one-time" items, and no EBITDA in the filer's own
  mouth: a text search of the 10-K, the proxy and the two earnings releases read found the word nowhere.
- **The habits, recorded here and carried to Q5.** (1) *An adjusted figure featured.* From February 2026 the company reports
  "adjusted net income", GAAP net income plus "the deferral of an equity portion of a carrying cost" on plant placed in service
  but not yet in rates, a non-cash and non-taxable addition of $6.7M in 2025 (2.6% of net income), reconciled to GAAP (10-K
  Item 7; 8-K 2026-02-18). The August 2026 release leads with it: "Raises 2026 Adjusted Earnings Expectations" (8-K
  2026-08-04, accession 0001587732-26-000033). The rows: a management that "regularly attempts to wave away very real costs by
  highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**; this adjustment adds a non-cash income rather
  than waving away a cost, and is small, but it is featured. (2) *Guidance.* The company guides on the adjusted figure ($306M to
  $314M, $4.83 to $4.95 a share for 2026) and states "long-term adjusted net income growth of 7 to 9 percent and adjusted net
  income per diluted share growth of 5 to 7 percent" (8-K 2026-02-18); the rows call it "the scourge of earnings "guidance""
  **[L2019-006]**. Both weigh against at Q4 **[M1994-018]** and are judged at Q5.
- **Suspicion or confusion?** None found. The statements are plain: one segment, the gas cost passed through and shown, the
  storm's costs and recoveries visible line by line, the securitization subsidiary's debt stated as non-recourse. "when the
  accounting confuses you, I would just tend to forget about it" **[M1995-063]** does not apply.
- **VERDICT on the accounts: WEIGHS FOR** (clear, conservative, explained in plain terms, the plus of **[M1994-018]**); the
  featured adjusted figure and the guidance **WEIGH AGAINST** and are carried to Q5 **[L2016-006]**, **[L2019-006]**. Recast
  earnings for Q7: owner cash after all capital spending and asset removal, stock pay as a cost, the Uri flows taken out as
  aberrational, the Kansas securitization stream and its bonds left out together.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stake the speakers read rather than meet; the two yardsticks are "how well they run the business" against
"the hand they were dealt", and "how well that they treat their owners" **[M1994-008]**, read in the proxy: "see how they
treat themselves versus how they treat the shareholders" **[M1994-009]**.

- **The people (10-K Item 1, executive officers).** Robert S. McAnnally, President and CEO since 2021, COO 2020 to 2021;
  Christopher P. Sighinolfi, CFO since 2024; Curtis L. Dinan, COO since 2021. Board led by a non-executive Chair, John W.
  Gibson, retiring at the 2026 meeting, with a lead independent director (proxy, accession 0001193125-26-137922); the CEO does
  not chair, so the difficulty of replacing "a mediocre CEO if that person is also Chairman" **[L2014-026]** does not arise. A
  ninth director, a former PG&E chief operating officer, was added on 2026-07-13 (8-K, accession 0001193125-26-302034).
- **The record against the hand dealt.** The hand is a regulated franchise; the play is to earn the allowed return and keep
  the regulators' trust. Return on equity held between 7.5% and 9.0% for ten years, beside Atmos and Spire (Q2); the 2021
  storm's costs of about $2 billion were carried, financed and recovered through two state securitizations with no write-off
  found in the statements read (Q2, Q4); ratings A3 and A- stable (10-K Item 7); safety measures reported in the top quartile
  of similar distributors (10-K Item 1, TRIR 1.27 in 2025). Regulators remember conduct: "There is no hiding your history when
  you stand before these regulators" **[L2008-008]**; the record read is of a company the three states keep granting
  mechanisms to.
- **The proxy: how they treat themselves.** CEO 2025 total direct pay $5,175,000 (salary $925,000, STI $1,300,000, LTI grant
  $2,950,000); Summary Compensation Table total $5,575,027; pay ratio 45 to 1. The annual incentive is paid on **GAAP** EPS
  (threshold $3.94, target $4.26, actual $4.37), with emissions and safety measures, not on the adjusted figure; the long-term
  award is performance units on total shareholder return relative to the 12-company peer group, plus restricted units. The
  2022 units paid 50% of target on a 25th-percentile result. Clawbacks beyond the legal minimum; hedging and pledging banned;
  CEO ownership guideline six times salary; the CEO owned 59,530 shares on 2026-03-01 (proxy). Nothing here is "heads I win,
  tails you lose" **[L1994-020]**: the 2022 grant paid half when the stock lagged.
- **The habits carried from Q4, read with the integrity record** **[M2004-067]**. The adjusted figure is new (none in the FY2021
  or FY2022 10-Ks; first in February 2026), small ($6.7M on $264.2M), non-cash, reconciled line by line, and explained as a
  regulatory income the rate-setting process recognises; and the pay plan does not use it. Guidance is given annually and a
  five-year growth "outlook" is stated (8-K 2026-02-18); the rows warn that predictions "corrode CEO behavior" **[L2000-039]**
  and that one becomes "downright incredulous if they consistently reach their declared targets" **[L2002-041]**. Whether past
  guidance was always met was not tested: the earnings releases before 2026 were not read (recorded as unread). No tell of
  dishonesty was found: no reserve movements, no restatements, no obscured key figure, no stock price promoted as the goal; the
  reports describe the storm, the rate cases and their shortfalls (Texas got about a third of its ask) in plain terms, the
  candour of **[M1998-036]**.
- **Doubt?** "If you’ve got doubts, forget it." **[M2013-088]**. I have a weighing against on the habits, not a doubt about
  honesty: the adjusted figure adds a regulator-recognised income rather than removing a cost, and the incentive pay is set on
  the GAAP number, which is the opposite of the pattern the rows condemn.
- **Ability.** Weighs for, modestly: steady regulated returns, the storm handled without loss to owners on the filed record,
  better mechanisms won in all three states. The business is one where "you’re almost certain of earning it, I mean, if you
  behave yourself" **[M2010-037]**, so ability shows mainly in behaving well before the regulators.
- **VERDICT on integrity: IN** (no tell found; the habits weigh against and are recorded) **[M2013-088]**, **[M2004-067]**;
  **ability WEIGHS FOR** **[M1994-008]**, **[L2008-008]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
- **The retention test** **[R1995-009]**, **[M1998-110]**. Market value at 2016-12-31: 52,283,260 shares (10-K FY2016 balance
  sheet) × $63.96 (aggregator close, flagged) = $3,344M. At 2025-12-31: 62,692,392 shares (10-K FY2025) × $77.25 (proxy) =
  $4,843M. Increase $1,499M. Kept and raised over 2017 to 2025: earnings retained $748.0M plus equity issued $744.1M = $1,492M.
  About $1.00 of market value for each dollar kept or raised over nine years: the market leg is met with nothing to spare. The
  intrinsic-value leg is read against the Q7 range (written back below with Q7).
- **Dividends.** $2.68 a share declared for 2025, about 61% of net income ($160.7M paid on $264.2M); the stated aim is "a
  return of capital to shareholders via a dividend that we believe will be competitive with our peer group" (10-K Item 7). In
  the same year the company issued $212.2M of stock. The rows: a dividend set by a ratio or by peers "strikes us as nuts"
  **[M2000-051]**; the test is whether a dollar kept becomes more than a dollar **[M1994-061]**. Paying out $160.7M while raising
  $212.2M is a round trip through the market whose cost the holder bears; the speakers' own utility "never had a penny of
  dividends", while "other utility companies pay high dividends" **[M2019-059]**. Weighs against.
- **Buybacks.** None in the years read; the business has no funds "beyond the near-term needs of the business"; nothing to
  test. *(The Q7 range's bottom is written back below for the record.)*
- **Issuance and deals.** No acquisitions (goodwill unchanged since 2014) and no stock-paid deal: the one STOP of Part A
  **[L2009-019]** does not arise. Shares are issued every year through forward sales and an at-the-market program ($225M program
  of February 2026; forwards at $78.45 to $81.90 a share, 10-K and 10-Q), 52.3 million shares at 2016 to 62.9 million now, up
  about a fifth. The rows' warning against companies "hell-bent on issuing shares" **[L2014-015]** is carried in the framework
  as a candidate second STOP, unresolved (section VI). Here the issuance funds rate base at the equity ratio the regulators set
  (59% to 60%, Item 1 table) and is announced, priced and reconciled; it is the utility case the speakers name, "if you’re going
  to need lots of money, you probably ought to behave in a way that encourages people to give you lots of money"
  **[M2025-046]**. Value given against value got is read at Q7: issuance above per-share value transfers value to existing
  holders, issuance below it takes it from them **[R1995-010]**.
- **Part A WEIGHS AGAINST**: retention barely meets the market test, the dividend is set to match peers while new stock is
  sold, and the issuance is serial; none is a STOP (**[M1998-110]**, **[M2000-051]**, **[L2014-015]**).

### Part B: the pay, the board and the owners
- **Pay tied to what the person controls** **[M2003-019]**: partly. The annual incentive is on GAAP EPS, safety and emissions,
  which managers influence; but in a regulated utility EPS rises with rate base, that is with capital spent and approved, so
  an EPS target rewards deploying capital rather than earning more on it: "you get what you reward for" **[M2016-083]**. The
  long-term award rides on relative total shareholder return, a market measure outside a manager's control, the "lottery
  ticket" of **[L1996-018]**, softened by being relative to peers and by its demonstrated downside (the 2022 grant at 50%).
- **The process.** The committee "targets the median level of total compensation" and uses "its independent executive
  compensation consultant" (proxy, CD&A): the comparative-data method the rows call a ratchet, comp committees as "slaves to
  comparative data" **[L2005-015]**. The amounts are modest for the size of the company and the CEO's pay ratio is 45 to 1.
- **The board and the owners.** A separate Chair and a lead independent director; directors hold stock under a five-times-
  retainer guideline; the largest holder is an index manager (BlackRock, 12.80%, proxy). The owners are told the bad news
  (rate-case shortfalls, the storm) in plain terms.
- **Part B UNDECIDED**: no "heads I win, tails you lose" **[L1994-020]**, GAAP earnings in the plan, a split board; against
  that, pay tied to EPS growth and peer-relative stock returns set by peer-median benchmarking (**[M2016-083]**,
  **[L2005-015]**).

### Written back from Q7 (committed with Q7)
- **The retention test against intrinsic value:** the bottom of the Q7 range is negative per share (below), so on the run's
  computation the $1,492M kept and raised since 2016 did not become intrinsic value per share at the 5.43% rate after charging
  the capital it consumes; only the market leg (about $1.00 per $1) is met. Weighs against.
- **The buyback test:** no repurchases to test. **Issuance:** shares sold at $70 to $82 (forward prices $78.45 and $81.90)
  are sold above the run's per-share value range, so on the computation the new holders, not the old, pay for the capital the
  business consumes **[R1995-010]**; this is the computation's verdict on issuance, not on the business. Part A stays WEIGHS
  AGAINST.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, **[M1996-025]**, as a range, by the
CONVENTION construction of Q7 and its specifics. Arithmetic in `Test Runs/_research 2026-10-18 OGS/q7_compute.py` (output
`cache/q7_out.txt`); all inputs from the filed cash-flow statements (10-K FY2025, 0001587732-26-000009, for 2023 to 2025;
10-K FY2022, 0001587732-23-000015, for 2021 and 2022) and the 10-Q balance sheet at 2026-06-30 (0001587732-26-000035).

**Owner cash, the window 2021 to 2025 ($ millions):**

| | 2021 | 2022 | 2023 | 2024 | 2025 | average |
|---|---|---|---|---|---|---|
| cash before capital spending, all-equity basis | 477.3 | 334.3 | 851.5 | 493.8 | 683.9 | 568.1 |
| capex plus asset removal (all spending) | 544.3 | 656.5 | 728.7 | 762.1 | 759.5 | 690.2 |
| **owner cash after all spending, all-equity** | −67.0 | −322.2 | 122.8 | −268.3 | −75.6 | **−122.1** |
| maintenance only (71.25% of spending) | 387.8 | 467.8 | 519.2 | 543.0 | 541.1 | 491.8 |
| **owner cash after maintenance only, all-equity** | 89.5 | −133.4 | 332.3 | −49.2 | 142.7 | **76.4** |
| depreciation variant (D&A less securitization amortization) | 270.0 | 109.4 | 599.1 | 227.5 | 398.8 | 321.0 |
| owner cash after all spending, equity basis | −117.5 | −384.6 | 39.6 | −380.8 | −180.8 | −204.8 |
| owner cash after maintenance only, equity basis | 39.0 | −195.8 | 249.1 | −161.6 | 37.6 | −6.4 |

How built: operating cash as filed, less share-based compensation (a cost, not added back), less other investing net, with
these taken out as aberrational on the filer's own description **[L2005-003]** (Q7 specific (a)): the Winter Storm Uri
regulatory-asset build of 2021 ($1,929.8M added back) and the Oklahoma securitization proceeds of 2022 and 2023 ($1,330.6M and
$197.4M removed). Working capital (non-Uri) is counted each year, average −$37.4M (specific (d)). All-equity basis: interest
expense added back after the year's effective tax rate (14.0% to 17.8%), the company's own tax (Q7, Whose tax). **CONVENTION
of this run:** the Kansas securitization subsidiary (KGSS-I) is left out on both sides, its bonds ($238.5M at 2026-06-30) out
of net debt and its principal repayments ($20.7M, $27.9M, $29.5M in 2023 to 2025) and an estimated interest share out of owner
cash; rationale: the bonds are "non-recourse" to ONE Gas and are serviced by a dedicated customer charge that ends when they
are repaid (10-K FY2025, Note 17), so counting the stream as perpetual or the bonds as the company's debt would each misstate
the other. **The maintenance guess** **[M2000-144]**, **[L1999-024]** (specific (e)): the 2026 plan puts "approximately $230
million" of "approximately $800 million" into extensions to new customers (8-K 2026-02-18, accession 0001587732-26-000006); the
rest, 71.25%, is taken as maintenance, the integrity and replacement work that keeps the network in place. The literal window,
as filed, with the storm flows in, averages −$269.5M (equity) and −$178.2M (all-equity) a year, shown beside.

**Growth shown.** Operating income 10.2% a year 2021 to 2025, net income 6.4%, revenue 7.6% (gas cost included). The
maintenance-only owner cash, with working capital at its average, rose from $85.7M to $128.2M, 10.6% a year; the all-spending
series is negative at both ends, so its growth is meaningless and that series is carried at no growth (specific (b)).

**The range (all-equity, central, specific (e)):** the maintenance-only case at no growth, and the growth case in which the
same cash grows at the 10.6% shown for ten years while the growth spending ($198.4M a year, the 28.75% of spending for
extensions) is charged against it and stops after year ten, discounted at 5.43%, net debt $3,146.5M (other long-term debt
$2,133.7M, current maturities $249.9M, notes payable $770.8M, less cash $7.9M, 10-Q 2026-06-30; the August 2026 notes refinanced
the term loan and paper and leave the total unchanged, 424B5 capitalization table), 62.856M shares:

| case | value a share at 5.43% | at 10% | expected return at $75.60 |
|---|---|---|---|
| maintenance only, no growth | **−$27.68** | −$37.91 | 1.0% |
| maintenance only, shown growth, growth spending charged | **−$21.86** | −$44.11 | 2.0% |
| beside: all spending, no growth | −$85.82 | −$69.48 | below zero |
| beside: depreciation variant, no growth | $43.98 | $1.00 | 4.1% |
| beside: depreciation variant grown at the operating-income rate with no spending charged (a ceiling no rule admits) | $161.83 | $53.45 | 8.5% |
| beside: a regulated check, pre-capex cash and all spending each at their shown rates ten years, then the depreciation variant flat (`q7_regulated_check.py`) | $38.54 | −$30.20 | 4.5% |
| equity-only beside: maintenance only, no growth / growth | −$1.86 / −$28.21 | −$1.01 / −$21.51 | below zero |
| literal window, as filed, no growth | −$106.07 | | below zero |

**Value range:** **−$27.68 to −$21.86 a share** against **$75.60** (all-equity basis, central); the equity-only range beside,
−$28.21 to −$1.86.

**The floor, tested first** (CONVENTION, Q7): about ten percent pre-tax, applied to owner cash after the company's own tax
**[M2003-149]**. **No case earns it at the price.** The central pair returns 1.0% and 2.0% a year at $75.60; the depreciation
variant 4.1%; the coherent regulated check 4.5%; and even the ceiling that credits all the growth while charging none of the
spending that buys it, which the growth rule forbids **[L2000-023]**, reaches 8.5%. The reason is the business itself, not
the construction: it earns about 6% after tax on its capital (Q3), the market values that capital at $7,898.5M against
$6,391.6M at book (Q3), and the growth it shows is bought with new capital at the same 6% **[M2012-057]**. "growth can destroy
value if it requires cash inputs in the early years of a project or enterprise that exceed the discounted value of the cash"
**[L2000-023]**: at the government rate the growth roughly pays for itself; at the floor it does not.

**Width:** not reached; the floor closes first. **Screamer:** no **[M2009-005]**.

**Fair price (a reporting figure, never a verdict; Part VII):** each end of the central range valued at ten percent, the two
averaged, after the company's own tax, on the all-equity basis less net debt: **−$41.01 a share** (central). Equity-only beside:
**−$11.26 a share**. Neither is a price at which the name could be bought; both say that at a ten percent floor the cash this
business leaves for its owners after the capital it consumes is worth less than its debt. No cheap price is reported.

- **VERDICT: OUT.** No case in the range earns the floor at $75.60, which is "a point at which we drop out of the game"
  **[M2003-149]**; the value at the government rate is itself below the price on every case the rules admit **[L2000-021]**,
  **[M1996-025]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (the file closed at Q7).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (Natural gas distribution is not among the businesses the framework names.)

---
## THE BOX
**OUT at Q7**: no case of the range earns the floor at $75.60; value range **−$27.68 to −$21.86 a share** (all-equity basis,
central maintenance-only pair at the 5.43% Treasury rate; equity-only −$28.21 to −$1.86) against **$75.60**; fair price
**−$41.01** all-equity, **−$11.26** equity-only, not positive. Q1 IN, Q2 IN as the regulated exception, Q3 weighs against,
Q4 weighs for (habits against, carried), Q5 integrity IN, Q6 weighs against; Q8 to Q12 not reached.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; the box unchanged, operator rule 2; each with its source **[M1997-127]**.)*
- **Bearing on Q8 (the bond).** The dividend is $2.72 a share annualized (10-K Item 5), 3.6% of $75.60, against the 5.43%
  30-year Treasury of 2026-10-16. The bond filter is "one opportunity cost of buying the stock is to compare it with a bond"
  **[M1997-089]**; not applied.
- **Bearing on Q9 (debt and exposures).** Total debt $3,392.9M at 2026-06-30, of which $238.5M is the non-recourse Kansas
  securitization bonds (424B5 capitalization table, accession 0001193125-26-347036; 10-Q). Notes payable (commercial paper,
  maturities up to 270 days) $770.8M, backed by a $1.5 billion revolving credit agreement to October 30, 2030 with no borrowings
  at year-end 2025; covenant debt-to-capital ex-KGSS-I at most 70%, actual 47.6% at 2025-12-31; senior notes $2.2 billion with
  none due within a year at 2025-12-31; the $250M term loan due September 2026 was refinanced by the August 2026 notes; ratings
  A3 and A- stable (10-K Item 7). Coverage, operating earnings before interest and tax over interest expense, 2025: ($321.5M +
  $142.8M) / $142.8M = 3.25 times (statement of income); the speakers' definition is pre-tax earnings over interest, "not
  EBITDA/interest" **[L2012-002]**. The 10-K's own risk factor: "An increase in the price of natural gas could cause us to
  experience a significant increase in short-term or long-term debt because we must pay suppliers for natural gas when
  purchased" (Item 1A); the 2021 storm required $2.5 billion of new notes in one year (10-K FY2022 cash-flow statement). Three
  states, one business: "A catastrophic event can render a single utility insolvent" **[L2005-019]**. The "little or no debt"
  criterion **[R1997-001]** is stated for whole businesses; not applied.
- **Bearing on Q5 (integrity):** none beyond those already judged at Q5. The habits (adjusted figure featured from February
  2026, annual guidance and a five-year growth outlook) were weighed there, not left for a later run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. **Slip, declared:** before the copy I listed `Test Runs/` filtered for this
      company's names (no match). Written question by question and committed after each, with two departures: the research
      for Q1 to Q7 (filings, competitor data, the Q7 arithmetic) was fetched and read before the sections were written, so the
      sections record a reading done ahead of the writing; and Q5 and Q6 were committed together in one commit
      (fe974394) instead of two.
- [x] Dispatched: the brief allowed per-question pathspec commits of my own two paths; the lock (`Screens/_daily/`) was present
      at the start and is the dispatcher's; folding is the dispatching session's (operator rule ten). A run not in the register
      binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. Seen by accident and not used: the commit
      subjects of another gas distributor's run, and a memory-index line on the queue (declared under contamination at the top).
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `Test Runs/_research 2026-10-18 OGS/check_ids.py`, which also
      checks that each quoted fragment beside an id is in that row; no E-ids. Every filing fact carries its document and
      accession.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; nothing after it is a clearance. The Q7 figures
      are a valuation reached in sequence (Q1 to Q6 closed without a STOP), not a computation after a stop.
- [x] Owner cash after every real cost, built from the filed cash-flow statements, never a net-income proxy (operator rule 5).
      Sovereign from the US Treasury, dated 2026-10-16. Price from an aggregator, flagged, cross-checked to the proxy's year-end
      price.
- [x] Contrary evidence written down as found (foundations line, Q2's threats, Q3's capital, Q4's habits).
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used (its share counts, price, sovereign, balance-sheet table); its
      owner-earnings lines were rejected for the reasons in Step 0.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the commit).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q7 specific (e) does not fit a rate-base business.** It assumes maintenance spending keeps the business "in the same
economic place" and growth spending buys growth; at a regulated utility the integrity and replacement program, which I took as
maintenance (71.25% of spending, from the company's own split), is also what the regulator lets it earn on, so it raises rate
base and earnings. The maintenance-only no-growth case then charges spending that buys growth and credits none, and both ends
of the central range come out negative per share (−$27.68 and −$21.86). I kept the convention's figures as the reporting range
and added a coherent regulated check (spending and pre-capex cash each at their shown rates for ten years, then a flat rate base
with spending equal to depreciation), which gives $38.54 at 5.43% and 4.5% a year at the price. The box does not depend on the
choice, since no construction reaches the floor, but the range and the fair price are not meaningful as values for this kind of
business, and a negative fair price is no use as an alert. A paragraph for rate-base businesses is missing. (2) **A multi-year
aberration.** Specific (a) speaks of a first or last window year; Winter Storm Uri spans 2021 (the cost) to 2023 (the last
recovery). I took the storm's flows out of the years they fell in and showed the literal window beside; no text says to.
(3) **Securitization bonds.** No rule says whether non-recourse, self-liquidating securitization debt and its dedicated customer
charge belong in net debt and owner cash; I left both out together (a CONVENTION of the run, stated at Q7). (4) **Q2's
regulated exception.** The text carries "a return set by a regulator" to Q3 as a second best but says nothing about how to judge
the twenty-year policy risk to a regulated network, which is the question that decides Q2 for any gas distributor; I judged it
on the filings of these three states (customer additions, House Bill 4384, renewed ROEs). Another analyst could reasonably have
closed Q2 TOO HARD (NATURE) on the same evidence; the text gives no test that separates the two. (5) **Whose tax at a utility.**
The effective rate (14% to 18%) is lowered by excess-deferred-tax credits that are returned to customers in rates; I used the
effective rate for the interest shield, as "the company's own tax", and note that the statutory rate would lower the all-equity
figures slightly. (6) **The no-rival case**: the brief's rule (comparators as a CONVENTION when the 10-K names none) was needed
and used; the 10-K's Item 5 peer group was the natural source.
