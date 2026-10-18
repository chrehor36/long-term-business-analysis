"""SWX run 2026-10-18: Q7 arithmetic from the filed figures transcribed below (USD millions).
Every input carries its source in the comment. Run: python -I calc.py"""
print('COMPUTATION, NOT A CLEARANCE (the heading of operator rule 3; this script first ran before Q2 to Q4 closed)')
yrs = [2021, 2022, 2023, 2024, 2025]
# Southwest Gas Corporation statements of cash flows (FY2023 10-K 0001692115-24-000038 for 2021-2022;
# FY2025 10-K 0001692115-26-000062 for 2023-2025)
ocf   = [25.245, 284.403, 391.545, 1252.982, 618.815]
sbc   = [6.392, 5.776, 4.877, 10.022, 12.989]        # stock-pay add-back lines
dtax  = [53.237, 42.387, 71.874, 68.954, 172.454]    # deferred income taxes add-back
capex = [601.983, 683.131, 762.081, 846.590, 807.866]
dna   = [253.398, 263.043, 295.462, 303.095, 330.724]
intpd = [90.240, 107.980, 139.747, 156.998, 176.958] # interest paid, net of capitalized
ni    = [187.135, 154.380, 228.412, 262.096, 300.308] # SWG Corp net income (2023 as adjusted, FY2025 10-K)
rev   = [1521.790, 1935.069, 2494.220, 2482.990, 1942.480]
opm   = [1090.883, 1145.853, 1242.853, 1325.626, 1444.844]  # operating margin (filer's non-GAAP; 2021-22 segment)
# PGA balance (receivable + / payable -), filed tables: end-2020 -52.583 (FY2021 10-K), end-2025 -304.871 (FY2025 10-K)
# cash effect by year: 2021 -343.728, 2022 -158.975 (CF lines), 2023 -102.765 (CF line as first filed, FY2023 10-K),
# 2025 +65.277 (CF line); 2024 = residual so that the window total equals the balance change.
pga_total = -(-304.871 - (-52.583))       # +252.288 inflow over the window
pga = [-343.728, -158.975, -102.765, None, 65.277]
pga[3] = pga_total - sum(x for x in pga if x is not None)
T = 0.24   # CONVENTION of this run: marginal tax on interest, 21% federal plus about 3% state (rate reconciliation, FY2025 10-K)
rows = []
for i, y in enumerate(yrs):
    base = ocf[i] - sbc[i] - pga[i]                # cash from operations after stock pay, gas-cost swings removed
    eq_pre = base - dtax[i]                         # deferred tax charged as if paid (book tax)
    ae_pre = eq_pre + intpd[i] * (1 - T)            # all-equity: interest added back after tax
    rows.append(dict(y=y, pga=pga[i], base=base, eq_pre=eq_pre, ae_pre=ae_pre,
                     ae_dna=ae_pre - dna[i], ae_cap=ae_pre - capex[i], eq_dna=eq_pre - dna[i], eq_cap=eq_pre - capex[i],
                     ae_asfiled_dna=ocf[i] - sbc[i] + intpd[i] * (1 - T) - dna[i], nopat=ni[i] + intpd[i] * (1 - T)))
def avg(k): return sum(r[k] for r in rows) / len(rows)
print('year   PGA    cash-ops  eq-pre  ae-pre  AE-after-D&A  AE-after-capex  EQ-after-D&A  EQ-after-capex  AE as filed(D&A)  NI+int(1-t)')
for r in rows:
    print(f"{r['y']} {r['pga']:8.1f} {r['base']:8.1f} {r['eq_pre']:7.1f} {r['ae_pre']:7.1f} {r['ae_dna']:12.1f} {r['ae_cap']:14.1f} {r['eq_dna']:12.1f} {r['eq_cap']:14.1f} {r['ae_asfiled_dna']:16.1f} {r['nopat']:11.1f}")
for k in ['ae_dna', 'ae_cap', 'eq_dna', 'eq_cap', 'ae_asfiled_dna', 'nopat']:
    print(f'avg {k}: {avg(k):.1f}')
growth_spend = sum(capex) / 5 - sum(dna) / 5
print(f'avg capex {sum(capex)/5:.1f}  avg D&A {sum(dna)/5:.1f}  growth spending (capex - D&A) {growth_spend:.1f}')
def cagr(a, b, n): return (b / a) ** (1 / n) - 1
g_end = cagr(rows[0]['ae_dna'], rows[-1]['ae_dna'], 4)
h1 = (rows[0]['ae_dna'] + rows[1]['ae_dna']) / 2
h2 = (rows[3]['ae_dna'] + rows[4]['ae_dna']) / 2
g_half = cagr(h1, h2, 3)
g_sales = cagr(rev[0], rev[-1], 4)
g_opm = cagr(opm[0], opm[-1], 4)
g_nopat = cagr(rows[0]['nopat'], rows[-1]['nopat'], 4)
print(f'growth of AE owner cash (D&A basis): end-to-end {g_end:.2%}, halves {g_half:.2%}; sales {g_sales:.2%}; operating margin {g_opm:.2%}; NI+int(1-t) {g_nopat:.2%}')
print('owner cash / revenue by year:', ' '.join(f"{rows[i]['ae_dna']/rev[i]:.1%}" for i in range(5)))
# ---- valuation ----
r_t = 0.0543   # US Treasury 30-year par yield 2026-10-16 (tools/run.py, Treasury daily par yield curve)
price = 87.45  # close 2026-10-16, aggregator, live quote only
shares = 72.445853  # cover of the 10-Q 0001692115-26-000112, as of 2026-07-31
debt = 3409.859 + 100.000   # 10-Q balance sheet 2026-06-30: long-term debt + current maturities
cash = 270.518
pga_liab = 286.815          # deferred purchased gas costs (liability), 10-Q 2026-06-30
nol_dta = 146.287           # holdings NOL deferred tax asset, FY2025 10-K
nol_pv = nol_dta / 3 * sum(1 / (1 + r_t) ** k for k in (1, 2, 3))
net_debt = debt - cash + pga_liab
print(f'net debt: borrowings {debt:.1f} - cash {cash:.1f} = {debt-cash:.1f}; + PGA over-collection {pga_liab:.1f} = {net_debt:.1f}; NOL shelter PV {nol_pv:.1f}')
mcap = price * shares
ev = mcap + net_debt - nol_pv
print(f'market cap {mcap:.1f}; EV (all-equity basis) {ev:.1f}')
def pv_case(oc, g, spend, r):
    """ten years: owner cash after maintenance growing at g, less growth spending growing at the same g; then no growth, spending stops"""
    v = 0.0
    for t in range(1, 11):
        v += (oc * (1 + g) ** t - spend * (1 + g) ** t) / (1 + r) ** t
    v += oc * (1 + g) ** 10 / r / (1 + r) ** 10
    return v
def nogrowth(oc, r): return oc / r
def ps(v, nd=None): return (v - (net_debt if nd is None else nd) + nol_pv) / shares
oc_ae = avg('ae_dna'); oc_eq = avg('eq_dna'); oc_gen = avg('nopat')
g_cut = min(g_sales, r_t)
for label, g in [('shown 2021-25 end-to-end', g_end), ('cut to sales growth, not above the discount rate', g_cut)]:
    for rr in (r_t, 0.10):
        v = pv_case(oc_ae, g, growth_spend, rr)
        print(f'growth case [{label}] g={g:.2%} at r={rr:.2%}: whole {v:.0f}  per share {ps(v):.2f}')
for rr in (r_t, 0.10):
    v0 = nogrowth(oc_ae, rr)
    print(f'no-growth maintenance case at r={rr:.2%}: whole {v0:.0f}  per share {ps(v0):.2f}')
    vall = nogrowth(avg('ae_cap'), rr)
    print(f'all-spending no-growth (literal window) at r={rr:.2%}: whole {vall:.0f}  per share {ps(vall):.2f}')
for rr in (r_t, 0.10):
    v = nogrowth(oc_gen, rr)
    print(f'GENEROUS no-growth on NI+int(1-t) avg {oc_gen:.1f} at r={rr:.2%}: per share {ps(v):.2f}; without PGA as debt {ps(v, debt-cash):.2f}')
end_a = nogrowth(oc_ae, 0.10)
end_b = pv_case(oc_ae, g_end, growth_spend, 0.10)
fair_whole = (end_a + end_b) / 2
print(f'FAIR (central, shown growth): ends at 10% {end_a:.0f} and {end_b:.0f}; avg {fair_whole:.0f}; per share {ps(fair_whole):.2f}; without PGA as debt {ps(fair_whole, debt-cash):.2f}')
end_b2 = pv_case(oc_ae, g_cut, growth_spend, 0.10)
print(f'FAIR (cut growth): per share {ps((end_a + end_b2) / 2):.2f}')
eq_a = nogrowth(oc_eq, 0.10)
eq_b = pv_case(oc_eq, g_end, growth_spend, 0.10)
print(f'FAIR equity-only: ends {eq_a:.0f} and {eq_b:.0f}; per share {((eq_a + eq_b) / 2 + nol_pv) / shares:.2f}')
lo_hi = sorted([ps(nogrowth(oc_ae, r_t)), ps(pv_case(oc_ae, g_end, growth_spend, r_t))])
print(f'RANGE per share at {r_t:.2%}: {lo_hi[0]:.2f} to {lo_hi[1]:.2f} against {price}')
lo_hi_eq = sorted([(nogrowth(oc_eq, r_t) + nol_pv) / shares, (pv_case(oc_eq, g_end, growth_spend, r_t) + nol_pv) / shares])
print(f'RANGE equity-only at {r_t:.2%}: {lo_hi_eq[0]:.2f} to {lo_hi_eq[1]:.2f}')
print(f'yield at the price: central {oc_ae/ev:.2%}; generous NI-based {oc_gen/ev:.2%}; generous without PGA as debt {oc_gen/(mcap+debt-cash-nol_pv):.2%}')
def npv(r, oc, g, spend): return pv_case(oc, g, spend, r) - ev
lo, hi = 0.001, 0.5
gg = min(g_nopat, 0.0999)
for _ in range(200):
    mid = (lo + hi) / 2
    if npv(mid, oc_gen, gg, growth_spend) > 0:
        lo = mid
    else:
        hi = mid
print(f'IRR at the price, generous growth case (g={gg:.2%}, growth spending charged): {lo:.2%}')
lo, hi = 0.001, 0.5
for _ in range(200):
    mid = (lo + hi) / 2
    if npv(mid, oc_gen, gg, 0.0) > 0:
        lo = mid
    else:
        hi = mid
print(f'IRR at the price, most generous case (NI-based owner cash at g={gg:.2%} for ten years, NO growth spending charged): {lo:.2%}')
eq_b2 = pv_case(oc_eq, g_cut, growth_spend, 0.10)
print(f'FAIR equity-only (cut growth): per share {((eq_a + eq_b2) / 2 + nol_pv) / shares:.2f}')
lo_hi_eq2 = sorted([(nogrowth(oc_eq, r_t) + nol_pv) / shares, (pv_case(oc_eq, g_cut, growth_spend, r_t) + nol_pv) / shares])
print(f'RANGE equity-only (cut growth) at {r_t:.2%}: {lo_hi_eq2[0]:.2f} to {lo_hi_eq2[1]:.2f}')
print(f'cap test: owner cash year 10 at shown growth {oc_ae*(1+g_end)**10:.1f} against sales year 10 at sales growth {rev[-1]*(1+g_sales)**10:.1f} = {oc_ae*(1+g_end)**10/(rev[-1]*(1+g_sales)**10):.1%}; highest share in window {max(rows[i]["ae_dna"]/rev[i] for i in range(5)):.1%}')
