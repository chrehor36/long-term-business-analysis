"""Q7 arithmetic for the EFX run of 2026-10-07. Arithmetic only; every input is a filed figure named in the run file.

Construction (Q7 CONVENTION and its specifics, FRAMEWORK v5): base = five-year average of owner cash after every real
cost; carried ten years at the growth shown (capped by it), then zero nominal growth; discounted at the 30-year Treasury
(5.64%, 2026-10-06). All-equity basis (central): owner cash before interest, after the company's own tax, valued as a
whole business, less net debt at 2026-06-30. Equity-only basis beside: owner cash after interest, valued as equity.
International (10.0% of five-year segment operating income) is carried at no growth (Q2, business of parts).
Fair price (Part VII reporting figure): the price at which the midpoint of the range earns 10%: the growth g_m whose
stream is worth the midpoint at 5.64% is found, and that stream is discounted at 10%.
"""
R = 0.0564
FLOOR = 0.10
SHARES = 117.484896  # million, 10-Q cover 2026-06-30
PRICE = 142.40
NET_DEBT = 5485.3 - 170.1  # total debt less cash, 10-Q 2026-06-30
INTL_SHARE = 0.100

yrs = [2021, 2022, 2023, 2024, 2025]
ocf = [1334.8, 757.1, 1116.8, 1324.5, 1615.7]
sbc = [54.9, 62.6, 71.8, 81.6, 78.4]
capex = [469.0, 624.5, 601.3, 511.5, 481.4]
intpaid = [139.7, 161.7, 231.5, 214.9, 209.7]
tax = [200.7, 229.5, 166.2, 203.2, 230.6]
pretax = [949.2, 929.7, 717.9, 810.5, 894.9]
acq_net = [2935.6, 433.8, 283.8 - 6.9, 0.0, 74.1 - 1.2]
breach_paid = [4.3, 345.0, 13.6, 0.0, 0.0]  # settlement payments by year (cumulative totals in the 10-Ks)

oc = [o - s - c for o, s, c in zip(ocf, sbc, capex)]
etr = [t / p for t, p in zip(tax, pretax)]
u = [x + i * (1 - e) for x, i, e in zip(oc, intpaid, etr)]


def pv(base, g, r, intl=INTL_SHARE):
    """PV of base grown at g for ten years (non-International share only), then flat forever."""
    total = 0.0
    for t in range(1, 11):
        cash = base * (1 - intl) * (1 + g) ** t + base * intl
        total += cash / (1 + r) ** t
    last = base * (1 - intl) * (1 + g) ** 10 + base * intl
    total += (last / r) / (1 + r) ** 10
    return total


def solve_g(target, base, r):
    lo, hi = -0.5, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(base, mid, r) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def cagr(a, b, n):
    return (b / a) ** (1 / n) - 1 if a > 0 and b > 0 else float("nan")


def case(name, base, g, equity_only=False):
    lo_v, hi_v = pv(base, 0.0, R), pv(base, g, R)
    lo_v, hi_v = min(lo_v, hi_v), max(lo_v, hi_v)
    sub = 0.0 if equity_only else NET_DEBT
    lo_ps, hi_ps = (lo_v - sub) / SHARES, (hi_v - sub) / SHARES
    mid = (lo_v + hi_v) / 2
    gm = solve_g(mid, base, R)
    fair = (pv(base, gm, FLOOR) - sub) / SHARES
    width = hi_ps / lo_ps if lo_ps > 0 else float("inf")
    print(f"{name:58s} base {base:7.1f}  g {g*100:5.2f}%  range ${lo_ps:7.2f} to ${hi_ps:7.2f}  "
          f"width {width:5.2f}x  fair ${fair:7.2f}")
    return lo_ps, hi_ps, fair


if __name__ == "__main__":
    for y, a, b, c, e in zip(yrs, oc, u, acq_net, etr):
        print(f"{y}: owner cash {a:8.1f}  all-equity {b:8.1f}  acquisitions net {c:8.1f}  ETR {e*100:4.1f}%")
    ub, ob = sum(u) / 5, sum(oc) / 5
    ab = sum(acq_net) / 5
    g_u = cagr(u[0], u[-1], 4)
    g_o = cagr(oc[0], oc[-1], 4)
    print(f"avg all-equity {ub:.1f}; avg equity-only {ob:.1f}; avg net acquisitions {ab:.1f}")
    print(f"growth shown, end years 2021-2025: all-equity {g_u*100:.2f}%, equity-only {g_o*100:.2f}%")
    h1 = (u[0] + u[1]) / 2; h2 = (u[3] + u[4]) / 2
    print(f"halves (2021-22 vs 2024-25, 2.5y apart): {cagr(h1, h2, 2.5)*100:.2f}%")
    print("--- all-equity basis (central) ---")
    print("(c) default pair, acquisitions deducted, total growth credited:")
    case("  acquisitions deducted", ub - ab, g_u)
    print("(c) organic pair, acquisitions left out, organic growth credited (filer's 2025 local-currency 7%, capped by shown):")
    case("  acquisitions left out, g 7.0%", ub, min(0.07, g_u))
    case("  acquisitions left out, breach payments added back, g 7.0%", ub + sum(breach_paid) / 5, min(0.07, g_u))
    # cycle base, trough to trough 2019-2023 on the filer's mortgage description (shown beside)
    u19 = -135.5 + 105.3 * (1 - 0.086); u20 = 470.2 + 130.9 * (1 - 0.232)
    cyc = (u19 + u20 + u[0] + u[1] + u[2]) / 5
    case("  cycle base 2019-2023, acquisitions left out, g 7.0%", cyc, 0.07)
    print("--- equity-only basis (beside) ---")
    case("  acquisitions left out, g 7.0%", ob, min(0.07, g_o), equity_only=True)
    case("  acquisitions deducted", ob - ab, g_o, equity_only=True)
    # what the price implies
    target = PRICE * SHARES + NET_DEBT
    print(f"EV at price ${target:,.0f}M; growth needed on the organic base to earn 10%: "
          f"{solve_g(target, ub, FLOOR)*100:.1f}% a year for ten years; to be worth it at 5.64%: {solve_g(target, ub, R)*100:.1f}%")
    print(f"return at price, no growth: {ub/target*100:.2f}%  (owner-cash yield on EV)")
