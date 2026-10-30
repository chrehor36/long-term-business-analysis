"""GFF run, Q7 COMPUTATION, NOT A CLEARANCE (file closed at Q2). USD millions. Sources in the run file.
Continuing operations as recast (8-K 2026-08-07, 0001628280-26-054906, Ex.99.1) and 10-Q 0001628280-26-053536."""
R = 0.0564      # 30y Treasury par, 2026-10-06
FLOOR = 0.10    # Q7 floor CONVENTION, about ten percent
SH = 45.294716  # cover shares, 2026-07-31
PRICE = 94.51   # close 2026-10-06 (aggregator)
TAX = 0.272     # filer's FY2025 effective rate excluding discrete items (recast MD&A), for the interest add-back
yrs = {  # OCF continuing, SBC, capex (gross), cash interest paid
    "FY2023": (332.826, 39.178, 31.445, 99.833),
    "FY2024": (307.370, 25.570, 50.279, 100.676),
    "FY2025": (307.794, 24.191, 41.692, 92.887),
}
# TTM to 2026-06-30: FY2025 less 9M FY2025 plus 9M FY2026; interest = expense (cash paid not in the 10-Q)
ttm = (307.794 - 234.516 + 217.944, 24.191 - 16.898 + 20.652, 41.692 - 32.498 + 23.736, 95.737 - 72.763 + 64.254)
def oc(v):
    ocf, sbc, capex, intr = v
    eq = ocf - sbc - capex
    return eq, eq + intr * (1 - TAX)
rows = {k: oc(v) for k, v in yrs.items()}
rows["TTM 2026-06"] = oc(ttm)
for k, (eq, ae) in rows.items():
    print(f"{k:12s} equity-basis owner cash {eq:7.1f}   all-equity basis {ae:7.1f}")
base_eq = sum(rows[k][0] for k in yrs) / 3
base_ae = sum(rows[k][1] for k in yrs) / 3
g_eq = (rows["FY2025"][0] / rows["FY2023"][0]) ** 0.5 - 1
g_ae = (rows["FY2025"][1] / rows["FY2023"][1]) ** 0.5 - 1
print(f"base (FY2023-25 mean): equity {base_eq:.1f}, all-equity {base_ae:.1f}; growth shown FY2023->FY2025: {g_eq:.2%} / {g_ae:.2%}")
def stream(c0, g):
    return [c0 * (1 + g) ** t for t in range(1, 11)]
def pv(s, r):
    v = sum(c / (1 + r) ** t for t, c in enumerate(s, 1))
    return v + s[-1] / r / (1 + r) ** 10   # year 11 on: zero nominal growth
NET_DEBT_0630 = 1164.436                 # 10-Q: gross debt 1,274.786 less cash 110.350
AUS_CASH = 180.910                        # subsequent event stated in the 10-Q (Australasia close, 2026-07-31)
NET_DEBT = NET_DEBT_0630 - AUS_CASH
CLAIMS = 162.039 + 118.600 + 48.593 + 20.896   # Veritage PIK note + 43% equity; Australasia PIK note + 49% equity (carrying)
print(f"net debt {NET_DEBT:.1f} (06-30 {NET_DEBT_0630:.1f} less Australasia cash {AUS_CASH:.1f}); AMES claims at carrying {CLAIMS:.1f}")
for label, c0, g, debt in (("ALL-EQUITY (central)", base_ae, g_ae, NET_DEBT), ("EQUITY-ONLY (beside)", base_eq, g_eq, 0.0)):
    top_s, bot_s = stream(c0, 0.0), stream(c0, g)
    top, bot = pv(top_s, R), pv(bot_s, R)
    mid_s = [(a + b) / 2 for a, b in zip(top_s, bot_s)]
    fair = pv(mid_s, FLOOR)
    ps = lambda v: (v - debt) / SH
    print(f"{label}: whole-business range {bot:,.0f} to {top:,.0f} (width {top/bot:.2f} to 1)")
    print(f"   per share {ps(bot):.2f} to {ps(top):.2f}; midpoint {ps((top+bot)/2):.2f}; FAIR PRICE (midpoint stream at 10%) {ps(fair):.2f}"
          f"; with AMES claims at carrying +{CLAIMS/SH:.2f}/sh -> range {ps(bot)+CLAIMS/SH:.2f} to {ps(top)+CLAIMS/SH:.2f}, fair {ps(fair)+CLAIMS/SH:.2f}")
    # expected return at the price on the central (midpoint) stream: solve r with pv(mid_s, r) - debt = PRICE*SH
    lo, hi = 0.0001, 0.5
    for _ in range(100):
        m = (lo + hi) / 2
        if pv(mid_s, m) - debt > PRICE * SH: lo = m
        else: hi = m
    print(f"   expected return at ${PRICE} on the midpoint stream: {m:.2%}")
# literal window shown beside: tools/run.py consolidated five-year mean (incl. AMES, pre-recast), capex basis
lit = 177.6
print(f"literal five-year window (consolidated incl. AMES, run.py, after interest): owner cash {lit}; no-growth equity value {lit/R:,.0f}; per share {lit/R/SH:.2f} (equity-only basis)")

# Specific (e): maintenance-only case. Maintenance guessed as depreciation (D&A less amortization of intangibles).
# D&A continuing: 35.506, 35.949, 38.473 (recast cash-flow statement). Amortization: FY2026 guidance $15M (8-K 2026-08-05 Ex.99.1);
# amortization as filed in the recast intangibles note.
AMORT = {"FY2023": 14.581, "FY2024": 14.342, "FY2025": 14.581}  # recast Note (intangibles), filed amortization
DA = {"FY2023": 35.506, "FY2024": 35.949, "FY2025": 38.473}
growth_capex = {k: yrs[k][2] - (DA[k] - AMORT[k]) for k in yrs}
print("growth spending above depreciation:", {k: round(v, 1) for k, v in growth_capex.items()})
maint_ae = base_ae + sum(growth_capex.values()) / 3
maint_eq = base_eq + sum(growth_capex.values()) / 3
print(f"maintenance-only base: all-equity {maint_ae:.1f}, equity {maint_eq:.1f}")
for label, cm, ca, g, debt in (("ALL-EQUITY (central, spec e)", maint_ae, base_ae, g_ae, NET_DEBT), ("EQUITY-ONLY (beside, spec e)", maint_eq, base_eq, g_eq, 0.0)):
    top_s, bot_s = stream(cm, 0.0), stream(ca, g)
    top, bot = pv(top_s, R), pv(bot_s, R)
    mid_s = [(a + b) / 2 for a, b in zip(top_s, bot_s)]
    fair = pv(mid_s, FLOOR)
    ps = lambda v: (v - debt) / SH
    lo, hi = 0.0001, 0.5
    for _ in range(100):
        m = (lo + hi) / 2
        if pv(mid_s, m) - debt > PRICE * SH: lo = m
        else: hi = m
    print(f"{label}: per share {ps(bot):.2f} to {ps(top):.2f} (width {top/bot:.2f} to 1 whole-business); midpoint {ps((top+bot)/2):.2f}; "
          f"FAIR {ps(fair):.2f} (claims at carrying: {ps(fair)+CLAIMS/SH:.2f}); expected return at price on midpoint stream {m:.2%}")
