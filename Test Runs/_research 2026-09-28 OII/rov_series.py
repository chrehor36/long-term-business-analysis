# ROV series from the filed 10-K segment tables (see rov_tables.txt and the 10-K accessions in tenk_list.txt)
# ROV revenue: 'Remotely Operated Vehicles' segment revenue FY2007-FY2019 (10-Ks FY2009, FY2011, FY2013, FY2016, FY2019);
# FY2018-FY2025: Subsea Robotics revenue x filed 'ROV' % (10-Ks FY2020-FY2025). Overlap FY2019: 449,830 vs 583,652 x 77% = 449,412.
old = {2007:(531381,144242,72880,None,.87),2008:(625921,190343,79052,None,.82),2009:(649228,207683,86527,None,.79),2010:(662105,211725,91667,None,.75),
       2011:(755033,224705,94999,72920,None),2012:(853520,248972,102225,82126,None),2013:(981728,281973,108201,91618,None),
       2014:(1069022,320550,117882,98302,None),2015:(807723,192514,121944,83838,None),2016:(522121,25193,112588,59963,None),
       2017:(393655,22366,101951,47282,None),2018:(394801,1641,101464,52084,None),2019:(449830,1591,100480,58347,None)}
new = {2018:(513701,-46572,101464,52084,.77),2019:(583652,11627,100480,58347,.77),2020:(493332,-65817,91499,54411,.81),2021:(538515,76874,91242,53113,.79),
       2022:(621921,118248,91250,56231,.77),2023:(752521,174293,91250,61874,.77),2024:(829822,235211,91500,61382,.78),2025:(855216,257107,91250,59629,.78)}
print('FY  | ROV revenue $M | op income $M | op margin | days avail | days utilized | utilization | ROV revenue per day utilized $')
for y,(r,oi,da,du,u) in old.items():
    if du is None: du = round(da*u)
    print(f'{y} old | {r/1e3:,.1f} | {oi/1e3:,.1f} | {100*oi/r:.0f}% | {da:,} | {du:,}{"*" if u else ""} | {100*du/da:.0f}% | {r*1000/du:,.0f}')
for y,(r,oi,da,du,p) in new.items():
    rr = r*p
    print(f'{y} new | SR {r/1e3:,.1f}, ROV {p:.0%} = {rr/1e3:,.1f} | SR {oi/1e3:,.1f} | {100*oi/r:.0f}% | {da:,} | {du:,} | {100*du/da:.0f}% | {rr*1000/du:,.0f}')
print('* days utilized derived as utilization % x days available (2007-2010 tables give utilization, not days)')
