# owner earnings [E2-23]: OCF (face) less stock compensation (face add-back) less (c) at two ends:
#   capex end = "Additions to property and equipment" (face); depreciation end = face D&A less acquired-intangible amortization (face)
# $M. Sources: each year's 10-K cash-flow statement (FY2010-FY2026), read in k2012/k2015/k2018/k2021/k2023/k2026 and companyfacts.
ocf ={2010:111.26,2011:127.19,2012:126.75,2013:123.56,2014:136.76,2015:139.36,2016:144.16,2017:143.72,2018:170.37,2019:181.62,2020:205.22,2021:352.16,2022:325.30,2023:254.40,2024:298.98,2025:287.56,2026:292.07}
sbc ={2010:1.135,2011:1.138,2012:1.641,2013:1.864,2014:3.523,2015:5.957,2016:9.430,2017:14.631,2018:28.240,2019:32.280,2020:32.367,2021:48.982,2022:42.183,2023:39.230,2024:38.042,2025:40.833,2026:41.365}
cap ={2010:4.644,2011:3.630,2012:6.017,2013:22.454,2014:13.821,2015:19.905,2016:16.898,2017:15.179,2018:20.934,2019:25.411,2020:51.744,2021:44.301,2022:44.908,2023:38.244,2024:62.877,2025:31.006,2026:28.850}
da  ={2010:8.130,2011:8.700,2012:12.467,2013:12.321,2014:19.175,2015:37.226,2016:42.764,2017:60.036,2018:64.463,2019:78.171,2020:82.737,2021:87.747,2022:101.069,2023:107.238,2024:111.711,2025:109.903,2026:97.359}
am  ={2010:0.960,2011:1.465,2012:5.094,2013:5.061,2014:10.276,2015:26.169,2016:29.395,2017:44.393,2018:46.983,2019:58.550,2020:60.865,2021:64.239,2022:73.054,2023:76.413,2024:79.9,2025:76.0,2026:61.8}
CAP=11370.9; SOV=5.56
oe_c={y:ocf[y]-sbc[y]-cap[y] for y in ocf}; oe_d={y:ocf[y]-sbc[y]-(da[y]-am[y]) for y in ocf}
print('FY   OCF    SBC   capex  deprec  OEcap   OEdep  SBC%OCF')
for y in sorted(ocf): print(y, f'{ocf[y]:7.1f} {sbc[y]:6.1f} {cap[y]:6.1f} {da[y]-am[y]:6.1f} {oe_c[y]:7.1f} {oe_d[y]:7.1f} {100*sbc[y]/ocf[y]:5.1f}%')
def w(a,b):
    n=b-a+1; c=sum(oe_c[y] for y in range(a,b+1))/n; d=sum(oe_d[y] for y in range(a,b+1))/n; return c,d
print('\ntrailing windows ending FY2026, cap $%.1fM, sovereign %.2f%%'%(CAP,SOV))
for a in [2026,2025,2024,2023,2022,2020,2017,2012,2010]:
    c,d=w(a,2026); print(f'{2026-a+1:2d}y FY{a}-26: capex end {c:7.1f} ({100*c/CAP:4.2f}%)  deprec end {d:7.1f} ({100*d/CAP:4.2f}%)')
print('\nrolling five-year windows (capex end / deprec end)')
for b in range(2014,2027):
    c,d=w(b-4,b); print(f'FY{b-4}-{b}: {c:7.1f} / {d:7.1f}')
