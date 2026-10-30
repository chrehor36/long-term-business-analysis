import json
d=json.load(open('cache/facts.json'))
def inst(tag,ns='us-gaap'):
    g=d['facts'].get(ns,{})
    if tag not in g: return {}
    out={}
    for u,v in g[tag]['units'].items():
        for x in v:
            if x.get('form') in ('10-K','10-K/A') and x['end'][5:]=='12-31':
                e=x['end'][:4]
                if e not in out or x['filed']>out[e][1]: out[e]=(x['val'],x['filed'])
    return {k:round(v[0]/1e6) for k,v in out.items() if k>='2015'}
tags=[('Assets','us-gaap'),('StockholdersEquity','us-gaap'),('MinorityInterest','us-gaap'),('RedeemableNoncontrollingInterestEquityCarryingAmount','us-gaap'),('CashAndCashEquivalentsAtCarryingValue','us-gaap'),('RestrictedCashAndCashEquivalentsAtCarryingValue','us-gaap'),('ShortTermInvestments','us-gaap'),('AccountsReceivableNetCurrent','us-gaap'),('InventoryNet','us-gaap'),('Goodwill','us-gaap'),('IntangibleAssetsNetExcludingGoodwill','us-gaap'),('PropertyPlantAndEquipmentNet','us-gaap'),('RetainedEarningsAccumulatedDeficit','us-gaap'),('RecourseDebtCurrent','aes'),('RecourseDebtNonCurrent','aes'),('NonRecourseDebtCurrent','aes'),('NonRecourseDebtNonCurrent','aes'),('TreasuryStockValue','us-gaap'),('AccumulatedOtherComprehensiveIncomeLossNetOfTax','us-gaap')]
yrs=[str(y) for y in range(2015,2026)]
print('item'.ljust(52),' '.join(y.rjust(7) for y in yrs))
for t,ns in tags:
    a=inst(t,ns)
    print(t[:52].ljust(52),' '.join(str(a.get(y,'-')).rjust(7) for y in yrs))
print([k for k in d['facts']['aes'].keys() if 'Debt' in k][:40])
