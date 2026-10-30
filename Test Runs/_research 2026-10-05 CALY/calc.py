# CALY run 2026-10-05: arithmetic only. Sources: 10-K FY2025 (0000837465-26-000010), 10-Q Q2 2026 (0000837465-26-000022),
# selected financial data in 10-Ks FY2002/2003/2008/2013/2018, Acushnet and Fortune Brands filings (see run file).
r=0.0566; price=14.28; sh=178.510521
# consolidated golf-era operating income and sales (USD M)
oi={1998:-40.1,1999:79.9,2000:122.1,2001:112.5,2002:110.1,2003:65.9,2004:-24.7,2005:17.2,2006:37.1,2007:90.2,2008:84.2,
    2009:-30.5,2010:-26.6,2011:-81.1,2012:-116.2,2013:-10.8,2014:30.7,2015:26.9,2016:44.2,2017:78.8,2018:128.4,2019:132.7,
    2023:194.1,2024:152.9,2025:128.1}
sales={1998:703.1,1999:719.0,2000:837.6,2001:816.2,2002:792.1,2003:814.0,2004:934.6,2005:998.1,2006:1017.9,2007:1124.6,2008:1117.2,
    2009:950.8,2010:967.7,2011:886.5,2012:834.1,2013:842.8,2014:886.9,2015:843.8,2016:871.2,2017:1048.7,2018:1242.8,2019:1701.1,
    2023:2132.7,2024:2077.7,2025:2060.1}
m={y:oi[y]/sales[y] for y in oi}
for y in sorted(m): print(y, f"{m[y]*100:6.1f}%")
loss=[y for y in oi if oi[y]<0]; print('loss years',loss,len(loss),'of',len(oi))
avg_m=sum(m.values())/len(m); agg_m=sum(oi.values())/sum(sales.values())
print(f"mean margin {avg_m*100:.2f}%  aggregate margin {agg_m*100:.2f}%")
mm=[m[y] for y in range(1998,2020)]; print(f"1998-2019 mean {sum(mm)/len(mm)*100:.2f}%")
# Acushnet / Fortune Brands golf margins
ac={2005:(171.5,1265.8),2006:(166.0,1313.4),2007:(165.5,1405.4),2008:(125.3,1368.9),2009:(25.0,1218.3),2010:(88.7,1241.6),
    2012:(80.2,1451.1),2013:(114.9,1477.2),2014:(104.2,1537.6),2015:(117.6,1503.0),2016:(140.8,1572.3),2017:(169.8,1560.3),2018:(172.3,1633.7),
    2019:(185.7,1681.4),2020:(145.5,1612.2),2021:(259.8,2147.9),2022:(281.5,2270.3),2023:(285.3,2382.0),2024:(304.3,2457.1),2025:(299.4,2558.7)}
for y,(a,b) in sorted(ac.items()): print('GOLF',y,f"{a/b*100:5.1f}%", '  CALY', f"{m[y]*100:5.1f}%" if y in m else '')
am=[a/b for a,b in ac.values()]; print(f"Acushnet mean margin {sum(am)/len(am)*100:.2f}%, min {min(am)*100:.1f}%")
# continuing owner cash
ocf={2023:224.9,2024:166.2,2025:219.7}; sbc={2023:33.3,2024:27.6,2025:23.8}; capex={2023:50.0,2024:48.7,2025:31.8}; da={2023:45.7,2024:44.5,2025:46.4}
intr={2023:70.7,2024:63.0,2025:60.6}; t=0.21
oc={y:ocf[y]-sbc[y]-capex[y] for y in ocf}; ocd={y:ocf[y]-sbc[y]-da[y] for y in ocf}
ocu={y:oc[y]+intr[y]*(1-t) for y in ocf}
for y in ocf: print(y,'OC capex',round(oc[y],1),'OC D&A',round(ocd[y],1),'unlevered',round(ocu[y],1))
mean=lambda d: sum(d.values())/len(d)
C=mean(ocu); print('mean levered',round(mean(oc),1),'mean D&A basis',round(mean(ocd),1),'mean unlevered',round(C,1))
g_shown=(ocu[2025]/ocu[2023])**0.5-1; print('growth shown unlevered owner cash 2023-25',round(g_shown*100,2),'%')
g_sales=(1375.1/1124.6)**(1/18)-1; print('golf equipment sales growth 2007-2025',round(g_sales*100,2),'%')
def val(c,g,r=r,n=10):
    v=0; x=c
    for i in range(1,n+1):
        x*=(1+g); v+=x/(1+r)**i
    v+= x/r/(1+r)**n   # zero nominal growth after year 10
    return v
netcash=278.1-43.1-3.6-4.1; tg=213.9
print('net cash 2026-06-30',round(netcash,1))
for lab,c,g in [('no growth',C,0.0),('capped growth (sales 2007-25)',C,g_sales),('shown growth',C,g_shown)]:
    ev=val(c,g); eq=ev+netcash+tg; print(f"{lab:32s} EV {ev:7.0f} equity {eq:7.0f} per share {eq/sh:6.2f}")
# whole-cycle variant: mean margin over the 25 comparable years on 2025 sales, after 21% tax, D&A~capex
oiw=avg_m*2060.1; cw=oiw*(1-t); print('whole-cycle OI',round(oiw,1),'owner cash',round(cw,1))
for lab,g in [('no growth',0.0),('capped',g_sales)]:
    ev=val(cw,g); eq=ev+netcash+tg; print(f"whole-cycle {lab:10s} EV {ev:7.0f} per share {eq/sh:6.2f}")
oia=agg_m*2060.1; ca=oia*(1-t); print('aggregate-margin owner cash',round(ca,1), 'per share no growth',round((val(ca,0)+netcash+tg)/sh,2))
# fair price: central case clears ~10% pre-tax (owner cash yield on EV + growth)
for lab,c,g in [('central (3yr mean, capped growth)',C,g_sales),('whole-cycle',cw,g_sales)]:
    ev=c/(0.10-g); print(f"FAIR {lab}: EV {ev:.0f} -> per share {(ev+netcash+tg)/sh:.2f}")
# cheap: whole-cycle owner cash, no growth, at 10%
ev=cw/0.10; print('CHEAP whole-cycle no growth at 10%: per share',round((ev+netcash+tg)/sh,2))
print('EV at price', round(price*sh-netcash-tg,0), 'yield on EV central', round(C/(price*sh-netcash-tg)*100,2),'%')
