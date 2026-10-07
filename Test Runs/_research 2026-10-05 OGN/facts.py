import json
f=json.load(open('facts.json'))['facts']['us-gaap']
tags=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','CostOfGoodsAndServicesSold','SellingGeneralAndAdministrativeExpense','ResearchAndDevelopmentExpense','ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost','RestructuringCharges','InterestExpense','InterestExpenseNonoperating','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeTaxExpenseBenefit','NetIncomeLoss','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','ShareBasedCompensation','DepreciationDepletionAndAmortization','DepreciationAndAmortization','Depreciation','AmortizationOfIntangibleAssets','PaymentsOfDividendsCommonStock','PaymentsOfDividends','PaymentsForRepurchaseOfCommonStock','PaymentsToAcquireBusinessesNetOfCashAcquired','ProceedsFromIssuanceOfLongTermDebt','RepaymentsOfLongTermDebt','IncomeTaxesPaidNet','InterestPaidNet','ImpairmentOfIntangibleAssetsExcludingGoodwill','ResearchAndDevelopmentInProcess','WeightedAverageNumberOfDilutedSharesOutstanding','EarningsPerShareDiluted','GrossProfit','OperatingIncomeLoss']
for t in tags:
    if t not in f: continue
    u=f[t]['units']
    for unit,vals in u.items():
        out={}
        for v in vals:
            if v.get('fp')=='FY' and v['form'].startswith('10-K'):
                # annual duration
                if 'start' in v:
                    from datetime import date
                    s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                    if (e-s).days<350: continue
                out.setdefault(v['end'][:4], v['val'])  # first-filed
        if out: print(t, unit, dict(sorted(out.items())))
