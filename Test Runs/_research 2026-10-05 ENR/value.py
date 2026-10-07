# ENR arithmetic for the run file. COMPUTATION, NOT A CLEARANCE. Inputs from filings (USD millions).
OCF={2016:193.9,2017:197.2,2018:228.7,2019:149.5,2020:376.4,2021:179.7,2022:1.0,2023:395.2,2024:429.6,2025:147.1}
SBC={2016:20.4,2017:24.3,2018:28.2,2019:27.1,2020:24.5,2021:10.2,2022:13.2,2023:21.8,2024:23.1,2025:25.6}
CAPEX={2016:28.7,2017:25.2,2018:24.2,2019:55.1,2020:65.3,2021:64.9,2022:77.8,2023:56.8,2024:97.9,2025:83.9}
DA={2016:34.3,2017:50.2,2018:45.1,2019:92.8,2020:111.9,2021:118.5,2022:121.6,2023:122.7,2024:120.5,2025:126.7}
oe={y:OCF[y]-SBC[y]-CAPEX[y] for y in OCF}; oed={y:OCF[y]-SBC[y]-DA[y] for y in OCF}
for y in OCF: print(y, round(oe[y],1), round(oed[y],1))
m=lambda d,ys: sum(d[y] for y in ys)/len(ys)
A5=m(oe,range(2021,2026)); A5p=m(oe,range(2016,2021)); A10=m(oe,range(2016,2026)); A3=m(oe,range(2023,2026)); A5d=m(oed,range(2021,2026))
print('5yr',round(A5,1),'prior5',round(A5p,1),'10yr',round(A10,1),'3yr',round(A3,1),'5yr DA',round(A5d,1))
g=(A5/A5p)**(1/5)-1; print('shown growth across windows',round(g*100,2))
ttm=(147.1-85.6+156.0)-(25.6-19.7+20.4)-(83.9-69.1+52.1); print('TTM',round(ttm,1))
r=0.0563; sh=68.483637; price=21.24
def val(c,gr,yrs=10):
    pv=0;cf=c
    for t in range(1,yrs+1):
        cf*=1+gr; pv+=cf/(1+r)**t
    pv+=cf/r/(1+r)**yrs   # zero nominal growth after year ten
    return pv
for name,c in [('5yr',A5),('10yr whole-cycle',A10),('3yr',A3),('TTM',ttm),('5yr+45X earned in window',A5+120.9/5)]:
    lo=val(c,g); hi=val(c,0.0)
    print(f'{name:28s} C={c:6.1f} shown-growth {lo:7.0f} (${lo/sh:5.2f})  no-growth {hi:7.0f} (${hi/sh:5.2f})  ratio {hi/lo:4.2f}')
# refinancing variant: 2028/2029 notes 583.7@4.75, 791.3@4.375, 742.2@3.50 refinanced at 6.00 (Sep 2025 notes)
notes=[(583.7,4.75),(791.3,4.375),(742.2,3.50)]; tot=sum(a for a,_ in notes); wavg=sum(a*c for a,c in notes)/tot
inc=tot*(6.00-wavg)/100; t=(0.159+0.292+0.200)/3
print('notes',round(tot,1),'wavg',round(wavg,3),'extra interest pre-tax',round(inc,1),'after tax',round(inc*(1-t),1),'avg ETR',round(t,4))
Cref=A5-inc*(1-t); print('5yr after refinancing',round(Cref,1), 'no-growth $',round(val(Cref,0)/sh,2),'shown $',round(val(Cref,g)/sh,2))
# fair price: price at which the central case clears 10% pre-tax. central = mean of the two ends' cash paths
import math
def irr_price(c,gr,target,tax):
    # price P such that pre-tax IRR = target: discount pre-tax cash (c/(1-tax)) at target
    pre=c/(1-tax); pv=0;cf=pre
    for k in range(1,11):
        cf*=1+gr; pv+=cf/(1+target)**k
    pv+=cf/target/(1+target)**10
    return pv
for name,c in [('5yr',A5),('10yr',A10)]:
    p0=irr_price(c,0,0.10,t); pg=irr_price(c,g,0.10,t)
    print(name,'fair (10% pre-tax) no-growth $',round(p0/sh,2),' shown-growth $',round(pg/sh,2),' central $',round((p0+pg)/2/sh,2))
print('mktcap',round(price*sh,1))
# expected pre-tax return at today's price, central case 5yr, no growth
print('pre-tax yield at price, 5yr no-growth', round(A5/(1-t)/(price*sh)*100,2))
p0=irr_price(Cref,0,0.10,t); pg=irr_price(Cref,g,0.10,t)
print('refi fair no-growth $',round(p0/sh,2),'shown $',round(pg/sh,2),'central $',round((p0+pg)/2/sh,2))
print('cheap = half bottom: base $',round(val(A5,g)/sh/2,2),' refi $',round(val(Cref,g)/sh/2,2),' whole-cycle $',round(val(A10,g)/sh/2,2))
# net debt and coverage
print('net debt Jun26', round(3327.3+30.5-173.4,1), 'EV at price', round(price*sh+3327.3+30.5-173.4,1))
