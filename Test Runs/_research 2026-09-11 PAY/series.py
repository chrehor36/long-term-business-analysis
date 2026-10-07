#!/usr/bin/env python3
"""Annual series from companyfacts for PAY - transcription only, no verdict."""
import json, os, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
f = json.load(open(os.path.join(HERE, "cache", "companyfacts.json")))
ug = f["facts"]["us-gaap"]
dei = f["facts"].get("dei", {})

def annual(tag, unit="USD", forms=("10-K",), dur=True):
    out = {}
    for x in ug.get(tag, {}).get("units", {}).get(unit, []):
        if x.get("form") not in forms: continue
        fy_end = x["end"]
        if dur:
            s = x.get("start")
            if not s: continue
            from datetime import date
            d = (date.fromisoformat(fy_end) - date.fromisoformat(s)).days
            if not (340 <= d <= 380): continue
        # earliest filed value for that period (vintage = as originally filed), keep also latest
        key = fy_end
        if key not in out or x["filed"] < out[key][1]:
            out[key] = (x["val"], x["filed"], x["accn"])
    return out

def latest(tag, unit="USD", forms=("10-K",), dur=True):
    out = {}
    for x in ug.get(tag, {}).get("units", {}).get(unit, []):
        if x.get("form") not in forms: continue
        fy_end = x["end"]
        if dur:
            s = x.get("start")
            if not s: continue
            from datetime import date
            d = (date.fromisoformat(fy_end) - date.fromisoformat(s)).days
            if not (340 <= d <= 380): continue
        key = fy_end
        if key not in out or x["filed"] > out[key][1]:
            out[key] = (x["val"], x["filed"], x["accn"])
    return out

tags_dur = [
 "Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","CostOfRevenue","CostOfGoodsAndServicesSold",
 "GrossProfit","OperatingIncomeLoss","NetIncomeLoss","IncomeTaxExpenseBenefit","IncomeTaxesPaidNet","IncomeTaxesPaid",
 "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
 "NetCashProvidedByUsedInOperatingActivities","NetCashProvidedByUsedInInvestingActivities","NetCashProvidedByUsedInFinancingActivities",
 "ShareBasedCompensation","AllocatedShareBasedCompensationExpense",
 "DepreciationDepletionAndAmortization","DepreciationAndAmortization","Depreciation","AmortizationOfIntangibleAssets",
 "PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToDevelopSoftware","PaymentsForSoftware","PaymentsToAcquireIntangibleAssets",
 "PaymentsToAcquireBusinessesNetOfCashAcquired","PaymentsForRepurchaseOfCommonStock","ProceedsFromIssuanceInitialPublicOffering",
 "ProceedsFromStockOptionsExercised","ProceedsFromIssuanceOfCommonStock",
 "IncreaseDecreaseInAccountsReceivable","IncreaseDecreaseInAccountsPayable","IncreaseDecreaseInAccruedLiabilities",
 "ResearchAndDevelopmentExpense","SellingAndMarketingExpense","GeneralAndAdministrativeExpense",
 "WeightedAverageNumberOfDilutedSharesOutstanding","WeightedAverageNumberOfSharesOutstandingBasic",
 "InterestPaidNet","InterestExpense","InvestmentIncomeInterest","InterestIncomeOther","OtherNonoperatingIncomeExpense",
]
tags_inst = [
 "CashAndCashEquivalentsAtCarryingValue","Cash","RestrictedCash","RestrictedCashCurrent","AccountsReceivableNetCurrent",
 "Assets","Liabilities","StockholdersEquity","Goodwill","IntangibleAssetsNetExcludingGoodwill","PropertyPlantAndEquipmentNet",
 "CapitalizedComputerSoftwareNet","LongTermDebt","DebtCurrent","LongTermDebtNoncurrent","OperatingLeaseLiability",
 "AccountsPayableCurrent","AccruedLiabilitiesCurrent","ContractWithCustomerLiabilityCurrent","DeferredRevenueCurrent",
 "CommonStockSharesOutstanding","CommonStockSharesIssued","DeferredTaxAssetsNet","DeferredTaxAssetsNetNoncurrent",
]
print("== DURATION TAGS (as first filed; 10-K annual) ==")
for t in tags_dur:
    a = annual(t, unit="shares" if "Shares" in t else "USD")
    if a:
        print(t)
        for k in sorted(a): print(f"   {k}  {a[k][0]:>16,.0f}   filed {a[k][1]} {a[k][2]}")
print("\n== INSTANT TAGS (latest filed) ==")
for t in tags_inst:
    a = latest(t, unit="shares" if "Shares" in t else "USD", dur=False)
    if a:
        print(t)
        for k in sorted(a): print(f"   {k}  {a[k][0]:>16,.0f}   filed {a[k][1]}")
print("\n== ALL us-gaap TAGS PRESENT ==")
print(", ".join(sorted(ug.keys())))
print("\n== DEI ==")
for t in dei:
    for u, xs in dei[t]["units"].items():
        for x in xs[-4:]:
            print(t, u, x.get("end"), x.get("val"), x.get("form"), x.get("filed"))
