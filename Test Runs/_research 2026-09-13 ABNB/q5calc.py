# ABNB - COMPUTATION, NOT A CLEARANCE (unless Q1-Q4 all IN). Arithmetic only.
CAP = 170.19 * 589585682 / 1e6      # $M
SH = 589.585682                      # M shares
SOV = 0.0535
FLOOR = 0.10
bases = {
  "5y 2020-2024 incl. 2020, D&A end (conservative)": 1118,
  "6y 2020-2025, D&A end":                           1426,
  "5y 2021-2025 ex-2020, float-stripped (OE_C) D&A": 2028,
  "5y 2021-2025 ex-2020, D&A end":                   2485,
  "3y 2023-2025, capex end":                         2938,
  "TTM to 2026-06-30, capex end":                    3120,
}
print("cap $M %.1f" % CAP)
for k, oe in bases.items():
    y = oe / CAP
    g_floor = FLOOR - y          # Gordon: P = OE*(1+g)/(r-g) ~ OE/(r-g) at year-1 earnings
    g_floor_exact = (FLOOR * CAP - oe) / (CAP + oe)
    g_sov_exact = (SOV * CAP - oe) / (CAP + oe)
    print(f"{k}: OE {oe:,}  yield {100*y:.2f}%  pts over sovereign {100*(y-SOV):+.2f}  perpetual g for 10% floor {100*g_floor_exact:.2f}%  for bond {100*g_sov_exact:.2f}%")

print("\nvalue per share at the 10% floor, Gordon OE*(1+g)/(0.10-g)")
for oe in (2028, 2485, 3120):
    row = []
    for g in (0.0, 0.03, 0.05, 0.06, 0.07):
        v = oe * (1 + g) / (FLOOR - g)
        row.append(f"g={int(g*100)}%: ${v/SH:,.0f}")
    print(f" OE {oe:,}: " + "  ".join(row))

# DCF engine (casts no vote): N years at growth G from base, then terminal growth T, discounted at 10%
def dcf(base, G, N, T, r=FLOOR):
    pv = 0.0; oe = base
    for t in range(1, N + 1):
        oe *= (1 + G); pv += oe / (1 + r) ** t
    tv = oe * (1 + T) / (r - T)
    return pv + tv / (1 + r) ** N
print("\nengine: growth needed for 10 years (then 3% terminal) to justify the cap at 10%")
for base in (2485, 3120):
    lo, hi = 0.0, 0.5
    for _ in range(80):
        mid = (lo + hi) / 2
        if dcf(base, mid, 10, 0.03) < CAP: lo = mid
        else: hi = mid
    print(f" base {base:,}: {100*mid:.1f}% a year for 10 years, then 3%")
# steady-state OE implied: price at 10% floor with 3% terminal growth in year 10
for base in (2485, 3120):
    need_oe10 = CAP * (1.10 ** 10) * (FLOOR - 0.03) / 1.03  # ignoring interim cash
    print(f" ignoring interim cash, year-10 OE needed (3% terminal) ~ ${need_oe10:,.0f}M vs base {base:,} -> x{need_oe10/base:.1f}")
# what 2025 revenue growth the price assumes, at the 2025 OE margin
print("\nOE margin on revenue 2025 (D&A end): %.1f%%" % (100 * 2963 / 12241))
