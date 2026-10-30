"""PM Q7 arithmetic under the v5 CONVENTION (Framework/THE FRAMEWORK v5.md, Q7, the range):
five-year mean owner cash (FY2021-2025, owner_cash.py), carried ten years at the growth shown on
aggregate owner cash, then zero nominal growth, discounted at the US Treasury 30-year par yield.
"""
r = 0.0566            # US Treasury 30-yr par yield, 10/05/2026 (tools/sources.py)
shares = 1558.613439  # millions, cover of 10-Q 0001628280-26-049493
price = 189.53        # 2026-10-05, tools/run.py aggregator quote, flagged
base_capex = 9373.0   # 5-yr mean owner cash, capex basis, USD M
base_da = 9153.0      # 5-yr mean owner cash, D&A basis
g_shown = -0.0106     # 2021->2025 aggregate owner cash, capex basis
g_long = 0.0428       # 2018->2025, shown for comparison only (outside the convention's window)
tax = 2737 / 13880    # FY2025 provision / pre-tax earnings, 10-K 0001628280-26-005939


def value(base, g, years=10):
    pv, c = 0.0, base
    for t in range(1, years + 1):
        c *= (1 + g)
        pv += c / (1 + r) ** t
    pv += (c / r) / (1 + r) ** years  # zero nominal growth after year ten
    return pv


cap = price * shares
print(f"market cap {cap:,.0f}M at ${price}")
for label, base in (("capex basis", base_capex), ("D&A basis", base_da)):
    for gl, g in (("no growth", 0.0), ("shown growth -1.06%", g_shown), ("2018-25 growth 4.28% (comparison only)", g_long)):
        v = value(base, g)
        print(f"{label:12} {gl:40} value {v:9,.0f}M  ${v/shares:7.2f}/sh")
print(f"owner cash yield at price: {base_capex/cap*100:.2f}% after tax")
print(f"effective tax rate FY2025 {tax*100:.1f}%; floor 10% pre-tax ~ {10*(1-tax):.2f}% after tax (CONVENTION)")
after = 0.10 * (1 - tax)
# expected return ~ owner cash yield + growth; price at which it equals the after-tax floor
for gl, g in (("no-growth ('cheap')", 0.0), ("central, midpoint of the ends ('fair')", g_shown / 2), ("comparison 4.28%", g_long)):
    p = base_capex / (after - g) / shares
    print(f"price at which {gl} clears the floor: ${p:.2f}")
# growth the price implies at the sovereign (perpetuity)
print(f"perpetual growth implied by price at {r*100:.2f}%: {(r - base_capex/cap)*100:.2f}%")
