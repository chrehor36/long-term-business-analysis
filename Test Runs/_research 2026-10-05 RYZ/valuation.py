# COMPUTATION - NOT A CLEARANCE (the file closes at Q2). Arithmetic for the owner's three reported prices.
from ryz_table import R
r=0.0563; shares=51.898653; price=27.15; netdebt=913.0; t=0.25  # tax CONVENTION 25% (21% federal + state), stated in run
Z={ # Olympic Steel (ZEUS) from its own 10-K XBRL: op, ocf, capex, dda, sbc
2009:(-97.3,57.3,11.9,12.2,-1.1),2010:(6.1,-38.8,17.8,13.9,0.6),2011:(44.5,15.8,39.5,16.7,0.8),2012:(18.4,27.4,23.4,22.2,2.0),
2013:(19.7,54.7,16.1,23.6,1.7),2014:(-9.2,-39.6,7.8,21.8,2.1),2015:(-27.8,107.5,7.3,19.9,1.8),2016:(5.7,-9.8,6.8,19.4,0.5),
2017:(24.0,-19.0,10.2,18.6,1.1),2018:(57.1,-50.5,25.7,18.0,1.5),2019:(16.6,129.6,10.2,19.5,2.2),2020:(0.6,61.7,9.8,20.0,1.2),
2021:(172.5,-146.4,11.0,21.0,1.0),2022:(133.7,185.9,19.9,20.2,1.3),2023:(77.7,175.2,21.3,27.2,1.8),2024:(47.9,33.7,29.5,30.9,2.0)}
def ryz_eq(y): s,gp,op,tn,l,ocf,cx,da,sbc,d,e,acq=R[y]; return ocf-cx-(sbc or 0)
def ryz_un(y): s,gp,op,tn,l,ocf,cx,da,sbc,d,e,acq=R[y]; return op*(1-t)+da-cx-(sbc or 0)
def z_eq(y): op,ocf,cx,da,sbc=Z[y]; return ocf-cx-max(sbc,0)
def z_un(y): op,ocf,cx,da,sbc=Z[y]; return op*(1-t)+da-cx-max(sbc,0)
print('RYZ equity owner cash by year', {y:round(ryz_eq(y),1) for y in range(2016,2026)})
print('ZEUS equity owner cash by year', {y:round(z_eq(y),1) for y in range(2020,2025)})
C5=sum(ryz_eq(y) for y in range(2021,2026))/5 + sum(z_eq(y) for y in range(2020,2025))/5
print('Convention C5 (RYZ 2021-25 + ZEUS 2020-24):', round(C5,1), ' RYZ part', round(sum(ryz_eq(y) for y in range(2021,2026))/5,1),' ZEUS part', round(sum(z_eq(y) for y in range(2020,2025))/5,1))
def pv(C,g,years=10):
    v=0; c=C
    for k in range(1,years+1):
        c=c*(1+g); v+=c/(1+r)**k
    v+= c/r/(1+r)**years  # then zero nominal growth
    return v
g_tons=(1947/2095)**(1/4)-1
print('shown growth (tons 2021->2025 CAGR):', round(g_tons*100,2),'%')
top=pv(C5,0); bot=pv(C5,g_tons)
print('Convention range equity $M: bottom',round(bot),' top',round(top),' per share',round(bot/shares,2),'-',round(top/shares,2),' width',round(top/bot,2))
print('yield on price of C5:', round(C5/(price*shares)*100,2),'%')
# full cycle unlevered
UR=sum(ryz_un(y) for y in range(2009,2026))/17; UZ=sum(z_un(y) for y in range(2009,2025))/16
print('full-cycle unlevered RYZ 2009-25',round(UR,1),' ZEUS 2009-24',round(UZ,1),' combined',round(UR+UZ,1))
interest_at=57.2*(1-t)  # Q2 2026 interest 14.3 annualized x4, after tax
Ceq=UR+UZ-interest_at
print('central equity owner cash (full cycle, less after-tax interest on today debt):',round(Ceq,1))
print('central no-growth value $M',round(Ceq/r),' per share',round(Ceq/r/shares,2))
fair=Ceq/0.10; print('FAIR price (10% pre-tax, zero growth):',round(fair),'$M ->',round(fair/shares,2),'/sh')
print('expected pre-tax return at price on central case:', round(Ceq/(price*shares)*100,2),'%')
# rolling 5-yr minimum of combined unlevered owner cash (2009-2024 common years)
rolls={}
for y0 in range(2009,2021):
    ys=range(y0,y0+5); rolls[y0]=sum(ryz_un(y)+z_un(y) for y in ys)/5
w=min(rolls,key=rolls.get); print('rolling 5yr combined unlevered:',{k:round(v,1) for k,v in rolls.items()}); print('worst window',w,'-',w+4, round(rolls[w],1))
Cw=rolls[w]-interest_at; cheap=Cw/0.10
print('worst-window equity cash',round(Cw,1),' CHEAP price (worst window yields 10%):',round(cheap),'$M ->',round(cheap/shares,2),'/sh')
print('after-tax equivalent of 10% pre-tax at 23.8% investor tax:', round(10*(1-0.238),2),'%')
