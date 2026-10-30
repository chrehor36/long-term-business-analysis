# Owner earnings = filed OCF - SBC - (c); (c) at two ends: filed capex, and depreciation only (no amortization of acquired intangibles).
# $M. Sources: 10-K cash-flow statements (2015/2016/2017/2020/2022/2025 vintages) and depreciation notes; 2019-2022 depreciation = CF D&A less intangible amortization less equity-affiliate step-up amortization.
import sys
D={ # year: (OCF, SBC, capex, depreciation, note)
2013:(73.801,4.161,11.439,12.339,'Legacy Quaker'),
2014:(54.690,5.309,13.052,12.306,'Legacy Quaker'),
2015:(73.432,5.919,11.033,12.395,'Legacy Quaker'),
2016:(73.753,6.349,9.954,12.557,'Legacy Quaker'),
2017:(64.762,4.190,10.872,12.598,'Legacy Quaker'),
2018:(78.779,3.724,12.886,12.373,'Legacy Quaker'),
2019:(82.374,4.861,15.545,44.895-26.7-0.4,'Houghton from 1 Aug; approx dep'),
2020:(178.389,10.996,17.901,83.246-55.9-1.2,'COVID; WC release'),
2021:(48.933,11.038,21.457,86.550-59.9-1.2,'inflation; WC build'),
2022:(41.794,11.666,28.539,80.467-57.5-1.0,'inflation; WC build'),
2023:(279.020,14.605,38.800,23.8,'WC release'),
2024:(204.578,14.991,41.794,25.9,''),
2025:(136.453,13.611,55.856,30.4,'restructuring cash 26.6'),
}
CAP=163.45*17207702/1e6; SCREENCAP=2855.0
print('cap %.1f'%CAP)
print('| year | note | OCF | SBC | capex | dep | OE capex end | OE dep end |')
for y,(o,s,c,d,n) in D.items():
    print(f'| {y} | {n} | {o:,.1f} | {s:,.1f} | {c:,.1f} | {d:,.1f} | {o-s-c:,.1f} | {o-s-d:,.1f} |')
def win(a,b):
    ys=[y for y in D if a<=y<=b]
    ce=sum(D[y][0]-D[y][1]-D[y][2] for y in ys)/len(ys)
    de=sum(D[y][0]-D[y][1]-D[y][3] for y in ys)/len(ys)
    lo,hi=min(ce,de),max(ce,de)
    return lo,hi
print('windows ending 2025 (combined perimeter from 2020):')
for n in range(2,14):
    a=2026-n; lo,hi=win(a,2025)
    tag='' if a>=2020 else ' (spans pre-2020 perimeter)'
    print(f'  {n}y {a}-2025: {lo:,.1f} to {hi:,.1f}  yield {lo/CAP:.2%} to {hi/CAP:.2%}{tag}')
lo,hi=win(2014,2018); print('Legacy Quaker 2014-18: %.1f-%.1f'%(lo,hi))
# screen reproduction
for (a,b) in ((2023,2025),(2021,2025)):
    ys=range(a,b+1)
    for lab,fn in (('capex',lambda y:D[y][2]),('dep',lambda y:D[y][3])):
        v=sum(D[y][0]-D[y][1]-fn(y) for y in ys)/len(ys); print('screen check',a,b,lab,round(v,1),'on screen cap %.2f%%'%(100*v/SCREENCAP))
# D&A incl amortization as (c), 3y and 5y
DA={2021:86.550,2022:80.467,2023:81.987,2024:84.119,2025:93.453}
for (a,b) in ((2023,2025),(2021,2025)):
    v=sum(D[y][0]-D[y][1]-DA[y] for y in range(a,b+1))/(b-a+1); print('D&A-incl-amortization as (c)',a,b,round(v,1))
# OCF level shift
m1=sum(D[y][0] for y in (2017,2018,2019,2020,2021,2022))/6; m2=sum(D[y][0] for y in (2023,2024,2025))/3
print('OCF mean 2017-22 %.1f, 2023-25 %.1f, ratio %.2f'%(m1,m2,m2/m1))
print('OCF 2021-22 mean %.1f vs 2023-24 %.1f'%((48.933+41.794)/2,(279.02+204.578)/2))
