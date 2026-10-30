import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
# same-vintage GM through downturns
rows=[("FY2009",5013.6,-38.3,28.5,42.4),("FY2012",8719,-17.1,38.0,41.5),("FY2013",7509,-13.9,39.8,38.0),("FY2019",14608,-12.6,43.7,45.0)]
for fy,rev,dr,gm,prev in rows:
    print(f"{fy} rev {rev:>9,.0f} {dr:+.1f}%   GM {prev:.1f} -> {gm:.1f}  = {gm-prev:+.1f} pts")
print()
# AGS profit mix
print("AGS share of revenue / gross profit / operating income")
for lab,rev,gp,oi,trev,tgp,toi in [("FY2023",5732,1821,1529,26517,12384,7654),
                                    ("FY2024",6225,2137,1812,27176,12897,7867),
                                    ("FY2025",6385,2134,1792,28368,13808,8289),
                                    ("9M FY2026 recast",5005,1748,1461,24037,11968,7429)]:
    print(f"  {lab:18s} rev {rev/trev*100:5.1f}%   GP {gp/tgp*100:5.1f}%   OI {oi/toi*100:5.1f}%")
print()
print("China decomposition")
ch=[("FY2017",2758,14698),("FY2018",5047,16705),("FY2019",4277,14608),("FY2020",5456,17202),
    ("FY2021",7535,23063),("FY2022",7254,25785),("FY2023",7247,26517),("FY2024",10117,27176),("FY2025",8529,28368)]
prev=None
for fy,c,t in ch:
    ex=t-c
    s=f"  {fy} China {c:6,} ({c/t*100:4.1f}%)  ex-China {ex:6,}"
    if prev: s+=f"   ChinaYoY {(c/prev[0]-1)*100:+6.1f}%  ex-ChinaYoY {(ex/prev[1]-1)*100:+6.1f}%"
    print(s); prev=(c,ex)
print()
print("Incremental return on NTOA [E2-56]/[E5-40]")
for lab,oi0,oi1,n0,n1 in [("FY2022->FY2025",7784,8470,15308,24367),("FY2019->FY2025",3350,8470,11622,24367),
                          ("FY2016->FY2025",2152,8470,7265,24367),("FY2013->FY2025",769,8470,5203,24367)]:
    print(f"  {lab}: dOI {oi1-oi0:+6,}  dNTOA {n1-n0:+7,}  incremental {(oi1-oi0)/(n1-n0)*100:6.1f}%")
