import json, sys
sys.path.insert(0, sys.argv[0].rsplit("/",1)[0]); sys.stdout.reconfigure(encoding="utf-8")
from fetch import get
from datetime import date
peers={"PWR":"0001050915","MYRG":"0000700923","PRIM":"0001361538"}
def series(g,tag):
    out={}
    if tag not in g: return out
    for u,vals in g[tag]["units"].items():
        for v in vals:
            if v.get("form")!="10-K": continue
            if "start" in v and (date.fromisoformat(v["end"])-date.fromisoformat(v["start"])).days<350: continue
            yr=int(v["end"][:4]) if v["end"][5:7]!="01" else int(v["end"][:4])-1
            out.setdefault(yr,(v["val"]/1e6,v["accn"]))
    return out
for t,cik in peers.items():
    d=json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json")); g=d["facts"]["us-gaap"]
    rev=series(g,"RevenueFromContractWithCustomerExcludingAssessedTax"); oi=series(g,"OperatingIncomeLoss")
    ocf=series(g,"NetCashProvidedByUsedInOperatingActivities"); cx=series(g,"PaymentsToAcquirePropertyPlantAndEquipment"); sbc=series(g,"ShareBasedCompensation")
    a=series(g,"Assets"); gw=series(g,"Goodwill"); ia=series(g,"IntangibleAssetsNetExcludingGoodwill")
    print("==",t,d["entityName"])
    yrs=[y for y in range(2016,2026) if y in rev and y in oi]
    print("op margin %: "+" ".join(f"{y}:{oi[y][0]/rev[y][0]*100:.1f}" for y in yrs))
    h1=[y for y in yrs if y<=2020]; h2=[y for y in yrs if y>=2021]
    for nm,hs in (("2016-20",h1),("2021-25",h2)):
        print(f"  {nm} op margin (sum/sum) {sum(oi[y][0] for y in hs)/sum(rev[y][0] for y in hs)*100:.1f}%")
    oy=[y for y in yrs if y in ocf and y in cx and y in sbc]
    oc={y:ocf[y][0]-sbc[y][0]-cx[y][0] for y in oy}
    print("  owner cash (OCF-SBC-capex)/revenue by year: "+" ".join(f"{y}:{oc[y]/rev[y][0]*100:.1f}" for y in oy))
    print(f"  owner cash/revenue over {oy[0]}-{oy[-1]}: {sum(oc.values())/sum(rev[y][0] for y in oy)*100:.1f}%")
    ta=[y for y in yrs if y in a and y in gw and y in ia]
    print("  pre-tax op income / tangible assets %: "+" ".join(f"{y}:{oi[y][0]/(a[y][0]-gw[y][0]-ia[y][0])*100:.1f}" for y in ta))
    print("  revenue: "+" ".join(f"{y}:{rev[y][0]:.0f}" for y in yrs))
    print("  FY2025 accession:", rev[2025][1], " FY2016 first-filed accession:", rev[2016][1])
