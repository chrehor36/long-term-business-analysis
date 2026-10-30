"""UMC owner earnings, NT$ millions, from the filed cash-flow statements (cfread_out.json; each figure from the newest 20-F
that carries the year). Construction (CONVENTION, framework VI): OCF - dividends received (listed stakes valued at market in Q5)
- equity-settled SBC add-back - (c). (c): capex end = PP&E + intangibles - asset grants; judged end = K x (dep + amort), K the
full-decade 2016-2025 ratio of that net capex to D&A. D&A end INVALID [E5-20], displayed only. Arithmetic only."""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
cf = json.load(open(os.path.join(H, "cfread_out.json")))
def c(k, y):
    d = cf[k][y]; return d[max(d)]
yrs = [str(y) for y in range(2015, 2026)]
row = {}
for y in yrs:
    ocf = c("ocf", y); divr = c("div_recd", y); sbc = c("sbc", y)
    net_capex = -c("capex", y) - c("intang", y) - c("grants", y)
    da = c("dep", y) + c("amort", y)
    row[y] = dict(ocf=ocf, div_recd=divr, sbc=sbc, net_capex=net_capex, da=da, int_recd=c("int_recd", y), int_paid=-c("int_paid", y))
dec = [str(y) for y in range(2016, 2026)]
K = sum(row[y]["net_capex"] for y in dec) / sum(row[y]["da"] for y in dec)
# H1 2026 and H1 2025 from the Q2 2026 consolidated report (TIFRS translation), for a TTM display
h1_26 = dict(ocf=55678.697, div_recd=1050.194, sbc=475.002, net_capex=21348.637+1339.043-3781.133, da=30813.547+1411.485)
h1_25 = dict(ocf=45923.736, div_recd=290.309, sbc=427.219, net_capex=21695.646+1373.894-3722.471, da=27227.474+1406.668)
ttm = {k: row["2025"][k] + h1_26[k] - h1_25[k] for k in h1_26}
row["TTM"] = ttm
for y, r in row.items():
    base = r["ocf"] - r["div_recd"] - r["sbc"]
    r["base"] = base; r["oe_capex"] = base - r["net_capex"]; r["oe_judged"] = base - K * r["da"]; r["oe_da"] = base - r["da"]
    r["capex_da"] = r["net_capex"] / r["da"]
print(f"K (2016-2025 net capex / D&A) = {K:.3f}")
print("year |    OCF  -divR  -SBC | netcapex    D&A | OE capex | OE judged | OE D&A(INVALID) | capex/DA")
for y, r in row.items():
    print(f"{y:5s}| {r['ocf']:7,.0f} {r['div_recd']:6,.0f} {r['sbc']:5,.0f} | {r['net_capex']:8,.0f} {r['da']:6,.0f} | {r['oe_capex']:8,.0f} | {r['oe_judged']:9,.0f} | {r['oe_da']:8,.0f} | {r['capex_da']:.2f}")
W = {"5-yr 2021-2025": [str(y) for y in range(2021, 2026)], "10-yr 2016-2025": dec, "3-yr 2023-2025": ["2023", "2024", "2025"],
     "prior 5-yr 2016-2020": [str(y) for y in range(2016, 2021)], "11-yr 2015-2025": yrs}
win = {}
for n, ys in W.items():
    m = lambda k: sum(row[y][k] for y in ys) / len(ys)
    win[n] = dict(oe_capex=m("oe_capex"), oe_judged=m("oe_judged"), oe_da=m("oe_da"), div_recd=m("div_recd"), net_int=m("int_recd") - m("int_paid"))
    print(f"{n:22s} capex {win[n]['oe_capex']:8,.0f}  judged {win[n]['oe_judged']:8,.0f}  D&A {win[n]['oe_da']:8,.0f}  (div recd {win[n]['div_recd']:,.0f}; net interest {win[n]['net_int']:,.0f})")
acq = {"2019 USJC (Mie) acquisition, investing": 12800.981, "2023 USCXM minority buy-out, financing 'Decrease in other financial liabilities'": 21209.443, "2017 acquisition of NCI": 1308.614}
print("acquisitions of capacity outside capex:", acq, "10-yr total", round(sum(acq.values()) - 1308.614), "per yr", round((sum(acq.values()) - 1308.614) / 10))
json.dump(dict(K=K, rows=row, windows=win, acquisitions=acq), open(os.path.join(H, "oe_out.json"), "w"), indent=1)
