import json, sys
def annual(facts, tag, unit='USD', duration=True):
    try: arr=facts['facts']['us-gaap'][tag]['units'][unit]
    except KeyError: return {}
    out={}
    for x in arr:
        if x.get('form') not in ('10-K','10-K/A'): continue
        if duration:
            if 'start' not in x: continue
            from datetime import date
            s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
            if not (350<= (e-s).days <=380): continue
        fy=x['end'][:4]
        # keep first filed (earliest 'filed') for each end
        k=x['end']
        if k not in out or x['filed']<out[k][1]: out[k]=(x['val'],x['filed'],x['accn'])
    return out
if __name__=='__main__':
    f=json.load(open(sys.argv[1])); 
    for tag in sys.argv[2:]:
        dur = not tag.startswith('@')
        t=tag.lstrip('@')
        d=annual(f,t,duration=dur)
        print(t, {k[:4]:round(v[0]/1e6,1) for k,v in sorted(d.items()) if k>='2015-06'})
