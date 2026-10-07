# Arithmetic only: (operating income + D&A) / average gross real estate, and OI / average net, from companyfacts 10-K facts.
import json, sys
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
def facts(path):
    return json.load(open(path, encoding="utf-8"))["facts"]["us-gaap"]
def fy(g, tag, dur=True):
    out = {}
    if tag not in g: return out
    for u in g[tag]["units"].values():
        for x in u:
            if x.get("form") not in ("10-K", "10-K/A"): continue
            if dur:
                if "start" not in x: continue
                d = (date.fromisoformat(x["end"]) - date.fromisoformat(x["start"])).days
                if not 350 < d < 380: continue
            elif "start" in x: continue
            out.setdefault(x["end"][:4], x["val"] / 1e6)   # earliest filed vintage
    return out
P = "../_research 2026-09-18 EQIX/peers/"
cos = {"DLR": "companyfacts.json", "EQIX": "../_research 2026-09-18 EQIX/companyfacts.json", "CONE": P+"CONE_companyfacts.json",
       "QTS": P+"QTS_companyfacts.json", "COR": P+"COR_companyfacts.json", "SWCH": P+"SWCH_companyfacts.json",
       "DFT": "peers/DFT_0001407739_companyfacts.json"}
for co, path in cos.items():
    g = facts(path)
    oi = fy(g, "OperatingIncomeLoss")
    da = {}
    for t in ["DepreciationAndAmortization", "DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet"]:
        for k, v in fy(g, t).items(): da.setdefault(k, v)
    s3 = fy(g, "RealEstateGrossAtCarryingValue", dur=False)
    cost = fy(g, "RealEstateInvestmentPropertyAtCost", dur=False)
    ppe = fy(g, "PropertyPlantAndEquipmentGross", dur=False)
    rev = {}
    for t in ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "OperatingLeasesIncomeStatementLeaseRevenue"]:
        for k, v in fy(g, t).items(): rev.setdefault(k, v)
    print("==", co)
    for y in sorted(oi):
        if y < "2012": continue
        den = s3 if s3 else (cost if cost else ppe)
        py = str(int(y) - 1)
        avg = (den[y] + den[py]) / 2 if y in den and py in den else None
        r = (oi[y] + da.get(y, float("nan"))) / avg * 100 if avg else None
        print(y, "rev", round(rev.get(y, float("nan")), 1), "OI", round(oi[y], 1), "DA", round(da.get(y, float("nan")), 1),
              "SchIII", round(s3.get(y, float("nan")), 1), "cost", round(cost.get(y, float("nan")), 1), "ppe", round(ppe.get(y, float("nan")), 1),
              "(OI+DA)/avg", None if r is None else round(r, 1))
