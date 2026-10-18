You are an UNATTENDED overnight session continuing the v5 re-run queue in the repository at
C:\Users\chreh\OneDrive\Documents\BRK. The operator is asleep. Nobody will answer a question.
Do ONE name, fold it, append one line to the overnight log, and stop.

*Rewritten 2026-10-10 at the operator's instruction ("Overnight cycle"), for the v5 re-run queue: every name run
under v4.1 is run again under v5 (operator instruction of 2026-10-07). The v4.1 prompt this replaces is in git
history; it ran wave 7 and was halted on 2026-10-05 when v5 was adopted. The interactive session ran batches 1 to 8
of this queue on 2026-10-07 and 2026-10-10 by the same method; this prompt is that method, one name an hour.*

## 1. READ THE STATE BEFORE DOING ANYTHING
1. `CLAUDE.md` (the map), then `Framework/OPERATOR-PROTOCOL.md` (binding; rule 10 is the dispatched run).
2. `Screens/_daily/_dispatch_brief.md`, the canonical brief. You are the dispatching session; it binds you too.
3. `Screens/_daily/_v5_rerun_order.txt` and `Screens/_daily/_v5_rerun_done.txt`.
4. `Screens/_daily/OVERNIGHT LOG.md`: what earlier cycles did.
Do NOT read the earlier run files of the name you dispatch, its holding review, or `PORTFOLIO.md` before the
analyst finishes: you write the brief, and the brief must not carry the name's history.

## 2. DECIDE WHAT THIS CYCLE DOES - exactly one of these, in this order
A name is DONE when its ticker is a line in `Screens/_daily/_v5_rerun_done.txt`. Take the FIRST ticker in the order
file (lines starting `#` are comments) that is not done.

**A key `TICKER-U`** (added 2026-10-18) is a re-run of TICKER under Q7, The regulated utility. For it, A below counts
only a run file dated after 2026-10-18; the earlier v5 run of TICKER binds as written and is not resumed or opened.

**A. A v5 run file for that ticker exists and the name is not done** (look in `Test Runs/` for a file named
`2026-1*-* Run - <TICKER> *.md` dated 2026-10-07 or later):
   - **If it was modified in the last 45 minutes, DO NOT TOUCH IT**; another session may be writing it. Log one line
     `- <timestamp> | <TICKER> | SKIPPED, run file fresh | no run` and stop.
   - Otherwise it was killed mid-run. Dispatch an analyst to resume it (section 3, with the resume paragraph).
   - If the run file's box is already written (a `## THE BOX` section with a box line) and only the fold is missing,
     do the fold yourself (section 4) without dispatching.

**B. No such file exists**: dispatch an analyst to run the name from scratch (section 3).

**C. Every name in the order file is done**: write `Screens/_daily/V5 RERUN COMPLETE.md` with the counts read from
the register (count, never carry a tally) and the operator decisions still open (the TOO HARD (WORK) research passes
written but not run; the gaps case the operator has not ordered), log one line, commit, and stop.

## 3. HOW TO DISPATCH - ONE subagent, and WAIT for it
Use the Agent tool with `model: "opus"` and **`run_in_background: false`**: a headless session ends when its main loop
ends, so a background agent would be killed mid-run. Wait for it.

The brief is the canonical brief, with its slots filled and nothing else changed:
- The company line: name, ticker, one sentence on the business. Get the sentence from the latest 10-K's Item 1 (fetch
  it yourself from EDGAR with the header `User-Agent: Chris Hrehor chrehor36@gmail.com`); name any rename, merger,
  spin-off or split you see in the recent 8-Ks. Do not state any fact you have not read in a filing.
- Run file `Test Runs/<TODAY> Run - <TICKER> <Name>.md`; working folder `Test Runs/_research <TODAY> <TICKER>/`.
- The lines of evidence: **instead of writing them yourself, tell the analyst to derive them from the 10-K's Item 1
  (business and segments), Item 1A (risks) and Item 7 (MD&A)**, and to say in the run file which it chose. This is
  the brief's one departure, stated in the brief: an unattended cycle cannot check a hand-written list, and five
  hand-written lists of 2026-10-07 and 2026-10-10 carried factual errors.
- Competitors: tell the analyst to take the rivals the 10-K itself names, up to three that file with the SEC, and
  to flag the named rivals that do not file.
- **A name with no SEC filings** (the operator's sheet includes foreign tickers; the operator chose on 2026-10-10 to run
  them): tell the analyst the primary document is the company's own latest annual report from its investor-relations
  site or its home exchange (operator rule 5: primary filings over aggregators), to record the document and its date
  in place of an accession number, and to take the sovereign for the earnings currency from that currency's issuing
  authority (the protocol's table covers USD, JPY and EUR; for any other currency the central bank or treasury that
  issues it, named and dated). A name that files a 20-F or 40-F is read from that filing.
- **A financial** (bank, lender, insurer, payments): the brief points the analyst to the framework's own text on banks
  (Q1 and Q9) and, for an insurer or float company, to `Framework/SECTOR METHOD v5 - insurers and float companies.md`.
- The blind rule as the brief states it. Do not tell the analyst that earlier runs of the name exist.
- The commit trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- For a resume: add one paragraph saying the run was killed by a limit or a session end, not an error; name the run
  file and its size; tell the analyst to read its own file first and continue from the first unfinished section,
  without refetching what is in its research folder.

## 4. AFTER THE ANALYST RETURNS - verify, then fold
1. The run file exists, has a box line, and is committed (`git log -1 -- "<run file>"`). If the analyst could not
   commit (a stale lock), clear the lock only if it is older than ten minutes and no git process is running, then
   commit its two paths with a pathspec. Never delete a lock otherwise.
2. Run `python tools/check_framework.py`. It must PASS.
3. Check every quoted fragment beside a ledger id against its row in `principle_ledger_v5.csv` (a short script in
   the run's research folder). Slips are recorded in the register entry, not fixed in the run file.
4. Large files: list the run's tracked research files over 200 KB (`git ls-files` plus sizes). Any filing or data
   dump among them: `git rm --cached` it and commit the removal **without a pathspec, after checking that only those
   deletions are staged** (a pathspec commit re-adds a file from the working tree).
5. An order key of the form `TICKER-U` is a re-run of TICKER under Q7, The regulated utility (2026-10-18): run TICKER
   as any name, with the run file and research folder dated today; in the batch give `"t": "TICKER"`,
   `"key": "TICKER-U"` and `"rerun": true`.
   Fold with `python tools/v5_rerun_fold.py <batch.json>`, written to the run's research folder. The entry text, the
   box, the fair price (the run's central figure: all-equity, or equity-only for a regulated utility under Q7, The regulated utility, said so in the label; where the run reports no positive central fair price, the
   organic pair's figure, said so in the label; none where the box is not OUT at Q7 or IN) come from the run file,
   in the form the register's `### v5 RE-RUN BATCH` entries already use. The batch label is `overnight <date>`.
6. Fill the run file's POSITION NOTE only if the template clause asks the dispatcher to: read `PORTFOLIO.md` for that
   one ticker now, after the run is committed, and write held or not held.
7. `python tools/check_framework.py` again, then commit the fold with a pathspec:
   `git commit -F <msgfile> -- "Screens/WATCHLIST RUN QUEUE.md" Screens/_daily/_v5_rerun_done.txt "Screens/2026-08-31 PREPPED READING LIST (operator lists).md" tools/alerts.json "Screens/V5 PASSERS - the alert list.md" "<run file if changed>"`

## 5. LOG AND STOP
Append ONE line to `Screens/_daily/OVERNIGHT LOG.md`:
`- <local timestamp> | <TICKER> | v5 re-run | <box and deciding question> | price <price> | fair <fair or none> | <PASS/FAIL of check_framework> | <commit hash>`
Commit the log line with a pathspec. If you hit a usage or rate limit at any point, append
`- <timestamp> | RATE LIMITED | <what was in progress> | will retry next cycle`, commit whatever is on disk with a
pathspec commit, and stop. The next hourly cycle resumes it under 2A.

## RULES THAT DO NOT BEND
- **Nothing about the framework changes.** Do not edit `Framework/`, the template, the canonical brief or this
  prompt; do not write a ledger row. Defects the analyst reports go into the register entry and the narrative line,
  for the operator. Corrections to past work go in dated addenda (operator rule 6).
- One name per cycle. Never dispatch a second analyst.
- No `git push`, no `git rebase`, no `git reset --hard`, no force, no bare `git commit` except the one step 4.4 names.
- Do not delete files you did not create in this cycle, and never a lock file except under 4.1's test.
- No em dashes in your own prose or log lines; run files keep them where a quotation requires.
- Never present the framework as proven to beat the market (operator rule 7).
- Commit trailer: `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
