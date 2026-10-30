"""NRG run 2026-10-26: owner cash and the Q7 COMPUTATION (arithmetic only; every input from the filings named in the run file).
USD millions unless stated. Run: python -I calc.py"""
YEARS = [2021, 2022, 2023, 2024, 2025]
# FY2023 10-K (0001013871-24-000005) cash flow for 2021-2023; FY2025 10-K (0001013871-26-000004) for 2023-2025
OCF      = [493, 360, -221, 2306, 1913]
ACQDERIV = [938, 1995, 342, -3, 59]        # net receipts from settlement of acquired derivatives (financing section)
SBC      = [21, 28, 101, 102, 134]          # amortization of unearned equity compensation
CAPEX    = [269, 367, 598, 472, 1147]
INSUR    = [0, 0, 240, 3, 100]              # insurance proceeds for PP&E (investing)
ALLOW    = [0, 6, 24, 18, 1]                # net purchases of emissions allowances
INTPAID  = [433, 383, 548, 626, 572]        # interest paid, net of capitalized (cash flow notes)
TAXPAID  = [32, 66, 48, 182, 67]            # income taxes paid, net of refunds
ACQ      = [3559, 62, 2523, 38, 596]        # payments for acquisitions of businesses and assets, net of cash acquired
SALES    = [830, 109, 2007, 501, 6]         # proceeds from sale of assets, net of cash disposed
MAINT    = [177, 236, 519, 264, 367]        # maintenance + environmental cash capex (MD&A tables); growth = the rest
REV      = [26989, 31543, 28823, 28130, 30713]
TAX = 0.25        # CONVENTION: 21% federal + 4.1% state (FY2025 rate reconciliation), rounded
R = 0.0533        # 30-year par yield, US Treasury, 2026-10-23 (tools/run.py sovereign line)
FLOOR = 0.10
SHARES = 210.210483  # millions, cover of 10-Q filed 2026-08-04 (as of 2026-07-31)
PRICE = 92.31
DEBT = 1512 + 21744   # 10-Q 2026-06-30: current + long-term debt and finance leases
CASH = 162
NETDEBT = DEBT - CASH
PREF = 650            # Series A preferred, liquidation preference

def avg(x): return sum(x) / len(x)
rows = []
for i, y in enumerate(YEARS):
    netcap = CAPEX[i] - INSUR[i] + ALLOW[i]
    growth = CAPEX[i] - MAINT[i]
    U = OCF[i] + ACQDERIV[i] - SBC[i] - netcap + INTPAID[i] + TAXPAID[i]           # pre-tax, before interest, after all spending
    Um = U + growth                                                                    # maintenance-only
    rows.append((y, U, U * (1 - TAX), Um * (1 - TAX), growth, ACQ[i] - SALES[i], U * (1 - TAX) / REV[i]))
print("year  U_pretax  U_after  Umaint_after  growthcapex  netacq  U_after/rev")
for r in rows: print(f"{r[0]}  {r[1]:8,.0f}  {r[2]:7,.0f}  {r[3]:11,.0f}  {r[4]:10,.0f}  {r[5]:6,.0f}  {r[6]:.1%}")
U_all = avg([r[2] for r in rows]); U_m = avg([r[3] for r in rows]); G = avg([r[4] for r in rows]) * (1 - TAX)
NA = avg([r[5] for r in rows])
print(f"\n5-yr avg owner cash after all spending (after 25% tax): {U_all:,.0f}; maintenance-only: {U_m:,.0f}; growth spending after tax: {G:,.0f}; net acquisitions: {NA:,.0f}")
print(f"serial-acquirer test: net purchases {NA:,.0f} vs half of owner cash before purchases {U_all/2:,.0f} -> {'SERIAL' if NA > U_all/2 else 'not serial'}")
first = avg([rows[0][2], rows[1][2]]); second = avg([rows[3][2], rows[4][2]])
print(f"halves: 2021-22 avg {first:,.0f}; 2024-25 avg {second:,.0f}; rate over 3 yrs {(second/first)**(1/3)-1:.2%}/yr")
noacqderiv = avg([(rows[i][1] - ACQDERIV[i]) * (1 - TAX) for i in range(5)])
print(f"beside: owner cash without acquired-derivative receipts {noacqderiv:,.0f}")
tt = avg([rows[0][2], rows[1][2], rows[2][2]]); print(f"beside: trough-to-trough 2021-2023 avg {tt:,.0f}")

# LS Power portfolio (closed 2026-01-30), own filed record FY2025 (8-K 2026-03-02, 0001104659-26-022295, ex99-1/4/5), USD thousands -> M
lsp_pre = (640.173 + 236.067) + (122.541 + 28.078) + 87.809 - (71.836 - 27.010) - 10.134 - 3.400
LSP = lsp_pre * (1 - TAX)
print(f"\nLSP FY2025 unlevered pre-tax owner cash {lsp_pre:,.0f}; after 25% tax {LSP:,.0f}")

def annuity(r, n): return (1 - (1 + r) ** -n) / r
# NOL shelter (CONVENTION): tax-effected NOLs net of valuation allowance + credits, FY2025 10-K
shelter = 1395 + 326 + 107 - 150 + 288
use = 350  # per year; CONVENTION: normalized tax at 25% minus the up-to-$90M the filer expects to pay in 2026, rounded
n = shelter / use
def shelter_pv(r): return use * annuity(r, int(n)) + (shelter - use * int(n)) * (1 + r) ** -(int(n) + 1)
print(f"shelter {shelter:,.0f} over {n:.1f} yrs: PV at {R:.2%} {shelter_pv(R):,.0f}; at 10% {shelter_pv(FLOOR):,.0f}")

def case_value(r, c_top_maint, growth_after, lsp):
    top = c_top_maint / r                                  # maintenance-only, no growth, forever
    bottom = c_top_maint / r - growth_after * annuity(r, 10)   # growth spending charged 10 yrs, growth shown = 0
    return top + lsp / r + shelter_pv(r), bottom + lsp / r + shelter_pv(r)
def per_share(ev): return (ev - NETDEBT - PREF) / SHARES
for label, r in (("long rate", R), ("at 10%", FLOOR)):
    t, b = case_value(r, U_m, G, LSP)
    print(f"{label}: EV top {t:,.0f} bottom {b:,.0f}; per share top {per_share(t):.2f} bottom {per_share(b):.2f}")
t10, b10 = case_value(FLOOR, U_m, G, LSP)
print(f"FAIR PRICE all-equity (avg of ends at 10%): {(per_share(t10)+per_share(b10))/2:.2f}")
# default pair beside: acquisitions deducted, total growth ~0
print(f"default pair beside (acquisitions deducted, no growth, at long rate): {per_share((U_all-NA)/R + LSP/R + shelter_pv(R)):.2f}")
# equity-only beside: owner cash after interest at today's debt; interest = FY2026 run-rate from 10-Q H1 interest expense x2
INT26 = 595 * 2
eq_top = (U_m + LSP - INT26 * (1 - TAX)); eq_bot_g = G
def eq_ps(r):
    top = eq_top / r + shelter_pv(r) - PREF
    bot = top - eq_bot_g * annuity(r, 10)
    return top / SHARES, bot / SHARES
for label, r in (("long rate", R), ("at 10%", FLOOR)):
    a, b = eq_ps(r); print(f"equity-only {label}: top {a:.2f} bottom {b:.2f}; avg {(a+b)/2:.2f}")
mc = SHARES * PRICE; ev = mc + NETDEBT + PREF
print(f"\nmarket cap {mc:,.0f}; net debt {NETDEBT:,.0f}; pref {PREF}; EV {ev:,.0f}")
for c in (U_m + LSP, U_all + LSP):
    print(f"owner cash {c:,.0f} -> yield on EV at price {c/ev:.2%}; with shelter PV removed from EV {c/(ev-shelter_pv(R)):.2%}")
print(f"growth needed for 10% at the price, top case: {FLOOR - (U_m+LSP)/(ev-shelter_pv(FLOOR)):.2%} a year forever")

# Specific (b): growth shown between the halves is negative; carried as the bottom (decline 10 yrs, then flat), growth spending charged 10 yrs
g = (second / first) ** (1 / 3) - 1
def decline_value(r, c, gs):
    pv = sum(c * (1 + g) ** t / (1 + r) ** t for t in range(1, 11))
    pv += c * (1 + g) ** 10 / r / (1 + r) ** 10
    return pv - gs * annuity(r, 10)
for label, r in (("long rate", R), ("at 10%", FLOOR)):
    top = U_m / r + LSP / r + shelter_pv(r)
    bot = decline_value(r, U_m, G) + LSP / r + shelter_pv(r)
    print(f"[b] {label}: top {per_share(top):.2f}  bottom (decline {g:.2%}) {per_share(bot):.2f}  width ratio {per_share(top)/per_share(bot) if per_share(bot)>0 else float('nan'):.2f}")
    if r == FLOOR: print(f"[b] FAIR PRICE all-equity: {(per_share(top)+per_share(bot))/2:.2f}")
# equity-only with the decline bottom
for label, r in (("long rate", R), ("at 10%", FLOOR)):
    top = (eq_top / r + shelter_pv(r) - PREF) / SHARES
    bot = (decline_value(r, U_m, G) + (LSP - INT26 * (1 - TAX)) / r + shelter_pv(r) - PREF) / SHARES
    print(f"[b] equity-only {label}: top {top:.2f} bottom {bot:.2f} avg {(top+bot)/2:.2f}")
# literal window beside (no cycle base): same five years; 2021 is the filer's Uri year
print(f"literal-window end-year rate 2021->2025: {(rows[4][2]/rows[0][2])**0.25-1:.2%}/yr")
