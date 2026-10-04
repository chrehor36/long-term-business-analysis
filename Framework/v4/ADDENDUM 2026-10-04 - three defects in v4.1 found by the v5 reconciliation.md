# ADDENDUM 2026-10-04 — three defects in v4.1 found by the v5 reconciliation, and how each was corrected
**Operator rule 6: a defect found later is corrected by addendum.** The reconciliation of the v5 drafts against v4.1
(`Framework/v5/RECONCILIATION - v5 against v4.1.md`, section 3) read every rule of `THE FRAMEWORK v4.md` beside the
meetings and found four things wrong with v4.1 itself. Three are citation and label defects and are corrected here
by dated in-place notes, at the operator's decision of 2026-10-04. The fourth, the PERMANENT designation for marketable
securities (which its authors withdrew in 2016, L2016-010 and R2016-001 in the v5 ledger), changes a rule and goes to
the operator as a PRIME RULE 5 case; it is not touched here.

## 1. Bar 1 quoted words that are not on the shelf
**What stood.** Under Bar 1 (Part IV, the normal method), the line *"it's hard to go wrong when you're buying dollar
bills for 80 cents or less"*, cited to **[E5-09]**. E5-09's text, from the 2012 letter, is *"But never forget: In
repurchase decisions, price is all-important. Value is destroyed when purchases are made above intrinsic value."* The
quoted words appear nowhere on the shelf. They were a paraphrase wearing a citation, the defect class PRIME RULE 1 and
PRIME RULE 3 exist to catch, and checks 1 to 4 of the acceptance test cannot see it because they test the ledger row
against its source, not the document's inline quotation against the row.

**What the shelf has.** The 2013 meeting, heading 8, on Berkshire's own buybacks: *"If you can repurchase your shares at
a significant discount from intrinsic value, it like buying dollar bills at 90 cents or 80 cents or whatever it may be,
and it's a very sure way of improving per-share value."* (transcript artifact "it like" kept). The 1996 meeting has the
figure the other way round, on issuing stock below value.

**The correction.** Ledger row **E5-63** added first (the row before the rule, PRIME RULE 6), then the Bar 1 line replaced
by the verbatim 2013 sentence cited to it, with a dated note saying what stood before. `python tools/check_framework.py`
PASS, 312 rows.

## 2. "Name the scarce input the business controls" at Q2, no id and no label
An analyst's instruction with no ledger row behind it and no CONVENTION label, inside the Q1 and Q2 opening text. It is
useful and it is ours. Labelled **CONVENTION** in place with a one-line rationale naming the nearest corpus ([E3-31] and
the Q2 tests). Found by part 1 of the reconciliation.

## 3. The three-figure report at Q5, no id and no label
"Report three things: the yield; what the price already assumes; what you are paid, as points over the sovereign."
The corpus compares the return with the bond ([E4-21], [E5-43]) and prescribes no report form; the three figures are
this project's format. Labelled **CONVENTION** in place. Found by part 3 of the reconciliation, row 12, which also
notes that the 2026-09-20 sweep recorded in Part VI did not list it.

## What this says about the acceptance test
All three defects sat in a governing document that passed six checks on every run for weeks. The checks resolve an id to
a row and the row to its source; none asks whether an inline quotation in a document matches the row it cites. That is
a seventh check, and whether to add it is a tooling decision for the operator: it would get the same answer sooner and
add no number. Recorded here, not implemented.
