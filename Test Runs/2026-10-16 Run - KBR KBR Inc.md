# Company Run — KBR, Inc. (NYSE: KBR) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching
session at the fold, after the run was committed (0587fe1c): `PORTFOLIO.md` read for this ticker only; not held.*

**Dispatch and contamination, declared at the start.** A dispatched blind analyst run, written unattended overnight. The
dispatching session holds the lock (`Screens/_daily/_overnight.lock` was present when this run started; I did not write or
touch it). Seen by accident and not used: (1) the commit subjects of the five most recent commits in the session context,
which describe a v5 run of another company in the same industry group (AECOM, ticker ACM), its box (OUT at Q2) and its
computed figures; (2) a directory listing of `Test Runs/` filtered to the string "2026-10-16", made to check that my file
name was free, which printed the names (not the contents) of thirty-eight other run files and research folders dated
today; (3) the memory index lines in the session context, which name counts of gate-clearers and a queue state and say
nothing of KBR. No other run file, research folder, holding review, `PORTFOLIO.md`, `Screens/RESUME STATE*`, the run queue
or the prepped reading list was opened, listed beyond that one filtered listing, or searched. The ACM subject line names a
Q2 OUT for a services contractor; I record that I saw it, because it is the kind of prior that could pull this run toward
the same box, and the Q2 section below rests only on KBR's own filings and its rivals' own filings.

**The lines of evidence, chosen by the analyst** *(departure from the canonical brief, stated in the brief: the
dispatcher wrote no list)*. Derived from the FY2025 10-K's Item 1, Item 1A and Item 7 (accession 0001357615-26-000051):
1. **Which part decides.** Two segments with different economics (Item 1, "Our Business Segments"; Item 7 segment table):
   Mission Technology Solutions (government services, mostly cost-reimbursable) and Sustainable Technology Solutions
   (process-technology licensing, engineering services, LNG joint ventures). Chosen because the parts paragraph of Q2
   decides the file on the part with more than half of five-year operating profit.
2. **How the contracts are won and kept** (Item 1A, "Risks Related to Our Industry": competitive award, recompetes,
   multiple-award vehicles, price emphasis, termination for convenience; Item 1, the HomeSafe termination). Chosen because
   this is the castle question for the deciding part.
3. **Contract mix and margins** (Item 1, "Contract Types"; Item 7 backlog by contract type). Chosen because the fee on a
   cost-reimbursable contract is where pricing power would show or not.
4. **Capital: acquisitions, goodwill, debt, receivables sold** (Item 7 cash flows and liquidity; Note 4; Note 11; Note 20).
   Chosen because owner cash and the balance sheet depend on them.
5. **The planned spin-off of MTS** (Item 1; 10-Q for the quarter ended 2026-07-03, Note 18, accession
   0001357615-26-000172). Chosen because a buyer today buys both parts and the separation changes debt and structure.
6. **Legal and government matters** (Item 7 "U.S. Government Matters"; the 2023 legacy legal settlement in the income
   statement). Chosen because they bear on Q4, Q5 and Q9.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $36.38 (2026-10-16; `tools/run.py` live quote, an AGGREGATOR quote, flagged per operator rule 5; the date
  is today and the figure may be intraday).
- **Shares by class** from the latest filing's cover: one class, common stock $0.001 par, **126,067,755** shares
  outstanding as of 2026-07-22 (10-Q for the quarter ended 2026-07-03, filed 2026-07-30, accession
  0001357615-26-000172; `python Screens/cover_shares.py KBR`). Checked against the 10-Q balance sheet: 183,154,727 issued
  less 57,086,972 treasury = 126,067,755, the same. The two 8-Ks filed after that 10-Q (2026-10-01, accession
  0001357615-26-000177, a director appointed; 2026-10-16, accession 0001357615-26-000181, bylaws amended) change no share
  count. The company repurchased $25M of stock in the second quarter (10-Q equity statement); any purchases after
  2026-07-22 are not yet filed.
- **Market cap:** $36.38 × 126.068M = **$4,586M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-15 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the 10-K for the fiscal year ended 2026-01-02 (filed 2026-02-26, accession
  0001357615-26-000051): Items 1, 1A, 7, the four statements, Notes 4, 5, 6, 12 (tax), 20 (receivables sold); the 10-K for
  FY2023 (filed 2024-02-20, accession 0001357615-24-000016): cash-flow statement, equity statement, segment table; the
  10-K for FY2021 (filed 2022-02-22, accession 0001357615-22-000012): cash-flow statement, stock pay; the 10-Q for the
  quarter ended 2026-07-03 (accession 0001357615-26-000172): balance sheet, equity statement, MD&A, Note 18; the proxy filed
  2026-03-30 (DEF 14A, accession 0001104659-26-036847), searched for its pay metrics only (the file closed before Q5);
  8-Ks of 2026-07-10 (accession 0001357615-26-000157, executive severance agreements amended), 2026-07-30 (accession
  0001357615-26-000170, second-quarter release), 2026-10-01 and 2026-10-16. **One figure cross-checked against the filed
  statement:** operating cash flow from continuing operations FY2025, $557M in the XBRL tag `tools/run.py` read and $557M
  on the filed consolidated statement of cash flows (10-K, accession 0001357615-26-000051, page 70). A second check:
  `tools/run.py` printed FY2023 operating cash flow as $331M, which is the total-company figure on the FY2023 10-K's own
  statement (accession 0001357615-24-000016), while for FY2025 it printed the continuing-operations figure; the tool mixes
  bases across years, so the series below is taken from the filed statements, not from the tool's table.
- **`tools/run.py` arithmetic lines only** (the tool's yield, "growth the price assumes" and ratio lines are not used,
  Part VII). Owner cash below is built from the filed statements by the analyst; the tool found no stock pay in XBRL ("n/f")
  and its owner-earnings column deducts none, which the filed equity statements correct.

**Owner cash after every real cost, from the filed statements (USD millions).** Operating cash flow as originally filed,
total company (for FY2023 to FY2025 the continuing and discontinued lines added, so that the HomeSafe joint venture's
losses, a real cost of a contract KBR ran, stay in); stock pay from the equity statements; capital spending from the
investing section (with HomeSafe's own capital spending added for FY2024 and FY2025); acquisitions net of sales of assets or
investments.

| FY | Op. cash | Stock pay | Capex | Owner cash before purchases | Acquisitions, net of sales | Owner cash after purchases | Revenue | Source |
|---|---|---|---|---|---|---|---|---|
| 2021 | 278 | 12 | 30 | **236** | 399 − 44 = 355 | −119 | 7,339 | 0001357615-22-000012; 0001357615-24-000016 |
| 2022 | 396 | 21 | 71 | **304** | 73 − 47 = 26 | 278 | 6,564 | 0001357615-24-000016 |
| 2023 | 331 | 20 | 80 | **231** | 0 | 231 | 6,956 | 0001357615-24-000016 |
| 2024 | 450 + 12 = 462 | 22 | 52 + 25 = 77 | **363** | 738 − 7 = 731 | −368 | 7,710 | 0001357615-26-000051 |
| 2025 | 557 − 33 = 524 | 21 | 42 + 12 = 54 | **449** | 14 − 3 = 11 | 438 | 7,786 | 0001357615-26-000051 |
| **5-yr average** | | | | **316.6** | 224.6 | **92.0** | | |

Notes on the series: (i) depreciation and amortization ran $137M to $169M a year against capital spending of $30M to
$80M; the gap is mostly the amortization of purchased intangibles (intangibles net $727M at FY2025, accumulated
amortization $501M), so capital spending, not D&A, is the measure of what the business spends to stay in place, and
the tool's "D&A basis" line overstates the need. (ii) The company sells receivables without recourse to MUFG Bank under
a standing programme ($2,143M derecognized in FY2025, $3,077M in FY2023, $2,991M in FY2021; Note 20 of each 10-K); the
year-end balance sold is not stated in the passages read, so the share of operating cash that rests on the programme is
not known. (iii) Returns of capital from equity-method joint ventures (investing section: $198M in FY2022, $60M, $36M,
$82M after) are left out of owner cash; the distributions of their earnings ($47M to $170M a year) are inside operating
cash, which is how Q4's equity-method paragraph counts such income. (iv) FY2025's operating cash was lifted by "the
resolution of an outstanding unapproved change order within our Mission Technology Solutions segment" and by lower
pension funding (10-K Item 7, Operating Activities); the amount of the change order is not stated there. (v) Interest paid
is inside operating cash ($63M in FY2021 rising to $141M in FY2025); owner cash before interest is the column plus cash
interest after tax at the company's rate.

**The balance sheets, eight year-ends, read first** **[M2025-032]** (Q4's rule; read here because the file closes before
Q4). From `tools/run.py`'s ten-year table (first-filed XBRL vintage, accessions 0001357615-19-000030 through
0001357615-26-000051), checked for FY2024 and FY2025 against the filed balance sheet (accession 0001357615-26-000051, page
68), USD millions:

| Year-end | Equity | Goodwill | Intangibles | Tangible equity | Cash | Debt (current + long-term) | Retained earnings |
|---|---|---|---|---|---|---|---|
| 2018 | 1,718 | 1,265 | 516 | −63 | 739 | 1,248 | 1,258 |
| 2019 | 1,843 | 1,265 | 495 | 83 | 712 | 1,210 | 1,441 |
| 2020 | 1,580 | 1,761 | 683 | −864 | 436 | 1,596 | 1,305 |
| 2021 | 1,687 | 2,060 | 708 | −1,081 | 370 | 1,868 | 1,260 |
| 2022 | 1,620 | 2,087 | 645 | −1,112 | 389 | 1,740 | 1,410 |
| 2023 | 1,383 | 2,109 | 618 | −1,344 | 304 | 1,832 | 1,072 |
| 2024 | 1,453 | 2,630 | 763 | −1,940 | 342 | 2,569 | 1,367 |
| 2025 | 1,503 | 2,677 | 727 | −1,901 | 500 | 2,596 | 1,697 |
| 2026-07-03 (10-Q) | 1,636 | 2,668 | 694 | −1,726 | 312 | 2,552 | 1,853 |

What the figures say: in seven years goodwill and intangibles rose by $1.6B (2018 $1,781M to 2025 $3,404M) while equity
did not rise at all ($1,718M to $1,503M) and debt doubled ($1,248M to $2,596M); the purchases (the 2020 and 2021 deals,
then LinQuest for $739M in August 2024) were paid with borrowed money and retained cash, and the owners' stake in tangible
assets went from about nil to minus $1.9B. Retained earnings rose only $439M from 2018 to 2025 after dividends; the
treasury account grew from $1,143M (end of 2022) to $1,842M (mid-2026), so buybacks took out more than was retained. Cash
fell from $739M to $312M. What they do not say: a services contractor needs little tangible capital, so negative tangible
equity is not by itself distress; the receivables on the balance sheet ($1,109M at mid-2026, about 51 days of revenue) are
net of the receivables sold, so the balance sheet understates the working capital the business actually carries. What
they cannot say: the condition of the classified programmes, which the 10-K says "may limit investor insight into portions
of our business" (Item 1A). The accumulated other comprehensive loss of $941M (mostly the frozen U.K. pension and
currency) sits against a pension surplus of $84M recognized at FY2025.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own it "if the market closed for five years" **[M1997-109]**,
and here the business a buyer would own changes shape in eleven weeks, since the 10-Q says the spin-off of MTS targets
"completion on January 4, 2027" (Note 18, accession 0001357615-26-000172); a buyer today buys both companies. No macro
enters: the defence budget figures that fill the MD&A's "Business Environment and Trends" (an $839 billion appropriation,
a desired $1.5 trillion) are forecasts of government conduct, and "macro conclusions are — just never enter into the
discussion" **[M2000-094]**; the run reads the business's own record. Who is paid to tell you: the release of 2026-07-30
features "Adjusted EBITDA" and an "Adjusted operating cash flows" guidance range in its first lines (accession
0001357615-26-000170); those are the company's words about itself and are read as such. **Contrary evidence, written down
as found** **[M1997-127]**: (1) the MTS castle has real features that argue for it, which a services reading could miss:
long-term U.K. PFI contracts of 15 to 35 years with 39% of backlog, staff with "high-level security clearance", decades of
relationships, and an $8 billion-ceiling single-award 20-year Antarctic contract won in 2026 (10-K Item 1; release of
2026-07-30); (2) KBR's consolidated operating margin rose every year from 3.1% (FY2021) to 10.0% (FY2025) on the filer's
XBRL, a widening that a castle test must explain rather than ignore; (3) against the business, the FY2025 cash was helped
by a one-time change-order resolution, the HomeSafe contract was "unexpectedly terminated" by U.S. Transportation Command
in June 2025, MTS revenue fell 4% in the first half of 2026, and "$10.6 billion of awarded work [is] currently under
protest" (release of 2026-07-30). I looked for "what’s wrong" and "what you’re missing" in each **[M2025-013]**.

## THE STANDING RULE
Does owning this put the buyer at risk of ruin? No, if it is bought with the buyer's own money and sized so that a large
fall changes nothing: "We are never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**,
and "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing in the business requires the buyer
to put up more cash after purchase; the target's own debt is Q9's question.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding means "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**; the question is the economics, not the product: "It’s the predictability of
  the economics of the situation 10 years out" **[M2000-104]**. By parts (Q1's holding-company paragraph extended to
  operating segments, CONVENTION of the framework): the part that matters is the part that decides under Q2's parts
  paragraph, here MTS (61% of five-year segment operating profit; the table is under Q2).
- **The key variables of MTS and whether they are foreseeable** **[M1998-044]**. MTS sells the time of engineers,
  scientists and logisticians to the U.S., U.K. and Australian governments, "primarily [...] under cost-reimbursable
  contracts with the DoW and other U.S. governmental agencies" (10-K Item 1, accession 0001357615-26-000051). Its economics
  turn on three variables: (a) how much of the customers' funded work it wins and keeps at each recompete; (b) the fee the
  customer allows above allowable cost (the FAR "define[s] allowable and unallowable costs", Item 1); (c) the little capital
  it needs ("Low capital intensity business model", Item 1). The second and third are stable and readable from the past
  statements, which is test 3's question, whether "the financial statements will tell me the information that’s useful to
  me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**: the
  segment margin has run from 5.0% to 8.3% (FY2023 to FY2025), and the field's margins (Q2) sit in the same band. The
  first variable is a competitive question, which is what Q2 asks. The total of government spending is a macro quantity
  this run does not forecast **[M2000-094]**.
- **The contrary evidence, written down** **[M1997-127]**. (1) The filer says its markets "are characterized by rapidly
  changing technology" (Item 1A, "Heightened competition"); rapid change is owned by Q2, and Q1 closes TOO HARD only
  where it puts the ten-year economics out of reach **[M1998-008]**. What KBR sells is staff paid by the hour or at cost
  plus fee; the technology its staff work on changes, the economic form of the contract does not, so I do not read the
  sentence as putting the economics out of reach. (2) "A significant portion of our revenue is from contracts [...] that
  are classified", and investors "may have limited insight into a substantial portion of our business" (Item 1A). This
  hides programmes, not the contract form or the margins, which are reported by segment. (3) STS's economics (licences
  sold into ammonia, refining and energy-transition projects, and equity earnings from LNG construction joint ventures)
  are lumpier and harder to foresee; STS does not decide (Q2 table), so it does not keep the whole outside the circle on
  this paragraph's threshold. (4) The spin-off splits the business in eleven weeks; each part is read on its own segment
  record, which the 10-K reports.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. My doubt
  is about the castle, not about the economics: I can say what MTS will look like in ten years in a general way (a low-
  margin, low-capital government contractor whose revenue moves with what it wins), and the question whether it keeps
  what it wins is Q2's.
- **VERDICT: IN.** The deciding part's economics can be foreseen in the general way the rows ask **[M2012-065]**,
  **[M2011-014]** ("What is important is that I understand the economic dynamics of the industry"); the filing facts are
  the contract form (cost-reimbursable, FAR-governed), the segment margins, and the low capital need, all in the 10-K
  (accession 0001357615-26-000051). Carried to Q2: the filer's own sentences on competition, recompetes and price.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**.

**The parts table** (a business of parts, CONVENTION of the framework: a part decides at more than half of five-year
operating profit; lumping parts together "impedes analysis" **[L2008-005]**). Segment operating income, USD millions, from
the 10-K segment tables (FY2021 and FY2022 under the former segments, Government Solutions and STS, 10-K FY2023,
accession 0001357615-24-000016; FY2023 to FY2025 as recast to MTS and STS, 10-K FY2025, accession 0001357615-26-000051).

| Part | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | 5-yr sum | Share of segment total | Castle | Decides |
|---|---|---|---|---|---|---|---|---|---|
| Government services (GS, then MTS) | 414 | 441 | 256 | 415 | 463 | 1,989 | **61%** | open (below) | **yes** |
| Sustainable Technology Solutions | −30 | 47 | 354 | 405 | 477 | 1,253 | 39% | not judged (does not decide) | no |
| Corporate | −153 | −145 | −161 | −161 | −162 | −782 | | | |

Two cautions on the table, written down as found **[M1997-127]**: the FY2025 recast moved the international government
business into both segments, so the FY2021 and FY2022 columns are on the older and wider government definition; and on the
three recast years alone STS carries 52% (1,236 of 2,370). On the convention's five-year figure the government-services
part decides; with the old FY2023 GS figure ($285M) in place of the recast one, it still carries more than half. STS's
FY2021 and FY2022 figures carry the Ichthys LNG and power-plant charges ($137M non-cash in FY2022, FY2023 10-K Item 7);
with that FY2022 charge added back, STS's five-year share is still about 41%.

**The castle tests on the deciding part (MTS), each with its filing fact** (10-K FY2025, accession 0001357615-26-000051,
unless stated).
1. **What keeps it standing, and how permanent** **[M1995-038]**. The filer names its advantages as its people, cleared
   staff, technical expertise, "Decades of enduring relationships", and "multi-year, mission-critical programs" (Item 1,
   Competitive Advantages). The permanence is stated in another part of the same filing: "Many of our existing contracts
   must be recompeted when their original period of performance ends, representing opportunities for competitors to take
   market share away from us or for our customers to obtain more favorable terms" (Item 1A). The advantage lasts one
   period of performance at a time. No recompete win rate is reported (a search of the 10-K, the 10-Q and the release of
   2026-07-30 for "win rate", "recompet" and "incumbent" found one passage, the one quoted).
2. **Would it stand without the lord** **[L2007-006]**. Yes, in the sense the row asks: no superstar is needed. The test is
   passed and does not help, since what the business lacks is not a manager but a barrier.
3. **The money test** **[M2011-015]**. Could a well-funded rival take it? The filer answers: "We compete with larger
   companies that have greater name recognition, financial resources and a larger technical staff. We also compete with
   smaller, more specialized companies that are able to concentrate their resources on particular areas. Additionally, we
   compete with the U.S. government’s own capabilities", and rivals may "initiate or withstand substantial price
   competition" (Item 1A, Heightened competition). The rivals are in every bid already, and the customer can also do the
   work itself. "If the answer had been yes, we wouldn’t have done it" **[M2011-015]**; here the filer says yes in its own
   words. It is a field where "you better be running very fast because there are a lot of other people that are going to
   be running and looking at what you’re doing" **[M2012-106]**.
4. **Pricing power and the agony before a rise** **[M2005-020]**. There is no list price to raise. On cost-reimbursable
   work the customer defines which costs are allowable, audits them (DCAA, DCMA) and can recover what it disallows (Item 1,
   Government Contracts and Regulations); "U.S. government procurement practices sometimes emphasize price over qualitative
   factors, such as technical capability and past performance. As a result of these competitive pricing pressures, our
   profit margins on future U.S. government contracts may be reduced" (Item 1A); and the government "has (and has
   exercised in the past) the ability to unilaterally definitize contracts" (Item 1A, UCAs). The customer, not the seller,
   sets the price, the case of the business whose price someone else sets: "whatever he charged for gas was my price"
   **[M2012-109]**.
5. **Would the customer still choose it over the low bid** **[M2017-009]**. The filer's own sentence, twice in Item 1A, is
   that procurement "sometimes emphasize[s] price over qualitative factors, such as technical capability and past
   performance". That is the failing answer: the customer buys on the low bid at least some of the time, and past
   performance, the factor that would otherwise protect the incumbent, is the factor the filer says can be outweighed.
   Against this, written down **[M1997-127]**: some of the work is of the kind where "people don’t simply just take the low
   bid" **[M2016-006]** (human spaceflight, intelligence, the 20-year Antarctic award), and the release of 2026-07-30 says
   "approximately $10.6 billion of awarded work currently under protest", which means KBR won those awards. But a protest
   is the losing bidders attacking each award as it is made, so the same fact shows the castle stormed at every gate.
6. **What the customer can do at will.** "nearly all contracts allow customers to terminate the agreement at any time for
   convenience" (Item 7, Backlog); "Generally, our customers have the contractual right to terminate or reduce the amount
   of work under our contracts at any time" (Item 1). The instance: U.S. Transportation Command "unexpectedly terminated
   HomeSafe's role in the Global Household Goods Contract" in June 2025, and the joint venture, 72% KBR's, had ceased all
   operations by year-end (Item 1, Significant Joint Ventures). One party is enough: "one competitor is frequently enough
   to ruin a business" **[M2012-108]**; here the one party is the customer, who also writes the rules.
7. **Widening or narrowing** **[M1999-108]**. The segment margin widened (MTS 5.0% FY2023, 7.5% FY2024, 8.3% FY2025), which
   the filer credits to the LinQuest acquisition, a $26M legacy-claim resolution and mix (Item 7). The rivals' margins
   widened in the same years (the competitor row below), so the widening is the field's, not KBR's. The customer is moving
   the other way: "shifts in the buying practices of U.S. government agencies, such as increased usage of fixed-price
   contracts, multiple-award contracts and small business set-aside contracts, could have adverse effects on government
   contractors, including us" (Item 1A), and the FAR overhaul "could transform how contracts are awarded, negotiated, and
   managed" (Item 1A). In the first half of 2026 MTS revenue fell 4% on lower EUCOM contingency work (10-Q MD&A, accession
   0001357615-26-000172), and the release adds "reduced activity within U.S. Government Federal Civilian Clients".
8. **What could destroy, modify or reduce it** **[M2000-014]**: the customer's budget decisions, its acquisition reforms,
   its own in-house capability and the recompete calendar, all named by the filer (Item 1A).

**The competitor row.** The 10-K names no rival (a search for "competitor", "competition", "compete" and the names of the
large U.S. government-services firms found only the general sentences quoted above). The rivals below are therefore a
**CONVENTION of this run**: the three largest U.S. government-services companies that file with the SEC and sell the same
kind of work (engineering, analytics, mission support) to the same customers; rationale: the brief allows up to three when
the 10-K names none, and these are the "larger companies" the filer describes. Metric: operating income over revenue, each
from the company's own 10-K XBRL facts (newest filed vintage; transcription only; the accession of the 10-K that last
filed each value is in `Test Runs/_research 2026-10-16 KBR/peers_output.txt`).

| Fiscal year | KBR | Leidos (LDOS) | CACI | Booz Allen (BAH, FY to March) |
|---|---|---|---|---|
| 2016 / 2017 | 0.7% | 5.9% | 7.1% | 8.7% |
| 2017 / 2018 | 6.3% | 5.5% | 6.8% | 8.4% |
| 2018 / 2019 | 9.5% | 7.3% | 7.6% | 9.0% |
| 2019 / 2020 | 6.4% | 8.2% | 7.6% | 9.0% |
| 2020 / 2021 | 1.0% | 8.1% | 8.0% | 9.6% |
| 2021 / 2022 | 3.1% | 8.4% | 8.9% | 8.2% |
| 2022 / 2023 | 5.2% | 7.6% | 8.0% | 4.8% |
| 2023 / 2024 | 6.5% | 4.0% | 8.5% | 9.5% |
| 2024 / 2025 | 8.5% | 11.0% | 8.9% | 11.4% |
| 2025 / 2026 | 10.0% | 12.3% | 9.6% | 9.2% |
| Latest 10-K accession | 0001357615-26-000051 | 0001336920-26-000030 | 0001628280-26-054195 | 0001628280-26-037521 |

(KBR's column is consolidated, both segments; MTS alone ran 5.0% to 8.3% over its three recast years. Booz Allen's revenue
fell from $11,980M to $11,217M in its year to March 2026, on its own XBRL facts: the same customer cutting the same kind of
work.)

**The field's returns over the last full cycle, judged in words** (CONVENTION of the framework: "ordinary" carries no
figure). Over ten years the four firms earned operating margins of roughly 4% to 12% of revenue, close together and moving
together; none held a margin the others could not reach, and each dipped in the years its own charges fell (KBR 2020 and
2021, Leidos 2023, Booz Allen 2023). On tangible capital the returns are high, because the business needs little of it;
but the owners of each paid for that business in goodwill (KBR's $2.7B against $1.5B of equity), and the margin is allowed
by the customer for the whole field. The returns on tangible capital are not what the castle protects; they are what the
customer leaves in a labour business. I do not close on "ordinary returns"; the file closes on the castle shown open.

**What argues for the castle, in full** **[M1997-127]**. Incumbency and past performance count in the evaluations; security
clearances take time to obtain; the U.K. PFIs run 15 to 35 years with contracted remuneration (Item 1); the Antarctic award
is single-award for 20 years; MTS backlog was $12.7B at FY2025, about 2.3 years of MTS revenue (Item 7). These are real, and
they make MTS a steady business for a few years. But each is a contract with a term, a termination-for-convenience clause
and a recompete at its end, on the filer's own description, and the PFIs are fixed-price and sit in equity-method joint
ventures (Aspire 45%, Affinity 50%). Steadiness for the backlog's life is not a castle for ten to twenty years: "A moat
that must be continuously rebuilt will eventually be no moat at all" **[L2007-005]**, and here the rebuilding is written
into every contract's period of performance.

**STS, the part that does not decide.** Its licensed process technologies (over 85, ammonia among them) may be a castle;
its engineering services and LNG joint-venture earnings are project work with joint and several partner liability (Item 7,
Off-Balance Sheet Arrangements). It is not judged here, because the file closes on the deciding part (the parts
CONVENTION); its figures enter the computation beneath the stop.

- **VERDICT: OUT.** The castle of the deciding part is shown open on the filer's own evidence: its contracts are recompeted
  as "opportunities for competitors to take market share away from us", its customer "sometimes emphasize[s] price over
  qualitative factors", can terminate "at any time for convenience" and did so to HomeSafe, and competes with it from "the
  U.S. government’s own capabilities" (10-K Items 1, 1A and 7, accession 0001357615-26-000051). The money test is answered
  yes by the filer **[M2011-015]**; the customer sets the price **[M2012-109]**; the low bid can win **[M2017-009]**; and the
  field's margins move together with no lasting edge for any firm (the competitor row). A castle shown open closes OUT,
  "If the answer had been yes, we wouldn’t have done it" **[M2011-015]**, not TOO HARD, since its future is judged from the
  evidence rather than left unknown; the three boxes are "in, out, and too hard" **[M2006-013]**. Q3 to Q12 are NOT
  REACHED as clearances.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED (Q2 closed the file OUT). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The eight balance sheets were read in Step 0 **[M2025-032]**; the facts found on the accounts are
under AFTER THE STOP.

## Q5 — WHO RUNS IT. STOP on integrity.
NOT REACHED. Integrity facts found before the stop are recorded under AFTER THE STOP, not judged; the box line carries the
flag (Part VII).

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts under AFTER THE STOP, including the prices paid for repurchases against the computed bottom of the range.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a verdict. The figures the owner asked for are computed below under the protocol's heading.

### COMPUTATION, NOT A CLEARANCE
*(operator rule 3: valuation arithmetic after a closing STOP; it carries no entry language and changes no box.)* Script and
output: `Test Runs/_research 2026-10-16 KBR/q7_compute.py`, `q7_output.txt`. Built by Q7's range convention, the floor
convention, the six specifics and the four PG specifics, as the text stands.

- **Cash input.** Owner cash after every real cost, five-year average FY2021 to FY2025 (Step 0 table), before purchases:
  $316.6M on the equity-only basis (after interest); **$391.0M on the all-equity basis** (cash interest paid added back after
  tax at the company's 25% rate of FY2024 and FY2025: $283M, $354M, $308M, $456M, $555M). After the company's own tax,
  with no conversion (Q7, Whose tax). Tax shelter check: the company's effective rate (25% to 28%) is above the 21%
  statutory rate, so the carryforward convention does not apply; the carryforwards on the FY2025 balance sheet (foreign tax
  credits $60M, losses $70M, other credits $37M, against a $124M valuation allowance; 10-K Note 12) are worth at most about
  $43M net, $0.34 a share, and are not added. Cash taxes paid ran $47M to $83M against book provisions of $92M to $156M;
  the passages read do not say why, so a variant at the book provision is shown beside (below).
- **Acquisitions, specific (c).** Net purchases over the window were $1,123M against $1,583M of owner cash before purchases,
  71%, more than half: KBR is a **serial acquirer** under the 2026-10-12 convention, and the central figure is the
  **organic pair**, purchases left out, organic growth credited. The filer reports no organic growth in the 10-K, 10-Q or
  release read (a search for "organic" in the 10-K found only "fund organic growth" in Item 1). **CONVENTION of this run:**
  organic growth is taken as at most the total revenue growth over the window, 1.49% a year (FY2021 $7,339M to FY2025
  $7,786M), since total growth includes the acquired revenue and so bounds organic growth from above; rationale: the
  framework asks for the filer's own organic figure, the filer gives none, and the bound is the least favourable figure that
  does not invent one. The default pair (purchases deducted, total growth credited) is shown beside.
- **Growth and the cap, specifics (f) and (a).** Owner cash before purchases grew 17.4% a year (FY2021 $236M to FY2025
  $449M), most of it bought (LinQuest) and lifted in FY2025 by a change-order resolution the filer names as the main cause
  of that year's rise (Item 7). Carried ten years, 17.4% would need owner cash of about 21.6% of sales against a highest
  share of 7.1% in the years read, so the cap cuts it to the business's own sales growth, 1.49%, the same figure as the
  organic bound. No window year is called aberrational by the filer in terms that set a cycle base, so the literal
  five-year window is the base; FY2025 alone is shown beside.
- **Working capital, specific (d):** inside operating cash. **Maintenance, specific (e):** capital spending ($30M to $80M a
  year) is taken as the maintenance need; the business is capital-light by the filer's description and the filing does not
  split growth spending from maintenance, so the all-spending case is the central one.
- **Net debt, all-equity basis:** borrowings $2,552M (current $49M, long-term $2,503M, 10-Q 2026-07-03) plus finance leases
  about $10M (FY2025 contractual table) less cash $312M and available-for-sale debt securities $50M = **$2,200M**; operating
  leases ($246M non-current liability) left out, as the convention says. No subsequent event in the 10-Q states an amount;
  the planned MTS borrowing to pay a distribution to KBR, which KBR says it will use to repay debt (10-K Item 7, Future uses
  of cash), moves debt between the two companies and leaves the combined net debt about where it is.
- **Discount rate:** the 30-year Treasury, 5.43%. Ten years, then zero nominal growth.

| Case (all-equity, central) | Growth, years 1 to 10 | Value of the business | Per share less net debt | Expected return at $36.38 |
|---|---|---|---|---|
| No growth | 0% | $7,201M | **$39.67** | 5.76% |
| Shown growth, capped | 1.49% | $8,109M | **$46.88** | 6.46% |

- **Value range (all-equity, central): $39.67 to $46.88 a share against $36.38.** Width 1.18 to one. Equity-only beside:
  $46.25 to $52.09.
- **The floor, tested first** (CONVENTION of the framework, 2026-10-10). No case earns about ten percent at the price: the
  all-equity cases return 5.8% and 6.5%, the equity-only cases 6.9% and 7.7%; FY2025 alone, the best year, returns 8.2% at
  no growth and 9.1% at the capped growth; the book-tax variant returns 5.0% and 5.6%; the default pair (purchases
  deducted, $166M a year all-equity) returns 2.5% at no growth. To earn ten percent at the price, the all-equity cash would
  have to grow 8.0% a year for ten years, five times the revenue growth shown. On Q7's own close this computation would be
  **OUT**: "there’s just a point at which we drop out of the game" **[M2003-149]**. The range sitting above the price is not
  a contradiction: the range is discounted at the long government rate, and the floor asks for about ten percent; the
  price is below the range and still too high for the floor.
- **FAIR PRICE (the operator's reporting figure; never a verdict; Part VII): $15.21 a share, all-equity basis (central)**:
  the no-growth case at ten percent is $13.56 a share and the capped-growth case $16.87, averaged, each after the company's
  own tax and less net debt of $2,200M. **Equity-only figure beside: $26.45** ($25.11 and $27.79). Neither is a buy signal.
  No cheap price is reported.
- **Q6's buyback line, written back here for the record** (Q6 not reached): the repurchases of FY2025, $329M (equity
  statement), averaged about $51 a share (treasury shares rose by 6.40M; this mixes in employee withholding and ESPP
  reissues), and the last quarter's were at $42.70 (10-K Item 5); both are above the computed bottom of the range ($39.67)
  and far above the fair price. The programme states a dollar authorization ($750M) and no price (Item 5).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US? WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT**, decided at **Q2**: the castle of the deciding part (Mission Technology Solutions, 61% of five-year segment
operating profit) is shown open on the filer's own 10-K (recompetes "representing opportunities for competitors to take
market share away from us"; procurement that "sometimes emphasize[s] price over qualitative factors"; termination for
convenience, exercised against HomeSafe; the government's "own capabilities" as a rival) and the competitor row shows a
field of close, co-moving margins. COMPUTATION, NOT A CLEARANCE beneath the stop: value $39.67 to $46.88 all-equity
against $36.38, no case earns the floor, fair price $15.21 ($26.45 equity-only). **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on later questions, each with its source **[M1997-127]**; no verdict; the box unchanged,
operator rule 2.)*

**Q3 (capital).** Capital spending ran $30M to $80M a year against revenue of $6.6B to $7.8B (Step 0 table); the
filer calls the model "Low capital intensity" (10-K Item 1). Growth has been bought: $1,123M of net purchases in five years
(the 2021 deals, net $355M; LinQuest $738M in 2024) and $832M in FY2020 before the window (10-K FY2021 cash-flow statement,
accession 0001357615-22-000012), while revenue grew 1.49% a year over FY2021 to FY2025. The purchases added $1.6B of
goodwill and intangibles from 2018 to 2025 (Step 0).

**Q4 (the accounts).** (1) The release of 2026-07-30 leads with "Adjusted EBITDA" and "Adjusted EPS" and gives
fiscal-2026 guidance ranges for revenue, adjusted EBITDA, adjusted EPS and "Adjusted operating cash flows", which it
"reaffirms" (accession 0001357615-26-000170); these are the adjusted-figure and guidance habits the framework weighs at Q4
and judges at Q5. (2) Receivables are sold without recourse under a standing programme ($2.1B to $3.1B a year; Note 20),
with the balance sold at year-end not found in the passages read. (3) Distributions from equity-method joint ventures were
$170M in FY2025 against equity earnings of $210M; returns of joint-venture capital ($198M in FY2022, $82M in FY2025) sit in
investing. (4) A legacy legal settlement cost $144M in 2023 (10-K FY2023 Item 7 and Note on the Howard qui tam: KBR "paid
$109 million, of which $57 million comprised restitution damages, and $35 million to the relators as attorney’s fees",
denying liability; accession 0001357615-24-000016). (5) Convertible notes and warrants were settled in 2023 and 2024 for
cash: $843M paid to settle notes, $493M received on the note hedge, $217M and $33M paid on warrants, with $494M of
"Charges associated with Convertible Notes" in FY2023 (cash-flow and income statements). (6) Spin-off costs and other
charges were $46M in the first half of 2026 (10-Q).

**Q5 (integrity, recorded not judged).** (1) The guidance and the featured adjusted figures above. (2) The 2023 qui tam
settlement above, with restitution damages paid and liability denied. (3) On 2026-07-10 the executive severance and
change-in-control agreements were amended: the cash severance multiple for officers other than the CEO rose from 1.0x to
1.5x, and "Cause" was redefined so that it "shall not include [...] any failure to achieve any performance targets" (8-K,
accession 0001357615-26-000157). (4) The proxy's short-term incentive pays on adjusted EPS, adjusted operating cash flow
and individual KPIs, and the committee applied "55.8% negative discretion" to the adjusted-EPS result "to reflect the loss
from discontinued operations from HomeSafe Alliance" (DEF 14A, accession 0001104659-26-036847); the long-term award pays
on TSR and three-year book-to-bill. A later run that reaches Q5 must answer these.

**Q6 (the money and the owners).** Buybacks of $138M (FY2023), $218M (FY2024) and $329M (FY2025) under a dollar
authorization with no stated price (10-K Item 5); FY2025's averaged about $51 a share and the fourth quarter's $42.70,
above the computed bottom of $39.67 (the computation above). Dividends $72M to $84M a year. The 2023 to 2024 cash
settlement of the convertible notes and warrants (Q4 item 5). The planned spin-off of MTS, intended tax-free, targeting
2027-01-04 (10-Q Note 18).

**Q9 (debt and exposures).** Debt $2,552M at 2026-07-03 against owner cash before interest of about $391M a year;
maturities of $551M in FY2027 and $788M in FY2029 (10-K contractual obligations table); a net leverage ratio of 2.3x by the
company's own adjusted measure (release of 2026-07-30). Letters of credit of $310M drawn on committed and uncommitted lines,
with uncommitted capacity "at the provider’s sole discretion" (Item 1A); joint-venture performance guarantees that are
"usually joint and several" and whose maximum the company is "unable to estimate" (Item 7); a frozen U.K. pension in surplus
($84M). For a whole-business purchase the "little or no debt" criterion would be the question; for a part-interest the
rows state none.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early): Step 0
      to Q1, then Q2, then this close, each a pathspec commit of my two paths.
- [x] Dispatched: the brief allowed the per-question commits; the lock was held by the dispatching session (present when I
      started; not touched by me). The fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One `ls` of `Test Runs/` filtered to
      "2026-10-16" printed other run file names; the session context showed commit subjects about an ACM run; both are
      declared at the top under contamination and were not used.
- [x] Every v5 id resolves (checked by `Test Runs/_research 2026-10-16 KBR/check_run.py`); every filing fact has its
      accession; the competitor figures are XBRL transcriptions with their accessions in `peers_output.txt`.
- [x] The order was kept; Q2's STOP closed the run; nothing after it is a clearance; the figures beneath it are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay, capital spending, acquisitions shown), never a net-income proxy; the
      sovereign from the US Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as found (foundations, Q1, Q2's "What argues for the castle"); the facts for
      later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run; rows of 2025 and earlier only.
- [x] Only the arithmetic lines of `tools/run.py` were used, and two of them were found inconsistent and replaced by the
      filed statements (Step 0).
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the commit message).
- Honest limits: the five-year segment table mixes the old and new segment definitions; the receivables sold at year-end,
  the change-order amount, the cause of the cash-tax gap and any organic growth figure were not found in what I read; I
  read the proxy only for its pay metrics; the rivals' margins are XBRL transcriptions, not read from their statements.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The parts threshold across a segment recast.** The five-year rule gives MTS 61% and the decision; the three recast
years give STS 52%. The filer recast its segments in FY2025 and only three years exist on the new basis, so the five-year
figure has to splice two definitions. The framework does not say which basis governs when the filer's segments change
inside the window; I used the five-year splice, as the text's number says, and wrote the sensitivity down. (2) **Organic
growth "as the filer reports it"** for a serial acquirer whose filings report none: the text has no fallback, and I
confessed one (total revenue growth as the upper bound). (3) **A pending spin-off.** The framework has a rule for a signed,
unclosed acquisition and none for a separation eleven weeks away that changes what the buyer owns; the parts rule did the
work here, but a name whose deciding part is about to leave would need one. (4) **Discontinued operations in owner cash.**
The text does not say whether a discontinued part's cash losses (HomeSafe, $33M of operating cash out in FY2025) are a real
cost of the owner's window; I kept them in. (5) **Cash tax below book tax for reasons other than carryforwards.** Whose tax
addresses carryforwards and credits only; here cash taxes ran about $54M a year below the provision with the cause
unstated, and I showed a book-tax variant beside. (6) **The tooling.** `tools/run.py` mixed continuing and total operating
cash across years and found no stock pay in XBRL, though the equity statements show $12M to $22M a year; a run that trusted
its owner-earnings column would have overstated owner cash. (7) **Range against floor.** With the sovereign at 5.43% the
range sits above the price while no case earns the floor; the floor-first rule settles it, but a reader of the reporting
figures alone could misread a price below the range as cheap; the fair price is the figure that answers that.
