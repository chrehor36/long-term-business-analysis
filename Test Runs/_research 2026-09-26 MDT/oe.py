"""MDT owner earnings, COMPUTATION - NOT A CLEARANCE (the file closed at Q2). Arithmetic only.
Inputs: the filed consolidated statements of cash flows, fiscal 2013-2026 (10-Ks in tenk_*.txt; values equal the
companyfacts tags read by xb.py; FY2013 operating cash from the FY2015 10-K). $ millions.
OE = operating cash flow - stock-based compensation - (c), with (c) at two ends:
  capex end  = additions to property, plant and equipment (total capex)
  dep end    = depreciation only (the D&A caption less amortization of acquired intangibles, which is not maintenance)
Also shown: the D&A caption as (c) (the screen's bottom construction), and each end less cash acquisitions."""
CAP = 113382.8
Y = list(range(2013, 2027))
OCF = dict(zip(Y, [4942, 4959, 4902, 5218, 6880, 4684, 7007, 7234, 6240, 7346, 6039, 6787, 7044, 7330]))
SBC = dict(zip(Y, [152, 145, 439, 375, 348, 344, 290, 297, 344, 359, 355, 393, 429, 457]))
CPX = dict(zip(Y, [457, 396, 571, 1046, 1254, 1068, 1134, 1213, 1355, 1368, 1459, 1587, 1859, 1904]))
DEP = dict(zip(Y, [488, 501, 573, 889, 937, 821, 895, 907, 919, 974, 999, 954, 1054, 1186]))
DA = dict(zip(Y, [819, 850, 1306, 2820, 2917, 2644, 2659, 2663, 2702, 2707, 2697, 2647, 2861, 2958]))
ACQ = dict(zip(Y, [820, 385, 14884, 1213, 1324, 137, 1827, 488, 994, 91, 1867, 211, 98, 406]))
print('| FY | OCF | SBC | capex | depreciation | D&A caption | acquisitions | OE capex end | OE dep end |')
print('|---|---|---|---|---|---|---|---|---|')
for y in Y:
    print(f'| {y} | {OCF[y]:,} | {SBC[y]} | {CPX[y]:,} | {DEP[y]:,} | {DA[y]:,} | {ACQ[y]:,} | {OCF[y]-SBC[y]-CPX[y]:,} | {OCF[y]-SBC[y]-DEP[y]:,} |')
m = lambda d, ys: sum(d[y] for y in ys) / len(ys)
print()
print('| window | years | OE capex end | yield | OE dep end | yield | D&A-caption end | yield | capex end less acquisitions | yield |')
print('|---|---|---|---|---|---|---|---|---|---|')
lo, hi = 1e9, -1e9
for n in range(3, 15):
    ys = Y[-n:]
    base = m(OCF, ys) - m(SBC, ys)
    c, d, a = base - m(CPX, ys), base - m(DEP, ys), base - m(DA, ys)
    q = c - m(ACQ, ys)
    tag = '' if ys[0] >= 2016 else ' (spans the pre-Covidien perimeter, marked)'
    print(f'| {n}y{tag} | FY{ys[0]}-FY{ys[-1]} | {c:,.0f} | {c/CAP:.2%} | {d:,.0f} | {d/CAP:.2%} | {a:,.0f} | {a/CAP:.2%} | {q:,.0f} | {q/CAP:.2%} |')
    if ys[0] >= 2016:
        lo, hi = min(lo, c, d), max(hi, c, d)
print()
print(f'Range, one-company perimeter FY2016-FY2026, every window 3y-11y, both ends: {lo:,.0f} to {hi:,.0f}; {lo/CAP:.2%} to {hi/CAP:.2%} on cap {CAP:,}')
# screen reproduction
ys5 = Y[-5:]; ys3 = Y[-3:]
print('screen top 4,875 = 5y capex end:', round(m(OCF, ys5) - m(SBC, ys5) - m(CPX, ys5), 1))
print('screen bottom 3,737 = 5y D&A-caption end:', round(m(OCF, ys5) - m(SBC, ys5) - m(DA, ys5), 1))
print('dividends FY2024-26 mean 3,631 vs OE; buybacks FY2024-26 mean', round((2138+3235+1035)/3))
