# citation check for the CDNL run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately followed by an id is in that row (elisions [...] split the fragment)
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
run, ledger = sys.argv[1], sys.argv[2]
text = open(run, encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(ledger, encoding="utf-8-sig"))}
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().lower()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids: print("E-ids found:", eids); bad += 1
ids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", text))
for i in sorted(ids):
    if i not in rows: print("MISSING id", i); bad += 1
# quote then id: "....." **[ID]**  (allow up to 3 chars between)
for m in re.finditer(r'"([^"]{8,}?)"\s{0,3}\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text):
    frag, i = m.group(1), m.group(2)
    row = norm(rows.get(i, ""))
    for piece in frag.split("[...]"):
        p = norm(piece).strip(" .,")
        if p and p not in row:
            print(f"NOT IN ROW {i}: {piece[:90]}"); bad += 1
print("ids checked:", len(ids), "| result:", "PASS" if not bad else f"FAIL ({bad})")
