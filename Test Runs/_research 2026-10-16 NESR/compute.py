# COMPUTATION, NOT A CLEARANCE. Figures in US$ millions from the filed cash-flow statements:
# FY2025 10-K 0001493152-26-009139 (2023-2025); FY2023 20-F 0001493152-24-017128 (2021-2023); FY2022 20-F 0001493152-23-046470 (2020 restated)
Y = [2021, 2022, 2023, 2024, 2025]
OCF   = [127.743, 92.576, 176.959, 229.329, 264.242]
SBC   = [9.759, 9.269, 6.763, 6.032, 8.321]
CAPEX = [107.076, 122.415, 68.190, 105.105, 143.454]
IPM   = [0, 17.367, 16.031, 0, 0]
OTHINV= [8.299, 7.552, 1.000, 9.087, 13.689]
DISP  = [2.760, 0.626, 1.758, 3.058, 4.905]
FLEASE= [21.361, 3.108, 2.403, 3.193, 3.905]
SELLER= [15.333, 14.443, 15.569, 3.781, 7.408]
ACQ   = [51.921, 0, 0, 0, 0]
INTPD = [9.890, 19.236, 33.914, 38.306, 28.481]
DA    = [122.125, 115.845, 142.230, 142.784, 141.729]
AMORT = [18.042, 18.865, 18.774, 18.774, 18.774]
APCHG = [31.221, 33.651, -3.365, -38.517, 116.160]
REV   = [876.729, 909.517, 1145.915, 1301.704, 1324.047]
T = 0.20   # CONVENTION of the run: tax shield on interest at 20%
R = 0.0543; F = 0.10
SH = 100.851754; PRICE = 19.11
# net debt 2026-06-30 (10-Q 0001493152-26-036720): LTD current 64.500 + ST 50.415 + LTD 159.706 - cash 174.994
ND = 64.500 + 50.415 + 159.706 - 174.994
dep = [d - a for d, a in zip(DA, AMORT)]
allsp = [o - s - c - i - oi + dp - fl - se - aq for o, s, c, i, oi, dp, fl, se, aq in zip(OCF, SBC, CAPEX, IPM, OTHINV, DISP, FLEASE, SELLER, ACQ)]
maint = [o - s - d - oi + dp for o, s, d, oi, dp in zip(OCF, SBC, dep, OTHINV, DISP)]
unl = lambda xs: [x + i * (1 - T) for x, i in zip(xs, INTPD)]
avg = lambda xs: sum(xs) / len(xs)
print("year      " + " ".join(f"{y:>8}" for y in Y))
for name, xs in [("all-sp eq", allsp), ("maint eq", maint), ("all-sp unl", unl(allsp)), ("maint unl", unl(maint)), ("depr", dep), ("AP change", APCHG)]:
    print(f"{name:10}" + " ".join(f"{x:8.1f}" for x in xs) + f"   avg {avg(xs):7.1f}")
print("net debt 2026-06-30", round(ND, 1), " market cap", round(SH * PRICE, 1), " EV", round(SH * PRICE + ND, 1))
for label, base_unl, base_eq in [("bottom: all spending, no growth", avg(unl(allsp)), avg(allsp)),
                                 ("top: maintenance only, no growth", avg(unl(maint)), avg(maint))]:
    ev = base_unl / R; ev10 = base_unl / F
    print(f"{label}: base unl {base_unl:.1f}  EV@sov {ev:.0f}  per sh all-equity {(ev-ND)/SH:.2f}  | equity-only {base_eq/R/SH:.2f}  | @10% all-eq {(ev10-ND)/SH:.2f} eq-only {base_eq/F/SH:.2f}  | yield on EV at price {100*base_unl/(SH*PRICE+ND):.2f}%")
b, t = avg(unl(allsp)), avg(unl(maint))
print("fair all-equity", round(((b / F + t / F) / 2 - ND) / SH, 2), " fair equity-only", round((avg(allsp) / F + avg(maint) / F) / 2 / SH, 2))
print("width top/bottom", round((t / R - ND) / ((b / R) - ND), 2), "(per share);", round(t / b, 2), "(whole business)")
# beside: 2025 AP inflow removed (working-capital draw the filer ties to payment timing)
allsp2 = allsp[:]; allsp2[4] -= APCHG[4]; maint2 = maint[:]; maint2[4] -= APCHG[4]
b2, t2 = avg(unl(allsp2)), avg(unl(maint2))
print("beside, 2025 AP increase removed: bottom per sh", round((b2 / R - ND) / SH, 2), " top per sh", round((t2 / R - ND) / SH, 2), " fair", round(((b2 / F + t2 / F) / 2 - ND) / SH, 2))
# growth test: halves of the window
for name, xs in [("all-sp unl", unl(allsp)), ("maint unl", unl(maint))]:
    print(name, "first half (2021-22) avg", round(avg(xs[:2]), 1), " second half (2024-25) avg", round(avg(xs[3:]), 1))
print("sales CAGR 2021-2025", round(100 * ((REV[-1] / REV[0]) ** 0.25 - 1), 1), "%")
# what growth would the price need: maintenance case, g for ten years then zero, at the floor 10%
def val(base, g, r, yrs=10):
    v = 0; c = base
    for k in range(1, yrs + 1):
        c *= (1 + g); v += c / (1 + r) ** k
    return v + c / r / (1 + r) ** yrs
ev_mkt = SH * PRICE + ND
for g in [0.0, 0.05, 0.109, 0.20]:
    print(f"maint unl at g={g:.3f} for ten years: value@10% {val(t, g, F):.0f} vs EV {ev_mkt:.0f}; value@sov {val(t, g, R):.0f}")
# beside: six-year span 2020-2025 (2020 as restated, FY2022 20-F 0001493152-23-046470)
o20, s20, c20, oi20, dp20, fl20, se20, aq20, i20 = 134.453, 7.832, 82.632, 1.074, 0.487, 19.581, 3.834, 13.218, 13.051
dep20 = 121.0 - 15.817  # D&A 2020 restated (tagged DepreciationDepletionAndAmortization 121) less amortization 15.817
a20 = o20 - s20 - c20 - oi20 + dp20 - fl20 - se20 - aq20
m20 = o20 - s20 - dep20 - oi20 + dp20
A6 = [a20] + allsp; M6 = [m20] + maint; I6 = [i20] + INTPD
bu = avg([x + i * (1 - T) for x, i in zip(A6, I6)]); tu = avg([x + i * (1 - T) for x, i in zip(M6, I6)])
print("beside, 2020-2025: 2020 all-sp eq", round(a20, 1), "maint eq", round(m20, 1), "| bottom per sh", round((bu / R - ND) / SH, 2), "top per sh", round((tu / R - ND) / SH, 2), "fair", round(((bu / F + tu / F) / 2 - ND) / SH, 2))
