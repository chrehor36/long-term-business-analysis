# Same metric, same window, filing-sourced (companyfacts = transcription of the filed faces; each subject's key figure is checked against a filed face in the run file).
import json, sys, os
sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__))
def load(t):
    p = os.path.join(here, f"{t}_companyfacts.json") if t != "SOUN" else os.path.join(here, "..", "companyfacts.json")
    return json.load(open(p))
REV = ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","RevenueFromContractWithCustomerIncludingAssessedTax","SalesRevenueNet"]
def annual(f, tags, unit="USD"):
    from datetime import date
    merged = {}
    for tag in tags:
        out = {}
        for x in f["facts"].get("us-gaap", {}).get(tag, {}).get("units", {}).get(unit, []):
            if x.get("form") in ("10-K","20-F","10-K/A","20-F/A") and x.get("start"):
                s, e = date.fromisoformat(x["start"]), date.fromisoformat(x["end"])
                if 350 <= (e - s).days <= 380:
                    k = e.year if e.month >= 6 else e.year - 1
                    if k not in out or x["filed"] >= out[k][1]:
                        out[k] = (x["val"], x["filed"])
        for k, v in out.items():
            merged.setdefault(k, v[0])
    return merged
def first(f, taglists):
    for tl in taglists:
        a = annual(f, tl)
        if a: return a
    return {}
M = {"rev": [REV],
     "gp": [["GrossProfit"]],
     "cor": [["CostOfRevenue","CostOfGoodsAndServicesSold"]],
     "opinc": [["OperatingIncomeLoss"]],
     "ocf": [["NetCashProvidedByUsedInOperatingActivities"]],
     "sbc": [["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"]],
     "capex": [["PaymentsToAcquirePropertyPlantAndEquipment"]],
     "capsw": [["PaymentsToDevelopSoftware","PaymentsForSoftware"]]}
for t in sys.argv[1:]:
    f = load(t); d = {k: first(f, v) for k, v in M.items()}
    print("==", t, f.get("entityName"))
    for y in sorted(d["rev"]):
        if y < 2019: continue
        r = d["rev"][y]; g = lambda k: d[k].get(y)
        gp = g("gp") if g("gp") is not None else (r - g("cor") if g("cor") is not None else None)
        pct = lambda v: f"{100*v/r:6.1f}%" if v is not None else "   n/a"
        oe = None
        if g("ocf") is not None and g("sbc") is not None:
            oe = g("ocf") - g("sbc") - (g("capex") or 0) - (g("capsw") or 0)
        print(f"{y} rev {r/1e6:9.1f}  gm {pct(gp)}  opm {pct(g('opinc'))}  sbc/rev {pct(g('sbc'))}  ocf {(g('ocf') or 0)/1e6:8.1f}  (ocf-sbc-capex-capsw)/rev {pct(oe)}")
