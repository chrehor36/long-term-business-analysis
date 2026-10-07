# Owner earnings = operating cash flow as filed - SBC in full - (c) at two ends. No net-income proxy.
# Figures: filed cash-flow statements (10-K of each year or its restated vintage in companyfacts; cross-checked in cfs.py).
import sys
sys.stdout.reconfigure(encoding='utf-8')
cap=175270.5
D={ # year: (OCF, SBC, capex, depreciation, amortization, acquisitions cash, dividends, buybacks)
2013:(3324,262,1145,928,791,580,None,None),
2014:(3675,246,1077,918,630,3317,None,None),
2015:(2966,292,1110,871,601,235,None,None),
2016:(3203,310,1121,803,550,80,None,None),
2017:(5570,406,1135,1046,1975,17183,1849,117),
2018:(6300,477,1394,1100,2178,54,1974,238),
2019:(6136,519,1638,1078,1936,170,2270,718),
2020:(7901,546,2177,1195,2132,42,2560,403),
2021:(10533,640,1885,1491,2047,187,3202,2299),
2022:(9581,685,1777,1254,2013,0,3309,3795),
2023:(7261,644,2202,1277,1966,877,3556,1227),
2024:(8558,673,2207,1340,1878,0,3836,1295),
2025:(9566,664,2171,1434,1682,105,4116,893),
}
tag={2013:'post-AbbVie; pre-St. Jude',2014:'pre-St. Jude',2015:'Mylan/Zoetis sales; pre-St. Jude',2016:'pre-St. Jude (AMO still in)',2017:'St. Jude from 4 Jan, Alere from 3 Oct; AMO sold',2018:'',2019:'',2020:'COVID tests $3.9bn',2021:'COVID tests $7.7bn',2022:'COVID tests $8.4bn; Sturgis recall',2023:'COVID tests $1.6bn; CSI',2024:'COVID $0.7bn',2025:'COVID $0.3bn'}
print('| year | perimeter / named break | OCF | SBC | capex | depreciation | OE capex end | OE depreciation end | screen-style (c)=D+A |')
print('|---|---|---|---|---|---|---|---|---|')
oe={}
for y,(o,s,c,d,a,acq,div,bb) in D.items():
    oe[y]=(o-s-c,o-s-d,o-s-d-a)
    print(f'| {y} | {tag[y]} | {o:,} | {s:,} | {c:,} | {d:,} | {o-s-c:,} | {o-s-d:,} | {o-s-d-a:,} |')
print()
print('Every trailing window ending 2025:')
for n in range(3,14):
    ys=list(range(2026-n,2026))
    lo=sum(oe[y][0] for y in ys)/n; hi=sum(oe[y][1] for y in ys)/n
    b=min(lo,hi); t=max(lo,hi)
    mark='' if ys[0]>=2017 else '  [spans pre-St. Jude perimeter]'
    cov=' [carries COVID 2020-22]' if ys[0]<=2022 else ''
    print(f'  {n:2d}y {ys[0]}-2025: ${b:,.0f}M to ${t:,.0f}M = {b/cap:.2%} to {t/cap:.2%}{mark}{cov}')
nc=[2017,2018,2019,2023,2024,2025]
lo=sum(oe[y][0] for y in nc)/6; hi=sum(oe[y][1] for y in nc)/6
print(f'  6 non-COVID years of the 2017+ perimeter (2017-19, 2023-25): ${lo:,.0f}M to ${hi:,.0f}M = {lo/cap:.2%} to {hi/cap:.2%}')
nc=[2018,2019,2023,2024,2025]
lo=sum(oe[y][0] for y in nc)/5; hi=sum(oe[y][1] for y in nc)/5
print(f'  5 non-COVID years excl. St. Jude year (2018-19, 2023-25): ${lo:,.0f}M to ${hi:,.0f}M = {lo/cap:.2%} to {hi/cap:.2%}')
# screen reproduction
sb=sum(oe[y][2] for y in (2023,2024,2025))/3; st=sum(oe[y][0] for y in range(2021,2026))/5
print(f'screen bottom check (3y, (c)=depreciation+amortization): {sb:,.1f}; screen top check (5y capex end): {st:,.1f}')
# TTM to 2026-06-30
o=9566-3464+3803; s=664-431+485; c=2171-986+896; d=1434-693+783
print(f'TTM to 2026-06-30: OCF {o:,} SBC {s:,} capex {c:,} dep {d:,} -> OE {o-s-c:,} to {o-s-d:,}; {(o-s-c)/cap:.2%} to {(o-s-d)/cap:.2%} (includes ~3 months of Exact Sciences and the cash settlement of its equity awards)')
# payouts vs OE
for y in range(2017,2026):
    o,s,c,d,a,acq,div,bb=D[y]
    print(f'  {y}: dividends {div:,} + buybacks {bb:,} = {div+bb:,} vs OE capex end {oe[y][0]:,}  ({(div+bb)/oe[y][0]:.0%})')
