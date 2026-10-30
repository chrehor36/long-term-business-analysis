#!/usr/bin/env python3
"""Extract annual + quarterly series from SEC companyfacts. Arithmetic only."""
import json, os, sys, collections

OUT = os.path.dirname(os.path.abspath(__file__))

def load(cik):
    with open(os.path.join(OUT, f"facts_{cik}.json"), "r", encoding="utf-8") as f:
        return json.load(f)

def annual(facts, tag, unit="USD"):
    """FY duration facts: fp=FY, form 10-K, ~365d."""
    res = {}
    for taxo in ("us-gaap", "dei", "srt"):
        node = facts["facts"].get(taxo, {}).get(tag)
        if not node:
            continue
        for u, items in node["units"].items():
            if u != unit:
                continue
            for it in items:
                if it.get("form") not in ("10-K", "10-K/A"):
                    continue
                if "start" in it:
                    from datetime import date
                    s = date.fromisoformat(it["start"]); e = date.fromisoformat(it["end"])
                    d = (e - s).days
                    if not (300 <= d <= 400):
                        continue
                if it.get("fp") != "FY":
                    continue
                fy = it["end"][:4] if "start" in it else it["end"][:4]
                key = it["end"]
                # prefer latest accession
                prev = res.get(key)
                if prev is None or it["accn"] >= prev[1]:
                    res[key] = (it["val"], it["accn"], it.get("fy"))
    return dict(sorted(res.items()))

def instant(facts, tag, unit="USD"):
    res = {}
    for taxo in ("us-gaap", "dei", "srt"):
        node = facts["facts"].get(taxo, {}).get(tag)
        if not node:
            continue
        for u, items in node["units"].items():
            if u != unit:
                continue
            for it in items:
                if "start" in it:
                    continue
                if it.get("form") not in ("10-K", "10-K/A"):
                    continue
                key = it["end"]
                prev = res.get(key)
                if prev is None or it["accn"] >= prev[1]:
                    res[key] = (it["val"], it["accn"], it.get("fy"))
    return dict(sorted(res.items()))

def show(facts, tags, unit="USD", kind="annual", label=""):
    for t in tags:
        d = annual(facts, t, unit) if kind == "annual" else instant(facts, t, unit)
        if d:
            print(f"\n== {label or t} [{t}] ({unit}) ==")
            for k, (v, a, fy) in d.items():
                print(f"  {k}  {v:>18,.0f}   {a}")
            return d
    print(f"\n== NOT FOUND: {tags} ==")
    return {}

if __name__ == "__main__":
    cik = sys.argv[1]
    f = load(cik)
    print(f["entityName"])
    print("TAGS AVAILABLE:", len(f["facts"].get("us-gaap", {})))
    if len(sys.argv) > 2 and sys.argv[2] == "list":
        for t in sorted(f["facts"].get("us-gaap", {})):
            print(t)
        sys.exit()
    show(f, ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"], label="Revenue")
    show(f, ["GrossProfit"])
    show(f, ["OperatingIncomeLoss"])
    show(f, ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
             "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"], label="Pretax income")
    show(f, ["NetIncomeLoss"])
    show(f, ["NetCashProvidedByUsedInOperatingActivities"], label="OCF")
    show(f, ["PaymentsToAcquirePropertyPlantAndEquipment"], label="Capex")
    show(f, ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet", "Depreciation"], label="D&A")
    show(f, ["ShareBasedCompensation"], label="SBC")
    show(f, ["PaymentsForRepurchaseOfCommonStock"], label="Buybacks")
    show(f, ["IncomeTaxesPaidNet", "IncomeTaxesPaid"], label="Cash taxes")
    show(f, ["StockholdersEquity"], kind="instant", label="Equity")
    show(f, ["Assets"], kind="instant")
    show(f, ["Liabilities"], kind="instant")
    show(f, ["Goodwill"], kind="instant")
    show(f, ["FiniteLivedIntangibleAssetsNet", "IntangibleAssetsNetExcludingGoodwill"], kind="instant", label="Intangibles")
    show(f, ["CashAndCashEquivalentsAtCarryingValue"], kind="instant", label="Cash")
    show(f, ["LongTermDebtNoncurrent"], kind="instant", label="LT debt")
    show(f, ["LongTermDebtCurrent", "DebtCurrent"], kind="instant", label="Current debt")
    show(f, ["OperatingLeaseRightOfUseAsset"], kind="instant", label="Operating lease ROU")
    show(f, ["OperatingLeaseLiabilityNoncurrent"], kind="instant", label="Op lease liab noncurrent")
    show(f, ["OperatingLeaseLiabilityCurrent"], kind="instant", label="Op lease liab current")
    show(f, ["FinanceLeaseRightOfUseAssetAmortization", "FinanceLeaseLiabilityPaymentsDue"], kind="instant", label="Finance lease")
    show(f, ["RightOfUseAssetObtainedInExchangeForOperatingLeaseLiability"], label="ROU acquired - operating")
    show(f, ["RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability"], label="ROU acquired - finance")
    show(f, ["InventoryNet"], kind="instant", label="Inventory")
    show(f, ["AccountsPayableCurrent"], kind="instant", label="AP")
    show(f, ["NumberOfStores"], unit="store", label="Stores")
    show(f, ["WeightedAverageNumberOfSharesOutstandingBasic"], unit="shares", label="WA basic shares")
    show(f, ["WeightedAverageNumberOfDilutedSharesOutstanding"], unit="shares", label="WA diluted shares")
    show(f, ["CommonStockSharesOutstanding"], unit="shares", kind="instant", label="Shares outstanding")
