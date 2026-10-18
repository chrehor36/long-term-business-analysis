import json, sys
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
TAGS = ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","OperatingIncomeLoss","NetCashProvidedByUsedInOperatingActivities",
 "PaymentsToAcquirePropertyPlantAndEquipment","ShareBasedCompensation","AllocatedShareBasedCompensationExpense","Assets","Goodwill",
 "IntangibleAssetsNetExcludingGoodwill","CashAndCashEquivalentsAtCarryingValue","StockholdersEquity","InterestExpense","InterestExpenseNonoperating",
 "IncomeTaxesPaidNet","PaymentsForRepurchaseOfCommonStock","DepreciationDepletionAndAmortization","DepreciationAndAmortization","LongTermDebt","LongTermDebtNoncurrent","DebtCurrent","LongTermDebtCurrent"]
def series(cf, tag):
    u = cf['facts'].get('us-gaap',{}).get(tag,{}).get('units',{}).get('USD',[])
    out = {}
    for f in u:
        if f.get('form') not in ('10-K','10-K/A'): continue
        end = f['end']; y = int(end[:4])
        if 'start' in f:
            d = (date.fromisoformat(end)-date.fromisoformat(f['start'])).days
            if d < 350 or d > 380: continue
        if end[5:7] != '12': continue
        prev = out.get(y)
        if prev is None or f['filed'] > prev[1]: out[y] = (f['val']/1e6, f['filed'])
    return {y:v[0] for y,v in out.items()}
t = sys.argv[1]
cf = json.load(open(f'cache/cf_{t}.json'))
yrs = range(2015, 2026)
print(t, cf['entityName'])
for tag in TAGS:
    s = series(cf, tag)
    if not s: continue
    print(f"{tag[:42]:42s}", " ".join(f"{s.get(y, float('nan')):8.0f}" for y in yrs))
print(" "*42, " ".join(f"{y:8d}" for y in yrs))
