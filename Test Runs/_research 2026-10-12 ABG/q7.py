# ABG owner cash recast and Q7 arithmetic. Arithmetic only; every input is from a filed statement (accessions in the run file).
# USD millions. Floor-plan notes are treated as operating (the filer's adjusted operating cash flow); see run file Q4.
T = 0.25            # CONVENTION of this run: tax rate for the after-tax add-back of other interest (filer's effective 24.8-25.7% 2023-2025)
R = 0.056           # sovereign, US Treasury 30y par, 2026-10-09
F = 0.10            # floor, Q7 CONVENTION
SH = 17.951917      # cover shares, 10-Q 2026-06-30
PRICE = 165.28
yrs = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
adjcfo = {2019: 282.3, 2020: 442.6, 2021: 632.1, 2022: 987.0, 2023: 705.3, 2024: 688.4, 2025: 651.4}   # filer's reconciliations
cfo    = {2019: 349.8, 2020: 652.5, 2021: 1163.7, 2022: 696.0, 2023: 313.0, 2024: 671.2, 2025: 775.2}
sbc    = {2019: 12.5, 2020: 12.6, 2021: 16.2, 2022: 20.6, 2023: 23.5, 2024: 26.7, 2025: 27.7}
capex  = {2019: 57.6 + 9.2 + 4.9, 2020: 46.5 + 2.3, 2021: 74.2 + 7.8 + 217.1, 2022: 94.6 + 13.3, 2023: 142.3,
          2024: 162.6 + 145.6 + 11.9, 2025: 186.0 + 19.3}                    # ex-real-estate + real estate + leased property bought
capex_ex_re = {2019: 57.6, 2020: 46.5, 2021: 74.2, 2022: 94.6, 2023: 142.3, 2024: 162.6, 2025: 186.0}
dna    = {2019: 36.2, 2020: 38.5, 2021: 41.9, 2022: 69.0, 2023: 67.7, 2024: 75.0, 2025: 82.4}
oint   = {2019: 54.9, 2020: 56.7, 2021: 93.9, 2022: 152.2, 2023: 156.1, 2024: 179.1, 2025: 187.5}
acq    = {2019: 210.0, 2020: 954.1, 2021: 3660.4, 2022: 5.0, 2023: 1500.0, 2024: 4.7, 2025: 1761.8}
fp_acq = {2019: 55.3, 2020: 131.6, 2021: 214.5, 2022: 0.0, 2023: 256.1, 2024: 0.0, 2025: 262.7}
div    = {2019: 39.1, 2020: 177.9, 2021: 21.3, 2022: 701.2, 2023: 30.7, 2024: 196.3, 2025: 566.5}
fp_div = {2019: 14.1, 2020: 60.4, 2021: 0.8, 2022: 48.4, 2023: 0.0, 2024: 34.1, 2025: 90.7}
rev    = {2019: 7210.0, 2020: 7132.0, 2021: 9838.0, 2022: 15434.0, 2023: 14802.7, 2024: 17188.6, 2025: 17999.0}

ocb, oce, netacq, ocafter = {}, {}, {}, {}
print("year  adjCFO   SBC  capex  int*(1-t)  OC_before_acq(all-equity)  OC_equity  net_acq  OC_after_acq  OC/rev")
for y in yrs:
    ocb[y] = adjcfo[y] - sbc[y] - capex[y] + oint[y] * (1 - T)
    oce[y] = adjcfo[y] - sbc[y] - capex[y]
    netacq[y] = (acq[y] - fp_acq[y]) - (div[y] - fp_div[y])
    ocafter[y] = ocb[y] - netacq[y]
    print(f"{y} {adjcfo[y]:7.1f} {sbc[y]:5.1f} {capex[y]:6.1f} {oint[y]*(1-T):8.1f} {ocb[y]:10.1f} {oce[y]:10.1f} {netacq[y]:9.1f} {ocafter[y]:9.1f} {ocb[y]/rev[y]*100:6.2f}%")
avg = lambda d, ys: sum(d[y] for y in ys) / len(ys)
W = [2021, 2022, 2023, 2024, 2025]; C = [2019, 2020, 2021, 2022, 2023, 2024]
print("\nliteral window 2021-2025: OC_before avg %.1f  OC_equity avg %.1f  net acq avg %.1f  OC_after avg %.1f" % (avg(ocb, W), avg(oce, W), avg(netacq, W), avg(ocafter, W)))
print("cycle 2019-2024 (trough to trough): OC_before avg %.1f  OC_equity avg %.1f  net acq avg %.1f  OC_after avg %.1f" % (avg(ocb, C), avg(oce, C), avg(netacq, C), avg(ocafter, C)))
print("capex vs D&A 2025: %.1f vs %.1f ; ex-RE capex vs D&A: %.1f" % (capex[2025], dna[2025], capex_ex_re[2025]))

# net debt, all-equity basis, latest filed balance sheet 2026-06-30 (10-Q): debt current 447.7 + long-term 3,010.0; cash 30.4 + short-term investments 5.3
ND = 447.7 + 3010.0 - 30.4 - 5.3
FP = 300.7 + 1538.8   # floor plan, trade + non-trade (left with inventory; shown beside)
MC = PRICE * SH
EV = MC + ND
print(f"\nmarket cap {MC:.1f}  net debt {ND:.1f}  EV {EV:.1f}  floor plan beside {FP:.1f}")

def value(base_years1_10, growth, rate, after10, g_after=0.0):
    """PV of a 10-year stream starting at base*(1+g) in year 1, then after10 cash (at year-10 level for before-purchase stream) flat forever."""
    pv = 0.0; c = base_years1_10
    for t in range(1, 11):
        c = c * (1 + growth) if t > 1 or True else c
        pv += c / (1 + rate) ** t
    tv = after10 / rate / (1 + rate) ** 10
    return pv + tv

def case(name, base_after, base_before, g, rate):
    # years 1-10: base_after grown at g; after year 10: base_before grown 10 years at g, then flat (purchases stop)
    pv = sum(base_after * (1 + g) ** t / (1 + rate) ** t for t in range(1, 11))
    term = base_before * (1 + g) ** 10
    pv += term / rate / (1 + rate) ** 10
    eq = pv - ND
    return eq, eq / SH

for label, ys in (("CYCLE 2019-2024 (central base)", C), ("LITERAL WINDOW 2021-2025 (beside)", W)):
    b_before = avg(ocb, ys); b_after = avg(ocafter, ys)
    print(f"\n== {label}")
    # default pair: acquisitions deducted, total growth credited; after-acquisition series changes sign -> growth meaningless -> no-growth alone
    for rate in (R, F):
        eq, ps = case("default", b_after, b_before, 0.0, rate)
        print(f"default pair (acq deducted, no-growth alone) @ {rate*100:.1f}%: equity {eq:8.1f}  per share {ps:8.2f}")
    # organic pair: acquisitions left out; organic growth carried at zero (top) and negative (bottom, see run file)
    for g in (0.0, -0.02):
        for rate in (R, F):
            eq, ps = case("organic", b_before, b_before, g, rate)
            print(f"organic pair g={g*100:+.0f}% @ {rate*100:.1f}%: equity {eq:8.1f}  per share {ps:8.2f}")
    # equity-only beside: owner cash after interest against market cap, no growth
    be = avg(oce, ys)
    print(f"equity-only beside: owner cash after interest {be:.1f}; at {R*100:.1f}% value {be/R:.0f} = {be/R/SH:.2f}/sh; at 10% {be/F:.0f} = {be/F/SH:.2f}/sh; yield at price {be/MC*100:.2f}%")
    print(f"all-equity yield at price, no growth: {b_before/EV*100:.2f}%  (floor ~10%)")

# the floor: owner cash needed at no growth for the price to earn 10% on the all-equity basis
print(f"\nowner cash needed at no growth to earn 10% at the price: {EV*F:.1f}")
# implied organic growth needed for the organic pair to clear 10% at the price (10-year growth then flat)
lo, hi = -0.1, 0.3
b = avg(ocb, C)
for _ in range(60):
    mid = (lo + hi) / 2
    eq, ps = case("x", b, b, mid, F)
    if ps < PRICE: lo = mid
    else: hi = mid
print(f"growth for 10 years needed for the cycle-base organic case valued at 10% to reach the price: {mid*100:.2f}% a year")
# revenue growth 2019-2025 (total) and buybacks
print("revenue CAGR 2019-2025: %.1f%%" % ((rev[2025] / rev[2019]) ** (1 / 6) * 100 - 100))
print("OC_before CAGR 2019-2025: %.1f%%" % ((ocb[2025] / ocb[2019]) ** (1 / 6) * 100 - 100))

# --- beside: depreciation variant (D&A in place of all capital spending), and floor-plan notes counted in net debt
print("\n== BESIDE")
for label, ys in (("cycle 2019-2024", C), ("window 2021-2025", W)):
    b = avg(ocb, ys); dav = b + avg(capex, ys) - avg(dna, ys)
    for rate in (R, F):
        print(f"{label}: D&A variant base {dav:.1f} @ {rate*100:.1f}%: per share {(dav/rate-ND)/SH:8.2f} ; organic with floor plan in net debt: {(b/rate-ND-FP)/SH:8.2f}")
print("same-share check: fair price central (default pair) not positive -> alert on organic pair (Q7 (c), 2026-10-10)")
