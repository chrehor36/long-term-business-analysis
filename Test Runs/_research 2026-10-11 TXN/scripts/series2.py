import json, sys
from datetime import date
d = json.load(open(sys.argv[1])); g = d["facts"]["us-gaap"]
def annual(tags):
    out = {}
    for tag in tags:
        if tag not in g: continue
        for u, arr in g[tag]["units"].items():
            for x in arr:
                if x.get("form") not in ("10-K","20-F") or "start" not in x: continue
                ds, de = date.fromisoformat(x["start"]), date.fromisoformat(x["end"])
                if not (350 <= (de-ds).days <= 380): continue
                y = de.year if de.month > 6 else de.year - 1  # fiscal year label by end
                y = de.year
                key = y
                if key not in out or x["filed"] > out[key][1]:
                    out[key] = (x["val"], x["filed"], tag)
    return out
rev = annual(["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","SalesRevenueGoodsNet"])
op = annual(["OperatingIncomeLoss"])
gp = annual(["GrossProfit"])
cx = annual(["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"])
ocf = annual(["NetCashProvidedByUsedInOperatingActivities","NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"])
sbc = annual(["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"])
print("FYend,rev,op,op%,gm%,capex%rev,ocf,sbc")
for y in sorted(rev):
    if y < 2013: continue
    r = rev[y][0]
    def p(dct): return dct[y][0] if y in dct else None
    o, gg, c, of, s = p(op), p(gp), p(cx), p(ocf), p(sbc)
    f = lambda v: f"{v/1e6:.0f}" if v is not None else ""
    pc = lambda v: f"{100*v/r:.1f}" if v is not None else ""
    print(y, f(r), f(o), pc(o), pc(gg), pc(c), f(of), f(s), sep=",")
