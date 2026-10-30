"""Check script for the NWE run file (2026-10-25): no E-ids; every M/L/R id cited exists in
principle_ledger_v5.csv; every quoted fragment written directly beside an id is a substring of that row.
Run from the repository root:  python "Test Runs/_research 2026-10-25 NWE/check_ids.py"
"""
import csv, re, sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RUN = "Test Runs/2026-10-25 Run - NWE NorthWestern Energy.md"
LEDGER = "principle_ledger_v5.csv"
rows = {}
with open(LEDGER, encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        rows[r["id"]] = r["quote_verbatim"]
text = open(RUN, encoding="utf-8").read()

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("�", "'"), ("—", "-"), ("–", "-"), (" ", " ")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()

ids = re.findall(r"\*\*\[([A-Z]\d{4}-\d{3})\]\*\*", text)
eids = re.findall(r"\[E\d+-\d+\]", text)
missing = sorted({i for i in ids if i not in rows})
print(f"ids cited: {len(ids)} ({len(set(ids))} distinct); E-ids: {len(eids)}; missing from ledger: {missing}")

# quoted fragment immediately before an id: "..." **[ID]**   (allow a comma/space between)
bad = []
for m in re.finditer(r"\"([^\"]{6,}?)\"[.,;:)\s]{0,4}\*\*\[([A-Z]\d{4}-\d{3})\]\*\*", text):
    frag, i = m.group(1), m.group(2)
    if i not in rows:
        continue
    pieces = [p.strip() for p in frag.split("[...]") if p.strip()]
    row = norm(rows[i])
    for p in pieces:
        if norm(p) not in row:
            bad.append((i, p[:90]))
# also the form **[ID]**: "..."  (id then colon then quote) within the same line
for m in re.finditer(r"\*\*\[([A-Z]\d{4}-\d{3})\]\*\*:\s*\"([^\"]{6,}?)\"", text):
    i, frag = m.group(1), m.group(2)
    if i not in rows:
        continue
    for p in [p.strip() for p in frag.split("[...]") if p.strip()]:
        if norm(p) not in norm(rows[i]):
            bad.append((i, p[:90]))
for b in bad:
    print("QUOTE NOT IN ROW:", b)
ok = not missing and not eids and not bad
print("CHECK", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
