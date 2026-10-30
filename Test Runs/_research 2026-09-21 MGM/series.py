import json, io, sys
f = json.load(io.open('companyfacts.json', encoding='utf-8'))
us = f['facts'].get('us-gaap', {})
def annual(tag, forms=('10-K',), lo=340, hi=380, vintage='newest'):
    out = {}
    if tag not in us: return out
    for unit, items in us[tag]['units'].items():
        for it in items:
            if it.get('form') not in forms: continue
            s, e = it.get('start'), it.get('end')
            if s:
                from datetime import date
                d0 = date(*map(int, s.split('-'))); d1 = date(*map(int, e.split('-')))
                n = (d1-d0).days
                if not (lo <= n <= hi): continue
            fy = e[:4] if e[5:7] in ('12','01') else e[:4]
            key = e
            prev = out.get(key)
            if prev is None or it.get('filed','') > prev[1]:
                out[key] = (it['val'], it.get('filed',''), it.get('accn',''))
    return {k: v[0] for k, v in sorted(out.items())}
def inst(tag):
    out = {}
    if tag not in us: return out
    for unit, items in us[tag]['units'].items():
        for it in items:
            if it.get('form') not in ('10-K',): continue
            e = it['end']
            prev = out.get(e)
            if prev is None or it.get('filed','') > prev[1]:
                out[e] = (it['val'], it.get('filed',''))
    return {k: v[0] for k, v in sorted(out.items())}
tags = {
 'OCF': 'NetCashProvidedByUsedInOperatingActivities',
 'OCF_cont': 'NetCashProvidedByUsedInOperatingActivitiesContinuingOperations',
 'CAPEX': 'PaymentsToAcquirePropertyPlantAndEquipment',
 'DA': 'DepreciationDepletionAndAmortization',
 'DA2': 'DepreciationAmortizationAndAccretionNet',
 'SBC': 'ShareBasedCompensation',
 'NI': 'ProfitLoss',
 'NI_parent': 'NetIncomeLoss',
 'NCI': 'NetIncomeLossAttributableToNoncontrollingInterest',
 'REV': 'Revenues',
 'OPINC': 'OperatingIncomeLoss',
 'AP_AL': 'IncreaseDecreaseInAccountsPayableAndAccruedLiabilities',
 'DIST_NCI': 'PaymentsOfDistributionsToAffiliates',
 'BUYBACK': 'PaymentsForRepurchaseOfCommonStock',
 'OPLEASECOST': 'OperatingLeaseCost',
 'OPLEASECASH': 'OperatingLeasePayments',
}
res = {}
for k, t in tags.items():
    res[k] = annual(t)
for k in ('EQUITY','EQUITY_PARENT','EQUITY_NCI','DEBT','CASH','OPLEASELIAB','OPLEASELIAB_NC','GOODWILL','PPE'):
    pass
insts = {
 'EQUITY_TOTAL':'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest',
 'EQUITY_PARENT':'StockholdersEquity',
 'EQUITY_NCI':'MinorityInterest',
 'DEBT_LT':'LongTermDebtNoncurrent',
 'CASH':'CashAndCashEquivalentsAtCarryingValue',
 'OPLEASELIAB_NC':'OperatingLeaseLiabilityNoncurrent',
 'PPE':'PropertyPlantAndEquipmentNet',
 'GOODWILL':'Goodwill',
 'SHARES':'CommonStockSharesOutstanding',
}
for k,t in insts.items(): res[k]=inst(t)
json.dump(res, io.open('series.json','w',encoding='utf-8'), indent=1)
years = sorted({y for k in res for y in res[k]})
hdr = ['date'] + list(res.keys())
print(','.join(hdr))
for y in years:
    if not y.endswith(('-12-31','-12-30','-01-01')): continue
    row=[y]+[('%.1f'%(res[k][y]/1e6) if y in res[k] else '') for k in res]
    print(','.join(row))
