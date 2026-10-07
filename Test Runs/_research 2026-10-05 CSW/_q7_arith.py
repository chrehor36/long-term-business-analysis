# Arithmetic for the CSW run, 2026-10-05. Inputs from filed statements (10-K FY2017..FY2026 cash flow lines via XBRL,
# cross-checked FY2026 against the filed 10-K 0001624794-26-000027). COMPUTATION, not a clearance.
ocf  ={2017:39.0,2018:43.2,2019:59.7,2020:69.9,2021:66.3,2022:69.1,2023:121.5,2024:164.3,2025:168.4,2026:149.7}
sbc  ={2017:4.6,2018:4.2,2019:3.9,2020:5.1,2021:5.1,2022:8.4,2023:9.8,2024:11.5,2025:13.6,2026:14.9}
capex={2017:9.4,2018:5.5,2019:7.5,2020:11.4,2021:8.8,2022:15.7,2023:14.0,2024:16.6,2025:16.3,2026:17.3}
dep  ={2017:7.9,2018:7.7,2019:7.4,2020:7.9,2021:9.2,2022:11.6,2023:12.8,2024:14.0,2025:14.2,2026:15.9}
intp ={2017:2.6,2018:2.1,2019:1.3,2020:1.2,2021:1.9,2022:5.0,2023:12.5,2024:12.3,2025:4.8,2026:20.9}
sh   ={2017:15.8,2018:15.7,2019:15.5,2020:15.2,2021:15.1,2022:15.8,2023:15.5,2024:15.6,2025:16.3,2026:16.7}
T=0.25  # blended statutory rate the filer uses in its own pro forma note (10-K FY2026, Note 2)
print("FY   OC(capex)  OC(dep)  unlev OC   OC/sh")
oc={};uo={}
for y in ocf:
    oc[y]=ocf[y]-sbc[y]-capex[y]; uo[y]=oc[y]+intp[y]*(1-T)
    print(y, f"{oc[y]:8.1f} {ocf[y]-sbc[y]-dep[y]:8.1f} {uo[y]:9.1f} {oc[y]/sh[y]:7.2f}")
avg5=sum(uo[y] for y in range(2022,2027))/5; avg5l=sum(oc[y] for y in range(2022,2027))/5
print(f"5-yr avg unlevered {avg5:.1f}; levered {avg5l:.1f}")
print(f"growth shown, unlevered OC FY22->FY26: {(uo[2026]/uo[2022])**(1/4)-1:.1%}; FY21->FY26 {(uo[2026]/uo[2021])**(1/5)-1:.1%}")
# claims ahead of the common at 2026-06-30 (10-Q 0001624794-26-000046): debt 29.458+825.993, cash 47.495;
# redeemable NCI 18.989 and contingent consideration 16.7 at 2026-03-31 (10-K)
debt=29.458+825.993; cash=47.495; claims=debt-cash+18.989+16.7
shares=16.293487; price=305.83
print(f"net claims ahead of common {claims:.1f}; mkt cap {shares*price:.1f}; EV at price {shares*price+claims:.1f}")
r=0.0563
def ev(base,g,r,n=10,gt=0.0):
    pv=sum(base*(1+g)**t/(1+r)**t for t in range(1,n+1))
    cn=base*(1+g)**n; term=cn*(1+gt)/(r-gt)
    return pv+term/(1+r)**n
def ps(e): return (e-claims)/shares
for nm,b in [("5-yr avg (convention)",avg5)]:
    lo=ev(b,0,r); hi=ev(b,min(r,0.0563),r)
    print(f"{nm}: base {b:.1f}  no-growth EV {lo:.0f} -> ${ps(lo):.1f}/sh ; shown-growth(capped 5.63%) EV {hi:.0f} -> ${ps(hi):.1f}/sh ; ratio {ps(hi)/ps(lo):.2f}")
# pro forma base: FY2026 unlevered + missing months of MARS (Apr 1 - Nov 4 2025, ~7.1 months) and Aspen (Apr 2025, 1 month),
# on the filer's own adjusted EBITDA (MARS $52.3M TTM, 8-K 0001193125-25-264609; Aspen $28.5M 2024, 8-K 0001193125-25-056730), taxed at 25%
pf=uo[2026]+52.3*(1-T)*7.1/12+28.5*(1-T)*1/12
lo=ev(pf,0,r); hi=ev(pf,r,r)
print(f"pro forma base {pf:.1f}: no-growth ${ps(lo):.1f} ; capped-growth ${ps(hi):.1f}")
# what the price implies
print(f"unlevered owner-cash yield at price: 5-yr {avg5/(shares*price+claims):.2%}; pro forma {pf/(shares*price+claims):.2%}")
# implied ten-year growth at price, discounting at the 10% floor, zero terminal growth
import math
for b in (avg5,pf):
    lo_g,hi_g=0.0,0.6
    for _ in range(100):
        m=(lo_g+hi_g)/2
        if ps(ev(b,m,0.10))<price: lo_g=m
        else: hi_g=m
    print(f"base {b:.1f}: 10-yr growth needed for a 10% return at ${price}: {m:.1%} a year, then none")
# FAIR: central case = pro forma base, 5% a year for ten years, then 0 nominal, discounted at the 10% floor
for g in (0.03,0.05,0.07):
    print(f"FAIR at 10%, pro forma base, g={g:.0%} ten years then 0: ${ps(ev(pf,g,0.10)):.1f}")
# CHEAP: the price at which the central base with no growth at all returns 10%
print(f"CHEAP (pro forma base, no growth, 10%): ${ps(pf/0.10):.1f}; on the 5-yr base: ${ps(avg5/0.10):.1f}")
# incremental return on capital, FY2021 -> FY2026
add_cap=(513.1-64.6)+347.4-234.1+((debt-cash)-(242.3+0.6-10))
print(f"capital added FY22-26 ~{add_cap:.0f}; unlevered OC change {uo[2026]-uo[2021]:.1f} (+pro forma {pf-uo[2026]:.1f}) -> {(pf-uo[2021])/add_cap:.1%} after tax")
