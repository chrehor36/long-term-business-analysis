import io
p="Test Runs/_research 2026-09-12 ACMR/q3.md"; s=io.open(p,encoding="utf-8").read()
reps=[("**$4bn is 4.4 times FY2025 revenue and\n  3.5 times the top of the 2026 guide.**","**$4bn is 4.4 times FY2025 revenue and\n  3.4 times the top of the 2026 guide.**"),
("**+47% in seven and a half\n  years**, about 5% a year,","**+47% in about eight\n  years**, about 5% a year,"),
("**An 18.8% dilution of the look-through claim in\n  eighteen months**","**An 18.8% dilution of the look-through claim in\n  nineteen months**"),
("Weighted basic shares, split-adjusted (3-for-1, 2022)","Weighted basic shares, split-adjusted (three-for-one, effected March 2022 as a stock dividend)")]
for a,b in reps:
    assert a in s, a[:40]; s=s.replace(a,b)
io.open(p,"w",encoding="utf-8").write(s); print("ok")
