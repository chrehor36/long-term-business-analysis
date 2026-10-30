"""BOUYF run 2026-10-12: COMPUTATION, NOT A CLEARANCE (the file closed at Q2).
Every input is a filed figure (EUR m) from the consolidated cash-flow statements of the URDs
FY2021 (D.22-0139), FY2023 (D.24-0153) and FY2025 (D.26-0111), or the H1 2026 release of 2026-07-30.
Run: python -I q7_computation.py
"""
TAX = 0.2583          # French statutory rate stated in the FY2025 URD tax note (15.2)
R_SOV = 0.03778       # ECB euro-area AAA 30y spot, 2026-10-08 (tools/sources.py)
R_FLOOR = 0.10        # Q7 floor CONVENTION, Part VII fair-price definition
SHARES = 388_438_129 - 1_035_555   # issued 30 Sep 2026 less treasury 31 Dec 2025 (latest count filed)
PRICE = 40.30
NET_DEBT = {"2026-06-30": 6515, "2025-12-31": 4204}

Y = [2021, 2022, 2023, 2024, 2025]
CAF   = dict(zip(Y, [3165, 3324, 3855, 4307, 4180]))   # after net interest, lease interest, tax paid
CAPEX = dict(zip(Y, [-2446, -2625, -2572, -2714, -2488]))
DISP  = dict(zip(Y, [472, 404, 455, 230, 571]))
DEBTFA= dict(zip(Y, [-90, -105, -92, 216, -13]))       # net payables on fixed assets
LEASE = dict(zip(Y, [-361, -441, -559, -555, -455]))   # lease principal repaid
SBC   = dict(zip(Y, [-10, -15, -22, -9, -19]))         # IFRS 2 charge incl. NCI, consolidated equity statements
WC    = dict(zip(Y, [204, -606, 1148, 776, 954]))
NETDEBTCOST = dict(zip(Y, [155, 198, 286, 187, 212]))
# acquisitions net: consolidated activities, non-consolidated securities, perimeter cash, other investing flows
ACQ   = dict(zip(Y, [823, -6227, -196, -1215, -54]))
NI    = dict(zip(Y, [1305, 1131, 1201, 1222, 1272]))
NCI   = dict(zip(Y, [180, 158, 161, 164, 134]))
SALES = dict(zip(Y, [37589, 44322, 56017, 56752, 56877]))

def oc_eq(y):      # equity-only owner cash before acquisitions and WC, group share
    v = CAF[y] + CAPEX[y] + DISP[y] + DEBTFA[y] + LEASE[y] + SBC[y]
    return v * (1 - NCI[y] / NI[y])

def oc_ae(y):      # all-equity: add back cost of net debt after tax
    v = CAF[y] + CAPEX[y] + DISP[y] + DEBTFA[y] + LEASE[y] + SBC[y] + NETDEBTCOST[y] * (1 - TAX)
    return v * (1 - NCI[y] / NI[y])

def acq_gs(y):     # acquisitions, group share
    return ACQ[y] * (1 - NCI[y] / NI[y])

def value(c_before, c_after, g, r):
    """years 1-10: cash after purchases growing at g; from year 11: cash before purchases (grown) at zero growth."""
    v = 0.0
    for t in range(1, 11):
        v += c_after * (1 + g) ** t / (1 + r) ** t
    term = c_before * (1 + g) ** 10 / r
    return v + term / (1 + r) ** 10

def per_share(v, nd):
    return (v - nd) * 1e6 / SHARES

def avg(f, ys):
    return sum(f(y) for y in ys) / len(ys)

if __name__ == "__main__":
    print("year  OCeq  OCae  ACQgs  WC   sales  OCae/sales")
    for y in Y:
        print(y, round(oc_eq(y)), round(oc_ae(y)), round(acq_gs(y)), WC[y], SALES[y], f"{oc_ae(y)/SALES[y]:.2%}")
    maxshare = max(oc_ae(y) / SALES[y] for y in Y)
    # ---- literal window 2021-2025, acquisitions deducted (Equans purchase inside)
    lit = avg(lambda y: oc_ae(y) + acq_gs(y), Y)
    print(f"\nLITERAL WINDOW 2021-25 all-equity, acquisitions deducted: avg {lit:.0f} (sign changes across the window)")
    print(f"  no-growth value at sovereign: {lit / R_SOV:.0f} -> per share {per_share(lit / R_SOV, NET_DEBT['2026-06-30']):.2f}")
    # ---- merger base: 2023-2025, the three full years with Equans
    B = [2023, 2024, 2025]
    base_ae = avg(oc_ae, B); base_eq = avg(oc_eq, B); base_acq = avg(acq_gs, B)
    print(f"\nMERGER BASE 2023-25: OCae {base_ae:.0f}, OCeq {base_eq:.0f}, acquisitions {base_acq:.0f}")
    g_shown = (oc_ae(2025) / oc_ae(2023)) ** 0.5 - 1
    g_sales = (SALES[2025] / SALES[2023]) ** 0.5 - 1
    share10 = base_ae * (1 + g_shown) ** 10 / (SALES[2025] * (1 + g_sales) ** 10)
    print(f"  shown growth of owner cash 2023->25: {g_shown:.2%}/yr; carried 10y -> {share10:.1%} of sales vs highest filed {maxshare:.2%}")
    g = g_sales if share10 > maxshare else g_shown
    print(f"  growth carried (cap (f)): {g:.2%}/yr (sales growth 2023->25)")
    for label, nd in NET_DEBT.items():
        lo_s = value(base_ae, base_ae, 0.0, R_SOV)                    # no growth, no purchases
        hi_s = value(base_ae, base_ae + base_acq, g, R_SOV)           # growth bought for ten years
        lo_f = value(base_ae, base_ae, 0.0, R_FLOOR)
        hi_f = value(base_ae, base_ae + base_acq, g, R_FLOOR)
        ends = sorted([per_share(lo_s, nd), per_share(hi_s, nd)])
        fair = (per_share(lo_f, nd) + per_share(hi_f, nd)) / 2
        print(f"\n  net debt {label} ({nd}): RANGE all-equity EUR {ends[0]:.2f} - {ends[1]:.2f} per share; "
              f"no-growth case {per_share(lo_s, nd):.2f}, growth case {per_share(hi_s, nd):.2f}")
        print(f"     FAIR (each end at 10%, averaged) all-equity: EUR {fair:.2f}  [ends {per_share(lo_f, nd):.2f} / {per_share(hi_f, nd):.2f}]")
    # equity-only
    lo_s = value(base_eq, base_eq, 0.0, R_SOV); hi_s = value(base_eq, base_eq + base_acq, g, R_SOV)
    lo_f = value(base_eq, base_eq, 0.0, R_FLOOR); hi_f = value(base_eq, base_eq + base_acq, g, R_FLOOR)
    print(f"\n  EQUITY-ONLY range EUR {min(lo_s, hi_s)*1e6/SHARES:.2f} - {max(lo_s, hi_s)*1e6/SHARES:.2f}; fair {((lo_f + hi_f)/2)*1e6/SHARES:.2f}")
    # with working capital (variant)
    base_wc = avg(lambda y: oc_ae(y) + WC[y] * (1 - NCI[y] / NI[y]), B)
    lo_f = value(base_wc, base_wc, 0.0, R_FLOOR); hi_f = value(base_wc, base_wc + base_acq, g, R_FLOOR)
    print(f"  variant WITH working-capital releases 2023-25: base {base_wc:.0f}; fair all-equity "
          f"{(per_share(lo_f, NET_DEBT['2026-06-30']) + per_share(hi_f, NET_DEBT['2026-06-30']))/2:.2f}")
    # floor test at the price
    ev = PRICE * SHARES / 1e6 + NET_DEBT["2026-06-30"]
    print(f"\n  price {PRICE}: market cap {PRICE*SHARES/1e6:.0f}m, EV {ev:.0f}m; no-growth yield on EV {base_ae/ev:.2%}; "
          f"growth case yield {(base_ae+base_acq)/ev:.2%} (+{g:.2%} growth)")
