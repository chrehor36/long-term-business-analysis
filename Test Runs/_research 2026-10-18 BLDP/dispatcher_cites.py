# Dispatcher check: every quoted fragment adjacent to a v5 ledger id appears in that row's quote.
import csv, re, sys, unicodedata
RUN = "Test Runs/2026-10-18 Run - BLDP Ballard Power Systems.md"
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s).strip().lower()
rows = {}
with open("principle_ledger_v5.csv", encoding="utf-8") as f:
    r = csv.reader(f); hdr = next(r)
    for row in r: rows[row[0]] = row
qcol = [i for i, h in enumerate(hdr) if "quote" in h.lower()][0]
text = open(RUN, encoding="utf-8").read()
ID = r"\*\*\[([MLR]\d{4}-\d{3}[a-z]?)\]\*\*"
n = bad = 0
for m in re.finditer(ID, text):
    i = m.group(1)
    if i not in rows: print("MISSING", i); bad += 1; continue
    before = text[max(0, m.start() - 400):m.start()]
    q = re.findall(r'["\u201c]([^"\u201d]{6,})["\u201d]\s*[,.;:)]?\s*$', before)
    if not q: continue
    n += 1
    src = norm(rows[i][qcol])
    for part in re.split(r"\s*\[\.\.\.\]\s*|\s*\.\.\.\s*", q[-1]):
        p = norm(part).strip(" .,;:")
        if p and p not in src:
            print("SLIP", i, repr(part[:90])); bad += 1
print("adjacent fragments checked", n, "problems", bad)
