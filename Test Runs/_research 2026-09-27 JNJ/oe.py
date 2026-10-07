# Owner earnings, COMPUTATION - NOT A CLEARANCE. OCF, SBC, capex, D&A from companyfacts (checked against the filed
# statements for 2023-2025, and 2025/2024/2023 figures in the 10-K 2025); depreciation alone from each 10-K's PP&E note
# (as first filed, i.e. including the consumer segment in years whose OCF includes it). No net-income proxy.
import sys; sys.stdout.reconfigure(encoding='utf-8')
cap=653612.7
Y={ # fy: (ocf, sbc, capex, D&A incl intangible amortization, depreciation only)
2013:(17414,728,3595,4104,2700),2014:(18710,792,3714,3895,2500),2015:(19569,874,3463,3746,2500),2016:(18767,878,3226,3754,2500),
2017:(21056,962,3279,5642,2600),2018:(22201,978,3670,6929,2600),2019:(23416,977,3498,7009,2500),2020:(23536,1005,3347,7231,2600),
2021:(23410,1135,3652,7390,2700),2022:(21194,1138,4009,6970,2700),2023:(22791,1162,4543,7486,2600),2024:(24266,1176,4424,7339,2800),
2025:(24530,1354,4832,7503,2900)}
note={2013:'consumer inside',2014:'consumer inside',2015:'consumer inside',2016:'consumer inside',2017:'consumer inside; Actelion from June',
2018:'consumer inside',2019:'consumer inside',2020:'consumer inside',2021:'consumer inside; $3.2bn talc paid (KVUE run)',2022:'consumer inside',
2023:'consumer to 23 Aug; not recast',2024:'two-segment company',2025:'two-segment company'}
# Kenvue carve-out figures from the KVUE run (Kenvue's own filings): ocf, sbc, capex, dep
K={2020:(3397,115,229,331),2021:(334,141,295,317),2022:(2525,137,375,296)}
oe={}
print('| FY | perimeter | OCF | SBC | capex | depreciation | D&A incl. amortization | OE capex end | OE depreciation end | OE screen construction (D&A as c) |')
print('|---|---|---|---|---|---|---|---|---|---|')
for y,(o,s,c,da,d) in Y.items():
    oe[y]=(o-s-c,o-s-d,o-s-da)
    print(f'| {y} | {note[y]} | {o:,} | {s:,} | {c:,} | {d:,} | {da:,} | {oe[y][0]:,} | {oe[y][1]:,} | {oe[y][2]:,} |')
def w(a,b,i): 
    v=[oe[y][i] for y in range(a,b+1)]; return sum(v)/len(v)
print()
for n in range(3,14):
    a=2025-n+1; lo=min(w(a,2025,0),w(a,2025,1)); hi=max(w(a,2025,0),w(a,2025,1))
    print(f'{n}y {a}-2025: ${lo:,.0f}M-${hi:,.0f}M, {100*lo/cap:.2f}-{100*hi/cap:.2f}%   screen construction {w(a,2025,2):,.0f}')
print('2y 2024-2025 (the company on offer only): $%s-$%s, %.2f-%.2f%%'%(f'{w(2024,2025,0):,.0f}',f'{w(2024,2025,1):,.0f}',100*w(2024,2025,0)/cap,100*w(2024,2025,1)/cap))
# TTM to 2026-06-28: FY2025 + H1 2026 - H1 2025
o=24530+11130-8052; s=1354+758-698; c=4832+2370-1838; d=2900
print('TTM to 2026-06-28: OCF %d SBC %d capex %d -> capex end %d (%.2f%%); dep end (FY2025 dep) %d (%.2f%%)'%(o,s,c,o-s-c,100*(o-s-c)/cap,o-s-d,100*(o-s-d)/cap))
# Consumer removed with Kenvue's own carve-out figures, 2020-2022 (a disclosed construction)
print()
for y,(ko,ks,kc,kd) in K.items():
    oo,ss,cc,dd=Y[y][0]-ko,Y[y][1]-ks,Y[y][2]-kc,Y[y][4]-kd
    print(f'{y} ex-consumer (JNJ less Kenvue carve-out): OCF {oo:,} SBC {ss:,} capex {cc:,} dep {dd:,} -> OE capex end {oo-ss-cc:,}, dep end {oo-ss-dd:,}')
# 2021 with the $3.2bn talc payment: it is JNJ's liability (retained); it stays in JNJ's owner earnings
