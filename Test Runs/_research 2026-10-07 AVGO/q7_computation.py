# COMPUTATION, NOT A CLEARANCE. Q7 arithmetic for the reporting figures of a file closed at Q1. $ millions unless stated.
# Inputs transcribed from the 10-Ks (AVGO 0001730168-21-000153 .. -25-000121; VMware 0001124610-22/23 10-Ks via XBRL) and the 10-Q 0001730168-26-000080.
r, floor, shares, price = 0.0564, 0.10, 4773.629865, 375.81
debt, cash = 59419, 23975                          # 10-Q balance sheet, 2026-08-02; finance leases nil (10-K FY2025 note)
net_debt = debt - cash
T = 0.21                                            # CONVENTION of this run: interest shield at the US federal statutory rate
yrs = ["FY2021","FY2022","FY2023","FY2024","FY2025"]
ocf   = [13764,16736,18085,19962,27537]; sbc = [1704,1533,2171,5741,7568]; capex = [443,424,452,548,623]
intp  = [1565,1386,1503,3250,2672]
acq   = [8,246,53,25978,0]; divest = [45,0,0,3485,300]
oc    = [o-s-c for o,s,c in zip(ocf,sbc,capex)]                       # owner cash, levered
unlev = [x+i*(1-T) for x,i in zip(oc,intp)]                           # before interest, after tax
acqn  = [a-d for a,d in zip(acq,divest)]
# VMware stand-alone (fiscal years ended 2022-01-28 and 2023-02-03): OCF-SBC-capex, interest paid
vmw = [4357-1075-386 + 200*(1-T), 4300-1290-450 + 292*(1-T)]
vmw_map = [vmw[0], vmw[1], vmw[1], 0, 0]                              # FY2023 uses VMware's last filed year (approximation, said so)
combined = [u+v for u,v in zip(unlev, vmw_map)]
def cagr(a,b,n): return (b/a)**(1/n)-1
def stream(cf,g):  # ten years at g, then zero nominal growth
    return [cf*(1+g)**t for t in range(1,11)]
def pv(cf,g,rate):
    s = stream(cf,g); return sum(x/(1+rate)**t for t,x in enumerate(s,1)) + s[-1]/rate/(1+rate)**10
def case(name, base, g):
    lo, hi = sorted([pv(base,0,r), pv(base,g,r)])
    ps = lambda ev: (ev-net_debt)/shares
    mid_fair_ev = (pv(base,0,floor)+pv(base,g,floor))/2
    print(f"\n{name}: base {base:,.0f}  growth {100*g:.1f}%")
    print(f"  enterprise range ${lo:,.0f}M to ${hi:,.0f}M ; per share ${ps(lo):,.2f} to ${ps(hi):,.2f} (ratio {hi/lo:.2f}) against ${price}")
    print(f"  FAIR PRICE (all-equity): ${ps(mid_fair_ev):,.2f}  [EV at floor ${mid_fair_ev:,.0f}M]")
    return ps
for y,a,b,c,d,e in zip(yrs,oc,intp,unlev,acqn,combined): print(f"{y}: owner cash {a:,} interest paid {b:,} unlevered {c:,.0f} acq net {d:,} combined {e:,.0f}")
print("market cap", f"{shares*price:,.0f}", "net debt", net_debt, "EV", f"{shares*price+net_debt:,.0f}")
mean_u = sum(unlev)/5; mean_c = sum(combined)/5; mean_ad = (sum(unlev)-sum(acqn))/5
g_u = cagr(unlev[0],unlev[4],4); g_c = cagr(combined[0],combined[4],4)
print(f"means: unlevered {mean_u:,.0f}; acquisitions deducted {mean_ad:,.0f}; combined companies {mean_c:,.0f}")
case("A. CENTRAL - merger inside the window, combined companies' own averages (spec. c)", mean_c, g_c)
case("B. BESIDE - Broadcom as filed, acquisitions net of divestitures deducted, total growth credited (spec. c default)", mean_ad, g_u)
# equity-only beside: owner cash after interest against market value
mean_lev_c = sum(o+v for o,v in zip(oc,[4357-1075-386+0,4300-1290-450,4300-1290-450,0,0]))/5
g_lev = cagr(oc[0]+2896, oc[4], 4)
lo, hi = pv(mean_lev_c,0,r)/shares, pv(mean_lev_c,g_lev,r)/shares
fair_eq = (pv(mean_lev_c,0,floor)+pv(mean_lev_c,g_lev,floor))/2/shares
print(f"\nEQUITY-ONLY beside (combined, after interest): base {mean_lev_c:,.0f} growth {100*g_lev:.1f}% range ${lo:,.2f}-${hi:,.2f}; fair ${fair_eq:,.2f}")
# trailing four quarters, the boom, shown only
ttm_oc = (27537-19834)-(7568-5373)-(623-386) + (32950-6287-1013)
ttm_int = (3210-2449) + 2355
print(f"\nTTM (Q4 FY25 + 9M FY26): owner cash {ttm_oc:,}; unlevered approx {ttm_oc+ttm_int*(1-T):,.0f} (interest expense used for interest paid)")
print(f"price-implied: EV/central base = {(shares*price+net_debt)/mean_c:.1f}x ; yield on EV {100*mean_c/(shares*price+net_debt):.2f}%; TTM unlevered yield on EV {100*(ttm_oc+ttm_int*(1-T))/(shares*price+net_debt):.2f}%")
# the boom as base, shown only (not a Q7 base: one year, aberrational on the filer's own word "significant upturn")
ttm_u = ttm_oc+ttm_int*(1-T)
case("C. SHOWN ONLY - trailing four quarters as base, combined-company growth", ttm_u, g_c)
case("D. SHOWN ONLY - trailing four quarters as base, as-filed growth", ttm_u, g_u)
