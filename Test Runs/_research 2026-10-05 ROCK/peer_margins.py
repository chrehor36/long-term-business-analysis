import json
def series(t):
    f=json.load(open(f"{t}_facts.json")); g=f["facts"]["us-gaap"]
    def ann(tags):
        out={}
        for tag in tags:
            if tag not in g: continue
            for x in g[tag]["units"]["USD"]:
                if x["form"]!="10-K": continue
                fr=x.get("frame","")
                if fr.startswith("CY") and len(fr)==6: out.setdefault(int(fr[2:]),(x["val"],x["accn"]))
        return out
    s=ann(["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet"]); o=ann(["OperatingIncomeLoss"])
    return {y:(s[y][0]/1e6,o[y][0]/1e6,100*o[y][0]/s[y][0],o[y][1]) for y in s if y in o and y>=2015}
for t in ["SSD","NX","ARRY"]:
    d=series(t); print(t)
    for y in sorted(d): print("  ",y,"sales %.1f OI %.1f margin %.1f%% accn %s"%d[y])
