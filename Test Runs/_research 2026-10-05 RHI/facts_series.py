import json,sys
f=json.load(open('facts.json'))['facts']['us-gaap']
def ser(tag, form='10-K'):
    if tag not in f: return {}
    out={}
    for u,vals in f[tag]['units'].items():
        for v in vals:
            if v.get('form')!=form: continue
            if 'start' in v:
                from datetime import date
                s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                if not (350<(e-s).days<380): continue
            fy=v['end'][:4]
            # keep the latest filed
            if fy not in out or v['filed']>out[fy][1]:
                out[fy]=(v['val'],v['filed'])
    return {k:v[0] for k,v in out.items()}
tags=sys.argv[1:]
for t in tags:
    s=ser(t)
    print(t, {k:round(v/1e6,1) if abs(v)>1e4 else v for k,v in sorted(s.items())})
