import json,sys
f=sys.argv[1]
d=json.load(open(f))['facts']
tags=['Assets','StockholdersEquity','CashAndCashEquivalentsAtCarryingValue','AccountsReceivableNetCurrent','Goodwill','IntangibleAssetsNetExcludingGoodwill','LongTermDebtNoncurrent','LongTermDebt','RetainedEarningsAccumulatedDeficit','DeferredRevenueCurrent','ContractWithCustomerLiabilityCurrent','TreasuryStockValue','CommonStockSharesOutstanding']
res={}
for t in tags:
    for ns in ('us-gaap',):
        if t in d.get(ns,{}):
            for u,vals in d[ns][t]['units'].items():
                for v in vals:
                    if v.get('form')!='10-K': continue
                    e=v['end']
                    if e[5:]!='12-31': continue
                    k=(t,e)
                    if k not in res or v['filed']<res[k][1]: res[k]=(v['val'],v['filed'])
ends=sorted(set(e for (_,e) in res))
print('end        '+' '.join(f'{t[:10]:>10}' for t in tags))
for e in ends:
    if e<'2014': continue
    print(e,' '.join(f'{res[(t,e)][0]/1e6:10.1f}' if (t,e) in res else f'{"-":>10}' for t in tags))
