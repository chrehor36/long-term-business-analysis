"""TJX REFRESH RUN — 2026-08-26. Book One + Book Two + Price Ladder (Ruling 6).

Discount rate = Aesop certainty spread (Ruling 4 as amended by 4-A), NOT WACC/beta.
Terminal value = E2-22 growing-coupon reading. Bare sovereign never a perpetuity input.
"""
import math

SOV   = 5.19          # 30-yr, 2026-08-26, Yahoo ^TYX; FRED DGS30 matches through 08-24
SPREAD= 3.00          # WIDE moat, Ruling 4-A floor
CAVEAT= 0.00          # Gate 3 clean (CPSC flag = product safety, not financial candor)
R     = (SOV + SPREAD + CAVEAT) / 100
PRICE = 137.75        # 2026-08-26 close, Yahoo (aggregator, live price only)
SH_DIL= 1117.0        # diluted WAS, Q2 FY27 8-K filed 2026-08-19 (conservative)
SH_EST= 1100.0        # est. actual o/s: 1,104.7M cover 2026-05-29 less 5.1M Q2 buyback
MOS   = 0.20          # Ruling 5 (35%) is PROPOSED, not in force

# ---- OE tier tables, three methods -----------------------------------------
# XBRL 10-K facts, $M
NI   = {2021:  90, 2022:3283, 2023:3498, 2024:4474, 2025:4864, 2026:5494}
DA   = {2021: 871, 2022: 868, 2023: 887, 2024: 964, 2025:1104, 2026:1247}
CAPX = {2021: 568, 2022:1045, 2023:1457, 2024:1722, 2025:1918, 2026:1957}
WCCF = {2021:3168, 2022:-1572, 2023:-695, 2024: 401, 2025:  58, 2026:-301}  # cash effect

YRS = sorted(NI)
A = {y: NI[y]+DA[y]-CAPX[y]            for y in YRS}          # prior-run method (no WC)
B = {y: NI[y]+DA[y]-CAPX[y]+WCCF[y]    for y in YRS}          # raw annual WC swing
WC_NORM = -sum(WCCF[y] for y in (2023,2024,2025,2026))/4      # required WC increment
C = {y: NI[y]+DA[y]-CAPX[y]-WC_NORM    for y in YRS}          # normalized (Buffett 1986)

print("="*78)
print("GATE 4 — OWNER EARNINGS TIER TABLE, THREE METHODS ($M)")
print("="*78)
print(f"{'FY':>6}{'A: no WC':>12}{'B: raw dWC':>12}{'C: normalized':>15}")
for y in YRS:
    print(f"{y:>6}{A[y]:>12,.0f}{B[y]:>12,.0f}{C[y]:>15,.0f}")
print(f"\n  required WC increment (4-yr post-COVID avg) = ${WC_NORM:,.0f}M/yr")
print(f"  LOWEST TIER   A ${min(A.values()):,.0f}  |  B ${min(B.values()):,.0f}"
      f"  |  C ${min(C.values()):,.0f}")

# ---- Book One: the Statute ---------------------------------------------------
mc_dil = PRICE*SH_DIL/1000; mc_est = PRICE*SH_EST/1000
print("\n"+"="*78)
print(f"BOOK ONE — THE STATUTE   hurdle = sovereign {SOV:.2f}% (large cap, no size premium)")
print("="*78)
print(f"  market cap ${mc_dil:,.1f}B (diluted) / ${mc_est:,.1f}B (est. o/s) @ ${PRICE}")
for lbl, tab in (("A no-WC", A), ("B raw dWC", B), ("C normalized", C)):
    lo = min(tab.values()); rec = tab[2026]
    print(f"  {lbl:14s} lowest ${lo:>6,.0f}M -> {lo/(mc_dil*1000)*100:5.2f}%   "
          f"most-recent ${rec:>6,.0f}M -> {rec/(mc_dil*1000)*100:5.2f}%   "
          f"both {'FAIL' if rec/(mc_dil*1000)*100 < SOV else 'PASS'}")

# ---- Book Two ----------------------------------------------------------------
def dcf(base, g1, tgr, r, yrs=10):
    pv, oe = 0.0, base
    for t in range(1, yrs+1):
        g = g1 + (tgr-g1)*(t-1)/(yrs-1)
        oe *= (1+g)
        pv += oe/(1+r)**t
    return pv + (oe*(1+tgr)/(r-tgr))/(1+r)**yrs

def solve_g(target, base, tgr, r):
    lo, hi = -0.5, 1.0
    for _ in range(200):
        m=(lo+hi)/2
        if dcf(base,m,tgr,r) < target: lo=m
        else: hi=m
    return (lo+hi)/2

def irr(base, g1, tgr, mc):
    lo, hi = 0.0001, 1.0
    for _ in range(200):
        m=(lo+hi)/2
        if dcf(base,g1,tgr,m) > mc: lo=m
        else: hi=m
    return (lo+hi)/2

# g1 anchor: LOWER of recent OE growth or guidance (strict input rule)
# guidance FY27 adj diluted EPS $5.15-5.20 vs FY26 actual $4.87 = +5.75% to +6.78%/sh
# less ~1.0%/yr share shrink (1,128 -> 1,117 diluted WAS YoY) => total-OE growth
G_GUIDE = (5.15/4.87 - 1) - 0.010
G_RECENT = 0.09
G1 = min(G_GUIDE, G_RECENT)
print("\n"+"="*78)
print("BOOK TWO — AESOP CERTAINTY SPREAD")
print("="*78)
print(f"  rate = {SOV:.2f}% sovereign + {SPREAD:.2f}% WIDE moat + {CAVEAT:.2f}% caveat = {R*100:.2f}%")
print(f"  g1 anchor: guidance-implied {G_GUIDE*100:.2f}%  vs recent-OE {G_RECENT*100:.1f}%"
      f"  -> LOWER = {G1*100:.2f}%   (guidance NOW VERIFIED, 8-K 2026-08-19)")

SCEN = {
  "BEAR": (B[2023], 0.02, 0.020, "lowest clean post-COVID tier (method B), inflation-only growth"),
  "BASE": (A[2025], G1,   0.025, "FY2025 tier, method A (comparability with 07-31 run)"),
  "BASE-C":(C[2025], G1,  0.025, "FY2025 tier, method C (WC-corrected)"),
  "BULL": (A[2026], 0.09, 0.030, "latest tier, growth at the old 9% anchor"),
}
print(f"\n{'':8}{'baseOE$M':>10}{'g1':>7}{'TGR':>7}{'IV/sh dil':>11}{'IV/sh est':>11}   rationale")
ivs={}
for k,(b,g1,tgr,rat) in SCEN.items():
    ev = dcf(b,g1,tgr,R)
    ivs[k]=(ev/SH_DIL, ev/SH_EST)
    print(f"{k:8}{b:>10,.0f}{g1*100:>6.2f}%{tgr*100:>6.1f}%{ev/SH_DIL:>11,.2f}{ev/SH_EST:>11,.2f}   {rat}")

FAIR  = ivs["BASE"][0]
CHEAP = FAIR*(1-MOS)
print(f"\n  FAIR  (=IV, base)         ${FAIR:,.2f}")
print(f"  CHEAP (IV x {1-MOS:.2f})           ${CHEAP:,.2f}")
print(f"  CURRENT                   ${PRICE:,.2f} = {PRICE/FAIR:.2f}x fair "
      f"({'premium' if PRICE>FAIR else 'discount'} {abs(PRICE/FAIR-1)*100:.0f}%)")

# ---- sensitivity grid (dispositive per Ruling 4-A) ---------------------------
print("\nSENSITIVITY GRID — IV/share (diluted), base OE & g1, varying r and TGR")
b,g1,_,_ = SCEN["BASE"]
print(f"{'r / TGR':>10}"+"".join(f"{t*100:>10.1f}%" for t in (0.020,0.025,0.030)))
cheap_ok=fair_ok=n=0
for rr in (0.0619,0.0719,0.0819,0.0919):
    row=f"{rr*100:>9.2f}%"
    for tgr in (0.020,0.025,0.030):
        iv=dcf(b,g1,tgr,rr)/SH_DIL
        n+=1
        if PRICE <= iv*(1-MOS): cheap_ok+=1
        if PRICE <= iv:         fair_ok+=1
        row+=f"{iv:>11,.0f}"
    print(row)
print(f"\n  cells where price <= CHEAP (IV x 0.80): {cheap_ok}/{n}"
      f"  -> majority? {'YES' if cheap_ok>n/2 else 'NO'}")
print(f"  cells where price <= FAIR  (IV):        {fair_ok}/{n}"
      f"  -> majority? {'YES' if fair_ok>n/2 else 'NO'}")

# ---- reverse-DCF diagnostics (Ruling 6) --------------------------------------
mc = PRICE*SH_DIL
print("\n"+"="*78)
print("REVERSE-DCF DIAGNOSTICS")
print("="*78)
ir = irr(b, g1, 0.025, mc)
print(f"  IRR at current price on base-case growth: {ir*100:.2f}%  vs sovereign {SOV:.2f}%"
      f"  = {ir*100-SOV:+.2f} points of equity premium")
gi = solve_g(mc, b, 0.025, R)
print(f"  Implied year-1 OE growth to justify ${PRICE}: {gi*100:.2f}%"
      f"   (base case assumes {g1*100:.2f}%)")
y0 = A[2026]/mc
print(f"  Current earnings yield on most-recent tier (method A): {y0*100:.2f}%")
for g in (0.0475, 0.09):
    if y0 < SOV/100:
        print(f"  Years for yield-on-cost to reach {SOV:.2f}% at {g*100:.2f}% growth: "
              f"{math.log((SOV/100)/y0)/math.log(1+g):.1f}")

# ---- what price makes each test pass ----------------------------------------
print("\n"+"="*78)
print("THE ACTIONABLE LINES")
print("="*78)
print(f"  CHEAP  (full size)     ${CHEAP:,.2f}")
print(f"  FAIR   (starter)       ${FAIR:,.2f}")
px_stat = A[2026]/(SOV/100)/SH_DIL
print(f"  Book One pass price (most-recent tier / {SOV:.2f}%): ${px_stat:,.2f}")
px_lo = min(A.values())/(SOV/100)/SH_DIL
print(f"  Book One pass price (LOWEST tier, as anchored):     ${px_lo:,.2f}")
print("="*78)
