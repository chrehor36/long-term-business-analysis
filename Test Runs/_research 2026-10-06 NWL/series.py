import json,sys
d=json.load(open(sys.argv[1]))['facts']['us-gaap']
def annual(tag):
    if tag not in d: return {}
    out={}
    for u,arr in d[tag]['units'].items():
        for x in arr:
            if x.get('form') in ('10-K','10-K/A') and x.get('fp')=='FY':
                if 'start' in x:
                    from datetime import date
                    s=date.fromisoformat(x['start']);e=date.fromisoformat(x['end'])
                    if (e-s).days<350: continue
                y=x['end'][:4]
                # keep latest-filed value per year
                if y not in out or x['filed']>out[y][1]: out[y]=(x['val'],x['filed'],x['accn'])
    return out
tags=sys.argv[2:]
for t in tags:
    a=annual(t)
    print(t, {y:round(v[0]/1e6) for y,v in sorted(a.items()) if y>='2012'})
