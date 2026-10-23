import json, sys
from datetime import date
def series(d, tag, dur):
    out = {}
    if tag not in d: return out
    for u, rows in d[tag]['units'].items():
        for r in rows:
            if r.get('form') not in ('20-F','20-F/A'): continue
            if not r['end'].endswith('12-31'): continue
            if dur:
                if 'start' not in r: continue
                if not (350 <= (date.fromisoformat(r['end'])-date.fromisoformat(r['start'])).days <= 380): continue
            elif 'start' in r: continue
            y = int(r['end'][:4])
            if y not in out or r['filed'] > out[y][1]: out[y] = (r['val'], r['filed'], r['accn'])
    return out
for f in sys.argv[1:]:
    j = json.load(open(f)); d = j['facts'].get('ifrs-full', {})
    print('==', j['entityName'])
    ni = series(d,'ProfitLossAttributableToOwnersOfParent',True); eq = series(d,'EquityAttributableToOwnersOfParent',False)
    op = series(d,'ProfitLossFromOperatingActivities',True); rev = series(d,'Revenue',True)
    for y in range(2015, 2026):
        e0 = eq.get(y-1,(None,))[0]; e1 = eq.get(y,(None,))[0]; n = ni.get(y,(None,))[0]
        roe = (n/((e0+e1)/2)*100) if (n is not None and e0 and e1) else None
        print(y, 'NI', n and round(n/1e9,1), 'Eq', e1 and round(e1/1e9,1), 'ROE%', roe and round(roe,1), 'accn', ni.get(y,(0,0,''))[2])
