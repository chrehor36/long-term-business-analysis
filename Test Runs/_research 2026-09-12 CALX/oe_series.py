import json, collections
d = json.load(open("companyfacts_1406666.json"))
us = d["facts"]["us-gaap"]
def annual(tag):
    out = {}
    if tag not in us: return out
    for unit, rows in us[tag]["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K","10-K/A"): continue
            if "start" not in r: continue
            sd, ed = r["start"], r["end"]
            # full year
            if not (350 <= (int(ed[:4])*365+int(ed[5:7])*30+int(ed[8:10])) - (int(sd[:4])*365+int(sd[5:7])*30+int(sd[8:10])) <= 380): continue
            fy = ed[:4]
            key=(fy, r["val"])
            out.setdefault(fy, []).append((r["val"], r.get("accn"), r.get("fy"), r.get("fp"), ed))
    return out
tags = {
 "OCF":"NetCashProvidedByUsedInOperatingActivities",
 "OCFcont":"NetCashProvidedByUsedInOperatingActivitiesContinuingOperations",
 "SBC":"ShareBasedCompensation",
 "DA":"DepreciationDepletionAndAmortization",
 "DA2":"DepreciationAmortizationAndAccretionNet",
 "DA3":"Depreciation",
 "CAPEX":"PaymentsToAcquirePropertyPlantAndEquipment",
 "REV":"RevenueFromContractWithCustomerExcludingAssessedTax",
 "REV2":"Revenues",
 "REV3":"SalesRevenueNet",
 "GP":"GrossProfit",
 "NI":"NetIncomeLoss",
 "AP":"IncreaseDecreaseInAccountsPayable",
 "CAPSW":"PaymentsToDevelopSoftware",
 "CAPSW2":"CapitalizedComputerSoftwareAdditions",
 "OPINC":"OperatingIncomeLoss",
 "RD":"ResearchAndDevelopmentExpense",
 "BUYBACK":"PaymentsForRepurchaseOfCommonStock",
 "ISSUE":"ProceedsFromIssuanceOfCommonStock",
 "ISSUE2":"ProceedsFromStockOptionsExercised",
 "DILSH":"WeightedAverageNumberOfDilutedSharesOutstanding",
}
res = {}
for k,t in tags.items():
    res[k]=annual(t)
years = sorted(set(y for k in res for y in res[k]))
print("tag availability:")
for k in tags:
    print(f"  {k:8s} {tags[k]:55s} years={sorted(res[k].keys())}")
print()
def pick(k, y):
    v = res[k].get(y)
    if not v: return None
    # prefer the ORIGINAL filing value (earliest accn fy) -> but report all distinct
    vals = sorted(set(x[0] for x in v))
    return vals
print("YEAR  OCF        SBC       D&A      CAPEX     REV        NI       APchg")
for y in years:
    row=[y]
    for k in ["OCF","SBC","DA","CAPEX","REV","NI","AP"]:
        vv = pick(k,y)
        if vv is None:
            vv = pick(k+"2",y) if k+"2" in res else None
        row.append(vv)
    print(row)
