import json, sys
from datetime import date
def series(f, tags):
    g=f['facts'].get('us-gaap',{})
    out={}
    for t in tags:
        if t not in g: continue
        for unit,vals in g[t]['units'].items():
            if unit!='USD': continue
            for v in vals:
                if v.get('form','').startswith('10-K') and 'start' in v:
                    s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                    if (e-s).days<350: continue
                    y=v['end'][:4]
                    out.setdefault(y, (v['val'], v['accn'], t))
    return out
for name in ['VTRS','MYL','PRGO','TEVA']:
    f=json.load(open(f'peers/{name}_facts.json'))
    rev=series(f,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'])
    cogs=series(f,['CostOfGoodsAndServicesSold','CostOfRevenue','CostOfGoodsSold'])
    gp=series(f,['GrossProfit'])
    ocf=series(f,['NetCashProvidedByUsedInOperatingActivities'])
    cap=series(f,['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'])
    print('==',name, f.get('entityName'))
    for y in sorted(rev):
        if y<'2014': continue
        r=rev[y][0]; c=cogs.get(y,(None,))[0]; g=gp.get(y,(None,))[0]
        if g is None and c is not None: g=r-c
        gm = f"{g/r*100:5.1f}%" if g else '  n/a'
        print(y, f"rev {r/1e6:9.0f}", f"GM {gm}", f"OCF {ocf.get(y,(0,))[0]/1e6:7.0f}", f"capex {cap.get(y,(0,))[0]/1e6:6.0f}", rev[y][1], rev[y][2])
