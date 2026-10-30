# Q7 arithmetic for CWCO run 2026-10-28. USD millions. Sources: filed cash-flow statements (accessions in run file).
yrs=[2017,2018,2019,2020,2021,2022,2023,2024,2025]
ocf_c={2017:13.294,2018:7.990,2019:17.419,2020:18.971,2021:8.588,2022:23.152,2023:9.114,2024:38.172,2025:42.209}
sbc  ={2017:0.804,2018:0.850,2019:1.192,2020:1.163,2021:0.977,2022:1.417,2023:1.934,2024:1.398,2025:1.771} # 2025 incl 0.069 stock for services
capex={2017:4.550,2018:16.203,2019:3.525,2020:1.728,2021:1.490,2022:7.543,2023:5.048,2024:6.697,2025:8.541}
nci  ={2017:0,2018:0,2019:0,2020:0,2021:0.011,2022:1.102,2023:0,2024:0.232,2025:0.913}
intin={2017:0.381,2018:0.663,2019:0.589,2020:0.540,2021:0.685,2022:0.447,2023:0.696,2024:2.094,2025:2.670}
da   ={2017:7.290,2018:7.034,2019:7.203,2020:7.407,2021:6.921,2022:6.187,2023:6.576,2024:6.692,2025:6.903}
rev  ={2017:59.37,2018:65.72,2019:68.79,2020:72.63,2021:66.86,2022:94.10,2023:180.21,2024:133.97,2025:132.07}
oc={y:ocf_c[y]-sbc[y]-capex[y]-nci[y]-intin[y] for y in yrs}
ocd={y:ocf_c[y]-sbc[y]-da[y]-nci[y]-intin[y] for y in yrs}
for y in yrs: print(y,'owner cash (all spending, before interest) %.2f  D&A variant %.2f  share of sales %.1f%%'%(oc[y],ocd[y],100*oc[y]/rev[y]))
avg=lambda d,ys: sum(d[y] for y in ys)/len(ys)
W=[2021,2022,2023,2024,2025]; C=[2019,2020,2021,2022,2023,2024,2025]
print('literal 5y avg %.2f  D&A var %.2f'%(avg(oc,W),avg(ocd,W)))
print('cycle 2019-2025 avg %.2f  D&A var %.2f'%(avg(oc,C),avg(ocd,C)))
print('9y 2017-2025 avg %.2f'%avg(oc,yrs))
print('interest income avg 2019-2025 %.3f; 2021-25 %.3f'%(avg(intin,C),avg(intin,W)))
h1=avg(oc,[2019,2020,2021]);h2=avg(oc,[2023,2024,2025]);print('halves %.2f -> %.2f growth %.1f%%'%(h1,h2,100*((h2/h1)**(1/4)-1)))
print('sales growth 2019->2025 %.1f%%; halves %.1f%%'%(100*((rev[2025]/rev[2019])**(1/6)-1),100*((avg(rev,[2023,2024,2025])/avg(rev,[2019,2020,2021]))**(1/4)-1)))
r=0.0530; g=0.0530
def val(X,g,r,n=10):
    pv=sum(X*(1+g)**t/(1+r)**t for t in range(1,n+1))
    return pv+X*(1+g)**n/r/(1+r)**n
def irr(X,g,ev):
    lo,hi=0.0001,0.5
    for _ in range(200):
        m=(lo+hi)/2
        if val(X,g,m)>ev: lo=m
        else: hi=m
    return m
shares=16.012865; price=27.12; mcap=shares*price
cash=132.629006; debt=0.013110+0.002875; ncib=5.355211
netcash=cash-debt-ncib
ev=mcap-netcash
print('mcap %.2f netcash(after NCI book) %.2f EV %.2f'%(mcap,netcash,ev))
for lab,X in (('cycle',avg(oc,C)),('literal',avg(oc,W)),('cycle D&A',avg(ocd,C)),('cycle less licence cut 1.9',avg(oc,C)-1.9)):
    lo=val(X,0,r); hi=val(X,g,r)
    plo=(lo+netcash)/shares; phi=(hi+netcash)/shares
    f0=val(X,0,0.10); f1=val(X,g,0.10)
    fair=((f0+netcash)/shares+(f1+netcash)/shares)/2
    print('%-28s X=%.2f range $%.2f-$%.2f (width %.2f:1) | at price: no-growth yield %.2f%%, growth-case IRR %.2f%% | fair $%.2f (ends $%.2f, $%.2f)'%(lab,X,plo,phi,phi/plo,100*X/ev,100*irr(X,g,ev),fair,(f0+netcash)/shares,(f1+netcash)/shares))
# equity-only beside: owner cash after interest (interest income added; interest expense ~0) against market value, no net cash added
for lab,X,I in (('cycle',avg(oc,C),avg(intin,C)),('literal',avg(oc,W),avg(intin,W))):
    Xe=X+I
    f0=val(Xe,0,0.10); f1=val(Xe,g,0.10)
    print('equity-only %s Xe=%.2f range $%.2f-$%.2f fair $%.2f; yield at mcap %.2f%%, growth IRR %.2f%%'%(lab,Xe,val(Xe,0,r)/shares,val(Xe,g,r)/shares,(f0+f1)/2/shares,100*Xe/mcap,100*irr(Xe,g,mcap)))
