# print annual values (12-month duration or instant at FY end) for given tags from cache/facts.json
import json, sys
d=json.load(open('cache/facts.json'))['facts']['us-gaap']
from datetime import date
def ann(tag):
    if tag not in d: return {}
    out={}
    for unit,vals in d[tag]['units'].items():
        for v in vals:
            if v.get('form') not in ('40-F','10-K','40-F/A'): continue
            e=v['end']
            if 'start' in v:
                s=date.fromisoformat(v['start']); en=date.fromisoformat(e)
                if not (350<=(en-s).days<=380): continue
            if not e.endswith('12-31'): continue
            # keep latest-filed value per end year
            k=e[:4]
            if k not in out or v['filed']>out[k][1]:
                out[k]=(v['val'],v['filed'],v['accn'])
    return out
tags=sys.argv[1:]
yrs=sorted({y for t in tags for y in ann(t)})
print('tag'.ljust(60),' '.join(y.rjust(9) for y in yrs))
for t in tags:
    a=ann(t)
    print(t[:60].ljust(60),' '.join((f"{a[y][0]/1e6:9.1f}" if y in a else ' '*9) for y in yrs))
