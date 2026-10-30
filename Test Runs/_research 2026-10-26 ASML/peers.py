"""Competitor rows from XBRL companyfacts (transcription; the run cross-checks one figure per peer against the filed 10-K).
Operating margin and owner cash (OCF - SBC - capex) as a share of sales, by fiscal year, 2016-2025, plus
operating income after tax proxy is NOT used; the capital test is operating income against tangible capital employed
(total assets - cash & marketable securities - goodwill - intangibles - non-interest current liabilities is too fine
for XBRL; we use equity + debt - cash - goodwill - intangibles, said so)."""
import json, os, sys, time, urllib.request
from datetime import date
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
UA = "Chris Hrehor chrehor36@gmail.com"
PEERS = {"AMAT": "0000006951", "LRCX": "0000707549", "KLAC": "0000319201", "ASML": "0000937966"}


def facts(cik):
    p = os.path.join(CACHE, f"facts_{cik}.json")
    if not os.path.exists(p):
        req = urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            open(p, "wb").write(r.read())
        time.sleep(0.3)
    return json.load(open(p))["facts"]["us-gaap"]


def annual(g, tags, instant=False):
    out = {}
    for t in tags:
        if t not in g:
            continue
        for unit, vals in g[t]["units"].items():
            for x in vals:
                if x.get("form") not in ("10-K", "20-F", "10-K/A"):
                    continue
                if not instant:
                    if "start" not in x: continue
                    d = (date.fromisoformat(x["end"]) - date.fromisoformat(x["start"])).days
                    if not 350 <= d <= 380: continue
                fy = int(x["end"][:4]) if x["end"][5:7] > "03" else int(x["end"][:4]) - 1
                if fy not in out or x["filed"] > out[fy][1]:
                    out[fy] = (x["val"] / 1e6, x["filed"], x["end"])
        # keep first tag that has data for the year; later tags fill gaps
    return out


def merged(g, tags, instant=False):
    res = {}
    for t in tags:
        a = annual(g, [t], instant)
        for k, v in a.items():
            res.setdefault(k, v)
    return res


rows = {}
for tk, cik in PEERS.items():
    g = facts(cik)
    rev = merged(g, ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"])
    op = merged(g, ["OperatingIncomeLoss"])
    if tk == "KLAC":  # KLAC tags no operating income after FY2014: pre-tax income plus interest expense, said so in the run
        _pre = merged(g, ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"])
        _int = merged(g, ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt"])
        op = {k: (v[0] + (_int.get(k, (0,))[0] or 0), v[1], v[2]) for k, v in _pre.items()}
    ocf = merged(g, ["NetCashProvidedByUsedInOperatingActivities", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"])
    capex = merged(g, ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"])
    sbc = merged(g, ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"])
    tax = merged(g, ["IncomeTaxExpenseBenefit"])
    pre = merged(g, ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
                     "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments",
                     "IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic"])
    eq = merged(g, ["StockholdersEquity"], True)
    gw = merged(g, ["Goodwill"], True)
    intang = merged(g, ["IntangibleAssetsNetExcludingGoodwill", "FiniteLivedIntangibleAssetsNet"], True)
    cash = merged(g, ["CashAndCashEquivalentsAtCarryingValue"], True)
    sti = merged(g, ["ShortTermInvestments", "AvailableForSaleSecuritiesDebtSecuritiesCurrent", "MarketableSecuritiesCurrent"], True)
    lti = merged(g, ["LongTermInvestments", "AvailableForSaleSecuritiesDebtSecuritiesNoncurrent", "MarketableSecuritiesNoncurrent"], True)
    debt = merged(g, ["LongTermDebtNoncurrent", "LongTermDebt"], True)
    debtc = merged(g, ["LongTermDebtCurrent", "DebtCurrent"], True)
    print(f"\n== {tk}  (fiscal year labelled by the calendar year in which it ends; AMAT Oct, LRCX/KLAC June, ASML Dec; USD/EUR millions)")
    print("FY    sales     op%   ownercash%  tax%   ROTC(op after tax / tangible capital)")
    for fy in range(2016, 2027):
        if fy not in rev or fy not in op: continue
        s = rev[fy][0]; o = op[fy][0]
        oc = (ocf.get(fy, (None,))[0] or 0) - (sbc.get(fy, (0,))[0] or 0) - (capex.get(fy, (0,))[0] or 0)
        tr = (tax[fy][0] / pre[fy][0]) if fy in tax and fy in pre and pre[fy][0] else None
        cap = None
        if fy in eq:
            cap = eq[fy][0] + (debt.get(fy, (0,))[0] or 0) + (debtc.get(fy, (0,))[0] or 0) - (cash.get(fy, (0,))[0] or 0) \
                  - (sti.get(fy, (0,))[0] or 0) - (lti.get(fy, (0,))[0] or 0) - (gw.get(fy, (0,))[0] or 0) - (intang.get(fy, (0,))[0] or 0)
        rotc = (o * (1 - (tr or 0.15)) / cap) if cap and cap > 0 else None
        print(f"{fy}  {s:8.0f}  {100*o/s:5.1f}   {100*oc/s:6.1f}   {'' if tr is None else '%4.1f' % (100*tr)}   "
              f"{'n/a' if rotc is None else '%5.1f%%' % (100*rotc)}  (tangible capital {cap if cap is None else round(cap)})")
        rows.setdefault(tk, {})[fy] = dict(sales=s, op=o, oc=oc, tax=tr, cap=cap)
json.dump(rows, open(os.path.join(HERE, "peers.json"), "w"), indent=1)
