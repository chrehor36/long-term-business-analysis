import json,sys
sys.stdout.reconfigure(encoding='utf-8')
def annual(f,tax,tag,forms=('10-K','40-F','20-F')):
    try: units=f['facts'][tax][tag]['units']
    except KeyError: return {}
    out={}
    for u,arr in units.items():
        for r in arr:
            if r.get('form') not in forms: continue
            if 'start' in r:
                from datetime import date
                s=date.fromisoformat(r['start']); e=date.fromisoformat(r['end'])
                if not 340<=(e-s).days<=380: continue
            fy=r['end'][:4]
            # keep latest filed value for each period end
            k=r['end']
            if k not in out or r['filed']>out[k][1]: out[k]=(r['val'],r['filed'],r.get('accn'),u)
    return out
T={'ACM':('us-gaap',['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','OperatingIncomeLoss','NetIncomeLoss','StockholdersEquity','Goodwill','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','ShareBasedCompensation','PaymentsToAcquireBusinessesNetOfCashAcquired']),
   'J':('us-gaap',['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','OperatingIncomeLoss','NetIncomeLoss','StockholdersEquity','Goodwill','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','ShareBasedCompensation','PaymentsToAcquireBusinessesNetOfCashAcquired']),
   'STN':('ifrs-full',['Revenue','ProfitLossFromOperatingActivities','ProfitLoss','Equity','Goodwill','CashFlowsFromUsedInOperatingActivities','GrossProfit'])}
for t,(tax,tags) in T.items():
    f=json.load(open(f'cache/peers/{t}_facts.json'))
    print('=====',t)
    for tag in tags:
        a=annual(f,tax,tag)
        rows=sorted(a.items())[-11:]
        print(tag, ' | '.join(f"{k}:{v[0]/1e6:,.0f}" for k,v in rows), (rows[-1][1][2] if rows else ''))
