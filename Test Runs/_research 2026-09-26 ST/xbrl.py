import json
d=json.load(open('companyfacts.json'))['facts']
g=d['us-gaap']
tags=['NetCashProvidedByUsedInOperatingActivities','ShareBasedCompensation','AllocatedShareBasedCompensationExpense','PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','Depreciation','AmortizationOfIntangibleAssets','DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet','PaymentsToAcquireBusinessesNetOfCashAcquired','ProceedsFromDivestitureOfBusinesses','ProceedsFromSaleOfProductiveAssets','Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','CostOfRevenue','CostOfGoodsAndServicesSold','OperatingIncomeLoss','InterestPaidNet','InterestPaid','InterestExpense','IncomeTaxesPaidNet','IncomeTaxesPaid','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','NetIncomeLoss','GoodwillImpairmentLoss','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividends','MinorityInterest','FinanceLeasePrincipalPayments','RepaymentsOfLongTermCapitalLeaseObligations','StockholdersEquity','LongTermDebt','Goodwill','IntangibleAssetsNetExcludingGoodwill','PropertyPlantAndEquipmentNet','AccountsReceivableNetCurrent','InventoryNet','AccountsPayableCurrent','CashAndCashEquivalentsAtCarryingValue']
out={}
for t in tags:
    if t not in g: continue
    u=g[t]['units']; k=list(u)[0]
    ser={}
    for f in u[k]:
        if f.get('form') not in ('10-K','10-K/A'): continue
        fy=f['end'][:4]
        if 'start' in f:
            from datetime import date
            s=date.fromisoformat(f['start']); e=date.fromisoformat(f['end'])
            if (e-s).days<350: continue
        ser.setdefault(fy,{})[f['accn']]=f['val']
    out[t]={fy:v for fy,v in sorted(ser.items())}
    print(t, {fy:[round(x/1e6,1) for x in v.values()] for fy,v in sorted(ser.items())})
json.dump(out,open('xbrl_series.json','w'),indent=0)
