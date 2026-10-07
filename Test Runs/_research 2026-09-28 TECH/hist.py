# operating record from the filed selected-data tables (FY2000-FY2013) and companyfacts (FY2014-FY2026); $M
# FY2000-2008 operating margin % as printed in the 10-K five-year tables (k2004, k2008); FY2009-2013 from k2013's table
tab = {  # fy: (net sales $M, operating margin % as filed)
 2000:(103.838,37.9),2001:(115.357,40.0),2002:(130.900,26.8),2003:(145.011,46.7),2004:(161.257,51.0),
 2005:(178.652,54.7),2006:(202.617,53.6),2007:(223.482,55.6),2008:(257.420,56.1),
 2009:(263.956,57.1),2010:(269.047,58.1),2011:(289.962,56.2),2012:(314.560,52.8),2013:(310.575,51.0)}
cf = {2014:(357.8,159.8),2015:(452.2,147.0),2016:(499.0,150.6),2017:(563.0,120.6),2018:(643.0,136.2),2019:(714.0,146.7),
 2020:(738.7,157.4),2021:(931.0,237.3),2022:(1105.6,296.6),2023:(1136.7,298.9),2024:(1159.1,206.7),2025:(1219.6,102.3),2026:(1215.0,251.9)}
rows={}
for y,(r,m) in tab.items(): rows[y]=(r, r*m/100)
for y,(r,o) in cf.items(): rows[y]=(r,o)
for y in sorted(rows): r,o=rows[y]; print(y, f'{r:8.1f} {o:7.1f} {100*o/r:5.1f}%')
def cum(a,b):
    R=sum(rows[y][0] for y in range(a,b+1)); O=sum(rows[y][1] for y in range(a,b+1)); return R,O,100*O/R
for a,b in [(2000,2013),(2003,2013),(2014,2021),(2022,2026),(2014,2026),(2000,2026)]:
    R,O,m=cum(a,b); print(f'cum FY{a}-FY{b}: revenue {R:8.1f} op income {O:7.1f} margin {m:5.1f}%')
# segment operating income (excl. amortization, SBC, other unallocated), from each 10-K's segment note
seg = {2015:[('Biotechnology',325.897,171.059),('Clinical Controls',60.377,18.148),('Protein Platforms',66.247,4.469)],
       2018:[('Biotechnology',421.536,199.100),('Protein Platforms',111.885,17.996),('Diagnostics',110.108,28.280)],
       2017:[('Biotechnology',364.504,175.163),('Protein Platforms',91.464,9.648),('Diagnostics',107.139,28.575)],
       2016:[('Biotechnology',317.340,168.613),('Protein Platforms',77.324,3.592),('Diagnostics',104.484,30.412)],
       2019:[('Protein Sciences',543.159,240.919),('Diagnostics and Genomics',171.674,10.079)],
       2020:[('Protein Sciences',555.352,234.929),('Diagnostics and Genomics',184.549,14.965)],
       2021:[('Protein Sciences',704.564,328.837),('Diagnostics and Genomics',227.744,38.425)],
       2022:[('Protein Sciences',832.311,377.623),('Diagnostics and Genomics',274.843,48.977)],
       2023:[('Protein Sciences',845.747,373.684),('Diagnostics and Genomics',292.602,43.037)],
       2024:[('Protein Sciences',830.902,354.775),('Diagnostics and Genomics',326.392,24.546)],
       2025:[('Protein Sciences',870.245,370.353),('Diagnostics and Spatial Biology',346.263,21.324)],
       2026:[('Protein Sciences',874.620,359.401),('Diagnostics and Spatial Biology',336.365,37.698)]}
for y in sorted(seg):
    print(y, ' | '.join(f'{n} {r:.1f} / {o:.1f} = {100*o/r:.1f}%' for n,r,o in seg[y]))
