import json,sys
def series(f,tags,form='10-K'):
    d=json.load(open(f))['facts']
    out={}
    for t in tags:
        for ns in ('us-gaap','mtch'):
            if t in d.get(ns,{}):
                for u,vals in d[ns][t]['units'].items():
                    for v in vals:
                        if v.get('form')!=form or v.get('fp')!='FY': continue
                        s,e=v.get('start'),v['end']
                        if s and (int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])<11: continue
                        key=e
                        # keep latest filed
                        if key not in out or v['filed']>out[key][1]: out[key]=(v['val'],v['filed'],t)
    return out
tags={'Revenue':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'],'OpInc':['OperatingIncomeLoss'],'NI':['NetIncomeLoss'],
'OCF':['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],'SBC':['ShareBasedCompensation'],
'Capex':['PaymentsToAcquirePropertyPlantAndEquipment'],'Dep':['Depreciation','DepreciationDepletionAndAmortization'],'Buyback':['PaymentsForRepurchaseOfCommonStock'],
'IntExp':['InterestExpense','InterestExpenseNonoperating'],'Tax':['IncomeTaxExpenseBenefit'],'Shares':['WeightedAverageNumberOfDilutedSharesOutstanding']}
for f in sys.argv[1:]:
    print('==',f)
    res={k:series(f,v) for k,v in tags.items()}
    ends=sorted(set(e for r in res.values() for e in r))
    print('end       '+' '.join(f'{k:>9}' for k in tags))
    for e in ends:
        if e<'2014': continue
        print(e,' '.join(f'{(res[k][e][0]/1e6 if e in res[k] else float("nan")):9.1f}' for k in tags))
