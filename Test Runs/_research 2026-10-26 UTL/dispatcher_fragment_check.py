# Dispatcher's check (work-hours cycle 2026-10-26): every quoted fragment adjacent to a v5 id is in that id's row.
import csv, re
RUN = "Test Runs/2026-10-26 Run - UTL Unitil.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
def norm(s):
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"')):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()
text = open(RUN, encoding="utf-8").read()
ids = re.findall(r"\b([MLR]\d{4}-\d{3})\b", text)
missing = sorted(set(i for i in ids if i not in rows))
eids = re.findall(r"\bE\d-\d{2}\b", text)
pairs = bad = 0
for para in re.split(r"\n\s*\n", text):
    para = re.sub(r"\s+", " ", para)
    for m in re.finditer(r'"([^"]{12,}?)"[^"]{0,40}?\*{0,2}\[?\*{0,2}([MLR]\d{4}-\d{3})', para):
        q, i = m.group(1), m.group(2)
        if i not in rows:
            continue
        pairs += 1
        frags = [f.strip(" .,;:") for f in re.split(r"\[\.\.\.\]|\.\.\.|…", q) if len(f.strip(" .,;:")) > 3]
        if not all(norm(f) in norm(rows[i]) for f in frags):
            bad += 1
            print("NOT IN ROW", i, "|", q[:140])
print(f"ids {len(ids)} distinct {len(set(ids))} missing {missing} E-ids {eids} adjacent pairs {pairs} not-in-row {bad}")
