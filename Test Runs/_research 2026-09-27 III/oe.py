"""III owner earnings, from the filed cash-flow statements of each 10-K (cfs_blocks.txt), thousands.
OE = operating cash (newest filed vintage) - stock-based compensation (cash-flow line, in full [E5-06]) - (c).
(c), two ends, a disclosed judgment [E2-09, E3-44]:
  capex end = 'Purchase of furniture, fixtures and equipment' (capitalized internal-use software is recorded inside it, per the 10-K policy note)
  D&A end   = 'Depreciation expense' (acquired-intangible amortization excluded, as in the WFCF/JKHY construction [E2-43])
Acquisitions (cash, contingent consideration paid, installments) are shown beside, never netted in.
No net-income proxy anywhere (operator rule 5)."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# year: (OCF, SBC, capex, depreciation, acquisition cash incl contingent/installments, divestiture cash in)
D = {
 2008: (20481, 1963, 1634, 1529, 0, 0),
 2009: (4056, 2831, 1239, 1419, 0, 0),
 2010: (5747, 3087, 957, 1420, 0, 0),
 2011: (871, 3143, 1690, 1483, 13684, 0),
 2012: (10730, 2797, 1823, 1707, 24 + 2000, 0),
 2013: (23055, 3385, 1901, 1647, 0, 0),
 2014: (7007, 3107, 2170, 1792, 890 + 1633, 0),
 2015: (8310, 5049, 1378, 1760, 537 + 2322 + 661, 0),     # OCF restated from 6,813 by the 1,497 withholding reclass (10-K FY2017)
 2016: (12359, 7047, 2359, 1903, 55187 + 3854, 0),        # restated from 10,659 by the 1,700 withholding reclass
 2017: (11444, 7439, 3169, 3207, 889 + 2665 + 543, 0),
 2018: (19128, 9862, 3999, 2739, 1200, 0),
 2019: (20437, 9589, 1922, 2697, 865, 0),
 2020: (43971, 8891, 1181, 2664, 2317, 0),
 2021: (41942, 6467, 2320, 2688, 2558, 0),
 2022: (11146, 7460, 3423, 3045, 3450 + 1000, 0),
 2023: (12272, 9132, 3433, 3094, 1000 + 1460, 0),
 2024: (19865, 8046, 2830, 3282, 1657, 21822),
 2025: (29011, 7835, 4022, 3263, 1636 + 550, 720 + 1954),
}
# stock issued for acquisitions (non-cash, filed supplemental lines)
STOCK_ACQ = {2011: 7980 + 6250, 2016: 10944, 2025: 250}
CAP = 254655  # $K, Step 0
print('| FY | OCF | SBC | capex | depreciation | OE capex end | OE D&A end | acquisitions (cash) |')
print('|---|---|---|---|---|---|---|---|')
oe = {}
for y, (o, s, c, d, a, dv) in D.items():
    oe[y] = (o - s - c, o - s - d)
    print(f'| {y} | {o:,} | {s:,} | {c:,} | {d:,} | {oe[y][0]:,} | {oe[y][1]:,} | {a:,}' + (f' (divestiture +{dv:,})' if dv else '') + (f' (+{STOCK_ACQ[y]:,} stock/notes)' if y in STOCK_ACQ else '') + ' |')
# TTM to 2026-06-30 = FY2025 + H1 2026 - H1 2025
t_o = 29011 + 4535 - 12896; t_s = 7835 + 3933 - 4424; t_c = 4022 + 1354 - 1679; t_d = 3263 + 1634 - 1634
print(f'TTM to 2026-06-30: OCF {t_o:,} SBC {t_s:,} capex {t_c:,} dep {t_d:,} -> OE capex end {t_o-t_s-t_c:,}, D&A end {t_o-t_s-t_d:,}')
print()
print('| window ending FY2025 | capex end | D&A end | yield on $254.7M | capex/dep | acquisitions per year (cash) |')
print('|---|---|---|---|---|---|')
ys = sorted(D)
res = []
for n in (1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 18):
    w = [y for y in ys if y > 2025 - n]
    a = sum(oe[y][0] for y in w) / n; b = sum(oe[y][1] for y in w) / n
    cd = sum(D[y][2] for y in w) / sum(D[y][3] for y in w)
    acq = sum(D[y][4] for y in w) / n
    res.append((n, a, b))
    print(f'| {n}y FY{w[0]}-25 | {a:,.0f} | {b:,.0f} | {min(a,b)/CAP:.2%}-{max(a,b)/CAP:.2%} | {cd:.2f} | {acq:,.0f} |')
lo = min(min(a, b) for _, a, b in res if _ >= 3); hi = max(max(a, b) for _, a, b in res if _ >= 3)
print(f'range over windows 3-18y both ends: {lo:,.0f} to {hi:,.0f}  ({lo/CAP:.2%} to {hi/CAP:.2%})')
# windows that exclude the 2020-21 working-capital release and its 2022-23 reversal: show 2020-2023 as a block
blk = [2020, 2021, 2022, 2023]
print('2020-23 block mean capex end %.0f, D&A end %.0f' % (sum(oe[y][0] for y in blk) / 4, sum(oe[y][1] for y in blk) / 4))
cum_acq = sum(D[y][4] for y in ys); cum_div = sum(D[y][5] for y in ys); cum_oe = sum(oe[y][0] for y in ys)
print(f'FY2008-25 cumulative: OE capex end {cum_oe:,}; cash acquisitions {cum_acq:,}; divestiture in {cum_div:,}; stock/notes for acquisitions {sum(STOCK_ACQ.values()):,}')
print(f'18y OE capex end net of cash acquisitions and divestiture: {(cum_oe-cum_acq+cum_div)/18:,.0f} per year ({(cum_oe-cum_acq+cum_div)/18/CAP:.2%})')
