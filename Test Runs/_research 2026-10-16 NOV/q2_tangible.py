# NOV pre-tax pre-interest earnings with every goodwill, intangible and long-lived impairment added back,
# against tangible capital (equity + debt - cash - goodwill - intangibles). XBRL first-filed values, USD millions.
ebit = {2014:3599,2015:-486,2016:-2518,2017:-290,2018:134,2019:-6362,2020:-2695,2021:-153,2022:316,2023:700,2024:922,2025:463}
gw   = {2015:1485,2016:972,2019:3509,2020:1295,2025:40}
ll   = {2014:104,2015:204,2016:54,2017:10,2018:21,2019:2209+56,2020:513+42,2022:114,2023:51,2024:109,2025:30}
tc   = {2014:7339,2015:7404,2016:6149,2017:5841,2018:5819,2019:4937,2020:3332,2021:3089,2022:3762,2023:5065,2024:4748,2025:4397}
rev  = {2014:21440,2015:14757,2016:7251,2017:7304,2018:8453,2019:8479,2020:6090,2021:5524,2022:7237,2023:8583,2024:8870,2025:8744}
print('year  EBIT  +gw  +ll  adj  tangcap  adj/tc  adj/rev')
for y in sorted(ebit):
    a = ebit[y]+gw.get(y,0)+ll.get(y,0)
    print(y, ebit[y], gw.get(y,0), ll.get(y,0), a, tc[y], f'{100*a/tc[y]:.1f}%', f'{100*a/rev[y]:.1f}%')
for a_,b_ in [(2014,2024),(2015,2024),(2015,2025),(2022,2025)]:
    ys=[y for y in ebit if a_<=y<=b_]
    A=sum(ebit[y]+gw.get(y,0)+ll.get(y,0) for y in ys); T=sum(tc[y] for y in ys); R=sum(rev[y] for y in ys)
    print(f'{a_}-{b_}: adj EBIT {A} / tangible capital-years {T} = {100*A/T:.1f}%  ; margin {100*A/R:.1f}%')
