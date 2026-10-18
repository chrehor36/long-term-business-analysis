# COMPUTATION, NOT A CLEARANCE. Q7 range and fair price for HORIBA, JPY millions, FY2021-FY2025 window.
T = 0.305                      # statutory effective rate, yuho FY2025 tax note
r = 0.04134                    # JGB 30y, MOF jgbcme.csv, 2026-10-08
SH = 42_021_555                # shares outstanding 2026-06-30
NETCASH = 102_564 - 6_303      # net cash 2026-06-30 less interim dividend paid 2026-08-31
yrs = [2021, 2022, 2023, 2024, 2025]
OCF   = dict(zip(yrs, [35268, 33966, 16652, 40335, 54383]))
CAPEX = dict(zip(yrs, [12572, 12083, 9171, 19447, 26142]))
DA    = dict(zip(yrs, [10063, 10911, 12097, 12653, 13180]))
LEASE = dict(zip(yrs, [1252, 1482, 1762, 1875, 1859]))
SP    = dict(zip(yrs, [0, 0, 0, 169, 271]))
ACQ   = dict(zip(yrs, [0, 0, 2421, 0, 2497]))
INT_IN  = dict(zip(yrs, [182, 585, 1892, 2428, 2219]))
INT_OUT = dict(zip(yrs, [481, 680, 721, 879, 874]))
SALES = dict(zip(yrs, [224314, 270133, 290558, 317369, 333081]))
def avg(d): return sum(d.values())/len(d)
adj = {y: (INT_OUT[y]-INT_IN[y])*(1-T) for y in yrs}          # to the all-equity basis (before interest)
allsp = {y: OCF[y]-CAPEX[y]-LEASE[y]-SP[y]-ACQ[y] for y in yrs}  # all spending incl. acquisitions, after interest
maint = {y: OCF[y]-DA[y]-LEASE[y]-SP[y] for y in yrs}            # maintenance guess = depreciation, after interest
allsp_ae = {y: allsp[y]+adj[y] for y in yrs}; maint_ae = {y: maint[y]+adj[y] for y in yrs}
def cagr(d): return (d[2025]/d[2021])**(1/4)-1
print("adj to all-equity by year", {y: round(adj[y]) for y in yrs}, "avg", round(avg(adj)))
for n,d in [("all-spending after acq, equity", allsp), ("all-spending after acq, all-equity", allsp_ae),
            ("maintenance-only, equity", maint), ("maintenance-only, all-equity", maint_ae)]:
    print(f"{n:38s}", {y: round(v) for y,v in d.items()}, "avg", round(avg(d)), "cagr %.2f%%" % (100*cagr(d)))
print("sales cagr %.2f%%" % (100*((SALES[2025]/SALES[2021])**0.25-1)))
print("max owner cash / sales: maint %.3f allsp %.3f" % (max(maint[y]/SALES[y] for y in yrs), max(allsp[y]/SALES[y] for y in yrs)))

def pv(c0, g, rate, growth_spend0=0.0):
    """ten years at g, then flat; growth spending (growing at g) deducted for years 1-10 only."""
    v = 0.0
    for t in range(1, 11):
        v += (c0*(1+g)**t - growth_spend0*(1+g)**t) / (1+rate)**t
    v += c0*(1+g)**10 / rate / (1+rate)**10
    return v
def per_share(ev, add_cash=True): return (ev + (NETCASH if add_cash else 0)) * 1e6 / SH

M0 = avg(maint_ae); A0 = avg(allsp_ae); G0 = M0 - A0; g = cagr(maint_ae)
M0e = avg(maint); A0e = avg(allsp); G0e = M0e - A0e; ge = cagr(maint)
print(f"\nCENTRAL (all-equity): M0={M0:.0f} A0={A0:.0f} growth spend={G0:.0f} g={100*g:.2f}%  net cash {NETCASH}")
for rate,label in [(r,"at JGB 4.134%"),(0.10,"at 10%")]:
    lo = pv(M0, 0.0, rate); hi = pv(M0, g, rate, G0)
    print(f"  {label}: no-growth end ¥{per_share(lo):,.0f}  shown-growth end ¥{per_share(hi):,.0f}  ratio {max(lo,hi)/min(lo,hi):.2f}  avg ¥{(per_share(lo)+per_share(hi))/2:,.0f}")
print(f"EQUITY-ONLY beside: M0={M0e:.0f} A0={A0e:.0f} g={100*ge:.2f}%")
for rate,label in [(r,"at JGB 4.134%"),(0.10,"at 10%")]:
    lo = pv(M0e, 0.0, rate); hi = pv(M0e, ge, rate, G0e)
    print(f"  {label}: no-growth ¥{per_share(lo,False):,.0f}  growth ¥{per_share(hi,False):,.0f}  avg ¥{(per_share(lo,False)+per_share(hi,False))/2:,.0f}")
# all-spending literal case beside (no maintenance guess): A0 at its own shown growth
ga = cagr(allsp_ae)
for rate,label in [(r,"at JGB"),(0.10,"at 10%")]:
    lo = pv(A0, 0.0, rate); hi = pv(A0, ga, rate)
    print(f"ALL-SPENDING literal beside {label}: g={100*ga:.2f}% no-growth ¥{per_share(lo):,.0f} growth ¥{per_share(hi):,.0f}")
# ten-year average beside (cycle reading)
oc10 = [2302,16106,9077,12873,15954,21444,20401,5719,18844,26111]
print("ten-year average owner cash (equity basis, before acq):", sum(oc10)/10)
# what the price implies
price=26330; ev = price*SH/1e6 - NETCASH
print(f"EV at price ¥{ev:,.0f}m; yield on M0 {100*M0/ev:.2f}%, on A0 {100*A0/ev:.2f}%")
# growth needed for the shown-growth case to equal price at 10%
lo,hi = 0.0, 0.6
for _ in range(60):
    mid=(lo+hi)/2
    if per_share(pv(M0, mid, 0.10, G0)) < price: lo=mid
    else: hi=mid
print(f"ten-year growth needed for central growth case to earn 10% at the price: {100*lo:.1f}%/yr")
