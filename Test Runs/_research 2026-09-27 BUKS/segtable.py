# Segment revenue = total segment costs + segment operating income, both as filed in each year's 10-K MD&A segment table
# (seg_out.txt); FY2025-2026 read directly from the 10-K 2026 MD&A. $K.
D={2012:(34298,2928,14630,2558),2013:(34215,2987,15111,-1484),2014:(29204,1818,16146,103),2015:(29001,1794,16742,-475),
2016:(28187,1597,15985,-975),2017:(29227,1622,17892,1878),2018:(29562,1721,16575,402),2019:(30537,1480,22895,3798),
2020:(27018,1265,30547,7041),2021:(25159,5046,30421,854),2022:(29176,9971,28168,6158),2023:(29452,8589,37076,65),
2024:(29923,8717,35214,4522),2025:(29125,9142,38016,7685),2026:(29084,8296,40430,20157)}
print('| FY | casino revenue | casino op. income | margin | aerospace revenue | aerospace op. income | margin | aerospace share of segment op. income |')
print('|---|---|---|---|---|---|---|---|')
sa=sp=0
for y,(pc,po,ac,ao) in D.items():
    pr=pc+po; ar=ac+ao
    print(f'| {y} | {pr/1e3:.1f} | {po/1e3:.1f} | {po/pr:.1%} | {ar/1e3:.1f} | {ao/1e3:.1f} | {ao/ar:.1%} | {ao/(ao+po):.0%} |')
    sa+=ao; sp+=po
print('sum 2012-2026 aerospace OI',sa/1e3,'casino OI',sp/1e3)
import statistics
m=[D[y][3]/(D[y][2]+D[y][3]) for y in D]; print('aero margin mean %.1f%% median %.1f%% min %.1f%% max %.1f%%'%(100*statistics.mean(m),100*statistics.median(m),100*min(m),100*max(m)))
m2=[D[y][3]/(D[y][2]+D[y][3]) for y in D if y<=2024]; print('aero margin 2012-2024 mean %.1f%%'%(100*statistics.mean(m2)))
