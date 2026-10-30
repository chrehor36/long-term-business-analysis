"""PAM 2026-10-26: COMPUTATION, NOT A CLEARANCE. Owner cash, the Q7 range and the fair price.
All inputs in US$ millions from the filed statements (accessions in the run file). Run: python -I q7_compute.py"""

YEARS = [2021, 2022, 2023, 2024, 2025]
# Continuing operations. 2021 OCF 729 less discontinued (Edenor) 116.
OCF = {2021: 613, 2022: 619, 2023: 575, 2024: 435, 2025: 778}
CAPEX = {2021: 206 + 4, 2022: 416 + 31, 2023: 758, 2024: 447, 2025: 993}          # PP&E + intangibles paid
ASSET_SALES = {2021: 6, 2022: 21, 2023: 20 + 1, 2024: 0, 2025: 9}                 # intangible and PP&E sale collections
# Net acquisitions (paid less collected): companies, capital integrations, areas; 2024 nets the cash acquired with OCP.
NET_ACQ = {2021: 17 - 51, 2022: 111 - 44, 2023: 1 - 72, 2024: 48 - 39 - 71 - 9, 2025: 1 + 44 - 1 - 7}
# Equity-method convention: cash dividends received from investees (2024 adds the JV share repurchase 37;
# 2025 adds dividends from CIESA collected in financial assets, 45, R116 of the FY2025 20-F).
DIVS = {2021: 18, 2022: 10, 2023: 0, 2024: 9 + 37, 2025: 25 + 45}
DA = {2021: 205, 2022: 212, 2023: 267, 2024: 342, 2025: 414}
INT_PAID = {2021: 140, 2022: 162, 2023: 280, 2024: 145, 2025: 161}
SALES = {2021: 1508, 2022: 1829, 2023: 1732, 2024: 1876, 2025: 1998}
# Change in income-tax liabilities (provision + current + 2025 payment plan): 142,208,184,72,332,335
DTAX = {2021: 66, 2022: -24, 2023: -112, 2024: 260, 2025: 3}

R = 0.0533          # US Treasury 30-year par yield, 2026-10-23
FLOOR = 0.10
ADS_RATIO = 25
SHARES = 1343.6 - 3.5   # millions of common shares outstanding (capital 2026-08-03 less comp-plan treasury 3.5M)
ADS = SHARES / ADS_RATIO
PRICE_ADS = 79.50
MKT = ADS * PRICE_ADS
# Net debt 2026-06-30: borrowings 2,575 + 25; less cash 979 and current FVTPL securities 302.
NET_DEBT = 2575 + 25 - 979 - 302


def pv(flows, r, terminal_flow, n=10):
    v = sum(f / (1 + r) ** (t + 1) for t, f in enumerate(flows))
    v += (terminal_flow / r) / (1 + r) ** n
    return v


def cagr(a, b, n):
    return (b / a) ** (1 / n) - 1 if a > 0 and b > 0 else None


def avg(d):
    return sum(d.values()) / len(d)


def show(title, d):
    print(f"{title:44s}" + "".join(f"{d[y]:>8.0f}" for y in YEARS) + f"   avg {avg(d):7.1f}")


all_sp = {y: OCF[y] - CAPEX[y] + ASSET_SALES[y] - NET_ACQ[y] + DIVS[y] for y in YEARS}
all_sp_org = {y: OCF[y] - CAPEX[y] + ASSET_SALES[y] + DIVS[y] for y in YEARS}
maint = {y: OCF[y] - DA[y] + ASSET_SALES[y] - NET_ACQ[y] + DIVS[y] for y in YEARS}
maint_org = {y: OCF[y] - DA[y] + ASSET_SALES[y] + DIVS[y] for y in YEARS}
growth_sp = {y: CAPEX[y] - DA[y] for y in YEARS}

print("COMPUTATION, NOT A CLEARANCE (US$ millions)")
print("year" + " " * 40 + "".join(f"{y:>8d}" for y in YEARS))
show("OCF continuing (before interest paid)", OCF)
show("capital spending (PP&E + intangibles)", CAPEX)
show("D&A (maintenance guess)", DA)
show("net acquisitions", NET_ACQ)
show("dividends from investees", DIVS)
show("owner cash, all spending, acq deducted", all_sp)
show("owner cash, all spending, organic", all_sp_org)
show("owner cash, maintenance only, acq deducted", maint)
show("owner cash, maintenance only, organic", maint_org)
show("growth spending (capex - D&A)", growth_sp)
show("interest paid", INT_PAID)
show("change in income-tax liabilities", DTAX)
print(f"sales CAGR 2021-2025 {cagr(SALES[2021], SALES[2025], 4):.2%}")
g = cagr(maint[2021], maint[2025], 4)
print(f"maintenance owner cash growth 2021-2025 {g:.2%} (end years {maint[2021]} -> {maint[2025]})")
h1 = sum(maint[y] for y in (2021, 2022)) / 2
h2 = sum(maint[y] for y in (2024, 2025)) / 2
print(f"halves check: 2021-22 avg {h1:.0f}, 2024-25 avg {h2:.0f}")
print(f"market cap {MKT:,.0f} on {ADS:.2f}M ADS at ${PRICE_ADS}; net debt {NET_DEBT}; EV {MKT + NET_DEBT:,.0f}")


def cases(base, gsp, g, r):
    """top = no growth on maintenance owner cash; bottom = shown growth g for ten years with growth
    spending charged (growing at g) and stopping at year ten; then zero nominal growth."""
    top = base / r
    flows = [base * (1 + g) ** t - gsp * (1 + g) ** t for t in range(1, 11)]
    term = base * (1 + g) ** 10
    bottom = pv(flows, r, term)
    return top, bottom


base = avg(maint)
gsp = avg(growth_sp)
for label, r in (("at the sovereign 5.33%", R), ("at the floor 10% (fair price)", FLOOR)):
    top, bot = cases(base, gsp, g, r)
    lo, hi = min(top, bot), max(top, bot)
    print(f"\nALL-EQUITY range {label}: EV {lo:,.0f} to {hi:,.0f}; equity {lo - NET_DEBT:,.0f} to {hi - NET_DEBT:,.0f}")
    print(f"   per ADS ${(lo - NET_DEBT) / ADS:,.2f} to ${(hi - NET_DEBT) / ADS:,.2f}; per share ${(lo - NET_DEBT) / SHARES:,.3f} to ${(hi - NET_DEBT) / SHARES:,.3f}")
    if r == FLOOR:
        fair = ((top - NET_DEBT) + (bot - NET_DEBT)) / 2
        print(f"   FAIR PRICE all-equity: ${fair / ADS:,.2f} per ADS (${fair / SHARES:,.3f} per share)")
    if r == R:
        print(f"   width top/bottom (EV): {hi / lo:.2f}x")

# yield tests at the price: does any case earn the floor?
ev = MKT + NET_DEBT
print(f"\nfloor test, all-equity: maintenance no-growth owner cash {base:.0f} / EV {ev:,.0f} = {base / ev:.2%} (zero growth)")
print(f"floor test, all-spending literal: {avg(all_sp):.0f} / EV = {avg(all_sp) / ev:.2%}")
# equity-only
eq_base = base - avg(INT_PAID)
print(f"\nEQUITY-ONLY: maintenance owner cash after interest {eq_base:.0f}; yield on market cap {eq_base / MKT:.2%}")
for label, r in (("sovereign", R), ("10%", FLOOR)):
    top = eq_base / r
    flows = [(base * (1 + g) ** t - gsp * (1 + g) ** t) - avg(INT_PAID) for t in range(1, 11)]
    bot = pv(flows, r, base * (1 + g) ** 10 - avg(INT_PAID))
    lo, hi = min(top, bot), max(top, bot)
    print(f"   equity-only {label}: equity {lo:,.0f} to {hi:,.0f}; per ADS ${lo / ADS:,.2f} to ${hi / ADS:,.2f}")
    if r == FLOOR:
        print(f"   FAIR PRICE equity-only: ${(top + bot) / 2 / ADS:,.2f} per ADS (${(top + bot) / 2 / SHARES:,.3f} per share)")

# literal all-spending window beside
lit = avg(all_sp)
print(f"\nLITERAL all-spending window, no growth: EV {lit / R:,.0f}; equity {lit / R - NET_DEBT:,.0f}; per ADS ${(lit / R - NET_DEBT) / ADS:,.2f}")
# tax-accrual variant: charge the increase in unpaid income-tax liabilities
tv = base - avg(DTAX)
print(f"tax-accrual variant: maintenance owner cash {tv:.0f}; no-growth EV {tv / R:,.0f}; per ADS ${(tv / R - NET_DEBT) / ADS:,.2f}")
