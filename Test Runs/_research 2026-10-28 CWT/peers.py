import json,sys
from datetime import date
sys.stdout.reconfigure(encoding='utf-8')
def annual(f,tag):
    d=f['facts'].get('us-gaap',{}).get(tag)
    out={}
    if not d: return out
    for u,arr in d['units'].items():
        for x in arr:
            if x.get('form') in ('10-K','10-K/A') and x.get('fp')=='FY':
                if 'start' in x and (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<350: continue
                if x['end'][5:7]!='12': continue
                y=int(x['end'][:4])
                if y not in out or x['filed']>out[y][1]: out[y]=(x['val'],x['filed'])
    return {y:v[0] for y,v in out.items()}
def first(f,tags):
    r={}
    for t in tags:
        for y,v in annual(f,t).items(): r.setdefault(y,v)
    return r
for name in ['facts','facts_awr','facts_sjw','facts_awk']:
    f=json.load(open('cache/%s.json'%name))
    ni=first(f,['NetIncomeLossAvailableToCommonStockholdersBasic','NetIncomeLoss','ProfitLoss'])
    eq=first(f,['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'])
    rev=first(f,['Revenues','RegulatedOperatingRevenueWater','RevenueFromContractWithCustomerExcludingAssessedTax','RegulatedAndUnregulatedOperatingRevenue'])
    ocf=first(f,['NetCashProvidedByUsedInOperatingActivities'])
    cap=first(f,['PaymentsToAcquireWaterAndWasteWaterSystems','PaymentsToAcquireProductiveAssets','PaymentsToAcquirePropertyPlantAndEquipment','PaymentsForCapitalImprovements'])
    print('==',f['entityName'])
    roes=[]
    for y in range(2016,2026):
        e0,e1=eq.get(y-1),eq.get(y)
        roe=ni[y]/((e0+e1)/2)*100 if (y in ni and e0 and e1) else None
        if roe and y>=2016: roes.append((y,roe))
        print(y,'NI %.1f'%(ni.get(y,0)/1e6),'Eq %.1f'%(eq.get(y,0)/1e6),'Rev %.1f'%(rev.get(y,0)/1e6),'OCF %.1f'%(ocf.get(y,0)/1e6),'Capex %.1f'%(cap.get(y,0)/1e6),'ROE %s'%('%.1f'%roe if roe else '-'))
    r=[x for y,x in roes if 2021<=y<=2025]; r10=[x for y,x in roes]
    print('avg ROE 2021-25 %.1f ; avg ROE all years shown %.1f (%d yrs)'%(sum(r)/len(r),sum(r10)/len(r10),len(r10)))
