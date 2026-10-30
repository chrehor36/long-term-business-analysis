"""Q5 arithmetic for CL, on the FRESH pair struck 2026-09-18. Arithmetic only; no conclusion.
Price US$87.73, close of 2026-09-17 (tools/sources.py price(), aggregator, flagged).
Sovereign USD 30-year 5.29%, 09/17/2026, US Treasury daily par yield curve via tools/sources.py sovereign('USD').
Shares 797,172,829 (10-Q cover, accession 0000021665-26-000042, quarter ended 2026-06-30); split factor after
the measurement date 1.0. Owner-earnings windows from Q4 (oe.py / oe_out.md)."""
PRICE, SOV, SH = 87.73, 5.29, 797_172_829
CAP = PRICE * SH / 1e6           # $M
OE = {"most conservative (10-yr, ex working-capital release)": 2680,
      "10-yr 2016-25": 2738,
      "5-yr 2021-25  [E2-42] DEFAULT": 2833,
      "3-yr 2023-25": 3269,
      "TTM to 2026-06-30 (one year, not a mean)": 3680}
G_REALISED = 5.3   # owner earnings per diluted share, 2016-2025 CAGR, from oe_out.md
FLOOR = 10.0       # [E4-28]
print(f"shares {SH:,} x ${PRICE} = market cap ${CAP:,.1f}M")
print(f"sovereign {SOV}% (09/17/2026)   [E4-28] floor {FLOOR}%   realised OE/share growth {G_REALISED}%\n")
print("| window | owner earnings $M | yield on cap | multiple | points vs sovereign | expectancy = yield + realised growth | vs the 10% floor |")
print("|---|---|---|---|---|---|---|")
for k, oe in OE.items():
    y = oe / CAP * 100
    print(f"| {k} | {oe:,} | {y:.2f}% | {1/(y/100):.1f}x | {y-SOV:+.2f} | {y+G_REALISED:.2f}% | {y+G_REALISED-FLOOR:+.2f} |")
print("\nWhat the price already assumes (perpetual growth in OE per share required):")
for k, oe in OE.items():
    y = oe / CAP * 100
    print(f"  {k}: to reach the {FLOOR}% floor, g = {FLOOR-y:.2f}%/yr; to merely match the {SOV}% bond, g = {SOV-y:.2f}%/yr")
print("\nValue per share at the [E4-28] floor, at three growth assumptions (value = OE / (10% - g)):")
print("| window | g = 5.3% (the full realised decade rate) | g = 3.0% (hard-currency pricing ~1% + buyback ~1.1% + 1pt) | g = 0% (static) |")
print("|---|---|---|---|")
for k, oe in OE.items():
    row = []
    for g in (5.3, 3.0, 0.0):
        v = oe / ((FLOOR - g) / 100)      # $M
        row.append(f"${v/SH*1e6:.2f}")
    print(f"| {k} | {row[0]} | {row[1]} | {row[2]} |")
print(f"\ncheck: cap/OE(5-yr) = {CAP/2833:.1f}x ; price {PRICE} vs value at g=5.3%, 5-yr = ${2833/0.047/SH*1e6:.2f}")
