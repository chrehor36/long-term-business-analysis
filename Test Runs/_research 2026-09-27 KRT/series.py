import json,datetime,sys
sys.stdout.reconfigure(encoding='utf-8')
F=json.load(open('companyfacts.json'))['facts']
G=F['us-gaap']
def ann(tag,inst=False):
    out={}
    if tag not in G: return out
    for unit,vals in G[tag]['units'].items():
        for v in vals:
            if v.get('form') not in ('10-K','10-K/A','S-1','S-1/A','424B4','10-Q'): continue
            if v.get('fp')!='FY' and v.get('form')=='10-Q': continue
            e=datetime.date.fromisoformat(v['end'])
            if inst:
                if v.get('start'): continue
                if e.month!=12: continue
            else:
                if not v.get('start'): continue
                s=datetime.date.fromisoformat(v['start'])
                if not 340<(e-s).days<380: continue
            k=e.year
            if k not in out or v['filed']>out[k][1]: out[k]=(v['val'],v['filed'],v['form'])
    return out
tags=['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','GrossProfit','OperatingIncomeLoss','NetIncomeLoss','ProfitLoss','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','PaymentsForDepositsOnPropertyPlantAndEquipment','DepreciationDepletionAndAmortization','DepreciationAndAmortization','Depreciation','ShareBasedCompensation','AllocatedShareBasedCompensationExpense','PaymentsOfDividends','PaymentsOfDividendsCommonStock','IncomeTaxesPaidNet','IncomeTaxExpenseBenefit','PaymentsForRepurchaseOfCommonStock','ProceedsFromIssuanceInitialPublicOffering','OperatingLeaseRightOfUseAssetAmortizationExpense','IncreaseDecreaseInOperatingLeaseLiability']
for t in tags:
    a=ann(t)
    if a: print(t, {k:(round(v[0]/1e3),v[2]) for k,v in sorted(a.items())})
for t in ['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','Assets','CashAndCashEquivalentsAtCarryingValue','ShortTermInvestments','LongTermDebt','LongTermDebtNoncurrent','LongTermDebtCurrent','LineOfCredit','InventoryNet','LiabilitiesCurrent','AssetsCurrent','Goodwill','OperatingLeaseLiability']:
    a=ann(t,True)
    if a: print(t, {k:round(v[0]/1e3) for k,v in sorted(a.items())})
print([k for k in F.keys()])
