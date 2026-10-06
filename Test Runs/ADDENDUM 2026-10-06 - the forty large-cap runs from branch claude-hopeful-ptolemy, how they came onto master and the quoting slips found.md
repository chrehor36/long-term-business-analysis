# ADDENDUM 2026-10-06: the forty large-cap runs from branch claude/hopeful-ptolemy-5kwiln, how they came onto master, and the quoting slips found

**Operator rule 6.** No run file is edited; this addendum records how the files arrived and what a mechanical check found in
them. It covers the forty purchase runs dated 2026-10-06 whose file names begin `2026-10-06 Run - ` and whose tickers are AAPL,
ADP, AMGN, AMZN, AXP, BA, BAC, CAT, CRM, CSCO, CVX, DIS, GD, GOOGL, GS, HD, HON, IBM, JNJ, JPM, KO, LLY, LMT, MCD, MMM, MO, MRK,
MS, MSFT, NKE, NVDA, PG, PM, SHW, TRV, UNH, V, WFC, WMT and XOM, with their `_research 2026-10-06 <TICKER>/` folders.

## Where they came from
A separate session ran them on the GitHub branch `claude/hopeful-ptolemy-5kwiln` of the public repository, from its export
commit 7ed1b2ab: the operator's twenty (the Dow by price weight), then twenty more (the rest of the Dow and the ten largest
never-run names on `Screens/_input/list_largecap.csv`). Because the public export carries no `PORTFOLIO.md`, no holding review
and no research folder, the runs were blind to the holdings by construction. Each run was committed question by question
(write-early kept), and the branch folded them into its own copies of the register, the reading list and the session-state
file. The branch could not write `tools/alerts.json` (its permission check refused the write), so no alert was armed there.

## How they came onto master
Not by a git merge: the branch descends from the public export, which is a different history from this repository. The run
files and research folders were copied by file on 2026-10-06, and the research folders enter only as `.gitignore` admits them
(raw filings stay out, as for every run since 2026-09-01). The branch's forty register entries and its two dated notes are
copied verbatim into `Screens/WATCHLIST RUN QUEUE.md` under `### REGISTER BACKFILL 2026-10-06 (b)`; its two reading-list
sections are appended verbatim to `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`. The fourteen names that closed
OUT at Q7 on price (ADP, AXP, CAT, GD, HD, HON, KO, MCD, PG, PM, SHW, TRV, V, WMT) now carry a fair-price alert at each run's own
figure (section F of the gaps case: the fair price alone; no cheap price), and the v4.1 bands of 2026-08-31 to 2026-09-04 on
CAT, HD, KO, MCD, PG, SHW and WMT are retired (left in the file, inactive, labelled), since the v5 runs of the same names
supersede those v4.1 runs for alert purposes. V is held; its holding review's add band ($300) stands beside the purchase run's
fair price ($114), the two resting on different ranges, to be reconciled at the next review.

The branch itself carries the research folders in full, including raw filings that the public repository's policy withholds
(`NOTICE.md`). It is recommended that the operator delete the branch on GitHub once this addendum is on master; nothing on it
is lost, since every run file and every fold line is now here.

## What the runs reported that the framework has since settled
Fifteen of the forty report a cheap price under a rule of the run's own, as the runs of 2026-10-05 did; these are reporting
figures, headed COMPUTATION, written before the operator's decision of 2026-10-06 (section F: no cheap price), and no verdict
uses them. The gaps the branch's fold lists overlap the gaps case decided the same day: the floor's tax basis (section E, now in
Q7), the measure of "the growth shown" and the negative or sign-changing figure (section D(b), under test), acquisitions and
finance-lease assets in owner cash (section D(c), under test). Two items the branch raised are still open for the operator:
**[M1994-063]** read two ways on the defence primes (the LMT run closed TOO HARD (NATURE) at Q2 on it; the GD run cited it and
read Q2 IN), and the tool defects the runs list (no retry on EDGAR's HTTP 429, no CIK override for a redomiciled filer, an
operating-cash line printed for banks and insurers).

## The quoting check, and what it flagged
The main session's check (every quoted fragment beside a ledger id must be in that row) was run on all forty files. Every id in
every file resolves to a row of `principle_ledger_v5.csv`, and no file cites a v4 id. The check flagged the fragments below as
quoted beside an id without being the row's own words. On reading, they are of the kind the addendum of 2026-10-06 on OSIS and
BCC records: the framework's own wording, a heading, or a paraphrase of the row, set in quotation marks beside the id of the
row it summarises. The rows say what the fragments say; the quotation marks are the slip. No verdict in any of these files
rests on the wording of a fragment rather than on the row it cites. Another analyst can verify each in under two minutes by
opening the row.

| file | id | fragment flagged |
|---|---|---|
| AAPL | M2023-034 | "much more of a consumer products business" |
| AXP | M2001-087 | "price past the moat" |
| AXP | M2013-043 | "could not get rid of American Express, or even get them to cut their fees" |
| CAT | L2014-026 | "hard to replace a mediocre CEO if that person is also Chairman" |
| CAT | L2002-020 | "6½-7% after corporate tax" (the row's own figure, with a character the source file renders differently) |
| CSCO | M2000-105 | "a forecast the industry's own insiders would not write down" (the framework's wording for the row) |
| GOOGL | M2004-092 | "being way wrong with Google or Apple" |
| GOOGL | M2000-105 | "Would the insiders write it down?" (the framework's wording) |
| GS | M2002-094 | "the readable half does not make the unreadable half readable" |
| JNJ | M1999-075 | "Businesses that live on continued invention" (the framework's Q1 list item) |
| JNJ | M2000-038 | "never OUT on the business" |
| LLY | M1999-075 | "Businesses that live on continued invention" (the framework's Q1 list item) |
| MCD | M2009-005 | "so far below" |
| MMM | M2002-009 | "is involved" |
| NKE | M2011-084 | "How far off could I be?" |
| NVDA | M2000-105 | "would not write it down" (the framework's wording) |
| PM | M2012-067 | "Can I name the winner, not just the industry?" (the framework's wording) |
| SHW | M2006-076 | "Is it important and knowable?" (the framework's wording) |
| SHW | M1999-130 | "Ask the competitors" (the framework's Q2 heading) |
| SHW | M2003-120 | "earned also on deposits that are added" |
| SHW | L2002-041 | "consistently reach[es] their declared targets" (an inflection inserted in brackets) |
| SHW | M1996-038 | "a long record, not a promise" |
| TRV | M2007-081 | "read rather than meet" |
| UNH | M2006-088 | "much of it is in the political realm" |
| UNH | M1999-126 | "all goes into the too hard pile" |
| UNH | M1999-119 | "economics usually win out" |
| V | M2005-090 | "a very important part of a director’s wellbeing" |
| WFC | M2005-068 | "no assurance" (twice) |
| XOM | M2009-059 | "still going to be doing fine" |

The rule these slips break is the canonical brief's: never an id beside words that are not the row's own, and never beside the
framework's own wording. The brief the branch's session used is not on master; whatever it said, the rule binds every run.
