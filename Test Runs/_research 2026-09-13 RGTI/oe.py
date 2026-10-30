# Owner earnings for RGTI, $K, from filed cash-flow statements (10-K FY2022, FY2025; 10-Q Q2 2026; 8-K 2022-03-07 EX-99.1 for FY Jan-2021).
# OE = OCF - SBC - (c); (c) = capex end or D&A end.  All values in thousands.
Y = {
 "FYJan21(12m)": dict(rev=5543, ocf=-30067, sbc=2592, capex=4400, da=4299, interest=0),
 "FY21(11m)":    dict(rev=8196, ocf=-29044, sbc=1765, capex=7008, da=4651),
 "FY22":         dict(rev=13102, ocf=-62689, sbc=44812, capex=22737, da=7017),
 "FY23":         dict(rev=12008, ocf=-50579, sbc=12409, capex=9059, da=7426),
 "FY24":         dict(rev=10790, ocf=-50627, sbc=13069, capex=11098, da=6906),
 "FY25":         dict(rev=7088, ocf=-58543, sbc=17605, capex=18676, da=8169),
}
H125 = dict(rev=3273, ocf=-29820, sbc=7728, capex=8214, da=3723)
H126 = dict(rev=9538, ocf=-31993, sbc=12910, capex=16404, da=5484)
Y["TTM 2026-06"] = {k: Y["FY25"][k]-H125[k]+H126[k] for k in H125}
for k,v in Y.items():
    v["oe_capex"] = v["ocf"]-v["sbc"]-v["capex"]; v["oe_da"] = v["ocf"]-v["sbc"]-v["da"]
    print(f'{k:14} rev {v["rev"]:>8,} ocf {v["ocf"]:>9,} sbc {v["sbc"]:>7,} capex {v["capex"]:>7,} da {v["da"]:>6,}  OE@capex {v["oe_capex"]:>9,}  OE@D&A {v["oe_da"]:>9,}  SBC/rev {v["sbc"]/v["rev"]*100:6.1f}%')
def win(keys):
    n=len(keys); c=sum(Y[k]["oe_capex"] for k in keys)/n; d=sum(Y[k]["oe_da"] for k in keys)/n
    return c,d
W = {"5 periods FY21(11m)-FY25": ["FY21(11m)","FY22","FY23","FY24","FY25"],
     "4y FY22-FY25": ["FY22","FY23","FY24","FY25"], "3y FY23-FY25": ["FY23","FY24","FY25"],
     "2y FY24-FY25": ["FY24","FY25"], "TTM": ["TTM 2026-06"],
     "6 periods FYJan21-FY25 (Legacy Rigetti 8-K EX-99.1 + 10-Ks)": ["FYJan21(12m)","FY21(11m)","FY22","FY23","FY24","FY25"]}
allv=[]
for name,keys in W.items():
    c,d=win(keys); allv += [c,d]
    print(f"{name:60} mean OE capex end {c:>9,.0f}  D&A end {d:>9,.0f}")
print("range", min(allv), max(allv))
# cumulative
keys=["FY21(11m)","FY22","FY23","FY24","FY25"]
cum = {f: sum(Y[k][f] for k in keys)+H126[f] for f in ["rev","ocf","sbc","capex","da"]}
print("cum FY21(11m)..H1-26", cum, "SBC/rev", cum["sbc"]/cum["rev"])
