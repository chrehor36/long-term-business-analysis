"""Competitor-row arithmetic for the CL Q2 run. TRANSCRIPTION AND ARITHMETIC ONLY. No conclusion.
Same definition as the subject's ntoa.py:
NTOA = total assets - cash - current marketable securities - goodwill - other intangibles - operating ROU assets
       - (current liabilities - debt due within one year - current operating lease liabilities).
Return on avg NTOA = GAAP operating profit / average of the year's and prior year's NTOA.
Peers are SEC registrants with companyfacts on disk. Fiscal years are each company's own; the FY label is the
calendar year of the fiscal year END. UL and HLN are 20-F/IFRS filers and are NOT here; they are read by hand."""
import json, os, sys
from datetime import date
HERE = os.path.dirname(os.path.abspath(__file__))

def load(tk):
    p = os.path.join(HERE, f"{tk}_companyfacts.json")
    return json.load(open(p, encoding="utf-8"))["facts"]

def annual(F, tag, instant=False):
    best = {}
    for ns in ("us-gaap", "ifrs-full"):
        if ns not in F or tag not in F[ns]:
            continue
        for unit, arr in F[ns][tag]["units"].items():
            if unit not in ("USD", "shares"):
                continue
            for x in arr:
                if x.get("form") not in ("10-K", "10-K/A"):
                    continue
                if x.get("fp") != "FY":
                    continue
                e = x["end"]
                if not instant:
                    if "start" not in x:
                        continue
                    d = (date.fromisoformat(e) - date.fromisoformat(x["start"])).days
                    if not (340 <= d <= 380):
                        continue
                fy = x.get("fy")
                # label by fiscal-year end date year, not the filer's fy field
                y = int(e[:4])
                if instant:
                    # a 10-K instant can be the prior year-end comparative; keep both, keyed by year
                    pass
                if y not in best or x["filed"] > best[y][1]:
                    best[y] = (x["val"], x["filed"])
    return {y: v[0] for y, v in best.items()}

def first(F, tags, instant=False):
    d = {}
    for t in tags:
        for y, v in annual(F, t, instant).items():
            d.setdefault(y, v)
    return d

M = 1e6
SALES = ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet",
         "RevenueFromContractWithCustomerIncludingAssessedTax"]
def metrics(tk, years):
    F = load(tk)
    sales = first(F, SALES)
    gross = first(F, ["GrossProfit"])
    op = first(F, ["OperatingIncomeLoss"])
    assets = first(F, ["Assets"], True)
    cash = first(F, ["CashAndCashEquivalentsAtCarryingValue", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"], True)
    mkt = first(F, ["MarketableSecuritiesCurrent", "ShortTermInvestments", "AvailableForSaleSecuritiesDebtSecuritiesCurrent"], True)
    gw = first(F, ["Goodwill"], True)
    intang = first(F, ["IntangibleAssetsNetExcludingGoodwill", "FiniteLivedIntangibleAssetsNet"], True)
    rou = first(F, ["OperatingLeaseRightOfUseAsset"], True)
    cl = first(F, ["LiabilitiesCurrent"], True)
    debtc = first(F, ["DebtCurrent"], True)
    stb = first(F, ["ShortTermBorrowings", "OtherShortTermBorrowings"], True)
    ltdc = first(F, ["LongTermDebtCurrent"], True)
    notesp = first(F, ["NotesPayableCurrent", "CommercialPaper"], True)
    leasec = first(F, ["OperatingLeaseLiabilityCurrent"], True)
    rows = []
    prev = None
    for y in years:
        if y not in assets or y not in cl:
            rows.append((y, None)); prev = None; continue
        d = debtc.get(y)
        if d is None:
            d = (stb.get(y) or 0) + (ltdc.get(y) or 0) + (notesp.get(y) or 0)
        ntoa = (assets[y] - (cash.get(y) or 0) - (mkt.get(y) or 0) - (gw.get(y) or 0) - (intang.get(y) or 0) - (rou.get(y) or 0)) \
               - (cl[y] - d - (leasec.get(y) or 0))
        ntoa /= M
        s = sales.get(y); o = op.get(y); gp = gross.get(y)
        avg = (ntoa + prev) / 2 if prev is not None else ntoa
        rows.append((y, dict(sales=s/M if s else None, gross=gp/M if gp else None, op=o/M if o else None,
                             ntoa=ntoa, ret=(o/M/avg) if (o and avg) else None,
                             gm=(gp/s) if (gp and s) else None, om=(o/s) if (o and s) else None,
                             debt_used=d/M)))
        prev = ntoa
    return rows

if __name__ == "__main__":
    yrs = list(range(2016, 2027))
    for tk in sys.argv[1:]:
        print("=" * 90); print(tk)
        print("| FY end yr | net sales | gross profit | gross margin | op profit | op margin | NTOA | ret on avg NTOA | debt<1y used |")
        print("|---|---|---|---|---|---|---|---|---|")
        for y, m in metrics(tk, yrs):
            if not m: continue
            f = lambda v, sp="{:,.0f}": (sp.format(v) if v is not None else "n/f")
            print(f"| {y} | {f(m['sales'])} | {f(m['gross'])} | {f(m['gm'],'{:.1%}')} | {f(m['op'])} | {f(m['om'],'{:.1%}')} | {f(m['ntoa'])} | {f(m['ret'],'{:.1%}')} | {f(m['debt_used'])} |")
