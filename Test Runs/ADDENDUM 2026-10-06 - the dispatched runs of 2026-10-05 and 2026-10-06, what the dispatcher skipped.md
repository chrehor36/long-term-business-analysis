# ADDENDUM 2026-10-06: the dispatched runs of 2026-10-05 and 2026-10-06, and what the dispatcher skipped

**Operator rule 6.** No run file is edited; this addendum corrects the record. It covers every purchase run dated
2026-10-05 and 2026-10-06 in `Test Runs/` (the file names begin `2026-10-05 Run - ` and `2026-10-06 Run - `; count them from
the folder), and the research passes of 2026-10-05 (HRB, BN, TBTC, SONY, MBUU). All were dispatched by the interactive session
to blind analysts, one analyst per name, with the briefs recorded in that session's transcript.

## What the runs kept
Every run cites the v5 ledger verbatim and nothing from the archived v4 ledger; the acceptance test passed before every commit;
the hard sequence was kept, with everything after a closing STOP headed COMPUTATION; the filings were read and their accession
numbers recorded; aggregator quotes are flagged; no run claims the framework beats the market. No verdict in any of these files
rests on anything this addendum records.

## What the dispatcher skipped, and on which rule
1. **Write-early (template self-audit, first line; `Screens/WATCHLIST RUN QUEUE.md`, THE WRITE-EARLY PROTOCOL).** Every brief
   said "do not commit". The analysts therefore wrote each file in one pass after the reading, and their self-audits say so.
   The protocol exists so that a run killed at a session limit loses one question, not everything; several runs of these two
   days were in fact killed at limits and had to be resumed from whatever was on disk. The fault is the dispatcher's, not the
   analysts'.
2. **The lock (`CLAUDE.md`, the Automation table; `Screens/_daily/_overnight.lock`).** The map says an interactive session
   running a name writes the lock first. None was written for any of these runs. Nothing collided, because the overnight task
   was disabled throughout, but the rule was not kept.
3. **The fold (`Screens/WATCHLIST RUN QUEUE.md`, THE FOLD).** None of these runs was entered in the register under
   `## COMPLETED FROM THE QUEUE` on the day it was run, so under `Test Runs/README - which run files are in force.md` none of
   them bound anything until the backfill of 2026-10-06, filed the same day as this addendum. The six names on the wave 7 order
   file among them (AROC, BOOT, EXTR, FIX, LINC, OSIS) were not added to the done file either.
4. **Reporting figures without one definition.** The operator asked each run for a fair price and a cheap price. The briefs
   defined "fair" (the price at which the central case clears the floor of about ten percent pre-tax) but left "cheap" to each
   analyst, so the cheap prices of these two days rest on rules that differ from run to run, each confessed in its file. They
   are reporting figures, labelled COMPUTATION, and no verdict uses them. `Framework/v5/CASE 2026-10-05 - gaps found by the
   small-cap runs, for the operator's approval.md`, section F, proposes one definition.
5. **A convention the text does not contain.** The briefs of the first small-cap batch (RES, DBD, MOV, CTS, MBUU) pointed the
   analysts to a Part VI convention for "a boom inside the five-year window". No such convention exists. The MBUU analyst said
   so and confessed its own; later briefs dropped the reference.
6. **The blind rule, two leaks.** The TBTC and SONY research-pass pre-registrations told both analysts to read a file that
   states the operator's holding (recorded in those passes' "two closes compared" files). The CVSA analyst's text search across
   `Test Runs/2026-10-05*.md` printed the names of three holding reviews; it opened none and declared it.
7. **A quoting slip, already corrected.** The OSIS and BCC runs quoted the framework's own phrase beside a ledger id; see
   `Test Runs/ADDENDUM 2026-10-06 - OSIS and BCC runs, framework wording quoted beside M2000-019.md`.

## What was done about it on 2026-10-06
The register backfill (`Screens/WATCHLIST RUN QUEUE.md`, `### REGISTER BACKFILL 2026-10-06`), the done-file and overnight-log
lines for the six wave 7 names, the narrative fold in `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`, the
opportunity-set note in `PORTFOLIO.md` for the gate-clearers, and the rules that keep it from happening again: operator rule 10
in `Framework/OPERATOR-PROTOCOL.md`, the section THE DISPATCHED RUN in `Screens/WATCHLIST RUN QUEUE.md`, two self-audit lines
in `Test Runs/_TEMPLATE - Company Run.md`, and the canonical brief `Screens/_daily/_dispatch_brief.md`.
