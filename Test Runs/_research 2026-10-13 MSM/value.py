# MSM COMPUTATION, NOT A CLEARANCE. Filed figures in USD millions (10-K FY2025 0001003078-25-000123,
# FY2023 0001003078-23-000102 for FY2021-22 columns, 10-Q Q3 FY2026 0001003078-26-000080).
yrs=[2021,2022,2023,2024,2025]
ocf ={2021:224.462,2022:246.183,2023:699.582,2024:410.696,2025:333.717}
rpa ={2021:0,2022:0,2023:300.0,2024:0,2025:0}          # one-time receivables sale (RPA note)
sbc ={2021:17.721,2022:19.264,2023:18.639,2024:18.848,2025:12.551}
capex={2021:53.746,2022:61.373,2023:92.493,2024:99.406,2025:92.840}
acq ={2021:22.000,2022:57.865,2023:20.182,2024:23.990,2025:0.790}
fl  ={2021:2.584,2022:2.466,2023:2.193,2024:3.625,2025:1.512}
dep ={2021:57.2,2022:58.3,2023:59.8,2024:64.8,2025:72.1}  # XBRL Depreciation tag, per run.py facts
intp={2021:13.995,2022:16.903,2023:22.432,2024:24.721,2025:23.891}
fee ={2021:0,2022:0,2023:12.175,2024:18.438,2025:15.767}
sales={2021:3243.2,2022:3691.9,2023:4009.3,2024:3821.0,2025:3769.5}
T=0.25  # filer's effective tax rate FY2024-25 (25.3%, 24.9%)
allsp={y:ocf[y]-rpa[y]-sbc[y]-capex[y]-acq[y]-fl[y] for y in yrs}
mnt  ={y:ocf[y]-rpa[y]-sbc[y]-dep[y]-fl[y] for y in yrs}
for y in yrs: print(y,'all-spend %.1f'%allsp[y],'maint-only(no acq) %.1f'%mnt[y],'share of sales %.1f%%'%(100*allsp[y]/sales[y]))
avg=lambda d:sum(d.values())/len(d)
A_all=avg(allsp); A_m=avg(mnt); A_int=avg(intp)*(1-T); A_fee=avg(fee)*(1-T)
print('5yr avg all-spend %.1f  maint %.1f  after-tax interest %.1f  after-tax RPA fees %.1f'%(A_all,A_m,A_int,A_fee))
g_end=(allsp[2025]/allsp[2021])**(1/4)-1
g_sales=(sales[2025]/sales[2021])**(1/4)-1
print('shown growth end-to-end %.1f%%  halves %.1f -> %.1f ; sales growth %.2f%%'%(100*g_end,(allsp[2021]+allsp[2022])/2,(allsp[2024]+allsp[2025])/2,100*g_sales))
def pv(c0,g,r,n=10):
    v=0;c=c0
    for t in range(1,n+1):
        c*=1+g; v+=c/(1+r)**t
    return v+ c/r/(1+r)**n   # zero nominal growth after year ten
r=0.056; shares=55.846; price=128.67
nd=417.219+89.555-74.094; rpa_bal=350.0
print('net debt %.1f'%nd)
cases={}
# all-equity basis: owner cash before interest (after tax)
lo_ae=pv(A_m+A_int,0,r); hi_ae=pv(A_all+A_int,g_sales,r)
lo_eq=pv(A_m,0,r); hi_eq=pv(A_all,g_sales,r)
print('ALL-EQUITY  no-growth maint %.0f  growth all-spend %.0f  -> per share %.2f .. %.2f'%(lo_ae,hi_ae,(lo_ae-nd)/shares,(hi_ae-nd)/shares))
print('EQUITY-ONLY per share %.2f .. %.2f'%(lo_eq/shares,hi_eq/shares))
# beside: all-spending no-growth (literal default) 
print('beside all-spend no-growth AE per share %.2f'%((pv(A_all+A_int,0,r)-nd)/shares))
print('beside maint growth AE per share %.2f'%((pv(A_m+A_int,g_sales,r)-nd)/shares))
# floor test: expected return at the price for each case (IRR on EV)
ev=price*shares+nd
def irr(c0,g,target):
    lo,hi=0.0001,0.5
    for _ in range(200):
        m=(lo+hi)/2
        if pv(c0,g,m)>target: lo=m
        else: hi=m
    return m
for nm,c,g in [('no-growth maint',A_m+A_int,0),('growth all-spend',A_all+A_int,g_sales),('maint+growth (beside)',A_m+A_int,g_sales)]:
    print('IRR at price on EV %.0f: %s %.2f%%'%(ev,nm,100*irr(c,g,ev)))
eqv=price*shares
for nm,c,g in [('no-growth maint',A_m,0),('growth all-spend',A_all,g_sales)]:
    print('IRR equity-only %s %.2f%%'%(nm,100*irr(c,g,eqv)))
# fair price: each end at 10%, averaged
f_ae=((pv(A_m+A_int,0,0.10)-nd)/shares+(pv(A_all+A_int,g_sales,0.10)-nd)/shares)/2
f_eq=(pv(A_m,0,0.10)/shares+pv(A_all,g_sales,0.10)/shares)/2
print('FAIR all-equity %.2f  equity-only %.2f  price %.2f'%(f_ae,f_eq,price))
# beside: RPA counted as debt, its fees added back as interest
f_rpa=((pv(A_m+A_int+A_fee,0,0.10)-nd-rpa_bal)/shares+(pv(A_all+A_int+A_fee,g_sales,0.10)-nd-rpa_bal)/shares)/2
print('FAIR all-equity with RPA as debt %.2f'%f_rpa)
lo_r=(pv(A_m+A_int+A_fee,0,r)-nd-rpa_bal)/shares; hi_r=(pv(A_all+A_int+A_fee,g_sales,r)-nd-rpa_bal)/shares
print('range with RPA as debt %.2f .. %.2f'%(lo_r,hi_r))
print('width ratio %.2f'%(((hi_ae-nd)/shares)/((lo_ae-nd)/shares)))
# literal window without RPA removal, shown beside
lit={y:ocf[y]-sbc[y]-capex[y]-acq[y]-fl[y] for y in yrs}; print('literal 5yr avg all-spend incl RPA inflow %.1f'%avg(lit))
# literal window shown beside (RPA inflow left in, all spending, acquisitions deducted)
L=avg(lit)
print('LITERAL pair AE per share %.2f .. %.2f'%((pv(L+A_int,0,r)-nd)/shares,(pv(L+A_int,g_sales,r)-nd)/shares))
print('LITERAL IRR no-growth %.2f%% growth %.2f%%'%(100*irr(L+A_int,0,ev),100*irr(L+A_int,g_sales,ev)))
# earlier years' share of sales (all spending, acquisitions deducted; finance leases not deducted)
old={2016:(401.1,14.0,87.9,0,2863.5),2017:(246.8,13.9,46.5,42.3,2887.7),2018:(339.7,14.9,44.9,87.0,3203.9),2019:(328.4,16.3,51.8,11.6,3363.8),2020:(396.7,16.9,47.0,2.3,3192.4)}
for y,(o,s,c,a,sl) in old.items(): print(y,'share %.1f%%'%(100*(o-s-c-a)/sl))
print('growth case year-10 share of sales at shown 15.2%%: %.1f%%'%(100*A_all*(1+g_end)**10/(sales[2025]*(1+g_sales)**10)))
