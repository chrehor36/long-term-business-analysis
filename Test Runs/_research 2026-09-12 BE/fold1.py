# -*- coding: utf-8 -*-
"""FOLD steps 1 and 2 for the BE run: the COMPLETED entry and the TIER 3 strike."""
import io, os

ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
p = os.path.join(ROOT, "Screens", "WATCHLIST RUN QUEUE.md")
t = io.open(p, encoding="utf-8").read()

# ---- STEP 2: strike BE in the TIER 3 roster
old = "SWK, ~~ARM~~, ~~CALX~~, BE, ~~MU~~"
new = "SWK, ~~ARM~~, ~~CALX~~, ~~BE~~, ~~MU~~"
assert t.count(old) == 1, "tier 3 roster line not found exactly once"
t = t.replace(old, new)

# ---- STEP 1: the COMPLETED entry
entry = io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "fold_entry.md"), encoding="utf-8").read()
anchor = "## COMPLETED FROM THE QUEUE\n"
assert t.count(anchor) == 1, "COMPLETED header not found exactly once"
t = t.replace(anchor, anchor + entry)

io.open(p, "w", encoding="utf-8").write(t)
print("fold steps 1 and 2 written to", p)
