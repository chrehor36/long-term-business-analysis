# COMPUTATION - NOT A CLEARANCE. Owner cash per year (USD M) from the filed cash-flow statements.
ocf ={2022:163.8,2023:205.7,2024:288.4,2025:333.7,2026:470.8}  # continuing operations
sbc ={2022:22.6,2023:14.3,2024:25.9,2025:41.6,2026:41.2}
capex={2022:31.1,2023:37.0,2024:48.9,2025:50.3,2026:77.7}
dep ={2022:44.6,2023:41.6,2024:39.7,2025:40.7,2026:43.9}
dtax={2022:-13.7,2023:-4.9,2024:11.1,2025:18.4,2026:68.4}
A={y:ocf[y]-sbc[y]-capex[y] for y in ocf}
B={y:A[y]-dtax[y] for y in ocf}
D={y:ocf[y]-sbc[y]-dep[y] for y in ocf}
mean=lambda d,ys: sum(d[y] for y in ys)/len(ys)
Y5=[2022,2023,2024,2025,2026]; Y4=[2023,2024,2025,2026]
for n,d in [('A capex',A),('B capex, tax at provision',B),('D depreciation',D)]:
    print(n,{y:round(v,1) for y,v in d.items()},'5yr',round(mean(d,Y5),1),'4yr ex-FY22',round(mean(d,Y4),1))
r=0.0566; sh=34.0388; price=125.39; tax=0.225
def V(C,g,r=r):
    pv=sum(C*(1+g)**t/(1+r)**t for t in range(1,11))
    pv+=C*(1+g)**10/r/(1+r)**10
    return pv
cagr=lambda d,a,b:(d[b]/d[a])**(1/(b-a))-1
print('shown growth A FY22-26 %.1f%%  FY23-26 %.1f%%'%(100*cagr(A,2022,2026),100*cagr(A,2023,2026)))
for lab,C in [('A 5yr',mean(A,Y5)),('A 4yr',mean(A,Y4)),('B 5yr',mean(B,Y5)),('B 4yr',mean(B,Y4)),('D 5yr',mean(D,Y5))]:
    lo=V(C,0); hi=V(C,r)
    print(f'{lab}: C={C:.1f}  no-growth ${lo:,.0f}M = ${lo/sh:.2f}/sh   capped growth {r:.2%} ${hi:,.0f}M = ${hi/sh:.2f}/sh  ratio {hi/lo:.2f}')
# fair price: central case = A 5yr, growth midpoint, pre-tax gross-up, discounted at 10%
C=mean(A,Y5); gc=r/2
fair=V(C/(1-tax),gc,0.10)
print(f'FAIR central A5 g={gc:.2%}: ${fair:,.0f}M = ${fair/sh:.2f}/sh')
fairB=V(mean(B,Y5)/(1-tax),gc,0.10); print(f'FAIR central B5: ${fairB/sh:.2f}/sh')
fair4=V(mean(A,Y4)/(1-tax),gc,0.10); print(f'FAIR central A4: ${fair4/sh:.2f}/sh')
cheap=(mean(B,Y5)/(1-tax))/0.15
print(f'CHEAP no-growth B5 at 15% pre-tax: ${cheap:,.0f}M = ${cheap/sh:.2f}/sh')
mc=price*sh; print('mkt cap',round(mc,0))
# implied pre-tax yield and growth at price
for lab,Cx in [('A5',mean(A,Y5)),('A FY26',A[2026]),('B5',mean(B,Y5))]:
    print(lab,'after-tax yield %.2f%%  pre-tax yield %.2f%%'%(100*Cx/mc,100*Cx/(1-tax)/mc))
# expected pre-tax return at price for central case (IRR)
def irr(P,C,g):
    lo,hi=0.0,0.5
    for _ in range(100):
        m=(lo+hi)/2
        (lo,hi)=(m,hi) if V(C,g,m)>P else (lo,m)
    return m
print('IRR pre-tax central A5 at price %.2f%%'%(100*irr(mc,mean(A,Y5)/(1-tax),gc)))
print('IRR pre-tax capped-growth A5 at price %.2f%%'%(100*irr(mc,mean(A,Y5)/(1-tax),r)))
