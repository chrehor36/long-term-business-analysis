"""CHFFF run: decade returns and owner cash from data_10y.csv (HK$'000), filed figures only.
Run: python -I calc_returns.py  (from this folder)."""
import csv, os
here = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(here, 'data_10y.csv'))))
# borrowings (current + non-current) and cash (cash + deposits > 3m + pledged), from the filed balance sheets
borrow = {2016: 21615649, 2017: 31454003, 2018: 38526167, 2019: 53179873, 2020: 74978910,
          2021: 99125664, 2022: 94724500, 2023: 94624144, 2024: 91669439, 2025: 88548513}
cash = {2016: 7037597, 2017: 10838364, 2018: 15974480, 2019: 12302988, 2020: 11706048,
        2021: 15604986, 2022: 11782743, 2023: 8632740, 2024: 8041996, 2025: 10524155}
debtors_gross = {2016: 1377070, 2017: 2342587, 2018: 2511537, 2019: 3699034, 2020: 6466852,
                 2021: 13772488, 2022: 16252797, 2023: 21388229}
debtors_net = {2023: 19980322, 2024: 21126596, 2025: 24152344}
over13 = {2016: 118201, 2017: 106493, 2018: 162432, 2019: 420826, 2020: 1032004, 2021: 2355773,
          2022: 5645921, 2023: 8950268, 2024: 9875977, 2025: 11631247}
print('year  rev   opprof  equity_tot  netdebt  ROCE_pretax  ROE_attrib  netdebt/eq  ownercash_AE  ownercash_EQ  debtors>13m')
oc = {}
for r in rows:
    y = int(r['year']); f = {k: float(v) for k, v in r.items() if k not in ('year', 'source')}
    eq_tot = f['equity_attrib'] + f['nci'] + f['perps']
    nd = borrow[y] - cash[y]
    ce = eq_tot + nd
    roce = f['op_profit'] / ce
    roe = f['attrib'] / f['equity_attrib']
    # owner cash, all-equity basis: operating cash (after tax, before interest paid; interest paid sits in financing)
    # less PP&E and intangible (concession) additions, less acquisitions net of cash acquired
    ae = f['ocf'] - f['ppe_capex'] - f['intangible_capex'] - f['acquisitions']
    # equity basis: less interest paid (incl. lease interest) and perpetual distributions
    eqb = ae - f['interest_paid'] - f['lease_interest'] - f['perp_dist']
    oc[y] = (ae, eqb)
    print(y, f"{f['revenue']/1e6:7.0f} {f['op_profit']/1e6:6.0f} {eq_tot/1e6:9.0f} {nd/1e6:8.0f}  {roce*100:6.1f}%  {roe*100:6.1f}%  {nd/eq_tot:5.2f}  {ae/1e6:9.0f}  {eqb/1e6:9.0f}  {over13[y]/1e6:7.0f}")
w = [2021, 2022, 2023, 2024, 2025]
print('5y avg owner cash all-equity 2021-25 (HK$m):', round(sum(oc[y][0] for y in w)/5/1e3), ' equity basis:', round(sum(oc[y][1] for y in w)/5/1e3))
w10 = list(range(2016, 2026))
print('10y avg owner cash all-equity 2016-25 (HK$m):', round(sum(oc[y][0] for y in w10)/10/1e3), ' equity basis:', round(sum(oc[y][1] for y in w10)/10/1e3))
print('halves: 2021-22 avg AE', round((oc[2021][0]+oc[2022][0])/2/1e3), ' 2024-25 avg AE', round((oc[2024][0]+oc[2025][0])/2/1e3))
