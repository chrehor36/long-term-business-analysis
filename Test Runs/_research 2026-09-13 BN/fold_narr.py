import os
D = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(D, "..", "..", "Screens", "2026-08-31 PREPPED READING LIST (operator lists).md")
t = open(P, encoding="utf-8").read()
add = open(os.path.join(D, "fold_narrative.md"), encoding="utf-8").read()
add = add.replace("**Started 01:20, killed by a session limit after Q1 at 01:39,",
                  "**Research began 01:20; the session was killed by a session limit after Q1 (last write 01:39); the run was")
add = add.replace("resumed at\n05:35 from the drafts on disk", "resumed at\n05:35 from the drafts on disk")
assert "exactly one name without a price and a pass/fail line: BN." in t
if not t.endswith("\n"):
    t += "\n"
open(P, "w", encoding="utf-8").write(t + add)
print("appended", len(add))
