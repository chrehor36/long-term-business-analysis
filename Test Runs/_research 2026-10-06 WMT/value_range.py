"""Q7 arithmetic for WMT under the v5 CONVENTION (Q7): five-year mean owner cash after every real cost, carried at the growth
shown (capped by Q3) for ten years, then no growth (zero nominal), discounted at the 30-year Treasury.
COMPUTATION, NOT A CLEARANCE. Inputs from owner_cash.py (filed cash-flow statements), Step 0 (price, shares, sovereign)."""

R = 0.0566          # US Treasury 30-year par yield, 2026-10-05 (tools/sources.py)
SHARES = 7933.746   # millions, 10-Q cover, accession 0000104169-26-000154
PRICE = 105.07      # close 2026-10-05, aggregator (flagged)
TAX = 0.244         # FY2026 effective tax rate (10-K MD&A) to translate the ~10% pre-tax floor to after-tax owner cash
FLOOR_AT = 0.10 * (1 - TAX)


def value(c0, g, r, years=10):
    """PV of cash c0*(1+g)^t for t=1..years, then flat at year-10 level forever."""
    pv, c = 0.0, c0
    for t in range(1, years + 1):
        c *= 1 + g
        pv += c / (1 + r) ** t
    pv += (c / r) / (1 + r) ** years
    return pv


def irr(c0, g, price_total):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(c0, g, mid) > price_total:
            lo = mid
        else:
            hi = mid
    return mid


mcap = PRICE * SHARES
cases = [
    ("capex basis, no growth (bottom)", 9591, 0.0),
    ("capex basis, 2.8% shown growth (top)", 9591, 0.028),
    ("capex basis, 5.8% (op-income growth, the Q3 cap)", 9591, 0.058),
    ("D&A basis, no growth (variant)", 17663, 0.0),
    ("D&A basis, 5.8% (variant, capped)", 17663, 0.058),
    ("D&A basis, 18.4% shown (rejected, base year)", 17663, 0.184),
]
print(f"market cap at ${PRICE}: ${mcap/1000:,.1f}B; floor after tax {FLOOR_AT:.2%} (10% pre-tax at {TAX:.1%})")
for name, c0, g in cases:
    v = value(c0, g, R)
    e = irr(c0, g, mcap)
    fair = value(c0, g, FLOOR_AT) / SHARES
    print(f"{name:52s} value ${v/1000:8,.1f}B = ${v/SHARES:7.2f}/sh; expected return at price {e:.2%} after tax "
          f"({e/(1-TAX):.2%} pre-tax); price that earns the floor ${fair:7.2f}")
# what growth the price implies (ten years then flat) at the bond rate, and at the floor
for label, r in (("bond rate", R), ("floor", FLOOR_AT)):
    lo, hi = 0.0, 0.6
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(9591, mid, r) < mcap:
            lo = mid
        else:
            hi = mid
    print(f"growth for ten years the price implies on the capex-basis cash at the {label}: {mid:.1%}")
