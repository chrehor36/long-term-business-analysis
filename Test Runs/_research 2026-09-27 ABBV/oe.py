"""ABBV owner earnings, COMPUTATION - NOT A CLEARANCE (Q2 closed OUT; nothing here is entry language).
Figures typed from the filed cash-flow statements: 2023-2025 10-K 2025 (0001551152-26-000008); 2022 10-K 2024
(0001551152-25-000020); 2019-2021 10-K 2021 (0001551152-22-000007); 2016-2018 10-K 2018 (0001551152-19-000008);
2013-2015 10-K 2015 (0001047469-16-010239); 2010-2012 10-K 2012 (0001047469-13-002827, Abbott carve-out, MARKED, never pooled).
OCF less SBC in full [E5-06] less (c) at two ends [E2-23, E3-44]: capex end, and depreciation end (depreciation only;
amortization of acquired intangibles is not maintenance). Both ends ALSO less the contingent-consideration payments the filer
classes in FINANCING (royalty-type payments on the bought risankizumab rights; the excess over acquisition-date fair value is
already inside OCF), because they are a cost of the product's sales. No net-income proxy anywhere (operator rule 5).
Acquisitions = 'Acquisition of businesses, net of cash acquired' + 'Other acquisitions and investments' (investing)."""
CAP = 264.34 * 1767117285 / 1e6
# year: OCF, SBC, capex, dep, amort, acq_business_cash, other_acq, cc_financing, dividends, buybacks, perimeter
D = {
2010: (4976, 167, 448, 476, 708, 2621, 0, 0, None, None, 'Abbott carve-out'),
2011: (6247, 163, 356, 508, 764, 273, 0, 0, None, None, 'Abbott carve-out'),
2012: (6345, 187, 333, 525, 625, 688, 0, 0, None, None, 'Abbott carve-out'),
2013: (6267, 212, 491, 388, 509, 0, 405, 0, 2555, 320, 'pre-Allergan'),
2014: (3549, 241, 612, 383, 403, 0, 622, 0, 2661, 652, 'pre-Allergan; OCF after the $1.6bn Shire break fee'),
2015: (7535, 282, 532, 417, 419, 11488, 964, 0, 3294, 7567, 'pre-Allergan; Pharmacyclics'),
2016: (7041, 396, 479, 425, 764, 2495, 262, 0, 3717, 6033, 'pre-Allergan; SBC the expense tag 396 > CF line 353'),
2017: (9960, 365, 529, 425, 1076, 0, 308, 268, 4107, 1410, 'pre-Allergan'),
2018: (13427, 421, 638, 471, 1294, 0, 736, 78, 5580, 12014, 'pre-Allergan'),
2019: (13324, 430, 552, 464, 1553, 0, 1135, 163, 6366, 629, 'pre-Allergan'),
2020: (17588, 753, 798, 666, 5805, 38260, 1350, 321, 7716, 978, 'Allergan from 2020-05-08'),
2021: (22777, 692, 787, 803, 7718, 525, 1377, 698, 9261, 934, 'with Allergan'),
2022: (24943, 671, 695, 778, 7689, 255, 539, 1132, 10043, 1487, 'with Allergan'),
2023: (22839, 747, 777, 752, 7946, 0, 1223, 752, 10539, 1972, 'with Allergan; Humira US LOE 2023-01-31'),
2024: (18806, 911, 974, 764, 7622, 17493, 3024, 0, 11025, 1708, 'with Allergan; ImmunoGen, Cerevel'),
2025: (19030, 955, 1214, 762, 7377, 204, 5237, 0, 11657, 980, 'with Allergan'),
}
def oe(y):
    o,s,c,d,a,ab,oa,cc = D[y][:8]
    return o-s-c-cc, o-s-d-cc, ab+oa
print('cap $%.1fM (264.34 x 1,767,117,285)' % CAP)
print('| year | perimeter | OCF | SBC | capex | dep | CC in financing | acquisitions (business + other) | OE capex end | OE dep end | OE capex end less acquisitions |')
print('|---|---|---|---|---|---|---|---|---|---|---|')
for y in D:
    ce, de, aq = oe(y)
    o,s,c,d,a,ab,oa,cc = D[y][:8]
    print(f'| {y} | {D[y][10]} | {o:,} | {s} | {c:,} | {d} | {cc} | {aq:,} | {ce:,} | {de:,} | {ce-aq:,} |')
lo, hi = 1e18, -1e18; rows = []
for n in range(3, 14):
    ys = list(range(2026 - n, 2026))
    m = lambda f: sum(f(y) for y in ys) / n
    ce = m(lambda y: oe(y)[0]); de = m(lambda y: oe(y)[1]); aq = m(lambda y: oe(y)[2])
    lo = min(lo, ce, de); hi = max(hi, ce, de)
    tag = 'post-Allergan only' if ys[0] >= 2021 else ('spans Allergan' if ys[0] >= 2013 else '')
    print(f'{n:>2}y {ys[0]}-2025 ({tag}): capex end {ce:,.0f} ({ce/CAP:.2%}) | dep end {de:,.0f} ({de/CAP:.2%}) | mean acquisitions {aq:,.0f} | less acquisitions {min(ce,de)-aq:,.0f} to {max(ce,de)-aq:,.0f} ({(min(ce,de)-aq)/CAP:.2%} to {(max(ce,de)-aq)/CAP:.2%})')
print(f'COMBINED registrant range, every window 3-13 years, both ends: {lo:,.0f} to {hi:,.0f} = {lo/CAP:.2%} to {hi/CAP:.2%}')
# TTM to 2026-06-30: H1 2026 OCF 7,265 SBC 610 capex 587 dep 382 acq 1,090; H1 2025 OCF 6,788 SBC 589 capex 504 dep 367 acq 204+1,274; CC financing 0 both
ttm_o = 19030 - 6788 + 7265; ttm_s = 955 - 589 + 610; ttm_c = 1214 - 504 + 587; ttm_d = 762 - 367 + 382
print(f'TTM to 2026-06-30: OCF {ttm_o:,} SBC {ttm_s} capex {ttm_c:,} dep {ttm_d}: capex end {ttm_o-ttm_s-ttm_c:,} ({(ttm_o-ttm_s-ttm_c)/CAP:.2%}), dep end {ttm_o-ttm_s-ttm_d:,} ({(ttm_o-ttm_s-ttm_d)/CAP:.2%})')
# screen reproduction
for n in (3, 5):
    ys = list(range(2026 - n, 2026)); m = lambda i: sum(D[y][i] for y in ys) / n
    print(n, 'y screen tries: OCF-SBC-capex', round(m(0)-m(1)-m(2)), '| OCF-SBC-dep', round(m(0)-m(1)-m(3)), '| OCF-SBC-dep-amort', round(m(0)-m(1)-m(3)-m(4)))
# distributions against owner earnings
for y in (2021, 2022, 2023, 2024, 2025):
    ce, de, aq = oe(y); dv, bb = D[y][8], D[y][9]
    print(f'{y}: dividends {dv:,} + buybacks {bb:,} = {dv+bb:,} vs OE capex end {ce:,}; plus acquisitions {aq:,}: total {dv+bb+aq:,}')
tot_bus = sum(D[y][5] for y in range(2013, 2026)); tot_oa = sum(D[y][6] for y in range(2013, 2026))
print('business cash 2013-2025', tot_bus, 'other acq 2013-2025', tot_oa)
