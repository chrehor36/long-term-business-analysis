import os
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
R = os.path.join(ROOT, "Test Runs", "_research 2026-09-18 RIVN")
p = os.path.join(ROOT, "Screens", "WATCHLIST RUN QUEUE.md")
s = open(p, encoding="utf-8").read()
entry = open(os.path.join(R, "_fold_entry.md"), encoding="utf-8").read()
note = open(os.path.join(R, "_fold_note.md"), encoding="utf-8").read()
assert "RIVN (Rivian" not in s, "already folded"
h = "## COMPLETED FROM THE QUEUE\n"
assert s.count(h) == 1
s = s.replace(h, h + entry, 1)
a = "| perimeter or restatement above threshold: read the filing first | ~~SMCI~~, ~~SNOW~~, ~~TSLA~~, RIVN, DJT, BX, AEHR |"
assert s.count(a) == 1
s = s.replace(a, a.replace(" RIVN,", " ~~RIVN~~,"))
anchor = "*SPOT and SPGI had runs on 2026-07-15"
assert s.count(anchor) == 1
s = s.replace(anchor, note + anchor)
open(p, "w", encoding="utf-8").write(s)
print("queue folded")
q = os.path.join(ROOT, "Screens", "2026-08-31 PREPPED READING LIST (operator lists).md")
t = open(q, encoding="utf-8").read()
assert "UPDATE 2026-09-18 - RIVN" not in t
t = t.rstrip("\n") + "\n\n" + open(os.path.join(R, "_fold_narrative.md"), encoding="utf-8").read()
open(q, "w", encoding="utf-8").write(t)
print("reading list folded")
