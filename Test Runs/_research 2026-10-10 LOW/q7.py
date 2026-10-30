# Q7 arithmetic for the LOW run (v5 Q7 CONVENTION construction and its six specifics). Arithmetic only; the run file
# states every choice. USD millions. Inputs transcribed from the filed cash-flow and income statements (10-Ks named in
# the run file); interest-net = operating income - pre-tax earnings; tax rate = provision / pre-tax.
R = 0.056          # 30-year Treasury par yield, 2026-10-09 (Step 0)
FLOOR = 0.10       # the floor CONVENTION, about ten percent
SH = 561.054019    # shares, millions (10-Q cover, 2026-08-25)
PRICE = 186.00

# fiscal: (OCF, SBC, capex, opinc, pretax, tax, acquisitions paid, proceeds from sale of business)
D = {
 2011: (4349, 107, 1829, 3279, 2906, 1067, 100, 0),
 2012: (3762, 100, 1211, 3562, 3137, 1178, 0, 0),
 2013: (4111, 100, 940, 4150, 3673, 1387, 203, 0),
 2014: (4929, 119, 880, 4792, 4276, 1578, 0, 0),
 2015: (4784, 117, 1197, 4971, 4419, 1873, 0, 0),
 2016: (5617, 90, 1167, 5846, 5201, 2108, 2356, 0),
 2017: (5065, 99, 1123, 6586, 5489, 2042, 509, 0),
 2018: (6193, 74, 1174, 4018, 3394, 1080, 0, 0),
 2019: (4296, 98, 1484, 6314, 5623, 1342, 0, 0),
 2020: (11049, 155, 1791, 9647, 7739, 1904, 0, 0),
 2021: (10113, 230, 1853, 12093, 11208, 2766, 0, 0),
 2022: (8589, 223, 1829, 10159, 9036, 2599, 0, 0),
 2023: (8140, 210, 1964, 11557, 10175, 2449, 0, 100),
 2024: (9625, 221, 1927, 10466, 9153, 2196, 0, 177),
 2025: (9864, 247, 2213, 10153, 8747, 2093, 10088, 0),
}

def rows():
    out = {}
    for y, (ocf, sbc, capex, oi, pt, tx, acq, sold) in D.items():
        oc = ocf - sbc - capex                     # owner cash, equity basis (after interest)
        intr = oi - pt                             # interest, net
        t = tx / pt
        u = oc + intr * (1 - t)                    # owner cash before interest, after the company's tax (all-equity)
        netacq = acq - sold
        out[y] = dict(oc=oc, intr=intr, t=t, u=u, acq=netacq, u_acq=u - netacq, oc_acq=oc - netacq)
    return out

def value(c0, g, r=R, years=10):
    """c0 grown at g for ten years then flat (zero nominal growth), discounted at r. Year 1 cash = c0*(1+g)."""
    v = 0.0; c = c0
    for t in range(1, years + 1):
        c = c * (1 + g)
        v += c / (1 + r) ** t
    v += (c / r) / (1 + r) ** years
    return v

def solve_g_for_value(c0, target, r=R):
    lo, hi = -0.5, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(c0, mid, r) < target: lo = mid
        else: hi = mid
    return (lo + hi) / 2

def cagr(a, b, n):
    if a <= 0 or b <= 0: return None
    return (b / a) ** (1 / n) - 1

def mean(xs): return sum(xs) / len(xs)

if __name__ == "__main__":
    X = rows()
    print("fiscal  owner_cash  interest  tax%  unlevered  net_acq  unlev-acq")
    for y in sorted(X):
        r_ = X[y]
        print(f"{y}  {r_['oc']:9.0f}  {r_['intr']:8.0f}  {100*r_['t']:4.1f}  {r_['u']:9.0f}  {r_['acq']:7.0f}  {r_['u_acq']:9.0f}")

    NET_DEBT = 37556 - (3172 + 235)      # 10-Q 2026-07-31: debt (current 2,352 + long-term 35,204) less cash and short-term investments
    NET_DEBT_YE = 39921 - (982 + 370)    # 10-K 2026-01-30, shown beside
    print("\nnet debt 2026-07-31:", NET_DEBT, " at 2026-01-30:", NET_DEBT_YE)

    def report(label, base, g, nd=NET_DEBT, equity_only=False):
        lo_g, hi_g = (min(0.0, g), max(0.0, g))
        v0 = value(base, lo_g); v1 = value(base, hi_g)
        vmid = (v0 + v1) / 2
        gm = solve_g_for_value(base, vmid)
        fair_whole = value(base, gm, FLOOR)
        sub = 0 if equity_only else nd
        ps = lambda v: (v - sub) / SH
        print(f"\n{label}: base {base:,.0f}  g {100*g:.2f}%")
        print(f"  range (whole {'equity' if equity_only else 'business'}) {v0:,.0f} .. {v1:,.0f}; per share {ps(v0):,.2f} .. {ps(v1):,.2f}; width {max(v0,v1)/min(v0,v1) if min(v0,v1)>0 else float('nan'):.2f}x (per share {max(ps(v0),ps(v1))/min(ps(v0),ps(v1)) if min(ps(v0),ps(v1))>0 else float('nan'):.2f}x)")
        print(f"  midpoint {vmid:,.0f} -> {ps(vmid):,.2f}/sh; midpoint stream growth {100*gm:.2f}%; fair price (stream at 10%) {ps(fair_whole):,.2f}/sh")
        mcap = PRICE * SH
        ev = mcap + sub
        print(f"  at ${PRICE}: market value {ev:,.0f}; year-one cash yield {base/ev*100:.2f}%")
        return v0, v1, ps(fair_whole)

    yrs5 = [2021, 2022, 2023, 2024, 2025]
    cyc = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
    prev = [2012, 2013, 2014, 2015, 2016, 2017, 2018]

    for basis, key, key_acq, eq in (("ALL-EQUITY", "u", "u_acq", False), ("EQUITY-ONLY", "oc", "oc_acq", True)):
        print(f"\n================ {basis} ================")
        # literal window
        lit = [X[y][key_acq] for y in yrs5]
        lit_g = cagr(X[2021][key], X[2025][key], 4)
        print("literal 5-yr window, acquisitions deducted, mean", round(mean(lit)), "total growth end-to-end", None if lit_g is None else round(100*lit_g, 2))
        report("LITERAL WINDOW (acq deducted, total growth)", mean(lit), lit_g if lit_g is not None else 0.0, equity_only=eq)
        # cycle base, default pair: acquisitions deducted, total growth between successive cycle averages
        cb = mean([X[y][key_acq] for y in cyc]); pb = mean([X[y][key_acq] for y in prev])
        g_cyc = cagr(pb, cb, 7)
        report("CYCLE BASE fiscal 2019-2025 (acq deducted, growth between cycle averages)", cb, g_cyc, equity_only=eq)
        # organic pair: acquisitions left out, organic growth only (comparable sales, compounded, as the filer reports it)
        cb_o = mean([X[y][key] for y in cyc])
        comps = {2019: 2.6, 2020: 26.1, 2021: 6.9, 2022: -0.9, 2023: -4.7, 2024: -2.7, 2025: 0.2,
                 2012: 1.4, 2013: 4.8, 2014: 4.3, 2015: 4.8, 2016: 4.2, 2017: 4.0, 2018: 2.4}
        p = 1
        for y in range(2019, 2026): p *= 1 + comps[y] / 100
        g_org = p ** (1 / 7) - 1
        report("ORGANIC PAIR: cycle base, acquisitions left out, comparable-sales growth fiscal 2019-2025", cb_o, g_org, equity_only=eq)

# ---- second pass (the run file's stated construction) ----
if __name__ == "__main__":
    print("\n\n######## STATED CONSTRUCTION ########")
    X = rows()
    sales = {2012:50521,2013:53417,2014:56223,2015:59074,2016:65017,2017:68619,2018:71309,
             2019:72148,2020:89597,2021:96250,2022:97059,2023:86377,2024:83674,2025:86286}
    prev=[2012,2013,2014,2015,2016,2017,2018]; cyc=[2019,2020,2021,2022,2023,2024,2025]
    s_prev=mean([sales[y] for y in prev]); s_cyc=mean([sales[y] for y in cyc])
    g_sales=cagr(s_prev,s_cyc,7)
    print(f"sales cycle averages {s_prev:,.0f} -> {s_cyc:,.0f}; total sales growth {100*g_sales:.2f}%")
    # implied margin check for the uncut owner-cash growth
    for key,lab in (("u_acq","all-equity, acq deducted"),("oc_acq","equity-only, acq deducted")):
        pb=mean([X[y][key] for y in prev]); cb=mean([X[y][key] for y in cyc]); g=cagr(pb,cb,7)
        ratio10=((1+g)/(1+g_sales))**10
        print(f"{lab}: owner cash/sales at cycle {cb/s_cyc*100:.2f}%; uncut growth {100*g:.2f}% implies x{ratio10:.2f} on owner cash/sales by year ten -> {cb/s_cyc*100*ratio10:.2f}%")
    FBM_AFTER_TAX = (-28 + 192) * 2 * (1 - 0.239)   # H1 fiscal 2026 'Other' operating income before amortization, annualised, after tax
    print(f"FBM+ADG on filed record (annualised H1 FY2026, before amortization, after tax): {FBM_AFTER_TAX:,.0f}")
    NET_DEBT = 37556 - (3172 + 235)
    comps={2019:2.6,2020:26.1,2021:6.9,2022:-0.9,2023:-4.7,2024:-2.7,2025:0.2}
    p=1
    for y in cyc: p*=1+comps[y]/100
    g_org=p**(1/7)-1
    def rng(label, base, g, nd):
        v0=value(base,min(0,g)); v1=value(base,max(0,g)); vm=(v0+v1)/2
        gm=solve_g_for_value(base,vm); fair=value(base,gm,FLOOR)
        ps=lambda v:(v-nd)/SH
        lo,hi=sorted((ps(v0),ps(v1)))
        print(f"{label}\n   base {base:,.0f}  g {100*g:.2f}%  net debt {nd:,.0f}\n   range ${lo:,.2f} .. ${hi:,.2f} per share (whole {v0:,.0f}..{v1:,.0f}); width {hi/lo:.2f}x; midpoint ${ps(vm):,.2f}; fair price ${ps(fair):,.2f}; mid-stream g {100*gm:.2f}%")
        return lo,hi,ps(fair)
    print()
    # central, all-equity
    bA=mean([X[y]['u_acq'] for y in cyc])
    rng("A  DEFAULT PAIR, all-equity: cycle base acq deducted, total growth cut back to total sales growth", bA, g_sales, NET_DEBT)
    rng("A' same, growth uncut (before the cut-back, shown only)", bA, cagr(mean([X[y]['u_acq'] for y in prev]),bA,7), NET_DEBT)
    bB=mean([X[y]['u'] for y in cyc])+FBM_AFTER_TAX
    rng("B  ORGANIC PAIR, all-equity: cycle base acq left out + FBM/ADG filed record, comparable-sales growth", bB, g_org, NET_DEBT)
    bL=mean([X[y]['u'] for y in [2021,2022,2023,2024,2025]])
    rng("L  LITERAL WINDOW fiscal 2021-2025, all-equity, acq left out, growth end to end", bL, cagr(X[2021]['u'],X[2025]['u'],4), NET_DEBT)
    bLd=mean([X[y]['u_acq'] for y in [2021,2022,2023,2024,2025]])
    rng("L' LITERAL WINDOW, all-equity, acq deducted, growth end to end", bLd, cagr(X[2021]['u'],X[2025]['u'],4), NET_DEBT)
    # equity-only beside
    bAe=mean([X[y]['oc_acq'] for y in cyc])
    rng("A-eq DEFAULT PAIR, equity-only", bAe, g_sales, 0)
    bBe=mean([X[y]['oc'] for y in cyc])+FBM_AFTER_TAX*0.0+FBM_AFTER_TAX
    rng("B-eq ORGANIC PAIR, equity-only", bBe, g_org, 0)
