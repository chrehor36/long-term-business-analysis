import json
d=json.load(open('companyfacts.json'))['facts']['us-gaap']
tags=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','GrossProfit','OperatingIncomeLoss','NetIncomeLoss','NetCashProvidedByUsedInOperatingActivities','ShareBasedCompensation','DepreciationDepletionAndAmortization','DepreciationAndAmortization','PaymentsToAcquirePropertyPlantAndEquipment','StockholdersEquity','Goodwill','IntangibleAssetsNetExcludingGoodwill','AmortizationOfIntangibleAssets','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividends','PaymentsOfDividendsCommonStock','OperatingLeasePayments','OperatingLeaseCost','LongTermDebt','LongTermDebtNoncurrent','MinorityInterest','IncomeTaxesPaidNet','IncomeTaxExpenseBenefit','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','PaymentsToAcquireBusinessesNetOfCashAcquired']
out={}
for t in tags:
    if t not in d: continue
    u=d[t]['units']
    for unit,vals in u.items():
        for v in vals:
            if v.get('form') not in ('10-K','10-K/A'): continue
            fp=v.get('fp'); 
            if 'start' in v:
                import datetime
                s=datetime.date.fromisoformat(v['start']); e=datetime.date.fromisoformat(v['end'])
                if not (350<(e-s).days<380): continue
            key=v['end']
            out.setdefault(t,{})
            # keep latest filed
            if key not in out[t] or v['filed']>out[t][key][1]:
                out[t][key]=(v['val'],v['filed'],v['accn'])
json.dump(out,open('xbrl_series.json','w'),indent=0)
for t in out:
    ks=sorted(out[t])
    print(t, ks[0], ks[-1], len(ks))
