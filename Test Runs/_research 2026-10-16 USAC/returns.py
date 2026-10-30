"""Field returns and owner cash for the USAC run (2026-10-16). Arithmetic only; every input is a filed figure.
USAC inputs: first-filed 10-K XBRL values (ff.py), checked against the filed statements of FY2025.
2014-2017 = USA Compression before the 2018 combination; 2018-2025 = the combined partnership.
Archrock, Kodiak: first-filed 10-K XBRL values; Archrock 2025 adjusted for the gain on sale and the
sales-tax benefit its 10-K names. Units $M."""

# Return on tangible assets: operating profit before impairments / year-end (assets - goodwill - intangibles - cash)
usac = {  # year: (operating income, goodwill + long-lived impairments, assets, goodwill, intangibles, cash)
 2014: (37.6, 2.3, 1516.5, 208.1, 82.4, 0.0),
 2015: (-135.6, 172.2 + 27.3, 1509.8, 35.9, 78.8, 0.0),
 2016: (34.4, 5.8, 1472.4, 35.9, 75.2, 0.1),
 2017: (37.1, 5.0, 1492.1, 35.9, 71.7, 0.0),
 2018: (65.3, 8.7, 3774.6, 619.4, 392.6, 0.1),
 2019: (168.4, 5.9, 3730.4, 619.4, 363.2, 0.0),
 2020: (-464.9, 619.4 + 8.1, 2948.7, 0.0, 333.8, 0.0),
 2021: (140.9, 5.1, 2768.0, 0.0, 304.4, 0.0),
 2022: (169.3, 1.5, 2665.7, 0.0, 275.0, 0.0),
 2023: (232.0, 12.3, 2736.8, 0.0, 245.7, 0.0),
 2024: (294.4, 0.9, 2745.6, 0.0, 216.3, 0.0),
 2025: (306.5, 7.8, 2619.9, 0.0, 186.9, 8.6),
}
# Archrock: pretax + interest + impairments (AssetImpairmentCharges and goodwill), less gains named
aroc = {  # year: (pretax, interest, impairments, adjustments, assets, goodwill, intangibles, cash)
 2016: (-89.4, 83.9, 87.4, 0.0, 2414.8, 0.0, 86.7, 3.1),
 2017: (-42.6, 88.8, 29.1, 0.0, 2408.0, 0.0, 68.9, 10.5),
 2018: (35.3, 93.3, 28.1, 0.0, 2552.5, 0.0, 52.4, 5.6),
 2019: (58.5, 104.7, 44.7, 0.0, 3110.0, 100.6, 77.5, 3.7),
 2020: (-86.0, 105.7, 99.8, 0.0, 2779.7, 0.0, 61.5, 1.1),   # goodwill only; long-lived impairment untagged
 2021: (39.0, 108.1, 0.0, 0.0, 2590.0, 0.0, 47.9, 1.6),     # impairment untagged
 2022: (60.6, 101.3, 0.0, 0.0, 2598.8, 0.0, 37.1, 1.6),
 2023: (142.2, 111.5, 0.0, -10.2, 2655.9, 0.0, 30.2, 1.3),  # gain on sale 10.2 (FY2025 10-K table)
 2024: (232.4, 123.6, 0.0, -17.9, 3824.2, 52.2, 98.3, 4.4),  # gain on sale 17.9
 2025: (423.6, 165.3, 0.0, -47.1 - 35.0, 4349.3, 125.2, 143.9, 1.6),  # gain 47.1; sales-tax benefit 35.0
}
kgs = {  # year: (operating income, impairments, assets, goodwill, intangibles, cash)
 2023: (244.1, 0.0, 3244.1, 305.6, 122.9, 5.6),
 2024: (249.4, 9.9, 4435.1, 415.2, 162.7, 4.8),
 2025: (340.0, 6.3, 4318.0, 408.7, 154.5, 3.2),
}

def pr(name, rows):
    print(name)
    vals = []
    for y, r in rows.items():
        print(f"  {y}: {r[0]:7.1f} / {r[1]:7.1f} = {100*r[0]/r[1]:5.1f}%")
        vals.append(100 * r[0] / r[1])
    print(f"  mean {sum(vals)/len(vals):.1f}%")

pr('USAC return on tangible assets (op. income before impairments / tangible assets)',
   {y: (a + b, A - g - i - c) for y, (a, b, A, g, i, c) in usac.items()})
pr('Archrock (pretax + interest + impairments - named gains and benefit) / tangible assets',
   {y: (p + n + m + adj, A - g - i - c) for y, (p, n, m, adj, A, g, i, c) in aroc.items()})
pr('Kodiak (op. income before impairments) / tangible assets',
   {y: (a + b, A - g - i - c) for y, (a, b, A, g, i, c) in kgs.items()})

# USAC owner cash, combined partnership, $M
ocf  = {2019: 300.6, 2020: 293.2, 2021: 265.4, 2022: 260.6, 2023: 271.9, 2024: 341.3, 2025: 394.3}
sbc  = {2019: 10.8, 2020: 8.4, 2021: 15.5, 2022: 15.9, 2023: 22.2, 2024: 16.6, 2025: 4.3}
capx = {2019: 171.1, 2020: 109.1, 2021: 45.2, 2022: 134.2, 2023: 238.5, 2024: 204.9, 2025: 117.3}
proc = {2019: 22.5 + 4.2, 2020: 2.6 + 1.3, 2021: 4.5 + 1.6, 2022: 3.7 + 0.6, 2023: 5.3 + 0.5, 2024: 1.3 + 1.5, 2025: 2.3 + 0.1}
intp = {2019: 105.4, 2020: 120.7, 2021: 120.6, 2022: 129.0, 2023: 163.6, 2024: 154.3, 2025: 181.3}
da   = {2019: 231.4, 2020: 239.0, 2021: 238.8, 2022: 236.7, 2023: 246.1, 2024: 264.8, 2025: 284.8}
inv2ppe = {2019: 21.8, 2020: 17.4, 2021: 10.8, 2022: 22.3, 2023: 54.6, 2024: 78.5, 2025: 37.3}
dinv = {2019: 25.1, 2020: 11.7, 2021: 12.6, 2022: 31.6, 2023: 76.8, 2024: 101.9, 2025: 41.1}  # inventory purchases in OCF
maint = {2019: 29.6, 2020: 23.3, 2021: 19.5, 2022: 23.8, 2023: 25.2, 2024: 31.9, 2025: 39.4}
rev  = {2019: 698.4, 2020: 667.7, 2021: 632.6, 2022: 704.6, 2023: 846.2, 2024: 950.4, 2025: 998.1}

print('\nUSAC owner cash, all spending deducted ($M): equity-only = OCF - SBC - capex + disposal proceeds; all-equity adds cash interest')
eq, ae, aeDA = {}, {}, {}
for y in ocf:
    eq[y] = ocf[y] - sbc[y] - capx[y] + proc[y]
    ae[y] = eq[y] + intp[y]
    # D&A variant: OCF before the inventory build that became fleet, less SBC, less D&A as the spending charge
    aeDA[y] = ocf[y] + inv2ppe[y] - sbc[y] - da[y] + intp[y]
    tot = capx[y] + inv2ppe[y]
    print(f"  {y}: equity-only {eq[y]:7.1f}  all-equity {ae[y]:7.1f}  D&A variant all-equity {aeDA[y]:7.1f}  total fleet spending {tot:6.1f}  filer maintenance {maint[y]:5.1f}  owner cash/sales {100*ae[y]/rev[y]:5.1f}%")
for lab, d in (('equity-only', eq), ('all-equity', ae), ('D&A variant', aeDA)):
    w5 = [d[y] for y in range(2021, 2026)]
    w7 = [d[y] for y in range(2019, 2026)]
    print(f"  {lab}: 5-yr mean 2021-25 {sum(w5)/5:7.1f};  7-yr mean 2019-25 (peak to peak) {sum(w7)/7:7.1f}")
print('  total fleet spending 2019-2025:', round(sum(capx.values()) + sum(inv2ppe.values()), 1),
      ' filer maintenance total:', round(sum(maint.values()), 1))
