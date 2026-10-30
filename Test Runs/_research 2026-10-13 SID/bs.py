import json
f=json.load(open("cache/facts.json"))["facts"]["ifrs-full"]
def inst(tag):
    out={}
    if tag not in f or "BRL" not in f[tag]["units"]: return out
    for x in f[tag]["units"]["BRL"]:
        if x.get("form")!="20-F" or "start" in x: continue
        y=x["end"][:4]
        if x["end"][5:]!="12-31": continue
        # take value from the 20-F whose own fiscal year is y (fp FY), earliest filed
        if str(x.get("fy"))!=y: continue
        if y not in out or x["filed"]<out[y][1]: out[y]=(x["val"],x["filed"],x["accn"])
    return out
tags=["Assets","CashAndCashEquivalents","CurrentInvestments","TradeReceivables","Inventories","NoncurrentInventories","PropertyPlantAndEquipment","IntangibleAssetsAndGoodwill","InvestmentsInSubsidiariesJointVenturesAndAssociates","ShorttermBorrowings","LongtermBorrowings","Equity","EquityAttributableToOwnersOfParent","NoncontrollingInterests","RetainedEarnings","DeferredTaxAssets"]
ys=[str(y) for y in range(2016,2025)]
print("tag".ljust(52)," ".join(y.rjust(8) for y in ys))
for t in tags:
    a=inst(t)
    print(t[:52].ljust(52)," ".join((f"{a[y][0]/1e6:8.0f}" if y in a else "       -") for y in ys))
