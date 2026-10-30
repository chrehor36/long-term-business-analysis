import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
P = print

cap = 999_637_371 * 60.95 / 1e6          # 60,928
fd = 1_101_437_371
capfd = fd * 60.95 / 1e6                 # 67,133
sov = 5.25
pref = 679.0

P("cap {:,.0f}   fully diluted cap {:,.0f}   sovereign {}%".format(cap, capfd, sov))

# --- the base: CONTINUING operations only. OxyChem closed 2026-01-02.
ocf = {2023: 10235.0, 2024: 10519.0, 2025: 9606.0}
sbc = {2023: 203.0, 2024: 213.0, 2025: 234.0}
P("\nCONTINUING-OPS OCF (FY2025 10-K, restated for discontinued ops): {}".format(ocf))
m3 = sum(ocf.values()) / 3
s3 = sum(sbc.values()) / 3
P("  3-yr mean OCF {:,.0f}  less 3-yr mean SBC {:,.0f}  = base {:,.0f}".format(m3, s3, m3 - s3))
P("  FY2025 alone  {:,.0f}  less SBC {:,.0f}          = base {:,.0f}".format(ocf[2025], sbc[2025], ocf[2025] - sbc[2025]))

cases = [
    ("(c)=5,700  2026 plan midpoint - HOLDS VOLUME FLAT", 5700.0),
    ("(c)=6,427  FY2025 capex as spent", 6427.0),
    ("(c)=7,500  THE JUDGMENT (D&A 7,533; midpoint replacement 7,474)", 7500.0),
    ("(c)=8,026  drill-bit-only replacement at 2025 F&D $15.34/Boe", 8026.0),
]
for wname, base in (("3-yr mean", m3 - s3), ("FY2025", ocf[2025] - sbc[2025])):
    P("\n== window: {} (base {:,.0f}) ==".format(wname, base))
    for lab, c in cases:
        oe = base - c
        toc = oe - pref
        P("  {:<62} OE {:>7,.0f} | to common {:>7,.0f} | {:>6.2f}% on cap | {:>6.2f}% fully diluted".format(
            lab, oe, toc, toc / cap * 100, toc / capfd * 100))

P("\n--- SPREAD [E4-25] ---")
lo = (m3 - s3 - 8026 - pref)
hi = (ocf[2025] - sbc[2025] - 5700 - pref)
P("  conservative end (3-yr mean, (c)=drill-bit) {:,.0f}  ->  {:.2f}% on cap".format(lo, lo / cap * 100))
P("  optimistic end   (FY2025,  (c)=volume-flat) {:,.0f}  ->  {:.2f}% on cap".format(hi, hi / cap * 100))
P("  spread, conservative end as a fraction of the optimistic end: {:.0%}".format(lo / hi))

P("\n--- [E4-41] NORMALISE THE MEAN DOWN FOR LUCK: the window's WTI vs the nine-year WTI ---")
wti = {2017: 50.80, 2018: 64.90, 2019: 57.03, 2020: 39.16, 2021: 67.99, 2022: 94.53, 2023: 77.62, 2024: 75.72, 2025: 64.81}
m9 = sum(wti.values()) / 9
w3 = (wti[2023] + wti[2024] + wti[2025]) / 3
P("  nine-year mean WTI ${:.2f} | FY2023-25 mean WTI ${:.2f} | the window sits ${:.2f} ABOVE the long-run mean".format(m9, w3, w3 - m9))
P("  x $240M/$ = ${:,.0f}M/yr of pre-tax cash; at a 27% cash-tax rate = ${:,.0f}M/yr after tax".format((w3 - m9) * 240, (w3 - m9) * 240 * 0.73))
P("  SENSITIVITY, NOT A SUBTRACTION (windage is spent once): it would move the 3-yr (c)=7,500 line")
v = m3 - s3 - 7500 - pref
P("    from {:,.0f} ({:.2f}%) to {:,.0f} ({:.2f}%)".format(v, v / cap * 100, v - (w3 - m9) * 240 * 0.73, (v - (w3 - m9) * 240 * 0.73) / cap * 100))

P("\n--- Q5: THE PRICE. capitalised at the sovereign, on FULLY DILUTED shares ---")
for lab, c in cases:
    for wname, base in (("3-yr", m3 - s3), ("FY25", ocf[2025] - sbc[2025])):
        toc = base - c - pref
        P("  {:<62} {} -> ${:,.1f}bn -> ${:.2f}/sh".format(lab, wname, toc / (sov / 100) / 1000, toc / (sov / 100) / fd * 1e6))

P("\n--- Q5: at the [E4-28] 10% floor ---")
for lab, c in cases:
    for wname, base in (("3-yr", m3 - s3), ("FY25", ocf[2025] - sbc[2025])):
        toc = base - c - pref
        P("  {:<62} {} -> ${:,.1f}bn -> ${:.2f}/sh".format(lab, wname, toc / 0.10 / 1000, toc / 0.10 / fd * 1e6))

P("\n--- what the price already assumes ---")
for lab, c in cases:
    toc = (m3 - s3) - c - pref
    y = toc / cap
    P("  {:<62} yield {:.2f}% | {:+.2f} pts vs sovereign | perpetual growth needed for the 10% floor: {:+.2f} pts".format(
        lab, y * 100, (y - sov / 100) * 100, 10.0 - y * 100))

P("\n--- COVERAGE [E2-54]: interest met out of cash flow NET OF AMPLE CAPEX ---")
P("  OCF is stated AFTER cash interest, so the test is run by adding interest back.")
for lab, c in cases:
    pre_int = ocf[2025] + 1079.0
    P("  {:<62} (OCF+interest {:,.0f}) - (c) {:,.0f} = {:,.0f}; FY2025 interest 1,079 -> {:.2f}x".format(
        lab, pre_int, c, pre_int - c, (pre_int - c) / 1079.0))
P("  at the CURRENT interest run-rate (Q2-2026 filed $108M x4 = $432M):")
for lab, c in cases:
    pre_int = ocf[2025] + 432.0
    P("  {:<62} -> {:.2f}x".format(lab, (pre_int - c) / 432.0))
