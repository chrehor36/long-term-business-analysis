# Owner cash and COMPUTATION (not a clearance). USD millions. Sources: XBRL first-filed 10-K values, cross-checked to FY2025 10-K statements.
yrs   =[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
sales =[798.3,848.3,829.0,952.6,595.4,645.5,928.2,866.6,889.8,893.8,851.6,1072.1,1221.5,1130.6,1277.9,1837.6]
opinc =[37.3,16.5,-25.0,-17.7,14.3,24.7,36.4,34.4,36.4,-26.4,55.3,81.9,111.3,110.7,54.8,-194.0]
impair=[0,1.8,0.9,1.5,0.5,0,12.6,0,0,74.6,0,0,0,0,0,302.3]
ocf   =[89.1,52.9,26.5,43.5,20.8,67.1,86.4,78.6,104.6,96.4,100.8,78.6,98.0,147.1,88.8,164.9]
capex =[14.7,25.3,42.9,37.9,33.8,30.0,37.2,34.6,26.5,24.9,25.7,24.0,33.1,37.4,37.1,62.6]
sbc   =[4.5,4.9,5.6,4.9,3.9,4.3,6.1,5.2,1.9,2.0,0.9,2.0,2.3,2.5,3.0,3.7]
da    =[28.3,34.0,37.7,60.5,33.9,35.2,53.1,57.5,51.8,49.6,47.2,42.7,40.1,42.9,60.3,103.4]
amort =[None,6.3,8.2,8.9,9.1,10.2,16.9,18.4,16.2,15.3,14.3,12.8,11.9,12.1,21.6,39.3]
oc=[o-c-s for o,c,s in zip(ocf,capex,sbc)]
print("year  sales  opinc  op%  op%exImp  OC(capex)  OC/sales  capex/D&A")
for i,y in enumerate(yrs):
    ex=opinc[i]+impair[i]
    print(f"{y} {sales[i]:7.1f} {opinc[i]:6.1f} {100*opinc[i]/sales[i]:5.1f} {100*ex/sales[i]:6.1f} {oc[i]:8.1f} {100*oc[i]/sales[i]:7.1f} {capex[i]/da[i]:6.2f}")
import statistics as st
print("sum OC 2010-2025", round(sum(oc),1), " mean", round(st.mean(oc),1))
print("mean op% exImp 2010-2025", round(st.mean([(opinc[i]+impair[i])/sales[i]*100 for i in range(16)]),2))
print("mean op% exImp 2014-2025 (post-aluminum)", round(st.mean([(opinc[i]+impair[i])/sales[i]*100 for i in range(4,16)]),2))
ocm=[oc[i]/sales[i] for i in range(16)]
print("mean OC/sales 2010-2025", round(100*st.mean(ocm),2), " median", round(100*st.median(ocm),2))
oc5=oc[-5:]; print("OC 2021-2025", [round(x,1) for x in oc5], "mean", round(st.mean(oc5),2))
# depreciation-only variant (amortization of acquired intangibles added back), 2021-2025
dep=[da[i]-amort[i] for i in range(11,16)]
ocd=[ocf[i]-sbc[i]-(da[i]-amort[i]) for i in range(11,16)]
print("OC dep-only 2021-2025", [round(x,1) for x in ocd], "mean", round(st.mean(ocd),2))
ocda=[ocf[i]-sbc[i]-da[i] for i in range(11,16)]
print("OC full D&A 2021-2025", [round(x,1) for x in ocda], "mean", round(st.mean(ocda),2))
# TTM to 2026-07-31
ttm_ocf=164.897-76.643+57.268; ttm_cap=62.642-40.996+33.066; ttm_sbc=3.685-2.762+3.617; ttm_sales=1837.641-1347.795+1373.301
ttm_oc=ttm_ocf-ttm_cap-ttm_sbc
print("TTM sales", round(ttm_sales,1), "OCF", round(ttm_ocf,1), "capex", round(ttm_cap,1), "SBC", round(ttm_sbc,1), "OC", round(ttm_oc,1))
shares=45.826208; price=18.91; mcap=shares*price
print("mcap", round(mcap,1))
r=0.0566
def pv(base,g,rate=r,n=10):
    v=0; c=base
    for t in range(1,n+1):
        c=c*(1+g); v+=c/(1+rate)**t
    term=c/rate/(1+rate)**n   # zero nominal growth after year 10
    return v+term
# shown growth: five-year aggregate OC CAGR and whole-span CAGR
g5=(oc[-1]/oc[-5])**(1/4)-1; g15=(oc[-1]/oc[0])**(1/15)-1
print("growth shown 2021-2025 CAGR", round(100*g5,1), "% ; 2010-2025 CAGR", round(100*g15,2),"%")
base=st.mean(oc5)
for g,lab in [(0,"no growth"),(g15,"whole-span shown growth")]:
    v=pv(base,g); print(f"value ({lab}) {v:7.1f}M  per share {v/shares:6.2f}")
v_abs=pv(base,g5); print(f"(five-year growth {100*g5:.1f}% carried 10 yrs: {v_abs:.0f}M, per share {v_abs/shares:.2f}; year-10 OC {base*(1+g5)**10:.0f}M)")
# whole-cycle variant: whole-span OC/sales on TTM sales, interest adjustment
m=st.mean(ocm)
wc=m*ttm_sales
print("whole-cycle OC = mean OC/sales x TTM sales =", round(wc,1))
# The span 2010-2025 bore little interest until 2024; current interest TTM:
ttm_int=55.812-42.344+36.387
print("TTM interest expense", round(ttm_int,1))
for g,lab in [(0,"no growth"),(g15,"whole-span growth")]:
    v=pv(wc,g); print(f"whole-cycle value ({lab}) {v:7.1f}M per share {v/shares:6.2f}")
print("yield at price: OC5", round(100*base/mcap,2), "% TTM", round(100*ttm_oc/mcap,2), "% whole-cycle", round(100*wc/mcap,2),"%")
# Fair price: OC/ (price*shares) = 10%  (equity basis; OC is after company's tax and interest = buyer's pre-tax receipt)
for lab,b in [("OC5",base),("TTM",ttm_oc),("whole-cycle",wc)]:
    print(f"fair (10% on equity, no growth) {lab}: {b/0.10/shares:6.2f}   cheap (15%): {b/0.15/shares:6.2f}")
# EV basis: unlevered OC = OC + after-tax interest (21% assumed); net debt
netdebt = 663.365-62.094  # total debt 7/31/26 (26.551+636.814) less cash
ul = base + 0.79*ttm_int
ev_fair = ul/0.10
print("net debt", round(netdebt,1), "unlevered OC5 approx", round(ul,1), "EV at 10%", round(ev_fair,1), "equity", round(ev_fair-netdebt,1), "per share", round((ev_fair-netdebt)/shares,2))
print("cum net income 2009-2025: ", round(sum([-137.1,23.1,9.1,-16.5,-11.7,29.2,16.1,-1.9,18.7,26.3,-46.7,38.5,57.0,88.3,82.5,33.1,-250.8]),1))
print("---- whole-cycle at today's debt")
ints=[0.4,0.4,0.5,0.6,0.6,1.0,36.5,9.6,11.1,9.6,5.2,2.5,2.6,8.1,20.6,55.8]
t=0.21
ul_m=st.mean([(oc[i]+(1-t)*ints[i])/sales[i] for i in range(16)])
ulwc=ul_m*ttm_sales; eqwc=ulwc-(1-t)*ttm_int
print("unlevered OC/sales mean", round(100*ul_m,2), "unlevered whole-cycle OC", round(ulwc,1), "equity OC at today's interest", round(eqwc,1))
for g,lab in [(0,"no growth"),(g15,"whole-span growth")]:
    v=pv(eqwc,g); print(f"  value ({lab}) {v:7.1f}M per share {v/shares:6.2f}")
print("  fair 10% equity", round(eqwc/0.10/shares,2), " cheap 15% equity", round(eqwc/0.15/shares,2))
print("  EV basis: fair", round((ulwc/0.10-netdebt)/shares,2), " cheap", round((ulwc/0.15-netdebt)/shares,2))
ul5=base+(1-t)*st.mean(ints[-5:])
print("OC5 unlevered", round(ul5,1), " EV-basis fair", round((ul5/0.10-netdebt)/shares,2), " OC5 at today's interest", round(ul5-(1-t)*ttm_int,1), "fair equity", round((ul5-(1-t)*ttm_int)/0.10/shares,2))
print("expected return at price, OC5 no growth", round(100*base/mcap,2), " with 2.3% growth", round(100*base/mcap+100*g15,2))
print("whole-cycle eq yield at price", round(100*eqwc/mcap,2))
# returns on capital
print("ROTC FY2025: EBITA ex-impairment", round(-194.0+302.3+39.3,1))
