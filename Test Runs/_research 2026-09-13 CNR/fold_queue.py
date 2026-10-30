import re, sys
R = "Test Runs/_research 2026-09-13 CNR/"
Q = "Screens/WATCHLIST RUN QUEUE.md"
L = "Screens/2026-08-31 PREPPED READING LIST (operator lists).md"
RUN = "Test Runs/2026-09-13 Run - CNR Core Natural Resources.md"

# 0. run file: add the E2-63 brief defect
s = open(RUN, encoding="utf-8").read()
add = ("5. **\"[E2-63] can be decomposed directly\"**, set beside the units series - **[E2-63] is the capped-upside row**\n"
       "   (*\"limited upside potential also unless more capital is continuously invested\"*); the units test is **[E4-55]**.\n"
       "   This run used [E2-63] for the ceiling it states (Q1, Q5). The NEGG run found the same line in its brief.\n")
if "[E2-63] can be decomposed directly" not in s:
    s = s.rstrip("\n") + "\n" + add
    open(RUN, "w", encoding="utf-8").write(s)

# 1. queue: entry at the top of COMPLETED, and strike the roster
q = open(Q, encoding="utf-8").read()
entry = open(R + "fold_entry.md", encoding="utf-8").read().rstrip("\n") + "\n"
head = "## COMPLETED FROM THE QUEUE\n"
assert q.count(head) == 1
if "- **CNR (Core Natural Resources, Inc.), 2026-09-13" not in q:
    q = q.replace(head, head + entry, 1)
old = "~~DRI~~, CNR, ~~COKE~~"
if old in q:
    q = q.replace(old, "~~DRI~~, ~~CNR~~, ~~COKE~~", 1)
assert "~~CNR~~" in q
open(Q, "w", encoding="utf-8").write(q)

# 2. reading list: append the narrative fold
l = open(L, encoding="utf-8").read()
if "## UPDATE 2026-09-13 - CNR:" not in l:
    l = l.rstrip("\n") + "\n" + open(R + "fold_narrative.md", encoding="utf-8").read()
    open(L, "w", encoding="utf-8").write(l)
print("fold applied")
