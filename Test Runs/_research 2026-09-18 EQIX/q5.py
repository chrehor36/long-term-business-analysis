cap = 1025.94 * 98_671_686 / 1e6
cash = 979 + 1245
sov = 5.29
print(f"cap {cap:,.1f}; business (cap - cash) {cap-cash:,.1f}")
cases = [("company (c), FY2025 [rejected, display]", 2974, 193),
         ("central (c), FY2025", 1323, 193),
         ("central (c), five-year default", 961, 93),
         ("conservative (c), FY2025 (replacement cost)", 246, 193),
         ("conservative (c), five-year", -57, 93),
         ("D&A end FY2025 [INVALID end, display]", 1347, 193),
         ("company AFFO FY2025 (company measure, display)", 3761, 193)]
for nm, oe, ii in cases:
    y_cap = 100*oe/cap
    y_bus = 100*(oe-ii)/(cap-cash)
    g = 10 - y_bus
    print(f"{nm}: OE {oe:,}; on cap {y_cap:.2f}%; ex-interest on business {y_bus:.2f}%  vs sov {y_bus-sov:+.2f} pts; perpetual g to reach 10% {g:.2f}%; mult {cap/oe if oe>0 else float('nan'):.0f}x")
print("\nvalue per share = (OE - interest)/(0.10-g) + cash, / 98.67M")
for nm, oe in [("company (c)", 2974-193), ("central FY2025", 1323-193), ("central 5y", 961-93)]:
    row = []
    for g in (0.03, 0.05, 0.07, 0.08):
        v = (oe/(0.10-g) + cash)/98.671686
        row.append(f"g={g:.0%}: ${v:,.0f}")
    print(nm, row)
