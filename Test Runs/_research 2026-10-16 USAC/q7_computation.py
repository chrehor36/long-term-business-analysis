"""COMPUTATION, NOT A CLEARANCE. Q7's range convention for USAC, 2026-10-16. Arithmetic only; inputs from returns_output.txt
and the filings named in the run file. $M except per-unit figures."""
R = 0.0543          # 30-year US Treasury par yield, 2026-10-15
FLOOR = 0.10        # the floor CONVENTION, about ten percent
UNITS = 144.943345  # millions, 10-Q cover 2026-07-31
NET_DEBT = 2950.5   # principal 2,960.0 less cash 9.5, 2026-06-30
PRICE = 24.88
EV = PRICE * UNITS + NET_DEBT

ae = {2019: 250.8, 2020: 300.3, 2021: 331.4, 2022: 243.8, 2023: 180.6, 2024: 276.9, 2025: 456.4}   # all-equity owner cash
eq = {2019: 145.4, 2020: 179.6, 2021: 210.8, 2022: 114.8, 2023: 17.0, 2024: 122.6, 2025: 275.1}    # equity-only (window interest)
JW = 105.669 + 17.234 - 78.223 + 3.478   # J-W year to 2025-10-31: OCF + interest paid - capex + disposal proceeds, after its own tax
INTEREST_NOW = 0.61e3 * 0.0574 + 1000 * 0.07125 + 750 * 0.0625 + 600 * 0.0675  # today's debt at its coupons (revolver after the 2035 notes)

def value(oc, g, r, years=10):
    """PV of oc growing at g for `years`, then zero growth forever, discounted at r."""
    pv, c = 0.0, oc
    for t in range(1, years + 1):
        c *= (1 + g)
        pv += c / (1 + r) ** t
    return pv + (c / r) / (1 + r) ** years

def irr(oc, g, target):
    lo, hi = 0.0001, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(oc, g, mid) > target: lo = mid
        else: hi = mid
    return mid

cyc = sum(ae.values()) / 7                       # cycle base 2019-2025, peak to peak by utilization
lit = sum(ae[y] for y in range(2021, 2026)) / 5  # literal five-year window
h1 = (ae[2019] + ae[2020] + ae[2021]) / 3; h2 = (ae[2023] + ae[2024] + ae[2025]) / 3
g_cyc = (h2 / h1) ** (1 / 4) - 1                 # halves of the cycle, midpoints 2020 and 2024
g_lit = (ae[2025] / ae[2021]) ** (1 / 4) - 1     # literal end years
sales_g = (998.1 / 632.6) ** (1 / 4) - 1
print(f"EV at price {EV:,.1f}; J-W owner cash (own filed year) {JW:.1f}; interest on today's debt {INTEREST_NOW:.1f}")
print(f"cycle base 2019-25 {cyc:.1f} (+J-W {cyc+JW:.1f}); literal 2021-25 {lit:.1f} (+J-W {lit+JW:.1f})")
print(f"growth: cycle halves {100*g_cyc:.2f}%/yr; literal end years {100*g_lit:.2f}%/yr; sales 2021-25 {100*sales_g:.2f}%/yr")

def report(label, oc, g):
    v_r = value(oc, g, R); v_f = value(oc, g, FLOOR)
    print(f"  {label}: owner cash {oc:.1f}, g {100*g:.2f}% -> whole business {v_r:,.0f} at {100*R:.2f}% = ${(v_r-NET_DEBT)/UNITS:.2f}/unit; "
          f"at 10% {v_f:,.0f} = ${(v_f-NET_DEBT)/UNITS:.2f}/unit; expected return at the price {100*irr(oc,g,EV):.2f}%")
    return (v_r - NET_DEBT) / UNITS, (v_f - NET_DEBT) / UNITS

print("CENTRAL (all-equity basis, cycle base, all spending deducted, J-W added at no growth on its own year):")
base = cyc + JW
lo_r, lo_f = report("no-growth end", base, 0.0)
hi_r, hi_f = report("shown-growth end (cycle halves)", base, g_cyc)
print(f"  RANGE ${min(lo_r,hi_r):.2f} to ${max(lo_r,hi_r):.2f} against ${PRICE}; FAIR (mean of the two ends at 10%) ${(lo_f+hi_f)/2:.2f}")

print("BESIDE: literal window 2021-2025 (first year a trough on the filer's description):")
l0 = report("literal no-growth", lit + JW, 0.0)
l1 = report("literal shown growth (end years)", lit + JW, g_lit)

print("BESIDE: D&A variant (depreciation as the spending charge), cycle base:")
da = {2019: 185.6, 2020: 183.9, 2021: 142.5, 2022: 159.3, 2023: 221.8, 2024: 292.7, 2025: 323.8}
dab = sum(da.values()) / 7 + JW
d0 = report("D&A no-growth", dab, 0.0)

print("BESIDE: equity-only (owner cash after interest on today's debt, against the market value of the units):")
for lab, oc, g in (("equity-only no-growth", base - INTEREST_NOW, 0.0), ("equity-only shown growth", base - INTEREST_NOW, g_cyc)):
    v_r = value(oc, g, R); v_f = value(oc, g, FLOOR)
    print(f"  {lab}: {oc:.1f} -> ${v_r/UNITS:.2f}/unit at {100*R:.2f}%, ${v_f/UNITS:.2f}/unit at 10%; return at the price {100*irr(oc,g,PRICE*UNITS):.2f}%")
oc = base - INTEREST_NOW
print(f"  equity-only FAIR ${(value(oc,0,FLOOR)+value(oc,g_cyc,FLOOR))/2/UNITS:.2f}")

# maintenance guess the filing allows: fleet / life x new-unit cost
print(f"maintenance guess: 3,894,332 HP / 25 years x $1,240/HP = {3894332/25*1240/1e6:.0f}M a year; average total spending 2019-25 = {1263.0/7:.0f}M")
