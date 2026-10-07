import io
p="q3q4.md"; s=io.open(p,encoding="utf-8").read()
reps=[
("**Revenue compounded 43% a year FY2019-FY2025 ($73.5M → $443.6M)","**Revenue compounded 34.9% a year FY2019-FY2025 ($73.5M → $443.6M)"),
("$252.3M of stock compensation;","$253.3M of stock compensation;"),
("(TTM −$16.6M to −$20.3M, one-quarter of the\n  FY2022 figure)","(TTM −$16.6M to −$20.3M, about a fifth to a quarter of the\n  FY2022 figure)"),
("and cover about one year of the 2025 option-exercise and ESPP\n  issuance only.","against **4,013,092 shares added in FY2025 alone** — about 35% of one year's issuance."),
("In FY2025 the company **stopped paying cash to net-settle vesting taxes** ($12.8M in 2024,\n  zero in 2025) and **resumed in 2026** ($5.0M in H1-2026) — so FY2025 issuance was larger, and its\n  financing outflow smaller, than the pattern either side of it.",
 "The cash paid to net-settle vesting taxes was $16.0M (2023), $12.8M (2024), **zero in 2025** and $5.0M in\n  H1-2026; the FY2025 equity statement shows 3,295,924 RSU shares issued on vesting with no withholding\n  payment, so the year's issuance ran gross."),
("the competitor row shows Q2 Holdings with the same\n  structure (convertible notes, capped calls, account-opening and lending acquisitions, Adjusted EBITDA\n  reporting, SBC above 10% of revenue)",
 "the competitor row shows Q2 Holdings with the same\n  financial structure (convertible notes with capped calls in its cash-flow statement, SBC above 10% of\n  revenue)"),
("**adding it back does not change the sign of any year** (FY2025 capex end −$42.5M → about −$29.6M; TTM\n  −$20.3M → about −$7.9M).",
 "**adding it back does not change the sign of any year** (adding back the \"Deferred costs\" working-capital\n  line, −$12.3M in FY2025 and −$12.4M TTM: FY2025 capex end −$42.5M → about −$30.2M; TTM −$20.3M → about\n  −$7.9M)."),
("(ii) organic growth has slowed from 22.4%\nto 15.9%, and the credit agreement's 10% recurring-revenue-growth covenant is the kind of line a slowdown\ncrosses;",
 "(ii) organic growth has slowed from 22.4%\nto 15.9%, and until 2026-12-31 the credit agreement tests recurring-revenue growth of at least 10%;"),
]
for a,b in reps:
    if a not in s: print("MISSING:", a[:90]); continue
    s=s.replace(a,b)
io.open(p,"w",encoding="utf-8").write(s)
