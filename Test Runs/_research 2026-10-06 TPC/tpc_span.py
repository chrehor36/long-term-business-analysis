"""Whole-span arithmetic for TPC from filed figures (USD millions). Sources: 10-K selected data and segment MD&A tables,
FY2012 (0001140361-13-009018), FY2014 (0000077543-15-000013), FY2016 (0000077543-17-000009), FY2018 (0000077543-19-000009),
FY2019 (0000077543-20-000008), FY2020 (0000077543-21-000020), FY2022 (0000077543-23-000023), FY2024 (0000077543-25-000025),
FY2025 (0000077543-26-000028); cash-flow lines from XBRL companyfacts (first-filed vintage). Segment income is pre-impairment."""
yrs = list(range(2013, 2026))
civ_r = [1441.4,1687.1,1889.9,1669.0,1602.2,1586.1,1779.4,2199.9,2095.8,1734.9,1883.9,2118.9,2846.8]
civ_i = [177.7,220.6,145.2,172.7,192.2,168.3,59.3,245.8,266.2,21.1,198.6,138.3,390.9]
bld_r = [1552.0,1503.8,1802.5,2069.8,1941.3,1861.7,1742.0,1984.6,1428.1,1242.6,1302.5,1617.6,1852.2]
bld_i = [24.5,24.7,-1.2,51.6,34.2,43.9,37.2,53.2,28.7,7.2,-91.2,-24.1,58.2]
spc_r = [1182.3,1301.3,1228.0,1234.3,1213.7,1006.9,929.4,1134.2,1118.0,813.3,693.8,590.4,844.0]
spc_i = [49.0,51.0,15.7,37.9,18.9,43.4,-16.4,17.2,-10.0,-168.0,-144.8,-103.3,-7.5]
oi    = [203.8,241.7,105.4,201.9,179.5,191.9,-365.0,262.3,226.8,-204.8,-114.6,-103.8,232.0]  # consolidated, after impairment
imp   = [0,0,0,0,0,0,379.9,0,0,0,0,0,0]
rev   = [a+b+c for a,b,c in zip(civ_r,bld_r,spc_r)]
print("year   rev    civ%   bld%   spc%   cons% (pre-imp)")
for i,y in enumerate(yrs):
    print(y, f"{rev[i]:7.1f} {100*civ_i[i]/civ_r[i]:6.1f} {100*bld_i[i]/bld_r[i]:6.1f} {100*spc_i[i]/spc_r[i]:6.1f} {100*(oi[i]+imp[i])/rev[i]:6.1f}")
S=sum
print("2013-2025 cumulative margins: civil %.1f%%  building %.1f%%  specialty %.1f%%  consolidated pre-imp %.1f%%  after imp %.1f%%" % (
 100*S(civ_i)/S(civ_r), 100*S(bld_i)/S(bld_r), 100*S(spc_i)/S(spc_r), 100*(S(oi)+S(imp))/S(rev), 100*S(oi)/S(rev)))
print("corporate+unallocated 2013-2025:", round(S(oi)+S(imp)-S(civ_i)-S(bld_i)-S(spc_i),1))
# cash lines 2010-2025 (XBRL first-filed vintage; 2015 OCF continuing-operations tag)
cy = list(range(2010,2026))
ocf = [26.3,-30.5,-67.9,50.7,-56.7,14.1,113.3,163.6,21.4,136.5,172.8,-148.5,207.0,308.5,503.5,748.1]
cap = [25.2,66.7,41.4,42.4,75.0,35.9,15.7,30.3,77.1,84.2,54.8,38.6,59.8,53.0,37.4,180.9]
sbc = [12.8,8.8,9.5,6.6,18.6,9.5,13.4,21.2,22.8,19.1,11.8,11.6,9.1,12.3,40.4,150.0]
sbc_cash = {2023:2.8, 2024:4.0, 2025:90.4}   # Note 10, 10-K FY2025: cash paid to settle liability awards (in OCF already)
nci = {2017:17.5,2018:29.0,2019:46.5,2020:48.5,2021:22.7,2022:47.4,2023:46.5,2024:23.3,2025:51.6}
dep = [21.4,32.2,40.6,43.4,40.2,37.9,63.8,48.4,43.7,58.8,74.9,82.7,49.8,43.0,51.6,47.6]
print("\nyear   OCF   capex   SBC  SBCcash  NCIdist  owner_cash")
oc = []
for i,y in enumerate(cy):
    v = ocf[i]-cap[i]-sbc[i]+sbc_cash.get(y,0)-nci.get(y,0)
    oc.append(v); print(y, f"{ocf[i]:7.1f} {cap[i]:6.1f} {sbc[i]:6.1f} {sbc_cash.get(y,0):6.1f} {nci.get(y,0):7.1f} {v:9.1f}")
def avg(a,b): 
    sel=[oc[cy.index(y)] for y in range(a,b+1)]; return sum(sel)/len(sel)
print("mean 2021-2025: %.1f  2016-2025: %.1f  2010-2025: %.1f" % (avg(2021,2025), avg(2016,2025), avg(2010,2025)))
print("cumulative 2010-2025: %.1f" % sum(oc))
# depreciation variant (D&A in place of capex)
od = [ocf[i]-dep[i]-sbc[i]+sbc_cash.get(y,0)-nci.get(y,0) for i,y in enumerate(cy)]
print("D&A-variant mean 2021-2025: %.1f  2010-2025: %.1f" % (sum(od[-5:])/5, sum(od)/len(od)))
