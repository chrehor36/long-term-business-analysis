"""COMPUTATION, NOT A CLEARANCE. Q7 range and the reporting fair price for CMC. $M except per share."""
SH = 110.624335          # cover shares, 10-Q 2026-05-31, as of 2026-06-25
PRICE = 64.77
r0 = 0.056               # Treasury 30y, 2026-10-09
T = 0.236
debt = 3428.920          # total debt at face incl. finance leases 192.0, 10-Q Note 8, 2026-05-31
cash = 559.759 + 3.458   # cash + restricted cash, 2026-05-31
lit = 373.476            # accrued contingent litigation-related loss, 2026-05-31
lit_at = lit * (1 - T)   # after the tax deduction on payment (CONVENTION of the run)
nd = debt - cash
nd_lit = nd + lit_at
# cycle base FY2017-FY2025 (nine years), unlevered owner cash after all capital spending, before purchases
P = 297.7; A = 147.8
# literal window FY2021-25
P_w = 363.3; A_w = 157.8
# depreciation variant (maintenance = D&A), cycle
P_dep = 405.8
# Foley on its own filed record: FY2024 audited, OCF 146.660 + cash interest (28.661 - 2.081 amortization) - capex 9.059 - SBC 2.885, taxed at T
foley_pre = 146.660 + (28.661 - 2.081) - 9.059 - 2.885
foley = foley_pre * (1 - T)
g_shown = 0.157; sales_g = 0.111; g = min(sales_g, r0)   # cap: absurdity cut to sales growth, never above the discount rate
def no_growth(P, r): return P / r
def growth(P, A, g, r):
    pv = sum((P - A) * (1 + g) ** t / (1 + r) ** t for t in range(1, 11))
    pv += P * (1 + g) ** 10 / r / (1 + r) ** 10
    return pv
def ps(ev, net): return (ev - net) / SH
print(f"net debt {nd:.1f}; with litigation after tax {nd_lit:.1f}; Foley owner cash pre-tax {foley_pre:.1f}, after CMC tax {foley:.1f}")
print(f"absurdity check: P x (1+{g_shown})^10 = {P*(1+g_shown)**10:.0f}, {P*(1+g_shown)**10/7798.5*100:.1f}% of FY2025 sales vs highest share 12.6% -> carried g = {g*100:.1f}%")
rows = []
for lab, r in (("at the sovereign 5.6%", r0), ("at the floor 10%", 0.10)):
    lo = no_growth(P, r) + no_growth(foley, r)
    hi = growth(P, A, g, r) + no_growth(foley, r)
    print(f"{lab}: EV no-growth {lo:.0f}  EV shown-growth {hi:.0f}  | per share (net debt + lit) {ps(lo, nd_lit):.2f} to {ps(hi, nd_lit):.2f}  | without litigation {ps(lo, nd):.2f} to {ps(hi, nd):.2f}")
    rows.append((lo, hi))
fair = (ps(rows[1][0], nd_lit) + ps(rows[1][1], nd_lit)) / 2
print(f"FAIR PRICE all-equity (avg of two ends at 10%): {fair:.2f}")
# literal window beside: growth meaningless -> no-growth alone
lw = no_growth(P_w, r0) + no_growth(foley, r0)
print(f"literal window FY2021-25, no-growth alone: EV {lw:.0f} -> {ps(lw, nd_lit):.2f}/sh; at 10%: {ps(no_growth(P_w,.10)+no_growth(foley,.10), nd_lit):.2f}")
# depreciation variant beside
for lab, r in (("5.6%", r0), ("10%", 0.10)):
    lo = no_growth(P_dep, r) + no_growth(foley, r); hi = growth(P_dep, A, g, r) + no_growth(foley, r)
    print(f"D&A variant at {lab}: {ps(lo, nd_lit):.2f} to {ps(hi, nd_lit):.2f}")
# organic pair beside (purchases left out, organic growth: filer reports none -> no growth)
print(f"organic pair (no organic rate reported -> no-growth): same as no-growth end {ps(rows[0][0], nd_lit):.2f}")
# equity-only: owner cash after current interest. Interest run rate: Q3 FY2026 interest expense 40.205 x4 plus capitalized 6.0 x4
int_now = (40.205 + 6.0) * 4
E = P + foley - int_now * (1 - T)
for lab, r in (("5.6%", r0), ("10%", 0.10)):
    lo = E / r - lit_at; hi = growth(E, A, g, r) - lit_at
    print(f"equity-only at {lab}: owner cash after interest {E:.1f}; {lo/SH:.2f} to {hi/SH:.2f}")
    if r == 0.10: print(f"FAIR PRICE equity-only: {((lo+hi)/2)/SH:.2f}")
# implied return at the price on the central top case: solve r where top value = market EV
mev = PRICE * SH + nd_lit
lo_r, hi_r = 0.001, 0.30
for _ in range(100):
    mid = (lo_r + hi_r) / 2
    v = growth(P, A, g, mid) + no_growth(foley, mid)
    if v > mev: lo_r = mid
    else: hi_r = mid
print(f"market EV {mev:.0f}; return at the price on the top case {mid*100:.2f}%")
