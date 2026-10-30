import json,sys
from datetime import date
def ann(d,tag,tax='us-gaap'):
    f=d['facts'].get(tax,{}).get(tag)
    if not f: return {}
    out={}
    for x in list(f['units'].values())[0]:
        if x.get('form')!='10-K': continue
        if 'start' in x and (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<350: continue
        out[x['end'][:4]]=(x['val'],x['accn'])  # latest filed wins
    return out
for c in ['0001567683','0001603145']:
    d=json.load(open(f'cache/facts_{c}.json'))
    print(c,d['entityName'])
    for t in ['Revenues','OperatingIncomeLoss','Assets','PropertyPlantAndEquipmentNet','LongTermDebt','DepreciationDepletionAndAmortization','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','NetIncomeLoss','StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','PartnersCapitalAccountUnits','InterestExpense','InterestExpenseNonoperating']:
        a=ann(d,t)
        print(' ',t,{k:v[0]//1000000 for k,v in sorted(a.items()) if k>='2016'})
        if a: print('    accn latest',sorted(a.items())[-1][1][1])
