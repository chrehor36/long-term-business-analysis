# peer table from SEC companyfacts: latest annual filing value per fiscal year-end (Dec 31)
import json, sys, datetime as dt
def get(d, tax, c, forms):
    out = {}
    if c not in d['facts'].get(tax, {}): return out
    for u, xs in d['facts'][tax][c]['units'].items():
        for x in xs:
            if x.get('form') not in forms: continue
            e = x['end']
            if 'start' in x and (dt.date.fromisoformat(e) - dt.date.fromisoformat(x['start'])).days < 350: continue
            y = int(e[:4]) if e[5:7] in ('12',) else None
            if y is None: continue
            if y not in out or x['filed'] > out[y][1]:
                out[y] = (x['val'], x['filed'], x['accn'])
    return out
f, tax, forms = sys.argv[1], sys.argv[2], tuple(sys.argv[3].split(','))
d = json.load(open(f))
yrs = range(2015, 2026)
print(d['entityName'])
for c in sys.argv[4].split(','):
    g = get(d, tax, c, forms)
    print(c[:45].ljust(45), *[(str(round(g[y][0]/1e6)) if y in g else '-').rjust(7) for y in yrs])
    if g: print('   accn of latest:', g[max(g)][2], 'filed', g[max(g)][1])
