import io
for p in ["Test Runs/2026-09-12 Run - ACMR ACM Research.md","Test Runs/_research 2026-09-12 ACMR/q2.md"]:
    s=io.open(p,encoding="utf-8").read()
    a="**Two of those three test results\narrived and one of them went partly against me** — (c), see the concentration table."
    b="**All three test results arrived:\n(a) and (b) went with the prior, and (c) went partly against it** — see the concentration table."
    assert a in s; s=s.replace(a,b)
    a2="the [E2-44] test, eleven years, same\nformula**"
    b2="the [E2-44] test, ten filed years, same\nformula**"
    assert a2 in s; s=s.replace(a2,b2)
    io.open(p,"w",encoding="utf-8").write(s)
print("ok")
