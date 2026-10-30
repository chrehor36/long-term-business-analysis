rev = {2015:919,2016:1656,2017:2562,2018:3652,2019:4805,2020:3378,2021:5992,2022:8399,2023:9917,2024:11102,2025:12241}
gbv = {2016:13925,2017:20975,2018:29441,2019:37963,2020:23897,2021:46877,2022:63212,2023:73252,2024:81784,2025:91273}
nights = {2016:125.7,2017:185.8,2018:250.3,2019:326.9,2020:193.2,2021:300.6,2022:394,2023:448,2024:492,2025:533}
for y in sorted(gbv):
    print(y, 'rev', rev[y], 'gbv', gbv[y], 'take %.2f%%' % (100*rev[y]/gbv[y]), 'nights', nights[y], 'GBV/night %.1f' % (gbv[y]/nights[y]), 'rev/night %.2f' % (rev[y]/nights[y]))
print('2020 vs 2019: nights %.1f%% gbv %.1f%% rev %.1f%%' % (100*(nights[2020]/nights[2019]-1),100*(gbv[2020]/gbv[2019]-1),100*(rev[2020]/rev[2019]-1)))
# 2025 cost structure
r=12241
for k,v in [('merchant fees and chargebacks',1666),('SBC',1592),('salaries',2009),('marketing',1704),('prof services',1218),('non-income taxes',305),('other',1203),('op income',2544),('interest income',705),('pretax',3137)]:
    print(k, v, '%.1f%% of revenue' % (100*v/r))
print('interest income share of pretax 2023-25: %.1f %.1f %.1f' % (100*721/2102, 100*818/3331, 100*705/3137))
print('H1 2026 take', 100*6286/56434, 'Q2 26', 100*3608/27247)
