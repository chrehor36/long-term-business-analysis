# Return on equity (profit attributable to owners / year-end equity attributable to owners), from each filer's own
# five-year summary: ENN (AR2025 ten-year comparison), China Resources Gas 1193.HK (AR2025, AR2020 financial summaries,
# HK$'000), China Gas Holdings 0384.HK (AR2025/26, AR2020/21 financial summaries, years to 31 March, HK$'000),
# Towngas Smart Energy 1083.HK (AR2025, AR2020 five-year summaries). Also the parts table from ENN's segment notes.
enn_p = [2151, 2802, 2818, 5670, 6278, 7755, 5867, 6816, 5987, 5904]
enn_e = [14966, 16952, 21385, 25868, 30561, 35777, 39040, 42660, 45101, 47825]
crg_p = [3289399, 3653994, 4450101, 5043477, 5151292, 6395368, 4733455, 5223705, 4088148, 3546793]
crg_e = [17768243, 21992648, 24081120, 26795437, 36274287, 41256915, 39307612, 40772231, 41171967, 44176114]
cg_p = [4147732, 6095153, 8224382, 9188474, 10478683, 7662036, 4293484, 3184939, 3251614, 2719049]   # FY to Mar 2017..2026
cg_e = [20550233, 28455996, 35321051, 39604964, 51936860, 63577893, 57900584, 53927655, 53864695, 57173594]
tg_p = [974, 1365, 1224, 1308, 1447, 1253, 965, 1575, 1606, 1585]
tg_e = [13499, 15845, 16229, 18612, 20723, 22895, 21505, 22847, 23448, 25722]
print("year  ENN    CRGas  ChinaGas(FY Mar+1) TownGasSE")
for i, y in enumerate(range(2016, 2026)):
    f = lambda p, e: p[i] / e[i] * 100
    print(f"{y}  {f(enn_p,enn_e):5.1f}  {f(crg_p,crg_e):5.1f}  {f(cg_p,cg_e):5.1f}              {f(tg_p,tg_e):5.1f}")
for nm, p, e in [("ENN", enn_p, enn_e), ("CRGas", crg_p, crg_e), ("ChinaGas", cg_p, cg_e), ("TownGasSE", tg_p, tg_e)]:
    print(nm, "10-yr avg ROE %.1f%%" % (sum(a / b for a, b in zip(p, e)) / 10 * 100), "| 2016-20 %.1f%% | 2021-25 %.1f%%" % (
        sum(a / b for a, b in zip(p[:5], e[:5])) / 5 * 100, sum(a / b for a, b in zip(p[5:], e[5:])) / 5 * 100))
seg = {"Retail gas": [6164, 6445, 6049, 6225, 6127], "Integrated energy": [1365, 1556, 1907, 2220, 2338],
       "Wholesale of gas": [358, 2736, 1095, 94, 51], "Construction and installation": [4446, 2941, 2770, 1895, 1662],
       "Value added / smart home": [1723, 2078, 2517, 2971, 3114]}
tot = sum(sum(v) for v in seg.values())
print("\nParts table, segment profit 2021-2025 (RMB m):", tot)
for k, v in seg.items(): print(f"  {k:30s} {sum(v):6d} {sum(v)/tot*100:5.1f}%  2021 {v[0]} -> 2025 {v[-1]}")
