# Citation check for the CNP run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# in the same sentence-chunk as an id (the text since the previous id or line break pair) is found in one of the ids that
# follow it before the next quote. Run from the repository root: python -I "Test Runs/_research 2026-10-18 CNP/check_cites.py"
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = "Test Runs/2026-10-18 Run - CNP CenterPoint Energy.md"
rows = {r[0]: r[2] for r in csv.reader(open("principle_ledger_v5.csv", encoding="utf-8"))}
text = open(RUN, encoding="utf-8").read()
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("�", "'")
    s = s.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip().lower()
problems = 0
eids = re.findall(r"\[E\d-\d+\]", text)
if eids: print("E-ids found:", eids); problems += len(eids)
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
missing = sorted(set(i for i in ids if i not in rows))
if missing: print("MISSING ids:", missing); problems += len(missing)
# fragment check: split the text at each bold id group; quotes in the chunk before an id group must be in one of its ids
flat = re.sub(r"\s+", " ", text)
pos = 0
for m in re.finditer(r"((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)", flat):
    chunk = flat[pos:m.start()]
    group = re.findall(r"[MLR]\d{4}-\d{3}", m.group(1))
    pos = m.end()
    # only the last sentence part before the ids: after the last ';' or '. ' boundary
    seg = re.split(r"(?<=[.;:])\s(?=[A-Z(*])|\s-\s(?=\*\*)|\s#+\s|\s\|\s", chunk)[-1] if chunk else ""
    for q in re.findall(r'"([^"]{6,})"', seg):
        parts = [p.strip(" .,;") for p in q.split("[...]")]
        ok = all(any(norm(p) in norm(rows.get(g, "")) for g in group) for p in parts if len(p) > 3)
        if not ok:
            problems += 1
            print("NOT IN ROW", group, "::", q[:140])
print("ids cited:", len(set(ids)), "| problems:", problems)
