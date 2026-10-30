import json
cf=json.load(open('companyfacts.json'))['facts']['us-gaap']
tags=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','OperatingIncomeLoss','NetIncomeLoss','NetCashProvidedByUsedInOperatingActivities','ShareBasedCompensation','PaymentsToAcquirePropertyPlantAndEquipment','DepreciationDepletionAndAmortization','DepreciationAndAmortization','Depreciation','AmortizationOfIntangibleAssets','IncreaseDecreaseInAccountsPayable','IncreaseDecreaseInAccountsReceivable','IncreaseDecreaseInInventories','StockholdersEquity','LongTermDebt','Goodwill','IntangibleAssetsNetExcludingGoodwill','GrossProfit','MinorityInterest','NetIncomeLossAttributableToNoncontrollingInterest']
out={}
for t in tags:
    if t not in cf: continue
    for u,v in cf[t]['units'].items():
        d={}
        for x in v:
            if x.get('form') not in ('10-K','10-K/A'): continue
            if 'start' in x:
                import datetime
                a=datetime.date.fromisoformat(x['start']);b=datetime.date.fromisoformat(x['end'])
                if not (350<(b-a).days<380): continue
            d[x['end'][:4]]=x['val']
        out[t]=d
        print(t, {k:round(v/1e6,2) for k,v in sorted(d.items())})
json.dump(out,open('xbrl_series.json','w'),indent=0)
