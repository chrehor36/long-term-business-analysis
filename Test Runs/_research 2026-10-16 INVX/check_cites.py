# Check: no E-ids; every M/L/R id in the ledger; every quoted fragment beside an id is in that row.
import csv, re, sys
run = sys.argv[1]
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
t = open(run, encoding="utf-8").read()
def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2014", "-").replace("\u2013", "-")
    return re.sub(r"\s+", " ", s).strip()
bad = 0
checked = []
eids = re.findall(r"\[E\d+-\d+\]", t)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", t)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); bad += 1
# quoted fragments: for each paragraph/bullet, quotes that end right before an id (within the same sentence span)
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", t):
    i = m.group(1)
    j = m.start()
    pre = t[max(0, j - 6):j]
    # the quote must close immediately before the id: '" **[' or '." **[' or '" — **['
    k = t.rfind('"', 0, j)
    if k < 0 or len(t[k + 1:j].strip(" .,;:—-")) > 0:
        continue
    o = t.rfind('"', 0, k)
    q = t[o + 1:k]
    row = norm(rows.get(i, ""))
    for frag in re.split(r"\s*\[\.\.\.\]\s*", norm(q)):
        frag = frag.strip(" .,;:")
        if frag and frag not in row:
            print("NOT IN ROW", i, "|", frag[:140]); bad += 1
    checked.append(i)
print("ids", len(set(ids)), "quotes checked", len(checked), "problems", bad)
