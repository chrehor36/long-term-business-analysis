# CPK run 2026-10-17: arithmetic for Q3, Q4, Q7. Figures in USD millions from the filed statements
# (10-K FY2025 0001628280-26-011753 for 2023-2025; 10-K FY2022 0001628280-23-004607 for 2021-2022).
yrs = [2021, 2022, 2023, 2024, 2025]
ocf   = [150.5, 158.9, 203.5, 239.4, 233.7]
sbc   = [5.9, 6.4, 7.6, 8.4, 8.5]
capex = [186.9, 128.3, 188.6, 355.3, 448.6]
acq   = [36.4, 11.8, 925.0, -0.6, 0.0]
da    = [62.7, 69.0, 65.5, 65.7, 91.7]        # D&A line
dao   = [10.2, 11.0, 11.9, 15.8, 15.9]        # depreciation and accretion in operations expenses
rsam  = [0.0, 0.0, 0.0, 15.5, 0.0]            # FCG RSAM benefit that lowered 2024 D&A (10-K FY2025 MD&A note 2)
intpd = [20.8, 24.3, 30.5, 73.0, 73.2]        # interest paid (XBRL InterestPaid, supplemental)
pti   = [112.7, 123.6, 115.3, 161.8, 193.0]
tax   = [29.2, 33.8, 28.1, 43.2, 52.7]
opinc = [131.1, 142.9, 150.8, 228.2, 255.9]
oth   = [1.7, 5.1, 1.4, 2.0, 9.6]
ni    = [83.5, 89.8, 87.2, 118.6, 140.3]
t = [tx/p for tx, p in zip(tax, pti)]
maint = [a + b + c for a, b, c in zip(da, dao, rsam)]
oc_m_eq = [o - s - m for o, s, m in zip(ocf, sbc, maint)]
aft_int = [i * (1 - tr) for i, tr in zip(intpd, t)]
oc_m_u = [x + a for x, a in zip(oc_m_eq, aft_int)]
oc_all_eq = [o - s - c for o, s, c in zip(ocf, sbc, capex)]
oc_all_u = [x + a for x, a in zip(oc_all_eq, aft_int)]
oc_all_u_acq = [x - q for x, q in zip(oc_all_u, acq)]
growth_sp = [c - m for c, m in zip(capex, maint)]
def show(name, s):
    print(f"{name:34s}", " ".join(f"{v:8.1f}" for v in s), f" avg {sum(s)/len(s):8.1f}")
print("year".ljust(34), " ".join(f"{y:8d}" for y in yrs))
show("effective tax rate %", [100*x for x in t])
show("maintenance guess (D&A+O&M dep+RSAM)", maint)
show("OC maint, equity (after interest)", oc_m_eq)
show("after-tax interest paid", aft_int)
show("OC maint, all-equity", oc_m_u)
show("OC all capex, equity", oc_all_eq)
show("OC all capex, all-equity", oc_all_u)
show("  same less acquisitions", oc_all_u_acq)
show("growth spending (capex - maint)", growth_sp)
nopat = [(o + x) * (1 - tr) for o, x, tr in zip(opinc, oth, t)]
show("NOPAT (op inc + other) x (1-t)", nopat)
# capital employed
eq = {2020: 697.0, 2021: 774.0, 2022: 832.7, 2023: 1246.1, 2024: 1390.2, 2025: 1598.5}
debt = {2021: 550.0 + 18.0 + 222.0 - 5.0, 2025: 1327.1 + 134.6 + 158.0 - 1.8}
ce21 = eq[2021] + debt[2021]; ce25 = eq[2025] + debt[2025]
print(f"capital employed 2021 {ce21:.1f}  2025 {ce25:.1f}; NOPAT 2021 {nopat[0]:.1f} 2025 {nopat[-1]:.1f}")
print(f"return on incremental capital 2021->2025: {(nopat[-1]-nopat[0])/(ce25-ce21)*100:.2f}%")
gw = 507.5 - 45.0
print(f"same, goodwill added in window ({gw:.1f}) taken out: {(nopat[-1]-nopat[0])/(ce25-ce21-gw)*100:.2f}%")
print(f"return on capital employed 2025: {nopat[-1]/ce25*100:.2f}%  2021: {nopat[0]/ce21*100:.2f}%")
roe = [n/((a+b)/2) for n, a, b in zip(ni, [eq[y-1] for y in yrs], [eq[y] for y in yrs])]
show("ROE on average equity %", [100*x for x in roe])

# ---- Q7 ----
price = 132.18; sh = 24.106455
mcap = price * sh
nd = 1317.9 + 131.7 + 238.1 - 0.4      # 10-Q 2026-06-30
ev = mcap + nd
print(f"\nmarket cap {mcap:.1f}  net debt {nd:.1f}  EV {ev:.1f}")
r = 0.0543
def pva(rate, n=10): return (1 - (1 + rate) ** -n) / rate
def value(base, rate, G=0.0, R=0.0):
    # base owner cash, no growth; growth programme: G spent each year for ten years, each earning R for ever from the next year;
    # spending stops after year ten (purchases and growth stop together).
    v0 = base / rate
    v_g = (R / rate - 1) * G * pva(rate) if G else 0.0
    return v0 + v_g
B5 = sum(oc_m_u) / 5
B2 = sum(oc_m_u[-2:]) / 2
G5 = sum(growth_sp) / 5
R_shown = (nopat[-1]-nopat[0])/(ce25-ce21)
R_allow = 0.50 * 0.0975 + 0.50 * 0.0525 * (1 - 0.26)   # CONVENTION of this run: about half equity at the allowed ROE band, half debt at the filed coupon band
print(f"base 5yr {B5:.1f}  base 2yr {B2:.1f}  growth spend avg {G5:.1f}  R shown {R_shown*100:.2f}%  R allowed {R_allow*100:.2f}%")
def ps(evv): return (evv - nd) / sh
cases = {}
for nm, base, G, R in [("no growth, 5yr base", B5, 0, 0), ("growth at allowed R, 5yr base", B5, G5, R_allow),
                       ("growth at shown R, 5yr base", B5, G5, R_shown),
                       ("no growth, post-FCG 2yr base", B2, 0, 0), ("growth at allowed R, post-FCG base", B2, G5, R_allow),
                       ("2025 NOPAT, no growth", nopat[-1], 0, 0),
                       ("2025 NOPAT, 2026 guidance growth 465/yr at allowed R", nopat[-1], 465.0, R_allow)]:
    v = value(base, r, G, R); v10 = value(base, 0.10, G, R)
    cases[nm] = (ps(v), ps(v10))
    print(f"{nm:52s} sovereign: EV {v:8.1f}  per share {ps(v):7.2f} | at 10%: EV {v10:8.1f} per share {ps(v10):7.2f}")
lo, hi = cases["no growth, 5yr base"][0], cases["growth at allowed R, 5yr base"][0]
print(f"\nCENTRAL RANGE all-equity: {lo:.2f} to {hi:.2f}  width {hi/lo:.2f}x")
fair = (cases["no growth, 5yr base"][1] + cases["growth at allowed R, 5yr base"][1]) / 2
print(f"FAIR PRICE all-equity (ends at 10%, averaged): {fair:.2f}")
# expected return at the price for the most generous case: solve rate where value = EV
def solve(base, G, R):
    lo_, hi_ = 0.001, 0.5
    for _ in range(200):
        m = (lo_ + hi_) / 2
        if value(base, m, G, R) > ev: lo_ = m
        else: hi_ = m
    return m
for nm, base, G, R in [("5yr base no growth", B5, 0, 0), ("5yr base growth allowed R", B5, G5, R_allow),
                       ("2025 NOPAT + guidance growth allowed R", nopat[-1], 465.0, R_allow)]:
    print(f"expected return at the price, {nm}: {solve(base, G, R)*100:.2f}%")
# equity-only
E5 = sum(oc_m_eq) / 5
roe_allow = 0.0975
def veq(base, rate, G=0.0, Req=0.0, eqshare=0.5):
    return base / rate + ((Req / rate - 1) * G * eqshare * pva(rate) if G else 0.0)
e_lo = veq(E5, r) / sh; e_hi = veq(E5, r, G5, roe_allow) / sh
e_lo10 = veq(E5, 0.10) / sh; e_hi10 = veq(E5, 0.10, G5, roe_allow) / sh
print(f"\nEQUITY-ONLY base {E5:.1f}: range {e_lo:.2f} to {e_hi:.2f}; at 10%: {e_lo10:.2f} and {e_hi10:.2f}; fair {(e_lo10+e_hi10)/2:.2f}")
print(f"earnings yields at price: NI2025/mcap {ni[-1]/mcap*100:.2f}%  NOPAT2025/EV {nopat[-1]/ev*100:.2f}%  OC maint eq avg/mcap {E5/mcap*100:.2f}%")
# all-spending case, literal window (b): series changes sign
print(f"all-spending all-equity avg {sum(oc_all_u)/5:.1f} (changes sign): range is the no-growth case alone; value {sum(oc_all_u)/5/r:.1f} EV -> per share {ps(sum(oc_all_u)/5/r):.2f}")
print(f"default pair, acquisitions deducted: avg {sum(oc_all_u_acq)/5:.1f}")
print(f"serial-acquirer test: net purchases {sum(acq):.1f} vs half of OC before purchases (maint, all-equity) {sum(oc_m_u)/2:.1f}")
