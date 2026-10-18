# MAGN owner cash and Q7 computation (COMPUTATION, NOT A CLEARANCE). USD millions.
# Treasure (HHNF carve-out) fiscal years end ~Sep 30; Glatfelter (GLT) twelve months to Sep 30 from 10-K less 9M prior plus 9M current (XBRL, CIK 41719).
T = {  # OCF, SBC, capex(+other investing), depreciation, tax gap (current tax expense less cash taxes paid, deducted only where positive)
 2021:dict(ocf=380,sbc=6,capex=131+10,dep=111,taxgap=76-66),
 2022:dict(ocf=324,sbc=7,capex=104,dep=115,taxgap=0),
 2023:dict(ocf=257,sbc=7,capex=88,dep=118,taxgap=43-29),
 2024:dict(ocf=192,sbc=7,capex=72,dep=127,taxgap=28-9),
}
G = {  # GLT TTM to Sep: OCF, interest paid, SBC, capex, D&A, acquisitions
 2021:dict(ocf=123.0,int=6.2,sbc=5.7,capex=26.5,da=57.5,acq=172.3),
 2022:dict(ocf=-31.9,int=20.1,sbc=1.1,capex=41.6,da=67.7,acq=291.1),
 2023:dict(ocf=-18.4,int=52.3,sbc=3.0,capex=32.9,da=63.6,acq=0.0),
 2024:dict(ocf=7.9,int=66.6,sbc=3.1,capex=30.2,da=63.0,acq=0.0),
}
M2025=dict(ocf=103,int=124,sbc=19,capex=67,dep=156)
sales={2021:2827+985.5,2022:2803+1451.9,2023:2275+1439.0,2024:2187+1309.2,2025:3316}
oc={};ocd={};acq={}
for y in range(2021,2025):
    t=T[y];g=G[y]
    oc[y]=t['ocf']-t['sbc']-t['capex']-t['taxgap'] + g['ocf']+g['int']-g['sbc']-g['capex']
    ocd[y]=t['ocf']-t['sbc']-t['dep']-t['taxgap'] + g['ocf']+g['int']-g['sbc']-g['da']
    acq[y]=g['acq']
m=M2025
oc[2025]=m['ocf']+m['int']-m['sbc']-m['capex']; ocd[2025]=m['ocf']+m['int']-m['sbc']-m['dep']; acq[2025]=0
yrs=range(2021,2026)
print('year  ownercash(all capex)  dep-variant  acquisitions  net-of-acq  sales')
for y in yrs: print(y, round(oc[y],1), round(ocd[y],1), acq[y], round(oc[y]-acq[y],1), round(sales[y],1))
avg=lambda d,ys: sum(d[y] for y in ys)/len(ys)
lit=list(yrs); cyc=list(range(2022,2026))
print('avg literal',round(avg(oc,lit),1),' avg ex-FY2021',round(avg(oc,cyc),1))
print('dep variant avg literal',round(avg(ocd,lit),1),' ex-FY2021',round(avg(ocd,cyc),1))
net={y:oc[y]-acq[y] for y in yrs}
print('net-of-acq avg literal',round(avg(net,lit),1),' ex-FY2021',round(avg(net,cyc),1))
print('purchases',sum(acq.values()),' half of owner cash before purchases',round(sum(oc.values())/2,1))
sg=(sales[2025]/sales[2021])**(1/4)-1; print('sales growth FY21-25',round(sg*100,2),'%')
og=(0.97*0.92*0.99*0.98)**(1/4)-1; print('organic volume growth FY22-25 per filer',round(og*100,2),'%')
print('owner cash growth literal end years',round(((oc[2025]/oc[2021])**0.25-1)*100,2),'%  ex-FY2021',round(((oc[2025]/oc[2022])**(1/3)-1)*100,2),'%')
# valuation
r=0.0543; shares=35.8; price=11.05; netdebt=1901-280; netdebt_face=706+500+760-280
mv=shares*price; ev=mv+netdebt
def pv(base,g,rate):
    v=0;cf=base
    for t in range(1,11):
        cf=cf*(1+g); v+=cf/(1+rate)**t
    v+= (cf/rate)/(1+rate)**10
    return v
print('market value',round(mv,1),' net debt',netdebt,' EV',round(ev,1))
cases={}
for name,base,g in [('central organic, base ex-FY2021',avg(oc,cyc),og),('organic, literal base',avg(oc,lit),og),
                    ('default pair, base ex-FY2021',avg(net,cyc),sg),('default pair, literal',avg(net,lit),sg),
                    ('dep variant ex-FY2021',avg(ocd,cyc),og),('dep variant literal',avg(ocd,lit),og)]:
    top=pv(base,0,r); bot=pv(base,g,r)
    t10=pv(base,0,0.10); b10=pv(base,g,0.10)
    fair=((t10+b10)/2-netdebt)/shares
    print(f"{name}: base {base:.1f} g {g*100:.2f}%  range EV {bot:.0f}-{top:.0f}  per share {(bot-netdebt)/shares:.2f} to {(top-netdebt)/shares:.2f}  width {top/bot if bot>0 else float('nan'):.2f}x  yield at EV no-growth {base/ev*100:.2f}%  fair(all-equity) {fair:.2f}")
# equity-only: owner cash after today's cash interest (TTM est 128) against market value
cash_int=128
for name,base,g in [('central organic ex-FY2021',avg(oc,cyc),og),('organic literal',avg(oc,lit),og)]:
    b=base-cash_int
    t10=pv(b,0,0.10); b10=pv(b,g,0.10)
    print(f"equity-only {name}: base after interest {b:.1f}; range per share {pv(b,g,r)/shares:.2f} to {pv(b,0,r)/shares:.2f}; fair {((t10+b10)/2)/shares:.2f}; yield on mkt value {b/mv*100:.2f}%")
# TTM to 2026-06-27
ocf=103-7+76; capex=67-52+44; sbc=19-15+13; intexp=141-102+112; noncash=17-12+18
ttm=ocf+(intexp-noncash)-sbc-capex
print('TTM: OCF',ocf,'capex',capex,'SBC',sbc,'cash interest est',intexp-noncash,'owner cash before interest',ttm,' yield on EV',round(ttm/ev*100,2),'%')
# Beside: the TTM figure as a base (not the convention's input; shown only)
for g in (0,og):
    top=pv(ttm,g,r); t10=pv(ttm,g,0.10)
    print(f"TTM base {ttm} g {g*100:.2f}%: value per share at sovereign {(top-netdebt)/shares:.2f}; at 10% {(t10-netdebt)/shares:.2f}")
t10=pv(ttm,0,0.10); b10=pv(ttm,og,0.10); print('TTM fair (avg of ends at 10%)',round(((t10+b10)/2-netdebt)/shares,2))
# face-value net debt beside
c=avg(oc,cyc); t10=pv(c,0,0.10); b10=pv(c,og,0.10)
print('central fair with face-value debt',round(((t10+b10)/2-netdebt_face)/shares,2),' range',round((pv(c,og,r)-netdebt_face)/shares,2),round((pv(c,0,r)-netdebt_face)/shares,2))
# owner cash needed for the central fair price to equal the price: solve no-growth at 10%
need=(mv+netdebt)*0.10; print('owner cash before interest needed for 10% on EV at no growth',round(need,1))
