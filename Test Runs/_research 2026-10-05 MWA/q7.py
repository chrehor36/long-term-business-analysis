# Q7 arithmetic for MWA (computation only). Figures from filed 10-K cash-flow statements (accessions in run file).
ocf  ={2018:133.1,2019:92.5,2020:140.3,2021:156.7,2022:52.3,2023:109.0,2024:238.8,2025:219.3}
sbc  ={2018:5.2,2019:4.3,2020:5.3,2021:8.1,2022:8.7,2023:8.5,2024:9.0,2025:10.7}   # cash-flow add-back
capex={2018:55.7,2019:86.6,2020:67.7,2021:62.7,2022:54.7,2023:47.6,2024:47.4,2025:47.3}
dep  ={2018:20.9,2019:26.0,2020:29.6,2021:31.4,2022:32.0,2023:34.4,2024:39.1,2025:39.7}
ni   ={2018:105.6,2019:63.8,2020:72.0,2021:70.4,2022:76.6,2023:85.5,2024:115.9,2025:191.7}
oc={y:ocf[y]-sbc[y]-capex[y] for y in ocf}
od={y:ocf[y]-sbc[y]-dep[y] for y in ocf}
for y in ocf: print(y, 'owner cash %.1f'%oc[y], ' dep-variant %.1f'%od[y], ' NI %.1f'%ni[y])
yrs=[2021,2022,2023,2024,2025]
a=sum(oc[y] for y in yrs)/5; ad=sum(od[y] for y in yrs)/5
print('5yr avg owner cash %.1f ; dep variant %.1f'%(a,ad))
print('8yr avg owner cash %.1f'%(sum(oc.values())/8))
g_end=(oc[2025]/oc[2021])**(1/4)-1
print('endpoint growth FY21-25 %.1f%%'%(100*g_end))
print('first2 avg %.1f last2 avg %.1f'%((oc[2021]+oc[2022])/2,(oc[2024]+oc[2025])/2))
sales={2015:793.4,2020:964.1,2025:1429.7}
print('sales growth 2015-25 %.1f%%  2020-25 %.1f%%'%(100*((1429.7/793.4)**0.1-1),100*((1429.7/964.1)**0.2-1)))
r=0.0563; sh=156.125679; price=22.02; mcap=price*sh
def pv(c,g,rate,n=10):
    v=0; cf=c
    for t in range(1,n+1):
        cf=c*(1+g)**t; v+=cf/(1+rate)**t
    v+= (c*(1+g)**n)/rate/(1+rate)**n
    return v
def irr(c,g,target):
    lo,hi=0.0001,0.5
    for _ in range(200):
        m=(lo+hi)/2
        if pv(c,g,m)>target: lo=m
        else: hi=m
    return m
gcap=r  # cap at the discount rate (Q3 arithmetic, read literally)
print('mcap %.0f'%mcap)
for name,c in [('5yr owner cash',a),('5yr dep variant',ad),('FY2025 owner cash',oc[2025])]:
    lo=c/r; hi=pv(c,gcap,r)
    print(f'{name}: base {c:.1f}  no-growth {lo:.0f} (${lo/sh:.2f})  shown-growth(cap {gcap*100:.2f}%) {hi:.0f} (${hi/sh:.2f})  width {hi/lo:.2f}  IRR@price nogrowth {100*irr(c,0,mcap):.2f}%  growth {100*irr(c,gcap,mcap):.2f}%')
# TTM to June 2026
ttm_oc = oc[2025] + (154.2-10.5-43.6) - (135.8-7.3-32.8)
print('TTM owner cash %.1f'%ttm_oc)
c=ttm_oc; print(f'TTM: no-growth {c/r:.0f} (${c/r/sh:.2f}) growth {pv(c,gcap,r):.0f} (${pv(c,gcap,r)/sh:.2f}) IRR growth {100*irr(c,gcap,mcap):.2f}%')
# pretax check
ttm_pti=254.2+(214.3-185.5); print('TTM pretax income %.1f yield %.2f%%'%(ttm_pti,100*ttm_pti/mcap))
# Fair price: central case = 5yr avg owner cash, growth half the cap, discounted at after-tax equivalent of 10% pre-tax
tax=0.246; rr=0.10*(1-tax)
gc=gcap/2
for name,c in [('5yr',a),('FY2025',oc[2025]),('TTM',ttm_oc)]:
    v=pv(c,gc,rr); print(f'fair ({name} base, g {gc*100:.2f}%, rate {rr*100:.2f}%): {v:.0f}  ${v/sh:.2f}')
print('--- fair and cheap ---')
cen=(a+oc[2025])/2
for rate in (rr,0.07):
    v=pv(cen,gc,rate); print(f'central base {cen:.1f} g {gc*100:.2f}% rate {rate*100:.2f}%: {v:.0f}  ${v/sh:.2f}')
print('cheap: 5yr no-growth at floor rate %.0f  $%.2f'%(a/rr, a/rr/sh))
print('diluted shares 157.3: range $%.2f-$%.2f'%(a/r/157.3, pv(a,gcap,r)/157.3))
# tangible capital employed
ca={2018:685.5,2019:566.9,2020:581.2,2021:653.7,2022:680.0,2023:706.8,2024:858.4,2025:1028.9}
cash={2018:347.1,2019:176.7,2020:208.9,2021:227.5,2022:146.5,2023:160.3,2024:309.9,2025:431.5}
cl={2018:167.1,2019:178.5,2020:155.0,2021:220.1,2022:241.0,2023:218.8,2024:258.0,2025:290.3}
cd={2018:0.7,2019:0.9,2020:1.1,2021:1.0,2022:0.8,2023:0.7,2024:0.8,2025:1.2}
ppe={2018:150.9,2019:217.1,2020:253.8,2021:283.4,2022:301.6,2023:311.7,2024:318.8,2025:335.7}
oi={2018:121.7,2019:124.3,2020:116.8,2021:131.7,2022:111.6,2023:127.4,2024:181.7,2025:260.6}
for y in ca:
    tc=(ca[y]-cash[y])-(cl[y]-cd[y])+ppe[y]
    print(y,'tangible capital %.1f'%tc,' op income %.1f'%oi[y],' pre-tax return %.1f%%'%(100*oi[y]/tc))
