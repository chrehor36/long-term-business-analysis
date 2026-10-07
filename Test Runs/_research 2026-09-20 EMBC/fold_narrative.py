p = r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\2026-08-31 PREPPED READING LIST (operator lists).md"
n = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-20 EMBC\_narrative_fold.md"
s = open(p, encoding="utf-8").read()
assert "# EMBC (Embecta Corp.)" not in s
add = open(n, encoding="utf-8").read()
if not s.endswith("\n"):
    s += "\n"
s = s + add
open(p, "w", encoding="utf-8").write(s)
print("appended", len(add), "chars; file now", len(s))
