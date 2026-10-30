import json, sys
from datetime import date
def annual(g,k,inst=False):
    out={}
    if k not in g: return out
    for u,vals in g[k]['units'].items():
        for x in vals:
            if x['form']!='10-K' or not x['end'].endswith('12-31'): continue
            if not inst:
                if 'start' not in x: continue
                d=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
                if not 350<d<380: continue
            y=int(x['end'][:4])
            if y not in out or x['filed']>out[y][1]: out[y]=(x['val'],x['filed'],x['accn'])
    return out
for cik in sys.argv[1:]:
    d=json.load(open(f'cache/facts_{cik}.json')); g=d['facts']['us-gaap']
    print('==',d['entityName'])
    for k,inst in [('OperatingIncomeLoss',0),('NetIncomeLossAvailableToCommonStockholdersBasic',0),('NetIncomeLoss',0),('StockholdersEquity',1),('PropertyPlantAndEquipmentNet',1),('PublicUtilitiesPropertyPlantAndEquipmentNet',1),('PaymentsToAcquirePropertyPlantAndEquipment',0),('Revenues',0)]:
        a=annual(g,k,inst)
        print(k,{y:(round(v[0]/1e6),v[2]) for y,v in sorted(a.items()) if 2019<=y<=2025})
