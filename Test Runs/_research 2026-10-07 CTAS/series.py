import json,sys
cik=sys.argv[1] if len(sys.argv)>1 else 'cache/ctas_companyfacts.json'
d=json.load(open(cik))['facts']['us-gaap']
def fy(tag):
    if tag not in d: return {}
    out={}
    for u,arr in d[tag]['units'].items():
        for x in arr:
            if x.get('form') in ('10-K','10-K405','10-KT') and x.get('fp')=='FY':
                s=x.get('start'); e=x['end']
                if s:
                    from datetime import date
                    ds=date.fromisoformat(s); de=date.fromisoformat(e)
                    if not (350<(de-ds).days<380): continue
                # first-filed value per end date
                if e not in out or x['filed']<out[e][1]:
                    out[e]=(x['val'],x['filed'],x['accn'])
    return out
tags=sys.argv[2:] if len(sys.argv)>2 else []
for t in tags:
    v=fy(t)
    print(t)
    for e in sorted(v): print('  ',e,round(v[e][0]/1e6,1),v[e][2])
