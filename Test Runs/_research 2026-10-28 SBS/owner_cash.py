"""SBS (SABESP) owner cash and the Q7 range. Arithmetic only; every input is from the filed statements named in
the run file (R$ million). tools/run.py failed on this IFRS filer, so the figures are typed from the filings."""
import sys
sys.stdout.reconfigure(encoding="utf-8")

Y = [2021, 2022, 2023, 2024, 2025]
# Net cash generated from operating activities (interest paid and income tax paid are inside it; note 35 policy).
# 2021-2023: FY2023 20-F (0001292814-24-001825); 2024-2025: FY2025 20-F (0001292814-26-002681).
OCF = {2021: 3913.753, 2022: 3967.599, 2023: 4854.352, 2024: 7404.568, 2025: 8361.115}
# Cash capital spending: acquisition of contract assets, intangible assets and PP&E (incl. PP&E line where separate).
CAPEX = {2021: 3696.669 + 50.281, 2022: 3550.537 + 73.668, 2023: 4138.574, 2024: 8030.674, 2025: 13740.392}
# Payments in financing: Public-Private Partnership (PPP) and program contract commitments (deferred asset payments).
PPP = {2021: 579.486 + 121.521, 2022: 590.201 + 16.255, 2023: 673.645 + 81.357, 2024: 569.725 + 35.497, 2025: 480.492}
# Depreciation and amortization (cash flow statement add-back): the maintenance guess.
DA = {2021: 2253.0, 2022: 2451.0, 2023: 2790.856, 2024: 2676.642, 2025: 2208.762}
INT = {2021: 845.445, 2022: 1505.488, 2023: 1936.419, 2024: 1976.694, 2025: 2696.320}
# Sanitation revenue net of sales taxes, excluding construction revenue and the financial-asset restatement.
SALES = {2021: 19491 - 4377, 2022: 22056 - 4864, 2023: 21513.442 - 1457.125 - 84.593, 2024: 21725.8, 2025: 22213.0}

TAX = 0.34          # statutory IRPJ + CSLL
SOV = 0.1493        # NTN-F 2037, Tesouro Direto, 2026-10-27
FLOOR = 0.10
SHARES = 3517.275575  # million, outstanding after the EMAE merger, less treasury

# Net debt, consolidated, 2026-06-30 interim (0001292814-26-004252)
BORR = 5289.831 + 46367.971
PPP_L = 477.241 + 2844.977
DERIV = 2293.799           # derivative liabilities (swaps on the foreign-currency debt)
CASH = 4243.477 + 13197.409
NET_DEBT = BORR + PPP_L + DERIV - CASH
EQUITY_BOOK = 45310.286
# Long-term debt for the utility credit: borrowings + PPP liabilities (finance-lease-like), end-2020 and end-2025
LTD_2020 = (3034.449 + 14224.175) + (130.207 + 3045.066)
LTD_2025 = (5092.816 + 35049.531) + (469.687 + 2856.008)
LTD_INC = (LTD_2025 - LTD_2020) / 5
LTD_SHARE = (BORR + PPP_L) / (BORR + PPP_L + EQUITY_BOOK)

def avg(d): return sum(d[y] for y in Y) / len(Y)

print("year  OCF    capex   PPP   D&A   int   sales | OC_all  OC_maint  growth_spend  OC_maint/sales")
OC_all, OC_m, GS = {}, {}, {}
for y in Y:
    OC_all[y] = OCF[y] - CAPEX[y] - PPP[y]
    OC_m[y] = OCF[y] - DA[y] - PPP[y]
    GS[y] = CAPEX[y] - DA[y]
    print(f"{y} {OCF[y]:7.0f} {CAPEX[y]:7.0f} {PPP[y]:5.0f} {DA[y]:5.0f} {INT[y]:5.0f} {SALES[y]:6.0f} | {OC_all[y]:7.0f} {OC_m[y]:8.0f} {GS[y]:9.0f}   {OC_m[y]/SALES[y]*100:5.1f}%")
b_all, b_m, gs, intr = avg(OC_all), avg(OC_m), avg(GS), avg(INT)
print(f"5y avg: OC_all {b_all:.0f}  OC_maint {b_m:.0f}  growth spending {gs:.0f}  interest paid {intr:.0f}")
g_shown = (OC_m[2025] / OC_m[2021]) ** 0.25 - 1
g_sales = (SALES[2025] / SALES[2021]) ** 0.25 - 1
yr10 = b_m * (1 + g_shown) ** 10
print(f"shown growth of OC_maint 2021-2025: {g_shown*100:.1f}%/yr; carried ten years gives {yr10:,.0f}, "
      f"{yr10/(SALES[2025]*(1+g_sales)**10)*100:.0f}% of sales grown at the sales rate (highest seen {max(OC_m[y]/SALES[y] for y in Y)*100:.1f}%)")
print(f"sales growth 2021-2025: {g_sales*100:.1f}%/yr  -> specific (f): growth carried = sales growth")
g = g_sales
credit_cap = gs * LTD_SHARE
credit = min(LTD_INC, credit_cap)
print(f"LTD increase over window {LTD_2025-LTD_2020:,.0f}, per year {LTD_INC:,.0f}; own LTD share of LT capital 2026-06-30 {LTD_SHARE*100:.1f}%; "
      f"cap {credit_cap:,.0f}; credit {credit:,.0f}")
print(f"net debt 2026-06-30: borrowings {BORR:,.0f} + PPP {PPP_L:,.0f} + derivatives {DERIV:,.0f} - cash&investments {CASH:,.0f} = {NET_DEBT:,.0f}")

def value(base, r, growth=0.0, spend=0.0, cred=0.0):
    """Ten years at growth (spending net of credit grows with it, stops at year ten), then flat at year-ten cash."""
    pv = 0.0
    for t in range(1, 11):
        c = base * (1 + growth) ** t - (spend - cred) * (1 + growth) ** (t - 1)
        pv += c / (1 + r) ** t
    term = base * (1 + growth) ** 10 / r
    return pv + term / (1 + r) ** 10

def report(label, base, spend, cred, debt_adj=0.0):
    out = {}
    for rn, r in (("sovereign", SOV), ("floor 10%", FLOOR)):
        ng = value(base, r)
        gr = value(base, r, g, spend, cred)
        out[rn] = ((ng - debt_adj) / SHARES, (gr - debt_adj) / SHARES)
    return out

print("\n== Equity-only basis (CENTRAL for a regulated utility): maintenance-only owner cash after interest ==")
eq = report("eq", b_m, gs, credit)
for k, (ng, gr) in eq.items():
    print(f"  {k:10s} no-growth R${ng:6.2f}  growth (g={g*100:.1f}%, growth spending {gs:,.0f} less credit {credit:,.0f}) R${gr:6.2f}")
lo, hi = sorted(eq["sovereign"])
fair_eq = sum(eq["floor 10%"]) / 2
print(f"  RANGE at sovereign R${lo:.2f} to R${hi:.2f}; FAIR PRICE (each end at 10%, averaged) R${fair_eq:.2f}")
print(f"  growth spending charged: year one {gs:,.0f}, year ten {gs*(1+g)**9:,.0f}; credit year one {credit:,.0f}, year ten {credit*(1+g)**9:,.0f}")

print("\n== Equity-only, growth case with NO debt credit (beside) ==")
nc = report("nc", b_m, gs, 0.0)
for k, (ng, gr) in nc.items(): print(f"  {k:10s} no-growth R${ng:6.2f}  growth R${gr:6.2f}")

print("\n== Equity-only, all spending charged (beside) ==")
print(f"  5y avg owner cash after all capital spending {b_all:,.0f}: negative; value not positive at any rate")

print("\n== All-equity basis (beside): maintenance owner cash before interest after tax, less net debt ==")
b_ae = b_m + intr * (1 - TAX)
ae = report("ae", b_ae, gs, 0.0, NET_DEBT)
for k, (ng, gr) in ae.items(): print(f"  {k:10s} no-growth R${ng:6.2f}  growth R${gr:6.2f}")
print(f"  base {b_ae:,.0f}; FAIR (10%) R${sum(ae['floor 10%'])/2:.2f}")

print("\n== Sensitivity, not a case of the convention: 2025 alone as the base (post-privatization tariff year) ==")
s25 = report("s25", OC_m[2025], gs, credit)
for k, (ng, gr) in s25.items(): print(f"  {k:10s} no-growth R${ng:6.2f}  growth R${gr:6.2f}")

print("\n== Floor test at the price ==")
P = 25.53
mcap = P * SHARES
print(f"  price R${P} x {SHARES:,.1f}m = R${mcap:,.0f}m")
for nm, base in (("no-growth, window base", b_m), ("2025 alone", OC_m[2025])):
    print(f"  {nm}: owner cash yield on market value {base/mcap*100:.1f}%")
# expected return of the growth case at the price: solve r where value = price
def irr(base, spend, cred):
    lo_, hi_ = 0.0001, 0.5
    for _ in range(100):
        mid = (lo_ + hi_) / 2
        if value(base, mid, g, spend, cred) / SHARES > P: lo_ = mid
        else: hi_ = mid
    return mid
print(f"  growth case (central, with credit): expected return at the price {irr(b_m, gs, credit)*100:.1f}%")
print(f"  growth case, 2025 base: expected return at the price {irr(OC_m[2025], gs, credit)*100:.1f}%")

print("\n== More bases beside (sensitivity, not cases of the convention) ==")
ttm_ocf = 8361.115 - 4281.094 + 4127.702      # FY2025 less H1 2025 plus H1 2026 (interim, consolidated)
ttm_da = 2208.762 - 1127 + 1436                # D&A from the 2Q26 release, half-years
ttm = ttm_ocf - ttm_da - 480.492               # PPP payments taken at the FY2025 level (H1 2026 not read)
for nm, base in (("2024-2025 average", (OC_m[2024] + OC_m[2025]) / 2), ("trailing twelve months to 2026-06-30", ttm)):
    r = report(nm, base, gs, credit)
    print(f"  {nm}: base {base:,.0f}; sovereign R${r['sovereign'][0]:.2f} to R${r['sovereign'][1]:.2f}; "
          f"at 10% R${r['floor 10%'][0]:.2f} / R${r['floor 10%'][1]:.2f}; fair R${sum(r['floor 10%'])/2:.2f}; "
          f"growth-case return at price {irr(base, gs, credit)*100:.1f}%")
