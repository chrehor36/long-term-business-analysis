"""COMPUTATION, NOT A CLEARANCE: Q7's range and the fair price for RAIL, by Q7's range convention.
Inputs are the filed figures (XBRL first-filed, checked against the 10-Ks); USD millions. Arithmetic only."""
r, floor, stat = 0.0543, 0.10, 0.21
shares = 32.791280 + 3 * 0.004132            # cover count 2026-07-31 plus the three penny warrants
price = 5.92
debt = 2.875 + 97.850                          # 10-Q 2026-06-30, current and long-term debt
cash = 62.978                                  # 10-Q 2026-06-30, incl. 0.503 restricted
net_debt = debt - cash
dta = 52.053                                   # net deferred tax asset, 10-Q 2026-06-30 (shelter cap)
yrs = list(range(2011, 2026))
ocf = dict(zip(yrs, [30.0, 53.0, 32.2, -6.0, -65.7, 0.2, 40.3, -31.6, -19.0, -58.9, -55.4, 11.5, 4.8, 44.9, 34.8]))
sbc = dict(zip(yrs, [2.2, 1.7, 2.3, 2.1, 2.2, 1.1, 1.2, 3.2, 1.2, 1.0, 3.0, 2.1, 1.2, 3.1, 3.6]))
capex = dict(zip(yrs, [1.8, 9.1, 17.3, 11.8, 16.7, 13.8, 1.0, 2.2, 5.6, 9.8, 2.3, 7.8, 12.7, 5.0, 3.4]))
dep = dict(zip(yrs, [8.8, 8.4, 10.1, 10.1, 10.0, 9.7, 9.4, 12.0, 12.4, 9.2, 4.3, 4.1, 4.6, 5.8, 6.2]))
flp = {2022: 0.738, 2023: 1.007, 2024: 2.145, 2025: 1.093}
acq = {2025: 6.3}
intpaid = dict(zip(yrs, [None, None, None, None, 0.1, 0.1, 0.1, 0.1, 0.2, 0.4, 6.5, 8.8, 4.9, 4.6, 13.8]))
def oc_eq(y):    # owner cash after interest: operating cash less stock pay, all capital spending, finance-lease principal, acquisitions
    return ocf[y] - sbc[y] - capex[y] - flp.get(y, 0) - acq.get(y, 0)
def oc_all(y):   # before interest: add back cash interest at the statutory rate's after-tax cost
    return oc_eq(y) + (intpaid[y] or 0) * (1 - stat)
def mean(f, ys): return sum(f(y) for y in ys) / len(ys)
print("year  owner cash (equity)  (all-equity)  dep-variant(equity)")
for y in yrs:
    print(y, f"{oc_eq(y):8.1f} {oc_all(y) if intpaid[y] is not None else float('nan'):8.1f} {ocf[y]-sbc[y]-dep[y]-flp.get(y,0)-acq.get(y,0):8.1f}")
def shelter_pv(oc_case):
    """PV at the long rate of 21% of a positive case's owner cash a year, until the recorded net DTA is used."""
    if oc_case <= 0: return 0.0
    left, pv, t = dta, 0.0, 0
    while left > 1e-9 and t < 200:
        t += 1; s = min(left, stat * oc_case); left -= s; pv += s / (1 + r) ** t
    return pv
def value(oc, rate):          # no-growth case: zero nominal growth for ever (growth meaningless, specific (b))
    return oc / rate
cases = {
    "CENTRAL cycle base FY2018-FY2024 (spec (a))": list(range(2018, 2025)),
    "beside: cycle FY2017-FY2023": list(range(2017, 2024)),
    "beside: literal window FY2021-FY2025": list(range(2021, 2026)),
}
out = []
for name, ys in cases.items():
    a, e = mean(oc_all, ys), mean(oc_eq, ys)
    sh = shelter_pv(a)
    ev = value(a, r); eq_all = (ev + sh - net_debt) / shares
    fair_all = (value(a, floor) + sh - net_debt) / shares
    eq_only = (value(e, r) + shelter_pv(e)) / shares
    fair_eq = (value(e, floor) + shelter_pv(e)) / shares
    req = floor * (price * shares + net_debt - sh)
    out.append((name, a, e, sh, eq_all, fair_all, eq_only, fair_eq, a / (price * shares + net_debt - sh) * 100, req))
# working-capital specific (d): FY2021 VAT receivable draw of 24.7 tied by the filer to production increases and refund delays
ys = list(range(2021, 2026))
a = mean(oc_all, ys) + 24.7 / 5; e = mean(oc_eq, ys) + 24.7 / 5; sh = shelter_pv(a)
out.append(("beside: literal window, FY2021 VAT draw removed (spec (d))", a, e, sh, (value(a, r) + sh - net_debt) / shares,
            (value(a, floor) + sh - net_debt) / shares, (value(e, r) + shelter_pv(e)) / shares, (value(e, floor) + shelter_pv(e)) / shares,
            a / (price * shares + net_debt - sh) * 100, floor * (price * shares + net_debt - sh)))
print(f"\nshares {shares:.3f}M  price {price}  market value {price*shares:.1f}  net debt {net_debt:.2f}  sovereign {r:.2%}")
for o in out:
    print(f"\n{o[0]}\n  owner cash all-equity {o[1]:.2f}  equity-only {o[2]:.2f}  shelter PV {o[3]:.1f}"
          f"\n  value/share at {r:.2%} (all-equity) {o[4]:.2f}   fair price at 10% (all-equity) {o[5]:.2f}"
          f"\n  value/share equity-only {o[6]:.2f}   fair equity-only {o[7]:.2f}"
          f"\n  return at the price (all-equity, on EV less shelter) {o[8]:.1f}%  owner cash needed for 10%: {o[9]:.1f}")

# CHECK, not a case: the years after the move to Mexico only, FY2022-FY2025 (a chosen start year, flagged)
ys = list(range(2022, 2026)); a = mean(oc_all, ys); sh = shelter_pv(a)
print(f"\nCHECK FY2022-FY2025 only: owner cash all-equity {a:.2f}, shelter PV {sh:.1f}, "
      f"return at the price {a/(price*shares+net_debt-sh)*100:.1f}%, no-growth value/share at 5.43% {(a/r+sh-net_debt)/shares:.2f}")
ys = [2024, 2025]; a = mean(oc_all, ys); sh = shelter_pv(a)
print(f"CHECK FY2024-FY2025 only (the two best years): owner cash all-equity {a:.2f}, shelter PV {sh:.1f}, "
      f"return at the price {a/(price*shares+net_debt-sh)*100:.1f}%")
