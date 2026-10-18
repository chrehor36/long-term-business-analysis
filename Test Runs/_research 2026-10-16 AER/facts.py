import json,sys
from collections import defaultdict
def annual(d,tags,kind='dur'):
    out={}
    for tag in tags:
        f=d['facts'].get('us-gaap',{}).get(tag)
        if not f: continue
        for u,vals in f['units'].items():
            if u!='USD': continue
            for v in vals:
                if v.get('form') not in ('10-K','20-F','10-K/A','20-F/A','10-KT'): continue
                end=v['end']
                if kind=='dur':
                    if 'start' not in v: continue
                    from datetime import date
                    s=date.fromisoformat(v['start']); e=date.fromisoformat(end)
                    if not (330<(e-s).days<400): continue
                yr=end[:7]
                # keep first-filed (earliest filed) value
                if yr not in out or v['filed']<out[yr][1]:
                    out[yr]=(v['val'],v['filed'],tag)
    return out
T={'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','OperatingLeasesIncomeStatementLeaseRevenue'],
 'pti':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments','IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic'],
 'ni':['NetIncomeLoss','ProfitLoss'],
 'int':['InterestExpense','InterestExpenseOperating','InterestExpenseDebt','InterestExpenseNonoperating'],
 'eq':['StockholdersEquity'],'assets':['Assets'],
 'da':['DepreciationDepletionAndAmortization','DepreciationAndAmortization','Depreciation'],
 'ocf':['NetCashProvidedByUsedInOperatingActivities']}
t=sys.argv[1]; d=json.load(open(f'cache/facts_{t}.json'))
res={k:annual(d,v,'inst' if k in('eq','assets') else 'dur') for k,v in T.items()}
yrs=sorted(set(y for r in res.values() for y in r))
print(t,' '.join(f'{k:>9}' for k in T))
for y in yrs:
    if y<'2009': continue
    print(y,' '.join(f"{(res[k][y][0]/1e6 if y in res[k] else float('nan')):9.0f}" for k in T))
