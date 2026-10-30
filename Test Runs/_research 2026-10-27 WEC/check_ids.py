import csv, re, sys
run = open("Test Runs/2026-10-27 Run - WEC WEC Energy Group.md", encoding="utf-8").read()
rows = {r[0]: r[2] for r in csv.reader(open("principle_ledger_v5.csv", encoding="utf-8"))}
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("�", "")
    s = s.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip().lower()
ok = True
eids = re.findall(r"\[E\d+-\d+\]", run)
if eids: print("E-ids found:", eids); ok = False
ids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", run))
for i in sorted(ids):
    if i not in rows: print("MISSING id", i); ok = False
flat = re.sub(r"\s+", " ", run)
pat = re.compile(r'"([^"]{6,400})"[^"\[]{0,60}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
n = 0
for m in pat.finditer(flat):
    frag, i = m.group(1), m.group(2)
    n += 1
    parts = [p for p in re.split(r"\[\.\.\.\]", frag)]
    for p in parts:
        p = norm(p).strip(" .,")
        if p and i in rows and p not in norm(rows[i]):
            print("NOT IN ROW", i, "::", p[:120]); ok = False
print("ids:", len(ids), "quoted fragments checked:", n, "PASS" if ok else "FAIL")
