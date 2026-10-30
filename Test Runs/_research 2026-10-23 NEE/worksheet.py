# NEE run 2026-10-23: arithmetic only. Every input is a filed figure ($ millions) with its source noted.
# Sources: NEE/FPL combined 10-K FY2025 (0000753308-26-000015, covers 2023-2025) and FY2023 (0000753308-24-000008,
# covers 2021-2023); FY2024 10-K (0000753308-25-000011) for the 2022 differential-membership payments; 10-Q Q3 2026
# (0000753308-26-000081) for the latest balance sheet; reserve amortization from the MD&A of the FY2021-FY2025 10-Ks.
Y = [2021, 2022, 2023, 2024, 2025]
R = 0.0529          # US Treasury 30-year par yield, 2026-10-22 (tools/sources.py)
FLOOR = 0.10        # Q7 floor CONVENTION (about ten percent)
T = 0.21            # federal statutory rate, used only to put interest after tax for the all-equity basis
PRICE = 81.90       # close 2026-10-22, aggregator (Yahoo via tools/sources.py), flagged
SHARES = 2097.306049  # millions, 10-Q cover, outstanding at 2026-09-30

# --- NEE consolidated cash flow
nee_ocf   = [7553, 8262, 11301, 13260, 12485]
nee_da    = [3924, 4503, 5879, 5462, 6580]
nee_int   = [1323, 1375, 2463, 2737, 3501]        # cash paid for interest, net of capitalized
fpl_capex_c = [7408, 9067, 9302, 7992, 8719]      # "Capital expenditures of FPL" on NEE statement
neer_inv  = [8247, 9541, 15565, 16215, 15332]     # "Independent power and other investments of NEER"
nuc_fuel  = [275, 223, 185, 399, 553]
oth_capex = [147, 452, 61, 123, 2]
neer_sales = [2761, 1564, 1883, 2659, 1115]       # "Sale of independent power and other investments of NEER"
fcg_sale  = [0, 0, 924, 0, 0]                     # Florida City Gas business sold (FPL)
dm_in     = [2779, 4158, 2745, 2257, 3276]        # proceeds from differential membership investors
dm_out    = [None, 179, 75, 740, 516]             # payments to them (2021 not separately stated; inside "Other - net")
dividends = [3024, 3352, 3782, 4235, 4680]
equity_issued = [14, 1460, 4514, 48, 2038]
ni_attr   = [3573, 4147, 7310, 6946, 6835]
ni_total  = [2827, 3246, 6282, 5698, 5332]
nci_alloc = [746, 901, 1028, 1248, 1503]          # net loss attributable to noncontrolling interests
sbc = [119, 142, 139, 138, 185]                   # share-based compensation expense (XBRL AllocatedShareBasedCompensationExpense), deducted: added back inside OCF

# --- FPL stand-alone (FPL statements in the same combined 10-K)
fpl_ocf   = [5358, 4894, 8296, 8506, 8533]
fpl_capex = [7411, 9067, 9302, 7992, 8719]
fpl_nuc   = [159, 118, 98, 222, 216]
fpl_da    = [2266, 2695, 3789, 2827, 3778]
fpl_resam = [429, 114, 227, 328, 593]             # reserve amortization credited inside D&A (MD&A)
fpl_ltd_iss = [2588, 2942, 5678, 3205, 3785]
fpl_ltd_ret = [1304, 441, 1548, 1721, 1821]
fpl_int   = [586, 707, 1034, 1143, 1225]
fpl_ni    = [3206, 3701, 4552, 4543, 5012]
fpl_eq    = {2020: 29228, 2021: 33594, 2022: 38920, 2023: 38835, 2024: 43076, 2025: 46986}
fpl_contrib = [1700, 3625, 0, 3400, 0]
fpl_div_to_nee = [540, 2000, 4545, 3700, 1100]
ALLOWED_DEBT_SHARE = 1 - 0.596                     # 2025 rate agreement: 59.6% equity ratio

# --- segment net income attributable to NEE
neer_ni = [599, 285, 3558, 2299, 2975]
corp_ni = [-232, 161, -800, 104, -1152]

def avg(a): return sum(a) / len(a)
def cagr(a, b, n): return (b / a) ** (1 / n) - 1 if a > 0 and b > 0 else None
def pv_flat(c, r): return c / r
def pv_growth(c0, g, r, grow_spend=0.0):
    """c0 grows at g for years 1..10, flat after; grow_spend charged in years 1..10 only"""
    v = 0.0
    c = c0
    for t in range(1, 11):
        c = c * (1 + g)
        v += (c - grow_spend) / (1 + r) ** t
    v += (c / r) / (1 + r) ** 10
    return v

out = []
p = out.append
p("== PARTS: five-year net income attributable to NEE (CODM measure, Note 16)")
f5, n5, c5 = sum(fpl_ni), sum(neer_ni), sum(corp_ni)
p(f"FPL {f5}  NEER {n5}  Corp&Other {c5}  total {f5+n5+c5}  FPL share of total {f5/(f5+n5+c5):.1%}, of segments {f5/(f5+n5):.1%}")
p(f"NEER five-year NI attributable {n5}, of which HLBV loss allocated to noncontrolling interests {sum(nci_alloc)} ({sum(nci_alloc)/n5:.0%})")
p(f"NEER net income before that allocation: {[a-b for a,b in zip(neer_ni,nci_alloc)]}")

p("\n== Q3: FPL return on average book equity")
for i, y in enumerate(Y):
    e = (fpl_eq[y-1] + fpl_eq[y]) / 2
    p(f"{y}: NI {fpl_ni[i]} / avg equity {e:.0f} = {fpl_ni[i]/e:.1%}")
p(f"five-year: {sum(fpl_ni)/sum((fpl_eq[y-1]+fpl_eq[y])/2 for y in Y):.1%}")
p(f"FPL capex+nuclear fuel {sum(fpl_capex)+sum(fpl_nuc)} vs D&A {sum(fpl_da)} (+reserve amort {sum(fpl_resam)}) over 2021-25; "
  f"ratio {(sum(fpl_capex)+sum(fpl_nuc))/(sum(fpl_da)+sum(fpl_resam)):.2f}x")
p(f"FPL net cash to NEE (dividends less contributions) 2021-25: {sum(fpl_div_to_nee)-sum(fpl_contrib)}")

# NEER + Corporate = NEE less FPL
rest_ocf = [a - b for a, b in zip(nee_ocf, fpl_ocf)]
rest_da = [a - b for a, b in zip(nee_da, fpl_da)]
rest_int = [a - b for a, b in zip(nee_int, fpl_int)]
rest_nuc = [a - b for a, b in zip(nuc_fuel, fpl_nuc)]
rest_spend = [a + b + c for a, b, c in zip(neer_inv, rest_nuc, oth_capex)]
p("\n== NEER + Corporate (NEE less FPL)")
p(f"OCF {rest_ocf} avg {avg(rest_ocf):.0f}; D&A {rest_da} avg {avg(rest_da):.0f}; interest paid {rest_int} avg {avg(rest_int):.0f}")
p(f"spending (NEER investments + nuclear fuel + other) {rest_spend} avg {avg(rest_spend):.0f}; asset sales avg {avg(neer_sales):.0f}")
# cash return on growth: change in OCF before after-tax interest vs growth spending
pre = [o + i * (1 - T) for o, i in zip(rest_ocf, rest_int)]
growth_spend = sum(rest_spend) - sum(neer_sales) - sum(rest_da) - sum(rest_nuc)
p(f"OCF + after-tax interest: {[round(x) for x in pre]}; change 2021->2025 {pre[-1]-pre[0]:.0f}; "
  f"less change in D&A {rest_da[-1]-rest_da[0]} = {pre[-1]-pre[0]-(rest_da[-1]-rest_da[0]):.0f} "
  f"on net growth spending {growth_spend:.0f} over 2021-25 = {(pre[-1]-pre[0]-(rest_da[-1]-rest_da[0]))/growth_spend:.1%}")

p("\n== Q4/Q7 owner cash, consolidated, by year")
for i, y in enumerate(Y):
    allsp = nee_ocf[i] - fpl_capex_c[i] - neer_inv[i] - nuc_fuel[i] - oth_capex[i]
    p(f"{y}: OCF {nee_ocf[i]} - all capital spending {fpl_capex_c[i]+neer_inv[i]+nuc_fuel[i]+oth_capex[i]} = {allsp}; "
      f"+ asset/business sales {neer_sales[i]+fcg_sale[i]} = {allsp+neer_sales[i]+fcg_sale[i]}; dividends paid {dividends[i]}; equity issued {equity_issued[i]}")

# ---------------- Q7 COMPUTATION ----------------
p("\n== Q7 COMPUTATION, NOT A CLEARANCE")
# FPL, equity-only (regulated-utility rule)
fpl_maint = [d + r_ + n for d, r_, n in zip(fpl_da, fpl_resam, fpl_nuc)]
fpl_oc_maint = [o - m for o, m in zip(fpl_ocf, fpl_maint)]
fpl_spend = [c + n for c, n in zip(fpl_capex, fpl_nuc)]
fpl_net_ltd = [a - b for a, b in zip(fpl_ltd_iss, fpl_ltd_ret)]
fpl_cap = [ALLOWED_DEBT_SHARE * s for s in fpl_spend]
fpl_credit = [min(n, c) for n, c in zip(fpl_net_ltd, fpl_cap)]
fpl_oc_all = [o - s + cr + fs for o, s, cr, fs in zip(fpl_ocf, fpl_spend, fpl_credit, fcg_sale)]
fpl_oc_all_nocredit = [o - s + fs for o, s, fs in zip(fpl_ocf, fpl_spend, fcg_sale)]
p(f"FPL maintenance guess (D&A + reserve amortization added back + nuclear fuel) {fpl_maint} avg {avg(fpl_maint):.0f}")
p(f"FPL owner cash after maintenance only {fpl_oc_maint} avg {avg(fpl_oc_maint):.0f}; growth 2021->25 {cagr(fpl_oc_maint[0], fpl_oc_maint[-1], 4)}")
p(f"FPL net LTD raised {fpl_net_ltd} (sum {sum(fpl_net_ltd)}), cap at {ALLOWED_DEBT_SHARE:.1%} of spending {[round(c) for c in fpl_cap]}, credit {fpl_credit}")
p(f"FPL owner cash, all spending, debt credited (+FCG sale) {fpl_oc_all} avg {avg(fpl_oc_all):.0f}; without credit {fpl_oc_all_nocredit} avg {avg(fpl_oc_all_nocredit):.0f}")
fpl_growth_spend = avg(fpl_spend) - avg(fpl_maint) - avg(fcg_sale) - avg(fpl_credit)
p(f"FPL growth spending net of the debt credit, avg {fpl_growth_spend:.0f}")

# NEER + Corp, all-equity (owner cash before interest, after tax), NCI distributions deducted
dm_out_f = [x if x is not None else 0 for x in dm_out]
rest_maint = [d + n for d, n in zip(rest_da, rest_nuc)]
rest_oc_maint = [o + i * (1 - T) - m - d - k for o, i, m, d, k in zip(rest_ocf, rest_int, rest_maint, dm_out_f, sbc)]
rest_oc_all = [o + i * (1 - T) - s + sl + di - d for o, i, s, sl, di, d in zip(rest_ocf, rest_int, rest_spend, neer_sales, dm_in, dm_out_f)]
rest_oc_all_nodm = [o + i * (1 - T) - s + sl - d for o, i, s, sl, d in zip(rest_ocf, rest_int, rest_spend, neer_sales, dm_out_f)]
p(f"NEER+Corp maintenance guess (D&A + nuclear fuel) {rest_maint} avg {avg(rest_maint):.0f}")
p(f"NEER+Corp all-equity owner cash after maintenance only {[round(x) for x in rest_oc_maint]} avg {avg(rest_oc_maint):.0f}; growth 2021->25 {cagr(rest_oc_maint[0], rest_oc_maint[-1], 4)}")
p(f"NEER+Corp all-equity owner cash, all spending, sales and tax-equity proceeds credited {[round(x) for x in rest_oc_all]} avg {avg(rest_oc_all):.0f}; "
  f"without tax-equity proceeds {[round(x) for x in rest_oc_all_nodm]} avg {avg(rest_oc_all_nodm):.0f}")
rest_growth_spend = avg(rest_spend) - avg(neer_sales) - avg(dm_in) - avg(rest_maint)
p(f"NEER+Corp growth spending net of sales and tax-equity proceeds, avg {rest_growth_spend:.0f}")

# Net debt, latest filed (10-Q 2026-09-30): CP 3,716; other ST 4,258; current LTD 8,833; LTD 97,125; cash 5,579
nee_debt = 3716 + 4258 + 8833 + 97125
nee_cash = 5579
nee_net_debt = nee_debt - nee_cash
# FPL debt at 2025-12-31 (latest FPL balance sheet read): CP 1,130; current LTD 641; LTD 28,041; cash 42
fpl_net_debt = 0 + 328 + 30192 - 819   # FPL 10-Q balance sheet 2026-09-30 (CP 0, current LTD 328, LTD 30,192, cash 819)
rest_net_debt = nee_net_debt - fpl_net_debt
mcap = PRICE * SHARES
p(f"\nmarket cap {mcap:,.0f}; NEE debt {nee_debt:,} cash {nee_cash:,} net {nee_net_debt:,} (2026-09-30); FPL net debt {fpl_net_debt:,} (2026-09-30); "
  f"NEER+Corp net debt by difference {rest_net_debt:,}; NCI (book, 2026-09-30) 10,719 (VIE) of total; EV {mcap+nee_net_debt:,.0f}")

def per_share(v): return v / SHARES

# Shown growth rates
_cl = [-599, -1465, 1104, 1016, -89]
fpl_oc_maint_x = [a - c for a, c in zip(fpl_oc_maint, _cl)]   # fuel-clause timing removed, for the growth rate only
g_fpl = cagr(fpl_oc_maint_x[0], fpl_oc_maint_x[-1], 4)
g_rest = cagr(rest_oc_maint[0], rest_oc_maint[-1], 4)
p(f"shown growth of maintenance-only owner cash: FPL {g_fpl:.1%}, NEER+Corp {g_rest:.1%}")

def case_values(r):
    # no-growth, maintenance-only
    fpl_ng = pv_flat(avg(fpl_oc_maint), r)
    rest_ng = pv_flat(avg(rest_oc_maint), r) - rest_net_debt
    # growth case: maintenance-only owner cash grows at the shown rate ten years; growth spending charged ten years
    fpl_g = pv_growth(avg(fpl_oc_maint), g_fpl, r, fpl_growth_spend)
    rest_g = pv_growth(avg(rest_oc_maint), g_rest, r, rest_growth_spend) - rest_net_debt
    return fpl_ng, rest_ng, fpl_g, rest_g

for label, r in (("at the long government rate 5.29%", R), ("at ten percent (fair-price convention)", FLOOR)):
    fpl_ng, rest_ng, fpl_g, rest_g = case_values(r)
    p(f"\n-- {label}")
    p(f"no-growth (maintenance only): FPL equity {fpl_ng:,.0f} + NEER/Corp equity {rest_ng:,.0f} = {fpl_ng+rest_ng:,.0f} -> ${per_share(fpl_ng+rest_ng):.2f}/sh")
    p(f"growth case (growth spending charged): FPL {fpl_g:,.0f} + NEER/Corp {rest_g:,.0f} = {fpl_g+rest_g:,.0f} -> ${per_share(fpl_g+rest_g):.2f}/sh")

# Beside 1: whole company equity-only (FPL credit only), maintenance-only, no growth
nee_maint = [a + b for a, b in zip(fpl_maint, rest_maint)]
nee_oc_eq_maint = [o - m - d - k for o, m, d, k in zip(nee_ocf, nee_maint, dm_out_f, sbc)]
p(f"\nBESIDE, whole-company equity-only owner cash after maintenance only {[round(x) for x in nee_oc_eq_maint]} avg {avg(nee_oc_eq_maint):.0f}; "
  f"no growth at 5.29%: {pv_flat(avg(nee_oc_eq_maint), R):,.0f} -> ${per_share(pv_flat(avg(nee_oc_eq_maint), R)):.2f}/sh; at 10%: ${per_share(pv_flat(avg(nee_oc_eq_maint), FLOOR)):.2f}/sh")
nee_oc_eq_all = [o - s + sl + fs + di - d + cr - k for o, s, sl, fs, di, d, cr, k in zip(nee_ocf, [a+b+c+e for a,b,c,e in zip(fpl_capex_c, neer_inv, nuc_fuel, oth_capex)], neer_sales, fcg_sale, dm_in, dm_out_f, fpl_credit, sbc)]
p(f"BESIDE, whole-company equity-only, all spending, sales, tax-equity proceeds and FPL debt credit {[round(x) for x in nee_oc_eq_all]} avg {avg(nee_oc_eq_all):.0f}")
# Beside 2: whole company all-equity
nee_oc_ae_maint = [o + i * (1 - T) - m - d - k for o, i, m, d, k in zip(nee_ocf, nee_int, nee_maint, dm_out_f, sbc)]
v = pv_flat(avg(nee_oc_ae_maint), R) - nee_net_debt
p(f"BESIDE, whole-company all-equity owner cash after maintenance only avg {avg(nee_oc_ae_maint):.0f}; no growth at 5.29% less net debt: {v:,.0f} -> ${per_share(v):.2f}/sh; "
  f"at 10%: ${per_share(pv_flat(avg(nee_oc_ae_maint), FLOOR) - nee_net_debt):.2f}/sh")

# Floor test: expected return at the price on the best case
# equity-only maintenance-only no growth: yield = owner cash / market cap
p(f"\nFLOOR TEST: equity-only maintenance-only owner cash avg {avg(nee_oc_eq_maint):.0f} / market cap {mcap:,.0f} = {avg(nee_oc_eq_maint)/mcap:.2%} (no growth)")
s_fpl = avg(fpl_oc_maint); s_rest = avg(rest_oc_maint)
p(f"sum-of-parts owner cash for the equity: FPL {s_fpl:.0f} + NEER/Corp {s_rest:.0f} less after-tax interest on NEER/Corp net debt is not netted here")
# solve for the rate at which the growth case equals the market cap
def growth_total(r):
    fpl_ng, rest_ng, fpl_g, rest_g = case_values(r)
    return fpl_g + rest_g, fpl_ng + rest_ng
lo, hi = 0.0001, 0.5
for _ in range(100):
    mid = (lo + hi) / 2
    if growth_total(mid)[0] > mcap: lo = mid
    else: hi = mid
p(f"rate at which the growth case equals the market cap: {mid:.2%}")
lo, hi = 0.0001, 0.5
for _ in range(100):
    mid2 = (lo + hi) / 2
    if growth_total(mid2)[1] > mcap: lo = mid2
    else: hi = mid2
p(f"rate at which the no-growth case equals the market cap: {mid2:.2%}")

# Fair price: each end valued at 10%, averaged, per share (central basis)
fpl_ng, rest_ng, fpl_g, rest_g = case_values(FLOOR)
fair_central = per_share(((fpl_ng + rest_ng) + (fpl_g + rest_g)) / 2)
p(f"\nFAIR PRICE (central basis as read): ${fair_central:.2f}")
# equity-only whole company beside: two ends at 10%
eo_ng = pv_flat(avg(nee_oc_eq_maint), FLOOR)
eo_g = pv_growth(avg(nee_oc_eq_maint), cagr(nee_oc_eq_maint[0], nee_oc_eq_maint[-1], 4),
                 FLOOR, fpl_growth_spend + rest_growth_spend + avg(rest_int) * 0)  # growth spending charged
p(f"whole-company equity-only, growth {cagr(nee_oc_eq_maint[0], nee_oc_eq_maint[-1], 4):.1%}: ends at 10% ${per_share(eo_ng):.2f} and ${per_share(eo_g):.2f}; fair ${per_share((eo_ng+eo_g)/2):.2f}")
ae_ng = pv_flat(avg(nee_oc_ae_maint), FLOOR) - nee_net_debt
ae_g = pv_growth(avg(nee_oc_ae_maint), cagr(nee_oc_ae_maint[0], nee_oc_ae_maint[-1], 4), FLOOR, fpl_growth_spend + avg(fpl_credit) + rest_growth_spend) - nee_net_debt
p(f"whole-company all-equity, growth {cagr(nee_oc_ae_maint[0], nee_oc_ae_maint[-1], 4):.1%}: ends at 10% ${per_share(ae_ng):.2f} and ${per_share(ae_g):.2f}; fair ${per_share((ae_ng+ae_g)/2):.2f}")

# ranges at 5.29% for the beside bases
eo_g_r = pv_growth(avg(nee_oc_eq_maint), cagr(nee_oc_eq_maint[0], nee_oc_eq_maint[-1], 4), R, fpl_growth_spend + rest_growth_spend)
p(f"whole-company equity-only range at 5.29%: ${per_share(pv_flat(avg(nee_oc_eq_maint), R)):.2f} (no growth) and ${per_share(eo_g_r):.2f} (growth)")
ae_g_r = pv_growth(avg(nee_oc_ae_maint), cagr(nee_oc_ae_maint[0], nee_oc_ae_maint[-1], 4), R, fpl_growth_spend + avg(fpl_credit) + rest_growth_spend) - nee_net_debt
p(f"whole-company all-equity range at 5.29%: ${per_share(pv_flat(avg(nee_oc_ae_maint), R) - nee_net_debt):.2f} (no growth) and ${per_share(ae_g_r):.2f} (growth)")

print("\n".join(out))


# ===== REVISED Q7 (as the run file reports it) =====
q = []
P = q.append
clause = [-599, -1465, 1104, 1016, -89]   # "Cost recovery clauses and franchise fees" in OCF (fuel clause timing), NEE = FPL lines
P("\n===== Q7 AS REPORTED IN THE RUN FILE =====")
P(f"cost-recovery-clause swing in OCF {clause}, five-year sum {sum(clause)} (nets out over the window)")
eq_maint = nee_oc_eq_maint
eq_maint_x = [a - c for a, c in zip(eq_maint, clause)]   # remove the clause timing for the GROWTH RATE only
g_eq_lit = cagr(eq_maint[0], eq_maint[-1], 4)
g_eq = cagr(eq_maint_x[0], eq_maint_x[-1], 4)
P(f"equity-only owner cash after maintenance only {[round(x) for x in eq_maint]} avg {avg(eq_maint):.0f}; literal growth {g_eq_lit:.1%}")
P(f"same, clause timing removed (growth rate only) {[round(x) for x in eq_maint_x]} growth {g_eq:.1%}")
gs_eq = fpl_growth_spend + rest_growth_spend
P(f"growth spending charged in the growth case (FPL net of debt credit {fpl_growth_spend:.0f} + NEER/Corp net of sales and tax-equity proceeds {rest_growth_spend:.0f}) = {gs_eq:.0f}")
for lab, r in (("5.29%", R), ("10%", FLOOR)):
    ng = pv_flat(avg(eq_maint), r); gg = pv_growth(avg(eq_maint), g_eq, r, gs_eq); gl = pv_growth(avg(eq_maint), g_eq_lit, r, gs_eq)
    P(f"CENTRAL equity-only @ {lab}: no growth ${per_share(ng):.2f}; growth ({g_eq:.1%}) ${per_share(gg):.2f}; literal-window growth ({g_eq_lit:.1%}) ${per_share(gl):.2f}")
ng10 = pv_flat(avg(eq_maint), FLOOR); gg10 = pv_growth(avg(eq_maint), g_eq, FLOOR, gs_eq)
P(f"FAIR PRICE, central equity-only: ${per_share((ng10+gg10)/2):.2f}")
def solve(f):
    lo, hi = 0.0001, 0.6
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) > mcap: lo = mid
        else: hi = mid
    return mid
P(f"expected return at the price: no-growth {avg(eq_maint)/mcap:.2%}; growth case {solve(lambda r: pv_growth(avg(eq_maint), g_eq, r, gs_eq)):.2%}; "
  f"growth case with no growth spending charged at all (not allowed by (e), shown as the outer bound) {solve(lambda r: pv_growth(avg(eq_maint), g_eq, r, 0)):.2%}")
# all-spending case beside
P(f"all-spending equity-only owner cash {[round(x) for x in nee_oc_eq_all]} avg {avg(nee_oc_eq_all):.0f}: negative in every year; no range on it")
# cap (f) check for FPL-type growth: year-10 owner cash vs highest share of sales
rev = [17069, 20956, 28114, 24753, 27412]   # NEE operating revenues (10-K FY2023/FY2025; 2021 from FY2023 10-K)
y10 = avg(eq_maint) * (1 + g_eq) ** 10
share = max(o / s for o, s in zip(eq_maint, rev))
rev_g = cagr(rev[0], rev[-1], 4)
P(f"cap (f): year-10 owner cash {y10:.0f}; highest owner-cash share of sales in window {share:.1%}; sales growth {rev_g:.1%} -> year-10 sales {rev[-1]*(1+rev_g)**10:.0f}, share needed {y10/(rev[-1]*(1+rev_g)**10):.1%}")

# sum-of-parts beside (FPL equity-only + NEER/Corp all-equity), with corrected FPL net debt
for lab, r in (("5.29%", R), ("10%", FLOOR)):
    a, b, c, d = case_values(r)
    P(f"BESIDE sum-of-parts @ {lab}: no growth ${per_share(a+b):.2f}; growth ${per_share(c+d):.2f}")
a, b, c, d = case_values(FLOOR)
P(f"BESIDE sum-of-parts fair ${per_share((a+b+c+d)/2):.2f}")
# all-equity whole company beside
for lab, r in (("5.29%", R), ("10%", FLOOR)):
    ng = pv_flat(avg(nee_oc_ae_maint), r) - nee_net_debt
    gg = pv_growth(avg(nee_oc_ae_maint), g_eq, r, gs_eq + avg(fpl_credit)) - nee_net_debt
    P(f"BESIDE all-equity @ {lab}: no growth ${per_share(ng):.2f}; growth ({g_eq:.1%}, all growth spending charged, no debt credit) ${per_share(gg):.2f}")
ng = pv_flat(avg(nee_oc_ae_maint), FLOOR) - nee_net_debt; gg = pv_growth(avg(nee_oc_ae_maint), g_eq, FLOOR, gs_eq + avg(fpl_credit)) - nee_net_debt
P(f"BESIDE all-equity fair ${per_share((ng+gg)/2):.2f}")

# Dominion beside (signed, unclosed merger paid in shares): combined averages, no-growth maintenance-only case only
D_ocf = [4037, 3700, 6572, 5018, 5361]      # Dominion OCF (XBRL; 2025 checked against the 10-K FY2025 statement, 0001193125-26-063120)
D_da = [2117, 2442, 2580, 2345, 2387]
D_oc = [o - d for o, d in zip(D_ocf, D_da)]
new_sh = 716.0                               # joint proxy: approx. 716 million NEE shares to be issued
deal_cash = 360 + 2250 * (1 - T)             # cash consideration + customer bill credits after tax (both from the joint proxy)
comb = avg(eq_maint) + avg(D_oc)
for lab, r in (("5.29%", R), ("10%", FLOOR)):
    v = (pv_flat(comb, r) - deal_cash) / (SHARES + new_sh)
    P(f"BESIDE combined with Dominion @ {lab}, no growth, maintenance only: ${v:.2f}/sh (Dominion owner cash avg {avg(D_oc):.0f}, NEE {avg(eq_maint):.0f})")
P(f"NEE price/maintenance owner cash: {mcap/avg(eq_maint):.1f}x; deal value given (716M x $81.90 + $360M) {716*PRICE+360:,.0f} / Dominion maintenance owner cash {avg(D_oc):.0f} = {(716*PRICE+360)/avg(D_oc):.1f}x")
print("\n".join(q))
