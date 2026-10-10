import json,sys
from datetime import date
def series(f,ns,tags,forms=('10-K','20-F')):
    d=json.load(open(f))['facts']
    res={}
    for tg in tags:
        for n in ns:
            if n in d and tg in d[n]:
                for u,arr in d[n][tg]['units'].items():
                    for x in arr:
                        if x['form'].split('/')[0] in forms and x.get('start') and x.get('fp')=='FY':
                            s=date.fromisoformat(x['start']);e=date.fromisoformat(x['end'])
                            if 350<(e-s).days<380 and x['end']>='2013-06-01':
                                res.setdefault(tg+' '+u,{})[x['end'][:7]]=(x['val'],x['accn'])
    return res
for nm,ns,tags in [('LRCX',['us-gaap'],['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','OperatingIncomeLoss','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','ShareBasedCompensation','ResearchAndDevelopmentExpense']),
                   ('KLAC',['us-gaap'],['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','OperatingIncomeLoss','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','ShareBasedCompensation','ResearchAndDevelopmentExpense']),
                   ('ASML',['ifrs-full'],['Revenue','ProfitLossFromOperatingActivities','CashFlowsFromUsedInOperatingActivities','PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities','ResearchAndDevelopmentExpense'])]:
    print('=====',nm)
    for k,v in series(f'peers/{nm}_facts.json',ns,tags).items():
        print(k); print('   '+'  '.join(f"{y}:{v[y][0]/1e6:,.0f}" for y in sorted(v)))
        print('   last accn', v[max(v)][1])
