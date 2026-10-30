# COMPUTATION, NOT A CLEARANCE. Owner cash (USD thousands) from the filed cash-flow statements.
# owner cash = OCF - stock option expense - common stock issued for services - equipment purchases (- patent purchase 2021)
rows = {  # year: (OCF, option exp, stock for services, capex, other capital, interest paid)
 2019: (-4422, 1522, 710, 35, 0, None),
 2020: (-4154, 2459, 666, 23, 0, None),
 2021: (-3937, 1872, 367, 21, 13, 99),
 2022: (-2762, 2071, 291, 271, 0, 36),
 2023: (-2365, 2124, 384, 478, 0, 58),
 2024: (-3206, 2063, 416, 1235, 0, 33),
 2025: (-8297, 2965, 648, 46, 0, 344),
}
oc = {y: r[0]-r[1]-r[2]-r[3]-r[4] for y, r in rows.items()}
for y in sorted(oc): print(y, "owner cash", oc[y])
win = [2021, 2022, 2023, 2024, 2025]
eq = sum(oc[y] for y in win)/5
ae = sum(oc[y] + rows[y][5] for y in win)/5
print("5yr mean equity-only (after interest):", round(eq))
print("5yr mean all-equity (before interest):", round(ae))
print("first half 2021-22:", (oc[2021]+oc[2022])/2, " second half 2024-25:", (oc[2024]+oc[2025])/2)
sov = 0.0543; floor = 0.10
shares = 328.731362  # millions, cover of 10-Q filed 2026-08-14
# net debt at 2026-06-30 (10-Q 0001437749-26-028023), USD thousands
debt = 1331 + 3523 + 87 + 165 + 111 + 200
cash = 2188
nd = debt - cash
nd_adj = nd + 325 - 325 - 376   # Clyra notes after quarter (+debt, +cash), Clearthink proceeds (+cash)
print("debt", debt, "cash", cash, "net debt", nd, "with stated subsequent events", nd_adj)
# no-growth case: ten years then zero nominal growth = perpetuity of the base
def pv(base, r): return base / r
for label, base, sub in [("all-equity", ae, nd_adj), ("equity-only", eq, 0)]:
    v = pv(base, sov) - sub
    f = pv(base, floor) - sub
    print(f"{label}: value at sovereign {v/1000:.1f}M = {v/1000/shares:.3f}/sh ; at 10% {f/1000:.1f}M = {f/1000/shares:.3f}/sh")
price = 0.07
print("market cap $M", round(price*shares, 2))
# sensitivity: best single year and 2021-2024 mean
m4 = sum(oc[y] for y in [2021, 2022, 2023, 2024])/4
print("2021-2024 mean (2025 left out):", round(m4), " per share at sovereign:", round((m4/sov - nd_adj)/1000/shares, 3))
best = max(oc[y] for y in win)
print("best year in window:", best)
print("--- beside the central figure ---")
dep = {2021: 20, 2022: 45, 2023: 103, 2024: 155, 2025: 145}
capx = {y: rows[y][3] + rows[y][4] for y in win}
maint = eq + sum(capx.values())/5 - sum(dep.values())/5
print("avg capex", sum(capx.values())/5, "avg dep", sum(dep.values())/5, "maintenance-only base (equity-only)", round(maint))
print("  maintenance-only at sovereign per share (equity-only):", round(maint/sov/1000/shares, 3))
print("2021-2024 mean equity-only per share at sovereign:", round(m4/sov/1000/shares, 3))
nci = {2021: 186, 2022: -659, 2023: -1144, 2024: -1945, 2025: -3409}
par = eq - sum(nci.values())/5
print("NCI avg loss share", sum(nci.values())/5, "parent-attributable sensitivity base", round(par), "per share at sovereign", round(par/sov/1000/shares, 3))
# literal window growth: compound rate between end years of a negative series
print("literal window: 2021", oc[2021], "-> 2025", oc[2025], " change", round((oc[2025]/oc[2021]-1)*100), "% (more negative)")
