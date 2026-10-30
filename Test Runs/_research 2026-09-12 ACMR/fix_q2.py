import io
p="q2.md"; s=io.open(p,encoding="utf-8").read()
old1="**in FY2025 KLAC, LRCX, AMAT, ASML and ACLS all held or raised\n  gross margin; ACMR is the only filer in the row whose margin fell by more than a point.**"
new1="**in FY2025 KLAC, LRCX, AMAT, ASML and ACLS all held or raised\n  gross margin; only two filers in the row fell — ONTO by 2.5 points and ACMR by 5.7, more than\n  twice as far.**"
assert old1 in s; s=s.replace(old1,new1)
old2="R&D is **16.1% of revenue, second-highest in the row**\n(Nova 16.3% is the only higher)"
new2="R&D is **16.1% of revenue, the highest in this row**\n(only Nova, at 16.3% in the precedent KLAC/LRCX rows, is higher)"
assert old2 in s; s=s.replace(old2,new2)
io.open(p,"w",encoding="utf-8").write(s); print("fixed")
