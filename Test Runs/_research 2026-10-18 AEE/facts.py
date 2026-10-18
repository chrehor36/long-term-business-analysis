import json,sys
TAGS={'NI':['NetIncomeLoss','NetIncomeLossAvailableToCommonStockholdersBasic'],
'OCF':['NetCashProvidedByUsedInOperatingActivities'],
'CAPEX':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
'DA':['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet'],
'REV':['Revenues','RevenueFromContractWithCustomerIncludingAssessedTax','RegulatedAndUnregulatedOperatingRevenue'],
'EQ':['StockholdersEquity'],
'DIV':['PaymentsOfDividendsCommonStock','PaymentsOfDividends'],
'ISS':['ProceedsFromIssuanceOfCommonStock'],
'INT':['InterestExpense','InterestExpenseNonoperating','InterestExpenseDebt'],
'TAX':['IncomeTaxExpenseBenefit'],
'SBC':['ShareBasedCompensation'],
'PPE':['PublicUtilitiesPropertyPlantAndEquipmentNet','PropertyPlantAndEquipmentNet'],
}
def series(d,tags,fp='FY'):
    out={}
    g=d['facts'].get('us-gaap',{})
    for t in tags:
        if t not in g: continue
        for u,arr in g[t]['units'].items():
            for x in arr:
                if x.get('fp')!='FY' or not x.get('form','').startswith('10-K'): continue
                end=x['end']; 
                if 'start' in x:
                    from datetime import date
                    s=date.fromisoformat(x['start']); e=date.fromisoformat(end)
                    if (e-s).days<350: continue
                y=int(end[:4])
                if y not in out: out[y]=(x['val'],t,x['accn'])
    return out
t=sys.argv[1]; d=json.load(open(f'cache/facts/{t}.json'))
yrs=range(2015,2026)
res={k:series(d,v) for k,v in TAGS.items()}
print(t, d['entityName'])
print('year '+' '.join(f'{k:>8}' for k in TAGS))
for y in yrs:
    print(y,' '.join(f"{(res[k][y][0]/1e6 if y in res[k] else float('nan')):8.0f}" for k in TAGS))
for k in TAGS: print(k, sorted(set(v[1] for v in res[k].values())))
