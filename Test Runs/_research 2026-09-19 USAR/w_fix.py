# -*- coding: utf-8 -*-
import os
os.chdir(r"C:\Users\chreh\OneDrive\Documents\BRK")
p = "Test Runs/2026-09-19 Run - USAR USA Rare Earth.md"
s = open(p, encoding="utf-8").read()
n0 = len(s)

fixes = [
 # TTM revenue arithmetic: FY2025 $1,643k (all of it in H2) + H1 2026 $11,519k = $13,162k
 ("the business collected about $16.9M of revenue and **used $75.3M of\noperating cash in the first half of 2026 alone**",
  "the business collected **$13.2M** of revenue (FY2025's $1,643k, all of it in the second half,\nplus H1 2026's $11,519k) and **used $75.3M of operating cash in the first half of 2026 alone**"),
 ("revenue about $16.9M against a TTM operating cash outflow of $106.1M",
  "revenue of **$13.2M** against a TTM operating cash outflow of $106.1M"),
 ("TTM revenue of about **$16.9M** against\n  TTM operating and capital cash outflows of about **$245M**",
  "TTM revenue of **$13.2M** against\n  TTM operating and capital cash outflows of **$245.5M** ($106.1M operating plus $139.5M capital)"),
 ("done: $16.9M of TTM revenue, a negative gross margin, and $245M of annual cash consumption.**",
  "done: $13.2M of TTM revenue, a negative gross margin, and $245.5M of cash consumed in the last\ntwelve months.**"),
 # the $4.1bn programme against pro forma cash: 4,100/1,392 = 2.9x, not 11x
 ("since the $4.1bn\n   programme is 11x the cash on hand and the company",
  "since the $4.1bn\n   programme is **about 2.9x the cash on hand** and the company"),
 # make the per-share table foot to the filed balance sheet
 ("""| less total liabilities ($2,002.2M) | **$(5.39)** | (35.1)% |
| **= pro forma book value** | **$12.69** | 82.6% |""",
  """| other assets (receivables $6.3M, inventories $74.8M, prepaid $12.3M, other current $77.9M, equipment deposits $46.9M, right-of-use $2.2M, other non-current $0.5M = $220.9M) | **$0.59** | 3.8% |
| less total liabilities ($2,002.2M) | **$(5.39)** | (35.1)% |
| less mezzanine equity, the 12% preferred ($10.3M) | **$(0.03)** | (0.2)% |
| **= pro forma book value attributable to common ($4,714.5M)** | **$12.69** | 82.6% |"""),
]
bad = [a for a, b in fixes if a not in s]
if bad:
    for a in bad:
        print("NOT FOUND:", repr(a[:90]))
    raise SystemExit(1)
for a, b in fixes:
    s = s.replace(a, b, 1)

open(p, "w", encoding="utf-8").write(s)
print("ok", n0, "->", len(s))
