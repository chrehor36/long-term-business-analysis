import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
OUT=os.path.dirname(os.path.abspath(__file__))
cf=json.load(open(os.path.join(OUT,"companyfacts.json")))
us=cf["facts"].get("us-gaap",{})
def annual(tag, form_ok=("10-K",)):
    """return {fy: (val, accn, end)} for FY-length duration facts"""
    d=us.get(tag)
    if not d: return {}
    out={}
    for unit,rows in d["units"].items():
        for r in rows:
            if r.get("form") not in form_ok: continue
            if r.get("fp")!="FY": continue
            st=r.get("start"); en=r.get("end")
            if st and en:
                from datetime import date
                y0=date.fromisoformat(st); y1=date.fromisoformat(en)
                if (y1-y0).days<330 or (y1-y0).days>400: continue
            fy=r.get("fy")
            key=en
            # prefer latest-filed
            if key not in out or r["accn"]>out[key][1]:
                out[key]=(r["val"],r["accn"],r.get("frame",""))
    return out
def inst(tag):
    d=us.get(tag)
    if not d: return {}
    out={}
    for unit,rows in d["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K",): continue
            if "start" in r: continue
            en=r["end"]
            if en not in out or r["accn"]>out[en][1]:
                out[en]=(r["val"],r["accn"])
    return out
tags=["NetCashProvidedByUsedInOperatingActivities","ShareBasedCompensation",
 "PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets",
 "PaymentsForCapitalImprovements","PaymentsToDevelopSoftware","PaymentsToAcquireSoftware",
 "PaymentsToAcquireIntangibleAssets","CapitalizedComputerSoftwareAdditions",
 "DepreciationDepletionAndAmortization","DepreciationAmortizationAndAccretionNet",
 "Depreciation","DepreciationAndAmortization","AmortizationOfIntangibleAssets",
 "Revenues","RevenueFromContractWithCustomerExcludingAssessedTax",
 "NetIncomeLoss","OperatingIncomeLoss","ResearchAndDevelopmentExpense",
 "PaymentsForRepurchaseOfCommonStock","StockholdersEquity",
 "CashAndCashEquivalentsAtCarryingValue","ShortTermInvestments","MarketableSecuritiesCurrent",
 "IncomeTaxesPaidNet","IncomeTaxesPaid","IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
 "WeightedAverageNumberOfDilutedSharesOutstanding","WeightedAverageNumberOfSharesOutstandingBasic",
 "PaymentsToAcquireBusinessesNetOfCashAcquired","OperatingLeaseRightOfUseAsset",
 "Liabilities","Assets","Goodwill","FiniteLivedIntangibleAssetsNet"]
for t in tags:
    a=annual(t)
    if not a:
        print(f"{t}: EMPTY"); continue
    s=" ".join(f"{k[:4]}={v[0]/1e6:,.1f}" for k,v in sorted(a.items()) if k>="2018")
    print(f"{t}: {s}")
print()
print("--- INSTANT (balance sheet) ---")
for t in ["StockholdersEquity","CashAndCashEquivalentsAtCarryingValue","MarketableSecuritiesCurrent","ShortTermInvestments","Assets","Liabilities","Goodwill","FiniteLivedIntangibleAssetsNet","LongTermDebtNoncurrent","OperatingLeaseLiabilityNoncurrent","OperatingLeaseLiabilityCurrent","ConvertibleDebtNoncurrent"]:
    a=inst(t)
    if not a: print(f"{t}: EMPTY"); continue
    s=" ".join(f"{k}={v[0]/1e6:,.1f}" for k,v in sorted(a.items()) if k>="2019-12")
    print(f"{t}: {s}")
