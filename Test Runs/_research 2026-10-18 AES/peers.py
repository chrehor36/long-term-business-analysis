import json,sys
from datetime import date
def annual(d,tag):
    for ns in ('us-gaap',):
        g=d['facts'].get(ns,{})
        if tag not in g: return {}
        out={}
        for u,v in g[tag]['units'].items():
            for x in v:
                if x.get('form') in ('10-K','10-K/A') and x.get('fp')=='FY':
                    if 'start' in x and (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<350: continue
                    e=x['end'][:4]
                    if e not in out or x['filed']>out[e][1]: out[e]=(x['val'],x['filed'])
        return {k:v[0]/1e6 for k,v in out.items()}
tags=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','NetIncomeLoss','StockholdersEquity','LongTermDebt','LongTermDebtNoncurrent']
for t in sys.argv[1:]:
    d=json.load(open(f'cache/{t}.json' if t=='facts' else f'cache/peers/{t}.json'))
    print('==',t)
    for tag in tags:
        a=annual(d,tag)
        print(' ',tag,{k:round(v) for k,v in sorted(a.items()) if k>='2016'})
