# Dispatcher's fold check: every quoted fragment immediately followed by a v5 id is inside that row's quote.
import csv, re, sys
csv.field_size_limit(10**9)
rows = {}
with open("principle_ledger_v5.csv", encoding="utf-8") as f:
    r = csv.reader(f); hdr = next(r)
    qi = [i for i, h in enumerate(hdr) if "quote" in h.lower()][0]
    for row in r: rows[row[0]] = row[qi]
def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s).strip().lower()
text = open(sys.argv[1], encoding="utf-8").read()
ids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", text))
print("ids", len(ids), "missing", sorted(i for i in ids if i not in rows))
print("E-ids", re.findall(r"\[E\d+-\d+\]", text))
pat = re.compile(r'[“"]([^"“”]{8,}?)[”"][^"“”\[]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]')
n = bad = 0
for m in pat.finditer(text):
    frag, rid = m.group(1), m.group(2); n += 1
    q = norm(rows.get(rid, ""))
    for piece in re.split(r"\[\.\.\.\]|\.\.\.|…", frag):
        p = norm(piece).strip(" .,;:")
        if p and p not in q:
            bad += 1; print("SLIP", rid, "|", piece[:120])
print("checked", n, "slips", bad)
