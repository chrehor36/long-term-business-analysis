# HY run 2026-10-13: Q7 arithmetic (COMPUTATION, NOT A CLEARANCE). Inputs transcribed from the 10-K cash-flow
# statements (XBRL companyfacts, cross-checked: FY2025 OCF 86.1 on the filed statement, acc 0001173514-26-000049).
yrs=list(range(2016,2026))
ocf=dict(zip(yrs,[-48.9,164.7,67.6,76.7,166.9,-253.5,40.6,150.7,170.7,86.1]))
sbc=dict(zip(yrs,[4.9,8.8,5.7,8.2,1.3,4.0,6.4,29.3,23.6,7.5]))
capex=dict(zip(yrs,[42.7,41.0,38.8,49.7,51.7,44.3,28.8,35.4,47.8,62.5]))
da=dict(zip(yrs,[39.1,42.8,44.0,43.3,42.9,46.2,43.4,45.1,47.6,45.8]))
acq=dict(zip(yrs,[116.1,1.0,78.0,0,0,0,8.4,3.2,2.2,2.6]))   # 2023 = purchase of noncontrolling interest
intr=dict(zip(yrs,[6.7,14.6,16.0,19.8,13.7,15.5,28.4,37.3,33.8,31.2]))
rev=dict(zip(yrs,[2569.7,2885.2,3174.4,3291.8,2812.1,3075.7,3548.3,4118.3,4308.2,3769.3]))
opi=dict(zip(yrs,[34.9,76.0,38.8,53.9,49.9,-152.3,-39.1,208.7,244.8,-22.1]))
T=0.21  # CONVENTION of this run: US statutory rate for the interest shield
R=0.056; F=0.10
shares=17.930387; price=31.93; netdebt=500.0-72.6
def avg(f,ys): return sum(f(y) for y in ys)/len(ys)
def cases(ys,label):
    org_capex=avg(lambda y: ocf[y]-sbc[y]-capex[y],ys)
    org_da=avg(lambda y: ocf[y]-sbc[y]-da[y],ys)
    dflt=avg(lambda y: ocf[y]-sbc[y]-capex[y]-acq[y],ys)
    shield=avg(lambda y: intr[y]*(1-T),ys)
    netacq=sum(acq[y] for y in ys); before=sum(ocf[y]-sbc[y]-capex[y] for y in ys)
    print(f'--- {label} {ys[0]}-{ys[-1]}: net purchases {netacq:.1f} vs owner cash before purchases {before:.1f}')
    for name,eq in [('organic, all spending',org_capex),('organic, maintenance=D&A',org_da),('default, purchases deducted',dflt)]:
        ae=eq+shield
        print(f'{name:30s} equity-only {eq:7.1f}/yr  all-equity {ae:7.1f}/yr | at 5.6%: EV {ae/R:7.0f} -> {(ae/R-netdebt)/shares:7.2f}/sh ; equity {eq/R:6.0f} -> {eq/R/shares:6.2f}/sh | at 10%: AE {(ae/F-netdebt)/shares:7.2f}/sh ; EQ {eq/F/shares:6.2f}/sh')
cases(yrs,'cycle base'); cases(yrs[5:],'literal window')
h1=[2016,2017,2018,2019,2020]; h2=yrs[5:]
for f,n in [(lambda y: ocf[y]-sbc[y]-capex[y],'organic'),(lambda y: ocf[y]-sbc[y]-capex[y]-acq[y],'default')]:
    print('halves',n, round(avg(f,h1),1), round(avg(f,h2),1))
print('op margin 2016-25', round(sum(opi.values())/sum(rev.values())*100,2),'%; mean op profit',round(sum(opi.values())/10,1))
print('market cap', round(shares*price,1), 'EV', round(shares*price+netdebt,1), 'net debt', netdebt)
print('owner-cash yield on EV (central, organic all spending, cycle base):', round((avg(lambda y: ocf[y]-sbc[y]-capex[y],yrs)+avg(lambda y: intr[y]*(1-T),yrs))/(shares*price+netdebt)*100,2),'%')
