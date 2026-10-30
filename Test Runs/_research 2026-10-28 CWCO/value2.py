# Q7 for CWCO run 2026-10-28, second pass: specific (c) acquisitions deducted, purchases stop after year ten;
# (d) working-capital beside; regulated-utility basis checked (no long-term debt raised: credit nil).
# USD millions. Inputs from value.py (filed cash-flow statements) plus the investing lines of the filed statements:
# 2019 PERC 51% net of cash 3.147, sale of discontinued ops (CW-Belize) +6.971; 2020 Aerex minority 8.5, PERC 10% 0.9;
# 2023 REC 3.420, PERC 39% cash 2.440 (+368,383 shares, already in the count). 10-Ks FY2020, FY2025.
exec(open('value.py').read().split('r=0.0530')[0].replace("print(","(lambda *a,**k:None)("))
acq={y:0.0 for y in yrs}; acq[2019]=3.147-6.971; acq[2020]=8.5+0.9; acq[2023]=3.420+2.440
wc={2023:-31.5,2024:11.1,2025:12.6}  # sums of the 'Change in' lines, filed statements (Q4)
r=0.0530; F=0.10
shares=16.012865; price=27.12; mcap=shares*price
cash=132.629006; debt=0.013110+0.002875; ncib=5.355211
netcash=cash-debt-ncib; ev=mcap-netcash
def pv(stream,rate):  # stream: list of 10 yearly cash, then terminal level (no growth)
    v=sum(c/(1+rate)**(t+1) for t,c in enumerate(stream[:10]))
    return v+stream[10]/rate/(1+rate)**10
def cases(Xb,A,g):
    # no-growth: owner cash before purchases, flat (a business that buys no growth spends nothing to buy it)
    ng=[Xb]*11
    # growth: purchases deducted for ten years (growing with the growth), then stop; terminal on before-purchase cash
    gr=[(Xb-A)*(1+g)**(t+1) for t in range(10)]+[Xb*(1+g)**10]
    return ng,gr
def irr(stream,target):
    lo,hi=0.0001,0.6
    for _ in range(200):
        m=(lo+hi)/2
        if pv(stream,m)>target: lo=m
        else: hi=m
    return m
C=[2019,2020,2021,2022,2023,2024,2025]; W=[2021,2022,2023,2024,2025]
def show(lab,ys,adj=None,g=0.0530,beside_ng_deduct=False):
    Xb=sum(oc[y]+(adj[y] if adj else 0) for y in ys)/len(ys); A=sum(acq[y] for y in ys)/len(ys)
    ng,gr=cases(Xb,A,g)
    if beside_ng_deduct: ng=[Xb-A]*11
    lo=(pv(ng,r)+netcash)/shares; hi=(pv(gr,r)+netcash)/shares
    if lo>hi: lo,hi=hi,lo
    f=((pv(ng,F)+netcash)/shares+(pv(gr,F)+netcash)/shares)/2
    print('%-44s Xb=%.2f A=%.2f range $%.2f-$%.2f (%.2f:1) | IRR at price: no-growth %.2f%%, growth %.2f%% | fair $%.2f'%(
        lab,Xb,A,lo,hi,hi/lo,100*irr(ng,ev),100*irr(gr,ev),f))
    return Xb,A
print('mcap %.2f net cash %.2f EV %.2f'%(mcap,netcash,ev))
show('CENTRAL cycle 2019-25, acq deducted (growth)',C)
show('beside: literal window 2021-25',W)
show('beside: cycle, acq deducted in no-growth too',C,beside_ng_deduct=True)
show('beside: cycle, D&A in place of capex',C,adj={y:ocd[y]-oc[y] for y in yrs})
show('beside: cycle less licence cut 1.9/yr',C,adj={y:-1.9 for y in yrs})
show('beside: cycle, 2023-25 WC changes at zero',C,adj={y:-wc.get(y,0) for y in yrs})
show('beside: 9 years 2017-25',yrs)
show('beside: growth uncapped at halves 14.8% (not defensible)',C,g=0.148)
# equity-only beside: owner cash after interest (interest income added; interest expense nil), against market cap, no cash added
Xb=sum(oc[y]+intin[y] for y in C)/len(C); A=sum(acq[y] for y in C)/len(C)
ng,gr=cases(Xb,A,0.053)
print('equity-only cycle: Xe=%.2f range $%.2f-$%.2f fair $%.2f; IRR at mcap no-growth %.2f%% growth %.2f%%'%(Xb,pv(ng,r)/shares,pv(gr,r)/shares,(pv(ng,F)+pv(gr,F))/2/shares,100*irr(ng,mcap),100*irr(gr,mcap)))
print('owner cash before purchases by year:',{y:round(oc[y],2) for y in yrs}); print('acq by year:',{y:round(acq[y],2) for y in yrs})
print('net purchases 2019-25 %.2f vs owner cash before purchases %.2f'%(sum(acq[y] for y in C),sum(oc[y] for y in C)))
h1=sum(oc[y]-acq[y] for y in [2019,2020,2021])/3; h2=sum(oc[y]-acq[y] for y in [2023,2024,2025])/3
print('halves after purchases %.2f -> %.2f, %.1f%%/yr'%(h1,h2,100*((h2/h1)**0.25-1)))
print('share of sales max %.1f%%'%max(100*oc[y]/rev[y] for y in yrs))
print('bottom of range per share (for Q6) printed above as CENTRAL lo')
