# OGS run 2026-10-18: Q7 arithmetic (COMPUTATION; the convention of Q7 in THE FRAMEWORK v5, specifics a to f).
# Every input is transcribed from the filed cash-flow statements (10-K FY2025 0001587732-26-000009 for 2023-2025;
# 10-K FY2022 0001587732-23-000015 for 2020-2022) and balance sheet (10-Q Q2 2026 0001587732-26-000035). $ millions.
Y = [2021, 2022, 2023, 2024, 2025]
NI   = [206.434, 221.742, 231.232, 222.850, 264.224]
DA   = [207.233, 228.479, 279.830, 296.699, 317.256]
DEFT = [43.449, -22.034, 24.773, 106.522, 49.507]
SBC  = [10.498, 10.741, 12.184, 13.733, 14.791]
PROV = [9.131, 6.003, 9.698, 6.705, 8.207]
OCF  = [-1535.657, 1570.842, 939.532, 368.411, 578.833]
SEC  = [0.0, 1330.582, 197.366, 0.0, 0.0]          # Oklahoma securitization proceeds inside OCF (Uri)
URI_RA = [-1562.574 - 367.210, 0, 0, 0, 0]          # 2021 regulatory asset build, the Uri gas costs (filer: Winter Storm Uri)
REMOV = [49.029, 47.032, 62.023, 58.952, 52.268]    # asset removal costs, inside OCF
CAPEX = [495.246, 609.486, 666.634, 703.165, 707.226]
OINV  = [7.554 - 1.717, 8.632 - 4.008, 8.508 - 5.499, 10.402 - 6.072, 12.724 - 4.626]  # other investing, net out
INT   = [60.3, 77.5, 115.339, 147.235, 142.809]    # interest expense, net (XBRL InterestExpense 2021-22; statement 2023-25)
PRETAX= [246.7, 268.2, 271.727, 259.236, 321.459]
TAX   = [40.3, 46.5, 40.495, 36.386, 57.235]
KGSS_PRIN = [0.0, 0.0, 20.716, 27.939, 29.493]     # KGSS-I bond principal repaid (financing), serviced by the securitization charges
KGSS_INT  = [0.0, 2.0, 17.6, 16.4, 14.9]           # estimate: 5.486% on average KGSS-I bonds outstanding (CONVENTION of the run, stated)
KGSS_AMORT= [0.0, 3.5, 27.5, 30.4, 32.2]           # securitized intangible amortization inside D&A: 2025 = 265.951-233.786; 2022-2024 sum 61.4 = 327.4-265.951 (10-K FY2025 Note), split estimated
REV   = [1808.6, 2578.0, 2371.990, 2083.558, 2427.428]
OPINC = [310.3, 350.0, 377.590, 398.899, 457.467]

MAINT_SHARE = 1 - 230.0 / 800.0   # 2026 guidance, 8-K 2026-02-18 ex.99.1: $230M of $800M for extensions to new customers
RATE = 0.0543
PRICE = 75.60
SHARES = 62.856270
NET_DEBT_EX_KGSS = 2133.688 + 249.918 + 770.800 - 7.858   # 10-Q 2026-06-30; KGSS-I bonds excluded (non-recourse, self-liquidating)
KGSS_BONDS = 207.115 + 31.404

def avg(x): return sum(x) / len(x)
etr = [t / p for t, p in zip(TAX, PRETAX)]
# working capital, non-Uri: OCF less the pre-working-capital items, removal costs and the Uri items
wc = [o - (n + d + t + s + p) + r - sc - u for o, n, d, t, s, p, r, sc, u in zip(OCF, NI, DA, DEFT, SBC, PROV, REMOV, SEC, URI_RA)]
wc_avg = avg(wc)
# cash before capital spending, equity basis, SBC treated as a cost (not added back), KGSS-I principal removed
pre_eq = [n + d + t + p + w - o - k for n, d, t, p, w, o, k in zip(NI, DA, DEFT, PROV, wc, OINV, KGSS_PRIN)]
at_int = [(i - ki) * (1 - e) for i, ki, e in zip(INT, KGSS_INT, etr)]
pre_ae = [a + b for a, b in zip(pre_eq, at_int)]
spend = [c + r for c, r in zip(CAPEX, REMOV)]
maint = [s * MAINT_SHARE for s in spend]
growth_sp = [s - m for s, m in zip(spend, maint)]
da_ex = [d - k for d, k in zip(DA, KGSS_AMORT)]

def show(name, xs): print(f"{name:42s}", " ".join(f"{x:9.1f}" for x in xs), f" avg {avg(xs):9.1f}")
print("year".ljust(42), " ".join(f"{y:9d}" for y in Y))
show("effective tax rate x100", [e * 100 for e in etr])
show("working capital (non-Uri)", wc)
show("cash before capex, equity", pre_eq)
show("after-tax interest ex-KGSS", at_int)
show("cash before capex, all-equity", pre_ae)
show("capex + removal (all spending)", spend)
show("maintenance (71.25%)", maint)
show("D&A ex-KGSS amortization", da_ex)
A_ae = [p - s for p, s in zip(pre_ae, spend)]; M_ae = [p - m for p, m in zip(pre_ae, maint)]; D_ae = [p - d for p, d in zip(pre_ae, da_ex)]
A_eq = [p - s for p, s in zip(pre_eq, spend)]; M_eq = [p - m for p, m in zip(pre_eq, maint)]; D_eq = [p - d for p, d in zip(pre_eq, da_ex)]
show("OWNER CASH all-equity, all spending", A_ae); show("OWNER CASH all-equity, maintenance only", M_ae); show("OWNER CASH all-equity, depreciation variant", D_ae)
show("OWNER CASH equity, all spending", A_eq); show("OWNER CASH equity, maintenance only", M_eq); show("OWNER CASH equity, depreciation variant", D_eq)
# smoothed (working capital at its five-year average) for the growth measure
sm = lambda series: [x - w + wc_avg for x, w in zip(series, wc)]
show("maint-only all-equity, WC smoothed", sm(M_ae)); show("all-spending all-equity, WC smoothed", sm(A_ae))
show("revenue", REV); show("operating income", OPINC)
def cagr(a, b, n): return (b / a) ** (1 / n) - 1 if a > 0 and b > 0 else float('nan')
print("growth: revenue %.2f%%  operating income %.2f%%  net income %.2f%%  maint-only smoothed %.2f%%" % (
    100 * cagr(REV[0], REV[-1], 4), 100 * cagr(OPINC[0], OPINC[-1], 4), 100 * cagr(NI[0], NI[-1], 4), 100 * cagr(sm(M_ae)[0], sm(M_ae)[-1], 4)))

def value(c0, g, r, gs=0.0):
    """c0 grown at g for ten years then flat (zero nominal growth), less growth spending gs held level ten years then stopped."""
    pv = 0.0; c = c0
    for t in range(1, 11):
        c = c * (1 + g); pv += (c - gs) / (1 + r) ** t
    pv += c / r / (1 + r) ** 10
    return pv
def irr(c0, g, price_ev, gs=0.0):
    lo, hi = 0.0005, 1.0
    if value(c0, g, lo, gs) < price_ev: return float('nan')   # no positive rate equates: return below ~0
    for _ in range(200):
        mid = (lo + hi) / 2
        try: v = value(c0, g, mid, gs)
        except ZeroDivisionError: v = float('inf')
        if v > price_ev: lo = mid
        else: hi = mid
    return mid
mcap = PRICE * SHARES; ev = mcap + NET_DEBT_EX_KGSS
print(f"\nmarket cap {mcap:,.1f}  net debt ex-KGSS {NET_DEBT_EX_KGSS:,.1f}  EV {ev:,.1f}  (KGSS-I bonds {KGSS_BONDS:,.1f} beside)")
M0 = avg(M_ae); A0 = avg(A_ae); D0 = avg(D_ae); G0 = avg(growth_sp)
gM = cagr(sm(M_ae)[0], sm(M_ae)[-1], 4)
gS = min(cagr(REV[0], REV[-1], 4), RATE)
cases = {
  "M no growth (central top)": (M0, 0.0, 0.0),
  "M grown at shown growth, growth spending charged (central bottom/top)": (M0, gM, G0),
  "A all spending, no growth (literal)": (A0, 0.0, 0.0),
  "D depreciation variant, no growth": (D0, 0.0, 0.0),
  "D depreciation variant at op-income growth (no spending charged; indefensible ceiling)": (D0, cagr(OPINC[0], OPINC[-1], 4), 0.0),
}
print(f"M0 {M0:.1f}  A0 {A0:.1f}  D0 {D0:.1f}  growth spending G0 {G0:.1f}  gM {gM*100:.2f}%  sales cap {gS*100:.2f}%")
out = {}
for k, (c0, g, gs) in cases.items():
    v = value(c0, g, RATE, gs); v10 = value(c0, g, 0.10, gs)
    ps = (v - NET_DEBT_EX_KGSS) / SHARES; ps10 = (v10 - NET_DEBT_EX_KGSS) / SHARES
    out[k] = (ps, ps10)
    print(f"{k:88s} value/sh @5.43% {ps:9.2f}  @10% {ps10:9.2f}  IRR at price {irr(c0, g, ev, gs)*100:6.2f}%")
# equity-only beside
Me = avg(M_eq); De = avg(D_eq); Ge = G0
print(f"\nequity-only: M {Me:.1f}  D {De:.1f}")
for k, (c0, g, gs) in {"M eq no growth": (Me, 0, 0), "M eq growth": (Me, gM, Ge), "D eq no growth": (De, 0, 0)}.items():
    v = value(c0, g, RATE, gs) / SHARES; v10 = value(c0, g, 0.10, gs) / SHARES
    print(f"{k:30s} value/sh @5.43% {v:9.2f}  @10% {v10:9.2f}  IRR at price {irr(c0, g, mcap, gs)*100:6.2f}%")
# return on capital: operating income after tax against capital employed (equity + net debt ex-KGSS - goodwill), 2025
cap25 = 3440.123 + (2133.018 + 249.674 + 737.400 - 10.620) - 157.953
print(f"\nQ3: 2025 operating income after 21%% tax {457.467*0.79:.1f} on capital {cap25:,.1f} = {457.467*0.79/cap25*100:.2f}%")

# literal window, as filed (Uri flows and KGSS-I included), equity and all-equity, no growth
lit_eq = [o - s_ - c - oi for o, s_, c, oi in zip(OCF, SBC, CAPEX, OINV)]
lit_ae = [x + i * (1 - e) for x, i, e in zip(lit_eq, INT, etr)]
show("LITERAL owner cash equity (as filed)", lit_eq); show("LITERAL owner cash all-equity", lit_ae)
nd_incl = NET_DEBT_EX_KGSS + KGSS_BONDS
print(f"literal no-growth all-equity per share: {(avg(lit_ae)/RATE - nd_incl)/SHARES:.2f}; equity-only {avg(lit_eq)/RATE/SHARES:.2f}")
# the reporting figures
top5 = out["M grown at shown growth, growth spending charged (central bottom/top)"]; bot5 = out["M no growth (central top)"]
print(f"RANGE (all-equity, central maintenance-only pair) at 5.43%: {min(top5[0], bot5[0]):.2f} to {max(top5[0], bot5[0]):.2f}")
fair = (top5[1] + bot5[1]) / 2
Me_ng10 = value(Me, 0, 0.10) / SHARES; Me_g10 = value(Me, gM, 0.10, Ge) / SHARES
print(f"FAIR PRICE all-equity: {fair:.2f}; equity-only: {(Me_ng10 + Me_g10)/2:.2f}")
print(f"equity-only range at 5.43%: {value(Me,0,RATE)/SHARES:.2f} to {value(Me,gM,RATE,Ge)/SHARES:.2f}")
