# COMPUTATION - NOT A CLEARANCE. Figures USD millions from the filed statements (XBRL first-filed vintage, checked to the FY2025 10-K for 2023-2025).
d={ # year: OCF, SBC, capex, D&A, acquisitions, NI, EBIT, buybacks
2010:(98.2,7.0,18.0,38.0,5.1,75.5,124.1,0),
2011:(115.7,7.9,27.1,39.1,13.8,100.2,147.4,50.0),
2012:(67.4,8.5,30.2,41.2,3.8,92.8,148.2,0),
2013:(76.1,6.4,19.0,41.5,0,71.0,121.2,57.8),
2014:(110.3,7.8,10.0,40.6,0,75.7,131.0,50.4),
2015:(180.5,8.9,13.4,38.0,44.2,75.9,126.5,91.8),
2016:(96.1,11.1,12.3,38.1,10.8,84.7,148.8,50.0),
2017:(-307.1,12.8,19.2,42.6,186.9,90.7,179.3,0),
2018:(292.6,15.4,17.3,37.5,74.9,163.7,233.5,22.1),
2019:(127.9,16.0,69.1,46.2,664.3,159.4,240.6,27.9),
2020:(355.6,17.7,24.2,65.6,6.4,172.6,271.6,25.0),
2021:(163.7,18.2,52.1,55.4,0,219.3,332.1,50.0),
2022:(98.1,22.7,70.9,56.6,68.2,280.6,413.7,107.9),
2023:(619.5,29.0,39.3,62.5,481.5,281.3,419.8,217.1),
2024:(632.8,34.0,46.8,98.1,270.2,249.7,388.6,200.0),
2025:(303.8,33.7,24.5,106.3,285.3,157.3,334.9,151.1)}
oe_c={y:v[0]-v[1]-v[2] for y,v in d.items()}
oe_d={y:v[0]-v[1]-v[3] for y,v in d.items()}
for y in d: print(y, 'OEcapex %.1f  OE_DA %.1f  NI %.1f  OCF/NI %.2f'%(oe_c[y],oe_d[y],d[y][5],d[y][0]/d[y][5]))
avg=lambda s,ys: sum(s[y] for y in ys)/len(ys)
w5=range(2021,2026); w10=range(2016,2026); w16=range(2010,2026)
for nm,w in [('5y',w5),('10y',w10),('16y',w16)]:
    print(nm,'OEc %.1f OEd %.1f NI %.1f acq/yr %.1f buyback/yr %.1f EBIT %.1f'%(avg(oe_c,w),avg(oe_d,w),avg({y:d[y][5] for y in d},w),avg({y:d[y][4] for y in d},w),avg({y:d[y][7] for y in d},w),avg({y:d[y][6] for y in d},w)))
    print('   sums: OEc %.1f acq %.1f buyback %.1f'%(sum(oe_c[y] for y in w),sum(d[y][4] for y in w),sum(d[y][7] for y in w)))
r=0.0566; sh=29.348850
def dcf(b,g,r=r,n=10):
    pv=0;c=b
    for t in range(1,n+1):
        c*=1+g; pv+=c/(1+r)**t
    return pv + c/r/(1+r)**n
cagr=lambda a,b,n:(b/a)**(1/n)-1
print('EBIT cagr 2021-25 %.4f ; 2015-25 %.4f ; 2016-25 %.4f'%(cagr(332.1,334.9,4),cagr(126.5,334.9,10),cagr(148.8,334.9,9)))
g5=cagr(332.1,334.9,4)
for nm,b,g in [('5y DA no-growth',avg(oe_d,w5),0),('5y capex no-growth',avg(oe_c,w5),0),('5y capex shown g',avg(oe_c,w5),g5),('5y DA shown g',avg(oe_d,w5),g5),
               ('10y DA no-growth',avg(oe_d,w10),0),('10y capex no-growth',avg(oe_c,w10),0),
               ('10y capex at EBIT cagr 2016-25 free (ceiling, acquisitions not deducted)',avg(oe_c,w10),cagr(148.8,334.9,9))]:
    v=dcf(b,g); print('%-75s base %.1f g %.4f value %.0f  per share %.2f'%(nm,b,g,v,v/sh))
# fair and cheap
t=0.25
for nm,b in [('5y capex',avg(oe_c,w5)),('10y capex',avg(oe_c,w10)),('central midpoint',(avg(oe_c,w5)+avg(oe_c,w10))/2),('10y DA',avg(oe_d,w10))]:
    print('%-20s base %.1f  pretax %.1f  equity value at 10%% pretax %.0f  per share %.2f   at 20%%: %.2f'%(nm,b,b/(1-t),b/(1-t)/0.10,b/(1-t)/0.10/sh,b/(1-t)/0.20/sh))
ebit5=avg({y:d[y][6] for y in d},w5); nd=1475.089-363.482
print('EV basis: 5y EBIT %.1f -> EV at 10%% %.0f - net debt %.1f = %.0f -> per share %.2f'%(ebit5,ebit5/0.10,nd,ebit5/0.10-nd,(ebit5/0.10-nd)/sh))
ebit10=avg({y:d[y][6] for y in d},w10)
print('EV basis: 10y EBIT %.1f -> per share %.2f'%(ebit10,(ebit10/0.10-nd)/sh))
p=159.39; mc=p*sh; print('mcap %.0f  EV %.0f  pretax yield on 5y OEc %.2f%%  10y %.2f%%  EBIT5/EV %.2f%%'%(mc,mc+nd,avg(oe_c,w5)/(1-t)/mc*100,avg(oe_c,w10)/(1-t)/mc*100,ebit5/(mc+nd)*100))
print('decade owner cash vs acquisitions+earnout+warrant: OEc10 %.1f  acq %.1f'%(sum(oe_c[y] for y in w10),sum(d[y][4] for y in w10)))
print('incremental EBIT 2016->2025 %.1f over acquisitions %.1f = %.1f%% pre-tax'%(334.9-148.8,sum(d[y][4] for y in range(2017,2026)),100*(334.9-148.8)/sum(d[y][4] for y in range(2017,2026))))
