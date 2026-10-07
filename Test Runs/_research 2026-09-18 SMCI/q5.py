# COMPUTATION - NOT A CLEARANCE. Yields and growth-to-floor on the struck pair.
P = 40.35; S = 656_965_384; PREF = 130_686_000
capC = P*S/1e6; capP = P*(S+PREF)/1e6; sov = 5.29
print("cap common %.1f  cap with preferred at min conversion %.1f" % (capC, capP))
cases = [("5y convention, capex end", -1790.9), ("5y convention, D&A end", -1730.2), ("FY2026 convention, capex end", -7384.0),
         ("5y before WC build, less write-downs, capex end", 919.3), ("5y same, D&A end", 980.0), ("3y same, capex end", 1271.6),
         ("FY2026 same, capex end", 2076.2), ("FY2026 same, D&A end", 2184.5), ("10y same, capex end", 489.4)]
for n, oe in cases:
    for lab, cap in (("common", capC), ("with pref", capP)):
        y = 100*oe/cap
        g = "refused (negative base)" if oe <= 0 else "%.1f%%" % (100*(0.10 - oe/cap)/(1 + oe/cap))
        print("%-50s %-9s OE %8.1f  yield %6.2f%%  vs sov %+6.2f  growth to 10%%: %s" % (n, lab, oe, y, y - sov, g))
print("value per share (OE/(0.10-g)) over common + minimum preferred conversion:")
for n, oe in [("5y display", 919.3), ("FY2026 display", 2076.2), ("3y display", 1271.6)]:
    print(n, {g: round(oe/(0.10-g)/((S+PREF)/1e6), 1) for g in (0.03, 0.05, 0.07)})
# company guidance, displayed only: Q1 FY2027 GAAP EPS 0.89-0.98 x 745M diluted, annualised
for eps in (0.89, 0.98):
    ni = eps*745*4
    print("guided NI annualised %.0f  on cap w/pref %.2f%%" % (ni, 100*ni/capP))
