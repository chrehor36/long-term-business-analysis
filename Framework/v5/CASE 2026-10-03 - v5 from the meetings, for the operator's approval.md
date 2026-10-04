# CASE — 2026-10-03 — v5, a framework built by a blind read of the annual meetings
## Presented under PRIME RULE 5 and PRIME RULE 4. The operator approved the build and the read on 2026-10-03 ("yes go and use auto mode"); adoption of v5 as a governing document is NOT approved by this case and returns to the operator as a ruling case at the end.

**Why this exists.** The operator's theory, stated 2026-10-03: *the meetings are a conglomeration of all his
lessons learned.* If that is so, a framework built from the meetings alone, with the report each meeting
answers, should carry every load-bearing rule the whole shelf carries, and may carry some the whole-shelf read
missed. v4.1 was built from the whole shelf and only part of it rests on a meeting. Whether the meetings alone
reproduce it, improve on it, or leave holes is an empirical question, and the way this project answers an
empirical question is to pre-register the test, run it, and record the result (operator rule 9).

**What this case asks.** Three things, each with the corpus behind it:
1. **PRIME RULE 5:** build a candidate replacement for `THE FRAMEWORK v4.md` and `THE HOLDINGS FRAMEWORK.md`
   whose question set is not fixed in advance. The meetings decide how many questions there are.
2. **PRIME RULE 4:** admit, as quotable, the parts of each Berkshire annual report that Buffett and Munger wrote
   and signed and that are not already on the shelf through the letters folder. Everything else in the report
   stays OFF-SHELF context.
3. **Operator rule 7 stays as written**, and the case says plainly where it would lose its source under a
   meetings-only shelf.

---
# CASE 1 — BUILD v5 BY A BLIND READ, WITH THE QUESTION COUNT OPEN

## What the framework says today
`THE FRAMEWORK v4.md` is v4.1: six questions in order, four verdicts, and the standard that every rule quotes
the corpus by ledger id or is labelled CONVENTION. Its own header says it is *"the whole framework. If a rule is
not here, it is not in force."* It was built on 2026-08-26 from the whole shelf and amended on 2026-08-28 from
Test D, a pre-registered read of the corpus against it.

## What this project's own record shows (counted from the files on 2026-10-03)
- The ledger holds 311 rows; 78 cite a meeting, 163 a letter, the rest the six smaller folders. *(this project's own record)*
- v4.1 cites 204 distinct ids; 65 are meeting-sourced and 139 rest only on another folder, 98 of them on the
  letters. By question: Q2 cites 20 meeting ids against 24 non-meeting; Q3, 21 against 56; Q4, 9 against 31;
  Q5, 13 against 13; Q6, 4 against 11. *(this project's own record)*
- The holdings framework cites 34 ids; 6 are meeting-sourced. Its H2 section and its "never a reason" section
  cite no meeting at all. *(this project's own record)*
- Four meeting years have never been cited by any row: 2015, 2020, 2021 and 2024. *(this project's own record)*
- The 32 transcripts run 1994 to 2025 with no gap, about 1.46 million words. *(this project's own record)*

So the theory is live, not idle: if the meetings carry the whole of Q3, nobody has yet shown it, because the
Q3 rules were sourced to the letters first.

## What the corpus says
1. **The authors describe the meeting as the place the owners get their answers, and the report as the
   document the meeting is about.** The 1996 answer on what he reads for: *"I like to know as much as I can about
   the person that's running it and how they think about the business and what's really going on in the
   business."* **[E3-28]**, 1996 meeting. And in 2003: *"you want to read lots of annual reports. You really want to
   have a database in your mind so that you can tell what kind of a business you're looking at, in general, by
   looking at the figures."* **[E4-14]**, 2003 meeting. The meeting is where the authors apply that reading aloud,
   for six hours a year, in answer to questions they did not choose.
2. **The authors frame their own method as lessons learned, not a system laid down.** *"what I've learned is I
   know enough not - to know that I don't know enough to make an investment decision."* **[E4-19]**, 2006 meeting.
   *"Typically, our most egregious mistakes fall in the omission, rather than the commission, category [...] their
   invisibility does not reduce their cost."* **[E3-47]**, 1991 letter. The operator's theory is that the meetings are
   where those lessons are stated most often and most plainly, because a questioner asks for them.
3. **The corpus's own instruction on how to test a favoured hypothesis applies to this one.** Darwin *"trained
   himself, early, to intensively consider any evidence tending to disconfirm any hypothesis of his, more so if he
   thought his hypothesis was a particularly good one"* **[E4-26]**. *"you must not fool yourself, and you're the
   easiest person to fool"* **[E3-41]**. The operator likes this theory; the builder of v4.1 has an incentive to
   defend v4.1 **[E4-27]**. Both incentives are declared here, and the design below is built to refute the theory,
   not confirm it.
4. **Yardsticks before the act.** *"I believe in establishing yardsticks prior to the act; retrospectively, almost
   anything can be made to look good in relation to something or other."* **[E1-02]**, 1961. The pass rules for the
   comparison are therefore fixed in the pre-registration before a transcript is read.
5. **On the width of the question set the corpus is permissive, not prescriptive.** *"We've got three boxes at the
   company: in, out, and too hard."* **[E4-19]**. *"we get paid, not for jumping over 7-foot bars, but for stepping
   over 1-foot bars"* **[E4-18]**, 2005 meeting. Nothing in the corpus fixes six questions; v4's six are the
   2026-08-26 audit's reading of the shelf. A blind read may find fewer or more, and the case does not prejudge it.

## The reading the text supports
**A blind read of the meetings is a legitimate test of v4.1 and a legitimate way to build a candidate.** Blind
means the reader does not open v4.1, the holdings framework, the existing ledger or any run file while reading;
rows are written as the lessons appear; the questions are drafted from the rows afterwards; only then is the
draft set beside v4.1 and every difference explained. The reader's prior knowledge of Buffett and the
auto-loaded protocol are contamination that cannot be removed in this harness, and the pre-registration names
them as hazards instead of pretending they are absent.

## The change, if approved
No governing document changes at this stage. A new folder `Framework/v5/` holds the case, the pre-registration,
the reading register and notes, and later the drafts. A separate ledger `principle_ledger_v5.csv` holds the
rows; its ids carry prefixes that cannot collide with the E1 to E5 series. `tools/check_framework.py` learns the
new id class and verifies the second ledger with the same two checks it runs on the first. `THE FRAMEWORK
v4.md` stays GOVERNING, every run and review proceeds under it, and nothing in `principle_ledger.csv` is touched.

## What this would touch
- **Verdicts of record: none.** No run file, register entry, alert band or PORTFOLIO row changes.
- **The queue:** wave 7 stays paused (operator decision 2026-10-03) because the read uses the same hourly slot,
  the same lock and the same usage budget.
- **Adoption** (v5 becoming GOVERNING) is a separate decision, taken on a written comparison and the
  pre-registered tests, in a ruling case the operator approves, amends or refuses. Until then v5 is a test record.

---
# CASE 2 — ADMIT THE SIGNED REPORT SECTIONS TO THE SHELF (PRIME RULE 4)

## What the shelf says today
PRIME RULE 4 names eight classes. `CLAUDE.md` marks `Annual Reports/` and `Quarterly Reports/` OFF-SHELF:
*"Berkshire's own annual reports and 10-Qs, context only; the letter portion is cited through the letters folder."*
The reports on disk run FY1995 to FY2025. Each printed report carries, besides the chairman's letter, sections
written in the chairman's own voice and signed by him: **Owner-Related Business Principles** (the Owner's Manual
as printed that year, which is on the shelf in one edition through `Owners Manual/`), **Acquisition Criteria**,
**Intrinsic Value**, and **The Managing of Berkshire**. The financial statements, the notes and Management's
Discussion are management's filing, not the authors' articulation of a principle.

## What the corpus says
1. The Owner's Manual is already a shelf class, and the ledger cites it (**[E2-32]**, **[E3-52]**, **[E3-54]**, from
   `Owners Manual/An Owners Manual.txt`). The printed-in-report edition is the same text as published each year,
   with its year-by-year revisions; admitting it by year admits nothing new in kind.
2. The acquisition criteria are already cited through the letters where they were printed inside a letter
   (**[E2-75]**, 1987). The same criteria stand as a separate signed section of every report from FY1995; the shelf
   today admits the sentence when it appears in the letter and refuses it when it appears on the next page.
3. The reading rule the authors give for a report is **[E3-28]** and **[E4-14]** above: the report is for learning
   what is really going on in the business and how the person running it thinks. The sections named here are
   exactly the places where the person running Berkshire says how he thinks.

## The reading the text supports
**The authors' own signed words are on the shelf wherever they are printed; the filing around them is not.**
That is the line PRIME RULE 4 already draws when it names the 2014 fiftieth-anniversary pair *"published inside
that year's Berkshire annual report"* as a shelf class while leaving the report OFF-SHELF.

## The change, if approved
PRIME RULE 4 gains a ninth class: *"the signed chairman's sections of each Berkshire annual report (Owner-Related
Business Principles as printed that year, Acquisition Criteria, Intrinsic Value, The Managing of Berkshire),
cited to `Annual Reports/<FY> Annual Report.txt` with a line span; the financial statements, notes and
Management's Discussion in the same file stay OFF-SHELF context."* `CLAUDE.md`'s row for `Annual Reports/` is
corrected the same day with a dated note saying what it said before. **The change to the protocol is made only
when the first R-row is written**, so that PRIME RULE 6 holds: the row exists, then the rule that admits its class.

## What this would touch
- **Verdicts of record: none.** No existing row cites a report file.
- **The verbatim check** applies to the new class unchanged: a row's words must be found in the cited file in
  document order. The 1996 report file carries a few non-UTF-8 bytes; the matcher already replaces undecodable
  bytes and normalises to letters and digits, so it is unaffected.
- **Which years carry the sections.** A heading sweep of the report files on 2026-10-03 found the signed
  sections printed in FY1995 through FY2017 and none by those headings from FY2018 onward, when the printed
  report carries the letter alone and the Owner's Manual moved to the website. So R-rows can arise only from
  the 1996 to 2018 meetings' AM units; later AM units read the letter only. *(this project's own record)*

---
# CASE 3 — THE HONESTY RULE UNDER A MEETINGS-ONLY SHELF

Operator rule 7 rests on **[E5-19]**: *"Why did Berkshire under Buffett do so well? Only four large factors occur to
me: (1) The constructive peculiarities of Buffett, (2) The constructive peculiarities of the Berkshire system,
(3) Good luck, and (4) The weirdly intense, contagious devotion of some shareholders and other admirers"*. That is a
Special Letters row, not a meeting. If v5 is adopted, rule 7 keeps citing [E5-19] from the full shelf, because the
protocol is not a meetings-only document and the shelf is not narrowed by v5. The pre-registration asks the blind
read to look for the meeting equivalent, and records "no instance found" with the sweep named if there is none.
**The market-beating claim stays UNPROVEN under v5 exactly as under v4.1**, and no result of the read can change
that sentence.

---
# WHAT THE OPERATOR DECIDED, AND WHAT REMAINS WITH THE OPERATOR
1. **Case 1, the build and the read: approved 2026-10-03** by the operator's instruction to proceed in auto mode,
   after the four design choices were put to the operator and answered: meetings plus the signed report
   sections; intended replacement; blind fresh read; headless hourly cycle; both frameworks in scope; wave 7
   paused; adoption by the operator on the written comparison.
2. **Case 2, the shelf class: approved in principle** by the operator's choice of "Buffett and Munger's own text" on
   2026-10-03. The protocol edit is made when the first R-row exists (PRIME RULE 6).
3. **Case 3 adds no convention and changes nothing.**
4. **Adoption of v5 as GOVERNING: not decided.** It returns as `Framework/v5/RULING CASE <date> - adopt v5, for the
   operator's approval.md` after the pre-registered comparison and tests, and the operator approves, amends or
   refuses it. Every clause above cites a ledger row that verifies against its source
   (`tools/check_framework.py`, check 4).
