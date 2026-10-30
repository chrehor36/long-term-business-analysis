import json,sys
from datetime import date
def load(f):
    return json.load(open(f))['facts']['us-gaap']
def dur(g,tags):
    out={}
    for tag in tags:
        for x in g.get(tag,{}).get('units',{}).get('USD',[]):
            if not x['form'].startswith('10-K') or 'start' not in x: continue
            if (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<350: continue
            if x['end'][5:]!='12-31': continue
            y=x['end'][:4]
            if y not in out or x['filed']>out[y][1]: out[y]=(x['val'],x['filed'],x['accn'])
        if out: pass
    return out
def inst(g,tags):
    out={}
    for tag in tags:
        for x in g.get(tag,{}).get('units',{}).get('USD',[]):
            if x['form'].startswith('10-K') and x['end'][5:]=='12-31':
                y=x['end'][:4]
                if y not in out or x['filed']>out[y][1]: out[y]=(x['val'],x['filed'],x['accn'])
    return out
yrs=[str(y) for y in range(2016,2026)]
for name in sys.argv[1:]:
    g=load(f'cache/facts_{name}.json')
    ni=dur(g,['NetIncomeLossAvailableToCommonStockholdersBasic']) or {}
    ni2=dur(g,['NetIncomeLoss'])
    for y in ni2:
        if y not in ni: ni[y]=ni2[y]
    eq=inst(g,['StockholdersEquity'])
    ocf=dur(g,['NetCashProvidedByUsedInOperatingActivities'])
    cap=dur(g,['PaymentsToAcquireProductiveAssets','PaymentsToAcquirePropertyPlantAndEquipment'])
    da=dur(g,['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet'])
    print('==',name)
    row=[]
    for y in yrs:
        p=str(int(y)-1)
        r=None
        if y in ni and y in eq and p in eq:
            r=ni[y][0]/((eq[y][0]+eq[p][0])/2)*100
        row.append(f"{r:5.1f}" if r is not None else "    -")
    print(' ROE%  ',' '.join(row))
    print(' NI    ',' '.join(f"{ni[y][0]/1e6:5.0f}" if y in ni else '    -' for y in yrs))
    print(' OCF   ',' '.join(f"{ocf[y][0]/1e6:5.0f}" if y in ocf else '    -' for y in yrs))
    print(' capex ',' '.join(f"{cap[y][0]/1e6:5.0f}" if y in cap else '    -' for y in yrs))
    print(' D&A   ',' '.join(f"{da[y][0]/1e6:5.0f}" if y in da else '    -' for y in yrs))
    last=max(ocf) if ocf else None
    print(' accn latest 10-K:', ocf[last][2] if last else '-')
