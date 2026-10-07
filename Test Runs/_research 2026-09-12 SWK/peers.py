import sys, json
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
from datetime import date

RES = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-12 SWK"

PEERS = ["SWK", "SNA", "ITW", "EMR", "FBIN", "HD", "LOW", "TTC", "MMM"]

INST = {
    "rev": ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues",
            "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet"],
    "opinc": ["OperatingIncomeLoss"],
    "pretax": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
               "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"],
    "tax": ["IncomeTaxExpenseBenefit"],
    "gross": ["GrossProfit"],
}
BAL = {
    "ppe": ["PropertyPlantAndEquipmentNet"],
    "inv": ["InventoryNet"],
    "ar": ["AccountsReceivableNetCurrent", "ReceivablesNetCurrent"],
    "ap": ["AccountsPayableCurrent", "AccountsPayableTradeCurrent"],
    "gw": ["Goodwill"],
    "intang": ["FiniteLivedIntangibleAssetsNet", "IntangibleAssetsNetExcludingGoodwill"],
    "assets": ["Assets"],
    "cash": ["CashAndCashEquivalentsAtCarryingValue"],
    "equity": ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
    "ltd": ["LongTermDebtNoncurrent", "LongTermDebt"],
    "std": ["ShortTermBorrowings", "OtherShortTermBorrowings", "LongTermDebtCurrent",
            "DebtCurrent", "CommercialPaper"],
}


def instants(facts, tags, forms=("10-K",)):
    out = {}
    for tax in ("us-gaap",):
        node = facts.get("facts", {}).get(tax, {})
        for t in tags:
            if t not in node:
                continue
            for unit, pts in node[t]["units"].items():
                if unit != "USD":
                    continue
                for x in pts:
                    if x.get("form") in forms and not x.get("start"):
                        e, f = x["end"], x.get("filed") or ""
                        prev = out.get(e)
                        if prev is None or f > prev[1]:
                            out[e] = (x["val"] / 1e6, f, t)
    return {k: v[0] for k, v in out.items()}


rows = {}
for tk in PEERS:
    try:
        cik, nm = sources.cik_for(tk)
        facts = sources.sec_facts(cik)
    except Exception as e:
        print(tk, "FETCH FAIL", type(e).__name__, e)
        continue
    d = {}
    for k, tags in INST.items():
        s, _, _ = sources.annual(facts, tags, vintage="newest")
        d[k] = s
    # newest fiscal year end common to revenue and opinc
    ys = sorted(set(d["rev"]) & set(d["opinc"]))
    fy = ys[-1]
    bal = {}
    for k, tags in BAL.items():
        bal[k] = instants(facts, tags)
    # balance-sheet date closest to fy
    def pick(k):
        s = bal[k]
        if not s:
            return None
        if fy in s:
            return s[fy]
        cands = [e for e in s if abs((date.fromisoformat(e) - date.fromisoformat(fy)).days) <= 8]
        return s[max(cands)] if cands else None
    b = {k: pick(k) for k in BAL}
    debt = (b.get("ltd") or 0) + (b.get("std") or 0)
    rows[tk] = dict(name=nm, fy=fy, rev=d["rev"][fy], opinc=d["opinc"][fy],
                    pretax=d["pretax"].get(fy), tax=d["tax"].get(fy),
                    gross=d["gross"].get(fy), debt=debt, **b)
    r = rows[tk]
    eff = (r["tax"] / r["pretax"]) if (r["tax"] and r["pretax"]) else None
    nopat = r["opinc"] * (1 - eff) if eff else None
    tang = None
    if all(r.get(k) is not None for k in ("ppe", "inv", "ar", "ap")):
        tang = r["ppe"] + r["inv"] + r["ar"] - r["ap"]
    gwi = (r.get("gw") or 0) + (r.get("intang") or 0)
    ic = (r.get("equity") or 0) + r["debt"] - (r.get("cash") or 0)
    print(f"\n{tk} {nm}  FY end {fy}")
    print(f"   rev {r['rev']:>12,.0f}  opinc {r['opinc']:>10,.0f}  op margin {100*r['opinc']/r['rev']:>6.1f}%"
          f"  gross% {100*r['gross']/r['rev'] if r['gross'] else float('nan'):>6.1f}")
    print(f"   ppe {r.get('ppe')}  inv {r.get('inv')}  ar {r.get('ar')}  ap {r.get('ap')}  -> tangible {tang}")
    print(f"   gw {r.get('gw')} intang {r.get('intang')} assets {r.get('assets')}  gwi/assets "
          f"{100*gwi/r['assets'] if r.get('assets') else float('nan'):.0f}%")
    print(f"   equity {r.get('equity')}  debt {debt:,.0f}  cash {r.get('cash')}  IC {ic:,.0f}")
    if tang:
        print(f"   RONTOA {100*r['opinc']/tang:>6.1f}%   incl GW&I {100*r['opinc']/(tang+gwi):>6.1f}%")
    if nopat and ic:
        print(f"   eff tax {100*eff:.1f}%  NOPAT {nopat:,.0f}  after-tax ROIC {100*nopat/ic:>6.1f}%")

json.dump(rows, open(rf"{RES}\peers.json", "w"), indent=1, default=str)
