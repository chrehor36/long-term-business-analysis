# -*- coding: utf-8 -*-
"""Pull XBRL annual series for the BA competitor row. Transcription/screening only."""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
OUT = "Test Runs/_research 2026-09-12 BA/peers"

TICKERS = ["LMT","NOC","RTX","GD","ERJ","SPR","TXT","TDG","HEI","BA"]
FORMS = ("10-K","20-F")

TAGS = {
 "REV": ["RevenueFromContractWithCustomerExcludingAssessedTax","Revenues",
         "RevenueFromContractWithCustomerIncludingAssessedTax","SalesRevenueNet"],
 "OPINC": ["OperatingIncomeLoss","ProfitLossFromOperatingActivities"],
 "NI": ["NetIncomeLoss","ProfitLoss"],
 "OCF": ["NetCashProvidedByUsedInOperatingActivities",
         "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations",
         "CashFlowsFromUsedInOperatingActivities"],
 "CAPEX": ["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets",
           "PaymentsForCapitalImprovements","PurchaseOfPropertyPlantAndEquipment"],
 "DA": ["DepreciationDepletionAndAmortization","DepreciationAmortizationAndAccretionNet",
        "DepreciationAndAmortization","DepreciationAmortisationAndImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLoss"],
 "SBC": ["ShareBasedCompensation","AllocatedShareBasedCompensationExpense",
         "ShareBasedCompensationArrangementByShareBasedPaymentAwardCompensationCost"],
}
# instant (point-in-time) tags
ITAGS = {
 "CASH": ["CashAndCashEquivalentsAtCarryingValue","CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents",
          "CashAndCashEquivalents"],
 "STINV": ["ShortTermInvestments","OtherShortTermInvestments","MarketableSecuritiesCurrent",
           "AvailableForSaleSecuritiesDebtSecuritiesCurrent"],
 "LTDNC": ["LongTermDebtNoncurrent","LongTermDebtAndCapitalLeaseObligations","LongTermBorrowings"],
 "LTDC": ["LongTermDebtCurrent","LongTermDebtAndCapitalLeaseObligationsCurrent","DebtCurrent",
          "ShortTermBorrowings","CurrentPortionOfLongTermDebt"],
 "LTDTOT": ["LongTermDebt","DebtLongtermAndShorttermCombinedAmount","Borrowings"],
 "EQ": ["StockholdersEquity","StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest","Equity"],
}

def instants(facts, tags, forms=FORMS):
    from datetime import date
    out = {}
    for tax in ("us-gaap","ifrs-full"):
        node = facts.get("facts",{}).get(tax,{})
        for t in tags:
            if t not in node: continue
            for unit, pts in node[t]["units"].items():
                if unit not in ("USD","BRL"): continue
                for x in pts:
                    if x.get("form") in forms and not x.get("start") and x.get("end"):
                        f = x.get("filed") or ""
                        prev = out.get(x["end"])
                        if prev is None or (prev[1]==t and f>prev[2]) or (prev[1]!=t and tags.index(t)<tags.index(prev[1]) if prev[1] in tags else False):
                            if prev is None or prev[1]==t:
                                out[x["end"]] = (x["val"]/1e6, t, f)
    return {k:v[0] for k,v in out.items()}, unitless(out)

def unitless(out):
    return None

res = {}
for tk in TICKERS:
    cik, name = sources.cik_for(tk)
    print("="*70); print(tk, cik, name)
    if not cik:
        res[tk] = {"error":"no cik"}; continue
    try:
        f = sources.sec_facts(cik)
    except Exception as e:
        print("  FACTS FAIL", e); res[tk]={"cik":cik,"name":name,"error":str(e)}; continue
    d = {"cik":cik,"name":name,"tags":{},"series":{},"instants":{}}
    for k,tags in TAGS.items():
        s, used, unit = sources.annual(f, tags, forms=FORMS, vintage="newest")
        d["series"][k]=s; d["tags"][k]=(used,unit)
        yrs = sorted(s)[-4:]
        print(f"  {k:<6} unit={unit} tags={used}")
        for y in yrs: print(f"      {y} {s[y]:>14,.1f}")
    for k,tags in ITAGS.items():
        s,_ = instants(f, tags)
        d["instants"][k]=s
        yrs = sorted(s)[-3:]
        print(f"  [i]{k:<5} " + "  ".join(f"{y}={s[y]:,.0f}" for y in yrs))
    res[tk]=d
    time.sleep(0.3)

json.dump(res, open(os.path.join(OUT,"xbrl_raw.json"),"w"), indent=1)
print("\nwrote xbrl_raw.json")
