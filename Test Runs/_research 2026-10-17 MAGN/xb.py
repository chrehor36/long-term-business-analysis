import json,sys
cik=sys.argv[1]; tags=sys.argv[2].split(','); maxfiled=sys.argv[3] if len(sys.argv)>3 else '9999'
d=json.load(open(f'cache/cf_{cik}.json'))
for tag in tags:
    for ns in ('us-gaap','dei'):
        if tag in d['facts'].get(ns,{}):
            u=d['facts'][ns][tag]['units']
            for unit,vals in u.items():
                rows={}
                for v in vals:
                    if v['form'] not in ('10-K','10-K/A') or v['filed']>maxfiled: continue
                    if 'start' in v:
                        from datetime import date
                        s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                        if not 340<(e-s).days<380: continue
                    k=v['end']
                    if k not in rows: rows[k]=(v['val'],v['accn'],v['filed'])  # first filed
                print(tag,unit)
                for k in sorted(rows): print('  ',k,rows[k][0]/1e6 if unit=='USD' else rows[k][0],rows[k][1],rows[k][2])
