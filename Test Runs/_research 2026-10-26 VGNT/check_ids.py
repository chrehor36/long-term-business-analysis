import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r[0]: r[2] for r in csv.reader(open(sys.argv[2], encoding="utf-8-sig"))}
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("�", "'").replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip().lower()
bad = 0
eids = re.findall(r"\[(E\d+-\d+)\]", run)
if eids: print("E-ids found:", eids); bad += 1
ids = set(re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run))
for i in sorted(ids):
    if i not in rows: print("MISSING", i); bad += 1
# quoted fragment immediately before an id: "...." **[ID]**  (allow trailing punctuation inside quotes)
n = 0
for m in re.finditer(r'"([^"\n]{6,}?)"[.,;]?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run.replace("\n", " ")):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    n += 1
    row = norm(rows[i])
    for part in frag.split("[...]"):
        p = norm(part).strip(" .,;:")
        if p and p not in row:
            print("NOT IN ROW", i, "::", part[:120]); bad += 1
print("ids:", len(ids), "quoted fragments checked:", n, "problems:", bad)
