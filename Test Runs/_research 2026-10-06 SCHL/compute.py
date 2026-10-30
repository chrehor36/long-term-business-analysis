# Arithmetic only. Sources: filed cash-flow statements (10-K FY2017, FY2020, FY2023, FY2026) and XBRL first-filed values.
oc = {  # FY: (OCF, SBC, PPE capex, prepub, finance-lease principal)
2017:(142.2,10.1,65.7,26.9,2.0), 2018:(141.5,10.7,121.5,36.1,2.0), 2019:(116.4,8.3,95.0,38.1,2.0),
2020:(2.1,3.8,62.7,28.5,2.0), 2021:(71.0,6.6,47.2,20.7,2.3), 2022:(226.0,7.8,42.0,17.2,2.3),
2023:(148.9,10.5,62.0,26.9,2.3), 2024:(154.6,11.0,58.4,22.8,2.3), 2025:(124.2,9.3,52.2,24.5,1.7),
2026:(50.9,8.5,48.4,17.9,2.1)}
own={y:round(a-b-c-d-e,1) for y,(a,b,c,d,e) in oc.items()}
for y in own: print(y, oc[y], "owner cash", own[y])
m5=sum(own[y] for y in range(2022,2027))/5; m10=sum(own.values())/10
print("5yr mean FY22-26 as filed", round(m5,1), " 10yr mean FY17-26", round(m10,1))
# adjustments disclosed in the filings
gain_tax=41.4   # FY2026 higher net tax payments 'largely attributable to the gain' (10-K MD&A)
refund=48.8     # FY2022 income taxes paid net = -48.8 (refund), XBRL IncomeTaxesPaidNet
slb_pretax=30.1 # FY2025 Adj EBITDA 145.4 less pro forma 115.3 (8-K 2026-07-23 Ex.99.1)
already=(151.5-132.4)   # FY2026 reported less pro forma: the part not yet borne in FY2026
borne_fy26=slb_pretax-already
tax=0.25        # CONVENTION of this run
slb_avg_after=(slb_pretax - borne_fy26/5)*(1-tax)
print("SLB cost borne in FY2026 approx", round(borne_fy26,1), " recast deduction on 5yr mean after tax", round(slb_avg_after,1))
bottom=m5 - refund/5 - slb_avg_after
central=m5 - refund/5 + gain_tax/5 - slb_avg_after
top=m5 + gain_tax/5 - slb_avg_after
print("owner cash cases (after tax): bottom",round(bottom,1)," central",round(central,1)," top",round(top,1))
r=0.0566
shares=18.409444
cash_adj=134.9-80.5-23.0   # May 31 2026 cash less debt, less ~$23M of FY2027 repurchases to Aug 26 (590,895 sh, 8-K 2026-08-27)
def pv(c,g,yrs=10,r=r):
    v=0; x=c
    for t in range(1,yrs+1):
        x=x*(1+g); v+=x/(1+r)**t
    v+= x/r/(1+r)**yrs   # zero nominal growth after year 10
    return v
for name,c in [("bottom",bottom),("central",central),("top",top)]:
    for g in (0.0,-0.006):
        ev=pv(c,g); eq=ev+cash_adj
        print(f"{name} g={g:+.3f}: EV {ev:6.0f}  equity {eq:6.0f}  per share {eq/shares:6.2f}")
# fair price: central case pre-tax owner cash earns 10% on EV (no growth shown)
pre=central/(1-tax); fair_ev=pre/0.10; fair=(fair_ev+cash_adj)/shares
print("central pre-tax",round(pre,1)," fair EV",round(fair_ev)," fair price/share",round(fair,2))
preb=bottom/(1-tax); cheap=(preb/0.15+cash_adj)/shares
print("cheap: bottom pre-tax",round(preb,1)," /15% + net cash -> per share",round(cheap,2))
price=37.41; mcap=price*shares; ev=mcap-cash_adj
print("market cap",round(mcap,1)," EV",round(ev,1)," pre-tax yield central on EV", round(pre/ev*100,2),"%  bottom",round(preb/ev*100,2),"% top",round(top/(1-tax)/ev*100,2),"%")
# margins
rev={2009:1849.3,2010:1912.9,2011:1906.1,2012:2148.8,2013:1792.4,2014:1822.3,2015:1635.8,2016:1672.8,2017:1741.6,2018:1628.4,2019:1653.9,2020:1487.1,2021:1300.3,2022:1642.9,2023:1704.0,2024:1589.7,2025:1625.5,2026:1581.9}
oi={2009:60.6,2010:128.4,2011:100.7,2012:186.3,2013:67.9,2014:63.1,2015:32.9,2016:67.6,2017:88.9,2018:55.6,2019:25.0,2020:-88.5,2021:-22.7,2022:97.4,2023:106.3,2024:14.5,2025:15.8,2026:15.2}
mg={y:oi[y]/rev[y]*100 for y in rev}
print("SCHL op margin", {y:round(v,1) for y,v in mg.items()})
print("SCHL mean FY2009-26", round(sum(mg.values())/len(mg),2), " FY2012-26", round(sum(mg[y] for y in range(2012,2027))/15,2), " sum OI FY2017-26", round(sum(oi[y] for y in range(2017,2027)),1))
hc={2012:(1189,86,27),2013:(1369,142,34),2014:(1434,197,36),2015:(1667,221,52),2016:(1646,185,55),2017:(1636,199,52),2018:(1758,239,52),2019:(1754,252,42),2020:(1666,214,33),2021:(1985,303,36),2022:(2191,306,49),2023:(1979,167,49),2024:(2093,269,54),2025:(2149,296,54),2026:(2288,287,60)}
hm={y:(e-d)/r_*100 for y,(r_,e,d) in hc.items()}
print("HarperCollins EBITDA-D&A margin", {y:round(v,1) for y,v in hm.items()}, "mean", round(sum(hm.values())/len(hm),2))
ss={2009:(793,43),2010:(791,61),2011:(787,83),2012:(790,80),2013:(809,106),2014:(778,100),2015:(780,108),2016:(767,113),2017:(830,126),2018:(825,142),2019:(814,127),2020:(901,141)}
sm={y:o/r_*100 for y,(r_,o) in ss.items()}
print("S&S op margin", {y:round(v,1) for y,v in sm.items()}, "mean", round(sum(sm.values())/len(sm),2))
print("SCHL FY2009-2020 mean", round(sum(mg[y] for y in range(2009,2021))/12,2))
