"""Q7 arithmetic for MLLUY (Metallurgical Corporation of China, HKEX 1618 / SSE 601618).
COMPUTATION, NOT A CLEARANCE wherever the run closed before Q7. Arithmetic only; every judgment is
in the run file. RMB billions unless stated. Sources: consolidated cash flow statements, income
statements, EPS notes and segment notes of the annual reports 2016-2025 (HKEX 1618), the 2026 interim
report (gearing note, balance sheet at 30 June 2026), quotes of 2026-10-16 (aggregator, flagged).
usage: python -I q7_computation.py"""

# ---- filed inputs (RMB bn) --------------------------------------------------------------------
CFO = {2016: 18.559, 2017: 18.418, 2018: 14.050, 2019: 17.578, 2020: 28.032,
       2021: 17.640, 2022: 18.153, 2023: 5.892, 2024: 7.848, 2025: 15.323}
CAPEX = {2016: 3.115, 2017: 4.079, 2018: 5.595, 2019: 4.110, 2020: 3.743,
         2021: 3.551, 2022: 4.314, 2023: 4.595, 2024: 6.863, 2025: 6.278}
NET_ACQ = {2021: -0.088, 2022: 0.356 - 0.004, 2023: -0.012, 2024: 0.0, 2025: 0.0}  # 2025 segment sale excluded (in net debt)
NET_INVEST = {2021: 4.972 - 3.136, 2022: 5.472 - 0.588, 2023: 4.902 - 0.472, 2024: 3.593 - 0.487, 2025: 4.337 - 0.485}
DA = {2021: 3.546, 2022: 3.931, 2023: 4.065, 2024: 4.489, 2025: 4.787}          # segment notes
INT_EXP = {2021: 2.140, 2022: 2.633, 2023: 2.643, 2024: 3.393, 2025: 3.654}     # income statements (2024 as restated)
PERP = {2021: 1.086, 2022: 1.039, 2023: 1.782, 2024: 1.862, 2025: 1.275}        # EPS notes
NCI_DIV = {2021: 1.935, 2022: 1.601, 2023: 1.237, 2024: 0.464, 2025: 1.782}     # cash flow statements
REV = {2016: 219.558, 2021: 500.572, 2022: 592.669, 2023: 633.870, 2024: 552.025, 2025: 455.380}

# balance sheet at 30 June 2026 (interim report, gearing note and balance sheet)
NET_DEBT = 20.812        # company's own: borrowings + bonds + leases less cash and cash equivalents
PERPETUAL = 54.100       # perpetual bonds, classed in equity by the filer
MINORITY = 28.192        # minority interests, book
CLAIMS = NET_DEBT + PERPETUAL + MINORITY

# shares: 20,691,619,170 issued at 30 June 2026 less repurchased-uncancelled stated at the interim
# report's date (181,683,707 A and 33,815,000 H)
A_SH = 17_852_619_170 - 181_683_707
H_SH = 2_839_000_000 - 33_815_000
SHARES = (A_SH + H_SH) / 1e9
H_HKD, A_RMB, HKDRMB, USDHKD = 1.315, 2.58, 0.8526, 7.8477   # closes 2026-10-16 (Yahoo, aggregator)
H_RMB = H_HKD * HKDRMB
RATE = 0.0206            # MoF China government bond yield curve, 30-year, 2026-10-16
FLOOR = 0.10


def pv(cash0, g, r, years=10):
    """cash0 = base-year owner cash; grows at g for `years`, then flat (zero nominal growth)."""
    v, c = 0.0, cash0
    for t in range(1, years + 1):
        c *= (1 + g)
        v += c / (1 + r) ** t
    v += (c / r) / (1 + r) ** years
    return v


def show(name, oc, label):
    yrs = sorted(oc)
    base = sum(oc.values()) / len(oc)
    first, last = oc[yrs[0]], oc[yrs[-1]]
    g = (last / first) ** (1 / (yrs[-1] - yrs[0])) - 1 if first > 0 and last > 0 else None
    print(f"\n== {name}: {label}")
    print("   by year:", ", ".join(f"{y} {oc[y]:.2f}" for y in yrs), f"| five-year average {base:.3f}")
    print("   shown growth end-to-end:", "meaningless (sign change)" if g is None else f"{100*g:.2f}%/yr")
    return base, g


def per_share(total_value, deduct):
    return (total_value - deduct) / SHARES


oc_all = {y: CFO[y] - CAPEX[y] - NET_ACQ[y] for y in range(2021, 2026)}
base, g = show("A. central, all-equity basis", oc_all, "CFO (interest paid sits in financing under ASBE) less all capex less net acquisitions")
print(f"   share of sales: max owner cash/sales in window {max(oc_all[y]/REV[y] for y in oc_all)*100:.2f}%")
cases = {"no growth": 0.0, f"decline {100*g:.1f}%": g}
vals = {}
for k, gg in cases.items():
    v_r = pv(base, gg, RATE)
    v_f = pv(base, gg, FLOOR)
    vals[k] = (v_r, v_f)
    print(f"   {k:16s} whole business at {100*RATE:.2f}%: {v_r:7.1f} -> per share RMB {per_share(v_r, CLAIMS):6.2f};"
          f" at 10%: {v_f:6.1f} -> per share RMB {per_share(v_f, CLAIMS):6.2f}")
lo = min(per_share(v[0], CLAIMS) for v in vals.values()); hi = max(per_share(v[0], CLAIMS) for v in vals.values())
fair = sum(per_share(v[1], CLAIMS) for v in vals.values()) / 2
print(f"   RANGE per share RMB {lo:.2f} to {hi:.2f}; width {hi/lo:.1f} to 1" if lo > 0 else f"   RANGE per share RMB {lo:.2f} to {hi:.2f}")
print(f"   FAIR PRICE (each end at 10%, averaged) RMB {fair:.2f} per share = HK$ {fair/HKDRMB:.2f} per H share = US$ {20*fair/HKDRMB/USDHKD:.2f} per ADR")
print(f"   claims deducted: net debt {NET_DEBT} + perpetual {PERPETUAL} + minority {MINORITY} = {CLAIMS:.1f}")
print(f"   expected return at the price, no-growth case: EV at H price {SHARES*H_RMB + CLAIMS:.1f} -> {100*base/(SHARES*H_RMB+CLAIMS):.2f}%;"
      f" EV at A and H market prices {A_SH/1e9*A_RMB + H_SH/1e9*H_RMB + CLAIMS:.1f} -> {100*base/(A_SH/1e9*A_RMB + H_SH/1e9*H_RMB + CLAIMS):.2f}%")
print(f"   without the perpetual and minority claims (net debt only): no-growth return at H price {100*base/(SHARES*H_RMB+NET_DEBT):.2f}%")

# beside: depreciation variant, investments variant, cycle base, literal window
oc_da = {y: CFO[y] - DA[y] - NET_ACQ[y] for y in range(2021, 2026)}
show("A2. beside: depreciation in place of capex", oc_da, "CFO less D&A less net acquisitions")
oc_inv = {y: oc_all[y] - NET_INVEST[y] for y in range(2021, 2026)}
b_inv, _ = show("A3. beside: also net cash into investments (PPP and associate stakes)", oc_inv, "A less net investment payments")
oc10 = {y: CFO[y] - CAPEX[y] for y in range(2016, 2026)}
b10 = sum(oc10.values()) / 10
h1 = sum(oc10[y] for y in range(2016, 2021)) / 5; h2 = sum(oc10[y] for y in range(2021, 2026)) / 5
print(f"\n== A4. beside: ten-year base 2016-2025 (CFO less capex): average {b10:.2f}; halves {h1:.2f} -> {h2:.2f}"
      f" ({100*((h2/h1)**(1/5)-1):.1f}%/yr between half-averages)")
for k, gg in {"no growth": 0.0, "half-to-half": (h2/h1)**(1/5)-1}.items():
    print(f"   {k:14s} at 10%: per share RMB {per_share(pv(b10, gg, FLOOR), CLAIMS):6.2f}; at {100*RATE:.2f}%: RMB {per_share(pv(b10, gg, RATE), CLAIMS):6.2f}")

# equity-only beside
oc_eq = {y: oc_all[y] - INT_EXP[y] - PERP[y] - NCI_DIV[y] for y in range(2021, 2026)}
b_eq, g_eq = show("B. beside: equity-only", oc_eq, "A less interest expense, perpetual coupons and dividends to minority holders")
v_r, v_f = b_eq / RATE, b_eq / FLOOR
print(f"   no-growth case alone (series changes sign): value at {100*RATE:.2f}% {v_r:.1f} -> RMB {v_r/SHARES:.2f}/share;"
      f" FAIR (10%) {v_f:.1f} -> RMB {v_f/SHARES:.2f}/share = HK$ {v_f/SHARES/HKDRMB:.2f} = US$ {20*v_f/SHARES/HKDRMB/USDHKD:.2f}/ADR")

print(f"\nprice: H HK$ {H_HKD} = RMB {H_RMB:.3f}; A RMB {A_RMB}; ADR at 20 H = US$ {20*H_HKD/USDHKD:.2f}; shares {SHARES:.4f} bn"
      f"; market value at A and H prices RMB {A_SH/1e9*A_RMB + H_SH/1e9*H_RMB:.1f} bn; all shares at H price RMB {SHARES*H_RMB:.1f} bn")
