import json, os

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")

resolved = json.load(open(os.path.join(SCRATCH, "sp500_2013_resolved_ciks.json")))
earliest = json.load(open(os.path.join(SCRATCH, "earliest_10k_by_ticker.json")))

pre1996 = [(t, r) for t, r in earliest.items() if r["earliest_10k"] and r["earliest_10k"] < "1996-01-01"]
print(f"{len(pre1996)} tickers with pre-1996 10-Ks")

results = {}
for t, r in pre1996:
    cik = r["cik"]
    fn = os.path.join(CACHE, f"subs_{cik}.json")
    if not os.path.exists(fn):
        continue
    subs = json.load(open(fn))
    recent = subs["filings"]["recent"]
    forms = recent["form"]
    all_entries = list(zip(forms, recent["filingDate"], recent["accessionNumber"], recent["primaryDocument"]))
    for extra in subs["filings"].get("files", []):
        efn = os.path.join(CACHE, f"subs_{cik}_{extra['name']}")
        if os.path.exists(efn):
            edata = json.load(open(efn))
            if "form" in edata:
                all_entries += list(zip(edata["form"], edata["filingDate"], edata["accessionNumber"], edata["primaryDocument"]))
    tenks = [(f, d, a, p) for f, d, a, p in all_entries if f in ("10-K", "10-K405", "10-KSB")]
    if not tenks:
        continue
    tenks.sort(key=lambda x: x[1])
    form, date, accn, primdoc = tenks[0]
    results[t] = {"cik": cik, "form": form, "filing_date": date, "accession": accn, "primary_doc": primdoc}

json.dump(results, open(os.path.join(SCRATCH, "earliest_10k_docs.json"), "w"), indent=1)
print(f"Resolved doc locations for {len(results)} / {len(pre1996)}")
# show distribution by year
from collections import Counter
years = Counter(r["filing_date"][:4] for r in results.values())
for y in sorted(years):
    print(y, years[y])
