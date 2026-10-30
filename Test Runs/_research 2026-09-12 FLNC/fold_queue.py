p = "Screens/WATCHLIST RUN QUEUE.md"
s = open(p, encoding="utf-8").read()

# STEP 2: strike FLNC in the tier-3 roster
old = "~~SWK~~, ~~ARM~~, ~~CALX~~, ~~BE~~, ~~MU~~, ~~ROKU~~, RGTI, ~~ORCL~~, ~~BA~~, ~~ACMR~~, ~~ALKT~~, ~~INTC~~, ~~ACVA~~, NEGG, FLNC"
new = "~~SWK~~, ~~ARM~~, ~~CALX~~, ~~BE~~, ~~MU~~, ~~ROKU~~, RGTI, ~~ORCL~~, ~~BA~~, ~~ACMR~~, ~~ALKT~~, ~~INTC~~, ~~ACVA~~, NEGG, ~~FLNC~~"
assert s.count(old) == 1
s = s.replace(old, new)

# STEP 2b: note beside the STILL LIVE line (dated text left as written)
anchor = "The SIGN CHANGE sub-class is now fully run: all three found the label did not describe owner earnings.)*"
assert s.count(anchor) == 1
s = s.replace(anchor, anchor + " *(FLNC RUN 2026-09-12: struck - closed at Q2 on the business. **The label \"negative on every construction\" was FACTUALLY RIGHT for FLNC**, unlike BE: rebuilt, owner earnings are -$183M to -$101M on every window and both (c) ends. **It was still the wrong instruction**: every reason the number is negative - the asymmetric cell-cost curve, sponsor-lent bankability, customer deposits discharged at a 5-13% gross margin - sits in Q1, Q2 and Q4, which the label told the run to skim. NEGG is now the last name live under the first sub-class; read it as unlabelled.)*")

# STEP 1: the COMPLETED entry, newest first
head = "## COMPLETED FROM THE QUEUE\n"
assert s.count(head) == 1
entry = open("Test Runs/_research 2026-09-12 FLNC/fold_entry.md", encoding="utf-8").read()
s = s.replace(head, head + entry)
open(p, "w", encoding="utf-8").write(s)
print("queue folded")
