"""Q7 arithmetic for Visa under the v5 range CONVENTION (COMPUTATION, not a clearance).
Owner cash = OCF - stock pay - capex, filed statements (see the run file, Step 0). USD millions."""

oc = {2018: 11896, 2019: 11621, 2020: 9288, 2021: 13980, 2022: 17277, 2023: 18931, 2024: 17843, 2025: 20680}
base = sum(oc[y] for y in range(2021, 2026)) / 5          # five-year mean, CONVENTION
rate = 0.0566                                              # US Treasury 30-year par, 2026-10-05
shares = 1876.0                                            # class A equivalent, millions (Step 0)
price = 369.71                                             # aggregator close 2026-10-05, flagged
cap = price * shares

def cagr(a, b, n): return (b / a) ** (1 / n) - 1

g5 = cagr(oc[2021], oc[2025], 4)      # growth shown over the five-year window, aggregate
g7 = cagr(oc[2018], oc[2025], 7)      # full record read, FY2018 to FY2025
g6 = cagr(oc[2019], oc[2025], 6)      # from the last pre-pandemic year

def value(g, r=rate, b=base, years=10):
    """ten years at g, then zero nominal growth; discounted at r; cash at year end."""
    v, c = 0.0, b
    for t in range(1, years + 1):
        c *= 1 + g
        v += c / (1 + r) ** t
    v += (c / r) / (1 + r) ** years
    return v

def irr(g, p=cap):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(g, mid) > p: lo = mid
        else: hi = mid
    return mid

def implied_g(p=cap, r=rate):
    lo, hi = -0.05, 0.6
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(mid, r) < p: lo = mid
        else: hi = mid
    return mid

print("base (five-year mean owner cash, FY2021-25): %.0f" % base)
print("growth shown: 2021-25 %.2f%%; 2018-25 %.2f%%; 2019-25 %.2f%%" % (100 * g5, 100 * g7, 100 * g6))
print("market cap at $%.2f x %.0fM = %.0f" % (price, shares, cap))
rows = [("no growth", 0.0), ("growth = discount rate 5.66%", rate), ("full record 2018-25", g7),
        ("from 2019", g6), ("five-year shown 2021-25", g5)]
for name, g in rows:
    v = value(g)
    print("%-32s g=%6.2f%%  value %9.0f  per share $%7.2f  IRR at price %.2f%%" % (name, 100 * g, v, v / shares, 100 * irr(g)))
print("growth the price implies at %.2f%%: %.2f%% a year for ten years" % (100 * rate, 100 * implied_g()))

tax = 0.171   # GAAP effective tax rate FY2025 (10-K FY2025, Item 7 reconciliation, 17.1%)
floor_at = 0.10 * (1 - tax)
print("floor: 10%% pre-tax = %.2f%% after tax at %.1f%%" % (100 * floor_at, 100 * tax))
print("growth needed for the price to earn the floor: %.2f%%" % (100 * implied_g(cap, floor_at)))
for name, g in rows:
    print("  price at which %-32s returns the floor: $%7.2f" % (name, value(g, floor_at) / shares))
for lbl, at in (("row's own translation, 6.5% after tax", 0.065), ("7% after tax", 0.07)):
    print("  [%s] cheap $%.2f, top-case $%.2f" % (lbl, value(0, at) / shares, value(g5, at) / shares))
print("range width (top/bottom): %.2f to 1" % (value(g5) / value(0)))
