import json
x=json.load(open('xb_rows.json'))
g=lambda k,y: x.get(k,{}).get(str(y))
# fiscal 2017 from the 424B1 (2018-10-30) statements, $
pro={2017:dict(Rev=76343441,GP=41697229,OpInc=-6170891)}
rows=[]
for y in range(2017,2027):
    R=g('Rev',y) or pro.get(y,{}).get('Rev'); GP=g('GP',y) or pro.get(y,{}).get('GP'); OI=g('OpInc',y) or pro.get(y,{}).get('OpInc')
    NI=g('NI',y); Eq=g('Equity',y); C=g('Cash',y); Adv=g('Adv',y); A=g('Assets',y)
    rows.append((y,R,GP,OI,NI,Eq,C,Adv,A))
print('FY    sales   GM%   OI    OM%   NI     equity  cash  opcap  OI/avg-opcap  NI/avg-eq  adv%  OI/avg(assets-cash)')
prev=None
out=[]
for y,R,GP,OI,NI,Eq,C,Adv,A in rows:
    oc=(Eq-C) if (Eq is not None and C is not None) else None
    nc=(A-C) if (A is not None and C is not None) else None
    r1=r2=r3=None
    if prev:
        if oc is not None and prev[0] is not None: r1=OI/((oc+prev[0])/2)
        if NI is not None and Eq and prev[1]: r2=NI/((Eq+prev[1])/2)
        if nc is not None and prev[2] is not None: r3=OI/((nc+prev[2])/2)
    f=lambda v,s=1e6,p='%7.1f': (p%(v/s)) if v is not None else '      -'
    pc=lambda v: ('%6.1f%%'%(100*v)) if v is not None else '     -'
    line='%d %s %s %s %s %s %s %s %s %s %s %s %s'%(y,f(R),pc(GP/R),f(OI),pc(OI/R),f(NI),f(Eq),f(C),f(oc),pc(r1),pc(r2),pc(Adv/R if Adv else None),pc(r3))
    print(line); out.append(line)
    prev=(oc,Eq,nc)
open('q2_series.txt','w').write('\n'.join(out))
