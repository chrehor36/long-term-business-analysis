import json,sys
d=json.load(open(sys.argv[1]))
g=d['facts']['us-gaap']
tags=sys.argv[2].split(',')
for t in tags:
    if t not in g: print(t,'MISSING'); continue
    u=g[t]['units']; un=list(u)[0]
    rows={}
    for x in u[un]:
        if x.get('fp')=='FY' and x['form'].startswith('10-K') and 'frame' in x and len(x['frame'])==6:
            rows[x['end']]=(x['val'],x['accn'])
        elif x.get('fp')=='FY' and x['form'].startswith('10-K') and 'start' not in x and x['end'][5:]=='09-30':
            rows.setdefault(x['end'],(x['val'],x['accn']))
    print(t,un)
    for k in sorted(rows):
        if k>='2014': print('  ',k,rows[k][0]/1e6 if un=='USD' else rows[k][0],rows[k][1])
