# Owner earnings = operating cash flow (continuing) - stock compensation in full - (c); (c) at the capex end and at the depreciation end.
# Face lines: "Net cash flows provided by operating activities (of continuing operations)", "Incentive stock compensation", "Capital expenditures",
# depreciation from the segment note ("Depreciation expense"). No net-income proxy anywhere.
Y=[2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
ocf={2016:-38.0,2017:-34.3,2018:-0.8,2019:170.9,2020:276.0,2021:326.0,2022:295.9,2023:333.6,2024:362.0,2025:289.8}
sbc={2016:7.3,2017:11.8,2018:15.4,2019:11.8,2020:6.0,2021:40.1,2022:17.7,2023:9.4,2024:14.8,2025:59.1}
cap={2016:32.6,2017:30.8,2018:28.4,2019:29.7,2020:28.8,2021:46.3,2022:47.8,2023:52.7,2024:68.4,2025:62.2}
dep={2016:46.6,2017:46.4,2018:44.6,2019:41.5,2020:42.2,2021:39.7,2022:41.6,2023:42.6,2024:40.0,2025:41.1}
# TTM to 2026-06-30 = FY2025 + H1 2026 - H1 2025 (10-Q 0001590714-26-000065)
ttm=dict(ocf=289.8+33.0-98.6, sbc=59.1+20.7-11.3, cap=62.2+53.0-28.7, dep=41.1+29.7-19.7)
CAP=35.12*243690914/1e6
oe_c={y:ocf[y]-sbc[y]-cap[y] for y in Y}; oe_d={y:ocf[y]-sbc[y]-dep[y] for y in Y}
print('FY | OCF | SBC | capex | depreciation | OE capex end | OE depreciation end')
for y in Y: print(f"{y}{' (excluded: Platform debt)' if y<2019 else ''} | {ocf[y]:.1f} | {sbc[y]:.1f} | {cap[y]:.1f} | {dep[y]:.1f} | {oe_c[y]:.1f} | {oe_d[y]:.1f}")
tc=ttm['ocf']-ttm['sbc']-ttm['cap']; td=ttm['ocf']-ttm['sbc']-ttm['dep']
print(f"TTM 2026-06 | {ttm['ocf']:.1f} | {ttm['sbc']:.1f} | {ttm['cap']:.1f} | {ttm['dep']:.1f} | {tc:.1f} | {td:.1f}")
print(f'\ncap {CAP:.1f}; trailing windows ending FY2025 (priced perimeter FY2019-FY2025)')
for n in range(1,8):
    ys=list(range(2026-n,2026)); c=sum(oe_c[y] for y in ys)/n; d=sum(oe_d[y] for y in ys)/n
    print(f"{n}y {ys[0]}-{ys[-1]}: capex end {c:.1f} ({100*c/CAP:.2f}%) | dep end {d:.1f} ({100*d/CAP:.2f}%)")
print(f"TTM: capex end {tc:.1f} ({100*tc/CAP:.2f}%) | dep end {td:.1f} ({100*td/CAP:.2f}%)")
ex19={y:oe_c[y] for y in range(2020,2026)}
print('\nrolling 3-year windows (capex / dep):')
for s in range(2019,2024):
    ys=range(s,s+3); print(f"{s}-{s+2}: {sum(oe_c[y] for y in ys)/3:.1f} / {sum(oe_d[y] for y in ys)/3:.1f}")
acq={2019:63.9,2020:9.0,2021:536.5,2022:22.6,2023:214.8,2024:3.9,2025:0.0}
print('\nFY2019-FY2025 sums: OE capex end', round(sum(oe_c[y] for y in range(2019,2026)),1), 'OE dep end', round(sum(oe_d[y] for y in range(2019,2026)),1),
      'acquisitions', round(sum(acq.values()),1), 'Graphics sale 321.2; H1 2026 acquisitions 865.8')
