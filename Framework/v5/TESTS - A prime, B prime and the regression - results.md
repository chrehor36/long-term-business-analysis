# TESTS A', B' AND THE REGRESSION — results under the v5 drafts. 2026-10-04 to 2026-10-05.
**A record, scored against the pass rules fixed in `Framework/v5/PREREGISTRATION - v5 blind read and comparison.md`
before any transcript was read.** The protocol every test session followed is
`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`; the run files are in `Framework/v5/tests/`.
These runs bind nothing and change no verdict of record; v4.1 governs. *(this project's own record)*

## Test A' — reproducibility. Two independent sessions, two names, no contact.
**Pass rule:** the same verdict at every question for both names; quantities may differ, verdicts may not.

| | HRB analyst 1 | HRB analyst 2 | TJX analyst 1 | TJX analyst 2 |
|---|---|---|---|---|
| Q1 understand | IN | IN | IN | IN |
| Q2 castle | **TOO HARD** | **TOO HARD** | IN | IN |
| Q3 capital | not reached | not reached | weighs for | weighs for |
| Q4 earnings | not reached | not reached | weighs against, narrowly | weighs for |
| Q5 who runs it | not reached | not reached | IN; ability for | IN; ability for |
| Q6 use of money | not reached | not reached | weighs against | weighs for |
| Q7 value | not reached | not reached | **OUT** | **OUT** |
| The box | TOO HARD at Q2 | TOO HARD at Q2 | OUT at Q7 | OUT at Q7 |
| Value beside $132.68 | | | about $140 to $345 | about $130 to $300 |
| Holdings draft (HRB held) | six answers in the same direction as analyst 2 | six answers in the same direction as analyst 1 | | |

**Result: every STOP verdict and both boxes agree, on both names.** HRB: Q1 IN, Q2 TOO HARD, for the same reason in
both runs (the 10-K's own warning that AI and government pre-filled returns may reduce the need for assisted
preparation, which the draft's rows send to the too-hard box). TJX: Q1 IN, Q2 IN on the same competitor row built from
Ross's and Burlington's own filings, Q5 IN, Q7 OUT with overlapping value ranges and the price at the bottom of both.
**Two weighings diverged on TJX**, Q4 (whether eleven "above plan" releases in a row are the tell the rows name) and
Q6 (whether a fixed-sum buyback at rising prices with no stated limit weighs against). Under the rule as written the
test passes; the divergence is recorded as a defect in how the draft defines those two weighings, not rounded away.
Both HRB analysts also reached the same six holdings answers in direction, with Q5 (the better use of the money)
undecided for both because the protocol forbids opening the portfolio file.

**What the four sessions reported wrong in the draft, in common:** (1) Q1's doubt tests ("if it is not very
predictable, forget it"; "if you have doubts, it isn't") can close a file that the draft's routing sends to Q2, so two
analysts can reach the same box through different deciding questions; (2) nothing says whether a purchase STOP closes
Q11 for a held name, or whether an add to a TOO HARD name is barred; (3) the draft never says how a retailer passes
Q1 and Q2 while using retail as its example of false understanding and "to coast is to fail" as a failing answer;
(4) Q4's "rules OUT" lists the make-the-numbers habit beside confusing accounts without saying whether the habit alone
is suspicion; (5) Q7 with no floor number leaves a price just under a wide range to close as OUT or TOO HARD at the
analyst's choice; (6) `tools/run.py` prints two v4 ids and the ten percent floor into every run, a contamination all
four sessions declared and ignored; (7) my brief gave HRB's fiscal year-end wrong (June 30 since FY2022, not April 30);
both analysts used the filed year.

## Test B' — blind falsification. The five sealed cases of `Framework/v4/testB/`.
**Pass rule:** zero false passes against `_SEALED_KEY.json`, opened once after all five runs were written.

| case | identity (unsealed) | pre-registered expectation | v5 result | v4.1's result (2026-08-28) | score |
|---|---|---|---|---|---|
| A | WFC 2018-01-02 | Q3 should fail | **TOO HARD at Q1**: a global bank whose two sides cannot be read from the case | Q2 UNRESEARCHED, Q3 never cleared | not cleared; unconfirmable blind, as v4 found |
| B | AAPL 2016-05-16 | should pass Q1 to Q4 | **TOO HARD at Q1**: fast-moving technology; the consumer-behaviour reading needs data the case lacks | Q2 UNRESEARCHED | miss in the pass direction, the same property of blind testing v4 recorded |
| C | IBM 2011-11-14 | should fail | **TOO HARD at Q1**; named blind the EPS-from-buybacks-on-flat-revenue thesis and the shrunken-equity return | Q2 UNRESEARCHED, same thesis named | hit |
| D | OXY 2019-08-08 | defended, not graded | **OUT at Q2**: a commodity seller with no cost edge claimed | Q2 OUT | the same documented divergence from the author's own purchase |
| E | KHC 2018-01-02 | should fail or UNRESEARCHED | **TOO HARD at Q2**; biggest concern: brands losing pricing power to a few very large retailers and their own labels | Q2 UNRESEARCHED, single-year base named | hit |

**Result: zero false passes. Test B' passes its falsification half.** No case reached the IN box; the refusals land
where v4.1's did, and in two cases (C, E) the session named the later failure mechanism from the case alone. The
acceptance half is untestable blind under v5 exactly as under v4.1: Apple stops at Q1 because the one route in for a
consumer-technology business needs retention and product data the sealed case does not carry.

**Three defects of the test, not of the drafts, found by the sessions:** (1) the draft quotes rows dated after the
cases' anchors that name specific companies and how purchases turned out (M2012-073, M2017-019, M2023-030, M2020-035,
M2023-082, M2024-054 and the narrated-mistake lists), so a blind session is handed the speaker's later verdict; every
session declined to use them, and a point-in-time test under v5 needs a rule barring rows dated after the anchor;
(2) `CASE_B.json` carries a real identifier field, a gap in the de-identification, not looked up; (3) the case files
carry filing dates but no accession numbers and a weighted-average share count, so operator rule 4's record could not
be met and is marked unmet in every run.

**The draft's own gaps the five sessions named:** the bank door against the bank exclusion for a very large bank; no
box for "the documents that would decide this were not read" as distinct from "too hard in principle"; a mixed castle
(one company, several businesses) has no rule; the commodity producer with an unknown cost position has no default
between OUT and TOO HARD, and the PetroChina rows (M2004-082, M2005-023), where a commodity producer was bought cheap
against its reserves, are left out of Q2; Q12's place after a failed STOP is undefined.

## The regression — the six live names and the five Roth holdings
**Pass rule:** no pass mark; every verdict that differs from the v4.1 verdict of record is explained from the rows.
The union of the two lists is seven names; HRB and TJX are taken from Test A' (analyst 1's runs), the other five from
`Framework/v5/tests/R <TICKER> - run.md`. Prices are the 2026-10-02 closes (aggregator, flagged); sovereigns from the
issuing authorities (US Treasury 30-year 5.63%, ECB 30-year 3.835%, Japan MoF 30-year 4.122%).

| name | v4.1 verdict of record | v5 purchase draft | v5 holdings draft (held names) | the difference, explained |
|---|---|---|---|---|
| HRB | Q2 OUT, two blind analysts (Test A, 2026-08-27); held, three hold conditions pass | Q2 TOO HARD, both analysts | keep; threat graded major, not life-threatening; no add supported | same question, different box. v4.1 found the franchise failed on evidence; v5's Q2 sends a castle whose future turns on a technology the 10-K itself calls "difficult to predict" to the too-hard box (M2000-019, M2001-069) |
| TJX | Q1 to Q4 IN, quit on at the floor (Test A, 2026-08-27, "don't buy at $135") | Q1 and Q2 IN, Q3 to Q6 weighed, Q7 OUT at $132.68 (value about $130 to $345) | not held | same practical result: not buyable at the price. v5 closes OUT because the price sits at the bottom of a wide range and needs a pencil (M2009-005); v4.1 said "quit on at the floor" |
| TBTC | held; a Q2 moat defect (key person); business-fact sell line; no adds | Q1 IN narrowly, Q2 TOO HARD | keep by default; retained earnings weigh against; no add | same box class, different reason: v5 reads the filing's "rapid technological advances" and a 47.5% customer; v4.1 read the person |
| ASML | Q1 to Q4 IN (run of 2026-08-28); exited the same day on Q6's overvaluation condition | **Q1 TOO HARD** | weighs for on castle, management and retained money; against on price and on "a mistake to buy" | **the one real change.** v4.1 called the business understood and sold it on price; v5 will not call it understood (ten-year earnings turn on technology, three governments' export licences and customers' cycles; M1998-008, L1993-023, M2006-076). Both agree there is no purchase at 60 times earnings |
| V | never run under v4.1 (the anchor holding; its v3.0 run is history) | Q1 and Q2 IN (same-metric row against Mastercard), Q3 to Q6 weighed, Q7 OUT: value about $300 to $900, most $400 to $600, against $361 | keep; "neither buyer nor seller"; do not add at $361 | no v4.1 verdict to differ from. The first full reading of the Roth's anchor; the box turns on Q7's unfixed growth input |
| NCLTY | Q2 OUT (franchise test of 2026-09-18) | Q2 OUT | castle narrowed, weighs toward sale; retained money below a dollar; no add | the same, on the same evidence: price per customer up 14.5%, customers down 12.8%, sales flat, the board's own "being cheaper" priority |
| MITSY | Q2 OUT (run of 2026-08-28); held, three hold conditions pass | Q1 TOO HARD | keep by default; no add supported | one question earlier, same class: iron ore, LNG and oil prices, the yen and ¥1.4tn a year of new investment make ten-year earnings unforeseeable (M2002-092) |

**Result: every difference is explained, and all by one feature of v5.** No name reaches IN under either framework.
v5's third box, TOO HARD, takes four names (HRB, TBTC, ASML, MITSY) that v4.1 either failed on evidence (HRB,
MITSY) or called understood (ASML, TBTC's business). Two names are the same (NCLTY, TJX in effect). For the holdings,
the v5 holdings draft returns "keep, no add" on every held name, with "weighs toward sale" only on NCLTY's castle and
retained money; it names no outcome because the rows give none.

**The seven runs' common findings about the drafts:** (1) the overlap of Q1 and Q2 on rapid change lets a name close at
Q1 TOO HARD, Q1 OUT or Q2 TOO HARD, which scoring by "the deciding question" will show as disagreement; (2) Q7 has no
rule for the growth input or the horizon, so a wide range can close as OUT or TOO HARD; (3) the holdings draft's Q5
(a better use of the money) cannot be answered by a session barred from the portfolio, and its Q6 does not say whether a
purchase-draft TOO HARD on a held name is "a mistake to buy, now recognised"; (4) nothing settles whether an add to a
TOO HARD name is barred; (5) no rule for a holding company understood by its parts or as a whole, or for equity-method
income at Q3, Q4 and Q7; (6) the protocol's accession rule assumes an SEC filer; EDINET ids and the company's own
report stood in for NCLTY and MITSY.

## The five tests, as pre-registered
| test | rule | result |
|---|---|---|
| 1 acceptance test on the drafts | PASS with `--also` | **PASS**, both drafts |
| 2 Test A' reproducibility | same verdict at every question, two names | **PASS** on every STOP and both boxes; two weighings diverged on TJX, recorded |
| 3 Test B' blind falsification | zero false passes | **PASS**; acceptance half untestable blind, as under v4.1 |
| 4 regression | every difference explained | **done**; one real change (ASML), explained |
| 5 reconciliation and calibration | table complete; metric reported | **done**; hypothesis fails narrowly on one rule by the operator's ruling; 72 of 78 |

The ruling case for adoption can now be written. It carries these five results, the six load-bearing PARTLY rules, the
drafts' recorded gaps, and the PERMANENT finding against v4.1.

## The re-test after the correction pass, 2026-10-05: PG, two analysts
**Pass rule, as for Test A':** the same verdict at every question. Price $144.91 (close 2026-10-02, aggregator, flagged);
sovereign 5.63%. Both analysts worked under the corrected draft, including the Q7 range convention and the two kept
conventions.

| | PG analyst 1 | PG analyst 2 |
|---|---|---|
| Q1 | IN | IN |
| Q2 | IN (same-metric row against Kimberly-Clark) | IN (same-metric row against Colgate) |
| Q3 | weighs for | weighs for |
| Q4 | no STOP; weighs for | no STOP; weighs against ("Core EPS" with recurring restructuring; no make-the-numbers habit) |
| Q5 | IN on integrity; ability undecided | IN on integrity; ability undecided |
| Q6 | weighs against (a fixed $5bn buyback with no price, above the range) | weighs against (same, and the combined chair) |
| Q7 | **OUT**: about $103 to $130 a share against $144.91; return at the price about 5.1% | **OUT**: about $105 to $135 against $144.91; return 5% to 7%, below the floor |
| The box | OUT at Q7 | OUT at Q7 |

**Result: PASS.** Every STOP and the box agree, and the two ranges built under the new convention overlap almost
entirely; one weighing (Q4) diverged, as on TJX. v4.1's verdict of record for PG (wave 7, 2026-09) was Q1 to Q4 IN and
quit on at the floor: the same practical result. **Both analysts named the same four open inputs in the Q7 convention**
(aggregate or per-share growth; all capex or maintenance; "no real growth" against a nominal rate; the close when the
price sits above the range), plus the Q6 buyback test's dependence on Q7; the convention paragraph was given those
specifics the same day. Option B's gate is met.
