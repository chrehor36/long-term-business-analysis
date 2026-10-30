import json, sys
d = json.load(open(sys.argv[1]))['facts']['us-gaap']
for t in sys.argv[2].split(','):
    if t not in d: print(t,'MISSING'); continue
    u = d[t]['units']; k=list(u)[0]; rows={}
    for f in u[k]:
        if f.get('fp')=='FY' and f['form'].startswith('10-K') and 'start' not in f:
            rows.setdefault(f['end'], f['val'])
    print(t, ' '.join(f"{e[:7]}:{v/1e6:.0f}" for e,v in sorted(rows.items()) if e>='2015'))
