"""PNW Q7 arithmetic (and Q4 owner-cash table). Figures in USD millions from the filed cash-flow statements
(FY2023-2025 from 10-K 0000764622-26-000011; FY2016-2022 from the XBRL companyfacts of each year's own 10-K, accessions
in the run file). Run: python -I q7.py"""
yrs = list(range(2016, 2026))
OCF = dict(zip(yrs, [1023, 1118, 1277, 957, 966, 860, 1241, 1208, 1610, 1805]))
SBC = dict(zip(yrs, [19, 21, 20, 18, 18, 18, 16, 17, 24, 27]))
INV = dict(zip(yrs, [1252, 1429, 1193, 1131, 1278, 1387, 1618, 1694, 1934, 2379]))  # net cash used for investing
DA = dict(zip(yrs, [565, 611, 651, 664, 686, 719, 818, 854, 956, 970]))  # D&A incl nuclear fuel (cash-flow line)
NCI = dict(zip(yrs, [23, 23, 23, 23, 23, 21, 21, 21, 21, 18]))  # distributions to noncontrolling interests (Palo Verde lessors)
PVACQ = {y: 0 for y in yrs}; PVACQ[2025] = 199  # Palo Verde sale-leaseback interests bought (financing line, 2025)
REV = dict(zip(yrs, [3499, 3565, 3691, 3471, 3587, 3804, 4324, 4696, 5125, 5340]))
INTPAID = dict(zip(yrs, [184, 189, 208, 219, 217, 228, 245, 311, 360, 389]))
AFUDCD = dict(zip(yrs, [20, 22, 25, 19, 19, 21, 28, 44, 48, 48]))  # borrowed AFUDC shown in investing

print("year  OC_all  OC_maint  growth_spend  maint_share_of_sales")
OCall, OCm, GS = {}, {}, {}
for y in yrs:
    OCall[y] = OCF[y] - SBC[y] - INV[y] - NCI[y] - PVACQ[y]
    OCm[y] = OCF[y] - SBC[y] - DA[y] - NCI[y]
    GS[y] = INV[y] + PVACQ[y] - DA[y]
    print(y, f"{OCall[y]:7.0f} {OCm[y]:8.0f} {GS[y]:12.0f}   {OCm[y]/REV[y]:6.1%}")
W = range(2021, 2026)
avg = lambda d: sum(d[y] for y in W) / 5
a_all, a_m, a_gs = avg(OCall), avg(OCm), avg(GS)
print(f"5-yr avg 2021-25: OC_all {a_all:.1f}  OC_maint {a_m:.1f}  growth spending {a_gs:.1f}")
best_share = max(OCm[y] / REV[y] for y in yrs)
print(f"highest maintenance owner cash / sales in FY2016-2025: {best_share:.1%}")

# growth shown: end-to-end meaningless (102 -> 790); halves: 2021-22 avg vs 2024-25 avg, 3 years apart
h1 = (OCm[2021] + OCm[2022]) / 2; h2 = (OCm[2024] + OCm[2025]) / 2
g_shown = (h2 / h1) ** (1 / 3) - 1
g_sales = (REV[2025] / REV[2021]) ** (1 / 4) - 1
print(f"shown growth (halves) {g_shown:.1%}; carried 10 yrs gives OC {a_m*(1+g_shown)**10:,.0f} = "
      f"{a_m*(1+g_shown)**10/(REV[2025]*(1+g_sales)**10):.0%} of sales at sales growth -> cut (f) to sales growth {g_sales:.2%}")
g = g_sales

# debt credit (utility): LTD incl current maturities; no finance leases or securitization bonds found
LTD2020, LTD2025 = 6314, 9206 + 600
credit_avg = (LTD2025 - LTD2020) / 5
LTD_06_2026, EQ_06_2026 = 9775.8 + 775.0, 7034.8
cap = LTD_06_2026 / (LTD_06_2026 + EQ_06_2026)
print(f"LTD increase/yr {credit_avg:.1f}; credit/growth spending {credit_avg/a_gs:.1%}; cap (own LTD share of LT capital 2026-06-30) {cap:.1%}")

SH = 121.197234  # cover count 2026-07-28
FWD_SH = 4.426350 + 8.306132 + 84 / 103.0  # Feb-2024 remainder + ATM forwards + July 2026 forward (~$84M at ~$103)
FWD_CASH = 4.426350 * 62.82 + 808.887 + 84
PRICE = 105.88
MCAP = SH * PRICE
print(f"shares {SH:.3f}M  price {PRICE}  market cap {MCAP:,.0f}; forward shares {FWD_SH:.2f}M for ~${FWD_CASH:,.0f}M")


def value(oc0, gs0, g, r, credit_share, years=10):
    """equity value: OC grows at g for 10 years, growth spending grows at g, charged net of the debt credit,
    both stop at year 10; then OC flat (zero nominal growth) in perpetuity."""
    v = 0.0
    for t in range(1, years + 1):
        oc = oc0 * (1 + g) ** t
        gs = gs0 * (1 + g) ** t
        credit = min(credit_avg * (1 + g) ** t, credit_share * gs)
        v += (oc - gs + credit) / (1 + r) ** t
    term = oc0 * (1 + g) ** years / r
    return v + term / (1 + r) ** years


def ng(oc0, r):
    return oc0 / r


R, FLOOR = 0.0533, 0.10
out = {}
for label, r in (("sovereign 5.33%", R), ("floor 10%", FLOOR)):
    nog = ng(a_m, r); gro = value(a_m, a_gs, g, r, cap)
    out[label] = (nog, gro)
    print(f"EQUITY-ONLY (utility central) at {label}: no-growth {nog:,.0f} (${nog/SH:.1f}/sh)  growth {gro:,.0f} (${gro/SH:.1f}/sh)")
nog10, gro10 = out["floor 10%"]
fair = (nog10 + gro10) / 2
print(f"FAIR PRICE (equity-only, central): ${fair/SH:.2f}/sh;  with forward shares and their cash: ${(fair+FWD_CASH)/(SH+FWD_SH):.2f}/sh")
lo, hi = sorted(out["sovereign 5.33%"])
print(f"RANGE equity-only: ${lo/SH:.1f} to ${hi/SH:.1f} (width {hi/lo:.2f} to 1); forward-diluted ${(lo+FWD_CASH)/(SH+FWD_SH):.1f} to ${(hi+FWD_CASH)/(SH+FWD_SH):.1f}")

# implied return at the price for each case
def irr(fn):
    lo_, hi_ = 0.0001, 0.5
    for _ in range(100):
        mid = (lo_ + hi_) / 2
        if fn(mid) > MCAP: lo_ = mid
        else: hi_ = mid
    return mid
print(f"return at price: no-growth {a_m/MCAP:.2%}; growth case {irr(lambda r: value(a_m, a_gs, g, r, cap)):.2%}")

# literal window, all spending, no maintenance split (shown beside)
print(f"LITERAL all-spending average {a_all:.0f}: negative; no value on it at any rate")

# ALL-EQUITY beside: add back after-tax cash interest (paid + borrowed AFUDC), tax at 21% federal + 4.9% AZ net
tax = 0.21 + 0.049 * (1 - 0.21)
intr = sum(INTPAID[y] + AFUDCD[y] for y in W) / 5 * (1 - tax)
NETDEBT = 9775.8 + 775.0 + 818.6 - 9.1
for label, r in (("sovereign", R), ("floor", FLOOR)):
    nog = ng(a_m + intr, r) - NETDEBT
    gro = value(a_m + intr, a_gs, g, r, 0.0) - NETDEBT
    print(f"ALL-EQUITY at {label}: after-tax interest {intr:.0f}; net debt {NETDEBT:,.0f}; no-growth ${nog/SH:.1f}/sh, growth ${gro/SH:.1f}/sh")

# sensitivity: growth case at the floor if the cap were the 2025 request's debt share 47.65%
print(f"sensitivity, cap 47.65%: growth at floor ${value(a_m, a_gs, g, FLOOR, 0.4765)/SH:.1f}/sh; "
      f"cap 60% but credit uncapped at avg: ${value(a_m, a_gs, g, FLOOR, 1.0)/SH:.1f}/sh")
# sensitivity: no-growth on the best single year (2025) maintenance owner cash
print(f"sensitivity, 2025 maintenance owner cash {OCm[2025]} at the floor: ${OCm[2025]/FLOOR/SH:.1f}/sh; at sovereign ${OCm[2025]/R/SH:.1f}/sh")
