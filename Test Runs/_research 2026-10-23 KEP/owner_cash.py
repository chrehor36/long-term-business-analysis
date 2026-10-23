"""KEP owner cash and the Q7 COMPUTATION (arithmetic only; every input from the filed 20-F statements).
KRW billions. Sources (consolidated statements of cash flows / financial position / notes):
  FY2025 20-F acc 0001193125-26-190113 (2023-2025); FY2023 20-F acc 0001193125-24-125063 (2021-2023);
  FY2021 20-F acc 0001193125-22-132015 (2019-2021); FY2019 20-F acc 0001193125-20-125462 (2017-2019);
  FY2017 20-F acc 0001193125-18-141125 (2015-2017). Latest filing wins where restated (2021 OCF 4,491 in FY2023 20-F).
D&A 2016-2024 from SEC XBRL (DepreciationAndAmortisationExpense, transcription), 2025 from the filed cash flow (13,630 + 159).
"""
Y = list(range(2016, 2026))
OCF   = [16521, 11250, 6680, 8213, 13208, 4491, -23478, 1522, 15876, 20880]
CAPEX = [12029, 12536, 12267, 14000, 13281, 12687, 12347, 13908, 14216, 15834]   # PPE
INTG  = [124, 144, 111, 229, 120, 113, 81, 75, 92, 103]                         # intangibles
PROC  = [208, 86, 234, 523, 332, 278, 630, 310, 403, 468]                       # PPE disposals
AACQ  = [113, 207, 319, 108, 342, 673, 361, 498, 452, 2096]                     # associates/JV bought
ADSP  = [47, 11, 2, 0, 5, 4, 56, 6, 237, 14]                                    # associates/JV sold
LEASE = [0, 123, 134, 573, 614, 572, 563, 574, 613, 550]   # 2016: no line found in the FY2017 statement; 0 taken
DIVP  = [2090, 1341, 600, 99, 81, 812, 42, 45, 127, 217]   # consolidated "Dividends paid" (XBRL 2016-2020; filed 2021-2025)
OWND  = [1990, 1271, 507, 0, 0, 781, 0, 0, 0, 137]         # KEPCO's own: DPS x 641.96M (3,100/1,980/790/0/0/1,216/0/0/0/213)
HYB   = [16, 13, 13, 13, 13, 13, 13, 10, 10, 2]           # hybrid bond dividends (2017-2018 taken as 13, line truncated)
INTP  = [2041, 1886, 1896, 2028, 2082, 1928, 2518, 4246, 4697, 4393]            # interest paid
DA    = [8961, 9774, 10025, 11129, 11548, 11942, 12461, 13032, 13997, 13789]
ROU   = [0, 0, 0, 581, 586, 559, 509, 537, 539, 478]
DEBT  = [53639, 54747, 61035, 67877, 69725, 80530, 120605, 133632, 132533, 129769]  # borrowings + debt securities, year end
DEBT_2015 = 58754   # 50,907 LT + 7,243 current portion + 604 short-term (FY2017 20-F Item 5)
EQ    = [73051, 72965, 71093, 68890, 70668, 65327, 42000, 37265, 41363, 49323]   # total equity
PEQ   = [71724, 71681, 69744, 67496, 69297, 63780, 40545, 35845, 39915, 48170]   # owners of the parent
CASH  = [3051, 2370, 1358, 1810, 2030, 2635, 3235, 4343, 2383, 2241]
NI    = [7148, 1441, -1174, -2264, 2094, -5216, -24429, -4716, 3622, 8667]       # profit for the year
PNI   = [7049, 1299, -1315, -2346, 1992, -5305, -24467, -4823, 3492, 8545]
REV   = [59763, 59336, 60033, 58568, 57927, 60012, 70546, 87476, 92578, 96568]
OP    = [12296, 5320, -685, -1708, 4098, -5723, -32241, -4245, 8461, 14011]
PPE   = [145743, 150882, 152743, 164702, 168709, 173135, 177865, 179876, 182983, 187752]

TAX = 0.2692          # applicable rate the FY2025 20-F states for 2025 (26.92%), used for the interest add-back
R = 0.04189           # KTB 30y, Bank of Korea ECOS 817Y002/010230000, 2026-10-23
FLOOR = 0.10
SHARES = 641_964_077  # cover of the FY2025 20-F; dividend 6-K 2026-02-26 states the same count
PRICE_KRW = 28650     # KRX close 2026-10-23 (aggregator, flagged)
FX = 1324.9           # KRW per USD 2026-10-23 (aggregator, flagged)
NET_DEBT = 129769 - 2241   # borrowings and debt securities less cash, 2025-12-31 (capital-management note)

n = len(Y)
nci = [DIVP[i] - OWND[i] for i in range(n)]
netaff = [AACQ[i] - ADSP[i] for i in range(n)]
fixed = [CAPEX[i] + INTG[i] for i in range(n)]
maint = [DA[i] - ROU[i] for i in range(n)]
# owner cash, equity-only (after interest, after tax), all spending, before any debt credit
oc_all = [OCF[i] - fixed[i] + PROC[i] - netaff[i] - LEASE[i] - nci[i] - HYB[i] for i in range(n)]
# maintenance-only: maintenance = depreciation of owned assets + amortization (D&A less right-of-use depreciation)
oc_mnt = [OCF[i] - maint[i] + PROC[i] - LEASE[i] - nci[i] - HYB[i] for i in range(n)]
ia = [INTP[i] * (1 - TAX) for i in range(n)]

def row(name, v): print(f'{name:44s}' + ''.join(f'{x:>9,.0f}' for x in v) + f'  | sum {sum(v):>9,.0f}')
print(' ' * 44 + ''.join(f'{y:>9d}' for y in Y))
for nm, v in [('Revenue', REV), ('Operating profit', OP), ('Profit for the year', NI), ('Profit to owners of parent', PNI),
              ('Operating cash flow (after interest, tax)', OCF), ('Fixed-asset spending (PPE+intangible)', fixed),
              ('Maintenance guess (D&A less ROU dep)', maint), ('Net associates/JV bought', netaff), ('Lease principal', LEASE),
              ('Dividends to minorities (derived)', nci), ('Interest paid', INTP),
              ('OWNER CASH all spending, equity-only', oc_all), ('OWNER CASH maintenance-only, equity-only', oc_mnt),
              ('Borrowings + debt securities (year end)', DEBT), ('Total equity', EQ), ('Parent equity', PEQ), ('Cash', CASH), ('PPE', PPE)]:
    row(nm, v)

# Owner cash as share of sales, ROE
print('\nROE on average parent equity (%):', [round(PNI[i] / ((PEQ[i] + PEQ[i - 1]) / 2) * 100, 1) for i in range(1, n)])
print('Debt / (debt + equity) at 2025-12-31: %.2f%%' % (DEBT[-1] / (DEBT[-1] + EQ[-1]) * 100))

def credit(span):
    a, b = span
    idx = [i for i in range(n) if a <= Y[i] <= b]
    d0 = DEBT_2015 if a == 2016 else DEBT[idx[0] - 1]
    d_raised = DEBT[idx[-1]] - d0
    fx = sum(fixed[i] for i in idx); ocf = sum(OCF[i] for i in idx)
    share = DEBT[-1] / (DEBT[-1] + EQ[-1])
    cap = share * fx
    not_from_ops = fx - ocf
    d_fa = max(0.0, min(d_raised, cap, not_from_ops))
    return idx, d_raised, fx, ocf, cap, not_from_ops, d_fa

def value_no_growth(c, r): return c / r   # ten years flat then no growth = a flat perpetuity

def report(label, span):
    idx, d_raised, fx, ocf, cap, nfo, d_fa = credit(span)
    k = len(idx)
    mfx = sum(maint[i] for i in idx)
    cases = {}
    cases['A all spending, no credit (beside)'] = sum(oc_all[i] for i in idx) / k
    cases['B all spending, debt credit (regulated rule)'] = (sum(oc_all[i] for i in idx) + d_fa) / k
    cases['C maintenance-only, debt credit pro rata (CENTRAL)'] = (sum(oc_mnt[i] for i in idx) + d_fa * mfx / fx) / k
    cases['D maintenance-only, no credit (beside)'] = sum(oc_mnt[i] for i in idx) / k
    print(f'\n=== {label}: years {Y[idx[0]]}-{Y[idx[-1]]} ({k} yrs)')
    print(f'  debt raised {d_raised:,.0f}; fixed-asset spending {fx:,.0f}; operating cash {ocf:,.0f}; spending not met from operations {nfo:,.0f};'
          f' debt-share cap {cap:,.0f}; debt credited to fixed assets {d_fa:,.0f}; maintenance share of spending {mfx/fx:.3f}')
    first = [i for i in idx[:k // 2]]; second = [i for i in idx[k - k // 2:]]
    for nm, c in cases.items():
        v = value_no_growth(c, R); f = value_no_growth(c, FLOOR)
        print(f'  {nm:52s} owner cash/yr {c:>8,.0f}  value@{R*100:.3f}% {v:>10,.0f}bn = {v*1e9/SHARES:>9,.0f} won/sh;'
              f'  @10% {f*1e9/SHARES:>9,.0f} won/sh; return at price {c/(PRICE_KRW*SHARES/1e9)*100:6.2f}%')
    # all-equity beside: add back after-tax interest, value less net debt
    for nm, base in [('all-equity, all spending (no credit)', [oc_all[i] + ia[i] for i in idx]),
                     ('all-equity, maintenance-only', [oc_mnt[i] + ia[i] for i in idx])]:
        c = sum(base) / k
        v = c / R - NET_DEBT; f = c / FLOOR - NET_DEBT
        ev = PRICE_KRW * SHARES / 1e9 + NET_DEBT
        print(f'  {nm:52s} owner cash/yr {c:>8,.0f}  equity value@sov {v*1e9/SHARES:>9,.0f} won/sh; @10% {f*1e9/SHARES:>9,.0f} won/sh;'
              f' return on EV {c/ev*100:6.2f}%')
    h1 = sum(oc_mnt[i] for i in first) / len(first); h2 = sum(oc_mnt[i] for i in second) / len(second)
    print(f'  growth check, maintenance case: first half avg {h1:,.0f}, second half avg {h2:,.0f}')

report('CYCLE BASE, peak to peak (specific (a))', (2016, 2025))
report('LITERAL WINDOW, last five years (beside)', (2021, 2025))
mc = PRICE_KRW * SHARES / 1e9
print(f'\nMarket value of common: {mc:,.0f}bn KRW; ${mc*1e9/FX/1e6:,.0f}M; per ADS (1/2 share) ${PRICE_KRW/2/FX:.2f}; net debt {NET_DEBT:,.0f}bn')
print(f'P/E on FY2025 parent profit: {mc/PNI[-1]:.2f}; price/parent book: {mc/PEQ[-1]:.2f}')
print(f'Floor test: owner cash needed per year for 10% at the price (equity-only, no growth): {mc*FLOOR:,.0f}bn')
