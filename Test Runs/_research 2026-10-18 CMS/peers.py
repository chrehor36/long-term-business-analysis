import json,sys
from datetime import date
def series(g,tag):
    out={}
    if tag not in g: return out
    for unit,arr in g[tag]['units'].items():
        for x in arr:
            if x.get('form')!='10-K': continue
            if 'start' in x:
                d=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
                if d<350 or d>380: continue
            k=x['end']
            if k[5:]!='12-31': continue
            if k not in out or x['filed']>out[k][1]:
                out[k]=(x['val'],x['filed'],x['accn'])
    return out
for name in sys.argv[1:]:
    d=json.load(open(f'cache/peers/{name}.json' if name!='CMS' else 'cache/facts.json'))
    g=d['facts']['us-gaap']
    ni=series(g,'NetIncomeLossAvailableToCommonStockholdersBasic') or {}
    ni2=series(g,'NetIncomeLoss')
    eq=series(g,'StockholdersEquity')
    ocf=series(g,'NetCashProvidedByUsedInOperatingActivities')
    da=series(g,'DepreciationDepletionAndAmortization') or series(g,'DepreciationAndAmortization')
    if not da: da=series(g,'DepreciationAmortizationAndAccretionNet')
    cap=series(g,'PaymentsToAcquirePropertyPlantAndEquipment')
    print('==',name, d.get('entityName'))
    roes=[]
    for y in range(2015,2026):
        k=f'{y}-12-31'; kp=f'{y-1}-12-31'
        n=(ni.get(k) or ni2.get(k) or (None,))[0]
        e=eq.get(k,(None,))[0]; ep=eq.get(kp,(None,))[0]
        roe = n/((e+ep)/2) if n and e and ep else None
        if roe: roes.append(roe)
        f=lambda s:(s.get(k,(None,))[0] or 0)/1e6
        print(y, 'NI',round((n or 0)/1e6), 'Eq',round((e or 0)/1e6), 'ROE', f'{roe:.1%}' if roe else '-', 'OCF',round(f(ocf)),'capex',round(f(cap)),'D&A',round(f(da)), (ni.get(k) or ni2.get(k) or (0,0,''))[2])
    if roes: print('mean ROE', f'{sum(roes)/len(roes):.1%}', 'n',len(roes))
