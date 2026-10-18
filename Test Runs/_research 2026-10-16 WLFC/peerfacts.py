import json,sys
from datetime import date
f=sys.argv[1]; tags=sys.argv[2:]
d=json.load(open(f))['facts']
def series(tag, inst=False):
    for ns in ('us-gaap','ifrs-full'):
        if ns in d and tag in d[ns]:
            out={}
            for u,arr in d[ns][tag]['units'].items():
                for x in arr:
                    if x.get('form') not in ('10-K','20-F','10-K/A','20-F/A'): continue
                    if inst:
                        if 'start' in x: continue
                        if x['end'][5:]!='12-31': continue
                    else:
                        if 'start' not in x: continue
                        if (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<350: continue
                    y=x['end'][:4]
                    if y not in out or x['filed']<out[y][1]: out[y]=(x['val'],x['filed'],x['accn'])
            return out
    return {}
for t in tags:
    inst=t.startswith('@'); tt=t.lstrip('@')
    s=series(tt,inst)
    print(tt, ' '.join(f"{y}:{v[0]/1e6:.0f}" for y,v in sorted(s.items()) if y>='2015'))
