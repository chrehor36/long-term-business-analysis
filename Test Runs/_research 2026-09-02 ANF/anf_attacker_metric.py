#!/usr/bin/env python3
"""Return on unleveraged net tangible operating assets [E2-43] - identical formula both
sides, imported unchanged from the AEO/NKE runs:
  numerator   = operating income (10-K)
  denominator = net PP&E + inventories + trade receivables - trade payables
All figures SEC companyfacts, form 10-K, dedup by period end (earliest filing wins).
Transcription and screening, not a verdict [E3-27].
"""
import json, os, sys
from datetime import date

ROOT = r"c:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "Screens"))
sys.path.insert(0, os.path.join(ROOT, "Backtests", "scripts"))
import floor_screen as FS  # noqa: E402
import bt17_microcap as M  # noqa: E402

OPINC = ["OperatingIncomeLoss"]
PPE = ["PropertyPlantAndEquipmentNet"]
INV = ["InventoryNet", "InventoryFinishedGoodsNetOfReserves"]
REC = ["ReceivablesNetCurrent", "AccountsReceivableNetCurrent", "NontradeReceivablesCurrent"]
PAY = ["AccountsPayableCurrent", "AccountsPayableTradeCurrent"]
OLL = ["OperatingLeaseLiability"]  # total; fall back to current+noncurrent
OLL2 = ["OperatingLeaseLiabilityCurrent", "OperatingLeaseLiabilityNoncurrent"]
EQ = ["StockholdersEquity"]
CASH = ["CashAndCashEquivalentsAtCarryingValue"]
STINV = ["ShortTermInvestments", "MarketableSecuritiesCurrent"]


def instant(facts, tags):
    """{date: value} for instant (balance-sheet) tags from 10-K/10-Q filings; earliest
    filing per date wins, earlier tag in list wins."""
    ns = facts.get("facts", {}).get("us-gaap", {})
    by_end = {}
    for rank, tag in enumerate(tags):
        for x in ns.get(tag, {}).get("units", {}).get("USD", []):
            if x.get("form") not in ("10-K", "10-K/A", "10-Q", "20-F"):
                continue
            e, f = x.get("end"), x.get("filed")
            if not (e and f) or x.get("start"):
                continue
            ed, fd = date.fromisoformat(e), date.fromisoformat(f)
            prev = by_end.get(ed)
            if prev is None or (rank == prev[1] and fd < prev[2]):
                by_end[ed] = (float(x["val"]), rank, fd)
    return {e: v for e, (v, _, _) in by_end.items()}


def series(cik, label, years=11):
    p = os.path.join(M.CACHE, f"facts_{cik}.json")
    if not os.path.exists(p):
        print(f"{label}: NO CACHED FACTS - fetch needed"); return
    facts = json.load(open(p, encoding="utf-8"))
    op = FS.annual(facts, OPINC)
    ppe, inv = instant(facts, PPE), instant(facts, INV)
    rec, pay = instant(facts, REC), instant(facts, PAY)
    oll_t, ollc = instant(facts, OLL), instant(facts, OLL2[:1])
    olln = instant(facts, OLL2[1:])
    print(f"\n=== {label} (CIK {cik}) ===")
    print(f"{'FY end':>12s} {'op income':>10s} {'PP&E':>9s} {'inv':>9s} {'recv':>8s} "
          f"{'payab':>9s} {'denom':>9s} {'RONTOA':>8s} {'lease-cap':>9s}")
    for e in sorted(op)[-years:]:
        o = op[e]
        parts = [ppe.get(e), inv.get(e)]
        if None in parts:
            print(f"{str(e):>12s} {o/1e6:>10,.1f}  balance-sheet tag missing"); continue
        r, pa = rec.get(e, 0.0), pay.get(e, 0.0)
        den = parts[0] + parts[1] + r - pa
        ol = oll_t.get(e)
        if ol is None:
            c, n = ollc.get(e), olln.get(e)
            ol = (c or 0) + (n or 0) if (c or n) else None
        den_l = den + ol if ol else None
        print(f"{str(e):>12s} {o/1e6:>10,.1f} {parts[0]/1e6:>9,.1f} {parts[1]/1e6:>9,.1f} "
              f"{r/1e6:>8,.1f} {pa/1e6:>9,.1f} {den/1e6:>9,.1f} {o/den:>8.1%} "
              + (f"{o/den_l:>9.1%}" if den_l else "        -"))


series(1018840, "ANF Abercrombie & Fitch")
series(919012, "AEO American Eagle", years=2)
series(39911, "GPS Gap Inc", years=2)
series(912615, "URBN Urban Outfitters", years=2)
series(1397187, "LULU Lululemon", years=2)
