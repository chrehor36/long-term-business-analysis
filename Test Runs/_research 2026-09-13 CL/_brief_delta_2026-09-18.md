DELTA TO `_brief_resume_2035.md` - READ THAT BRIEF FIRST, THEN THIS
Written by the overnight cycle of 2026-09-18 08:10 EDT (cycle `2026-09-18_0810`). The operator is asleep. Nobody will
answer a question. Everything in the earlier brief still stands except where this file corrects it.

## A. WHY THE GAP: FIVE DAYS, AND NOT BECAUSE ANOTHER SESSION WAS WORKING
The killed session stopped writing at 2026-09-13 17:09 and left its resume brief at 20:35-20:44. **No cycle has run since.**
`Screens/_daily/_overnight_logs/_scheduler_trace.log` shows every hourly cycle from 2026-09-14 13:35 through 2026-09-15 09:35
ending `RATE LIMITED (exit 1)`, then nothing until this one. The queue stalled on rate limits, not on work in progress.
**Nothing has touched the CL run file or its research folder since 2026-09-13. You own both.**

## B. THE RUN FILE KEEPS ITS DATE, AND STEP 0 AND Q1 ARE HISTORY
- The file stays `Test Runs/2026-09-13 Run - CL Colgate-Palmolive.md`. **Do not rename it and do not edit Step 0 or Q1**
  (operator rule 6: corrections go in an addendum, never by editing history).
- **Open your Q2 section with a dated resume note**, in the form the BAM, BN, AMZN and NVDA resumes used: that the first
  session was killed by a session limit with Step 0 (`d4398ab`) and Q1 (`0c3de6e`) committed, that the scheduler was rate
  limited for five days, and that this session resumed on 2026-09-18 and re-struck the price and the sovereign (see C).

## C. THE PRICE AND THE SOVEREIGN ARE FIVE DAYS STALE. RE-STRIKE BOTH, RECORD BOTH PAIRS.
Step 0 carries USD 30-year **5.35% (09/11/2026)** and **US$86.80 (2026-09-11 close)**, 797,172,829 shares
(10-Q cover `0000021665-26-000042`), cap US$69,194.6M.
- **[E4-15] asks for the currently observed rate, so the arithmetic must run on today's pair, not on a five-day-old one.**
  At Q5, strike the sovereign fresh from the **US Treasury daily par yield curve** through `tools/sources.py` `sovereign("USD")`
  (issuing authority first; FRED is the fallback only) and strike the close fresh through `tools/sources.py` `price()`, flagged
  as an aggregator quote.
- **Record both pairs in the Q5 section**, say plainly that Step 0's pair was struck on 2026-09-13 and is left as filed, and
  **use the fresh pair for every computed figure, including the cap.** Recompute the cap from the fresh close and the same share
  count, and re-confirm the share count against the 10-Q cover yourself. If a newer 10-Q or 8-K has been filed since 2026-09-13,
  read it: `Screens/_daily/2026-09-1[4-7] daily.md` reported no new filings from watched names, but CL is not on that watch list.
- For orientation only, never as a source: the daily fetch files show USD 30y 5.34% (09/14), 5.36% (09/15), 5.35% (09/16),
  5.29% (09/17). Strike it yourself.

## D. A DRAFT THE EARLIER BRIEF DOES NOT MENTION
`_research 2026-09-13 CL/resume/q2_org.py` and `resume/q2_org_out.md` (written 20:43-20:44, after that brief was composed):
a mechanical extraction of volume, net selling price, foreign exchange, organic sales and the current-year operating margin
**by region and year, 2016-2025, each from that year's own 10-K MD&A, with the source sentence carried beside every row**.
It is extraction and arithmetic, with no conclusion, and it is more useful than `q2_subject_out.md` because it shows its
sentence. It is still an unverified input: spot-check cells against the filings, and note that some cells read `?` or `n/f`
where the sentence did not give the component. **Do not treat any `?` as a zero.**

## E. WHAT YOU MUST NOT TOUCH
**Another session is working in this repository right now.** At 08:08-08:11 today it was writing
`Test Runs/_research 2026-09-18 NCLTY/` and `Test Runs/2026-09-18 Q2 FRANCHISE TEST - NCLTY Nitori.md` (Nitori, a Q2 franchise
test; not a wave 5 name, nothing to do with CL).
- **Leave every NCLTY file alone.** Leave `Screens/_daily/` alone, including the daily notes, the lock and the logs.
  Leave `Test Runs/_research 2026-09-13 ERIC/peers/OTHERS_row.md` alone (it is modified in the working tree by an earlier session).
- **Never run a bare `git commit` or `git add -A`.** Stage by name and commit with an explicit pathspec every time:
  `git add -- "<path>" ...` then `git commit -F "<fresh msg file>" -- "<path>" ...`. The index is shared.
- The `Screens/_daily/` untracked daily notes for 2026-09-12 through 2026-09-17 are not yours to commit.

## F. THE REGISTER COUNT, MEASURED THIS MORNING
`## COMPLETED FROM THE QUEUE` holds **96** entries right now, counted from the heading to `## THE WRITE-EARLY PROTOCOL` on
lines beginning `- **`. **After your entry it should read 97. Count it yourself and report the number you counted**, not this one.
The newest entry, which your entry goes above, is NVDA.

## G. ONE STANDING CAUTION, REPEATED BECAUSE IT HAS COST THIS QUEUE TWICE
The killed session left drafts written out of order: `sec_q3_draft.md`, `q2_subject_out.md`, `oe_out.md`, `q5_out.md`.
The BAM resume found two lines in that session's drafts that presupposed a Q2 verdict, one of them a thin-evidence Q4 IN.
**Hunt for the same thing here before any drafted line enters the run file.** Q2 is decided on its own evidence, on the
competitor row, and nowhere else. Report what you found.
