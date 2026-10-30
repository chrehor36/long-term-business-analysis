# Company Run — Everforth, Inc. (NYSE: EFOR; ASGN Incorporated until 2026-04-24) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**TEST RECORD.** This is a T2 re-run under `Framework/v5/tests/T2 PROTOCOL - the four re-runs of 2026-10-06.md` and
`Framework/v5/tests/RULES UNDER TEST 2026-10-06 - sections D and H.md`. It binds nothing, enters no register and changes
no verdict of record. Where a rule under test bears, the sentence says "rule under test, section D(a)" (or whichever
letter). Working folder: `Framework/v5/tests/_work_T2_EFOR/` (raw filings under `raw/`, gitignored there; the
arithmetic is `q7_computation.py` and its saved output).

**POSITION NOTE, declared before any verdict:** not checked. The template line says to check `PORTFOLIO.md`; the T2
protocol's blind rule forbids opening it, and the protocol wins. The analyst does not know and did not try to learn
whether the operator holds or wants this name.

**CONTAMINATION, declared and not used.** (1) Before the blind rule was applied, a directory listing of
`Framework/v5/tests/` was made to find the protocol file; it showed the file names of the other test runs (A HRB, A TJX,
A2 PG, B CASE_A to CASE_E, R ASML, R MITSY, R NCLTY, R TBTC, R V, SM MKL, T2 ENSG, T2 RYZ and their working folders).
No file was opened. (2) `git log` subjects seen while checking the repository state named ENSG, RYZ, EFOR, PBH and ABG
as re-run or alert names. (3) The session's git status and memory index, supplied by the environment, listed research
folder names (ARCB, AYI, BDC, CHD) and a memory line about the queue's state. Nothing in (1) to (3) was read further
or used. (4) The dispatch brief named this company's former name and ticker, which is also in the filings. (5) At the
closing commit, after every section of this file was written, the git log showed commit subjects of the other T2
re-runs (RYZ, PBH, ENSG) that carry question verdicts; seen after the fact, not used, declared here.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $35.51 (2026-10-06, aggregator live quote via `tools/run.py`; flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 41.0 million common shares as of 2026-07-24, one class (Form
  10-Q for the quarter ended 2026-06-30, filed 2026-07-31, accession `0000890564-26-000050`;
  `python Screens/cover_shares.py EFOR` gives the same 41,000,000). Checks: 40.9 million outstanding on the balance
  sheet at 2026-06-30 (same filing); 41,275,049 at 2026-03-31 (DEF 14A filed 2026-04-27, accession
  `0000890564-26-000031`); 41.7 million at 2025-12-31 (10-K). No 8-K or prospectus after the 10-Q changes the count
  (the 8-K of 2026-07-29, accession `0000890564-26-000047`, is the earnings release). Preferred stock: 1.0 million
  authorised, none issued (10-K FY2025 balance sheet).
- **Market cap:** $1,456M (41.0M × $35.51).
- **Sovereign for the earnings currency:** USD 5.66%, US Treasury daily par yield curve, 30-year, 2026-10-05
  (`python tools/sources.py`, the issuing authority).
- **Filings read** (operator rule 4): Form 10-K for FY2025, filed 2026-02-25, accession `0000890564-26-000013`
  (Items 1, 1A, 5, 7, 8 and the notes); Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-31, accession
  `0000890564-26-000050`; DEF 14A filed 2026-04-27, accession `0000890564-26-000031`; the 8-Ks of 2026-04-24 (name and
  ticker change, `0000890564-26-000025`), 2026-07-09 (credit agreement amendment, `0000890564-26-000045`), 2025-07-31
  (incremental term loan A, `0000890564-25-000042`), 2025-03-06 (TopBloc stock consideration, `0000890564-25-000014`),
  2026-01-20 (Quinnox agreement and Q4 estimates, `0000890564-26-000004`), and the earnings releases furnished with the
  8-Ks of 2026-07-29 (`0000890564-26-000047`), 2026-02-04 (`0000890564-26-000008`) and 2025-02-05
  (`0000890564-25-000006`); the 10-Ks for FY2024 (`0000890564-25-000008`), FY2022 (`0000890564-23-000004`), FY2021
  (`0000890564-22-000007`), FY2019 (`0000890564-20-000007`), FY2018 (`0000890564-19-000019`) and FY2016
  (`0000890564-17-000046`), for the acquisitions, the divestiture, the segment history and the risk-factor language.
  **One figure cross-checked against the filed statement:** goodwill of $2,143.2M at 2025-12-31 on the filed
  consolidated balance sheet (10-K FY2025, `0000890564-26-000013`) against the XBRL fact of $2,143M printed by
  `tools/run.py`; also cash $161.2M and long-term debt $1,169.4M, both agreeing. The 10-K's own ten-year arithmetic
  below is transcription from the filed statements.
- **The rename, as the 8-Ks state it:** ASGN Incorporated changed its corporate name to Everforth, Inc. on 2026-04-24
  by charter amendment filed in Delaware on 2026-04-22; no stockholder vote was needed; the ticker moved from ASGN to
  EFOR on the NYSE the same day (8-K `0000890564-26-000025`). The six operating brands (Apex Systems, Creative Circle,
  CyberCoders, ECS, GlideFast, TopBloc) are being unified under the one name (10-K FY2025, Item 1).
- `python tools/run.py EFOR` arithmetic lines only (USD millions; the tool's v4 material was ignored, Part VII):
  owner cash after every real cost, OCF − SBC − capex, by year: 2023: 456.9 − 44.0 − 39.9 = 373.0; 2024: 400.0 − 42.3
  − 35.3 = 322.4; 2025: 327.9 − 47.9 − 39.8 = 240.2; three-year mean 311.9 (capex basis), 246.8 (D&A basis, D&A being
  100.3, 96.3 and 113.5, of which amortisation of acquired intangibles was 71.7, 58.1 and 64.8); five-year 2021 to 2025
  mean 252.6 (capex basis). SBC resolved and complete: one line, `ShareBasedCompensation`, 44.0, 42.3, 47.9, agreeing
  with the 10-K's statement of cash flows. Capex: `PaymentsToAcquirePropertyPlantAndEquipment`; no software, intangible
  or other capitalised spending line beside it in the filings' cash-flow statements (the 10-K reports capitalised
  software inside property and equipment, net book value $46.0M at 2025-12-31, so the capex line already carries it).

### The balance sheets, ten year-ends, read before the income account **[M2025-032]** (done here because the file closes before Q4)
From `tools/run.py` (first-filed XBRL vintages, USD millions; 2016 to 2020 include the Oxford business, sold 2021-08-17;
accessions `0000890564-17-000046` through `0000890564-26-000013`), with the June 2026 10-Q beside:

| year-end | assets | liabilities | equity | cash | receivables | goodwill | intangibles | LT debt | retained |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 1,753 | 884 | 869 | 27 | 387 | 874 | 378 | 640 | 316 |
| 2017 | 1,810 | 819 | 991 | 37 | 429 | 894 | 353 | 575 | 428 |
| 2018 | 2,688 | 1,506 | 1,182 | 42 | 614 | 1,421 | 489 | 1,100 | 586 |
| 2019 | 2,941 | 1,565 | 1,376 | 95 | 649 | 1,487 | 476 | 1,032 | 745 |
| 2020 | 3,278 | 1,691 | 1,587 | 274 | 679 | 1,618 | 488 | 1,033 | 926 |
| 2021 | 3,503 | 1,637 | 1,865 | 530 | 708 | 1,570 | 488 | 1,034 | 1,174 |
| 2022 | 3,586 | 1,684 | 1,901 | 70 | 854 | 1,892 | 570 | 1,067 | 1,200 |
| 2023 | 3,545 | 1,652 | 1,892 | 176 | 742 | 1,894 | 498 | 1,037 | 1,196 |
| 2024 | 3,429 | 1,652 | 1,777 | 205 | 651 | 1,893 | 440 | 1,034 | 1,097 |
| 2025 | 3,677 | 1,873 | 1,804 | 161 | 674 | 2,143 | 454 | 1,169 | 1,092 |
| 2026-06-30 | 4,024 | 2,218 | 1,805 | 153 | 766 | 2,280 | 596 | 1,438 | 1,082 |

What the figures say. **Equity against goodwill and intangibles:** goodwill plus intangibles exceed equity in every one
of the eleven columns; at 2025-12-31 they are $2,597M against equity of $1,804M, and at 2026-06-30 $2,876M against
$1,805M, so tangible equity has been negative throughout and is now about −$1,071M. The purchased goodwill is read
separately: left out when judging the business, counted when judging the capital allocation, "because we paid for it"
**[M2011-060]**. Every step up in goodwill is a purchase: ECS in 2018 ($775.0M, goodwill $528.2M, 10-K FY2018,
`0000890564-19-000019`, Note 3), the two 2019 deals ($113.0M), four in 2020 ($186.0M), three in 2021 ($221.3M), two in
2022 ($483.0M, of which GlideFast $350.0M), TopBloc in 2025 ($340.0M, goodwill $248.7M) and Quinnox in March 2026
($290.0M, goodwill $137.4M provisional). **Cash:** $530M at 2021-12-31 after the Oxford sale ($525.0M, gain $216.9M,
10-K FY2021, `0000890564-22-000007`, Note 4), spent to $70M a year later on GlideFast and buybacks; $153M to $205M
since. **Receivables against sales:** 17.0% of revenue at 2025-12-31 (674/3,980) against 18.6% at the 2022 peak
(854/4,581) and 17.5% in 2019 on the then-larger company; the 10-Q shows receivables up $92M in the first half of 2026 on
flat revenue, which the filer attributes to days sales outstanding; no inventory, as a service business. **Debt:**
borrowings at principal were $1,182.6M at 2025-12-31 (revolver $45.0M, term loan A $98.8M, term loan B $488.8M, 4.625%
senior notes $550.0M due 2028; 10-K Note 9) and $1,451.8M at 2026-06-30 after Quinnox (revolver $318.0M; 10-Q Note 5);
on 2026-07-07 the revolver was enlarged to $600M and extended to 2031, with a spring-forward to 91 days before the 2028
notes if more than $110M of them are then outstanding, and term loan A was repaid from it (8-K `0000890564-26-000045`).
**Retained earnings:** $1,200M at 2022 falling to $1,082M at 2026-06-30 although net income over the period was $577M,
because repurchases are charged against retained earnings ($223.7M in 2023, $273.7M in 2024, $118.9M in 2025, $29.2M in
H1 2026; statements of stockholders' equity). The share count fell from 49.5M (2022-12-31) to 40.9M (2026-06-30).
**What they do not say:** the segment assets are not disclosed, since the chief operating decision maker "does not
evaluate, manage or measure performance of segments using asset information" (10-K Note 15), so the capital in each
segment cannot be read. **What they cannot say:** whether the goodwill is worth what was paid; the 2025 test was
qualitative only, and the Creative Circle trademark was the auditor's critical audit matter (10-K, Deloitte report).

### What the ten-year filings say of the business (facts, for the questions below)
- Revenue (continuing operations, as recast after the Oxford sale): 2019 $3,415.6M; 2020 $3,502.1M; 2021 $4,009.5M;
  2022 $4,581.1M; 2023 $4,450.6M; 2024 $4,099.7M; 2025 $3,980.4M (10-Ks FY2021, FY2022, FY2024, FY2025); H1 2026
  $1,975.3M against $1,988.9M (10-Q). Operating income: 276.2, 281.2, 350.9, 409.5, 364.1, 304.4, 230.3; H1 2026 68.8
  against 106.2. Net income 2025 $113.5M, H1 2026 $19.7M.
- Segments (10-K FY2025 Note 15 and the earlier 10-Ks): Commercial revenue 2021 $2,927.1M, 2022 $3,435.7M, 2023
  $3,174.4M, 2024 $2,868.7M, 2025 $2,790.2M; segment operating income 355.9, 411.1, 344.1, 286.5, 248.1 (margins 12.2%,
  12.0%, 10.8%, 10.0%, 8.9%). Inside Commercial, Assignment (contract professionals by the hour) fell from $2,476.1M
  (2022) to $1,500.1M (2025), −39%, while Consulting rose from $959.6M to $1,290.1M, with the purchased GlideFast and
  TopBloc inside it. Federal Government revenue 2021 $1,082.4M, 2022 $1,145.4M, 2023 $1,276.2M, 2024 $1,231.0M, 2025
  $1,190.2M; segment operating income 76.1, 89.1, 99.2, 95.2, 93.3 (margins 7.0%, 7.8%, 7.8%, 7.7%, 7.8%). Corporate
  SG&A not allocated: $111.1M in 2025 ($77.3M in 2024).
- Gross margin: consolidated 28.8% (2023), 28.9% (2024), 28.9% (2025), 27.9% (H1 2026); Commercial 32.1%, 32.5%,
  32.8%, then 31.5% (H1 2026); Federal 20.6%, 20.4%, 19.7%, 19.6%.
- Customers: no client other than the U.S. federal government above 10% of revenue; prime contracts with federal
  agencies 26% of 2025 revenue (24% in 2024, 25.2% in 2021, 19.0% in 2019); in 2018 the U.S. Army was 32% of the ECS
  segment. Government contracts "can be terminated by the U.S. government either for its convenience or if we default"
  (10-K FY2021, Item 1A). Commercial contracts: about 90% time-and-materials; "many of our agreements may be terminated
  at will" and "clients are free to place orders with our competitors" (10-K FY2021, Item 1A).
- Federal contract base: backlog $2,948.5M at 2025-12-31 (funded $492.9M), coverage 2.5× trailing revenue; new awards
  $1,020.3M in 2025, book-to-bill 0.9 (0.8 in 2023, 1.1 in 2024, 0.8 for the twelve months to June 2026); the 2025
  decline is "mainly related to the loss of certain contracts as a result of initiatives associated with DOGE" (10-K
  FY2025, Item 7). Contract mix 2025: T&M $474.6M, cost-reimbursable $366.9M, firm-fixed-price $348.7M.
- People: about 19,600 billable professionals on a full-time-equivalent basis in 2025, 21,300 in 2024, 25,500 in 2022
  (the 2016 to 2021 10-Ks count heads, not FTEs: 52,260 in 2016, 61,900 in 2018, 63,400 in 2019, 52,900 in 2021);
  internal employees 2,800 (2025), 3,200 (2024), 4,000 (2022), 4,300 (2018 and 2019).
- Bill rates and hours: disclosed only through FY2019 ("Assignment revenue hours worked and average revenue per hour
  worked were each up approximately 4.8 percent from 2018", 10-K FY2019; 2018 growth "primarily related to growth in
  hours billed and to a lesser extent, growth in average bill rates", 10-K FY2018). No hours, rate or utilisation figure
  is given in any 10-K or 10-Q from FY2020 onward; the brief's request for bill rates and utilisation through the last
  downturn cannot be met from the filings and is recorded under "what could not be got".
- Acquisitions and the divestiture, cash paid net of cash acquired (statements of cash flows): 2018 $760.2M; 2019
  $116.4M; 2020 $186.2M; 2021 $222.8M against $503.8M received for Oxford; 2022 $484.6M against $9.8M received; 2023 and
  2024 nil; 2025 $304.1M (TopBloc, plus 458,283 shares worth about $32.79M, 8-K `0000890564-25-000014`); H1 2026
  $283.6M (Quinnox). The acquired revenue is reported inside the segments from the date of purchase; the 10-Ks give no
  organic-growth figure for the company (the FY2016 10-K gave a pro forma rate for Creative Circle; none since).
- Buybacks (10-K Note 11 and the 10-Q): 2021 $181.3M; 2022 $281.4M; 2023 3.4M shares for $275.7M (about $81 a share);
  2024 3.5M for $329.3M (about $94; the Q4 2024 release gives $90.45 for that quarter); 2025 3.1M for $171.8M (about
  $55; Q4 2025 at $46.05); H1 2026 1.2M for $49.9M (about $42). A new $1.0 billion authorisation on 2025-11-17 names no
  price. Stock pay: $44.0M, $42.3M, $47.9M (2023 to 2025), $29.7M in H1 2026; unrecognised $70.5M at 2025-12-31.
- Debt cost: interest expense, net, $66.4M, $64.3M, $67.7M (2023 to 2025) on weighted borrowings of $1.21 billion at
  5.6% in 2025; $37.5M in H1 2026. Secured leverage covenant 3.75× lender-defined EBITDA, 2.17× at 2026-06-30, stepping
  to 3.25× by mid-2028 (10-Q Note 5; 8-K `0000890564-26-000045`).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what this business will earn over years, not what the quotation will do
**[M1997-109]**, and the fall in the quotation since the company itself paid about $94 a share for 3.5 million shares in
2024 is not instruction, since the market "just tells us prices" **[M2006-077]**. Who is paid to tell you bears
directly: every quarterly release leads with guidance met or exceeded and an adjusted figure, and the January 2026
Quinnox release carries the seller's revenue growth and margin for the coming year; the rows say not to ask the barber
**[M2011-083]**, and no projection in a release is used below. The analyst's habits: contrary evidence is written down
as found **[M1997-127]**. **Contrary evidence, written down as found** **[M1997-127]**: the evidence that favours the
business, against the verdict below, is this. Operating cash flow stayed positive through two downturns ($424.8M in
2020, $327.9M in 2025) and capital spending is small ($35M to $40M a year against depreciation of $38M). Returns on the
tangible capital actually in the business are high in every year, 42% to 81% pre-tax on equity less goodwill and
intangibles plus debt, because the capital is receivables. The federal segment's backlog covers 2.5 years of its
revenue and its margin held at 7.0% to 7.8% through five years. Commercial consulting bookings ran at 1.2× revenue in
2025 and the twelve months to June 2026. The 2023 performance shares paid zero on the NOPAT test (DEF 14A); the chair is
independent; the company has retired 17% of its shares since 2022. The secured leverage covenant stood at 2.17× in June
2026, inside its limit. *(This line asked for a pre-committed falsifier until 2026-10-05; that CONVENTION was removed
under the v5 scope directive.)*

## THE STANDING RULE
Nothing in the target can call the buyer's tune if the buyer owns the shares with no borrowed money **[M2012-081]**,
**[L2014-005]**; the target's own debt and its 2028 maturity are the target's risk, weighed at Q9, not the buyer's ruin,
and no feature of the shares can produce "sudden demands for large sums" on the holder **[L2014-024]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test, applied.** The question is whether I have "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**, not whether I understand the product
  **[M2011-014]**. The product is plain: the company hires IT professionals and places them with clients, who are
  billed by the hour under time-and-materials contracts for about 90% of commercial revenue (10-Q `0000890564-26-000050`,
  Note 9); the consulting work uses "the same talent pool as our assignment work" (10-K FY2025 `0000890564-26-000013`,
  Item 1); the federal segment sells the same labour to agencies under T&M, cost-reimbursable and firm-fixed-price
  contracts of three to five years. Costs of services are "primarily compensation for our billable professionals"
  (Item 7). The economics are a spread between what the client pays per hour and what the professional is paid, less
  the cost of the recruiters and account managers who make the match, and the spread has held at a 28% to 29% gross
  margin and a 6% to 9% operating margin through the span read (Step 0). The key variables **[M1998-044]** are four,
  and the filings name them: hours billed and the rate per hour (disclosed through FY2019, not since), the pay of the
  professionals, the internal headcount (2,800 against 4,300 six years ago) and, for the federal third, the contract
  base (backlog 2.5× revenue, book-to-bill 0.8 to 1.1). The past statements do tell the future ones: the 2020 and
  2024 to 2025 downturns show the same shape, revenue down 8% then 3%, gross margin unmoved, operating margin down
  from 8.9% to 5.8%, cash still positive. Ten years out, an IT labour business of this kind will still earn a thin
  spread on hours, swinging with corporate IT budgets, in a field the filer itself calls "highly competitive and
  fragmented with limited barriers to entry" (10-K FY2025, Item 1A, and every 10-K read back to FY2016). That is a
  forecast the industry's own insiders write down every year in their 10-Ks, so test 5 **[M2000-105]** is met, and the
  winner need not be named because the field's shape, not the winner, is what the forecast rests on.
- **The doubt, stated.** What is not foreseeable to the decimal is the volume of hours: the Assignment business fell
  39% from 2022 to 2025 and billable full-time equivalents from 25,500 to 19,600, which the filer attributes to the
  macro cycle (10-K FY2024, Item 7; FY2025, Item 7), while the question whether AI tools reduce the hours of IT
  contractors that enterprises buy is open, the filer arguing the opposite in its July 2026 release
  (`0000890564-26-000047`). This is a forecast about customer behaviour, "what their prospective customers will do in
  the future" **[M2017-019]**, not about a technology the company must invent; it goes to the castle (Q2, test 11),
  which is where the rows put what can "destroy, or modify, or reduce the economic strengths" **[M2000-014]**. The
  precision asked is low, and the model of how far off one can be is wide but bounded: a smaller business of the same
  shape. Doubt about the castle is not doubt about the circle **[M2002-092]**.
- **Routing.** Not a bank or a lender; a business of two operating segments, each understood by the same economics,
  so the by-parts reading (Q1's holding-company paragraph, extended to segments by section B) finds no part outside the
  circle. The industry is not one of "rapid and continuous change" in the sense the rows rule out **[L2007-005]**,
  since the service (hours of labour) has not changed; what changes is the demand for it. The change question is
  therefore Q2's **[M1999-063]**.
- **VERDICT: IN.** The economics of the business ten years out can be foreseen in a general way **[M2000-037]**: a
  thin, cyclical spread on billed hours in a fragmented field, which the filer's own statements describe
  (10-K FY2025, Items 1 and 1A). The volume doubt is carried to Q2 as the first thing it must answer.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question starts from the attacker: "why is that castle still standing?" **[M1995-038]**. The filer's own answer to
the attacker question is given first, in its own words, because it decides the rest: "The IT industry is highly
competitive and fragmented with limited barriers to entry" (10-K FY2025, `0000890564-26-000013`, Item 1A); the same
sentence, with "contract staffing industry" or "professional staffing and consulting services industry" for the
subject, stands in the FY2016, FY2019, FY2022 and FY2024 10-Ks (`0000890564-17-000046`, `0000890564-20-000007`,
`0000890564-23-000004`, `0000890564-25-000008`). The rows say what follows: "there are some industries that are just
never going to have barriers to entry. And in those industries, you better be running very fast" **[M2012-106]**.

**The parts table** (section B; five-year segment operating profit 2021 to 2025, 10-K FY2025 Note 15 and 10-K FY2022
Note 15):

| part | five-year segment operating profit | share | castle | decides |
|---|---|---|---|---|
| Commercial (Assignment by the hour, 54% of 2025 segment revenue; Consulting 46%) | $1,645.7M | 78% | open, on the evidence below | yes, more than half |
| Federal Government (ECS; defence, intelligence, civilian IT contracts) | $453.9M | 22% | standing but ordinary, below | no |

The file closes on the Commercial segment. The federal part is read beside it and does not change the verdict.

**The castle tests on the deciding part, each with its filing fact.**
1. **What keeps it standing, and how permanent?** The filer's claim is a talent database and speed: "we can quickly
   build custom-fit teams for our clients", with "enduring, trusted relationships with enterprise clients" (Item 1).
   How permanent: by the filer's own account "clients are free to place orders with our competitors", "many of our
   agreements may be terminated at will", "Most of our agreements with clients do not provide for exclusive use of our
   services", and rivals "seek to gain or retain market share by reducing prices" (10-K FY2021, `0000890564-22-000007`,
   Item 1A; the same passage in FY2025). A relationship that the client can end at will and that is not exclusive is
   not a reason the attacker fails; it is the ordinary condition of a fragmented field, where "anything you do, your
   competitors can copy" **[M1996-017]**. The 2017 form asks what wards off the marauders, and the rows say "there are
   going to be marauders. And they'll never go away" **[M2017-012]**; nothing in the filings names a thing the marauder
   cannot do.
2. **Would it stand without the lord?** "Our workforce is and will always be the core of our business" (Item 1,
   Human Capital); the output is people's hours, sold by 2,800 internal staff who must "continually secure new
   contracts" (Item 1A). This is a business where "you have to stay smart", not one that "doesn't require good
   management" **[M1996-037]**; the test is failed in the sense that the castle is the sales force, which any rival
   can hire.
3. **The money test.** Could a well-funded attacker take it? The filer says the barriers are limited (above); the
   company itself entered federal IT by purchase in 2018 for $775M and bought six consultancies in five years, which
   is the attacker's path shown to be open; the two largest rivals in commercial IT staffing, Insight Global and
   TEKsystems, are private and file nothing with the SEC (flagged: no filing read), and the filer names "professional
   services firms, traditional consulting agencies, and specialized boutique industry or solutions-focused businesses"
   as the field (Item 1A). "Normally, if you've got a profitable business, you know, a dozen people want to go into it"
   **[M2000-077]**, and here the filer says they can.
4. **Pricing power and the agony before a rise.** The last disclosed rate figure is 2019: revenue per hour up 4.8%
   with hours up 4.8% (10-K FY2019); the filer stopped reporting hours and rates after that year. Since then the
   evidence is the margin: gross margin held at 28.8% to 28.9% in 2023 to 2025 while revenue fell 13%, but the filer
   attributes the hold to mix (more consulting), not to price, and reports commercial gross margin down 120 basis points
   in the first half of 2026 (10-Q, Item 2). Through vendor-management systems the client sets the terms: subcontract
   and VMS participation "may subject us to greater risks or lower margins" (10-K FY2021, Item 1A). No instance in the
   filings of a price rise taken against the client's wish; the price behaviour the rows say to observe **[M2005-020]**
   is not observable here because the filer does not disclose it, and what it does disclose (margin held by mix while
   volume fell) is the mark of the business whose rival sets its price: "whatever he charged for gas was my price"
   **[M2012-109]**.
5. **Unit volume and share of mind.** Billable full-time equivalents 25,500 (2022), 21,300 (2024), 19,600 (2025);
   Assignment revenue $2,476.1M (2022) to $1,500.1M (2025), −39% (10-Ks FY2022, FY2024, FY2025). The rows want "a lot
   more unit cases sold" **[M1999-054]**; here the units sold fell by a quarter in three years. Share of mind: the
   customer buys "IT professionals", and the filer's own competition paragraph says it is "viewed as a better partner"
   by the professionals, not asked for by name by the clients (Item 1). The company is now replacing its six brands
   with a new name (8-K `0000890564-26-000025`), which is the opposite of a name the customer asks for.
6. **The low-cost position.** The filer claims a "cost advantage over the competition" because "we do not rely upon a
   large bench" (Item 1). The filings give no cost per hour against any rival; what can be compared is below (the
   competitor row): the gross margin is in line with Kforce's and the operating margin below Robert Half's in every
   year but 2025. Not shown to be the low-cost operator, which in a commodity-like service "is all-important"
   **[L2000-017]**.
7. **The brand in the customer's mind.** Six brands, one being unified away; the Creative Circle trademark was the
   auditor's critical audit matter for impairment in 2025 (10-K, Deloitte report); trademarks of $305.2M carried as
   indefinite-lived against a business whose revenue fell three years running. No evidence the client asks for Apex or
   Creative Circle "by name" **[M2023-073]**.
8. **Would the customer still choose it over the low bid?** The contracts are non-exclusive, at-will, run through
   VMS platforms where the client compares bids, and the filer warns of rivals "reducing prices" (Item 1A). This is
   the customer who takes the low bid, and the rows' failing answer: "most insureds don't care from whom they buy"
   **[L2004-003]**; the See's question "would people still want to be both eating and giving away that candy in
   preference to other candies?" **[M2017-009]** has no analogue in an hourly IT contractor.
9. **Ask the competitors.** From their own filings (the row below): the whole field's operating margins fell together
   from 2022 to 2025, Robert Half's to 1.4%, Kforce's to 3.8%, this company's to 5.8%. No rival's filing names this
   company as the one it fears; the field moves as one, which is the mark of the commodity business where the
   industry's factors overwhelm any one firm's strategy, and the rows warn that "one competitor is frequently enough to
   ruin a business" **[M2012-108]** in a field where the filer counts its competitors as the whole fragmented industry.
10. **Widening or narrowing?** Commercial segment operating margin 12.2% (2021), 12.0% (2022), 10.8% (2023), 10.0%
    (2024), 8.9% (2025), while consulting rose from 22% to 46% of the segment's revenue; corporate SG&A rose from
    $77.3M to $111.1M; the filer "expect[s] competition to continue to increase particularly as we grow our IT consulting
    footprint" (Item 1). Narrowing, on the filer's own figures and words, the thing the rows say to watch "whether it's
    likely to widen further or shrink on you" **[M1999-108]**. The consulting pivot is a change for the better that
    has not shown in the margin over any full cycle: under section C it is credited only on the evidence of a full
    cycle **[L1995-022]**, and here the cycle in hand shows the margin falling as the mix rose.
11. **What could destroy, modify or reduce it, five to fifteen years out?** The question carried from Q1: whether
    AI tooling cuts the hours of IT contractors that enterprises buy. The evidence in hand is the 39% fall in Assignment
    revenue since 2022, which the filer attributes to the macro cycle and its July 2026 release reframes as "the last
    mile of the AI valuation equation will be IT services" (`0000890564-26-000047`); the rows ask what "will destroy,
    or modify, or reduce the economic strengths" **[M2000-014]**, and a business that sells developer hours is the one
    most exposed if the hours per task fall. It is not necessary to decide this; the castle is open on tests 1 to 10.

**The competitor row.** Same metrics from the rivals' own filings, ten fiscal years, transcription from each company's
XBRL as first filed (operating margin; operating income over tangible capital, defined as equity less goodwill and
intangibles plus long-term debt, pre-tax). Insight Global and TEKsystems are private, not SEC filers, flagged.

| company (latest 10-K accession) | op. margin, best year in the span | op. margin, worst year | op. margin 2025 (or latest FY) | OI / tangible capital, span |
|---|---|---|---|---|
| Everforth / ASGN (`0000890564-26-000013`) | 8.9% (2021, 2022) | 5.8% (2025) | 5.8% | 42% to 81% |
| Robert Half, RHI (`0000315213-26-000006`) | 12.5% (2021) | 1.4% (2025) | 1.4% | 7% to 70% |
| Kforce, KFRC (`0000930420-26-000007`) | 6.8% (2022) | 3.8% (2025) | 3.8% | 50% to 83% |
| CACI, FY June (`0001628280-26-054195`) | 9.6% (FY2026) | 6.8% (FY2017) | 9.6% | 58% to 77% (to FY2024; equity not tagged after) |
| SAIC, FY Jan/Feb (`0001571123-26-000029`) | 10.0% (FY2024) | 4.7% (FY2019) | 7.2% | 15% to 89% |
| Accenture, FY Aug (`0001467373-25-000217`) | 15.2% (FY2022) | 12.6% (FY2017) | 14.7% | 70% to 138% |
| Insight Global, TEKsystems (Allegis) | private; no filing | | | |

**The field's returns over the last full cycle, judged in words** (section C). On the tangible capital the businesses
need, every staffing and services firm in the row earns a high pre-tax return, because the capital is receivables and
a thin margin "only works in terms of return on capital if you turn your equity extraordinarily fast" **[M2017-096]**;
that is the field's nature, not a castle, since the same return is open to any entrant with a sales force and a credit
line. On the capital the owners actually paid, which must be counted "because we paid for it" **[M2011-060]**, this
company earned 13% pre-tax on equity in 2025 and 22% at the 2022 peak, with $1.2 billion of debt beside; Robert Half,
with no goodwill of size and no debt, fell from 58% to 6% on equity across the same cycle; Kforce from 64% to 40%. The
field's returns swing from excellent to poor with the IT hiring cycle and are set by the cycle, not by any firm's
position; the two federal contractors earn steady 7% to 10% margins on cost-based government contracts, a return that
is ordinary and regulated in effect. The returns of the field's durable players, read over the cycle, are those of a
commodity-like service, and the rows' marks of the commodity business are all present here, the customer's indifference **[L2004-003]**, every improvement passed to the customer,
the rival setting the price **[M2012-109]**, fewness of rivals no cure **[M2013-052]**.

**The federal part, beside.** Contracts of three to five years and a backlog of 2.5× revenue give visibility, and
cleared staff (about 500 cybersecurity and 900 AI and data professionals with clearances, Item 1) are a barrier of a
kind; but the customer can terminate for convenience, the 2025 revenue fell on DOGE-related contract losses, the
book-to-bill has been below one in two of the last three years and in the twelve months to June 2026, and the segment's
margin of 7.0% to 7.8% is the ordinary return of the cost-plus field CACI and SAIC show. A standing castle that protects
only ordinary returns is OUT under section C and, in any case, this part does not decide.

**Why OUT and not TOO HARD.** The rows send a castle to TOO HARD when its future cannot be judged, "a moat that's
tenuous in any way [...] We don't know how to valuate that" **[M2000-019]**. Here the future of the castle is not in
doubt; the filer states its condition in its own risk factors every year (limited barriers, non-exclusive at-will
contracts, price competition), the unit volume has fallen by a quarter, the margin has narrowed through the consulting
pivot, and the rivals' filings show the whole field moving with the cycle. That is "a castle shown on the evidence to be
filling in" in the words of the framework's routing paragraph: the list's first item, the business whose returns the
rivals copy, on the rows that say so **[M1996-017]**, **[M2012-106]**, and the customer who takes the low bid, on the
rows that say so **[L2004-003]**, **[M2017-009]**. A fair price does not reopen it: "What you
can't do is turn any investment into a good deal by paying little" **[M2019-015]**, and "If you really think a business
is declining, most of the time you should avoid it" **[M2012-062]**. The attacker test gives the answer the rows give:
"If the answer had been yes, we wouldn't have done it" **[M2011-015]**.

- **VERDICT: OUT.** The deciding part's castle is open on the filer's own evidence (10-K FY2025 Item 1A; 10-K FY2021
  Item 1A; unit volume, Items 1 of FY2022 to FY2025; segment margins, Note 15) and on the rivals' filings; the file
  closes here **[M2011-015]**, **[M2012-106]**, **[L2004-003]**. Q3 to Q6 are NOT REACHED; Q7 to Q10 are computed below
  under the heading COMPUTATION, NOT A CLEARANCE, as the T2 protocol requires.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED.** The file closed at Q2. The facts found that bear here (the ten-year balance sheets in Step 0; the
return on tangible capital against the return on the capital paid; the acquisitions as the growth spending) are under
AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The balance sheets were read in Step 0 as the template asks **[M2025-032]**. The facts found on the
real costs, the adjusted figure in the filer's own mouth and the tells are under AFTER THE STOP, not weighed.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.** Integrity facts were found (guidance each quarter, the adjusted figure featured, the pay design, the
ownership) and are recorded under AFTER THE STOP, not judged; the box line carries the flag.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** The buyback prices paid, the acquisitions and the pay plan are recorded under AFTER THE STOP; the
buyback test against the bottom of the computed range is recorded there too, as a fact and not a weighing.

## Q7 — WHAT IS IT WORTH? STOP.
### COMPUTATION, NOT A CLEARANCE
*(The file closed at Q2. Everything below is arithmetic required by the T2 protocol so that the rules under test can be
seen to bear; it carries no entry language and clears nothing, operator rule 3. The script is
`Framework/v5/tests/_work_T2_EFOR/q7_computation.py`, its output saved beside it.)*

**The cash, as the rows define it.** Value is "the discounted value of the cash that can be taken out of a business
during its remaining life" **[R1996-018]**, credited "for whatever net cash is left every year" **[M1998-080]**, after
asking whether more cash must go in **[M2014-068]**; the rate is the long government bond **[L2000-021]**, **[M1996-025]**,
5.66% (US Treasury 30-year, 2026-10-05). Owner cash after every real cost is operating cash flow less stock pay less
capital spending, year by year from the filed statements of cash flows (10-Ks FY2021 to FY2025); interest is already
paid inside it, and the company's own income tax is paid inside it (the floor is applied to cash after the company's
tax, section E; no carryforward or credit that runs out inside ten years was found: the deductible goodwill of the ECS
and TopBloc purchases amortises over fifteen years for tax, which is why cash taxes ran below the book provision, $5.0M
current against $49.1M in 2025, and that shelter runs past ten years, so section E's separate pricing is not
triggered; it is noted that owner cash on a book-tax basis would be about $30M to $45M a year lower in 2023 to 2025).

| year | OCF | SBC | capex | owner cash, after interest | aberrations removed | adjusted, after interest | + interest × (1 − 25%) | adjusted, before interest | acquisitions net of disposals |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 424.8 | 32.3 | 32.6 | 359.9 | −85.7 | 274.2 | 29.8 | 304.0 | 186.2 |
| 2021 | 193.7 | 52.7 | 34.7 | 106.3 | +134.4 | 240.6 | 28.1 | 268.8 | −281.0 |
| 2022 | 307.8 | 49.3 | 37.5 | 221.0 | +42.9 | 263.9 | 34.4 | 298.3 | 474.8 |
| 2023 | 456.9 | 44.0 | 39.9 | 373.0 | 0 | 373.0 | 49.8 | 422.8 | 0 |
| 2024 | 400.0 | 42.3 | 35.3 | 322.4 | 0 | 322.4 | 48.2 | 370.6 | 0 |
| 2025 | 327.9 | 47.9 | 39.8 | 240.2 | 0 | 240.2 | 50.8 | 291.0 | 304.1 |
| H1 2026 | 70.7 | 29.7 | 15.3 | 25.7 (H1 2025: 96.7) | | | | | 283.6 |

The aberrations are the two the filer itself names inside operating cash (10-K FY2021 `0000890564-22-000007`, Item 7,
Liquidity): the CARES Act payroll-tax deferral of $85.7M received in 2020 and repaid half in 2021 and half in 2022, and
$91.5M of income tax paid in 2021 on the gain on the sale of Oxford, a tax on a disposal and not on operations. 2020 and
2021 also contain the Oxford business's own cash until 2021-08-17, which cannot be separated from the filed cash-flow
statement and is left in, said so. The tax rate on the interest add-back, 25%, is a CONVENTION of this run (the federal
statutory 21% plus state taxes net of the federal benefit, 4.3% in the FY2025 10-K's rate reconciliation).

**The base: rule under test, section D(a).** The first year of the five-year window, 2021, is aberrational on the
filer's own account (the tax on the gain and the deferral repayment, above), and the last year, 2025, sits in a decline
that the first half of 2026 shows continuing, so neither end year is a fair base; the rows warn that "a base year in
which earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]** and that growth
presentations are distorted by "a calculated selection of either initial or terminal dates" **[L2003-004]**. The base
is therefore the average over the last full cycle, trough to trough, 2020 to 2025 (rule under test, section D(a)):
operating income troughed at $281.2M in 2020 and stands at $230.3M in 2025 with the first half of 2026 lower still, so
the 2025 trough is not yet established and the cycle may prove longer, said so. Cycle averages, adjusted: $285.7M after
interest, $325.9M before interest; net acquisitions $114.0M a year. The literal five-year window is shown beside it:
$252.6M after interest, $294.9M before interest (unadjusted), net acquisitions $99.6M a year. The rows' principle for the
cycle average is that a cyclical business is valued on the earnings over the whole run of years, "what difference does
it make to us if the earnings average, say, 300 million a year, if it comes in in a very lumpy fashion?" **[M2011-102]**,
and the price mistake is paying "too much, in relation to average earnings" **[M2021-039]**.

**The growth shown: rules under test, sections D(a) and D(b).** Section D(a) measures growth between the averages of
successive cycles; only one cycle exists on continuing operations (Oxford is inside every year before 2021 and ECS was
bought in 2018), so no earlier cycle average can be built, said so. The growth is therefore measured on the adjusted
series between the end years of the window, 2021 to 2025, before interest: $268.8M to $291.0M, 2.0% a year. Section
D(b) was checked: the series does not change sign and the compound rate between end years is meaningful once the
aberrations are removed, so the halves rule is not needed; the halves of the window give 5.3% and the halves of the
cycle 7.6%, shown and not carried, because the second half holds the GlideFast and TopBloc purchases whose cost is
charged below. The growth shown is positive, so section D(b)'s decline rule does not bear; the first half of 2026
(owner cash after interest $25.7M against $96.7M) is contrary evidence written down **[M1997-127]**, not a base.

**The acquisitions: rule under test, section D(c).** Cash paid for businesses net of businesses sold is capital
spending for the range: $114.0M a year over the cycle (the Oxford proceeds of $503.8M net against $1,197.7M paid for
ten businesses in 2020 to 2025). The default pair is applied: acquisitions deducted and the total growth credited (the
2.0% above is total growth, acquired revenue inside it; it is the rate at which the rows refuse the flattery, "We just
put way more capital into the business" **[M2023-081]**). The second pair, acquisitions left out and only organic growth
credited, cannot be shown because the filer reports no organic growth figure in any 10-K read (the pro forma rate for
Creative Circle in FY2016 was the last). TopBloc was financed by the $100M term loan A and the revolver (8-K
`0000890564-25-000042`, which names acquisitions and buybacks as the use) and Quinnox by the revolver (10-Q Note 5); both
are valued as if paid with equity, unlevered owner cash less today's net debt **[L2017-004]** (rule under test, section
D(c)). Quinnox closed after the window: its $283.6M of cash cost is inside today's net debt and none of its cash is in
the base, said so; the seller's figures in the January 2026 release are not used.

**Working capital: rule under test, section D(d).** The increase in working capital is inside operating cash flow
already (receivables, payables and accrued payroll lines of the statement of cash flows) and is therefore deducted; no
single year's draw is tied by the filer to one contract or event; 2025's receivables rise is attributed to days sales
outstanding generally (10-K Item 7). Nothing further to apply.

**Growth spending: rule under test, section D(e).** The filing allows the maintenance guess for property: capital
spending ($35M to $40M a year) runs level with depreciation ($38.0M in 2025, Note 8), the filer separates no growth
capex, and the rows accept depreciation as the proxy where it holds **[M1998-127]**, with the owner entitled to the
guess **[M2000-144]**; the growth spending of this business is its acquisitions, the second kind of need the rows name,
"optional outlays, aimed at business growth" **[L1999-024]**. The central case is therefore owner cash after
maintenance only, $325.9M before interest, with the growth spending charged against the growth it buys: that is the
case with net acquisitions of $114.0M deducted and the total growth of 2.0% credited, which is section D(c)'s default
pair. Section D(e)'s last sentence bears on the ends of the range: the no-growth end may not charge all spending and
also cap the growth, so the no-growth case is built on the maintenance-only base, and the after-acquisitions base at no
growth is shown beside and not used.

**The cap: rule under test, section D(f).** The rate carried, 2.0%, is below the discount rate, so no cap bites inside
or after the ten years **[M1997-095]**; no result traces to an absurdity **[M1999-067]**.

**The basis: rule under test, section H.** The central figure is built on the all-equity basis: owner cash before
interest and after the company's tax, against the market value of the shares plus net debt. Net debt is borrowings at
principal less cash at 2026-06-30, $1,451.8M − $152.9M = $1,298.9M (10-Q Note 5 and balance sheet; the filing states
long-term debt net of $3.7M of deferred loan costs and $10.0M of current principal, and the principal is used here, said
so); no finance leases are disclosed; operating leases ($62.5M) are left out, said so. The equity-only figure, owner
cash after interest against the market value, is shown beside it and never decides alone. The rows' reason: value a
business "on an all-equity basis" because debt makes "even a high-priced deal" look accretive **[L2017-004]**.

**The range** (ten years at the growth shown, then no growth, discounted at 5.66%; the framework's Q7 CONVENTION):

| case (all-equity basis, rule H) | base, $M | growth | whole business, $M | less net debt 1,299, $M | per share (41.0M) |
|---|---|---|---|---|---|
| after net acquisitions, total growth credited (D(c) default; D(e) central) | 211.9 | 2.0% | 4,387 | 3,088 | $75.3 |
| maintenance only, no growth (D(e): the no-growth end) | 325.9 | 0 | 5,758 | 4,459 | $108.8 |
| after net acquisitions, no growth (charges all spending and caps growth; shown, not used, D(e)) | 211.9 | 0 | 3,744 | 2,445 | $59.6 |

- **Value range:** $75 to $109 a share against $35.51 (all-equity basis, rule under test, section H); width 1.31 to 1.
  The ends are the two cases the rules produce, and the growth case is the bottom: at 2.0% total growth the $114M a
  year of acquisitions buys less cash than it costs, so the growth case is worth less than the business standing still
  without them. The literal window beside (rule under test, section D(a)): maintenance-only no-growth $95 a share;
  after acquisitions no-growth $53; the end-year growth on the unadjusted window (21% a year from the aberrational 2021)
  is not carried **[L2005-003]**. **Equity-only basis beside** (rule under test, section H): bases $285.7M maintenance
  only and $171.7M after acquisitions, growth 0.0% on the adjusted after-interest series; range $74 to $123 a share,
  width 1.67 to 1.
- **Fair price (a reporting figure, never a verdict; Part VII):** the price at which the midpoint of the range earns
  the floor of about ten percent **[M2003-149]**, **[M1994-004]**, applied to owner cash after the company's own tax
  and before the holder's, with no conversion (section E). On equity plus net debt (rule under test, section H): the
  midpoint of the two cases discounted at 10% is a whole-business figure of $2,844M, less net debt $1,299M, **$37.7 a
  share**. On equity alone: $55.7 a share. The two differ by $18 a share, which is rule H's point: the lenders take
  the first dollar, and the per-share discount on the equity-only basis is the magnified one **[L2017-004]**. No cheap
  price is reported.
- **The expected return at the price**, for the comparison at Q8: at an enterprise value of $2,755M (market value
  $1,456M plus net debt), the after-acquisitions growth case returns 8.9% and the maintenance-only no-growth case
  11.8%, both on the all-equity basis; on the equity-only basis against the market value alone, 11.8% and 19.6%.
- **What the computation would say if it were a verdict, which it is not:** the range is narrower than three to one,
  and the price sits below its bottom on both bases, by 53% on the all-equity basis; whether that is "startlingly low"
  **[L2000-025]** or a pencil-and-paper case **[M1996-084]**, **[M2009-005]** is not decided, because the castle is open
  and a tenuous moat is the thing the rows say they "don't know how to valuate" **[M2000-019]**; the cash stream of an
  open castle is not "how sure" **[M2009-004]**. The margin a run asks for grows as certainty falls **[M1997-080]**, and
  a wide margin does not substitute for the understanding the castle question withheld **[M2007-022]**.
- **VERDICT: NOT REACHED** (the file closed at Q2; the figures above are the protocol's required computation).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
### COMPUTATION, NOT A CLEARANCE
- **The bond.** The first filter is the government bond **[M1997-089]**, 5.66%. On the all-equity basis the expected
  return at today's enterprise value is 8.9% on the after-acquisitions growth case and 11.8% on the maintenance-only
  case (Q7); the first sits below the floor of about ten percent, "a point at which we drop out of the game"
  **[M2003-149]**, and the second above it. The rows want "a significantly higher return [...] than we are from a
  government bond" **[M2007-095]**; on the central case the margin over the bond is about three points, and on the
  maintenance-only case about six. Whether that margin would pass is not decided, because the comparison presumes a
  cash stream the castle question found unsure, and the rows take out of the filter the stocks one would "think so
  poorly of" that the bond is preferred **[M1997-089]**.
- **More of what I already own; the company's own stock.** The blind rule forbids knowing what is held; the ranking
  against the best thing already owned cannot be run and is not pretended. The company's own alternative, buying in its
  stock, is a fact for Q6 under AFTER THE STOP.
- **VERDICT: NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
### COMPUTATION, NOT A CLEARANCE
- **Debt against the ability to pay it, under bad conditions** **[M1995-104]**. Borrowings at principal $1,451.8M at
  2026-06-30 against owner cash after every real cost of $240.2M in 2025 and $25.7M in the first half of 2026 (Q7
  table): six years of 2025's cash, and the 2026 run-rate would not service it from operations. Interest expense, net,
  $67.7M in 2025 against pre-tax income of $162.6M, 2.4 times covered; in the first half of 2026, $37.5M against $31.3M,
  under one times. The secured leverage covenant stood at 2.17× lender-defined EBITDA against a limit of 3.75× stepping
  to 3.25× by mid-2028 (10-Q Note 5; 8-K `0000890564-26-000045`); the covenant is measured on EBITDA, the figure the
  rows call nonsense **[M1998-086]**, and a fall in earnings of the kind 2026 shows would close the gap.
- **Maturities, not assumed to roll** **[L2010-020]**: the $550.0M 4.625% notes are due in 2028; term loan B ($486.3M)
  in 2030; the enlarged revolver ($600M, drawn $318.0M at June 30 plus the term loan A it repaid in July) runs to 2031
  but springs forward to 91 days before the 2028 notes if more than $110M of them is then outstanding (8-K
  `0000890564-26-000045`). So a refinancing of the notes must be done by early 2028 or the revolver comes due with them:
  a near-term cash requirement of the kind the three strengths forbid, "no significant near-term cash requirements"
  **[L2014-023]**, against cash of $152.9M.
- **Valued as if it had no debt** **[L2017-004]**: done at Q7, rule under test, section H.
- **Sudden demands, counterparties, aggregation.** No collateral calls, derivatives or cash-out features; the lenders
  are a bank syndicate under a secured facility over "substantially all of the Company's assets" (10-K Note 9), so a
  covenant breach puts the switch in the lenders' hands, the capital-structure risk the rows name, "if there's a hiccup
  in the business that the lenders foreclose" **[M1997-009]**. The federal third depends on one customer that can
  terminate for convenience, with the DOGE-related losses of 2025 as the instance; the commercial two-thirds on
  corporate IT budgets that move together, the aggregation the rows warn of, "unrecognized concentrations of risk"
  **[M2003-034]**. Legal: wage-and-hour class and PAGA actions disclosed as not material (10-K Note 10).
- **The one STOP for a whole business bought**: criterion (3), "Businesses earning good returns on equity while
  employing little or no debt" **[R1997-001]**, is not met at $1.45 billion of borrowings against $1.8 billion of equity
  that is itself negative of goodwill; as a part-interest in the market the criterion is weighed, not applied
  (Q9's text).
- **WEIGHS AGAINST** (recorded, not a clearance): the debt is large against the cash the business now makes, carries
  a 2028 wall, and is secured on everything.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
### COMPUTATION, NOT A CLEARANCE
No position is taken. The framework would have the buyer do nothing: the file closed at Q2, and inaction is the
default, "you don't get paid for activity, you only get paid for being right" **[M1998-137]**. The omission test
**[M2001-006]** does not reach a business outside the castle's protection: passing over a business whose castle is
shown open is not the error the rows count, which is "something we understand, and we stand there and stare at it, and
we don't do anything" **[M2001-006]**. The price below the computed range is written down as the thing that would make
this an omission if the castle finding were wrong; that is the one fact a later run of this name should test first.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
Not one of the named businesses (casinos, tobacco, loading schemes). The money is made by placing IT workers and
delivering IT projects; the disclosed litigation is wage-and-hour and job-posting class actions, which the filer calls
not material (10-K Note 10). On the newspaper test **[M2008-011]** nothing found weighs against; recorded, not reached.

---
## THE BOX
**OUT, at Q2**: the castle of the deciding part (Commercial, 78% of five-year segment operating profit) is shown open
on the filer's own evidence and the rivals' filings; a test record, binding nothing. Q7 was computed and not reached:
$75 to $109 a share on the all-equity basis (rule under test, section H) against $35.51, fair price $37.7 (equity-only
beside: $74 to $123, fair $55.7), COMPUTATION, NOT A CLEARANCE. Integrity facts recorded, not judged.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on a later question, written down as found **[M1997-127]**; no verdict; the box unchanged
(operator rule 2).

**Q3.** Return on the capital the business needs: operating income over equity less goodwill and intangibles plus
debt, 42% to 81% pre-tax across 2016 to 2025 (Step 0 table; 10-Ks). Return on the capital paid, goodwill included
**[M2011-060]**: operating income over equity 13% (2025), 17% (2024), 22% (2022), on equity that carries $1.2 billion of
debt beside it. Reinvestment to stand still: capital spending $35M to $40M against depreciation $38M. The added capital
is the acquisitions, $1,197.7M paid for ten businesses in 2020 to 2025 and $283.6M for Quinnox in 2026; the company's
operating income in 2025 ($230.3M) was below 2019's continuing figure ($276.2M) after $2.0 billion of purchases since
2018, and the rows' test of added capital is what it earns **[M2023-081]**.

**Q4.** The real costs: stock pay $47.9M (2025), amortisation of acquired intangibles $64.8M, of which customer
relationships (six to thirteen-year lives) are the kind the rows say to add back **[L2012-003]** and are not added back
in the owner-cash figures, which are cash; "acquisition, integration, and strategic planning expenses" of $26.5M in
2025, $1.9M in Q4 2024, $9.8M in Q2 2026 and $8.3M in Q2 2025, every year a one-time item; a $4.4M software write-off;
a terminated deferred-compensation plan that raised the tax rate (10-K Item 7). EBITDA in the filer's own mouth:
"Adjusted EBITDA" leads every release and the proxy's bonus table, defined as EBITDA plus stock pay plus the
acquisition and integration expenses plus write-offs ($422.6M for 2025 against net income $113.5M; DEF 14A Annex A),
and the loan covenant is set on lender-defined EBITDA; the rows: "The one figure we regard as utter nonsense is the
so-called EBITDA" **[M1998-086]**, and the count of such purchases "is going to be about zero" **[M2002-026]**. The
featured adjusted figure and the guidance habit are the Q4 weighing carried to Q5 **[L2016-006]**. The accounts
themselves: no reserve movement, prepaid build or inventory found; the critical audit matter was a trademark's
impairment judgment; the goodwill test was qualitative; current taxes ran at $5.0M against a $49.1M provision in 2025.

**Q5 (integrity facts recorded, not judged).** Quarterly guidance ranges for revenue and adjusted EBITDA are given
and each release leads with their having been met or exceeded ("Revenues, Net Income, Adjusted EBITDA and Adjusted
EBITDA Margin Exceed the High-End of Guidance Estimates", 8-K `0000890564-26-000047`; "Revenues at the High-End of
Guidance Estimates", `0000890564-26-000008`); the rows on "guidance" and the desire to "hit the number" **[L2019-006]**
and on those who "consistently reach their declared targets" **[L2002-041]** bear, as does what managers "do in public
in relation to their investors and the promises they make" **[M2004-067]**. Against that: the 2025 cash bonus paid
below target (75.5% and 72.3% on the two metrics) and the 2023 performance shares paid zero on the NOPAT test with the
relative-TSR modifier at the 26th percentile (DEF 14A), which is a plan that did not pay when the numbers were not
made. The bonus's "Performance Target Adjusted EBITDA" added $21.3M of further adjustments (force majeure, litigation,
foreign exchange) to the release's own adjusted figure (Annex A). The chief executive, Theodore Hanson, has run the
company since May 2019 and been with it 27 years; 2025 total compensation $10,475,672, pay ratio 152:1; he holds 324,878
shares (about $11.5M at the price, 0.8%), all directors and officers 3.2%; his brother is employed as a consulting
services director with pay not reviewed by him (DEF 14A). Say-on-pay 98.7%; the chair is independent and separate; the
board is classified in three-year terms, which "certain stockholders" asked to change (DEF 14A). The CEO letter: none;
the releases speak of "a hallmark of our business" and "proven, repeatable acquisition strategy" and do not name a
mistake. Hunt for the disconfirming: the zero PSU payout and the independent chair are the facts for the people.

**Q6.** Part A. Buybacks: no stated price in any authorisation ($1.0 billion, 2025-11-17; 10-K Note 11), which weighs
against unless the prices paid sit at or below the bottom of the Q7 range **[L2016-002]**, **[L1999-023]**; the prices
paid were about $81 (2023), $94 (2024), $55 (2025) and $42 (H1 2026) a share against a computed range bottom of $75 on
the all-equity basis: the 2024 purchases ($329.3M) and most of 2023's were above that bottom, those of 2025 and 2026
below it; the rows' test is "what is smart at one price is dumb at another" **[L2011-003]**. Deals: six purchases in
five years for cash and a little stock; TopBloc's 10% in shares (458,283 at about $71.6) when the shares later traded at
$35; no all-stock deal, so the one STOP does not arise; value given against value got cannot be read because segment
assets and the acquired businesses' later results are not disclosed, and no post-mortem is published **[L2014-013]**.
The Quinnox release reports the seller's revenue growth and adjusted EBITDA margin for the first year, the projection
the rows decline **[M2011-083]**. Retention: equity $1,804M at 2025 against $1,865M at 2021 after $577M of net income
and $1,228M of buybacks; the share count down 24% since 2021; market value at the price $1,456M against $3.0 billion of
goodwill and intangibles bought. Part B. The cash bonus is 80% adjusted EBITDA growth and 20% revenue growth, both
company-wide, plus individual objectives paid at 175% to 200% of target in 2025; the performance shares are three-year
NOPAT growth with a relative-TSR modifier; the comparator group and the consultant (Semler Brossy) are named; a
clawback stricter than the SEC's is disclosed (DEF 14A). The rows read a plan by whether it ties pay "to what is
actually under the reasonable control of the person" **[M2003-019]**; growth in an adjusted figure that excludes stock
pay and integration costs is the thing the rows say to count, not exclude **[L2015-003]**. Directors' own purchases
with their savings are not disclosed as such; holdings are small except two founders' trusts.

**Q9.** The debt facts are in the Q9 computation above; the 2028 notes and the spring-forward are the near-term
requirement **[L2014-023]**.

**Q11 (for any later holding review).** The thing to watch is the volume of billed hours and the Commercial segment
margin against the consulting mix; the filer has stopped disclosing hours and rates, so the segment margin and the
billable FTE count are the only unit measures left in the filings.

## SELF-AUDIT
- [x] **Not fully.** `python tools/run.py EFOR` was run once before the template was copied, to see whether the tool
      worked on the new ticker; the copy was made before any other fetch. Confessed as a write-early violation. Written
      question by question and committed after each from the first commit on (five commits: Step 0 to the standing
      rule; Q1; Q2; Q3 to Q7; Q8 to Q12; this closing commit). The session was cut by a timed limit after the first
      stage was written and before it was committed; the first commit was made on resumption from what was on disk.
- [x] Dispatched as a T2 test re-run: the protocol grants the per-question commits with a two-path pathspec; the lock
      is the dispatcher's. The working folder path `Framework/v5/tests/_work_T2_EFOR` is ignored by the repository's
      `.gitignore` (line 117, `Framework/v5/tests/_work_*/`), so git refused it in the pathspec and every commit carries
      the run file alone; the working folder stays on disk, uncommitted, like the earlier test working folders. Not
      forced. A test record enters no register (T2 protocol).
- [x] The blind rule was kept: no run file, holding review, `PORTFOLIO.md`, resume state, register or reading list
      was opened, listed or searched; the accidental sightings (a directory listing of the tests folder made to find the
      protocol, git log subjects, the session's status and memory lines) are declared under CONTAMINATION and not used.
- [x] Every v5 id resolves (`check_run.py` in the working folder: 89 distinct ids in 117 citations, all in
      `principle_ledger_v5.csv`, no E-ids, every quoted fragment beside an id found in that row); every filing fact
      carries its accession; the numbers are filed figures, the rows' figures, or confessed conventions (the 25% tax
      rate on the interest add-back; the aberration adjustments taken from the filer's own statement).
- [x] The order was kept; Q2 closed the run; everything after it is headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash is operating cash flow less stock pay less capital spending, never a net-income proxy; the sovereign
      is the Treasury's own 30-year par yield; the price is an aggregator quote and is flagged.
- [x] Contrary evidence written down as found (the foundations line; the H1 2026 cash; the zero PSU payout); the facts
      for later questions are under AFTER THE STOP; the box line carries the integrity flag.
- [x] Not a point-in-time run; the anchor is today and no row is dated after it.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 rule lines and its "growth the price assumes" were
      ignored.
- [x] `python tools/check_framework.py` PASS before every commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Five things. **(1) Rule D(e) inverts the ends of the range.** The framework's Q7 CONVENTION makes the no-growth case
one end and the shown-growth case the other, both on one base; D(e)'s last sentence forbids charging all spending and
also capping the growth, so the no-growth end must stand on the maintenance-only base while the growth end deducts
the acquisitions. For a business whose growth spending buys less than it costs, as here (2.0% total growth against
$114M a year of purchases), the growth case becomes the bottom of the range and the no-growth case the top, and the
"width" then measures the value the acquisitions destroy rather than the uncertainty of the stream. The run applied
the rule as written and said so; the framework should say whether that is the intended reading or whether D(e)
means the no-growth end to stand on the maintenance-only base only when the growth spending is shown to earn its keep.
**(2) D(a)'s cycle has no clean prior cycle for a serial acquirer.** Growth "between the averages of successive
cycles" cannot be measured when the earlier cycle holds a business since sold and lacks one since bought; the run fell
back to the end years of the adjusted window and said so, but the rule gives no fallback. **(3) D(a) and the
not-yet-established trough.** The rule assumes the last trough is visible; here 2025 may not be the trough (H1 2026 is
lower), so the cycle average is provisional, and the rule should say what to do when the window ends mid-decline
(the D(b) decline carry was checked and did not bear because the adjusted end years rose, which itself looks wrong
against a first half down 73%). **(4) Rule H's "as the filing states them".** The filing states long-term debt net of
deferred loan costs and current maturities; the run used principal and said so; H should name principal. **(5) The
template's position note** asks the analyst to check `PORTFOLIO.md`, which the blind rule forbids; the protocol was
followed. Also noted: the brief's "sale of a staffing unit in 2024" is wrong (Oxford was sold on 2021-08-17; the 2024
cash flow shows no divestiture), its request for bill rates and utilisation through the downturn cannot be met from the
filings (not disclosed since FY2019), and its two-path pathspec cannot be honoured for the working folder because the
repository ignores it.
