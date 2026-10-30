"""Pull annual series from companyfacts for CALX. Transcription and screening only."""
import json, os, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
cf = json.load(open(os.path.join(HERE, "companyfacts_1406666.json"), encoding="utf-8"))
facts = cf["facts"]

TAGS = [
 ("us-gaap","Revenues"), ("us-gaap","RevenueFromContractWithCustomerExcludingAssessedTax"),
 ("us-gaap","SalesRevenueServicesNet"), ("us-gaap","SalesRevenueNet"),
 ("us-gaap","NetIncomeLoss"), ("us-gaap","ProfitLoss"),
 ("us-gaap","NetCashProvidedByUsedInOperatingActivities"),
 ("us-gaap","ShareBasedCompensation"), ("us-gaap","AllocatedShareBasedCompensationExpense"),
 ("us-gaap","PaymentsToAcquirePropertyPlantAndEquipment"),
 ("us-gaap","PaymentsToDevelopSoftware"), ("us-gaap","PaymentsForSoftware"),
 ("us-gaap","PaymentsToAcquireIntangibleAssets"),
 ("us-gaap","DepreciationDepletionAndAmortization"), ("us-gaap","DepreciationAndAmortization"),
 ("us-gaap","Depreciation"), ("us-gaap","AmortizationOfIntangibleAssets"),
 ("us-gaap","CapitalizedComputerSoftwareAmortization1"), ("us-gaap","CapitalizedComputerSoftwareAdditions"),
 ("us-gaap","StockholdersEquity"), ("us-gaap","StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"),
 ("us-gaap","Assets"), ("us-gaap","Liabilities"),
 ("us-gaap","CashAndCashEquivalentsAtCarryingValue"),
 ("us-gaap","LongTermDebt"), ("us-gaap","LongTermDebtNoncurrent"), ("us-gaap","LineOfCredit"),
 ("us-gaap","IncomeTaxesPaidNet"), ("us-gaap","IncomeTaxesPaid"),
 ("us-gaap","IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"),
 ("us-gaap","OperatingIncomeLoss"), ("us-gaap","GrossProfit"), ("us-gaap","CostOfRevenue"), ("us-gaap","CostOfServices"),
 ("us-gaap","WeightedAverageNumberOfDilutedSharesOutstanding"), ("us-gaap","WeightedAverageNumberOfSharesOutstandingBasic"),
 ("us-gaap","CommonStockSharesOutstanding"), ("us-gaap","CommonStockSharesIssued"),
 ("dei","EntityCommonStockSharesOutstanding"),
 ("us-gaap","ProceedsFromIssuanceOfCommonStock"), ("us-gaap","ProceedsFromStockOptionsExercised"),
 ("us-gaap","ProceedsFromIssuanceOrSaleOfEquity"),
 ("us-gaap","PaymentsForRepurchaseOfCommonStock"),
 ("us-gaap","ConcentrationRiskPercentage1"),
 ("us-gaap","IncreaseDecreaseInAccountsReceivable"),
 ("us-gaap","AccountsReceivableNetCurrent"),
 ("us-gaap","Goodwill"), ("us-gaap","IntangibleAssetsNetExcludingGoodwill"),
 ("us-gaap","InterestPaidNet"),
 ("us-gaap","PaymentsToAcquireProductiveAssets"),
 ("us-gaap","PaymentsForCapitalizedInternalUseSoftware"),
 ("us-gaap","PaymentsToAcquireSoftware"),
 ("us-gaap","CapitalizedComputerSoftwareNet"),
 ("us-gaap","IncreaseDecreaseInAccountsPayable"),
 ("us-gaap","IncreaseDecreaseInInventories"),
 ("us-gaap","IncreaseDecreaseInDeferredRevenue"),
 ("us-gaap","InventoryNet"),
 ("us-gaap","DeferredRevenueCurrent"),
 ("us-gaap","ContractWithCustomerLiabilityCurrent"),
 ("us-gaap","ContractWithCustomerLiabilityNoncurrent"),
 ("us-gaap","ResearchAndDevelopmentExpense"),
 ("us-gaap","SellingGeneralAndAdministrativeExpense"),
 ("us-gaap","IncomeTaxExpenseBenefit"),
 ("us-gaap","DeferredIncomeTaxExpenseBenefit"),
 ("us-gaap","StockRepurchasedDuringPeriodShares"),
 ("us-gaap","StockRepurchasedDuringPeriodValue"),
 ("us-gaap","MarketableSecuritiesCurrent"),
 ("us-gaap","ShortTermInvestments"),
 ("us-gaap","OperatingLeaseLiability"),
 ("us-gaap","RestructuringCharges"),
 ("us-gaap","ImpairmentOfIntangibleAssetsExcludingGoodwill"),
 ("us-gaap","ProceedsFromSaleOfPropertyPlantAndEquipment"),
]

def annual(tag_ns, tag):
    d = facts.get(tag_ns, {}).get(tag)
    if not d: return None
    units = d["units"]
    unit = "USD" if "USD" in units else ("shares" if "shares" in units else list(units)[0])
    rows = units[unit]
    out = {}
    for r in rows:
        if r.get("fp") not in ("FY", None) and unit == "USD":
            # keep only FY duration facts for flows; instant facts have no fp filter issue
            pass
        fy_end = r["end"]
        # duration facts: need ~1yr span
        if "start" in r:
            from datetime import date
            s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
            if not (330 <= (e - s).days <= 380): continue
        key = fy_end
        # prefer the latest filing (restated) for each period end
        prev = out.get(key)
        if prev is None or r["filed"] > prev["filed"]:
            out[key] = r
    return unit, out

if __name__ == "__main__":
    for ns, tag in TAGS:
        res = annual(ns, tag)
        if not res:
            print(f"-- {tag}: ABSENT"); continue
        unit, out = res
        print(f"== {tag} ({unit})")
        for k in sorted(out):
            r = out[k]
            v = r["val"]
            if unit == "USD": v = f"{v/1e6:10.3f}M"
            print(f"   {k}  {v}   filed {r['filed']}  form {r['form']}  acc {r['accn']}")
