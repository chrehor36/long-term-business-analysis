# DSGR run 2026-10-12: Q7 arithmetic, COMPUTATION, NOT A CLEARANCE (the file closed at Q2).
# Every input is a filed figure (USD thousands), source in the comment; no projection is used.
# Range by the Q7 range convention of THE FRAMEWORK v5: five-year average of owner cash after every
# real cost, carried ten years at the growth shown (capped), then zero nominal growth, at the long
# government rate; acquisitions deducted with total growth credited (default), organic pair beside;
# a merger inside the window (April 1, 2022) valued on the combined companies' own averages.
# Fair price (Part VII): each end case valued at 10 percent, the two averaged, per share.

SOV = 0.0560          # US Treasury 30-year par yield, 10/09/2026 (tools/sources.py)
FLOOR = 0.10
PRICE = 35.03         # close 2026-10-09, aggregator via tools/run.py (live quote only, flagged)
SHARES = 46_255_422   # 10-Q cover, 0000703604-26-000041, as of 2026-07-31
# net debt at 2026-06-30 (10-Q 0000703604-26-000041): total debt 733,772 + finance leases 603 + 775
# less cash and cash equivalents 66,938 (restricted cash 8,542 left out: collateral and escrow)
NET_DEBT = 733_772 + 603 + 775 - 66_938
T_INT = 0.25          # CONVENTION of this run: interest added back after a 25% shield (21% federal + state)

# combined companies, FY2021 to FY2025 (thousands)
# 2021: TestEquity+Gexpro as reported in FY2022 10-K (0000703604-23-000033) + Lawson Products FY2021 10-K (0000703604-22-000019)
# 2022: DSG as reported (0000703604-23-000033) + Lawson Q1 2022 10-Q (0000703604-22-000027)
# 2023-2025: FY2025 10-K (0000703604-26-000008) and FY2024 10-K (0000703604-25-000012)
Y = {
 # year: (OCF, stock pay (negative benefit not credited), PP&E, rental, proceeds rental, proceeds PP&E, acquisitions, interest paid)
 2021: (10_320 + 5_449, 0 + 4_838, 3_026 + 8_193, 10_755, 6_341, 0, 33_936 + 33_000, 15_395 + 968),
 2022: (-11_029 - 211, 2_448 + 0, 8_307 + 2_057, 11_794, 8_756, 0, 115_343 + 9_757, 22_153 + 98),
 2023: (102_286, 7_940 + 427, 15_337, 9_341, 5_990, 0, 259_835 + 1_000, 38_048 + 2_581),
 2024: (56_453, 5_233, 13_684, 9_509, 5_124, 3_662, 199_423 + 15_853, 52_905 + 2_889),
 2025: (83_849, 6_672, 21_015, 19_480, 12_749, 990, 2_176, 51_872 + 2_725),
}
# literal window: 2021 and 2022 as reported, without the Lawson additions
LIT = dict(Y)
LIT[2021] = (10_320, 0, 3_026, 10_755, 6_341, 0, 33_936, 15_395)
LIT[2022] = (-11_029, 2_448, 8_307, 11_794, 8_756, 0, 115_343 + 9_757, 22_153)

def rows(d):
    out = {}
    for y, (ocf, sbc, ppe, rent, prr, prp, acq, intp) in sorted(d.items()):
        capex = ppe + rent - prr - prp
        eq = ocf - sbc - capex                 # owner cash after interest, before acquisitions
        ae = eq + intp * (1 - T_INT)           # all-equity: before interest, after the company's tax
        out[y] = dict(capex=capex, eq=eq, ae=ae, eq_acq=eq - acq, ae_acq=ae - acq, acq=acq)
    return out

def pv(base, g, r, after=None):
    """ten years at g from base, then zero nominal growth on `after` (defaults to the year-10 figure)"""
    v, c = 0.0, base
    for t in range(1, 11):
        c = c * (1 + g); v += c / (1 + r) ** t
    tail = c if after is None else after
    return v + (tail / r) / (1 + r) ** 10

def irr(base, g, ev, after=None):
    lo, hi = 0.0001, 1.0
    if pv(base, g, 0.0001, after) < ev: return None
    for _ in range(200):
        m = (lo + hi) / 2
        (lo, hi) = (m, hi) if pv(base, g, m, after) > ev else (lo, m)
    return m

def ps(x): return x / SHARES * 1000

def show(label, d):
    R = rows(d)
    print('\n' + label)
    print('  year   net capex   eq-before-acq   AE-before-acq    acquisitions   AE-after-acq   eq-after-acq')
    for y, x in R.items():
        print('  %d  %9.1f  %14.1f  %14.1f  %14.1f  %13.1f  %13.1f' % (y, x['capex']/1e3, x['eq']/1e3, x['ae']/1e3, x['acq']/1e3, x['ae_acq']/1e3, x['eq_acq']/1e3))
    avg = {k: sum(R[y][k] for y in R) / len(R) for k in ('eq', 'ae', 'eq_acq', 'ae_acq')}
    print('  five-year averages (USD M): eq %.1f  AE %.1f  AE after acq %.1f  eq after acq %.1f' % tuple(avg[k]/1e3 for k in ('eq', 'ae', 'ae_acq', 'eq_acq')))
    return R, avg

R, A = show('COMBINED COMPANIES (the merger rule), FY2021-FY2025', Y)
RL, AL = show('LITERAL WINDOW (as reported), FY2021-FY2025', LIT)

EV_PRICE = PRICE * SHARES / 1000 + NET_DEBT
MCAP = PRICE * SHARES / 1000
print('\nmarket value %.1fM; net debt at 2026-06-30 %.1fM; value at the price (all-equity) %.1fM' % (MCAP/1e3, NET_DEBT/1e3, EV_PRICE/1e3))

# growth shown: owner cash changes sign inside the window (both series), halves meaningless -> no-growth alone
# (specific (b)). Organic growth as the filer reports it: 2024 -34.5M on 1,570.4M; 2025 +54.4M on 1,804.1M.
g_org = ((1 - 34_500 / 1_570_402) * (1 + 54_400 / 1_804_104)) ** 0.5 - 1
print('organic growth reported (2024, 2025), compound per year: %.2f%%' % (100 * g_org))

def case(label, base, g, after=None, eq_only=False):
    debt = 0 if eq_only else NET_DEBT
    v_s = pv(base, g, SOV, after) - debt
    v_f = pv(base, g, FLOOR, after) - debt
    ev = MCAP if eq_only else EV_PRICE
    r = irr(base, g, ev, after)
    print('  %-58s at %.2f%%: %8.1fM  $%7.2f/sh | at 10%%: %8.1fM  $%7.2f/sh | return at price: %s' % (
        label, 100*SOV, v_s/1e3, ps(v_s), v_f/1e3, ps(v_f), ('%.1f%%' % (100*r)) if r is not None else 'none (value below price at any rate)'))
    return ps(v_s), ps(v_f)

print('\nDEFAULT PAIR, acquisitions deducted, total growth credited (no-growth alone, specific (b)); after year 10 the purchases stop (owner cash before purchases, no growth)')
d_s, d_f = case('all-equity, combined', A['ae_acq'], 0.0, after=A['ae'])
case('all-equity, literal window', AL['ae_acq'], 0.0, after=AL['ae'])
case('equity-only, combined', A['eq_acq'], 0.0, after=A['eq'], eq_only=True)
print('\nORGANIC PAIR beside, acquisitions left out, organic growth as reported')
o0s, o0f = case('all-equity, no growth', A['ae'], 0.0)
o1s, o1f = case('all-equity, organic growth %.2f%%' % (100*g_org), A['ae'], g_org)
e0s, e0f = case('equity-only, no growth', A['eq'], 0.0, eq_only=True)
e1s, e1f = case('equity-only, organic growth', A['eq'], g_org, eq_only=True)
case('all-equity, literal window, no growth', AL['ae'], 0.0)
print('\nSENSITIVITY, not a convention case: the three best years only (2023-2025), acquisitions left out')
b = sum(R[y]['ae'] for y in (2023, 2024, 2025)) / 3
case('all-equity, 2023-2025 average %.1fM, no growth' % (b/1e3), b, 0.0)
case('all-equity, 2023-2025 average, Hisco retention 34.6M added back to 2024', b + 34_600/3, 0.0)

print('\nREPORTING FIGURES')
print('  value range, default pair (central): no-growth case alone, $%.2f a share all-equity' % d_s)
print('  value range, organic pair beside: $%.2f to $%.2f a share all-equity; equity-only $%.2f to $%.2f' % (o0s, o1s, e0s, e1s))
print('  fair price, default pair: $%.2f a share all-equity (not positive)' % d_f)
print('  fair price, organic pair: $%.2f all-equity (average of the two ends at 10%%); equity-only $%.2f' % ((o0f + o1f)/2, (e0f + e1f)/2))
print('  price $%.2f' % PRICE)
