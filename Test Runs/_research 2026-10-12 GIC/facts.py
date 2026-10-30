import json,sys
def series(cik, tags, form='10-K', dur=True):
    d=json.load(open(f'cache/facts_{cik}.json'))
    out={}
    for t in tags:
        f=d['facts'].get('us-gaap',{}).get(t)
        if not f: continue
        for u,vals in f['units'].items():
            for v in vals:
                if v.get('form')!=form: continue
                if dur:
                    if 'start' not in v: continue
                    from datetime import date
                    s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                    if not (350<=(e-s).days<=380): continue
                yr=v['end'][:4] if v['end'][5:7]!='01' else str(int(v['end'][:4])-1)
                key=(yr)
                # keep earliest filed (first vintage)
                if key not in out or v['filed']<out[key][1]:
                    out[key]=(v['val'],v['filed'],t,v['accn'])
    return out
if __name__=='__main__':
    cik=sys.argv[1]; dur=sys.argv[2]=='d'; tags=sys.argv[3:]
    s=series(cik,tags,dur=dur)
    for k in sorted(s): print(k, round(s[k][0]/1e6,1), s[k][1], s[k][2], s[k][3])
