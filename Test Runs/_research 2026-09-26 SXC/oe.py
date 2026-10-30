# Owner earnings from the FILED cash-flow statements (latest 10-K showing each year), no net-income proxy.
# OE = OCF - SBC - (c); (c) = total capex (+ finance-lease principal where filed) OR D&A less acquired-intangible amortisation.
# NCI: A = less total NCI net income as filed (the structure of each year: SXCP public unitholders 2013-2019 + Indiana Harbor 14.8%)
#      B = less the NCI that still exists (Indiana Harbor 14.8%): filed split 2015-2019; 2012 and 2020-2025 all NCI is Indiana Harbor; 2013-2014 split not filed -> 0 deducted, flagged
CAP=9.57*84874850/1e6
SOV=5.49
# year: (OCF, SBC, DA, capex, source 10-K)
Y={2011:(101.3,2.1,58.4,238.1,'FY2013'),2012:(206.1,6.7,80.8,80.6,'FY2013'),2013:(151.3,7.6,96.0,145.6,'FY2015'),
2014:(112.3,9.8,106.3,125.2,'FY2016'),2015:(141.1,7.2,109.1,75.8,'FY2017'),2016:(219.1,6.5,114.2,63.7,'FY2018'),
2017:(148.5,4.8,128.2,75.6,'FY2019'),2018:(185.8,3.1,141.6,100.3,'FY2020'),2019:(181.9,4.5,143.8,110.1,'FY2021'),
2020:(157.8,3.8,133.7,73.9,'FY2022'),2021:(233.1,6.1,133.9,98.6,'FY2023'),2022:(208.9,6.7,142.5,75.5,'FY2024'),
2023:(249.0,5.1,142.8,109.2,'FY2025'),2024:(168.8,4.0,118.9,72.9,'FY2025'),2025:(109.1,2.4,153.6,66.8,'FY2025')}
AMORT={2011:0,2012:0,2013:0.8,2014:1.5,2015:5.1,2016:11.2,2017:11.1,2018:11.1,2019:8.8,2020:2.5,2021:2.0,2022:2.0,2023:2.1,2024:1.9,2025:2.0}
FINLEASE={2024:0.2,2025:10.3}
NCI_A={2011:-1.7,2012:3.7,2013:25.1,2014:24.3,2015:32.3,2016:45.1,2017:-18.9,2018:20.8,2019:3.9,2020:5.1,2021:5.4,2022:4.2,2023:6.0,2024:7.6,2025:5.4}
NCI_B={2011:-1.7,2012:3.7,2013:0.0,2014:0.0,2015:-1.8,2016:-1.0,2017:-5.4,2018:-0.8,2019:1.3,2020:5.1,2021:5.4,2022:4.2,2023:6.0,2024:7.6,2025:5.4}
rows={}
out=[]
out.append(f'cap ${CAP:,.1f}M (9.57 x 84,874,850); sovereign {SOV}%')
out.append('FY | OCF | SBC | D&A | amort | capex+finlease | NCI A | NCI B | OE capex end (B) | OE D&A-net end (B) | OE capex end (A) | OE D&A end (A) | src')
for y,(ocf,sbc,da,cx,src) in sorted(Y.items()):
    c1=cx+FINLEASE.get(y,0); c2=da-AMORT[y]
    r=dict(capB=ocf-sbc-c1-NCI_B[y], daB=ocf-sbc-c2-NCI_B[y], capA=ocf-sbc-c1-NCI_A[y], daA=ocf-sbc-c2-NCI_A[y])
    rows[y]=r
    out.append(f'{y} | {ocf:.1f} | {sbc:.1f} | {da:.1f} | {AMORT[y]:.1f} | {c1:.1f} | {NCI_A[y]:.1f} | {NCI_B[y]:.1f} | {r["capB"]:.1f} | {r["daB"]:.1f} | {r["capA"]:.1f} | {r["daA"]:.1f} | {src}')
out.append('')
out.append('window ending FY2025 | capex end B | D&A end B | yield capB | yield daB | capex end A | D&A end A | yield lowest')
allv=[]
for n in range(3,16):
    ys=[y for y in range(2026-n,2026)]
    m={k:sum(rows[y][k] for y in ys)/n for k in ['capB','daB','capA','daA']}
    lo=min(m.values()); hi=max(m.values())
    allv+= [m['capB'],m['daB'],m['capA'],m['daA']]
    out.append(f'{n}y FY{ys[0]}-25 | {m["capB"]:.1f} | {m["daB"]:.1f} | {100*m["capB"]/CAP:.2f}% | {100*m["daB"]/CAP:.2f}% | {m["capA"]:.1f} | {m["daA"]:.1f} | {100*lo/CAP:.2f}%-{100*hi/CAP:.2f}%')
out.append(f'COMBINED 3y-15y, both ends, both NCI treatments: ${min(allv):.1f}M to ${max(allv):.1f}M = {100*min(allv)/CAP:.2f}% to {100*max(allv)/CAP:.2f}% vs {SOV}%')
# screen reproduction: screen uses OCF-SBC-capex / OCF-SBC-DA without NCI, 3y/5y
for n in (3,5):
    ys=range(2026-n,2026)
    a=sum(Y[y][0]-Y[y][1]-Y[y][3] for y in ys)/n; b=sum(Y[y][0]-Y[y][1]-Y[y][2] for y in ys)/n
    out.append(f'screen-style {n}y no NCI: capex end {a:.1f}, D&A end {b:.1f}')
# TTM to 2026-06-30
ocf=109.1+45.5-43.3; sbc=2.4+3.1-1.8; cx=66.8+32.9-17.5; fl=10.3+3.0-0.2; da=153.6+84.8-57.4; nci=5.4+3.5-3.7
out.append(f'TTM to 2026-06-30: OCF {ocf:.1f} SBC {sbc:.1f} capex {cx:.1f} finlease {fl:.1f} D&A {da:.1f} NCI {nci:.1f} -> capex end {ocf-sbc-cx-fl-nci:.1f}, D&A end {ocf-sbc-(da-2.0)-nci:.1f}')
open('oe_out.txt','w').write('\n'.join(out)); print('\n'.join(out))
