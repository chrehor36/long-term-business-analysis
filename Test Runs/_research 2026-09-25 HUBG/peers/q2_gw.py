"""HUBG and JBHT: operating income over average (NTOA + goodwill + intangibles), i.e. with the price paid for
acquisitions put back into capital. Reliable HUBG filings only (filed on or before 2023-02-28).
TRANSCRIPTION AND ARITHMETIC ONLY."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hubg_row as H
H.SALES = H.SALES + ["RevenueFromContractWithCustomerIncludingAssessedTax"]
yrs = list(range(2008, 2026))
for tk, k in (("HUBG", dict(cutoff="2023-02-28")), ("JBHT", {})):
    F = H.load(tk)
    gw = H.first(F, ["Goodwill"], True, **k)
    it = H.first(F, ["IntangibleAssetsNetExcludingGoodwill", "FiniteLivedIntangibleAssetsNet"], True, **k)
    rows = H.metrics(tk, yrs, **k)
    prev = None
    print(tk)
    for y, m in rows:
        if not m: prev = None; continue
        cap = m["ntoa"] + (gw.get(y) or 0) / 1e6 + (it.get(y) or 0) / 1e6
        r = (m["op"] / ((cap + prev) / 2)) if (prev and m["op"] is not None) else None
        print(f"  {y}: goodwill {(gw.get(y) or 0)/1e6:,.0f} intang {(it.get(y) or 0)/1e6:,.0f} capital {cap:,.0f} op {m['op']:,.0f} ret {'' if r is None else f'{r:.1%}'}")
        prev = cap
