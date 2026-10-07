# ICEE gallons (the 10-K sentence each year, base ICEE business) and Frozen Beverages 'Beverages' revenue line ($M) from the segment note
gal={2011:0,2012:0,2013:-4,2014:-1,2015:7,2016:6,2017:6,2018:6,2019:3,2020:-41,2021:16,2022:39,2023:10,2024:-3,2025:-4}
bev={2011:133.372,2012:135.436,2013:132.274,2014:133.283,2015:142.705,2016:150.118,2017:154.157,2018:160.937,2019:171.820,2020:107.004,2021:124.498,2022:184.063,2023:224.655,2024:230.030,2025:219.312}
# Frozen Beverages segment operating income and identifiable assets ($M) from each 10-K segment note (old structure to FY2022 includes allocated corporate; FY2023-25 new structure before corporate)
fb={2009:(14.536,129.282),2010:(15.661,139.978),2011:(18.582,141.310),2012:(21.881,143.437),2013:(22.903,153.579),2014:(21.916,161.940),2015:(24.582,171.609),2016:(26.653,178.543),2017:(26.272,210.390),2018:(28.415,217.549),2019:(29.950,223.889),2020:(-12.466,286.816),2021:(6.132,291.584),2022:(33.800,303.619),2023:(51.843,339.486),2024:(52.996,358.892),2025:(49.529,364.473)}
idx=100.0
print('FY   gallons%  gal_index(FY2012=100)  beverages$M  rev/gal index  FB OI  FB assets  OI/assets')
for y in range(2009,2026):
    if y in gal and y>2012: idx*=1+gal[y]/100
    g=idx if y>=2012 else None
    rpg=(bev[y]/bev[2012])/(idx/100)*100 if y>=2012 else None
    oi,a=fb[y]
    print(y, gal.get(y,''), ('%.1f'%g) if g else '', bev.get(y,''), ('%.1f'%rpg) if rpg else '', '%.1f'%oi, '%.1f'%a, '%.1f%%'%(100*oi/a))
