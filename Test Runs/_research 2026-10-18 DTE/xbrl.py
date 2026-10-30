import json, sys
f = json.load(open('cache/facts.json'))
g = f['facts']['us-gaap']
def annual(tag):
    if tag not in g: return {}
    out = {}
    for unit, arr in g[tag]['units'].items():
        for x in arr:
            if x.get('form') in ('10-K','10-K/A') and x.get('fp') == 'FY':
                fr = x.get('frame','')
                # duration facts: keep full-year frames CYxxxx; instant: CYxxxxQ4I
                if fr.startswith('CY') and (len(fr)==6 or fr.endswith('Q4I')):
                    y = int(fr[2:6]); out[y] = x['val']
    return out
tags = sys.argv[1:]
for t in tags:
    a = annual(t)
    print(t, {k: round(v/1e6) if abs(v)>1e5 else v for k, v in sorted(a.items()) if k >= 2014})
