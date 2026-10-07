import json, sys, io
from datetime import date
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
f=json.load(open('companyfacts.json'))['facts']['ifrs-full']
tags=['CashFlowsFromUsedInOperatingActivities','PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities','AdjustmentsForSharebasedPayments','AdjustmentsForDepreciationExpense','AdjustmentsForAmortisationExpense','PaymentsOfLeaseLiabilitiesClassifiedAsFinancingActivities','CashFlowsUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities','IncomeTaxesPaidRefundClassifiedAsOperatingActivities','InterestReceivedClassifiedAsOperatingActivities','Revenue','GrossProfit','ProfitLossFromOperatingActivities','ProfitLossBeforeTax','PaymentsToAcquireOrRedeemEntitysShares','ProceedsFromExerciseOfOptions']
for tg in tags:
    if tg not in f: print('MISSING', tg); continue
    arr=f[tg]['units'].get('EUR',[])
    d={}
    for x in arr:
        if 'start' not in x or not x.get('form','').startswith('20-F'): continue
        if not 350<(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<380: continue
        d.setdefault(x['end'][:4],set()).add(round(x['val']/1e6))
    print(tg[:60], {y:sorted(v) for y,v in sorted(d.items())})
print([k for k in f if 'Lease' in k and 'Payment' in k])
print([k for k in f if 'Control' in k or 'Acqui' in k][:10])
print([k for k in f if 'Tax' in k and 'Paid' in k])
