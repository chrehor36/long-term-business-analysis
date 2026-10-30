import json,sys
from datetime import date
REV=['SalesRevenueNet','Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueGoodsNet','RevenueFromContractWithCustomerIncludingAssessedTax']
OI=['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments','IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic']
def ser(f,tags):
    out={}
    for t in tags:
        if t not in f['us-gaap']: continue
        for x in f['us-gaap'][t]['units'].get('USD',[]):
            if x.get('form') not in ('10-K','10-K/A') or 'start' not in x: continue
            d0=date.fromisoformat(x['start']); d1=date.fromisoformat(x['end'])
            if (d1-d0).days<350: continue
            y=d1.year if d1.month>6 else d1.year-1
            out.setdefault(t,{}).setdefault(y,x['val'])
    return out
for name in sys.argv[1:]:
    f=json.load(open(f'peers/{name}_facts.json' if name!='KSS' else 'KSS_facts.json'))['facts']
    r=ser(f,REV); o=ser(f,OI); p=ser(f,['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'])
    years=sorted({y for d in r.values() for y in d})
    print('==',name, 'rev tags:',list(r), 'oi tags:',list(o))
    for y in years:
        rv=max([r[t][y] for t in r if y in r[t]])
        oi=[o[t][y] for t in o if y in o[t]]
        oi=oi[0] if oi else None
        print(f'  FY{y} rev {rv/1e6:,.0f}  opinc/pretax {oi/1e6 if oi else float("nan"):,.0f}  margin {100*oi/rv if oi else float("nan"):.1f}%')
