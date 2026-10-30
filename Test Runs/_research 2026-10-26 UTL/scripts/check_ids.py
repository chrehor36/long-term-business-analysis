import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('C:/Projects/BRK/principle_ledger_v5.csv', encoding='utf-8-sig'))}
txt = open('C:/Projects/BRK/Test Runs/2026-10-26 Run - UTL Unitil.md', encoding='utf-8').read()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', txt)
print("E-ids:", eids or "none")
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', txt)
missing = sorted(set(i for i in ids if i not in rows))
print("ids:", len(set(ids)), "distinct;", "missing:", missing or "none")
bad += len(missing) + len(eids)
# quoted fragment immediately before an id: "..." optional words/punct then **[ID]**
flat = re.sub(r'\s*\n\s*', ' ', txt)
for m in re.finditer(r'"([^"]{6,}?)"[^"\[]{0,60}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    q = re.sub(r'\s+', ' ', rows[i])
    parts = [p.strip(' .,;:') for p in frag.split('[...]')]
    ok = all(p in q for p in parts if p)
    if not ok:
        bad += 1; print("MISMATCH", i, "::", frag[:120])
print("RESULT:", "PASS" if bad == 0 else f"FAIL ({bad})")
