import sys, json
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources

cik = "0000093556"
txt = sources._get(f"https://data.sec.gov/submissions/CIK{cik}.json", sources.SEC_UA,
                   f"sub_{cik}.json", max_age_h=24)
r = json.loads(txt).get("filings", {}).get("recent", {})
forms, dates = r.get("form", []), r.get("filingDate", [])
items, accs = r.get("items", []), r.get("accessionNumber", [])
prim = r.get("primaryDocDescription", [])
since = max([d for f, d in zip(forms, dates) if f in ("10-K", "20-F", "40-F")], default="")
print("newest annual filing date:", since)
nNone = sum(1 for x in items if x is None)
print("items entries that are None:", nNone, "of", len(items))
print()
for i, f in enumerate(forms):
    d = dates[i]
    if since and d <= since:
        continue
    it = items[i] if i < len(items) else ""
    it = it or ""
    if f in sources.DEAL_FORMS:
        print("HARD", f, d, accs[i], it)
    elif f.startswith("8-K"):
        print("8-K ", d, accs[i], "|", it)
print()
print("--- all 10-K / 10-Q filings, newest 25 ---")
n = 0
for i, f in enumerate(forms):
    if f in ("10-K", "10-Q"):
        print(f, dates[i], accs[i], r.get("reportDate", [])[i] if r.get("reportDate") else "")
        n += 1
        if n >= 25:
            break
