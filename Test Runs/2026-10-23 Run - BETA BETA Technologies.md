# Company Run — BETA Technologies, Inc. (NYSE: BETA) — 2026-10-23
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Dispatch.** A dispatched purchase run under the canonical brief, with the one departure the brief states (the evidence
lines and the rivals taken from the company's own 10-K and prospectus). Working folder
`Test Runs/_research 2026-10-23 BETA/` (notes, the tool outputs, `q7_computation.py`, `f4_parse.py`, `check_ids.py`; raw
filings in its ignored `cache/`).

**Contamination, declared.** A directory listing of `Test Runs/` made at the start, to check the date's existing files,
showed the names of other companies' run and research files dated 2026-10-23 (utilities) and two addenda of that date
about utility runs. None is about this company; none was opened; nothing in them is used. The git snapshot given at the
start showed recent commit subjects about utility runs and framework cases; not used. No file about BETA under any name
was seen. No search across `Test Runs/` was made. The session's memory index, loaded automatically, carries one-line
summaries of the queue's state (counts of gate-clearers and holding reviews owed, no tickers of this name); not used.
The listing itself is a breach of the letter of the blind rule ("list"), declared here and in the self-audit.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **The company, from its own filings.** BETA Technologies, Inc., Delaware, South Burlington, Vermont; SIC "Aircraft";
  former name "Beta Technologies Inc." to 2025-08-27 (EDGAR submissions header). Designs electric aircraft (ALIA CTOL
  CX300, ALIA VTOL A250, the military MV250), electric motors (H500A), battery packs, flight control computers and
  aircraft chargers. One reportable segment, "Development and Manufacturing of Electric Aircraft" (10-Q, note 10).
  IPO closed 2025-11-05: 34,330,882 Class A shares at $34.00, net proceeds $1,103.3M, with a 6.3811681-for-1 forward
  split and conversion of all preferred into common (10-K note 1; prospectus 424B4, 2025-11-04, `0001193125-25-265029`).
- **Price:** $18.37 (2026-10-23, live quote from the aggregator `tools/run.py` uses; **aggregator, flagged** per operator
  rule 5). Not cross-checked against a second quote.
- **Shares by class** from the latest filing's cover: 225,439,576 Class A and 8,501,484 Class B outstanding as of
  2026-08-06 (10-Q for the quarter to 2026-06-30, filed 2026-08-12, `0001628280-26-055982`; `python Screens/cover_shares.py
  BETA` gives the same). Charter note: each Class B share carries 40 votes, "is convertible into one share of common
  stock, at the option of the holder, at any time", and is held by the chief executive (10-K note on stockholders' equity;
  10-K risk factors), so the classes are one economic class and are added: **233,941,060**. Check against issued less
  treasury: the 2026-06-30 balance sheet shows 225,344,422 Class A and 8,501,484 Class B issued and outstanding, no
  treasury line; the difference to the cover (95,154 Class A) is issuance between 2026-06-30 and 2026-08-06. No 8-K or
  prospectus after the 10-Q changes the count (8-Ks after 2026-08-12: none in the EDGAR list; Forms 4 and 144 only).
  `tools/run.py` used a pre-IPO balance-sheet count (37.579M at 2025-09-30) and a $0.69B market cap; **that line is wrong
  for this name and is not used**.
- **Market cap:** $18.37 x 233.94M = **$4,297M**.
- **Sovereign for the earnings currency (USD):** **5.29%**, US Treasury daily par yield curve, 30-year, 2026-10-22 (issuing
  authority, as `tools/run.py` fetched it from `tools/sources.py`).
- **Filings read** (operator rule 4): the 10-K for FY2025 (filed 2026-03-09, `0001628280-26-015838`): business, risk
  factors, MD&A, statements and notes; the 10-Qs for Q1 2026 (`0001628280-26-033914`) and Q2 2026 (`0001628280-26-055982`);
  the IPO prospectus (`0001193125-25-265029`, searched for named competitors and the risk factors on competition); the proxy
  (DEF 14A filed 2026-04-29, `0001140361-26-017861`, the summary compensation table); 8-Ks of 2025-11-06
  (`0001193125-25-269718`), 2026-02-18 and its amendment (`0001628280-26-009452`, `0001628280-26-009466`), 2026-06-15
  (`0001628280-26-043215`), 2026-07-22 (`0001628280-26-049223`), and the three earnings releases furnished as exhibit 99.1
  (FY2025 `0001628280-26-015788`, Q1 2026 `0001628280-26-033824`, Q2 2026 `0001628280-26-055933`); every Form 4 filed in
  2026 (parsed by `f4_parse.py`); the list of Forms 144.
- **One figure cross-checked against the filed statement:** net cash used in operating activities FY2025, $(267,798)
  thousand on the filed cash-flow statement of the 10-K, against $(267.8)M in `tools/run.py`; capital spending $45,447
  thousand against $45.4M. Both agree.
- `python tools/run.py BETA`, arithmetic lines only (output kept in `run_py_output.txt`). Owner cash = operating cash less
  stock pay less capital spending, USD millions, as filed: 2023 **-320.2**, 2024 **-308.3**, 2025 **-348.0**; three years
  of data only (the company filed no annual statements before the prospectus; the prospectus and 10-K carry 2023 to 2025),
  so the "five-year" mean is a three-year mean, **-325.5**. On depreciation instead of capital spending: -175.6, -251.2,
  -324.6, mean -250.5. Capital spending 153.2, 73.5, 45.4; depreciation and amortization 8.6, 16.5, 22.0. Stock pay 9.0,
  12.1, 34.8, all expensed and subtracted; the GE warrant expense, $6.1M in 2025 (10-K cash-flow statement), is further
  stock pay added back in operating cash and is subtracted in the computation below. Paid-in-kind interest 0.2, 2.2, 2.2
  is inside operating cash (immaterial). Finance-lease principal 0.0, 0.1, 0.1. Every owner-cash year is negative.
  First half of 2026 (10-Q): operating cash -170.2, stock pay 38.1, warrant expense 11.3, capital spending 65.3, so owner
  cash about -284.9 for six months.

## THE FOUNDATIONS (not a gate)
Three foundations bear. **A share is a business:** the question is "Would I be happy buying this stock if the market
closed for five years?" **[M1997-109]**, and a business that has produced no positive owner cash in any year filed can
only be owned for what it will produce later or for what "somebody else will pay you for it later on, irrespective of
what the asset produces, and I call that speculation" **[M2002-078]**. **Who is paid to tell you:** the listing is eleven
months old and was a seller's choice of date, "the seller decides when to come to market in most cases" **[M2004-100]**;
the rows find it "nonsense" that such a security "is going to be the single cheapest thing to buy out of thousands and
thousands and thousands of businesses in the world" **[M2012-066]**; and the case for the company is made almost wholly in
its own projections (a $3.47B "Backlog", a $250B addressable market "through 2035", battery replacement revenue
estimated at "approximately $13 million" per aircraft over 20 years, all from the 10-K business section), which the rows
do not consult: they have "never looked at a projection in connection with either a security" **[M1995-050]**, and "You do
not want to ask an investment banker what he thinks the earnings are going to be in five years" **[M2011-083]**. **The
market serves:** the price fell from the $34.00 offering price to $18.37, which "just tells us prices" in the row's own
words only if the facts and reasoning lead somewhere **[M2006-077]**; a lower price is not evidence. The analyst's habit
applied: written down as found, "write it down in the first 30 minutes" **[M1997-127]**, and looking for what is wrong,
"somewhat critical of everything" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the company's motor target slipped: the FY2025 release
said the H500A was "on track for FAA type certification in the first half of 2026"; the Q2 2026 release (furnished
2026-08-12) reports "formal FAA testing underway" and no type certificate; the aircraft certification is targeted
"approximately 12 months following" the motor's (10-K), so the dated chain has moved at its first link. (2) The 10-K's own
note 1: "it is uncertain when, if ever, the Company will realize significant revenue from sales." (3) The backlog is
mostly options (602 of 891 aircraft at 2025-12-31) and its agreements "generally contain conditions", some "depend on
certification", payment arises "after meeting certain manufacturing milestones" (10-K risk factors). (4) Remaining
performance obligations at 2026-06-30 were $33.0M (10-Q note 4), against a $3.9B aircraft "backlog" claimed in the Q1 2026
release. (5) Losses widened: loss from operations $186.6M, $272.2M, $372.7M in 2023 to 2025, and $291.1M in the first half
of 2026 alone. (6) The 2026 adjusted EBITDA outlook was moved from ($305)M to ($395)M (March) to ($400)M to ($445)M
(August). (7) The chief executive sold 811,162 shares, about $16.5M, between 2026-05-07 and 2026-10-22 (Forms 4). In the
other direction: $1,479.5M of cash at 2026-06-30 against $184.0M of notes, a director's open-market purchases of 43,080
shares (Forms 4, 2026-05-19 to 2026-09-02), and revenue rising from $15.4M (2023) to $35.6M (2025).

## THE STANDING RULE
The buyer's conduct, not the target's: nothing in this file requires borrowing, a margin account or a position that could
force a sale, so the rule is not engaged by the run; it is the buyer's to keep: "We are never going to risk what we have
and need" **[M2012-081]**; "Never risk permanent loss of capital." **[L2023-005]**. A holder of this name would be
holding a claim on a business that burns about $300M a year and has said it expects "to utilize a combination of equity
and debt financings to fund any future remaining capital needs" (10-Q liquidity section), which is a risk of permanent
loss weighed nowhere here, since the file closes before Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the text states it.** Understanding is "a reasonable probability of being able to asses where the business
will be in 10 years" **[M2000-037]**, "a reasonable fix on about what the earning power and competitive position will look
like in five or 10 years" **[M2012-065]**; it is "the predictability of the economics of the situation 10 years out" that is
asked, not knowledge of the product **[M2000-104]**. The product here is clear enough from the 10-K (electric aircraft,
motors, battery packs, chargers); the economics are what is asked for.

**The filing facts.**
- **No economics yet to read.** The 10-K's note 1: the company "has devoted substantially all of its time and efforts to
  performing research and development activities, raising capital, recruiting management and technical staff", is
  "still in the development phase for its aircraft", is subject to "risks and uncertainties common to early-stage
  companies", and "it is uncertain when, if ever, the Company will realize significant revenue from sales." Of each
  aircraft: "We have not yet delivered any certified aircraft and therefore, no associated revenue has been recognized"
  (10-K business section). Revenue to date is engineering services, chargers, motors and batteries sold to other
  developers: $15.4M (2023), $15.1M (2024), $35.6M (2025); $24.8M in the first half of 2026, of which $15.9M from related
  parties (United Therapeutics, GE Aerospace and an institute; 10-Q statement of operations footnote 1, note 12).
- **The key variables, and how predictable they are** **[M1998-044]**: (a) when, and whether, the H500A motor, then the CX300,
  then the A250 are certified: each date is set as "approximately 12 months following" the last, and the first date (the
  H500A in "the first half of 2026") has already passed without a certificate (FY2025 and Q2 2026 releases); (b) the
  price and unit cost of an aircraft no one has yet built for sale, at a rate the plant is "designed to support" of "more
  than 300 aircraft annually at maturity" (10-K); (c) battery life and replacement pricing, on which the company rests "a
  majority of the lifetime revenue" (10-K), an estimate of its own; (d) how many of the 891 to 991 aircraft of "Backlog",
  mostly options and conditional on certification, become paid deliveries; (e) what the military buys, where the
  requirements and timeframe for the MV250 "remains to be defined" (10-K); (f) battery-cell and hybrid-propulsion
  technology, which the company itself expects to change ("improving battery technology over the lifetime of the
  aircraft"; the GE turbogenerator "co-develop" programme). None of the six can be read off the figures filed; each is a
  forecast, and most are the company's own. "If something is not very predictable, forget it." **[M1998-044]**
- **Do the past statements tell me the future ones?** No: three years of losses from development spending describe a
  laboratory and a plant under construction, not the business that is projected; "if you can’t make a decision on
  something like PetroChina off the figures, forget about going further" **[M2008-069]**.
- **Can I name the winner, not just the industry?** The 10-K names the field's own decisive factors: "the ability to certify
  the aircraft and commence commercial production in a timely manner", "the ability to capture first-mover advantage, if
  any", "the ability to develop or otherwise capture the benefits of next-generation technologies" (10-K, Competition). The
  rows: "industries we know that may have a wonderful future" with no idea of the winners are not thought about
  **[M2012-067]**; "we try to stick with businesses where we know the winners" **[M2014-097]**; and seeing "dramatic growth
  ahead for an industry does not mean we can judge what its profit margins and returns on capital will be as a host of
  competitors battle for supremacy" **[L2009-005]** (the row's elided examples, per its note, include aircraft in 1930).
- **Would the insiders write it down?** The company writes down a market size and a backlog, which are a seller's
  projections **[M2011-083]**; it does not write down its own earnings, and its audited note says revenue is uncertain
  "when, if ever". That is the test whose insiders "would not want to put down on paper their predictions" of the
  field's economics ten years out **[M2000-105]**.

**Which box.** Two readings of the text apply, and they point to different boxes:
1. **OUT, on Q1's list.** Q1's list of what it rules OUT names start-ups: "Start-ups are not our game." **[L2007-015]**;
   "Well, if you blot out startups" a whole layer of complexity goes **[M2008-088]**; and the acquisition criteria ask for
  "Demonstrated consistent earning power (future projections are of no interest to us" **[R1997-001]**. On its own
  audited description (development phase, no certified product, revenue "when, if ever"), BETA is a start-up: the
  business the price pays for has not begun. The rows give this exclusion as a filter, not as ignorance, and the list has
  kept it through every correction pass that moved the ignorance items to TOO HARD.
2. **TOO HARD (NATURE), on the routing.** A business "that must deal with fast-moving technology is not going to lend itself
   to reliable evaluations of its long-term economics" **[L1993-023]**; "where we think the future technology could hurt
   the business as it presently exists" it fails the filter **[M1998-008]**; "We view change as more of a threat into the
   investment process than an opportunity" **[M1999-063]**; industries whose winners cannot be named go to the same box.
   The cause would be NATURE: the industry's own insiders do not write the forecast down **[M2000-105]**, and study does not
   cure it, "the nature of the industry would be the roadblock" **[L1993-023]**; "we’re not going to learn enough in the
   followings five months to make up for the fact that we went in deficient in the first place" **[M2008-086]**.

**Decided: OUT, on the start-up item.** The list item is the more specific rule and fits the filing facts exactly; the
routing paragraph governs a business whose economics exist but cannot be foreseen, and here they do not yet exist. The
difference is the box's name only: both close the file at Q1, neither is reopened by a lower price on these figures
(owner cash is negative in every year, so no case of the COMPUTATION below earns the floor at any positive price), and
neither is a judgment that the company is bad: "The only way we know how to make money is to try and evaluate
businesses" **[M2000-038]**. The doubt test agrees: "if you have doubts about something being into your circle of
competence" it is outside **[M2002-092]**. The conflict between the two readings, and section I's description of Q1 as a
TOO HARD question only, is reported under WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR.

- **VERDICT: OUT** (Q1; start-up: no certified product, no revenue from the business priced, three years of negative owner
  cash; **[L2007-015]**, **[M2008-088]**, **[R1997-001]**; the alternative reading TOO HARD (NATURE) recorded,
  **[L1993-023]**, **[M2000-105]**). The file closes here. Q2 to Q12 are NOT REACHED.

## Q2 — WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (Q1 closed the file). The competitor figures already gathered are under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0 and are set out under AFTER THE STOP, as the brief asks.

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED. Integrity facts were found before the stop; they are recorded under AFTER THE STOP and flagged in the box
line, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. (The buyback line needs the bottom of a Q7 range; there are no buybacks: "Issuer Purchases of Equity
Securities: None", 10-Q Part II, Item 2.)

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The two reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US? WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT, at Q1** (a start-up: no certified product, no revenue from the business the price pays for, negative owner cash in
every year filed; the alternative reading of the same facts is TOO HARD (NATURE), recorded at Q1). **Integrity facts
recorded, not judged** (a director's resignation at the end of a board committee review, and the amended 8-K that dropped
the sentence about the review; see AFTER THE STOP, Q5). Q7 was not reached; the COMPUTATION below has every case
negative, so no case earns the floor at the price of $18.37.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; the
box is unchanged, operator rule 2.)*

**Bears on Q2 (the competitor row, from the rivals' own filings).** The 10-K names no competitor; it names the field's
sources of competition as "conventional air transport solutions and manufacturers or other suppliers of other electric
aircraft" and lists the success factors quoted at Q1. The rivals the 10-K and prospectus themselves name (as customers or
partners who also build electric aircraft): Archer Aviation (SEC filer, 10-K filed 2026-03-02, `0001824502-26-000019`),
Eve Holding (Embraer-backed, SEC filer, 10-K filed 2026-03-16, `0001554855-26-000300`), Vertical Aerospace (named as
"Vertical Aviation"; a foreign private issuer filing a 20-F under IFRS; its figures not tabulated here), and Textron
eAviation (a segment inside Textron; its segment figures not read). Same metrics, USD millions, from the XBRL company
facts of those filings (transcription; not cross-checked against the rivals' filed pages, said so):

| Company | Metric | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| BETA | operating income (loss) | n/f | n/f | (186.6) | (272.2) | (372.7) |
| BETA | operating cash | n/f | n/f | (158.0) | (222.7) | (267.8) |
| BETA | capital spending | n/f | n/f | 153.2 | 73.5 | 45.4 |
| Archer | operating income (loss) | (358.3) | (347.4) | (446.9) | (509.7) | (729.3) |
| Archer | operating cash | (108.4) | (200.4) | (271.6) | (368.6) | (432.9) |
| Archer | capital spending | 3.5 | 6.9 | 44.3 | 82.0 | 78.8 |
| Archer | revenue | n/f | n/f | 0.0 | 0.0 | 0.3 |
| Eve | operating income (loss) | (18.2) | (189.5) | (130.5) | (156.4) | (225.4) |
| Eve | operating cash | (14.9) | (59.5) | (94.5) | (136.0) | (160.4) |
| Eve | capital spending | 0.0 | 0.5 | 0.2 | 5.2 | 12.6 |

(n/f = not filed for that year, or not in the facts read.) Over the whole span on record, no named rival that files with
the SEC has a year of operating profit or of positive operating cash; the field has no cycle of returns to read. BETA's
revenue ($35.6M in 2025) is the largest of the three, and all of it is from components, chargers and engineering
services, not certified aircraft.

**Bears on Q3.** Property and equipment, net: $276.3M (2023, prospectus `0001193125-25-265029`), $319.6M (2024), $348.5M
(2025, 10-K), $402.8M (2026-06-30, 10-Q), with $68.5M of construction in progress at the last date. Capital spending
2023 to 2025 totals $272.2M; a further $65.3M in the first half of 2026. The plant is "designed to support production of
more than 300 aircraft annually at maturity" and has permits "for expansion to over 355,000 square feet" (10-K). No return
on the capital is yet earned.

**Bears on Q4: the balance sheets, read before the income account** (only four year-ends exist, not eight to ten; 2022
and 2023 from `tools/run.py` and the prospectus, 2024 and 2025 from the 10-K, 2026-06-30 from the 10-Q; USD millions):

| Date | Cash | PP&E net | Notes payable | Total liabilities | Equity incl. preferred | Accumulated deficit |
|---|---|---|---|---|---|---|
| 2022-12-31 | 430 (XBRL, not read on the filed page) | n/r | n/r | n/r | 551 (XBRL) | n/r |
| 2023-12-31 | 253.5 | 276.3 | 134.6 | n/r | 385 (XBRL) | n/r |
| 2024-12-31 | 301.4 | 319.6 | 152.1 | 230.4 | 435.9 | (969.3) |
| 2025-12-31 | 1,710.2 | 348.5 | 185.5 | 288.4 | 1,817.8 | (1,913.5) |
| 2026-06-30 | 1,479.5 | 402.8 | 184.0 | 318.3 | 1,615.2 | (2,184.5) |

(n/r = not read.) What moved and why: equity is wholly raised capital, $3,799.9M of paid-in capital against a $2,184.5M
accumulated deficit at 2026-06-30; cash rose $1,408.8M in 2025 on the IPO ($1,103.3M net), the Series C and C-1 preferred
($606.3M gross) and a sale-leaseback ($32.7M), and has fallen $230.8M in the first half of 2026. No goodwill or
intangibles are carried; receivables and deferred revenue are small ($3.6M and $21.9M at 2026-06-30). The debt is an
Export-Import Bank credit facility whose lender holds "first-priority liens on and security interests in our Final
Assembly Facility" (10-K risk factors), plus the sale-leaseback financing with "an associated company of a board member"
for two buildings, a related-party $32.9M (10-Q note 12 and balance-sheet footnote 3). What the figures cannot say: what an
aircraft will cost or sell for. In the income account: the 2025 net loss of $745.9M includes a $379.6M "Loss on issuance
of convertible preferred stock", "attributable to the difference between the fair value and aggregate proceeds received
from the issuance of Series C and C-1" (10-K MD&A); Q2 2026 includes $15.0M of acquired in-process research expensed and a
$5.3M loss on abandoned equipment. The company features EBITDA and adjusted EBITDA, gives adjusted EBITDA guidance each
quarter (the 2026 range moved from ($305)M to ($395)M, to ($355)M to ($445)M, to ($400)M to ($445)M), and its chief
operating decision maker's segment measure leaves out stock pay and warrant expense (10-Q note 10). Under the framework
these are recorded at Q4 as a weighing and carried to Q5; here they are recorded only.

**Bears on Q5 (integrity facts, recorded, not judged).**
- The 8-K filed 2026-02-19 (`0001628280-26-009452`) reported that director Dean Kamen "voluntarily stepped down", effective
  "January 18, 2026", and that his "resignation concludes the review initiated on February 4, 2026 by the Nominating and
  Corporate Governance Committee of the Company's Board, which did not identify any violations of the law." An amendment
  filed the same day (`0001628280-26-009466`), "to correct a clerical error", gives the date as "February 18, 2026" and
  does not contain the sentence about the review. The subject of the review is not stated in either filing.
- Control: the chief executive holds all Class B shares, about 7.0% of the capital and about 62.0% of the votes at
  2025-12-31; the company is a "controlled company" under NYSE rules (10-K risk factors).
- Insider sales: the chief executive sold 811,162 Class A shares for about $16.5M between 2026-05-07 and 2026-10-22, some of
  the Forms 4 citing a Rule 10b5-1 plan; five other officers sold small amounts on 2026-05-07 (about $1.1M together); Forms 144 have been filed on
  most trading days since 2026-09-24 (EDGAR list). A director (Michael Stone) bought 43,080 shares, about $0.8M, between
  2026-05-19 and 2026-09-02 (Forms 4).
- Pay: the chief executive's total compensation was $15,859,072 for 2025 against $1,060,000 for 2024, including a
  $5,132,000 cash bonus (proxy, summary compensation table); the 2026 PSUs vest on "quarterly pre-set objectives"
  (10-Q note 8).
- A stated target missed: the H500A type certificate "in the first half of 2026" (FY2025 release) had not been granted at
  the Q2 2026 release.
- The Security Control Agreement with the Defense Department and QIA Industrials Holding, put in place for foreign
  ownership, control or influence, was terminated by the DCSA on 2026-07-14 because QIA "no longer has representation"
  on the board (8-K `0001628280-26-049223`).

**Bears on Q6.** No buybacks and no dividends ("We do not intend to pay dividends and may never pay dividends", 10-K).
Shares issued for Biocogniv, 715,587 Class A worth about $10.8M with $4.2M of cash and holdback, expensed as in-process
research (10-Q note 3, Part II Item 2). Preferred stock issued in 2025 at $379.6M below its fair value (above). Potential
dilution at 2026-06-30: 2,552,467 unvested GE warrants and 20,613,487 shares issuable under stock plans (10-Q note 9),
about 9.9% of the 233.94M shares. The company expects to fund itself with "a combination of equity and debt financings"
(10-Q).

**Bears on Q9.** Cash $1,479.5M against notes of $184.0M at 2026-06-30; operating cash plus capital spending used $235.5M
in the first half of 2026, which at that rate is about three years of cash. The Ex-Im lien on the Final Assembly Facility
is above. "We do not have material cash requirements related to current contractual obligations" (10-Q).

## COMPUTATION, NOT A CLEARANCE
*(The owner's reporting figures, Part VII, The owner's price; computed because the brief asks for them; neither is a
verdict or entry language, operator rule 3. Script: `Test Runs/_research 2026-10-23 BETA/q7_computation.py`.)*

- **The cash input.** Owner cash after every real cost, by Q7's range convention, from the 10-K cash-flow statement
  (`0001628280-26-015838`): operating cash less stock pay less the GE warrant expense less capital spending. Equity-only
  (after interest, as filed): -320.2, -308.3, -354.1 (2023 to 2025, USD millions), mean **-327.5**. All-equity (before net
  interest: cash interest paid added back, interest income taken out, since the cash that earns it is counted in net debt):
  -332.5, -307.6, -363.4, mean **-334.5**. The window is three years, the only ones filed (see what was wrong or unclear).
- **Specific (e), the maintenance case, central.** The filing gives no maintenance figure; it describes the capital
  spending as building the plant and the charging network. The maintenance guess is depreciation, $8.6M, $16.5M, $22.0M:
  maintenance-case owner cash, all-equity -187.9, -250.6, -339.9, mean **-259.5**; equity-only mean **-252.5**. The
  growth spending above it ($144.6M, $57.0M, $23.4M) buys no growth case (below).
- **Specific (b), decline.** Every year is negative and the burn is rising, so a compound growth rate between end years is
  meaningless, and between the halves of a three-year window it is meaningless too. By (b) the range is **the no-growth
  case alone, said so**. The first half of 2026 (owner cash about -284.9 for six months) is worse than every year of the
  window and is not used to set the base; it would make every figure below more negative.
- **Specifics (a), (c), (d), (f).** (a) no window year is called aberrational by the filer; 2023's capital spending peak is
  the plant's construction, and the maintenance case already removes it. (c) no acquisitions for cash in the window; the
  2026 Biocogniv deal (mostly shares) was expensed and is inside 2026 operating figures, outside the window. (d) working
  capital changes are inside operating cash, counted. (f) no growth is carried, so no cap applies.
- **The floor, tested first.** At $18.37 no case earns about ten percent: every case's owner cash is negative, so the
  expected return at any positive price is below the floor, "a point at which we drop out of the game" **[M2003-149]**.
- **Net debt** (2026-06-30, 10-Q): notes payable $8.5M current and $175.4M non-current, less cash $1,479.5M = **-$1,295.5M**
  (net cash); operating leases left out ($22.7M), said so; finance leases immaterial.
- **VALUE RANGE (COMPUTATION).** No-growth case at the 5.29% sovereign, per share on 233.94M shares:
  - central, all-equity, maintenance case: **-$15.43** a share (equity-only beside: **-$20.40**);
  - all-spending case beside: all-equity **-$21.49**, equity-only **-$26.47**;
  - the literal window is the same three years; there is no other window to show.
  Against the price of **$18.37**.
- **FAIR PRICE (COMPUTATION; Part VII, each end case at ten percent, averaged; one end case only here).** Central,
  all-equity, maintenance case: **-$5.55** a share; equity-only beside: **-$10.79**. All-spending beside: all-equity
  **-$8.76**, equity-only **-$14.00**. Tax: the company's own, which is almost nothing ($0.8M provision in 2025) on losses;
  no shelter is priced and no tax is charged on negative cash. Growth spending in a growth case: none, there being no growth
  case. Not a regulated utility; no debt credit. No cheap price is reported.
- What the arithmetic says and does not: a negative perpetuity values the business as if it burned cash forever, which
  no owner would allow; it states that the filed record holds no owner cash to value, the value being "the present value,
  the appropriate interest rate, of all the future streams of cash going in or out of the business" **[M1994-077]**, every
  stream filed being outward, and that "growth can destroy value if it requires cash inputs in the early years of a
  project or enterprise that exceed the discounted value of the cash that those assets will generate in later years"
  **[L2000-023]**. Any positive value would rest on the company's projections, which the run does not use.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after Step 0, after Q1, and at
      the close (write-early). The file closed at Q1, so the later questions were written once as NOT REACHED.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (not checked
      by this analyst); the run binds nothing until folded into the register (operator rule ten).
- [ ] **Blind rule, partly breached and declared:** a listing of `Test Runs/` filtered to the run date showed other
      companies' file names (utilities); none was opened or used, none is about this company. `PORTFOLIO.md`, holding
      reviews, the resume-state files, the register and the reading list were not opened, listed or searched.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by `check_ids.py` in the research folder); every filing
      fact has its accession or names its filing; no E-ids.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance; the figures after the stop are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the US Treasury
      curve; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found; the facts for later questions are under AFTER THE STOP; the integrity flag
      is in the box line.
- [x] No point-in-time anchor; not applicable.
- [x] Only the arithmetic lines of `tools/run.py` were used; its share count and market cap were wrong for this name
      (a pre-IPO count) and were replaced from the 10-Q cover.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1's box for a start-up is stated two ways.** Q1's list of what it rules OUT names start-ups (**[L2007-015]**,
**[M2008-088]**) and has kept them through every correction that moved ignorance items to TOO HARD, while section I
describes Q1's failing box only as TOO HARD ("a business whose economics cannot be foreseen (Q1)") and the routing sends
fast-moving technology and industries whose winners cannot be named to TOO HARD (NATURE). An electric-aircraft developer is
all three at once. I chose OUT on the more specific item and recorded the other reading; the text should say which governs
when a start-up is also in a fast-changing field, and whether section I's list of OUT sources should name Q1. (2) **The
five-year window when only three years exist.** Q7's convention averages five years and says nothing of a company with
fewer filed years; I used the three and said so. (3) **"Owner cash before interest" on the all-equity basis is silent on
interest income.** With $1.5B of cash counted in net debt, leaving the interest it earns inside owner cash would count it
twice. CONVENTION of this run: on the all-equity basis owner cash is taken before net interest (interest paid added back,
interest income removed); rationale: the cash that earns the income is already credited in net debt. (4) **A negative
perpetuity.** Specific (b) leaves the no-growth case alone when the series never turns positive; for a business that has
never had positive owner cash this values the burn as permanent, which is arithmetic and not a description of any
outcome; the text does not say whether such a range should be reported as "not computable" instead. I reported the
numbers with that caution. (5) **`tools/run.py` share count.** For a company listed after its last balance-sheet count
the tool took a pre-IPO count (37.6M against 233.9M) and printed a market cap about a sixth of the true one; the template's
instruction to check the cover caught it, but the tool's market-cap line should not be trusted for recent listings.
