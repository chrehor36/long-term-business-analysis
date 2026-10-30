# COMPUTATION, NOT A CLEARANCE: Q7 range and fair price for GXYYY, HK$ millions unless per share.
import importlib.util,sys
r=0.04597; floor=0.10; shares=4379.240712; price=33.06; ads=5
DA={2014:1884.445,2015:3086.292,2016:3572.577,2017:3348.665,2018:3315.913,2019:3456.596,2020:2816.740,2021:2264.113,2022:2088.338,2023:2835.702,2024:3560.992,2025:3794.212}
# owner cash series from owner_cash.py (as paid) -- recomputed here
D={2015:(6753.375,67.249,439.846,6594.138,5.568,0.164,0,105.095,650.0,50991.0,1066.138),
2016:(12865.401,88.309,410.265,2127.839,21.903,0,0,48.371,0,52826.0,1167.301),
2017:(18737.538,94.380,381.049,2021.997,9.668,16.002,0,89.392,0,62520.0,1572.377),
2018:(14051.765,128.140,209.253,3033.046,50.902,0,0,186.438,0,55210.901,1843.375),
2019:(19702.265,140.704,275.391,4171.658,2.483,42.511,0,300.711,0,51901.991,1809.473),
2020:(-7418.491,139.844,297.811,5797.018,1.342,52.455,0,430.156,0,12876.099,0),
2021:(-3274.964,130.923,206.043,6930.761,5.115,53.350,0,376.952,0,19695.530,332.846),
2022:(-2882.847,96.534,181.190,5077.238,61.980,52.862,0,354.511,0,11473.793,0),
2023:(11663.166,69.325,251.279,6018.284,0.273,79.461,267.948,167.259,850.342,35684.253,1064.617),
2024:(11713.501,163.238,261.373,4868.198,5.825,91.384,268.880,59.127,-27.423,43432.373,1330.582),
2025:(14460.713,207.150,229.454,3482.126,5.224,93.639,269.827,27.966,-0.730,49242.325,1582.775)}
rows={}
for y,(cgo,tax,sbc,cap,disp,lease,conc,jv,acq,rev,ex) in D.items():
    pre=cgo-tax-sbc+disp-lease-conc+jv          # before capex, as paid
    rows[y]=dict(allsp=pre-cap, maint=pre-DA[y], ex=ex, acq=acq, rev=rev)
def avg(ys,k,stat=True,acq=True):
    return sum(rows[y][k]-(rows[y]['ex'] if stat else 0)-(rows[y]['acq'] if acq else 0) for y in ys)/len(ys)
c1=[2015,2016,2017,2018,2019]; c2=[2023,2024,2025]; win=[2021,2022,2023,2024,2025]
def val(B,g,rate,stop_acq=0.0):
    pv=0; c=B
    for t in range(1,11):
        c=c*(1+g); pv+=c/(1+rate)**t
    term=(c+stop_acq)/rate/(1+rate)**10
    return pv+term
# net cash at 30 June 2026 with the interim dividend paid after the date (subsequent event stated in the interim report)
cash=15704.003; secs_amort=12370.548+5709.056; fvoci=5466.544; borrow=1831.228; intdiv=0.90*shares; nci=465.367
netcash=cash+secs_amort+fvoci-borrow-intdiv
shelter=sum(1582.775/(1+r)**t for t in (1,2))  # exemption 2026-2027 at the 2025 level, PV at the long rate
print(f'net cash {netcash:,.0f}  nci {nci:,.0f}  shelter PV {shelter:,.0f}')
mcap=price*shares; ev=mcap-netcash+nci
print(f'market cap {mcap:,.0f}  EV(all-equity) {ev:,.0f}')
def case(label,k,stat,acq_in_base=True):
    B1=avg(c1,k,stat); B2=avg(c2,k,stat)
    g=(B2/B1)**(1/7)-1
    acqavg=sum(rows[y]['acq'] for y in c1)/5
    top=val(B1,0,r,acqavg); bot=val(B1,g,r,acqavg*(1+g)**0)
    sh=shelter if stat else 0
    tps=(top+netcash-nci+sh)/shares; bps=(bot+netcash-nci+sh)/shares
    t10=val(B1,0,floor,acqavg); b10=val(B1,g,floor,acqavg)
    fair=((t10+b10)/2+netcash-nci+sh)/shares
    # equity-only: owner cash after interest; the company is net cash, interest paid is small; equity-only = all-equity here less nothing for debt
    yld_top=B1/ev; 
    print(f'{label}: base {B1:,.0f} recent {B2:,.0f} g {g:.2%} | range/sh {bps:.2f} to {tps:.2f} (ratio {tps/bps:.2f}) | fair {fair:.2f}/sh {fair*ads:.2f}/ADS | top-case yield at price {yld_top:.2%}')
    return B1,B2,g,bps,tps,fair
print('central: maintenance (D&A) case, statutory Macau complementary tax, acquisitions deducted:')
C=case('central maint stat',  'maint',True)
case('all-spending stat    ','allsp',True)
case('maint as-paid tax    ','maint',False)
case('all-spending as-paid ','allsp',False)
# literal window
for k in ('maint','allsp'):
    for st in (True,False):
        print('literal window 2021-2025',k,'stat' if st else 'paid', round(avg(win,k,st)))
print('2025 alone maint stat',round(rows[2025]['maint']-rows[2025]['ex']),' as paid',round(rows[2025]['maint']))
for y in sorted(rows): print(y, {k:round(v) for k,v in rows[y].items()}, 'stat maint', round(rows[y]['maint']-rows[y]['ex']))
# concession-term-only variant: central base, decline, cash ends 2032 (7 years), no residual
B1,B2,g,_,_,_=C
pv=sum(B1*(1+g)**t/(1+r)**t for t in range(1,8))
print('concession-term only (2026-2032, no residual): per share', round((pv+netcash-nci+shelter)/shares,2))
# equity-only: owner cash after interest paid, with the interest and listed dividends actually received (the securities' own yield),
# valued at the floor with no balance-sheet addition; cycle 2015-2019 and recent 2023-2025 net investment income from the cash-flow statements
nii={2015:133.157-60.569,2016:81.177+2.100-45.187,2017:532.610+2.650-123.438,2018:964.551+69.130-139.910,2019:1189.168+119.053-119.292,
     2023:818.351+33.540-137.385,2024:978.213+56.727-47.232,2025:1245.269+59.975-72.212}
n1=sum(nii[y] for y in c1)/5; n2=sum(nii[y] for y in c2)/3
B1,B2,g,_,_,_=C
acqavg=sum(rows[y]['acq'] for y in c1)/5
E1=B1+n1; E2=B2+n2; ge=(E2/E1)**(1/7)-1
t10=val(E1,0,floor,acqavg); b10=val(E1,ge,floor,acqavg)
fe=((t10+b10)/2-nci+shelter)/shares
print(f'equity-only: base {E1:,.0f} recent {E2:,.0f} g {ge:.2%} fair {fe:.2f}/sh {fe*ads:.2f}/ADS; yield at price {E1/mcap:.2%}')
