"""Q7 arithmetic for Spire (SR), USD millions. Every input is a filed figure (accession in the run file) or a CONVENTION
named in the run file. This script computes; it concludes nothing."""

R = 0.0543          # 30-year Treasury par yield, 2026-10-16 (tools/sources.py)
FLOOR = 0.10        # the floor CONVENTION (Q7)
T = 0.247           # 21% federal + 3.7% state and local (10-K Note 12 rate reconciliation, FY2025)
PRICE = 82.03       # close 2026-10-16, aggregator, flagged
SHARES = 59.112807  # 10-Q cover, 2026-07-31
NET_DEBT = 5758.0 + 238.1 + 1263.5 - 20.7   # 10-Q balance sheet 2026-06-30: LTD + current LTD + notes payable - cash
MCAP = PRICE * SHARES
EV = MCAP + NET_DEBT
INT_RUNRATE = 85.6 * 4                       # 10-Q: interest expense, net, quarter to 2026-06-30, annualized

yrs = [2021, 2022, 2023, 2024, 2025]
# ---- literal window, consolidated as filed (all businesses, including those sold in 2026) ----
ocf   = dict(zip(yrs, [249.8, 55.0, 440.2, 912.4, 578.0]))
sbc   = dict(zip(yrs, [13.9, 6.4, 9.8, 5.8, 6.7]))
intp  = dict(zip(yrs, [98.7, 119.9, 177.5, 205.6, 207.1]))   # interest paid, net of capitalized
capex = dict(zip(yrs, [624.8, 552.2, 662.5, 861.3, 922.4]))
acq   = dict(zip(yrs, [0.0, 0.0, 37.0, 175.9, 0.0]))
da    = dict(zip(yrs, [213.1, 237.3, 254.8, 278.4, 298.2]))
lit_all = {y: ocf[y] - sbc[y] + intp[y] * (1 - T) - capex[y] - acq[y] for y in yrs}
lit_mnt = {y: ocf[y] - sbc[y] + intp[y] * (1 - T) - da[y] for y in yrs}
avg = lambda d, ys=yrs: sum(d[y] for y in ys) / len(ys)
print('LITERAL WINDOW (consolidated as filed; all-equity, before interest at 24.7%):')
print('  all spending   ', ' '.join(f'{lit_all[y]:8.1f}' for y in yrs), f'  mean {avg(lit_all):8.1f}')
print('  maint. at D&A  ', ' '.join(f'{lit_mnt[y]:8.1f}' for y in yrs), f'  mean {avg(lit_mnt):8.1f}')

# ---- central: the continuing business at the price date ----
gu_op  = dict(zip(yrs, [374.0, 339.9, 350.8, 400.6, 406.2]))  # Gas Utility segment operating income
gu_da  = dict(zip(yrs, [204.4, 227.9, 244.4, 263.6, 277.6]))
gu_cx  = dict(zip(yrs, [590.4, 528.6, 588.6, 691.1, 816.8]))
gu_rev = {2020: 1752.0, 2021: 2119.3, 2022: 1946.1, 2023: 2456.9, 2024: 2437.9, 2025: 2207.6}
gu_op20 = 334.3
# working capital and other operating cash lines, consolidated cash-flow statements (AR, inventories, regulatory
# assets and liabilities, AP, delayed/advance billings, taxes accrued, other assets and liabilities, other)
wc = {2021: -343.0 - 111.0 + 76.6 + 177.7 - 12.4 + 8.9 - 116.1 + 17.3,
      2022: -26.5 - 117.2 - 409.0 + 190.7 - 25.5 + 11.2 - 93.5 + 8.8,
      2023: 334.2 + 142.8 - 68.7 - 389.2 + 1.5 + 15.0 - 117.6 + 13.0,
      2024: 12.7 + 15.8 + 341.4 - 25.1 + 37.5 + 1.1 - 65.6 + 8.3,
      2025: -38.4 - 18.6 + 26.5 + 47.5 + 8.1 + 6.0 - 93.4 + 13.1}
WC = avg(wc)                                   # five-year average: the Uri build (2021) and its recovery (2022-24) both inside
base_years = [2022, 2023, 2024, 2025]          # FY2021 aberrational on the filer's own description (Winter Storm Uri)
GU_NOPAT = avg(gu_op, base_years) * (1 - T)
GU_GROWTH_SPEND = avg(gu_cx, base_years) - avg(gu_da, base_years)
PIPE_CORP = (0.27 * 83.8 - 8.2) * (1 - T)      # FY2025: pipelines' share of Midstream (filer's 27% NI mix) + Other
TN = ((124.942 - 0.121 - 4.883) + (121.605 - 3.638 - 5.864)) / 2 * (1 - T)   # Spire Tennessee, 8-K/A Ex. 99.1
TN_CAPEX = (1801.112 - 1669.464) + 35.914      # change in net PP&E plus D&A, calendar 2025
TN_ALL = TN + 35.914 - TN_CAPEX
print('\nWORKING CAPITAL and other operating lines by year:', ' '.join(f'{wc[y]:.1f}' for y in yrs), f'; mean {WC:.1f}')
BASE_M = GU_NOPAT + WC + PIPE_CORP + TN
BASE_A = GU_NOPAT + avg(gu_da, base_years) - avg(gu_cx, base_years) + WC + PIPE_CORP + TN_ALL
print(f'CENTRAL base, maintenance-only (D&A as maintenance): GU {GU_NOPAT:.1f} + WC/other {WC:.1f} + pipelines/corporate '
      f'{PIPE_CORP:.1f} + Tennessee {TN:.1f} = {BASE_M:.1f}')
print(f'  all-spending base: {BASE_A:.1f}  (Tennessee all-spending {TN_ALL:.1f}); growth spending GU {GU_GROWTH_SPEND:.1f}/yr')

def cagr(a, b, n): return (b / a) ** (1 / n) - 1
g_shown = cagr(gu_op[2022], gu_op[2025], 3)
g_lit = cagr(gu_op[2021], gu_op[2025], 4)
g_sales = cagr(gu_rev[2022], gu_rev[2025], 3)
g_sales_lit = cagr(gu_rev[2021], gu_rev[2025], 4)
share = {y: (gu_op[y] if y in gu_op else gu_op20) * (1 - T) / gu_rev[y] for y in gu_rev}
hi = max(share.values())
yr10_share = GU_NOPAT * (1 + g_shown) ** 10 / (gu_rev[2025] * (1 + g_sales) ** 10)
print(f'\nGROWTH: GU operating income FY2022-25 {g_shown:.2%} (literal FY2021-25 {g_lit:.2%}); GU revenue FY2022-25 '
      f'{g_sales:.2%} (literal {g_sales_lit:.2%})')
print('  owner cash share of GU revenue:', ', '.join(f'{y} {share[y]:.1%}' for y in sorted(share)), f'; highest {hi:.1%}')
print(f'  at the shown rate, year-ten owner cash / year-ten revenue = {yr10_share:.1%} -> cap (f) '
      f'{"BINDS: growth cut to sales growth" if yr10_share > hi else "does not bind"}')
g_cap = g_sales if yr10_share > hi else g_shown
# (e): never charge all spending and also cap the growth that spending bought -> the central growth end charges the
# growth spending at the SHOWN rate; the (f)-capped rate is shown beside only.
g = g_shown

def pv_growth(base_grow, base_flat, spend, g, r, n=10):
    """Grow base_grow at g for n years while charging growth spending (grown at g); flat parts held; then no growth,
    no growth spending, zero nominal growth after year n."""
    pv = 0.0
    for t in range(1, n + 1):
        cf = base_grow * (1 + g) ** t + base_flat - spend * (1 + g) ** (t - 1)
        pv += cf / (1 + r) ** t
    term = (base_grow * (1 + g) ** n + base_flat) / r
    return pv + term / (1 + r) ** n

def case_values(r, base_m, gu, spend, g):
    flat = base_m - gu
    v_no = base_m / r
    v_gr = pv_growth(gu, flat, spend, g, r)
    return v_no, v_gr

def per_share(v): return (v - NET_DEBT) / SHARES

print(f'\nPRICE {PRICE} x {SHARES:.4f}M = market cap {MCAP:.1f}; net debt 2026-06-30 {NET_DEBT:.1f}; EV {EV:.1f}')
for label, gg in (('central: shown rate', g), ('beside: (f) cap applied', g_cap), ('beside: literal window', g_lit)):
    v_no, v_gr = case_values(R, BASE_M, GU_NOPAT, GU_GROWTH_SPEND, gg)
    f_no, f_gr = case_values(FLOOR, BASE_M, GU_NOPAT, GU_GROWTH_SPEND, gg)
    print(f'{label:24s} g={gg:.2%}: at 5.43% no-growth {v_no:8.1f} -> ${per_share(v_no):7.2f}/sh; growth {v_gr:8.1f} -> '
          f'${per_share(v_gr):7.2f}/sh | at 10%: ${per_share(f_no):7.2f} and ${per_share(f_gr):7.2f}; '
          f'fair (avg) ${(per_share(f_no)+per_share(f_gr))/2:7.2f}')

# equity-only beside: owner cash after interest at the run-rate, against the market value
EQ_BASE = BASE_M - INT_RUNRATE * (1 - T)
print(f'\nEQUITY-ONLY: base {BASE_M:.1f} - after-tax run-rate interest {INT_RUNRATE*(1-T):.1f} = {EQ_BASE:.1f}; '
      f'no-growth at 5.43% {EQ_BASE/R:.1f} = ${EQ_BASE/R/SHARES:.2f}/sh; at 10% ${EQ_BASE/FLOOR/SHARES:.2f}/sh')
v_gr_eq = pv_growth(GU_NOPAT, EQ_BASE - GU_NOPAT, GU_GROWTH_SPEND, g, R)
f_gr_eq = pv_growth(GU_NOPAT, EQ_BASE - GU_NOPAT, GU_GROWTH_SPEND, g, FLOOR)
print(f'  growth case equity-only: at 5.43% ${v_gr_eq/SHARES:.2f}/sh; at 10% ${f_gr_eq/SHARES:.2f}/sh; '
      f'fair (avg at 10%) ${(EQ_BASE/FLOOR + f_gr_eq)/2/SHARES:.2f}/sh')

# the floor test: expected return at the price on each case, and on the most generous variant
def irr(fn, lo=-0.5, hi=0.5):
    for _ in range(200):
        mid = (lo + hi) / 2
        if fn(mid) > EV: lo = mid
        else: hi = mid
    return mid
print('\nFLOOR TEST, expected return at the price (EV basis):')
print(f'  central no-growth: {BASE_M/EV:.2%}')
print(f'  central growth case: {irr(lambda r: pv_growth(GU_NOPAT, BASE_M-GU_NOPAT, GU_GROWTH_SPEND, g, r), 0.001, 0.5):.2%}')
GEN_GU = gu_op[2025] * (1 - 0.18)                       # FY2025 run-rate, effective book rate 18.0%
GEN_BASE = GEN_GU + 0.0 + (0.27 * 83.8 - 8.2) * 0.82 + 121.605 * 0.82   # no WC drag, Tennessee before interest income kept
print(f'  most generous (FY2025 run-rate, 18% tax, no working-capital drag, growth {g_shown:.2%} uncapped, growth spending '
      f'charged): base {GEN_BASE:.1f}; no-growth {GEN_BASE/EV:.2%}; growth '
      f'{irr(lambda r: pv_growth(GEN_GU, GEN_BASE-GEN_GU, GU_GROWTH_SPEND, g_shown, r), 0.001, 0.5):.2%}')
print(f'  same, growth spending NOT charged (indefensible under (e), shown only as a ceiling): '
      f'{irr(lambda r: pv_growth(GEN_GU, GEN_BASE-GEN_GU, 0.0, g_shown, r), 0.001, 0.5):.2%}')
print(f'\nLITERAL beside: maintenance mean {avg(lit_mnt):.1f} -> no-growth at 5.43% ${per_share(avg(lit_mnt)/R):.2f}/sh; '
      f'all-spending mean {avg(lit_all):.1f} (not positive)')
print(f'Mississippi sale (signed, not closed): +$75.0 cash beside, its earnings out; deferred storage consideration $50.0 '
      f'beside; Oct-2026 $350 bonds beside if not used to repay notes: net debt {NET_DEBT+350:.1f}')
