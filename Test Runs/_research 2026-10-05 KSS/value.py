# COMPUTATION - NOT A CLEARANCE. Owner cash = company FCF as filed (OCF + proceeds from financing obligations
# - capex - finance lease and financing obligation payments) less stock pay. USD millions. Fiscal years.
import math
fcf={2012:381,2013:1127,2014:1234,2015:671,2016:1264,2017:881,2018:1403,2019:700,2020:908,2021:1556,2022:-639,2023:519,2024:104,2025:935}
sbc={2012:50,2013:55,2014:48,2015:48,2016:41,2017:55,2018:87,2019:56,2020:40,2021:48,2022:30,2023:42,2024:30,2025:34}
ocf={2016:2148,2017:1691,2018:2107,2019:1657,2020:1338,2021:2271,2022:282,2023:1168,2024:648,2025:1380}
da={2016:938,2017:991,2018:964,2019:917,2020:874,2021:838,2022:808,2023:749,2024:743,2025:700}
oc={y:fcf[y]-sbc[y] for y in fcf}
ocd={y:ocf[y]-sbc[y]-da[y] for y in ocf}
for y in sorted(oc): print(y, 'owner cash (capex+leases)', oc[y], ' D&A variant', ocd.get(y,''))
def mean(d,ys): return sum(d[y] for y in ys)/len(ys)
w5=range(2021,2026); w10=range(2016,2026); w3=range(2023,2026)
print('5yr mean capex',mean(oc,w5),' D&A',mean(ocd,w5))
print('10yr mean capex',mean(oc,w10),' D&A',mean(ocd,w10))
print('3yr mean capex',mean(oc,w3),' D&A',mean(ocd,w3))
# growth shown on aggregate owner cash: least-squares slope of log not possible with negatives; use linear trend
def lin(d,ys):
    ys=list(ys); n=len(ys); xm=sum(ys)/n; ym=sum(d[y] for y in ys)/n
    b=sum((y-xm)*(d[y]-ym) for y in ys)/sum((y-xm)**2 for y in ys); return b,ym
for nm,d,ys in [('5yr capex',oc,w5),('10yr capex',oc,w10),('5yr D&A',ocd,w5),('10yr D&A',ocd,w10)]:
    b,ym=lin(d,ys); print(nm,'linear trend $/yr',round(b,1),' as % of mean',round(100*b/ym,1))
print('endpoint 5yr capex', (oc[2025]/oc[2021])**(1/4)-1, ' 10yr', (oc[2025]/oc[2016])**(1/9)-1)
rev={2016:19681,2021:19433,2025:15527,2011:18804}
print('revenue CAGR 2016-25',(rev[2025]/rev[2016])**(1/9)-1,' 2021-25',(rev[2025]/rev[2021])**(1/4)-1, ' 2011-25',(rev[2025]/rev[2011])**(1/14)-1)
r=0.0563; sh=113.376
def pv(c0,g,r=r,n=10):
    v=0; c=c0
    for t in range(1,n+1):
        c=c*(1+g); v+=c/(1+r)**t
    return v + c/r/(1+r)**n
for label,c0 in [('5yr capex',mean(oc,w5)),('5yr D&A',mean(ocd,w5)),('10yr capex (whole cycle)',mean(oc,w10)),('10yr D&A',mean(ocd,w10))]:
    for g in [0,-0.026,-0.033,-0.055,-0.121]:
        v=pv(c0,g); print(f'{label:26s} c0 {c0:7.1f} g {g:+.3f} value {v:8.0f}M  ${v/sh:6.2f}/sh')
print('--- fair and cheap (COMPUTATION) ---')
t=0.21
def pv_r(c0,g,rr,n=10,perpetual_decline=False):
    if perpetual_decline: return c0*(1+g)/(rr-g)
    return pv(c0,g,r=rr,n=n)
for label,c0 in [('5yr capex',458.2),('5yr D&A',345.4),('10yr capex',716.8)]:
    for g in [0,-0.055,-0.121]:
        v=pv_r(c0/(1-t),g,0.10); print(f'fair @10% pre-tax {label:10s} g {g:+.3f}: {v:7.0f}M ${v/sh:6.2f}')
for label,c0 in [('5yr capex',458.2),('5yr D&A',345.4)]:
    for g in [-0.055,-0.121]:
        v=pv_r(c0,g,r,perpetual_decline=True); print(f'perpetual decline @sovereign {label} g {g}: {v:7.0f}M ${v/sh:6.2f}')
        v=pv_r(c0/(1-t),g,0.10,perpetual_decline=True); print(f'perpetual decline @10% pretax {label} g {g}: {v:7.0f}M ${v/sh:6.2f}')
print('mkt cap at 19.48:',19.48*sh)
