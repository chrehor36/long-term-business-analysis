"""Competitor row from the competitors' own filings (XBRL company facts; transcription, the filed statements govern).
Fetches companyfacts into cache/peers/, prints per fiscal year: revenue, operating income, OCF, SBC, capex,
operating margin and owner cash (OCF - SBC - capex) as a share of revenue, with the accession of the 10-K/20-F used."""
import json, os, sys, time, urllib.request
from datetime import date

UA = "LongTermBusinessAnalysis research chrehor36@gmail.com"
HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, "cache", "peers")
os.makedirs(C, exist_ok=True)

PEERS = {"PG": 80424, "CL": 21665, "KMB": 55785, "CLX": 21076, "CHD": 313927, "UL": 217410}
TAGS = {
    "rev": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet", "Revenue"],
    "opi": ["OperatingIncomeLoss", "ProfitLossFromOperatingActivities"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations", "CashFlowsFromUsedInOperatingActivities"],
    "pti": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments", "ProfitLossBeforeTax"],
    "sbc": ["ShareBasedCompensation", "AdjustmentsForSharebasedPayments"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets", "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"],
}

def load(tk, cik):
    p = os.path.join(C, f"{tk}.json")
    if not os.path.exists(p):
        url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
        for attempt in range(4):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
                with urllib.request.urlopen(req, timeout=120) as r:
                    data = r.read()
                open(p, "wb").write(data)
                break
            except Exception as e:
                print("retry", tk, e, file=sys.stderr)
                time.sleep(2)
        time.sleep(0.4)
    return json.load(open(p))

def annual(facts, names):
    out = {}
    for ns in ("us-gaap", "ifrs-full"):
        g = facts["facts"].get(ns, {})
        for n in names:
            if n not in g:
                continue
            for u, arr in g[n]["units"].items():
                for f in arr:
                    if f.get("form") not in ("10-K", "20-F", "10-K/A", "20-F/A") or "start" not in f:
                        continue
                    days = (date.fromisoformat(f["end"]) - date.fromisoformat(f["start"])).days
                    if not 350 <= days <= 380:
                        continue
                    k = f["end"][:4] if f["end"][5:7] != "06" else f["end"][:4]
                    prev = out.get(k)
                    if prev is None or f["filed"] > prev[2]:
                        out[k] = (f["val"], u, f["filed"], f["accn"], n)
    return out

for tk, cik in PEERS.items():
    facts = load(tk, cik)
    s = {k: annual(facts, v) for k, v in TAGS.items()}
    print("==", tk, facts.get("entityName"))
    yrs = sorted(set(s["rev"]) & set(s["ocf"]))[-6:]
    for y in yrs:
        def g(k):
            return s[k].get(y, (None,))[0]
        rev, opi, ocf, sbc, cx, pti = g("rev"), g("opi"), g("ocf"), g("sbc") or 0, g("capex"), g("pti")
        om = f"{opi / rev:.1%}" if opi and rev else "n/a"
        pm = f"{pti / rev:.1%}" if pti and rev else "n/a"
        oc = f"{(ocf - sbc - cx) / rev:.1%}" if None not in (ocf, cx, rev) else "n/a"
        unit = s["rev"][y][1]
        print(f"  FY{y} rev {rev/1e6:>9,.0f} {unit} op.margin {om:>6} pretax {pm:>6} ownercash/rev {oc:>6}  "
              f"[{s['rev'][y][3]}; rev tag {s['rev'][y][4]}]")
