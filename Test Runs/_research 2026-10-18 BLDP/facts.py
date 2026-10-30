import json,sys
d=json.load(open('cache/facts.json'))['facts']['ifrs-full']
want=sys.argv[1:]
for k in want:
    if k not in d: print('MISSING',k); continue
    u=d[k]['units']; 
    for un,arr in u.items():
        rows={}
        for x in arr:
            if x.get('form','').startswith('40-F') and (x.get('fp')=='FY'):
                key=x['end'] if 'start' not in x else (x['start'],x['end'])
                if 'start' in x:
                    from datetime import date
                    s=date.fromisoformat(x['start']);e=date.fromisoformat(x['end'])
                    if (e-s).days<300: continue
                rows[x['end']]=(x['val'],x['accn'])
        print(k,un, ' '.join(f"{e[:4]}:{v/1e6:.1f}" for e,(v,a) in sorted(rows.items())))
