"""Q7 arithmetic for the PNR run, 2026-10-10. COMPUTATION from filed statements; conventions as named in the run file.
All $M. Sources: filed cash-flow statements in the 10-Ks FY2021 (2019-2021), FY2023 (2021-2023), FY2025 (2023-2025),
10-Q Q2 2026 (balance sheet 2026-06-30). Interest = cash paid for interest, net (supplemental disclosure)."""
R = 0.056          # UST 30y par yield 2026-10-09 (Treasury)
FLOOR = 0.10       # Q7 floor CONVENTION, about ten percent
TAX = 0.14         # company effective rate, 14.1% FY2025 / 13.0% FY2024 (used only to un-lever cash interest)
SHARES = 159.63795 # cover, 10-Q Q2 2026
PRICE = 52.47
NETDEBT = 1606.0 - 91.8   # LT debt less cash, 2026-06-30 (no short-term borrowings on the face); leases left out
TACO = 1425.0             # stated subsequent event (10-Q note 16), agreed not closed; shown beside only
#        OCF     SBC   capex  intpaid  acq(net of business sales)
D = {2019:(345.2, 21.4, 58.5, 33.7, 287.8-15.3),
     2020:(574.2, 20.3, 62.2, 41.0, 58.0),
     2021:(613.6, 29.8, 60.2, 29.9, 338.5-1.4),
     2022:(364.3, 24.9, 85.2, 57.0, 1580.9),
     2023:(620.8, 29.1, 76.0,146.4, 0.6),
     2024:(766.9, 39.7, 74.4,145.6, 108.0),
     2025:(814.8, 37.0, 68.8, 79.8, 292.1)}
DEP = {2021:51.2, 2022:54.1, 2023:59.5, 2024:60.3, 2025:59.6}
CORE = [0.062, -0.049, -0.004, 0.019]   # core sales growth 2022..2025 (filer's own organic measure)
def uoc(y):  o,s,c,i,a = D[y]; return o + i*(1-TAX) - s - c   # unlevered owner cash, all capex
def eoc(y):  o,s,c,i,a = D[y]; return o - s - c                # equity owner cash (after interest)
def acq(y):  return D[y][4]
def pv(base, g, r, n=10):
    """base grows at g for n years, then flat (zero nominal growth) forever; discounted at r."""
    tot, cf = 0.0, base
    for t in range(1, n+1):
        cf *= (1+g); tot += cf/(1+r)**t
    return tot + (cf/r)/(1+r)**n
def cagr(a, b, n): return (b/a)**(1/n) - 1
W = [2021, 2022, 2023, 2024, 2025]
def show(label, base, g, debt, per=SHARES):
    lo, hi = sorted([pv(base, 0.0, R), pv(base, g, R)])
    f_lo, f_hi = pv(base, 0.0, FLOOR), pv(base, g, FLOOR)
    fair = (f_lo + f_hi)/2
    print(f"{label}\n   base {base:7.1f}  growth {g*100:5.2f}%  whole-business range {lo:8.0f} to {hi:8.0f} (width {hi/lo if lo>0 else float('nan'):.2f}x)"
          f"\n   less net debt {debt:6.0f}: per share ${(lo-debt)/per:6.2f} to ${(hi-debt)/per:6.2f} against ${PRICE}"
          f"\n   fair (midpoint case at the {FLOOR*100:.0f}% floor): whole {fair:8.0f}, per share ${(fair-debt)/per:6.2f}")
    return lo, hi, fair
print("YEAR  UOC   EOC   ACQ   dep-variant(EOC with depreciation for capex)")
for y in sorted(D):
    dv = (D[y][0]-D[y][1]-DEP[y]) if y in DEP else float('nan')
    print(y, f"{uoc(y):7.1f} {eoc(y):7.1f} {acq(y):7.1f} {dv:7.1f}")
au = sum(uoc(y) for y in W)/5; ae = sum(eoc(y) for y in W)/5; aa = sum(acq(y) for y in W)/5
gu = cagr(uoc(2021), uoc(2025), 4); ge = cagr(eoc(2021), eoc(2025), 4)
org = 1.0
for c in CORE: org *= (1+c)
go = org**(1/4) - 1
print(f"\nwindow FY2021-FY2025: avg UOC {au:.1f}, avg EOC {ae:.1f}, avg acquisitions {aa:.1f}")
print(f"total growth UOC {gu*100:.2f}%/yr, EOC {ge*100:.2f}%/yr; organic (core sales 2022-2025) {go*100:.2f}%/yr")
print(f"price {PRICE}, market cap {PRICE*SHARES:.0f}, net debt {NETDEBT:.1f}, EV {PRICE*SHARES+NETDEBT:.0f}")
print("\n== CENTRAL: all-equity basis, default pair (acquisitions deducted, total growth credited)")
c = show("all-equity, default pair", au-aa, gu, NETDEBT)
show("  same, Taco financing added to net debt (beside)", au-aa, gu, NETDEBT+TACO)
print("\n== BESIDE: equity-only basis, default pair (owner cash after interest against market value)")
show("equity-only, default pair", ae-aa, ge, 0.0)
print("\n== BESIDE: organic pair (acquisitions left out, only organic growth credited)")
show("all-equity, organic pair", au, go, NETDEBT)
show("  same, Taco financing added (beside)", au, go, NETDEBT+TACO)
show("equity-only, organic pair", ae, go, 0.0)
print("\n== BESIDE: depreciation for capex (all-equity, organic pair)")
du = sum((D[y][0]-D[y][1]-DEP[y]) + D[y][3]*(1-TAX) for y in W)/5
show("all-equity, organic pair, depreciation variant", du, go, NETDEBT)
print("\n== BESIDE: seven-year span FY2019-FY2025 (trough 2019, boom 2020-22, fall 2023), not the convention's window")
S = [2019,2020,2021,2022,2023,2024,2025]
a7 = sum(uoc(y) for y in S)/7; q7a = sum(acq(y) for y in S)/7
h1 = sum(uoc(y) for y in S[:3])/3; h2 = sum(uoc(y) for y in S[4:])/3
g7 = (h2/h1)**(1/4) - 1
print(f"   avg UOC {a7:.1f}, avg acq {q7a:.1f}; halves {h1:.1f} -> {h2:.1f}, growth between halves {g7*100:.2f}%/yr")
show("all-equity, seven-year, acquisitions deducted", a7-q7a, g7, NETDEBT)
show("all-equity, seven-year, organic", a7, go, NETDEBT)
print("\n== TTM to 2026-06-30 (direction only): OCF 814.8-567.7+504.4, capex 68.8-27.7+37.4, SBC 37.0-21.2+19.5")
ttm_e = (814.8-567.7+504.4) - (68.8-27.7+37.4) - (37.0-21.2+19.5)
print(f"   equity owner cash TTM {ttm_e:.1f}")
# implied: what growth does the price need, all-equity, organic base, at the sovereign
ev = PRICE*SHARES + NETDEBT
lo_g, hi_g = -0.5, 0.5
for _ in range(100):
    m = (lo_g+hi_g)/2
    if pv(au, m, R) > ev: hi_g = m
    else: lo_g = m
print(f"\nprice implies growth of {m*100:.2f}%/yr for ten years on the organic base ({au:.1f}) at {R*100:.2f}%")
# expected return at the price, organic base, no growth (perpetuity yield)
print(f"owner-cash yield at the price, organic base: {au/ev*100:.2f}% (all-equity); {ae/(PRICE*SHARES)*100:.2f}% (equity-only)")
print(f"after acquisitions: {(au-aa)/ev*100:.2f}% (all-equity)")
