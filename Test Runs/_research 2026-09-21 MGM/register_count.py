# -*- coding: utf-8 -*-
"""Re-derive the register entry number BY LINE INDEX, never by string.replace."""
import io, os, re
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Q = os.path.join(BASE, "Screens", "WATCHLIST RUN QUEUE.md")
lines = io.open(Q, encoding="utf-8").read().split("\n")
heads = [i for i, l in enumerate(lines) if l.strip() == "## COMPLETED FROM THE QUEUE"]
tails = [i for i, l in enumerate(lines) if l.strip().startswith("## THE WRITE-EARLY PROTOCOL")]
print("heading line matches (line-exact):", [i + 1 for i in heads])
print("tail  line matches:", [i + 1 for i in tails])
assert len(heads) == 1, "heading is NOT unique - stop"
assert len(tails) == 1, "tail is NOT unique - stop"
h, tl = heads[0], tails[0]
slice_ = lines[h:tl]
entries = [l for l in slice_ if re.match(r"^- \*\*", l)]
print("slice lines:", len(slice_), "from line", h + 1, "to", tl)
print("entries counted (^- \*\*):", len(entries))
print("first three:", [e[:90] for e in entries[:3]])
print("last three:", [e[:90] for e in entries[-3:]])
print()
print("NEXT ENTRY NUMBER =", len(entries) + 1)
