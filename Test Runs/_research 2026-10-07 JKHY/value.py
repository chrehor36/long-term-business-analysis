"""Q7 arithmetic for JKHY (CONVENTION construction of the framework, Q7). USD millions; per share on 70.1126M shares."""
R = 0.0564; FLOOR = 0.10; SH = 70.112608; PRICE = 146.07
NETDEBT = 40.000 - 12.056 + 0.61 * SH      # debt less cash at 2026-06-30, plus the dividend declared 2026-08-21 (Note 15)
def pv(c, g, r, n=10):
    v = 0.0; x = c
    for t in range(1, n + 1):
        x *= (1 + g); v += x / (1 + r) ** t
    return v + x / r / (1 + r) ** n          # zero nominal growth after year ten
def solve_g(c, target, r):
    lo, hi = -0.5, 0.5
    for _ in range(200):
        m = (lo + hi) / 2
        if pv(c, m, r) < target: lo = m
        else: hi = m
    return m
def case(name, c, g):
    lo_v, hi_v = pv(c, 0, R), pv(c, g, R)
    bot, top = min(lo_v, hi_v), max(lo_v, hi_v)
    mid = (bot + top) / 2
    gm = solve_g(c, mid, R)
    fair_ev = pv(c, gm, FLOOR)
    ps = lambda v: (v - NETDEBT) / SH
    print(f"{name}: C={c:.1f} g={g*100:.2f}%  EV range {bot:,.0f}-{top:,.0f}  per share ${ps(bot):.2f}-${ps(top):.2f}"
          f"  width {top/bot:.2f}x  mid-stream g={gm*100:.2f}%  fair EV {fair_ev:,.0f} fair price ${ps(fair_ev):.2f}")
    return ps(bot), ps(top), ps(fair_ev)
print(f"net debt {NETDEBT:.1f}; market value {PRICE*SH:,.0f}; EV at price {PRICE*SH+NETDEBT:,.0f}")
case("A default pair (all-equity, acquisitions deducted, total growth at book tax)", 272.8, 0.0805)
case("B organic pair (all-equity, acquisitions left out, filer's organic revenue growth)", 327.2, 0.073)
case("C at book tax, acquisitions deducted", 306.1 - 54.4, 0.0805)
case("D literal window, as-filed end-to-end growth (shown, not used)", 272.8, 0.1329)
# equity-only beside: owner cash after interest, against market value alone (no net debt)
def case_eq(name, c, g):
    lo_v, hi_v = pv(c, 0, R), pv(c, g, R); mid = (lo_v + hi_v) / 2; gm = solve_g(c, mid, R)
    print(f"{name}: per share ${lo_v/SH:.2f}-${hi_v/SH:.2f} fair ${pv(c, gm, FLOOR)/SH:.2f}")
case_eq("equity-only default pair", 319.4 - 54.4, 0.0805)
case_eq("equity-only organic pair", 319.4, 0.073)
# what growth does the price imply at the sovereign and at the floor, on the default base
ev = PRICE * SH + NETDEBT
print("growth for ten years implied by price: at 5.64%% %.2f%%; at 10%% %.2f%%" % (solve_g(272.8, ev, R) * 100, solve_g(272.8, ev, FLOOR) * 100))
print("organic base: at 10%% %.2f%%" % (solve_g(327.2, ev, FLOOR) * 100))
