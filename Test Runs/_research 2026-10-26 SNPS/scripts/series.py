"""Owner-cash and margin series for SNPS and its rivals from cached XBRL (first-filed annual values).
Arithmetic only. owner cash (all spending) = OCF - SBC - capex. Figures USD millions."""
import json
from datetime import date
def ann(t, tag, start="2015-06-01"):
    f = json.load(open(f"cache/facts_{t}.json"))["facts"]["us-gaap"]
    if tag not in f: return {}
    u = list(f[tag]["units"])[0]; rows = {}
    for r in f[tag]["units"][u]:
        if r.get("form") not in ("10-K",) or r["end"] < start: continue
        if "start" in r:
            days = (date.fromisoformat(r["end"]) - date.fromisoformat(r["start"])).days
            if not 350 <= days <= 380: continue
        e=date.fromisoformat(r["end"]); y=str(e.year-1) if (e.month==1 and e.day<=7) else str(e.year)
        rows.setdefault(y, []).append((r["filed"], r["val"]))
    return {k: sorted(v)[0][1] / 1e6 for k, v in rows.items()}
def merge(*ds):
    out = {}
    for d in ds:
        for k, v in d.items(): out.setdefault(k, v)
    return out
spec = {
 "SNPS": dict(rev=["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax"], oi=["OperatingIncomeLoss"],
              ocf=["NetCashProvidedByUsedInOperatingActivities","NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
              sbc=["ShareBasedCompensation"], capex=["PaymentsToAcquirePropertyPlantAndEquipment"], acq=["PaymentsToAcquireIntangibleAssets"],
              bb=["PaymentsForRepurchaseOfCommonStock"], rd=["ResearchAndDevelopmentExpense"]),
 "ANSS": dict(rev=["Revenues"], oi=["OperatingIncomeLoss"], ocf=["NetCashProvidedByUsedInOperatingActivities"], sbc=["ShareBasedCompensation"],
              capex=["PaymentsToAcquireProductiveAssets"], acq=["PaymentsToAcquireBusinessesNetOfCashAcquired"], bb=["PaymentsForRepurchaseOfCommonStock"], rd=["ResearchAndDevelopmentExpense"]),
 "CDNS": dict(rev=["RevenueFromContractWithCustomerExcludingAssessedTax","Revenues"], oi=["OperatingIncomeLoss"], ocf=["NetCashProvidedByUsedInOperatingActivities"],
              sbc=["ShareBasedCompensation"], capex=["PaymentsToAcquirePropertyPlantAndEquipment"], acq=["PaymentsToAcquireBusinessesNetOfCashAcquired"], bb=["PaymentsForRepurchaseOfCommonStock"], rd=["ResearchAndDevelopmentExpense","ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost","ResearchAndDevelopmentExpenseSoftwareExcludingAcquiredInProcessCost"]),
 "KEYS": dict(rev=["Revenues","SalesRevenueNet"], oi=["OperatingIncomeLoss"], ocf=["NetCashProvidedByUsedInOperatingActivities"], sbc=["ShareBasedCompensation"],
              capex=["PaymentsToAcquirePropertyPlantAndEquipment"], acq=["PaymentsToAcquireBusinessesNetOfCashAcquired"], bb=["PaymentsForRepurchaseOfCommonStock"], rd=["ResearchAndDevelopmentExpense"]),
}
res = {}
for t, s in spec.items():
    d = {k: merge(*[ann(t, tag) for tag in tags]) for k, tags in s.items()}
    years = sorted(y for y in d["rev"] if "2016" <= y <= "2025")
    print(f"\n{t}  year  rev  opinc  op%  OCF  SBC  capex  OC=OCF-SBC-capex  OC%  acq  buyback  R&D%")
    res[t] = {}
    for y in years:
        g = lambda k: d[k].get(y)
        rev, oi, ocf, sbc, cx = g("rev"), g("oi"), g("ocf"), g("sbc"), g("capex")
        oc = (ocf - sbc - cx) if None not in (ocf, sbc, cx) else None
        res[t][y] = dict(rev=rev, oi=oi, ocf=ocf, sbc=sbc, capex=cx, oc=oc, acq=g("acq"), bb=g("bb"), rd=g("rd"))
        f = lambda v: "   -" if v is None else f"{v:8,.1f}"
        pct = lambda a, b: "  - " if a is None or b is None else f"{100*a/b:5.1f}%"
        print(t, y, f(rev), f(oi), pct(oi, rev), f(ocf), f(sbc), f(cx), f(oc), pct(oc, rev), f(g("acq")), f(g("bb")), pct(g("rd"), rev))
json.dump(res, open("series.json", "w"), indent=1)
