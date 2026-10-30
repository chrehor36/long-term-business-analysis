"""THE PRICE LADDER — required Gate 6 output (Ruling 6).

Every run that reaches Gate 6 must answer three questions, not one:
  CHEAP   = IV x (1 - MOS)   the price at which you buy with a cushion
  FAIR    = IV               pay intrinsic value, earn exactly the discount rate
  CURRENT = the quote        and, critically, WHAT RETURN IT ACTUALLY DELIVERS

plus the reverse-DCF diagnostics that say what the current price already assumes.
"""
import math

SOV = 5.28

def dcf(base, g1, tgr, r, yrs=10):
    pv, oe = 0.0, base
    for t in range(1, yrs + 1):
        g = g1 + (tgr - g1) * (t - 1) / (yrs - 1)
        oe *= (1 + g)
        pv += oe / (1 + r) ** t
    return pv + (oe * (1 + tgr) / (r - tgr)) / (1 + r) ** yrs

def solve_g(target, base, tgr, r):
    lo, hi = -0.5, 1.0
    for _ in range(300):
        m = (lo + hi) / 2
        if dcf(base, m, tgr, r) < target: lo = m
        else: hi = m
    return (lo + hi) / 2

def irr(base, g1, tgr, mc):
    lo, hi = 0.0001, 1.0
    for _ in range(300):
        m = (lo + hi) / 2
        if dcf(base, g1, tgr, m) > mc: lo = m
        else: hi = m
    return (lo + hi) / 2

NAMES = {
  "TJX":  dict(px=157.34, sh=1104.7, base=4050.0, recent=4784.0, g1=0.09,
               moat="WIDE",   spread=3.0, caveat=0.0, mos=0.20,
               note="Gate 3 clean (CPSC flag is product safety, not financial). "
                    "g1 = slowest observed annual OE growth."),
  "DOV":  dict(px=204.62, sh=134.7,  base=1182.0, recent=1253.0, g1=0.04,
               moat="NARROW", spread=4.5, caveat=0.5, mos=0.20,
               note="Gate 3 caveat: combined Chair/CEO since 2024, LTI ROIC-gating "
                    "unverified. FY2024 OE excluded as base (contained a large gain). "
                    "g1 near the +2% four-year organic rate, rounded up."),
  "SBUX": dict(px=105.25, sh=1139.7, base=1322.0, recent=1322.0, g1=0.06,
               moat="NARROW", spread=4.5, caveat=0.5, mos=0.20,
               note="Gate 3 caveat: buyback record + negative book equity. NOTE: the "
                    "input rule (g1 = LOWER of recent OE growth or guidance) taken "
                    "literally gives a NEGATIVE g1, since OE fell $4,253M (FY21) to "
                    "$1,322M (FY25). 6% is a recovery assumption and is GENEROUS "
                    "relative to the rule — flagged, not hidden."),
}

for t, d in NAMES.items():
    r = (SOV + d["spread"] + d["caveat"]) / 100
    mc = d["px"] * d["sh"]
    iv_total = dcf(d["base"], d["g1"], 0.025, r)
    iv = iv_total / d["sh"]
    fair, cheap = iv, iv * (1 - d["mos"])
    print("=" * 74)
    print(f"{t}   price ${d['px']:,.2f}   mkt cap ${mc/1000:,.1f}B   "
          f"{mc/d['recent']:.1f}x most-recent OE")
    print(f"  discount rate = {SOV:.2f}% sovereign + {d['spread']:.1f}% {d['moat']} moat"
          f" + {d['caveat']:.1f}% Gate-3 caveat = {r*100:.2f}%")
    print(f"  base OE ${d['base']:,.0f}M · g1 {d['g1']*100:.0f}% fading to 2.5% over 10y")
    print(f"\n  THE PRICE LADDER")
    print(f"    CHEAP   ${cheap:8,.2f}   (IV x {1-d['mos']:.2f}) — buy with a cushion")
    print(f"    FAIR    ${fair:8,.2f}   (= IV) — pay value, earn the {r*100:.2f}% rate")
    print(f"    CURRENT ${d['px']:8,.2f}   — {d['px']/fair:.2f}x fair value"
          f"  ({'DISCOUNT' if d['px']<fair else 'PREMIUM'} {abs(d['px']/fair-1)*100:.0f}%)")
    ir = irr(d["base"], d["g1"], 0.025, mc)
    print(f"\n  WHAT THE CURRENT PRICE DELIVERS")
    print(f"    IRR at base-case growth: {ir*100:.2f}%   vs {SOV:.2f}% risk-free"
          f"  -> {'+' if ir*100>SOV else ''}{ir*100-SOV:.2f} pts of equity premium")
    gimp = solve_g(mc, d["base"], 0.025, r)
    print(f"    Implied year-1 OE growth to justify the price: {gimp*100:.1f}%"
          f"  (base case assumes {d['g1']*100:.0f}%)")
    y0 = d["recent"] / mc
    if y0 < SOV/100:
        for g in (0.06, 0.09, 0.12):
            n = math.log((SOV/100)/y0)/math.log(1+g)
            print(f"    Years for yield-on-cost to reach {SOV:.2f}% at {g*100:.0f}% growth: {n:.1f}")
            break
    print(f"\n  {d['note']}")
print("=" * 74)
