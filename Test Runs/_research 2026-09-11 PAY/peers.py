#!/usr/bin/env python3
"""Competitor row for PAY - same metric, same window (FY2025), from each peer's own
companyfacts (10-K XBRL). Transcription only; accession recorded per figure."""
import sys, os, json, time, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sources as S
from datetime import date
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
CACHE = os.path.join(HERE, "cache"); os.makedirs(CACHE, exist_ok=True)

def facts_for(tk):
    p = os.path.join(CACHE, f"peer_{tk}.json")
    if os.path.exists(p): return json.load(open(p))
    c = {"ESMT": 1863105}.get(tk) or S.cik_for(tk)
    if isinstance(c, (tuple, list)): c = c[0]
    c = int(str(c).lstrip("0"))
    for i in range(4):
        try:
            d = urllib.request.urlopen(urllib.request.Request(
                f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json", headers=UA), timeout=90).read()
            break
        except Exception as e:
            time.sleep(2*(i+1)); last = e
    j = json.loads(d); json.dump(j, open(p, "w")); time.sleep(0.4); return j

def val(f, tags, fy_end_year, unit="USD", dur=True):
    ug = f["facts"].get("us-gaap", {})
    best = None
    for t in tags:
        for x in ug.get(t, {}).get("units", {}).get(unit, []):
            if x.get("form") not in ("10-K", "10-K/A", "20-F", "40-F"): continue
            e = x["end"]
            if not e.startswith(str(fy_end_year)) and not (e.startswith(str(fy_end_year+1)) and e[5:7] in ("01","02","03")): continue
            if dur:
                s = x.get("start")
                if not s: continue
                dd = (date.fromisoformat(e) - date.fromisoformat(s)).days
                if not (340 <= dd <= 380): continue
            if best is None or x["filed"] > best[1]:
                best = (x["val"], x["filed"], x["accn"], e, t)
        if best: return best
    return None

REV = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax"]
COR = ["CostOfRevenue", "CostOfGoodsAndServicesSold"]
GP = ["GrossProfit"]
OI = ["OperatingIncomeLoss"]
OCF = ["NetCashProvidedByUsedInOperatingActivities"]
SBC = ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"]
CAPEX = ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"]
SW = ["PaymentsToDevelopSoftware", "PaymentsForSoftware", "PaymentsToAcquireIntangibleAssets"]
NI = ["NetIncomeLoss", "ProfitLoss"]
CASH = ["CashAndCashEquivalentsAtCarryingValue"]
DEBT = ["LongTermDebt", "LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities", "DebtLongtermAndShorttermCombinedAmount", "LongTermDebtNoncurrent"]
GW = ["Goodwill"]
ASSETS = ["Assets"]

peers = [("PAY",2025), ("FISV",2025), ("FIS",2025), ("JKHY",2025), ("ACIW",2025), ("FLYW",2025), ("BILL",2025), ("ESMT",2022)]
out = []
for tk, yr in peers:
    f = facts_for(tk)
    r = {"tk": tk, "name": f.get("entityName")}
    for k, tags, dur in [("rev", REV, True), ("cor", COR, True), ("gp", GP, True), ("oi", OI, True), ("ocf", OCF, True),
                         ("sbc", SBC, True), ("capex", CAPEX, True), ("sw", SW, True), ("ni", NI, True),
                         ("cash", CASH, False), ("debt", DEBT, False), ("gw", GW, False), ("assets", ASSETS, False)]:
        v = val(f, tags, yr, dur=dur)
        r[k] = v
    # prior year revenue for growth
    r["rev_prev"] = val(f, REV, yr-1)
    out.append(r)

def m(v): return f"{v[0]/1e6:,.1f}" if v else "n/a"
print("| ticker | FY end | revenue $M | growth | gross margin | op margin | OCF $M | SBC $M | SBC/OCF | capex+sw $M | OE (OCF-SBC-capex-sw) $M | cash $M | debt $M | goodwill $M | accession |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for r in out:
    rev = r["rev"][0] if r["rev"] else None
    gp = r["gp"][0] if r["gp"] else (rev - r["cor"][0] if (rev and r["cor"]) else None)
    oi = r["oi"][0] if r["oi"] else None
    ocf = r["ocf"][0] if r["ocf"] else None
    sbc = r["sbc"][0] if r["sbc"] else 0
    capex = (r["capex"][0] if r["capex"] else 0) + (r["sw"][0] if r["sw"] else 0)
    oe = ocf - sbc - capex if ocf is not None else None
    g = (rev / r["rev_prev"][0] - 1) if (rev and r["rev_prev"]) else None
    pct = lambda x: f"{x*100:.1f}%" if x is not None else "n/a"
    print(f"| {r['tk']} | {r['rev'][3] if r['rev'] else ''} | {m(r['rev'])} | {pct(g)} | {pct(gp/rev if (gp is not None and rev) else None)} | {pct(oi/rev if (oi is not None and rev) else None)} | {m(r['ocf'])} | {m(r['sbc'])} | {pct(sbc/ocf if ocf else None)} | {capex/1e6:,.1f} | {oe/1e6 if oe is not None else float('nan'):,.1f} | {m(r['cash'])} | {m(r['debt'])} | {m(r['gw'])} | {r['rev'][2] if r['rev'] else ''} |")
print()
for r in out:
    print(r["tk"], {k: (v[4], v[3], v[2]) for k, v in r.items() if isinstance(v, tuple)})
