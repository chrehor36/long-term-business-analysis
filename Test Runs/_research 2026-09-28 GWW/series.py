import json
f=json.load(open('facts.json'))['facts']['us-gaap']
tags=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet','GrossProfit','OperatingIncomeLoss','NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations','PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','DepreciationDepletionAndAmortization','DepreciationAndAmortization','Depreciation','AmortizationOfIntangibleAssets','ShareBasedCompensation','AllocatedShareBasedCompensationExpense','NetIncomeLoss','NetIncomeLossAttributableToNoncontrollingInterest','ProfitLoss','PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividendsMinorityInterest','IncomeTaxesPaidNet','IncomeTaxesPaid','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','InterestExpense','InterestPaidNet','StockholdersEquity','Goodwill','IntangibleAssetsNetExcludingGoodwill','Assets','CashAndCashEquivalentsAtCarryingValue','LongTermDebt','InventoryLIFOReserve','ProceedsFromDivestitureOfBusinesses','PaymentsForProceedsFromOtherInvestingActivities']
out={}
for t in tags:
    if t not in f: continue
    for u,vals in f[t]['units'].items():
        by={}
        for v in vals:
            if v.get('form') not in ('10-K','10-K/A'): continue
            fp=v.get('fp'); 
            if 'start' in v:
                from datetime import date
                s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                if not (330<(e-s).days<400): continue
            y=v['end'][:4]
            # first filed value for that period end
            key=v['end']
            if key not in by or v['filed']<by[key]['filed']: by[key]=v
        ser={k[:4]:round(by[k]['val']/1e6,1) for k in sorted(by)}
        print(t,u,ser)
