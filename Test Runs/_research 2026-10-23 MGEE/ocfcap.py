import json,sys
from datetime import date
for f in sys.argv[1:]:
    d=json.load(open(f));g=d['facts']['us-gaap']
    def annual(tag):
        out={}
        for u,vals in g.get(tag,{'units':{}})['units'].items():
            for v in vals:
                if v.get('form')!='10-K' or 'start' not in v: continue
                if not 350<(date.fromisoformat(v['end'])-date.fromisoformat(v['start'])).days<380: continue
                if v['end'] not in out or v['filed']>out[v['end']][1]: out[v['end']]=(v['val'],v['filed'])
        return out
    o=annual('NetCashProvidedByUsedInOperatingActivities');c=annual('PaymentsToAcquirePropertyPlantAndEquipment') or {}
    if not c or max(c)<'2025': 
        for t in ['PaymentsToAcquireProductiveAssets','PaymentsForConstructionInProcess','PaymentsToAcquireAndDevelopRealEstate']:
            cc=annual(t); 
            for k,v in cc.items(): c.setdefault(k,v)
    r=annual('Revenues') or annual('RegulatedAndUnregulatedOperatingRevenue')
    print(d['entityName'])
    so=sc=0
    for y in sorted(o):
        if '2016'<=y[:4]<='2025' and y in c:
            so+=o[y][0];sc+=c[y][0];print(' ',y[:4],f"OCF {o[y][0]/1e6:8.1f} capex {c[y][0]/1e6:8.1f} OCF-capex {(o[y][0]-c[y][0])/1e6:8.1f}")
    print('  sum OCF',round(so/1e6,1),'sum capex',round(sc/1e6,1),'capex/OCF',round(sc/so,2))
