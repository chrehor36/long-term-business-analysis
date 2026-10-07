import os
R = r"C:\Users\chreh\OneDrive\Documents\BRK"
H = os.path.join(R, "Test Runs", "_research 2026-09-19 PATH")
p = os.path.join(R, "Screens", "2026-08-31 PREPPED READING LIST (operator lists).md")
t = open(p, encoding="utf-8").read()
assert "PATH: Q2 OUT" not in t
f = open(os.path.join(H, "_fold.md"), encoding="utf-8").read()
t = t.rstrip("\n") + "\n" + f
open(p, "w", encoding="utf-8").write(t)
q = os.path.join(R, "Screens", "SURVIVAL SHAPES - index.md")
u = open(q, encoding="utf-8").read()
old = "DASH (2026-09-18, a feature: 73.4% of operating cash FY2021-25 on the charge, grants of $1.8bn in H1 2026) |"
assert u.count(old) == 1
u = u.replace(old, "DASH (2026-09-18, a feature: 73.4% of operating cash FY2021-25 on the charge, grants of $1.8bn in H1 2026), "
              "PATH (2026-09-19, the mechanism: 205.9% of operating cash FY2022-26 on the charge; five-year owner earnings -$211.5M, "
              "-$339.8M at the larger of charge and grant value; $1.09bn of buybacks retired the issuance) |")
open(q, "w", encoding="utf-8").write(u)
print("ok")
