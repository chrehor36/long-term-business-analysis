# Q7 computation for VSEC, 2026-10-16. Arithmetic only; every input is a filed figure cited in the run file.
r = 0.0543          # US Treasury 30-year par yield, 2026-10-15
floor = 0.10
price = 164.08
shares = 28.064972 + 1.415752 + 2.4472   # cover + exchangeable subsidiary shares + TEU at max rate
debt = 32.004 + 914.953                   # 10-Q 2026-06-30 balance sheet
cash = 75.360
net_debt = debt - cash
earnout = 33.850

# VSE continuing operations, FY2023-FY2025 (FY2025 10-K), USD millions
vse = {
 2023: dict(rev=544.020, opinc=50.145, addback=0.0,  tax=4.495/19.060, da=23.416-7.314, amort=11.742, capex=18.666-2.280, wc=-92.424),
 2024: dict(rev=786.256, opinc=58.756, addback=12.205, tax=4.407/23.809, da=28.762-2.951, amort=17.625, capex=20.704-2.343, wc=-106.859),
 2025: dict(rev=1112.275, opinc=89.595, addback=29.200, tax=15.546/69.039, da=39.924-0.731, amort=25.995, capex=21.281-0.208, wc=-113.128),
}
# PAG audited statements (8-K 2026-05-07, Ex. 99.2)
pag = {
 2024: dict(rev=472.049, opinc=63.233, addback=0.0, tax=0.25, da=14.081, amort=14.081-6.420, capex=10.580, wc=-7.499),
 2025: dict(rev=595.562, opinc=92.400, addback=0.0, tax=0.25, da=25.485, amort=25.485-9.465, capex=16.026, wc=-15.615),
}
def series(d, amort_addback=True):
    out = {}
    for y, x in d.items():
        nopat = (x['opinc'] + x['addback']) * (1 - x['tax'])
        dep = x['da'] - x['amort']
        maint = nopat + x['da'] - dep if amort_addback else nopat + x['da'] - x['da']  # capex at depreciation (+amort add-back) or at full D&A
        allsp = nopat + x['da'] - x['capex'] + x['wc']
        out[y] = dict(maint=maint, allsp=allsp, rev=x['rev'], growth_capex=x['capex'] - dep)
    return out
def avg(s, k): return sum(v[k] for v in s.values()) / len(s)

def value(C0, R0, g, spend_per_dR, rate, years=10):
    pv = 0.0; C = C0; R = R0
    for t in range(1, years + 1):
        Rn = R * (1 + g); Cn = C * (1 + g)
        cf = Cn - spend_per_dR * (Rn - R)
        pv += cf / (1 + rate) ** t
        R, C = Rn, Cn
    tv = C / rate  # zero nominal growth after year ten, growth spending stops
    return pv + tv / (1 + rate) ** years

for addback in (True, False):
    v = series(vse, addback); p = series(pag, addback)
    C0 = avg(v, 'maint') + avg(p, 'maint')
    A0 = avg(v, 'allsp') + avg(p, 'allsp')
    R0 = avg(v, 'rev') + avg(p, 'rev')
    wc_int = (190.732 + 41.468 + 553.834 - 154.506 - 73.161) / 1112.275   # FY2025 year-end working capital / revenue
    dR = (1112.275 - 544.020) / 2
    gcap = avg(v, 'growth_capex') / dR
    spend = wc_int + gcap
    print(f"\n=== amortization added back: {addback}")
    for y in v: print('VSE', y, {k: round(val, 1) for k, val in v[y].items()})
    for y in p: print('PAG', y, {k: round(val, 1) for k, val in p[y].items()})
    print(f"C0 maintenance-only {C0:.1f}  all-spending {A0:.1f}  R0 {R0:.1f}  WC intensity {wc_int:.3f}  growth capex per dR {gcap:.3f}")
    for g in (0.0, 0.11, 0.14):
        for rate in (r, floor):
            ev = value(C0, R0, g, spend, rate)
            print(f"g={g:.2f} rate={rate:.4f}: EV {ev:,.0f}  equity {ev-net_debt:,.0f}  per share {(ev-net_debt)/shares:,.2f}")
    # implied return at the price for the growth case (bisection)
    target = price * shares + net_debt
    for g in (0.0, 0.14):
        lo, hi = 0.001, 0.5
        for _ in range(100):
            mid = (lo + hi) / 2
            if value(C0, R0, g, spend, mid) > target: lo = mid
            else: hi = mid
        print(f"expected return at ${price} (all-equity), g={g}: {mid*100:.2f}%")
    # equity-only: owner cash after the company's after-tax interest (pro forma 2025 interest 56.725, at 25%)
    I = 56.725 * 0.75
    for g in (0.0, 0.14):
        for rate in (r, floor):
            ev = value(C0, R0, g, spend, rate) - I / rate
            print(f"EQUITY-ONLY g={g:.2f} rate={rate:.4f}: equity {ev:,.0f} per share {ev/shares:,.2f}")
    lo_ae = (value(C0, R0, 0.0, spend, floor) - net_debt) / shares
    hi_ae = (value(C0, R0, 0.14, spend, floor) - net_debt) / shares
    lo_eo = (value(C0, R0, 0.0, spend, floor) - I / floor) / shares
    hi_eo = (value(C0, R0, 0.14, spend, floor) - I / floor) / shares
    print(f"FAIR all-equity {(lo_ae+hi_ae)/2:.2f}  equity-only {(lo_eo+hi_eo)/2:.2f}")
print(f"\nshares {shares:.6f}M  net debt {net_debt:.1f}  market value {price*shares:,.1f}  earn-out obligation beside {earnout}")
