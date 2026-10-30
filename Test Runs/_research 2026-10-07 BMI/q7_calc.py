"""Q7 arithmetic for BMI (COMPUTATION; figures in $M from the filed statements; see run file for accessions)."""
# year: (OCF, SBC, capex, depreciation, acquisitions, net interest income pre-tax)
d = {
2008:(26.143,None,13.237,None,None,None),
2009:(36.588,1.2,7.750,6.7,0.0,None),
2010:(18.396,1.4,9.238,6.7,7.3,None),
2011:(31.317,1.5,5.3,7.1,4.0,None),
2012:(34.802,1.3,8.2,7.6,51.5,None),
2013:(34.818,1.4,14.3,8.5,15.4,None),
2014:(35.735,1.4,12.3,8.9,20.8,None),
2015:(35.831,1.5,19.8,10.0,1.9,None),
2016:(56.185,1.5,10.6,10.7,1.8,None),
2017:(49.751,1.725,15.1,12.1,20.376,-0.789),
2018:(60.350,4.174,8.6,11.4,8.048,-1.157),
2019:(80.714,1.214,7.5,11.6,0.0,-0.253),
2020:(89.6,1.4,9.1,12.3,29.1,-0.030),
2021:(87.5,2.3,6.7,11.3,45.3,0.020),
2022:(82.5,3.1,5.9,11.1,0.0,0.552),
2023:(110.117,5.188,12.003,10.937,17.127,4.047),
2024:(155.034,6.182,12.818,11.103,3.000,8.613),
2025:(183.698,9.190,14.026,11.103,184.024,5.124),
}
TAX=0.25  # company's own rate, 24.1-25.0% in 2023-2025 (10-K)
oc={}; ocd={}
for y,(ocf,sbc,cap,dep,acq,ii) in d.items():
    if sbc is None: continue
    adj = (ii or 0.0)*(1-TAX)            # all-equity basis: remove after-tax net interest income
    oc[y]  = ocf - sbc - cap - adj        # capex basis
    ocd[y] = ocf - sbc - dep - adj        # depreciation variant
for y in sorted(oc): print(y, round(oc[y],1), round(ocd[y],1), d[y][4])
def avg(s,ys): return sum(s[y] for y in ys)/len(ys)
def acqavg(ys): return sum(d[y][4] for y in ys)/len(ys)
def cagr(a,b,n): return (b/a)**(1/n)-1
r=0.0564
def value(base,g,years=10):
    pv=0; c=base
    for t in range(1,years+1):
        c*=1+g; pv+=c/(1+r)**t
    return pv + c/r/(1+r)**years
def price_at(base,g,rate,years=10):
    pv=0; c=base
    for t in range(1,years+1):
        c*=1+g; pv+=c/(1+rate)**t
    return pv + c/rate/(1+rate)**years
SH=28.986847; ND=-95.733+12.0  # net debt 2026-06-30: no borrowings, cash 95.733, UDlive earn-out fair value 12.0
P=123.73; MC=SH*P; EV=MC+ND
print('mcap',round(MC,1),'net debt',round(ND,1),'EV',round(EV,1))
cases={}
W=[2021,2022,2023,2024,2025]; C=[2019,2020,2021,2022,2023,2024,2025]; PRIOR=[2011,2012,2013,2014,2015,2016,2017,2018]
gW=cagr(oc[2021],oc[2025],4)
gC=cagr(avg(oc,PRIOR),avg(oc,C),7.5)
print('literal window avg OC',round(avg(oc,W),1),'acq avg',round(acqavg(W),1),'growth 2021-25',round(gW*100,1))
print('cycle 2019-25 avg OC',round(avg(oc,C),1),'acq avg',round(acqavg(C),1),'prior cycle 2011-18 avg',round(avg(oc,PRIOR),1),'growth between cycle avgs',round(gC*100,1))
sales={2008:279.552,2010:276.634,2018:433.732,2025:916.663}
gS=cagr(sales[2008],sales[2025],17); print('sales peak-to-peak 2008-2025 CAGR',round(gS*100,2))
def show(name,base,g):
    lo=value(base,0); hi=value(base,g)
    lo_ps=(lo-ND)/SH; hi_ps=(hi-ND)/SH
    f_lo=price_at(base,0,0.10); f_hi=price_at(base,g,0.10); fair=(f_lo+f_hi)/2
    print(f"{name}: base {base:.1f} g {g*100:.1f}% | value {lo:.0f}-{hi:.0f} ($M) ratio {hi/lo:.2f} | per share ${lo_ps:.2f}-${hi_ps:.2f} | fair(10%) EV {fair:.0f} -> ${(fair-ND)/SH:.2f}/sh | EV/hi {EV/hi:.2f}")
    return lo,hi,fair
show('W1 window, acq deducted, total growth', avg(oc,W)-acqavg(W), gW)
show('W2 window, acq left out, total growth (NOT ALLOWED, shown for scale)', avg(oc,W), gW)
show('C1 cycle 2019-25, acq deducted, growth between cycles', avg(oc,C)-acqavg(C), gC)
show('X1 window base acq deducted, growth cut back to sales p2p', avg(oc,W)-acqavg(W), gS)
show('X2 cycle base acq deducted, growth cut back to sales p2p', avg(oc,C)-acqavg(C), gS)
show('D1 depreciation variant window acq deducted, total growth', avg(ocd,W)-acqavg(W), cagr(ocd[2021],ocd[2025],4))
# equity-only figures: owner cash after interest (interest income kept), against market value
ocq={y:oc[y]+(d[y][5] or 0)*(1-TAX) for y in oc}
def show_eq(name,base,g):
    lo=value(base,0); hi=value(base,g); f=(price_at(base,0,0.10)+price_at(base,g,0.10))/2
    print(f"EQ {name}: base {base:.1f} value {lo:.0f}-{hi:.0f} per share ${lo/SH:.2f}-${hi/SH:.2f} fair ${f/SH:.2f}")
show_eq('window acq deducted total growth', avg(ocq,W)-acqavg(W), gW)
show_eq('cycle acq deducted cut back', avg(ocq,C)-acqavg(C), gS)
# what growth does the price imply at 10% (all-equity), on each base
import math
for nm,b in [('W1',avg(oc,W)-acqavg(W)),('C1',avg(oc,C)-acqavg(C)),('2025 alone, no acq',oc[2025])]:
    lo,hi=-0.5,0.6
    for _ in range(80):
        m=(lo+hi)/2
        if price_at(b,m,0.10)>EV: hi=m
        else: lo=m
    print('growth for 10 yrs needed to earn 10% at EV on',nm,round(m*100,1),'%')
print('owner-cash yield on EV: 2025',round(oc[2025]/EV*100,2),'% ; window avg',round(avg(oc,W)/EV*100,2),'% ; window avg less acq',round((avg(oc,W)-acqavg(W))/EV*100,2),'%')
print('--- additions')
# equity-only for the cut-back central case
show_eq('window acq deducted cut back (central X1, equity-only)', avg(ocq,W)-acqavg(W), gS)
# organic pair: acquisitions left out, organic sales growth as the filer reports it (2021 9.2%, 2022 11.9%, 2023 ~23.5%, 2024 ~17%, 2025 6.1%)
# organic % per year from the filer's MD&A: 2021: (79.7-40.7)/425.5; 2022: 60.4/505.2 (no deal); 2023: (703.6-565.6)/565.6 less Syrinix (not separately stated -> total used); 2024: total 17.5% (Telog/Unity $3.0M purchase, revenue not stated -> total used); 2025: (90.1-39.7)/826.6
org=[(79.7-40.7)/425.5, 60.4/505.2, (703.592-565.6)/565.6, (826.558-703.592)/703.592, (90.1-39.7)/826.558]
import functools
gO=functools.reduce(lambda a,b:a*(1+b),org[1:],1)**(1/4)-1
print('organic sales growth by year',[round(x*100,1) for x in org],'CAGR 2021-2025 (4 yrs)',round(gO*100,1))
show('O1 organic pair: acq left out, organic growth', avg(oc,W), gO)
show('O2 organic pair cut back to sales p2p', avg(oc,W), gS)
for nm,b in [('W1 base',avg(oc,W)-acqavg(W)),('O base (acq left out)',avg(oc,W))]:
    lo,hi=-0.5,0.6
    for _ in range(80):
        m=(lo+hi)/2
        if value(b,m)>EV: hi=m
        else: lo=m
    print('growth at which the TOP of the range (5.64%) equals EV,',nm,round(m*100,1),'%')
# margin-bound check: OC margin needed in 2035 if OC grows at gW and sales grow at gS
m25=oc[2025]/916.663
print('2025 OC margin',round(m25*100,1),'% ; margin needed in yr10 at 18.9% OC growth with 7.24% sales growth',round(m25*((1+gW)/(1+gS))**10*100,1),'%')
print('gross margin 2025 41.7% (10-K)')
