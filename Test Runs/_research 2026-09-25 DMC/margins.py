import re
def load(f):
    rows={}
    for line in open(f):
        p=line.split()
        if p and p[0].isdigit():
            rows[p[0]]=p[1:]
    return rows
names={'series_DMC.txt':'DMC','series_1857475.txt':'Dole plc','series_18169.txt':'Dole Food Co','series_101063.txt':'Chiquita','series_1802974.txt':'Mission Produce','series_88948.txt':'Seneca'}
for f,n in names.items():
    r=load(f); out=[]
    for y,v in sorted(r.items()):
        def g(i):
            try: return float(v[i])
            except: return None
        rev,gp,op,ni=g(0),g(1),g(2),g(3)
        s=f"{y}: " + (f"GM {100*gp/rev:.1f}% " if rev and gp else "") + (f"OM {100*op/rev:.1f}%" if rev and op is not None else "")
        out.append(s)
    print(n,' | '.join(out))
r=load('series_DMC.txt')
print('DMC NI/avg equity:')
ys=sorted(r); import statistics
roes=[]
for i,y in enumerate(ys):
    if i==0: continue
    ni=float(r[y][3]); e0=r[ys[i-1]][11]; e1=r[y][11]
    if e0=='-' : continue
    roe=100*ni/((float(e0)+float(e1))/2); roes.append(roe); print(y,f"{roe:.1f}%",end='; ')
print('\nmean',statistics.mean(roes))
oms=[100*float(r[y][2])/float(r[y][0]) for y in ys]; print('OM mean 2008-25',statistics.mean(oms),'max',max(oms),'min',min(oms))
