# competitor row from the competitors' own XBRL company facts (10-K, FY values); transcription and arithmetic only
import json, sys
from datetime import date
def annual(path, tags, ns="us-gaap", forms=("10-K","10-K/A","20-F")):
    d = json.load(open(path))["facts"].get(ns, {})
    out = {}
    for t in tags:
        vals = {}
        for unit, arr in d.get(t, {}).get("units", {}).items():
            for x in arr:
                if x.get("form") not in forms or x.get("fp") != "FY": continue
                if "start" in x:
                    s = date.fromisoformat(x["start"]); e = date.fromisoformat(x["end"])
                    if not (350 <= (e - s).days <= 380): continue
                y = int(x["end"][:4]) if x["end"][5:7] > "06" else int(x["end"][:4])
                key = x["end"]
                if (key not in vals) or x["filed"] > vals[key][1]: vals[key] = (x["val"], x["filed"])
        out[t] = {k: v[0] for k, v in vals.items()}
    return out
def first(o, tags, k):
    for t in tags:
        if k in o.get(t, {}): return o[t][k]
    return None
REV = ["RevenueFromContractWithCustomerExcludingAssessedTax","Revenues","SalesRevenueNet","SalesRevenueGoodsNet","Revenue"]
OPI = ["OperatingIncomeLoss","ProfitLossFromOperatingActivities"]
OCF = ["NetCashProvidedByUsedInOperatingActivities","CashFlowsFromUsedInOperatingActivities"]
CAPEX = ["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets","PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"]
SBC = ["ShareBasedCompensation","AllocatedShareBasedCompensationExpense","AdjustmentsForSharebasedPayments"]
ACQ = ["PaymentsToAcquireBusinessesNetOfCashAcquired","CashFlowsUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities"]
if __name__ == "__main__":
    name, path, ns = sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "us-gaap")
    o = annual(path, REV+OPI+OCF+CAPEX+SBC+ACQ, ns)
    keys = sorted({k for t in o for k in o[t] if k >= "2014"})
    print(f"{name} ({ns}; millions; fiscal year end)")
    print("  FYend        rev     opinc  opm%      ocf   capex   sbc   acq   (ocf-capex-sbc)/rev%")
    for k in keys:
        r=first(o,REV,k); op=first(o,OPI,k); oc=first(o,OCF,k); cx=first(o,CAPEX,k); sb=first(o,SBC,k) or 0; aq=first(o,ACQ,k) or 0
        if not r: continue
        f=lambda v: f"{v/1e6:8.0f}" if v is not None else "       -"
        opm = f"{100*op/r:5.1f}" if op else "    -"
        oc_ = f"{100*(oc-cx-sb)/r:6.1f}" if (oc and cx) else "     -"
        print(f"  {k} {f(r)} {f(op)} {opm} {f(oc)} {f(cx)} {f(sb)} {f(aq)} {oc_}")
