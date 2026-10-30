"""TEX Q7 computation (beneath the stop if a STOP closed earlier). Every input is a filed figure; sources in comments.
Units: USD millions. Terex FY Dec; REV FY Oct (pro forma note treats the two-month gap as immaterial, S-X Art. 11)."""
R = 0.056          # US Treasury 30-year par yield, 10/09/2026 (tools/sources.py)
FLOOR = 0.10       # CONVENTION, Q7 floor
TAX = 0.245        # statutory rate the filer itself uses (8-K 0000097216-26-000124, Ex. 99.2, note (8))
NET_DEBT = 2687 - 407   # 10-Q 0000097216-26-000116: total debt less cash, 2026-06-30
SHARES = 114.3          # cover, 2026-07-28
PRICE = 51.485
yrs = [2021, 2022, 2023, 2024, 2025]
# Terex: 10-K cash-flow statements (FY2023 10-K 0000097216-24-000013 for 2021-2023; FY2025 10-K 0000097216-26-000035 for 2023-2025)
tex = dict(
    ocf=[293.4, 261.2, 459.3, 326.0, 440.0],
    sbc=[33.1, 30.3, 43.6, 30.0, 32.0],
    capex=[59.7, 109.6, 127.2, 137.0, 118.0],
    proceeds=[1.9, 0.2, 33.6, 1.0, 3.0],
    dep=[44.3, 42.4, 51.7, 58.0, 69.0],          # depreciation expense, PP&E note
    int_paid=[51.3, 37.4, 39.0, 53.0, 156.0],     # supplemental cash flow (XBRL InterestPaid)
    int_inc=[3.7, 2.8, 7.6, 13.0, 12.0],          # interest income (XBRL InvestmentIncomeInterest)
    acq=[42.7, 50.1, 23.8, 2001.0, 0.0],
    divest=[0.0, 0.0, 0.0, 0.0, 109.0],
)
# REV Group FY2021-FY2025 10-Ks (cash-flow statements; XBRL first-filed vintages)
rev = dict(
    ocf=[158.3, 91.6, 126.5, 53.4, 241.1],
    sbc=[7.8, 8.7, 14.4, 12.7, 12.3],
    capex=[24.7, 24.8, 32.8, 27.6, 51.1],
    proceeds=[0, 0, 0, 0, 0],                     # not tagged after FY2018; taken as nil (flagged)
    dep=[22.2, 25.2, 22.7, 23.2, 24.3],
    int_paid=[14.8, 12.0, 24.2, 23.8, 17.8],
    int_inc=[0, 0, 0, 0, 0],
    acq=[0, 0, 0, 0, 0],
    divest=[2.0, 0, 0.6, 371.6, 0],
)
def series(d):
    after_int = [d['ocf'][i] - d['sbc'][i] - d['capex'][i] + d['proceeds'][i] for i in range(5)]
    addback = [(d['int_paid'][i] - d['int_inc'][i]) * (1 - TAX) for i in range(5)]
    pre_int = [after_int[i] + addback[i] for i in range(5)]
    maint = [pre_int[i] + (d['capex'][i] - d['proceeds'][i] - d['dep'][i]) for i in range(5)]
    return after_int, pre_int, maint
def avg(x): return sum(x) / len(x)
def pv(c, g, r, n=10):
    v = 0; cf = c
    for t in range(1, n + 1):
        cf = cf * (1 + g); v += cf / (1 + r) ** t
    v += cf / r / (1 + r) ** n      # zero nominal growth after year ten (PG re-test specific)
    return v
def per_share(ev): return (ev - NET_DEBT) / SHARES
out = []
for name, d in (("Terex", tex), ("REV", rev)):
    a, p, m = series(d)
    out.append((name, a, p, m))
    print(name, "owner cash after interest", [round(x, 1) for x in a], "avg", round(avg(a), 1))
    print(name, "owner cash before interest (all-equity)", [round(x, 1) for x in p], "avg", round(avg(p), 1))
    print(name, "maintenance-only, before interest", [round(x, 1) for x in m], "avg", round(avg(m), 1))
comb_pre = avg(out[0][2]) + avg(out[1][2])
comb_maint = avg(out[0][3]) + avg(out[1][3])
comb_after = avg(out[0][1]) + avg(out[1][1])
print("combined all-spending pre-interest avg", round(comb_pre, 1), " maintenance-only", round(comb_maint, 1))
# Organic growth: filer reports none for the window; segment sales (10-K notes): legacy Terex 2021 MP 1691.8 + AWP 2178.8;
# 2025 MP 1681 + Aerials 2060 + Utilities held at its 2024 figure 594 (ES 2024 822 less ESG's 228 since 2024-10-08).
g_tex = (4335 / 3870.6) ** 0.25 - 1
g_rev = (2463.5 / 2380.8) ** 0.25 - 1      # REV reported sales, divestitures inside (organic understated)
w = avg(out[0][2]) / comb_pre
g = w * g_tex + (1 - w) * g_rev
print("organic growth Terex %.2f%%  REV %.2f%%  combined (owner-cash weighted) %.2f%%" % (g_tex*100, g_rev*100, g*100))
# Serial-acquirer test: net purchases over the window against half of owner cash before purchases (Terex + REV)
net_purch = sum(tex['acq']) - sum(tex['divest']) + sum(rev['acq']) - sum(rev['divest'])
oc_before = sum(out[0][2]) + sum(out[1][2])
print("net purchases", round(net_purch, 1), "vs half of owner cash before purchases", round(oc_before / 2, 1))
# Default pair beside: acquisitions deducted, total growth credited (Terex total sales 3886.8 -> 5421)
def_cash = comb_pre - (net_purch / 5)
g_tot = (5421 / 3886.8) ** 0.25 - 1
print("default pair: cash after net purchases avg", round(def_cash, 1), "total sales growth %.2f%%" % (g_tot * 100))
print()
cases = {}
for label, c in (("all-spending", comb_pre), ("maintenance-only", comb_maint)):
    for gl, gg in (("no growth", 0.0), ("organic growth", g)):
        ev = pv(c, gg, R); ev10 = pv(c, gg, FLOOR)
        cases[(label, gl)] = (ev, ev10)
        print("%-17s %-15s EV %7.0f  per share %6.2f | at 10%%: EV %6.0f per share %6.2f" % (label, gl, ev, per_share(ev), ev10, per_share(ev10)))
# expected return at the price: the rate r* at which pv(c,g,r*) = EV at price
ev_price = PRICE * SHARES + NET_DEBT
def irr(c, gg):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(c, gg, mid) > ev_price: lo = mid
        else: hi = mid
    return mid
print("EV at price", round(ev_price))
for (label, gl), _ in cases.items():
    c = comb_pre if label == "all-spending" else comb_maint
    gg = 0.0 if gl == "no growth" else g
    print("expected return at the price, %s %s: %.2f%%" % (label, gl, irr(c, gg) * 100))
# Equity-only beside: owner cash after today's interest (10-Q: interest expense net $45M in the quarter to 2026-06-30, x4)
int_now = 45 * 4 * (1 - TAX)
for label, c in (("all-spending", comb_pre), ("maintenance-only", comb_maint)):
    ce = c - int_now
    for gl, gg in (("no growth", 0.0), ("organic growth", g)):
        print("equity-only %-17s %-15s per share at 5.6%% %6.2f | at 10%% %6.2f" % (label, gl, pv(ce, gg, R) / SHARES, pv(ce, gg, FLOOR) / SHARES))
