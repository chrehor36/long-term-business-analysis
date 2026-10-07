import json
d=json.load(open('facts_MD.json'))
g=d['facts']['us-gaap']
def ann(tag, mode='first', unit='USD'):
    out={}
    if tag not in g: return out
    for u,vals in g[tag]['units'].items():
        if u!=unit: continue
        for v in vals:
            if v.get('form') not in ('10-K','10-K/A'): continue
            if 'start' in v:
                from datetime import date
                s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                if not 340<=(e-s).days<=380: continue
            fy=v['end'][:4]
            if fy not in out or (mode=='first' and v['filed']<out[fy][1]) or (mode=='last' and v['filed']>out[fy][1]):
                out[fy]=(v['val'],v['filed'],v['accn'])
    return out
tags={'rev':['Revenues','HealthCareOrganizationRevenue','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueNet','HealthCareOrganizationPatientServiceRevenue'],
'opinc':['OperatingIncomeLoss'],'ni':['NetIncomeLoss'],'nicont':['IncomeLossFromContinuingOperations'],
'ocf':['NetCashProvidedByUsedInOperatingActivities'],'ocfc':['NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],
'capex':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireOtherPropertyPlantAndEquipment'],
'acq':['PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsToAcquireBusinessesGross'],
'sbc':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],'da':['DepreciationDepletionAndAmortization','DepreciationAndAmortization'],
'buyb':['PaymentsForRepurchaseOfCommonStock'],'gwimp':['GoodwillImpairmentLoss'],'int':['InterestExpense','InterestExpenseNonoperating'],
'tax':['IncomeTaxExpenseBenefit'],'dil':['WeightedAverageNumberOfDilutedSharesOutstanding']}
import sys
mode=sys.argv[1] if len(sys.argv)>1 else 'first'
res={}
for k,ts in tags.items():
    m={}
    for t in ts:
        unit='shares' if k=='dil' else 'USD'
        a=ann(t,mode,unit)
        for fy,v in a.items():
            if fy not in m: m[fy]=v
    res[k]=m
years=sorted(set(y for m in res.values() for y in m))
print('FY   '+' '.join(f'{k:>8}' for k in tags))
for y in years:
    print(y,' '.join(f"{(res[k][y][0]/1e6 if y in res[k] else float('nan')):8.1f}" for k in tags))
