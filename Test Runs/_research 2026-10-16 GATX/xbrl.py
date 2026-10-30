import json, sys
d = json.load(open(sys.argv[1]))['facts']['us-gaap']
def annual(tag):
    if tag not in d: return {}
    out = {}
    for u, rows in d[tag]['units'].items():
        for r in rows:
            if r.get('form') in ('10-K',) and r.get('fp') == 'FY' and 'frame' in r and r['frame'].startswith('CY') and len(r['frame'])==6:
                out[int(r['frame'][2:])] = r['val']
    return out
tags = sys.argv[2:]
for t in tags:
    a = annual(t)
    print(t[:60].ljust(60), ' '.join(f"{y}:{a[y]/1e6:,.1f}" for y in sorted(a) if y>=2012))
