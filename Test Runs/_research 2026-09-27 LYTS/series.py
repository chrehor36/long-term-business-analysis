import json,datetime,sys
sys.stdout.reconfigure(encoding='utf-8')
F=json.load(open('companyfacts.json'))['facts']['us-gaap']
def ann(tag,inst=False):
    out={}
    if tag not in F: return out
    for unit,vals in F[tag]['units'].items():
        for v in vals:
            if v.get('form') not in ('10-K','10-K/A'): continue
            e=datetime.date.fromisoformat(v['end'])
            if inst:
                if v.get('start'): continue
            else:
                if not v.get('start'): continue
                s=datetime.date.fromisoformat(v['start'])
                if (e-s).days<340: continue
            fy=e.year if e.month>=6 else e.year-1
            if e.month!=6: continue
            k=fy
            # prefer latest filed
            if k not in out or v['filed']>out[k][1]: out[k]=(v['val'],v['filed'],v['accn'])
    return out
flows=['Revenues','SalesRevenueNet','RevenueFromContractWithCustomerIncludingAssessedTax','OperatingIncomeLoss','NetIncomeLoss','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','DepreciationDepletionAndAmortization','Depreciation','AmortizationOfIntangibleAssets','ShareBasedCompensation','AllocatedShareBasedCompensationExpense','PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsToAcquireBusinessesGross','StockIssuedDuringPeriodValueAcquisitions','GoodwillImpairmentLoss','GoodwillAndIntangibleAssetImpairment','IncreaseDecreaseInAccountsPayable','IncreaseDecreaseInInventories','IncreaseDecreaseInAccountsAndNotesReceivable','PaymentsOfDividends','PaymentsOfDividendsCommonStock','ProceedsFromIssuanceOfCommonStock','StockIssuedDuringPeriodValueNewIssues','InterestPaidNet','IncomeTaxesPaidNet','IncomeTaxExpenseBenefit','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','InterestExpense','PaymentsRelatedToTaxWithholdingForShareBasedCompensation','StockIssuedDuringPeriodValueEmployeeBenefitPlan']
insts=['Assets','AssetsCurrent','LiabilitiesCurrent','CashAndCashEquivalentsAtCarryingValue','Goodwill','IntangibleAssetsNetExcludingGoodwill','OtherIntangibleAssetsNet','StockholdersEquity','LongTermDebtNoncurrent','LongTermDebt','LongTermDebtCurrent','LineOfCredit','InventoryNet','AccountsPayableCurrent']
for t in flows+insts:
    d=ann(t, t in insts)
    if not d: print(t,'--'); continue
    print(t, ' '.join(f'{k}:{v[0]/1e6:.1f}' for k,v in sorted(d.items())))
