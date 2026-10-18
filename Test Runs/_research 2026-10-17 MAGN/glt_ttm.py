import json
from datetime import date
d=json.load(open('cache/cf_0000041719.json'))
def series(tag):
    out={}
    if tag not in d['facts']['us-gaap']: return out
    for v in d['facts']['us-gaap'][tag]['units'].get('USD',[]):
        if v['filed']>'2024-11-01': continue
        if 'start' not in v: continue
        s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
        key=(v['start'],v['end'])
        if key not in out: out[key]=(v['val']/1e6,v['accn'])
    return out
tags=['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations','PaymentsToAcquirePropertyPlantAndEquipment','ShareBasedCompensation','InterestPaidNet','OperatingIncomeLoss','RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','DepreciationDepletionAndAmortization','Depreciation','PaymentsToAcquireBusinessesNetOfCashAcquired']
for t in tags:
    s=series(t)
    print(t)
    for y in range(2019,2025):
        fy=s.get((f'{y-1}-01-01',f'{y-1}-12-31'))
        n9=s.get((f'{y}-01-01',f'{y}-09-30'))
        p9=s.get((f'{y-1}-01-01',f'{y-1}-09-30'))
        ttm=None
        if fy and n9 and p9: ttm=round(fy[0]-p9[0]+n9[0],1)
        print('  TTM to Sep',y,ttm,' FY',y-1,fy and round(fy[0],1),' 9M',y,n9 and round(n9[0],1),n9 and n9[1],' 9M',y-1,p9 and round(p9[0],1))
