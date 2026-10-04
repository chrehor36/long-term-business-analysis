import json, re

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"

recon = json.load(open(f"{SCRATCH}\\sp500_2008_reconstruction.json"))
left = recon["left_index_since"]

# find the removal reason for each ticker (the reversed_changes list has
# [date, added_ticker, added_name, removed_ticker, removed_name, reason])
reasons = {}
for d, added, added_name, removed, removed_name, reason in recon["reversed_changes"]:
    if removed and removed not in reasons:
        reasons[removed] = {"name": removed_name, "reason": reason, "date": d}

FAILED_KW = ["bankrupt", "chapter 11", "delisted", "ceased operations", "liquidat",
             "receivership", "conservatorship", "insolven", "went private due to financial",
             "delisting"]
ACQUIRED_KW = ["acquired", "purchased", "merger", "merged", "acquisition", "bought",
               "combined with", "to be acquired", "completion of its acquisition",
               "buyout", "take-private", "went private"]
SPINOFF_KW = ["spun off", "spin-off", "spinoff", "separation of"]

def classify(reason):
    r = reason.lower()
    if any(k in r for k in FAILED_KW):
        return "FAILED"
    if any(k in r for k in SPINOFF_KW):
        return "SPINOFF"
    if any(k in r for k in ACQUIRED_KW):
        return "ACQUIRED"
    if "market capitalization" in r or "market cap" in r:
        return "MARKET_CAP_DECLINE_UNCLASSIFIED"
    return "OTHER_UNCLASSIFIED"

results = {}
for t in left:
    info = reasons.get(t)
    if info is None:
        results[t] = {"name": "?", "reason": "NO REASON CAPTURED", "class": "NO_DATA"}
        continue
    cls = classify(info["reason"])
    results[t] = {"name": info["name"], "reason": info["reason"], "class": cls, "date": info["date"]}

from collections import Counter
c = Counter(v["class"] for v in results.values())
print("Auto-classification of 218 tickers that left the reconstructed 2008 index:")
for k, v in c.most_common():
    print(f"  {k}: {v}")

print()
print("=== MARKET_CAP_DECLINE_UNCLASSIFIED (needs manual review -- ambiguous, could be decline-but-alive or a slow failure) ===")
for t, v in sorted(results.items()):
    if v["class"] == "MARKET_CAP_DECLINE_UNCLASSIFIED":
        print(f"  {t:8} {v['name']:35} ({v['date']})")

print()
print("=== NO_DATA (no removal reason captured -- likely removed before our reconstruction reversed enough changes, or a parsing gap) ===")
for t, v in sorted(results.items()):
    if v["class"] == "NO_DATA":
        print(f"  {t}")

json.dump(results, open(f"{SCRATCH}\\sp500_2008_fates_auto.json", "w"), indent=1)
