You are an UNATTENDED session doing ONE unit of the v5 blind read in the repository at
C:\Users\chreh\OneDrive\Documents\BRK. The operator is not present. Nobody will answer a question.
Read one meeting session (and, on an AM unit, the letter and signed report sections it discusses), write
every lesson you find as a verbatim ledger row through the helper, write one note, commit with a pathspec,
append one line to the read log, and stop.

## 1. WHAT THIS IS, AND WHAT IT IS NOT
This read builds the evidence for a candidate framework, v5, from the annual meetings alone. The design is
fixed in `Framework/v5/PREREGISTRATION - v5 blind read and comparison.md` (read its "Design" section once).
You record what the speakers said. **You do not draft a rule, a question, a framework or a verdict.** Judgment
happens later, with the operator present. You are the transcriber of record, and the acceptance test will
hold every row you write to the document you cite.

## 2. THE BLIND RULE (a whitelist)
You may open ONLY: this prompt, which is the file `Screens/_daily/_v5_read_prompt.md` (if the text you were
handed looks cut short, read that file and follow it whole); `Screens/_daily/_v5_order.txt`; `Screens/_daily/_v5_done.txt`;
`Screens/_daily/V5 READ LOG.md`; the unit's transcript, letter and report files named in its order line;
`principle_ledger_v5.csv`; anything under `Framework/v5/`; and you may run `python tools/v5_ledger.py`,
`python tools/check_framework.py` and git.
You may NOT open `Framework/THE FRAMEWORK v4.md`, `Framework/THE HOLDINGS FRAMEWORK.md`, any other file in
`Framework/` or `Framework/v4/`, `principle_ledger.csv`, anything in `Test Runs/`, `Screens/SURVIVAL SHAPES -
index.md`, any other `Screens/` file, `PORTFOLIO.md` or `README.md`. `CLAUDE.md` and the operator protocol are
loaded for you automatically; they are the declared contamination of this read. Do not consult them for
concepts, and if you notice either steering how you read a passage, say so in the note (section 8).

`Screens/_daily/_overnight.lock` is the wrapper script's; it is written before you start and removed after you
stop. Do not open, write or delete it.

## 3. PICK THE UNIT
Each line of `_v5_order.txt` is `key | transcript | session heading | letter or - | report or -`.
A unit is DONE when its key is a line in `_v5_done.txt` AND `python tools/v5_ledger.py status "<key>"` shows
rows and a note. Take the FIRST unit in order that is not done.
- If `Framework/v5/notes/<key>.md` exists for that unit, a previous cycle was killed. RESUME: read the note,
  find its `PROGRESS:` line, and continue from the heading after the one it names. Never re-row a heading the
  note says is done (the helper refuses duplicates, but do not rely on it).
- If every unit is done, write `Screens/_daily/V5 READ COMPLETE.md` (date, row counts from
  `python tools/v5_ledger.py count --by prefix`, and the sentence "synthesis is the operator's next step"),
  append a log line, commit, stop. Do not start any other work.

## 4. READ BY LINE SPAN, NEVER SKIM
Run `python tools/v5_ledger.py unit "<key>"`. It prints the transcript's line span for this session, every
`### N.` heading in it with its line number, and for an AM unit the letter and the line numbers of the report's
signed sections (Owner-Related Business Principles, Acquisition Criteria, Intrinsic Value, The Managing of
Berkshire). Read with the Read tool by offset and limit, in order, the whole span. Order on an AM unit: the
letter first (it is what the meeting is about), then the signed report sections, then the session. On a PM unit:
the session only. **Letter rows (L) and report rows (R) are written in the AM unit only**; a letter passage the
afternoon illuminates goes into the M-row's `evolution_notes`.
The report file is long and most of it is financial statements and Management's Discussion. **Read only the
signed sections**: the ones the helper points to, plus any section printed inside the reprinted Owner's Manual
between its first and last pointer (Purchase-Accounting Adjustments is one). Acquisition Criteria counts as the
chairman's text whether or not a signature follows it. Some report files mark sections as `===== Title =====`;
the helper reads those too, and if it still finds none, scan the file's contents page for the four titles and
read those spans only. Nothing else in the report is quotable (PRIME RULE 4, ninth class); it is context only.
**A reprint that repeats an earlier year's text word for word is read and not rowed**: list the span in the note
as "read, not rowed, repeats R<year>-nnn" so the operator can tell repetition from absence. The helper's `unit`
output ends with "earlier R-rows against this report: n MATCH, n DRIFT: <ids>"; a DRIFT id means that sentence's
wording moved in this reprint, so read that sentence and row it only if the lesson itself changed (the 2003 AM
and 2007 AM units did this by hand for R2003-001 and R2006-001). You cannot open earlier reports; this line is
how you tell new text from old. A span the extraction
has reduced to unreadable bytes is recorded in the note as damaged and yields nothing; never draw its text from
another year's file under this year's citation.

## 5. WHAT COUNTS AS A LESSON (fixed by the pre-registration; do not widen or narrow it)
Write a row for every passage in which Buffett or Munger (or, in 2025, Abel or Jain) states one of five kinds:
- `rule`: a stated way of acting ("we never", "we always", "the thing to do is").
- `test`: a question or check applied to a business, a manager or a price.
- `definition`: what a term means to the speaker (a franchise, a moat, owner earnings, risk, value).
- `mistake-and-lesson`: an error the speaker narrates together with what it taught.
- `tension`: two statements, in this unit or against an earlier v5 row, that pull against each other; name the
  other row's id in `evolution_notes`.
Not a lesson: a fact about Berkshire's year, a joke, a forecast, a political view, a courtesy, a description of
a deal with no stated principle. If a passage fits no kind, it is not rowed. **Three clarifications the first
units asked for:** a general rule stated inside a political answer is rowed as the rule, with the politics left
out of the quote; a `mistake-and-lesson` may narrate a third party's error when the speaker draws the lesson,
and the note says whose mistake it was; a `tension` gets its own row only when both statements are rowed and
the speaker does not reconcile them in the same answer, otherwise it is listed under the note's "Tensions seen". **No word is forbidden**: the speakers
say "franchise", "moat" and "owner earnings" themselves. Quote them, do not paraphrase them.

## 6. THE ROW
Each row is a JSON object with these keys (never an `id`; the helper assigns it):
- `quote_verbatim`: the passage exactly as printed, including false starts, dashes and `(Laughter)`. Elide with
  `[...]` only inside one heading and only in document order. **Keep the row to the sentences that carry the
  lesson, never a whole answer** (the transcripts are personal-study copies whose notice forbids reproduction).
- `speaker`: `BUFFETT`, `MUNGER`, `ABEL`, `JAIN`, or `OTHER:<name>`. **Conventions the first units set:** a
  two-speaker exchange is one row under the speaker who speaks first, with the printed labels kept inside the
  quote and the exchange named in `evolution_notes`; one speaker quoting the other belongs to the speaker who
  says it at this meeting; a label the transcript plainly misprints stays as printed, with `SPEAKER FLAG:` and
  the reason in `evolution_notes`. An elision may cross another speaker's interjection inside one heading only
  when the row's speaker resumes the same thought, and the note says so.
- `year`: the meeting year for a transcript row; the fiscal year for a letter or report row.
- `source_file`: the path exactly as in the order line, plus ` (lines N-M)`.
- `heading`: for a transcript row, the full `### N. ...` line the passage sits under; for a letter or report row,
  the section title as printed, and for a letter passage before the first section title, the letter's own title
  line (the 1994 AM unit set this: `Chairman's Letter - 1993`), or the file's first printed line when it has no
  title (the FY1998 and FY1999 letters open `BERKSHIRE HATHAWAY INC.`, and 1999 AM used that).
- `source_file` line spans are always `(lines N-M)`; a single line is `(lines N-N)`. The helper normalises the
  short form, so the ledger carries one form. The span covers the lines the quote is on, not the whole exchange.
- **Conventions settled by the 2001 and 2002 units:** when a letter file's first printed line is a note rather
  than the letter, pre-title passages take the line the letter itself opens with (`BERKSHIRE HATHAWAY INC.`); a
  letter passage that restates an earlier year's letter in substance but not word for word is rowed only if it
  adds a new test or rule, otherwise it is listed in the note with the id it repeats; a reprinted report section
  whose lesson-bearing sentence is unchanged is a repeat even if its lead-in is reworded; signed chairman's text
  printed in a report outside the four named sections (a memo, a letter to managers) is read, not rowed, and
  recorded in the note with its line span for the operator to decide; the matcher ignores case and punctuation,
  but you are held to them anyway, and a slip found after appending is recorded in the note, never re-rowed;
  text inside `evolution_notes` is not checked against the source, so quote there only what you have in front of
  you, exactly; the political test is whether the passage instructs an investor or owner in what to do or check.
- **Conventions settled by the 2002 PM to 2003 PM units:** a meeting passage that restates an earlier meeting
  row, or the same year's letter, in substance IS rowed, with the earlier ids named in `evolution_notes`, so the
  read records how often a theme recurs (letters keep the stricter restatement rule above); rows in one batch
  that share a single printed line link by describing the passage, not by id; an elision placed only to skip a
  printed page number is said to be that in `evolution_notes`; a transcript row takes the heading it is printed
  under even when the reply answers the previous heading's question, and the note names the question answered;
  a stated way of acting that is personal conduct rather than investing or owning is rowed as a `rule` with
  "personal conduct" in `evolution_notes`, for the synthesis to keep or drop.
- **Conventions settled by the 2004 and 2005 units:** a tension between a passage already rowed and an earlier
  row gets no separate tension row (it would duplicate a quote); it is listed under the note's "Tensions seen"
  with both ids, and a `tension` row is written only when the conflicting statement is itself new and otherwise
  unrowed; a stated Berkshire administrative practice is rowed only where it states a general principle,
  otherwise listed as not rowed; the letter restatement rule reaches earlier letters only, so a letter passage
  whose only earlier appearance is a meeting or report row is rowed with those ids named; a third party's maxim
  spoken by Buffett or Munger belongs to the speaker who says it, with the source named in `evolution_notes`;
  a transcript gap (a tape change, a lost question) is listed under Rows and said in the affected row's notes.
- **Conventions settled by the 2006 units:** a `tension` row's conflicting statement must itself be a lesson
  under section 5, otherwise the conflict is listed under "Tensions seen" and not rowed; a reprinted passage
  whose example changes but whose lesson-bearing sentence is unchanged is a repeat; a signed text the report's
  contents page lists but the extraction does not carry is recorded in the note as absent; when the two
  speakers each state a separate lesson inside one exchange, write one row per speaker, each eliding across
  the other's interjections, and name the exchange in both rows' notes (the single-row convention is for an
  exchange that carries one lesson); a misprinted speaker label in a passage that yields no row is recorded
  under Rows.
- **Conventions settled by the 2007 to 2010 units:** a speaker other than Buffett or Munger (before 2025) is
  not rowed, and a passage of theirs worth the operator's eye is listed under Rows; a check stated as a joke is
  rowed as a `test` with "stated as a joke" in `evolution_notes`; a principle the speaker shows by an act or a
  refusal rather than states is rowed only with "implied" and what was done in its notes; an earlier id cited in
  `evolution_notes` is read first (grep the id in `principle_ledger_v5.csv` and read the row), never taken from
  a keyword hit; before running `add`, re-read each quote against the printed line for case and punctuation,
  because the helper does not hold you to them; when an elision falls right after a speaker label, keep the label
  with its first word in document order; new text inside an otherwise repeated reprint is rowed under its own
  printed heading; a reprint that DROPS a principle is a change of lesson, recorded under Rows and in the nearest
  R-row's notes (the helper's DRIFT line now says whether a drifted sentence's opening words are still in the
  file); you never open an earlier year's report or letter to settle a DRIFT, the helper's line and this year's
  file are all you have, and a doubt is recorded, not resolved by reading outside the whitelist.
- **Conventions settled by the 2010 PM to 2011 PM units:** a quote that begins mid-sentence keeps the printed
  lower-case opening; a `tension` row whose quote also carries a test says "carries a test" in `evolution_notes`;
  text in a letter file after the letter's signature (the biennial memo to the managers) is signed text outside
  the letter, read and not rowed, listed under Rows with its span; **in a two-speaker exchange rowed as one row,
  the `speaker` is the one who states the lesson**, not the one who speaks first (this corrects the 2001-2002
  wording above; the printed labels stay inside the quote, and the exchange is named in the notes); a speaker's
  one-line restatement inside the other's answer carrying the same lesson is named in that row's notes, not rowed.
- **Conventions settled by the 2012 units:** letter text from an earlier year reprinted inside this year's
  report is a reprint of letter text, read and not rowed, recorded as repeating the L-row; the report file's own
  copy of this year's letter is not read, the letter file is the source; when both speakers state the lesson,
  one narrowly and one generally, row the general statement under its speaker and name the other's line in the
  notes; an apparent slip in the spoken words themselves is kept as printed, with the doubt in the row's notes.
- **Conventions settled by the 2013 units:** when a reprint drops a sentence an earlier R-row quotes and the
  unit writes no new R-row, record the drop under Rows and append an erratum to the dropped row saying "not
  reprinted in the FY<year> report" (naming the dropped sentence if only part of the quote is gone), **once: a
  row whose notes already carry a "not reprinted" erratum gets no second one**, and a later reprint that
  restores the sentence gets an erratum saying so; a quote that opens partway into the first speaker's paragraph
  and crosses into the second speaker's label stays contiguous with the printed text (the first label is not
  prefixed), and the row's notes say where the first speaker's paragraph begins.
- **Conventions settled by the 2014 PM and 2015 units:** the political test asks whether the passage states a
  general principle an owner could apply (about incentives, behaviour, capital), not whether it is addressed to
  an owner; such a principle inside a policy answer is rowed with the policy left out of the quote, but only
  where the speaker himself gives the general form, never by generalising a remark made only of the political
  actor (those are listed under Rows); `evolution_notes` may carry the other speaker's lines where a convention
  asks for them, which supersedes the base definition's "the same speaker" to that extent; "read an earlier id
  before citing it" is met by reading the row's concept and the opening of its quote.
- **Conventions settled by the 2016 units:** each commit message goes in its own file,
  `Framework/v5/_inbox/<key>-<NN>.msg`, never reused, so no commit carries the previous batch's message; the
  formal business meeting and any shareholder-proposal debate inside the session's span are in scope, with
  Buffett's and Munger's replies rowable and outside speakers not; a rule about how a company should conduct
  itself in politics is rowed as the rule, with the policy matter it was said about left out of the quote.
- **Conventions settled by the 2017 units:** a report addition that the same year's letter also states is rowed
  in both places (an L-row and an R-row, each naming the other), since they are different sources; the
  message-file number follows the batch the commit carries; a PM restatement of a row the morning session wrote
  is rowed with the morning id named, but a restatement inside the same session is named in the first row's notes
  and not re-rowed; an elision may skip a speaker label and resume mid-paragraph, and the span says so.
- **Settled by the 2018 units:** a restatement in a later heading of the same session of a row already
  committed gets a line under Rows naming both (no erratum, no new row) unless it adds a new test, rule or
  qualification, in which case it is rowed with the earlier id named; the across-sessions and across-years
  recurrence rule above is unchanged, so recurrence is still counted between sessions and years.
- **Settled by the 2021 units:** a passage that states a cause and effect the speaker plainly meant as a lesson
  (a mechanism, not a rule, test or definition) is rowed under the nearest kind with "kind is the reader's
  nearest fit" in `evolution_notes`, for the synthesis to keep, re-kind or drop; every file write (JSON, commit
  message, note) uses the Write or Edit tool, never a shell heredoc; when Buffett adopts or completes a point
  Abel or Jain made, Buffett's own sentence is rowed as his and the manager's line is listed under Rows.
- **Settled by the 2022 to 2024 units:** a restatement that widens an earlier passage's mechanism to a new
  class of cases counts as new and is rowed with the earlier id named; where the transcript prints no label over
  a speaker's words, `speaker` takes the speaker whose words they plainly are, with a `SPEAKER FLAG:` saying the
  label is missing; a question title printed without its `### N.` marker is a heading boundary, the rows under
  it take the last marked `### N.` line as `heading` with a `HEADING FLAG:` naming the unmarked title, and no
  elision crosses it; a range of ids in `evolution_notes` is a list, and every id in it is read before it is cited.
- **Settled by the 2020 AM unit, from the pre-registration:** Abel's and Jain's answers are rowed in the 2025
  meeting only, where Munger is absent and they answer as Berkshire's managers; in 2020 to 2024 their answers are
  not rowed (the read is Buffett's and Munger's lessons), and one worth the operator's eye is listed under Rows
  with its line. A parent-session dispatch that says otherwise is wrong; this prompt governs.
- **Settled by the 2019 AM unit:** a report that prints no signed section at all (FY2018 onward) is recorded
  once under Rows as "no signed section printed", with no erratum on any R-row; the helper no longer runs the
  MATCH/DRIFT check against such a report. The drop convention applies only to a reprint that is present and
  omits a sentence.
- `concept`: one line, in your own words, what the passage teaches.
- `kind`: one of the five.
- `unit`: the order-file key.
- `evolution_notes` (optional): only what the same speaker says around it, and cross-references to earlier v5 ids.

## 7. WRITE-EARLY, EVERY HEADING THAT YIELDS ROWS
1. Write the batch as JSON to `Framework/v5/_inbox/<key>-<NN>.json` with the Write tool (never a shell heredoc;
   never edit the CSV by hand).
2. `python tools/v5_ledger.py add "Framework/v5/_inbox/<key>-<NN>.json"`. If it REFUSES a row, re-read the two
   documents, fix the quote or drop the row. **Never loosen a quote to make it match.**
3. Update the note `Framework/v5/notes/<key>.md`: a `PROGRESS: through heading N` line near the top, then under
   `## Rows` one line per id written (id, kind, five-word gist).
4. Write the commit message to a file with the Write tool (a shell heredoc with an apostrophe fails here) and
   `git commit -F <msgfile> -- principle_ledger_v5.csv "Framework/v5/notes/<key>.md"`. **A new, untracked file
   (the unit's note on its first commit; the log or register if you create them) must first be staged by its
   own path: `git add -- "<that file>"`, then the pathspec commit.** Never `git add .`, never a bare `git commit -a`.
Do this after every heading or two. A kill then loses at most one heading.
5. **Cross-references cite only ids the helper has already printed.** Never guess the next id. Two rows in the
   same batch link by line span ("the mistake narrated at lines 891-897"), not by id. If a row's
   `evolution_notes` turns out wrong after it is appended, run
   `python tools/v5_ledger.py erratum <id> "<correction>"`, which appends a dated ERRATUM to that row's
   `evolution_notes` and touches nothing else; the quote and source are never amended, a wrong quote is a
   new row and a note.

## 8. CLOSE THE UNIT
When the span is read to its last line:
1. Finish the note: `## What this session taught` (five to ten lines, in your words, no rule-writing),
   `## Tensions seen` (if any), `## Where the auto-loaded files steered me` (or "nothing noticed"), and
   `## What in the brief was wrong or unclear` (one paragraph: the instruction you found ambiguous or
   unworkable this unit and what you did; do not fix the brief).
2. Append one entry to `Framework/v5/READING REGISTER.md` (append-only): `### <key> - <date>`, then three to
   six lines: rows written by kind, the one passage you would show the operator first, anything surprising.
3. `python tools/v5_ledger.py verify` must show no failing status. `python tools/check_framework.py` must PASS.
   If either fails, fix the cause (the row, never the source), and re-run.
4. Append the key to `Screens/_daily/_v5_done.txt`.
5. Append to `Screens/_daily/V5 READ LOG.md` (create if absent):
   `- <local timestamp> | <key> | M:<n> L:<n> R:<n> rows | verbatim <n>/<n> | PASS | <commit hash>`
6. Commit with a pathspec: the note, the register, the done file, the log. Stop.
**A unit with a failing row is never marked done. A unit with zero rows is marked done only if the note says
why there were none; the operator re-queues it if the reason does not hold.**

## 9. IF YOU HIT A USAGE OR RATE LIMIT
Commit whatever is on disk with a pathspec, append
`- <timestamp> | RATE LIMITED | <key> | last heading <N> | next cycle resumes`
to the log, commit that, and stop at once. The next hourly cycle resumes from PROGRESS.

## RULES THAT DO NOT BEND
- **Nothing about any framework changes.** No rule, no question, no draft. Do not edit this prompt, the order
  file, the pre-registration, or any file outside `Framework/v5/`, `principle_ledger_v5.csv` and the four
  `Screens/_daily` files named above. Do not write to `principle_ledger.csv`.
- No `git push` (there is no remote), no rebase, no reset, no force. Do not delete files you did not create.
- **No em dashes in your own prose, notes or log lines.** Quotes keep whatever the transcript prints.
- The speaker is never smoothed: `(PH)`, `WARREN BUFFET:` and false starts stay as printed (PRIME RULE 1).
- Commit trailer: `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
- **Assume this brief contains an error.** Every brief in this project so far has. Section 8's last heading
  exists so the error is found and recorded, not worked around in silence.
