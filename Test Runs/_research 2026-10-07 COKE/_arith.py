# Arithmetic for the COKE run of 2026-10-07. Every input is a filed figure (USD millions unless stated); sources in the run file.
# Nothing here is a verdict. After the Q2 stop every figure is COMPUTATION, NOT A CLEARANCE.
r = 0.0564          # 30-year US Treasury par yield, 2026-10-06 (tools/sources.py)
floor = 0.10        # Q7 floor CONVENTION, about ten percent
shares = 66.564294  # million, cover of 10-Q filed 2026-08-05 (56,517,334 Common + 10,046,960 Class B)
price = 194.61
# --- price per case (bottle/can sales / bottle/can physical cases, 10-K MD&A tables)
bc = {2019: 4141.422, 2020: 4402.543, 2021: 4882.049, 2022: 5541.373, 2023: 6041.772, 2024: 6333.316, 2025: 6612.720}
cases = {2019: 358.812/1.045, 2020: 358.812, 2021: 366.036, 2022: 362.191, 2023: 355.367, 2024: 353.103, 2025: 354.048}
print('price per case:', {y: round(bc[y]/cases[y], 2) for y in bc})
print('price/case 2019->2025 %.1f%%; cases %.1f%%' % (100*(bc[2025]/cases[2025]/(bc[2019]/cases[2019])-1), 100*(cases[2025]/cases[2019]-1)))
# --- owner cash after every real cost (equity basis = after interest, as OCF is):
# OCF - capex + PP&E sale proceeds - sub-bottling payments (financing) - finance lease principal - distribution rights bought
oc_rows = {
 2019: (290.370, 171.374, 4.064, 27.182, 0.0, 0.0),
 2020: (494.461, 202.034, 3.385, 43.400, 5.861, 0.0),
 2021: (521.755, 155.693, 5.274, 39.097, 4.778, 8.993),
 2022: (554.506, 298.611, 7.369, 36.515, 2.988, 30.649),
 2023: (810.690, 282.304, 0.695, 28.208, 2.303, 0.0),
 2024: (876.357, 371.015, 0.569, 64.312, 2.488, 0.0),
 2025: (931.904, 312.315, 6.594, 68.884, 1.809, 0.0),
}
oc = {y: a - b + c - d - e - f for y, (a, b, c, d, e, f) in oc_rows.items()}
# after-tax net interest added back for the all-equity basis (interest expense, net, income statement; tax at 26%, the 2024-25 effective rate)
netint = {2019: 45.990, 2020: 36.735, 2021: 33.449, 2022: 24.792, 2023: -0.918, 2024: 1.848, 2025: 42.678}
ocu = {y: oc[y] + netint[y]*(1-0.26) for y in oc}
dep = {2021: 157.320, 2022: 147.962, 2023: 153.472, 2024: 170.343, 2025: 195.081}
ocd = {y: oc[y] + oc_rows[y][1] - oc_rows[y][2] - dep[y] for y in dep}   # depreciation in place of capex
for y in sorted(oc): print(y, 'owner cash (after interest) %.1f  before interest %.1f' % (oc[y], ocu[y]), ' depreciation variant %.1f' % ocd[y] if y in ocd else '')
W = range(2021, 2026)
base_eq = sum(oc[y] for y in W)/5; base_ae = sum(ocu[y] for y in W)/5; base_dep = sum(ocd[y] for y in W)/5
g_shown = (oc[2025]/oc[2021])**0.25 - 1; g_shown_u = (ocu[2025]/ocu[2021])**0.25 - 1
sales = {2021: 5562.714, 2025: 7228.055}; g_sales = (sales[2025]/sales[2021])**0.25 - 1
print('5-yr base: equity %.1f  all-equity %.1f  depreciation variant (equity) %.1f' % (base_eq, base_ae, base_dep))
print('growth shown 2021->2025: equity %.1f%%  all-equity %.1f%%; net sales %.1f%%' % (100*g_shown, 100*g_shown_u, 100*g_sales))
def pv(base, g, rate, n=10):
    v = 0; c = base
    for t in range(1, n+1):
        c = c*(1+g); v += c/(1+rate)**t
    return v + (c/rate)/(1+rate)**n
nd = 100.0 + 2413.112 + 0.422 + 1.047 - 171.687   # debt + finance leases - cash, 10-Q at 2026-07-03; no stated subsequent events
print('net debt %.1f' % nd)
for label, base, g in [('all-equity', base_ae, g_sales), ('all-equity literal growth', base_ae, g_shown_u)]:
    lo = pv(base, 0, r); hi = pv(base, g, r)
    print(label, 'EV range %.0f to %.0f (x%.2f); per share %.2f to %.2f' % (lo, hi, hi/lo, (lo-nd)/shares, (hi-nd)/shares))
for label, base, g in [('equity-only', base_eq, g_sales), ('equity-only literal', base_eq, g_shown)]:
    lo = pv(base, 0, r); hi = pv(base, g, r)
    print(label, 'range %.0f to %.0f (x%.2f); per share %.2f to %.2f' % (lo, hi, hi/lo, lo/shares, hi/shares))
# fair price: the stream whose value at the sovereign is the midpoint of the range, discounted at the floor
def solve_g(base, target):
    lo, hi = -0.5, 0.5
    for _ in range(200):
        m = (lo+hi)/2
        if pv(base, m, r) < target: lo = m
        else: hi = m
    return m
for label, base, g, debt in [('all-equity', base_ae, g_sales, nd), ('equity-only', base_eq, g_sales, 0.0)]:
    mid = (pv(base, 0, r) + pv(base, g, r))/2; gm = solve_g(base, mid); fair = pv(base, gm, floor)
    print(label, 'midpoint %.0f (growth %.2f%%); value of that stream at the floor %.0f; fair price per share %.2f' % (mid, 100*gm, fair, (fair-debt)/shares))
# what the price implies: owner-cash yield
ev = price*shares + nd
print('market cap %.0f  EV %.0f  yield all-equity %.2f%%  equity-only %.2f%%' % (price*shares, ev, 100*base_ae/ev, 100*base_eq/(price*shares)))
print('2025 alone: all-equity yield %.2f%%' % (100*ocu[2025]/ev))
# buyback prices (post-split dollars)
print('KO 2024: $925 pre-split = $92.50; KO 2025: 2400/18.83546 = $%.2f; open market 2025: 212.0/1.778081 = $%.2f' % (2400/18.83546, 212.0/1.778081))
# expansion paid, 2014-2017 net cash prices (10-K FY2017 table) and sub-bottling paid since
exp = [12.2,30.9,13.2,18.0,7.0,15.3,26.7,5.4,75.9,34.8,68.5,99.7,32.1,104.6,87.9,15.9,39.6,3.4]
sb = [24.683, 27.182, 43.400, 39.097, 36.515, 28.208, 64.312, 68.884]
print('expansion net cash %.1f; sub-bottling paid 2018-2025 %.1f' % (sum(exp), sum(sb)))
# depreciation variant beside (capital spending replaced by depreciation of PP&E), all-equity basis
ocdu = {y: ocd[y] + netint[y]*(1-0.26) for y in ocd}
base_dep_u = sum(ocdu[y] for y in W)/5; g_dep = (ocdu[2025]/ocdu[2021])**0.25 - 1
lo = pv(base_dep_u, 0, r); hi = pv(base_dep_u, g_sales, r)
mid = (lo+hi)/2; gm = solve_g(base_dep_u, mid); fair = pv(base_dep_u, gm, floor)
print('depreciation variant all-equity: base %.1f (shown growth %.1f%%), per share %.2f to %.2f, fair price %.2f' % (base_dep_u, 100*g_dep, (lo-nd)/shares, (hi-nd)/shares, (fair-nd)/shares))
# contract interest due 2026 on today's debt, for the equity-only figure read against today's balance sheet
print('equity-only base less the after-tax rise in interest to the 2026 contractual figure: %.1f' % (base_eq - (138.7 - sum(netint[y] for y in W)/5)*(1-0.26)))
