run = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - NEGG Newegg Commerce.md"
r = open(run, encoding="utf-8").read()
old_c = r[r.index("- [x] **weak accounting — the cockroach count [E4-22 first].**"):r.index("- [ ] **unintelligible footnotes**")]
new_c = """- [x] **weak accounting — the cockroach count [E4-22 first].** Three, none of them large alone: **(1)** material
  weaknesses in internal control at FY2021 and FY2022 (*"lack of structure and responsibility, insufficient
  number of qualified resources"*, FY2021 20-F Item 15), remediated by FY2023; **(2)** the XBRL sign errors on net
  income in two vintages (Step 0); **(3)** the auditor's one critical audit matter is **$48.5M of vendor-incentive
  receivables** estimated from *"a significant number of vendor agreements with various terms and conditions"* —
  [E2-50]'s *"stroke of a pen"* class, equal to 30% of year-end equity. **And an Interim CFO since May 2024,
  twenty-eight months.** *"There is seldom just one cockroach in the kitchen."* None found is a restatement.
  *(Corrected in drafting, before commit of this section's final form: a fourth "cockroach" — the 20-F's
  "2.2 million buyers purchased over 312,000 items" read as an impossible sentence — was withdrawn on reading the
  four prior 20-Fs, which carry the same construction every year (675,000 items in 2021). "Items" is the count of
  distinct products bought, and it is a units series, used at Q2.)*
"""
r = r.replace(old_c, new_c)
a = "; and the 20-F still opens with an\nimpossible sentence about 312,000 items."
assert a in r
r = r.replace(a, ".")
# Q2 point 3 addition
b = "visits dropped from the metrics table the year they fell 20%."
assert b in r
r = r.replace(b, b + """ **And the 20-F's own opening paragraph carries three more physical series,
restated each year (Item 4.A, FY2021–FY2025 20-Fs): cumulative orders since 2005 of *"over 176 million"* (2021),
187M, 193M, 198M, 203M — so roughly 11M orders in 2022, then about 6M, 5M and 5M a year (±1M on "over" rounding);
distinct items bought *"over 675,000"* (2021) → 604,000 → 436,000 → 302,000 → 312,000; and SKUs offered *"more than 38
million"* from 56,000 brands (2021) → 20M/51,000 → 6M/35,000 → 4M/27,000 → 4.9M/22,000.** On the filer's own
cumulative count, **annual orders are less than half what they were in 2022**.""")
open(run, "w", encoding="utf-8").write(r)
print("ok")
