"""Citation check for the UGI run file: no E-ids; every M/L/R id in the v5 ledger;
every quoted fragment directly before an id (or ids) is found in one of those rows. Usage: check_cites.py RUNFILE"""
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
LEDGER = r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv"
rows = {r["\ufeffid"] if "\ufeffid" in r else r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(LEDGER, encoding="utf-8"))}
def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2014", "-").replace("\u2013", "-")
    return re.sub(r"\s+", " ", s).strip().lower()
text = open(sys.argv[1], encoding="utf-8").read()
problems = 0
if re.search(r"\[E\d", text):
    print("E-id found"); problems += 1
ids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", text))
for i in sorted(ids):
    if i not in rows: print("MISSING id", i); problems += 1
# quoted fragment followed (within 6 chars) by one or more bold ids
for m in re.finditer(r'"([^"\n]{6,400}?)"[^"\n]{0,12}?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,; ]*)+)', text):
    frag = m.group(1)
    cids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", m.group(2))
    parts = [p.strip() for p in frag.split("[...]") if p.strip()]
    ok = any(all(norm(p) in norm(rows.get(c, "")) for p in parts) for c in cids)
    if not ok:
        print("FRAGMENT NOT IN ROW", cids, "::", frag[:120]); problems += 1
print(len(ids), "ids;", problems, "problems")
