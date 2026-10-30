"""MSA run 2026-10-10: owner cash recast (Q4) and the Q7 range and fair price, as COMPUTATION.
Every input is a filed figure (USD millions), cited in the run file. Arithmetic only; the judgments are in the run file."""
YEARS = [2021, 2022, 2023, 2024, 2025]
# Filed consolidated statements of cash flows (10-K FY2022 for 2021-2022, 10-K FY2025 for 2023-2025)
OCF   = {2021: 199.145, 2022: 157.455, 2023: 92.857, 2024: 296.428, 2025: 363.867}
SBC   = {2021: 18.908, 2022: 19.650, 2023: 30.023, 2024: 18.185, 2025: 15.197}
CAPEX = {2021: 43.837, 2022: 42.553, 2023: 42.764, 2024: 54.223, 2025: 68.438}
ACQ   = {2021: 392.437 + 13.381, 2022: 0.0, 2023: 0.0, 2024: 0.0, 2025: 189.275}  # incl. 2021 purchase of minority interests
NCI_DIST = {2021: 5.632, 2022: 0, 2023: 0, 2024: 0, 2025: 0}                    # dividends to minority partners
CONTRIB = {2023: 341.186}                                                         # cash contributed on the MSA LLC sale
INT_PAID = {2021: 9.3, 2022: 20.7, 2023: 47.258, 2024: 35.703, 2025: 32.135}      # supplemental cash flow / XBRL InterestPaidNet
INT_INC  = {2021: 3.3, 2022: 4.2, 2023: 8.2, 2024: 7.0, 2025: 5.9}               # XBRL InterestIncomeOperating (Note 17)
DA    = {2021: 50.317, 2022: 56.317, 2023: 60.773, 2024: 64.333, 2025: 71.591}   # cash-flow D&A
AMORT = {2021: 16.8, 2022: 19.1, 2023: 18.1, 2024: 17.8, 2025: 20.7}             # amortization of acquired intangibles (XBRL; Note 14)
TAX = 0.24                    # filer's effective rate, 23.9% (2025), 24.0% (2024), rounded; applied to net interest only
R = 0.056                     # 30-year Treasury par yield, 2026-10-09
FLOOR = 0.10                  # CONVENTION (Q7): about ten percent
NET_DEBT = 954.7              # 2026-06-30 net debt $399.7M + Autronica $555M (10-Q Note 20)
SHARES = 38.578289            # cover, 2026-07-24
PRICE = 180.71

def oc(y, contrib_back=True, acq=False, maint_only=False):
    capex = (DA[y] - AMORT[y]) if maint_only else CAPEX[y]
    v = OCF[y] - SBC[y] - capex - NCI_DIST[y] + (INT_PAID[y] - INT_INC[y]) * (1 - TAX)
    if contrib_back: v += CONTRIB.get(y, 0)
    if acq: v -= ACQ[y]
    return v

def pv(base, g, r=R, n=10):
    """base carried at g for n years, then zero nominal growth, discounted at r (Q7 convention)."""
    s = sum(base * (1 + g) ** t / (1 + r) ** t for t in range(1, n + 1))
    term = base * (1 + g) ** n / r / (1 + r) ** n
    return s + term

def per_share(ev):
    return (ev - NET_DEBT) / SHARES

def show(label, series):
    avg = sum(series.values()) / len(series)
    print(f"{label:58s} " + " ".join(f"{series[y]:8.1f}" for y in YEARS) + f"   avg {avg:7.1f}")
    return avg

print("owner cash, all-equity (before net interest after tax), USD M:", YEARS)
a1 = show("A. pre-acquisition, contribution put back (central)", {y: oc(y) for y in YEARS})
a2 = show("B. pre-acquisition, literal (contribution counted)", {y: oc(y, contrib_back=False) for y in YEARS})
a3 = show("C. acquisitions deducted, contribution put back", {y: oc(y, acq=True) for y in YEARS})
a4 = show("D. acquisitions deducted, literal", {y: oc(y, contrib_back=False, acq=True) for y in YEARS})
a5 = show("E. maintenance-only capex, pre-acq, contribution back", {y: oc(y, maint_only=True) for y in YEARS})
a6 = show("F. maintenance-only, acquisitions deducted, contribution back", {y: oc(y, acq=True, maint_only=True) for y in YEARS})

# organic growth, filer's own yearly figures 2021-2025 (2023 constant currency)
org = [-0.023, 0.099, 0.161, 0.015, 0.007]
p = 1.0
for x in org: p *= 1 + x
g_org = p ** (1 / 5) - 1
print(f"\norganic growth compounded 2021-2025: {g_org:.4f}")

def total_growth(series):
    s = [series[y] for y in YEARS]
    first, second = (s[0] + s[1]) / 2, (s[3] + s[4]) / 2
    return s, first, second

for lab, ser in [("C", {y: oc(y, acq=True) for y in YEARS}), ("D", {y: oc(y, contrib_back=False, acq=True) for y in YEARS})]:
    s, f, sc = total_growth(ser)
    print(f"total growth test on {lab}: end years {s[0]:.1f} -> {s[-1]:.1f}; halves {f:.1f} -> {sc:.1f}",
          "(sign change: meaningless)" if (min(s) < 0 < max(s)) else "")

print("\nRANGES (enterprise value -> per share, net debt $954.7M, 38.578M shares) against price $180.71")
def rng(label, base, g):
    lo, hi = pv(base, 0.0), pv(base, g)
    lo, hi = min(lo, hi), max(lo, hi)
    print(f"{label:64s} EV {lo:7.0f} to {hi:7.0f}  per share ${per_share(lo):7.2f} to ${per_share(hi):7.2f}  width {hi/lo if lo>0 else float('nan'):.2f}x")
    return lo, hi
rA = rng("A, organic pair (pre-acq, organic growth credited), CENTRAL", a1, g_org)
rE = rng("E, organic pair, maintenance-only capex", a5, g_org)
rB = rng("B, organic pair, literal window (contribution counted)", a2, g_org)
rC = rng("C, default pair: acquisitions deducted, no-growth only", a3, 0.0)
rD = rng("D, default pair literal: acquisitions deducted, no-growth only", a4, 0.0)

print("\nFAIR PRICE: the midpoint case (base at half the shown growth for ten years, then zero), discounted at the 10% floor")
def fair(label, base, g):
    ev = pv(base, g / 2, r=FLOOR)
    eq_ev = ev  # all-equity basis
    print(f"{label:64s} EV {ev:7.0f}  per share ${per_share(eq_ev):7.2f}")
    return per_share(eq_ev)
fA = fair("A, central (all-equity)", a1, g_org)
fE = fair("E, maintenance-only", a5, g_org)
fB = fair("B, literal", a2, g_org)

# equity-only: owner cash after interest (not added back), against market cap alone
def oc_eq(y, contrib_back=True):
    return oc(y, contrib_back) - (INT_PAID[y] - INT_INC[y]) * (1 - TAX)
eA = sum(oc_eq(y) for y in YEARS) / 5
# equity-only must also bear Autronica's financing cost: $555M at the revolver rate 4.56% after tax, not in the window
autr_int = 555 * 0.0456 * (1 - TAX)
eA_adj = eA - autr_int
ev_eq = pv(eA_adj, g_org / 2, r=FLOOR)
print(f"\nequity-only: owner cash after net interest avg {eA:.1f}; less Autronica financing after tax {autr_int:.1f} -> {eA_adj:.1f};"
      f" fair per share ${ev_eq/SHARES:.2f}")
lo_e, hi_e = pv(eA_adj, 0), pv(eA_adj, g_org)
print(f"equity-only range per share ${lo_e/SHARES:.2f} to ${hi_e/SHARES:.2f}")

# expected return at the price, central case: rate that sets pv(base, g) = EV at price
ev_price = PRICE * SHARES + NET_DEBT
lo, hi = 0.0, 0.5
for _ in range(100):
    mid = (lo + hi) / 2
    if pv(a1, g_org, r=mid) > ev_price: lo = mid
    else: hi = mid
print(f"\nimplied return at the price, central base and full organic growth: {mid:.4f}; EV at price {ev_price:.1f}")
for _ in range(1):
    lo, hi = 0.0, 0.5
    for _ in range(100):
        mid = (lo + hi) / 2
        if pv(a1, g_org / 2, r=mid) > ev_price: lo = mid
        else: hi = mid
    print(f"implied return at the price, central base, midpoint growth: {mid:.4f}")

print("\nSENSITIVITIES (shown beside, not the convention's case)")
yrs4 = [2022, 2023, 2024, 2025]
b4 = sum(oc(y) for y in yrs4) / 4
p4 = 1.0
for x in org[1:]: p4 *= 1 + x
g4 = p4 ** 0.25 - 1
lo4, hi4 = pv(b4, 0), pv(b4, g4)
print(f"four-year window 2022-2025 (2021 treated as supply-constrained): base {b4:.1f}, organic growth {g4:.4f}:"
      f" ${per_share(lo4):.2f} to ${per_share(hi4):.2f}")
autr = 555 / SHARES
print(f"Autronica credited at its cost instead of at nothing: +${autr:.2f} a share on every figure;"
      f" central top becomes ${per_share(rA[1]) + autr:.2f}; four-year top becomes ${per_share(hi4) + autr:.2f}")
ga = 0.06
print(f"central base at 6% growth (above the shown organic rate): top ${per_share(pv(a1, ga)):.2f}")
