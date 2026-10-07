import json, datetime
d=json.load(open('companyfacts.json'))['facts']['us-gaap']
def series(tags, dur=True, latest=True):
    out={}
    for tag in tags:
        if tag not in d: continue
        for unit,rows in d[tag]['units'].items():
            for r in rows:
                if not r['form'].startswith('10-K'): continue
                if dur:
                    if 'start' not in r: continue
                    a=datetime.date.fromisoformat(r['start']); b=datetime.date.fromisoformat(r['end'])
                    if not 350<(b-a).days<380: continue
                y=int(r['end'][:4]) if r['end'][5:7]>='06' else int(r['end'][:4])-1
                key=r['end']
                if key[5:]!='08-31': continue
                prev=out.get(key)
                if prev is None or (latest and r['filed']>prev[1]) or (not latest and r['filed']<prev[1]):
                    out[key]=(r['val']/1e6,r['filed'],tag)
    return {k:v[0] for k,v in sorted(out.items())}
S={
 'rev':series(['Revenues','SalesRevenueNet','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueGoodsNet']),
 'gp':series(['GrossProfit']),
 'oi':series(['OperatingIncomeLoss']),
 'pti':series(['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments']),
 'ni':series(['NetIncomeLoss']),
 'ar':series(['AccountsReceivableNetCurrent'],dur=False),
 'inv':series(['InventoryNet'],dur=False),
 'ppe':series(['PropertyPlantAndEquipmentNet'],dur=False),
 'ap':series(['AccountsPayableCurrent'],dur=False),
 'eq':series(['StockholdersEquity'],dur=False),
 'gw':series(['Goodwill'],dur=False),
 'intang':series(['IntangibleAssetsNetExcludingGoodwill'],dur=False),
 'cash':series(['CashAndCashEquivalentsAtCarryingValue'],dur=False),
 'ltd':series(['LongTermDebtNoncurrent','LongTermDebt'],dur=False),
 'ta':series(['Assets'],dur=False),
}
json.dump(S,open('xbrl_series.json','w'),indent=1)
yrs=sorted(set(k for v in S.values() for k in v))
print('end       '+' '.join(f'{k:>8}' for k in S))
for y in yrs: print(y,' '.join(f'{S[k].get(y,float("nan")):8.1f}' for k in S))
