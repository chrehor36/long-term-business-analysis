import sys, json
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
from datetime import date

RES = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-12 SWK"
PEERS = ["SNA", "FBIN", "EMR", "TTC", "HD", "LOW", "ITW"]

DUR = {
    "rev": ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues",
            "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet",
            "RevenuesNetOfInterestExpense"],
    "opinc": ["OperatingIncomeLoss"],
    "pretax": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
               "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments",
               "IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign"],
    "tax": ["IncomeTaxExpenseBenefit"],
    "intexp": ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt",
               "InterestIncomeExpenseNet"],
    "intinc": ["InvestmentIncomeInterest", "InterestIncomeOther"],
    "gross": ["GrossProfit"],
}
BAL = {
    "ppe": ["PropertyPlantAndEquipmentNet"],
    "inv": ["InventoryNet"],
    "ar": ["AccountsReceivableNetCurrent", "ReceivablesNetCurrent",
           "AccountsAndOtherReceivablesNetCurrent", "AccountsNotesAndLoansReceivableNetCurrent"],
    "ap": ["AccountsPayableCurrent", "AccountsPayableTradeCurrent"],
    "gw": ["Goodwill"],
    "intang": ["FiniteLivedIntangibleAssetsNet", "IntangibleAssetsNetExcludingGoodwill"],
    "assets": ["Assets"],
    "cash": ["CashAndCashEquivalentsAtCarryingValue", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"],
    "equity": ["StockholdersEquity"],
    "ltd": ["LongTermDebtNoncurrent"],
    "std": ["ShortTermBorrowings", "OtherShortTermBorrowings", "LongTermDebtCurrent",
            "DebtCurrent", "CommercialPaper", "NotesPayableCurrent"],
}


def instants(facts, tags):
    out = {}
    node = facts.get("facts", {}).get("us-gaap", {})
    for t in tags:
        if t not in node:
            continue
        for unit, pts in node[t]["units"].items():
            if unit != "USD":
                continue
            for x in pts:
                if x.get("form") == "10-K" and not x.get("start"):
                    e, f = x["end"], x.get("filed") or ""
                    if e not in out or f > out[e][1] or (f == out[e][1] and t == tags[0]):
                        out[e] = (x["val"] / 1e6, f)
    return {k: v[0] for k, v in out.items()}


for tk in PEERS:
    try:
        cik, nm = sources.cik_for(tk)
        facts = sources.sec_facts(cik)
    except Exception as e:
        print(tk, "FETCH FAIL", e); continue
    d = {}
    for k, tags in DUR.items():
        s, t, _ = sources.annual(facts, tags, vintage="newest")
        d[k] = s
    ys = sorted(d["rev"])
    if not ys:
        print(tk, "no revenue"); continue
    fy = ys[-1]
    b = {}
    for k, tags in BAL.items():
        s = instants(facts, tags)
        if fy in s:
            b[k] = s[fy]
        else:
            c = [e for e in s if abs((date.fromisoformat(e) - date.fromisoformat(fy)).days) <= 8]
            b[k] = s[max(c)] if c else None
    rev = d["rev"][fy]
    op = d["opinc"].get(fy)
    pt = d["pretax"].get(fy)
    ie = d["intexp"].get(fy)
    ebit = op if op is not None else ((pt + ie) if (pt is not None and ie is not None) else None)
    debt = (b.get("ltd") or 0) + (b.get("std") or 0)
    tang = None
    if all(b.get(k) is not None for k in ("ppe", "inv", "ar", "ap")):
        tang = b["ppe"] + b["inv"] + b["ar"] - b["ap"]
    gwi = (b.get("gw") or 0) + (b.get("intang") or 0)
    ic = (b.get("equity") or 0) + debt - (b.get("cash") or 0)
    eff = (d["tax"][fy] / pt) if (pt and d["tax"].get(fy)) else None
    print(f"\n{tk:5s} {nm[:34]:34s} FY {fy}  rev {rev:>10,.0f}")
    print(f"      opinc(tag) {op}  pretax {pt}  intexp {ie}  -> EBIT {ebit}")
    if ebit:
        print(f"      EBIT margin {100*ebit/rev:.1f}%")
    print(f"      ppe {b.get('ppe')} inv {b.get('inv')} ar {b.get('ar')} ap {b.get('ap')} tang {tang}")
    print(f"      gw {b.get('gw')} intang {b.get('intang')} gwi {gwi:,.0f} assets {b.get('assets')}")
    print(f"      equity {b.get('equity')} debt {debt:,.0f} cash {b.get('cash')} IC {ic:,.0f} efftax "
          f"{100*eff if eff else float('nan'):.1f}%")
    if ebit and tang:
        print(f"      RONTOA {100*ebit/tang:.1f}%  inclGWI {100*ebit/(tang+gwi):.1f}%")
    if ebit and ic and eff:
        print(f"      ROIC(at) {100*ebit*(1-eff)/ic:.1f}%")
