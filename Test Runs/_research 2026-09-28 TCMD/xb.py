import json,sys
f=json.load(open('cache/facts.json'))
g=f['facts'].get('us-gaap',{})
tags=sys.argv[1:] 
def annual(tag):
    if tag not in g: return {}
    out={}
    for u,vals in g[tag]['units'].items():
        for v in vals:
            if v.get('fp')=='FY' and v.get('form','').startswith('10-K') and 'frame' in v or (v.get('form','').startswith('10-K') and v.get('start') and v['end'][5:]=='12-31' and v['start'][5:]=='01-01'):
                if v.get('start') and v['start'][5:]!='01-01': continue
                y=v['end'][:4]
                if y not in out or v['filed']>out[y][1]: out[y]=(v['val'],v['filed'])
    return {k:out[k][0] for k in sorted(out)}
def inst(tag):
    if tag not in g: return {}
    out={}
    for u,vals in g[tag]['units'].items():
        for v in vals:
            if 'start' in v: continue
            if v['end'][5:]!='12-31' and v['end']<'2026-01-01': continue
            y=v['end']
            if y not in out or v['filed']>out[y][1]: out[y]=(v['val'],v['filed'])
    return {k:out[k][0] for k in sorted(out)}
if __name__=='__main__':
    if tags==['list']:
        for k in sorted(g): print(k, list(g[k]['units']))
    for t in tags:
        a=annual(t) or inst(t)
        print(t, {k:round(v/1e6,3) if abs(v)>1000 else v for k,v in a.items()})
