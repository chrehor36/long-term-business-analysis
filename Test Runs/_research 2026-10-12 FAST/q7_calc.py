# Q7 arithmetic for FAST, figures transcribed from the filed 10-K cash-flow and income statements (USD millions)
# acc: FY2025 0000815556-26-000009 (2023-2025); FY2023 0000815556-24-000009 (2021-2023); FY2022 0000815556-23-000009; FY2020 0000815556-21-000008; earlier from XBRL first-filed vintages
yrs   =[2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
ocf   =[416.1,499.4,550.3,519.9,585.2,674.2,842.7,1101.8,770.1,941.0,1432.7,1173.3,1295.9]
sbc   =[5.4,7.0,5.8,4.1,5.2,5.1,5.7,5.7,5.6,7.2,7.3,8.0,8.4]
capex =[206.5,189.5,155.2,189.5,119.9,176.3,246.4,168.1,156.6,173.8,172.8,226.5,245.3]
procd =[5.0,5.8,9.9,6.5,7.4,9.5,6.6,10.6,8.4,11.4,12.2,12.4,14.8]
acq   =[0,5.6,23.5,0,58.7,3.7,0,125.0,0,0,0,0,0]
da    =[None]*7+[162.4,170.7,176.6,177.3,175.4,179.2]
sales =[3326.1,3733.5,3869.2,3962.0,4390.5,4965.1,5333.7,5647.3,6010.9,6980.6,7346.7,7546.0,8200.5]
intexp=[None]*7+[9.7,9.7,14.3,10.8,7.3,6.2]
intinc=[None]*7+[0.6,0.1,0.7,4.1,5.4,5.5]
TAX=0.24
oc={};ocu={};ocg={};ocd={}
print("year  OCF  ownercash(net capex, acq deducted)  %sales   gross-capex variant   D&A variant")
for i,y in enumerate(yrs):
    o=ocf[i]-sbc[i]-(capex[i]-procd[i])-acq[i]
    oc[y]=o
    ocg[y]=ocf[i]-sbc[i]-capex[i]-acq[i]
    ni=(intexp[i]-intinc[i]) if intexp[i] is not None else None
    if ni is not None: ocu[y]=o+ni*(1-TAX)
    if da[i] is not None: ocd[y]=ocf[i]-sbc[i]-da[i]-acq[i]
    print(y, f"{ocf[i]:8.1f} {o:8.1f} {o/sales[i]*100:6.1f}%  {ocg[y]:8.1f}  {ocd.get(y,float('nan')):8.1f}  unlev {ocu.get(y,float('nan')):8.1f}")
W=[2021,2022,2023,2024,2025]
avg=lambda d:sum(d[y] for y in W)/5
Bu=avg(ocu); Be=avg(oc); Bg=avg(ocg); Bd=avg(ocd)
print(f"\n5-yr avg owner cash: all-equity (before net interest) {Bu:.1f}; equity-only {Be:.1f}; gross-capex {Bg:.1f}; D&A {Bd:.1f}")
g_shown=(oc[2025]/oc[2021])**(1/4)-1
g_sales=(sales[-1]/sales[yrs.index(2021)])**(1/4)-1
print(f"shown growth of aggregate owner cash 2021->2025: {g_shown*100:.2f}%   sales growth 2021->2025: {g_sales*100:.2f}%")
maxshare=max(oc[y]/sales[yrs.index(y)] for y in yrs)
yr10_oc=Bu*(1+g_shown)**10; yr10_sales=sales[-1]*(1+g_sales)**10
print(f"cap test: owner cash yr10 at shown rate {yr10_oc:.0f} vs sales yr10 at sales growth {yr10_sales:.0f} = {yr10_oc/yr10_sales*100:.1f}% of sales; highest share earned {maxshare*100:.1f}%")
g = g_sales if yr10_oc/yr10_sales>maxshare else g_shown
print(f"growth carried: {g*100:.2f}%")
def pv(B,g,r):
    s=sum(B*(1+g)**t/(1+r)**t for t in range(1,11))
    return s + B*(1+g)**10/r/(1+r)**10
R=0.056
NETDEBT=120.0-204.7   # 2026-06-30, 10-Q 0000815556-26-000041
SH=1147.497573; PRICE=51.55
EV=PRICE*SH+NETDEBT
for lab,B in [("all-equity",Bu),("equity-only",Be)]:
    lo=B/R; hi=pv(B,g,R)
    adj = -NETDEBT if lab=="all-equity" else 0.0
    print(f"\n{lab}: B={B:.1f}  no-growth {lo:,.0f}  growth {hi:,.0f}  width {hi/lo:.2f}x")
    print(f"   per share: {(lo+adj)/SH:.2f} to {(hi+adj)/SH:.2f}   against price {PRICE}")
    f0=B/0.10; f1=pv(B,g,0.10); fair=((f0+f1)/2+adj)/SH
    print(f"   at 10%: no-growth {f0:,.0f}, growth {f1:,.0f}; FAIR PRICE {fair:.2f}")
# expected return at the price, growth case, all-equity
def irr(B,g,target):
    lo,hi=-0.05,0.5
    for _ in range(200):
        m=(lo+hi)/2
        if pv(B,g,m)>target: lo=m
        else: hi=m
    return m
print(f"\nmarket EV (all-equity) {EV:,.0f}; market cap {PRICE*SH:,.0f}")
print(f"expected return at price, growth case: {irr(Bu,g,EV)*100:.2f}%; no-growth case: {Bu/EV*100:.2f}%")
print(f"growth case at the SHOWN rate {g_shown*100:.1f}% uncut: value/share {(pv(Bu,g_shown,R)-NETDEBT)/SH:.2f}; return at price {irr(Bu,g_shown,EV)*100:.2f}%")
# cycle construction beside
c1=[2016,2017,2018,2019,2020]; c2=[2021,2022,2023]
a1=sum(ocu.get(y,oc[y]) for y in c1)/5; a2=sum(ocu[y] for y in c2)/3
print(f"\ncycle beside (owner-cash troughs 2016, 2021, 2024): avg 2016-20 {a1:.1f}, avg 2021-23 {a2:.1f}, growth between midpoints (2018->2022) {((a2/a1)**(1/4)-1)*100:.2f}%")
gc=min(g_sales,(a2/a1)**0.25-1)
print(f"   cycle base {a2:.1f}: range/share {(a2/R-NETDEBT)/SH:.2f} to {(pv(a2,gc,R)-NETDEBT)/SH:.2f} (growth {gc*100:.2f}%)")
print(f"D&A variant: range/share {(Bd/R-NETDEBT)/SH:.2f} to {(pv(Bd,g,R)-NETDEBT)/SH:.2f}")
print(f"gross-capex variant: range/share {(Bg/R-NETDEBT)/SH:.2f} to {(pv(Bg,g,R)-NETDEBT)/SH:.2f}")
# variant beside: earnings-based (net income, so working-capital growth not charged), growth at sales rate
ni={2021:925.0,2022:1086.9,2023:1155.0,2024:1150.6,2025:1258.4}
Bn=sum(ni.values())/5
print(f"\nNI-based variant: B={Bn:.1f}; range/share {(Bn/R-NETDEBT)/SH:.2f} to {(pv(Bn,g,R)-NETDEBT)/SH:.2f}; return at price, growth case {irr(Bn,g,EV)*100:.2f}%")
print(f"sovereign-rate check: what growth for 10 yrs then flat would the price need at 5.6%?")
lo,hi=0.0,0.6
for _ in range(200):
    m=(lo+hi)/2
    if pv(Bu,m,R)<EV: lo=m
    else: hi=m
print(f"   implied 10-year growth of owner cash at the long rate: {m*100:.1f}%")
lo,hi=0.0,0.8
for _ in range(200):
    m=(lo+hi)/2
    if pv(Bu,m,0.10)<EV: lo=m
    else: hi=m
print(f"   implied 10-year growth for the floor (10%): {m*100:.1f}%")
