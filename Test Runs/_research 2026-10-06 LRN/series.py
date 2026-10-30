import json,sys
d=json.load(open(sys.argv[1]))
g=d['facts'].get('us-gaap',{}); g.update({('lrn:'+k):v for k,v in d['facts'].get('lrn',{}).items()})
def annual(tag):
    if tag not in g: return {}
    out={}
    for u,vals in g[tag]['units'].items():
        for v in vals:
            if v.get('fp')=='FY' and v.get('form','').startswith('10-K'):
                s,e=v.get('start'),v['end']
                if s and (int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])<11: continue
                fy=e[:4] if e[5:7]>='06' else str(int(e[:4]))
                # keep earliest filed (first vintage)
                if e not in out or v['filed']<out[e][1]: out[e]=(v['val'],v['filed'])
    return {k:v[0] for k,v in out.items()}
tags=sys.argv[2].split(',')
allk=sorted(set().union(*[annual(t).keys() for t in tags]))
res={t:annual(t) for t in tags}
print('end'.ljust(11)+''.join(t.split(':')[-1][:22].rjust(24) for t in tags))
for k in allk:
    if k<'2009': continue
    print(k.ljust(11)+''.join((f"{res[t][k]/1e6:,.1f}" if k in res[t] else '-').rjust(24) for t in tags))
