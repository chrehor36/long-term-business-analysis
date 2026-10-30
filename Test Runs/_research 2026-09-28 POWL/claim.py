src = r"Test Runs/_TEMPLATE - Company Run.md"
dst = r"Test Runs/2026-09-28 Run - POWL Powell Industries.md"
t = open(src, encoding="utf-8").read()
lines = t.split("\n")
lines[0] = "# Company Run — Powell Industries, Inc. (POWL) — 2026-09-28"
lines.insert(1, "*Claimed at dispatch 2026-09-28 late evening EDT by the unattended overnight cycle (lock PID 10992). WAVE 7 name 109 of 218 by `Screens/_daily/_wave7_order.txt` (the done file has 108 lines ending PFGC; the order file's line 109 is POWL). Written early: each question is appended as it closes and committed.*")
open(dst, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print("ok")
