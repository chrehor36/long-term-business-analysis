# Q7 arithmetic for the CHD run of 2026-10-07. USD millions. Inputs from the filed statements (see run file).
R=0.0564; FLOOR=0.10; SH=237.204; PRICE=96.54
NETDEBT=49.9+2206.3-254.8   # 10-Q 2026-06-30: short-term borrowings + long-term debt - cash; no finance leases found
yrs=list(range(2016,2026))
OCF=[655.3,681.5,763.6,864.5,990.3,993.8,885.2,1030.6,1156.2,1215.4]
SBC=[16.0,18.1,23.3,20.8,21.5,23.7,32.3,63.6,59.2,58.0]
CAPEX=[49.8,45.0,60.4,73.7,98.9,118.8,178.8,223.5,179.8,122.4]
DEP=[59.7,60.9,64.4,63.8,66.2,68.4,67.0,72.8,83.2,89.7]          # depreciation of plant only
INTX=[27.7,52.6,79.4,73.6,61.0,54.5,89.6,110.9,95.0,95.2]
INTI=[0,0,0,0,0,0,0,13.0,26.3,23.5]                              # interest income where filed separately
TAXR=[0.350,0.350,0.210,0.204,0.193,0.198,0.209,0.219,0.226,0.230] # effective; 2017 statutory 35% (effective negative from tax reform)
ACQ=[305.3,1260.0,49.8,475.0,512.7,556.0,546.8,0.0,19.9,656.0]
DIV=[0,0,0,0,7.0,0,0,0,6.6,160.3]
n=len(yrs)
oc_all=[OCF[i]-SBC[i]-CAPEX[i] for i in range(n)]
oc_m=[OCF[i]-SBC[i]-DEP[i] for i in range(n)]
ati=[(INTX[i]-INTI[i])*(1-TAXR[i]) for i in range(n)]
u_all=[oc_all[i]+ati[i] for i in range(n)]
u_m=[oc_m[i]+ati[i] for i in range(n)]
nacq=[ACQ[i]-DIV[i] for i in range(n)]
avg=lambda x:sum(x)/len(x)
def cagr(a,b,k): return (b/a)**(1/k)-1
def pv(c0,g,r,years=10):
    v=0; c=c0
    for t in range(1,years+1):
        c=c*(1+g); v+=c/(1+r)**t
    return v + c/r/(1+r)**years
def irr(c0,g,ev):
    lo,hi=0.001,1.0
    for _ in range(200):
        m=(lo+hi)/2
        if pv(c0,g,m)>ev: lo=m
        else: hi=m
    return m
def ps(ev,nd=NETDEBT): return (ev-nd)/SH
print('year  OC_all  OC_maint  aftertax_int  U_all  U_maint  net_acq')
for i in range(n): print(yrs[i], round(oc_all[i],1), round(oc_m[i],1), round(ati[i],1), round(u_all[i],1), round(u_m[i],1), round(nacq[i],1))
EVP=PRICE*SH+NETDEBT
print(f'\nnet debt {NETDEBT:.1f}  market cap {PRICE*SH:.0f}  EV at price {EVP:.0f}')
def block(label, sl, k):
    ua=avg(u_all[sl]); um=avg(u_m[sl]); na=avg(nacq[sl])
    g_tot=cagr(u_all[sl][0],u_all[sl][-1],k)
    g_org=0.0324 if label.startswith('5') else 0.0402
    A=pv(um,0,R); B=pv(ua-na,g_tot,R); C=pv(ua,g_org,R)
    print(f'\n== {label}: avg U_all {ua:.1f}  avg U_maint {um:.1f}  avg net acquisitions {na:.1f}  total growth {g_tot*100:.2f}%  organic {g_org*100:.2f}%')
    for nm,cash,g,ev in [('A no growth, maintenance only',um,0,A),('B total growth, purchases deducted',ua-na,g_tot,B),('C organic growth, purchases left out',ua,g_org,C)]:
        print(f'  {nm:40s} cash {cash:7.1f} g {g*100:5.2f}%  EV {ev:8.0f}  per share ${ps(ev):6.2f}  IRR at price {irr(cash,g,EVP)*100:5.2f}%  EV at 10% {pv(cash,g,FLOOR):7.0f}')
    lo,hi=min(A,B),max(A,B)
    print(f'  default range (B..A): ${ps(lo):.2f} to ${ps(hi):.2f}  ratio {hi/lo:.2f}; organic pair (A..C): ${ps(A):.2f} to ${ps(C):.2f}')
    # fair price: midpoint case = mean of the two end cash streams, discounted at the floor
    fairD=(pv(um,0,FLOOR)+pv(ua-na,g_tot,FLOOR))/2
    fairO=(pv(um,0,FLOOR)+pv(ua,g_org,FLOOR))/2
    print(f'  FAIR (all-equity) default pair ${ps(fairD):.2f}; organic pair ${ps(fairO):.2f}')
    return um,ua,na,g_tot,g_org
um,ua,na,g,go=block('5-year window 2021-2025', slice(5,10), 4)
block('10-year whole-cycle variant 2016-2025', slice(0,10), 9)
# equity-only beside (5-year): levered owner cash against market cap
lm=avg(oc_m[5:]); la=avg(oc_all[5:]); gl=cagr(oc_all[5],oc_all[9],4)
A=pv(lm,0,R); B=pv(la-na,gl,R); C=pv(la,0.0324,R)
print(f'\n== equity-only (5-yr): avg OC_maint {lm:.1f} avg OC_all {la:.1f} growth {gl*100:.2f}%')
for nm,cash,gg,ev in [('A',lm,0,A),('B',la-na,gl,B),('C',la,0.0324,C)]:
    print(f'  {nm} equity value {ev:8.0f} per share ${ev/SH:6.2f}  IRR at market cap {irr(cash,gg,PRICE*SH)*100:5.2f}%')
fairE=(pv(lm,0,FLOOR)+pv(la-na,gl,FLOOR))/2
fairEO=(pv(lm,0,FLOOR)+pv(la,0.0324,FLOOR))/2
print(f'  FAIR (equity-only) default ${fairE/SH:.2f}; organic ${fairEO/SH:.2f}')
