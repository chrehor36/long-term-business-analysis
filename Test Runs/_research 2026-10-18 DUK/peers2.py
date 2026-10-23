# Same metrics for DUK and three comparators from each company's own 10-K XBRL (companyfacts), first-filed value per FY.
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
names = {'0001326160':'DUK','0000092122':'SO','0000715957':'D','0000004904':'AEP'}
def series(f, tags, instant=False):
    out = {}
    for tag in tags:
        try: units = f['facts']['us-gaap'][tag]['units']['USD']
        except KeyError: continue
        for u in units:
            if u.get('form') != '10-K': continue
            if instant:
                if 'start' in u or u['end'][5:] != '12-31': continue
            else:
                if 'start' not in u or u['start'][5:] != '01-01' or u['end'][5:] != '12-31' or u['start'][:4] != u['end'][:4]: continue
            y = int(u['end'][:4])
            if y in out and out[y][3] != tag: continue   # first tag that has the year wins
            if y not in out or u['filed'] < out[y][1]:
                out[y] = (u['val'], u['filed'], u['accn'], tag)
    return out
rows = {}
for c, n in names.items():
    f = json.load(open(f'cache/peers/cf_{c}.json'))
    ni = series(f, ['NetIncomeLossAvailableToCommonStockholdersBasic','NetIncomeLoss'])
    eq = series(f, ['StockholdersEquity'], True)
    assets = series(f, ['Assets'], True)
    gw = series(f, ['Goodwill'], True)
    oi = series(f, ['OperatingIncomeLoss'])
    rev = series(f, ['Revenues','RevenueFromContractWithCustomerIncludingAssessedTax','RegulatedAndUnregulatedOperatingRevenue'])
    ocf = series(f, ['NetCashProvidedByUsedInOperatingActivities'])
    capex = series(f, ['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','PaymentsForConstructionInProcess'])
    print('==', n)
    roes=[]; rotas=[]
    for y in range(2016, 2026):
        def v(s,yy): return s.get(yy,(None,))[0]
        e0,e1 = v(eq,y-1), v(eq,y); nv = v(ni,y)
        roe = nv/((e0+e1)/2)*100 if (nv is not None and e0 and e1) else None
        a0,a1 = v(assets,y-1), v(assets,y); g0,g1 = v(gw,y-1) or 0, v(gw,y) or 0
        o = v(oi,y)
        rota = o/(((a0-g0)+(a1-g1))/2)*100 if (o is not None and a0 and a1) else None
        if roe is not None: roes.append(roe)
        if rota is not None: rotas.append(rota)
        print(y, 'NIcommon', nv and round(nv/1e6), 'ROE%', roe and round(roe,1), 'OpInc', o and round(o/1e6),
              'tangAssets', a1 and round((a1-g1)/1e6), 'OpInc/tangA%', rota and round(rota,2),
              'rev', v(rev,y) and round(v(rev,y)/1e6), 'OCF', v(ocf,y) and round(v(ocf,y)/1e6), 'capex', v(capex,y) and round(v(capex,y)/1e6),
              'accn', ni.get(y,(0,0,None))[2], ni.get(y,(0,0,0,None))[3])
    if roes: print('  mean ROE %.1f over %d yrs; mean OpInc/tangible assets %.2f over %d yrs' % (sum(roes)/len(roes), len(roes), sum(rotas)/len(rotas), len(rotas)))
