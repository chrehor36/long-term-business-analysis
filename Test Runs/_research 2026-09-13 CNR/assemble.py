import os
p = "Test Runs/2026-09-13 Run - CNR Core Natural Resources.md"
R = "Test Runs/_research 2026-09-13 CNR/"
s = open(p, encoding="utf-8").read()
a = "**The company says it returned \"approximately 80 percent of its free cash flow.\""
b = ("**The program's own terms say where the money comes from**: *\"Any repurchases are to be funded from\n"
     "available cash on hand or short-term borrowings\"* (10-K FY2025, Note 4). **The company says it returned\n"
     "\"approximately 80 percent of its free cash flow.\"")
if a in s and "funded from\navailable cash on hand" not in s:
    s = s.replace(a, b, 1)
i = s.index("## SELF-AUDIT")
s = s[:i] + open(R + "_register.md", encoding="utf-8").read()
open(p, "w", encoding="utf-8").write(s)
print("ok", len(s))
