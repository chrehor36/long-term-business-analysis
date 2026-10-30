"""Owner earnings FY1993-FY2026 from the filed cash-flow statements (newest vintage per year), $M.
OCF as filed; SBC per Step 0 (FY1993-1995 unmeasured = 0; FY1996-2002 after-tax pro forma; FY2003-2005 pre-tax pro forma + acquisition-related
face line; FY2006+ face lines); capex = 'Acquisition of property and equipment'; dep = property depreciation
(FY2011+ the filer's rounded 'Depreciation and amortization expenses for property and equipment'; FY1993-2010 the D&A face line less the
income-statement amortization of goodwill and purchased intangibles in operating expenses, which leaves cost-of-sales amortization and
'other noncash items' inside, so the depreciation end is overstated there, i.e. conservative); acq = acquisitions net of cash acquired."""
import json
D={1993:(176.0,0,33.9,13.6,0),1994:(328.3,0,69.8,36.3,0),1995:(442.8,0,151.8,75.0,17.9),1996:(1062.7,41.1,282.8,132.6,0),
1997:(1448,152,332,214,0),1998:(2865,247,429,329-23,0),1999:(4325,536,602,489-61,19),2000:(6141,1119,1086,863-291,-24),
2001:(6392,1691,2271,2236-1055,13),2002:(6587,1520,2641,1957-699,-16),2003:(5319,2226,717,1463-394,-33),2004:(6962,2269,613,1199-242,104),
2005:(7568,1782,692,1020-227,911),2006:(7899,1137,772,1293-393,5399),2007:(10104,965,1251,1413-407,3684),2008:(12089,1112,1268,1744-499,398),
2009:(9897,1231,1005,1768-533,426),2010:(10173,1517,1008,2030-491,5279),2011:(10079,1620,1174,1100,266),2012:(11491,1401,1126,1100,375),
2013:(12894,1120,1160,1200,6766),2014:(12332,1348,1275,1200,2989),2015:(12552,1440,1227,1100,326),2016:(13570,1458,1146,1000,3161),
2017:(13876,1526,964,1100,3324),2018:(13666,1576,834,1100,3006),2019:(15831,1570,909,1000,2175),2020:(15426,1569,770,900,327),
2021:(15454,1761,692,800,7038),2022:(13226,1886,477,800,373),2023:(19886,2353,849,700,301),2024:(10880,3074,670,700,25994),
2025:(14193,3641,905,700,291),2026:(14177,3830,1410,700,516)}
CAP=420674.0; SOV=0.0549; SH=3942.586873
rows={}
print('FY   OCF     SBC   capex  dep   OEcap   OEdep   acq   SBC/OCF')
for y,(o,s,c,d,a) in D.items():
    rows[y]=dict(ocf=o,sbc=s,capex=c,dep=d,acq=a,oec=o-s-c,oed=o-s-d)
    print(y,'%7.1f %6.1f %6.1f %6.1f %8.1f %8.1f %7.1f %5.1f%%'%(o,s,c,d,o-s-c,o-s-d,a,100*s/o))
json.dump(rows,open('oe_rows.json','w'),indent=0)
print()
res=[]
lo,hi=1e18,-1e18
for n in (1,3,5,10,15,20,25,30,34):
    ys=[y for y in range(2027-n,2027)]
    m=lambda k: sum(rows[y][k] for y in ys)/n
    oc,od,acq=m('oec'),m('oed'),m('acq')
    lo=min(lo,oc,od); hi=max(hi,oc,od)
    print(f'{n:2d}y FY{ys[0]}-{ys[-1]}: capex end {oc:9.1f} ({100*oc/CAP:.2f}%)  dep end {od:9.1f} ({100*od/CAP:.2f}%)  acq/yr {acq:8.1f}  capex end less acq {oc-acq:9.1f} ({100*(oc-acq)/CAP:.2f}%)  SBC/OCF {100*m("sbc")/m("ocf"):.1f}%')
print('range all windows both ends', round(lo,1), round(hi,1), '%.2f%%..%.2f%%'%(100*lo/CAP,100*hi/CAP))
# rolling 5y capex end
print('rolling 5y capex-end means:', {y:round(sum(rows[k]['oec'] for k in range(y-4,y+1))/5) for y in range(1997,2027,1)})
# screen reproduction
f=lambda ys,k: sum(rows[y][k] for y in ys)/len(ys)
print('screen oe_bottom 3y FY2023-25 capex end', round(f(range(2023,2026),'oec'),1), ' oe_top 5y FY2021-25 capex end', round(f(range(2021,2026),'oec'),1))
# computation: per share at 10% and at sovereign
for n in (3,5,10):
    ys=range(2027-n,2027)
    for k in ('oec','oed'):
        v=f(ys,k); print(n,k,'at 10%%: $%.0f/sh  at 5.49%%: $%.0f/sh'%(v/0.10/SH, v/SOV/SH))
v5=f(range(2022,2027),'oec'); v5a=v5-f(range(2022,2027),'acq')
print('5y with acquisitions counted', round(v5a,1), 'at 10%% $%.0f at sov $%.0f'%(v5a/0.10/SH, v5a/SOV/SH))
# growth needed: perpetuity g such that yield + g = 10%
for n in (3,5):
    v=f(range(2027-n,2027),'oec'); y0=v/CAP; print(n,'y yield',round(100*y0,2),'growth needed to 10% floor ~',round(100*(0.10-y0),2),' to sov', round(100*(SOV-y0),2))
cumS=sum(r['sbc'] for r in rows.values()); cumO=sum(r['ocf'] for r in rows.values()); print('cum SBC/OCF FY1993-2026 %.1f%%'%(100*cumS/cumO), 'cum acq', sum(r['acq'] for r in rows.values()), 'cum capex', sum(r['capex'] for r in rows.values()), 'cum dep', round(sum(r['dep'] for r in rows.values())))
