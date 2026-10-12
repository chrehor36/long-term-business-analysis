import json,sys
from datetime import date
d=json.load(open('cache/facts.json'))
g=d['facts']['us-gaap']
def ser(t):
    if t not in g: return {}
    u=list(g[t]['units'].values())[0]; rows={}
    for x in u:
        if not x.get('form','').startswith('10-K'): continue
        if 'start' in x and (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<350: continue
        rows.setdefault(x['end'][:7],[]).append((x['filed'],x['val'],x['accn']))
    out={}
    for k,v in rows.items():
        v.sort(); out[k]=v
    return out
for t in sys.argv[1:]:
    s=ser(t)
    print(t)
    for k in sorted(s):
        if k<'2016': continue
        vals=sorted(set(x[1] for x in s[k]))
        print('   ',k, ' / '.join(f"{v/1e3:,.0f}" for v in vals), s[k][0][2])
