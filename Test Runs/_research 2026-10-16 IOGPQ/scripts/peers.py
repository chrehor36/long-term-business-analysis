import json, urllib.request, os, sys
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def facts(cik):
    p=f"cache/facts_{cik}.json"
    if not os.path.exists(p):
        open(p,"wb").write(urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json",headers=UA),timeout=60).read())
    return json.load(open(p,encoding="utf-8"))
def annual(f, tags):
    out={}
    for ns in f["facts"]:
        for t in tags:
            if t in f["facts"][ns]:
                for u,vals in f["facts"][ns][t]["units"].items():
                    for v in vals:
                        if v.get("form") in ("10-K","20-F","10-K/A","20-F/A") and v.get("fp")=="FY" and "start" in v:
                            from datetime import date
                            s=date.fromisoformat(v["start"]); e=date.fromisoformat(v["end"])
                            if 340<(e-s).days<380:
                                key=v["end"][:4]
                                out.setdefault(key,(v["val"],v["accn"],t,u))  # earliest filed kept
    return out
for name,cik in [("ION",866609),("SLB",87347),("CGG",1037962),("GEOS",1001115)]:
    f=facts(cik)
    rev=annual(f,["Revenues","SalesRevenueNet","RevenueFromContractWithCustomerExcludingAssessedTax","Revenue"])
    op=annual(f,["OperatingIncomeLoss","ProfitLossFromOperatingActivities"])
    print("==",name)
    for y in sorted(set(rev)|set(op)):
        if y<"2010": continue
        r=rev.get(y); o=op.get(y)
        m = f"{o[0]/r[0]*100:6.1f}%" if r and o and r[0] else "   n/a"
        print(y, r and f"rev {r[0]/1e6:10.1f} {r[3]} {r[1]}", o and f"op {o[0]/1e6:9.1f} {o[1]} {o[2]}", m)
