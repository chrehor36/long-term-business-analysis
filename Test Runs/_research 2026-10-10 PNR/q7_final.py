"""Q7 arithmetic for the PNR run, 2026-10-10, under Q7's range convention as amended 2026-10-10 (specific (c): acquisition
spending stops after year ten; (f): the sales-growth cut; the floor tested first; Part VII fair price = the two end cases
valued at ten percent, averaged). COMPUTATION from the filed statements; inputs checked line by line against the filed
cash-flow statements of the FY2021, FY2023 and FY2025 10-Ks and the Q2 2026 10-Q. All $M.
Supersedes q7.py (the earlier session's draft, written before Q6 and before the 2026-10-10 amendments were applied)."""
R, FLOOR, TAX = 0.056, 0.10, 0.14       # UST 30y 2026-10-09 (Treasury); floor CONVENTION; company effective rate (unlevering cash interest only)
SHARES, PRICE = 159.63795, 52.47
NETDEBT = 1606.0 - 91.8                 # total debt less cash, 2026-06-30 (10-Q); no finance leases on the face; operating leases left out
TACO = 1425.0                           # signed 2026-07-27, not closed; price paid from cash and ~$1.4B new debt (10-Q note 16)
#        OCF     SBC   capex  intpaid  acquisitions net of business sales     sales
D = {2019:(345.2, 21.4, 58.5, 33.7, 287.8-15.3, 2957.0),
     2020:(574.2, 20.3, 62.2, 41.0, 58.0,       3018.0),
     2021:(613.6, 29.8, 60.2, 29.9, 338.5-1.4,  3765.0),
     2022:(364.3, 24.9, 85.2, 57.0, 1580.9,     4122.0),
     2023:(620.8, 29.1, 76.0,146.4, 0.6,        4104.5),
     2024:(766.9, 39.7, 74.4,145.6, 108.0,      4082.8),
     2025:(814.8, 37.0, 68.8, 79.8, 292.1,      4176.0)}
DEP = {2021:51.2, 2022:54.1, 2023:59.5, 2024:60.3, 2025:59.6}
CORE = [0.062, -0.049, -0.004, 0.019]   # filer's core sales growth 2022..2025
uoc = lambda y: D[y][0] + D[y][3]*(1-TAX) - D[y][1] - D[y][2]   # all-equity owner cash, all capex
eoc = lambda y: D[y][0] - D[y][1] - D[y][2]                     # equity-only owner cash (after interest)
acq = lambda y: D[y][4]
def pv(net, gross, g, r, n=10):
    """years 1..n: net*(1+g)^t (owner cash less purchases); after n: gross*(1+g)^n flat (purchases stop with growth)."""
    tot = sum(net*(1+g)**t/(1+r)**t for t in range(1, n+1))
    return tot + gross*(1+g)**n/r/(1+r)**n
def irr(net, gross, g, target):
    lo, hi = 0.001, 0.5
    for _ in range(200):
        m = (lo+hi)/2
        if pv(net, gross, g, m) > target: lo = m
        else: hi = m
    return m
W = [2021, 2022, 2023, 2024, 2025]
avg = lambda f, ys: sum(f(y) for y in ys)/len(ys)
au, ae, aa = avg(uoc, W), avg(eoc, W), avg(acq, W)
asales = avg(lambda y: D[y][5], W)
gu = (uoc(2025)/uoc(2021))**0.25 - 1; ge = (eoc(2025)/eoc(2021))**0.25 - 1
gs = (D[2025][5]/D[2021][5])**0.25 - 1
go = 1.0
for c in CORE: go *= (1+c)
go = go**0.25 - 1
EV, MC = PRICE*SHARES + NETDEBT, PRICE*SHARES
print("YEAR   UOC    EOC    ACQ   UOC/sales")
for y in sorted(D): print(y, f"{uoc(y):7.1f} {eoc(y):7.1f} {acq(y):7.1f}  {uoc(y)/D[y][5]*100:5.1f}%")
hi_share = max(uoc(y)/D[y][5] for y in D)
print(f"\nwindow FY2021-25: avg UOC {au:.1f}, avg EOC {ae:.1f}, avg acquisitions {aa:.1f}, avg sales {asales:.0f}")
print(f"shown growth: UOC {gu*100:.2f}%, EOC {ge*100:.2f}%; sales {gs*100:.2f}% (total); organic (core) {go*100:.2f}%")
y10 = au*(1+gu)**10; s10 = asales*(1+gs)**10
print(f"(f) test: UOC carried 10y at {gu*100:.2f}% = {y10:.0f} on sales {s10:.0f} = {y10/s10*100:.1f}% of sales; highest UOC/sales 2019-2025 {hi_share*100:.1f}%"
      f" -> {'CUT to sales growth' if y10/s10 > hi_share else 'no cut'}")
y10e = ae*(1+ge)**10
print(f"(f) test equity-only: EOC carried 10y at {ge*100:.2f}% = {y10e:.0f} = {y10e/s10*100:.1f}% of sales -> cut")
print(f"\nprice {PRICE}; market value {MC:.0f}; net debt {NETDEBT:.1f}; EV {EV:.0f}")
def case(label, net0, gross0, gnet, debt, target):
    lo = pv(net0, gross0, 0.0, R); hi = pv(net0, gross0, gnet, R)
    f_lo = pv(net0, gross0, 0.0, FLOOR); f_hi = pv(net0, gross0, gnet, FLOOR)
    fair = (f_lo+f_hi)/2
    r_lo, r_hi = irr(net0, gross0, 0.0, target), irr(net0, gross0, gnet, target)
    a, b = sorted([lo, hi])
    print(f"{label}\n   whole {a:7.0f} to {b:7.0f} (width {b/a:.2f}x); per share ${(a-debt)/SHARES:6.2f} to ${(b-debt)/SHARES:6.2f}"
          f"\n   at 10%: {f_lo:6.0f} / {f_hi:6.0f}; FAIR per share ${(fair-debt)/SHARES:6.2f}"
          f"\n   expected return at the price: no-growth end {r_lo*100:5.2f}%, growth end {r_hi*100:5.2f}%")
    return (a-debt)/SHARES, (b-debt)/SHARES, (fair-debt)/SHARES
print("\n== CENTRAL: all-equity, default pair (acquisitions deducted to year ten, total growth credited, cut to sales growth)")
C = case("all-equity, default pair, g = sales growth", au-aa, au, gs, NETDEBT, EV)
print("\n== BESIDE")
E = case("equity-only, default pair, g = sales growth (against market value)", ae-aa, ae, gs, 0.0, MC)
case("all-equity, default pair, shown growth UNCUT (literal, before (f))", au-aa, au, gu, NETDEBT, EV)
case("all-equity, default pair, Taco added to net debt, credited at nothing (no filed record)", au-aa, au, gs, NETDEBT+TACO, EV+TACO)
case("all-equity, the no-growth end read as no purchases at all (alternative reading of (c)): owner cash flat, no growth", au, au, 0.0, NETDEBT, EV)
O = case("all-equity, organic pair (acquisitions left out, core growth)", au, au, go, NETDEBT, EV)
case("equity-only, organic pair", ae, ae, go, 0.0, MC)
du = avg(lambda y: D[y][0]-D[y][1]-DEP[y] + D[y][3]*(1-TAX), W)
case("all-equity, organic pair, depreciation for capex", du, du, go, NETDEBT, EV)
S = [2019,2020,2021,2022,2023,2024,2025]
a7, q7a = avg(uoc, S), avg(acq, S)
gs7 = (D[2025][5]/D[2019][5])**(1/6) - 1
case(f"all-equity, seven-year 2019-2025, acquisitions deducted, sales growth {gs7*100:.2f}%", a7-q7a, a7, gs7, NETDEBT, EV)
best = max(uoc(y) for y in D)
case(f"all-equity, BEST YEAR owner cash {best:.0f} with no purchases, total sales growth (an upper bound no convention allows)", best, best, gs, NETDEBT, EV)
ttm_e = (814.8-567.7+504.4) - (68.8-27.7+37.4) - (37.0-21.2+19.5)
print(f"\nTTM to 2026-06-30 equity-only owner cash {ttm_e:.1f} (FY2025 {eoc(2025):.1f}), direction only")
print(f"\nREPORT: central range ${C[0]:.2f} to ${C[1]:.2f}; fair (all-equity) ${C[2]:.2f}; equity-only range ${E[0]:.2f} to ${E[1]:.2f}, fair ${E[2]:.2f}")
