# Long series for Q2: revenue, gross margin, operating (or pre-tax) margin, pre-tax return on average equity,
# real revenue, store count. Sources: five-year selected-data tables of the FY2001, FY2005, FY2009 10-Ks
# (FY1997-FY2008), XBRL checked to the filed FY2025 statements (FY2009-FY2025), MD&A store tables.
import json
cpi = json.load(open('cpi_annual.json'))
# (revenue, gross profit, margin line $, which line, equity at year end) in $ thousands
old = {
 1997: (984367, 376446, None, 'op 7.5%', 193198),
 1998: (1160909, 450208, None, 'op 7.9%', 302030),
 1999: (1460000, 567027, None, 'op 7.5%', 383309),
 2000: (1829483, 693628, None, 'op 5.4%', 427458),
 2001: (2086662, 793989, 122106, 'pretax', 532531),
 2002: (2360830, 951601, 202282, 'pretax', 643978),
 2003: (2754368, 1110577, 255638, 'pretax', 804591),
 2004: (3136931, 1271145, 310205, 'pretax', 957662),
 2005: (3538947, 1435482, 348798, 'pretax', 1125318),
 2006: (3727513, 1487287, 337186, 'pretax', 1151431),
 2007: (3944934, 1535971, 316340, 'pretax', 1165723),
 2008: (3361472, 1135172, 41953, 'pretax', 1147984),
}
x = json.load(open('xbrl_series.json'))
def g(t, k):
    v = x.get(t, {}).get(k); return v[0] if v else None
ends = {2009: '2010-01-31', 2010: '2011-01-30', 2011: '2012-01-29', 2012: '2013-02-03', 2013: '2014-02-02',
        2014: '2015-02-01', 2015: '2016-01-31', 2016: '2017-01-29', 2017: '2018-01-28', 2018: '2019-02-03',
        2019: '2020-02-02', 2020: '2021-01-31', 2021: '2022-01-30', 2022: '2023-01-29', 2023: '2024-01-28',
        2024: '2025-02-02', 2025: '2026-02-01'}
eq_end = {y: v[4] / 1e3 for y, v in old.items()}
stores = {1997: 276, 1998: 298, 1999: 344, 2000: 382, 2001: 415, 2002: 478, 2003: 512, 2004: 552, 2005: 570,
          2006: 588, 2007: 600, 2008: 627, 2009: 610, 2010: 592, 2011: 576, 2012: 581, 2013: 585, 2014: 601,
          2015: 618, 2016: 629, 2017: 631, 2018: 625, 2019: 614, 2020: 581, 2021: 544, 2022: 530, 2023: 518,
          2024: 512, 2025: 506}
rows = []
for y in range(1997, 2026):
    if y in old:
        rev, gp, line, kind, eq = old[y]; rev /= 1e3; gp /= 1e3
        if line: m = line / 1e3; mpct = 100 * m / rev
        else: mpct = float(kind.split()[1].rstrip('%')); m = rev * mpct / 100
        eq /= 1e3
    else:
        k = ends[y]
        rev = (g('RevenueFromContractWithCustomerExcludingAssessedTax', k) or g('SalesRevenueNet', k)) / 1e6
        gp = g('GrossProfit', k) / 1e6; m = g('OperatingIncomeLoss', k) / 1e6; mpct = 100 * m / rev
        kind = 'op'; eq = g('StockholdersEquity', k) / 1e6
    eq_end[y] = eq
    avg = (eq + eq_end[y - 1]) / 2 if (y - 1) in eq_end else None
    real = rev * cpi['2025'] / cpi[str(y)]
    rows.append((y, rev, 100 * gp / rev, m, mpct, kind, (100 * m / avg) if avg else None, real, stores.get(y)))
print('FY   revenue   GM%   margin$   margin%  basis   pretax/avgEq  real rev (2025$)  stores')
for r in rows:
    print(f'{r[0]} {r[1]:9.1f} {r[2]:5.1f} {r[3]:8.1f} {r[4]:6.1f}  {r[5]:7s} {"" if r[6] is None else f"{r[6]:6.1f}%":>10}  {r[7]:9.1f}  {r[8]}')
def agg(a, b):
    R = sum(r[1] for r in rows if a <= r[0] <= b); M = sum(r[3] for r in rows if a <= r[0] <= b)
    return 100 * M / R
for a, b in [(1997, 2019), (1997, 2007), (2010, 2019), (2015, 2019), (2020, 2025), (2023, 2025)]:
    print(f'aggregate margin {a}-{b}: {agg(a, b):.1f}%')
json.dump(rows, open('longtable.json', 'w'))
