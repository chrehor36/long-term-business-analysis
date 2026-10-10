import json,sys
d=json.load(open('facts.json'))['facts']
def ann(tag,ns='us-gaap',unit='USD'):
    try: u=d[ns][tag]['units'][unit]
    except KeyError: return {}
    out={}
    for x in u:
        if x.get('fp')=='FY' and x.get('form') in ('10-K','10-K/A'):
            s,e=x.get('start'),x['end']
            if s and (int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])<11: continue
            y=int(e[:4])
            # keep earliest filed (first-filed vintage) per year
            if y not in out or x['filed']<out[y][1]: out[y]=(x['val'],x['filed'])
    return {k:v[0] for k,v in out.items()}
tags=sys.argv[1:]
rows={t:ann(t) for t in tags}
years=sorted(set().union(*[r.keys() for r in rows.values()]))
print('year '+' '.join(t[:22].rjust(23) for t in tags))
for y in years:
    print(y, ' '.join((f"{rows[t][y]/1e6:23.1f}" if y in rows[t] else ' '*23) for t in tags))
