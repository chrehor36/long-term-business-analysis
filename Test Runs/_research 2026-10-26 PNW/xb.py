import json,sys
sys.stdout.reconfigure(encoding='utf-8')
d=json.load(open('cache/facts_PNW.json'))['facts']
tags=sys.argv[1:]
def ann(tag):
    out={}
    for ns in d:
        if tag in d[ns]:
            for u,arr in d[ns][tag]['units'].items():
                for f in arr:
                    if f.get('form')=='10-K' and f.get('fp')=='FY':
                        y=int(f['end'][:4])
                        if f['end'][5:]!='12-31': continue
                        if 'start' in f and int(f['start'][:4])!=y: continue
                        if f.get('fy')==y and y not in out: out[y]=f['val']
    return out
for t in tags:
    o=ann(t); print(t.ljust(60),' '.join(f"{y}:{o[y]/1e6:,.0f}" for y in sorted(o) if 2015<=y<=2025))
