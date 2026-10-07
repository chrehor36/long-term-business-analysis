# Owner cash = OCF - SBC - capex (USD millions). Sources: S-1 2012 (0001047469-12-010624) for 2009-2011;
# 10-K cash-flow statements (XBRL transcription, checked against filed statements) for 2012-2025.
ocf={2009:-35.2,2010:10.3,2011:-43.0,2012:77.6,2013:33.4,2014:101.8,2015:80.3,2016:151.9,2017:151.6,2018:163.6,2019:245.6,2020:294.5,2021:667.0,2022:1041.2,2023:687.5,2024:438.3,2025:254.1}
sbc={2009:0,2010:0,2011:0,2012:0,2013:2.9,2014:5.9,2015:5.8,2016:8.2,2017:9.7,2018:8.8,2019:8.0,2020:7.8,2021:7.9,2022:11.9,2023:15.4,2024:15.5,2025:12.1}
capex={2009:21.4,2010:35.8,2011:39.3,2012:27.4,2013:45.8,2014:61.2,2015:87.5,2016:83.6,2017:75.5,2018:80.0,2019:82.7,2020:79.4,2021:106.5,2022:114.1,2023:215.4,2024:229.6,2025:241.4}
da={2009:40.9,2010:34.9,2011:37.0,2012:33.4,2013:38.0,2014:51.4,2015:55.6,2016:72.8,2017:80.4,2018:146.8,2019:80.1,2020:95.2,2021:80.8,2022:101.6,2023:132.5,2024:144.1,2025:158.2}
acq={2009:0,2010:0,2011:5.8,2012:2.4,2013:103.0,2014:0,2015:0,2016:215.9,2017:0,2018:25.5,2019:15.7,2020:0,2021:0,2022:515.2,2023:162.8,2024:10.2,2025:33.4}
sales={2009:1973.3,2010:2240.6,2011:2248.1,2012:2779.1,2013:3273.5,2014:3573.7,2015:3633.4,2016:3911.2,2017:4432.0,2018:4995.3,2019:4643.4,2020:5474.8,2021:7926.1,2022:8387.3,2023:6838.2,2024:6724.3,2025:6404.6}
Y=sorted(ocf)
oc={y:ocf[y]-sbc[y]-capex[y] for y in Y}; ocd={y:ocf[y]-sbc[y]-da[y] for y in Y}
print("year   OCF    SBC  capex   D&A   OC(capex) OC(D&A)  acq   sales  OC/sales")
for y in Y: print(f"{y} {ocf[y]:7.1f} {sbc[y]:5.1f} {capex[y]:6.1f} {da[y]:6.1f} {oc[y]:9.1f} {ocd[y]:7.1f} {acq[y]:6.1f} {sales[y]:7.1f} {oc[y]/sales[y]*100:6.2f}%")
w5=[2021,2022,2023,2024,2025]
a5=sum(oc[y] for y in w5)/5; a5d=sum(ocd[y] for y in w5)/5
print("5yr avg OC capex",round(a5,1),"D&A",round(a5d,1))
S=sum(sales.values()); m=sum(oc.values())/S; md=sum(ocd.values())/S; ma=(sum(oc.values())-sum(acq.values()))/S
print("whole span 2009-2025: OC/sales %.3f%%  D&A basis %.3f%%  after acquisitions %.3f%%"%(m*100,md*100,ma*100))
print("simple avg OC 2009-2025",round(sum(oc.values())/len(Y),1), " ex-spike (drop 2021,2022)", round(sum(oc[y] for y in Y if y not in (2021,2022))/(len(Y)-2),1))
# 2012-2025 (post-recession base, 14 yrs)
Y2=[y for y in Y if y>=2012]; S2=sum(sales[y] for y in Y2)
print("2012-2025 OC/sales %.3f%%"%(sum(oc[y] for y in Y2)/S2*100))
r=0.0566; sh=34.891
for base_name,base in (("2025 sales",6404.6),("2021-25 avg sales",sum(sales[y] for y in w5)/5)):
    for nm,mm in (("capex",m),("D&A",md),("after acq",ma)):
        c=base*mm
        print(f"{base_name:18s} {nm:9s} OC={c:6.1f}  no-growth value at {r:.2%} = {c/r:7.0f}M = ${c/r/sh:6.2f}/sh ; at 10% floor EV = {c/0.10:6.0f}M = ${c/0.10/sh:6.2f}/sh")
print()
ex=[y for y in Y if y not in (2021,2022)]
mex=sum(oc[y] for y in ex)/sum(sales[y] for y in ex)
print("ex-spike (no 2021-22) OC/sales %.3f%%"%(mex*100))
price=74.84; mcap=price*sh; nd=450.0-304.8
print(f"mcap {mcap:.0f}  net debt (6/30/26) {nd:.1f}  EV {mcap+nd:.0f}")
base=6404.6
cases={"low: ex-spike margin":mex,"central: whole-span margin":m,"high: D&A basis whole span":md,"after-acquisitions":ma}
for k,mm in cases.items():
    c=base*mm
    v_sov=c/r - nd
    fair=(c/0.10 - nd)/sh
    cheap=(c/0.20 - nd)/sh
    print(f"{k:28s} OC {c:6.1f}  yield on EV {c/(mcap+nd)*100:5.2f}%  value@sov ${v_sov/sh:7.2f}  fair(10% on EV) ${fair:6.2f}  cheap(20%) ${cheap:6.2f}")
# five-year convention
print("5yr convention no-growth top: $%.2f/sh (capex), $%.2f (D&A)"%((a5/r-nd)/sh,(a5d/r-nd)/sh))
g=(oc[2025]/oc[2021])**(1/4)-1
print("shown growth 2021->2025 CAGR %.1f%%"%(g*100))
def pv(c0,g,r,n=10):
    v=0;c=c0
    for t in range(1,n+1):
        c*=1+g; v+=c/(1+r)**t
    v+= c/r/(1+r)**n
    return v
print("shown-growth end (capex):", round((pv(a5,g,r)-nd)/sh,2))
# pre-tax treatment alternative (gross up at 25%)
c=base*m; print("central pre-tax gross-up fair: $%.2f"%((c/0.75/0.10-nd)/sh))
