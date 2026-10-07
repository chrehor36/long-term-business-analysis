import json,sys
from fetch import get
tk=sys.argv[1]; cik=int(sys.argv[2])
d=json.loads(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json',f'{tk}_facts.json'))
g=d['facts'].get('us-gaap',{})
def annual(tag):
    if tag not in g: return {}
    out={}
    for u,arr in g[tag]['units'].items():
        for x in arr:
            if x.get('form') in ('10-K','10-K/A') and x.get('fp')=='FY':
                s=x.get('start'); e=x['end']
                if s and (int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])<11: continue
                # keep first-filed per end
                if e not in out or x['filed']<out[e][1]: out[e]=(x['val'],x['filed'])
    return {k[:4]:v[0] for k,v in out.items()}
tags=sys.argv[3].split(',')
rows={}
for t in tags:
    a=annual(t)
    for y,v in a.items(): rows.setdefault(y,{})[t]=v
print('year,'+','.join(tags))
for y in sorted(rows):
    print(y+','+','.join(str(round(rows[y][t]/1e6,1)) if t in rows[y] and abs(rows[y][t])>1000 else str(rows[y].get(t,'')) for t in tags))
