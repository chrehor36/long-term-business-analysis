import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
t = open("Test Runs/2026-10-18 Run - DTE DTE Energy.md", encoding="utf-8").read()
def norm(s): return re.sub(r'\s+', ' ', s).strip()
problems = 0
eids = re.findall(r'\[E\d-\d+\]', t)
if eids: print("E-ids found:", eids); problems += len(eids)
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); problems += 1
# quoted fragment immediately before an id: "....." **[ID]**  (allow ", " or ";" chains of ids after)
for m in re.finditer(r'"([^"]{3,900})"\s*(?:\)|,)?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t):
    frag, i = norm(m.group(1)), m.group(2)
    if i not in rows: continue
    row = norm(rows[i])
    parts = [norm(p) for p in frag.split('[...]') if norm(p)]
    for p in parts:
        if p not in row:
            print(f"FRAGMENT NOT IN {i}: {p[:120]}"); problems += 1
print(f"{len(set(ids))} distinct ids, {len(ids)} citations; problems: {problems}")
