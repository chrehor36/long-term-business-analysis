import json,sys
f=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'facts.json'))
g=f['facts']['us-gaap']
def series(tags, fp='FY', dur=True):
    out={}
    for t in tags:
        if t not in g: continue
        for u,vals in g[t]['units'].items():
            for v in vals:
                if v.get('fp')!=fp or v.get('form') not in ('10-K','10-K/A'): continue
                if dur:
                    if 'start' not in v: continue
                    from datetime import date
                    s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                    if not (350<(e-s).days<380): continue
                end=v['end']
                # keep first-filed per end
                key=end
                if key not in out or v['filed']<out[key][1]:
                    out[key]=(v['val'],v['filed'],t)
    return out
items={
 'Sales':['Revenues','SalesRevenueNet','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueGoodsNet'],
 'GP':['GrossProfit'],
 'OpInc':['OperatingIncomeLoss'],
 'NI':['NetIncomeLoss'],
 'NIcont':['IncomeLossFromContinuingOperations'],
 'OCF':['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],
 'Capex':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
 'SBC':['ShareBasedCompensation'],
 'DA':['DepreciationDepletionAndAmortization','DepreciationAndAmortization'],
 'Buyback':['PaymentsForRepurchaseOfCommonStock'],
 'Acq':['PaymentsToAcquireBusinessesNetOfCashAcquired'],
 'GWimp':['GoodwillImpairmentLoss'],
 'DilSh':['WeightedAverageNumberOfDilutedSharesOutstanding'],
 'Int':['InterestExpense'],
}
res={k:series(v) for k,v in items.items()}
ends=sorted(set(e for r in res.values() for e in r if e>='2007'))
print('end       '+' '.join(f'{k:>9}' for k in items))
for e in ends:
    row=[]
    for k in items:
        v=res[k].get(e)
        row.append(f'{v[0]/1e6:9.1f}' if v and k!='DilSh' else (f'{v[0]/1e6:9.2f}' if v else '        -'))
    print(e, ' '.join(row))
