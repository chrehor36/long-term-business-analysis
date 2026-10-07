# COMPUTATION - NOT A CLEARANCE. Arithmetic for the PRKS run of 2026-10-05.
r=0.0566; sh=45.341309; price=34.45
ocf={2011:268.2,2012:303.5,2013:289.8,2014:261.5,2015:286.3,2016:280.4,2017:192.5,2018:293.9,2019:348.4,2020:-120.7,2021:503.0,2022:564.6,2023:504.9,2024:480.1,2025:380.1}
sbc={2011:0.8,2012:1.2,2013:6.0,2014:2.3,2015:6.5,2016:37.5,2017:23.2,2018:22.2,2019:11.1,2020:7.5,2021:39.7,2022:18.2,2023:17.0,2024:13.7,2025:17.2}
capex={2011:225.3,2012:191.7,2013:166.3,2014:154.6,2015:157.3,2016:160.5,2017:172.5,2018:179.8,2019:195.2,2020:109.2,2021:128.9,2022:200.7,2023:304.8,2024:248.4,2025:217.5}
da={2011:213.6,2012:167.0,2013:166.1,2014:176.3,2015:182.5,2016:199.6,2017:163.3,2018:161.0,2019:160.6,2020:150.5,2021:148.7,2022:152.6,2023:154.2,2024:163.4,2025:174.5}
core={2018:177.2,2019:171.8,2020:94.7,2021:69.4,2022:131.9,2023:226.2,2024:177.7,2025:182.4}
intx={2011:110.1,2012:111.4,2013:93.5,2014:81.5,2015:65.6,2016:62.7,2017:78.0,2018:80.9,2019:84.2,2020:100.9,2021:116.6,2022:117.5,2023:146.7,2024:167.8,2025:134.1}
dtax={2021:-4.1,2022:95.5,2023:72.6,2024:50.7,2025:49.1}
oe={y:ocf[y]-sbc[y]-capex[y] for y in ocf}
oed={y:ocf[y]-sbc[y]-da[y] for y in ocf}
oec={y:ocf[y]-sbc[y]-core[y] for y in core}
for y in sorted(oe): print(y, 'OE capex %.1f'%oe[y], 'OE D&A %.1f'%oed[y], ('OE core %.1f'%oec[y]) if y in oec else '')
avg=lambda d,ys: sum(d[y] for y in ys)/len(ys)
y5=range(2021,2026); y3=range(2023,2026); yall=range(2011,2026)
b5=avg(oe,y5); b3=avg(oe,y3); ball=avg(oe,yall); bx20=avg(oe,[y for y in yall if y!=2020])
print('5yr %.1f  3yr %.1f  15yr %.1f  15yr ex2020 %.1f  5yr D&A %.1f  3yr core %.1f'%(b5,b3,ball,bx20,avg(oed,y5),avg(oec,y3)))
print('5yr deferred tax avg %.1f ; 3yr %.1f'%(avg(dtax,y5),avg(dtax,y3)))
ltm=410.0-19.3-245.2; print('LTM OE %.1f'%ltm)
g=(oe[2025]/oe[2021])**(1/4)-1; print('shown growth 2021->2025 CAGR %.4f'%g)
def pv(base,g,r=r,n=10):
    v=0; c=base
    for t in range(1,n+1):
        c=c*(1+g); v+=c/(1+r)**t
    return v + (c/r)/(1+r)**n
hi=pv(b5,0.0); lo=pv(b5,g)
print('CONVENTION range on 5yr: no-growth %.0f ($%.2f)  shown-growth %.0f ($%.2f)  ratio %.2f'%(hi,hi/sh,lo,lo/sh,hi/lo))
for nm,b in [('3yr',b3),('LTM',ltm),('15yr',ball)]:
    print(nm,'no-growth equity %.0f  $%.2f/sh'%(pv(b,0),pv(b,0)/sh))
# whole-cycle enterprise basis: unlevered = OE + interest*(1-0.25)
un={y:oe[y]+intx[y]*0.75 for y in oe}
uall=avg(un,yall); netdebt=2290.3-19.1
print('unlevered 15yr avg %.1f ; 5yr %.1f'%(uall,avg(un,y5)))
ev=uall/r; print('whole-cycle EV no-growth %.0f  less net debt %.0f -> equity %.0f $%.2f'%(ev,netdebt,ev-netdebt,(ev-netdebt)/sh))
# whole-cycle equity at today's interest (LTM interest 130.2)
wc_eq=uall-130.2*0.75; print('whole-cycle OE at today interest %.1f'%wc_eq)
mc=price*sh; print('mcap %.0f'%mc)
for nm,b in [('5yr',b5),('3yr',b3),('LTM',ltm),('15yr',ball),('wc at today int',wc_eq),('3yr full tax',b3-avg(dtax,y3))]:
    print('%s yield at price %.2f%%  fair@10%% $%.2f'%(nm,100*b/mc,b/0.10/sh))
