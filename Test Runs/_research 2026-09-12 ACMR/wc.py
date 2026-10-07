import json, io
d=json.load(io.open("Test Runs/_research 2026-09-12 ACMR/companyfacts.json",encoding="utf-8"))
us=d["facts"]["us-gaap"]
def inst(tag):
    out={}
    for f in us.get(tag,{}).get("units",{}).get("USD",[]):
        if f.get("form") not in ("10-K","10-K/A") or f.get("start") or not f["end"].endswith("12-31"): continue
        k=f["end"][:4]; p=out.get(k)
        if p is None or f["filed"]>p[1]: out[k]=(f["val"],f["filed"])
    return {k:v[0] for k,v in sorted(out.items())}
ar=inst("AccountsReceivableNetCurrent"); inv=inst("InventoryNet")
rev={"2018":74643,"2019":107524,"2020":156624,"2021":259751,"2022":388832,"2023":557723,"2024":782118,"2025":901309}
cor={"2018":40194,"2019":56870,"2020":87025,"2021":144895,"2022":205217,"2023":281508,"2024":390564,"2025":501242}
print("year   AR($k)    DSO   INV($k)   inv-months-of-COGS   (AR+INV)/rev")
for y in rev:
    a=ar.get(y); i=inv.get(y)
    if a is None or i is None: print(y, a, i); continue
    a/=1000; i/=1000
    print(f"{y}  {a:>9,.0f}  {a/rev[y]*365:>5.0f}  {i:>9,.0f}   {i/cor[y]*12:>6.1f}              {(a+i)/rev[y]*100:>5.0f}%")
