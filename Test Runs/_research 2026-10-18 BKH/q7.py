# COMPUTATION, NOT A CLEARANCE (until Q1 to Q6 close in the run file). USD millions; filed statements.
import sys
sys.stdout.reconfigure(encoding="utf-8")
Y = list(range(2016, 2026))
# Filed cash-flow statements: 10-K FY2018 (2016-2018, continuing ops), FY2021 (2019-2021), FY2022 (2022), FY2025 (2023-2025)
OCF = dict(zip(Y, [317.7, 409.0, 494.3, 505.5, 541.9, -64.6, 584.8, 944.4, 719.3, 673.4]))
SBC = dict(zip(Y, [10.9, 7.6, 12.4, 12.1, 5.4, 9.7, 8.6, 7.0, 10.6, 11.8]))
CAPEX = dict(zip(Y, [455.0, 326.0, 457.5, 818.4, 767.4, 677.5, 604.4, 555.6, 744.2, 819.8]))
DA = dict(zip(Y, [175.5, 188.2, 196.3, 209.1, 224.5, 236.0, 250.9, 256.8, 270.1, 283.8]))
NCI = dict(zip(Y, [9.6, 18.4, 19.6, 17.9, 15.8, 15.7, 17.4, 18.3, 17.4, 9.8]))
DEFTAX = dict(zip(Y, [82.7, 81.0, -24.2, 38.0, 38.1, 7.3, 25.6, 25.4, 52.0, 54.3]))
INTPAID = dict(zip(Y, [113.6, 132.4, 138.0, 131.8, 136.5, 142.7, 152.5, 157.3, 174.4, 196.4]))
REV = dict(zip(Y, [1538.9, 1680.3, 1754.3, 1734.9, 1696.9, 1949.1, 2551.8, 2331.3, 2127.7, 2310.0]))
NI = dict(zip(Y, [137.1, 194.1, 265.3, 199.3, 227.6, 236.7, 258.4, 262.2, 273.1, 291.6]))  # to common, continuing
W = list(range(2021, 2026))
def avg(d, ys):
    ys = list(ys)
    return sum(d[y] for y in ys) / len(ys)
M = {y: OCF[y] - SBC[y] - DA[y] - NCI[y] - DEFTAX[y] for y in Y}      # maintenance basis, book tax
Mcash = {y: OCF[y] - SBC[y] - DA[y] - NCI[y] for y in Y}              # maintenance basis, cash tax
A = {y: OCF[y] - SBC[y] - CAPEX[y] - NCI[y] - DEFTAX[y] for y in Y}   # all spending, book tax
print("year   M(book)  M(cash)   A(all)   NI   M/rev")
for y in Y:
    print(y, f"{M[y]:8.1f} {Mcash[y]:8.1f} {A[y]:8.1f} {NI[y]:6.1f} {M[y]/REV[y]*100:5.1f}%")
M0 = avg(M, W)
print(f"\nwindow 2021-2025 M(book) avg {M0:.1f}; M(cash) avg {avg(Mcash, W):.1f}; A avg {avg(A, W):.1f}; NI avg {avg(NI, W):.1f}")
p1 = avg(M, range(2016, 2021)); p2 = avg(M, range(2017, 2021)); p3 = avg(M, range(2018, 2021))
g_lit = (M0 / p1) ** (1 / 5) - 1; g_ex16 = (M0 / p2) ** (1 / 4.5) - 1; g_1820 = (M0 / p3) ** (1 / 4) - 1
print(f"prior cycle avg 2016-20 {p1:.1f} -> growth {g_lit*100:.2f}%; 2017-20 {p2:.1f} -> {g_ex16*100:.2f}%; 2018-20 {p3:.1f} -> {g_1820*100:.2f}%")
gNI = (avg(NI, W) / avg(NI, range(2016, 2021))) ** (1 / 5) - 1
print(f"earnings check: NI to common cycle growth {gNI*100:.2f}%")
gRev = (avg(REV, W) / avg(REV, range(2016, 2021))) ** (1 / 5) - 1
print(f"sales cycle growth {gRev*100:.2f}%  max M/rev in filings {max(M[y]/REV[y] for y in Y)*100:.1f}%")
# Debt credit (Q7, The regulated utility): net debt raised over the window, capped at allowed debt share x capital spending
nd2020 = 234.04 + 8.436 + 3528.1 - 6.356
nd2025 = 4701.1 - 182.8
gross = 4701.1 - (234.04 + 8.436 + 3528.1)
credit = nd2025 - nd2020
rb = [(663.8, .52), (46.8, .47), (207.3, .43), (551.2, .48), (823.4, .54), (378.4, .49), (209.3, .49), (781.3, .49), (450.8, .49)]
allowed = sum(a * b for a, b in rb) / sum(a for a, b in rb)
capex_w = sum(CAPEX[y] for y in W); da_w = sum(DA[y] for y in W); growth_w = capex_w - da_w
print(f"\ncapex 2021-25 {capex_w:.1f}; D&A {da_w:.1f}; growth spending {growth_w:.1f}")
print(f"net debt 2020 {nd2020:.1f} -> 2025 {nd2025:.1f}: credit {credit:.1f} (gross debt change {gross:.1f})")
print(f"allowed debt share (rate-base weighted, stated jurisdictions) {allowed*100:.1f}%; cap x all capex {allowed*capex_w:.1f}; x growth spending {allowed*growth_w:.1f}")
G = (growth_w - credit) / 5; Gall = growth_w / 5; Ggross = (growth_w - gross) / 5
print(f"growth spending/yr: gross of credit {Gall:.1f}; net of credit {G:.1f}; net of gross-debt credit {Ggross:.1f}")
def val(M0, g, Gs, r):
    pv = sum((M0 * (1 + g) ** t - Gs) / (1 + r) ** t for t in range(1, 11))
    return pv + M0 * (1 + g) ** 10 / r / (1 + r) ** 10
def irr(M0, g, Gs, price):
    lo, hi = 0.0011, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if val(M0, g, Gs, mid) > price:
            lo = mid
        else:
            hi = mid
    return mid
SH = 76.253141; P = 76.63; CAP = SH * P
shelter_nom = 380.1 * 0.21 + 104.1 + 8.1
r = 0.0543
shelter = sum(shelter_nom / 5 / (1 + r) ** t for t in range(1, 6))
shelter10 = sum(shelter_nom / 5 / (1.10) ** t for t in range(1, 6))
print(f"\nshelter nominal {shelter_nom:.1f}, PV {shelter:.1f} ({shelter/SH:.2f}/share); at 10% {shelter10:.1f}")
print(f"market cap {CAP:.0f}")
print("\nEQUITY-ONLY (central for the regulated utility), M0 =", round(M0, 1))
cases = [("no growth", 0.0, 0.0), ("growth 2017-20 vs 2021-25", g_ex16, G), ("growth literal 2016-20 vs 2021-25", g_lit, G), ("growth literal, gross-debt credit", g_lit, Ggross)]
for name, g, Gs in cases:
    v = val(M0, g, Gs, r) if g else M0 / r
    v10 = val(M0, g, Gs, 0.10) if g else M0 / 0.10
    e = irr(M0, g, Gs, CAP - shelter) if g else M0 / (CAP - shelter)
    print(f"  {name:36s} at 5.43%: {v:7.0f} = {(v+shelter)/SH:6.2f}/sh | at 10%: {(v10+shelter10)/SH:6.2f}/sh | return at price {e*100:5.2f}%")
nog10 = (M0 / 0.10 + shelter10) / SH
gr10 = (val(M0, g_ex16, G, 0.10) + shelter10) / SH
grl10 = (val(M0, g_lit, G, 0.10) + shelter10) / SH
print(f"  FAIR (avg of ends at 10%), central pair (no growth, cycle growth ex-2016): {(nog10+gr10)/2:.2f}; with literal growth: {(nog10+grl10)/2:.2f}")
Aw = avg(A, W) + credit / 5
print(f"  all-spending, debt credited: avg {Aw:.1f}/yr -> no-growth value {Aw/r:.0f} = {(Aw/r + shelter)/SH:.2f}/sh at 5.43%")
print(f"  M(cash tax) no-growth: {(avg(Mcash, W)/r)/SH:.2f}/sh at 5.43%, {(avg(Mcash, W)/0.10)/SH:.2f} at 10%")
nd_now = 90.0 + 410.0 + 3993.9 - 71.5
int_at = avg(INTPAID, W) * (1 - 0.21)
U0 = M0 + int_at
print(f"\nALL-EQUITY beside: U0 = {U0:.1f} (after-tax interest {int_at:.1f}); net debt 2026-06-30 {nd_now:.1f}; EV at price {CAP + nd_now:.0f}")
for name, g in [("no growth", 0.0), ("growth ex-2016", g_ex16), ("growth literal", g_lit)]:
    v = val(U0, g, Gall, r) if g else U0 / r
    v10 = val(U0, g, Gall, 0.10) if g else U0 / 0.10
    e = irr(U0, g, Gall, CAP + nd_now - shelter) if g else U0 / (CAP + nd_now - shelter)
    print(f"  {name:20s} 5.43%: {(v - nd_now + shelter)/SH:7.2f}/sh | 10%: {(v10 - nd_now + shelter10)/SH:7.2f}/sh | EV return {e*100:5.2f}%")
a_n = (U0 / 0.10 - nd_now + shelter10) / SH; a_g = (val(U0, g_ex16, Gall, 0.10) - nd_now + shelter10) / SH
print(f"  FAIR all-equity (avg ends at 10%): {(a_n + a_g)/2:.2f}")
# MERGER beside: NorthWestern's own filed record (XBRL, CIKs 1993004 / 73088)
nOCF = [220.0, 307.2, 489.2, 406.7, 394.5]; nSBC = [5.3, 5.5, 5.2, 4.7, 7.0]; nDA = [187.5, 195.0, 210.5, 227.6, 249.5]
nCAP = [434.3, 515.1, 566.9, 549.2, 524.5]; nDEF = [0.5, -9.0, 6.6, -9.0, 7.1]
nM = [a - b - c - d for a, b, c, d in zip(nOCF, nSBC, nDA, nDEF)]
pOCF = [286.8, 322.7, 382.0, 296.7, 352.1]; pSBC = [6.7, 5.6, 7.7, 8.0, 4.1]; pDA = [159.3, 166.1, 174.5, 172.9, 179.6]; pDEF = [-8.2, 12.4, -13.2, -13.9, -7.6]
pM = [a - b - c - d for a, b, c, d in zip(pOCF, pSBC, pDA, pDEF)]
nM0 = sum(nM) / 5; npM = sum(pM) / 5
n_credit = (3286.0 + 150.0 - 8.8) - (2315.3 + 100.0 - 5.8)
n_gw = sum(nCAP) - sum(nDA); n_cap = 0.543 * sum(nCAP)
nG = (n_gw - min(n_credit, n_cap)) / 5
print(f"\nNWE M by year {[round(x,1) for x in nM]} avg {nM0:.1f}; prior {[round(x,1) for x in pM]} avg {npM:.1f}")
print(f"NWE capex {sum(nCAP):.1f}, D&A {sum(nDA):.1f}, growth spending {n_gw:.1f}; net debt raised {n_credit:.1f}; cap 54.3% x capex {n_cap:.1f}; x growth {0.543*n_gw:.1f}; G {nG:.1f}")
cM0 = M0 + nM0; cG = G + nG; cprior = avg(M, range(2017, 2021)) + sum(pM[1:]) / 4
cg = (cM0 / cprior) ** (1 / 4.5) - 1
cSH = SH + 60.194486
print(f"COMBINED: M0 {cM0:.1f}, G {cG:.1f}, growth (2017-20 vs 2021-25) {cg*100:.2f}%, shares {cSH:.2f}")
for name, g, Gs in [("no growth", 0.0, 0.0), ("growth", cg, cG)]:
    v = val(cM0, g, Gs, r) if g else cM0 / r
    v10 = val(cM0, g, Gs, 0.10) if g else cM0 / 0.10
    print(f"  {name:10s} 5.43%: {(v+shelter)/cSH:6.2f}/sh | 10%: {(v10+shelter10)/cSH:6.2f}/sh")
cf = ((cM0 / 0.10) + val(cM0, cg, cG, 0.10) + 2 * shelter10) / 2 / cSH
print(f"  FAIR combined equity-only: {cf:.2f}  (NWE NOL shelter not added: 452.2 x 21% = {452.2*.21:.0f}, {452.2*.21/cSH:.2f}/sh nominal)")
