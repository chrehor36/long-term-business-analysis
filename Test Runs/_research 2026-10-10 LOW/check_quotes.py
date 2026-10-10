# Check the LOW run file: (1) no E-ids; (2) every M/L/R id exists in principle_ledger_v5.csv; (3) every quoted fragment
# that stands immediately before an id (or before a run of ids) is found in at least one of those rows, after normalising
# quotes, dashes and whitespace, with "[...]" splitting a fragment into parts that must each be found.
import csv, re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
RUN = os.path.join(ROOT, "Test Runs", "2026-10-10 Run - LOW Lowe's.md")
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8-sig"))}
s = open(RUN, encoding="utf-8").read()

def norm(t):
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    t = t.replace("—", "-").replace("–", "-").replace("�", "")
    t = re.sub(r"\s+", " ", t)
    return t.strip().lower()

bad = 0
eids = re.findall(r"\[E\d-\d+\]", s)
print("E-ids:", eids if eids else "none")
bad += len(eids)
ids = sorted(set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", s)))
missing = [i for i in ids if i not in rows]
print(f"ids cited: {len(ids)}; missing: {missing if missing else 'none'}")
bad += len(missing)

# quoted fragment(s) followed (within 12 chars, allowing ')', ',', '.', spaces) by one or more ids
pat = re.compile(r'"([^"]{6,}?)"[\s\.,;:)]{0,6}((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[\s,]*)+)')
checked = 0
for m in pat.finditer(s):
    frag = m.group(1)
    cited = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))
    parts = [p for p in re.split(r"\[\.\.\.\]", frag) if p.strip()]
    ok = False
    for c in cited:
        q = norm(rows.get(c, ""))
        if all(norm(p).strip(" .,;:'\"") in q for p in parts):
            ok = True; break
    checked += 1
    if not ok:
        bad += 1
        print("NOT FOUND:", cited, "|", frag[:160])
print(f"quoted fragments checked: {checked}")
print("RESULT:", "PASS" if bad == 0 else f"FAIL ({bad})")
sys.exit(0 if bad == 0 else 1)
