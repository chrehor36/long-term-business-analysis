import json,sys
def annual(g,tag,unit="USD"):
    out={}
    if tag not in g: return out
    for x in g[tag]["units"].get(unit,[]):
        if x.get("form") in ("10-K","10-K/A") and x.get("fp")=="FY":
            s,e=x.get("start"),x["end"]
            if s and (int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])<11: continue
            y=int(e[:4])
            if y not in out or x["filed"]<out[y][1]: out[y]=(x["val"],x["filed"])
    return {k:v[0] for k,v in out.items()}
def first(g,tags):
    d={}
    for t in tags:
        for y,v in annual(g,t).items(): d.setdefault(y,v)
    return d
for t in ["AMN","CCRN","RHI","KFRC"]:
    fn="facts.json" if t=="AMN" else f"peers/{t}_facts.json"
    g=json.load(open(fn))["facts"]["us-gaap"]
    rev=first(g,["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueServicesNet","SalesRevenueNet"])
    gp=first(g,["GrossProfit"])
    op=first(g,["OperatingIncomeLoss"])
    ocf=first(g,["NetCashProvidedByUsedInOperatingActivities","NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"])
    cap=first(g,["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"])
    sbc=first(g,["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"])
    gw=first(g,["GoodwillImpairmentLoss"])
    print(t); print(" yr     rev    GM%    opInc   OM%    OCF  capex   SBC  (OCF-SBC-capex)/rev%")
    for y in sorted(rev):
        if y<2009: continue
        r=rev[y]/1e6; o=op.get(y); gpp=gp.get(y)
        oc=ocf.get(y); c=cap.get(y,0); s=sbc.get(y,0)
        oe=(oc-s-c)/1e6 if oc is not None else None
        print(f" {y} {r:8.1f} {100*gpp/1e6/r if gpp else float('nan'):5.1f} {o/1e6 if o is not None else float('nan'):8.1f} {100*o/1e6/r if o is not None else float('nan'):5.1f} {oc/1e6 if oc else float('nan'):7.1f} {c/1e6:5.1f} {s/1e6:5.1f}  {100*oe/r if oe is not None else float('nan'):5.1f}  gwimp={gw.get(y,0)/1e6:.0f}")
