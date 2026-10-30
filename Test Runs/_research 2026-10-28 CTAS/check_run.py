# Check the run file: no E-ids; every M/L/R id exists in the v5 ledger; every quoted fragment
# immediately before an id ("..." **[ID]**) appears in that row (curly quotes and dashes normalized; [...] splits).
import csv, re, sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:\Projects\BRK\Test Runs\2026-10-28 Run - CTAS Cintas.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(r"C:\Projects\BRK\principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u2014", "-"), ("\u2013", "-"), ("\ufffd", "")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
missing = sorted({i for i in ids if i not in rows})
if missing: print("missing ids:", missing); bad += 1
pairs = re.findall(r'"([^"\n]{3,400})"\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
for q, i in pairs:
    if i not in rows: continue
    row = norm(rows[i])
    for frag in q.split("[...]"):
        f = norm(frag).strip(" .,;:")
        if f and f not in row:
            print(f"NOT IN ROW {i}: {frag!r}"); bad += 1
# em dashes in own prose
if "\u2014" in text: print("em dash present:", text.count("\u2014")); bad += 1
print(f"ids cited: {len(ids)} ({len(set(ids))} distinct); quote-id pairs checked: {len(pairs)}; problems: {bad}")
print("PASS" if bad == 0 else "FAIL")
