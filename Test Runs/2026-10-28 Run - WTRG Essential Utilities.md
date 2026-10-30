# Company Run — Essential Utilities, Inc. (NYSE: WTRG) — 2026-10-28
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-28: the operator does not hold this name (`PORTFOLIO.md` has no WTRG or Essential row).*

**Dispatch.** A purchase run of record dispatched under `Screens/_daily/_dispatch_brief.md` with two stated departures
(the repository path, now `C:\Projects\BRK`; and the lines of evidence derived by the analyst from the 10-K's Items 1, 1A
and 7, not written by the dispatcher). The lines chosen are listed under Step 0.

**Contamination, declared and not used.** (1) A directory listing of `Test Runs/` made to check that this run's file name
was free showed the file names of five other runs dated today, among them `2026-10-28 Run - AWK American Water Works.md`
(the counterparty to WTRG's signed merger), `... AWR American States Water.md` and `... CWT California Water Service
Group.md`, with their research folders. None was opened, listed further or searched. (2) The session's starting context
showed the last commit subjects, which name a CWT run closed "OUT at Q7" with a range and fair price for CWT; not used,
and CWT's figures in the competitor row below come from CWT's own filings only. (3) The session's memory index carries
generic queue-state lines (counts of gate-clearers, a paused wave); none names this company; not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $42.45 (2026-10-28, `tools/sources.py` price, an aggregator quote, flagged per operator rule 5 as a live
  quote only; the same tool gives American Water (AWK) $141.10 at 2026-10-27, so the merger consideration of 0.305 AWK a
  share is about $43.04 on those two quotes, which are a day apart).
- **Shares by class** from the latest filing's cover: one class, common stock $0.50 par, **283,778,605** shares as of
  2026-07-27 (10-Q for the quarter ended 2026-06-30, filed 2026-08-05, accession `0000078128-26-000077`;
  `python Screens/cover_shares.py WTRG`). Check against the balance sheet of the same 10-Q: issued 287,261,673 less
  treasury 3,488,132 = 283,773,541 at 2026-06-30; the cover count is 5,064 higher, consistent with the at-the-market and
  dividend-reinvestment issuance the 10-Q reports. No 8-K or prospectus after the 10-Q reports an issuance of size (the
  8-Ks of 2026-08-17, 2026-08-31 and 2026-09-17 were listed; the last is the merger settlement).
- **Market cap:** 283.779M x $42.45 = **$12,046.4M**.
- **Sovereign for the earnings currency (USD):** **5.30%**, US Treasury daily par yield curve, 30-year, 2026-10-27
  (`tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-26, accession `0000078128-26-000050` (Items 1, 1A,
  7 and 8: the statements, Notes 18 Rate Activity and 19 Segment Information); 10-K for FY2023, filed 2024-02-29,
  `0001562762-24-000047` (cash flows 2021 to 2023, segment table 2021 to 2023); 10-K for FY2021, filed 2022-03-01,
  `0001562762-22-000068` (statement of capitalization at 2020 and 2021 year-ends); 10-Q for the quarter ended 2026-06-30,
  filed 2026-08-05, `0000078128-26-000077` (balance sheet, debt, at-the-market program, pending acquisitions); proxy
  (DEF 14A) filed 2026-03-17, `0001552781-26-000133`; 8-K filed 2025-10-27, `0001552781-25-000341` (merger agreement);
  8-K filed 2026-09-17, `0001552781-26-000492` (PaPUC joint petition for non-unanimous settlement).
- **One figure cross-checked against the filed statement:** total assets at 2025-12-31, $19,464,845 thousand on the
  filed balance sheet of `0000078128-26-000050`, against `tools/run.py`'s XBRL table, $19,465M: agree. Stockholders'
  equity $6,857,456 thousand filed against $6,857M: agree.
- `python tools/run.py WTRG`, arithmetic lines only: the tool's owner-earnings window stopped at FY2018 (it found no
  capex tag after 2018 under the elements it reads) and so its yield lines are stale and are **not used**; its ten-year
  balance-sheet table is used in Q4, checked against the filed statements. Owner cash is built below from the filed
  cash-flow statements (Q4 and Q7).

**The lines of evidence, chosen from the 10-K (the brief's second departure).** From Item 1: (i) the regulated model,
rate base and the commissions' rate allowances ("The profitability of our utility operations is influenced to a great
extent by the timeliness and adequacy of rate allowances"), with the infrastructure surcharges, fully projected test
years and Pennsylvania's fair-market-value acquisition law; (ii) the two segments, water (53.6% of 2025 revenue) and
natural gas (45.2%), and Aqua Pennsylvania's weight (57% of water revenue, about 72% of water income); (iii) competition,
which the filing says is little for daily service and real for acquisitions and, in gas, from other fuels; (iv) the
capital plan, about $8.7 billion for 2026 to 2030. From Item 1A: (v) "Changes in our earnings per share may differ from
changes in our rate base"; (vi) the gas risks: declining use per customer, explosion and pipeline integrity, and climate
rules; (vii) concentration in Pennsylvania; (viii) "We have substantial indebtedness" ($8,331,987 thousand of debt at
2025-12-31) and dependence on capital markets; (ix) the merger risks, including the $370 million termination fee. From
Item 7: (x) rate base $12.4 billion at 2025-12-31 ($7.8 billion water, $4.6 billion gas), guided to grow about 8% a year
through 2029; (xi) return on equity 8.4%, 9.6%, 9.0% in 2023 to 2025 and capital spending at 3.5 to 3.7 times
depreciation; (xii) an effective tax rate of (15.4%), (3.8%) and 0.6% in 2023 to 2025 from the repairs deduction flowed
through to customers.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether one would be content to own this "if the market closed for five years"
**[M1997-109]**, and for a regulated utility the business is the rate base and the return the commissions allow on it.
The market serves: today's quote sits beside a fixed exchange ratio into another company's stock, and the price says
nothing about the value of the business unless the facts and reasoning lead there **[M2006-077]**. Margin of safety: if
the case needs pencil and paper it is too close **[M1996-084]**. No macro forecast enters: the rate level and the gas
price are not forecast here **[M2000-094]**. Who is paid to tell you: the filing's growth guidance ("around 6% and 11%"
rate-base growth) is the company's own projection and is not used as an input. **Contrary evidence, written down as
found** **[M1997-127]**: (1) capital spending ran 3.5 to 3.7 times depreciation in 2023 to 2025, and owner cash after all
spending was negative in every year of the window (Q7); (2) the business has needed new shares every year (at-the-market
sales of $300,117 thousand in 2025, $36,134 thousand in 2024, $322,983 thousand in 2023) to fund it; (3) the effective
tax rate was below zero in two of the last three years, so reported net income runs ahead of what a full-tax business
would show (Q4); (4) the gas half carries a long-dated question the water half does not: declining use per customer and
climate rules (Item 1A); (5) a signed merger fixes the holder's outcome to another company's stock if it closes.

## THE STANDING RULE
Owning this puts the buyer at risk of ruin only through the buyer's own conduct: bought with the buyer's own money,
unlevered and sized so that it can be held through any fall, it cannot "risk what we have and need for what we don’t
have and don’t need" **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The
target's own debt is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**. The product need not be
  understood in its chemistry; "the economic dynamics of the industry" must be **[M2011-014]**.
- **The key variables and whether they are foreseeable** **[M1998-044]**. For a regulated utility the earning power is
  the rate base times the return the commissions allow on its equity share, less what the business fails to earn of it
  (lag, disallowance). The filing names the drivers itself: rate base, "the timeliness and adequacy of rate allowances"
  (Item 1), and the gap between earnings and rate-base growth ("we may experience periods in which growth in earnings is
  less than growth in rate base", Item 1A). Rate base is a book quantity built from the company's own spending plan
  ($8.7 billion for 2026 to 2030, Item 1) and is foreseeable in a general way; the allowed return is set in public
  proceedings, and the rows treat it as nearly certain if the utility behaves: "when you get an allowed return in the
  electric utility you’re almost certain of earning it, I mean, if you behave yourself" **[M2010-037]**. Costs that pass
  through (purchased gas through the PGA clause, Item 1) leave the utility indifferent: "those utilities are pass-through
  organizations" **[M2012-013]**.
- **The parts** (Q1's holding-company paragraph read with Q2's business of parts). Segment net income 2021 to 2025, from
  Note 19 of `0000078128-26-000050` and the segment table of `0001562762-24-000047`: Regulated Water $293,703, $314,352,
  $340,961, $350,305, $410,920 thousand (sum $1,710.2M); Regulated Natural Gas $148,193, $185,276, $200,563, $293,617,
  $267,375 thousand (sum $1,095.0M; 2024 includes a $91,581 thousand gain on a sale of assets). Water is 61% of the two
  segments' five-year net income, and more on any pre-tax measure (gas carried negative income tax provisions every year:
  $(40,013) to $(113,353) thousand). **Water decides.** Gas does not, and Q1 is answered for water; the gas part is read
  at Q2 and carried.
- **Water, ten years out.** A regulated water and wastewater utility in eight states, monopoly service in practice ("the
  applicable utility commissions usually allow only one regulated utility to provide service to customers in a given
  area", Item 1, Competition), no technology that changes the product, demand set by population and weather. Where it
  will be in ten years is foreseeable in a general way: a larger rate base earning about what the commissions allow, with
  more customers by acquisition. That is "the absence of change" the rows look for **[M1999-063]**. The insiders would
  write the forecast down: the filing does, as a rate-base growth rate through 2029 (Item 7), which is test 5 of Q1
  **[M2000-105]** passed on its face (the figure itself is not used: the foundations).
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. The doubts
  found are about the price and the regulator's future generosity, which are Q2, Q3 and Q7 questions, not about whether
  the economics can be seen. The gas part's ten-year economics (use per customer, climate rules) are less foreseeable,
  and it is not the deciding part.
- **VERDICT: IN.** The deciding part, regulated water, is a business whose ten-year economics can be foreseen in a general
  way from its filings **[M2012-065]**, **[M2000-037]**; its key variables (rate base, allowed return, lag) are known and
  reasonably predictable **[M1998-044]**, **[M2010-037]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. The deciding part is
regulated water (Q1, the parts); gas is read and carried.

- **What keeps it standing: a natural franchise held under a regulator.** The rows list "a natural franchise because of
  surface capabilities" among the moats **[M1995-037]**. The filing: service rights are "generally non-exclusive, although
  the applicable utility commissions usually allow only one regulated utility to provide service to customers in a given
  area", and "As a regulated utility, we believe there is little competition for the daily water, wastewater, and natural
  gas service we provide" (Item 1, Competition, `0000078128-26-000050`). The key factor is the pipe in the ground plus the
  commission's grant; it is as permanent as the commissions and the condemnation statutes allow.
- **The attacker with money** **[M2011-015]**. A hundred million or a hundred billion dollars would not buy a second set
  of mains under the same streets with the commission's leave; the filing names the one form the attack takes, "a very
  small number of instances in one of our southern states" where a municipal system lays parallel mains, and condemnation
  by municipalities (eminent domain or a reserved right of purchase), for which the company "would be entitled to fair
  market value" (Item 1). The money test passes for water. The real competition is for acquisitions, where competition
  "from other regulated utilities, governmental entities, and strategic and financial buyers" may push prices "to
  unacceptable levels" (Item 1A): that bears on the growth, not on the standing castle.
- **Pricing power and the agony before a rise** **[M2005-020]**. The business cannot raise a price; it asks the commission.
  Every rise in the window was a public proceeding, mostly settled with the consumer advocate: Aqua Pennsylvania's 2025
  order "approving, with certain minor modifications, the joint petition for non-unanimous partial settlement" that
  "allowed a base rate increase designed to increase total annual operating revenues by $73,000" thousand; Peoples' 2024
  settlement, $93,000 thousand or 11.1% (Note 18). This is the prayer session written into the law, the opposite of
  pricing power; what replaces it is the allowed return on capital, which "you’re almost certain of earning it, I mean, if
  you behave yourself" **[M2010-037]**, and the regulators allow "an appropriate return on the huge amounts of capital we
  must deploy" only if the utility keeps its side **[L2009-011]**.
- **Unit volume and share of mind; the low bid; the brand.** Not the shape of this business: the customer has no choice of
  supplier. Use per customer is falling ("increased water conservation and the installation of water saving devices"; a
  0.5% fall in residential use costs about $3,700 thousand of revenue, Item 1), and the customer base grew at 1.1% a year
  2021 to 2025 adjusted for dispositions (Item 1), much of it bought.
- **What could destroy, modify or reduce it** **[M2000-014]**. Three things, from the filing and the rows. (1) The regulatory
  compact: "the regulatory climate in a few states has raised the specter of zero profitability or even bankruptcy"
  **[L2023-011]**; "whether you earn X or go broke is not an equation that works" **[M2024-011]**. Pennsylvania is the
  exposure (Item 1A, "Our operations are geographically concentrated in Pennsylvania"), and its water framework as the
  filing describes it is the opposite of hostile: consolidated tariffs, fully projected test years, the DSIC, a
  fair-market-value rate base for municipal purchases (Item 7 table). (2) Affordability: rates rising with a capital
  program at 3.5 times depreciation, which the filing names as "potential opposition to rate increases" (Item 1A); "you’d
  better hope that the rate of return allowed is commensurate in times of high inflation" **[M2005-052]**. (3)
  Condemnation and contamination (PFAS: at least $450,000 thousand of capital planned, Item 7), which add rate base rather
  than destroy it if recovered. None of the three shows the water castle filling in on the filed evidence.
- **Ask the competitors.** The 10-K names no rival (Items 1 and 1A name only classes: "other regulated utilities,
  governmental entities, and strategic and financial buyers"). **CONVENTION of this run:** the rivals are chosen by the
  analyst, three US investor-owned water utilities that file with the SEC: American Water Works (AWK, the largest, a
  direct rival for Pennsylvania municipal systems and the merger counterparty), American States Water (AWR) and California
  Water Service Group (CWT); rationale: the filing names none, and these are filers whose business is the same regulated
  water model. The rivals that do not file are the municipal and authority systems the filing calls the majority of the
  field ("The majority of these community water systems are government-owned", Item 1); flagged.
- **The competitor row** (return on average book equity: net income over the average of opening and closing equity, 2021
  to 2025, from each filer's 10-K figures as transcribed in its XBRL facts, not read in the filed statements; flagged):

  | filer | 5-yr return on average equity | by year 2021 to 2025 | capital spending / depreciation 2021 to 2025 | accession of the latest 10-K used |
  |---|---|---|---|---|
  | WTRG | 9.17% | 8.7, 8.8, 8.8, 9.8, 9.4 | 3.45 | `0000078128-26-000050` |
  | AWK | 11.86% (10.64% for 2022 to 2025; 2021's 18.4% stands out from its neighbours and was not read) | 18.4, 10.9, 10.8, 10.4, 10.5 | 3.44 | `0001410636-26-000034` |
  | AWR | 13.91% | 14.2, 11.2, 16.8, 14.1, 13.3 | 4.51 | `0001628280-26-009114` |
  | CWT | 8.28% (equity including the minority interest) | 9.7, 7.7, 3.8, 12.4, 7.7 | not tagged under the elements read | `0001628280-26-012444` |

  (Computed in `Test Runs/_research 2026-10-28 WTRG/peer_roe_output.txt`.) WTRG's equity carries $2,348,559 thousand of
  goodwill from the 2020 Peoples purchase (balance sheet, `0000078128-26-000050`), so its return on tangible equity is
  higher than 9.2%; and its income was flattered by negative tax provisions in the gas segment (Q4).
- **The parts table.**

  | part | share of five-year segment net income 2021 to 2025 | castle | decides |
  |---|---|---|---|
  | Regulated Water (8 states; Aqua Pennsylvania 57% of segment revenue) | 61% ($1,710.2M) | natural franchise under commissions; regulated return | yes |
  | Regulated Natural Gas (Peoples, western Pennsylvania and Kentucky) | 39% ($1,095.0M) | distribution franchise under the PaPUC; competes with other fuels; use per customer declining (Item 1A) | no |
  | Other (market-based services, corporate) | negative | none claimed | no |

  The gas part's castle stands today (rates set by the PaPUC and the Kentucky PSC; a $3,000,000 thousand pipe-replacement
  plan approved "without modification" on 2025-12-18, Item 1), but its twenty-year future carries the substitution
  question the rows ask of any business, whether it would be started today against its substitutes **[L2006-008]**, and
  "slow change can be much harder to perceive" **[M2014-038]**. It does not decide; it is carried in the consolidated
  figures to Q7.
- **The field's returns over the last full cycle.** On the filers' own figures the field earns about 8% to 14% on book
  equity, WTRG near the bottom. These are ordinary returns, and they are set by commissions. The framework: a field of
  ordinary returns "is OUT, not TOO HARD", and "A return set by a regulator is the exception, carried to Q3 as a second
  best". The rows' own words: "there’s no way we get rich on our utility investments. But there’s no way we get poor,
  either." **[M2009-104]**; "You can't expect to earn outsized profits in regulated utilities, but the industry offers
  owners the opportunity to deploy large sums at fair returns" **[L2005-005]**.
- **Widening or narrowing** **[M1999-108]**. The water franchise is widening in extent (twelve acquisitions in 2023 to 2025;
  four signed purchase agreements for about 203,000 equivalent customers at 2025-12-31, Item 7) and is not narrowing in
  kind on the filed evidence. The DELCORA purchase ($276,500 thousand) has been in litigation since 2019 (10-Q
  `0000078128-26-000077`), a sign that the municipal-sale road is contested.
- **VERDICT: IN.** The deciding part's castle, a natural franchise held under the commissions **[M1995-037]**, stands; the
  filed evidence shows it neither open to a funded attacker **[M2011-015]** nor filling in **[M2000-014]**. Its returns are
  ordinary and set by regulators, which the framework carries to Q3 as a second best rather than closing OUT
  **[M2009-104]**, **[L2005-005]**. The regulatory compact is the standing risk, weighed again at Q9 **[L2023-011]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
The rows' test: "does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**, and of
growth, "whether that’s good or bad depends on what we earn on that incremental $130 million over time" **[M2001-019]**.
For a utility the return is "measured by the operating earnings after depreciation", not by "the cash minus the increased
capital investment" **[M2014-086]**.

- **Return on the capital actually needed.** Operating income (after depreciation, before interest and tax) was $920,951
  thousand in 2025 against net property of $14,263,682 thousand at year-end (6.5%) and an estimated rate base of
  $12.4 billion (7.4%) (`0000078128-26-000050`, statements and Item 7). Return on average book equity 9.17% over 2021 to
  2025 (Q2 row), on equity that includes $2.35 billion of purchased goodwill.
- **What the added capital earned.** Operating income rose from $602,709 thousand (2021, `0001562762-24-000047`) to
  $920,951 thousand (2025), +$318.2M; net property rose from $9,512,877 thousand (2020-12-31, `0001562762-22-000068`) to
  $14,263,682 thousand (2025-12-31), +$4,750.8M. The increment earned about 6.7% pre-tax, before interest, on the added
  plant: in line with the whole (6.3% in 2021 on opening plant, 7.0% in 2025), neither rising nor falling much. That is
  the pattern the rows describe for a utility: "we’re not earning a higher rate of return on capital than we were when we
  started. We just put way more capital into the business" **[M2023-081]**.
- **To stand still and to grow.** Capital spending was $1,020,519 to $1,429,980 thousand a year, against depreciation and
  amortization of $297,952 to $417,471 thousand: 3.45 times over the five years (Q2 row; the filing gives 3.5, 3.7, 3.5
  for 2023 to 2025, Item 7). The maintenance guess the rows allow is the depreciation charge, "Every year we spend amounts
  equal to our depreciation charge simply to stay in the same economic place" **[L2000-035]**, **[M2000-144]**; the rest,
  about $855M a year with net acquisitions, is growth spending, an "optional outlay" in the rows' terms **[L1999-024]** only
  in part: much of it is replacement of old pipe under approved programs (the gas LTIIP, the DSIC), which the regulator
  turns into rate base. The rows name the compulsion: "it costs a lot more money to maintain capital expenditures now in
  dollar terms than it would’ve 30 years ago. So you have to keep putting more and more money into a public utility"
  **[M2005-052]**; "To earn more, their owners must invest more" **[L2011-019]**.
- **Where the money comes from.** Operating cash covered depreciation and the dividend only; the rest came from debt and new
  shares every year: at-the-market and forward sales $299,739 thousand (2021), $63,040 (2022), $322,983 (2023), $36,134
  (2024), $300,117 (2025), plus about $16,000 a year through the dividend plan (cash-flow statements). The rows' grading:
  "The second-best business is a business that also gives you more and more money. It takes more money, but the rate at
  which you invest — reinvest — the money to get that growth is a very satisfactory rate." **[M1998-081]**. The rate here
  is the allowed one, "fair returns" **[L2005-005]**, not a high one.
- **The growth arithmetic and its caps.** Customer growth is 1.1% a year (Item 1); revenue grew 7.1% a year 2021 to 2025
  with gas costs passed through; earnings grow only as fast as rate base, equity issuance and lag allow ("growth in
  earnings is less than growth in rate base", Item 1A). Growth here is bought dollar for dollar with new capital at about
  the allowed rate, so it adds value only to the degree that the allowed return on equity exceeds the owner's alternative.
- **WEIGHS AGAINST**, mildly: a capital-heavy business whose added capital earns a fair, regulated return, "the
  second-best choice, still a good choice" **[M2018-055]**, accepted in the rows on "decent returns on the incremental
  sums they invest" **[L2009-012]**, with growth that requires a constant inflow of new money **[L2011-019]**,
  **[M1998-081]**. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten year-ends** **[M2025-032]** (`tools/run.py` XBRL table, first-filed vintages, checked
  for 2024 and 2025 against `0000078128-26-000050` and for 2020 and 2021 against `0001562762-22-000068`; USD millions):

  | year-end | assets | equity | cash | receivables | goodwill | long-term debt (net, non-current) | retained earnings |
  |---|---|---|---|---|---|---|---|
  | 2016 | 6,159 | 1,850 | 4 | 97 | 42 | 1,738 | 1,033 |
  | 2017 | 6,332 | 1,958 | 4 | 99 | 42 | 2,008 | 1,133 |
  | 2018 | 6,964 | 2,009 | 4 | 101 | 53 | 2,398 | 1,174 |
  | 2019 | 9,362 | 3,881 | 1,869 | 67 | 64 | 2,943 | 1,210 |
  | 2020 | 13,705 | 4,684 | 5 | 155 | 2,325 | 5,508 | 1,262 |
  | 2021 | 14,658 | 5,184 | 11 | 141 | 2,341 | 5,780 | 1,434 |
  | 2022 | 15,719 | 5,377 | 11 | 206 | 2,341 | 6,371 | 1,534 |
  | 2023 | 16,841 | 5,896 | 5 | 144 | 2,341 | 6,826 | 1,707 |
  | 2024 | 18,027 | 6,199 | 9 | 167 | 2,341 | 7,368 | 1,949 |
  | 2025 | 19,465 | 6,857 | 35 | 217 | 2,349 | 8,110 | 2,281 |

  **What moved and why.** (1) **Equity against retained earnings.** Equity rose $5.0 billion over nine years; retained
  earnings rose $1.25 billion. The other $3.76 billion was new stock: the 2019 raise that pre-funded the Peoples purchase
  (the $1.87 billion of cash at 2019 year-end, spent in March 2020) and the yearly at-the-market sales since. The owners
  have been asked to put in three dollars for every dollar the business kept. (2) **Goodwill** went from $64M to $2,325M in
  2020: the Peoples purchase was paid well above its book, and that premium earns nothing in rates. (3) **Debt** rose from
  $1.7 billion to $8.1 billion non-current (total debt $8,331,987 thousand at 2025-12-31, Item 1A), faster than equity;
  long-term debt is now 1.18 times equity. (4) **Cash** is near zero every year except the pre-funding year: the business
  runs on its credit lines and commercial paper ($568,000 thousand outstanding at 2025-12-31, classified as long-term).
  (5) **Receivables** move with gas prices (2022's $206M); nothing out of line with sales. (6) **Regulatory assets**
  $2,109,448 thousand at 2025-12-31, of which **income taxes $1,897,167 thousand**, up from $1,712,714 thousand a year
  earlier (Note 6). This is the line to read: the repairs deduction is "flowed through" to customers (Item 1, Income Tax
  Accounting Method Change), so current tax expense is cut and a regulatory asset is booked for deferred taxes that future
  customers are expected to pay. "Deferred asset accounts" building is a tell the rows name **[M1995-064]**; here the
  account is created by an approved ratemaking method, disclosed in full, and the effect on what the figures say is that
  reported net income runs ahead of a full-tax figure while a growing claim on future rates is carried as an asset. "what
  the figures are saying and what they don’t say" **[M2025-032]**: they say the regulator has let the company book income
  now against taxes the customers will fund later; they do not say those future rates will be granted.
- **The real costs.** Depreciation is real **[R1996-023]**, "the worst kind of expense. It’s reverse float" **[M2003-106]**,
  and here it is the smaller part of the spending: depreciation and amortization averaged $350M against capital spending
  of $1,208M a year. Stock pay is small ($10,078 to $12,855 thousand a year) and is deducted in owner cash. No recurring
  restructuring charges were found in the statements read. The income tax line is the unusual one: effective rates of
  (15.4%), (3.8%) and 0.6% in 2023 to 2025 (Item 7), cash taxes paid of $5,692 to $11,269 thousand a year (supplemental
  cash-flow data); "all benefit of lower tax rates goes to customers" in a utility **[M2017-031]**, so the low tax is not
  a windfall to the owner, and owner cash is taken after the tax the company actually paid (Q7). One-time items in the
  window: a $92,224 thousand gain on a sale of assets in 2024 (gas assets, per the earnings release) and the 2025 PFAS
  settlement receipts (Item 7), both disclosed.
- **EBITDA, guidance, the adjusted figure.** No EBITDA was found in the 10-K or the 2025 earnings release (8-K filed
  2026-02-26, `0001552781-26-000071`, Exhibit 99.1). The company gives **guidance**: "Anticipated growth in long-term
  earnings per share at a compounded annual growth rate of 5 to 7% from the adjusted 2024 earnings per share of $1.97
  (Non-GAAP)", and the proxy letter says "We achieved earnings per share above our initial guidance range"
  (`0001552781-26-000133`). The **adjusted figure** removes the 2024 gain and weather effects, so it lowered 2024's figure
  from $2.17 to $1.97; it is used as the base of the guidance and of the pay plan's "Target EPS (adjusted for comp plan)",
  which was "Achieved" in each of 2023, 2024 and 2025 (proxy). The guidance and the habit of meeting targets are recorded
  here as a weighing against **[L2019-006]**, **[L2002-041]** and carried to Q5; the adjustment cut the figure rather than
  raised it, which is the opposite of waving away costs **[L2016-006]**.
- **The management's explanation.** The 10-K explains the regulatory mechanics, the tax method and its reversal risk, and
  says plainly that "growth in earnings is less than growth in rate base" may persist (Item 1A): clear speech of the kind
  the rows count as a plus **[M1994-018]**.
- **VERDICT on the accounts: WEIGHS AGAINST** (no STOP). The accounts are readable and not suspect: the rule is "when the
  accounting confuses you, I would just tend to forget about it as a company" **[M1995-063]**, and nothing here confused
  once the tax note and the regulatory-asset note were read; the unusual items are explained in the filer's own words
  **[M1994-018]**. They weigh against for three
  reasons: reported income runs ahead of a full-tax figure through flow-through taxes booked as a growing regulatory
  asset **[M1995-064]**; owner cash after all spending is negative in every year (Q7); and earnings guidance with targets
  met every year is carried to Q5 **[L2019-006]**, **[L2002-041]**. The recast owner cash is built in Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
The two yardsticks: "how well they run the business" against "the hand they were dealt", and "how well that they treat
their owners" **[M1994-008]**; read "the proxy statements ... see how they treat themselves versus how they treat the
shareholders" **[M1994-009]**. Integrity is applied on doubt: "If you’ve got doubts, forget it." **[M2013-088]**. For a
marketable stock the reading tests carry the weight.

- **Who.** Christopher H. Franklin, 60, with the company "for over 30 years", chief executive since July 2015, chairman
  as well (proxy `0001552781-26-000133`). He owns 342,081 shares outright (about $14.5M at $42.45) plus 266,145 options;
  2025 salary $1,103,931; total reported pay $9,212,815 (2024: $6,222,992). Under the merger he "will serve as Executive
  Vice Chair of American Water’s Board of Directors for a period of two" years (8-K `0001552781-25-000341`).
- **The integrity record read.** The 10-K reports no restatement and no material weakness (cover check boxes and the
  auditor's report, `0000078128-26-000050`; a text search for "restat", "material weakness", "penalt", "consent order"
  found only boilerplate). The reports explain the business in the filer's own terms, including the unflattering ones:
  "growth in earnings is less than growth in rate base; such differences may be material and may persist over multiple
  reporting periods" (Item 1A), and the tax flow-through and its reversal risk (Item 1A, Note 6). That is a management
  "telling us about the things that we would want to know about if we owned a hundred percent of the company"
  **[M1998-036]**.
- **The habits carried from Q4.** Earnings guidance (5% to 7% a year from adjusted 2024 EPS) and a pay plan whose "Target
  EPS (adjusted for comp plan)" was "Achieved" in 2023, 2024 and 2025 (proxy, Pay for Performance Alignment). The rows'
  warning is that "we become downright incredulous if they consistently reach their declared targets" **[L2002-041]** and
  that guidance encourages gaming **[L2019-006]**. Read with the rest of the record: three years of hitting an EPS target
  in a business whose revenue is set by commissions and whose biggest swing items (gas cost, weather in Pennsylvania gas
  since October 2024) pass through or are normalized is less telling than the same record in an unregulated business; the
  one adjustment featured (2024) cut EPS from $2.17 to $1.97 rather than raised it; and the stock-price leg of the pay
  plan paid 64% to 83% of target in years of negative three-year TSR (proxy table), so the plan did not shield the
  managers from the owners' experience. No doubt about integrity arises from this record. It stays a weight against
  ability's independence from the numbers, not a doubt about honesty **[M1994-018]**.
- **Love of the business.** Thirty years in the company and a meaningful holding of bought or retained shares; the merger
  hands control to another company, with the chief executive taking a two-year board role, not the top job. No sign in the
  filings read of a seller indifferent to what follows; the merger agreement keeps "substantial operations in
  Pennsylvania" (Item 7). The rows' test of a seller who cares about whom he sells to **[M2002-030]** is not decisive for a
  public company sold for stock.
- **Ability.** Read against the hand dealt **[M1994-008]**: return on equity at the bottom of the three filer peers
  (9.2% against 11.9%, 13.9%, 8.3%, Q2), on an equity base swollen by the $2.3 billion of goodwill paid for Peoples in 2020;
  rate cases settled at constructive terms in the company's largest state; costs held (operations and maintenance fell
  from 28.2% to 25.8% of revenue 2024 to 2025, Item 7, partly the gas-cost denominator). A competent operator of a
  regulated franchise; the capital decision of 2020 (Peoples) is weighed at Q6.
- **VERDICT on integrity: IN.** No doubt was found on the record read **[M2013-088]**, **[M2015-047]**: clear reports
  **[M1998-036]**, no restatement, an adjustment that cut the featured figure. **Ability: WEIGHS AGAINST, mildly**: the
  returns sit at the low end of the field **[M1994-008]**, and the guidance-and-target habit is carried as a weight
  **[L2002-041]**, **[L2019-006]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
- **The retention test** **[R1995-009]**, **[M2011-072]**, **[M1998-110]**. Over 2021 to 2025 retained earnings rose from
  $1,261,862 thousand (2020-12-31, `0001562762-22-000068`) to $2,280,669 thousand (2025-12-31), +$1,018.8M kept; in the
  same years the owners put in about $1,112.6M of new stock (at-the-market and forward sales $1,022.0M, dividend plan
  $80.2M, option exercises $10.4M, cash-flow statements). Market value: 245,390,468 shares at $47.29 on 2020-12-31
  (`0001562762-22-000068` share counts; closes from the aggregator, flagged) = $11,604.5M; 283,082,809 shares at $38.36 on
  2025-12-31 = $10,859.1M. About $2.1 billion kept or newly put in, and the market value of the whole fell by $0.7
  billion. The market leg of the test is failed over the five years **[R1995-009]**, **[M2011-072]**. The intrinsic leg is
  Q7's: the range found there sits below the price paid by the market at every year-end of the window.
- **Dividends while issuing stock.** The company paid $258.7M to $373.8M of dividends a year while selling up to $323M of
  new stock a year to fund spending. The rows' test of a dividend is that the company "expects to regularly earn more than
  it can profitably employ" **[M2004-089]**; this one employs more than it earns and goes to the market for the rest, so
  part of each dividend is paid with the new holders' money, and "dividends impose a specific cash-out policy upon all
  shareholders" with inferior tax for the taxable holder **[L2012-014]**. It is the utility custom ("most utilities pay out
  70% or 80% of earnings and dividends", **[M2023-081]**), and it weighs against.
- **Buybacks.** Repurchases of $2,284 to $4,048 thousand a year (2023 to 2025) of shares; no buyback programme or price was
  found in the filings read; the amounts are of the size of share withholding on stock awards. With no programme of size,
  the buyback test of Q7's range has little to bite on; written back at Q7.
- **Issuance and deals.** "We will issue common stock only when we receive as much in business value as we give" **[R1995-010]**.
  Shares were sold every year (at-the-market sales; the equity statements give counts for two of the large years: 2023, 8,938,839 shares for $322,983 thousand, $36.13 a share; 2025, 7,671,350 shares for $300,117
  thousand, $39.12). Whether the business received as much value as it gave depends on Q7's range per share (written back
  at Q7). Serial issuance is the candidate second STOP the framework leaves unresolved: "we have never invested in
  companies that are hell-bent on issuing shares" **[L2014-015]**. Here the issuance funds regulated plant on which a
  return is allowed, it is announced as a standing at-the-market programme, and it is not paired with promotion found in
  the reports; it is weighed against, not treated as a STOP (the framework names it unresolved).
- **The Peoples purchase (2020).** Paid with debt and the shares raised in 2019; goodwill rose by about $2.26 billion
  (balance sheet, $64M at 2019-12-31 to $2,325M at 2020-12-31). The rows' rule is value given against value got **[L2014-012]**. Peoples' segment
  income rose from $148.2M (2021) to $267.4M (2025), helped by negative tax provisions every year (Q1), on segment capital
  spending of $397M to $650M a year; the goodwill earns nothing in rates. No post-mortem against the original projections
  was found in the filings read.
- **The deal now: Essential sold for American Water stock.** The all-stock STOP of Part A binds an acquirer issuing its own
  undervalued stock **[L2009-019]**; here Essential is the one being bought, so the STOP does not apply to Essential's
  board. For the holder, the board has agreed to exchange each share for 0.305 American Water shares; "the shareholders of
  the acquirer are concurrently selling part of their interest in everything they own" **[L2005-004]** is American Water's
  owners' question, not this run's. The value of what Essential's owners receive is American Water's business, not valued
  here (Q7 states the deal beside the central figure).
- **Part A: WEIGHS AGAINST.** The market leg of the retention test failed over five years **[R1995-009]**, **[M2011-072]**;
  dividends paid while stock is sold **[M2004-089]**, **[L2012-014]**; serial issuance weighed, not stopped **[L2014-015]**.

### Part B: the pay, the board and the owners
- **Pay tied to what the person controls** **[M2003-019]**. The short-term plan pays on an adjusted EPS target with safety,
  compliance and customer-service metrics; the long-term plan's performance shares on "total shareholder return (TSR),
  rate base growth, and controlling our operational expenses" (proxy). Rate base growth is a metric of capital put in; the
  rows' rule for capital-heavy units is to "charge managers a high rate for incremental capital they employ" **[L1994-019]**,
  because "managers, when using other people’s money, start thinking of it a little bit like free money" **[M1995-009]**.
  Paying for rate-base growth pays for spending, with the return left to the commission. Weighs against.
- **The ratchet.** "Mr. Franklin’s long-term incentive target increased from 320% to 370%" because "A comprehensive market
  benchmarking analysis conducted by the Committee’s independent compensation consultant indicated that the CEO’s prior
  LTI target of 320% was below the median of our peer group" (proxy). The rows name exactly this: "They get handed a sheet
  of paper that shows them comparables elsewhere ... And so there’s a ratcheting effect" **[M2004-017]**. Weighs against.
- **The board.** Chairman and chief executive combined, with a lead independent director; all other directors independent
  (proxy). "I've seen how hard it is to replace a mediocre CEO if that person is also Chairman" **[L2014-026]**. Directors'
  and officers' ownership guidelines count only shares owned (proxy, Ownership Guidelines).
- **Owners as partners.** Clear reports (Q5); earnings guidance given (Q4, carried) **[L2019-006]**; "the wrong manager"
  matters more than the wrong plan **[M2007-006]**, and the manager here is not the wrong one on the record read.
- **Part B: WEIGHS AGAINST, mildly**: pay on rate-base growth **[L1994-019]**, a consultant's ratchet **[M2004-017]**, a
  combined chair **[L2014-026]**; offset in part by a TSR leg that paid below target when owners lost **[M2003-019]**.

**Written back from Q7 (committed with Q7).** The bottom of Q7's central range is **$28.63** a share (top $32.98). The small
repurchases (no programme, no stated price) were made at market prices of the window, all above $28.63, so by the
framework's test of a buyback with no stated price they weigh against **[L2016-002]**; they are too small to matter. The
issuance runs the other way: shares sold at $36.13 (2023) and $39.12 (2025) were sold above the top of the range, so the
business received more than the per-share value it gave **[R1995-010]**; on this range the at-the-market programme did not
harm the continuing owners. Part A stays **WEIGHS AGAINST** on the retention test and the dividend-while-issuing pattern.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**; value is "the discounted value of the cash
that can be taken out of a business during its remaining life" **[R1996-018]**, and the question includes "are you going to
have to put more cash into after you buy it?" **[M2014-068]**. Arithmetic in `Test Runs/_research 2026-10-28 WTRG/scripts/value.py`,
output in `value_output.txt` beside it.

**The basis.** The deciding part earns a regulator-allowed return (Q2), so by Q7, The regulated utility, the **equity-only
basis is central**: owner cash after interest and after the company's own tax, against the market value of the shares
($12,046.4M); the all-equity figure is shown beside and never decides alone **[L2017-012]**, **[M2010-037]**.

**Owner cash by year, from the filed cash-flow statements** (USD millions; `0000078128-26-000050` for 2023 to 2025,
`0001562762-24-000047` for 2021 and 2022). Operating cash is after interest, after the tax the company paid, and after
working capital (specific (d)); stock pay is deducted; capital spending includes AFUDC's debt component as filed;
acquisitions are net of systems sold (specific (c)); customers' advances and contributions in aid of construction, net of
repayments, are credited against spending (**CONVENTION of this run**: they are cash customers pay toward plant, shown in
financing; rationale: leaving them out would charge the owner for plant the customers paid for; they average $12.2M and
move nothing). The $25,125 thousand convertible-note purchase of 2025 is left out (an investment outside the business,
$20,000 thousand returned in January 2026).

| year | operating cash | stock pay | D&A (maintenance guess) | capital spending | net acquisitions | customer contributions | owner cash after all spending | owner cash after maintenance | growth spending |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | 644.7 | 10.1 | 298.0 | 1,020.5 | 34.5 | 7.5 | (412.9) | 336.6 | 749.5 |
| 2022 | 600.3 | 12.2 | 321.2 | 1,062.8 | 115.8 | 6.7 | (583.8) | 266.9 | 850.7 |
| 2023 | 933.6 | 11.3 | 343.7 | 1,199.1 | 3.5 | 15.5 | (264.9) | 578.6 | 843.4 |
| 2024 | 770.3 | 9.8 | 369.6 | 1,329.7 | (166.8) | 11.0 | (391.4) | 391.0 | 782.4 |
| 2025 | 1,010.5 | 12.9 | 417.5 | 1,430.0 | 55.5 | 20.2 | (467.7) | 580.1 | 1,047.8 |
| **average** | 791.9 | 11.2 | 350.0 | 1,208.4 | 8.5 | 12.2 | **(424.1)** | **430.7** | **854.8** |

- **The literal window**: owner cash after all spending was negative in every year, averaging $(424.1)M. Before any credit
  for debt, the business has not produced a dollar for its owners in five years; it has consumed new money.
- **The maintenance guess** (specific (e)) is depreciation and amortization, the rows' proxy **[M1998-127]**, **[L2000-035]**,
  **[M2000-144]**; it is the generous guess for a utility replacing old pipe under approved programs (much of the spending
  above it is replacement the regulator rate-bases), and it is stated as a guess.
- **Tax** (Q7, Whose tax): owner cash is after the company's own cash tax ($5.7M to $11.3M a year). The low tax is the
  repairs deduction flowed through to customers under ratemaking, not a carryforward or credit that runs out inside ten
  years, so the statutory-rate convention for a shelter is not applied; the regulatory asset it builds (Q4) is a claim on
  future rates, not cash in the window. State tax losses at Peoples "cannot be utilized presently" (10-K FY2024 tax note),
  so no shelter value is added.
- **Working capital** is inside operating cash; its swings were gas-cost driven ($(169.6)M in 2022, +$175.4M in 2023) and
  average $(49.2)M a year over the window. No first or last year of the window is aberrational on the filer's own
  description, so no cycle base is used (specific (a)).
- **Growth shown** (aggregate, on owner cash after maintenance): $336.6M (2021) to $580.1M (2025), **14.57% a year**
  between end years. **The cap (specific (f))**: carried ten years, $430.7M x 1.1457^10 = $1,679M, against the highest share
  of sales the business has earned (28.2%, 2023) times sales carried at sales growth ($1,210M in year ten): the shown rate
  requires owner cash above any share of sales the business has earned, so the growth carried is **cut to the business's
  own sales growth, 7.14% a year** (revenue $1,878.1M in 2021 to $2,474.6M in 2025), below the discount rate. Both are
  written down; the uncut case is shown beside.
- **Growth spending and the utility debt credit** (specific (e) and The regulated utility, 2026-10-23). Growth spending
  (above the maintenance guess, with net acquisitions, less customer contributions) averaged **$854.8M** a year; in the
  growth case it grows at 7.14%: **$915.8M in year one, $1,703.3M in year ten, none after**. Long-term debt (borrowings due
  after a year, current maturities; commercial paper and short-term loans left out; no finance leases found on the
  statement of capitalization): $5,630.2M at 2020-12-31 (statement of capitalization, `0001562762-22-000068`, including the
  $385.0M revolver then due 2023) to $7,613.8M at 2025-12-31 ($8,181.8M total less $568.0M commercial paper,
  `0000078128-26-000050`): **+$396.7M a year**. Cap: the filing states no allowed capital structure for any part (Notes 18
  and 19, Item 7 read; the rate orders are reported as revenue settlements), so the cap is the business's own long-term
  debt share of long-term capital at the latest filed date, 2026-06-30: $8,131.0M / ($8,131.0M + $7,018.3M) = **53.67%**
  (`0000078128-26-000077`), applied to growth spending: $458.8M a year. The credit used is **$396.7M a year**, below the
  cap, credited against growth spending only, growing with it ($425.0M in year one, $790.6M in year ten) and stopping
  after year ten. Beside it: with the 2020 revolver counted as short-term, the increase is $473.7M a year, capped at
  $458.8M.

**The range, equity-only, discounted at 5.30%** (ten years, then zero nominal growth):

| case | value | per share |
|---|---|---|
| no growth: owner cash after maintenance $430.7M a year, no growth spending, no credit | $8,126M | **$28.63** |
| growth at 7.14% (cut): owner cash after maintenance grown, less growth spending grown, plus the debt credit grown, years 1 to 10; flat after | $9,359M | **$32.98** |
| beside: growth case with the alternative credit ($458.8M) | | $35.39 |
| beside: growth case with no debt credit | $4,990M | $17.59 |
| beside: uncut shown growth, 14.57% | $18,451M | $65.02 |
| beside: the literal window, owner cash after all spending plus the credit, flat ($(27.4)M a year) | $(517)M | not positive |
| **all-equity basis, beside** (owner cash before interest, $430.7M + cash interest paid $257.4M = $688.0M; net debt at 2026-06-30 $8,548.5M = long-term debt including current portion and commercial paper $8,516.2M + loans payable $41.0M less cash $8.6M; operating leases left out) | | no growth $15.62; growth (cut, no credit) $17.80 |

- **The floor, tested first** **[M2003-149]**. The expected return at the price of $42.45 on each case: **no growth 3.57%**;
  **growth (cut) 4.48%**; with the alternative credit 4.67%; even on the uncut 14.57% growth that the cap removes, 6.91%.
  **No case in the range earns about ten percent at the price.** The price is above the top of the central range ($32.98),
  which by the floor convention closes OUT however narrow the range.
- **Width** (for the record; it does not decide): top over bottom 1.15 to 1, far inside three to one.
- **The signed, unclosed deal, beside** (specific (c)). WTRG is the target: each share becomes 0.305 American Water shares
  at closing, about $43.04 on the day-old AWK quote. The box is decided on the central figure; what the deal does to it is
  to replace this business with a share of American Water's, whose value this run does not compute. The deal sets a
  market price under the quote; it says nothing about this business's value **[M2006-077]**.
- **Value range: $28.63 to $32.98 a share against $42.45** (equity-only, central). **Closes: OUT**: no case earns the floor
  at the price **[M2003-149]**; the price is above the top of the range, so the case is not a screamer and needs no pencil to
  reject **[M2009-005]**, **[L2013-012]**. Growth here is "usually a plus, sometimes a minus" **[L2000-023]**: the growth case is worth barely more than the no-growth case because every dollar of growth needs about
  a dollar of new capital at a regulated return.
- **Fair price (a reporting figure, never a verdict; Part VII):** **$13.00** a share, equity-only, central: the no-growth
  case valued at 10% ($4,307M, $15.18) and the growth case valued at 10% ($3,071M, $10.82), averaged; after the company's
  own tax. With the alternative debt credit, $13.95. **All-equity figure beside: $(11.24)**, not positive (no growth at 10%
  $(5.88), growth $(16.59)). No cheap price is reported. Growth spending $915.8M in year one, $1,703.3M in year ten, none
  after. Utility debt credit: long-term debt increase $396.7M a year, against growth spending only, cap 53.67% (the
  business's own long-term debt share of long-term capital at 2026-06-30; the filing states no allowed share).
- **VERDICT: OUT**, on the floor **[M2003-149]**: at $42.45 the expected return is 3.6% to 4.5% on the central cases and
  below ten percent on every case shown, the price sitting above the top of the range **[L2013-012]**, **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED as a judgment. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT**, decided at **Q7** (the floor): value range **$28.63 to $32.98** a share (equity-only, the regulated utility's
central basis) against **$42.45**; fair price $13.00 (equity-only), all-equity $(11.24). Q1 IN, Q2 IN (regulated return
carried as a second best), Q3 weighs against, Q4 weighs against, Q5 IN on integrity (ability weighs against mildly), Q6
weighs against.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; the box is unchanged, operator rule 2.)*
- **Q8.** The 30-year Treasury yields 5.30% (2026-10-27); the equity-only expected return at the price is 3.6% to 4.5%
  on the central cases (Q7) **[M1997-127]**.
- **Q9.** Total debt $8,331,987 thousand at 2025-12-31 (Item 1A); long-term debt including current portion and commercial
  paper $8,516.2M and loans payable $41.0M at 2026-06-30, against equity of $7,018.3M (`0000078128-26-000077`); cash
  $8.6M. Subsidiary debt of $3,068.8M is "substantially collateralized by utility plant" (statement of capitalization).
  Interest expense $329,081 thousand in 2025 against income before income taxes of $619,814 thousand (income before income taxes
  plus interest expense, $948.9M, over interest expense: about 2.9 times). Maturities include $500,000 thousand of notes due 2027 (statement of capitalization);
  commercial paper $384,723 thousand at 2026-06-30 with a weighted remaining term of 11 days, backed by the $1,000,000
  thousand revolver. The filing names covenants whose breach "could result in prepayment obligations" (Item 1A).
  Concentration: Pennsylvania (Item 1A); gas operations carry explosion and pipeline-integrity risk "near populated
  areas" (Item 1A); a captive insurer formed 2025-10-01 retains part of the liability risk (Item 7). Merger: a $370 million
  termination fee payable by Essential in certain cases; $835 million payable by American Water in others (8-K
  `0001552781-25-000341`).
- **Q12.** Water, wastewater and natural gas distribution; the filing names methane-reducing pipe replacement and PFAS
  treatment programs. No named-business question arises.
- **Q5.** No integrity facts beyond those judged at Q5.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `0865b074`); written question by question; committed after each
      (Q1 `520b2e4e`, Q2 `b633bfa6`, Q3 and Q4 `2131e8d0`, Q5 and Q6 `687fbbff` with a correction `0b2a3478`, Q7 with the
      Q6 write-back in the next commit).
- [x] Dispatched: the brief allowed per-question pathspec commits of this file and the research folder only; the lock in
      `Screens/_daily/` was present at the start (held by the dispatching session, not touched). The fold is the
      dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One directory listing of `Test Runs/`
      (to check this file's name) showed other runs' file names, declared above under Contamination and not used.
- [x] Every v5 id was checked against `principle_ledger_v5.csv` by the run's check script
      (`Test Runs/_research 2026-10-28 WTRG/scripts/check_ids.py`); every filing fact carries its accession; competitor
      figures are XBRL transcriptions of the rivals' 10-Ks, flagged as not read in the filed statements.
- [x] The order was kept; Q7, the first STOP that failed, closed the run; Q8 to Q12 are NOT REACHED; the facts after it
      are under AFTER THE STOP with no verdict.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy (operator rule 5);
      the sovereign from the US Treasury; aggregator quotes (price, AWK, year-end closes) flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (Foundations list; Q2's three threats; Q4's tax asset).
- [x] No point-in-time anchor: the run is dated today; rows of every year are admissible.
- [x] Only the arithmetic lines of `tools/run.py` were used, and its stale owner-earnings window (ending 2018) was not used.
- [x] `python tools/check_framework.py` run before the final commit (result in the closing commit message and below).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **The maintenance guess for a utility.** Specific (e) makes the maintenance-only case central "where the
filing allows the guess", and the utility debt credit is applied against "the spending beyond the maintenance guess".
For a utility much of the spending above depreciation is replacement of worn plant (the gas LTIIP, the DSIC) that keeps
the business "in the same economic place" in the physical sense while the regulator turns it into new rate base. The
text does not say whether such replacement is maintenance (it keeps the system running) or growth (it grows the rate base
and the allowed income). This run used depreciation as the guess, which is the generous reading; had replacement spending
been called maintenance, the no-growth case would fall sharply and the OUT would only be firmer. A sentence on regulated
replacement would settle it. (2) **The growth rate for the growth case.** Q7 measures growth on owner cash, which here
swings with gas-cost working capital, so the end-year rate (14.6%) and the halves rate (17.2%) differ and both fail the cap
of specific (f); the cut to sales growth then uses revenue that includes passed-through gas cost, which is not growth the
owner earns on. For a utility the natural growth measure is rate base, which the text does not name; the run used the
text's rule as written and said so. (3) **The target of a signed deal.** Specific (c) speaks of "A deal signed but not
closed" from the buyer's side ("valued beside it as if closed, on the target's own filed record with the financing added
to net debt"). When the company run is itself the target of an all-stock deal, "as if closed" means valuing the acquirer,
which the run cannot do without a second run; this run stated the exchange ratio and the market value of the
consideration and decided the box on the central figure, which the text does require.
