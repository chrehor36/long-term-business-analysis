# -*- coding: utf-8 -*-
"""Fixes found by quotecheck.py: spans I had inside quote marks that are not verbatim
from the source I attributed them to. PRIME RULE 1."""
import io, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(BASE, "Test Runs", "2026-09-21 Run - MGM MGM Resorts International.md")
t = io.open(P, encoding="utf-8").read()
n0 = len(t)

FIX = [
    # A. [E4-55]: the sentence I quoted is THE FRAMEWORK'S commentary, not the corpus row.
    (u'''This is precisely the shape **[E4-55]**
names: *"Dollar revenue flattered by pricing is how a shrinking franchise hides; the physical
series is the honest one."* Here it is dollar revenue flattered by hold, which is the same
disease with a different flatterer.''',
     u'''This is the shape **[E4-55]** names.
Its corpus row is Precision Steel, whose volume fell from 69 million pounds to 46 million while
price rises held dollar revenue level: *"This decline in physical volume is a serious reverse,
not likely to disappear in some 'bounce back' effect."* At MGM the dollar revenue is flattered by
hold rather than by price, which is the same disease with a different flatterer. *(The sentence
"Dollar revenue flattered by pricing is how a shrinking franchise hides; the physical series is
the honest one" is `THE FRAMEWORK v4.md`'s own commentary on [E4-55], not a corpus quotation, and
is not quoted here as one.)*'''),

    # B. [E2-59]: "the moat belongs to the regime" is framework prose; "That day is gone" is in
    # the ledger row's evolution_notes as a verified source line, not in quote_verbatim.
    (u'''The licence scarcity is a **regime’s** property, not the company’s, which is
exactly what **[E2-59]** distinguishes - administered arrangements can floor a commodity
business’s profits, but *"the moat belongs to the regime"*, and *"That day is gone"* is how it
ends; Macau’s own regime carries a stated end date of December 2032.''',
     u'''The licence scarcity is a **regime’s** property, not the company’s, which is
exactly what **[E2-59]** distinguishes: profit troubles in an over-supplied commodity business
*"may be escaped, true, if prices or costs are administered in some manner and thereby insulated
at least partially from normal market forces"* - and the row’s own example of that escape is
pricing *"until recently"* administered for truckers and for financial institutions’ deposit
costs, which is to say an escape the state can withdraw. Macau’s regime carries a stated end date
of December 2032. *(The phrases "the moat belongs to the regime" and "That day is gone" are,
respectively, `THE FRAMEWORK v4.md`’s own wording and a source line recorded in the [E2-59]
ledger row’s evolution notes rather than in its quote_verbatim; neither is quoted here as the
row.)*'''),

    # C. [E2-60]: second clause is the framework's rule, not the corpus row.
    (u'''Restricted earnings are
  those whose payout costs the business *"its ability to maintain … its financial strength"*, and
  *"where leverage rises to fund the payout, (c) was understated."*''',
     u'''Restricted earnings are
  those whose payout costs the business *"its ability to maintain … its financial strength"*; the
  rule that a payout funded by rising leverage means (c) was understated is `THE FRAMEWORK
  v4.md`’s reading of that row, and is applied here as such rather than quoted as corpus.'''),

    # D. [E5-11]: "the killer and is the one most often skipped" is framework prose.
    (u'''This is the one [E5-11] says is "the killer and is the one most often skipped."**''',
     u'''[E5-11] says of it: *"Ignoring that last necessity is what usually leads companies to
  experience unexpected problems."***'''),

    # E. [E5-39]: "cash is a lot like oxygen" is NOT in the [E5-39] row's quote_verbatim.
    (u'''but **[E5-39]** is explicit that
  bank lines are not counted: *"We will never be dependent on the kindness of strangers … cash is
  a lot like oxygen."*''',
     u'''but **[E5-39]** is explicit that bank lines are
  not counted: *"We will never be dependent on the kindness of strangers … we don’t count on bank
  lines. You know, we don’t count on … we don’t count on anything."* *(The often-repeated "cash is
  a lot like oxygen" is in the [E5-39] ledger row’s concept and evolution-notes fields, not in its
  quote_verbatim, and the source line it records reads "available cash **or credit** is a lot like
  oxygen"; it is therefore not quoted here.)*'''),

    # F. [E2-23]: I had written "what the business requires"; the row says "that".
    (u'''not measuring *"what the business requires to fully maintain
  its long-term competitive position and its unit volume."*''',
     u'''not measuring what **[E2-23]** calls the amount
  *"that the business requires to fully maintain its long-term competitive position and its unit
  volume."*'''),

    # G. the proxy quote, exact.
    (u'''*"each NEO receiv[ed] approximately 100% of their target award
  for this component"*''',
     u'''*"which resulted in each NEO receiving approximately 100% of their
  target award for this component of the bonus"*'''),

    # H. the screen's acq_note is itself truncated mid-word in the CSV.
    (u'''**The screen’s warning that *"the numerator
and the denominator may be different companies"* is correct and is worse than it looks**''',
     u'''**The screen’s warning — that the numerator and the
denominator may be different companies — is correct and is worse than it looks**'''),

    # I. [E2-47] in the row's own words.
    (u'''**The test cannot be run on book equity here and the reason is [E2-47]’s own carve-out** -
unusual debt-equity ratios and mis-stated asset values.''',
     u'''**The test cannot be run on book equity here and the reason is [E2-47]’s own carve-out**,
which excepts *"companies with unusual debt-equity ratios or those with important assets carried
at unrealistic balance sheet values."*'''),
]

missed = []
for old, new in FIX:
    if old in t:
        t = t.replace(old, new, 1)
    else:
        missed.append(old[:80])

io.open(P, "w", encoding="utf-8").write(t)
print("applied:", len(FIX) - len(missed), "of", len(FIX))
for m in missed:
    print("  NOT FOUND:", repr(m))
print("len", n0, "->", len(t))
