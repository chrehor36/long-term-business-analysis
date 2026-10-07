"""GFS Q2/Q4 series from the FILED statements, transcribed by hand from the 20-F cash-flow statements, income statements and
balance sheets (FY2021 20-F for 2019-2020 in thousands, rounded; FY2022-FY2025 in millions). Arithmetic only."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
# year: revenue, gross profit, net income (attrib. to shareholders where filed; total for 2019-2022), parent equity end,
#       OCF, D&A (cash-flow add-back), SBC (cash-flow add-back), capex (PP&E + intangibles), grant proceeds (investing + financing),
#       proceeds from sale of PP&E/intangibles, contract liabilities end, customer advances (purchase orders) end
D = {
 2019: dict(rev=5812.8, gp=-532.2, ni=-1371.2, eq=None,    ocf=496.8,  da=2678.2, sbc=0.0,   capex=772.8,  grants=335.2, ppe_sale=252.2, cl=144.6,  adv=None),
 2020: dict(rev=4851.0, gp=-712.0, ni=-1353.0, eq=7176.4,  ocf=1004.0, da=2522.0, sbc=1.0,   capex=592.0,  grants=312.0, ppe_sale=109.0, cl=134.7,  adv=34.7),
 2021: dict(rev=6585.0, gp=1013.0, ni=-254.0,  eq=7975.0,  ocf=2839.0, da=1618.0, sbc=223.0, capex=1767.0, grants=83.0,  ppe_sale=324.0, cl=1901.3, adv=117.9),
 2022: dict(rev=8108.0, gp=2239.0, ni=1446.0,  eq=9913.0,  ocf=2624.0, da=1623.0, sbc=181.0, capex=3059.0, grants=93.0,  ppe_sale=41.0,  cl=1918.0, adv=73.0),
 2023: dict(rev=7392.0, gp=2101.0, ni=1020.0,  eq=11104.0, ocf=2125.0, da=1451.0, sbc=150.0, capex=1804.0, grants=143.0, ppe_sale=24.0,  cl=1983.0, adv=22.0),
 2024: dict(rev=6750.0, gp=1651.0, ni=-265.0,  eq=10776.0, ocf=1722.0, da=1568.0, sbc=186.0, capex=625.0,  grants=10.0,  ppe_sale=56.0,  cl=1584.0, adv=36.0),
 2025: dict(rev=6791.0, gp=1690.0, ni=885.0,   eq=11928.0, ocf=1731.0, da=1314.0, sbc=200.0, capex=722.0,  grants=148.0, ppe_sale=170.0, cl=1230.0, adv=13.0),
}
eq2019 = 9020.0  # total equity 2019-12-31 (companyfacts ifrs-full:Equity; parent split not filed for 2019); NCI ~ 65-50
out = {}
for y, d in D.items():
    prev = D.get(y - 1)
    e0 = (prev["eq"] if prev and prev["eq"] else (eq2019 if y == 2020 else None))
    roe = d["ni"] / ((e0 + d["eq"]) / 2) * 100 if e0 and d["eq"] else None
    out[y] = dict(gm=round(d["gp"] / d["rev"] * 100, 1), roe=roe and round(roe, 1),
                  capex_rev=round(d["capex"] / d["rev"] * 100, 1), capex_da=round(d["capex"] / d["da"], 2),
                  net_capex_da=round((d["capex"] - d["grants"]) / d["da"], 2), da_rev=round(d["da"] / d["rev"] * 100, 1))
    print(y, out[y])
r = lambda a, b: round((D[b]["rev"] / D[a]["rev"]), 3)
print("revenue multiple 2019->2025", r(2019, 2025), "2021->2025", r(2021, 2025))
for a, b in ((2019, 2025), (2021, 2025), (2023, 2025)):
    cx = sum(D[y]["capex"] for y in range(a, b + 1)); da = sum(D[y]["da"] for y in range(a, b + 1)); g = sum(D[y]["grants"] for y in range(a, b + 1))
    print(f"{a}-{b}: capex {cx:,.0f} grants {g:,.0f} D&A {da:,.0f} capex/D&A {cx/da:.2f} net {((cx-g)/da):.2f}")
roes = [out[y]["roe"] for y in range(2021, 2026)]
print("5-yr mean ROE 2021-25", round(sum(roes) / 5, 1))
json.dump({"inputs": D, "derived": out}, open(os.path.join(HERE, "row_out.json"), "w"), indent=1)
