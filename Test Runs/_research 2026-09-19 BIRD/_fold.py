# BIRD fold, 2026-09-19: register entry (top of the register), wave 5 strike, dated note beside the table,
# narrative fold into the prepped reading list, survival-shapes index instances. Each insertion asserts its anchor.
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.join(here, "..", "..")
def rd(p): return open(p, encoding="utf-8").read()
def wr(p, t): open(p, "w", encoding="utf-8", newline="").write(t)
Q = os.path.join(root, "Screens", "WATCHLIST RUN QUEUE.md"); q = rd(Q)
nl = "\r\n" if "\r\n" in q else "\n"
fix = lambda s: s.replace("\r\n", "\n").replace("\n", nl)
assert "- **BIRD (" not in q
# 1. register entry directly under the heading line
h = nl + "## COMPLETED FROM THE QUEUE" + nl
assert q.count(h) == 1
q = q.replace(h, h + fix(rd(os.path.join(here, "_register_entry.md")).rstrip("\n")) + nl, 1)
# 2. strike
row = "| cap rejected as a broken input: read the cover | ~~HBB~~, ~~LCID~~, ~~SOUN~~, BIRD |"
assert q.count(row) == 1
q = q.replace(row, row.replace(", BIRD |", ", ~~BIRD~~ |"))
# 3. dated note after the SOUN note
i = q.index("*Dated note, 2026-09-19 (the SOUN run)")
j = q.index(nl, i)
q = q[:j] + nl + nl + fix(rd(os.path.join(here, "_wave5note.md")).strip("\n")) + q[j:]
wr(Q, q); print("queue ok")
# 4. reading list
R = os.path.join(root, "Screens", "2026-08-31 PREPPED READING LIST (operator lists).md"); r = rd(R)
nl2 = "\r\n" if "\r\n" in r else "\n"
assert "UPDATE 2026-09-19 - BIRD" not in r
r = r.rstrip() + nl2 + rd(os.path.join(here, "_readinglist.md")).replace("\n", nl2)
wr(R, r); print("reading list ok")
# 5. survival shapes
S = os.path.join(root, "Screens", "SURVIVAL SHAPES - index.md"); s = rd(S)
a8 = "the liquidity plan naming the ATM; common 200.0M to about 485M since FY2022) |"
assert s.count(a8) == 1
s = s.replace(a8, a8[:-2] + ", BIRD (2026-09-19, the mechanism, with #6 as a feature: Smartbird, formerly Allbirds, sold its footwear business and funds a GPU-leasing start with an ATM and notes convertible at 93% of the lowest ten-day VWAP; continuing overhead about $36M a year against one lease's receipts of about $1.0M; the $8.25M of notes alone about a third of the count at $2.30) |")
a6 = "growth capex funded by notes; #11 as mechanism, #1 as feature) |"
assert s.count(a6) == 1
s = s.replace(a6, a6[:-2] + ", BIRD (2026-09-19, a feature of #8: a lessor funded by two-year secured floorless convertible notes against three-year leases to one lessee reporting its own going-concern doubt) |")
wr(S, s); print("shapes ok")
