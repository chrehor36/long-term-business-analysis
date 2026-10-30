import json,sys
from datetime import date
f=json.load(open('companyfacts.json'))['facts']
g=f.get('us-gaap',{})
def annual(tag, inst=False):
    if tag not in g: return {}
    out={}
    for u,arr in g[tag]['units'].items():
        for x in arr:
            if x.get('form') not in ('10-K','10-K/A'): continue
            e=date.fromisoformat(x['end'])
            if e.month!=9: continue
            if not inst:
                if 'start' not in x: continue
                s=date.fromisoformat(x['start'])
                if not (350<(e-s).days<380): continue
            y=e.year
            # newest filed wins
            if y not in out or x['filed']>out[y][1]: out[y]=(x['val'],x['filed'])
    return {k:v[0] for k,v in sorted(out.items())}
tags=sys.argv[1:] or ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','GrossProfit','OperatingIncomeLoss','NetIncomeLoss','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','DepreciationDepletionAndAmortization','DepreciationAndAmortization','Depreciation','ShareBasedCompensation','AllocatedShareBasedCompensationExpense','FinanceLeasePrincipalPayments','RepaymentsOfLongTermCapitalLeaseObligations','OperatingLeaseCost','OperatingLeasePayments','FinanceLeaseInterestPayments','InterestExpense','PaymentsOfDividends','PaymentsForRepurchaseOfCommonStock','PaymentsToAcquireBusinessesNetOfCashAcquired','ProceedsFromSaleOfPropertyPlantAndEquipment']
for t in tags:
    a=annual(t)
    if a: print(t, {k:round(v/1e6,2) for k,v in a.items()})
print('--- instants')
for t in ['Assets','StockholdersEquity','Goodwill','IntangibleAssetsNetExcludingGoodwill','OperatingLeaseLiability','FinanceLeaseLiability','CapitalLeaseObligations','LongTermDebt','LineOfCredit','LongTermLineOfCredit','CashAndCashEquivalentsAtCarryingValue','PropertyPlantAndEquipmentNet','OperatingLeaseRightOfUseAsset','InventoryNet','AccountsPayableCurrent','LiabilitiesCurrent','AssetsCurrent']:
    a=annual(t,inst=True)
    if a: print(t, {k:round(v/1e6,2) for k,v in a.items()})
