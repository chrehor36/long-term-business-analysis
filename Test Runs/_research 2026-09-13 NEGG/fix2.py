p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 NEGG\sec_q2.md"
s = open(p, encoding="utf-8").read()
reps = [
 ("(*\"reduced business from certain 3PL customers\"*); B2C net sales fell from $0.9bn... no — B2C net sales rose\nto $1.2bn in 2025 on price, from $0.9bn.", "(*\"reduced business from certain 3PL customers\"*). B2C net sales did rise, $0.9bn → $1.2bn in 2025 — on price."),
 ("| −$22.6bn *(capex-heavy AWS build; not comparable in sign)*", "| −$56.7bn *(the AWS and fulfilment build; not comparable in sign)*"),
 ("| +$6.8bn *(FY2022–FY2026)*", "| +$6.0bn *(FY2022–FY2026)*"),
 ("OCF − capex +$65.5bn)*", "OCF − capex +$65.8bn, FY2022–FY2026)*"),
 ("| +$7.6bn *(2021–2025)*", "| +$6.6bn *(2021–2025)*"),
]
for a, b in reps:
    assert a in s, a[:50]
    s = s.replace(a, b)
banner = """---
> ⛔ **THE FILE CLOSES HERE — Q2 OUT, on the business.** Per the hard sequence, Q5 does not open.
> **Q3 and Q4 are RECORDED BELOW, NOT GOVERNING**, at the brief's instruction and per the queue's
> prohibition on skimming a gate: the triage label that filed this name as "negative on every construction
> ... the file's work is Q1-Q2 plus the honest statement" is the defect the correction of 2026-09-12 names.
> Nothing below can reopen Q2 **[E2-37, E3-39]**, and nothing below is a clearance.

"""
open(p, "w", encoding="utf-8").write(s)
run = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - NEGG Newegg Commerce.md"
r = open(run, encoding="utf-8").read()
i = r.index("## Q2 — IS IT A FRANCHISE? **[E3-03]**")
j = r.index("## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?")
r = r[:i] + s + banner + r[j:]
open(run, "w", encoding="utf-8").write(r)
print("ok")
