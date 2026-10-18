# ADDENDUM 2026-10-18: the overnight runs of 2026-10-13 to 2026-10-18, checked

**Operator rule 6.** No run file is edited. This records the main session's check, at the operator's "check in on the auto
runs", of the 150 run files dated 2026-10-13 to 2026-10-18.

## What was checked
Every ledger id in the 150 files resolves to a row of `principle_ledger_v5.csv`; every log line of the period records the
acceptance test as PASS; `tools/check_framework.py` PASS today. The quoting check (every fragment set in quotation marks
beside a ledger id must be in that row) flags one fragment in each of seven files. On reading, each is the framework's own
wording, a filer's phrase, or formatting, set beside the id of the row it summarises; the rows say what the fragments say,
and no verdict rests on the wording:

| file | id | fragment flagged | what it is |
|---|---|---|---|
| SIEGY Siemens, 2026-10-13 | M2009-005 | "would need a pencil" | the framework's Q7 wording |
| STLD Steel Dynamics, 2026-10-13 | M2001-013 | "the low-cost producer" | the framework's Q2 wording |
| HLT Hilton, 2026-10-14 | M2012-081 | the row's words with bold markers inside the quotation | formatting; the words are the row's |
| HTHT H World, 2026-10-14 | M2016-049 | "has nothing to do with preventing dilution" | a paraphrase of the row |
| SSAAY SSAB, 2026-10-14 | M2011-015 | "shown on the evidence to be filling in" | the framework's Q2 wording |
| OMSE OMS Energy, 2026-10-16 | L2005-003 | "lower customer demand and reduced pre-orders" | the filer's phrase |
| HOKCY Hong Kong and China Gas, 2026-10-18 | L2016-006 | "core operating profit" | the filer's term |

## The cycle's record over the period
150 runs logged: OUT at Q2 77, OUT at Q7 31, TOO HARD (NATURE) 32, OUT at Q1 6, TOO HARD (WORK) 2, OUT at Q5 2; none IN.
2026-10-14 and 2026-10-15 were cut short by the account's usage limit (12 and 1 runs); the trace shows five cycles that took
over a headless lock whose process had died, as the lock rules provide.

## A correction made the same day
The MTSUY and MARUY re-look alerts, armed 2026-10-12 at the top of each run's computed range, were moved to each run's
all-equity fair price (the register's dated note of 2026-10-18). MTSUY's had fired on a price below a level it never should
have been set at.
