import json,sys
f=json.load(open('cache/facts.json'))['facts']
def annual(tag, ns='us-gaap'):
    d=f.get(ns,{}).get(tag)
    if not d: return {}
    out={}
    for u,arr in d['units'].items():
        for x in arr:
            if x.get('form') in ('10-K','10-K/A') and x.get('fp')=='FY':
                if 'start' in x:
                    from datetime import date
                    s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                    if (e-s).days<350: continue
                y=int(x['end'][:4])
                # keep latest filed
                if y not in out or x['filed']>out[y][1]: out[y]=(x['val'],x['filed'],x['accn'])
    return out
if __name__=='__main__':
    for t in sys.argv[1:]:
        a=annual(t)
        print(t, {y:round(v[0]/1e6,1) for y,v in sorted(a.items()) if y>=2014})
