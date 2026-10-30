"""CHFFF run, Q2: parts table and the field's returns, filed figures only (HK$'000 for CEEG, RMB'000 for Dynagreen).
Segment figures from note 4 of each Annual Report; each year taken from the latest report that prints it
(2021 from AR2022's comparative, 2022 from AR2023's comparative, 2023 from AR2024's comparative, 2024 and 2025 from AR2025).
Run: python -I calc_q2.py"""
# year: (energy EBITDA, energy D&A, energy segment assets, total EBITDA, total D&A)
seg = {
    2021: (10225664, 651283, 114462032, 16555785, 1579481),   # AR2022 note 4 comparative (restated)
    2022: (9056301, 822393, 110305556, 13731572, 2079585),    # AR2023 note 4 comparative
    2023: (9078517, 902936, 107527318, 13194089, 2161659),    # AR2024 note 4 comparative
    2024: (6886316, 994252, 105640806, 10001525, 2186379),    # AR2025 note 4 comparative
    2025: (7109768, 1034983, 107199602, 10640015, 2218332),   # AR2025 note 4
}
se = st = 0
print('year  energy EBIT  total EBIT  energy share  energy EBIT / energy segment assets (pre-tax, pre-interest)')
for y, (e, ed, ea, t, td) in seg.items():
    eb, tb = e - ed, t - td
    se += eb; st += tb
    print(y, f"{eb/1e6:8.2f}bn {tb/1e6:8.2f}bn  {eb/tb*100:5.1f}%   {eb/ea*100:5.1f}%")
print(f"five-year energy share of segment profit after D&A: {se/st*100:.1f}%")
# Dynagreen (HKEX 01330 / SSE 601330), Five-Year Operations Highlights, AR2020 (2016-2020) and AR2025 (2021-2025), RMB'000
dyn = {2016: (218511, 5629834, 3515887), 2017: (239881, 6864526, 4579183), 2018: (365651, 10689006, 7616409),
       2019: (416088, 13670787, 10174272), 2020: (503385, 17446071, 11665793), 2021: (697786, 20214466, 13296885),
       2022: (744767, 22677440, 14864161), 2023: (629281, 22537266, 14263309), 2024: (585082, 21988773, 13459983),
       2025: (617501, 21926734, 13254406)}
print('Dynagreen: year  attributable profit / total equity (incl. NCI)   / total assets')
for y, (p, a, l) in dyn.items():
    print(y, f"{p/(a-l)*100:5.1f}%  {p/a*100:4.1f}%")
# CEEG on Dynagreen's basis: attributable profit / total equity (attributable + NCI + perpetual capital instruments)
import csv, os
here = os.path.dirname(os.path.abspath(__file__))
print('CEEG: year  attributable profit / total equity')
for r in csv.DictReader(open(os.path.join(here, 'data_10y.csv'))):
    te = float(r['equity_attrib']) + float(r['nci']) + float(r['perps'])
    print(r['year'], f"{float(r['attrib'])/te*100:5.1f}%")
