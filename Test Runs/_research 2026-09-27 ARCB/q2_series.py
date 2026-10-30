# ABF / Asset-Based segment series, figures as read from the filed segment tables and key-statistics tables
# (sources: segtab.txt, segtab2 output, orgrep.txt, units4.txt, EX-13 of 2003 and 2005 10-Ks)
import sys
sys.stdout.reconfigure(encoding='utf-8')
# year: (segment revenue $M, segment operating income $M, lbs per day)
D={2003:(1398.0,None,25963867),2004:(1585.4,None,28045219),2005:(1709.0,None,28259412),
2006:(1831.4,125.1,28749314),2007:(1770.7,84.5,27225100),2008:(1758.8,48.4,26086425),
2009:(1384.4,-168.5,23118590),2010:(1533.2,-58.3,25696634),2011:(1714.2,3.9,25383269),2012:(1701.5,-19.8,24193146),
2013:(1761.7,10.0,25065940),2014:(1928.5,50.1,26711015),2015:(1916.6,62.4,26318674),2016:(1916.4,33.6,25845741),
2017:(1993.3,57.9,25313938),2018:(2175.6,103.9,25294346),2019:(2144.7,102.1,24087269),2020:(2092.0,98.9,23998690),
2021:(2573.8,260.7,25824232),2022:(3010.9,381.1,26225019),2023:(2871.0,253.2,25606000),2024:(2750.1,242.6,21936000),2025:(2734.9,172.0,22208000)}
OR={2002:94.6,2003:94.3,2004:91.9,2005:90.9}
Y={2004:22.28,2005:23.90,2007:25.81,2008:26.70,2009:23.81,2010:23.68,2011:26.86,2012:28.03,2013:27.94,2014:28.74,2015:28.96,2016:29.35,
2017:31.27,2018:34.16,2019:35.44,2020:34.60,2021:39.70,2022:45.45,2023:44.46,2024:49.68,2025:49.02}
print('year  seg rev  seg OI  op margin  tons/day  $/cwt')
for y in sorted(D):
    r,o,l=D[y]
    m=('%.1f%%'%(100*o/r)) if o is not None else ('%.1f%% (OR %.1f%%)'%(100-OR[y],OR[y]))
    print(y, r, o, m, round(l/2000), Y.get(y,''))
# 2006 pounds per day derived: 2008 10-K says 2007 tonnage per day declined 5.3% from 2006 -> 27,225,100/0.947
# 2023-2025 tons/day read directly (12,803; 10,968; 11,104); lbs = tons*2000
import statistics as st
def mm(a,b): return [100*D[y][1]/D[y][0] for y in range(a,b+1) if D[y][1] is not None]
for a,b in [(2006,2008),(2009,2020),(2011,2020),(2021,2025),(2006,2025)]:
    v=mm(a,b); print('margin %d-%d: min %.1f max %.1f mean %.1f'%(a,b,min(v),max(v),st.mean(v)))
