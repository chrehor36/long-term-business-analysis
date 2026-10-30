"""Check the PNR run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that sits
beside an id (same paragraph, quote immediately before the id's bracket, allowing [...] elisions) is in that row.
Usage: python -I check_quotes.py (from the research folder)."""
import csv, re, sys
ROOT = "../../"
RUN = ROOT + "Test Runs/2026-10-10 Run - PNR Pentair.md"
rows = {r[0]: r[2] for r in csv.reader(open(ROOT + "principle_ledger_v5.csv", encoding="utf-8-sig"))}
txt = open(RUN, encoding="utf-8").read()
bad = 0
for m in re.finditer(r"\[(E\d[-\w]*)\]", txt):
    print("E-ID", m.group(1)); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", txt)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING", i); bad += 1
norm = lambda s: re.sub(r"\s+", " ", s.replace("�", "")).strip()
# a quote followed (within the same line run, up to 40 chars) by one or more bold ids
pat = re.compile(r"\"([^\"]{6,}?)\"[^\"\n]{0,40}?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[ ,]*)+)", re.S)
flat = txt.replace("\n", " ")
checked = 0
for m in pat.finditer(flat):
    q = m.group(1); cited = re.findall(r"\[([MLR]\d{4}-\d{3})\]", m.group(2))
    parts = [norm(p) for p in q.split("[...]") if norm(p)]
    ok = any(all(p in norm(rows.get(c, "")) for p in parts) for c in cited)
    checked += 1
    if not ok:
        print("NOT IN ROW", cited, "|", q[:120]); bad += 1
print(f"ids {len(set(ids))}, quotes checked {checked}, problems {bad}")
sys.exit(1 if bad else 0)
