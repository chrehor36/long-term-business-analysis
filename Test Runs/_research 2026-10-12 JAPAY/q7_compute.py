# Q7 COMPUTATION, NOT A CLEARANCE: JAPAY. Figures in JPY billions, from the filed cash-flow statements
# (Annual Securities Reports FY2022 (2021, 2022), FY2024 (2023, 2024), FY2025 (2025)); see the run file for sources.
years = [2021, 2022, 2023, 2024, 2025]
ocf   = [598.909, 483.799, 566.317, 630.011, 514.056]
ppe   = [86.350, 81.411, 94.861, 127.769, 143.204]
intan = [16.568, 17.997, 21.707, 22.598, 19.182]
lease = [20.449, 21.009, 23.613, 26.218, 24.787]
nci   = [1.958, 1.536, 2.594, 2.701, 2.691]
int_paid = [19.113, 23.728, 26.324, 33.980, 64.041]
int_recd = [19.245, 25.530, 41.189, 65.353, 111.202]
# acquisitions net of disposals (positive = cash out): business combinations, subsequent payments, associates bought,
# less proceeds from subsidiaries/associates sold and the pharmaceutical business transfer
acq = [-2.562, -(2.963 + 0.063), -1.369, 265.667 - 0.414, 68.271 + 24.752 - 2.272 - 42.811]
# Canada settlement cash paid in 2025 (cash-flow statement: decrease in provisions 177.164, settlement liabilities 49.645)
canada_2025 = 177.164 + 49.645

eq = [o - p - i - l - n for o, p, i, l, n in zip(ocf, ppe, intan, lease, nci)]
ue = [e + ip - ir for e, ip, ir in zip(eq, int_paid, int_recd)]
def show(name, s):
    print(f"{name:42s}", ' '.join(f'{x:8.1f}' for x in s), f' avg {sum(s)/len(s):8.1f}')
show('equity owner cash (literal)', eq)
show('all-equity owner cash (literal)', ue)
ue_adj = ue[:4] + [ue[4] + canada_2025]
eq_adj = eq[:4] + [eq[4] + canada_2025]
show('all-equity, 2025 Canada payment added back', ue_adj)
show('acquisitions net of disposals', acq)
ue_net = [u - a for u, a in zip(ue_adj, acq)]
eq_net = [u - a for u, a in zip(eq_adj, acq)]
ue_net_lit = [u - a for u, a in zip(ue, acq)]
show('CENTRAL: all-equity, Canada adj, after acq', ue_net)
show('equity-only, Canada adj, after acq', eq_net)
show('literal: all-equity, after acq', ue_net_lit)
show('before acquisitions (organic-type pair)', ue_adj)

def g(s):
    return (s[-1] / s[0]) ** (1 / 4) - 1 if s[0] > 0 and s[-1] > 0 else None
def halves(s):
    a = sum(s[:2]) / 2; b = sum(s[3:]) / 2  # first two vs last two years, midpoints 3 years apart
    return (b / a) ** (1 / 3) - 1
for nm, s in [('central', ue_net), ('equity', eq_net), ('literal', ue_net_lit), ('pre-acq', ue_adj)]:
    print(nm, 'end-year CAGR', None if g(s) is None else round(g(s) * 100, 2), '% ; halves', round(halves(s) * 100, 2), '%')

ADDBACK = 0.0  # purchases stop after year ten (section E of the 2026-10-10 case): terminal on cash before purchases
def pv(c, gr, r, years=10):
    v = 0.0; x = c
    for t in range(1, years + 1):
        x *= (1 + gr); v += x / (1 + r) ** t
    return v + (x + ADDBACK) / r / (1 + r) ** years

shares = 1776.000893  # million shares outstanding at 2026-06-30 (2,000,000,000 issued less 223,999,107 treasury)
price = 7230.0
debt = 117.087 + 1559.685          # bonds and borrowings, 2026-06-30
cash = 827.909
secs = 181.105 + 10.459 - (246.301 - 241.958)  # time deposits + debt securities 2025-12-31, less H1 2026 net withdrawal
canada_liab = 161.267              # settlement liabilities on litigation in Canada, 2026-06-30
iran_cash = 166.162                # cash held by Iranian subsidiaries, 2026-06-30
nd = debt - cash - secs + canada_liab
print(f'net debt central {nd:.1f}; excl. Iran cash from cash {nd + iran_cash:.1f}; without Canada {nd - canada_liab:.1f}')
mcap = shares * price / 1000
print(f'market cap {mcap:.1f} bn; EV {mcap + nd:.1f}')

def report(label, c, gr, netdebt, r):
    top = pv(c, 0.0, r); bot = pv(c, gr, r) if gr is not None else top
    lo, hi = sorted([bot, top])
    print(f'{label}: C={c:.1f} g={gr*100 if gr is not None else 0:.2f}% r={r*100:.2f}%  range EV {lo:.0f}-{hi:.0f}; per share {(lo-netdebt)/shares*1000:.0f}-{(hi-netdebt)/shares*1000:.0f}')
    return lo, hi

C = sum(ue_net) / 5; G = g(ue_net)
ADDBACK = sum(acq) / 5
print('purchases added back after year ten:', round(ADDBACK,1))
print('--- central (all-equity) ---')
report('at JGB 4.14%', C, G, nd, 0.0414)
report('at UST 5.60% (beside)', C, G, nd, 0.056)
lo10, hi10 = report('at 10% (fair price)', C, G, nd, 0.10)
fair = ((lo10 + hi10) / 2 - nd) / shares * 1000
print(f'FAIR PRICE all-equity: {fair:.0f} yen/share; per ADS {fair/2:.0f} yen')
print(f'expected yield at price, no-growth case: {C/(mcap+nd)*100:.2f}%')
# return at the price that makes PV = EV for the no-growth case = C/EV; for growth case solve r
def irr(c, gr, target):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        m = (lo + hi) / 2
        if pv(c, gr, m) > target: lo = m
        else: hi = m
    return m
print(f'return at price: no-growth {irr(C,0.0,mcap+nd)*100:.2f}%, shown-growth {irr(C,G,mcap+nd)*100:.2f}%')
print('--- equity-only ---')
ADDBACK = sum(acq) / 5
Ce = sum(eq_net) / 5; Ge = g(eq_net)
report('equity at 4.14%', Ce, Ge, canada_liab, 0.0414)
lo, hi = report('equity at 10%', Ce, Ge, canada_liab, 0.10)
print(f'FAIR PRICE equity-only: {((lo+hi)/2 - canada_liab)/shares*1000:.0f} yen/share')
print(f'return at price equity: no-growth {irr(Ce,0.0,mcap+canada_liab)*100:.2f}%, shown {irr(Ce,Ge,mcap+canada_liab)*100:.2f}%')
print('--- literal window beside ---')
ADDBACK = sum(acq) / 5
Cl = sum(ue_net_lit) / 5; Gl = g(ue_net_lit)
report('literal at 4.14%', Cl, Gl, nd - canada_liab, 0.0414)
lo, hi = report('literal at 10%', Cl, Gl, nd - canada_liab, 0.10)
print(f'fair literal: {((lo+hi)/2 - (nd - canada_liab))/shares*1000:.0f}')
print('--- before acquisitions: no purchases at all ---')
ADDBACK = 0.0
Cp = sum(ue_adj) / 5
report('pre-acq no growth 4.14%', Cp, 0.0, nd, 0.0414)
print('--- depreciation variant: capex replaced by D&A ex-leases (IR table) ---')
ADDBACK = sum(acq) / 5
da = [167.099, 176.888, 153.341, 148.421, 165.291]
capex_cash = [p + i for p, i in zip(ppe, intan)]
diff = [d - c for d, c in zip(da, capex_cash)]
print('D&A - cash capex by year', [round(x, 1) for x in diff], 'avg', round(sum(diff)/5, 1))
Cd = C - sum(diff) / 5
report('depreciation variant 4.14%', Cd, G, nd, 0.0414)
print('--- Iran cash excluded from cash ---')
report('central, Iran cash out, 4.14%', C, G, nd + iran_cash, 0.0414)
lo, hi = report('central, Iran cash out, 10%', C, G, nd + iran_cash, 0.10)
print(f'fair (Iran cash out): {((lo+hi)/2 - nd - iran_cash)/shares*1000:.0f}')
ADDBACK = sum(acq) / 5
# growth needed for the price: shown growth for ten years that makes PV at 10% equal EV
lo_g, hi_g = -0.5, 1.0
for _ in range(200):
    m = (lo_g + hi_g) / 2
    if pv(C, m, 0.10) < mcap + nd: lo_g = m
    else: hi_g = m
print(f'ten-year growth needed to earn 10% at the price: {m*100:.1f}% a year')
