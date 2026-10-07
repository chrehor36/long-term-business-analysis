# COMPUTATION - NOT A CLEARANCE. All $M. Sources in run file.
helix={2021:(140.117,7.689,8.322,141.514),2022:(51.108,7.451,33.504,142.686),2023:(152.457,6.510,19.588,138.423),2024:(186.028,7.266,23.303,137.202),2025:(136.749,6.568,16.342,134.538)}
# (OCF, SBC, capex, depreciation used as maintenance proxy)
horn={2021:(49.6,3.372,4.1,15.672),2022:(113.0,5.330,109.2,18.601),2023:(146.115,19.097,168.345,26.355),2024:(16.477,9.384,120.020,37.812),2025:(142.075,7.723,114.698,41.554)}
r=0.0563; cash=684.499; shares=222.166587+103.637  # M shares
print('shares as-converted',shares)
tot={};dep={}
for y in range(2021,2026):
    h=helix[y];k=horn[y]
    a=h[0]-h[1]-h[2]; b=k[0]-k[1]-k[2]
    da=h[0]-h[1]-h[3]; db=k[0]-k[1]-k[3]
    tot[y]=a+b; dep[y]=da+db
    print(y,f"helix {a:7.1f} horn {b:7.1f} combined {a+b:7.1f} | dep-variant helix {da:7.1f} horn {db:7.1f} comb {da+db:7.1f}")
avg=sum(tot.values())/5; avgd=sum(dep.values())/5
print('avg all-capex',avg,'avg dep variant',avgd)
g=(tot[2025]/tot[2021])**(1/4)-1
print('shown growth endpoints',g)
def pv(c,g,yrs=10):
    v=0;x=c
    for t in range(1,yrs+1):
        x*=1+g; v+=x/(1+r)**t
    v+= x/r/(1+r)**yrs
    return v
for name,c in [('all-capex',avg),('dep variant',avgd)]:
    ng=c/r; sg=pv(c,g)
    print(name,'no-growth PV',round(ng,1),'per sh',round((ng+cash)/shares,2),round(ng/shares,2),'| shown-growth PV',round(sg,1),'per sh',round((sg+cash)/shares,2), round(sg/shares,2))
price=7.96
mc=price*shares
print('mkt cap',mc,'EV-ish (mc-cash)',mc-cash,'yield all-capex',avg/(mc-cash),'dep',avgd/(mc-cash))
fair=(avg/0.10+cash)/shares
print('fair price (10% on central all-capex no-growth, cash credited)',fair)
print('cheap: half of bottom')
