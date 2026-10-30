# Checks the LHSW run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately before an id (the "..." **[ID]** pattern) is in that row.
import csv, re, sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
RUN = ROOT + r"\Test Runs\2026-10-13 Run - LHSW Lianhe Sowell International.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"')):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()
bad = 0
eids = re.findall(r"\[E\d-\d+\]", text)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); bad += 1
# quoted fragment directly before an id: "...." **[ID]**  (allow a closing ." or ," etc.)
flat = re.sub(r"\s+", " ", text)
for m in re.finditer(r'"([^"]{8,}?)"[.,;:]?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    frag, i = m.group(1), m.group(2)
    row = norm(rows.get(i, ""))
    for piece in [p for p in norm(frag).split("[...]")]:
        piece = piece.strip().strip(".,;: ")
        if piece and piece not in row:
            print(f"NOT IN ROW {i}: {piece[:120]}"); bad += 1
print(f"ids cited: {len(set(ids))}; quote checks done; problems: {bad}")
sys.exit(1 if bad else 0)
