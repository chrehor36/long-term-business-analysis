import sys; sys.stdout.reconfigure(encoding="utf-8")
def pv(c0,g,r,yrs=10):
    v=0;c=c0
    for t in range(1,yrs+1):
        c*=1+g; v+=c/(1+r)**t
    return v + c/r/(1+r)**yrs   # zero nominal growth after year ten
def irr(c0,g,ev):
    lo,hi=0.0001,0.6
    for _ in range(200):
        m=(lo+hi)/2
        if pv(c0,g,m)>ev: lo=m
        else: hi=m
    return m
yrs=[2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
ocf=[142.0,138.0,176.9,208.5,262.5,304.4,336.2,368.5,358.7,457.7]
sbc=[13.0,13.4,19.6,17.6,19.4,23.1,26.2,28.6,31.2,33.9]
cap=[11.9,9.7,9.7,16.2,12.2,8.6,10.6,26.9,18.1,18.6]
fl=[0,0,0,0,1.3,2.7,4.3,5.6,6.5,7.8]
rev=[2583.5,2753.4,2964.1,3107.3,2994.9,3213.5,3504.0,4522.6,5198.7,5442.6]
intp=[12.6,11.5,15.6,12.3,13.3,10.3,13.4,47.4,36.9,35.0]
acq=[81.3,8.0,68.3,84.2,68.5,84.9,49.1,854.3-109.3,93.7,97.3-2.4-3.9]
eo=[3,1,1,12,23,20,20,21.3,46.1,15.1]
oc=[ocf[i]-sbc[i]-cap[i]-fl[i] for i in range(10)]
print('owner cash by year:'); 
for i in range(10): print(f"  FY{yrs[i]}  OCF {ocf[i]:6.1f} SBC {sbc[i]:5.1f} capex {cap[i]:5.1f} fin.lease {fl[i]:4.1f} -> owner cash {oc[i]:6.1f}  share of revenue {oc[i]/rev[i]*100:4.1f}%  net purchases {acq[i]+eo[i]:6.1f}")
tax=0.274
w=slice(5,10)
base=sum(oc[w])/5; ai=sum(intp[w])/5*(1-tax); ub=base+ai
purch=sum(acq[w])+sum(eo[w])
print(f"5y avg owner cash {base:.1f}; after-tax interest {ai:.1f}; unlevered {ub:.1f}; net purchases FY21-25 {purch:.1f} vs half of owner cash before purchases {sum(oc[w])/2:.1f}")
g_tot=(oc[9]/oc[5])**0.25-1
g_org=(1.041*1.12*1.076*1.032)**0.25-1
g_org26=((1.041*1.12*1.076*1.032)*(3739.374-180)/4112.490)**0.2-1
g_rev=(rev[9]/rev[5])**0.25-1
print(f"growth: total owner cash FY21-25 {g_tot*100:.2f}%  organic revenue FY22-25 (filer) {g_org*100:.2f}%  incl FY26 9M {g_org26*100:.2f}%  revenue total {g_rev*100:.2f}%")
nd=235.0+575.0-230.835+0.072*256.044
sh=256.044; px=34.72; mc=sh*px; ev=mc+nd
print(f"net debt {nd:.1f} (incl. declared dividend {0.072*256.044:.1f}); market cap {mc:.1f}; EV {ev:.1f}")
r=0.0543
def show(lab,c0,g,debt=nd):
    V=pv(c0,g,r); V10=pv(c0,g,0.10)
    print(f"  {lab:40s} c0 {c0:6.1f} g {g*100:5.2f}%  value/sh {(V-debt)/sh:6.2f}  at10%/sh {(V10-debt)/sh:6.2f}  exp.return at price {irr(c0,g,mc+debt)*100:5.2f}%")
    return (V-debt)/sh,(V10-debt)/sh
print('CENTRAL: organic pair, all-equity')
a=show('no growth',ub,0); b=show('organic growth (filer, FY22-25)',ub,g_org)
print(f"  RANGE {a[0]:.2f} to {b[0]:.2f}; width {b[0]/a[0]:.2f}:1; FAIR (avg of 10% ends) {(a[1]+b[1])/2:.2f}")
print('equity-only beside (owner cash after interest vs market value):')
def showe(lab,c0,g):
    V=pv(c0,g,r); V10=pv(c0,g,0.10)
    print(f"  {lab:40s} value/sh {V/sh:6.2f} at10%/sh {V10/sh:6.2f} exp.return {irr(c0,g,mc)*100:5.2f}%"); return V/sh,V10/sh
c=showe('no growth',base,0); d=showe('organic growth',base,g_org)
print(f"  equity-only RANGE {c[0]:.2f} to {d[0]:.2f}; FAIR {(c[1]+d[1])/2:.2f}")
print('variant: organic growth incl FY26 9M decline')
e=show('organic incl FY26',ub,g_org26)
print('DEFAULT pair beside (purchases deducted, total growth):')
db=ub-purch/5
f=show('no growth',db,0); g=show('total growth',db,g_tot)
print(f"  default RANGE {f[0]:.2f} to {g[0]:.2f}; FAIR {(f[1]+g[1])/2:.2f}")
print('after year ten, purchases stop (default top on owner cash before purchases after yr10):')
def pv_switch(c0,c0b,g,r):
    v=0;c=c0;cb=c0b
    for t in range(1,11):
        c*=1+g; cb*=1+g; v+=c/(1+r)**t
    return v+cb/r/(1+r)**10
for lab,gg in [('default no growth, buy-stop after 10',0),('default total growth, buy-stop after 10',g_tot)]:
    V=pv_switch(db,ub,gg,r); V10=pv_switch(db,ub,gg,0.10); print(f"  {lab:40s} value/sh {(V-nd)/sh:6.2f} at10% {(V10-nd)/sh:6.2f}")
print('literal window check FY21-25 four-year base w/o FY25:')
b4=sum(oc[5:9])/4; show('FY21-24 avg, no growth',b4+ai,0)
# cap check
oc10=ub*(1+g_org)**10; rev10=rev[9]*(1+g_org)**10
print(f"cap check: owner cash yr10 {oc10:.0f} on revenue yr10 at same growth {rev10:.0f} = {oc10/rev10*100:.1f}% vs highest share {max(o/rv for o,rv in zip(oc,rev))*100:.1f}%")
