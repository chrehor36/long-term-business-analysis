"""KLAC second pass: margins, service split, balance-sheet denominators, share count.
Arithmetic only."""
import json, os, collections
from datetime import date

OUT = os.path.dirname(os.path.abspath(__file__))
facts_all = json.load(open(os.path.join(OUT, "companyfacts_KLAC.json"), encoding="utf-8"))["facts"]
US = facts_all["us-gaap"]
DEI = facts_all.get("dei", {})

def series(tag, ns=US, forms=("10-K", "10-K/A")):
    if tag not in ns:
        return {}
    by_end = collections.defaultdict(list)
    for unit, rows in ns[tag]["units"].items():
        for r in rows:
            if r.get("form") not in forms or r.get("fp") != "FY":
                continue
            if "start" in r:
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if not (330 <= (e - s).days <= 400):
                    continue
            by_end[r["end"]].append((r["filed"], r["val"], r.get("segment")))
    out = {}
    for end, lst in by_end.items():
        lst.sort()
        out[end] = lst[0][1]
    return out

def show(name, tag, ns=US, scale=1e6, nd=1):
    d = series(tag, ns)
    if not d:
        print(f"  {name:28s} -- TAG ABSENT: {tag}")
        return {}
    print(f"  {name:28s}", {e[:7]: round(v/scale, nd) for e, v in sorted(d.items())})
    return d

print("REVENUE / MARGIN TAGS")
rev = show("Revenues", "Revenues")
rev2 = show("RevFromContractWithCustomer", "RevenueFromContractWithCustomerExcludingAssessedTax")
for t in ["CostOfRevenue", "CostOfGoodsAndServicesSold", "CostOfGoodsSold",
          "CostOfServices", "GrossProfit"]:
    show(t, t)

print("\nSEGMENT-ISH / PRODUCT-SERVICE TAGS PRESENT (searching all us-gaap keys):")
for k in sorted(US):
    kl = k.lower()
    if any(s in kl for s in ("productmember", "servicemember")):
        print("   ", k)

print("\nBALANCE SHEET")
for t in ["Assets", "Liabilities", "LiabilitiesCurrent", "AssetsCurrent",
          "StockholdersEquity", "Goodwill", "IntangibleAssetsNetExcludingGoodwill",
          "FiniteLivedIntangibleAssetsNet", "LongTermDebtNoncurrent", "LongTermDebtCurrent",
          "LongTermDebt", "DebtLongtermAndShorttermCombinedAmount",
          "CashAndCashEquivalentsAtCarryingValue",
          "AvailableForSaleSecuritiesDebtSecuritiesCurrent",
          "MarketableSecuritiesCurrent", "ShortTermInvestments",
          "PropertyPlantAndEquipmentNet", "InventoryNet",
          "OperatingLeaseRightOfUseAsset", "OperatingLeaseLiabilityNoncurrent",
          "FinanceLeaseRightOfUseAsset", "ContractWithCustomerLiability",
          "ContractWithCustomerLiabilityCurrent"]:
    show(t, t)

print("\nINCOME / OTHER")
for t in ["OperatingIncomeLoss", "InterestExpense", "InterestExpenseDebt",
          "ResearchAndDevelopmentExpense", "SellingGeneralAndAdministrativeExpense",
          "AmortizationOfIntangibleAssets", "GoodwillImpairmentLoss",
          "RestructuringCharges", "PaymentsToAcquireBusinessesNetOfCashAcquired",
          "CapitalizedComputerSoftwareAdditions", "PaymentsForSoftware",
          "PaymentsToDevelopSoftware"]:
    show(t, t)

print("\nSHARES")
for t in ["CommonStockSharesOutstanding", "CommonStockSharesIssued",
          "WeightedAverageNumberOfSharesOutstandingBasic",
          "WeightedAverageNumberOfDilutedSharesOutstanding"]:
    show(t, t, scale=1e6, nd=1)
d = series("EntityCommonStockSharesOutstanding", DEI)
print("  dei cover shares            ", {e[:10]: round(v/1e6, 2) for e, v in sorted(d.items())})

print("\nDIVIDEND PER SHARE (declared)")
for t in ["CommonStockDividendsPerShareDeclared", "CommonStockDividendsPerShareCashPaid"]:
    show(t, t, scale=1, nd=4)
