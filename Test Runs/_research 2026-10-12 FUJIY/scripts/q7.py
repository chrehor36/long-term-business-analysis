"""Q7 COMPUTATION for FUJIY (all figures yen millions, fiscal years ending March of the following calendar year).
Sources: cash-flow statements in the annual Financial Results releases (extracts/cf_*.txt); FY2025 = year ended 2026-03-31."""
fy = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
ocf = [288619, 261152, 249343, 255667, 420861, 323934, 210452, 407941, 428162, 410555]
ppe = [74647, 63043, 68549, 84677, 100063, 126054, 269844, 417966, 502794, 521583]
sw  = [22318, 18541, 20471, 25047, 25544, 39853, 53628, 46746, 55211, 48983]
# investing "Other" incl. sales of PP&E (separate line from FY2023 restated): positive = inflow
oth = [-17770, -8779, -365, -8747, -13485, -8242, -7968, 15413, 33926 - 22499, 14073 - 23647]
da  = [117635, 127642, 129932, 122653, 123423, 132999, 142215, 150014, 163567, 172371]
# purchases of businesses net of disposals, plus capital transactions with noncontrolling interests (buy-outs)
acq = [1334, 127269, 84310 + 78551, 121789 + 241207, 173515 - 14707 - 1418, 10714 - 24480 + 3852,
       28653 - 218, 103849 - 12416 + 57895, 3873 + 671, 6113 - 7752 - 141]
intexp = {2021: 2316, 2022: 5006, 2023: 8483, 2024: 8752, 2025: 4993}
rev = {2021: 2525773, 2025: 3356969}
TAX = 0.306   # CONVENTION of this run: Japanese statutory effective rate, approx; used only to put interest after tax
SBC = 1800    # guess: treasury shares disposed as share-based pay, FY2024 2,237 and FY2025 1,399 (equity statements)
R_GOV = 0.0414; FLOOR = 0.10
NET_DEBT = 307269 + 668333 - 150651 - 45026   # 2026-06-30 balance sheet (Q1 FY2026 release)
SHARES = 1234150284 - 38542505                  # 2026-06-30, issued less treasury
PRICE = 3402.0; USDJPY = 158.438; ADS_RATIO = 0.5

capex = [p + s - o for p, s, o in zip(ppe, sw, oth)]
oc_all = [o - c for o, c in zip(ocf, capex)]
oc_mnt = [o - d for o, d in zip(ocf, da)]
growth_cap = [c - d for c, d in zip(capex, da)]
print('FY   OCF    capex   D&A   acq   OC_all   OC_maint  growthcap')
for i, y in enumerate(fy):
    print(y, ocf[i], capex[i], da[i], acq[i], oc_all[i], oc_mnt[i], growth_cap[i])
W = slice(5, 10)  # FY2021..FY2025
avg = lambda xs: sum(xs) / len(xs)
addback = avg([intexp[y] for y in range(2021, 2026)]) * (1 - TAX)
base_all = avg(oc_all[W]) + addback - SBC
base_mnt = avg(oc_mnt[W]) + addback - SBC
mnt_after_acq = [m - a for m, a in zip(oc_mnt[W], acq[W])]
base_def = avg(mnt_after_acq) + addback - SBC
gcap = avg(growth_cap[W])
g_tot = (mnt_after_acq[-1] / mnt_after_acq[0]) ** 0.25 - 1
g_org = (oc_mnt[9] / oc_mnt[5]) ** 0.25 - 1
g_sales = (rev[2025] / rev[2021]) ** 0.25 - 1
print(f'\nwindow FY2021-25: avg OC all-spending {avg(oc_all[W]):,.0f}; maint-only {avg(oc_mnt[W]):,.0f}; maint after acq {avg(mnt_after_acq):,.0f}')
print(f'after-tax interest add-back {addback:,.0f}; SBC deducted {SBC:,}')
print(f'bases (all-equity): all-spending {base_all:,.0f}; maint-only organic {base_mnt:,.0f}; DEFAULT maint after acq {base_def:,.0f}')
print(f'growth spending above D&A, window avg {gcap:,.0f}; net purchases over window {sum(acq[W]):,.0f}')
print(f'growth: total (maint after acq, end years) {g_tot:.2%}; organic maint {g_org:.2%}; sales {g_sales:.2%}')

def value(base, g, r, spend=0.0, years=10):
    v = 0.0; c = base
    for t in range(1, years + 1):
        c = base * (1 + g) ** t
        v += (c - spend) / (1 + r) ** t
    v += (c / r) / (1 + r) ** years
    return v
def case(name, base, g, spend):
    out = {}
    for r in (R_GOV, FLOOR):
        ev = value(base, g, r, spend) if g or spend else base / r
        out[r] = ev
    return out
cases = {
  'TOP: no growth, maintenance only, acquisitions deducted (default)': (base_def, 0.0, 0.0),
  'BOTTOM: growth case, total growth credited, growth spending charged': (base_def, g_tot, gcap),
  'beside: organic pair no growth (maint only, no acq)': (base_mnt, 0.0, 0.0),
  'beside: organic pair growth case': (base_mnt, g_org, gcap),
  'beside: literal window all-spending no growth': (base_all, 0.0, 0.0),
}
print()
res = {}
for k, (b, g, s) in cases.items():
    o = case(k, b, g, s); res[k] = o
    ps = {r: (o[r] - NET_DEBT) * 1e6 / SHARES for r in o}
    print(f'{k}\n   EV@{R_GOV:.2%} {o[R_GOV]:,.0f}  per share {ps[R_GOV]:,.0f} | EV@10% {o[FLOOR]:,.0f} per share {ps[FLOOR]:,.0f}')
mcap = PRICE * SHARES / 1e6; ev_px = mcap + NET_DEBT
print(f'\nmarket cap {mcap:,.0f}; net debt {NET_DEBT:,}; EV at price {ev_px:,.0f}; shares {SHARES:,}')
print(f'yield on EV, default base {base_def/ev_px:.2%}; maint organic {base_mnt/ev_px:.2%}')
top, bot = list(res.values())[0], list(res.values())[1]
fair_ae = ((top[FLOOR] + bot[FLOOR]) / 2 - NET_DEBT) * 1e6 / SHARES
# equity-only: owner cash after interest (no add-back) against market value, no debt deducted
eq_top = (base_def - addback) / FLOOR
eq_bot = value(base_def - addback, g_tot, FLOOR, gcap)
fair_eq = (eq_top + eq_bot) / 2 * 1e6 / SHARES
print(f'FAIR PRICE all-equity {fair_ae:,.0f} yen/share = ${fair_ae*ADS_RATIO/USDJPY:,.2f}/ADS; equity-only {fair_eq:,.0f} yen = ${fair_eq*ADS_RATIO/USDJPY:,.2f}/ADS')
print(f'price {PRICE:,.0f} yen = ${PRICE*ADS_RATIO/USDJPY:,.2f}/ADS')
# expected return at price, no-growth default case (cash yield on EV, zero growth)
