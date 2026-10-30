import json,datetime as dt
f=json.load(open('facts.json'))['facts']['us-gaap']
def annual(tag,unit='USD',first=True):
    out={}
    if tag not in f: return out
    for x in f[tag]['units'].get(unit,[]):
        if x.get('form')!='10-K': continue
        if 'start' in x:
            d=(dt.date.fromisoformat(x['end'])-dt.date.fromisoformat(x['start'])).days
            if d<350 or d>380: continue
        y=x['end'][:4]
        if y not in out or (first and x['filed']<out[y][1]) or (not first and x['filed']>out[y][1]):
            out[y]=(x['val'],x['filed'])
    return {k:round(v[0]/1e6,1) for k,v in sorted(out.items()) if k>='2014'}
import sys
for t in sys.argv[1:]:
    u='shares' if 'Shares' in t else 'USD'
    print(t, annual(t,u))
