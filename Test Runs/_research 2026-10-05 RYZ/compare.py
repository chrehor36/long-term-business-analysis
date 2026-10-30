import json, statistics as st
from series import series
from ryz_table import R
ryz_assets={2009:1775.8,2010:2053.5,2011:2058.4,2012:1954.1,2013:1951.8,2014:1855.6,2015:1545.2,2016:1558.7,2017:1711.9,2018:2086.3,2019:2022,2020:1802,2021:2366,2022:2334,2023:2570,2024:2440,2025:2405}
def get(t,tags):
    o=series(f'peers/{t}_facts.json',tags); m={}
    for k in tags:
        for y,v in o.get(k,{}).items(): m.setdefault(y,v/1e6)
    return m
rows={}
for t,revtags in [('RS',['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','SalesRevenueNet']),('ZEUS',['RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueGoodsNet','SalesRevenueNet']),('WS',['Revenues'])]:
    rev=get(t,revtags); op=get(t,['OperatingIncomeLoss']); at=get(t,['Assets'])
    ocf=get(t,['NetCashProvidedByUsedInOperatingActivities']); cx=get(t,['PaymentsToAcquirePropertyPlantAndEquipment'])
    rows[t]=(rev,op,at,ocf,cx)
print('year  RYZ_opm  RS_opm  ZEUS_opm  WS_opm | RYZ_op/assets RS_op/assets ZEUS_op/assets WS')
agg={k:[] for k in ['r','rs','z','w','ra','rsa','za','wa']}
for y in range(2009,2026):
    r=R[y][2]/R[y][0]*100; ra=R[y][2]/ryz_assets[y]*100
    out=[y,round(r,1)]
    vals=[]
    for t in ['RS','ZEUS','WS']:
        rev,op,at,_,_=rows[t]
        out.append(round(op[y]/rev[y]*100,1) if y in op and y in rev else None)
    out.append('|'); out.append(round(ra,1))
    for t in ['RS','ZEUS','WS']:
        rev,op,at,_,_=rows[t]
        out.append(round(op[y]/at[y]*100,1) if y in op and y in at else None)
    print(*out)
# span averages over common years
def span(t,y0,y1):
    rev,op,at,ocf,cx=rows[t]
    ys=[y for y in range(y0,y1+1) if y in op and y in rev]
    return ys, sum(op[y] for y in ys)/sum(rev[y] for y in ys)*100, sum(op[y] for y in ys)/sum(at[y] for y in ys if y in at)*100 if all(y in at for y in ys) else None
for t,y0,y1 in [('RS',2009,2025),('ZEUS',2011,2024),('WS',2021,2025)]:
    ys,m,a=span(t,y0,y1)
    ys2=[y for y in ys]
    rm=sum(R[y][2] for y in ys2)/sum(R[y][0] for y in ys2)*100
    ra=sum(R[y][2] for y in ys2)/sum(ryz_assets[y] for y in ys2)*100
    print(f'{t} {ys2[0]}-{ys2[-1]}: peer opm {m:.2f}% vs RYZ {rm:.2f}% ; peer op/assets {a if a is None else round(a,2)}% vs RYZ {ra:.2f}%')
# ZEUS losses years
rev,op,at,ocf,cx=rows['ZEUS']; print('ZEUS op by year',{y:round(op[y],1) for y in sorted(op)})
print('ZEUS OCF-capex 2020-24', round(sum(ocf[y]-cx[y] for y in range(2020,2025)),1))
rev,op,at,ocf,cx=rows['RS']; print('RS OCF-capex sum 2015-2025', round(sum(ocf[y]-cx[y] for y in range(2015,2026)),1), 'RS rev 2025',rev[2025])
