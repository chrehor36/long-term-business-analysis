#!/usr/bin/env python3
import sys, os, json
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources as S

facts = S.sec_facts("0001107843")
us = facts["facts"]["us-gaap"]
dei = facts["facts"].get("dei", {})

def series(tag, unit=None):
    """annual (FY, duration ~365d or instant) values, most recent filing wins"""
    if tag not in us: return {}
    node = us[tag]["units"]
    u = unit or list(node.keys())[0]
    out = {}
    for it in node[u]:
        if it.get("form") not in ("10-K", "10-K/A"): continue
        if it.get("fp") != "FY": continue
        s = it.get("start"); e = it["end"]
        if s:
            from datetime import date
            d0 = date.fromisoformat(s); d1 = date.fromisoformat(e)
            if not (330 <= (d1-d0).days <= 400): continue
        key = e
        prev = out.get(key)
        if prev is None or it.get("filed","") >= prev[1]:
            out[key] = (it["val"], it.get("filed"), it.get("accn"))
    return out

TAGS = ["NetCashProvidedByUsedInOperatingActivities","ShareBasedCompensation",
        "AllocatedShareBasedCompensationExpense",
        "DepreciationDepletionAndAmortization","Depreciation",
        "AmortizationOfIntangibleAssets","CapitalizedComputerSoftwareAmortization1",
        "PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireIntangibleAssets",
        "PaymentsToAcquireBusinessesNetOfCashAcquired",
        "CapitalizedComputerSoftwarePeriodIncreaseDecrease",
        "Revenues","RevenueFromContractWithCustomerExcludingAssessedTax",
        "NetIncomeLoss","OperatingIncomeLoss","StockholdersEquity",
        "Assets","Liabilities","CashAndCashEquivalentsAtCarryingValue",
        "PaymentsForRepurchaseOfCommonStock","GrossProfit",
        "ResearchAndDevelopmentExpense","SellingGeneralAndAdministrativeExpense",
        "ContractWithCustomerLiability","ContractWithCustomerLiabilityCurrent",
        "IncomeTaxesPaidNet","IncomeTaxesPaid",
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
        "OperatingLeaseRightOfUseAsset","LongTermDebt","Goodwill",
        "WeightedAverageNumberOfDilutedSharesOutstanding",
        "CommonStockSharesOutstanding","CapitalizedComputerSoftwareGross",
        "CapitalizedComputerSoftwareNet","FinanceLeaseRightOfUseAssetAmortization",
        ]
for t in TAGS:
    d = series(t)
    if not d:
        print(f"\n### {t}: (no annual FY data)"); continue
    print(f"\n### {t}")
    for k in sorted(d):
        v, f, a = d[k]
        print(f"   {k}  {v/1e6:>12,.1f}M   filed {f}  {a}")
