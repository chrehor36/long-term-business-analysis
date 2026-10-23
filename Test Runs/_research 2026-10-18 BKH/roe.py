import json, sys
from datetime import date
def inst(g, tag):
    out = {}
    if tag not in g: return out
    for unit, arr in g[tag]['units'].items():
        for x in arr:
            if 'start' in x or x.get('form') not in ('10-K','10-K/A'): continue
            e = date.fromisoformat(x['end'])
            if e.month == 12 and e.day == 31:
                if e.year not in out or x['filed'] > out[e.year][1]:
                    out[e.year] = (x['val'], x['filed'])
    return {k: v[0] for k, v in out.items()}
def ann(g, tag):
    out = {}
    if tag not in g: return out
    for unit, arr in g[tag]['units'].items():
        for x in arr:
            if x.get('fp') == 'FY' and x.get('form') in ('10-K','10-K/A') and 'start' in x:
                s = date.fromisoformat(x['start']); e = date.fromisoformat(x['end'])
                if 350 < (e - s).days < 380:
                    if e.year not in out or x['filed'] > out[e.year][1]:
                        out[e.year] = (x['val'], x['filed'])
    return {k: v[0] for k, v in out.items()}
name = sys.argv[1]
eq, ni = {}, {}
for f in sys.argv[2:]:
    g = json.load(open(f))['facts']['us-gaap']
    for k, v in inst(g, 'StockholdersEquity').items(): eq.setdefault(k, v)
    for k, v in ann(g, 'NetIncomeLoss').items(): ni.setdefault(k, v)
row = []
roes = []
for y in range(2016, 2026):
    if y in ni and y in eq and y-1 in eq:
        r = ni[y] / ((eq[y] + eq[y-1]) / 2)
        roes.append(r); row.append(f"{y}:{r*100:5.1f}%")
    else: row.append(f"{y}:  -  ")
print(name.ljust(5), ' '.join(row), f" avg {sum(roes)/len(roes)*100:.1f}% (n={len(roes)})")
print('      equity', {k: round(v/1e6) for k, v in sorted(eq.items()) if k >= 2015})
