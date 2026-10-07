import json
from datetime import date
f = json.load(open('cache/facts_cw.json'))['facts']['us-gaap']
def dur(t):
    out = {}
    for u, arr in f[t]['units'].items():
        for x in arr:
            if x.get('form') in ('10-K','10-K/A') and 'start' in x and 350 <= (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days <= 380:
                out[int(x['end'][:4])] = x['val'] / 1e6
    return out
ocf = dur('NetCashProvidedByUsedInOperatingActivities'); sbc = dur('ShareBasedCompensation')
cap = dur('PaymentsToAcquirePropertyPlantAndEquipment'); dep = dur('Depreciation'); am = dur('AmortizationOfIntangibleAssets'); da = dur('DepreciationAndAmortization')
pen = {2015: 139.61, 2016: -3.405, 2018: 43.759, 2020: 153.375}  # the face's pension line where it is a large outflow (voluntary contributions), recorded for a display only
rev = dur('SalesRevenueNet'); rev.update(dur('Revenues')); rev.update(dur('RevenueFromContractWithCustomerExcludingAssessedTax'))
yrs = list(range(2011, 2026))
rows = {}
print('FY    OCF    SBC  capex   dep  acqam   D&A | OE_capex  OE_dep  OE_D&A(screen) | OE/rev')
for y in yrs:
    a = ocf[y] - sbc[y] - cap[y]; b = ocf[y] - sbc[y] - dep[y]; c = ocf[y] - sbc[y] - da[y]
    rows[y] = (a, b, c)
    print(f'{y} {ocf[y]:6.1f} {sbc[y]:5.1f} {cap[y]:5.1f} {dep[y]:5.1f} {am.get(y,float("nan")):5.1f} {da[y]:6.1f} | {a:7.1f} {b:7.1f} {c:7.1f} | {100*min(a,b)/rev[y]:5.1f}%')
# TTM from the 10-Q (H1 2026 less H1 2025), face values
ttm_ocf = ocf[2025] + 175.528 - 97.820; ttm_sbc = sbc[2025] + 14.305 - 10.484; ttm_cap = cap[2025] + 41.283 - 35.154
ttm_da = da[2025] + 56.735 - 62.128
print(f'TTM  ocf {ttm_ocf:.1f} sbc {ttm_sbc:.1f} capex {ttm_cap:.1f} (grant proceeds 8.5 not netted) D&A {ttm_da:.1f} OE_capex {ttm_ocf-ttm_sbc-ttm_cap:.1f}')
cap_m = 532.36 * 36934444 / 1e6
print('cap', round(cap_m, 1))
def win(n, end=2025):
    ys = list(range(end - n + 1, end + 1))
    return [sum(rows[y][k] for y in ys) / n for k in range(3)]
print('window   capex-end        dep-end        D&A-end(screen)')
for n in (1, 3, 5, 7, 10, 15):
    a, b, c = win(n)
    print(f'{n:2d}y  {a:7.1f} ({100*a/cap_m:4.2f}%)  {b:7.1f} ({100*b/cap_m:4.2f}%)  {c:7.1f} ({100*c/cap_m:4.2f}%)')
print('rolling 5y windows (capex end / dep end):')
for e in range(2015, 2026):
    a, b, c = win(5, e); print(f'  FY{e-4}-{e}: {a:6.1f} / {b:6.1f}')
# sensitivity: add back the voluntary pension contributions of 2015, 2018, 2020 (display only)
adj = {2015: 125.0, 2018: 40.0, 2020: 150.0}
print('pension face line FY2015/2018/2020 (outflows):', pen)
# growth
def cagr(a, b, n): return (b / a) ** (1 / n) - 1
print('OE capex-end CAGR FY2016-25', round(100*cagr(rows[2016][0], rows[2025][0], 9), 1), 'dep-end', round(100*cagr(rows[2016][1], rows[2025][1], 9), 1))
print('rev CAGR FY2016-25', round(100*cagr(rev[2016], rev[2025], 9), 1))
print('5y means FY2016-20 vs FY2021-25 capex end', round(win(5,2020)[0],1), round(win(5,2025)[0],1))
