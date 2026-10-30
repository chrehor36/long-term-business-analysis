import json
d=json.load(open('companyfacts.json'))['facts']['us-gaap']
def inst(tag):
    out={}
    if tag not in d: return out
    for u,arr in d[tag]['units'].items():
        for x in arr:
            if x.get('form') in ('10-K',) and 'start' not in x and x['end'][5:] in ('09-30','12-31'):
                out[x['end']]=x['val']
    return out
tags=['AccountsReceivableNetCurrent','ReceivablesNetCurrent','UnbilledContractsReceivable','ContractWithCustomerAssetNetCurrent','InventoryNet','PropertyPlantAndEquipmentNet','AccountsPayableCurrent','CustomerAdvancesCurrent','ContractWithCustomerLiabilityCurrent','ContractWithCustomerLiability','Goodwill','IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet','StockholdersEquity','LongTermDebtNoncurrent','LongTermDebt','DebtCurrent','LongTermDebtCurrent','CashAndCashEquivalentsAtCarryingValue','Assets','EquipmentHeldForRentalNet','DeferredCostsCurrent','CapitalizedContractCostNet','OtherAssetsNoncurrent','LiabilitiesCurrent','AssetsCurrent']
res={}
for t in tags:
    a=inst(t)
    if a:
        res[t]={k:v for k,v in a.items()}
        print(t, {k[:7]:round(v/1e6,1) for k,v in sorted(a.items()) if k>='2007'})
json.dump(res,open('bs.json','w'))
