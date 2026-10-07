import sys, json
sys.path.insert(0,'tools')
import sources as s
f = s.sec_facts('0001845815')
json.dump(f, open('Test Runs/_research 2026-09-29 PAYO/facts.json','w'))
want = ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','OperatingIncomeLoss','NetIncomeLoss','NetCashProvidedByUsedInOperatingActivities','ShareBasedCompensation','AllocatedShareBasedCompensationExpense','DepreciationDepletionAndAmortization','DepreciationAndAmortization','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','PaymentsForRepurchaseOfCommonStock','WeightedAverageNumberOfSharesOutstandingBasic','StockholdersEquity','Goodwill']
for ns in f['facts']:
    for tag, v in f['facts'][ns].items():
        if tag in want or 'Interest' in tag and ns!='dei' and ('Customer' in tag or 'customer' in tag.lower()):
            for unit, arr in v['units'].items():
                rows = {}
                for x in arr:
                    if x.get('form') in ('10-K',) and x.get('fp')=='FY':
                        st = x.get('start','')
                        if st and (int(x['end'][:4])*12+int(x['end'][5:7]) - int(st[:4])*12-int(st[5:7])) in (11,12):
                            rows.setdefault(x['end'], x['val'])
                        elif not st:
                            rows.setdefault(x['end'], x['val'])
                print(ns, tag, unit, {k: round(val/1e6,1) if unit=='USD' else val for k, val in sorted(rows.items())})
