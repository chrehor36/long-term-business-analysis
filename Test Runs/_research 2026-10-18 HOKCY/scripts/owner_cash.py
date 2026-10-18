# Owner cash and Q7 arithmetic for HOKCY (HK$ millions). Every input is from the annual reports
# (figures as last reported: FY2025/FY2024 from AR2025; FY2023 from AR2024; FY2022 from AR2023; FY2021 from AR2022).
Y = [2021, 2022, 2023, 2024, 2025]
d = {
 # OCF after tax paid, before interest (interest paid is in financing in these statements)
 'ocf':   [10469.5, 9644.7, 10931.7, 9000.3, 10533.0],
 'ppe':   [7273.5, 7724.7, 8359.7, 6435.5, 5096.3],
 'rou':   [1113.2, 596.3, 67.9, 24.6, 35.3],
 'intang':[25.2, 13.4, 0.0, 0.0, 0.0],
 'sales': [93.2+48.6, 61.1+46.5, 73.8+65.5, 107.8+8.8, 22.1+3.4],
 'lease_p':[141.6, 132.5, 491.0, 199.6, 122.2],
 'lease_i':[13.5, 18.9, 28.0, 20.7, 20.3],
 'div_as':[1067.7, 1023.1, 1146.5, 1532.8, 1106.0],
 'div_jv':[508.9, 426.0, 558.3, 603.5, 583.4],
 'div_sec':[153.3, 167.7, 173.6, 149.7, 123.0],
 'int_paid':[1643.8+110.7, 1629.9+111.5, 1970.5+117.6, 2280.2+12.7, 1954.8],
 'nci_div':[612.2, 624.5, 662.6, 594.4, 649.6],
 'da':    [3288.6, 3525.4, 3549.2, 3567.9, 3802.9],
 'rev':   [53563.7, 60953.4, 56971.1, 55472.8, 54326.3],
 'wc':    [-(-385.9-161.7+985.5+92.3+4.4+10.7), -(-401.3-2153.2+1227.4+19.7+12.4+6.8),
           -(147.8+273.0+315.5+43.5+3.6+1.5), -(-116.8-1725.4+1090.4-18.9+24.5+3.4),
           -(-398.4+694.4-64.0-73.1+6.4+3.0)],  # increase in working capital (positive = absorbed)
}
# acquisitions net of disposals (positive = cash out), every investing/financing line for businesses, associates, JVs, NCI
acq = {
 2021: 6255.6+264.0-432.8+118.8+68.8-86.1+295.1+128.5 +50.0 -1232.2 -191.4,
 2022: 100.1+142.2-203.5+60.6+59.9-71.6-104.2+178.7 +34.4 -141.5 -75.0,
 2023: 297.4+58.5-344.1-2.5+78.8+71.0-11.7-329.4+299.5+7.1+2065.6-5398.2-468.3 +37.0 -64.4 -0.4,
 2024: 0.9+206.7-901.2-760.1+81.8-13.5+212.1-25.6+87.9+30.1+30.1-171.2+72.8 +43.3 -29.9,
 2025: 1.2-410.4-1558.5-71.4+56.7+264.6-200.5+232.4+583.3+155.4-65.3+263.7 +50.6 -448.3,
}
oc_pre = []  # owner cash before interest, before acquisitions, all capex deducted, before NCI dividends
for i,y in enumerate(Y):
    v = (d['ocf'][i] + d['div_as'][i] + d['div_jv'][i] + d['div_sec'][i] - d['ppe'][i] - d['rou'][i]
         - d['intang'][i] + d['sales'][i] - d['lease_p'][i] - d['lease_i'][i])
    oc_pre.append(v)
def avg(x): return sum(x)/len(x)
print("year  OCpre  -NCIdiv  -acq  =OC_default | capex  D&A  WCinc  interest")
oc_def=[]; oc_org=[]; oc_maint=[]; oc_eq=[]
for i,y in enumerate(Y):
    a = oc_pre[i]-d['nci_div'][i]
    oc_org.append(a); oc_def.append(a-acq[y])
    capex = d['ppe'][i]+d['rou'][i]+d['intang'][i]-d['sales'][i]
    oc_maint.append(a + capex - d['da'][i])   # maintenance taken as depreciation (proxy, M1998-127)
    oc_eq.append(a-acq[y]-d['int_paid'][i])
    print(y, round(oc_pre[i],1), round(a,1), round(acq[y],1), round(a-acq[y],1), '|', round(capex,1), d['da'][i], round(d['wc'][i],1), round(d['int_paid'][i],1))
for name,s in [('default (acq deducted)',oc_def),('organic (acq left out)',oc_org),('maintenance=D&A, acq left out',oc_maint),('equity-only default',oc_eq)]:
    h1=avg(s[:2]); h2=avg(s[3:]); 
    print(f"{name:32s} 5yr avg {avg(s):9.1f}  first-half(21-22) {h1:8.1f} second-half(24-25) {h2:8.1f} series {[round(x) for x in s]}")
print("revenue CAGR 2021-2025", round(((d['rev'][-1]/d['rev'][0])**0.25-1)*100,2),"%")
print("avg owner cash / avg revenue (default)", round(avg(oc_def)/avg(d['rev'])*100,2),'%')

def value(c,g,r,n=10):
    pv=0; cf=c
    for t in range(1,n+1):
        cf=c*(1+g)**t; pv+=cf/(1+r)**t
    pv+= cf/r/(1+r)**n   # zero nominal growth after year 10
    return pv
import sys
r=0.04246
shares=18659.87
price=7.215
borrow=16669.8+45856.5; cash=8227.3+297.9; sec_cur=1444.2
netdebt=borrow-cash-sec_cur
mcap=shares*price
print("net debt 30 Jun 2026", round(netdebt,1), "mcap", round(mcap,1), "EV", round(mcap+netdebt,1))
for name,s in [('default',oc_def),('organic',oc_org),('maint',oc_maint)]:
    c=avg(s)
    # growth shown: halves method (b) if series changes sign or CAGR meaningless; here use halves over 2.5 years apart? report both
    for g in [0.0]:
        V=value(c,g,r); print(f"{name}: c={c:.1f} g=0  V={V:.0f} per share all-equity {(V-netdebt)/shares:.2f}  at10% {(value(c,g,0.10)-netdebt)/shares:.2f}")
    print(f"  owner-cash yield on EV {c/(mcap+netdebt)*100:.2f}%")
ce=avg(oc_eq)
print(f"equity-only c={ce:.1f}; V(r)={value(ce,0,r):.0f} per share {value(ce,0,r)/shares:.2f}; at 10% {value(ce,0,0.10)/shares:.2f}; yield on mcap {ce/mcap*100:.2f}%")

print("\n==== Q7 RANGE (COMPUTATION) ====")
g_sales=(d['rev'][-1]/d['rev'][0])**0.25-1
org_cagr=(oc_org[-1]/oc_org[0])**0.25-1
print(f"organic owner cash CAGR 2021-25 {org_cagr*100:.2f}%; sales CAGR {g_sales*100:.2f}%")
c_def=avg(oc_def); c_m=avg(oc_maint)
for g in [org_cagr]:
    yr10=c_def*(1+g)**10; print(f"cap test: default carried at {g*100:.1f}% -> year-10 owner cash {yr10:.0f} = {yr10/d['rev'][-1]*100:.1f}% of 2025 sales; highest share earned {max(o/r for o,r in zip(oc_def,d['rev']))*100:.1f}% (default) / {max(o/r for o,r in zip(oc_org,d['rev']))*100:.1f}% (organic)")
cases={'bottom: all spending, acq deducted, growth cut to sales growth':(c_def,g_sales),
       'top: maintenance-only (D&A proxy), no growth':(c_m,0.0),
       'beside: maintenance-only at sales growth':(c_m,g_sales),
       'beside: all spending no growth':(c_def,0.0),
       'beside: organic (acq left out) at sales growth':(avg(oc_org),g_sales)}
EV=mcap+netdebt
for k,(c,g) in cases.items():
    V=value(c,g,r); V10=value(c,g,0.10)
    # expected return at price: solve r such that value(c,g,r)=EV
    lo,hi=0.0001,0.5
    for _ in range(100):
        mid=(lo+hi)/2
        if value(c,g,mid)>EV: lo=mid
        else: hi=mid
    print(f"{k:58s} c={c:7.0f} g={g*100:5.2f}% V@sov={V:8.0f} ps={(V-netdebt)/shares:6.2f} | V@10%ps={(V10-netdebt)/shares:6.2f} | IRR at price {mid*100:5.2f}%")
b=value(c_def,g_sales,0.10); t=value(c_m,0,0.10)
fair_ae=((b-netdebt)+(t-netdebt))/2/shares
# equity-only: subtract avg interest paid
ip=avg(d['int_paid'])
be=value(c_def-ip,g_sales,0.10); te=value(c_m-ip,0,0.10)
fair_eq=(be+te)/2/shares
print(f"avg interest paid {ip:.0f}")
for k,(c,g) in [('eq bottom',(c_def-ip,g_sales)),('eq top',(c_m-ip,0))]:
    lo,hi=0.0001,0.5
    for _ in range(100):
        mid=(lo+hi)/2
        if value(c,g,mid)>mcap: lo=mid
        else: hi=mid
    print(k, round(c), 'V@sov ps', round(value(c,g,r)/shares,2), 'IRR at price', round(mid*100,2))
print(f"FAIR PRICE all-equity HK${fair_ae:.2f}  equity-only HK${fair_eq:.2f}  price HK${price}")
fx=0.12742
print(f"per ADS (1 share) US${fair_ae*fx:.3f} all-equity, US${fair_eq*fx:.3f} equity-only")
# NCI at book instead of dividends
nci=12542.3
c_def2=avg([oc_def[i]+d['nci_div'][i] for i in range(5)]); c_m2=avg([oc_maint[i]+d['nci_div'][i] for i in range(5)])
b2=value(c_def2,g_sales,0.10)-netdebt-nci; t2=value(c_m2,0,0.10)-netdebt-nci
print(f"beside: NCI at book deducted instead of NCI dividends: fair all-equity HK${(b2+t2)/2/shares:.2f}; range ps {(value(c_def2,g_sales,r)-netdebt-nci)/shares:.2f} to {(value(c_m2,0,r)-netdebt-nci)/shares:.2f}")
# RMB sovereign sensitivity
for rr in [0.0206, 0.03986]:
    print(f"sensitivity sovereign {rr*100:.3f}%: range ps {(value(c_def,g_sales,rr)-netdebt)/shares:.2f} to {(value(c_m,0,rr)-netdebt)/shares:.2f}")
# literal window: no adjustment needed (same window). Interest tax shield estimate
print("interest tax shield est at 16.5%-25%:", round(ip*0.165), "-", round(ip*0.25))

print("\n==== FINAL RANGE AS WRITTEN IN THE RUN ====")
def irr(c,g,target):
    lo,hi=0.0001,0.6
    for _ in range(200):
        mid=(lo+hi)/2
        if value(c,g,mid)>target: lo=mid
        else: hi=mid
    return mid
g_m=(oc_maint[-1]/oc_maint[0])**0.25-1
print("maintenance series CAGR", round(g_m*100,2))
ends={'bottom all-spending no growth':(c_def,0.0),'top maintenance no growth':(c_m,0.0),
      'beside maintenance at own decline':(c_m,g_m),'beside all-spending at sales growth':(c_def,g_sales)}
for k,(c,g) in ends.items():
    print(f"{k:38s} V={value(c,g,r):8.0f} ps={(value(c,g,r)-netdebt)/shares:5.2f} @10% ps={(value(c,g,0.1)-netdebt)/shares:5.2f} IRR@price={irr(c,g,EV)*100:5.2f}%")
fa=((value(c_def,0,0.1)-netdebt)+(value(c_m,0,0.1)-netdebt))/2/shares
fe=(value(c_def-ip,0,0.1)+value(c_m-ip,0,0.1))/2/shares
print(f"fair all-equity {fa:.3f} equity-only {fe:.3f}; per ADS USD {fa*0.12742:.3f} / {fe*0.12742:.3f}")
print("eq-only range ps", round(value(c_def-ip,0,r)/shares,2), round(value(c_m-ip,0,r)/shares,2), "IRR top", round(irr(c_m-ip,0,mcap)*100,2))
# growth needed for the top case to earn 10% at the price
lo,hi=0,1
for _ in range(200):
    mid=(lo+hi)/2
    if value(c_m,mid,0.10)<EV: lo=mid
    else: hi=mid
print("ten-year growth needed for maintenance case to earn 10% at price:", round(mid*100,1),"% a year; year-10 owner cash", round(c_m*(1+mid)**10), "vs 2025 revenue", d['rev'][-1])
print("\n==== checks for the write-up ====")
print("at 3.986%: bottom ps", round((value(c_def,0,0.03986)-netdebt)/shares,2), "top ps", round((value(c_m,0,0.03986)-netdebt)/shares,2))
print("eq-only bottom IRR no growth", round(irr(c_def-ip,0,mcap)*100,2))
