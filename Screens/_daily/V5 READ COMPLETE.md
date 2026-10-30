# V5 READ COMPLETE - 2026-10-04 16:57

Every unit of `Screens/_daily/_v5_order.txt` is done: 64 units, 1994 AM to 2025 PM, plus the 2015 AM supplement
(the fiftieth-anniversary pair). Units 1 to 13 ran headless on the hourly task; units 14 to 64 ran interactively,
one subagent per unit under the same prompt, the parent session verifying every close.

`principle_ledger_v5.csv`: **4279 rows, every one verifying against its source** (`python tools/v5_ledger.py verify`;
`python tools/check_framework.py` PASS on both ledgers).
- By source: M 3480 (meetings), L 750 (letters), R 49 (signed report sections).
- By kind: rule 2033, test 1625, definition 307, mistake-and-lesson 290, tension 24.
- By speaker: Buffett 3551, Munger 718, Abel 8, Jain 2.
- Meeting rows by year run from 50 (2020) to 178 (1998).

**Synthesis is the operator's next step**, with the operator present, from this ledger only, as
`Framework/v5/PREREGISTRATION - v5 blind read and comparison.md` sets out: draft the two v5 documents from the rows,
then the reconciliation against v4.1, the calibration metric, Tests A' and B', the regression, then the ruling case.
v4.1 governs until the operator approves that case. Read first: `Framework/v5/READING REGISTER.md` (one entry per
unit, each with the passage the reader would show the operator first) and the notes in `Framework/v5/notes/`
(every unit's "Tensions seen" and "What in the brief was wrong or unclear").

**Left with the operator by the read:** whether the signed memos to the managers printed in the FY2001 and FY2010
files are admitted (read, not rowed, spans in the 2002 AM and 2011 AM notes); the `tension` kind is nearly empty
(24 rows) because the conventions sent conflicts to the notes' "Tensions seen" sections, which the synthesis
must harvest; the edges of the political test (general form versus remark about a political actor) were judged
unit by unit and are recorded in each note.
