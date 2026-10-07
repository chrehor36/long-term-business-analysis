import json, sys
sys.stdout.reconfigure(encoding="utf-8")
def inst(t, tag):
    g=json.load(open(f"{t}_companyfacts.json"))["facts"]["us-gaap"]
    out={}
    for x in g.get(tag,{}).get("units",{}).get("USD",[]):
        if x.get("form")!="10-K" or "start" in x: continue
        e=x["end"]
        if e[5:7] not in ("12",): continue
        y=e[:4]
        if y not in out or x["filed"]>out[y][1]: out[y]=(x["val"],x["filed"])
    return {k:v[0]/1e6 for k,v in out.items()}
# KO NTOA from the PEP research file (filed faces, formula stated there)
ntoa={"2021":32402,"2022":30553,"2023":34096,"2024":32267,"2025":43638}
oi={"2021":10308,"2022":10909,"2023":11311,"2024":9992,"2025":13762}
occ={"2021":846,"2022":1215,"2023":1951,"2024":4163,"2025":1261}
eq=inst("KO","EquityMethodInvestments")
hfs_a={"2024":131,"2025":5342}; hfs_l={"2024":3,"2025":2570}
for y in sorted(ntoa):
    e=eq.get(y); d=ntoa[y]-e-(hfs_a.get(y,0)-hfs_l.get(y,0))
    print(y, "EMI", e, "NTOA ex EMI & HFS net", round(d), "OI/that", f"{100*oi[y]/d:.1f}%", "(OI+other op charges)/that", f"{100*(oi[y]+occ[y])/d:.1f}%")
print("PEP EMI", inst("PEP","EquityMethodInvestments"))
print("PEP other", {k:v for k,v in inst("PEP","LongTermInvestments").items() if k>='2021'})
