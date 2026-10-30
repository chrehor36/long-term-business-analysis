"""Q7 arithmetic for the ASML run of 2026-10-26: COMPUTATION, NOT A CLEARANCE (the file closed at Q1).
All inputs are filed figures (FY2021-FY2025 20-F cash-flow statements, EUR millions) written out below,
so the arithmetic can be checked by hand. Q7's range convention: five-year average, aggregate growth between
end years, ten years then zero nominal growth, discounted at the ECB 30-year AAA rate; fair price = each end
case valued at 10%, averaged; all-equity basis central (net cash added), equity-only beside."""

# filed: OCF, SBC, PP&E capex, intangible purchases, D&A (cash-flow statement line), by year
F = {
    2021: dict(ocf=10846.0, sbc=118.0, capex=901.0, intang=40.0, da=471.0),
    2022: dict(ocf=8487.0, sbc=69.0, capex=1282.0, intang=38.0, da=584.0),
    2023: dict(ocf=5443.4, sbc=134.8, capex=2155.6, intang=40.6, da=739.8),
    2024: dict(ocf=11166.2, sbc=172.6, capex=2067.2, intang=15.9, da=918.6),
    2025: dict(ocf=12658.5, sbc=202.3, capex=1573.6, intang=57.6, da=1025.9),
}
# contract liabilities (customer down payments), year-end, XBRL ContractWithCustomerLiability, checked to the 20-F
CL = {2020: 5594.0, 2025: 19373.0}

R = 0.0362            # ECB euro area AAA 30-year, 2026-10-23
FLOOR = 0.10
SHARES = 384.1        # millions, issued and outstanding 2026-06-28 (statutory interim report, 6-K 2026-07-15)
SHARES_COVER = 385.417665
PRICE = 1424.80       # EUR, ASML.AS, 2026-10-26, aggregator
# net cash at 2026-09-27 (6-K 2026-10-14, Exhibit 99.3): cash 8,030.9 + short-term investments 4,704.2
# less debt: long-term 1,963.0 + current portion (YE2025 total 4,390.9 less repayments 692.9 + 1,000.4 in 2026
# = 2,697.6 outstanding; current = 2,697.6 - 1,963.0 = 734.6). Finance leases inside; operating leases left out.
CASH = 8030.9 + 4704.2
DEBT = 4390.9 - 692.9 - 1000.4
NETCASH = CASH - DEBT
EUR_USD = 1.1193      # ECB reference rate 2026-10-23, USD per EUR


def series(kind):
    out = {}
    for y, f in F.items():
        if kind == "all":      # all capital spending deducted
            out[y] = f["ocf"] - f["sbc"] - f["capex"] - f["intang"]
        elif kind == "maint":  # maintenance guess = D&A as filed on the cash-flow statement
            out[y] = f["ocf"] - f["sbc"] - f["da"]
    return out


def growth(s):
    return (s[2025] / s[2021]) ** (1 / 4) - 1


def pv(base, g, r, growth_spend0=0.0, years=10):
    """Owner cash grows at g for ten years from base (year 1 = base*(1+g)), growth spending (above maintenance)
    starts at growth_spend0 in year 1 and grows at g, stops after year 10; after year 10 cash is flat (zero nominal growth)."""
    v = 0.0
    c = base
    gs = growth_spend0
    for t in range(1, years + 1):
        c = c * (1 + g)
        v += (c - gs) / (1 + r) ** t
        gs = gs * (1 + g)
    v += (c / r) / (1 + r) ** years
    return v


def report(label, base, g, gspend, r):
    lo = base / r                          # no-growth case
    hi = pv(base, g, r, gspend)            # shown-growth case
    return lo, hi


def per_share(v, add_cash=True):
    return (v + (NETCASH if add_cash else 0.0)) / SHARES


if __name__ == "__main__":
    s_all, s_m = series("all"), series("maint")
    for name, s in (("all spending", s_all), ("maintenance (D&A)", s_m)):
        print(name, {y: round(v) for y, v in s.items()}, "mean", round(sum(s.values()) / 5), "growth %.2f%%" % (100 * growth(s)))
    capex_all = {y: F[y]["capex"] + F[y]["intang"] for y in F}
    gs_avg = sum(capex_all[y] - F[y]["da"] for y in F) / 5
    print("growth spending (capex+intangibles - D&A) average %.0f" % gs_avg)
    print("net cash %.1f (cash+STI %.1f, debt %.1f)" % (NETCASH, CASH, DEBT))
    mcap = PRICE * SHARES
    print("market cap %.0f, EV %.0f" % (mcap, mcap - NETCASH))
    cases = {}
    for name, s, gspend in (("central: maintenance case", s_m, gs_avg), ("beside: all-spending case", s_all, 0.0)):
        base = sum(s.values()) / 5
        g = growth(s)
        lo, hi = report(name, base, g, gspend, R)
        flo, fhi = report(name, base, g, gspend, FLOOR)
        fair = ((flo + fhi) / 2 + NETCASH) / SHARES
        fair_eq = ((flo + fhi) / 2) / SHARES
        cases[name] = (lo, hi)
        print("\n==", name, "base %.0f growth %.2f%% growth spending yr1 %.0f yr10 %.0f" % (base, 100 * g, gspend, gspend * (1 + g) ** 9))
        print("  range at %.2f%%: whole business %.0f to %.0f; per share (all-equity, net cash added) %.0f to %.0f; equity-only %.0f to %.0f"
              % (100 * R, lo, hi, per_share(lo), per_share(hi), per_share(lo, False), per_share(hi, False)))
        print("  width top/bottom %.2f" % (hi / lo))
        print("  fair price (each end at 10%%, averaged): all-equity EUR %.0f (USD %.0f), equity-only EUR %.0f (USD %.0f)"
              % (fair, fair * EUR_USD, fair_eq, fair_eq * EUR_USD))
        # expected return at the price on each case: solve r such that value(r) = EV
        ev = mcap - NETCASH
        for which, gg, gsp in (("no-growth", 0.0, 0.0), ("shown-growth", g, gspend)):
            a, b = 0.0001, 0.5
            for _ in range(200):
                m = (a + b) / 2
                val = base / m if gg == 0 else pv(base, gg, m, gsp)
                if val > ev: a = m
                else: b = m
            print("  expected return at the price, %s case: %.2f%%" % (which, 100 * m))
    # sensitivities (beside, not the convention's range)
    base = sum(s_m.values()) / 5
    for gg in (0.10, 0.151, 0.185):
        a, b = 0.0001, 0.9
        ev = mcap - NETCASH
        for _ in range(200):
            m = (a + b) / 2
            if pv(base, gg, m, gs_avg) > ev: a = m
            else: b = m
        print("sensitivity: maintenance base, %.1f%% growth for ten years then flat -> expected return at the price %.2f%%" % (100 * gg, 100 * m))
    # customer prepayments held flat (window build-up of contract liabilities removed)
    adj = (CL[2025] - CL[2020]) / 5
    print("contract-liability build-up per year in the window %.0f; maintenance base without it %.0f" % (adj, base - adj))
    lo2 = (base - adj) / R
    print("  no-growth value without it %.0f, per share %.0f" % (lo2, per_share(lo2)))
    print("price EUR %.2f; Nasdaq equivalent at ECB 1.1193 = USD %.2f" % (PRICE, PRICE * EUR_USD))
