import json, sys
sys.path.insert(0, '.')
from fetch import get
j = json.loads(get("https://data.sec.gov/api/xbrl/companyfacts/CIK0001057877.json"))
g = j['facts']['us-gaap']
def annual(tag, unit='USD'):
    if tag not in g: return {}
    out = {}
    for f in g[tag]['units'].get(unit, []):
        if f.get('form') == '10-K' and f.get('fp') == 'FY' and 'frame' in f and len(f['frame']) == 6:
            out[f['end'][:4]] = f['val']
    return out
tags = sys.argv[1:]
yrs = [str(y) for y in range(2014, 2026)]
for t in tags:
    a = annual(t)
    print(t[:55].ljust(56), ' '.join(('%8.1f' % (a[y]/1e6)) if y in a else '       -' for y in yrs))
print(' '*56, ' '.join(y.rjust(8) for y in yrs))
