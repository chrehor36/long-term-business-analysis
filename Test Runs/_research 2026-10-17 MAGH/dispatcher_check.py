# Dispatcher's check (overnight 2026-10-17): every quoted fragment that closes just before a run of v5 ids (quotes may span
# lines) must be in one of those rows; also any quote that opens just after an id with a colon. No E-ids; no missing ids.
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = "Test Runs/2026-10-17 Run - MAGH Magnitude International.md"
rows = {r[0]: r[2] for r in csv.reader(open('principle_ledger_v5.csv', encoding='utf-8'))}
def norm(s):
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('—', '-'), ('–', '-')): s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()
t = re.sub(r'\s*\n\s*', ' ', open(RUN, encoding='utf-8').read())
n = flags = 0
for m in re.finditer(r'"([^"]{4,800}?)"[\s.,;:)]*((?:\**\[?[MLR]\d{4}-\d{3}\]?\**[\s,;and]*)+)', t):
    frag, ids = m.group(1), re.findall(r'[MLR]\d{4}-\d{3}', m.group(2)); n += 1
    parts = [p for p in re.split(r'\[\.\.\.\]|\.\.\.', frag) if p.strip()]
    if not any(all(norm(p) in norm(rows.get(c, '')) for p in parts) for c in ids):
        flags += 1; print(ids, '|', frag[:160])
print("E-ids:", re.findall(r'\[E\d-\d+\]', t), "| missing:", sorted({x for x in re.findall(r'[MLR]\d{4}-\d{3}', t) if x not in rows}))
print(f"fragments checked: {n}, not in a cited row: {flags}")
