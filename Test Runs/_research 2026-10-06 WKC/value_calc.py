# COMPUTATION - NOT A CLEARANCE. All inputs USD millions from the filed cash-flow statements (accessions in the run file).
yrs=list(range(2010,2026))
ocf={2010:-35.7,2011:-142.5,2012:145.8,2013:264.3,2014:141.2,2015:447.5,
     2016:50.7+154.5,2017:-133.6+338.8,2018:-182.5+369.8,  # 2016-2018: OCF as restated + DPP receipts reclassified to investing (FY2018 10-K)
     2019:228.8,2020:604.1,2021:173.2,2022:138.5,2023:271.3,2024:259.9,2025:292.9}
sbc={2010:8.8,2011:11.0,2012:14.1,2013:16.7,2014:15.8,2015:17.0,2016:19.2,2017:21.2,2018:8.3,2019:23.6,2020:0.0,2021:19.6,2022:17.6,2023:24.2,2024:28.1,2025:25.5}
capex={2010:12.5,2011:19.5,2012:28.5,2013:82.7,2014:50.2,2015:51.0,2016:36.1,2017:54.0,2018:72.3,2019:80.9,2020:51.3,2021:39.2,2022:78.6,2023:87.6,2024:68.2,2025:65.6}
da={2010:19.1,2011:40.5,2012:36.7,2013:44.7,2014:59.4,2015:63.4,2016:82.3,2017:86.0,2018:81.5,2019:87.4,2020:85.8,2021:81.0,2022:107.8,2023:104.5,2024:106.4,2025:98.2}
tax={2010:24.8,2011:51.1,2012:26.5,2013:34.6,2014:40.8,2015:44.0,2016:37.5,2017:50.8,2018:85.3,2019:82.9,2020:68.5,2021:39.0,2022:66.6,2023:61.3,2024:60.6,2025:97.0}
acq={2010:177.8,2011:122.7,2012:217.8,2013:76.9,2014:273.6,2015:96.9,2016:430.8,2017:120.7,2018:21.3,2019:0,2020:128.6,2021:37.1,2022:643.9,2023:13.7+62.9,2024:40.0+51.8,2025:153.6+7.2}
div={2014:43.0,2019:30.8,2020:259.6,2021:25.0,2023:9.3,2024:209.0,2025:23.4}
oc={y:ocf[y]-sbc[y]-capex[y] for y in yrs}; ocd={y:ocf[y]-sbc[y]-da[y] for y in yrs}
print('year  OCF*   SBC  capex  D&A   OC(capex) OC(D&A) taxpaid  acq(net of divest)')
for y in yrs: print(y, f"{ocf[y]:7.1f} {sbc[y]:5.1f} {capex[y]:5.1f} {da[y]:5.1f} {oc[y]:9.1f} {ocd[y]:7.1f} {tax[y]:6.1f} {acq.get(y,0)-div.get(y,0):8.1f}")
avg=lambda d,ys: sum(d[y] for y in ys)/len(ys)
f5=range(2021,2026); w=yrs
print('5yr avg OC capex %.1f  D&A %.1f  tax %.1f'%(avg(oc,f5),avg(ocd,f5),avg(tax,f5)))
print('16yr avg OC capex %.1f  D&A %.1f  tax %.1f'%(avg(oc,w),avg(ocd,w),avg(tax,w)))
netacq=sum(acq.get(y,0)-div.get(y,0) for y in yrs); print('sum OC capex %.1f  net acquisitions %.1f  per yr %.1f'%(sum(oc.values()),netacq,netacq/16))
r=0.0566; sh=51.15161; px=36.43; mcap=sh*px
print('mcap %.1f'%mcap)
def pv(c,g,r=r,n=10):
    v=0; cf=c
    for t in range(1,n+1): cf*= (1+g); v+=cf/(1+r)**t
    return v+ cf/r/(1+r)**n   # then zero nominal growth
cases={'5yr capex basis':avg(oc,f5),'5yr D&A basis':avg(ocd,f5),'16yr capex basis':avg(oc,w),'16yr D&A basis':avg(ocd,w),'16yr acquisitions as standing-still cost':(sum(oc.values())-netacq)/16}
for k,c in cases.items():
    for g in (0.0,-0.024):
        v=pv(c,g); print(f"{k:42s} g={g:+.3f} cash {c:6.1f} value {v:7.0f}M  ${v/sh:6.2f}/sh")
# floor: ~10% pre-tax on equity price; pre-tax owner cash = OC + cash taxes
for k,(c,t) in {'5yr capex':(avg(oc,f5),avg(tax,f5)),'5yr D&A':(avg(ocd,f5),avg(tax,f5)),'16yr capex':(avg(oc,w),avg(tax,w)),'16yr D&A':(avg(ocd,w),avg(tax,w))}.items():
    pre=c+t
    print(f"{k:12s} pretax cash {pre:6.1f} yield at price {pre/mcap*100:5.2f}%  fair (10% pretax, g=0) ${pre/0.10/sh:6.2f}  fair (g=-2.4%) ${pre/0.124/sh:6.2f}  after-tax yield {c/mcap*100:5.2f}%")
# EV variant: add interest paid proxy (interest expense and other financing costs, net) and net debt at 2026-06-30
intr={2021:47.2,2022:117.4,2023:135.5,2024:116.0,2025:112.0}; netdebt=745.4-135.3
pre=avg(oc,f5)+avg(tax,f5)+avg(intr,f5); print('EV variant pre-tax pre-interest %.1f EV at price %.0f yield %.2f%% fair equity/share $%.2f'%(pre,mcap+netdebt,pre/(mcap+netdebt)*100,(pre/0.10-netdebt)/sh))
print('--- fair price = PV of PRE-TAX owner cash at 10% (price at which expected pre-tax return is ~10%), equity basis')
for k,(c,t) in {'5yr capex':(avg(oc,f5),avg(tax,f5)),'5yr D&A':(avg(ocd,f5),avg(tax,f5)),'16yr capex':(avg(oc,w),avg(tax,w)),'16yr D&A':(avg(ocd,w),avg(tax,w))}.items():
    for g in (0.0,-0.024):
        v=pv(c+t,g,r=0.10); print(f"{k:11s} g={g:+.3f} fair ${v/sh:6.2f}")
# IRR at today's price, 5yr capex pre-tax, g=-2.4%
def irr(c,g,price):
    lo,hi=0.0,0.5
    for _ in range(100):
        m=(lo+hi)/2
        if pv(c,g,r=m)>price: lo=m
        else: hi=m
    return m
for g in (0.0,-0.024):
    print('expected pre-tax return at $36.43, 5yr capex, g=%+.3f: %.2f%%'%(g,irr(avg(oc,f5)+avg(tax,f5),g,mcap)*100))
    print('expected pre-tax return at $36.43, 5yr D&A,   g=%+.3f: %.2f%%'%(g,irr(avg(ocd,f5)+avg(tax,f5),g,mcap)*100))
print('cheap = half of lowest standard case ($29.90): $%.2f; pre-tax D&A-basis yield there %.1f%%'%(29.90/2,(avg(ocd,f5)+avg(tax,f5))/(29.90/2*sh)*100))
print('growth shown: OC 2012-15 avg %.1f -> 2022-25 avg %.1f : %.2f%%/yr'%(avg(oc,range(2012,2016)),avg(oc,range(2022,2026)),((avg(oc,range(2022,2026))/avg(oc,range(2012,2016)))**(1/10)-1)*100))
print('op income 2012-14 avg %.1f -> 2022-24 avg %.1f : %.2f%%/yr'%((257.0+264.4+269.1)/3,(273.2+198.0+210.6)/3,(((273.2+198.0+210.6)/3)/((257.0+264.4+269.1)/3))**(1/10)*100-100))
