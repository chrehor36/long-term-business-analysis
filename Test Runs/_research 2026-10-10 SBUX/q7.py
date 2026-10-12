"""SBUX Q7 arithmetic (COMPUTATION). All inputs from the filed statements named in the run file.
USD millions. Fiscal years end late Sept/early Oct."""
FY = [2021, 2022, 2023, 2024, 2025]
OCF = [5989.1, 4397.3, 6008.7, 6095.6, 4747.5]          # cash flow statements, FY22 and FY25 10-Ks
SBC = [319.1, 271.5, 302.7, 308.3, 318.3]
CAPEX = [1470.0, 1841.3, 2333.6, 2777.5, 2305.5]
ACQ = [0.0, 0.0, 0.0, 0.0, 177.1]                        # acquisitions, net of cash acquired
DIVEST = [1175.0, 59.3, 110.0, 0.0, 0.0]                 # net proceeds from divestitures / sale of assets (Seattle's Best brand FY23)
DA = [1524.1, 1529.4, 1450.3, 1592.4, 1771.5]            # D&A per cash flow statement (XBRL DepreciationDepletionAndAmortization; FY23-25 checked to the FY25 10-K)
INT_PAID = [501.1, 474.7, 524.3, 570.7, 588.3]           # interest paid, net of capitalized
INT_INC = [90.1, 97.0, 81.2, 122.8, 113.3]               # interest income and other, net
TAX = [1156.6, 948.5, 1277.2, 1207.3, 650.6]
PRETAX = [5356.9, 4231.9, 5401.9, 4969.6, 2507.3]
SOV = 0.0560     # US Treasury 30-year par yield, 2026-10-09
FLOOR = 0.10     # Q7 CONVENTION, about ten percent
SHARES = 1140.0  # cover of 10-Q filed 2026-07-29, as of 2026-07-23
PRICE = 90.75    # close 2026-10-09, aggregator
DEBT = 1498.4 + 11780.2                  # 10-Q Jun 28 2026: current + long-term debt
CASHLIKE = 3449.8 + 160.5 + 313.2        # cash, short-term and long-term investments
NETDEBT = DEBT - CASHLIKE
CHINA_GIVEN = 0.60 * 4000.0             # 60% of the deal's filed enterprise value (~$4bn), after-window divestiture
CHINA_GOT = 2500.0                       # net proceeds per 10-Q Q3 FY2026 cash flow discussion (total consideration $3.1bn incl. share of JV debt); already inside NETDEBT at Jun 28 2026; credited only in the equity-only figure

def avg(x): return sum(x) / len(x)
def oc(include_divest=True, levered=True, basis="capex"):
    out = []
    for i in range(5):
        spend = CAPEX[i] if basis == "capex" else DA[i]
        v = OCF[i] - SBC[i] - spend - ACQ[i] + (DIVEST[i] if include_divest else 0.0)
        if not levered:
            t = TAX[i] / PRETAX[i]
            v += (INT_PAID[i] - INT_INC[i]) * (1 - t)
        out.append(v)
    return out
def halves_growth(s):
    a, b = avg(s[:2]), avg(s[-2:])
    return (b / a) ** (1 / 3) - 1
def pv(base, g, r, years=10):
    v, cf = 0.0, base
    for y in range(1, years + 1):
        cf *= (1 + g)
        v += cf / (1 + r) ** y
    term = cf / r / (1 + r) ** years     # zero nominal growth after year ten
    return v + term
def per_share(ev, all_equity=True):
    eq = ev - (NETDEBT if all_equity else 0.0) - CHINA_GIVEN + (0.0 if all_equity else CHINA_GOT)
    return eq / SHARES
def case(label, include_divest, basis="capex"):
    u = oc(include_divest, levered=False, basis=basis); l = oc(include_divest, levered=True, basis=basis)
    bu, bl = avg(u), avg(l); g = halves_growth(u); gl = halves_growth(l)
    top = per_share(pv(bu, 0.0, SOV)); bot = per_share(pv(bu, g, SOV))
    mid_ev_floor = (pv(bu, 0.0, FLOOR) + pv(bu, g, FLOOR)) / 2
    fair = per_share(mid_ev_floor)
    fair_eq = per_share((pv(bl, 0.0, FLOOR) + pv(bl, gl, FLOOR)) / 2, all_equity=False)
    top_eq = per_share(pv(bl, 0.0, SOV), False); bot_eq = per_share(pv(bl, gl, SOV), False)
    print(f"\n== {label}")
    print("  unlevered owner cash by FY:", [round(x, 1) for x in u], " avg", round(bu, 1), " halves growth", f"{g:.1%}")
    print("  levered owner cash by FY:  ", [round(x, 1) for x in l], " avg", round(bl, 1), " halves growth", f"{gl:.1%}")
    print(f"  ALL-EQUITY range ${bot:.2f} to ${top:.2f} a share (width {top/bot if bot>0 else float('nan'):.2f}x); fair price ${fair:.2f}")
    print(f"  EQUITY-ONLY range ${bot_eq:.2f} to ${top_eq:.2f}; fair price ${fair_eq:.2f}")
    print(f"  price ${PRICE}; implied all-equity yield on the no-growth base: {bu/(PRICE*SHARES+NETDEBT):.2%}")
print(f"net debt {NETDEBT:.1f}; market cap {PRICE*SHARES:.1f}; EV {PRICE*SHARES+NETDEBT:.1f}")
case("CENTRAL: literal window FY2021-25, all capital spending, divestiture proceeds inside the window counted per specific (c)", True)
case("VARIANT: in-window divestiture proceeds left out", False)
case("VARIANT: depreciation in place of capital spending, (c) literal", True, basis="da")
# the price-implied growth: what ten-year growth on the central unlevered base makes the PV at the sovereign equal the price
bu = avg(oc(True, False))
lo, hi = -0.5, 0.5
for _ in range(100):
    m = (lo + hi) / 2
    if per_share(pv(bu, m, SOV)) < PRICE: lo = m
    else: hi = m
print(f"\nten-year growth the price assumes at the sovereign (central base, zero after year ten): {m:.1%}")
for _ in range(1):
    lo, hi = -0.5, 0.9
    for _ in range(100):
        m = (lo + hi) / 2
        if per_share(pv(bu, m, FLOOR)) < PRICE: lo = m
        else: hi = m
    print(f"ten-year growth needed for the price to earn the floor: {m:.1%}")
