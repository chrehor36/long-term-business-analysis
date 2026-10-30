"""Owner earnings for IBM, rebuilt on ONE perimeter, both (c) ends, every valid window.

Perimeter rule (the CNR rule): IBM's CONSOLIDATED STATEMENT OF CASH FLOWS INCLUDES the cash
flows of discontinued operations.  FY2021 AR, page 42: "Our cash flows from operating,
investing and financing activities, as reflected in the Consolidated Statement of Cash Flows
... include the cash flows of discontinued operations", with the footnote "Includes cash flows
of discontinued operations of $1.6 billion, $4.4 billion and $4.5 billion in 2021, 2020 and
2019, respectively."  So FY2019, FY2020 and FY2021 operating cash CANNOT be used: Kyndryl is
inside them and IBM published only a single aggregate discontinued-cash figure, not a Kyndryl
cash-flow statement.  The revenue line WAS recast to continuing operations; the cash-flow
statement was NOT.  Therefore the clean perimeter is FY2022-FY2025 plus the TTM.
"""
M = 1.0  # all figures in $M, as filed

# --- filed lines, one perimeter (FY2022-FY2025), 10-K 0000051143-26-000010 and 0001558370-23-002376
YEARS = ['FY2022', 'FY2023', 'FY2024', 'FY2025', 'TTM 2026H1']
OCF        = {'FY2022': 10435.0, 'FY2023': 13931.0, 'FY2024': 13445.0, 'FY2025': 13193.0,
              'TTM 2026H1': 13193.0 + 7766.0 - 6071.0}
# IBM's own filed "change in Financing receivables" line from the MD&A free-cash-flow table
# (negative = the finance book GREW and consumed operating cash)
DFR        = {'FY2022': -700.0, 'FY2023': 1200.0, 'FY2024': -400.0, 'FY2025': -3200.0,
              'TTM 2026H1': None}
SBC        = {'FY2022': 987.0, 'FY2023': 1133.0, 'FY2024': 1311.0, 'FY2025': 1715.0,
              'TTM 2026H1': 1715.0 + 1004.0 - 842.0}
CAPEX_PPE  = {'FY2022': 1346.0, 'FY2023': 1245.0, 'FY2024': 1048.0, 'FY2025': 1091.0,
              'TTM 2026H1': 1091.0 + 461.0 - 454.0}
CAPEX_SW   = {'FY2022': 626.0, 'FY2023': 565.0, 'FY2024': 637.0, 'FY2025': 647.0,
              'TTM 2026H1': 647.0 + 313.0 - 314.0}
DISPOSALS  = {'FY2022': 111.0, 'FY2023': 321.0, 'FY2024': 557.0, 'FY2025': 121.0,
              'TTM 2026H1': 121.0 + 31.0 - 111.0}
DEPR_TOTAL = {'FY2022': 2407.0, 'FY2023': 2109.0, 'FY2024': 2168.0, 'FY2025': 2284.0,
              'TTM 2026H1': 2284.0 + 1088.0 - 1114.0}
ROU_AMORT  = {'FY2022': 900.0, 'FY2023': 900.0, 'FY2024': 900.0, 'FY2025': 900.0,
              'TTM 2026H1': 900.0}   # filing: "$0.9 billion in 2025, 2024 and 2023"
AMORT_SWIA = {'FY2022': 2395.0, 'FY2023': 2287.0, 'FY2024': 2499.0, 'FY2025': 2737.0,
              'TTM 2026H1': 2737.0 + 1535.0 - 1328.0}
AMORT_ACQ  = {'FY2022': 1747.0, 'FY2023': 1627.0, 'FY2024': 1830.0, 'FY2025': 2166.0,
              'TTM 2026H1': None}   # income-statement total from the segment reconciliation

def c_capex(y):
    """(c) at the CAPEX end: cash spent on plant and on software, net of disposal proceeds."""
    return CAPEX_PPE[y] + CAPEX_SW[y] - DISPOSALS[y]

def c_renewal_da(y):
    """(c) at the RENEWAL-ONLY D&A end: fixed-asset depreciation + capitalised-software
    amortisation.  Operating-lease ROU amortisation is EXCLUDED because the rent is already
    inside operating cash flow (the CRM precedent), and ACQUIRED-intangible amortisation is
    EXCLUDED because $8,316M a year of R&D above the line already renews the technology
    (the HON/UNH/EFX precedent).  Where AMORT_ACQ is unavailable the FY2025 ratio is used and
    the row is flagged."""
    acq = AMORT_ACQ[y] if AMORT_ACQ[y] is not None else AMORT_SWIA[y] * (2166.0 / 2737.0)
    sw_amort = AMORT_SWIA[y] - acq
    return (DEPR_TOTAL[y] - ROU_AMORT[y]) + sw_amort

def c_raw_da(y):
    """(c) at the RAW filed D&A end - the mechanical screen's number.  Refused below."""
    return DEPR_TOTAL[y] + AMORT_SWIA[y]

print('=== (c) constructions, $M')
print('%-11s %10s %10s %10s' % ('year', 'capex end', 'renewal D&A', 'raw D&A'))
for y in YEARS:
    print('%-11s %10.0f %10.0f %10.0f' % (y, c_capex(y), c_renewal_da(y), c_raw_da(y)))

print()
print('=== construction A: CONSOLIDATED operating cash as filed, less SBC, less (c)')
print('    (charges the growth of the finance book against the owner - the DELL reading)')
A = {}
for y in YEARS:
    A[y] = (OCF[y] - SBC[y] - c_capex(y), OCF[y] - SBC[y] - c_renewal_da(y))
    print('%-11s OCF %8.0f  SBC %6.0f  -> %8.0f (capex end) .. %8.0f (renewal D&A end)'
          % (y, OCF[y], SBC[y], A[y][0], A[y][1]))

print()
print('=== construction B: INDUSTRIAL operating cash (IBM\'s own filed line, "Net cash from')
print('    operating activities, excluding Financing receivables"), less SBC, less (c)')
B = {}
for y in YEARS:
    if DFR[y] is None:
        print('%-11s  NOT AVAILABLE - IBM publishes the financing-receivable change only annually' % y)
        continue
    ind = OCF[y] - DFR[y]
    B[y] = (ind - SBC[y] - c_capex(y), ind - SBC[y] - c_renewal_da(y))
    print('%-11s industrial OCF %8.0f  -> %8.0f (capex end) .. %8.0f (renewal D&A end)'
          % (y, ind, B[y][0], B[y][1]))

def windows(d, keys):
    out = {}
    ks = [k for k in keys if k in d]
    n = len(ks)
    for w in range(2, n + 1):
        sel = ks[n - w:]
        lo = sum(d[k][0] for k in sel) / w
        hi = sum(d[k][1] for k in sel) / w
        out['%d-yr %s-%s' % (w, sel[0], sel[-1])] = (lo, hi)
    return out

ANNUAL = ['FY2022', 'FY2023', 'FY2024', 'FY2025']
print()
print('=== every valid window x both (c) ends')
allv = []
for name, d in (('A consolidated', A), ('B industrial', B)):
    print('--', name)
    for k, (lo, hi) in windows(d, ANNUAL).items():
        print('   %-24s %8.0f .. %8.0f' % (k, lo, hi))
        allv += [lo, hi]
    if 'TTM 2026H1' in d:
        lo, hi = d['TTM 2026H1']
        print('   %-24s %8.0f .. %8.0f' % ('TTM (A only, see note)', lo, hi))
        allv += [lo, hi]
print()
print('COMBINED BAND across every window and both ends: %.0f .. %.0f  (width %.0f, %.1f%% of the low end)'
      % (min(allv), max(allv), max(allv) - min(allv), (max(allv) - min(allv)) / abs(min(allv)) * 100))

print()
print('=== yields at the 2026-09-18 close')
PRICE, SHARES = 229.55, 942134390
CAP = PRICE * SHARES / 1e6
print('cap $%.0fM' % CAP)
for label, v in [('band low', min(allv)), ('band high', max(allv))]:
    print('  %-10s %8.0f -> %.2f%%' % (label, v, v / CAP * 100))
for k in ['4-yr FY2022-FY2025', '3-yr FY2023-FY2025', '2-yr FY2024-FY2025']:
    for name, d in (('A', A), ('B', B)):
        w = windows(d, ANNUAL)
        if k in w:
            lo, hi = w[k]
            print('  %s %-22s %8.0f..%8.0f -> %.2f%%..%.2f%%' % (name, k, lo, hi, lo / CAP * 100, hi / CAP * 100))
ttm = A['TTM 2026H1']
print('  A TTM                    %8.0f..%8.0f -> %.2f%%..%.2f%%' % (ttm[0], ttm[1], ttm[0] / CAP * 100, ttm[1] / CAP * 100))

print()
print('=== IBM\'s own free cash flow, for comparison (NOT owner earnings: no SBC subtracted)')
for y, f in [('FY2022', 9300.0), ('FY2023', 11200.0), ('FY2024', 12700.0), ('FY2025', 14734.0)]:
    print('   %s  %8.0f   ->  %.2f%% of cap' % (y, f, f / CAP * 100))

print()
print('=== staying power arithmetic')
print('total debt 61260 ; Financing segment debt 15093 ; non-Financing debt 46167 (FY2025)')
print('Q2 2026: total debt 62000, IBM Financing debt 13000 -> non-Financing about 49000')
print('cash+restricted+marketable securities Q2 2026: 8200')
print('interest paid FY2025 2042 ; of which Financing intercompany expense 365 (segment note)')
print('coverage [E2-54]: (OCF %0.0f - capex %0.0f) / interest paid 2042 = %.1fx'
      % (OCF['FY2025'], c_capex('FY2025'), (OCF['FY2025'] - c_capex('FY2025')) / 2042.0))
twelve = 6424.0 + 6255.0 + c_capex('FY2025')
print('twelve-month hard claims: short-term debt 6424 + dividend 6255 + (c) %0.0f = %0.0f'
      % (c_capex('FY2025'), twelve))
print('against FY2025 OCF 13193 + Q2 2026 liquidity 8200 = 21393 ; ratio %.2f' % (twelve / 21393.0))
