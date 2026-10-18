# COMPUTATION, NOT A CLEARANCE. INVX owner cash and the Q7 range, from the filed statements (USD millions).
T = 0.21   # US statutory rate, used only to put interest after tax for the all-equity add-back
r_gov = 0.0543; floor = 0.10
shares = 69.935827; price = 27.39
# rows: OCF, deferred-tax adjustment in OCF (D; OCF - D charges book tax as if paid), SBC, capex, finance-lease principal, interest paid
legacy = {2021: (-2.025, 0.0, 0.703, 6.443, 0.0, 1.638),      # 424B3 F-7
          2022: (-5.811, -6.711, 0.907, 9.575, 2.432, 3.148),  # 424B3 F-7 / 10-K FY2024 F-9
          2023: (75.864, -7.406, 1.962, 15.487, 3.865, 5.747)} # 424B3 F-7 / 10-K FY2025 F-8
drq = {2021: (38.428, -8.701, 14.895, 9.990, 0.1, 0.0),          # Dril-Quip 10-K FY2023 p.59; fin lease 0.1 per run.py
       2022: (-36.771, 6.401, 10.363, 18.866, 0.0, 0.0),
       2023: (7.727, -2.867, 10.892, 32.626, 0.0, 0.0)}
combined = {2024: (93.439, -4.595, 13.248, 13.594, 5.698, 1.991),   # 10-K FY2025 F-8
            2025: (190.912, 34.291, 13.798, 35.132, 7.535, 1.023)}
drq_h1_2024 = (-13.408, -4.097, 6.166, 10.913, 0.0, 0.0)           # Dril-Quip 10-Q Q2 2024
def oc(row, equity_only=False):
    ocf, d, sbc, capex, fl, intp = row
    v = ocf - d - sbc - capex - fl
    return v if equity_only else v + intp * (1 - T)
years = [2021, 2022, 2023, 2024, 2025]
gap = 67 / 182   # CONVENTION of this run: Dril-Quip 2024-07-01 to 2024-09-05 prorated from H1 2024
res = {}
for eo in (False, True):
    s = {}
    for y in years:
        if y <= 2023:
            s[y] = oc(legacy[y], eo) + oc(drq[y], eo)
        else:
            s[y] = oc(combined[y], eo)
            if y == 2024:
                s[y] += oc(drq_h1_2024, eo) * (1 + gap)
    res[eo] = s
for eo, s in res.items():
    print("equity-only" if eo else "all-equity", {y: round(v, 1) for y, v in s.items()}, "avg", round(sum(s.values()) / 5, 1))
# acquisitions, cash paid for businesses net of cash acquired
acq = {2021: 22.200, 2022: 28.914, 2023: 18.350 + 82.287, 2024: 65.521, 2025: 83.668}
A = sum(acq.values()); OCsum = sum(res[False].values())
print("net purchases", round(A, 1), "owner cash before purchases", round(OCsum, 1), "serial?", A > OCsum / 2)
print("default pair avg owner cash after purchases", round((OCsum - A) / 5, 1))
first = (res[False][2021] + res[False][2022]) / 2; second = (res[False][2024] + res[False][2025]) / 2
print("halves", round(first, 1), round(second, 1))
tco = 11.0   # TCO 8-K 2026-06-15: "Free Cash Flow of $11 million" (CFO $12M less capex $0.2M, as rounded by the filer); the lower figure used
base = sum(res[False].values()) / 5 + tco
base_eo = sum(res[True].values()) / 5 + tco
debt = 25.1; cash = 222.1; tco_cash = 65.0; legal = 51.607; dis_earnout = 4.0
net_cash = cash - debt - tco_cash          # net debt at 2026-06-30 plus the TCO cash paid 2026-07-01 (filed subsequent event)
claims = legal + dis_earnout
# shelter: CONVENTION of this run, the net deferred tax asset at 2025-12-31 used evenly over four years, PV at the long rate
dta = 102.375; yrs = 4
shelter = dta / yrs * (1 - (1 + r_gov) ** -yrs) / r_gov
print("net cash", round(net_cash, 1), "claims", round(claims, 1), "shelter PV", round(shelter, 1))
def val(oc_, rate):  # no-growth case: level owner cash forever, zero nominal growth
    return oc_ / rate
for label, b in (("organic pair, no-growth (central)", base), ("since-merger beside: 2025 + TCO", res[False][2025] + tco)):
    ev = val(b, r_gov); eq = ev + net_cash - claims + shelter
    fair = val(b, floor) + net_cash - claims + shelter
    print(label, "base", round(b, 1), "value/sh", round(eq / shares, 2), "fair/sh", round(fair / shares, 2),
          "yield at price on EV", round(100 * b / (price * shares - net_cash + claims - shelter), 2), "%")
eo_val = val(base_eo, r_gov) - claims + shelter; eo_fair = val(base_eo, floor) - claims + shelter
print("equity-only: base", round(base_eo, 1), "value/sh", round(eo_val / shares, 2), "fair/sh", round(eo_fair / shares, 2),
      "yield on market cap", round(100 * base_eo / (price * shares), 2), "%")
# literal window, no TCO, beside
b0 = sum(res[False].values()) / 5
print("literal window without TCO: value/sh", round((val(b0, r_gov) + cash - debt - claims + shelter) / shares, 2))
