import json,sys
d=json.load(open('cache/facts.json'))
g=d['facts']['us-gaap']
def ann(tag,unit='USD'):
    if tag not in g: return {}
    out={}
    for u,rows in g[tag]['units'].items():
        if u!=unit: continue
        for r in rows:
            if r.get('form') not in ('10-K','10-K/A'): continue
            if 'frame' in r and len(r.get('frame',''))>6: continue
            s,e=r.get('start'),r['end']
            if s:
                from datetime import date
                ds=date.fromisoformat(s); de=date.fromisoformat(e)
                if (de-ds).days<350: continue
            fy=int(e[:4])
            # newest vintage
            if fy not in out or r['filed']>out[fy][1]: out[fy]=(r['val'],r['filed'])
    return {k:v[0] for k,v in sorted(out.items())}
tags=sys.argv[1:] or ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','CostOfRevenue','CostOfGoodsAndServicesSold','GrossProfit','OperatingIncomeLoss','NetIncomeLoss','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToDevelopSoftware','PaymentsToAcquireIntangibleAssets','ShareBasedCompensation','DepreciationDepletionAndAmortization','DepreciationAndAmortization','Depreciation','AmortizationOfIntangibleAssets','PaymentsToAcquireBusinessesNetOfCashAcquired','IncreaseDecreaseInInventories','IncreaseDecreaseInAccountsPayableAndAccruedLiabilities','IncreaseDecreaseInAccountsPayable','IncreaseDecreaseInAccountsReceivable','InventoryNet','AccountsReceivableNetCurrent','AccountsPayableCurrent','PropertyPlantAndEquipmentNet','Goodwill','IntangibleAssetsNetExcludingGoodwill','Assets','StockholdersEquity','CashAndCashEquivalentsAtCarryingValue','LongTermDebt','IncomeTaxesPaidNet','IncomeTaxExpenseBenefit','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','PaymentsForRepurchaseOfCommonStock','OperatingLeaseRightOfUseAsset','OperatingLeaseLiability','ResearchAndDevelopmentExpense','SellingGeneralAndAdministrativeExpense','InterestPaidNet']
for t in tags:
    a=ann(t)
    if a: print(t, {k:round(v/1e6,2) for k,v in a.items()})
    else: print(t,'--')
