import json, sys
from fetch import get
b=get('https://data.sec.gov/api/xbrl/companyfacts/CIK0001618673.json'); open('cache/facts.json','wb').write(b)
f=json.loads(b)['facts']['us-gaap']
def ann(tag):
    if tag not in f: return {}
    out={}
    for u,rows in f[tag]['units'].items():
        for r in rows:
            if r.get('form')!='10-K' or r.get('fp')!='FY': continue
            if 'start' in r:
                from datetime import date
                d=(date.fromisoformat(r['end'])-date.fromisoformat(r['start'])).days
                if d<340 or d>380: continue
            out.setdefault(r['end'],{})[r['filed']]=r['val']
    # newest vintage
    return {e:v[max(v)] for e,v in out.items()}
tags=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','OperatingIncomeLoss','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','ShareBasedCompensation','AllocatedShareBasedCompensationExpense','Depreciation','DepreciationDepletionAndAmortization','AmortizationOfIntangibleAssets','PaymentsToAcquireBusinessesNetOfCashAcquired','FinanceLeasePrincipalPayments','RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability','InterestPaidNet','IncomeTaxesPaidNet','StockholdersEquity','Goodwill','IntangibleAssetsNetExcludingGoodwill','LongTermDebt','InventoryLIFOReserve','IncreaseDecreaseInInventories','IncreaseDecreaseInAccountsPayable','NetIncomeLoss','GrossProfit','CostOfGoodsAndServicesSold','PaymentsForRepurchaseOfCommonStock','InterestExpense','InterestExpenseNonoperating','CapitalLeaseObligationsIncurred']
res={}
for t in tags:
    a=ann(t)
    if a: res[t]=a
    print(t, {k[:7]:round(v/1e6,1) for k,v in sorted(a.items())})
json.dump(res,open('series.json','w'),indent=0)
