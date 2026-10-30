import json,sys
sys.stdout.reconfigure(encoding='utf-8')
d=json.load(open('cache/companyfacts.json'))['facts']['us-gaap']
for tag in sys.argv[1:]:
    if tag not in d: print(tag,'NOT FOUND'); continue
    u=d[tag]['units']; k=list(u)[0]
    seen={}
    for f in u[k]:
        if f.get('fp')=='FY' and f['form']=='10-K' and f['end'][5:]=='12-31':
            # keep first-filed (earliest filed) for each end
            e=f['end']
            if ('start' in f) and (int(f['end'][:4])-int(f['start'][:4])!=0 and f['start'][5:]!='01-01'): continue
            if e not in seen or f['filed']<seen[e]['filed']: seen[e]=f
    print(tag, k, ' '.join(f"{e[:4]}:{seen[e]['val']/1e6:,.1f}" for e in sorted(seen) if e>='2014'))
