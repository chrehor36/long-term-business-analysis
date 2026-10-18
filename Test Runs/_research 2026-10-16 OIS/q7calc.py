# COMPUTATION, NOT A CLEARANCE: OIS value range and fair price (figures in USD millions)
OCF={2014:438.0,2015:256.1,2016:149.3,2017:95.4,2018:103.2,2019:137.4,2020:132.8,2021:7.2,2022:32.9,2023:56.6,2024:45.9,2025:105.1}
SBC={2014:25.6,2015:21.8,2016:21.3,2017:23.0,2018:22.6,2019:16.8,2020:8.4,2021:7.9,2022:6.9,2023:7.0,2024:8.7,2025:7.7}
CAPEX={2014:199.3,2015:114.7,2016:29.7,2017:35.2,2018:88.0,2019:56.1,2020:12.7,2021:17.5,2022:20.3,2023:30.7,2024:37.5,2025:31.2}
DA={2014:124.8,2015:131.3,2016:118.7,2017:107.7,2018:123.5,2019:123.3,2020:98.5,2021:80.7,2022:67.3,2023:60.8,2024:54.7,2025:47.4}
INT={2014:40.4,2015:5.6,2016:3.9,2017:4.2,2018:9.9,2019:9.6,2020:6.4,2021:6.5,2022:8.3,2023:7.9,2024:7.4,2025:7.2}
ACQ={2014:0.2,2015:33.4,2016:0.0,2017:12.9,2018:379.7,2019:0,2020:0,2021:0,2022:8.1,2023:0,2024:0,2025:0}
oc={y:OCF[y]-SBC[y]-CAPEX[y] for y in OCF}
ocda={y:OCF[y]-SBC[y]-DA[y] for y in OCF}
for y in sorted(oc): print(y, 'OC capex %.1f'%oc[y],' OC D&A %.1f'%ocda[y],' +int %.1f'%(oc[y]+INT[y]), ' acq %.1f'%ACQ[y])
avg=lambda d,ys: sum(d[y] for y in ys)/len(ys)
W=range(2021,2026); C=range(2017,2022); L=range(2022,2026)
print('literal window 2021-25 OC %.2f int %.2f all-eq %.2f; D&A basis %.2f'%(avg(oc,W),avg(INT,W),avg(oc,W)+avg(INT,W),avg(ocda,W)))
print('cycle 2017-21 OC organic %.2f int %.2f all-eq %.2f; with acq %.2f; acq total %.1f'%(avg(oc,C),avg(INT,C),avg(oc,C)+avg(INT,C),avg(oc,C)-avg(ACQ,C),sum(ACQ[y] for y in C)))
print('2022-25 OC %.2f all-eq %.2f'%(avg(oc,L),avg(oc,L)+avg(INT,L)))
g=(avg(oc,L)/avg(oc,C))**(1/4.5)-1; print('growth between averages (mid 2019 to mid 2023.5): %.2f%%'%(g*100))
def pv(cf,g,r,years=10):
    v=0;c=cf
    for t in range(1,years+1):
        c=c*(1+g); v+=c/(1+r)**t
    return v + c/r/(1+r)**years
r=0.0543; ND=18.6+2.036-19.802; SH=60.322619
for basis,top,lit in [('all-equity',avg(oc,C)+avg(INT,C),avg(oc,W)+avg(INT,W)),('equity-only',avg(oc,C),avg(oc,W))]:
    hi=pv(top,0,r); lo=pv(top,g,r); li=pv(lit,0,r)
    nd = ND if basis=='all-equity' else 0
    print(basis,'top %.1f bottom %.1f literal %.1f'%(hi,lo,li),' per share top %.2f bottom %.2f literal %.2f'%((hi-nd)/SH,(lo-nd)/SH,(li-nd)/SH))
    f=(pv(top,0,0.10)+pv(top,g,0.10))/2; print('   fair (avg of ends at 10%%) %.1f -> per share %.2f; literal at 10%% %.2f'%(f,(f-nd)/SH,(pv(lit,0,0.10)-nd)/SH))
    # expected return at price: rate at which value = price
    P=7.94*SH+nd
    for name,cf,gg in [('top',top,0),('bottom',top,g),('literal',lit,0)]:
        lo_,hi_=0.0001,1
        for _ in range(100):
            m=(lo_+hi_)/2
            if pv(cf,gg,m)>P: lo_=m
            else: hi_=m
        print('   expected return at $7.94, %s case: %.2f%%'%(name,m*100))
print('net debt 2026-06-30 %.1f'%ND)
