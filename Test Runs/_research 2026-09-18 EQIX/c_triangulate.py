# (c) for EQIX: three routes, FY2021-25, all from filed figures ($M). A DISCLOSED JUDGMENT, not an output.
cap_other = {2021: 2751.5, 2022: 2278.0, 2023: 2781.0, 2024: 3066.0, 2025: 4311.0}
real_est  = {2021: 201.8, 2022: 248.3, 2023: 384.0, 2024: 337.0, 2025: 994.0}
DA        = {2021: 1656.3, 2022: 1736.3, 2023: 1844.0, 2024: 2011.0, 2025: 2066.0}
AMZ       = {2021: 205.5, 2022: 204.8, 2023: 208.0, 2024: 208.0, 2025: 200.0}
REC       = {2021: 199.1, 2022: 188.9, 2023: 218.3, 2024: 250.0, 2025: 284.0}
total = sum(cap_other.values()) + sum(real_est.values())
# capacity (10-K portfolio tables, total cabinet capacity of consolidated IBXs, year end)
cap_2020, cap_2025 = 310_500, 392_300
added = cap_2025 - cap_2020
# land and construction in progress (gross PP&E note): not-yet-productive growth
land_2020, land_2025 = 944.1, 2757.0
cip_2020, cip_2025 = 1363.9, 2827.0
idle_growth = (land_2025 - land_2020) + (cip_2025 - cip_2020)
# project cost per sellable cabinet, from each year-end "projects under construction" table
cost_per_cab = {2020: 1893/32225, 2021: 1258/20525, 2022: 2174/34950, 2023: 2781/34750, 2024: 4256/41800, 2025: 6549/51900}
print("project $k per cabinet:", {y: round(v*1000, 1) for y, v in cost_per_cab.items()})
acq_share = (0.0, 0.15)  # share of added capacity that came by acquisition (MainOne, Entel, GPX, TIM): not filed as a cabinet count; bracketed
res = []
for a in acq_share:
    organic = added * (1 - a)
    for c in (cost_per_cab[2020], (cost_per_cab[2020]+cost_per_cab[2024])/2, cost_per_cab[2024]):
        growth = organic * c + idle_growth
        maint = (total - growth) / 5
        res.append(maint)
        print(f"acq share {a:.0%}, $k/cab {c*1000:.0f}: growth capex {growth:,.0f}, non-growth (c) {maint:,.0f}/yr")
print(f"\nFY2021-25: total capex+RE {total:,.0f}; capacity added {added:,} cabinets; land+CIP build-up {idle_growth:,.0f}")
print(f"(c) route 2 (capex minus growth), range {min(res):,.0f} to {max(res):,.0f} a year")
print(f"route 1 (D&A total) 5y mean {sum(DA.values())/5:,.0f}; depreciation only {sum(DA[y]-AMZ[y] for y in DA)/5:,.0f}")
print(f"company recurring 5y mean {sum(REC.values())/5:,.0f}")
# route 3: replacement cost. Book gross plant per cabinet of capacity (ex land, ex CIP) vs current project cost
gross_ex = 36972 - 2757 - 2827
book_per_cab = gross_ex / cap_2025
cur = cost_per_cab[2025]
dep_2025 = 2066 - 200
print(f"book gross plant ex land/CIP per cabinet ${book_per_cab*1000:,.1f}k vs FY2025 project cost ${cur*1000:,.1f}k -> ratio {cur/book_per_cab:.2f}")
print(f"replacement-cost depreciation FY2025 = {dep_2025:,.0f} x {cur/book_per_cab:.2f} = {dep_2025*cur/book_per_cab:,.0f}")
