# Dispatcher's check: every quoted fragment beside a v5 id is in that row's quote.
import csv, re, sys, unicodedata
RUN = "Test Runs/2026-10-13 Run - CYH Community Health Systems.md"
def norm(s):
    s = unicodedata.normalize("NFKC", s).replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s).strip().lower()
rows = {}
with open("principle_ledger_v5.csv", encoding="utf-8") as f:
    r = csv.reader(f); hdr = next(r)
    qi = [i for i, h in enumerate(hdr) if "quote" in h.lower()][0]
    for row in r:
        rows[row[0]] = norm(row[qi])
text = open(RUN, encoding="utf-8").read()
bad = 0; n = 0
for para in re.split(r"\n\s*\n", text):
    ids = re.findall(r"\[((?:M|L|R)[0-9A-Za-z\-]+)\]", para)
    if not ids: continue
    for m in re.finditer(r"\"([^\"]{6,})\"((?:[^\"]{0,40}?)\[((?:M|L|R)[0-9A-Za-z\-]+)\])", para):
        frag, rid = m.group(1), m.group(3)
        n += 1
        if rid not in rows: print("MISSING ID", rid); bad += 1; continue
        parts = [p.strip(" .,;:") for p in re.split(r"\[\.\.\.\]|\.\.\.", norm(frag)) if p.strip(" .,;:")]
        if not all(p in rows[rid] for p in parts):
            print("SLIP", rid, "|", frag[:120]); bad += 1
for rid in set(re.findall(r"\[((?:M|L|R)\d{4}-\d+)\]", text)):
    if rid not in rows: print("MISSING", rid); bad += 1
print("E-ids:", re.findall(r"\[E\d-\d+\]", text))
print(f"fragments checked {n}, problems {bad}")
