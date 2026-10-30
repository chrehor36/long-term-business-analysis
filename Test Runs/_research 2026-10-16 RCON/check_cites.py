"""Citation check for the RCON run file: (1) no E-ids; (2) every M/L/R id exists in principle_ledger_v5.csv;
(3) every double-quoted fragment that ends within 12 characters before a bold id is found in that id's row
(normalised for curly quotes, dashes and whitespace). Prints failures; exit 1 on any."""
import csv, re, sys, os
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(here, "..", "..")
run = os.path.join(root, "Test Runs", "2026-10-16 Run - RCON Recon Technology.md")
rows = {}
for r in csv.DictReader(open(os.path.join(root, "principle_ledger_v5.csv"), encoding="utf-8-sig")):
    rows[r["id"]] = r["quote_verbatim"]
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip().lower()
t = open(run, encoding="utf-8").read()
bad = 0
for m in re.finditer(r"\[(E\d?-?\d+[^\]]*)\]", t):
    if re.match(r"E\d", m.group(1)): print("E-id:", m.group(0)); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", t)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id:", i); bad += 1
checked = 0
for line in t.splitlines():
    for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", line):
        pre = line[:m.start()]
        q = re.search(r"[\"“]([^\"“”]{3,}?)[\"”][^\"“”]{0,12}$", pre)
        if not q: continue
        frag = q.group(1)
        parts = [p for p in re.split(r"\s*\[\.\.\.\]\s*", frag) if p.strip()]
        rid = m.group(1); row = norm(rows.get(rid, ""))
        checked += 1
        for p in parts:
            if norm(p) not in row:
                print(f"NOT IN ROW {rid}: {p!r}"); bad += 1
print(f"ids cited: {len(set(ids))}; quoted fragments checked: {checked}; failures: {bad}")
sys.exit(1 if bad else 0)
