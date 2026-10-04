# v5 — PRE-REGISTRATION. A blind read of the annual meetings, and the comparison against v4.1.
**2026-10-03. Committed BEFORE any transcript is read for rows.** Results append below the line. The case this
serves is `Framework/v5/CASE 2026-10-03 - v5 from the meetings, for the operator's approval.md`.

## The question

The operator's theory: the annual meetings are the conglomeration of every lesson Buffett and Munger learned,
so a framework built from the meetings alone, with the report each meeting answers, carries every load-bearing
rule. v4.1 was built from the whole shelf; 139 of the 204 ids it cites rest on no meeting. **Stated so it can be
refuted:** *a framework drafted only from the meetings and their reports reproduces every load-bearing rule of
v4.1.* It FAILS if any load-bearing rule of v4.1 is absent from the meetings after a recorded sweep of all 32
transcripts, or is contradicted by them. A FAIL is informative: it names what the meetings do not carry. A PASS
is not "the meetings say the same thing"; the whole-shelf read missed doctrine three times in August alone, so
the meetings are expected to add rules v4.1 lacks, and those are recorded as NEW.

**Load-bearing** (the Test D definition, kept): stated three or more times across the source, or framed by the
authors as central ("the most important", "the first rule", "the number one"), and capable of changing a run's
verdict.

## Design

### The unit and the order
One unit is one meeting **session**: the text between one `## ` heading of a transcript and the next (31
transcripts split Morning and Afternoon; 2020 splits `## Part 1` and `## Part 2: Q&A`). 64 units, in
`Screens/_daily/_v5_order.txt`, read in calendar order 1994 to 2025. The AM unit of a year also reads the
chairman's letter for the fiscal year the meeting discusses (meeting Y answers FY Y-1) and the signed sections
of that year's annual report where one is on disk (FY1995 onward); the PM unit reads the session alone. A whole
meeting with its letter would run to about 150k tokens and risk a mid-read compaction, which for a blind read is
the worst available failure; a session unit stays under about 100k.

### The blind rule
The reading session may open: the cycle prompt, the order and done files, the read log, the unit's transcript,
letter and report file, `principle_ledger_v5.csv`, `Framework/v5/**`, and run `tools/v5_ledger.py`. It may not
open `Framework/THE FRAMEWORK v4.md`, `Framework/THE HOLDINGS FRAMEWORK.md`, any other `Framework/` file,
`Framework/v4/`, `principle_ledger.csv`, `Test Runs/`, `Screens/SURVIVAL SHAPES - index.md`, or any run or
research file. **Declared contamination, which this design cannot remove:** `CLAUDE.md` and
`Framework/OPERATOR-PROTOCOL.md` are loaded into every session and quote four ledger rows and the six-question
shape; the reader is a language model with prior knowledge of Buffett and Munger. Each unit's note records any
place the reader noticed either steering a reading. The calibration metric below is the measure of how much the
read is the reader's prior and how much it is the text.

### The extraction protocol (fixed; the cycle prompt restates it and may not change it)
A row is written for every passage in which Buffett or Munger (or, from 2025, Abel or Jain) states one of five
kinds of thing:
- **rule**: a stated way of acting ("we never", "we always", "the thing to do is").
- **test**: a question or check applied to a business, a manager or a price.
- **definition**: what a term means to the speaker (a franchise, owner earnings, a moat, risk).
- **mistake-and-lesson**: an error narrated by the speaker together with what it taught.
- **tension**: two statements, in this unit or against an earlier v5 row, that pull against each other.
Not a lesson: a fact about Berkshire's year, a joke, a forecast, a political view, a courtesy. A passage that
fits no kind is not rowed. **No vocabulary is forbidden**: the speakers use "franchise", "moat" and "owner
earnings" themselves, and a reader told to avoid their words would be reading something else.

### The row
`principle_ledger_v5.csv`, twelve columns: the eight of `principle_ledger.csv` in order, then `speaker`, `kind`,
`heading` (the `### N.` line the passage sits under), `unit` (the order-file key). `quote_verbatim` is the
passage exactly as printed, false starts and `(Laughter)` kept or elided with `[...]`, elisions in document order
and never across headings, and never longer than the sentences that carry the lesson. `era` and
`supports_gate_or_sheet` carry the literal `(blind read)` until synthesis. Ids are `M<year>-<nnn>` for meeting
rows, `L<year>-<nnn>` for letter rows and `R<year>-<nnn>` for signed-report-section rows, assigned by the helper
only. **Every row is matched against its source before it is appended**, by the same matcher the acceptance
test runs (`tools/ledger_verbatim.py`); a row that does not verify is not written.

### Who reads
A headless hourly cycle (`Screens/_daily/_v5_read.ps1`, task `BRK-v5-read`), one unit per cycle, under the
shared lock, committing after every heading that yields rows and writing a note per unit. Wave 7 stays paused.
The operator reads `Framework/v5/READING REGISTER.md` and `Screens/_daily/V5 READ LOG.md` between cycles and
re-queues any unit that produced no rows.

## Pre-registered standards

### Reported, not targeted: the calibration metric
78 rows of `principle_ledger.csv` cite a meeting. After the read, count how many of them the blind read
independently re-found: a v5 row from the same transcript whose quote overlaps the E-row's quote by at least
one full sentence. Report the count and the list of misses. It is not a pass mark. A low number says the two
readings disagree about what matters, which is a finding about both.

### The reconciliation table
After synthesis, every rule of v4.1 and of the holdings framework is placed in one of four classes:
- **REPRODUCED**: a v5 row states it (same substance, meeting or report source).
- **ABSENT**: no v5 row states it after the full 64-unit sweep, worded "no instance found" and naming the sweep.
- **CONTRADICTED**: a v5 row cuts against it, with no resolution inside the meetings.
- **NEW IN V5**: a v5 rule with no v4.1 counterpart.
The hypothesis **FAILS** on the first ABSENT or CONTRADICTED rule that is load-bearing by the definition above.
Every ABSENT load-bearing rule is then listed with what it cost, in the form of `Framework/INVENTIONS - deleted
and why.md`, so that if v5 is adopted the loss is written down rather than discovered later.

### The tests a candidate must pass before adoption is even proposed
1. `python tools/check_framework.py --also "<each v5 draft>"`: PASS. No phantom id, no unlabelled number.
2. **Test A' (reproducibility):** two independent sessions, no contact, run the same two names under the v5
   drafts. Pass: the same verdict at every question for both names. Quantities may differ; verdicts may not.
3. **Test B' (blind falsification):** the five sealed cases in `Framework/v4/testB/` (key in `_SEALED_KEY.json`,
   unopened by the reader) run under the v5 purchase draft. Pass: zero false passes, as v4 scored on 2026-08-28.
4. **Regression:** the six live names of `Framework/v4/REGRESSION - the six live names under v4.md` and the five
   Roth holdings, run under the v5 drafts. Every verdict that differs from the v4.1 verdict of record is explained
   from the rows. There is no pass mark; the explanations are the result.
5. The reconciliation table complete, and the calibration metric reported.
**Adoption is a separate decision** the operator takes on a ruling case carrying these five results. A candidate
that fails test 3 is not proposed. A candidate whose hypothesis FAILED may still be proposed if every ABSENT rule
is either carried as a confessed CONVENTION or dropped with its cost stated; the operator decides which.

## Known hazards, stated in advance
1. **Session and usage-limit kills mid-unit.** Mitigated by per-heading appends and a PROGRESS line in the note;
   the loss is at most one heading. The resume rule forbids re-rowing a heading already rowed; the helper's
   duplicate check is the backstop. The weekly cap that stopped every cycle on 2026-10-01 is the main schedule risk.
2. **The shared lock.** `BRK-overnight` is disabled; if it is re-enabled during the read the two hourly tasks
   contend and the loser of an hour skips it. The lock format must stay `PID date ...` or the other script's
   parser breaks.
3. **CSV damage.** Every row goes through the helper; the prompt forbids editing the file directly and forbids
   shell heredocs. Check 3's malformed-row test is the backstop.
4. **Thin or odd years.** 2025 is short (about 27,600 words) and Munger is absent; Abel and Jain answer. 1994 PM is
   short. 2015, 2020, 2021 and 2024 have never been cited and may be thin or rich; nothing is assumed.
5. **The source copies.** The transcripts are personal study copies from berkshire.memorex.ai whose notice
   prohibits reproduction and distribution. Rows stay to the sentences carrying the lesson, never whole answers;
   the v5 ledger is not published; this is the same footing the 78 existing meeting rows stand on.
6. **Contamination of the blind read** through the auto-loaded map and protocol and through the reader's
   training. Declared above; measured by the calibration metric; recorded per unit in the notes.
7. **Letter and report rows live in the AM unit only.** A letter passage the afternoon discussion illuminates
   goes into the M-row's `evolution_notes`, not a new L-row.
8. **A reader that finds too much.** A row for every sentence would drown the synthesis. The five kinds and the
   "not a lesson" list are the filter; the operator's between-cycle review of the register is the second filter.
9. **The 1994 and 1995 meetings have no report on disk**, only the FY1993 and FY1994 letters. Recorded; no fix.

---
# RESULTS — appended as the read and the comparison proceed. Nothing above this line is edited after 2026-10-03.

## INTERIM LOG 1, 2026-10-04 08:00 - thirteen units read (1994 AM to 2000 AM). No synthesis, no comparison.
Counted from the files: 1,159 rows (M 858, L 257, R 44; rule 555, test 401, definition 137,
mistake-and-lesson 51, tension 15), every row verifying, every cycle on the hour, six to nine minutes each.
R-rows exist from the 1996, 1997, 1998 and 1999 AM units, so PRIME RULE 4's ninth class was written into the
protocol this morning, the row before the rule. The 1998 AM and later AM units found the reprinted Owner's
Manual repeating earlier years word for word and wrote no R-rows, listing the spans as read and not rowed.

**Brief amendments made this morning, from the units' own error reports.** None changes the five kinds or the
row; each codifies what the units already did so later units do not drift: a new untracked note is staged by
path before the pathspec commit; cross-references cite only ids the helper has printed, and a new `erratum`
command appends a dated correction to a row's `evolution_notes` only; the `(lines N)` locator is normalised to
`(lines N-N)`; the helper recognises `===== Title =====` section marks and the Owner's Manual's
Purchase-Accounting Adjustments section; Acquisition Criteria counts as the chairman's text with or without a
signature; a reprint is read and not rowed, and a damaged span is recorded and never filled from another year;
the two-speaker, quoting-the-other, misprinted-label and interjection conventions; a letter with no title line
takes its first printed line as heading; a rule inside a political answer is rowed as the rule; a third party's
mistake may be a `mistake-and-lesson` when the speaker draws the lesson; a tension gets its own row only when
both statements are rowed and unreconciled in the same answer; the lock file is the wrapper's.

**Three facts about the sources, recorded for the comparison:** the FY1994 report is not on disk, so the 1995
AM unit could not read the acquisition criteria the FY1994 letter points to (L1994-038's notes say so); the
1997 report file's reprinted Owner's Manual (report lines 704-1038) is unreadable bytes from start to end, a
shelf-damage fact with no row citing it; the FY1998 and FY1999 letter files open with no title line.

**Errata recorded by the units in their notes, now correctable:** M1995-110 (meant M1995-109), M1997-085
(Munger's row is M1997-084), M1999-073 (meant M1999-064). Applied with the erratum command below the line.

**2026-10-04 08:07 - the headless cycle is stopped at the operator's instruction ("let's not do this headless").**
Task `BRK-v5-read` disabled after 13 of 64 units; 1,159 rows, all verifying; the three errata above applied.
The order file, the done file, the helper and the protocol are unchanged, so the read can continue in
interactive sessions, unit by unit, under the same pre-registered design, or stop here. The operator decides.

**2026-10-04 11:25 - interim at the halfway mark, and one declared breach.** Units 14 to 33 (2000 PM to 2010 AM)
were read interactively, one subagent per unit under the same prompt, the parent session verifying each close.
2,654 rows at 33 units, every row verifying. **Breach of the blind rule's whitelist, recorded by the 2010 AM
session itself:** it printed nine lines of `Annual Reports/2008 Annual Report.txt`, a file not on its unit's
order line, to tell whether a DRIFT in the Owner's Manual reprint was a rewording or a deletion. No framework
text, no existing-ledger text and no run file was opened, so the purpose of the blind rule (no v4.1 steering)
is intact; the breach is a source outside the unit, and nothing from it is quoted. The helper's DRIFT line now
says whether a drifted sentence's opening words are still in this year's file, and the prompt forbids settling a
DRIFT by reading outside the whitelist. Brief amendments since INTERIM LOG 1, all conventions the units set and
none touching the five kinds: same-batch links by line span; letter-heading fallbacks; letter restatement scope;
reworded reprints; signed text outside the four sections recorded for the operator; case slips and notes text;
the political test; meeting restatements rowed with ids; printed heading; personal conduct; tension duplicates;
administrative practice; third-party maxims; transcript gaps; tension partner must be a lesson; changed example;
listed-but-missing text; one row per speaker when each states a lesson; other speakers not rowed; jokes as
tests; implied principles; read an id before citing it; re-read for case before `add`; label-then-elision form;
new text in a reprint; a dropped principle is a change of lesson; the MATCH/DRIFT helper line.

**2026-10-04 13:30 - a ruling on the FY2014 letter file, and the memos left with the operator.** The 2015 AM session
found the fiftieth-anniversary pair (Buffett's "Berkshire - Past, Present and Future" and Munger's "Vice Chairman's
Thoughts - Past and Future") printed in `Shareholder Letters/2014 Letter.txt` after the signature and, following the
memo convention, read it without rowing it. The parent session ruled the pair in: it is already PRIME RULE 4's
eighth shelf class, it is addressed to shareholders, and the letter points to it. A supplementary pass rowed it
under the same unit (L2014-006 to L2014-046, 41 rows, 25 Buffett and 16 Munger). The signed memos to the managers
printed in the FY2001 and FY2010 files remain read and not rowed, their spans recorded, for the operator to decide.
The supplement session noted that it recognised Munger's four factors of success as the source of operator rule 7's
[E5-19] and did not row the passage, since it explains rather than instructs; that is recorded as a possible
steering, and the passage's span is in the note.

## THE READ IS COMPLETE, 2026-10-04 16:57. No synthesis, no comparison yet.
64 units plus the 2015 AM supplement; 4279 rows, all verifying (M 3480, L 750, R 49; rule 2033,
test 1625, definition 307, mistake-and-lesson 290, tension 24; Buffett 3551, Munger 718,
Abel 8, Jain 2). Units 1 to 13 headless, 14 to 64 interactive under the same prompt. Every unit's own
error report was folded into the prompt as a convention the same day; none changed the five kinds or the row. One
declared whitelist breach (2010 AM, recorded above). Rulings taken by the parent session during the read: the
2014 pair rowed as the eighth shelf class; the memos to the managers left with the operator; Abel and Jain rowed
in 2025 only, as pre-registered. The completion file is `Screens/_daily/V5 READ COMPLETE.md`. **Next, in order and
with the operator present:** synthesis of the two drafts from this ledger alone; the reconciliation table; the
calibration metric against the 78 meeting-sourced E-rows; Tests A' and B'; the regression on the live names and
the Roth holdings; the ruling case. v4.1 governs until the operator approves it.

## SYNTHESIS DONE, 2026-10-04 evening; THE CALIBRATION METRIC, reported as pre-registered
**Synthesis.** Four theme maps (one per era, every row placed once), one merged map (26 themes, 18 speaker
orderings, 290 mistakes in 13 lessons, 128 tensions), the operator's structure decision (`Framework/v5/synthesis/
STRUCTURE DECISION 2026-10-04.md`: a preamble, a standing rule, Q1 to Q11, Q12 optional, a closing note), thirteen
section drafts each script-checked against the ledger by its drafter, and the assembled
`Framework/v5/DRAFT - THE FRAMEWORK v5.md` (about 46,000 words, 1,379 distinct ids, 119 open questions, 17 recorded
absences, two confessed conventions). Every drafter worked under the blind rule and recorded where the auto-loaded
map pulled; the pulls are in each section file's "Steering noticed" and are summarised in the merged map's section 7.

**The calibration metric** (defined above under "Reported, not targeted"): of the 78 rows of `principle_ledger.csv`
that cite a meeting transcript, the blind read independently re-found **72 (92 percent)**, where re-found means a v5
row from the same transcript whose quote shares at least one full sentence with the E-row's quote. Computed by
script from both ledgers on 2026-10-04 (the pairing list is in the session record). **Not re-found, six:** E5-32
(2022), E3-56 (1995), E4-61 and E4-62 (2002), E4-74 (1999), E5-62 (2013). The number is reported, not judged; a
reader may take it either as evidence that the two readings agree about what matters in the meetings, or as a
limit on how blind a reader with the same training can be. Both readings are recorded.

**Unreconciled between the sections, for the reconciliation step:** the same "little or no debt" criterion read as
the one STOP in both Q3 and Q9; financial institutions that cannot be seen into placed in both Q1 and Q9; rapid
change ruled out in both Q1 and Q2; the bond's two roles (discount rate at Q7, filter at Q8) owned by neither;
serial issuance (L2014-015) as a possible second STOP at Q6 or an integrity sign at Q5; the own-stock alternative
at Q8 limited by its drafter to a company's own capital.
