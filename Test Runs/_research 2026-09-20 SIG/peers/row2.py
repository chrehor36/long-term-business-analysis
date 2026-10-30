import json, os
from datetime import date
D=os.path.dirname(os.path.abspath(__file__))
T={"REV":["RevenueFromContractWithCustomerExcludingAssessedTax","Revenues","SalesRevenueNet"],
   "COGS":["CostOfGoodsAndServicesSold","CostOfRevenue","CostOfGoodsSold"],
   "OPINC":["OperatingIncomeLoss"],
   "ASSETS":["Assets"],"GW":["Goodwill"],
   "INTANG":["IntangibleAssetsNetExcludingGoodwill","FiniteLivedIntangibleAssetsNet"],
   "CASH":["CashAndCashEquivalentsAtCarryingValue"],
   "CURLIAB":["LiabilitiesCurrent"]}
def ann(g,tags,pit=False):
    out={}
    for t in tags:
        if t not in g: continue
        for unit,rows in g[t]["units"].items():
            if unit!="USD": continue
            for r in rows:
                if r.get("form") not in ("10-K","10-K/A"): continue
                if pit:
                    if "start" in r: continue
                else:
                    if "start" not in r: continue
                    s=date.fromisoformat(r["start"]); e=date.fromisoformat(r["end"])
                    if not (330<(e-s).days<400): continue
                k=r["end"]
                if k not in out or r["filed"]>out[k][1]: out[k]=(r["val"]/1e6,r["filed"])
    return out
print(f"{'tk':5} {'FYend':11} {'rev':>8} {'GM%':>6} {'OM%':>7} {'OpInc':>8} {'TangCapEmp':>11} {'OpInc/TCE%':>10}")
for tk in ["SIG","BRLT","MOV","FOSL","TPR"]:
    g=json.load(open(os.path.join(D,f"{tk}_companyfacts.json")))["facts"]["us-gaap"]
    res={k:ann(g,v,pit=k in("ASSETS","GW","INTANG","CASH","CURLIAB")) for k,v in T.items()}
    for e in sorted(set(res["REV"]))[-4:]:
        f=lambda k,d=None: (res[k].get(e) or (d,))[0]
        rev,cogs,op = f("REV"),f("COGS"),f("OPINC")
        a,cash,gw,it,cl = f("ASSETS"),f("CASH",0) or 0,f("GW",0) or 0,f("INTANG",0) or 0,f("CURLIAB")
        gm=(1-cogs/rev)*100 if rev and cogs else float('nan')
        om=op/rev*100 if rev and op is not None else float('nan')
        tce=(a-cash-gw-it-cl) if a is not None and cl is not None else float('nan')
        r=op/tce*100 if op is not None and tce and tce==tce else float('nan')
        print(f"{tk:5} {e:11} {rev or 0:8.1f} {gm:6.1f} {om:7.1f} {op if op is not None else 0:8.1f} {tce:11.1f} {r:10.1f}")
