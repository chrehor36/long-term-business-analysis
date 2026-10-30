"""Competitor-row transcription from companyfacts: UMC (IFRS, TWD) and GlobalFoundries (US GAAP, USD).
Gross margin, operating margin, revenue, capex, D&A. Newest vintage per period. Arithmetic only."""
import json, os
from datetime import date
HERE = os.path.dirname(os.path.abspath(__file__))


def annual(facts, ns, tags, unit, instant=False):
    out = {}
    for t in tags:
        node = facts.get(ns, {}).get(t)
        if not node:
            continue
        for x in node["units"].get(unit, []):
            if x.get("form") not in ("20-F", "10-K", "20-F/A"):
                continue
            if not instant:
                if "start" not in x:
                    continue
                d = (date.fromisoformat(x["end"]) - date.fromisoformat(x["start"])).days
                if not 340 <= d <= 380:
                    continue
            y = x["end"][:4]
            if y not in out or x["filed"] > out[y][1]:
                out[y] = (x["val"] / 1e6, x["filed"], x["accn"])
        if out:
            return {k: v[0] for k, v in out.items()}, t
    return {}, None


res = {}
umc = json.load(open(os.path.join(HERE, "peers", "UMC_companyfacts.json")))["facts"]
gfs = json.load(open(os.path.join(HERE, "peers", "GFS_companyfacts.json")))["facts"]
spec = {
    "UMC": (umc, "ifrs-full", "TWD", {
        "rev": ["Revenue", "RevenueFromContractsWithCustomers"], "gp": ["GrossProfit"],
        "oi": ["ProfitLossFromOperatingActivities"],
        "ocf": ["CashFlowsFromUsedInOperatingActivities"],
        "capex": ["PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"],
        "dep": ["AdjustmentsForDepreciationExpense", "DepreciationExpense"]}),
    "GFS": (gfs, "ifrs-full", "USD", {
        "rev": ["Revenue", "RevenueFromContractsWithCustomers"], "gp": ["GrossProfit"],
        "oi": ["ProfitLossFromOperatingActivities"], "ocf": ["CashFlowsFromUsedInOperatingActivities"],
        "capex": ["PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"],
        "dep": ["AdjustmentsForDepreciationAndAmortisationExpense", "DepreciationAndAmortisationExpense", "AdjustmentsForDepreciationExpense"]}),
}
for name, (f, ns, unit, tags) in spec.items():
    res[name] = {}
    for k, tl in tags.items():
        vals, used = annual(f, ns, tl, unit)
        res[name][k] = vals
        res[name][k + "_tag"] = used
    print("=====", name, unit)
    yrs = sorted(set(res[name]["rev"]))
    for y in yrs:
        r = res[name]["rev"].get(y); g = res[name]["gp"].get(y); o = res[name]["oi"].get(y)
        c = res[name]["capex"].get(y); d = res[name]["dep"].get(y); oc = res[name]["ocf"].get(y)
        gm = f"{100*g/r:5.1f}" if r and g is not None else "  n/a"
        om = f"{100*o/r:6.1f}" if r and o is not None else "   n/a"
        print(y, f"rev {r:>12,.0f}", "GM", gm, "OM", om, "capex", c, "dep", d, "ocf", oc)
json.dump(res, open(os.path.join(HERE, "peers", "peerseries_out.json"), "w"), indent=1)
