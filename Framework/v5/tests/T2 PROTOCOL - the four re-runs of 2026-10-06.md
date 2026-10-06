# T2 PROTOCOL: the four re-runs of 2026-10-06
*How a test re-run under `Framework/v5/tests/RULES UNDER TEST 2026-10-06 - sections D and H.md` is done. It departs from the
canonical dispatch brief (`Screens/_daily/_dispatch_brief.md`) only where this file says. These runs are test records: they bind
nothing, enter no register and change no verdict of record.*

## What the analyst reads
1. `Framework/THE FRAMEWORK v5.md` in full, as it reads today.
2. `Framework/v5/tests/RULES UNDER TEST 2026-10-06 - sections D and H.md`: apply its two texts exactly as if they stood where each
   says it stands, and write "rule under test, section D(a)" (or whichever) in every sentence where one bears.
3. `Test Runs/_TEMPLATE - Company Run.md` (the surface; copy it), `principle_ledger_v5.csv`, `Framework/OPERATOR-PROTOCOL.md`.
4. This file.

## What the analyst does not open
Everything the canonical brief's blind rule lists, and in addition: every file under `Test Runs/` except the template; every
`Framework/v5/CASE ...` file; every `Framework/v5/PREREGISTRATION ...` file; every other file under `Framework/v5/tests/`
(the earlier test runs carry verdicts on companies). A text search across those folders counts as opening them. Anything seen
by accident is declared under contamination in the run file and not used.

## Where the run goes
- The run file: `Framework/v5/tests/T2 <TICKER> - rerun.md`, copied from the template before any fetch.
- The working folder: `Framework/v5/tests/_work_T2_<TICKER>/`.
- Commit after each question with a pathspec of these two paths only:
  `git commit -m "T2 <TICKER>: <question closed>" -- "Framework/v5/tests/T2 <TICKER> - rerun.md" "Framework/v5/tests/_work_T2_<TICKER>"`,
  the message ending with the project's trailer line `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.
  Never `git add -A`, never push, never commit any other path.

## The run itself
As the canonical brief says: write-early; `python tools/run.py <TICKER>` arithmetic lines only; `python Screens/cover_shares.py
<TICKER>`; SEC EDGAR with the header `User-Agent: Chris Hrehor chrehor36@gmail.com`; competitors from their own filings; the hard
sequence, with everything after a closing STOP headed COMPUTATION, NOT A CLEARANCE. **Whatever the box, compute Q7 to the end
as a COMPUTATION**, so that the rule texts under test can be seen to bear: the value range, the fair price (the price at which
the midpoint of the range earns the floor), each on the basis the rules state, with the equity-only figure beside. No cheap
price. Report no other price figure.

## The reply
Box and deciding question; every place a rule under test bore, with its paragraph letter; the Q7 figures on each basis against
the price; what you could not get; what you saw of the blind-listed files. No em dashes in your own prose.
`python tools/check_framework.py` must PASS before each commit.

*Dated note, 2026-10-06, after the four runs: the commit pathspec above names the working folder, which `.gitignore` (the `Framework/v5/tests/_work_*/` line) already ignores, so every analyst committed the run file alone and the working folders stay on disk untracked, as the earlier test runs' do. All four analysts reported it; the line stands as written for the record. The template's position note asked for `PORTFOLIO.md`; the template now carries a blind-run clause.*
