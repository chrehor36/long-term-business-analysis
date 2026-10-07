"""COMPUTATION — NOT A CLEARANCE. The v5 Q7 CONVENTION construction, run for the record only (the run closed at Q5).
Cash input: five-year mean owner cash FY2021-FY2025 (owner_cash.py). Carried ten years at the growth shown, then zero
nominal growth, discounted at the US Treasury 30-year par yield of 2026-10-05. Ends: no growth and shown growth.
Sensitivities (not the convention's ends) use the FY2020-based growth and the twelve months to June 2026 as the base."""
RATE = 0.0566
SHARES = 14594.18          # millions, 10-Q cover 2026-07-17
PRICE = 332.89             # aggregator quote 2026-10-05
MEAN5 = 91845.0
TTM = 122977.0

def pv(base, g, r=RATE, years=10):
    total, cf = 0.0, base
    for t in range(1, years + 1):
        cf *= (1 + g)
        total += cf / (1 + r) ** t
    total += (cf / r) / (1 + r) ** years   # zero nominal growth after year ten
    return total

def implied_return(base, g, price_total, years=10):
    lo, hi = 0.0001, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(base, g, mid, years) > price_total: lo = mid
        else: hi = mid
    return mid

mcap = PRICE * SHARES
print(f"market cap {mcap:,.0f}M")
for label, base, g in (("no growth, five-year mean", MEAN5, 0.0),
                       ("shown growth FY2021-25 0.25%, five-year mean", MEAN5, 0.0025),
                       ("sensitivity: FY2020-25 growth 5.24%, five-year mean", MEAN5, 0.0524),
                       ("sensitivity: FY2020-25 growth 5.24%, TTM base", TTM, 0.0524)):
    v = pv(base, g)
    print(f"{label}: value {v:,.0f}M = ${v/SHARES:,.2f} a share; expected return at the price {implied_return(base, g, mcap)*100:.2f}%")
# the price at which the shown-growth case clears a 10% floor ("fair") and no-growth clears it ("cheap")
for label, g in (("fair (shown growth at 10%)", 0.0025), ("cheap (no growth at 10%)", 0.0)):
    print(f"{label}: ${pv(MEAN5, g, 0.10)/SHARES:,.2f} a share")
