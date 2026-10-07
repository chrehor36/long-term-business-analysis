import os
os.chdir(r"C:\Users\chreh\OneDrive\Documents\BRK")
Q = "Screens/WATCHLIST RUN QUEUE.md"
t = open(Q, encoding="utf-8").read()
entry = open(r"Test Runs/_research 2026-09-18 AEHR/_fold_entry.md", encoding="utf-8").read()
note = open(r"Test Runs/_research 2026-09-18 AEHR/_fold_note.md", encoding="utf-8").read()
assert "AEHR (Aehr" not in t
h = "## COMPLETED FROM THE QUEUE\n"
assert t.count(h) == 1
t = t.replace(h, h + entry, 1)
old = "| perimeter or restatement above threshold: read the filing first | ~~SMCI~~, ~~SNOW~~, ~~TSLA~~, ~~RIVN~~, ~~DJT~~, ~~BX~~, AEHR |"
assert t.count(old) == 1
t = t.replace(old, old.replace(", AEHR |", ", ~~AEHR~~ |"))
anchor = "*SPOT and SPGI had runs on 2026-07-15"
assert t.count(anchor) == 1
t = t.replace(anchor, note + "\n" + anchor, 1)
open(Q, "w", encoding="utf-8").write(t)

S = "Screens/SURVIVAL SHAPES - index.md"
s = open(S, encoding="utf-8").read()
row19 = "| 19 | **The shelf** *(proposed, pending the operator)* | CL (2026-09-18) |"
assert row19 in s
i = s.index(row19); j = s.index("\n", i)
row20 = ("\n| 20 | **The wave** *(proposed, pending the operator)* | AEHR (2026-09-18) | one customer's capacity build in one new "
         "market makes the record; when that market slows the systems and the per-device consumables stop together, the inventory "
         "built for the ramp stays, and the next market must be found and funded again, with new stock | |")
s = s[:j] + row20 + s[j:]
o = "**All seven are listed so briefs count correctly; none is settled.**"
assert o in s
s = s.replace(o, "AEHR proposed THE WAVE (2026-09-18), arguing it is neither #11 nor #8: the gains were not passed to customers "
              "(gross margin 46-50% through the wave) and customers paid most of the costs, but the demand was one buyer's capacity "
              "cycle, and the consumable that looked recurring stopped with it (contactors -60% in two years); #8 is carried as its "
              "feature, because over ten years new stock, not the customers, funded the working capital. **All eight are listed so "
              "briefs count correctly; none is settled.**")
open(S, "w", encoding="utf-8").write(s)
print("ok")
