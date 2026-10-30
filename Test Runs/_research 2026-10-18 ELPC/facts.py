import json,sys
d=json.load(open('cache/facts.json'))['facts']['ifrs-full']
for tag in sys.argv[1:]:
    if tag not in d: print(tag,'MISSING'); continue
    for u,vals in d[tag]['units'].items():
        best={}
        for v in vals:
            if v.get('form','').startswith('20-F') and (('start' in v and v['end'][5:]=='12-31' and v['start'][5:]=='01-01') or 'start' not in v and v['end'][5:]=='12-31'):
                k=v['end'][:4]
                if k not in best or v['filed']>best[k]['filed']: best[k]=v
        print(tag,u,' '.join(f"{k}:{best[k]['val']/1e6:,.0f}" for k in sorted(best)))
