"""TSM annual series FY2015-FY2024 from companyfacts (transcription), newest vintage per period end,
FY2025 typed from the FY2025 20-F (0001628280-26-025362) because companyfacts lacks it.
Arithmetic only. Output: series_out.json and a printed table (NT$ millions)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
f = json.load(open(os.path.join(HERE, "companyfacts.json")))["facts"]["ifrs-full"]

TAGS = {
    "rev": ["Revenue"],
    "gp": ["GrossProfit"],
    "oi": ["ProfitLossFromOperatingActivities"],
    "ni_parent": ["ProfitLossAttributableToOwnersOfParent"],
    "pretax": ["ProfitLossBeforeTax"],
    "ocf": ["CashFlowsFromUsedInOperatingActivities"],
    "capex": ["PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"],
    "intang": ["PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities"],
    "dep": ["AdjustmentsForDepreciationExpense", "DepreciationExpense"],
    "amort": ["AdjustmentsForAmortisationExpense", "AmortisationExpense"],
    "sbc": ["AdjustmentsForSharebasedPayments"],
    "grants": ["ProceedsFromGovernmentGrantsClassifiedAsInvestingActivities"],
    "equity_parent": ["EquityAttributableToOwnersOfParent"],
    "equity": ["Equity"],
    "cash": ["CashAndCashEquivalents"],
    "div_paid": ["DividendsPaidClassifiedAsFinancingActivities"],
    "tax_paid": ["IncomeTaxesPaidRefundClassifiedAsOperatingActivities"],
    "ppe": ["PropertyPlantAndEquipment"],
}


def annual(tags, instant=False):
    out = {}
    for t in tags:
        if t not in f:
            continue
        for x in f[t]["units"].get("TWD", []):
            if x.get("form") != "20-F":
                continue
            if "segment" in x:
                continue
            end = x["end"]
            if not instant:
                if "start" not in x:
                    continue
                from datetime import date
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
    inst = k in ("equity_parent", "equity", "cash", "ppe")
    res[k] = {y: v[0] for y, v in annual(tags, inst).items()}
    res[k + "_src"] = {y: v[2] + " " + v[3] for y, v in annual(tags, inst).items()}

# FY2025, typed from the FY2025 20-F (NT$ millions), consolidated statements F-4 to F-13
FY25 = {"rev": 3809054.0, "ocf": 2274975.6, "capex": 1272410.5, "intang": 10146.9, "dep": 679684.0,
        "amort": 8412.4, "sbc": 1246.1, "grants": 76258.8, "div_paid": 466779.2, "tax_paid": 267557.5,
        "pretax": 2041654.7}
for k, v in FY25.items():
    res[k]["2025"] = v

json.dump(res, open(os.path.join(HERE, "series_out.json"), "w"), indent=1)
yrs = [str(y) for y in range(2013, 2026)]
for k in TAGS:
    print(f"{k:14s}", " ".join(f"{res[k].get(y, float('nan')):>11,.0f}" for y in yrs))
print("years", yrs)
