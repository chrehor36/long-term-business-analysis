"""Q7 arithmetic under the v5 CONVENTION (COMPUTATION - NOT A CLEARANCE until Q1-Q4 and the STOPs before Q7 are IN).
Value = sum over years 1..10 of C(1+g)^t/(1+r)^t + terminal C(1+g)^10 / r / (1+r)^10 (zero nominal growth after ten years).
Checked against the HUBB run of 2026-10-05 (C=639.8, r=5.63%, g=7.2% gives 20,148)."""
R = 0.0566          # US Treasury 30-year par yield, 2026-10-05
C = 14086.6         # five-year mean owner cash FY2022-FY2026, $M (capex variant)
C_DA = 14746.2      # D&A variant
SH = 2391.075       # common-equivalent shares, M (2,324.433 cover + 66.642 ESOP convertible preferred)
PRICE = 145.94

def value(c, g, r=R, n=10):
    pv = sum(c * (1 + g) ** t / (1 + r) ** t for t in range(1, n + 1))
    return pv + c * (1 + g) ** n / r / (1 + r) ** n

def irr(c, g, price_total, n=10):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(c, g, mid, n) > price_total:
            lo = mid
        else:
            hi = mid
    return mid

def price_for(c, g, target):
    return value(c, g, target) / SH

print("check HUBB:", round(value(639.8, 0.072, 0.0563)))
mcap = SH * PRICE
g_shown = (14623 / 13039) ** 0.25 - 1
g_long = (14623 / 9018) ** (1 / 9) - 1
print(f"growth shown FY2022-26 {g_shown:.2%}; FY2017-26 {g_long:.2%}")
for label, c in (("capex", C), ("D&A", C_DA)):
    for g in (0.0, g_shown, g_long, R):
        v = value(c, g)
        print(f"{label:5} g={g:6.2%} value {v:10,.0f} $M  per share {v / SH:7.2f}  "
              f"return at price {irr(c, g, mcap):6.2%}")
# growth the price implies at the bond rate
lo, hi = -0.1, 0.3
for _ in range(200):
    mid = (lo + hi) / 2
    if value(C, mid) < mcap:
        lo = mid
    else:
        hi = mid
print(f"growth the price implies at {R:.2%}: {mid:.2%}")
# the floor: about 10% pre-tax; tax rate 20.8% (FY2026 effective, 10-K)
TAX = 0.208
floor_after = 0.10 * (1 - TAX)
print(f"floor after tax {floor_after:.2%}")
for g in (0.0, g_shown):
    print(f"price at which g={g:.2%} returns the floor: {price_for(C, g, floor_after):.2f}")
# growth needed for the price to return the floor
lo, hi = -0.1, 0.4
for _ in range(200):
    mid = (lo + hi) / 2
    if value(C, mid, floor_after) < mcap:
        lo = mid
    else:
        hi = mid
print(f"growth needed for the floor at the price: {mid:.2%}")
# buyback prices paid against the range: FY2024-26 from the statements of shareholders' equity
for fy, sh, usd in ((2024, 31.877, 5014), (2025, 38.552, 6517), (2026, 33.437, 5029)):
    print(f"FY{fy} average repurchase price ${usd / sh:.2f}")
g_mid = g_shown / 2
print(f"central case g={g_mid:.2%}: value per share {value(C, g_mid) / SH:.2f}; price at which it returns the floor "
      f"{price_for(C, g_mid, floor_after):.2f}; return at price {irr(C, g_mid, mcap):.2%}")
