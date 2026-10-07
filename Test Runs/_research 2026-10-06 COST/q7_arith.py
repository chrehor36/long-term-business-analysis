# Q7 arithmetic for the COST run of 2026-10-06. USD millions unless stated. Arithmetic only; no verdict.
r = 0.0566            # US Treasury 30-year par yield, 2026-10-05 (issuing authority)
floor = 0.10          # the v5 CONVENTION floor, about ten percent pre-tax, applied to owner cash after company tax
shares = 443.479      # millions, dei cover count, 10-Q filed 2026-06-03 (0000909832-26-000051)
price = 935.68        # aggregator live quote 2026-10-06, flagged
# filed figures (10-K FY2021..FY2025: 0000909832-21-000014, -22-000021, -23-000042, -24-000049, -25-000101; FY2026 from 8-K 0000909832-26-000084 ex.99.1, unaudited, "subject to reclassification")
yrs  = ["FY2021","FY2022","FY2023","FY2024","FY2025","FY2026"]
ocf  = [8958, 7392, 11068, 11339, 13335, 15825]
sbc  = [665, 724, 774, 818, 860, 924]
capex= [3588, 3891, 4323, 4710, 5498, 6435]
flp  = [67, 176, 291, 136, 147, 91]      # finance-lease principal (FY2026: "financing lease payments and other financing activities, net")
da   = [1781, 1900, 2077, 2237, 2426, 2674]
oc_capex = [o-s-c-f for o,s,c,f in zip(ocf,sbc,capex,flp)]
oc_da    = [o-s-d for o,s,d in zip(ocf,sbc,da)]
print("year      OCF   SBC  capex  fin.lease  D&A   owner cash(capex basis)  (D&A basis)")
for i,y in enumerate(yrs):
    print(f"{y}  {ocf[i]:6,} {sbc[i]:4,} {capex[i]:5,} {flp[i]:5,} {da[i]:5,}   {oc_capex[i]:6,}   {oc_da[i]:6,}")
def pv(c0, g, rate, n=10):
    s = sum(c0*(1+g)**t/(1+rate)**t for t in range(1,n+1))
    term = c0*(1+g)**n/rate/(1+rate)**n
    return s+term
def report(label, win, netcash_label, netcash):
    a = sum(oc_capex[i] for i in win)/len(win)
    a_da = sum(oc_da[i] for i in win)/len(win)
    first, last = oc_capex[win[0]], oc_capex[win[-1]]
    g = (last/first)**(1/(len(win)-1))-1
    print(f"\n=== {label}: five-year average owner cash {a:,.0f} (capex basis); {a_da:,.0f} (D&A basis); shown growth on aggregate owner cash, endpoints {first:,}->{last:,}: {g*100:.1f}%/yr")
    for gg,name in [(0.0,"no growth"),(g,"shown growth"),(min(g,r),"shown growth capped at the sovereign")]:
        v = pv(a,gg,r); v_da = pv(a_da,gg,r)
        print(f"  {name:38s} g={gg*100:5.1f}%  EV {v:9,.0f}  = ${v/shares:7.2f}/sh (EV)  ${ (v+netcash)/shares:7.2f}/sh (equity, + net cash {netcash_label})   [D&A basis EV ${v_da/shares:7.2f}/sh]")
    lo, hi = pv(a,0,r), pv(a,g,r)
    print(f"  range (EV, capex basis): ${lo/shares:,.0f} to ${hi/shares:,.0f} a share; top/bottom = {hi/lo:.2f}; with net cash: ${ (lo+netcash)/shares:,.0f} to ${(hi+netcash)/shares:,.0f}")
    # fair price: PV at the floor of the two end streams, midpoint
    f_lo, f_hi = pv(a,0,floor), pv(a,g,floor)
    mid = (f_lo+f_hi)/2
    print(f"  FAIR PRICE at {floor*100:.0f}% (midpoint of the two ends at the floor): EV ${mid/shares:,.0f}/sh [ends ${f_lo/shares:,.0f} and ${f_hi/shares:,.0f}]; equity (+ net cash) ${ (mid+netcash)/shares:,.0f}/sh")
    f_lo_c, f_hi_c = pv(a,0,floor), pv(a,min(g,r),floor)
    print(f"  FAIR PRICE, capped-growth variant: EV ${ (f_lo_c+f_hi_c)/2/shares:,.0f}/sh; equity ${ ((f_lo_c+f_hi_c)/2+netcash)/shares:,.0f}/sh")
    # expected return at the price (IRR of the midpoint stream vs market cap) 
    mc = price*shares
    def irr(c0,g):
        lo_,hi_=0.0001,1.0
        for _ in range(100):
            m=(lo_+hi_)/2
            if pv(c0,g,m) > mc - netcash: lo_=m
            else: hi_=m
        return m
    print(f"  expected return at ${price} (EV = market cap {mc:,.0f} less net cash): no-growth {irr(a,0)*100:.2f}%, shown-growth {irr(a,g)*100:.2f}%")
report("Window A, FY2021-FY2025 (the filed 10-K years)", [0,1,2,3,4], "FY2025: cash 14,161 + ST inv 1,123 - debt 5,805", 14161+1123-5805)
report("Window B, FY2022-FY2026 (FY2026 from the unaudited 8-K release)", [1,2,3,4,5], "FY2026: cash 20,207 + ST inv 1,094 - debt 6,162", 20207+1094-2248-3914)
print("\nCross-checks: FY2025 operating income/revenue", 10383/275235, "; owner cash FY2025 / market cap", 6830/(price*shares), "; FY2026", 8375/(price*shares))
print("Pre-tax operating income FY2021->FY2025 CAGR", ((10383/6708)**0.25-1)*100, "; revenue CAGR", ((275235/195929)**0.25-1)*100, "; FY2026 OI/rev", 11685/303154)

# D&A-basis variant of the fair price (Window A), added 2026-10-06 for the reporting line
a_da = sum(oc_da[i] for i in [0,1,2,3,4])/5
g_da = (oc_da[4]/oc_da[0])**0.25-1
lo, hi = pv(a_da,0,floor), pv(a_da,g_da,floor)
nc = 14161+1123-5805
print(f"\nD&A-basis fair price, Window A: average {a_da:,.0f}, shown growth {g_da*100:.1f}%; ends at 10%: ${lo/shares:,.0f} and ${hi/shares:,.0f}; midpoint EV ${(lo+hi)/2/shares:,.0f}/sh, equity ${((lo+hi)/2+nc)/shares:,.0f}/sh")
print(f"D&A-basis range at the sovereign, Window A: ${pv(a_da,0,r)/shares:,.0f} to ${pv(a_da,g_da,r)/shares:,.0f} EV; with net cash ${(pv(a_da,0,r)+nc)/shares:,.0f} to ${(pv(a_da,g_da,r)+nc)/shares:,.0f}")
# what the price implies: growth for ten years (then flat) at which the capex-basis stream returns 10% on today's EV
mc_ev = price*shares - nc
lo_,hi_=0.0,1.0
for _ in range(100):
    m=(lo_+hi_)/2
    if pv(5085,m,floor) < mc_ev: lo_=m
    else: hi_=m
print(f"Growth for ten years (then flat) at which the five-year-average owner cash of 5,085 returns 10% on today's EV of {mc_ev:,.0f}: {m*100:.1f}%/yr")
