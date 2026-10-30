# COMPUTATION, NOT A CLEARANCE. Q7's range convention applied to Sumitomo's owner cash (scripts/owner_cash.py output).
R = 0.04136          # 30y JGB, MOF, 2026-10-08
FLOOR = 0.10         # floor CONVENTION (about ten percent), used for the fair price
SH = 4_738_846_768   # post-split shares outstanding, 2026-06-30
ND_JUN = 3_713.5     # net interest-bearing debt, JPY bn, 2026-06-30 (Tanshin; leases excluded, lease payments are inside owner cash)
ND_MAR = 3_147.2     # 2026-03-31 (AFR), before the Sumisho Air Lease acquisition
PRICE = 1708.0; FX = 158.68
def pv(c, g, r, years=10):
    """C grows at g for `years` years (first year = c*(1+g)), then flat forever, discounted at r."""
    s = 0.0; x = c
    for t in range(1, years + 1):
        x = x * (1 + g); s += x / (1 + r) ** t
    return s + (x / r) / (1 + r) ** years
def case(label, c, g, nd):
    lo_ev, hi_ev = pv(c, 0.0, R), pv(c, g, R)
    lo, hi = (lo_ev - nd) * 1e9 / SH, (hi_ev - nd) * 1e9 / SH
    f_lo, f_hi = pv(c, 0.0, FLOOR), pv(c, g, FLOOR)
    fair = ((f_lo + f_hi) / 2 - nd) * 1e9 / SH
    # expected return at the price for each end (IRR on EV = price*SH + nd)
    ev = PRICE * SH / 1e9 + nd
    def irr(gg):
        a, b = 0.0001, 0.5
        for _ in range(200):
            m = (a + b) / 2
            if pv(c, gg, m) > ev: a = m
            else: b = m
        return m
    print(f"{label}\n  owner cash {c:.1f} bn/yr, growth {g*100:.2f}% for 10y then 0, net debt {nd:.1f} bn")
    print(f"  range at {R*100:.3f}%: EV {lo_ev:,.0f} to {hi_ev:,.0f} bn; per share JPY {lo:,.0f} to {hi:,.0f}"
          f" (per ADS ${lo/FX:.2f} to ${hi/FX:.2f}); width {'n/a' if lo<=0 else f'{hi/lo:.2f} to 1'}")
    print(f"  fair price (each end at 10%, averaged, less net debt): JPY {fair:,.0f} (per ADS ${fair/FX:.2f})")
    print(f"  expected return at JPY {PRICE:,.0f}: no-growth {irr(0.0)*100:.1f}%, growth case {irr(g)*100:.1f}%\n")
    return lo, hi, fair
print("== CENTRAL: organic pair (serial acquirer: net purchases 1,213 > half of 1,546 before purchases), all-equity basis")
case("A. owner cash before purchases + after-tax net interest; growth: shown 74.4% (halves) is absurd -> cap (f): own sales growth FY2021-25 7.5%/yr, never above the discount rate -> 4.136%", 329.7, R, ND_JUN)
print("== beside it")
case("B. equity-only: owner cash before purchases, after interest; same growth; no net debt subtracted", 309.2, R, 0.0)
case("C. default pair: acquisitions deducted (incl. SCSK minority buyout), total growth credited at the same cap", 87.1, R, ND_JUN)
case("D. working capital removed as aberrational (literal window shown in A)", 434.1, R, ND_JUN)
case("E. A with the aircraft-leasing deal excluded both ways (net debt at 2026-03-31)", 329.7, R, ND_MAR)
case("F. A with the halves growth of sales (5.9%/yr) also capped at the discount rate: identical to A", 329.7, R, ND_JUN)
