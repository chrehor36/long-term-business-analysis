import json, sys
sys.stdout.reconfigure(encoding='utf-8')
d=json.load(open('cache/facts.json'))
g=d['facts'].get('us-gaap',{})
want=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','GrossProfit','OperatingIncomeLoss','NetIncomeLoss',
'NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','DepreciationDepletionAndAmortization','Depreciation','DepreciationAndAmortization',
'ShareBasedCompensation','AllocatedShareBasedCompensationExpense','StockholdersEquity','IncreaseDecreaseInAccountsPayableAndAccruedLiabilities','IncreaseDecreaseInInventories','IncreaseDecreaseInAccountsReceivable',
'IncomeTaxesPaidNet','IncomeTaxExpenseBenefit','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividends','PaymentsOfDividendsCommonStock',
'AmortizationOfIntangibleAssets','InventoryNet','Assets','CashAndCashEquivalentsAtCarryingValue','LongTermDebt','LineOfCredit','PropertyPlantAndEquipmentNet','Goodwill','IntangibleAssetsNetExcludingGoodwill','OperatingLeaseLiability','ContractWithCustomerLiability','RestrictedStockExpense','PaymentsForRepurchaseOfWarrants','ProceedsFromWarrantExercises','ProceedsFromIssuanceOfCommonStock']
for t in want:
    if t not in g: print('--',t,'absent'); continue
    u=g[t]['units']; k=list(u)[0]
    rows={}
    for f in u[k]:
        if f.get('form') not in ('10-K','10-K/A'): continue
        if 'frame' in f and not f['frame'].endswith('I') and 'Q' in f['frame']: continue
        s=f.get('start'); e=f['end']
        if s:
            from datetime import date
            dd=(date.fromisoformat(e)-date.fromisoformat(s)).days
            if dd<340 or dd>380: continue
        rows.setdefault(e,f['val'])
    print(t,k, ' '.join(f"{e[:7]}:{v/1000:.0f}" for e,v in sorted(rows.items())))
print([t for t in g if 'Share' in t or 'Stock' in t or 'Compens' in t])
