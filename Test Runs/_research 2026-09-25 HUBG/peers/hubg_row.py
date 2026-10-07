"""HUBG competitor row. TRANSCRIPTION AND ARITHMETIC ONLY, NO CONCLUSION.
Adapted from peer_metrics_pg_copy.py (same NTOA definition). One change: an optional FILED CUTOFF, so HUBG
can be read only from filings made on or before 2023-02-24 (the FY2022 10-K), i.e. from statements the
registrant has NOT withdrawn under Item 4.02. HUBG values from later filings are printed separately and
labelled WITHDRAWN.
Metrics: GAAP operating margin; GAAP operating income / average NTOA."""
import json, os, sys
from datetime import date
HERE = os.path.dirname(os.path.abspath(__file__))
M = 1e6
def load(tk): return json.load(open(os.path.join(HERE, f"{tk}_companyfacts.json"), encoding="utf-8"))["facts"]
def annual(F, tag, instant=False, cutoff=None, after=None):
    best = {}
    for ns in ("us-gaap",):
        if ns not in F or tag not in F[ns]: continue
        for unit, arr in F[ns][tag]["units"].items():
            if unit != "USD": continue
            for x in arr:
                if x.get("form") not in ("10-K", "10-K/A") or x.get("fp") != "FY": continue
                if cutoff and x["filed"] > cutoff: continue
                if after and x["filed"] <= after: continue
                e = x["end"]
                if not instant:
                    if "start" not in x: continue
                    d = (date.fromisoformat(e) - date.fromisoformat(x["start"])).days
                    if not (340 <= d <= 380): continue
                y = int(e[:4])
                if y not in best or x["filed"] > best[y][1]: best[y] = (x["val"], x["filed"])
    return {y: v[0] for y, v in best.items()}
def first(F, tags, instant=False, **k):
    d = {}
    for t in tags:
        for y, v in annual(F, t, instant, **k).items(): d.setdefault(y, v)
    return d
SALES = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet", "SalesRevenueServicesNet"]
def metrics(tk, years, **k):
    F = load(tk)
    g = lambda tags, inst=False: first(F, tags, inst, **k)
    sales, op = g(SALES), g(["OperatingIncomeLoss"])
    assets, cash = g(["Assets"], True), g(["CashAndCashEquivalentsAtCarryingValue"], True)
    mkt = g(["MarketableSecuritiesCurrent", "ShortTermInvestments", "AvailableForSaleSecuritiesDebtSecuritiesCurrent"], True)
    gw, intang = g(["Goodwill"], True), g(["IntangibleAssetsNetExcludingGoodwill", "FiniteLivedIntangibleAssetsNet"], True)
    rou, cl = g(["OperatingLeaseRightOfUseAsset"], True), g(["LiabilitiesCurrent"], True)
    debtc = g(["DebtCurrent"], True); stb = g(["ShortTermBorrowings"], True)
    ltdc = g(["LongTermDebtCurrent"], True); cap = g(["FinanceLeaseLiabilityCurrent", "CapitalLeaseObligationsCurrent"], True)
    leasec = g(["OperatingLeaseLiabilityCurrent"], True)
    rows, prev = [], None
    for y in years:
        if y not in assets or y not in cl: rows.append((y, None)); prev = None; continue
        d = debtc.get(y)
        if d is None: d = (stb.get(y) or 0) + (ltdc.get(y) or 0) + (cap.get(y) or 0)
        ntoa = (assets[y] - (cash.get(y) or 0) - (mkt.get(y) or 0) - (gw.get(y) or 0) - (intang.get(y) or 0) - (rou.get(y) or 0)) - (cl[y] - d - (leasec.get(y) or 0))
        ntoa /= M
        s, o = sales.get(y), op.get(y)
        avg = (ntoa + prev) / 2 if prev is not None else None
        rows.append((y, dict(sales=s/M if s else None, op=o/M if o is not None else None, ntoa=ntoa,
                             om=(o/s) if (o is not None and s) else None, ret=(o/M/avg) if (o is not None and avg) else None)))
        prev = ntoa
    return rows
def show(tk, rows, label=""):
    print("=" * 80); print(tk, label)
    print("| FY | revenue $M | op income $M | op margin | NTOA $M | op inc / avg NTOA |"); print("|---|---|---|---|---|---|")
    f = lambda v, sp="{:,.0f}": (sp.format(v) if v is not None else "n/f")
    for y, m in rows:
        if m: print(f"| {y} | {f(m['sales'])} | {f(m['op'])} | {f(m['om'],'{:.1%}')} | {f(m['ntoa'])} | {f(m['ret'],'{:.1%}')} |")
if __name__ == "__main__":
    yrs = list(range(2008, 2026))
    show("HUBG", metrics("HUBG", yrs, cutoff="2023-02-28"), "(filings on or before 2023-02-28 only: NOT WITHDRAWN)")
    show("HUBG", metrics("HUBG", yrs, after="2023-02-28"), "(filings after 2023-02-28: FY2023-24 WITHDRAWN under Item 4.02)")
    for tk in sys.argv[1:]: show(tk, metrics(tk, yrs))
