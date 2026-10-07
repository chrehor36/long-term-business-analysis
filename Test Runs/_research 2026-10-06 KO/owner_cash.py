"""Owner cash for KO, FY2016-FY2025, after every real cost, from the filed cash-flow statements (XBRL, latest vintage;
FY2023-FY2025 cross-checked to the FY2025 10-K cash-flow statement, accession 0001628280-26-010047).

owner cash (capex basis) = OCF - stock-based compensation - purchases of PP&E
owner cash (D&A basis)   = OCF - stock-based compensation - depreciation and amortization

Recast (this run's CONVENTION, shown beside the as-filed figure, never instead of it):
  + fairlife contingent consideration paid inside operating cash flow (it is the purchase price of a business bought in
    2020, routed to operating activities by GAAP because it exceeded the acquisition-date fair value):
      2023: 167 (275 milestone less 108 in financing, FY2023 10-K)   2025: 6,069 (6,173 less 104 in financing, FY2025 10-K)
      2021: the first 100 milestone; its split between operating and financing is not stated; left as filed (immaterial).
  + the IRS Tax Litigation Deposit of 2024: 6,000 (tax years 2007-2009, refundable if the appeal succeeds). It is carried
    instead as a contingent liability at Q7 and Q9, together with the company's own $14bn estimate for 2010-2025.
"""
OCF = {2016: 8792, 2017: 7041, 2018: 7627, 2019: 10471, 2020: 9844, 2021: 12625, 2022: 11018, 2023: 11599, 2024: 6805, 2025: 7408}
SBC = {2016: 258, 2017: 219, 2018: 225, 2019: 201, 2020: 126, 2021: 337, 2022: 356, 2023: 254, 2024: 286, 2025: 279}
CAPEX = {2016: 2262, 2017: 1750, 2018: 1548, 2019: 2054, 2020: 1177, 2021: 1367, 2022: 1484, 2023: 1852, 2024: 2064, 2025: 2112}
DA = {2016: 1787, 2017: 1260, 2018: 1086, 2019: 1365, 2020: 1536, 2021: 1452, 2022: 1260, 2023: 1128, 2024: 1075, 2025: 1050}
FAIRLIFE_IN_OCF = {2023: 167, 2025: 6069}
IRS_DEPOSIT = {2024: 6000}
INTEREST_PAID = {2016: 663, 2017: 803, 2018: 903, 2019: 921, 2020: 935, 2021: 738, 2022: 848, 2023: 1415, 2024: 1669, 2025: 1724}
TAX_PAID = {2016: 1554, 2017: 1950, 2018: 2120, 2019: 2126, 2020: 1268, 2021: 2168, 2022: 2403, 2023: 2580, 2024: 3262, 2025: 2873}
REVENUE = {2016: 41863, 2017: 36212, 2018: 34300, 2019: 37266, 2020: 33014, 2021: 38655, 2022: 43004, 2023: 45754, 2024: 47061, 2025: 47941}
RECEIVABLES = {2016: 3856, 2017: 3667, 2018: 3396, 2019: 3971, 2020: 3144, 2021: 3512, 2022: 3487, 2023: 3410, 2024: 3569, 2025: 3038}

rows = []
print(f"{'FY':>4} {'OCF':>7} {'SBC':>5} {'capex':>6} {'D&A':>6} {'OC capex':>9} {'OC D&A':>8} {'recast':>7} {'OC capex recast':>15} {'OC D&A recast':>13} {'recv days':>9}")
for y in sorted(OCF):
    oc_c = OCF[y] - SBC[y] - CAPEX[y]
    oc_d = OCF[y] - SBC[y] - DA[y]
    adj = FAIRLIFE_IN_OCF.get(y, 0) + IRS_DEPOSIT.get(y, 0)
    days = RECEIVABLES[y] / REVENUE[y] * 365
    rows.append((y, oc_c, oc_d, oc_c + adj, oc_d + adj))
    print(f"{y:>4} {OCF[y]:>7,} {SBC[y]:>5} {CAPEX[y]:>6,} {DA[y]:>6,} {oc_c:>9,} {oc_d:>8,} {adj:>7,} {oc_c+adj:>15,} {oc_d+adj:>13,} {days:>9.1f}")

w = [r for r in rows if 2021 <= r[0] <= 2025]
n = len(w)
print()
print("five-year means FY2021-FY2025 (USD millions):")
print(f"  as filed:  capex basis {sum(r[1] for r in w)/n:,.1f}   D&A basis {sum(r[2] for r in w)/n:,.1f}")
print(f"  recast:    capex basis {sum(r[3] for r in w)/n:,.1f}   D&A basis {sum(r[4] for r in w)/n:,.1f}")
w2 = [r for r in rows if 2016 <= r[0] <= 2020]
print(f"  prior five FY2016-FY2020, recast = as filed: capex basis {sum(r[3] for r in w2)/5:,.1f}")

# factoring pull-forward sensitivity: receivables at FY2020 receivable days on FY2025 revenue, less actual
d2020 = RECEIVABLES[2020] / REVENUE[2020]
pull = d2020 * REVENUE[2025] - RECEIVABLES[2025]
print(f"\nfactoring sensitivity: FY2025 receivables at FY2020 days would be {d2020*REVENUE[2025]:,.0f} vs {RECEIVABLES[2025]:,} filed;"
      f" difference {pull:,.0f} over the window = {pull/5:,.0f} a year")

# pre-tax and unlevered variants of the recast capex-basis series
print("\nrecast capex basis, unlevered (+ interest paid x (1-0.21)) and pre-tax (+ interest paid + income taxes paid,"
      " IRS deposit excluded since it is already added back):")
for y, oc_c, oc_d, rc, rd in w:
    unlev = rc + INTEREST_PAID[y] * (1 - 0.21)
    pretax = rc + INTEREST_PAID[y] + TAX_PAID[y]
    print(f"  {y}  recast {rc:>7,}  unlevered {unlev:>9,.1f}  pre-tax {pretax:>7,}")
ul = [rc + INTEREST_PAID[y] * (1 - 0.21) for y, _, _, rc, _ in w]
pt = [rc + INTEREST_PAID[y] + TAX_PAID[y] for y, _, _, rc, _ in w]
print(f"  means: unlevered {sum(ul)/n:,.1f}   pre-tax {sum(pt)/n:,.1f}")
