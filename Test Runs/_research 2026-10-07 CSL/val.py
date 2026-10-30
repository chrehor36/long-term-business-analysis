"""CSL run 2026-10-07: owner cash for the continuing business and the Q7 arithmetic.
Every input is a filed figure (accessions in the run file). Arithmetic only; no verdict."""

# continuing-operations owner cash, all-equity basis, USD millions
# OCF total (cash-flow statements) less OCF of discontinued operations (Note 4 / disc-ops notes)
ocf_total = {2021: 421.7, 2022: 1000.9, 2023: 1201.3, 2024: 1030.3, 2025: 1101.8}
ocf_disc = {2021: 89.6, 2022: 60.5, 2023: 164.1, 2024: -8.9, 2025: -1.8}
sbc_cont = {2021: 27.0, 2022: 25.0, 2023: 31.7, 2024: 32.9, 2025: 34.8}   # stock-pay note, continuing
capex_cont = {2021: 105.5, 2022: 158.8, 2023: 110.8, 2024: 100.9, 2025: 131.2}  # segment note totals
int_exp = {2021: 80.2, 2022: 85.9, 2023: 75.6, 2024: 73.3, 2025: 78.5}
int_inc = {2021: 1.1, 2022: 6.8, 2023: 20.1, 2024: 60.3, 2025: 25.9}
etr = {2021: 104.3 / 489.9, 2022: 265.7 / 1123.7, 2023: 211.5 / 930.4, 2024: 245.8 / 1110.9, 2025: 206.3 / 948.8}
acq = {2021: 1571.3, 2022: 24.7, 2023: 36.1, 2024: 676.9, 2025: 109.6}  # cash paid for businesses, continuing
TAXCREDIT_2025 = 125.0  # accrued liability for a transferable energy tax credit acquired in 2025, settled after year-end (10-Q Q2 2026)

oc = {}
print('year  OCFcont   SBC   capex  ATnetint  owner cash (all-equity)  equity-only')
for y in range(2021, 2026):
    ocfc = ocf_total[y] - ocf_disc[y]
    atint = (int_exp[y] - int_inc[y]) * (1 - etr[y])
    eq = ocfc - sbc_cont[y] - capex_cont[y]
    ae = eq + atint
    if y == 2025:
        eq -= TAXCREDIT_2025
        ae -= TAXCREDIT_2025
    oc[y] = (ae, eq)
    print(f'{y}  {ocfc:7.1f} {sbc_cont[y]:6.1f} {capex_cont[y]:7.1f} {atint:8.1f}   {ae:8.1f}   {eq:8.1f}')


def avg(ys, k=0):
    return sum(oc[y][k] for y in ys) / len(ys)


lit = avg(range(2021, 2026)); cyc = avg(range(2022, 2026))
lit_eq = avg(range(2021, 2026), 1); cyc_eq = avg(range(2022, 2026), 1)
print(f'literal window 2021-25 mean: all-equity {lit:.1f}, equity-only {lit_eq:.1f}')
print(f'cycle base 2022-25 mean:     all-equity {cyc:.1f}, equity-only {cyc_eq:.1f}')
acq_lit = sum(acq.values()) / 5; acq_cyc = sum(acq[y] for y in range(2022, 2026)) / 4
print(f'acquisitions mean: literal {acq_lit:.1f}, cycle {acq_cyc:.1f}')

# growth measures
h1 = (oc[2021][0] + oc[2022][0]) / 2; h2 = (oc[2024][0] + oc[2025][0]) / 2
print(f'halves growth literal window (2021-22 vs 2024-25, 3 yrs): {(h2 / h1) ** (1 / 3) - 1:.4f}')
c1 = (oc[2022][0] + oc[2023][0]) / 2; c2 = (oc[2024][0] + oc[2025][0]) / 2
print(f'halves growth cycle base (2022-23 vs 2024-25, 2 yrs): {(c2 / c1) ** (1 / 2) - 1:.4f}')
print(f'end-year growth cycle base 2022->2025: {(oc[2025][0] / oc[2022][0]) ** (1 / 3) - 1:.4f}')
# organic revenue growth as the filer reports it (continuing): 2022 CCM +37.3% on 2,846.2 and CWT +13.6% on 990.5;
# 2023 CCM -16.3% on 3,885.2, CWT -14.7% on 1,564.2; 2024 consolidated organic; 2025 consolidated -2.9%
org22 = (2846.2 * 0.373 + 990.5 * 0.136) / (2846.2 + 990.5)
org23 = (3885.2 * -0.163 + 1564.2 * -0.147) / (3885.2 + 1564.2)
org24 = (5003.6 - 4586.9 - 86.9 - 1.3) / 4586.9   # 2024 change less MTL and PFB contributions (Note 3)
org25 = -0.029
f = (1 + org22) * (1 + org23) * (1 + org24) * (1 + org25)
print(f'organic: 2022 {org22:.4f} 2023 {org23:.4f} 2024 {org24:.4f} 2025 {org25:.4f}; 2021-25 CAGR {f ** 0.25 - 1:.4f}; 2022-25 CAGR {((1+org23)*(1+org24)*(1+org25)) ** (1/3) - 1:.4f}')

R = 0.0564
NETDEBT = 2889.9 - 665.3   # 10-Q 2026-06-30: total debt less cash; no securities; operating leases left out
SH = 39.714133
MCAP = 325.74 * SH


def pv(c, g, r=R, n=10):
    v = 0.0; cf = c
    for t in range(1, n + 1):
        cf *= (1 + g); v += cf / (1 + r) ** t
    return v + cf / r / (1 + r) ** n


def stream(c, g, n=10):
    out = []; cf = c
    for t in range(1, n + 1):
        cf *= (1 + g); out.append(cf)
    return out, cf


def pv_mid(cases, r):
    # the midpoint stream: the year-by-year average of the two end streams, the terminal at no growth
    (s1, t1), (s2, t2) = [stream(c, g) for c, g in cases]
    v = sum(((a + b) / 2) / (1 + r) ** (i + 1) for i, (a, b) in enumerate(zip(s1, s2)))
    return v + ((t1 + t2) / 2) / r / (1 + r) ** 10


def irr_of(cases, price_ev):
    lo, hi = 0.0, 0.5
    for _ in range(200):
        m = (lo + hi) / 2
        if pv_mid(cases, m) > price_ev: lo = m
        else: hi = m
    return m


print(f'\nmarket cap {MCAP:.0f}, net debt {NETDEBT:.1f}, EV {MCAP + NETDEBT:.0f}')
UNCRED = 0.0  # set below
# CCM margin, current segment basis: 2022-25 = sum OI / sum revenue; pre-change 2020-21 recast
ccm_rev = [3885.2, 3253.4, 3704.3, 3721.7]; ccm_oi = [1175.0, 913.9, 1084.3, 997.2]
m_new = sum(ccm_oi) / sum(ccm_rev); m_old = (524.2 + 619.9) / (2335.4 + 2846.2)
cut = (m_new - m_old) * (sum(ccm_rev) / 4) * (1 - sum(etr[y] for y in range(2022, 2026)) / 4)
print(f'CCM margin 2022-25 {m_new:.4f}, 2020-21 recast {m_old:.4f}; after-tax owner cash not credited: {cut:.1f}')
uncred = cyc - cut
cases = {
    'A credited, cycle base, no growth': (cyc, 0.0),
    'B credited, cycle base, organic 2021-25 growth': (cyc, f ** 0.25 - 1),
    'C uncredited (CCM at 2020-21 margin), no growth': (uncred, 0.0),
    'D default pair: cycle base less acquisitions, total growth (end years 2022-25)': (cyc - acq_cyc, (oc[2025][0] / oc[2022][0]) ** (1 / 3) - 1),
    'E literal window 2021-25, no growth': (lit, 0.0),
    'F literal window less acquisitions, halves growth 2021-25': (lit - acq_lit, (h2 / h1) ** (1 / 3) - 1),
}
vals = {}
for k, (c, g) in cases.items():
    ev = pv(c, g); eq = ev - NETDEBT
    vals[k] = (c, g, ev, eq / SH)
    print(f'{k}: C={c:.1f} g={g:.4f}  EV={ev:,.0f}  per share ${eq / SH:,.2f}')

for lo_k, hi_k in [('C uncredited (CCM at 2020-21 margin), no growth', 'B credited, cycle base, organic 2021-25 growth')]:
    lo = cases[lo_k]; hi = cases[hi_k]
    lo_ps = vals[lo_k][3]; hi_ps = vals[hi_k][3]
    print(f'\nRANGE (all-equity): ${lo_ps:,.2f} to ${hi_ps:,.2f}; width {hi_ps / lo_ps:.2f} to one; midpoint ${(lo_ps + hi_ps) / 2:,.2f}')
    fair_ev = pv_mid([lo, hi], 0.10); print(f'fair EV at 10%: {fair_ev:,.0f}; fair price all-equity ${(fair_ev - NETDEBT) / SH:,.2f}')
    print(f'expected return at the price (midpoint stream, all-equity): {irr_of([lo, hi], MCAP + NETDEBT):.4f}')
    print(f'expected return at the price, top case alone: {irr_of([hi, hi], MCAP + NETDEBT):.4f}; bottom alone: {irr_of([lo, lo], MCAP + NETDEBT):.4f}')
    # equity-only: owner cash after interest at today's debt: subtract after-tax interest on today's debt
    at_int_now = (2900 * 0.0 + 27.4 * 4 - 6.6 * 4) * (1 - 0.232)  # Q2 2026 run-rate net interest x4, at the 23.2% anticipated rate
    lo_e = (lo[0] - at_int_now, lo[1]); hi_e = (hi[0] - at_int_now, hi[1])
    fair_eq = pv_mid([lo_e, hi_e], 0.10)
    print(f'equity-only: after-tax net interest run-rate {at_int_now:.1f}; range ${pv(*lo_e) / SH:,.2f} to ${pv(*hi_e) / SH:,.2f}; fair price equity-only ${fair_eq / SH:,.2f}; expected return at price {irr_of([lo_e, hi_e], MCAP):.4f}')

# ---- the central construction used in the run file (Q7) ----
print('\n==== Q7 CENTRAL CONSTRUCTION ====')
dep = {2024: 70.2, 2025: 74.6}  # cash-flow statement depreciation (2024 includes CIT to 2024-05-21)
maint = 74.6  # maintenance guess: 2025 depreciation, the continuing business alone
growth_capex = sum(capex_cont[y] for y in range(2022, 2026)) / 4 - maint
print(f'capex 2022-25 mean {sum(capex_cont[y] for y in range(2022, 2026)) / 4:.1f}; maintenance (2025 depreciation) {maint}; growth and cost-reduction spending {growth_capex:.1f}')
CWT_SHARE = sum([128.6, 187.9, 173.6, 101.9]) / sum([128.6, 187.9, 173.6, 101.9] + ccm_oi)
print(f'CWT share of 2022-25 segment operating income {CWT_SHARE:.4f} (carried at no growth)')


def stream2(c_all, g, extra, n=10):
    """years 1-10: CCM share grows at g, CWT share flat, all spending charged; after year 10 no growth,
    so the growth spending stops (maintenance-only from year 11)."""
    out = []
    for t in range(1, n + 1):
        out.append(c_all * (1 - CWT_SHARE) * (1 + g) ** t + c_all * CWT_SHARE)
    term = out[-1] + extra
    return out, term


def pv2(s, r):
    cf, term = s
    return sum(x / (1 + r) ** (i + 1) for i, x in enumerate(cf)) + term / r / (1 + r) ** len(cf)


def mid(s1, s2):
    return [(a + b) / 2 for a, b in zip(s1[0], s2[0])], (s1[1] + s2[1]) / 2


def irr2(s, target):
    lo, hi = 0.0, 0.5
    for _ in range(200):
        m = (lo + hi) / 2
        if pv2(s, m) > target: lo = m
        else: hi = m
    return m


g_org = f ** 0.25 - 1
bottom = stream2(uncred + growth_capex, 0.0, 0.0)          # uncredited margin, no growth, maintenance only
top = stream2(cyc, g_org, growth_capex)                     # credited, organic growth, growth spending charged in years 1-10
lit_lo = stream2(lit + growth_capex, 0.0, 0.0)              # literal window, no growth, maintenance only
cyc_lo = stream2(cyc + growth_capex, 0.0, 0.0)              # credited, no growth, maintenance only
allsp_top = stream2(cyc, g_org, 0.0)                        # all-spending top (growth capex never stops)
EV_P = MCAP + NETDEBT
for name, s in [('BOTTOM uncredited no growth (maint only)', bottom), ('TOP credited organic growth', top),
                ('credited no growth (maint only)', cyc_lo), ('literal window no growth (maint only)', lit_lo),
                ('all-spending top, beside', allsp_top)]:
    ev = pv2(s, R)
    print(f'{name}: year-1 cash {s[0][0]:.1f}; EV {ev:,.0f}; per share ${(ev - NETDEBT) / SH:,.2f}; return at price {irr2(s, EV_P):.4f}')
lo_ps = (pv2(bottom, R) - NETDEBT) / SH; hi_ps = (pv2(top, R) - NETDEBT) / SH
print(f'RANGE all-equity ${lo_ps:,.2f} to ${hi_ps:,.2f}; width {hi_ps / lo_ps:.2f}:1; midpoint ${(lo_ps + hi_ps) / 2:,.2f}')
m = mid(bottom, top)
fair_ev = pv2(m, 0.10)
print(f'FAIR PRICE all-equity: EV {fair_ev:,.0f} less net debt -> ${(fair_ev - NETDEBT) / SH:,.2f}; expected return at the price {irr2(m, EV_P):.4f}')
# equity-only: owner cash after interest at the Q2 2026 run-rate of net interest, against market value alone
ati = (27.4 - 6.6) * 4 * (1 - 0.232)
b_e = stream2(uncred + growth_capex - ati, 0.0, 0.0)
t_e = ([x - ati for x in top[0]], top[1] - ati)
lo_e = pv2(b_e, R) / SH; hi_e = pv2(t_e, R) / SH
m_e = mid(b_e, t_e)
print(f'EQUITY-ONLY: after-tax interest {ati:.1f}; range ${lo_e:,.2f} to ${hi_e:,.2f}; fair price ${pv2(m_e, 0.10) / SH:,.2f}; expected return at price {irr2(m_e, MCAP):.4f}')
# old-basis sensitivity: CCM at its 2007-2016 mean margin
old = [14.0, 10.3, 13.8, 13.0, 12.0, 16.1, 14.9, 13.9, 17.5, 21.0]
m_oldbasis = sum(old) / len(old) / 100
cut2 = (m_new - m_oldbasis) * (sum(ccm_rev) / 4) * (1 - sum(etr[y] for y in range(2022, 2026)) / 4)
s_old = stream2(cyc - cut2 + growth_capex, 0.0, 0.0)
print(f'old-basis CCM margin {m_oldbasis:.4f}: owner cash {cyc - cut2:.1f}; per share ${(pv2(s_old, R) - NETDEBT) / SH:,.2f}')

# ---- the default pair (specific (c)): acquisitions deducted, total growth credited; (e) maintenance-only central ----
print('\n==== DEFAULT PAIR, as the brief and Q7 (c) name it ====')
g_tot = (oc[2025][0] / oc[2022][0]) ** (1 / 3) - 1
spend = acq_cyc + growth_capex
print(f'total growth of aggregate owner cash 2022->2025 (end years): {g_tot:.4f}; acquisitions + growth spending per year {spend:.1f}')


def stream3(c_base, g, n=10):
    """years 1-10: owner cash after maintenance, CCM share grown at g, CWT flat, less acquisitions and growth spending;
    after year 10 no growth, so the growth spending and acquisitions stop."""
    out = [c_base * (1 - CWT_SHARE) * (1 + g) ** t + c_base * CWT_SHARE - spend for t in range(1, n + 1)]
    return out, out[-1] + spend


cases3 = {
    'credited, no growth, maintenance only (no purchases)': stream2(cyc + growth_capex, 0.0, 0.0),
    'credited, total growth, purchases deducted': stream3(cyc + growth_capex, g_tot),
    'uncredited, no growth, maintenance only': stream2(uncred + growth_capex, 0.0, 0.0),
    'uncredited, total growth, purchases deducted': stream3(uncred + growth_capex, g_tot),
    'literal window 2021-25, no growth, maintenance only': stream2(lit + growth_capex, 0.0, 0.0),
    'organic pair beside: credited, organic growth, growth spending charged': top,
}
ps = {}
for k, s in cases3.items():
    ev = pv2(s, R); ps[k] = (ev - NETDEBT) / SH
    print(f'{k}: yr1 {s[0][0]:.1f}; EV {ev:,.0f}; ${ps[k]:,.2f}; return at price {irr2(s, EV_P):.4f}')
B = cases3['uncredited, total growth, purchases deducted']; T = cases3['credited, no growth, maintenance only (no purchases)']
lo_ps = (pv2(B, R) - NETDEBT) / SH; hi_ps = (pv2(T, R) - NETDEBT) / SH
print(f'RANGE (default pair, change not credited at the bottom): ${lo_ps:,.2f} to ${hi_ps:,.2f}; width {hi_ps / lo_ps:.2f}:1; midpoint ${(lo_ps + hi_ps) / 2:,.2f}')
M = mid(B, T)
fev = pv2(M, 0.10)
print(f'FAIR PRICE all-equity ${(fev - NETDEBT) / SH:,.2f} (fair EV {fev:,.0f}); expected return at the price on the midpoint stream {irr2(M, EV_P):.4f}')
Be = ([x - ati for x in B[0]], B[1] - ati); Te = ([x - ati for x in T[0]], T[1] - ati)
Me = mid(Be, Te)
print(f'EQUITY-ONLY range ${pv2(Be, R) / SH:,.2f} to ${pv2(Te, R) / SH:,.2f}; fair price ${pv2(Me, 0.10) / SH:,.2f}; expected return at the price {irr2(Me, MCAP):.4f}')
# credited-only range (if the change were credited): the two credited cases
Bc = cases3['credited, total growth, purchases deducted']
print(f'credited-only default pair: ${(pv2(Bc, R) - NETDEBT) / SH:,.2f} to ${hi_ps:,.2f}; fair ${(pv2(mid(Bc, T), 0.10) - NETDEBT) / SH:,.2f}')
