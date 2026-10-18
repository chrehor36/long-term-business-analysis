# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately before an id (or a run of ids) is in that row's quote.
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = "Test Runs/2026-10-13 Run - STLD Steel Dynamics.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
flat = re.sub(r"\s*\n\s*", " ", text)
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
print("E-ids:", eids or "none"); bad += len(eids)
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
missing = sorted({i for i in ids if i not in rows})
print("ids cited:", len(ids), "distinct:", len(set(ids)), "missing:", missing or "none"); bad += len(missing)
# fragment check: "...." followed by optional punctuation then one or more **[id]**
pat = re.compile(r'"([^"]{6,}?)"[\s.,;:)]*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[\s,]*)+)')
n = 0
for m in pat.finditer(flat):
    frag = m.group(1)
    fid = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))
    parts = [p.strip(" .,;:") for p in frag.split("[...]") if p.strip(" .,;:")]
    ok = any(all(p in rows.get(i, "") for p in parts) for i in fid)
    n += 1
    if not ok:
        bad += 1
        print("FRAGMENT NOT IN ROW:", fid, "|", frag[:160])
print("fragments checked:", n)
print("RESULT:", "PASS" if bad == 0 else "FAIL (%d)" % bad)
