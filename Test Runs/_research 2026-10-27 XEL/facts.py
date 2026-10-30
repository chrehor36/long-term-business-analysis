import json, sys
d = json.load(open(sys.argv[1]))
g = d['facts']['us-gaap']
def annual(tag, unit='USD'):
    out = {}
    if tag not in g: return out
    for f in g[tag]['units'].get(unit, []):
        if f.get('form') == '10-K' and f.get('fp') == 'FY':
            fr, to = f.get('start'), f['end']
            if fr and (int(to[:4]) - int(fr[:4]) > 1 or to[5:7] != '12'): continue
            if fr and fr[5:7] != '01': continue
            y = int(to[:4])
            if y not in out: out[y] = (f['val'], f['accn'])   # first filed
    return out
tags = sys.argv[2:]
for t in tags:
    a = annual(t)
    print(t, {y: round(v[0]/1e6) for y, v in sorted(a.items()) if y >= 2014})
