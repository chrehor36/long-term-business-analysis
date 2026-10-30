import json,sys
def load(t): return json.load(open(f'cache/{t}_companyfacts.json'))
def annual(d,tag,unit='USD',ns='us-gaap'):
    f=d['facts'].get(ns,{}).get(tag)
    if not f: return {}
    out={}
    for u,arr in f['units'].items():
        if u!=unit: continue
        for x in arr:
            if x.get('form') not in ('10-K','10-K/A'): continue
            fp=x.get('fp'); 
            if 'start' in x:
                from datetime import date
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if not (350<(e-s).days<380): continue
            y=x['end'][:4]
            # keep the latest-filed value per end date
            k=x['end']
            if k not in out or x['filed']>out[k][1]: out[k]=(x['val'],x['filed'],x['accn'])
    return out
if __name__=='__main__':
    t=sys.argv[1]; d=load(t)
    for tag in sys.argv[2:]:
        ns='us-gaap'
        if ':' in tag: ns,tag=tag.split(':')
        a=annual(d,tag,ns=ns)
        print(tag, {k[:4]:round(v[0]/1e6,1) for k,v in sorted(a.items())})
