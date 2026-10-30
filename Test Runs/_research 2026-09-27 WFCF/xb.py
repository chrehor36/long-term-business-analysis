import json
cf=json.load(open('companyfacts.json'))
g=cf['facts'].get('us-gaap',{})
def annual(tag):
    if tag not in g: return {}
    out={}
    for unit,vals in g[tag]['units'].items():
        for v in vals:
            if v.get('fp')=='FY' and v.get('form','').startswith('10-K'):
                fy=v['end'][:4]
                if 'start' in v:
                    from datetime import date
                    s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                    if (e-s).days<350: continue
                # newest filed wins
                if fy not in out or v['filed']>out[fy][1]: out[fy]=(v['val'],v['filed'])
    return {k:v[0] for k,v in sorted(out.items())}
tags=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueServicesNet','GrossProfit','OperatingIncomeLoss','NetIncomeLoss','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeTaxesPaidNet','IncomeTaxExpenseBenefit','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToDevelopSoftware','PaymentsToAcquireProductiveAssets','PaymentsToAcquireIntangibleAssets','DepreciationDepletionAndAmortization','DepreciationAndAmortization','Depreciation','AmortizationOfIntangibleAssets','ShareBasedCompensation','AllocatedShareBasedCompensationExpense','PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsToAcquireBusinessesGross','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividends','PaymentsOfDividendsCommonStock','ProceedsFromIssuanceOfCommonStock','ProceedsFromStockOptionsExercised','Assets','StockholdersEquity','Goodwill','CashAndCashEquivalentsAtCarryingValue','LiabilitiesCurrent','AssetsCurrent','IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet','LongTermDebt','WeightedAverageNumberOfSharesOutstandingBasic','PaymentsToAcquireEquityMethodInvestments','PaymentsToAcquireInvestments','IncomeLossFromEquityMethodInvestments','OperatingLeasePayments','InterestPaidNet']
res={}
for t in tags:
    a=annual(t)
    if a: res[t]=a; print(t, {k:(round(v/1e3) if abs(v)>1e4 else v) for k,v in a.items()})
json.dump(res,open('xb.json','w'),indent=1)
print([k for k in g.keys() if 'Share' in k or 'Stock' in k and 'Comp' in k][:60])
