import json,sys
d=json.load(open('cache/companyfacts.json'))['facts']['us-gaap']
def annual(tag):
    if tag not in d: return {}
    out={}
    for u,arr in d[tag]['units'].items():
        for x in arr:
            if x.get('form') in ('10-K','10-K/A') and x.get('fp')=='FY' and 'start' in x:
                # full-year duration
                from datetime import date
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if (e-s).days>350:
                    y=x['end'][:4]
                    out.setdefault(y, (x['val'], x['accn'], x['filed']))
                    # keep latest filed
                    if x['filed']>out[y][2]: out[y]=(x['val'],x['accn'],x['filed'])
    return out
tags=sys.argv[1:]
for t in tags:
    a=annual(t)
    print(t, ' '.join(f"{y}:{v[0]/1e6:.1f}" for y,v in sorted(a.items()) if y>='2012'))
