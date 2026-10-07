# Arithmetic only. Figures from XBRL company facts (first filed), cross-checked to the FY2025 10-K cash flow statement.
ocf={2016:126.9,2017:167.6,2018:160.2,2019:204.8,2020:176.7,2021:212.7,2022:192.3,2023:306.280,2024:285.815,2025:372.029}
sbc={2016:86.3,2017:100.4,2018:114.4,2019:121.5,2020:124.6,2021:151.7,2022:156.1,2023:173.451,2024:158.193,2025:133.993}
cap={2016:23.0,2017:30.2,2018:45.0,2019:37.5,2020:32.0,2021:28.3,2022:32.0,2023:26.847,2024:37.347,2025:48.353}
da ={2016:35.3,2017:41.2,2018:42.8,2019:49.4,2020:50.6,2021:55.7,2022:44.9,2023:42.184,2024:40.407,2025:50.092}
rev={2016:716.1,2017:850.8,2018:942.8,2019:1014.2,2020:872.9,2021:1031.8,2022:1193.5,2023:1337.1,2024:1412.1,2025:1465.0}
oc={y:ocf[y]-sbc[y]-cap[y] for y in ocf}; od={y:ocf[y]-sbc[y]-da[y] for y in ocf}
for y in sorted(oc): print(y, f"rev {rev[y]:7.1f}  OCF {ocf[y]:6.1f} SBC {sbc[y]:6.1f} ({sbc[y]/rev[y]*100:4.1f}% rev, {sbc[y]/ocf[y]*100:4.0f}% OCF) capex {cap[y]:5.1f}  owner cash {oc[y]:6.1f}  D&A basis {od[y]:6.1f}")
m5=sum(oc[y] for y in range(2021,2026))/5; m5d=sum(od[y] for y in range(2021,2026))/5; m10=sum(oc.values())/10
print(f"5-yr mean capex basis {m5:.1f}; D&A basis {m5d:.1f}; 10-yr mean {m10:.1f}")
# TTM to 2026-06-30
ttm=(372.029-156.029+133.638)-(133.993-72.244+56.256)-(48.353-23.555+27.409); print(f"TTM owner cash to 2026-06-30 {ttm:.1f}")
r=0.0563; sh=54.263621; netdebt=100.0-94.142
def value(C,g,r=r,n=10):
    pv=sum(C*(1+g)**t/(1+r)**t for t in range(1,n+1)); term=C*(1+g)**n/r/(1+r)**n; return pv+term
for name,C in [('5-yr',m5),('10-yr whole cycle',m10),('5-yr D&A',m5d)]:
    lo=value(C,0); hi=value(C,r)
    print(f"{name}: C {C:.1f}  no-growth {lo:.0f}M = ${(lo-netdebt)/sh:.2f}/sh ; shown-growth capped at {r:.2%}: {hi:.0f}M = ${(hi-netdebt)/sh:.2f}/sh ; ratio {hi/lo:.2f}")
print("revenue CAGR 2021-2025", (rev[2025]/rev[2021])**(1/4)-1, " 2016-2025",(rev[2025]/rev[2016])**(1/9)-1)
print("owner cash endpoint CAGR 2021-2025",(oc[2025]/oc[2021])**(1/4)-1)
# IRR solve: price at which the stream returns 10%
def price_for_irr(C,g,irr=0.10,n=10):
    return value(C,g,r=irr,n=n)
price=18.52; mcap=price*sh
for name,C,g in [('central: 5-yr mean, half the capped growth',m5,r/2),('5-yr mean, no growth',m5,0),('10-yr mean, no growth',m10,0)]:
    v=price_for_irr(C,g); print(f"{name}: 10% price = {v:.0f}M -> ${(v-netdebt)/sh:.2f}/sh")
# expected return at the price, central case
import math
def irr_at(P,C,g,n=10):
    lo,hi=0.0,1.0
    for _ in range(200):
        mid=(lo+hi)/2
        if value(C,g,r=mid,n=n)>P: lo=mid
        else: hi=mid
    return mid
for name,C,g in [('5-yr, half growth',m5,r/2),('5-yr, no growth',m5,0),('10-yr, no growth',m10,0),('TTM, no growth',ttm,0)]:
    print(f"expected return at ${price} ({mcap+netdebt:.0f}M EV): {name} {irr_at(mcap+netdebt,C,g):.2%}")
print(f"market cap {mcap:.1f}M; EV {mcap+netdebt:.1f}M")
# buybacks and SBC cumulative
bb={2017:12.6,2018:187.4,2019:481.0,2020:24.4,2021:262.9,2022:200.0,2023:200.0,2024:250.9,2025:290.9}
wh={2017:1.2,2018:50.1,2019:42.8,2020:23.6,2021:62.5,2022:61.0,2023:85.2,2024:73.4,2025:56.9}
print("buybacks 2017-2025",sum(bb.values()),"withholding",sum(wh.values()),"SBC 2016-2025",sum(sbc.values()),"OCF-capex 2016-2025",sum(ocf.values())-sum(cap.values()), "owner cash 2016-2025", sum(oc.values()))
