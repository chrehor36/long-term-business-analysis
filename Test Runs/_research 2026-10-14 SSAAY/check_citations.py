"""Citation check for the SSAAY run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
standing within 160 characters before an id (same paragraph) appears in that row (normalised quotes and whitespace)."""
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
run = open(ROOT + r"\Test Runs\2026-10-14 Run - SSAAY SSAB.md", encoding="utf-8").read()
R = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8-sig"))}
def norm(t): return re.sub(r"\s+", " ", t.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')).strip().lower()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", run); print("E-ids:", eids); bad += len(eids)
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
print("ids cited:", len(ids), "distinct:", len(set(ids)))
for i in sorted(set(ids)):
    if i not in R: print("MISSING", i); bad += 1
nfrag = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run):
    i = m.group(1); start = max(0, m.start() - 220); seg = run[start:m.start()]
    seg = seg.split("\n\n")[-1]
    # the quote immediately before the id (closing quote within 25 chars of the id)
    q = re.search(r'"([^"]{6,})"[^"]{0,25}$', seg)
    if not q or i not in R: continue
    frag = q.group(1).replace("[...]", "\x00")
    nfrag += 1
    for part in frag.split("\x00"):
        part = norm(part.strip(" .,;"))
        if part and part not in norm(R[i]): print("FRAGMENT NOT IN ROW", i, "|", part[:90]); bad += 1
print("fragments checked:", nfrag, "problems:", bad)
