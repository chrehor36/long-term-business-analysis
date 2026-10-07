"""Q3 capital arithmetic on filed figures ($M). Sources: HD 10-K FY2025 balance sheet (0001628280-26-019436) for the
operating-asset method; tools/run.py ten-year table (first-filed XBRL) for equity, debt on the face, goodwill,
intangibles and cash; operating income from history_output.txt; acquired-intangible amortization from the segment notes."""

# Method A: net tangible operating assets from the filed balance sheets (operating leases' ROU assets included as capital)
def nta(rec, inv, oca, ppe, rou, oth, ap, sal, stax, defrev, itax, oacc, oltl):
    return rec + inv + oca + ppe + rou + oth - (ap + sal + stax + defrev + itax + oacc + oltl)
fy25 = nta(5597, 25817, 1588, 28021, 9204, 806, 11491, 2529, 508, 2575, 114, 4358, 2512)
fy24 = nta(4903, 23451, 1670, 26702, 8592, 684, 11938, 2315, 628, 2610, 832, 4166, 2738)
oi25, oi24 = 20890 + 607, 21526 + 425   # operating income plus acquired-intangible amortization
print(f"A. net tangible operating assets FY2025 {fy25:,}  FY2024 {fy24:,}")
print(f"   pre-tax return before acquired amortization: FY2025 {100*oi25/fy25:.1f}%  FY2024 {100*oi24/fy24:.1f}%")

# Method B: equity + debt on the face - cash, with and without goodwill and intangibles (leases excluded both ends)
rows = {  # FY label: (equity, debt face sum, cash, goodwill, intangibles, operating income)
    "FY2016": (4333, 23601, 2538, 2093, 0, 13427),
    "FY2019": (-3116, 31483, 2133, 2254, 0, 15843),
    "FY2021": (-1696, 40086, 2343, 7449, 3503, 23040),
    "FY2025": (12813, 55772, 1389, 22344, 10329, 20890),
}
amort = {"FY2016": 0, "FY2019": 0, "FY2021": 0, "FY2025": 607}  # pre-2022 intangibles not separately tagged; treated as 0
cap = {}
for y, (eq, debt, cash, gw, ia, oi) in rows.items():
    total = eq + debt - cash
    tang = total - gw - ia
    cap[y] = (total, tang, oi, oi + amort[y])
    print(f"B. {y}: capital incl. goodwill {total:,}; tangible {tang:,}; op income {oi:,}; "
          f"pre-tax on total {100*oi/total:.1f}%; on tangible (before acq. amort.) {100*(oi+amort[y])/tang:.1f}%")
for a, b in [("FY2016", "FY2025"), ("FY2021", "FY2025"), ("FY2016", "FY2021")]:
    dcap = cap[b][0] - cap[a][0]
    doi = cap[b][2] - cap[a][2]
    print(f"   incremental {a}->{b}: capital incl. goodwill +{dcap:,}; operating income {doi:+,}; "
          f"incremental pre-tax return {100*doi/dcap:.1f}%")
print(f"C. acquisition cash FY2024 17,644 + FY2025 5,410 + H1 FY2026 1,333 = {17644+5410+1333:,}")
print(f"   Other segment H1 FY2026: OI 263 + amortization 244 = {263+244} on sales 9,057")
