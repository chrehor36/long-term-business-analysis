"""Return on the tangible capital the business needs, SHW, from companyfacts (first-filed 10-K vintage; transcription).
tangible operating capital = current assets - cash + net PP&E + operating ROU assets
                             - (accounts payable + compensation and taxes withheld + accrued taxes + other accruals)
                             - operating lease liabilities (current and long-term)
EBIT = income before income taxes + interest expense - interest income; pre-tax, before acquired-intangible amortization
shown beside it. USD millions."""
import json, sys
from datetime import date

g = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "cache/companyfacts_SHW.json"))["facts"]["us-gaap"]


def inst(tag, y):
    best = None
    for r in g.get(tag, {}).get("units", {}).get("USD", []):
        if r.get("form") == "10-K" and r["end"] == f"{y}-12-31" and "start" not in r:
            if best is None or r["filed"] < best["filed"]:
                best = r
    return best["val"] / 1e6 if best else None


def dur(tag, y):
    best = None
    for r in g.get(tag, {}).get("units", {}).get("USD", []):
        if r.get("form") == "10-K" and r["end"] == f"{y}-12-31" and "start" in r:
            s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
            if 350 <= (e - s).days <= 380 and (best is None or r["filed"] < best["filed"]):
                best = r
    return best["val"] / 1e6 if best else None


def first(fn, tags, y):
    for t in tags:
        v = fn(t, y)
        if v is not None:
            return v
    return 0.0


print(f"{'FY':>4} {'tang cap':>9} {'EBIT':>8} {'EBIT+amort':>11} {'ret':>6} {'ret+am':>7}")
res = {}
for y in range(2018, 2026):
    ca = first(inst, ["AssetsCurrent"], y)
    cash = first(inst, ["CashAndCashEquivalentsAtCarryingValue"], y)
    ppe = first(inst, ["PropertyPlantAndEquipmentNet"], y)
    rou = first(inst, ["OperatingLeaseRightOfUseAsset"], y)
    ap = first(inst, ["AccountsPayableCurrent"], y)
    comp = first(inst, ["EmployeeRelatedLiabilitiesCurrent"], y)
    tax = first(inst, ["AccruedIncomeTaxesCurrent", "TaxesPayableCurrent"], y)
    oth = first(inst, ["OtherAccruedLiabilitiesCurrent", "OtherLiabilitiesCurrent"], y)
    oll = first(inst, ["OperatingLeaseLiabilityCurrent"], y) + first(inst, ["OperatingLeaseLiabilityNoncurrent"], y)
    cap = ca - cash + ppe + rou - ap - comp - tax - oth - oll
    pti = first(dur, ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
                      "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"], y)
    ie = first(dur, ["InterestExpense", "InterestExpenseNonoperating"], y)
    ii = first(dur, ["InvestmentIncomeInterestAndDividend", "InvestmentIncomeInterest", "InvestmentIncomeNet"], y)
    am = first(dur, ["AmortizationOfIntangibleAssets"], y)
    ebit = pti + ie - ii
    res[y] = (cap, ebit, am)
    print(f"{y:>4} {cap:>9.0f} {ebit:>8.0f} {ebit+am:>11.0f} {ebit/cap*100:>5.0f}% {(ebit+am)/cap*100:>6.0f}%"
          f"   (ca {ca:.0f} cash {cash:.0f} ppe {ppe:.0f} rou {rou:.0f} ap {ap:.0f} comp {comp:.0f} tax {tax:.0f} oth {oth:.0f} oll {oll:.0f} pti {pti:.0f} ie {ie:.0f} ii {ii:.0f})")

a, b = res[2018], res[2025]
print(f"incremental 2018->2025: EBIT+amort {b[1]+b[2]-(a[1]+a[2]):.0f} on added tangible capital {b[0]-a[0]:.0f}")
