p = "Screens/WATCHLIST RUN QUEUE.md"
R = "Test Runs/_research 2026-09-18 SNOW/"
s = open(p, encoding="utf-8").read()
e = open(R + "_fold_entry.md", encoding="utf-8").read()
n = open(R + "_fold_note.md", encoding="utf-8").read()
a = "## COMPLETED FROM THE QUEUE\n- **SMCI (Super Micro Computer, Inc.), 2026-09-18"
assert s.count(a) == 1
s = s.replace(a, "## COMPLETED FROM THE QUEUE\n" + e + "- **SMCI (Super Micro Computer, Inc.), 2026-09-18")
b = "| perimeter or restatement above threshold: read the filing first | ~~SMCI~~, SNOW, TSLA, RIVN, DJT, BX, AEHR |"
assert s.count(b) == 1
s = s.replace(b, "| perimeter or restatement above threshold: read the filing first | ~~SMCI~~, ~~SNOW~~, TSLA, RIVN, DJT, BX, AEHR |")
anchor = "a `restatement_shift` of exactly 1.0 means nothing was found in the one element read.*\n"
assert s.count(anchor) == 1
s = s.replace(anchor, anchor + n)
open(p, "w", encoding="utf-8").write(s)
print("queue ok")
