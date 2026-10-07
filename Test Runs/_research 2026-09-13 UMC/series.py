"""UMC annual series FY2014-FY2024 from companyfacts (transcription, newest vintage per period end);
FY2025 typed from the FY2025 20-F (0001193125-26-193757) consolidated statements, because companyfacts lacks it.
Arithmetic only. Output series_out.json (NT$ millions)."""
import json, os
from datetime import date
HERE = os.path.dirname(os.path.abspath(__file__))
f = json.load(open(os.path.join(HERE, "companyfacts.json")))["facts"]["ifrs-full"]
TAGS = {
    "rev": ["Revenue"], "gp": ["GrossProfit"], "oi": ["ProfitLossFromOperatingActivities"],
    "ni_parent": ["ProfitLossAttributableToOwnersOfParent"], "pretax": ["ProfitLossBeforeTax"],
    "ocf": ["CashFlowsFromUsedInOperatingActivities"],
    "capex": ["PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"],
    "intang": ["PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities"],
    "dep": ["AdjustmentsForDepreciationExpense", "DepreciationExpense"],
    "amort": ["AdjustmentsForAmortisationExpense", "AmortisationExpense"],
    "sbc": ["AdjustmentsForSharebasedPayments"],
    "grants": ["ProceedsFromGovernmentGrantsClassifiedAsInvestingActivities"],
    "div_recd": ["DividendsReceivedClassifiedAsOperatingActivities"],
    "int_recd": ["InterestReceivedClassifiedAsOperatingActivities"],
    "int_paid": ["InterestPaidClassifiedAsOperatingActivities"],
    "tax_paid": ["IncomeTaxesPaidRefundClassifiedAsOperatingActivities"],
    "div_paid": ["DividendsPaidClassifiedAsFinancingActivities"],
    "equity_parent": ["EquityAttributableToOwnersOfParent"], "cash": ["CashAndCashEquivalents"],
    "ppe": ["PropertyPlantAndEquipment"],
    "share_assoc": ["ShareOfProfitLossOfAssociatesAndJointVenturesAccountedForUsingEquityMethod"],
}
INST = ("equity_parent", "cash", "ppe")
def annual(tags, instant=False):
    out = {}
    for t in tags:
        if t not in f:
            continue
        for x in f[t]["units"].get("TWD", []):
            if x.get("form") not in ("20-F", "20-F/A") or "segment" in x:
                continue
            end = x["end"]
            if end[5:] != "12-31":
                continue
            if not instant:
                if "start" not in x:
                    continue
                d = (date.fromisoformat(end) - date.fromisoformat(x["start"])).days
                if not (340 <= d <= 380):
                    continue
            key = end[:4]
            prev = out.get(key)
            if prev is None or x["filed"] > prev[1]:
                out[key] = (x["val"] / 1e6, x["filed"], x["accn"], t)
        if out:
            break
    return out
res = {}
for k, tags in TAGS.items():
    a = annual(tags, k in INST)
    res[k] = {y: v[0] for y, v in a.items()}
    res[k + "_src"] = {y: v[2] + " " + v[3] for y, v in a.items()}
# FY2025 typed from the FY2025 20-F (NT$ thousands -> millions): F-4 balance sheet, F-5 income statement, F-9/F-10 cash flows
FY25 = {"rev": 237553.2, "gp": 68906.5, "oi": 43948.7, "ni_parent": 40360.3, "pretax": 48081.667,
        "ocf": 99864.187, "capex": 47744.896, "intang": 2988.751, "dep": 56427.377, "amort": 2831.540,
        "sbc": 491.280, "grants": 5097.841, "div_recd": 2387.240, "int_recd": 2276.904, "int_paid": 1017.112,
        "tax_paid": 6360.694, "div_paid": 35784.383, "equity_parent": 365824.997, "cash": 110660.052,
        "ppe": 271395.296, "share_assoc": 657.163}
for k, v in FY25.items():
    res[k]["2025"] = v
    res[k + "_src"]["2025"] = "0001193125-26-193757 typed from filed statement"
json.dump(res, open(os.path.join(HERE, "series_out.json"), "w"), indent=1)
yrs = [str(y) for y in range(2013, 2026)]
print("years", yrs)
for k in TAGS:
    print(f"{k:14s}", " ".join(f"{res[k].get(y, float('nan')):>9,.0f}" for y in yrs))
