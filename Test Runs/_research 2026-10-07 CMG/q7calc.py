# CMG Q7 arithmetic (COMPUTATION). USD millions unless per share. Inputs from series.py (filed 10-K figures).
# Owner cash before interest = OCF - SBC - spending - interest income x (1 - effective tax rate)  [all-equity basis]
# Owner cash after interest  = OCF - SBC - spending                                             [equity-only basis]
r = 0.0564          # US Treasury 30-year par yield, 2026-10-06
floor = 0.10        # Q7 floor CONVENTION, about ten percent, after the company's own tax
shares = 1265.418   # cover, 2026-07-24
netcash = 775.0     # 2026-06-30: cash 228.2 + current investments 449.7 + long-term investments 97.1; no borrowings
price = 30.90

ocf  = {2015:683.3,2016:355.2,2017:468.2,2018:621.6,2019:721.6,2020:663.8,2021:1282.1,2022:1323.2,2023:1783.5,2024:2105.1,2025:2113.9}
sbc  = {2015:57.9,2016:64.2,2017:65.3,2018:69.2,2019:91.4,2020:82.6,2021:176.4,2022:98.0,2023:124.0,2024:131.7,2025:119.5}
capex= {2015:257.4,2016:258.8,2017:216.8,2018:287.4,2019:333.9,2020:373.4,2021:442.5,2022:479.2,2023:560.7,2024:593.6,2025:666.3}
da   = {2015:130.4,2016:146.4,2017:163.3,2018:202.0,2019:212.8,2020:238.5,2021:254.7,2022:286.8,2023:319.4,2024:335.0,2025:361.4}
inti = {2015:6.3,2016:4.2,2017:4.9,2018:10.1,2019:14.3,2020:3.6,2021:7.8,2022:21.1,2023:62.7,2024:93.9,2025:73.7}
tax  = {2015:0.382,2016:0.408,2017:0.36,2018:0.0,2019:0.236,2020:0.0,2021:0.197,2022:0.239,2023:0.242,2024:0.237,2025:0.236}
# (2018 and 2020 effective rates were negative on stock-pay and tax-law items; interest taken untaxed there: immaterial)

def A(y, before=True): return ocf[y]-sbc[y]-capex[y]-(inti[y]*(1-tax[y]) if before else 0)
def M(y, before=True): return ocf[y]-sbc[y]-da[y]-(inti[y]*(1-tax[y]) if before else 0)
def avg(f, ys, before=True): return sum(f(y,before) for y in ys)/len(ys)

def pv_flat(c, rate): return c/rate
def pv_growth(c0_years, m0, g, rate, years=10):
    """years 1-10: all-spending cash c0*(1+g)^t; after year 10 no growth and no growth spending: maintenance cash m0*(1+g)^10, flat."""
    v = sum(c0_years*(1+g)**t/(1+rate)**t for t in range(1, years+1))
    v += (m0*(1+g)**years/rate)/(1+rate)**years
    return v
def pv_growth_simple(c0, g, rate, years=10):
    v = sum(c0*(1+g)**t/(1+rate)**t for t in range(1, years+1))
    return v + (c0*(1+g)**years/rate)/(1+rate)**years

W = [2021,2022,2023,2024,2025]
print("Owner cash by year (before interest): all-spending / maintenance-only (D&A)")
for y in range(2015,2026): print(f"  {y}: {A(y):8.1f}  {M(y):8.1f}   after interest: {A(y,False):8.1f}  {M(y,False):8.1f}")
A0, M0 = avg(A,W), avg(M,W)
A0e, M0e = avg(A,W,False), avg(M,W,False)
g_lit = (A(2025)/A(2021))**(1/4)-1
g_litM = (M(2025)/M(2021))**(1/4)-1
g_pp = (A(2024)/A(2015))**(1/9)-1      # peak to peak, 2015 -> 2024 (cycle reading, specific (a))
g_ppM = (M(2024)/M(2015))**(1/9)-1
print(f"\n5-yr avg 2021-2025 before interest: all-spending {A0:.1f}, maintenance {M0:.1f}; after interest {A0e:.1f}, {M0e:.1f}")
print(f"growth shown, literal window 2021->2025: all-spending {g_lit*100:.1f}%, maintenance {g_litM*100:.1f}%")
print(f"growth shown, peak to peak 2015->2024: all-spending {g_pp*100:.1f}%, maintenance {g_ppM*100:.1f}%")
cyc = list(range(2015,2025))
print(f"cycle average 2015-2024 before interest: all-spending {avg(A,cyc):.1f}, maintenance {avg(M,cyc):.1f}")

def per_share(v, eq_only=False): return (v + (0 if eq_only else netcash))/shares

def show(label, bottom, top):
    b, t = per_share(bottom), per_share(top)
    print(f"{label:72s} bottom ${b:6.2f}  top ${t:6.2f}  width {t/b:4.2f}:1")
    return b, t

print(f"\nRANGES, all-equity basis (per share = (value + net cash {netcash}) / {shares}M), sovereign {r*100:.2f}%")
cases = {}
cases['L'] = show("1. literal window, all-spending both ends, g 17.9%", pv_flat(A0,r), pv_growth_simple(A0,g_lit,r))
cases['E'] = show("2. specific (e): bottom maintenance no-growth; top all-spending g 17.9%, maint. after yr 10", pv_flat(M0,r), pv_growth(A0,M0,g_lit,r))
cases['P'] = show("3. (e) with peak-to-peak growth 2015->2024", pv_flat(M0,r), pv_growth(A0,M0,g_pp,r))
# Q3 cap: owner-cash growth at most unit growth plus average-sales growth once margin is at its peak.
# CONVENTION of this run: the cap is computed from the filer's own figures: the 7,000 goal is for the U.S. and Canada;
# the US count 3,938 is used as the base because Canada's count is not filed (overstates unit growth slightly, in the business's favour)
# (5.9%/yr) plus international and partner units, plus average restaurant sales growth 2015-2025 (2.0%/yr).
g_units = (7000/3938)**(1/10)-1
g_auv = (3.104/2.532)**(1/10)-1
g_cap = (1+g_units)*(1+g_auv)-1
print(f"\nQ3 cap: units {g_units*100:.1f}%/yr (3,938 US -> 7,000 goal in 10 yrs) x average sales {g_auv*100:.1f}%/yr = {g_cap*100:.1f}%/yr")
cases['C'] = show(f"4. (e) with growth capped by Q3 at {g_cap*100:.1f}%", pv_flat(M0,r), pv_growth(A0,M0,g_cap,r))
cases['C1'] = show(f"5. all-spending both ends, growth capped {g_cap*100:.1f}%", pv_flat(A0,r), pv_growth_simple(A0,g_cap,r))

# Fair price: price at which the midpoint of the range earns the floor.
# The midpoint value is matched to a growth rate on the chosen case's construction, then that cash stream is valued at the floor.
def solve_g(target, fn):
    lo, hi = -0.5, 0.5
    for _ in range(200):
        mid=(lo+hi)/2
        if fn(mid) < target: lo=mid
        else: hi=mid
    return (lo+hi)/2
print("\nFAIR PRICE (midpoint of the range earning the 10% floor)")
for key, mk_top, mk_bot, lab in [
    ('E', lambda g,rt: pv_growth(A0,M0,g,rt), lambda rt: pv_flat(M0,rt), "case 2 (literal growth, (e))"),
    ('C', lambda g,rt: pv_growth(A0,M0,g,rt), lambda rt: pv_flat(M0,rt), "case 4 (Q3 cap, (e))"),
    ('L', lambda g,rt: pv_growth_simple(A0,g,rt), lambda rt: pv_flat(A0,rt), "case 1 (literal, all-spending)")]:
    b, t = cases[key]
    midv = (b+t)/2*shares - netcash
    g_mid = solve_g(midv, lambda g: mk_top(g, r))
    fair = (mk_top(g_mid, floor) + netcash)/shares
    print(f"  {lab:34s} midpoint ${(b+t)/2:6.2f}/sh  (growth {g_mid*100:.1f}% at the sovereign)  fair at 10%: ${fair:6.2f}  all-equity")
# equity-only figures: owner cash after interest, no net cash added
print("\nEQUITY-ONLY (owner cash after interest; market value of the shares only)")
for lab, bot, top in [("case 2", pv_flat(M0e,r), pv_growth(A0e,M0e,g_lit,r)), ("case 4", pv_flat(M0e,r), pv_growth(A0e,M0e,g_cap,r))]:
    b,t = bot/shares, top/shares
    midv=(b+t)/2*shares
    gm = solve_g(midv, lambda g: pv_growth(A0e,M0e,g,r))
    fair = pv_growth(A0e,M0e,gm,floor)/shares
    print(f"  {lab}: ${b:6.2f} to ${t:6.2f}, width {t/b:.2f}:1; fair at 10% ${fair:6.2f}")
# what return does the price imply? solve growth the price implies at the sovereign and the return at the central case
ev = price*shares - netcash
print(f"\nPrice ${price}: market value {price*shares:,.0f}M, EV {ev:,.0f}M")
g_impl = solve_g(ev, lambda g: pv_growth(A0,M0,g,r))
print(f"growth the price implies at the sovereign on construction (e): {g_impl*100:.1f}%/yr for ten years")
def irr(fn):
    lo,hi=0.0,0.5
    for _ in range(200):
        mid=(lo+hi)/2
        if fn(mid)>ev: lo=mid
        else: hi=mid
    return (lo+hi)/2
for lab,g in [("no growth (maint.)",None),(f"Q3 cap {g_cap*100:.1f}%",g_cap),(f"literal {g_lit*100:.1f}%",g_lit),(f"peak-to-peak {g_pp*100:.1f}%",g_pp)]:
    f = (lambda rt: pv_flat(M0,rt)) if g is None else (lambda rt, g=g: pv_growth(A0,M0,g,rt))
    print(f"  expected return at ${price} if owner cash follows {lab}: {irr(f)*100:.1f}%")
# Q6 test: buyback prices against the bottom of the range
print("\nBuyback average prices (split-adjusted, 10-K Note 7 / 10-Q): 2023 $36.55, 2024 $57.21, 2025 $42.54, H1 2026 $34.35, Q2 2026 $32.55")
