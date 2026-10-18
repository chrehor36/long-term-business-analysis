# Citation check for the TKAMY run file.
# 1) no E-ids; 2) every M/L/R id exists in principle_ledger_v5.csv;
# 3) every quoted fragment immediately followed by an id (within the same sentence) is a substring of that row.
import csv, re, sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8")
run, ledger = sys.argv[1], sys.argv[2]
rows = {}
with open(ledger, encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        rows[r["id"]] = r["quote_verbatim"]
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("’","'"),("‘","'"),("“",'"'),("”",'"'),("—","-"),("–","-"),("�","")]:
        s = s.replace(a, b)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()
text = open(run, encoding="utf-8").read()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids:
    print("E-ids found:", set(eids)); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
missing = sorted({i for i in ids if i not in rows})
print(f"ids cited: {len(ids)} ({len(set(ids))} distinct); missing: {missing}")
bad += len(missing)
# fragment check: a quoted string followed (within 12 chars) by one or more bold ids
pat = re.compile(r'"([^"\n]{3,600})"[^"\n]{0,40}?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[ ,;and]*)+)')
n = 0
for m in pat.finditer(text):
    frag = m.group(1)
    cids = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))
    parts = [p for p in re.split(r"\[\.\.\.\]", frag) if p.strip()]
    ok = False
    for cid in cids:
        q = norm(rows.get(cid, ""))
        if all(norm(p).strip(" .,;:") in q for p in parts):
            ok = True; break
    n += 1
    if not ok:
        bad += 1
        print(f"FRAGMENT NOT IN ROW {cids}: \"{frag[:120]}\"")
print(f"fragments checked: {n}; failures counted: {bad}")
sys.exit(1 if bad else 0)
