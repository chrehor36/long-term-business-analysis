"""Q7 arithmetic for the BIPC run of 2026-10-17. Inputs are BIP's own filed figures (BIP share, US$ millions),
listed with their sources in the run file's Step 0 table. Arithmetic only; no judgment is made here."""

years = [2021, 2022, 2023, 2024, 2025]
FFO = [1733, 2087, 2288, 2468, 2627]
MAINT = [321, 386, 450, 606, 663]
GROWTH_CAPEX = [1153, 1613, 1746, 2166, 3308]
INTEREST = [755, 991, 1340, 1650, 1709]
IDR = [206, 240, 266, 295, 320]
PREF = [67, 66, 63, 68, 62]          # preferred units and perpetual subordinated notes
DA = [1144, 1282, 1429, 1681, 1736]  # D&A attributable to the partnership
REV = [5281, 6571, 7124, 7742, 8009] # revenues attributable to the partnership

NET_DEBT = 33969       # debt attributable to the partnership net of its share of cash, 2026-06-30 (BIP Q2 2026)
PREF_CAP = 729 + 293   # preferred units (2026-06-30) + perpetual subordinated notes
UNITS = 791.7          # millions, time-weighted average, Q2 2026 (all unit-equivalents)
PRICE = 37.74
SOV = 0.0543
FLOOR = 0.10
ORGANIC = (0.10 + 0.08 + 0.07 + 0.08) / 4   # filer-reported organic growth 2022-2025

def avg(x):
    return sum(x) / len(x)

AFFO = [f - m for f, m in zip(FFO, MAINT)]
OC_UNLEV_M = [a + i - d for a, i, d in zip(AFFO, INTEREST, IDR)]           # before interest, maintenance only
OC_EQ_M = [a - d - p for a, d, p in zip(AFFO, IDR, PREF)]                    # after interest, maintenance only
OC_UNLEV_DA = [f + i - da - d for f, i, da, d in zip(FFO, INTEREST, DA, IDR)]  # depreciation variant

def pv_nogrowth(base, r):
    return base / r

def pv_growth(base, g, spend, r, n=10):
    """Years 1..n: base*(1+g)^t - spend; after year n growth and growth spending stop: base*(1+g)^n forever."""
    pv = 0.0
    for t in range(1, n + 1):
        pv += (base * (1 + g) ** t - spend) / (1 + r) ** t
    pv += (base * (1 + g) ** n) / r / (1 + r) ** n
    return pv

def per_unit_allequity(ev):
    return (ev - NET_DEBT - PREF_CAP) / UNITS

def per_unit_equity(eq):
    return eq / UNITS

def cagr(a, b, n):
    return (b / a) ** (1 / n) - 1

if __name__ == "__main__":
    print("years", years)
    print("AFFO", AFFO)
    print("owner cash before interest, maintenance only", OC_UNLEV_M, "avg", round(avg(OC_UNLEV_M)))
    print("owner cash equity basis, maintenance only", OC_EQ_M, "avg", round(avg(OC_EQ_M)))
    print("owner cash before interest, depreciation variant", OC_UNLEV_DA, "avg", round(avg(OC_UNLEV_DA)))
    print("growth capex avg", round(avg(GROWTH_CAPEX)))
    print("organic growth used", ORGANIC)
    print("shown aggregate growth 2021-25: unlevered maint %.4f, equity %.4f" % (
        cagr(OC_UNLEV_M[0], OC_UNLEV_M[-1], 4), cagr(OC_EQ_M[0], OC_EQ_M[-1], 4)))
    print("revenue growth 2021-25 %.4f" % cagr(REV[0], REV[-1], 4))
    print("owner cash / revenue", [round(o / r, 3) for o, r in zip(OC_UNLEV_M, REV)])
    M0, E0, G, D0 = avg(OC_UNLEV_M), avg(OC_EQ_M), avg(GROWTH_CAPEX), avg(OC_UNLEV_DA)
    y10 = M0 * (1 + ORGANIC) ** 10
    rev10 = avg(REV) * (1 + cagr(REV[0], REV[-1], 4)) ** 10
    print("cap check: year-10 owner cash %.0f vs revenue %.0f -> share %.3f" % (y10, rev10, y10 / rev10))
    print()
    for label, r in (("sovereign 5.43%", SOV), ("floor 10%", FLOOR)):
        ev_n = pv_nogrowth(M0, r)
        ev_g = pv_growth(M0, ORGANIC, G, r)
        ev_g_noorg = pv_growth(M0, ORGANIC, 0.0, r)
        eq_n = pv_nogrowth(E0, r)
        eq_g = pv_growth(E0, ORGANIC, G, r)
        ev_da = pv_nogrowth(D0, r)
        print("==", label)
        print(" ALL-EQUITY  no-growth (maint): EV %.0f -> per unit %.2f" % (ev_n, per_unit_allequity(ev_n)))
        print(" ALL-EQUITY  growth 8.25%% less growth capex: EV %.0f -> per unit %.2f" % (ev_g, per_unit_allequity(ev_g)))
        print(" ALL-EQUITY  growth 8.25%% with NO growth capex charged (generous test): EV %.0f -> per unit %.2f" % (
            ev_g_noorg, per_unit_allequity(ev_g_noorg)))
        print(" ALL-EQUITY  depreciation variant, no growth: EV %.0f -> per unit %.2f" % (ev_da, per_unit_allequity(ev_da)))
        print(" EQUITY-ONLY no-growth: %.0f -> per unit %.2f" % (eq_n, per_unit_equity(eq_n)))
        print(" EQUITY-ONLY growth less growth capex: %.0f -> per unit %.2f" % (eq_g, per_unit_equity(eq_g)))
        print(" EQUITY-ONLY growth, no growth capex charged: %.0f -> per unit %.2f" % (
            pv_growth(E0, ORGANIC, 0.0, r), per_unit_equity(pv_growth(E0, ORGANIC, 0.0, r))))
    print()
    # fair price: each end case valued at 10%, the two averaged
    ends_ae = [per_unit_allequity(pv_nogrowth(M0, FLOOR)), per_unit_allequity(pv_growth(M0, ORGANIC, G, FLOOR))]
    ends_eq = [per_unit_equity(pv_nogrowth(E0, FLOOR)), per_unit_equity(pv_growth(E0, ORGANIC, G, FLOOR))]
    print("fair price all-equity (avg of ends at 10%%): %.2f  ends %s" % (avg(ends_ae), [round(x, 2) for x in ends_ae]))
    print("fair price equity-only (avg of ends at 10%%): %.2f  ends %s" % (avg(ends_eq), [round(x, 2) for x in ends_eq]))
    # implied unlevered yield at the price
    ev_mkt = UNITS * PRICE + NET_DEBT + PREF_CAP
    print("market EV at price %.0f; owner cash before interest avg / EV = %.4f; 2025 / EV = %.4f" % (
        ev_mkt, M0 / ev_mkt, OC_UNLEV_M[-1] / ev_mkt))
    print("equity-only: avg owner cash / market cap = %.4f; 2025 = %.4f" % (E0 / (UNITS * PRICE), OC_EQ_M[-1] / (UNITS * PRICE)))
    # default pair (acquisitions deducted), derived net acquisitions from capital employed
    d_nd = 33773 - 14485; d_ic = 12806 - 9213
    retained = sum(a - dist for a, dist in zip([1412, 1701, 1838, 1862, 1964], [1257, 1418, 1516, 1644, 1743]))
    net_acq = d_nd + d_ic + retained - sum(GROWTH_CAPEX)
    print("derived net acquisitions 2021-25: dND %d + dIC %d + retained %d - growth capex %d = %d (avg %.0f)" % (
        d_nd, d_ic, retained, sum(GROWTH_CAPEX), net_acq, net_acq / 5))
    print("default-pair base (maint OC - growth capex - net acq): %.0f" % (M0 - G - net_acq / 5))
    print("serial-acquirer test: net purchases %d vs half of owner cash before purchases (unlevered) %.0f / (equity) %.0f" % (
        net_acq, sum(OC_UNLEV_M) / 2, sum(OC_EQ_M) / 2))
