import json,sys
d=json.load(open(sys.argv[1]))
tags=sys.argv[2].split(',')
facts=d['facts'].get('us-gaap',{})
for t in tags:
    if t not in facts: print('MISSING',t); continue
    u=list(facts[t]['units'].keys())[0]
    rows={}
    for f in facts[t]['units'][u]:
        if f.get('form') not in ('10-K','10-K/A'): continue
        fy_end=f['end']
        if 'start' in f:
            from datetime import date
            s=date.fromisoformat(f['start']); e=date.fromisoformat(f['end'])
            if (e-s).days<350: continue
        if not fy_end.endswith(sys.argv[3] if len(sys.argv)>3 else '12-31'): continue
        # keep latest filed
        if fy_end not in rows or f['filed']>rows[fy_end][1]:
            rows[fy_end]=(f['val'],f['filed'],f['accn'])
    print(t, u)
    for k in sorted(rows):
        if k>='2014': print('  ',k, round(rows[k][0]/1e6,1) if abs(rows[k][0])>1e4 else rows[k][0], rows[k][2])
