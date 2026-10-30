p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 NEGG\sec_q4_end.md"
s = open(p, encoding="utf-8").read()
def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b)
rep("lifts the\n  seven-year mean by $15M;", "lifts the\n  seven-year mean by about $17M (the six years without it average −$44.7M);")
rep("the band is $0.2M–$16.9M wide in any\n  year", "the band is $0.4M–$16.8M wide in any\n  year")
old = s[s.index("**Quantified from filed figures**"):s.index("**The case against this death, stated fairly [E4-51].**")]
new = """**Quantified from filed figures** *(arithmetic on the 2026-06-30 balance sheet, H1 2026 run-rates and the 2022–24
record, not a forecast)*:
- **Margin leg:** a return to 2023–24's 10.6–11.2% gross margin from H1 2026's 13.3% is **~2.4 points on the $1.23–1.47bn
  guided year = $30–35M of gross profit.** Against H1 2026's SG&A run-rate of **~$149M a year** (which already reflects
  the cost cuts — 2022–24's SG&A was $183–266M), that takes the operating result from +$8.8M a half to **roughly −$2M to
  −$20M a year**. *Honest correction to this file's own first draft: the 2022–24 losses of ~$50M a year were earned on a
  cost base $35–115M larger, and are not the right yardstick for the margin leg alone.* **Add a markdown on shortage-cost
  stock** — 10% of the $187.7M inventory is ~$19M, once.
- **Credit leg:** H1 2026 cost of sales ran **~$3.0M a day** ($543.2M ÷ 181). **Payables of $122.6M are ~41 days.** Terms
  cut to 30 days release **~$33M** to suppliers; to 15 days, **~$78M** — nearly the whole cash balance.
- **Bank leg:** $17M of letters of credit to collateralise if the revolver lapses; no drawn balance to repay.
- **Against $82.2M of cash:** a low-end margin year (−$20M), the one-off markdown (−$19M), a 30-day terms tightening
  (−$33M) and LC collateral (−$17M) total **−$89M**. **The margin and markdown legs alone leave the company with ~$43M and
  a smaller business; it is the credit leg — which is the lenders' choice, not the company's — that empties it.** Over
  two such years, with a baby shelf worth ~$6M a year and a controller that cannot subscribe, **the cash does not
  survive without new credit.**
- **Likelihood:** [ ] likely **[x] a real possibility** [ ] a low-level possibility. *The margin leg has happened in the
  record already (2022–24), and the credit leg partly did (payables −$57.4M in 2024). What is new is that the backstops
  that carried the company through it — $123.5M of cash at YE2022, a $100M revolver, a parent not yet in liquidation
  proceedings — are smaller or gone. What argues for "low-level" is the lower cost base; it is recorded, and it is why
  the likelihood is not "likely".*
- **[E4-40] — exposure, not experience.** The most recent experience is the best half-year since 2021. The exposure is
  $187.7M of shortage-cost inventory on $122.6M of 41-day credit.

"""
s = s.replace(old, new)
rep("- **Q3 2026 release** (last year's H1 release came 2025-08-21; the Q2 2026 release came 2026-08-27): inventory, payables\n  days, and the obsolete-inventory provision through the seasonal build.", "- **The next results release** (2026 moved to quarterly releases — Q1 on 2026-05-28, Q2 on 2026-08-27; 2025 had only an H1\n  release): inventory, payables days, and the obsolete-inventory provision through the seasonal build.")
open(p, "w", encoding="utf-8").write(s)
run = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - NEGG Newegg Commerce.md"
r = open(run, encoding="utf-8").read()
i = r.index("## Q4 — WILL IT SURVIVE?")
r = r[:i] + s
open(run, "w", encoding="utf-8").write(r)
r2 = r.replace("*IN PROGRESS — written under the write-early protocol.", "*Written under the write-early protocol; closed 2026-09-13.")
open(run, "w", encoding="utf-8").write(r2)
print("ok", len(r2))
