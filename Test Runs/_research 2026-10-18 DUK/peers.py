import json, sys
sys.stdout.reconfigure(encoding='utf-8')
names = {'0001326160':'DUK','0000092122':'SO','0000715957':'D','0000004904':'AEP'}
def annual(f, tag, instant=False):
    try: units = f['facts']['us-gaap'][tag]['units']['USD']
    except KeyError: return {}
    out = {}
    for u in units:
        if u.get('form') != '10-K' or u.get('fp') != 'FY': continue
        if instant:
            if 'start' in u: continue
            y = int(u['end'][:4])
            if u['end'][5:] != '12-31': continue
        else:
            if 'start' not in u: continue
            if int(u['end'][:4]) - int(u['start'][:4]) != 1 and not (u['start'][5:]=='01-01' and u['end'][5:]=='12-31'): continue
            if u['start'][5:]!='01-01' or u['end'][5:]!='12-31': continue
            y = int(u['end'][:4])
        # keep the first-filed value (earliest filed) for each year
        if y not in out or u['filed'] < out[y][1]:
            out[y] = (u['val'], u['filed'], u['accn'])
    return out
for c, n in names.items():
    f = json.load(open(f'cache/peers/cf_{c}.json'))
    ni = annual(f, 'NetIncomeLossAvailableToCommonStockholdersBasic') or annual(f,'NetIncomeLoss')
    ni2 = annual(f,'NetIncomeLoss')
    eq = annual(f, 'StockholdersEquity', True)
    ocf = annual(f,'NetCashProvidedByUsedInOperatingActivities')
    capex = annual(f,'PaymentsToAcquirePropertyPlantAndEquipment')
    da = annual(f,'DepreciationDepletionAndAmortization') or annual(f,'DepreciationAndAmortization')
    rev = annual(f,'Revenues')
    print('==', n)
    for y in range(2015, 2026):
        e0 = eq.get(y-1,(None,))[0]; e1 = eq.get(y,(None,))[0]
        nv = ni.get(y,(None,None,None))
        roe = (nv[0]/((e0+e1)/2)*100) if (nv[0] and e0 and e1) else None
        print(y, 'NIcommon', nv[0] and round(nv[0]/1e6), 'equityEnd', e1 and round(e1/1e6), 'ROE%', roe and round(roe,1),
              'OCF', ocf.get(y,(None,))[0] and round(ocf[y][0]/1e6), 'capex', capex.get(y,(None,))[0] and round(capex[y][0]/1e6),
              'D&A', da.get(y,(None,))[0] and round(da[y][0]/1e6), 'accn', nv[2])
