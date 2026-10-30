"""Annual series from companyfacts (screening/transcription only; every figure the run leans on is re-read in a filing).
Newest-filed value per fiscal-year end, annual durations only."""
import json, os
from datetime import date
HERE = os.path.dirname(os.path.abspath(__file__))
f = json.load(open(os.path.join(HERE, "companyfacts.json")))["facts"]["us-gaap"]


def annual(tags, instant=False):
    out = {}
    for t in tags:
        for u in f.get(t, {}).get("units", {}).get("USD", []):
            if u.get("form") != "10-K":
                continue
            e = u["end"]
            if not instant:
                if "start" not in u:
                    continue
                d = (date.fromisoformat(e) - date.fromisoformat(u["start"])).days
                if not 340 <= d <= 380:
                    continue
            prev = out.get(e)
            if prev is None or u["filed"] > prev[1]:
                out[e] = (u["val"] / 1e6, u["filed"])
    return {e: v for e, (v, _) in out.items()}


rev = annual(["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"])
gp = annual(["GrossProfit"])
oi = annual(["OperatingIncomeLoss"])
rd = annual(["ResearchAndDevelopmentExpense"])
ni = annual(["NetIncomeLoss"])
eq = annual(["StockholdersEquity"], instant=True)
tax = annual(["IncomeTaxesPaidNet", "IncomeTaxesPaid"])
pti = annual(["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
              "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"])
ends = sorted(e for e in rev if e >= "2014-01-01")
print("| FY end | revenue | gross margin | op income | op margin | R&D % rev | net income | equity (end) | NI / avg equity | cash tax / pretax |")
print("|---|---|---|---|---|---|---|---|---|---|")
prev_eq = None
for e in ends:
    r = rev.get(e); g = gp.get(e); o = oi.get(e); d = rd.get(e); n = ni.get(e); q = eq.get(e)
    roe = ""
    pe = [k for k in sorted(eq) if k < e]
    if q and pe and n:
        roe = f"{n / ((q + eq[pe[-1]]) / 2) * 100:.1f}%"
    ct = f"{tax[e] / pti[e] * 100:.1f}%" if e in tax and e in pti and pti[e] else ""
    fmt = lambda x: f"{x:,.0f}" if x is not None else ""
    print(f"| {e} | {fmt(r)} | {g / r * 100:.1f}% |" if g and r else f"| {e} | {fmt(r)} | |", end="")
    print(f" {fmt(o)} | {o / r * 100:.1f}% | {d / r * 100:.1f}% | {fmt(n)} | {fmt(q)} | {roe} | {ct} |" if o and r and d else f" {fmt(o)} | | | {fmt(n)} | {fmt(q)} | {roe} | {ct} |")
