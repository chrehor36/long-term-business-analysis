import json, sys
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
def series(d, tags, flow=True):
    out = {}
    for t in tags:
        if t not in d: continue
        u = list(d[t]["units"])[0]
        for x in d[t]["units"][u]:
            if x.get("fp") != "FY" or not x["form"].startswith("10-K"): continue
            if flow:
                if "start" not in x: continue
                if (date.fromisoformat(x["end"]) - date.fromisoformat(x["start"])).days < 300: continue
            y = int(x["end"][:4])
            if y not in out: out[y] = (x["val"], x["accn"], t)
    return out
for f in sys.argv[1:]:
    d = json.load(open(f))["facts"]["us-gaap"]
    rev = series(d, ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","SalesRevenueGoodsNet"])
    oi = series(d, ["OperatingIncomeLoss"])
    eq = series(d, ["StockholdersEquity","StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"], flow=False)
    ocf = series(d, ["NetCashProvidedByUsedInOperatingActivities","NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"])
    capex = series(d, ["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"])
    print("==", f)
    for y in range(2016, 2026):
        r = rev.get(y, (None,))[0]; o = oi.get(y, (None,))[0]
        m = f"{o/r*100:5.1f}%" if r and o is not None else "  n/a"
        print(y, f"rev {r/1e6 if r else 0:8.1f}", f"opinc {o/1e6 if o is not None else 0:7.1f}", "margin", m,
              f"equity {eq.get(y,(0,))[0]/1e6:7.1f}", f"ocf {ocf.get(y,(0,))[0]/1e6:6.1f}", f"capex {capex.get(y,(0,))[0]/1e6:6.1f}", rev.get(y,(0,'',''))[1], oi.get(y,(0,'',''))[1])
