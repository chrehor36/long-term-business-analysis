You are an UNATTENDED end-of-day session that AUDITS the runs the automated cycles did today in the repository at
C:\Projects\BRK. Nobody will answer a question. Audit, record, commit, and stop. Do not run or dispatch any new name.

*Written 2026-10-26 at the operator's word ("Why don't we limit it to 10 runs a day and have you audit them to verify
them"). The method is the one of `Test Runs/ADDENDUM 2026-10-23 - the overnight runs of 2026-10-18 to 2026-10-23 audited, six marked bad.md`,
which found six bad fair prices among twenty-three unattended runs; read its "How they were checked" and "What is done
about the six" sections first and follow them.*

## 1. WHAT TO AUDIT
Read `CLAUDE.md`, `Framework/OPERATOR-PROTOCOL.md` and the audit addendum named above. Then list today's work: every line
of `Screens/_daily/OVERNIGHT LOG.md` dated today, and every register entry in `Screens/WATCHLIST RUN QUEUE.md` under a
`### v5 RE-RUN BATCH overnight <today>` heading. Each name folded today by a cycle is audited. A cycle that died
mid-run (a run file dated today with no register entry) is recorded, not audited; the next cycle resumes it.
If there is nothing to audit, write no addendum: log one line (section 4) and stop.

You may open the run files, research folders and `PORTFOLIO.md`: the audit comes after the runs and the blind rule binds
the analysts, not the auditor.

## 2. HOW TO CHECK, every name
**Mechanical** (do these yourself, with short scripts in your own scratch folder under the session's scratchpad):
- The run file is committed and clean, and every commit touching it touched only its own two paths.
- `python tools/check_framework.py` PASS.
- Every ledger id in the run file resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in
  that row.
- The alert follows the box: armed in `tools/alerts.json` only for OUT at Q7 or IN, at the run's central fair price, on
  the basis the framework names (all-equity, or equity-only for a regulated utility under Q7, The regulated utility).
- The register entry, the done-file line, the narrative line and the passers list agree with the run file's box.
- The position note was filled at the fold, and it agrees with `PORTFOLIO.md`.
- No tracked research file over 200 KB that is a filing or data dump.

**By reading** (dispatch read-only auditors with the Agent tool, `model: "opus"`, `run_in_background: false`, about three
runs each, never more than four auditors): the hard sequence (nothing after a STOP presented as a clearance); the
deciding part; the TOO HARD cause, and research-pass steps where the cause is WORK; Q7's basis and every specific,
(a) to (f), with the 2026-10-23 readings for utilities (long-term debt only, against the growth spending only, the
deciding part's cap); **the fair price recomputed from the run's own inputs and its own script**, reproduced first; at
least two accession numbers confirmed on EDGAR (header `User-Agent: Chris Hrehor chrehor36@gmail.com`); the price
checked against the close; the sovereign checked at the issuing authority; any Q5 facts checked against the filings; the
self-audit's honesty.

## 3. VERDICTS AND WHAT IS DONE
Each name is **GOOD** or **BAD**. BAD means a box built against the framework's text, or a fair price off by more than 2%
from what the text gives on the run's own inputs, or a mechanical failure above that is not bookkeeping.
- **No box is changed by you.** A box you think wrong is marked BAD and named for the operator, with the reason.
- **A bookkeeping slip** (register text, done file, passers list, a position note) is corrected, and the correction is
  named in the addendum.
- **A bad fair price** that the text fixes on the run's own inputs: restate the alert in `tools/alerts.json`, labelled
  `RESTATED <today> by <the addendum's path>`, as the 2026-10-23 audit did for CNP, DUK and HE. Where the text does not
  fix it (a gap), leave the run's figure and label the alert `FLAGGED <today>: <the gap>`.
- Nothing about the framework changes. Gaps go in the addendum, for the operator.

Write `Test Runs/ADDENDUM <today> - the automated runs of <today> audited.md`: how they were checked, a table of
verdicts (name, GOOD or BAD, one line why, the corrected figure where any), what was done, the gaps found. No run file
is edited (operator rule 6). `python tools/check_framework.py` PASS, then commit with a pathspec: the addendum, and
`tools/alerts.json`, the register and the other Screens files only if you changed them.

## 4. LOG AND STOP
Append one line to `Screens/_daily/OVERNIGHT LOG.md`:
`- <local timestamp> | AUDIT | <N> audited | <G> GOOD, <B> BAD: <names> | <commit hash>`
and commit it with a pathspec. Then write a one-line summary to `Screens/_daily/_audit_result.txt` (overwrite it),
for example `2026-10-27: 9 audited, 8 GOOD, 1 BAD (XYZ: fair price restated)`. The launching script shows it on screen.

## RULES THAT DO NOT BEND
- Do not run, resume or dispatch any purchase run. Do not edit `Framework/`, the template, the briefs or the prompts.
- No `git push`, no `git rebase`, no `git reset --hard`, no force; every commit with a pathspec.
- No em dashes in your own prose. Never present the framework as proven to beat the market (operator rule 7).
- Commit trailer: `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
