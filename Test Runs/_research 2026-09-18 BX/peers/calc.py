# fee rate = FY2025 fee line / avg(YE2024, YE2025 fee-earning capital); growth = YE2025/YE2024 - 1; FRE growth FY25/FY24 - 1
R = {  # fee FY25, fee FY24 (same units as feaum? no: fee $M, feaum $M), YE23, YE24, YE25, FRE25, FRE24
 "BX":   (8075.601, 762607.902, 830708.603, 921674.454, 5737.537, 5282.065, 7548.857),
 "KKR":  (2496.783, None, 511963, 604144, 3714.313, 3267.796, 4100.841),
 "APO":  (2378, 492952, 568666, 709139, 2528, 2063, 3391),
 "CG":   (2396.6, 307418, 304358, 336778, 1236.2, 1104.6, None),
 "ARES": (3680.467, 262357, 292553, 384949, 1775.300, 1361.737, None),
 "OWL":  (2521.937, 102696, 159794, 187735, 1496.536, 1253.366, None),
 "TPG":  (1826.411, 136794, 141286, 170102, 952.572, 764.228, None),
 "BAM":  (4896, 456998, 538541, 602714, None, None, None),
 "BLK":  (19179, None, 11551251, 14041518, None, None, None),
 "TROW": (6602.3, None, 1606600, 1775600, None, None, None),
}
for k,(fee,y23,y24,y25,f25,f24,seg) in R.items():
    rate = fee/((y24+y25)/2)*1e4
    s = f"{k:5} rate {rate:6.1f}bp"
    if seg: s += f" (segment/base line {seg/((y24+y25)/2)*1e4:5.1f}bp)"
    s += f" | FEAUM YE24->25 {100*(y25/y24-1):5.1f}%"
    if y23: s += f" | CAGR 23-25 {100*((y25/y23)**0.5-1):5.1f}%"
    if f25: s += f" | FRE FY24->25 {100*(f25/f24-1):5.1f}%"
    print(s)
