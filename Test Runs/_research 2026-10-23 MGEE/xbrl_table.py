import json,sys
from datetime import date
d=json.load(open(sys.argv[1]));g=d['facts']['us-gaap']
def annual(tag,dur=True):
    out={}
    if tag not in g: return out
    for u,vals in g[tag]['units'].items():
        for v in vals:
            if v.get('form')!='10-K': continue
            if dur:
                if 'start' not in v: continue
                s=date.fromisoformat(v['start']);e=date.fromisoformat(v['end'])
                if not 350<(e-s).days<380: continue
            e=v['end']
            # keep latest filed
            if e not in out or v['filed']>out[e][1]: out[e]=(v['val'],v['filed'],v['accn'])
    return out
tags=sys.argv[2].split(',')
for t in tags:
    dur = not t.startswith('@')
    tt=t.lstrip('@')
    a=annual(tt,dur)
    print(tt)
    for e in sorted(a):
        if e>='2014': print('  ',e,f"{a[e][0]:>16,}",a[e][2])
