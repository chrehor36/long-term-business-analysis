"""MRK owner earnings, COMPUTATION - NOT A CLEARANCE. Figures typed from the filed cash-flow statements:
2023-2025 10-K 2025 (0000310158-26-000063); 2020-2022 10-K 2022 (0001628280-23-005061, continuing operations);
2019 10-K 2021 (0000310158-22-000003, continuing operations); 2017-2018 10-K 2019 (0000310158-20-000005, as filed, WITH Organon's businesses).
OCF less SBC in full [E5-06] less (c) at two ends: capex end, and depreciation end (depreciation only; amortization of acquired
intangibles is not maintenance). No net-income proxy. Acquisitions = cash paid for businesses and R&D asset acquisitions in investing."""
import itertools
CAP=148.78*2467171638/1e6
D={ # year: OCF, SBC, capex, depreciation, amortization, acquisitions (investing), perimeter
2017:(6451,312,1888,None,None,396,'with Organon'),
2018:(10922,348,2615,None,None,431,'with Organon'),
2019:(8884,388,3369,1615,1695,4954,'continuing'),
2020:(7617,441,4429,1669,1817,6606,'continuing'),
2021:(13122,479,4448,1578,1636,12907,'continuing'),
2022:(19095,541,4388,1824,2085,121,'continuing'),
2023:(13006,645,3863,1828,2044,12032,'continuing'),
2024:(21468,761,3372,2104,2395,4093,'continuing'),
2025:(16472,820,4112,3045,2793,10042,'continuing'),
}
print('cap $%.1fM'%CAP)
print('| year | OCF | SBC | capex | dep | amort | acq | OE capex end | OE dep end |')
for y,(o,s,c,d,a,q,p) in D.items():
    print(f'| {y} ({p}) | {o:,} | {s} | {c:,} | {d or "n/f"} | {a or "n/f"} | {q:,} | {o-s-c:,} | {o-s-d if d else "n/f":} |')
rows=[]
lo,hi=1e18,-1e18
for n in range(3,8):
    ys=list(range(2025-n+1,2026))
    m=lambda i: sum(D[y][i] for y in ys)/n
    ce=m(0)-m(1)-m(2); de=m(0)-m(1)-m(3); acq=m(5)
    lo=min(lo,ce,de); hi=max(hi,ce,de)
    print(f'{n}y {ys[0]}-2025: capex end {ce:,.0f} ({ce/CAP:.2%}) | dep end {de:,.0f} ({de/CAP:.2%}) | D&A caption end {m(0)-m(1)-m(3)-m(4):,.0f} | less acquisitions: {ce-acq:,.0f} to {de-acq:,.0f} ({(min(ce,de)-acq)/CAP:.2%} to {(max(ce,de)-acq)/CAP:.2%})')
print(f'COMBINED continuing-perimeter range 3-7y both ends: {lo:,.0f} to {hi:,.0f} = {lo/CAP:.2%} to {hi/CAP:.2%}')
# screen reproduction attempts
for n in (3,5):
    ys=list(range(2025-n+1,2026)); m=lambda i: sum(D[y][i] for y in ys)/n
    print(n,'y: capex end',round(m(0)-m(1)-m(2)),'D&A caption',round(m(0)-m(1)-m(3)-m(4)),'dep',round(m(0)-m(1)-m(3)))
