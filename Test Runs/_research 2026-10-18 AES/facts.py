import json,sys
d=json.load(open('cache/facts.json'))
g=d['facts']['us-gaap']; a=d['facts'].get('aes',{})
def annual(tag, src=None):
    src = src or (g if tag in g else a)
    if tag not in src: return {}
    out={}
    for u,v in src[tag]['units'].items():
        for x in v:
            if x.get('form') in ('10-K','10-K/A') and x.get('fp')=='FY':
                end=x['end']
                if 'start' in x:
                    from datetime import date
                    s=date.fromisoformat(x['start']); e=date.fromisoformat(end)
                    if (e-s).days<350: continue
                # keep the latest filed value for that end date
                if end not in out or x['filed']>out[end][1]: out[end]=(x['val'],x['filed'])
    return out
tags=sys.argv[1:]
for t in tags:
    o=annual(t)
    print(t, {k[:4]:round(v[0]/1e6) for k,v in sorted(o.items()) if k>='2012'})
