# Segment operating profit before equity income and impairments: gross profit - SG&A + other operating (R$ millions).
# 2021-2022 old four-segment basis (20-F FY2023 note 27); 2023-2025 new three-segment basis (20-F FY2025 note 27).
old = {  # brazil, na, sa, ss   (gross, sga, other) per segment
2021: [(12261.6,-781.9,137.6),(5421.4,-639.4,42.1),(1523.9,-157.9,27.5),(1553.0,-233.3,71.3)],
2022: [(5888.1,-819.8,31.2),(8404.8,-628.9,-14.9),(1647.5,-154.8,8.3),(2440.5,-266.1,12.9)],
2023: [(2658.5,-868.5,-50.7),(5795.4,-629.9,-12.9),(1104.1,-137.2,34.6),(1697.5,-281.3,-26.4)],
}
new = {
2023: [(3602.0,-986.4,-91.5),(6549.5,-793.2,1.6),(1104.1,-137.2,34.6)],
2024: [(3898.5,-939.3,-145.5),(4496.5,-808.8,36.3),(828.0,-177.2,12.5)],
2025: [(1880.9,-952.2,-61.6),(5487.5,-792.2,14.6),(597.4,-167.6,12.8)],
}
op = lambda t: sum(t)
o23 = [op(x) for x in old[2023]]; n23 = [op(x) for x in new[2023]]
ss_to_br = (n23[0]-o23[0]) / o23[3]; ss_to_na = (n23[1]-o23[1]) / o23[3]
print("2023 old", [round(x) for x in o23], "new", [round(x) for x in n23], "SS split to BR %.3f NA %.3f" % (ss_to_br, ss_to_na))
tot = {"Brazil":0,"North America":0,"South America":0}
for y in (2021,2022):
    b,n,s,ss = [op(x) for x in old[y]]
    tot["Brazil"] += b + ss*ss_to_br; tot["North America"] += n + ss*ss_to_na; tot["South America"] += s
    print(y, "BR %.0f NA %.0f SA %.0f SS %.0f" % (b,n,s,ss))
for y in (2023,2024,2025):
    b,n,s = [op(x) for x in new[y]]
    tot["Brazil"] += b; tot["North America"] += n; tot["South America"] += s
    print(y, "BR %.0f NA %.0f SA %.0f" % (b,n,s))
T = sum(tot.values())
for k,v in tot.items(): print(f"{k}: {v:,.0f}  {100*v/T:.1f}%")
# NA margins (old basis to 2022, new basis from 2023)
na = {2015:(1511.9-814.4+18.4,17312.2),2016:(916.0-778.2+26.2,15430.8),2017:(609.8-569.7+29.1,15433.4),2018:(1762.6-607.6+19.1,19927.4),
      2019:(1304.8-444.3+44.7,14656.0),2020:(1245.6-476.5+97.8,17458.3),2021:(op(old[2021][1]),27838.0),2022:(op(old[2022][1]),31098.9),
      2023:(op(new[2023][1]),33179.0),2024:(op(new[2024][1]),31931.4),2025:(op(new[2025][1]),35787.3)}
br = {2023:(op(new[2023][0]),31195.6),2024:(op(new[2024][0]),30217.8),2025:(op(new[2025][0]),29688.0)}
for y,(p,s) in na.items(): print("NA",y,f"{p:,.0f} / {s:,.0f} = {100*p/s:.1f}%")
for y,(p,s) in br.items(): print("BR",y,f"{p:,.0f} / {s:,.0f} = {100*p/s:.1f}%")
