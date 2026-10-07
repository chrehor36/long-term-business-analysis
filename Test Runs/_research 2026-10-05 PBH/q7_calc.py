# Arithmetic for the PBH run of 2026-10-05. Inputs are filed figures (accessions in the run file) or flagged.
# Owner cash (OE) = OCF - SBC - capex (as filed). Unlevered after-tax = OE + interest paid x (1-0.25). Pre-tax unlevered = OE + interest paid + income taxes paid.
oe   ={2011:82.4,2022:241.2,2023:209.5,2024:225.4,2025:232.1,2026:235.6}
intp ={2011:17.5,2022:61.4,2023:54.2,2024:63.2,2025:47.8,2026:43.8}
taxp ={2011:11.9,2022:46.6,2023:40.7,2024:59.6,2025:52.1,2026:45.9}
T=0.25
yrs=[2022,2023,2024,2025,2026]
ul={y:oe[y]+intp[y]*(1-T) for y in oe}
pt={y:oe[y]+intp[y]+taxp[y] for y in oe}
for y in sorted(oe): print(y,"OE",oe[y],"unlev after-tax",round(ul[y],1),"pre-tax unlev",round(pt[y],1))
avg_ul=sum(ul[y] for y in yrs)/5; avg_pt=sum(pt[y] for y in yrs)/5
print("5y avg unlev after-tax",round(avg_ul,1)," 5y avg pre-tax unlev",round(avg_pt,1))
g_shown=(ul[2026]/ul[2022])**(1/4)-1
print("growth shown (aggregate, unlevered after-tax, FY22->FY26)",round(100*g_shown,2),"%")
org=[2.8,1.0,1.7,0.1,1.3,-2.4,10.1,3.5,0.2,1.2,-4.5]
p=1
for x in org: p*=1+x/100
g_org=p**(1/len(org))-1
print("organic revenue geometric mean FY16-FY26",round(100*g_org,2),"%")
BR_ebitda=95.0; LAC_ebitda=12.0
acq_ul=(BR_ebitda+LAC_ebitda)*(1-T); acq_pt=BR_ebitda+LAC_ebitda
base_ul=avg_ul+acq_ul; base_pt=avg_pt+acq_pt
print("pro forma base after-tax unlev",round(base_ul,1)," pre-tax",round(base_pt,1))
shares=47.374522; price=45.61
debt=2045.0+95.0; cash=89.1-(150.0-95.0); leases=2.656+17.968
netdebt=debt-cash+leases
mcap=shares*price; ev=mcap+netdebt
print("mcap",round(mcap,1)," net debt",round(netdebt,1)," EV",round(ev,1))
r=0.0566
def pv(c0,g,rate,n=10):
    v=0; c=c0
    for t in range(1,n+1):
        c*=1+g; v+=c/(1+rate)**t
    return v + c/rate/(1+rate)**n
def irr(c0,g,target):
    lo,hi=0.0001,1.0
    for _ in range(200):
        m=(lo+hi)/2
        if pv(c0,g,m)>target: lo=m
        else: hi=m
    return m
cases={"shown decline":g_shown,"no growth":0.0,"whole-cycle organic":g_org}
print("\nVALUE at the long rate 5.66% (after-tax unlevered, 10 yrs then zero nominal growth), less net debt")
vals={}
for k,g in cases.items():
    E=pv(base_ul,g,r); eq=E-netdebt; vals[k]=eq/shares
    print(f"  {k:22s} g={100*g:5.2f}%  EV {E:7.0f}  equity {eq:7.0f}  per share {eq/shares:6.2f}")
print("  ratio top/bottom",round(vals['whole-cycle organic']/vals['shown decline'],2), " (five-year: ", round(vals['no growth']/vals['shown decline'],2),")")
print("\nLEGACY ONLY (no acquisitions after the window; acquisition debt counted, acquired brands at zero) -- stress")
for k,g in cases.items():
    E=pv(avg_ul,g,r); eq=E-netdebt
    print(f"  {k:22s} equity/share {eq/shares:6.2f}")
print("\nACQUISITIONS AT COST (brands bought = price paid 1,195; legacy only otherwise)")
for k,g in cases.items():
    E=pv(avg_ul,g,r)+1045+150; eq=E-netdebt
    print(f"  {k:22s} equity/share {eq/shares:6.2f}")
print("\nEXPECTED PRE-TAX RETURN at the price, all-equity basis (EV), pre-tax unlevered owner cash")
for k,g in cases.items():
    print(f"  {k:22s} {100*irr(base_pt,g,ev):5.2f}%")
print("  simple yield",round(100*base_pt/ev,2),"%")
# fair price: central (no growth) clears 10% pre-tax on EV
ev_fair=base_pt/0.10; fair=(ev_fair-netdebt)/shares
print("\nFAIR (no growth, 10% pre-tax all-equity): EV",round(ev_fair,0)," per share",round(fair,2))
# fair under shown decline and whole-cycle
for k,g in cases.items():
    lo,hi=0,20000
    for _ in range(200):
        m=(lo+hi)/2
        if irr(base_pt,g,m)>0.10: lo=m
        else: hi=m
    print(f"  price where {k} clears 10% pre-tax: {(m-netdebt)/shares:6.2f}")
ev_cheap=base_pt/0.15; print("CHEAP (no growth, 15% pre-tax all-equity): per share",round((ev_cheap-netdebt)/shares,2))
lo,hi=0,20000
for _ in range(200):
    m=(lo+hi)/2
    if irr(base_pt,g_shown,m)>0.15: lo=m
    else: hi=m
print("CHEAP (shown decline, 15%):",round((m-netdebt)/shares,2))
print("\nBuyback check: FY2026 repurchases $156.3M; March 2026 average price paid $60.49 (10-K Item 5)")
