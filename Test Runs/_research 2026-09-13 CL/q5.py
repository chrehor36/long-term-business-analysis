"""COMPUTATION — NOT A CLEARANCE. Yield, growth the price assumes at the ~10% floor, DCF engine, value range at the floor.
Arithmetic only; inputs from oe.py (filed cash-flow statements) and Step 0 (price, cover count, sovereign)."""
import os, sys
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources as S
HERE = os.path.dirname(os.path.abspath(__file__))
PRICE, SHARES = 86.80, 797_172_829
split = S.split_factor_after("CL", "2026-06-30")
CAP = PRICE * SHARES * split / 1e6
SOV, FLOOR = 0.0535, 0.10
BASES = {  # $M, from oe_out.md
    "10-yr 2016-25, capex end, ex working-capital release": 2680,
    "10-yr 2016-25, capex end": 2738,
    "5-yr 2021-25, capex end, ex working-capital release": 2763,
    "5-yr 2021-25, capex end (default window)": 2833,
    "3-yr 2023-25, capex end, ex working-capital release": 2879,
    "5-yr 2021-25, depreciation end": 2950,
    "3-yr 2023-25, capex end": 3269,
    "3-yr 2023-25, depreciation end": 3354,
    "TTM to 2026-06-30, capex end (single year)": 3680,
}
L = [f"split factor after 2026-06-30: {split}; cap US${CAP:,.1f}M", "",
     "| base | owner earnings $M | yield | points over 5.35% | perpetual growth for a 10% expectancy g=(r-y)/(1+y) | value at 10% and 3% growth, $/share | at 4% | at 5% |",
     "|---|---|---|---|---|---|---|---|"]
for k, oe in BASES.items():
    y = oe / CAP
    g = (FLOOR - y) / (1 + y)
    vals = [oe * (1 + gg) / (FLOOR - gg) / (SHARES / 1e6) for gg in (0.03, 0.04, 0.05)]
    L.append(f"| {k} | {oe:,} | {y:.2%} | {100*(y-SOV):+.2f} | {g:.2%} | ${vals[0]:.0f} | ${vals[1]:.0f} | ${vals[2]:.0f} |")

# DCF engine: growth for ten years, then 3% forever, discounted at the 10% floor; solve the 10-year rate that justifies the price
def pv(oe, g10, gt=0.03, r=FLOOR):
    v, x = 0.0, oe
    for t in range(1, 11):
        x *= 1 + g10
        v += x / (1 + r) ** t
    return v + x * (1 + gt) / (r - gt) / (1 + r) ** 10
L += ["", "| base | ten-year growth needed (then 3% forever, discounted at 10%) |", "|---|---|"]
for k, oe in BASES.items():
    lo, hi = -0.05, 0.30
    for _ in range(80):
        mid = (lo + hi) / 2
        if pv(oe, mid) < CAP:
            lo = mid
        else:
            hi = mid
    L.append(f"| {k} | {mid:.1%} a year |")
open(os.path.join(HERE, "q5_out.md"), "w", encoding="utf-8").write("\n".join(L))
print("\n".join(L))
