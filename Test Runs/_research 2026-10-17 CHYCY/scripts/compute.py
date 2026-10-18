# CHYCY Q7 COMPUTATION, NOT A CLEARANCE (the file closed at Q2). JPY millions. Inputs typed from the filed
# Kessan Tanshin cash flow statements and the 2026-06-30 balance sheet (see the run file's Step 0 table).
FY = ["FY2015","FY2016","FY2017","FY2018","FY2019","FY2020","FY2021","FY2022","FY2023","FY2024","FY2025"]
OCF   = [55526, -4375, -34115, -37941, -32217, -20806, -25591, 44157, 62747, 51175, 26132]
INTRCV= [ 1671,  1458,   1954,   1158,   1439,   1450,    702,  1519,  2681,  4908,  5920]  # interest and dividends received
INTPD = [  218,   205,    205,    215,    719,    823,    846,   792,   650,   718,   835]  # interest paid
CAPEX = [ 2607,  2100,   2594,   2253,   2262,   2149,   2139,  2784,  3886,  4022,  2346]  # PP&E + intangibles
SALES = [611548,603745,510873,341952,385925,315393,311115,430163,505981,456969,493942]
r_sov, r_floor = 0.0402, 0.10
SH = 259_183_465
cash, inv_sec, borrow = 169668, 4365, 2397          # 2026-06-30
pref, nci = 64_600_000 * 499.2 / 1e6, 2188           # preferred redemption claim; non-controlling interests (book)
adv_excess = 185277 - (35237 + 1299 + 8515)          # contract liabilities less receivables, contract assets, WIP
price = 617

oc_ae = [o - i + p - c for o, i, p, c in zip(OCF, INTRCV, INTPD, CAPEX)]   # all-equity: before interest
oc_eq = [o - c for o, c in zip(OCF, CAPEX)]                                  # equity-only: after interest
print("Owner cash by year (all-equity = OCF - interest&div received + interest paid - capex; equity-only = OCF - capex)")
for f, a, e, s in zip(FY, oc_ae, oc_eq, SALES):
    print(f"  {f}: all-equity {a:>9,}  equity-only {e:>9,}  all-equity/sales {a/s:6.1%}")
avg = lambda xs: sum(xs) / len(xs)
lit = oc_ae[6:11]; cyc = oc_ae[1:9]; cyc_b = oc_ae[0:8]; span = oc_ae
print(f"Literal five-year window FY2021-FY2025: sum {sum(lit):,} avg {avg(lit):,.0f}")
print(f"Cycle base FY2016-FY2023 (after the FY2015 peak through the FY2023 peak): sum {sum(cyc):,} avg {avg(cyc):,.0f}")
print(f"  beside: FY2015-FY2022: avg {avg(cyc_b):,.0f}; eleven years FY2015-FY2025: avg {avg(span):,.0f}")
cyc_eq = avg(oc_eq[1:9]); print(f"Equity-only cycle base FY2016-FY2023 avg {cyc_eq:,.0f}")

netcash = cash + inv_sec - borrow
claims = pref + nci
print(f"Net cash 2026-06-30: {cash:,} + {inv_sec:,} - {borrow:,} = {netcash:,}; preferred claim {pref:,.0f}; NCI {nci:,}")
print(f"Market value of common {SH*price/1e6:,.0f}; EV (common + preferred + NCI - net cash) = {SH*price/1e6 + claims - netcash:,.0f}")

def ng(base, r): return base / r                       # ten years at zero growth then zero growth = perpetuity
def gr(base, g, r):                                    # ten years at g, then zero nominal growth
    pv = sum(base * (1+g)**t / (1+r)**t for t in range(1, 11))
    return pv + base * (1+g)**10 / r / (1+r)**10
def per_share(ev, extra=0.0): return (ev + netcash - claims - extra) / SH * 1e6

B = avg(cyc)
print("\nCENTRAL (all-equity, cycle base, no growth alone: one full cycle only, growth between cycles not measurable)")
print(f"  value of operations at {r_sov:.2%}: {ng(B, r_sov):,.0f} -> per share {per_share(ng(B, r_sov)):,.0f} yen")
print(f"  fair price (operations at 10%): {ng(B, r_floor):,.0f} -> per share {per_share(ng(B, r_floor)):,.0f} yen")
print(f"  beside, excess advances {adv_excess:,} deducted: value {per_share(ng(B, r_sov), adv_excess):,.0f}; fair {per_share(ng(B, r_floor), adv_excess):,.0f} yen")
print(f"  equity-only: base {cyc_eq:,.0f}; value at sovereign {(cyc_eq/r_sov - claims)/SH*1e6:,.0f}; fair {(cyc_eq/r_floor - claims)/SH*1e6:,.0f} yen")
print(f"  expected return at the price on operations (all-equity): base / EV = {B/(SH*price/1e6 + claims - netcash):.1%}")

L = avg(lit)
h1, h2 = avg(oc_ae[6:8]), avg(oc_ae[9:11])
g_shown = (h2 / h1) ** (1/3) - 1
g_sales = (SALES[10] / SALES[6]) ** 0.25 - 1
g_cut = min(g_sales, r_sov)
print("\nBESIDE: literal five-year window")
print(f"  halves FY2021-22 avg {h1:,.0f} vs FY2024-25 avg {h2:,.0f}: shown rate {g_shown:.1%} a year (sign change between end years)")
print(f"  carried ten years that rate needs owner cash of {L*(1+g_shown)**10:,.0f}, against a highest all-equity owner cash/sales of {max(a/s for a,s in zip(oc_ae,SALES)):.1%}: cut (f)")
print(f"  sales growth FY2021-FY2025 {g_sales:.1%}; carried rate never above the discount rate: {g_cut:.2%}")
print(f"  no-growth: value {per_share(ng(L, r_sov)):,.0f}; growth: value {per_share(gr(L, g_cut, r_sov)):,.0f} yen per share")
print(f"  fair (both ends at 10%, averaged): {(per_share(ng(L, r_floor)) + per_share(gr(L, g_cut, r_floor)))/2:,.0f} yen")
print(f"  beside, excess advances deducted: no-growth {per_share(ng(L, r_sov), adv_excess):,.0f}; growth {per_share(gr(L, g_cut, r_sov), adv_excess):,.0f}")
S = avg(span)
print(f"\nBESIDE: eleven-year average {S:,.0f}: value {per_share(ng(S, r_sov)):,.0f}; fair {per_share(ng(S, r_floor)):,.0f}; with excess advances deducted value {per_share(ng(S, r_sov), adv_excess):,.0f} yen")

# Beside: the remaining preferred converted instead of redeemed (conversion only from 2029-07-01 at JPY 100; unpaid
# dividends JPY 63.2 at 2026-06-30 plus JPY 12 a year at 3% of JPY 400 to 2028-06-30 and, unredeemed, 12% compound after).
unpaid_2029 = 63.2 + 12 * 2 + (436 + 63.2 + 24) * 0.12          # to 2028-06-30 at 3%, then one year at 12% on (436+unpaid)
new_sh = 64_600_000 * (400 + unpaid_2029) / 100
dil = SH + new_sh
print(f"\nBESIDE: preferred converted at 2029-07: unpaid about {unpaid_2029:.1f} yen; {new_sh/1e6:,.0f}M new common; diluted {dil/1e6:,.0f}M")
eq10 = ng(B, r_floor) + netcash - nci
print(f"  central fair on the diluted count (no preferred claim deducted): {eq10/dil*1e6:,.0f} yen; at the sovereign {(ng(B, r_sov)+netcash-nci)/dil*1e6:,.0f} yen")
# Contract-liability build inside the literal window (cash flow statement lines 'Increase (decrease) in contract liabilities')
cl = {"FY2021": 65506, "FY2022": 14536, "FY2023": 22603, "FY2024": 22500, "FY2025": -26222}
print(f"Increase in contract liabilities inside the literal window: {sum(cl.values()):,} of owner cash {sum(lit):,}")
