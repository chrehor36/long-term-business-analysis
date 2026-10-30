# Dispatcher check (fold step 4.3): every quoted fragment immediately beside a ledger id is in that id's row.
import csv, re, sys
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r["﻿id"] if "﻿id" in r else r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
n = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().lower()
pairs = 0; slips = 0
for m in re.finditer(r'(?:"([^"]{4,400})"|“([^”]{4,400})”)\*?\*?\s*\**\s*\*\*\[([MLR]\d{4}-\d{3})\]', run):
    q = m.group(1) or m.group(2); i = m.group(3); pairs += 1
    parts = [p.strip(" ,.;:") for p in n(q).split("[...]")]
    t = n(rows.get(i, ""))
    if not all(p == "" or p in t for p in parts):
        slips += 1; print("SLIP?", i, "|", q[:150])
print("adjacent pairs:", pairs, "flagged:", slips)
