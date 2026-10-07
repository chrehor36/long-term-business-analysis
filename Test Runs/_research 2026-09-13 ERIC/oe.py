# Owner earnings, SEK million, from filed cash-flow statements and notes (sources in q4.md).
import json
Y = list(range(2011, 2026))
OCF = dict(zip(Y, [9982,22031,17389,18702,20597,14010,9601,9342,16873,28933,39065,30863,7177,46261,32954]))
CAPEX = dict(zip(Y, [4994,5429,4503,5322,8338,6129,3877,3975,5118,4493,3663,4477,3297,2340,2630]))
PPE_SALES = dict(zip(Y, [386,568,378,522,1301,482,1016,334,744,254,115,249,163,116,192]))
CAPDEV = dict(zip(Y, [1515,1641,915,1523,3302,4483,1444,925,1545,817,962,1720,2173,1300,1138]))
LEASE = dict(zip(Y, [0,0,0,0,0,0,0,0,2990,2417,2368,2593,2857,2492,2115]))
DEP = dict(zip(Y, [3499,4052,4227,4329,4705,4421,4103,3275,3587,3602,3674,4114,4272,3861,3247]))
CAPDEV_AM = dict(zip(Y, [995,1058,1407,1270,1379,1815,2681,2559,1519,906,1343,1586,1137,1480,1790]))
ACQ_AM = dict(zip(Y, [4470,4436,4521,4328,4139,2650,1667,1387,1019,1083,1164,1991,3321,2500,1821]))
SBC = dict(zip(Y, [413,405,388,717,865,957,885.4,677.5,375.4,148.6,93,89,82,93,175]))
ACQ = dict(zip(Y, [3181,11529,3147,4442,2201,984,289,1618,1753,9657,389,51995,1515,397,1099]))
DIV = dict(zip(Y, [53,9452,465,48,1,362,565,333,248,59,448,307,-625,86,11638]))
SALES = dict(zip(Y, [226921,227779,227376,227983,246920,222608,205378,210838,227216,232390,232314,271546,263351,247880,236681]))
rows = {}
for y in Y:
    base = OCF[y] - SBC[y] - LEASE[y]
    oe_cx = base - CAPEX[y] - CAPDEV[y]
    oe_da = base - DEP[y] - CAPDEV_AM[y]
    oe_net = base - (CAPEX[y] - PPE_SALES[y]) - CAPDEV[y]
    after_ma = oe_cx - ACQ[y] + DIV[y]
    rows[y] = dict(ocf=OCF[y], sbc=SBC[y], lease=LEASE[y], capex=CAPEX[y], capdev=CAPDEV[y], dep=DEP[y], capdev_am=CAPDEV_AM[y],
                   oe_capex=round(oe_cx), oe_da=round(oe_da), oe_capex_net_sales=round(oe_net), after_ma=round(after_ma),
                   cx_over_da=round((CAPEX[y]+CAPDEV[y])/(DEP[y]+CAPDEV_AM[y]),2), sales=SALES[y])
    print(y, rows[y])
def mean(k, a, b):
    v = [rows[y][k] for y in range(a, b+1)]; return round(sum(v)/len(v))
W = {'3y 2023-25': (2023,2025), '5y 2021-25': (2021,2025), '5y 2016-20': (2016,2020), '10y 2016-25': (2016,2025), '15y 2011-25': (2011,2025), '5y 2011-15': (2011,2015)}
out = {}
for n,(a,b) in W.items():
    out[n] = {k: mean(k,a,b) for k in ('oe_capex','oe_da','oe_capex_net_sales','after_ma','ocf','sales')}
    out[n]['cx_da'] = round(sum(CAPEX[y]+CAPDEV[y] for y in range(a,b+1))/sum(DEP[y]+CAPDEV_AM[y] for y in range(a,b+1)),2)
    print(n, out[n])
json.dump({'rows': rows, 'windows': out}, open('oe_out.json','w'), indent=1)
