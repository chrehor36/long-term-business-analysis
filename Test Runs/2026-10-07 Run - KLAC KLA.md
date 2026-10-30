# Company Run — KLA Corporation (Nasdaq: KLAC) — 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Dispatched run.** Brief: `Screens/_daily/_dispatch_brief.md` with the slots filled by the dispatching session (KLA
Corporation; process control and yield management equipment for semiconductor manufacturing; fiscal year ends June 30).
Analyst: a dispatched session. Template copied to this file before any fetch (2026-10-07); working folder
`Test Runs/_research 2026-10-07 KLAC/` (raw filings and XBRL downloads under its `cache/`, which is ignored).

**Contamination, declared and not used.** (1) The session context opened with a `git status` snapshot and five recent commit
subjects. They name other runs and research folders of 2026-09-26 to 2026-10-07 (ITW, JKHY, AYI, BDC, CHD, ARCB, ESI, HAS,
GFF, GRMN) and the boxes of four of them. None names KLA. (2) The user's memory index was in context: wave and queue
counts, "57 gate-clearers, nothing buyable", holding reviews owed. It names no ticker. (3) The dispatching message says
earlier run files about KLA exist. I did not open, list or search them and know nothing of their content. (4) `tools/run.py`
printed arithmetic lines only and no rule, id or verdict in this run. None of this was used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $195.36 (2026-10-07; `tools/run.py`, aggregator, live quote only, flagged per operator rule 5). **Ten-for-one split
  effective 11:59 p.m. ET, June 11, 2026**. *(The session was stopped by a usage limit after this section was drafted and
  resumed on 2026-10-10. The price was **not refreshed**; every figure stays at the 2026-10-07 quote and the 2026-10-06 rate.)* (8-K 2026-06-12, accession `0001193125-26-269375`, Item 5.03; announced 8-K
  2026-05-07, `0001193125-26-212093`). Every per-share figure below is on the post-split basis, as the FY2026 10-K restates them.
- **Shares by class** from the latest filing's cover: one class, Common Stock $0.001 par, **1,306,546,783** as of
  2026-08-03 (10-K for FY ended 2026-06-30, filed 2026-08-06, accession `0000319201-26-000027`; `python Screens/cover_shares.py
  KLAC`). Check: balance-sheet count 1,306.983M at 2026-06-30 (issued 2,816.579M less treasury). The cover is later and
  smaller by about 0.4M, which fits continued buying. No 8-K or prospectus after the 10-K changes the count (the 8-K of
  2026-08-06, `0001193125-26-338242`, declares a $0.23 dividend only). No 10-Q has been filed since the 10-K; the first-quarter
  10-Q (September 2026) is not yet due.
- **Market cap:** 1,306.547M × $195.36 = **$255,247M**.
- **Sovereign for the earnings currency (USD):** **5.64%**, US Treasury daily par yield curve, 30-year, 10/06/2026
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4): 10-K FY2026 (filed 2026-08-06, `0000319201-26-000027`): Items 1, 1A (trade and export
  controls), 5, 7, Notes 6, 10, 17 and the balance sheet. 10-K FY2023 (`0000319201-23-000031`): segment gross profit FY2021 to
  FY2023, customer concentration, ECI acquisition. 10-K FY2020 (`0000319201-20-000047`): Orbotech terms, segment gross margin
  FY2018 to FY2020, FY2020 impairment. 10-K FY2019 (`0000319201-19-000031`) fetched for the Orbotech closing. 10-Q for the
  quarter ended 2026-03-31 (`0000319201-26-000016`), fetched. Proxy DEF 14A filed 2026-09-22 (`0001193125-26-397898`): summary
  compensation table and incentive metrics. 8-Ks: 2026-02-05 (`0001193125-26-039637`), 2026-03-12 (`0001193125-26-102999`;
  dividend raised to $2.30 pre-split, new $7B buyback), 2026-05-07, 2026-06-12, 2026-07-28 earnings release (Exhibit 99.1,
  `0000319201-26-000024`), 2026-08-06.
- **One figure cross-checked against the filed statement:** total revenues FY2026 **$13,579,476 thousand** (10-K, Item 7
  table and Note 17) = XBRL 13,579M. Net cash from operations FY2026 **$4,143,079 thousand** (Item 7, Liquidity table) = the
  tool's 4,143. Total assets $17,951,535 thousand and stockholders' equity $6,349,820 thousand (balance sheet) = the tool's
  17,952 and 6,350.
- `python tools/run.py KLAC`, arithmetic lines only. Owner cash (OCF − stock pay − capital spending), USD millions: FY2024
  2,818; FY2025 3,482; FY2026 3,457. Depreciation-and-amortization variant: 2,675; 3,404; 3,428. Stock pay 213; 265; 310,
  tagged `ShareBasedCompensation` all three years; capex 277; 335; 376. The tool found no securities, other stock pay, or
  intangible or software payment lines inside operating cash or beside capex in the window. Five-year (FY2022 to FY2026)
  figures are in the research folder (`q7calc.py`) and under AFTER THE STOP, Q7.

**The balance sheets, FY2018 to FY2026, read before the income account** **[M2025-032]** (the template asks this at Q4; the
file closes before Q4, so it is done here). USD millions, first-filed XBRL (`tools/run.py`; FY2026 cross-checked above):

| June 30 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| equity | 1,621 | 2,659 | 2,665 | 3,378 | 1,401 | 2,920 | 3,368 | 4,692 | 6,350 |
| goodwill + intangibles | 374 | 3,773 | 3,436 | 3,196 | 3,514 | 3,214 | 2,685 | 2,237 | 2,045 |
| cash + securities | 2,880 | 1,739 | 1,980 | n/t | n/t | n/t | 4,504 | 4,495 | 4,902 |
| receivables | 652 | 990 | 1,107 | 1,305 | 1,812 | 1,753 | 1,833 | 2,264 | 2,889 |
| inventory | 932 | 1,262 | 1,311 | 1,575 | 2,147 | 2,877 | 3,035 | 3,212 | 3,649 |
| long-term debt | 2,237 | 3,173 | 3,470 | 3,423 | 6,661 | 5,891 | 5,880 | 5,884 | 5,887 |
| retained earnings | 1,056 | 715 | 655 | 1,277 | 367 | 848 | 1,137 | 2,179 | 3,684 |

(n/t: marketable securities not tagged under the tool's element that year; the FY2024 to FY2026 figures are the 10-K's own
Liquidity table.) What moved and why. (1) **Orbotech, February 2019**, put $3.4B of goodwill and intangibles on a $1.6B
equity base. (2) **FY2022**: debt rose from $3.4B to $6.7B and equity fell to $1.4B, below goodwill and intangibles, so tangible
equity was negative that year. Repurchases were $3,968M that year (XBRL `PaymentsForRepurchaseOfCommonStock`). (3) Since then,
equity has rebuilt to $6.35B on retained profit while buybacks continued. Goodwill and intangibles have fallen to $2.05B through
amortization and four Orbotech-line impairments (Note 6, and AFTER THE STOP, Q6). (4) Retained earnings stay small because
repurchases are charged to them (Note 10). (5) **Receivables grew faster than sales.** In FY2026 they rose 28% against
revenue up 12%, to 21% of revenue (16% in FY2018), and this was while receivables factored without recourse rose from $231M to
$515M (Item 7, Factoring Arrangements). (6) **Inventory** rose 14% against revenue up 12%. It was 27% of revenue in FY2026
against 23% in FY2018. The filer says it raised purchase commitments "to secure the supply of key components" (Item 7,
Executive Summary). Points (5) and (6) are the kind of trend the rows say to "look twice" at **[M1995-064]**; written down here,
not weighed (Q4 is not reached). What the balance sheets cannot say: anything about the technology lead that the economics
rest on. That is the question Q1 decides.

## THE FOUNDATIONS (not a gate)
Two foundations bear on this name. **A share is a business**: would I be content to own KLA if the market closed for five
years **[M1997-109]**? That depends on where its economics will be in ten years, which is Q1's question, not the quotation's.
**The market serves, it does not instruct** **[M2006-077]**: the FY2026 10-K's performance graph shows $100 of KLA stock in
June 2021 worth $978.58 in June 2026 (Item 5). That is a price record and tells me nothing about value; the run does not read
it as evidence of a castle. **The analyst's habits** **[M2025-013]**, **[M2016-055]**: the case for KLA is stated at Q1 as
strongly as I can state it before it is judged. **Contrary evidence, written down as found** **[M1997-127]**: (a) in Step 0,
receivables up 28% and inventory up 14% against sales up 12% in FY2026, with factoring more than doubled; (b) at Q1, the
evidence against my own close: gross margin of 56% to 64% in every fiscal year from FY2011 to FY2026, and process control
GM of 64% to 65% across the FY2024 dip.

## THE STANDING RULE
A part-interest bought for cash and held unlevered puts nothing at risk beyond the sum paid. The rule binds the buyer's
financing and sizing, not the target: "We are never going to risk what we have and need for what we don’t have and don’t
need." **[M2012-081]**; "Never risk permanent loss of capital." **[L2023-005]**. KLA's own debt, the China and export-control
exposure, and customer concentration belong to Q9 and are not reached.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding means "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years. So I’ve got some notion of how the industry will develop and where the company will stand within the
industry." **[M2012-065]**; "being able to asses where the business will be in 10 years" **[M2000-037]**. It is the economics,
not the product: "We just don’t know the economics of it 10 years from now." **[M2000-104]**, and the product may stay opaque
if "I understand the economic dynamics of the industry" **[M2011-014]**.

**What the business is, from the filing** (10-K FY2026, `0000319201-26-000027`, Item 1 and Note 17). Three segments.
**Semiconductor Process Control** (inspection, metrology, software and their service) had revenue of $12,245M of $13,579M in
FY2026 and segment profit of $5,483M of $5,655M. It earned 103% of total segment profit over FY2024 to FY2026, the only years the filer reports segment profit, because the
PCB part lost money in FY2024 and FY2025 after impairments. It also earned 90% of segment gross profit over FY2021 to FY2023
(10-K FY2023, Note 17). So it is the part that **decides** under Q1's parts paragraph and Q2's parts convention.
**Specialty Semiconductor Process** (SPTS deposition and etch) had revenue of $584M and profit of $65M. **PCB and Component
Inspection** (Orbotech's PCB line plus ICOS) had revenue of $750M and profit of $108M. Services are 23% of revenue. One
customer, Taiwan Semiconductor Manufacturing, was about 19% of revenue in FY2026 and FY2025 and 13% in FY2024. China was
29.8%, 33.3% and 42.8% of revenue in FY2026, FY2025 and FY2024.

**The key variables** **[M1998-044]**, and whether each can be foreseen ten years out:
1. *Customers' capital spending.* The filer: "it has historically been cyclical with respect to these manufacturers’ capital
   equipment procurement practices" (Item 1, Industry). FY2009 revenue was $1.52B, with a pre-tax loss of $603M
   (XBRL; FY2008 is not in the tagged data and was not read). Revenue fell 10% in FY2013, 4% in FY2015 and 6.5% in FY2024. The level in any year cannot be foreseen. The
   direction over ten years plausibly can be.
2. *KLA's place in process control through the next technology transitions.* The filer: "The markets for semiconductor and
   electronics technologies are characterized by rapid technological development and product innovation" (Item 1, Research
   and Development), and "The strength of our competitive positions in many of our existing markets is primarily due to our
   leading technology, which is the result of our continuing significant investments in product R&D." Its named rivals
   include ASML, Applied Materials, Hitachi High-Tech and Lasertec, "some of which may have greater financial, research,
   engineering, manufacturing and marketing resources than we have" (Item 1, Competition). R&D ran 11% to 24% of revenue,
   FY2009 to FY2026. **The filer states no market share** in inspection or metrology in the 10-K; it says "industry-leading"
   and "leading supplier".
3. *China.* Export rules from October 2022, October 2023, December 2024, January 2025 and September 2025 restrict what KLA may
   sell, ship and service there. The filer: "future revenue from China as a percentage of our overall revenue may decline", and
   the controls "may [...] make it easier for our China-based competitors to develop and sell their own products and take
   market share from us" (Item 1A). Some shipments "have been held up by U.S. Customs and Border Protection" (Item 1A). This is
   a forecast of two governments' policy.

**The tests, applied.**
- *Test 5, would the insiders write it down?* The rows' measure is whether those who know the field "would not want to put
  down on paper their predictions about where 10 companies you would choose in the tech field would be in 10 years, in terms
  of their economics. They would say, “That’s too hard.”" **[M2000-105]**. KLA's own filing does not write it down. It gives
  one quarter's guidance (Exhibit 99.1, 2026-07-28) and says "Our backlog on any particular date does not provide meaningful
  information about the timing of future revenue recognition" (Item 1, Backlog). Its risk factors put the competitive
  position on continued invention and the China share on rules not yet written. No ten-year economics of process control
  appear in any filing read.
- *Test 6, can I name the winner?* For the last seventeen years, yes: KLA. Ten years forward, the rows separate seeing the
  industry from seeing the company **[M2012-067]**: "Just because Charlie and I can clearly see dramatic growth ahead for an
  industry does not mean we can judge what its profit margins and returns on capital will be as a host of competitors battle
  for supremacy." **[L2009-005]**.
- *Test 7, is the forecast about customers or about technology?* About technology. The customer buys the tool that finds the
  defect at the next node, and the filer says its position rests on "leading technology". That is the case the rows send out
  of the filter: "if something comes in where there’s a technological component that’s of significance, or where we think
  the future technology could hurt the business as it presently exists, [...] it won’t make it through the filter."
  **[M1998-008]**.
- *Test 8, how far off could I be?* **[M2011-084]**. Far. A third of revenue depends on export policy, a fifth on one
  customer, and the core on staying a technology generation ahead of rivals that include ASML and Applied Materials.
- *Test 3, do the past statements tell me the future ones?* **[M2008-033]**. They tell me the past was excellent (below).
  They do not tell me whether the next transition keeps it so: "Companies get left behind. We don’t want to be in businesses
  where companies — where we feel companies can be left behind." **[M1997-023]**. That row is about Intel and is used here
  only as the test it applied, not as a verdict on this industry (Q2's convention on a row about one company).
- *Test 9, do I doubt it is inside?* Yes: "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]**.

**The case for IN, stated as strongly as I can** **[M2016-055]**, and written down as found **[M1997-127]**. KLA's gross margin
was between 55% and 64% in every fiscal year from FY2010 to FY2026. It fell to 43% only in FY2009. Pre-tax margin before
interest has been 19% to 43% in every year since FY2010, higher on average than Applied Materials, Lam Research, ASML, Nova or
Onto over the same span (AFTER THE STOP, Q2). Process Control's segment gross margin was 64.5% in FY2024, the dip year. The
filer says the industry's "overriding requirement" is yield, and process control intensity rises with node complexity (Item 1).
On this reading KLA resembles Lubrizol: a technical product whose economic dynamics, small market, few entrants and a
"connection with customers", were judged without the chemistry **[M2011-014]**, **[M2011-016]**. The record also suggests the
lead has been kept through many transitions, not rebuilt from nothing each time.

**Why that case does not carry the question.** The record is the past, and the speakers gave the technology case its own
answer: "a business that must deal with fast-moving technology is not going to lend itself to reliable evaluations of its
long-term economics." **[L1993-023]**; "Our problem -- which we can't solve by studying up -- is that we have no insights into
which participants in the tech field possess a truly durable competitive advantage." **[L1999-018]**. Lubrizol was a mature
chemistry with a connection to customers; KLA's filing says its position is "primarily due to our leading technology" in
markets of "rapid technological development". The castle the record shows is one "that must be continuously rebuilt"
**[L2007-005]**, and the rows' reason for setting such a business aside is that its future cannot be judged, not that it is
bad: "It doesn’t mean it isn’t a good buy. [...] It just means that we don’t know how to evaluate it." **[M2000-038]**. The
routing is fixed: a business whose ten-year economics cannot be foreseen because its industry changes fast closes at Q1,
TOO HARD **[M1998-008]**, **[M2006-013]**. The China share adds a second variable that is not a business forecast at all.

**The cause.** **NATURE.** The deciding question is whether KLA keeps its process-control lead, and its margins, through ten
years of node, packaging and inspection-physics transitions, and what share of a third of its sales export policy will
allow. It is a forecast the field's insiders do not write down **[M2000-105]**. It is not a filing I have failed to read:
"We couldn't solve this problem, moreover, even if we were to spend years intensely studying those industries."
**[L1993-023]**; "if we can’t make a decision in five minutes, we can’t make it in five months" **[M2008-086]**. A lower price
does not reopen it **[M2000-038]**, and the circle is not widened to find something to buy **[M1995-018]**. The cost is
accepted knowingly. A miss outside the circle is not an error by the rows' count **[M2001-006]**. If KLA were inside the circle,
passing it would be the costliest kind of error, and that is why the doubt test **[M2002-092]** and not the record decides.

- **VERDICT: TOO HARD (NATURE)**, closing the file. Q2 to Q12 NOT REACHED.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED (Q1 closed the file). Facts found are under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. (The balance sheets were read in Step 0.)

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The owner's reporting figures are under AFTER THE STOP, Q7, headed COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**. KLA's ten-year economics rest on keeping a technology lead in process control
through node, packaging and inspection transitions, and on what export policy allows in China (29.8% of FY2026 revenue).
That is a forecast the field's insiders do not write down **[M2000-105]**, **[L1993-023]**. Q7 was not reached. For the owner,
the COMPUTATION under AFTER THE STOP, Q7 gives a range of $43.75 to $95.77 (all-equity) against $195.36. No integrity facts
were found that need the flag.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.

**Q2, the castle.**
- *Parts* (10-K FY2026 Note 17, segment profit; 10-K FY2023 Note 17, segment gross profit), USD millions:

| part | FY2024 profit | FY2025 | FY2026 | share of FY2024-26 profit | FY2021-23 gross profit share |
|---|---|---|---|---|---|
| Semiconductor Process Control | 3,768 | 5,003 | 5,483 | 103% | 90% |
| Specialty Semiconductor Process | 91 | 99 | 65 | 2% | 4% |
| PCB and Component Inspection (PCB, Display and Component Inspection until FY2024) | (470) | (281) | 108 | (5%) | 6% |

  Process Control segment gross margin: 64.6% FY2021, 65.2% FY2022, 63.9% FY2023, 64.5% FY2024, 64.2% FY2025, 63.6% FY2026
  (segment revenue less segment cost of revenues). The PCB part's goodwill was impaired four times (Q6 below), and display
  manufacturing was ended in March 2024 (Note 6).
- *The field's returns over the span*, from each company's own annual filings. Pre-tax earnings plus interest over revenue,
  with the span average, the worst year and R&D over revenue:

| company | filing (latest) | span | avg margin | worst year | latest margin | latest R&D/rev |
|---|---|---|---|---|---|---|
| KLA | 10-K `0000319201-26-000027` | FY2009-FY2026 | 29.1% | -36.0% FY2009 | 43.4% | 11.3% |
| Applied Materials | 10-K `0001628280-25-056742` | FY2009-FY2025 | 20.8% | -9.3% FY2009 | 33.6% | 12.6% |
| Lam Research | 10-K `0000707549-26-000037` | FY2009-FY2026 | 21.5% | -23.0% FY2009 | 36.2% | 10.2% |
| Onto Innovation | 10-K `0001193125-26-066937` | 2009-2025 | 6.8% | -19.9% 2009 | 16.2% | 13.1% |
| Nova (**20-F filer**) | 20-F `0001178913-26-000504` | 2009-2025 | 20.9% | 6.7% 2009 | 34.7% | 16.3% |
| ASML (**20-F filer**, EUR) | 20-F `0001628280-26-011378` | 2009-2025 | 26.2% | -7.5% 2009 | 35.3% | 14.4% |

  Read from XBRL companyfacts of those filings (transcription; `comp.py`, `comp_out.txt`). Onto's tagged history before its
  October 2019 merger is Nanometrics, the surviving registrant. ASML's R&D tag is missing for 2015 and 2016. **Hitachi High-Tech
  and Lasertec are not SEC filers** and were not read, though the filer names both as competitors. Lam Research and Nova are
  not among the competitors KLA's 10-K names. On these figures the field's returns are not ordinary, and KLA's are the highest
  in it. Q2 would have to judge whether that lasts.
- *Share*: no market-share figure in the FY2026 10-K. *Backlog*: $12.57B at 2026-06-30 against $7.86B a year earlier, "due to
  strong demand driven by the AI infrastructure buildout" (Item 1). *Patents*: over 9,100 active (Item 1).

**Q3, capital.** Capital spending was $376M against depreciation and amortization of $394M in FY2026; amortization of
purchased intangibles was $191M (XBRL `AmortizationOfIntangibleAssets`). Working capital was $8.08B, up $1.46B in the year
(Item 7). Purchase commitments were $5.97B, mostly due within twelve months (Item 7).

**Q4, the accounts.** Stock pay was $310M in FY2026 (2.3% of revenue; 7.5% of operating cash). Goodwill and intangible
impairments: $256.6M FY2020; $192.6M and $70.5M FY2024; $230.4M plus $8.7M intangibles FY2025. The earnings release features
"non-GAAP diluted EPS" beside GAAP and reports results "at the upper end of the guidance range". It gives quarterly
guidance for revenue, GAAP and non-GAAP gross margin and EPS (8-K 2026-07-28, Ex. 99.1, `0000319201-26-000024`). These are
carried to Q5 as the convention says **[L2002-041]**, **[L2019-006]**; not weighed here. Receivables, inventory and factoring:
Step 0. Effective tax rate was 13.8% in FY2026, 12.5% in FY2025 and 13.4% in FY2024. The valuation allowance of $356.6M is mainly on
California credit carryforwards (Item 7).

**Q5, the people.** CEO Richard Wallace: total pay $29.95M FY2026, $25.10M FY2025, $22.83M FY2024 (DEF 14A
`0001193125-26-397898`, Summary Compensation Table). The annual bonus is paid on operating margin dollars and a balanced
scorecard. Performance RSUs are paid on relative free-cash-flow margin and non-GAAP EPS, and one EPS tranche "had been earned
at 147% of the target". Hedging and pledging are prohibited. These are not integrity facts; no flag is set.

**Q6, money and owners.**
- *Orbotech*, closed 2019-02-20: $38.86 cash plus 0.25 KLA share for each Orbotech share, total consideration about $3.26B
  (10-K FY2020 `0000319201-20-000047`, Note 1). Part cash and part stock, so it is not the all-stock case **[L2009-019]**.
  Goodwill impairments on the Orbotech lines total $750.1M through FY2025, and display was exited. *ECI Technology*, 2022-02-28:
  $431M (10-K FY2023). *Anchor Semiconductor*, 2021-07-01: $81.7M.
- *Buybacks* (Note 10, by trade date): FY2024 30.32M shares for $1,742.5M (average $57.47); FY2025 30.06M for $2,165.6M
  ($72.05); FY2026 18.24M for $2,303.9M ($126.31). In the fourth quarter of FY2026 the monthly averages were $170.47, $178.64
  and $227.35 (Item 5). FY2022 repurchases were $3,968M, the same year long-term debt rose by about $3.2B (Step 0). The
  programme names no price: "The specific timing, price and size of purchases will depend on prevailing stock prices" (8-K
  2026-03-12). Under Q6's convention a programme with no stated price is read against the bottom of the Q7 range
  **[L2016-002]**. The COMPUTATION range's bottom is $43.75 and its top $95.77, and FY2026's average price paid sits above the
  top. Not weighed. $9.74B of authority remains.
- *Dividends*: $1.06B paid FY2026; quarterly $0.23 post-split, the 17th consecutive annual increase (Item 7).

**Q7, value: COMPUTATION, NOT A CLEARANCE** (the reporting convention of Part VII, The owner's price; at the owner's request;
not a verdict and not entry language).
- Owner cash, OCF less stock pay, all capital spending and cash paid for businesses, USD millions, FY2022 to FY2026:
  2,400; 3,130; 2,815; 3,482; 3,457. **Equity-only base** 3,056.8. **All-equity** (after-tax interest added back at each year's
  effective rate): 2,552; 3,395; 3,084; 3,746; 3,702, **base 3,296.0**. Growth shown, compound between the window's end
  years on aggregate owner cash: 9.74% (all-equity), 9.55% (equity-only). Specific (c): acquisitions deducted, total growth
  credited (default pair). The filer reports no organic growth, so the organic pair cannot be shown. Specific (a): the filer
  describes neither FY2022 nor FY2026 as aberrational, so the literal window is the base and is the window shown. Specific
  (e): the filing gives no maintenance figure, so the all-spending case is central; the D&A variant (equity-only) averages
  3,092.6. Ten years at the shown growth, then zero nominal growth, at 5.64% (`q7calc.py`).
- Net debt at 2026-06-30: debt $5,887M carrying ($5.95B principal) less cash $1,650M and marketable securities $3,253M,
  plus the dividend declared after year-end that Note 19 states ($0.23 × 1,306.5M = $300.5M): **$1,284.5M**. Finance leases are
  "not material". Operating leases ($301.5M of obligations) are left out.
- **(a) VALUE RANGE, all-equity (central): $43.75 to $95.77 a share** (whole business $58.4B to $126.4B less net debt; top to
  bottom 2.16 to 1). The literal window is the same window. Equity-only beside it: $41.48 to $88.41.
- **(b) FAIR PRICE, all-equity (central): $36.55 a share**; equity-only $34.50. This is the price at which the range's
  midpoint earns about ten percent. Definition used (a reporting convention of this run, stated because the text gives
  none): the midpoint stream is the base grown at the rate whose present value at 5.64% equals the range's midpoint (5.78%
  all-equity, 5.65% equity-only), and the fair price is that stream's present value at 10%. Tax is the company's own, inside
  operating cash; there is no conversion, and no carryforward shelter is priced, since the California credits carry a valuation
  allowance.
- Against **$195.36**: the price is about twice the top of the range. The market value of $255.2B against all-equity owner
  cash of $3.30B is a yield of 1.29% against a 5.64% sovereign.

**Q9, exposures.** Coverage: pre-tax earnings plus interest over interest was 20.7 times in FY2026. Senior notes mature FY2029
to FY2063. The $1.5B revolver is undrawn, net leverage is 0.53 against a 3.25 covenant, and ratings are A (Fitch), A2 (Moody's)
and A- (S&P) (Item 7). One customer was 19% of revenue. China was 29.8%, with export rules that are tightening (the Affiliates
Rule is suspended to November 2026). Shipments were held at Customs. Customer deposits have had to be refunded when licences
were refused (Item 1A).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch, written section by section, committed after Step 0 and after Q1
      (write-early). The session was cut by a usage limit before the first commit and resumed on 2026-10-10. The file was on
      disk throughout, and the first commit came on resumption.
- [x] Dispatched: the brief allowed per-question pathspec commits. The lock is the dispatching session's (rule ten (b));
      I did not touch it. The fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. `Test Runs/` was never listed;
      only this run's own two paths were touched. Contamination is declared at the top.
- [x] Every v5 id resolves and every quoted fragment beside an id is in its row (`check_ids.py` in the research folder,
      PASS). Filing facts carry their accessions. Competitor figures carry their filings' accessions and are flagged as XBRL
      transcription.
- [x] The order was kept. Q1's STOP closed the run, and everything after it is facts or COMPUTATION.
- [x] Owner cash is OCF less stock pay, capital spending and acquisitions, never a net-income proxy. The sovereign is the US
      Treasury par curve. The price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as found (foundations line; the case for IN at Q1; receivables and inventory in
      Step 0).
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The fair price is defined in words but not in method.** "The price at which the midpoint of the range earns the floor"
can mean the midpoint value re-priced at 10%, or the midpoint cash stream discounted at 10%. They differ. I used the second
and stated it as a reporting convention of this run. (2) **Specific (a) cannot fire for the business it was written for.** A
year is aberrational only "on the filer's own description", and a semiconductor-equipment filer calls its business
"cyclical" but never calls a year a peak or a trough. So KLA's FY2022 to FY2026 window, running into an AI-driven record
year with backlog up 60%, is taken literally. (3) **The parts threshold** asks for "five-year operating profit". KLA reports
segment profit for three years only and segment gross profit for the three before. I used both and said so. (4) **Q1 and Q2
overlap on rapid change.** The routing sends fast-changing industries to Q1, while the row that best fits KLA, "A moat that
must be continuously rebuilt will eventually be no moat at all." **[L2007-005]**, is Q2's. A seventeen-year record of a
rebuilt moat that held is exactly the case where the two questions point different ways. (5) **Test 5 meets a filer that
does publish forecasts.** KLA gives quarterly guidance and investor-day models (the 8-K of 2026-03-12 cites an investor day;
its slides are not in the filing and were not read). The framework does not say how far ahead "write it down" must reach,
so I read it as ten years, per **[M2000-105]**.

**Errors in the brief**, as instructed to look for. (a) It asks for "share in inspection and metrology as the filer states
it". The FY2026 10-K states no share; it says only "industry-leading" and "leading supplier". (b) Its competitor list
includes Lam Research and Nova, which KLA's 10-K does not name, and leaves out Hitachi High-Tech and Lasertec, which it does
name (flagged as non-filers, which is right). (c) The canonical brief's Read-first item 2 says the template asks Q4's
balance sheets to be read "in Step 0 if the file closes before Q4". The template contains no such instruction; I followed
the brief. (d) The resume message of 2026-10-10 said I was "about to read the framework in full". I had read it and drafted
Step 0 before the stop; nothing turned on it.
