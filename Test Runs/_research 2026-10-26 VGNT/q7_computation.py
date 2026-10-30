# COMPUTATION, NOT A CLEARANCE (Q2 closed the file OUT). Figures from the information statement
# (0001193125-26-096776) combined cash flow statements and the Q2 2026 10-Q (0002078008-26-000018).
ocf   = {2023: 180, 2024: 707, 2025: 641}
capex = {2023: 244, 2024: 206, 2025: 160}
dep   = {2023: 193+12, 2024: 200+2, 2025: 226+1}   # depreciation + amortization
sbc   = {2023: 25, 2024: 28, 2025: 33}
nci   = {2023: 29, 2024: 26, 2025: 18}            # net income attributable to noncontrolling interest
oc  = {y: ocf[y]-capex[y]-sbc[y]-nci[y] for y in ocf}
ocd = {y: ocf[y]-dep[y]-sbc[y]-nci[y] for y in ocf}
avg3 = sum(oc.values())/3; avg2 = (oc[2024]+oc[2025])/2
avg3d = sum(ocd.values())/3; avg2d = (ocd[2024]+ocd[2025])/2
print("owner cash (all spending):", oc, "avg3 %.1f avg2 %.1f" % (avg3, avg2))
print("owner cash (depreciation variant):", ocd, "avg3 %.1f avg2 %.1f" % (avg3d, avg2d))
r = 0.0533; floor = 0.10
debt = 153 + 2071; cash = 554; nd = debt - cash
sh = 70.835265; price = 41.40; mcap = price*sh
ev = mcap + nd
print("net debt", nd, "mcap %.1f EV %.1f" % (mcap, ev))
# zero growth (shown growth nil; series changes sign) -> perpetuity at sovereign
for lab, x in (("bottom (3-yr window, literal)", avg3), ("top (2023 removed as aberrational)", avg2)):
    v = x / r
    print(lab, "value %.0f  per share %.2f  yield at EV %.2f%%" % (v, (v-nd)/sh, 100*x/ev))
# equity-only: interest at the Q2 2026 run-rate, after tax at the H1 2026 effective rate 16%
interest = 36*4; t = 0.16; int_at = interest*(1-t)
for lab, x in (("bottom", avg3), ("top", avg2)):
    e = x - int_at
    print("equity-only", lab, "owner cash %.1f value %.0f per share %.2f yield at mcap %.2f%%" % (e, e/r, e/r/sh, 100*e/mcap))
# fair price: each end valued at 10%, averaged
fp_all = ((avg3/floor + avg2/floor)/2 - nd)/sh
fp_eq  = (((avg3-int_at)/floor + (avg2-int_at)/floor)/2)/sh
print("fair price all-equity %.2f  equity-only %.2f" % (fp_all, fp_eq))
# depreciation variant
for lab, x in (("bottom dep", avg3d), ("top dep", avg2d)):
    print(lab, "per share %.2f" % ((x/r - nd)/sh))
print("width top/bottom %.2f" % ((avg2/r-nd)/(avg3/r-nd)))
