import json, sys
sys.stdout.reconfigure(encoding="utf-8")
def series(f, tag, dur=True):
    if tag not in f: return {}
    out = {}
    for unit in f[tag]["units"].values():
        for x in unit:
            if not x.get("form","").startswith("10-K") or x.get("fp")!="FY": continue
            if dur:
                s=x.get("start"); e=x["end"]
                if not s: continue
                m=(int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])
                if m<11 or m>13: continue
            out.setdefault(x["end"], (x["val"], x["accn"]))
    return out
for t in sys.argv[1:]:
    f=json.load(open(f"cache/peer_{t}.json"))["facts"]["us-gaap"]
    rev={}
    for tag in ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet"]:
        for k,v in series(f,tag).items(): rev.setdefault(k,v)
    oi=series(f,"OperatingIncomeLoss")
    eq=series(f,"StockholdersEquity",False); gw=series(f,"Goodwill",False)
    ia=series(f,"IntangibleAssetsNetExcludingGoodwill",False)
    print(t)
    for e in sorted(oi):
        if e<"2020-06": continue
        r=rev.get(e,(None,""))[0]; o=oi[e][0]
        te=(eq.get(e,(0,))[0]-gw.get(e,(0,))[0]-ia.get(e,(0,))[0])
        print(f"  {e}  rev {r/1e6 if r else 0:9.0f}M  opinc {o/1e6:7.0f}M  margin {100*o/r if r else 0:5.1f}%  tangible equity {te/1e6:7.0f}M  opinc/tang.eq {100*o/te if te else 0:5.1f}%  accn {oi[e][1]}")
