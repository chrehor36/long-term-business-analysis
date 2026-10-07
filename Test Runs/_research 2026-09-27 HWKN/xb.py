import json,sys
sys.stdout.reconfigure(encoding='utf-8')
f=json.load(open('cache/companyfacts.json'))['facts']
tags=sys.argv[1:]
for t in tags:
    for ns in ('us-gaap','dei','ifrs-full'):
        if t in f.get(ns,{}):
            u=f[ns][t]['units']
            for unit,vals in u.items():
                out={}
                for v in vals:
                    if v.get('form') in ('10-K','10-K/A') and v.get('fp')=='FY' and v.get('start'):
                        d=(v['end'])
                        import datetime
                        s=datetime.date.fromisoformat(v['start']);e=datetime.date.fromisoformat(v['end'])
                        if (e-s).days>340: out[d]=(v['val'],v['accn'])
                    elif v.get('form') in ('10-K',) and not v.get('start'):
                        out[v['end']]=(v['val'],v['accn'])
                print(t,unit)
                for k in sorted(out): print('  ',k,out[k][0]/1e6 if unit=='USD' else out[k][0],out[k][1])
