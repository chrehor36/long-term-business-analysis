import io
p="Test Runs/2026-09-12 Run - ACMR ACM Research.md"; s=io.open(p,encoding="utf-8").read()
a="— *while the company held\n  $969,229k of cash*."
b="— *seven weeks after a quarter-end at\n  which the company held $872,269k of cash and cash equivalents* (10-Q Q1-2026, 2026-03-31)."
assert a in s; s=s.replace(a,b); io.open(p,"w",encoding="utf-8").write(s); print("ok")
