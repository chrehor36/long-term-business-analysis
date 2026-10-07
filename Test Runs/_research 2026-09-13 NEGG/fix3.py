p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 NEGG\sec_q3.md"
s = open(p, encoding="utf-8").read()
reps = [
 ("class, equal to 28% of equity.", "class, equal to 30% of year-end equity."),
 (" **The $26.3M vesting value exceeds the company's entire 2025 gross-profit\n  growth attributable to price, and is 8.5% of today's market cap.**", " **The $26.3M vesting value is 8.5% of today's market cap.**"),
 ("The ATM was signed\n  **2025-07-15**, a week after the stock's run from $3.50 (May) began; **1,000,000 shares sold on 2025-07-17 for\n  $29.3M gross**; the Pricing Committee authorised 500,000 more on 2025-08-17 near the $128.09 peak (6-K\n  2025-08-19).", "The ATM was signed\n  **2025-07-15**, in the middle of the stock's run from a $3.50 close (May 2025) to **$128.09 (2025-08-14)**;\n  **1,000,000 shares sold on 2025-07-17 for $29.3M gross**; the Pricing Committee authorised 500,000 more on\n  2025-08-17, three days after the peak (6-K 2025-08-19)."),
 ("(Third Amendment, 2025-08-13), and the\n  founder had resigned from the board on 2025-07-08.", "(Third Amendment, dated 2025-08-13, the day before the closing peak), and the\n  founder had resigned from the board on 2025-07-08. (Galkin was the buyer on the other side of much of the\n  float: Forms 4 show him buying from 2025-07-08 at $18.10 to 2025-08-15 at $104.72.)"),
]
for a, b in reps:
    assert a in s, a[:60]
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
run = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - NEGG Newegg Commerce.md"
r = open(run, encoding="utf-8").read()
i = r.index("## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?")
j = r.index("## Q4 — WILL IT SURVIVE?")
r = r[:i] + s + r[j:]
open(run, "w", encoding="utf-8").write(r)
print("ok")
