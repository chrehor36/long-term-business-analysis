# PROTOCOL — running a name under the v5 drafts, for Tests A', B' and the regression. 2026-10-04.
**Pre-registered in `Framework/v5/PREREGISTRATION - v5 blind read and comparison.md`, "The tests a candidate must pass".**
This file fixes how every test run is done so that the runs can be compared. v4.1 governs the project; these runs
bind nothing and change no verdict of record. *(Dated note 2026-10-05: written while v4.1 governed; v5 was adopted the
next day on the strength of these tests, and the draft paths below were repointed to the governing files that day. The
seventeen runs in this folder remain test records and still bind nothing.)* They test whether the v5 drafts can be applied, reproduce, and refuse
what they should refuse.

## What a test session may open
- `Framework/THE FRAMEWORK v5.md` (the purchase draft) and, for a name the operator holds,
  `Framework/THE HOLDINGS FRAMEWORK v5.md`.
- `principle_ledger_v5.csv`, to read any row by id.
- `Framework/OPERATOR-PROTOCOL.md` for the rules of evidence (operator rules 4 and 5: read the filing, record document,
  date and accession; sovereign from the issuing authority; primary filings over aggregators, aggregators for live
  quotes only and flagged).
- `tools/sources.py` and `tools/run.py` (`python tools/run.py TICKER` prints the arithmetic: filing facts from SEC EDGAR,
  the sovereign, the market cap; it fills no judgment), `Screens/cover_shares.py` for the share count, and SEC EDGAR
  itself for the filings. For Test B' the case files in `Framework/v4/testB/` are the only data.
- Its own output file, and nothing else under `Framework/v5/tests/`.

## What a test session may NOT open
`Framework/ARCHIVE - v4.x (superseded 2026-10-05)/THE FRAMEWORK v4.md`, `Framework/ARCHIVE - v4.x (superseded 2026-10-05)/THE HOLDINGS FRAMEWORK.md`, anything else in `Framework/` or `Framework/v4/`
except the testB case and description files, `principle_ledger.csv`, any file under `Test Runs/` or `Screens/` (prior
run files carry the verdicts of record and would contaminate the test), `PORTFOLIO.md`, the other test sessions' files,
and `Framework/v4/testB/_SEALED_KEY.json`. For Test B' the session does not search the web for the company's identity
and does not guess it in writing; it works from the case numbers and the description.

## The run form
Write `Framework/v5/tests/<prefix> <TICKER or CASE> - <analyst or run>.md` with these sections, in order, each closed
before the next is opened:
0. **Step 0.** Price (date, source, flagged if an aggregator), share count by class from the latest filing's cover
   (document, date, accession), market cap, the sovereign for the earnings currency (issuing authority, dated). For
   Test B' the case file supplies these and the step records them as given.
1. **The foundations**, one paragraph: nothing to decide, but state which foundation bears on this name (a share as a
   business; the market serving or instructing; margin of safety; macro kept out; who is paid to tell you; the
   analyst's habits), with ids.
2. **The standing rule**, one line: does owning this put the buyer at risk of ruin (the buyer's conduct, not the
   target's)? Ids.
3. **Q1 to Q8 in order.** Each question: the test as the draft states it, applied to the filings; the verdict in the
   draft's own words, **IN, OUT or TOO HARD** for a STOP question, **WEIGHS FOR / WEIGHS AGAINST / UNDECIDED** with one
   sentence for a WEIGHING question; every judgment cites at least one v5 id in bold; the filing fact it rests on
   with its accession. **A STOP that returns OUT or TOO HARD closes the run**: later questions are marked NOT REACHED
   and may be recorded for the record under a heading `COMPUTATION — NOT A CLEARANCE` if the session wants to show
   the arithmetic, but no value is reported as a clearance. Q4 is a STOP only on confusion or suspicion about the
   accounts; Q5 only on integrity.
4. **Q9 and Q10** if reached: ruin as a weighing of the target's debt and exposures; the fat pitch and sizing as a
   weighing (no position is taken; say what the draft would have the buyer do).
5. **Q11 and Q12** where they apply: Q11 only for a name the operator holds, under the holdings draft (its six
   questions, each answered as the draft states them); Q12 the newspaper test.
6. **The box.** One line: IN, OUT or TOO HARD, with the question that decided it, and for a name that reaches Q7 the
   value as a range in round numbers beside the price, in the draft's own form (how much cash, how sure, how soon, at
   the long government rate; is the price so far below that it needs no pencil).
7. **Self-audit.** Every id resolves (grep it); every filing fact has an accession; no number appears without a row or a
   filing; no file outside the whitelist was opened; the order was kept and the first STOP stopped the run.
8. **What in the draft was wrong or unclear**, one paragraph: the instruction you found ambiguous, missing or
   unworkable, and what you did. Every draft so far has had one.

## Rules that do not bend
- Verbatim quotes only, from the v5 ledger or the filings; no em dashes in your own prose (the draft's heading and
  attribution forms keep theirs).
- The hard sequence: a STOP that fails closes the run; no value is a clearance before Q1 to Q6 are IN or weighed.
- No position is taken or recommended. The box and the value stance are the output.
- Commit nothing; the parent session commits and scores.
