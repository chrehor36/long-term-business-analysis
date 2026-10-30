"""Q7 arithmetic for the H run of 2026-10-14. Every input is a filed figure (accessions in the run file).
Arithmetic only; no verdict."""
T = 0.21            # US federal statutory rate (the filer's rate reconciliation starts there); CONVENTION of this run
RATE = 0.0556       # 30-yr Treasury par, 2026-10-13
FLOOR = 0.10
SHARES = 94.236736  # millions, 10-Q cover (A 41,600,929 + B 52,635,807)
PRICE = 162.92
NETDEBT = 605 + 3676 - 537 - 69   # 2026-06-30 balance sheet: debt incl. finance lease, less cash and short-term investments
yrs = [2021, 2022, 2023, 2024, 2025]
ocf   = dict(zip(yrs, [315, 674, 800, 633, 379]))
sbc   = dict(zip(yrs, [59, 61, 75, 64, 74]))
capex = dict(zip(yrs, [111, 201, 198, 170, 220]))
intp  = dict(zip(yrs, [145, 138, 115, 167, 277]))     # cash paid for interest
eqinv = dict(zip(yrs, [29-98, 8-54, 43-7, 88-62, 82-20]))   # contributions less returns, equity method and other investments
finr  = dict(zip(yrs, [21-7, 25-17, 43-1, 136-51, 16-14]))  # financing receivables issued less proceeds
acq   = dict(zip(yrs, [2916, 174, 175, 609, 1274]))
disp  = dict(zip(yrs, [758, 625, -10, 1421, 1666]))   # proceeds from sales of real estate and other, net
taxsale = dict(zip(yrs, [None, None, None, 77, 117]))  # cash taxes on asset sales, filer's figure (8-K 2026-02-12), 2024-25 only
dealcost = dict(zip(yrs, [None, None, 42, 42, 173]))   # transaction and integration costs, income statement

def lev(y):  return ocf[y] - sbc[y] - capex[y] - eqinv[y] - finr[y]
def unlev(y): return lev(y) + intp[y] * (1 - T)
def avg(f, ys=yrs): return sum(f(y) for y in ys) / len(ys)
def cagr(a, b, n): return (b / a) ** (1 / n) - 1 if a > 0 and b > 0 else None

def value(cf0, g, rate, purch=0.0, n=10):
    """CF_t = cf0*(1+g)^t - purch for t=1..n, then no growth on cf0*(1+g)^n (purchases stop) discounted at rate."""
    pv = 0.0
    for t in range(1, n + 1):
        pv += (cf0 * (1 + g) ** t - purch) / (1 + rate) ** t
    term = cf0 * (1 + g) ** n / rate / (1 + rate) ** n
    return pv + term

def ps(ev, debt=NETDEBT): return (ev - debt) / SHARES

print("year  lev  unlev")
for y in yrs: print(y, round(lev(y), 1), round(unlev(y), 1))
U = avg(unlev); L = avg(lev)
NP = (sum(acq.values()) - sum(disp.values())) / 5
print("avg unlev", round(U, 1), "avg lev", round(L, 1), "net purchases/yr", NP, "sum", sum(acq.values()) - sum(disp.values()))
print("serial test: net purchases", sum(acq.values()) - sum(disp.values()), "half of lev OC before purchases", round(sum(lev(y) for y in yrs) / 2, 1))
print("gross acquisitions", sum(acq.values()))
g_end = cagr(unlev(2021), unlev(2025), 4)
g_half = cagr((unlev(2021) + unlev(2022)) / 2, (unlev(2024) + unlev(2025)) / 2, 3)
g_end_l = cagr(lev(2021), lev(2025), 4)
print("growth unlev end-years", g_end, "halves", g_half, "lev end-years", g_end_l)
# variant window 2022-2025 (2021 dropped as the filer's COVID year)
ys2 = [2022, 2023, 2024, 2025]
U2 = avg(unlev, ys2); g2 = cagr(unlev(2022), unlev(2025), 3)
print("window 2022-25 avg unlev", round(U2, 1), "growth", g2)

cases = {}
# DEFAULT PAIR (acquisitions net of disposals deducted, total growth credited; purchases stop after year ten)
g = g_end
cases["default top: no growth, no purchases charged"] = (value(U, 0, RATE), value(U, 0, FLOOR))
cases["default bottom: shown decline, purchases deducted yrs 1-10"] = (value(U, g, RATE, NP), value(U, g, FLOOR, NP))
cases["default bottom alt: halves decline"] = (value(U, g_half, RATE, NP), value(U, g_half, FLOOR, NP))
# ORGANIC PAIR: owner cash before purchases, with the filer's own deal items taken out (cash taxes on asset sales; deal costs)
adj = {y: (taxsale[y] or 0) + (dealcost[y] or 0) for y in yrs}
UO = avg(lambda y: unlev(y) + adj[y])
gorg = 0.067   # net rooms growth excluding acquisitions, 2025 (8-K 2026-02-12)
cases["organic bottom: no growth"] = (value(UO, 0, RATE), value(UO, 0, FLOOR))
cases["organic top: 6.7% organic rooms growth"] = (value(UO, gorg, RATE), value(UO, gorg, FLOOR))
# GENEROUS STRESS (not a case the conventions build): best year unlevered, plus key money added back, 12% (fee CAGR 2019-25 incl. acquisitions)
best = unlev(2023) + 132
cases["stress: 2023 unlev + key money, 12% for ten years"] = (value(best, 0.12, RATE), value(best, 0.12, FLOOR))
print("UO", round(UO, 1))
for k, (v, vf) in cases.items():
    print(f"{k:58s} EV@5.56 {v:8.0f}  ps {ps(v):8.2f} | EV@10 {vf:8.0f} ps {ps(vf):8.2f}")
EV = PRICE * SHARES + NETDEBT
print("market cap", round(PRICE * SHARES, 1), "net debt", NETDEBT, "EV", round(EV, 1))
# equity-only (levered owner cash, after interest), no debt subtracted
LO = avg(lambda y: lev(y) + adj[y])
print("avg lev organic", round(LO, 1))
for name, cf, gg, pur in [("eq default top", L, 0, 0), ("eq default bottom", L, g_end, NP),
                          ("eq organic bottom", LO, 0, 0), ("eq organic top", LO, gorg, 0)]:
    v, vf = value(cf, gg, RATE, pur), value(cf, gg, FLOOR, pur)
    print(f"{name:20s} ps@5.56 {v/SHARES:8.2f}  ps@10 {vf/SHARES:8.2f}")
# cap check (f): organic top year-10 owner cash against the highest share of sales earned
rev_ex = {2021: 3028 - 1583, 2022: 5891 - 2620, 2023: 6667 - 3058, 2024: 6648 - 3352, 2025: 7101 - 3629}
print("unlev OC / revenue ex reimbursed:", {y: round(unlev(y) / rev_ex[y], 3) for y in yrs})
