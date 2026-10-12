"""Q7 arithmetic for the TECH run (framework v5, Q7 range convention). Inputs are the filed cash-flow statements
(10-K FY2023 0001558370-23-015226 for FY2022-FY2023; 10-K FY2026 0001104659-26-100322 for FY2024-FY2026), $M.
Interest paid is XBRL InterestPaidNet. Arithmetic only; the judgments are in the run file."""

SOV = 0.056            # 30-year Treasury par yield, 2026-10-09
FLOOR = 0.10           # CONVENTION, Q7 floor
TAX_INT = 0.25         # CONVENTION of this run: after-tax interest at 25% (filer's long-term GAAP rate 23.5%-26.3%)
SHARES = 156.818238    # cover, 2026-08-17
PRICE = 72.46
DEBT, CASH = 200.0, 264.712   # 2026-06-30 balance sheet; no finance leases stated; operating leases left out
NET_DEBT = DEBT - CASH

yrs = ['FY2022', 'FY2023', 'FY2024', 'FY2025', 'FY2026']
ocf = [325.272, 254.393, 298.981, 287.556, 292.073]
sbc = [42.183, 39.230, 38.042, 40.833, 41.365]
capex = [44.908, 38.244, 62.877, 31.006, 28.850]
intpaid = [11.0, 8.4, 14.5, 19.0, 14.4]
ww_dist = [0.0, 0.0, 6.997, 7.291, 6.043]
# businesses bought, net of businesses sold (Wilson Wolf forward and stake counted as a purchase)
acq = [25.0, 101.184 + 232.0 - 17.824, 169.707, 15.0 - 2.447, -4.617]
sales = [1105.599, 1136.702, 1159.060, 1219.635, 1215.039]
maint = 33.1           # maintenance guess: property and equipment depreciation, FY2023-FY2026 average

def avg(x): return sum(x) / len(x)

oc_eq = [o - s - c + w for o, s, c, w in zip(ocf, sbc, capex, ww_dist)]            # equity-only, before purchases
oc_ae = [e + i * (1 - TAX_INT) for e, i in zip(oc_eq, intpaid)]                       # all-equity, before purchases
oc_ae_after = [a - q for a, q in zip(oc_ae, acq)]
oc_eq_after = [a - q for a, q in zip(oc_eq, acq)]

print('year   OC eq   OC all-eq   purchases   OC all-eq after purchases')
for row in zip(yrs, oc_eq, oc_ae, acq, oc_ae_after):
    print('%s %7.1f %9.1f %10.1f %12.1f' % row)
B_ae, B_eq = avg(oc_ae), avg(oc_eq)
A = avg(acq)
B_maint_ae = B_ae + (avg(capex) - maint)
B_maint_eq = B_eq + (avg(capex) - maint)
print('\naverages: all-equity before purchases %.1f; equity-only %.1f; purchases %.1f; capex %.1f; maint-only add %.1f'
      % (B_ae, B_eq, A, avg(capex), avg(capex) - maint))
print('after purchases: all-equity %.1f; equity-only %.1f' % (B_ae - A, B_eq - A))

# growth shown
half1 = avg(oc_ae_after[:2]); half2 = avg(oc_ae_after[3:])
print('\nseries after purchases changes sign: %s' % [round(x, 1) for x in oc_ae_after])
print('halves (FY22-23 vs FY25-26, 3 yrs apart): %.1f -> %.1f, %.1f%%/yr (absurd: cut by (f))'
      % (half1, half2, ((half2 / half1) ** (1 / 3) - 1) * 100))
g_sales = (sales[-1] / sales[0]) ** (1 / 4) - 1
g_oc_before = (oc_ae[-1] / oc_ae[0]) ** (1 / 4) - 1
print('sales growth FY2022->FY2026 %.2f%%/yr; owner cash before purchases %.2f%%/yr' % (g_sales * 100, g_oc_before * 100))
organic = [0.17, 0.05, 0.01, 0.05, 0.00]
g_org = 1
for o in organic: g_org *= 1 + o
g_org = g_org ** (1 / 5) - 1
print('filer organic sales growth FY2022-FY2026 compounded %.2f%%/yr' % (g_org * 100))

def value(cash_y1_10, terminal_cash, g, r, g_terminal_base=None):
    """cash_y1_10: base cash in year 0 terms carried at g for years 1-10; terminal: zero growth after year 10 on
    terminal_cash (year-0 terms, grown at g to year 10)."""
    pv = sum(cash_y1_10 * (1 + g) ** t / (1 + r) ** t for t in range(1, 11))
    tv = terminal_cash * (1 + g) ** 10 / r / (1 + r) ** 10
    return pv + tv

def per_share(ev, all_equity=True):
    return (ev - NET_DEBT) / SHARES if all_equity else ev / SHARES

cases = {}
# default pair (c): purchases deducted, total growth credited, cut to sales growth by (f); purchases stop after year 10
cases['bottom: purchases deducted, growth 2.39% (sales), purchases stop after yr 10'] = (B_ae - A, B_ae, g_sales, B_eq - A, B_eq)
cases['purchases deducted, no growth, purchases stop after yr 10'] = (B_ae - A, B_ae, 0.0, B_eq - A, B_eq)
# (e) inversion: no-purchase no-growth, maintenance-only, as the top
cases['top: no purchases, no growth, maintenance-only capex'] = (B_maint_ae, B_maint_ae, 0.0, B_maint_eq, B_maint_eq)
cases['no purchases, no growth, all capex'] = (B_ae, B_ae, 0.0, B_eq, B_eq)
# organic pair beside
cases['organic pair: no purchases, shown owner-cash growth %.2f%%' % (g_oc_before * 100)] = (B_ae, B_ae, g_oc_before, B_eq, B_eq)
cases['most generous: no purchases, organic %.2f%%, maintenance-only' % (g_org * 100)] = (B_maint_ae, B_maint_ae, g_org, B_maint_eq, B_maint_eq)

print('\n%-78s %9s %9s %9s %9s %9s' % ('case', 'EV@5.6%', '$/sh ae', 'EV@10%', '$/sh ae', '$/sh eq@10'))
res = {}
for k, (c, tc, g, ceq, tceq) in cases.items():
    ev_s = value(c, tc, g, SOV); ev_f = value(c, tc, g, FLOOR); eq_f = value(ceq, tceq, g, FLOOR)
    eq_s = value(ceq, tceq, g, SOV)
    res[k] = (ev_s, per_share(ev_s), ev_f, per_share(ev_f), per_share(eq_f, False), per_share(eq_s, False))
    print('%-78s %9.0f %9.2f %9.0f %9.2f %9.2f' % (k, ev_s, per_share(ev_s), ev_f, per_share(ev_f), per_share(eq_f, False)))

kb = [k for k in res if k.startswith('bottom')][0]; kt = [k for k in res if k.startswith('top')][0]
lo, hi = res[kb][1], res[kt][1]
print('\nRANGE (all-equity, at 5.60%%): $%.2f to $%.2f a share; width %.2f to 1; price $%.2f' % (lo, hi, hi / lo, PRICE))
print('equity-only range at 5.60%%: $%.2f to $%.2f' % (res[kb][5], res[kt][5]))
fair_ae = (res[kb][3] + res[kt][3]) / 2
fair_eq = (res[kb][4] + res[kt][4]) / 2
print('FAIR PRICE (each end at 10%%, averaged): all-equity $%.2f; equity-only $%.2f' % (fair_ae, fair_eq))

# expected return at the price, by case: the discount rate that makes the case's value equal the price
def irr(c, tc, g, all_equity=True):
    target = PRICE * SHARES + (NET_DEBT if all_equity else 0)
    lo_r, hi_r = 0.0001, 0.5
    for _ in range(200):
        mid = (lo_r + hi_r) / 2
        if value(c, tc, g, mid) > target: lo_r = mid
        else: hi_r = mid
    return mid
print('\nexpected return at $%.2f, by case (all-equity):' % PRICE)
for k, (c, tc, g, ceq, tceq) in cases.items():
    print('  %-78s %5.2f%%' % (k, irr(c, tc, g) * 100))

# Wilson Wolf beside: purchase of the remaining 80.1% (signed, not closed)
print('\nWilson Wolf beside: equity-method share of income before basis amortization ~ (0.887 + 9.959) / 0.199 = %.1f at 100%%'
      % ((0.887 + 9.959) / 0.199))
for pay in (92.0 * 4.4 * 0.801, 1000.0):   # first-milestone revenue x 4.4 x 80.1%; the 10-K's ~$1B
    add = (0.887 + 9.959) / 0.199 * 0.801   # 80.1% of implied income, counted as owner cash (generous: earnings, not cash)
    ev_ae_b = value(B_ae - A, B_ae, g_sales, SOV) + add / SOV
    print('  if paid $%.0fM (added to net debt), with $%.1fM a year more: bottom $/sh %.2f (was %.2f)'
          % (pay, add, (ev_ae_b - NET_DEBT - pay) / SHARES, lo))
