import json
# TXRH filed traffic / check split (MD&A, each 10-K; FY2014-FY2025 from the DRI run's peer workpaper, FY2024-25 re-read in the
# FY2025 10-K) against BLS CPI-U Food Away From Home (CUUR0000SEFV), annual averages, fetched from api.bls.gov 2026-09-28.
T = {2014: (3.2, 1.5), 2015: (5.4, 1.8), 2016: (2.1, 1.4), 2017: (3.6, 0.9), 2018: (3.9, 1.5), 2019: (1.8, 2.9),
     2021: (27.6, 10.2), 2022: (1.9, 7.8), 2023: (5.4, 4.7), 2024: (4.4, 4.1), 2025: (2.8, 2.1)}
A = {}
for f in ['bls_fafh_2013_2022.json', 'bls_fafh_2020_2026.json']:
    for x in json.load(open(f))['Results']['series'][0]['data']:
        if x['period'] == 'M13': A[int(x['year'])] = float(x['value'])
print('FAFH annual averages', A)
print('FY  traffic  check  FAFH(yoy)  check-FAFH')
for y in sorted(T):
    f = (A[y] / A[y - 1] - 1) * 100
    print(y, T[y][0], T[y][1], round(f, 2), round(T[y][1] - f, 2))
def cum(ys, i):
    p = 1
    for y in ys: p *= 1 + T[y][i] / 100
    return (p - 1) * 100
for ys in [(2014, 2015, 2016, 2017, 2018, 2019), (2022, 2023, 2024, 2025), (2021, 2022, 2023, 2024, 2025)]:
    print(ys[0], '-', ys[-1], 'traffic %.1f%%  check %.1f%%  FAFH %d->%d %.1f%%' % (cum(ys, 0), cum(ys, 1), ys[0] - 1, ys[-1], (A[ys[-1]] / A[ys[0] - 1] - 1) * 100))
# menu price actions compounded (filed, each "approximately")
act = {'2022-25': [3.2, 2.9, 2.2, 2.7, 2.2, 0.9, 1.4, 1.7], '2021-25': [1.75, 4.2, 3.2, 2.9, 2.2, 2.7, 2.2, 0.9, 1.4, 1.7]}
for k, v in act.items():
    p = 1
    for a in v: p *= 1 + a / 100
    print('menu price actions', k, '%.1f%%' % ((p - 1) * 100))
# TXRH operating margin, every tagged year (companyfacts, OperatingIncomeLoss / revenue)
OI = {2009: 75.9, 2010: 90.6, 2011: 95.2, 2012: 110.5, 2013: 119.7, 2014: 130.4, 2015: 144.6, 2016: 171.9, 2017: 186.2, 2018: 187.8,
      2019: 212.0, 2020: 23.8, 2021: 297.2, 2022: 320.2, 2023: 354.0, 2024: 516.5, 2025: 474.7}
REV = {2009: 942.3, 2010: 1005.0, 2011: 1109.2, 2012: 1263.3, 2013: 1422.6, 2014: 1582.1, 2015: 1807.4, 2016: 1990.7, 2017: 2219.5,
       2018: 2457.4, 2019: 2756.2, 2020: 2398.1, 2021: 3463.9, 2022: 4014.9, 2023: 4631.7, 2024: 5373.3, 2025: 5878.1}
print('operating margin', {y: round(OI[y] / REV[y] * 100, 1) for y in OI})
