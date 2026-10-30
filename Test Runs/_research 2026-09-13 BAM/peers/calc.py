# Arithmetic only. Every input is transcribed from the 10-K text files in this folder (see peer_row.md).
# Units: each row keeps the filer's own unit; ratios are unit-free.
rows = {
 # ticker: (fee label, fee FY2025, [(alt label, alt fee)], FEAUM YE23, YE24, YE25, FRE25, FRR25, FRE24, FRR24)
 "BX":   ("GAAP Management and Advisory Fees, Net ($000)", 8075601, [("segment Base Management Fees ($000)", 7548857)], 762607902, 830708603, 921674454, 5737537, 8016049+1825428, 5282065, 7133534+2135945),
 "KKR":  ("GAAP Management Fees, Note 3 ($000)", 2496783, [("asset management segment Management Fees ($000)", 4100841)], None, 511963, 604144, 3714313, 4100841+1092577+181784, 3267796, 3461381+1165884+137992),
 "APO":  ("GAAP Management fees ($m)", 2378, [("Asset Management segment Management fees ($m)", 3391)], 492952, 568666, 709139, 2528, 3391+808+266, 2063, 2776+668+208),
 "CG":   ("GAAP Fund management fees ($m)", 2396.6, [("segment Fund management fees ($m)", 2243.1)], 307418, 304358, 336778, 1236.2, 2642.7, 1104.6, 2403.8),
 "ARES": ("GAAP Management fees ($000)", 3680467, [("segment Management fees, Total ($000)", 3682922)], 262357, 292553, 384949, 1775300, 3682922+301309+272707, 1361737, 2957430+231537+91879),
 "OWL":  ("GAAP Management fees, net ($000)", 2521937, [], 102696, 159794, 187735, 1496536, 2654712, 1253366, 2170563),
 "TPG":  ("GAAP Management fees ($000)", 1826411, [("non-GAAP FRE table Management fees ($000)", 1800061)], 136794, 141286, 170102, 952572, 2109255, 764228, 1831457),
 "BLK":  ("GAAP Total investment advisory, administration fees and securities lending revenue ($m)", 19179, [("GAAP Investment advisory and administration fees ($m)", 18474)], 10008995, 11551251, 14041518, None, None, None, None),
 "TROW": ("GAAP Investment advisory fees ($m)", 6602.3, [], 1444.5, 1606.6, 1775.6, None, None, None, None),
}
# unit of FEAUM per ticker relative to fee unit: multiply FEAUM by k to get the fee unit
k = {"BX": 1, "KKR": 1000, "APO": 1, "CG": 1, "ARES": 1000, "OWL": 1000, "TPG": 1000, "BLK": 1, "TROW": 1000}
for t, r in rows.items():
    lab, fee, alts, y23, y24, y25, fre25, frr25, fre24, frr24 = r
    avg = (y24 + y25) / 2
    bps = fee / (avg * k[t]) * 1e4
    print(f"{t}: {lab} {fee:,} / avg({y24:,}, {y25:,}) = {fee:,} / {avg:,.1f} x{k[t]} = {bps:.1f} bps")
    for al, af in alts:
        print(f"    alt {al}: {af:,} / {avg*k[t]:,.1f} = {af/(avg*k[t])*1e4:.1f} bps")
    if y23:
        c = (y25 / y23) ** 0.5 - 1
        print(f"    CAGR 2023-25: ({y25:,}/{y23:,})^(1/2)-1 = {c*100:.1f}%")
    if fre25:
        print(f"    FRE margin 2025: {fre25:,} / {frr25:,} = {fre25/frr25*100:.1f}%;  2024: {fre24:,} / {frr24:,} = {fre24/frr24*100:.1f}%")
# KKR 2023 FPAUM from rounded business-line tables ($bn)
print("KKR FPAUM YE2023 sum of business lines 108+112+226 =", 108+112+226, "$bn; CAGR (604.144/446)^0.5-1 =", round(((604.144/446)**0.5-1)*100, 1))
print("KKR segment mgmt fees 2023 sum 1286+826+919 =", 1286+826+919, "$m")
print("OWL FRE before NCI margin 1,547,525/2,654,712 =", round(1547525/2654712*100, 2))
print("BLK avg-AUM basis: 19,179/12,603,633 =", round(19179/12603633*1e4, 2), "bps; 18,474/12,603,633 =", round(18474/12603633*1e4, 2))
print("BLK GAAP op margin 7,045/24,216 =", round(7045/24216*100, 1), "; TROW GAAP op margin 2,188.8/7,314.8 =", round(2188.8/7314.8*100, 1), "; 2024", round(2333.3/7093.6*100,1))
print("TROW EFR check 6,602.3/1,677.3 avg AUM =", round(6602.3/1677.3*1e4, 1), "bps")
print("Perpetual shares: BX 523.6/1274.931 =", round(523.6/1274.931*100, 1), "% of Total AUM; APO 535.6/938.4 =", round(535.6/938.4*100, 1), "%; CG FEAUM 110.9/336.778 =", round(110.9/336.778*100, 1), "% and AUM 115.4/477 =", round(115.4/477*100, 1), "%; CG ex-Fortitude FEAUM 30.5/336.778 =", round(30.5/336.778*100,1), "%")
print("APO consolidated OCF check 7,263 + (17) =", 7263-17, "; CG -3,275.5 = 1,088.6 + (4,364.1) =", round(1088.6-4364.1,1), "; ARES 2,113,088+1,153,871 =", 2113088+1153871)
