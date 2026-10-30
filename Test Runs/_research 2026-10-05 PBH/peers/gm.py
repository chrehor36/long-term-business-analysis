import json,sys
from datetime import date
def annual(g,tags):
    out={}
    for tag in tags:
        if tag not in g: continue
        for u,vals in g[tag]["units"].items():
            for v in vals:
                if v.get("fp")=="FY" and (v["form"].startswith("10-K") or v["form"].startswith("20-F")) and "start" in v:
                    s=date.fromisoformat(v["start"]); e=date.fromisoformat(v["end"])
                    if 350<(e-s).days<380:
                        out.setdefault(v["end"][:7],(v["val"],v["accn"],tag))
    return out
for t in ["PRGO","CHD","KVUE","HLN"]:
    d=json.load(open(f"peers/{t}_facts.json"))
    g={}
    for ns in d["facts"]: g.update(d["facts"][ns])
    rev=annual(g,["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","SalesRevenueGoodsNet","Revenue"])
    gp=annual(g,["GrossProfit"])
    cogs=annual(g,["CostOfGoodsAndServicesSold","CostOfRevenue","CostOfGoodsSold","CostOfSales"])
    print(t)
    for k in sorted(rev):
        r=rev[k][0]; 
        if k in gp: m=gp[k][0]/r
        elif k in cogs: m=1-abs(cogs[k][0])/r
        else: m=None
        print("  ",k, round(r/1e6), None if m is None else round(100*m,1), rev[k][1], rev[k][2])
