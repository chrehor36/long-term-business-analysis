import json, urllib.request, os, time
from datetime import date
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"}
base=os.path.join(os.path.dirname(os.path.abspath(__file__)),"cache")
def series(g,tags):
    out={}
    for t in tags:
        for f in g.get(t,{}).get("units",{}).get("USD",[]):
            if f.get("form")=="10-K" and "start" in f:
                s=date.fromisoformat(f["start"]);e=date.fromisoformat(f["end"])
                if 350<(e-s).days<380 and f["end"]>="2020-12-01":
                    out.setdefault(f["end"][:4],(f["val"],f["accn"]))
        if out: return out,t
    return out,None
for name,cik in [("Xylem",1524472),("Pentair",77360),("AECOM",868857)]:
    p=os.path.join(base,f"peer_{cik}_facts.json")
    if not os.path.exists(p):
        open(p,"wb").write(urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json",headers=UA)).read()); time.sleep(0.3)
    g=json.load(open(p))["facts"]["us-gaap"]
    rev,rt=series(g,["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet"])
    op,ot=series(g,["OperatingIncomeLoss"])
    print(name,rt,ot)
    for y in sorted(rev):
        if y in op: print("  ",y,round(rev[y][0]/1e6),round(op[y][0]/1e6),f"{op[y][0]/rev[y][0]*100:.1f}%",op[y][1])
