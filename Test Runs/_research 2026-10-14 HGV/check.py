import csv, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
RUN = "../2026-10-14 Run - HGV Hilton Grand Vacations.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("../../principle_ledger_v5.csv", encoding="utf-8-sig"))}
raw = open(RUN, encoding="utf-8").read()
t = re.sub(r"\s*\n\s*", " ", raw)  # join wrapped lines


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip().lower()


bad = 0
eids = re.findall(r"\[E\d+-\d+\]", t)
if eids:
    print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", t)
missing = sorted(set(i for i in ids if i not in rows))
if missing:
    print("MISSING ids:", missing); bad += 1
# A quoted fragment followed (within 40 characters, no other quote between) by one or more bold ids.
# A fragment may itself contain inner quotes from the row; the matcher takes the shortest span.
pat = re.compile(r'"([^"]{3,900}?)"[^"*]{0,40}?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[ ,;]*)+)')
n = 0
for m in pat.finditer(t):
    frag = m.group(1)
    cited = re.findall(r"\[([MLR]\d{4}-\d{3})\]", m.group(2))
    parts = [p for p in re.split(r"\[\.\.\.\]", frag) if p.strip(" .,;:")]
    ok = any(all(norm(p.strip(" .,;:")) in norm(rows.get(c, "")) for p in parts) for c in cited)
    n += 1
    if not ok:
        bad += 1
        print("NOT IN ROW", cited, "::", frag[:140])
print(f"ids cited: {len(set(ids))} distinct; quoted fragments checked: {n}; problems: {bad}")
sys.exit(1 if bad else 0)
