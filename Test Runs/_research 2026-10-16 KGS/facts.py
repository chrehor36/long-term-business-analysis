import json, urllib.request, time, sys
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def cf(cik):
    p=f'cache/cf_{cik}.json'
    try: return json.load(open(p))
    except: pass
    b=urllib.request.urlopen(urllib.request.Request(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json',headers=UA),timeout=60).read()
    open(p,'wb').write(b); time.sleep(0.3); return json.loads(b)
TAGS={'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'],
 'opinc':['OperatingIncomeLoss'],'da':['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet'],
 'assets':['Assets'],'ocf':['NetCashProvidedByUsedInOperatingActivities'],'capex':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
 'int':['InterestExpense','InterestExpenseNonoperating','InterestExpenseDebt'],'ni':['NetIncomeLoss','ProfitLoss'],
 'impair':['AssetImpairmentCharges','ImpairmentOfLongLivedAssetsHeldForUse','GoodwillImpairmentLoss'],
 'ppe':['PropertyPlantAndEquipmentNet'],'gw':['Goodwill'],'eq':['StockholdersEquity','PartnersCapital','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','PartnersCapitalIncludingPortionAttributableToNoncontrollingInterest'],
 'debt':['LongTermDebtNoncurrent','LongTermDebt'],'sbc':['ShareBasedCompensation'],'acq':['PaymentsToAcquireBusinessesNetOfCashAcquired']}
def series(d,tags,annual=True):
    out={}
    for t in tags:
        for ns in ('us-gaap',):
            u=d['facts'].get(ns,{}).get(t)
            if not u: continue
            for unit,vals in u['units'].items():
                for v in vals:
                    if v.get('form') not in ('10-K','10-K/A','S-1','S-1/A','424B4','10-KT'): continue
                    fy=v['end'][:4]
                    if 'start' in v:
                        from datetime import date
                        s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                        if not (330<(e-s).days<400): continue
                    if v['end'][5:] not in ('12-31',): continue
                    out.setdefault(fy,v['val'])
        if out: return out,t
    return out,None
cik=int(sys.argv[1]); d=cf(cik); print(d['entityName'])
rows={}
for k,t in TAGS.items():
    s,tag=series(d,t); rows[k]=s; print(f'  {k}: {tag}')
yrs=sorted(set().union(*[set(v) for v in rows.values()]))
yrs=[y for y in yrs if y>='2012']
print('year '+' '.join(f'{k:>8}' for k in TAGS))
for y in yrs:
    print(y+' '+' '.join(f"{(rows[k].get(y,0) or 0)/1e6:8.1f}" for k in TAGS))
