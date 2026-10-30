# COMPUTATION, NOT A CLEARANCE. Computed during the Step 0 reading, before Q1 to Q4 closed (operator rule 3); it carries no entry language and decides nothing until Q7.
# DTE run 2026-10-18: Q7 arithmetic. Every input is a filed figure (10-K FY2025 0000936340-26-000054,
# FY2023 0000936340-24-000076, FY2021 0000936340-22-000077; 10-Q Q2 2026 0000936340-26-000146).
import sys
sys.stdout.reconfigure(encoding="utf-8")
Y = [2021, 2022, 2023, 2024, 2025]
OCF   = dict(zip(Y, [3067, 1977, 3220, 3643, 3409]))
DA    = dict(zip(Y, [1459, 1468, 1606, 1732, 1841]))
NF    = dict(zip(Y, [58, 42, 59, 55, 67]))          # nuclear fuel amortization
SC    = dict(zip(Y, [71, 62, 48, 54, 60]))          # stock-based compensation expense, Note 21
CAPU  = dict(zip(Y, [3633, 3311, 3872, 4399, 4343]))
CAPN  = dict(zip(Y, [139, 67, 62, 68, 86]))
ACQ   = dict(zip(Y, [0, 0, 0, 0, 210]))
NOTES = dict(zip(Y, [74, 30, 86, 449, 578]))        # investment in notes receivable net of collections
ISS   = dict(zip(Y, [4457, 2171, 3167, 4533, 4429]))
RED   = dict(zip(Y, [3522, 1587, 1616, 2139, 1291]))
INTP  = dict(zip(Y, [671, 638, 751, 869, 978]))     # cash interest paid, net of capitalized
UREV  = dict(zip(Y, [7288, 8243, 7466, 7990, 8849]))
BASE_INFRA = (4000 + 2700) / 5                      # 10-K Item 7: 2026-2030 base infrastructure, electric + gas
PRICE, SH = 129.73, 208.088069
DEBT = 1689 + 25895 + 0; CASH = 42                   # 10-Q 2026-06-30
NETDEBT = DEBT - CASH
EQ = 12154
RF = 0.0543; FLOOR = 0.10; TSTAT = 0.21 + 0.06 * (1 - 0.21)
mcap = PRICE * SH

def maint(y, base=False): return (BASE_INFRA if base else DA[y] + NF[y])
def M(y, base=False): return OCF[y] - maint(y, base) - SC[y]
def fixcap(y): return CAPU[y] + CAPN[y]
def growthsp(y, base=False): return fixcap(y) + ACQ[y] + NOTES[y] - maint(y, base)
def netdebt_raised(y): return ISS[y] - RED[y]

def value(m, g, G, r, n=10):
    """m: base owner cash; g growth for n years; G growth spending charged yearly for n years; then flat."""
    pv = 0.0
    for t in range(1, n + 1):
        pv += (m * (1 + g) ** t - G) / (1 + r) ** t
    term = m * (1 + g) ** n / r / (1 + r) ** n
    return pv + term

def irr(m, g, G, price_total):
    lo, hi = 0.001, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(m, g, G, mid) > price_total: lo = mid
        else: hi = mid
    return mid

def cagr(a, b, n): return (b / a) ** (1 / n) - 1

def run(win, label, base=False, share=None):
    n = len(win)
    m = sum(M(y, base) for y in win) / n
    fc = sum(fixcap(y) for y in win)
    nd = sum(netdebt_raised(y) for y in win)
    cap = share * fc
    credit = min(nd, cap)
    G = (sum(growthsp(y, base) for y in win) - credit) / n
    allsp = (sum(OCF[y] - fixcap(y) - ACQ[y] - NOTES[y] - SC[y] for y in win) + credit) / n
    ser = [M(y, base) for y in win]
    end_rate = cagr(ser[0], ser[-1], n - 1)
    h = n // 2
    first, second = sum(ser[:h]) / h, sum(ser[-h:]) / h
    span = (n - 1) - (h - 1)          # distance between half midpoints in years
    halves = cagr(first, second, span)
    srev_end = cagr(UREV[win[0]], UREV[win[-1]], n - 1)
    srev_h = cagr(sum(UREV[y] for y in win[:h]) / h, sum(UREV[y] for y in win[-h:]) / h, span)
    hi_share = max(M(y, base) / UREV[y] for y in win)
    print(f"\n=== {label}: window {win[0]}-{win[-1]}, maintenance={'base infrastructure' if base else 'D&A + nuclear fuel'}")
    print("owner cash maintenance-only, equity-only, by year:", {y: round(M(y, base)) for y in win})
    print(f"average M = {m:,.0f}; fixed-asset capex {fc:,.0f}; net LTD raised {nd:,.0f}; cap {share:.3f} x capex = {cap:,.0f}; debt credited {credit:,.0f}")
    print(f"equity growth spending charged per year G = {G:,.0f}; all-spending owner cash (debt credited) = {allsp:,.0f}")
    print(f"shown growth of M: end-years {end_rate*100:.1f}%/yr; halves {halves*100:.1f}%/yr; utility revenue end-years {srev_end*100:.2f}%, halves {srev_h*100:.2f}%; highest M/utility revenue {hi_share*100:.1f}%")
    for gname, g in [('halves rate (shown)', halves)]:
        m10 = m * (1 + g) ** 10; r10 = UREV[win[-1]] * (1 + srev_h) ** 10
        print(f"  (f) test: M at {g*100:.1f}% for 10 yrs = {m10:,.0f} = {m10/r10*100:.0f}% of utility revenue grown at its own rate (highest earned {hi_share*100:.1f}%)")
    g = srev_h
    res = {}
    for nm, (mm, gg, GG) in {'no-growth': (m, 0.0, 0.0), 'growth': (m, g, G)}.items():
        v_rf = value(mm, gg, GG, RF); v_fl = value(mm, gg, GG, FLOOR)
        res[nm] = (v_rf / SH, v_fl / SH, irr(mm, gg, GG, mcap))
        print(f"  {nm:9s} g={gg*100:.2f}%: value at {RF*100:.2f}% = ${v_rf/SH:,.2f}/sh; at 10% = ${v_fl/SH:,.2f}/sh; expected return at price = {res[nm][2]*100:.1f}%")
    lo, hi = sorted([res['no-growth'][0], res['growth'][0]])
    fair = (res['no-growth'][1] + res['growth'][1]) / 2
    print(f"  RANGE (sovereign) ${lo:,.2f} to ${hi:,.2f} vs price ${PRICE}; width {hi/lo:.2f}:1; FAIR (avg of ends at 10%) ${fair:,.2f}")
    # breakeven growth for the growth case to earn 10% at the price
    lo_g, hi_g = 0.0, 0.5
    for _ in range(100):
        mid = (lo_g + hi_g) / 2
        if value(m, mid, G, FLOOR) < mcap: lo_g = mid
        else: hi_g = mid
    print(f"  growth needed for 10% at the price (growth spending as charged): {mid*100:.1f}%/yr for ten years")
    # all-spending beside, no growth (series changes sign)
    print(f"  all-spending beside (no growth): at {RF*100:.2f}% ${allsp/RF/SH:,.2f}/sh; at 10% ${allsp/FLOOR/SH:,.2f}/sh")
    # all-equity beside
    mae = sum(OCF[y] + INTP[y] * (1 - TSTAT) - maint(y, base) - SC[y] for y in win) / n
    v_ae_rf = (mae / RF - NETDEBT) / SH; v_ae_fl = (mae / FLOOR - NETDEBT) / SH
    print(f"  all-equity beside: owner cash before interest {mae:,.0f}; no-growth at {RF*100:.2f}% ${v_ae_rf:,.2f}/sh; at 10% ${v_ae_fl:,.2f}/sh (net debt {NETDEBT:,})")
    return fair

print("COMPUTATION, NOT A CLEARANCE (operator rule 3): computed before Q1-Q4 closed.")
print(f"price {PRICE}, shares {SH}M, market cap {mcap:,.0f}M; debt {DEBT:,}; net debt {NETDEBT:,}; debt share consolidated {DEBT/(DEBT+EQ):.3f}; DTE Electric {15403/(15403+12426):.3f}")
s_cons = DEBT / (DEBT + EQ)
run([2022, 2023, 2024, 2025], 'CENTRAL (post-separation window)', share=s_cons)
run(Y, 'LITERAL five-year window (includes DT Midstream to 2021-06-30)', share=s_cons)
run([2022, 2023, 2024, 2025], 'GENEROUS variant: maintenance = filed base-infrastructure plan', base=True, share=s_cons)
run([2022, 2023, 2024, 2025], 'CENTRAL with DTE Electric debt share', share=15403/(15403+12426))
