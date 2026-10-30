# Check the MAGH run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately followed by one or more ids appears in at least one of those rows.
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = "Test Runs/2026-10-17 Run - MAGH Magnitude International.md"
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8') as f:
    r = csv.reader(f); next(r)
    for row in r: rows[row[0]] = row[2]
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('�', '-').replace('—', '-').replace('–', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()
text = open(RUN, encoding='utf-8').read()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', text)
if eids: print("E-ids found:", eids); bad += 1
ids = set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', text))
for i in sorted(ids):
    if i not in rows: print("MISSING id", i); bad += 1
# quoted fragment followed by ids: "..." then optional punctuation/space then **[ID]** (, **[ID]**)*
pat = re.compile(r'["“]([^"“”]{6,}?)["”][\s.,;:)]*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[\s,]*)+)')
n = 0
for m in pat.finditer(text):
    frag = m.group(1); cited = re.findall(r'[MLR]\d{4}-\d{3}', m.group(2)); n += 1
    parts = [p for p in re.split(r'\[\.\.\.\]', frag) if p.strip()]
    ok = any(all(norm(p) in norm(rows.get(c, '')) for p in parts) for c in cited)
    if not ok: print("NOT IN ROW:", cited, "|", frag[:120]); bad += 1
print(f"ids: {len(ids)}, quoted fragments checked: {n}, problems: {bad}")
