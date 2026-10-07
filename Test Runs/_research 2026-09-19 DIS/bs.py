import sys, os, json
sys.path.insert(0, os.path.abspath('tools'))
import sources
from datetime import date
f = json.load(open('Test Runs/_research 2026-09-19 DIS/companyfacts.json'))
def inst(tag):
    node = f['facts']['us-gaap'].get(tag)
    if not node: return {}
    out={}
    for unit,pts in node['units'].items():
        for x in pts:
            if x.get('form')=='10-K' and not x.get('start'):
                k=x['end']
                fl=x.get('filed','')
                if k not in out or fl>out[k][1]:
                    out[k]=(x['val']/1e6, fl)
    return {k:v[0] for k,v in sorted(out.items())}
for t in ['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest',
          'Assets','Goodwill','FiniteLivedIntangibleAssetsNet','IntangibleAssetsNetExcludingGoodwill',
          'LongTermDebtNoncurrent','LongTermDebtCurrent','CashAndCashEquivalentsAtCarryingValue',
          'PropertyPlantAndEquipmentNet','PropertyPlantAndEquipmentGross','LiabilitiesCurrent']:
    d=inst(t)
    print('==',t)
    for k in sorted(d):
        if k>='2016-01-01': print('  ',k, round(d[k],0))
