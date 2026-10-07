import io
for p in ["Test Runs/2026-09-12 Run - ACMR ACM Research.md","Test Runs/_research 2026-09-12 ACMR/q4.md"]:
    s=io.open(p,encoding="utf-8").read()
    a="— **73.2% at 2026-06-30** — because the\n   income ratio blends in the registrant's own 100%-owned (loss-making) operations."
    b="— **73.2% at 2026-06-30** — because the\n   FY2025 income ratio carries ownership of 81.5% for the eight and a half months before the\n   September 2025 private offering took it to 74.6% (the registrant's own loss-making operations pull\n   the ratio the other way, which is why it lands at 77.2% rather than nearer 80%)."
    assert a in s, p; s=s.replace(a,b); io.open(p,"w",encoding="utf-8").write(s)
print("ok")
