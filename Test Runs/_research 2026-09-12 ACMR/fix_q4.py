import io
p="Test Runs/_research 2026-09-12 ACMR/q4.md"; s=io.open(p,encoding="utf-8").read()
reps=[("**Adding it back moves the FY2025 D&A-end figure from −$60.2M to about\n−$52.1M**","**Adding back the undistributed $8,190k moves the FY2025 D&A-end figure from −$60.2M to\n−$52.0M**"),
("operating cash less capex was **−$67.6M**","the company's own filed free cash flow was **−$67,092k**")]
for a,b in reps:
    assert a in s, a[:50]; s=s.replace(a,b)
io.open(p,"w",encoding="utf-8").write(s); print("ok")
