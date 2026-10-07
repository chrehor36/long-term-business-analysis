import json,sys
def series(d,tags):
    out={}
    for t in tags:
        if t not in d: continue
        for x in list(d[t]['units'].values())[0]:
            if x.get('form','').startswith('10-K') and 'frame' in x and len(x['frame'])==6:
                out.setdefault(x['frame'],x['val'])
    return out
for f in sys.argv[1:]:
    d=json.load(open(f))['facts']['us-gaap']
    rev=series(d,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueServicesNet','SalesRevenueNet'])
    gp=series(d,['GrossProfit'])
    cor=series(d,['CostOfRevenue','CostOfServices','CostOfGoodsAndServicesSold','DirectCostsOfServices'])
    oi=series(d,['OperatingIncomeLoss'])
    ocf=series(d,['NetCashProvidedByUsedInOperatingActivities'])
    sbc=series(d,['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'])
    cap=series(d,['PaymentsToAcquirePropertyPlantAndEquipment'])
    print(f)
    for y in sorted(rev):
        if y<'CY2014': continue
        r=rev[y]; g=gp.get(y) or (r-cor[y] if y in cor else None)
        o=oi.get(y)
        print(y, round(r/1e6), 'GM%' , round(100*g/r,1) if g else '-', 'OM%', round(100*o/r,1) if o else '-', 'OCF',round(ocf.get(y,0)/1e6), 'SBC',round(sbc.get(y,0)/1e6),'capex',round(cap.get(y,0)/1e6))
