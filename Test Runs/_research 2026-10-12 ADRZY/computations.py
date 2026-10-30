"""ADRZY (Andritz AG) owner cash and the Q7 range. Every input is a line of the filed consolidated
statements of cash flows (Andritz Financial Reports 2016-2025, the year's own report; 2019 lease principal
from the lease note's total cash outflow less lease interest). MEUR. Run: python -I computations.py"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

# year: CFO, capex paid (PP&E + intangibles), PP&E disposal proceeds, lease principal (IFRS 16, from 2019),
#       acquisitions (net cash for company acquisitions + NCI purchases/payments to former shareholders
#       + payments for equity-method investments - sale of subsidiaries), interest received, interest paid,
#       lease interest (inside interest paid)
D = {
 2016: (366.6, 122.1, 19.4, 0.0, 104.1+2.4,            41.9, 24.7, 0.0),
 2017: (246.5, 115.5, 62.3, 0.0, 13.4+0.8-24.0,        33.8, 28.2, 0.0),
 2018: (7.8,   127.1, 7.8,  0.0, 270.0+0.4+6.3-25.3,   21.0, 36.5, 0.0),
 2019: (821.6, 122.0, 8.7, 46.5, 7.1+79.8+4.9,         20.6, 41.6, 5.0),
 2020: (461.5, 87.9, 21.4, 48.9, 0.0+20.5+5.0,         15.2, 40.3, 5.1),
 2021: (529.6, 110.3, 32.2, 48.5, 30.5+34.5+11.2,      17.9, 36.3, 4.5),
 2022: (710.8, 155.0, 46.2, 59.3, 62.0+0.1,            32.6, 19.1, 4.3),
 2023: (375.0, 170.8, 15.6, 50.6, 36.4+0.0,            62.3, 34.4, 6.8),
 2024: (636.5, 179.5, 16.5, 53.3, 36.9+14.9,           61.0, 38.9, 8.9),
 2025: (652.7, 198.1, 27.4, 52.0, 328.6+4.6,           32.9, 36.3, 9.3),
}
SALES = {2016:6039.0,2017:5889.1,2018:6031.5,2019:6673.9,2020:6699.6,2021:6463.0,2022:7542.9,2023:8660.0,2024:8313.7,2025:7883.1}
TAX = 0.237   # the filer's stated 2025 group tax rate (FR2025, management report 4c)
R_GOV = 0.0378  # ECB AAA euro area 30Y spot, 2026-10-08 (tools/sources.py)
FLOOR = 0.10
SHARES = 97_998_794 + 61_495 + 208_495 + 42_062   # FR2025 note 34c outstanding at 2025-12-31 + H1 2026 note 12b re-issues
PRICE = 81.40   # ANDR.VI close 2026-10-09, Yahoo (aggregator, live quote only)
NET_CASH = 593.3  # H1 2026 key figures: net liquidity 2026-06-30 (liquid funds less bank loans and Schuldscheindarlehen; leases excluded)

def oc(y, acq=True, disposals=False, all_equity=False):
    cfo, capex, disp, lease, acqs, ir, ip, li = D[y]
    v = cfo - capex - lease - (acqs if acq else 0.0) + (disp if disposals else 0.0)
    if all_equity:  # remove net non-lease interest after the company's tax (leases treated as an operating cost)
        v -= (ir - (ip - li)) * (1 - TAX)
    return v

def value(base, g, r, years=10):
    """PV at r of base*(1+g)^t for t=1..10, then flat (zero nominal growth) forever."""
    pv, c = 0.0, base
    for t in range(1, years + 1):
        c = base * (1 + g) ** t
        pv += c / (1 + r) ** t
    return pv + (c / r) / (1 + r) ** years

def irr(price_ev, base, g):
    lo, hi = 0.0005, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(base, g, mid) > price_ev: lo = mid
        else: hi = mid
    return mid

mc = SHARES * PRICE / 1e6
ev = mc - NET_CASH
print(f"shares {SHARES:,}  price {PRICE}  market value {mc:,.1f}  net cash {NET_CASH}  EV {ev:,.1f}")
print("\nyear  OC_eq(acq ded.)  OC_eq(before acq)  OC_ae(acq ded.)  OC_ae(before acq)  OC/sales")
for y in D:
    print(f"{y}  {oc(y):9.1f}  {oc(y,acq=False):9.1f}  {oc(y,all_equity=True):9.1f}  {oc(y,acq=False,all_equity=True):9.1f}  {oc(y,acq=False)/SALES[y]:.3f}")

def avg(ys, **k): return sum(oc(y, **k) for y in ys) / len(ys)
W = [2021, 2022, 2023, 2024, 2025]; P = [2016, 2017, 2018, 2019, 2020]
for label, k in (("all-equity", dict(all_equity=True)), ("equity-only", {})):
    print(f"\n==== {label} basis")
    a5 = avg(W, **k); a5o = avg(W, acq=False, **k); a5d = avg(W, disposals=True, **k)
    h1 = avg([2021, 2022], **k); h2 = avg([2024, 2025], **k)
    g_half = (h2 / h1) ** (1 / 3) - 1
    g_end = (oc(2025, **k) / oc(2021, **k)) ** (1 / 4) - 1
    a10 = avg(P + W, **k); gp = (avg(W, **k) / avg(P, **k)) ** (1 / 5) - 1
    print(f"five-year avg (acq deducted) {a5:.1f}; before acq {a5o:.1f}; with disposals credited {a5d:.1f}")
    print(f"literal end-year rate 2021->2025 {g_end:+.1%} (meaningless: 2025 acquisition year); halves 2021-22 avg {h1:.1f} -> 2024-25 avg {h2:.1f}: {g_half:+.1%}/yr")
    print(f"ten-year avg 2016-2025 {a10:.1f}; first half avg {avg(P,**k):.1f} -> second half {avg(W,**k):.1f}: {gp:+.1%}/yr")
    basis_debt = (-NET_CASH) if label == "all-equity" else 0.0
    denom = ev if label == "all-equity" else mc
    cases = {
      "A literal no-growth (top, sec. b)": (a5, 0.0),
      "B literal decline by halves (bottom, sec. b)": (a5, g_half),
      "C cycle base, growth between five-year halves (CENTRAL top)": (a10, gp),
      "E cycle base, no growth (CENTRAL bottom)": (a10, 0.0),
      "D organic pair, before acquisitions, no growth (beside)": (a5o, 0.0),
    }
    for n, (b, g) in cases.items():
        v_gov = value(b, g, R_GOV); v_fl = value(b, g, FLOOR)
        ps_gov = (v_gov - basis_debt) / SHARES * 1e6 if label == "all-equity" else v_gov / SHARES * 1e6
        ps_fl = (v_fl - basis_debt) / SHARES * 1e6 if label == "all-equity" else v_fl / SHARES * 1e6
        print(f"{n}: base {b:.1f} g {g:+.1%} | value @3.78% {v_gov:,.0f} -> {ps_gov:.2f}/sh | @10% {v_fl:,.0f} -> {ps_fl:.2f}/sh | expected return at price {irr(denom, b, g):.1%}")
    top = value(a5, 0.0, R_GOV); bot = value(a5, g_half, R_GOV)
    ctop = value(a10, gp, R_GOV); cbot = value(a10, 0.0, R_GOV)
    adj = (lambda v: (v + NET_CASH) / SHARES * 1e6) if label == "all-equity" else (lambda v: v / SHARES * 1e6)
    print(f"CENTRAL RANGE (cycle base, sec. a): {adj(cbot):.2f} to {adj(ctop):.2f} per share; width {adj(ctop)/adj(cbot):.2f}")
    cfair = (adj(value(a10, 0.0, FLOOR)) + adj(value(a10, gp, FLOOR))) / 2
    print(f"CENTRAL FAIR PRICE (each end at 10%, averaged): {cfair:.2f} per share")
    print(f"literal range beside: {adj(bot):.2f} to {adj(top):.2f} per share; width {adj(top)/adj(bot):.2f}")
    fair = (adj(value(a5, 0.0, FLOOR)) + adj(value(a5, g_half, FLOOR))) / 2
    print(f"literal fair price beside: {fair:.2f} per share")
