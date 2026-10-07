import math
# USD millions, from the filed cash-flow statements (accessions in run file)
yrs=[2021,2022,2023,2024,2025]
OCF=[539.902,744.658,761.240,561.644,761.985]
SBC=[26.184,29.613,34.486,35.966,38.426]
RCX=[278.498,443.138,226.976,280.857,317.685]
RPR=[55.210,70.703,51.290,63.997,65.868]
PCX=[30.498,43.664,22.237,18.435,24.331]
PPR=[0.387,0.504,13.272,1.867,2.944]
FLP=[17.399,42.228,16.634,19.429,27.332]
ACQ=[147.172,220.620,561.629,121.221,144.698]
DA=[318.202,343.507,338.654,384.972,430.021]
A=[o-s-r+p-c+q-f for o,s,r,p,c,q,f in zip(OCF,SBC,RCX,RPR,PCX,PPR,FLP)]
B=[a-x for a,x in zip(A,ACQ)]
D=[o-s-d-f for o,s,d,f in zip(OCF,SBC,DA,FLP)]
A2=A[:]; A2[3]+=225.7  # 2024 McGrath fee and deal costs added back (variant)
for n,v in [('A all-in as filed',A),('A2 2024 deal cost added back',A2),('B A less acquisitions',B),('D D&A variant (OCF-SBC-D&A-fin lease)',D)]:
    print(f"{n:42s}",' '.join(f'{x:8.1f}' for x in v),' avg',round(sum(v)/5,1))
def lsg(v):
    xs=range(len(v)); ly=[math.log(x) for x in v]; mx=sum(xs)/len(v); my=sum(ly)/len(v)
    b=sum((x-mx)*(y-my) for x,y in zip(xs,ly))/sum((x-mx)**2 for x in xs); return math.exp(b)-1
print('growth A: endpoint CAGR %.3f  log-linear %.3f'%((A[-1]/A[0])**0.25-1,lsg(A)))
print('growth A2: log-linear %.3f'%lsg(A2))
print('growth D: log-linear %.3f'%lsg(D))
r=0.0563; sh=181.190958; price=17.07
def value(C,g,r=r):
    pv=sum(C*(1+g)**t/(1+r)**t for t in range(1,11))
    pv+=C*(1+g)**10/r/(1+r)**10
    return pv
def irr_price(C,g,target=0.10):
    return value(C,g,target)
for nm,C in [('A',sum(A)/5),('A2',sum(A2)/5),('D',sum(D)/5),('B',sum(B)/5)]:
    for g in [0,0.0563]:
        print(nm,'g=%.4f'%g,'value/share %.2f'%(value(C,g)/sh),' price at 10%% expected return %.2f'%(irr_price(C,g)/sh))
print('mktcap',price*sh)
for nm,C in [('A',sum(A)/5),('A2',sum(A2)/5),('D',sum(D)/5),('B',sum(B)/5)]:
    print(nm,'yield at price %.2f%%'%(100*C/(price*sh)))
g=0.0563/2
for nm,C in [('A',sum(A)/5),('A2',sum(A2)/5),('D',sum(D)/5)]:
    print('central',nm,'g=%.4f value %.2f  fair(10%%) %.2f'%(g,value(C,g)/sh,irr_price(C,g)/sh))
# expected return at current price, A, no growth and central
def irr(C,g,P):
    lo,hi=0.0001,1
    for _ in range(100):
        m=(lo+hi)/2
        if value(C,g,m)>P: lo=m
        else: hi=m
    return m
for nm,C in [('A',sum(A)/5),('A2',sum(A2)/5),('D',sum(D)/5),('B',sum(B)/5)]:
    print('expected return at $17.07',nm,' g0 %.3f  gc %.3f'%(irr(C,0,price*sh),irr(C,g,price*sh)))
# rental depreciation vs net rental capex
rdep=[218.790,256.7,265.7,302.1,334.0]
net=[r-p for r,p in zip(RCX,RPR)]
print('net rental capex',[round(x,1) for x in net],round(sum(net)/5,1),' rental dep',rdep,round(sum(rdep)/5,1))
