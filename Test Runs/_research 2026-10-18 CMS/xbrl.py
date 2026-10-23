import json,sys
d=json.load(open(sys.argv[1]))
g=d['facts']['us-gaap']
def series(tag, fy=True):
    if tag not in g: return {}
    out={}
    for unit,arr in g[tag]['units'].items():
        for x in arr:
            if x.get('form') not in ('10-K','10-K/A'): continue
            if fy and x.get('fp')!='FY': continue
            if 'start' in x:
                # annual duration only
                from datetime import date
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if (e-s).days<350 or (e-s).days>380: continue
            k=x['end']
            # keep latest filed
            if k not in out or x['filed']>out[k][1]:
                out[k]=(x['val'],x['filed'],x['accn'])
    return out
tags=sys.argv[2:]
for t in tags:
    s=series(t)
    print(t)
    for k in sorted(s):
        if k>='2014-12-31': print('  ',k,s[k][0]/1e6 if isinstance(s[k][0],(int,float)) else s[k][0],s[k][2])
