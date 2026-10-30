# Owner earnings for EQIX, hand-built from the FILED cash-flow statements ($M).
# Sources: 10-K FY2017 (2015-2017 columns), FY2020 (2018-2020), FY2022 (2020-2022), FY2025 (2023-2025);
# 10-Q Q2 2026 and Q2 2025 for the TTM. Recurring capex from each 10-K's AFFO reconciliation.
# Capitalised SBC from the SBC note (FY2023-25 in the FY2025 10-K; earlier from each 10-K where found).
Y = list(range(2015, 2026))
OCF  = dict(zip(Y, [894.8, 1019.4, 1439.2, 1815.4, 1992.7, 2309.8, 2547.2, 2963.2, 3217.0, 3249.0, 3911.0]))
SBC  = dict(zip(Y, [132.4, 155.6, 175.5, 180.7, 236.5, 295.0, 363.8, 404.0, 407.0, 462.0, 498.0]))
# D&A on the face: FY2015-22 = Depreciation + Amortization of intangible assets (two lines);
# FY2023-25 = "Depreciation, amortization and accretion" (one line)
DEP  = dict(zip(Y, [498.1, 714.3, 865.5, 1024.1, 1088.6, 1224.3, 1450.8, 1531.5, None, None, None]))
AMZ  = dict(zip(Y, [27.4, 122.9, 177.0, 203.4, 196.3, 199.0, 205.5, 204.8, 208.0, 208.0, 200.0]))
DA   = {y: (DEP[y] + AMZ[y]) if DEP[y] is not None else None for y in Y}
DA.update({2023: 1844.0, 2024: 2011.0, 2025: 2066.0})
CAPX = dict(zip(Y, [868.1, 1113.4, 1378.7, 2096.2, 2079.5, 2282.5, 2751.5, 2278.0, 2781.0, 3066.0, 4311.0]))
RE   = dict(zip(Y, [38.3, 28.1, 95.1, 182.4, 169.2, 200.2, 201.8, 248.3, 384.0, 337.0, 994.0]))
FLP  = dict(zip(Y, [28.7, 114.4, 93.5, 103.8, 126.5, 115.3, 165.5, 134.2, 149.0, 140.0, 155.0]))  # finance/capital lease principal repaid (financing)
REC  = dict(zip(Y, [120.3, 141.8, 168.0, 203.1, 186.0, 160.6, 199.1, 188.9, 218.3, 250.0, 284.0]))
CSBC = {2023: 60.0, 2024: 77.0, 2025: 69.0}   # SBC capitalised into construction in progress
ACQ  = dict(zip(Y, [245.5, 1766.6, 3963.3, 829.7, 34.1, 1180.3, 158.5, 964.0, 0.0, 0.0, 251.0]))
INTINC = dict(zip(Y, [3.6, 3.5, 13.1, 14.5, 27.7, 8.7, 2.6, 36.3, 94.0, 137.0, 193.0]))
CAPINT = dict(zip(Y, [10.9, 13.3, 22.6, 19.9, 32.2, 26.8, 24.5, 18.2, 26.0, 36.0, 79.0]))
DIV  = dict(zip(Y, [521.5, 499.5, 621.5, 738.6, 836.2, 947.9, 1042.9, 1152.0, 1375.0, 1643.0, 1856.0]))
EQ   = dict(zip(Y, [829.5, 0.0, 2481.4, 388.2, 1661.0, 1981.4, 497.9, 796.0, 734.0, 1673.0, 99.0]))
DSH  = dict(zip(Y, [58.5, 70.8, 77.5, 80.2, 84.7, 88.4, 90.4, 91.8, 94.0, 95.8, 98.1]))  # diluted weighted, millions
REV  = dict(zip(Y, [2725.9, 3612.0, 4368.4, 5071.7, 5562.1, 5998.5, 6635.5, 7263.0, 8188.0, 8748.0, 9217.0]))

# TTM to 2026-06-30 = FY2025 - H1 2025 + H1 2026
TTM = dict(OCF=3911-1753+1784, SBC=498-240+273, DA=2066-982+1101, CAPX=4311-1739+2834,
           RE=994-99+224, REC=284-81+81, FLP=155, CSBC=69, INTINC=193)

def ends(y, d=None):
    if d is None:
        d = dict(OCF=OCF[y], SBC=SBC[y], DA=DA[y], CAPX=CAPX[y], RE=RE[y], REC=REC[y], FLP=FLP[y],
                 CSBC=CSBC.get(y, 0.0), AMZ=AMZ.get(y, 0.0))
    base = d["OCF"] - d["SBC"]
    return {
        "company_recurring": base - d["REC"] - d["FLP"],            # the company's own maintenance, plus lease principal
        "DA_total": base - d["DA"],                                   # corpus default [E3-44], total D&A
        "dep_only": base - (d["DA"] - d.get("AMZ", 0.0)),            # depreciation only (acquired-intangible amortisation excluded)
        "total_capex": base - d["CAPX"] - d["RE"] - d["FLP"] - d["CSBC"],  # all capital spending incl. growth
    }

print("year | OCF | SBC | D&A | capex(other) | real estate | lease principal | recurring | OE:recurring | OE:D&A | OE:dep-only | OE:total capex | per dil share (D&A)")
rows = {}
for y in Y:
    e = ends(y); rows[y] = e
    print(y, OCF[y], SBC[y], round(DA[y],1), CAPX[y], RE[y], FLP[y], REC[y], *[round(v) for v in e.values()], round(e["DA_total"]/DSH[y], 2))
tt = dict(TTM); tt["AMZ"] = 200.0 - 98 + 100  # H1 amortisation approx: FY2025 200, H1 2025 98; H1 2026 not split on face, assume ~100 (flagged)
e = ends(None, tt); rows["TTM"] = e
print("TTM", tt["OCF"], tt["SBC"], tt["DA"], tt["CAPX"], tt["RE"], tt["FLP"], tt["REC"], *[round(v) for v in e.values()])

def mean(keys, k):
    return sum(rows[y][k] for y in keys) / len(keys)
for name, ks in [("3y FY2023-25", [2023, 2024, 2025]), ("5y FY2021-25", list(range(2021, 2026))), ("10y FY2016-25", list(range(2016, 2026)))]:
    print(name, {k: round(mean(ks, k)) for k in rows[2025]})

print("\nSBC/OCF 2025 %.1f%%, 2021-25 %.1f%%, 2016-25 %.1f%%" % (100*SBC[2025]/OCF[2025],
      100*sum(SBC[y] for y in range(2021,2026))/sum(OCF[y] for y in range(2021,2026)),
      100*sum(SBC[y] for y in range(2016,2026))/sum(OCF[y] for y in range(2016,2026))))
print("recurring capex / D&A:", {y: round(REC[y]/DA[y]*100,1) for y in Y})
print("total capex (other+RE) / D&A:", {y: round((CAPX[y]+RE[y])/DA[y],2) for y in Y})
print("capex(other+RE)/revenue %:", {y: round(100*(CAPX[y]+RE[y])/REV[y],1) for y in Y})
s = lambda d, a, b: sum(d[y] for y in range(a, b+1))
print("\nFY2015-25 sums: OCF %.0f, capex+RE %.0f, acquisitions %.0f, dividends %.0f, equity raised %.0f" % (s(OCF,2015,2025), s(CAPX,2015,2025)+s(RE,2015,2025), s(ACQ,2015,2025), s(DIV,2015,2025), s(EQ,2015,2025)))
print("FY2021-25 sums: OCF %.0f, capex+RE %.0f, dividends %.0f, equity %.0f" % (s(OCF,2021,2025), s(CAPX,2021,2025)+s(RE,2021,2025), s(DIV,2021,2025), s(EQ,2021,2025)))
print("dividends vs OE (D&A end):", {y: (DIV[y], round(rows[y]['DA_total'])) for y in Y})
print("OE per diluted share at D&A end:", {y: round(rows[y]['DA_total']/DSH[y],2) for y in Y})
print("OE per diluted share at recurring end:", {y: round(rows[y]['company_recurring']/DSH[y],2) for y in Y})
print("diluted shares growth 2015->2025: %.1f%%, 2020->2025: %.1f%%" % (100*(DSH[2025]/DSH[2015]-1), 100*(DSH[2025]/DSH[2020]-1)))
