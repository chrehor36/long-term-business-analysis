import json,sys
sys.stdout.reconfigure(encoding='utf-8')
f=json.load(open('cache/facts.json'))
g=f['facts']['us-gaap']
def ann(tag, fy_only=True):
    if tag not in g: return {}
    out={}
    for u,v in g[tag]['units'].items():
        for x in v:
            if x.get('form') not in ('10-K','10-K/A','8-K'): continue
            if 'start' in x:
                from datetime import date
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if not 340<=(e-s).days<=380: continue
            key=x['end']
            # keep newest filed
            if key not in out or x['filed']>out[key][1]: out[key]=(x['val'],x['filed'],x['form'],x.get('accn'))
    return dict(sorted(out.items()))
tags=sys.argv[1:] or ['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations','ShareBasedCompensation','PaymentsToAcquirePropertyPlantAndEquipment','DepreciationDepletionAndAmortization','DepreciationAndAmortization','Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','GrossProfit','OperatingIncomeLoss','NetIncomeLoss','StockholdersEquity','PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsForRepurchaseOfCommonStock']
for t in tags:
    a=ann(t)
    print('==',t)
    for k,v in a.items(): print('  ',k, v[0]/1e6 if isinstance(v[0],(int,float)) else v[0], v[1], v[2])
