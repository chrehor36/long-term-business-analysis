## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (Step 0 with the
      foundations and standing rule; Q1; the facts after the stop, the computation and this audit), pathspec of the run
      file and the research folder only.
- [x] Dispatched to an analyst: the brief allowed the per-question commits. The lock is the dispatching session's (operator
      rule 10 (b)); the analyst did not write or check it. The fold into the register is the dispatcher's; until then this
      run binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; no file under `Test Runs/` was
      searched or listed except this run's own folder. What was seen by accident (the opening git status and commit
      subjects, the memory index) is declared under contamination at the top and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (checked by
      `Test Runs/_research 2026-10-13 HRIBF/scripts/check_ids.py`); no E-id is cited. Every filing fact carries its
      document and date (no accession numbers exist: Horiba is not an SEC registrant).
- [x] The order was kept; Q1 failed and closed the run; nothing after it is a clearance, and the Q7 figures are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy (operator rule 5);
      the sovereign is the JPY 30-year from the Ministry of Finance's jgbcme.csv, dated; the Tokyo price is an aggregator
      quote and is flagged; the stale OTC quote is flagged and unused.
- [x] Contrary evidence was written down as found (foundations; Q1's paragraph on the widening share and margins); the
      facts for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run; the anchor is today.
- [x] `tools/run.py` produced no output for this name (HTTP 404 at the SEC); none of its lines was used. All arithmetic is
      by hand from the filings, in `Test Runs/_research 2026-10-13 HRIBF/scripts/owner_cash.py` and `scripts/q7_compute.py`.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the notes file).
- Honest limits: the semiconductor segment's figures for the 2008-2009 downturn could not be read cleanly from the 2011
  annual report's charts and are not used; no rival's filing was read, because the company names none and the file closed
  before Q2; the H1 2026 lease balance was not restated in the semi-annual report and the year-end figure is used.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q7 specific (e) against the PG specific on growth.** The central case is maintenance-only owner cash "with the
growth spending charged against the growth it buys", and the growth shown "is measured on the aggregate owner cash". For
Horiba the two aggregate series grow at 12.1% (maintenance-only) and 1.2% (all spending, after acquisitions) over the same
window, and the choice moves the top of the range from about ¥13,100 to ¥35,100 a share. I measured growth on the central
(maintenance-only) series and deducted the growth spending, growing with it, for the ten years, stopping it after year ten
as specific (c) stops acquisition spending; the all-spending case is shown beside. The text does not say which series
carries the growth when (e) applies; it should. The box did not depend on it: no case earns the floor at the price.
(2) **The all-equity basis and interest income.** "Owner cash before interest" does not say whether interest earned on the
cash that is credited in net debt is removed. For a net-cash company it matters in the opposite direction from a borrower.
I removed net interest after tax at the statutory rate (¥0.5bn a year on average). (3) **The brief's competitor rule when
the annual report names no rival.** Horiba's yuho and integrated report name none; the brief has no instruction for that
case. The file closed at Q1, so no rival was chosen; a run reaching Q2 would need a rule. (4) **Q1 for a component maker
inside a fast-changing industry.** The routing sentence and its rows speak of businesses that "must deal with fast-moving
technology"; Horiba's product function has not changed in decades and its share and margins widened through ten years of
process change. Nothing in Q1's tests separates "the function is stable" from "the economics are foreseeable"; the box was
decided by test 9 (doubt) together with the company's own risk rating. A sentence saying whether a stable function inside
a changing industry is inside or outside the routing would make the call reproducible. (5) **Subsequent events.** The
net-debt convention adds "the subsequent events that filing itself states"; the interim dividend declared in the H1 report
and paid after its balance-sheet date was deducted as one. (6) **Non-registrants.** The template's accession fields and
`tools/run.py` assume an SEC filer; the brief's departure covered it, and the template could say so.
