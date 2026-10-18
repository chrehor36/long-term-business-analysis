"""COMPUTATION, NOT A CLEARANCE. Owner cash for FLR, USD millions, from the filed cash-flow statements
(company facts, latest 10-K vintage, accessions in facts output) plus NuScale's own filed OCF.
Run: python -I owner_cash.py"""
import sys; sys.stdout.reconfigure(encoding="utf-8")
Y = list(range(2016, 2026))
OCF  = dict(zip(Y, [705.9, 602.0, 162.2, 219.0, 186.0, 25.0, 31.0, 212.0, 828.0, -387.0]))
CAPX = dict(zip(Y, [235.9, 283.1, 211.0, 180.8, 113.0, 75.0, 75.0, 106.0, 164.0, 50.0]))
SBC  = dict(zip(Y, [40.1, 40.7, 43.0, 36.1, 22.0, 32.0, 19.0, 48.0, 31.0, 30.0]))
NCI  = dict(zip(Y, [57.9, 47.2, 63.5, 33.7, 23.0, 109.0, 60.0, 53.0, 14.0, 64.0]))
NINT = dict(zip(Y, [-52.6, -40.0, -40.6, -11.0, -46.0, -73.0, 35.0, 168.0, 150.0, 67.0]))  # net interest income (expense)
NUS  = {2021: -99.162, 2022: -148.609, 2023: -183.254, 2024: -82.249}  # NuScale OCF while consolidated (2024: nine months)
JVN  = {2021: 80.0, 2022: 53.0 - 19.0, 2023: 33.0 - 8.0, 2024: 93.0 - 34.0, 2025: 278.0 - 22.0}  # JV investments less returns of capital
SANTOS = 642.0  # 2025 net payment to Santos (10-K FY2025 MD&A note (1))
REV  = dict(zip(Y, [19036.5, 14806.5, 18851.0, 15454.5, 15788.0, 14156.0, 13744.0, 15474.0, 16315.0, 15503.0]))
T = 0.21  # CONVENTION of the run: US statutory rate applied to net interest when moving to the all-equity basis
def oc(y, core=True, alleq=False, santos=False, jv=False):
    v = OCF[y] - CAPX[y] - SBC[y] - NCI[y]
    if core: v -= NUS.get(y, 0.0)
    if santos and y == 2025: v += SANTOS
    if jv: v -= JVN.get(y, 0.0)
    if alleq: v -= NINT[y] * (1 - T)
    return v
def mean(ys, **k): return sum(oc(y, **k) for y in ys) / len(ys)
print("year   OCF  owner-cash(eq-only,literal)  core  core,all-equity  core,all-eq,+Santos  core,all-eq,JV-net  OC/revenue(core,all-eq)")
for y in Y:
    print(y, f"{OCF[y]:7.0f} {oc(y,core=False):9.0f} {oc(y):9.0f} {oc(y,alleq=True):9.0f} {oc(y,alleq=True,santos=True):9.0f} {oc(y,alleq=True,jv=True) if y>=2021 else float('nan'):9.0f} {100*oc(y,alleq=True)/REV[y]:6.2f}%")
W = list(range(2021, 2026)); C = list(range(2017, 2025))
for name, ys in [("window 2021-2025", W), ("ten years 2016-2025", Y), ("cycle 2017-2024", C)]:
    print(f"{name:22s} eq-only literal {mean(ys,core=False):7.1f} | core eq-only {mean(ys):7.1f} | core all-equity {mean(ys,alleq=True):7.1f} | +Santos {mean(ys,alleq=True,santos=True):7.1f}")
print("window, core all-equity, JV net deducted:", round(mean(W, alleq=True, jv=True), 1))
print("highest OC/revenue in years read (core, all-equity):", round(max(100*oc(y,alleq=True)/REV[y] for y in Y), 2), "%")
