# Q7 arithmetic for the MA run of 2026-10-10. Figures in USD millions from the filed cash-flow statements
# (10-K FY2025 0001141391-26-000013 for 2023-2025; FY2022 0001141391-23-000020 and FY2024 0001141391-25-000011 for 2021-2022;
# FY2020 0001141391-21-000018 for 2019-2020). Interest: paid where filed (2023-2025, 10-K FY2025 Note 13); expense for 2019-2022.
R = 0.056; SH = 876.0; ND = 14534.0; PRICE = 589.14; T = 0.21
ocf = {2019:8183, 2020:7224, 2021:9463, 2022:11195, 2023:11980, 2024:14780, 2025:17648}
sbc = {2019:250, 2020:254, 2021:273, 2022:295, 2023:460, 2024:526, 2025:597}
cap = {2019:422+306, 2020:339+369, 2021:407+407, 2022:442+655, 2023:371+717, 2024:474+720, 2025:489+726}
acq = {2019:1440, 2020:989, 2021:4436, 2022:313, 2023:0, 2024:2511, 2025:0}
intr= {2019:224, 2020:380, 2021:431, 2022:471, 2023:477, 2024:571, 2025:680}
dna = {2019:522, 2020:580, 2021:726, 2022:750, 2023:799, 2024:897, 2025:1143}
def oc(y, acqs=True, allequity=True, basis='capex'):
    c = ocf[y]-sbc[y]-(cap[y] if basis=='capex' else dna[y])-(acq[y] if acqs else 0)
    if allequity: c += intr[y]*(1-T)
    return c
def value(c, g, n=10, r=R):
    pv = sum(c*(1+g)**t/(1+r)**t for t in range(1,n+1))
    pv += c*(1+g)**n/r/(1+r)**n
    return pv
def per_share(v, allequity=True):
    return (v-ND)/SH if allequity else v/SH
def fair(c_mid_value_ps, allequity=True):
    pass
yrs = [2021,2022,2023,2024,2025]
out=[]
for ae in (True, False):
    lab = 'ALL-EQUITY' if ae else 'EQUITY-ONLY'
    pre = [oc(y,False,ae) for y in yrs]; post=[oc(y,True,ae) for y in yrs]
    base = sum(post)/5
    g_lit = (pre[-1]/pre[0])**(1/4)-1
    g_cyc = (oc(2025,False,ae)/oc(2019,False,ae))**(1/6)-1
    print(f'== {lab}')
    for y in yrs: print(y, 'pre-acq', round(oc(y,False,ae)), 'post-acq', round(oc(y,True,ae)), 'D&A basis post-acq', round(oc(y,True,ae,'dna')))
    print('5-yr avg owner cash after acquisitions', round(base), ' growth literal 2021-25 (pre-acq, aggregate)', round(g_lit*100,1), '% ; 2019-25', round(g_cyc*100,1),'%')
    for name,g in (('no growth',0.0),('cycle 2019-25',g_cyc),('literal 2021-25',g_lit)):
        v = value(base,g); ps = per_share(v,ae)
        print(f'  {name:18s} g={g*100:5.1f}%  value ${v/1e3:7.1f}B  per share ${ps:8.2f}')
    lo = per_share(value(base,0),ae)
    for name,g in (('cycle',g_cyc),('literal',g_lit)):
        hi = per_share(value(base,g),ae); mid=(lo+hi)/2
        # fair price: price at which the midpoint earns 10%: discount the midpoint case's cash at 10% -> equivalently
        # find growth-consistent value at r=10%. Midpoint defined as value-per-share midpoint; the cash stream that gives
        # the midpoint at 5.6% is scaled; its value at 10% is the fair price.
        # Midpoint stream: average of the two streams (no-growth and growth), valued at 10%.
        v10 = (value(base,0,r=0.10)+value(base,g,r=0.10))/2
        fp = per_share(v10,ae)
        print(f'  range {name}: ${lo:.2f} to ${hi:.2f}  ratio {hi/lo:.2f}  mid ${mid:.2f}  fair price (mid stream at 10%) ${fp:.2f}')

print('\n== returns at the price')
def irr(c,g,price_total):
    lo,hi=0.0,0.5
    for _ in range(200):
        m=(lo+hi)/2
        if value(c,g,r=m)>price_total: lo=m
        else: hi=m
    return m
for ae in (True,False):
    base = sum(oc(y,True,ae) for y in yrs)/5
    gl=(oc(2025,False,ae)/oc(2021,False,ae))**0.25-1; gc=(oc(2025,False,ae)/oc(2019,False,ae))**(1/6)-1
    P = PRICE*SH + (ND if ae else 0)
    for name,g in (('no growth',0),('cycle',gc),('literal top',gl)):
        print('AE' if ae else 'EO', name, 'value at 10% per share', round(per_share(value(base,g,r=0.10),ae),2), ' return at price', round(irr(base,g,P)*100,2),'%')

print('\n== sensitivities (all-equity unless noted)')
ae=True
lo_base = sum(oc(y,True,ae) for y in yrs)/5
y7=[2019,2020]+yrs
base7 = sum(oc(y,True,ae) for y in y7)/7
gc=(oc(2025,False,ae)/oc(2019,False,ae))**(1/6)-1
lo=per_share(value(base7,0)); hi=per_share(value(base7,gc))
v10=(value(base7,0,r=.10)+value(base7,gc,r=.10))/2
print('cycle span 2019-2025: base',round(base7),'g',round(gc*100,1),'range',round(lo,2),round(hi,2),'ratio',round(hi/lo,2),'fair',round(per_share(v10),2))
# D&A basis
bd = sum(oc(y,True,ae,'dna') for y in yrs)/5
gd=(oc(2025,False,ae,'dna')/oc(2021,False,ae,'dna'))**.25-1
lo=per_share(value(bd,0)); hi=per_share(value(bd,gd)); v10=(value(bd,0,r=.10)+value(bd,gd,r=.10))/2
print('D&A basis literal: base',round(bd),'g',round(gd*100,1),'range',round(lo,2),round(hi,2),'ratio',round(hi/lo,2),'fair',round(per_share(v10),2))
# organic pair: acquisitions left out of base, growth less one point
bo = sum(oc(y,False,ae) for y in yrs)/5
go=(oc(2025,False,ae)/oc(2021,False,ae))**.25-1-0.01
lo=per_share(value(bo,0)); hi=per_share(value(bo,go)); v10=(value(bo,0,r=.10)+value(bo,go,r=.10))/2
print('organic pair: base',round(bo),'g',round(go*100,1),'range',round(lo,2),round(hi,2),'ratio',round(hi/lo,2),'fair',round(per_share(v10),2))
# growth needed for top case to earn 10% at the price
P=PRICE*SH+ND
lo_g,hi_g=0,0.6
for _ in range(100):
    m=(lo_g+hi_g)/2
    if value(lo_base,m,r=0.10)<P: lo_g=m
    else: hi_g=m
print('growth for ten years needed for the literal base to earn 10% at $589.14 (all-equity):',round(m*100,1),'%')
print('EV at price', round(P), 'market cap', round(PRICE*SH))
