"""CYH owner cash and the Q7 range, COMPUTATION, NOT A CLEARANCE. Figures in USD millions from the filed
statements (10-K FY2021 0001564590-22-005570, FY2023 0000950170-24-018021, FY2025 0001193125-26-059509;
10-Q Q2 2026 0001193125-26-314196). Arithmetic only."""

years = [2021, 2022, 2023, 2024, 2025]
rev   = {2021: 12368, 2022: 12211, 2023: 12490, 2024: 12634, 2025: 12485}
ocf   = {2021: -131, 2022: 300, 2023: 210, 2024: 480, 2025: 543}
sbc   = {2021: 25, 2022: 20, 2023: 22, 2024: 17, 2025: 11}
capex = {2021: 469, 2022: 415, 2023: 467, 2024: 360, 2025: 335}
da    = {2021: 540, 2022: 534, 2023: 505, 2024: 486, 2025: 426}
acq   = {2021: 3, 2022: 9, 2023: 38, 2024: 25, 2025: 1}
nci   = {2021: 121, 2022: 125, 2023: 141, 2024: 155, 2025: 164}   # distributions to minority partners
flp   = {2021: 0, 2022: 0, 2023: 3, 2024: 2, 2025: 2}            # finance-lease principal (run.py lines; 2021-22 not printed)
gain_tax = {2021: 0, 2022: 0, 2023: 0, 2024: 17, 2025: 169}       # cash tax on divestiture gains (10-K FY2025 MD&A)
intpd = {2021: 778, 2022: 835, 2023: 801, 2024: 741, 2025: 804}   # cash interest paid
T = 0.25   # CONVENTION of this run: 21% federal plus about 4% state on the interest shield

def levered(y, base='capex'):
    spend = capex[y] if base == 'capex' else da[y]
    return ocf[y] + gain_tax[y] - sbc[y] - spend - acq[y] - nci[y] - flp[y]

def unlev(y, base='capex'):
    return levered(y, base) + intpd[y] * (1 - T)

def avg(f, ys, **k):
    return sum(f(y, **k) for y in ys) / len(ys)

SOV = 0.056
FLOOR = 0.10
SHARES = 141.009357           # millions, 10-Q cover 2026-07-16
PRICE = 3.00                  # aggregator, 2026-10-13
DEBT_PRINCIPAL = 9578 + 192   # total debt as filed 2026-06-30 plus unamortized issuance costs
CASH = 149
NET_DEBT = DEBT_PRINCIPAL - CASH
BASE_REV = 12485 - 1600       # 2025 revenue less the 2025 revenue of hospitals sold in 2026 (10-Q MD&A)

def pv_flat(c, r):
    # ten years then zero nominal growth = a flat perpetuity
    return c / r

def pv_growth(c, g, r, n=10):
    pv = 0; x = c
    for t in range(1, n + 1):
        x *= (1 + g); pv += x / (1 + r) ** t
    return pv + (x / r) / (1 + r) ** n

print('year  levered(capex)  levered(D&A)  unlevered(capex)  unlevered(D&A)  margin unlev capex')
for y in years:
    print(y, f'{levered(y):8.0f} {levered(y,base="da"):12.0f} {unlev(y):14.0f} {unlev(y,base="da"):14.0f}   {100*unlev(y)/rev[y]:5.1f}%')

cases = {}
for label, ys in [('central 2022-25 (2021 aberrational)', [2022, 2023, 2024, 2025]), ('literal 2021-25', years)]:
    for base in ('capex', 'da'):
        u = avg(unlev, ys, base=base); l = avg(levered, ys, base=base)
        m = sum(unlev(y, base=base) / rev[y] for y in ys) / len(ys)
        cases[(label, base)] = (u, l, m)
        print(f'\n{label} [{base}]: unlevered avg {u:.0f}, levered avg {l:.0f}, unlevered margin {100*m:.2f}%')

print(f'\nnet debt (principal) {NET_DEBT}; base revenue {BASE_REV}; shares {SHARES}M; price {PRICE}; market cap {PRICE*SHARES:.0f}')
print(f'EV at price {PRICE*SHARES + NET_DEBT:.0f}')
for k, (u, l, m) in cases.items():
    for scaled in (False, True):
        c = m * BASE_REV if scaled else u
        ev_s = pv_flat(c, SOV); ev_f = pv_flat(c, FLOOR)
        print(f'{k[0]:38s} {k[1]:5s} {"scaled" if scaled else "as-is ":6s} cash {c:6.0f}  EV@sov {ev_s:7.0f} per sh {(ev_s-NET_DEBT)/SHARES:7.2f}'
              f' | EV@10% {ev_f:7.0f} per sh {(ev_f-NET_DEBT)/SHARES:7.2f}  | yield on EV at price {100*c/(PRICE*SHARES+NET_DEBT):5.2f}%')

# equity-only: levered owner cash after interest against market value
for k, (u, l, m) in cases.items():
    print(f'equity-only {k}: levered avg {l:.0f} vs market cap {PRICE*SHARES:.0f} -> yield {100*l/(PRICE*SHARES):.1f}%')

# what owner cash would the price need at the floor (all-equity)?
need = (PRICE * SHARES + NET_DEBT) * FLOOR
print(f'\nunlevered owner cash needed for 10% on EV at the price: {need:.0f} (margin on base revenue {100*need/BASE_REV:.1f}%)')
# best single year, scaled
best = max(unlev(y) / rev[y] for y in years) * BASE_REV
print(f'best year margin scaled to base revenue: {best:.0f}; EV@10% {best/FLOOR:.0f}; per sh {(best/FLOOR-NET_DEBT)/SHARES:.2f}; EV@sov per sh {(best/SOV-NET_DEBT)/SHARES:.2f}')
# H1 2026
print('H1 2026 levered: OCF -209 - SBC 5 - capex 152 - acq 53 - NCI 90 =', -209 - 5 - 152 - 53 - 90, '; interest paid 437')

# shown growth: central capex series 2022->2025 end to end, and the cap of specific (f)
g_shown = (unlev(2025) / unlev(2022)) ** (1 / 3) - 1
g_sales_22_25 = (rev[2025] / rev[2022]) ** (1 / 3) - 1
g_sales_21_25 = (rev[2025] / rev[2021]) ** (1 / 4) - 1
print(f'\nshown growth of unlevered owner cash 2022-25: {100*g_shown:.1f}%/yr; ten years on 448 -> {448*(1+g_shown)**10:.0f} = {100*448*(1+g_shown)**10/BASE_REV:.0f}% of base revenue (highest margin earned 6.4%): absurd, cut by (f)')
print(f'sales growth 2022-25 {100*g_sales_22_25:.2f}%/yr; 2021-25 {100*g_sales_21_25:.2f}%/yr')
for c, lab in [(448, 'central capex as-is'), (cases[("central 2022-25 (2021 aberrational)", "capex")][2] * BASE_REV, 'central capex scaled')]:
    for g in (g_sales_22_25,):
        ev_s = pv_growth(c, g, SOV); ev_f = pv_growth(c, g, FLOOR)
        print(f'{lab:22s} growth {100*g:.2f}%: EV@sov {ev_s:.0f} per sh {(ev_s-NET_DEBT)/SHARES:.2f} | EV@10% {ev_f:.0f} per sh {(ev_f-NET_DEBT)/SHARES:.2f}')
