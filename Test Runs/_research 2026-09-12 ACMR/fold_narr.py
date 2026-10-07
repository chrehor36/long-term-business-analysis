import io
p="Screens/2026-08-31 PREPPED READING LIST (operator lists).md"
s=io.open(p,encoding="utf-8").read()
add=io.open("Test Runs/_research 2026-09-12 ACMR/fold_narrative.md",encoding="utf-8").read()
if not s.endswith("\n"): s+="\n"
s+=add
io.open(p,"w",encoding="utf-8").write(s)
r="Test Runs/2026-09-12 Run - ACMR ACM Research.md"
t=io.open(r,encoding="utf-8").read()
a="*(My [E2-49] prior now stands at six\n  fires and six failures.)*"
b="*(My [E2-49] prior now stands at seven\n  fires and six failures — ROKU fired, ACMR did not.)*"
assert a in t; t=t.replace(a,b); io.open(r,"w",encoding="utf-8").write(t)
print("ok")
