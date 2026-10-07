import json,sys
from datetime import date
def series(path,tags):
    d=json.load(open(path))
    g=d['facts']['us-gaap']
    res={}
    for k in tags:
        if k not in g: continue
        for u,arr in g[k]['units'].items():
            for x in arr:
                if not x['form'].startswith('10-K'): continue
                if 'start' in x:
                    s=date.fromisoformat(x['start']);e=date.fromisoformat(x['end'])
                    if not (350<=(e-s).days<=380): continue
                y=int(x['end'][:4]) if x['end'][5:7]>'06' else int(x['end'][:4])-1
                # keep latest-filed value per year (restated) - use first filed? keep first filed
                key=(k,y)
                if key not in res or x['filed']<res[key][1]:
                    res[key]=(x['val'],x['filed'])
    out={}
    for (k,y),(v,f) in res.items(): out.setdefault(k,{})[y]=v
    return out
if __name__=='__main__':
    tags=sys.argv[2].split(',')
    o=series(sys.argv[1],tags)
    for k in tags:
        if k in o: print(k,{y:round(o[k][y]/1e6,1) for y in sorted(o[k])})
