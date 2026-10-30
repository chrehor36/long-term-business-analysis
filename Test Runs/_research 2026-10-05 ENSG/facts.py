import sys, json
sys.path.insert(0,'tools')
import sources as s
cik = s.cik_for('ENSG')[0]
f = s.sec_facts(cik)
json.dump(f, open('Test Runs/_research 2026-10-05 ENSG/ENSG_facts.json','w'))
g = f['facts']['us-gaap']
def ann(tag):
    if tag not in g: return {}
    out={}
    for unit,vals in g[tag]['units'].items():
        for v in vals:
            if v.get('form') in ('10-K',) and v.get('fp')=='FY':
                # duration facts ~ 1 year, or instant
                st=v.get('start'); en=v['end']
                if st:
                    from datetime import date
                    d=(date.fromisoformat(en)-date.fromisoformat(st)).days
                    if d<340 or d>380: continue
                y=en[:4]
                # latest filed vintage
                if y not in out or v['filed']>out[y][1]:
                    out[y]=(v['val'],v['filed'])
    return {k:v[0] for k,v in out.items()}
tags = sys.argv[1:] 
for t in tags:
    a=ann(t)
    print(t, {k:round(v/1e6,1) if abs(v)>1e5 else v for k,v in sorted(a.items()) if k>='2014'})
