import json, os, datetime as dt
D=os.path.dirname(os.path.abspath(__file__))
R=json.load(open(os.path.join(D,'peers_raw.json')))
TICKS=['HUBB','VMI','NVT','AZZ','ATKR','THR','WIRE']
M=1e6
def g(d,k,i=0):
    v=d.get(k)
    return None if v is None else v[i]
for t in TICKS:
    d=R[t]
    ends=sorted(e for e in d['rev'] if e>='2018-06-01')
    print('\n==================',t)
    print('%-12s %10s %10s %10s %10s %10s %10s %10s %10s %10s %10s %10s %10s %-22s'%('FYend','days','rev','gp','cogs','oi','ni','eq','eq+nci','cfo','capex','d&a','assets','accn(rev)'))
    for e in ends:
        rv=d['rev'][e]
        def f(key,inst=False,scale=M):
            x=d[key].get(e)
            return '' if x is None else '%10.1f'%(x[0]/scale)
        print('%-12s %10d %s %s %s %s %s %s %s %s %s %s %s  %s'%(e,rv[4],
            '%10.1f'%(rv[0]/M), f('gp'), f('cogs'), f('oi'), f('ni'),
            f('eq'), f('eqt'), f('cfo'), f('capex'), f('da'), f('assets'), rv[1]))
    print('  GW/INT/LIAB:')
    for e in ends:
        def fi(key):
            x=d[key].get(e); return '' if x is None else '%10.1f'%(x[0]/M)
        print('   %-12s gw=%s int=%s liab=%s'%(e,fi('gw'),fi('int'),fi('liab')))
