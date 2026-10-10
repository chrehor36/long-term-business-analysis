import json,sys
from datetime import date
d=json.load(open(sys.argv[1]))['facts']['us-gaap']
def fy(tag,latest=True):
    if tag not in d: return {}
    out={}
    for u,arr in d[tag]['units'].items():
        for x in arr:
            if x.get('form','').startswith('10-K') and x.get('start'):
                if not (350<(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<380): continue
                e=x['end']
                if e not in out or (x['filed']>out[e][1] if latest else x['filed']<out[e][1]):
                    out[e]=(x['val'],x['filed'],x['accn'])
    return out
for t in sys.argv[2:]:
    v=fy(t); print(t)
    for e in sorted(v):
        if e>='2015': print('  ',e,round(v[e][0]/1e6,1),v[e][2])
