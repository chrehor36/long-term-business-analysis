# Q7 range, fair price and expected return at the price (R$ million unless per share). Conventions: Framework v5 Q7.
SOV = 0.1287; FLOOR = 0.10
SHARES = 2775.952565            # million, IR table September 2026 (ON + PNC outstanding)
PRICE_MCAP = 165331.0           # 2,396.17m x 59.49 + 379.79m x 59.99
NET_DEBT = 70972.6 + 683.7 - 11039.7 - (15189.7 + 441.1)   # borrowings + leases - cash - securities, 2026-06-30 (2Q26 6-K)
CDE = 4389.5 + 38569.5          # Law 14,182/2021 obligations, 2026-06-30
PTAX = 5.0826
def pv(base, g, r, years=10, tail=True, life=None):
    """g for years 1..10, then zero growth; life = number of years of cash (None = perpetual)."""
    v = 0.0; c = base
    n = life if life else 10
    for t in range(1, min(10, n) + 1):
        c = c * (1 + g); v += c / (1 + r) ** t
    if tail:
        if life is None:
            v += (c / r) / (1 + r) ** 10
        else:
            for t in range(11, life + 1):
                v += c / (1 + r) ** t
    return v
def irr(base, g, ev, life=None):
    lo, hi = 0.0005, 1.0  # perpetual tail needs r > 0; an IRR at the 0.05% bound means none positive
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(base, g, mid, life=life) > ev: lo = mid
        else: hi = mid
    return mid
def show(label, base, gs, debt, life=None):
    print(f"\n== {label}: base {base:,.0f}, growth cases {[round(g*100,2) for g in gs]}, debt deducted {debt:,.0f}, life {life}")
    ends = []
    for g in gs:
        ev = pv(base, g, SOV, life=life); ev10 = pv(base, g, FLOOR, life=life)
        ends.append((ev - debt) / SHARES); 
        print(f"  g={g*100:5.2f}%  value@sov {ev:10,.0f} -> per share {(ev-debt)/SHARES:8.2f} | value@10% per share {(ev10-debt)/SHARES:8.2f} | IRR at price {irr(base, g, PRICE_MCAP + debt, life)*100:6.2f}%")
    fair = sum((pv(base, g, FLOOR, life=life) - debt) / SHARES for g in gs) / len(gs)
    print(f"  RANGE per share {min(ends):.2f} to {max(ends):.2f}; FAIR (avg of ends at 10%) {fair:.2f} R$ = US$ {fair/PTAX:.2f} per ADS")
    return ends, fair
print(f"net debt {NET_DEBT:,.1f}; CDE {CDE:,.1f}; EV at price (all-equity) {PRICE_MCAP+NET_DEBT+CDE:,.0f}")
g_sales = (41282/34627) ** 0.25 - 1
g_shown_exgrant = (12299/6521) ** 0.25 - 1
print(f"sales growth 2021-25 {g_sales*100:.2f}%; owner-cash growth shown ex-grant {g_shown_exgrant*100:.2f}%")
# cap test (f)
base = 8388.08
print(f"cap test: base x (1+g)^10 = {base*(1+g_shown_exgrant)**10:,.0f} vs sales x 1.045^10 = {41282*(1+g_sales)**10:,.0f} -> share {base*(1+g_shown_exgrant)**10/(41282*(1+g_sales)**10)*100:.0f}% against highest filed share 29.8%")
# central: all-equity, grant aberrational, CDE in net debt
show("CENTRAL all-equity, 2022 grant left out (aberrational), CDE in net debt", base, [0.0, g_sales], NET_DEBT + CDE)
show("all-equity literal window (grant deducted), no-growth only (sign change)", 2001.02, [0.0], NET_DEBT + CDE)
show("all-equity, grant left out, CDE NOT in net debt (beside; CDE payments then unpaid in owner cash - overstated)", base, [0.0, g_sales], NET_DEBT)
show("all-equity, life-limited (cash to 2052, ~26 years) beside", base, [0.0, g_sales], NET_DEBT + CDE, life=26)
show("all-equity, most favourable defensible stress: latest year 2025 as base", 12299, [0.0, g_sales], NET_DEBT + CDE)
# equity-only
g_eq = (4842/5606) ** 0.25 - 1
print(f"\nequity-only ex-grant growth shown {g_eq*100:.2f}% (decline -> bottom)")
def show_eq(label, base, gs):
    print(f"\n== {label}: base {base:,.0f}")
    ends=[]
    for g in gs:
        v = pv(base, g, SOV); v10 = pv(base, g, FLOOR); ends.append(v/SHARES)
        print(f"  g={g*100:5.2f}% value per share @sov {v/SHARES:7.2f} @10% {v10/SHARES:7.2f}  IRR at price {irr(base,g,PRICE_MCAP)*100:6.2f}%")
    fair = sum(pv(base, g, FLOOR)/SHARES for g in gs)/len(gs)
    print(f"  RANGE {min(ends):.2f} to {max(ends):.2f}; FAIR {fair:.2f} R$ = US$ {fair/PTAX:.2f}")
show_eq("EQUITY-ONLY, grant left out", 4738.48, [g_eq, 0.0])
show_eq("EQUITY-ONLY literal (negative base)", -1648.58, [0.0])
show_eq("EQUITY-ONLY stress: 2025 as base", 4842, [0.0, g_sales])

# ---- refinements: purchases stop after year ten (tail on owner cash before purchases), depreciation variant, sensitivities
ACQ_AVG = (2721.9 + 74.3 + 1439.5 + 176.6 + 568.3) / 5
def pv2(base, g, r, add_tail):
    v = 0.0; c = base
    for t in range(1, 11):
        c *= (1 + g); v += c / (1 + r) ** t
    v += ((c + add_tail * (1 + g) ** 10) / r) / (1 + r) ** 10
    return v
def irr2(base, g, ev, add_tail):
    lo, hi = 0.0005, 1.0
    for _ in range(200):
        m = (lo + hi) / 2
        if pv2(base, g, m, add_tail) > ev: lo = m
        else: hi = m
    return m
def show2(label, base, gs, debt, add_tail=ACQ_AVG, eq=False):
    ends = []; fairs = []
    print(f"\n== {label}: base {base:,.0f}, tail adds purchases {add_tail:,.0f}")
    for g in gs:
        v = pv2(base, g, SOV, add_tail); v10 = pv2(base, g, FLOOR, add_tail)
        ends.append((v - debt) / SHARES); fairs.append((v10 - debt) / SHARES)
        print(f"  g={g*100:5.2f}% per share @sov {(v-debt)/SHARES:7.2f} (US$ {(v-debt)/SHARES/PTAX:6.2f}) @10% {(v10-debt)/SHARES:7.2f}  IRR at price {irr2(base, g, PRICE_MCAP + debt, add_tail)*100:5.2f}%")
    f = sum(fairs) / len(fairs)
    print(f"  RANGE {min(ends):.2f} to {max(ends):.2f} R$ (US$ {min(ends)/PTAX:.2f} to {max(ends)/PTAX:.2f}); FAIR {f:.2f} R$ = US$ {f/PTAX:.2f}")
print("\n\n######## REFINED (purchases stop after year ten)")
print(f"acquisitions average {ACQ_AVG:,.0f}")
show2("CENTRAL all-equity", base, [0.0, g_sales], NET_DEBT + CDE)
show2("EQUITY-ONLY", 4738.48, [g_eq, 0.0], 0.0)
dep_avg = (1443 + 2690 + 3621 + 3988 + 4577) / 5
capex_exgrant_avg = (2488 + (35277 - 31935.3) + 7391 + 7812 + 7424) / 5
print(f"\nD&A avg {dep_avg:,.0f}; capex avg ex-grant {capex_exgrant_avg:,.0f}")
show2("depreciation variant (D&A in place of capex), all-equity", base + capex_exgrant_avg - dep_avg, [0.0, g_sales], NET_DEBT + CDE)
show2("stress: judicial payments (avg 4,434) added back as if legacy ended, all-equity", base + 4434, [0.0, g_sales], NET_DEBT + CDE)
show2("stress: 2025 base + quota uplift 2.2bn, all-equity", 12299 + 2200, [0.0, g_sales], NET_DEBT + CDE)
