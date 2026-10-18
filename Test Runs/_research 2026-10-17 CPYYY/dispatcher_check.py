# Dispatcher's citation check (overnight 2026-10-17): every quoted fragment within 40 characters before a v5 id is in that row.
import csv, re
RUN = "Test Runs/2026-10-17 Run - CPYYY Centrica.md"
rows = {}
for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig")):
    rows[r["id"]] = r["quote_verbatim"]
def norm(t):
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u2014", "-"), ("\u2013", "-")):
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9' ]", "", re.sub(r"\s+", " ", t).lower()).strip()
text = open(RUN, encoding="utf-8").read()
n = bad = 0
for m in re.finditer(r"[\"\u201c]([^\"\u201c\u201d]{3,600})[\"\u201d][^\"\u201c\[\n]{0,40}\[([MLR]\d{4}-\d{3})\]", text):
    frag, i = m.groups()
    if i not in rows:
        print("MISSING", i); bad += 1; continue
    for p in [x for x in re.split(r"\[\.\.\.\]|\.\.\.|\u2026", frag) if norm(x)]:
        n += 1
        if norm(p) not in norm(rows[i]):
            bad += 1; print("SLIP", i, "::", p[:150])
ids = set(re.findall(r"\b([MLR]\d{4}-\d{3})\b", text))
print("ids", len(ids), "missing", [i for i in ids if i not in rows], "| fragments", n, "| slips", bad, "| E-ids", len(re.findall(r"\[E\d+-\d+\]", text)))
