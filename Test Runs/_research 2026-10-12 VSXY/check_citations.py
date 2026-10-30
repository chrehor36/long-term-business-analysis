"""Citation check for the VSXY run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
standing directly before an id (or a run of ids) is in one of those rows (elisions [...] split the fragment)."""
import csv, re, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RUN = os.path.join(ROOT, "Test Runs", "2026-10-12 Run - VSXY Victoria's Secret.md")
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8-sig"))}
t = open(RUN, encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s).strip()
bad = 0
if re.search(r"\[E\d-\d+\]", t):
    print("E-id found"); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", t)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING id", i); bad += 1
# quoted fragment immediately before an id run: "...." then optional punctuation/space then **[ID]** (, **[ID]**)*
pat = re.compile(r"\"([^\"]{3,600}?)\"[\s.,;:)]*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)")
flat = t.replace("\n", " ")
checked = 0
for m in pat.finditer(flat):
    frag = m.group(1)
    cites = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))
    parts = [norm(p) for p in frag.split("[...]") if norm(p)]
    ok = any(all(p.rstrip(".") in norm(rows.get(c, "")) for p in parts) for c in cites)
    checked += 1
    if not ok:
        print("NOT IN ROW", cites, "::", frag[:160]); bad += 1
print(f"ids {len(set(ids))}, fragments checked {checked}, problems {bad}")
sys.exit(1 if bad else 0)
