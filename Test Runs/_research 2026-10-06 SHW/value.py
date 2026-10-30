"""Q7 arithmetic for SHW under the v5 CONVENTION (Q7): five-year mean owner cash, carried at a growth rate for ten
years, then zero nominal growth, discounted at the long government rate. COMPUTATION, not a clearance. USD millions."""
R = 0.0566                 # US Treasury 30-year par yield, 2026-10-05 (tools/sources.py)
SH = 242.758151            # shares, 10-Q cover as of 2026-06-30 (0000089800-26-000049)
PRICE = 318.46             # close 2026-10-05, aggregator (tools/run.py), flagged
BASE = 1921.5              # five-year mean owner cash 2021-2025, all capex (owner.py)
BASE_DEP = 2384.5          # depreciation variant (owner.py)
TAX = 0.231                # effective tax rate 2025, 10-K FY2025 MD&A
FLOOR_PRE = 0.10           # CONVENTION: about ten percent pre-tax
FLOOR_AT = FLOOR_PRE * (1 - TAX)


def value(cf0, g, r=R, years=10):
    v, cf = 0.0, cf0
    for t in range(1, years + 1):
        cf *= (1 + g)
        v += cf / (1 + r) ** t
    return v + (cf / r) / (1 + r) ** years


def solve(f, lo, hi, target):
    for _ in range(200):
        mid = (lo + hi) / 2
        if (f(mid) - target) * (f(lo) - target) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


mcap = PRICE * SH
print(f"market cap {mcap:,.0f}  floor after tax {FLOOR_AT*100:.2f}%")
print(f"{'case':<44}{'value $M':>10}{'per share':>11}{'dep-variant/share':>19}")
for name, g in [("no growth (bottom)", 0.0), ("1.3% (five-year means)", 0.013),
                ("5.66% for ten years (strict cap)", R), ("6.0% for ten years (top, 2018-2025)", 0.060),
                ("9.0% (2021-2025 point, rejected)", 0.0896)]:
    v = value(BASE, g); vd = value(BASE_DEP, g)
    print(f"{name:<44}{v:>10,.0f}{v/SH:>11.2f}{vd/SH:>19.2f}")

gi = solve(lambda g: value(BASE, g), 0.0, 0.40, mcap)
print(f"growth for ten years the price implies at {R*100:.2f}%: {gi*100:.2f}%")
gf = solve(lambda g: value(BASE, g, FLOOR_AT), 0.0, 0.60, mcap)
print(f"growth for ten years needed to earn the floor ({FLOOR_AT*100:.2f}% after tax) at the price: {gf*100:.2f}%")
for g in (0.0, 0.06):
    irr = solve(lambda r: value(BASE, g, r), 0.0001, 0.5, mcap)
    irrd = solve(lambda r: value(BASE_DEP, g, r), 0.0001, 0.5, mcap)
    print(f"expected return at the price, growth {g*100:.1f}%: {irr*100:.2f}% after tax ({irr/(1-TAX)*100:.2f}% pre-tax);"
          f" dep variant {irrd*100:.2f}% ({irrd/(1-TAX)*100:.2f}% pre-tax)")
fair = value(BASE, 0.06, FLOOR_AT) / SH
cheap = value(BASE, 0.0, FLOOR_AT) / SH
print(f"fair price (top case returns the floor): {fair:.2f};  cheap price (no growth returns the floor): {cheap:.2f}")
print(f"dep variant: fair {value(BASE_DEP, 0.06, FLOOR_AT)/SH:.2f}; cheap {value(BASE_DEP, 0.0, FLOOR_AT)/SH:.2f}")
adj = BASE - 85 * (1 - TAX)
print(f"sensitivity: base less 2026 interest increase (85 pre-tax, MD&A) = {adj:.1f}: no growth {value(adj,0)/SH:.2f}, 6% {value(adj,0.06)/SH:.2f}")
