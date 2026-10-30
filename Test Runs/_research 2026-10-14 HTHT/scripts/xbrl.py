import sys, os, json
sys.path.insert(0, os.path.join(os.getcwd(), 'tools'))
import sources as S
cik,_=S.cik_for(sys.argv[1] if len(sys.argv)>1 else 'HTHT')
f=S.sec_facts(cik)['facts']['us-gaap']
def series(tag, inst=False):
    if tag not in f: return {}
    out={}
    for unit,vals in f[tag]['units'].items():
        for v in vals:
            if v.get('form') not in ('20-F','10-K','20-F/A','10-K/A'): continue
            end=v['end']
            if not inst:
                st=v.get('start')
                if not st: continue
                from datetime import date
                d=(date.fromisoformat(end)-date.fromisoformat(st)).days
                if d<340 or d>380: continue
            # keep latest filed value for that end
            k=end[:4] if end[5:7] in('12','11','10') else end
            prev=out.get(k)
            if prev is None or v['filed']>prev[1]: out[k]=(v['val'],v['filed'],unit)
    return out
tags=sys.argv[2].split(',')
inst=len(sys.argv)>3 and sys.argv[3]=='inst'
yrs=sorted(set(y for t in tags for y in series(t,inst)))
print('year'.ljust(12)+''.join(t[:22].rjust(24) for t in tags))
for y in yrs:
    row=y.ljust(12)
    for t in tags:
        s=series(t,inst).get(y)
        row+=(f"{s[0]/1e6:,.0f}" if s else '-').rjust(24)
    print(row)
