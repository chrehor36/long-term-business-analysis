import json, sys
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
def series(g, tags, instant=False):
    out = {}
    for tag in tags:
        if tag not in g: continue
        for unit, arr in g[tag]['units'].items():
            if unit != 'USD': continue
            for x in arr:
                if x.get('form') not in ('10-K','10-K/A'): continue
                e = date.fromisoformat(x['end'])
                if e.month != 12: continue
                if not instant:
                    if 'start' not in x: continue
                    d = (e - date.fromisoformat(x['start'])).days
                    if d < 350 or d > 380: continue
                elif 'start' in x: continue
                y = e.year
                prev = out.get(y)
                if prev is None or (prev[2]==tag and x['filed'] > prev[1]):
                    out[y] = (x['val']/1e6, x['filed'], tag)
        pass
    return {k: v[0] for k, v in out.items()}
res = {}
for name, fn in [('DTE','facts.json'),('CMS','facts_CMS.json'),('WEC','facts_WEC.json'),('XEL','facts_XEL.json')]:
    g = json.load(open('cache/'+fn))['facts']['us-gaap']
    ni = series(g, ['NetIncomeLoss','NetIncomeLossAvailableToCommonStockholdersBasic','ProfitLoss'])
    eq = series(g, ['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','CommonStockholdersEquity'], instant=True)
    da = series(g, ['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet'])
    cap = series(g, ['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','PaymentsForCapitalImprovements'])
    print('==', name)
    roes = []
    for y in range(2016, 2026):
        e0, e1 = eq.get(y-1), eq.get(y)
        roe = ni[y]/((e0+e1)/2)*100 if (y in ni and e0 and e1) else None
        if roe: roes.append(roe)
        print(y, 'NI', round(ni.get(y,0)), 'EQ', round(eq.get(y,0)), 'ROE', None if roe is None else round(roe,1), 'DA', round(da.get(y,0)), 'CAPEX', round(cap.get(y,0)))
    print('avg ROE', round(sum(roes)/len(roes),1) if roes else None, 'n', len(roes))
