You are an UNATTENDED overnight session continuing the watchlist queue in the repository at
C:\Users\chreh\OneDrive\Documents\BRK. The operator is asleep. Nobody will answer a question.
Do ONE bounded unit of work, commit it, append one line to the overnight log, and stop.

**DATED NOTE 2026-10-05, read before anything else.** This prompt describes a run under v4.1 (six questions, the
Q1 to Q5 hard sequence, the v4.1 run template). v4.1 was superseded on 2026-10-05 by `Framework/THE FRAMEWORK v5.md`
(twelve questions in the speakers' order, three boxes, the v5 run template now at `Test Runs/_TEMPLATE - Company
Run.md`). The task `BRK-overnight` is disabled and must stay disabled until this prompt is rewritten for v5 and the
operator says the queue resumes. If a cycle reads this note while the task is somehow enabled: write nothing, log
one line `- <timestamp> | HALTED | prompt predates v5 | no run`, and stop. The v4.1 path in section 1 below is kept
as written and is now `Framework/ARCHIVE - v4.x (superseded 2026-10-05)/THE FRAMEWORK v4.md`.

## 1. READ THE STATE BEFORE DOING ANYTHING
1. `CLAUDE.md` (the map of the repository), then `Framework/OPERATOR-PROTOCOL.md` (the binding
   operator protocol and prime rules; it moved out of CLAUDE.md on 2026-09-25), then
   `Framework/THE FRAMEWORK v4.md` (the governing document).
2. `Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md` - every tooling change,
   six errors not to repeat, and eight source limits already tested (do not re-attempt them).
3. `Screens/WATCHLIST RUN QUEUE.md` - the `## COMPLETED FROM THE QUEUE` register, the tier
   rosters (a completed name is written `~~TICKER~~`), the six-step FOLD, the brief prohibition,
   and the TAIL-TRIAGE CORRECTION of 2026-09-12.
4. `Screens/_daily/OVERNIGHT LOG.md` if it exists - what earlier overnight cycles did.

## 2. DECIDE WHAT THIS CYCLE DOES - exactly one of these, in this order
The names still to be run are **WAVE 7: the operator's three CSV lists**, in the order of
`Screens/_daily/_wave7_order.txt` (one ticker per line). **A name is DONE when it has an entry under
`## COMPLETED FROM THE QUEUE` AND its ticker is a line in `Screens/_daily/_wave7_done.txt`** (append it at
fold). Take the FIRST name in the order file that is not done. **Names flagged financial are not in the order
file and are not run** (the operator's directive of 2026-08-30; the held-out list is in the queue's WAVE 7
section). Read the WAVE 7 section of `Screens/WATCHLIST RUN QUEUE.md` before dispatching. **Count from the
register, never carry a tally forward.** Each name has a screen row in
`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`; the brief carries it UNLABELLED.

**A. A run file exists for a name that is NOT done** (look in `Test Runs/` for
`2026-09-1* Run - <TICKER> *.md`):
   - **If that file was modified in the last 45 minutes, DO NOT TOUCH IT** - another session may
     still be writing it. Skip to the next name.
   - Otherwise it was killed mid-run. Resume it: read the file, continue from the first template
     section not yet complete, finish every gate the hard sequence allows, and do the full fold.

**B. No such file exists** for the first name not done: run that name from scratch.

**C. Every wave 7 name is done**: write `Screens/_daily/LISTS COMPLETE.md` with the standing count
   from the register and the operator decisions still open (the three banks; the ~17 unpriced watchlist
   names that were never written to disk), append a line to the log, commit, and stop. Do not start the
   three CSV lists or any other work unattended.

## 3. HOW TO RUN A NAME - delegate it to ONE subagent and WAIT for it
Use the Agent tool with `model: "opus"` and **`run_in_background: false`**. A headless session ends
when its main loop ends, so a background agent would be killed mid-run. Wait for it.

Write the brief to the standard of the recent ones in this conversation's successors - read
`Test Runs/2026-09-12 Run - BA Boeing.md` or `... ROKU Roku.md` for what a finished run looks like.
The brief MUST carry:
- The screen row from `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, where one exists.
  **BAM and BN have no screen row.** They were held as "BLOCKED and out of scope" on 2026-09-02 as
  asset managers with consolidated funds. That was a session's scheduling note, not an operator
  decision: **"blocked" is not a fifth verdict.** If the perimeter cannot be measured from filings,
  the honest output is UNRESEARCHED (document named) or UNKNOWABLE (reason stated) plus a price
  under `COMPUTATION — NOT A CLEARANCE`. BAM (CIK 0001937926) files 10-K/10-Q since its FY2025 10-K
  and dates only from the December 2022 spin from BN. BN (CIK 0001001085) is an MJDS filer: 40-F
  and 6-K, IFRS, so its share count is read off the documents by hand. For BN, read
  `Framework/SECTOR METHOD - owner earnings for insurers and float-bearing holding companies.md`
  and the BRK, L, WTM, MKL, HHH and GHC runs of 2026-09-02 as precedent.
- **Read the row as UNLABELLED. Never tell a run which gate will be boring** (the CGNX prohibition).
- **Name survival shapes from `Screens/SURVIVAL SHAPES - index.md`**, which lists every shape a run has named, with its number; add any new one there when folding.
- **Check every ledger id in the brief against `principle_ledger.csv` before sending it.** My briefs through
  2026-09-13 cited [E4-52] for "what pay vests on"; **[E4-52] is the lollapalooza row (converging flags) and
  the incentives row is [E4-27].** The SONY run caught it.
- Strike the sovereign fresh from the US Treasury daily par yield curve, dated. Do not inherit one.
- Re-strike the price and read the share count off the cover of the LATEST periodic filing
  (`python Screens/cover_shares.py TICKER`); never sum share classes without reading the charter.
- **Verify SBC RESOLVES and is COMPLETE**: BE's did not resolve (the screen subtracted zero) and
  Boeing's stock-settled 401(k) resolved under a tag no SBC element contains.
- Check `deal_note` and, if anything is deal-shaped, READ the filing: a live merger makes the quote
  a spread, not an owner-earnings price (ROKU).
- Rebuild the owner-earnings width over every window and both (c) ends; report dollars and a word
  wherever the bottom sits near or below zero.
- Write-early: create the run file first, append each section as it closes, commit after every gate.
  **COMMIT WITH A PATHSPEC: `git commit -F <msgfile> -- <paths>`.** `git add X && git commit` commits
  the whole shared index and has swept other sessions' files into wrong commits six times. Write scripts to the research folder; bash heredocs containing
  apostrophes fail in this environment. Write commit messages to a file and use `git commit -F`.
- Hard sequence Q1 to Q5; STOP at the first question that is not IN; any valuation before Q1-Q4
  close is headed `COMPUTATION — NOT A CLEARANCE`.
- The six-step FOLD at the end of `Screens/WATCHLIST RUN QUEUE.md`, done by the run itself.

## 4. AFTER THE SUBAGENT RETURNS - verify, do not trust
- Confirm the COMPLETED entry exists, the ticker is struck in its roster (search the WHOLE file,
  not one tier), and alerts plus a PORTFOLIO row exist ONLY if all four gates cleared.
- Run `python tools/check_framework.py`. It must PASS. If it does not, fix the cause and re-run.
- If the fold is incomplete, complete it yourself.
- Commit any remaining changes with `git commit -F <msgfile> -- <paths>` (a pathspec, never a bare commit).

## 5. LOG AND STOP
Append ONE line to `Screens/_daily/OVERNIGHT LOG.md` (create it if absent):
`- <local timestamp> | <TICKER> | <verdict line, e.g. Q1 IN / Q2 OUT> | <price> | <PASS/FAIL> | <commit hash>`
If you hit a usage or rate limit at any point, append
`- <timestamp> | RATE LIMITED | <what was in progress> | will retry next cycle`
commit whatever is on disk with a pathspec commit, and stop immediately. The next hourly cycle resumes it.

## RULES THAT DO NOT BEND
- **Nothing about the framework changes.** Do not add, merge or delete a question; do not write a
  ledger row; do not edit `Framework/`. Corrections to past work go in dated addenda, never by
  rewriting history (operator rule 6).
- No `git push` (the repository has no remote), no `git rebase`, no `git reset --hard`, no force.
- Do not delete files you did not create in this cycle.
- **Do not use em dashes in your own prose or log lines.** Run files keep them because PRIME RULE 1
  requires verbatim quotation, and the required heading is literally `COMPUTATION — NOT A CLEARANCE`.
- Never present the framework as proven to beat the market (operator rule 7).
- Commit trailer: `Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`
