import json, os, time, urllib.request, re

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
DOCS = os.path.join(CACHE, "old_10k_docs")
os.makedirs(DOCS, exist_ok=True)
UA = "BRK-Framework research chrehor36@gmail.com"

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

docs = json.load(open(os.path.join(SCRATCH, "earliest_10k_docs.json")))

snippets = {}
fails = []
for i, (t, r) in enumerate(sorted(docs.items())):
    cik = r["cik"]
    accn = r["accession"]
    fn = os.path.join(DOCS, f"{t}.txt")
    if not os.path.exists(fn):
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accn}.txt"
        try:
            data = fetch(url)
            open(fn, "wb").write(data)
            time.sleep(0.12)
        except Exception as e:
            fails.append((t, f"FETCH_FAIL {e}"))
            continue
    text = open(fn, encoding="utf-8", errors="ignore").read()
    idx = text.lower().find("selected financial data")
    if idx < 0:
        # some filers title it slightly differently
        for alt in ["selected consolidated financial data", "five-year selected financial",
                    "five year financial summary", "selected financial highlights"]:
            idx = text.lower().find(alt)
            if idx >= 0:
                break
    if idx < 0:
        fails.append((t, "NO_SECTION_FOUND"))
        continue
    snippet = text[idx:idx+4000]
    snippets[t] = {"cik": cik, "accession": accn, "filing_date": r["filing_date"], "snippet": snippet}
    if i % 30 == 0:
        print(f"[{i}/{len(docs)}] {t}: found at offset {idx}")

json.dump(snippets, open(os.path.join(SCRATCH, "selected_financial_data_snippets.json"), "w"), indent=1)
json.dump(fails, open(os.path.join(SCRATCH, "selected_financial_data_fails.json"), "w"), indent=1)
print(f"\nExtracted: {len(snippets)} / {len(docs)}")
print(f"Failed: {len(fails)}")
