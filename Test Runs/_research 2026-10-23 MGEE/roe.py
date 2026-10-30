import json,sys
from datetime import date
def annual(g,tag,dur=True):
    out={}
    if tag not in g: return out
    for u,vals in g[tag]['units'].items():
        for v in vals:
            if v.get('form')!='10-K' or v.get('fp')!='FY': continue
            if dur:
                if 'start' not in v: continue
                if not 350<(date.fromisoformat(v['end'])-date.fromisoformat(v['start'])).days<380: continue
            e=v['end']
            if e not in out or v['filed']>out[e][1]: out[e]=(v['val'],v['filed'],v['accn'])
    return out
for f,ni_tags,eq_tags in [(a.split(':')[0],a.split(':')[1].split('+'),a.split(':')[2].split('+')) for a in sys.argv[1:]]:
    d=json.load(open(f));g=d['facts']['us-gaap'];print(f,d['entityName'])
    ni={};eq={}
    for t in ni_tags: 
        for k,v in annual(g,t).items(): ni.setdefault(k,v)
    for t in eq_tags:
        pass
    for t in eq_tags:
        for k,v in annual(g,t,False).items(): eq.setdefault(k,v)
    yrs=[y for y in sorted(ni) if y>='2015-12' and y<'2026']
    tot=[]
    for y in yrs:
        py=str(int(y[:4])-1)+y[4:]
        if y in eq and py in eq:
            r=ni[y][0]/((eq[y][0]+eq[py][0])/2); tot.append(r)
            print(' ',y,f"NI {ni[y][0]/1e6:9.1f} EQ {eq[y][0]/1e6:9.1f} ROE {r*100:5.1f}%",ni[y][2])
    if tot: print('  avg ROE',round(sum(tot)/len(tot)*100,2),'n',len(tot))
