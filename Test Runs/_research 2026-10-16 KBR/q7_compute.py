"""COMPUTATION, NOT A CLEARANCE. Q7 range and the fair price for KBR, from the filed figures in the run file.
Ten years at growth g, then zero nominal growth, discounted at r; ends = no-growth and shown-growth cases."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
def pv(c, g, r, n=10):
    v, cf = 0.0, c
    for t in range(1, n + 1):
        cf = c * (1 + g) ** t
        v += cf / (1 + r) ** t
    return v + cf / r / (1 + r) ** n
def irr(price, c, g):
    lo, hi = 0.0001, 1.0
    for _ in range(200):
        m = (lo + hi) / 2
        if pv(c, g, m) > price: lo = m
        else: hi = m
    return m
R, FLOOR, SH = 0.0543, 0.10, 126.068
PRICE = 36.38; CAP = PRICE * SH
ND = 2552 + 10 - 312 - 50          # borrowings + finance leases - cash - AFS securities, 10-Q 2026-07-03
oc   = [236, 304, 231, 363, 449]    # owner cash before purchases, after interest (equity-only basis)
intr = [63, 66, 102, 124, 141]      # cash interest paid
tax = 0.25                          # company's effective rate FY2024 and FY2025 (10-K Item 7)
oc_ae = [o + i * (1 - tax) for o, i in zip(oc, intr)]
acq = [355, 26, 0, 731, 11]
rev = [7339, 6564, 6956, 7710, 7786]
avg = lambda x: sum(x) / len(x)
C_eq, C_ae = avg(oc), avg(oc_ae)
print("owner cash before purchases, equity-only avg %.1f; all-equity avg %.1f" % (C_eq, C_ae))
print("all-equity series", [round(x, 1) for x in oc_ae])
print("net purchases %d vs owner cash before purchases %d -> %.0f%%" % (sum(acq), sum(oc), sum(acq) / sum(oc) * 100))
g_oc = (oc[-1] / oc[0]) ** 0.25 - 1
g_rev = (rev[-1] / rev[0]) ** 0.25 - 1
print("shown growth owner cash %.1f%%/yr; revenue %.2f%%/yr" % (g_oc * 100, g_rev * 100))
maxshare = max(o / s for o, s in zip(oc_ae, rev))
need = C_ae * (1 + g_oc) ** 10 / (rev[-1] * (1 + g_rev) ** 10)
print("highest owner-cash share of sales %.1f%%; shown growth carried ten years would need %.1f%% -> cap to sales growth" % (maxshare * 100, need * 100))
g = g_rev
print("NET DEBT %d; market cap %.0f; EV %.0f" % (ND, CAP, CAP + ND))
for label, C, basis in (("ALL-EQUITY (central)", C_ae, "ae"), ("EQUITY-ONLY (beside)", C_eq, "eq")):
    ends = []
    for gg in (0.0, g):
        v = pv(C, gg, R)
        ps = (v - ND) / SH if basis == "ae" else v / SH
        f = pv(C, gg, FLOOR)
        fps = (f - ND) / SH if basis == "ae" else f / SH
        price_basis = CAP + ND if basis == "ae" else CAP
        ends.append((gg, v, ps, fps, irr(price_basis, C, gg)))
    print(label)
    for gg, v, ps, fps, ir in ends:
        print("  g=%.2f%%  value %.0f  per share $%.2f  at-10%% per share $%.2f  expected return at the price %.2f%%" % (gg * 100, v, ps, fps, ir * 100))
    print("  range $%.2f to $%.2f; width %.2f to one; FAIR PRICE (avg of ends at 10%%) $%.2f" % (ends[0][2], ends[1][2], ends[1][2] / ends[0][2], (ends[0][3] + ends[1][3]) / 2))
# literal-year and variant checks
for lbl, C in (("latest year FY2025 all-equity", oc_ae[-1]), ("book-tax variant all-equity", C_ae - avg([62, 45, 43, 47, 73]))):
    print(lbl, "C=%.1f expected return at zero growth %.2f%%; at %.2f%% growth %.2f%%" % (C, irr(CAP + ND, C, 0) * 100, g * 100, irr(CAP + ND, C, g) * 100))
# default pair beside: acquisitions deducted, all-equity
C_def = avg([a - b for a, b in zip(oc_ae, acq)])
print("default pair (purchases deducted) all-equity avg %.1f; no-growth value per share $%.2f; expected return at the price %.2f%%" % (C_def, (pv(C_def, 0, R) - ND) / SH, irr(CAP + ND, C_def, 0) * 100))
# what growth would earn the floor at the price
for C, lbl, P in ((C_ae, "all-equity", CAP + ND), (C_eq, "equity-only", CAP)):
    lo, hi = 0.0, 0.5
    for _ in range(200):
        m = (lo + hi) / 2
        if pv(C, m, FLOOR) < P: lo = m
        else: hi = m
    print("growth for ten years needed to earn 10%% at the price (%s): %.1f%%/yr" % (lbl, m * 100))
