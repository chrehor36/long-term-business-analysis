# CNP 2026-10-18: the arithmetic behind Q3, Q4 and Q7. Every input is a filed figure (USD millions) with its source
# in the comment; the cases are those of Q7's range convention as the run file states them. Run: python -I q7.py
years = [2021, 2022, 2023, 2024, 2025]
# Statements of Consolidated Cash Flows: FY2023 10-K (0001130310-24-000010) for 2021-2022, FY2025 10-K (0001130310-26-000008) for 2023-2025
ocf      = [22, 1810, 3877, 2139, 2486]
capex    = [3164, 4419, 4401, 4513, 4870]
asset_aq = [0, 0, 0, 0, 357]          # Posey Solar asset acquisition 2025
finlease = [179, 485, 0, 0, 0]        # payment of obligation for finance lease (TEEEF), financing section
pref_div = [107, 49, 50, 0, 0]        # dividends on preferred stock
sbc      = [48, 51, 65, 34, 48]       # LTIP compensation expense, Note 8 (non-cash, added back inside operating cash)
da       = [1316, 1288, 1401, 1439, 1530]
lt_iss   = [4493, 2089, 6044, 3955, 3714]
lt_rep   = [2968, 1795, 3190, 1050, 1579]
cp_net   = [1132, -74, -1055, -539, -2]
divest   = [22, 2075, 144, 0, 1219]   # proceeds from divestitures
eq_sec   = [1320, 702, 0, 0, 0]       # proceeds from sale of equity securities (Energy Transfer units received for Enable)
enable_c = [-44, 0, 0, 0, 0]          # Enable merger transaction costs net of cash received, 2021
int_paid = [489, 480, 664, 805, 983]  # cash paid for interest, net of capitalized (supplemental)
revenue  = [8352, 9321, 8696, 8643, 9357]
op_inc   = [1363, 1566, 1760, 1990, 2110]
ni_common= [1391, 1008, 867, 1019, 1052]

TAX = 0.21           # federal statutory rate, for the interest shield on the all-equity basis (CONVENTION of this run)
DEBT_SHARE = 0.5675  # Houston Electric allowed long-term debt share, PUCT order 2025-03-13 (10-K Item 7)
SOV, FLOOR = 0.0543, 0.10
SH, SH_FWD, FWD_CASH = 658.72, 683.585, 910.0
PRICE = 40.55
MCAP = SH * PRICE
BERYL = 1100.0       # Beryl restoration costs the PUCT approved for securitization (Note 7), bonds sold 2026-02-26
OHIO_CASH, OHIO_NOTE, OHIO_PRETAX = 1420.0, 1200.0, 98.0   # 8-K 2026-10-01; Note 4 pre-tax income 2025
# Net debt at 2026-06-30 (10-Q 0001130310-26-000041): securitization 120+1746, other long-term debt 1616+21160, short-term 0,
# indexed debt derivative 451; less cash 49 and equity securities 404
debt_0630 = 120 + 1746 + 1616 + 21160 + 451
net_debt = debt_0630 - 49 - 404 - OHIO_CASH - OHIO_NOTE

n = len(years); S = sum
def avg(x): return S(x) / n
net_lt = [a - b + c for a, b, c in zip(lt_iss, lt_rep, cp_net)]
cap_all = [c + a + f for c, a, f in zip(capex, asset_aq, finlease)]
credit_window = min(S(net_lt), DEBT_SHARE * S(cap_all))
print("window", years[0], "-", years[-1])
print("net long-term debt and CP raised by year", net_lt, "sum", S(net_lt))
print("cap on the credit: %.4f x all capital spending %d = %.0f; credit taken %.0f" % (DEBT_SHARE, S(cap_all), DEBT_SHARE*S(cap_all), credit_window))

# Equity-only series (after interest), by year
all_spend = [o - s - c - p for o, s, c, p in zip(ocf, sbc, cap_all, pref_div)]
maint = [o - s - d - f - p for o, s, d, f, p in zip(ocf, sbc, da, finlease, pref_div)]
print("owner cash to equity, all spending, no credit:", all_spend, "avg %.0f" % avg(all_spend))
print("  with the window debt credit: avg %.0f" % (avg(all_spend) + credit_window / n))
print("  with divestiture proceeds as well (c): avg %.0f" % (avg(all_spend) + credit_window/n + (S(divest)+S(eq_sec)+S(enable_c))/n))
print("owner cash to equity, maintenance only (D&A as the guess):", maint, "avg %.0f" % avg(maint))
m_lit = avg(maint); m_rec = (S(maint) + BERYL) / n
print("  recast for the Beryl deferral recovered by the 2026 bonds: avg %.0f" % m_rec)
h1 = (maint[0] + maint[1]) / 2; h2 = (maint[3] + maint[4]) / 2
print("halves of the maintenance series: first %.0f, second %.0f (sign change, growth meaningless)" % (h1, h2))
# Ohio after the window: remove its after-tax earnings (pre-tax x (1-0.21)), add the proceeds
ohio_oc = OHIO_PRETAX * (1 - TAX)
def per_share(v, fwd=False): return (v + (FWD_CASH if fwd else 0)) / (SH_FWD if fwd else SH)

def no_growth(m, r): return m / r
def growth_case(m0, g, gspend, r, yrs=10):
    pv = 0.0; m = m0
    for t in range(1, yrs + 1):
        m *= (1 + g); pv += (m - gspend) / (1 + r) ** t
    return pv + (m / r) / (1 + r) ** yrs

print("\nEQUITY-ONLY (central for the regulated utility)")
for label, m in (("literal window", m_lit), ("recast (Beryl)", m_rec)):
    m_post = m - ohio_oc
    v_sov = no_growth(m_post, SOV) + OHIO_CASH + OHIO_NOTE
    v_10 = no_growth(m_post, FLOOR) + OHIO_CASH + OHIO_NOTE
    print("%s: owner cash %.0f, less Ohio %.0f = %.0f; yield on market cap %.2f%%" % (label, m, ohio_oc, m_post, 100*m_post/MCAP))
    print("   no-growth value at the sovereign $%.0fM = $%.2f a share ($%.2f with the forward shares)" % (v_sov, per_share(v_sov), per_share(v_sov, True)))
    print("   no-growth value at ten percent $%.0fM = $%.2f a share ($%.2f with the forward shares)" % (v_10, per_share(v_10), per_share(v_10, True)))
# Illustrative generous growth case (outside the range convention; for the floor test's robustness only)
gspend = (S(cap_all) - S(da)) / n - credit_window / n
g_oi = (op_inc[-1] / op_inc[0]) ** (1/4) - 1
g_rev = (revenue[-1] / revenue[0]) ** (1/4) - 1
print("\ngrowth spending a year net of the debt credit %.0f; operating income growth %.1f%%; revenue growth %.1f%%" % (gspend, 100*g_oi, 100*g_rev))
for g in (g_oi, g_rev):
    for r in (SOV, FLOOR):
        v = growth_case(m_rec - ohio_oc, g, gspend, r) + OHIO_CASH + OHIO_NOTE
        print("  illustrative growth case g=%.1f%% at r=%.2f%%: $%.0fM = $%.2f a share" % (100*g, 100*r, v, per_share(v)))
# what the price implies: the no-growth owner cash needed to earn ten percent at the price
print("owner cash a year needed for ten percent at the price on no growth: $%.0fM" % (FLOOR * (MCAP - OHIO_CASH - OHIO_NOTE) + ohio_oc))

print("\nALL-EQUITY (beside)")
ae_maint = [o - s - d - f + i * (1 - TAX) for o, s, d, f, i in zip(ocf, sbc, da, finlease, int_paid)]
ae_all = [o - s - c + i * (1 - TAX) for o, s, c, i in zip(ocf, sbc, cap_all, int_paid)]
for label, m in (("maintenance only, literal", avg(ae_maint)), ("maintenance only, recast", (S(ae_maint)+BERYL)/n), ("all spending", avg(ae_all))):
    m_post = m - ohio_oc
    ev = MCAP + net_debt
    print("%s: %.0f a year; EV %.0f (net debt %.0f); yield %.2f%%; no-growth at sovereign less net debt $%.2f; at ten percent $%.2f a share"
          % (label, m_post, ev, net_debt, 100*m_post/ev, (m_post/SOV - net_debt)/SH, (m_post/FLOOR - net_debt)/SH))

print("\nQ3 figures")
eq_common = {2020: 8348-2363, 2021: 9415-790, 2022: 10042-790, 2023: 9667, 2024: 10666, 2025: 11153}
gw = {2020: 4697, 2021: 4294, 2022: 4294, 2023: 4160, 2024: 3943, 2025: 3550}
for i, y in enumerate(years):
    a = (eq_common[y-1] + eq_common[y]) / 2; t = ((eq_common[y-1]-gw[y-1]) + (eq_common[y]-gw[y])) / 2
    print(y, "ROE on common %.1f%%; on tangible common %.1f%%" % (100*ni_common[i]/a, 100*ni_common[i]/t))
print("five-year operating cash %d vs capital spending %d; cash dividends to common %d" % (S(ocf), S(cap_all), S([385,440,485,522,574])))

print("\nFLOOR TEST: expected return at the price, equity-only, each case (market value less the Ohio proceeds)")
base_mv = MCAP - OHIO_CASH - OHIO_NOTE
def irr_growth(m0, g, gspend):
    lo, hi = -0.5, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        v = growth_case(m0, g, gspend, mid) if mid > 0.001 else 1e18
        if v > base_mv: lo = mid
        else: hi = mid
    return mid
mech_credit = min(credit_window / n, DEBT_SHARE * avg(da))
cases = {
  "maintenance only, literal (central)": m_lit - ohio_oc,
  "maintenance only, before the Beryl draw (beside)": m_rec - ohio_oc,
  "all spending with the debt credit (beside)": avg(all_spend) + credit_window / n - ohio_oc,
  "all spending with the debt credit and the divestiture proceeds (beside)": avg(all_spend) + credit_window/n + (S(divest)+S(eq_sec)+S(enable_c))/n - ohio_oc,
  "maintenance only with the debt credited against the maintenance spending too (mechanical reading, beside)": m_lit + mech_credit - ohio_oc,
  "the same, before the Beryl draw (beside)": m_rec + mech_credit - ohio_oc,
}
for k, v in cases.items():
    print("  %-100s owner cash %6.0f  return at the price on no growth %5.2f%%  value at sovereign $%6.2f  at ten percent $%6.2f"
          % (k, v, 100 * v / base_mv, per_share(v / SOV + OHIO_CASH + OHIO_NOTE), per_share(v / FLOOR + OHIO_CASH + OHIO_NOTE)))
print("  illustrative growth case (11.5%% for ten years, growth spending charged): return at the price %.2f%%" % (100 * irr_growth(m_rec - ohio_oc, g_oi, gspend)))
lo_end, hi_end = per_share(no_growth(m_lit - ohio_oc, FLOOR) + OHIO_CASH + OHIO_NOTE), per_share(no_growth(m_rec - ohio_oc, FLOOR) + OHIO_CASH + OHIO_NOTE)
print("\nFAIR PRICE, equity-only central: ends at ten percent $%.2f and $%.2f, average $%.2f" % (lo_end, hi_end, (lo_end + hi_end) / 2))
lo_f, hi_f = per_share(no_growth(m_lit - ohio_oc, FLOOR) + OHIO_CASH + OHIO_NOTE, True), per_share(no_growth(m_rec - ohio_oc, FLOOR) + OHIO_CASH + OHIO_NOTE, True)
print("  with the forward shares and their cash: $%.2f and $%.2f, average $%.2f" % (lo_f, hi_f, (lo_f + hi_f) / 2))
ae_lit = avg(ae_maint) - ohio_oc; ae_rec = (S(ae_maint) + BERYL) / n - ohio_oc
a1, a2 = (ae_lit / FLOOR - net_debt) / SH, (ae_rec / FLOOR - net_debt) / SH
print("FAIR PRICE, all-equity beside: $%.2f and $%.2f, average $%.2f" % (a1, a2, (a1 + a2) / 2))
