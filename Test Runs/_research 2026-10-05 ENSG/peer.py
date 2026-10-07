import sys, json
sys.path.insert(0,'tools')
import sources as s
from datetime import date
tk=sys.argv[1]
cik=s.cik_for(tk)[0]
f=s.sec_facts(cik)
json.dump(f,open(f'Test Runs/_research 2026-10-05 ENSG/{tk}_facts.json','w'))
g=f['facts'].get('us-gaap',{})
def ann(tag):
    out={}
    if tag not in g: return out
    for unit,vals in g[tag]['units'].items():
        for v in vals:
            if v.get('form') in ('10-K','10-K/A') and v.get('fp')=='FY':
                st=v.get('start'); en=v['end']
                if st:
                    d=(date.fromisoformat(en)-date.fromisoformat(st)).days
                    if d<340 or d>380: continue
                y=en[:4]
                if y not in out or v['filed']>out[y][1]: out[y]=(v['val'],v['filed'],v['accn'])
    return out
for t in sys.argv[2:]:
    a=ann(t)
    print(t,{k:round(v[0]/1e6,1) for k,v in sorted(a.items()) if k>='2013'})
    if a: print('   accn latest:',sorted(a.items())[-1][1][2])
