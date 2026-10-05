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
*(appended as the runs land)*
