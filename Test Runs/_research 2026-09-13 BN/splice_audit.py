import os
D = os.path.dirname(os.path.abspath(__file__))
run = os.path.join(D, "..", "2026-09-13 Run - BN Brookfield Corporation.md")
r = open(run, encoding="utf-8").read()
a = r.index("## SELF-AUDIT")
t = open(os.path.join(D, "frag_audit.md"), encoding="utf-8").read()
open(run, "w", encoding="utf-8").write(r[:a] + t)
print("ok", a)
