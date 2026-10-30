# CLIR owner cash and the Q7 COMPUTATION (NOT A CLEARANCE). USD thousands. Figures from the filed cash-flow statements:
# FY2025/24 10-K 0001104659-26-037699; FY2023/22 10-K 0001558370-24-004441; FY2021 10-K 0001558370-22-004842.
yrs=[2021,2022,2023,2024,2025]
ocf={2021:-6707,2022:-4992,2023:-3233,2024:-4373,2025:-4736}
sbc={2021:680,2022:373,2023:614,2024:528,2025:893}          # share-based compensation added back in OCF
svc={2021:33,2022:26,2023:10,2024:29,2025:65}               # common stock issued for services, added back
bonus_stock={2021:217,2022:107,2023:234,2024:326,2025:279}  # supplemental: equity awards for prior-year accrued compensation
capex={2021:73,2022:10,2023:0,2024:39,2025:4}
patents={2021:140,2022:154,2023:200,2024:179,2025:97}
interest={2021:1,2022:83,2023:324,2024:516,2025:439}       # interest income in other income (2021 from XBRL InvestmentIncomeInterest)
oc_eq={};oc_all={};oc_narrow={}
for y in yrs:
    oc_narrow[y]=ocf[y]-sbc[y]-svc[y]-capex[y]-patents[y]
    oc_eq[y]=oc_narrow[y]-bonus_stock[y]
    oc_all[y]=oc_eq[y]-interest[y]
mean=lambda d:sum(d.values())/len(d)
print('owner cash, SBC line only (after interest):',oc_narrow,'mean',round(mean(oc_narrow)))
print('owner cash, all stock pay (after interest, equity-only):',oc_eq,'mean',round(mean(oc_eq)))
print('owner cash before interest (all-equity):',oc_all,'mean',round(mean(oc_all)))
r=0.0560; floor=0.10
shares=6807455
netcash=9889+1749   # cash 2026-06-30 plus Private Sale net proceeds stated as subsequent event in 10-Q; no borrowings; operating leases left out
price=3.21
print('market cap $k',round(shares*price/1000),' EV $k',round(shares*price/1000-netcash))
# growth: the series is negative in every year; compound growth between negative end years is meaningless; halves (2021-22 vs 2024-25) also negative bases
def pv(c,rate): # ten years at zero growth then zero growth thereafter = perpetuity
    return c/rate
for lbl,c,add in [('all-equity',mean(oc_all),netcash),('equity-only',mean(oc_eq),0)]:
    v=pv(c,r)+add; f=pv(c,floor)+add
    print(lbl,'value at sovereign $k',round(v),'per share',round(v*1000/shares,2),'| fair (10%) $k',round(f),'per share',round(f*1000/shares,2))
# what the owner cash would have to be for the price to earn the floor (all-equity, no growth)
ev=shares*price/1000-netcash
print('owner cash needed for 10% on EV, $k/yr:',round(ev*floor), ' vs best year',max(oc_all.values()))
# growth-spending alternate: treat all R&D as growth spending (maintenance-only case)
rd={2021:2680,2022:505,2023:739,2024:1471,2025:1422}
alt={y:oc_all[y]+rd[y] for y in yrs}
print('maintenance-only alternate (R&D added back), before interest:',alt,'mean',round(mean(alt)))
m=mean(alt)
for lbl,rate in [('sovereign',r),('10% (fair)',floor)]:
    v=pv(m,rate)+netcash
    print('maintenance-only alternate, all-equity, at',lbl,'$k',round(v),'per share',round(v*1000/shares,2))
print('net cash per share',round(netcash*1000/shares,2))
