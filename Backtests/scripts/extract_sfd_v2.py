import json, os, re, csv

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
DOCS = os.path.join(SCRATCH, "bt_cache", "old_10k_docs")

# tickers with zero usable years from the first pass
FIELDS = ['ticker','fiscal_year','net_sales_or_revenue','unit','net_income','eps','total_assets','long_term_debt','shares_outstanding','notes']
rows = list(csv.DictReader(open(os.path.join(SCRATCH, "sfd_all_extracted.csv"))))
usable_tickers = set(r['ticker'] for r in rows if r['fiscal_year'] and r['fiscal_year'] != 'UNKNOWN')
all_tickers = set(r['ticker'] for r in rows)
retry_tickers = sorted(all_tickers - usable_tickers)
print(f"{len(retry_tickers)} tickers to retry")

def find_best_snippet(text):
    """Find every 'selected financial data' occurrence; score each by whether
    it's followed (within 300 chars) by a <TABLE> tag AND has a run of digits
    nearby (i.e. an actual table, not just a referencing sentence)."""
    low = text.lower()
    candidates = []
    idx = 0
    while True:
        idx = low.find("selected financial data", idx)
        if idx < 0:
            break
        window = text[idx:idx+400]
        has_table_tag = "<TABLE>" in window.upper()
        digit_count = sum(1 for c in window if c.isdigit())
        candidates.append((idx, has_table_tag, digit_count))
        idx += 1
    if not candidates:
        return None
    # prefer: has table tag, then most digits nearby, then LAST occurrence (exhibits come after main doc)
    candidates.sort(key=lambda c: (c[1], c[2], c[0]), reverse=True)
    best_idx = candidates[0][0]
    return text[best_idx:best_idx+4500]

snippets = {}
none_found = []
for t in retry_tickers:
    fn = os.path.join(DOCS, f"{t}.txt")
    if not os.path.exists(fn):
        none_found.append(t)
        continue
    text = open(fn, encoding="utf-8", errors="ignore").read()
    snippet = find_best_snippet(text)
    if snippet is None:
        none_found.append(t)
        continue
    snippets[t] = snippet

print(f"Found improved snippets for {len(snippets)} / {len(retry_tickers)}")
print(f"Still nothing: {len(none_found)}")

json.dump(snippets, open(os.path.join(SCRATCH, "sfd_retry_snippets.json"), "w"), indent=1)
json.dump(none_found, open(os.path.join(SCRATCH, "sfd_retry_none.json"), "w"), indent=1)
