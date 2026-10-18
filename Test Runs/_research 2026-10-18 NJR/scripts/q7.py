"""NJR owner cash and Q7 range. Every input is transcribed from the filed cash-flow statements (USD millions)."""
# FY: OCF, SBC, utility, solar, S&T/other, cost of removal, equity-investee net (+in/-out), acquisitions(-)/disposals(+), interest paid, D&A, revenue
D = {
 2016: dict(ocf=142.630, sbc=7.234, cap=176.067+149.063+0+29.066, eqi=-11.176+2.351, deals=0.748, intr=31.996, da=72.748),
 2017: dict(ocf=248.046, sbc=5.807, cap=144.106+149.400+0+32.143, eqi=-27.070+2.749, deals=-55.661+9.443, intr=44.362, da=81.841),
 2018: dict(ocf=398.286, sbc=12.845, cap=206.880+123.421+6.644+47.643, eqi=-16.151+3.117, deals=-10.000+27.916, intr=44.821, da=85.701),
 2019: dict(ocf=194.128, sbc=9.796, cap=304.809+157.828+23.100+40.195, eqi=-4.102+2.428, deals=205.745, intr=50.371, da=91.730),
 2020: dict(ocf=213.481, sbc=6.536, cap=290.040+133.841+24.228+22.059, eqi=-2.117+1.907, deals=-523.647, intr=66.146, da=119.894),
 2021: dict(ocf=390.954, sbc=7.149, cap=376.312+87.852+110.130+50.316, eqi=-0.690+3.183, deals=0.0, intr=78.650, da=111.387),
 2022: dict(ocf=323.480, sbc=14.827, cap=259.081+146.676+153.378+39.293, eqi=5.479+2.336, deals=0.0, intr=84.375, da=129.249),
 2023: dict(ocf=478.993, sbc=14.716, cap=350.304+107.303+42.757+40.555, eqi=2.294, deals=0.0, intr=108.194, da=152.941),
 2024: dict(ocf=427.407, sbc=16.028, cap=372.019+104.287+46.628+48.385, eqi=2.246, deals=0.0, intr=120.239, da=166.567),
 2025: dict(ocf=466.349, sbc=17.779, cap=391.906+238.185+29.957+46.030, eqi=0.612, deals=137.195, intr=130.333, da=188.774),
}
COR = {2016:29.066,2017:32.143,2018:47.643,2019:40.195,2020:22.059,2021:50.316,2022:39.293,2023:40.555,2024:48.385,2025:46.030}
T = 0.25   # CONVENTION of the run: interest shield at 21% federal plus the filer's state-net-of-federal line (about 4 points), window average
R = 0.0543 # US Treasury 30-year par yield, 2026-10-16
F = 0.10
SH = 101.467946  # cover count, 2026-07-31
ND = 3200.089 + 282.881 + 220.000 - 33.955  # LTD + current maturities + short-term debt - cash, 10-Q 2026-06-30
P = 52.19
rows = {}
print(f"{'FY':>4} {'OCF':>8} {'SBC':>6} {'capex':>8} {'OCall_eq':>9} {'OCall_ae':>9} {'OCmnt_eq':>9} {'OCmnt_ae':>9} {'gr_cap':>8}")
for y, d in D.items():
    allsp_eq = d['ocf'] - d['sbc'] - d['cap'] + d['eqi'] + d['deals']
    shield = d['intr'] * (1 - T)
    mnt_eq = d['ocf'] - d['sbc'] - d['da'] - COR[y]
    rows[y] = dict(all_eq=allsp_eq, all_ae=allsp_eq + shield, mnt_eq=mnt_eq, mnt_ae=mnt_eq + shield, growth_cap=(mnt_eq - allsp_eq))
    print(f"{y:>4} {d['ocf']:8.1f} {d['sbc']:6.1f} {d['cap']:8.1f} {allsp_eq:9.1f} {allsp_eq+shield:9.1f} {mnt_eq:9.1f} {mnt_eq+shield:9.1f} {mnt_eq-allsp_eq:8.1f}")
W = [2021, 2022, 2023, 2024, 2025]
avg = lambda k: sum(rows[y][k] for y in W) / len(W)
A = {k: avg(k) for k in ['all_eq', 'all_ae', 'mnt_eq', 'mnt_ae', 'growth_cap']}
print('5-yr averages FY2021-25:', {k: round(v, 1) for k, v in A.items()})
A10 = {k: sum(rows[y][k] for y in D)/10 for k in ['all_eq','all_ae','mnt_eq','mnt_ae']}
print('10-yr averages FY2016-25 (literal window beside):', {k: round(v, 1) for k, v in A10.items()})
# growth of maintenance owner cash, all-equity, end-years and halves
g_end = (rows[2025]['mnt_ae'] / rows[2021]['mnt_ae']) ** (1/4) - 1
h1 = (rows[2021]['mnt_ae'] + rows[2022]['mnt_ae']) / 2; h2 = (rows[2024]['mnt_ae'] + rows[2025]['mnt_ae']) / 2
g_half = (h2 / h1) ** (1/3) - 1
print(f"maintenance OC (all-equity) growth: end-years {g_end:.2%}, halves {g_half:.2%}")
def pv(cf0, g, r, years=10, spend=0.0):
    """cash flow cf0 grown at g for 10 years, minus flat 'spend' in years 1-10, then cf at year 10 held flat forever."""
    v = 0; cf = cf0
    for t in range(1, years + 1):
        cf = cf * (1 + g); v += (cf - spend) / (1 + r) ** t
    v += cf / r / (1 + r) ** years
    return v
def per_share(ev, basis):
    return (ev - (ND if basis == 'ae' else 0)) / SH
for basis in ['ae', 'eq']:
    m = A['mnt_' + basis]; gc = A['growth_cap']
    top = pv(m, 0.0, R)              # maintenance-only, no growth (central, filing allows the guess as depreciation proxy)
    grow = pv(m, g_half, R, spend=gc)  # growth credited at the shown rate, growth spending charged years 1-10, stops after year ten
    allnog = A['all_' + basis] / R     # all spending, no growth, forever (the literal all-spending case)
    print(f"[{basis}] top (mnt, no growth) EV {top:8.0f} -> ${per_share(top, basis):7.2f}/sh;  growth case EV {grow:8.0f} -> ${per_share(grow, basis):7.2f}/sh;  all-spend no-growth EV {allnog:8.0f} -> ${per_share(allnog, basis):7.2f}/sh")
    ftop = pv(m, 0.0, F); fgrow = pv(m, g_half, F, spend=gc)
    print(f"[{basis}] fair price: top@10% ${per_share(ftop, basis):7.2f}, growth@10% ${per_share(fgrow, basis):7.2f}, average ${ (per_share(ftop, basis)+per_share(fgrow, basis))/2:7.2f}")
mcap = P * SH; ev = mcap + ND
print(f"price {P}, shares {SH}M, mcap {mcap:.0f}, net debt {ND:.1f}, EV {ev:.0f}")
print(f"yield at price: maintenance all-equity {A['mnt_ae']/ev:.2%}; equity-only {A['mnt_eq']/mcap:.2%}; all-spending all-equity {A['all_ae']/ev:.2%}")
# generous test, the forbidden double count, only to show the floor cannot be reached: maintenance OC grown at the halves rate with no growth spending charged
for basis, base in [('ae', ev), ('eq', mcap)]:
    m = A['mnt_' + basis]
    lo, hi = 0.0, 0.5
    for _ in range(80):
        mid = (lo + hi) / 2
        (lo, hi) = (mid, hi) if pv(m, g_half, mid) > base else (lo, mid)
    print(f"[{basis}] IRR at price if maintenance OC grows {g_half:.2%} ten years with NO growth spending charged (not a case, a ceiling): {lo:.2%}")
