"""Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment adjacent to an id
(the nearest double-quoted string before the id on the same paragraph) is in that row's quote. Apostrophes and dashes normalised."""
import csv, re, os, sys
sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.abspath(os.path.join(here, "..", ".."))
run = open(os.path.join(root, "Test Runs", "2026-10-17 Run - FLR Fluor.md"), encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(os.path.join(root, "principle_ledger_v5.csv"), encoding="utf-8-sig"))}
def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2014", "-").replace("\u2013", "-")
    return re.sub(r"\s+", " ", s).strip().lower()
bad = 0
eids = re.findall(r"\[E\d-\d+\]", run)
print("E-ids:", eids or "none"); bad += len(eids)
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
missing = sorted({i for i in ids if i not in rows})
print("ids cited:", len(ids), "distinct:", len(set(ids)), "missing:", missing or "none"); bad += len(missing)
# quoted fragment immediately before an id: "...." followed (within 3 chars after optional punctuation) by **[ID]**
for m in re.finditer(r'"([^"]{6,600})"[\s.,;:()]{0,4}\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    parts = [p.strip() for p in re.split(r"\[\.\.\.\]", frag) if p.strip()]
    ok = all(norm(p) in norm(rows[i]) for p in parts)
    if not ok:
        bad += 1; print("NOT IN ROW", i, "::", frag[:160])
print("RESULT:", "PASS" if bad == 0 else f"FAIL ({bad})")
