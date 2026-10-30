"""XEL Q7 arithmetic. COMPUTATION, NOT A CLEARANCE (file closed at Q5). USD millions.
Sources: 10-K FY2025 0000072903-26-000009 (2023-2025), 10-K FY2022 0000072903-23-000007 (2021-2022 cash-flow lines),
10-Q Q2 2026 0000072903-26-000154 (balance sheet 2026-06-30), cover 624,634,306 shares."""
yrs   = [2021, 2022, 2023, 2024, 2025]
ocf   = [2189, 3932, 5327, 4641, 4083]
sbc   = [31, 20, 25, 33, 46]
capex = [4244, 4638, 5854, 7364, 10908]
da    = [2143, 2436, 2471, 2769, 2968]
nfa   = [114, 118, 96, 106, 114]          # nuclear fuel amortization (nuclear fuel sits in PP&E, bought inside capex)
intp  = [788, 887, 945, 1131, 1262]       # cash interest paid, net of capitalized
rev   = [13431, 15310, 14206, 13441, 14669]
rev2020 = 11526
SH = 624.634; PRICE = 77.86; R = 0.0531; FLOOR = 0.10
maint = [d + n for d, n in zip(da, nfa)]
oc_m  = [o - s - m for o, s, m in zip(ocf, sbc, maint)]          # owner cash after maintenance only (after interest, after tax)
oc_all= [o - s - c for o, s, c in zip(ocf, sbc, capex)]          # owner cash after all spending
grow  = [c - m for c, m in zip(capex, maint)]                    # growth spending
avg = lambda x: sum(x) / len(x)
B, G, A = avg(oc_m), avg(grow), avg(oc_all)
print("year  OCF  SBC  capex  maint  OC_maint  OC_all  growthspend  OC_maint/sales")
for i, y in enumerate(yrs):
    print(y, ocf[i], sbc[i], capex[i], maint[i], oc_m[i], oc_all[i], grow[i], f"{oc_m[i]/rev[i]:.1%}")
print(f"5-yr avg: OC_maint {B:.0f}  OC_all {A:.0f}  growth spending {G:.0f}  interest {avg(intp):.0f}")
# growth shown: halves (b), end years meaningless (2021 aberrational, Uri deferral)
h1, h2 = avg(oc_m[:2]), avg(oc_m[3:])
g_shown = (h2 / h1) ** (1 / 3) - 1
g_sales = (rev[-1] / rev[0]) ** (1 / 4) - 1
g_sales20 = (rev[-1] / rev2020) ** (1 / 5) - 1
print(f"halves {h1:.0f} -> {h2:.0f}: shown growth {g_shown:.1%}; ten years -> {B*(1+g_shown)**10:.0f} vs highest share of sales {max(o/r for o,r in zip(oc_m,rev)):.1%}")
print(f"sales growth 2021-2025 {g_sales:.2%}; 2020-2025 {g_sales20:.2%}")
# debt credit (utility rule): LT debt incl current maturities and finance leases, end-2020 to end-2025
lt2020 = 19645 + 421 + 77
lt2025 = 31832 + 501 + 1301
dinc = (lt2025 - lt2020) / 5
dinc_nolease = ((31832 + 501 + 1301 - 1239) - lt2020) / 5     # beside: 2025 non-cash finance lease addition left out
CAP = 0.466
print(f"LT debt end-2020 {lt2020}, end-2025 {lt2025}, increase/yr {dinc:.0f} (without the 2025 lease addition {dinc_nolease:.0f})")
def value(base, gsp, credit, g, r, years=10):
    pv = 0.0
    for t in range(1, years + 1):
        cf = base * (1 + g) ** t - gsp * (1 + g) ** (t - 1) + credit * (1 + g) ** (t - 1)
        pv += cf / (1 + r) ** t
    term = base * (1 + g) ** years / r / (1 + r) ** years
    return pv + term
def case_table(base, gsp, cap_share, g, label, debt_avg=dinc):
    credit = min(debt_avg, cap_share * gsp)
    ng  = base / R
    gr  = value(base, gsp, credit, g, R)
    ng10, gr10 = base / FLOOR, value(base, gsp, credit, g, FLOOR)
    lo, hi = sorted([ng, gr])
    fair = (ng10 + gr10) / 2 / SH
    print(f"[{label}] g={g:.2%} credit/yr={credit:.0f}  no-growth ${ng/SH:.2f}  growth ${gr/SH:.2f}  range ${lo/SH:.2f}-${hi/SH:.2f}  "
          f"@10%: ng ${ng10/SH:.2f} gr ${gr10/SH:.2f}  FAIR ${fair:.2f}  price ${PRICE}")
    # expected return at price, no-growth case (perpetuity yield)
    return lo / SH, hi / SH, fair
print("\nEQUITY-ONLY (central for a regulated utility), maintenance case central:")
c = case_table(B, G, CAP, g_sales, "central: sales-growth cap 2021-25, cap 46.6%")
case_table(B, G, CAP, g_sales20, "beside: sales growth 2020-25")
case_table(B, G, CAP, 0.06, "beside: 6% (ongoing EPS objective low end, management's figure, not the rule)")
case_table(B, G, 0.614, g_sales, "beside: cap at own LT debt share 61.4%")
case_table(B, G, CAP, g_sales, "beside: credit without the 2025 lease addition", debt_avg=dinc_nolease)
print(f"no-growth yield at price: {B/(PRICE*SH):.2%} (floor ~10%)")
print(f"all-spending case: avg owner cash {A:.0f}/yr -> value negative; per share {A/R/SH:.2f}")
# literal window base without the aberrational 2021 (beside)
B4 = avg(oc_m[1:]); G4 = avg(grow[1:])
case_table(B4, G4, CAP, (rev[-1]/rev[1])**(1/3)-1 if rev[-1]>rev[1] else 0.0, "beside: 2022-2025 base (2021 left out)")
# ALL-EQUITY beside: before interest, after tax at 21% shield; net debt 2026-06-30
TAXSH = 0.21
Bu = B + avg(intp) * (1 - TAXSH)
nd = 35948 + 999 + 2510 + 1288 + 39 - 2010
for g, lab in ((0.0, "no-growth"),):
    ev = Bu / R
    print(f"\nALL-EQUITY beside: unlevered maint owner cash {Bu:.0f}; EV no-growth {ev:.0f}; net debt {nd}; per share ${(ev-nd)/SH:.2f}")
evg = value(Bu, G, 0, g_sales, R)
print(f"ALL-EQUITY growth case (all growth spending, no credit): per share ${(evg-nd)/SH:.2f}")
fa = ((Bu/FLOOR - nd) + (value(Bu, G, 0, g_sales, FLOOR) - nd)) / 2 / SH
print(f"ALL-EQUITY fair price: ${fa:.2f}")
