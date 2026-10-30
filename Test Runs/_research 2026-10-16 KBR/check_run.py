"""Run-file check: no E-ids; every M/L/R id resolves in principle_ledger_v5.csv; every quoted fragment that
stands immediately before an id (same sentence, nearest quote) is found in that row's text, elisions [...] split."""
import csv, re, sys, os
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
run = open(os.path.join(ROOT, "Test Runs", "2026-10-16 Run - KBR KBR Inc.md"), encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8-sig"))}
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip().lower()
bad = 0
eids = re.findall(r"\[E\d-\d+\]", run)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
allids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", run))
for i in sorted(allids):
    if i not in rows: print("MISSING id", i); bad += 1
print("ids cited:", len(allids), "occurrences:", len(re.findall(r"\[([MLR]\d{4}-\d{3})\]", run)))
# quoted fragment immediately before an id: pattern "..." then optional spaces/punct then **[ID]**
for m in re.finditer(r'"([^"\n]{3,400})"[^"\n]{0,6}\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    text = norm(rows[i])
    parts = [norm(p) for p in re.split(r"\[\.\.\.\]|\[|\]", frag) if norm(p).strip(" .,")]
    ok = all(p.strip(" .,") in text for p in parts)
    if not ok:
        print("FRAGMENT NOT IN ROW", i, "::", frag); bad += 1
print("FAIL" if bad else "PASS", bad)
