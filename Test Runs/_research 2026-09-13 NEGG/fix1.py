p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 NEGG\sec_step0_q1.md"
s = open(p, encoding="utf-8").read()
reps = [
 ("**Share consolidation checked: a twenty-for-one share combination took effect 2026-04-07 — no, 2025-04-07**", "**Share consolidation checked: a twenty-for-one share combination took effect 2025-04-07**"),
 ("| **TTM to 2026-06-30** | **+3.5** | −36.6 | −40.0 | **5.8** | **10.4** | 3.2 | 19.1 |", "| **TTM to 2026-06-30** | **+3.5** | +4.7 | −40.0 | **5.8** | **10.4** | 3.2 | 9.3 |"),
 ("| 2023 | −15.6 | −49.3 | **−79.6** | −62.7 |", "| 2023 | −15.6 | −49.2 | **−79.5** | −62.7 |"),
 ("| 2025 | +28.1 | +6.4 | **+3.7** | −1.2 |", "| 2025 | +28.1 | +6.4 | **+3.8** | −1.1 |"),
 ("**For every $100 of goods it sells, about $84 goes to the supplier, $3 to freight and\n$2 to credit-card processors; about $9.50 of gross margin is left on its own inventory, before a warehouse,\na website or a salary is paid.**", "**For every $100 of its own goods it sells, about $87 goes to the supplier and $3 to freight;\nabout $9.50 of gross margin is left on its own inventory (2025), and card processors then take another\n$2.40 of every sales dollar out of SG&A before a warehouse, a website or a salary is paid.**"),
 ("the two lines reconcile to filed gross profit to the $0.1M in every year*):", "the two lines reconcile to filed gross profit to $0.1M in 2023–2025; in 2020–2022 an unallocated residual of\n$1.6M–$5.9M — reserve releases and other small cost lines — sits in neither*):"),
 ("**Operating loss: 2022 not tabled here, 2023 −$71.1M, 2024 −$51.6M, 2025 −$9.5M;\nH1 2026 +$8.8M.** 2020 and 2021 were the only operating profits in the seven years filed ($23.5M, $33.5M).", "**Operating result: 2022 −$49.5M, 2023 −$71.1M, 2024 −$51.6M, 2025 −$9.5M;\nH1 2026 +$8.8M.** 2020 and 2021 were the only operating profits in the seven years filed ($23.4M, $33.5M)."),
]
for a, b in reps:
    assert a in s, a[:60]
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
run = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - NEGG Newegg Commerce.md"
r = open(run, encoding="utf-8").read()
i = r.index("## STEP 0 — THE RATE, AND THE FILING")
j = r.index("## Q2 — IS IT A FRANCHISE? **[E3-03]**")
r = r[:i] + s + r[j:]
open(run, "w", encoding="utf-8").write(r)
print("ok", len(r))
