"""Sales growth for the MDT competitor row, from the row.py outputs' figures (companyfacts, as filed) and the
segment figures read from 10-K text. Arithmetic only."""
import math
S = {  # name: (start_label, start, end_label, end, 5y_start_label, 5y_start)
 'MDT as filed':            ('FY2017 (Apr-17)', 29710, 'FY2026 (Apr-26)', 36364, 'FY2021', 30117),
 'MDT ex-Cardinal divestiture (FY2017 less $2.4bn)': ('FY2017', 29710-2400, 'FY2026', 36364, 'FY2021', 30117),
 'SYK':  ('2016', 11325, '2025', 25116, '2020', 14351),
 'BSX':  ('2016', 8386, '2025', 20074, '2020', 9913),
 'ISRG': ('2016', 2706, '2025', 10065, '2020', 4358),
 'EW':   ('2016', 2964, '2025', 6068, '2020', 4386),
 'ZBH':  ('2016', 7668, '2025', 8232, '2020', 6128),
 'BDX':  ('FY2016 (Sep)', 12483, 'FY2025', 21840, 'FY2020', 16074),
 'SNN':  ('2016', 4669, '2025', 6164, '2020', 4560),
 'PHG (EUR)': ('2016', 17422, '2025', 17834, '2020', 17313),
 'GMED': ('2016', 564, '2025', 2939, '2020', 789),
 'DXCM': ('2016', 573, '2025', 4662, '2020', 1927),
 'ABT consolidated': ('2016', 20853, '2025', 44328, '2020', 34608),
}
for k, (a, x, b, y, c, z) in S.items():
    n = 9
    g = (y / x) ** (1 / n) - 1
    g5 = (y / z) ** (1 / 5) - 1
    print(f'{k}: {a} {x:,} -> {b} {y:,}: {y/x-1:+.1%} total, {g:.1%}/yr over 9y; 5y from {c} {z:,}: {g5:.1%}/yr')
# JNJ MedTech segment (10-K text): 2015 $25.1bn -> 2025 $33.8bn, 10 years
print(f'JNJ MedTech segment: 2015 25.1bn -> 2025 33.8bn: {33.8/25.1-1:+.1%}, {(33.8/25.1)**0.1-1:.1%}/yr over 10y')
# ABT Medical Devices segment (10-K 2025 segment note): 2023 16,887 -> 2025 21,387
print(f'ABT Medical Devices segment: 2023 16,887 -> 2025 21,387: {(21387/16887)**0.5-1:.1%}/yr over 2y; segment operating earnings margin 2023 {5306/16887:.1%}, 2024 {6153/18986:.1%}, 2025 {7212/21387:.1%}')
print(f'JNJ MedTech segment income before tax / sales: 2024 {3740/31857:.1%}, 2025 {4113/33792:.1%}')
# MDT segment EBITA / operating profit series (10-K segment notes, basis before corporate, SBC and centralized distribution)
seg = {'FY2016': (10697, 28833), 'FY2017': (11126, 29710), 'FY2018': (11498, 29953), 'FY2019': (11852, 30557), 'FY2020': (10224, 28913),
       'FY2021': (10632, 30117), 'FY2022': (12432, 31686), 'FY2023 (as first filed)': (11286, 31227), 'FY2023 (recast, 2025 10-K)': (11664, None),
       'FY2024 (2025 10-K)': (11979, None), 'FY2025 (2025 10-K)': (12518, 33489)}
for k, (p, s) in seg.items():
    print(k, f'{p:,}', f'{p/s:.1%}' if s else '')
print(f'MDT segment profit FY2016 -> FY2025: {12518/10697-1:+.1%}, {(12518/10697)**(1/9)-1:.1%}/yr')
print(f'MDT operating profit as filed FY2016 5,361 -> FY2026 6,467: {6467/5361-1:+.1%}, {(6467/5361)**0.1-1:.1%}/yr')
