"""Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment adjacent to an id
(the quote immediately before the id on the same paragraph) appears in that row's quote."""
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
norm = lambda t: re.sub(r"\s+", " ", t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()
bad = 0
eids = re.findall(r"\[E\d-\d+\]", run)
print("E-ids:", eids or "none"); bad += len(eids)
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", run)
missing = sorted({i for i in ids if i not in rows})
print("ids cited:", len(set(ids)), "missing:", missing or "none"); bad += len(missing)
# quoted fragment then ids: "...." **[ID]** (allow ", **[ID2]**" chains); check each fragment against each id in the chain
checked = 0
for m in re.finditer(r'"([^"]{6,}?)"\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)', run):
    frag = m.group(1); chain = re.findall(r"\[([MLR]\d{4}-\d{3})\]", m.group(2))
    parts = [p.strip() for p in frag.split("[...]") if p.strip()]
    ok = any(all(norm(p) in norm(rows.get(i, "")) for p in parts) for i in chain)
    checked += 1
    if not ok:
        bad += 1; print("NOT IN ROW:", chain, "|", frag[:120])
print("quoted fragments checked:", checked)
print("RESULT:", "PASS" if bad == 0 else f"FAIL ({bad})")
