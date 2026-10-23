import json,sys
f=sys.argv[1]; d=json.load(open(f))['facts'].get('ifrs-full',{})
for tag in sys.argv[2:]:
    if tag not in d: print(tag,'MISSING'); continue
    for u,vals in d[tag]['units'].items():
        best={}
        for v in vals:
            if not v.get('form','').startswith('20-F'): continue
            ok=('start' in v and v['end'][5:]=='12-31' and v['start'][5:]=='01-01') or ('start' not in v and v['end'][5:]=='12-31')
            if ok:
                k=v['end'][:4]
                if k not in best or v['filed']>best[k]['filed']: best[k]=v
        print(tag,u,' '.join(f"{k}:{best[k]['val']/1e6:,.0f}" for k in sorted(best)))
        print('   acc', ' '.join(f"{k}:{best[k]['accn']}" for k in sorted(best))[:400])
