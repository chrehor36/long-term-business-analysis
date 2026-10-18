# OGS run check: (1) no E-ids; (2) every M/L/R id exists in principle_ledger_v5.csv; (3) every quoted fragment that
# stands immediately before an id is in that row (elisions [...] split; straight and curly quotes and dashes normalised).
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = sys.argv[1]
LEDGER = sys.argv[2]
text = open(RUN, encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(LEDGER, encoding="utf-8-sig"))}

def norm(s):
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("—", "-"), ("–", "-"),
                 ("�", "?")):
        s = s.replace(a, b)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

problems = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids:
    print("E-ids found:", sorted(set(eids))); problems += len(eids)
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
missing = sorted({i for i in ids if i not in rows})
for i in missing:
    print("MISSING id:", i); problems += 1
# fragment immediately before an id: "...." then optional punctuation/space then **[ID]**
pat = re.compile(r'"((?:[^"]|""[^"]*"")+?)"[,.;:)]?\s*\(?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', re.S)
checked = 0
for m in pat.finditer(text):
    frag, rid = m.group(1), m.group(2)
    if rid not in rows: continue
    row = norm(rows[rid])
    parts = [p for p in re.split(r"\[\.\.\.\]", frag)]
    for p in parts:
        p2 = norm(p.replace('""', '"'))
        p2 = p2.strip(" .,;:")
        if not p2: continue
        checked += 1
        if p2 not in row:
            print(f"FRAGMENT NOT IN {rid}: {p.strip()[:120]!r}"); problems += 1
print(f"ids cited: {len(ids)} ({len(set(ids))} distinct); fragments checked: {checked}; problems: {problems}")
