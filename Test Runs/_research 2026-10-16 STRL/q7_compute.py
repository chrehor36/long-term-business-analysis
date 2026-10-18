# COMPUTATION, NOT A CLEARANCE. Arithmetic for the STRL run of 2026-10-16. USD millions.
yrs=[2021,2022,2023,2024,2025]
ocf=[151.6,219.1,478.6,497.1,440.0]          # 10-K cash-flow statements
sbc=[11.8,12.7,14.6,19.0,24.2]
capex=[46.7,60.9,64.4,81.0,77.3]
psale=[4.1,4.9,13.8,10.2,5.7]
nci=[2.5,0.0,2.45,0.0,40.1]                    # distributions to noncontrolling interest owners
nol=[6.5,6.5,0,0,0]                             # federal NOL shelter 2021-22 (~$58.7M x 21% + state), computed at statutory rate
da=[34.2,52.1,57.4,68.4,77.1]; amort=[11.5,14.1,15.2,17.0,22.2]
dep=[a-b for a,b in zip(da,amort)]
netint=[-19.3,-19.7,-15.2,2.4,2.6]              # interest, net (income statement)
tax=0.24
wc=[20.3,29.4,252.5,199.8,9.4]                  # cash released by operating assets and liabilities
acq=[180.9,18.0,51.2-14.0,11.2,482.3-2.0]       # cash paid for businesses net of disposition proceeds
sales=[1581.8,1769.4,1972.2,2115.8,2490.0]
def avg(x): return sum(x)/len(x)
oc_eq=[o-s-c+p-n-t for o,s,c,p,n,t in zip(ocf,sbc,capex,psale,nci,nol)]
addint=[-ni*(1-tax) for ni in netint]
oc_ae=[a+b for a,b in zip(oc_eq,addint)]
maint_adj=[(c-p)-d for c,p,d in zip(capex,psale,dep)]
oc_ae_m=[a+b for a,b in zip(oc_ae,maint_adj)]
oc_eq_m=[a+b for a,b in zip(oc_eq,maint_adj)]
print('year      oc_eq_all  oc_ae_all  oc_ae_maint  wc  acq')
for i,y in enumerate(yrs): print(y, round(oc_eq[i],1), round(oc_ae[i],1), round(oc_ae_m[i],1), wc[i], round(acq[i],1))
print('avgs: eq_all %.1f ae_all %.1f ae_maint %.1f eq_maint %.1f wc %.1f acq %.1f' % (avg(oc_eq),avg(oc_ae),avg(oc_ae_m),avg(oc_eq_m),avg(wc),avg(acq)))
print('serial test: net purchases %.1f vs half of owner cash before purchases %.1f' % (sum(acq), sum(oc_ae)/2))
g_shown=(oc_ae[-1]/oc_ae[0])**0.25-1; g_sales=(sales[-1]/sales[0])**0.25-1
print('shown growth agg owner cash %.1f%%, sales growth %.1f%%, highest owner cash/sales %.1f%%' % (g_shown*100,g_sales*100,max(o/s for o,s in zip(oc_ae,sales))*100))
org=[1.047,1.091,(143.5-61.1)/1972.2+1,(610.2-224.1)/1879.9+1]
p=1
for x in org: p*=x
g_org=p**0.25-1; print('organic revenue growth as filer reports, CAGR %.2f%%' % (g_org*100))
def val(base,g,r,n=10):
    pv=0; cf=base
    for t in range(1,n+1):
        cf*=1+g; pv+=cf/(1+r)**t
    return pv + (cf/r)/(1+r)**n
def val0(base,r): return base/r
R=0.0543
netdebt=283.875-464.451; sh=30.588518; px=424.36; mcap=px*sh
print('mcap %.1f  net debt %.1f  EV %.1f' % (mcap,netdebt,mcap+netdebt))
def report(label,base,g,eqbase=None,basis='ae'):
    lo=val0(base,R); hi=val(base,g,R); f_lo=val0(base,0.10); f_hi=val(base,g,0.10)
    if basis=='ae':
        ps=lambda v:(v-netdebt)/sh
    else:
        ps=lambda v:v/sh
    print(f'{label}: base {base:.1f} g {g*100:.1f}%  range ${ps(lo):.0f} to ${ps(hi):.0f} (ratio {hi/lo:.2f}); at 10%: ends ${ps(f_lo):.0f} / ${ps(f_hi):.0f}; FAIR ${ps((f_lo+f_hi)/2):.0f}; price ${px}')
    # implied return at price for the growth case: solve r
    target = mcap+netdebt if basis=='ae' else mcap
    lo_r,hi_r=0.0001,0.5
    for _ in range(100):
        mid=(lo_r+hi_r)/2
        if val(base,g,mid)>target: lo_r=mid
        else: hi_r=mid
    print(f'      expected return at price, growth case: {mid*100:.2f}%; no-growth case: {base/target*100:.2f}%')
cut = g_sales  # cap (f) applied below
report('CENTRAL all-equity, maintenance-only, organic pair (serial acquirer)', avg(oc_ae_m), g_org)
report('beside: all-equity, all spending, organic pair', avg(oc_ae), g_org)
report('beside: equity-only, maintenance, organic pair', avg(oc_eq_m), g_org, basis='eq')
report('beside: equity-only, all spending, organic pair', avg(oc_eq), g_org, basis='eq')
report('beside: default pair, acq deducted, total growth cut to sales growth (maint, ae)', avg(oc_ae_m)-avg(acq), cut)
report('beside: maintenance ae ex working-capital release, organic', avg(oc_ae_m)-avg(wc), g_org)
report('beside: literal window, uncut shown growth, maint ae, purchases left out (absurd, shown only)', avg(oc_ae_m), g_shown)
