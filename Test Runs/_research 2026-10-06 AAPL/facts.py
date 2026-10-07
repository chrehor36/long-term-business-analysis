"""Annual figures from SEC XBRL company facts (transcription only; the filed statements are read separately).
Usage: python facts.py CIK  -> prints FY values (first-filed 10-K vintage per fiscal year-end) for a list of tags.
The companyfacts JSON is cached under cache/ (gitignored)."""
import sys, os, json, time, urllib.request

UA = "LongTermBusinessAnalysis research chrehor36@gmail.com"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
cik = sys.argv[1].zfill(10)
path = os.path.join(CACHE, f"facts_{cik}.json")
if not os.path.exists(path):
    req = urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", headers={"User-Agent": UA})
    open(path, "wb").write(urllib.request.urlopen(req, timeout=60).read()); time.sleep(0.5)
d = json.load(open(path))
g = d["facts"].get("us-gaap", {})

TAGS = sys.argv[2].split(",") if len(sys.argv) > 2 else [
    "Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet", "OperatingIncomeLoss",
    "NetIncomeLoss", "NetCashProvidedByUsedInOperatingActivities", "ShareBasedCompensation",
    "PaymentsToAcquirePropertyPlantAndEquipment", "DepreciationDepletionAndAmortization",
    "DepreciationAmortizationAndAccretionNet", "PaymentsForRepurchaseOfCommonStock", "PaymentsOfDividends",
    "IncomeTaxesPaidNet", "StockholdersEquity", "Assets", "ResearchAndDevelopmentExpense",
    "WeightedAverageNumberOfDilutedSharesOutstanding", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
    "InterestExpense", "GrossProfit"]

def annual(tag):
    if tag not in g: return {}
    out = {}
    for unit, rows in g[tag]["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A", "20-F", "40-F"): continue
            fp = r.get("fp");
            if "start" in r:
                # duration: keep ~1-year spans
                from datetime import date
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if not (350 <= (e - s).days <= 380): continue
            key = r["end"]
            # first-filed vintage
            if key not in out or r["filed"] < out[key][1]:
                out[key] = (r["val"], r["filed"], r.get("accn"))
    return out

for t in TAGS:
    a = annual(t)
    if not a: continue
    print(f"== {t}")
    for k in sorted(a)[-15:]:
        v, f, acc = a[k]
        print(f"   {k}  {v/1e6 if abs(v) > 1e5 else v:>14,.1f}  filed {f}  {acc}")
