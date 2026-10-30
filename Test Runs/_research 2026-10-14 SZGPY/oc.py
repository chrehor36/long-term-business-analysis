"""Owner-cash arithmetic for the SZGPY run, from the filed consolidated cash flow statements
(EUR m; each year taken from the latest annual report that prints it: AR2017 for 2016-17, AR2019 for 2018-19,
AR2021 for 2020-21, AR2023 for 2022-23, AR2025 for 2024-25). Arithmetic only; no judgment."""

# year: (CFO, capex gross, capex subsidies received, PP&E disposals, interest paid, EBT, D&A incl. impairments)
CF = {
    2016: (290.2, -347.8, 0.0, 2.6, -32.9, 53.2, 332.1),
    2017: (273.7, -296.9, 0.0, 28.5, -33.9, 238.0, 390.4),
    2018: (527.8, -342.5, 0.0, 0.9, -40.5, 347.3, 371.3),
    2019: (250.7, -444.3, 0.0, 11.8, -29.8, -253.3, 541.3),
    2020: (18.3, -374.4, 0.0, 83.3, -26.7, -196.4, 295.2),
    2021: (329.4, -343.4, 0.0, 24.6, -56.7, 705.7, 507.6),
    2022: (596.5, -442.5, 0.0, 11.4, -92.4, 1245.4, 306.0),
    2023: (892.0, -751.8, 202.7, 42.6, -93.8, 238.4, 321.5),
    2024: (408.4, -968.7, 137.6, 18.7, -99.6, -296.2, 623.4),
    2025: (504.6, -1070.3, 370.5, 3.5, -88.2, -27.7, 317.7),
}
MAINT = round((306.0 + 321.5 + 317.7) / 3, 1)  # run CONVENTION: D&A of the three years without large impairments
RATE, FLOOR = 0.0376, 0.10
NET_DEBT = 2334.7 - 1204.1          # H1 2026: financial liabilities less cash and other investments of funds
CO_NET_FIN = 792.2                  # the company's own net financial position (excludes leases etc.)
SHARES = 60.097 - 5.109163          # m shares outstanding at 2026-06-30
PRICE = 47.92

def avg(xs):
    return sum(xs) / len(xs)

allsp = {y: c + k + s + d for y, (c, k, s, d, *_r) in CF.items()}
maint = {y: c - MAINT + d for y, (c, k, s, d, *_r) in CF.items()}
intp = {y: v[4] for y, v in CF.items()}
print("maintenance guess", MAINT)
print("year  all-spending  maintenance-only  interest-paid")
for y in CF:
    print(y, round(allsp[y], 1), round(maint[y], 1), intp[y])
for name, ser in (("all-spending", allsp), ("maintenance", maint)):
    five = avg([ser[y] for y in range(2021, 2026)])
    ten = avg(list(ser.values()))
    h1, h2 = avg([ser[2016 + i] for i in range(5)]), avg([ser[2021 + i] for i in range(5)])
    print(f"{name}: 5y avg {five:.1f}; 10y avg {ten:.1f}; first-half {h1:.1f}; second-half {h2:.1f}")
ten_m, five_m, ten_a = avg(list(maint.values())), avg([maint[y] for y in range(2021, 2026)]), avg(list(allsp.values()))
ten_i = avg(list(intp.values()))
mcap = SHARES * PRICE
print(f"market cap {mcap:.1f}; EV {mcap + NET_DEBT:.1f}; net debt {NET_DEBT:.1f}")
for label, oc in (("central 10y maint", ten_m), ("literal 5y maint", five_m), ("10y all-spending", ten_a)):
    v = oc / RATE
    print(f"{label}: owner cash {oc:.1f}; value at {RATE:.2%} {v:.1f}; less net debt {v - NET_DEBT:.1f}; "
          f"per share {(v - NET_DEBT) / SHARES:.2f}; per ADS {(v - NET_DEBT) / SHARES / 10:.3f}; "
          f"yield on EV {oc / (mcap + NET_DEBT):.2%}")
fair_all = (ten_m / FLOOR - NET_DEBT) / SHARES
fair_eq = ((ten_m + ten_i) / FLOOR) / SHARES
print(f"fair price all-equity {fair_all:.2f} (ADS {fair_all/10:.3f}); equity-only {fair_eq:.2f} (ADS {fair_eq/10:.3f}); "
      f"10y avg interest paid {ten_i:.1f}; equity-only yield {(ten_m + ten_i) / mcap:.2%}")
print(f"company-basis net debt variant: per share {(ten_m / RATE - CO_NET_FIN) / SHARES:.2f}; "
      f"fair {(ten_m / FLOOR - CO_NET_FIN) / SHARES:.2f}")
