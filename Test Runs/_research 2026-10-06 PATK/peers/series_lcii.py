import json
d=json.load(open('peers/LCII_facts.json'))['facts']['us-gaap']
def annual(tag):
    if tag not in d: return {}
    out={}
    for u,arr in d[tag]['units'].items():
        for x in arr:
            if x.get('fp')=='FY' and x.get('form','').startswith('10-K'):
                s,e=x.get('start'),x['end']
                if s and (int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])<11: continue
                y=e[:4]
                # keep first filed value
                if y not in out or x['filed']<out[y][1]: out[y]=(x['val'],x['filed'])
    return {k:v[0] for k,v in out.items()}
tags={'rev':['Revenues','SalesRevenueNet','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueGoodsNet'],
'opinc':['OperatingIncomeLoss'],'ni':['NetIncomeLoss'],'ocf':['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],
'capex':['PaymentsToAcquirePropertyPlantAndEquipment'],'acq':['PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsToAcquireBusinessesGross'],
'da':['DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet'],'amort':['AmortizationOfIntangibleAssets'],
'sbc':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],'buyback':['PaymentsForRepurchaseOfCommonStock'],'div':['PaymentsOfDividends','PaymentsOfDividendsCommonStock'],
'int':['InterestExpense','InterestExpenseNet','InterestPaidNet'],'tax':['IncomeTaxExpenseBenefit'],'dilsh':['WeightedAverageNumberOfDilutedSharesOutstanding'],'gw_impair':['GoodwillImpairmentLoss']}
res={}
for k,ts in tags.items():
    m={}
    for t in ts:
        for y,v in annual(t).items():
            m.setdefault(y,v)
    res[k]=m
years=sorted(set(y for m in res.values() for y in m))
print('year '+' '.join(f'{k:>9}' for k in tags))
for y in years:
    print(y,' '.join(f'{(res[k].get(y,float("nan"))/1e6 if k!="dilsh" else res[k].get(y,float("nan"))/1e6):9.1f}' for k in tags))
