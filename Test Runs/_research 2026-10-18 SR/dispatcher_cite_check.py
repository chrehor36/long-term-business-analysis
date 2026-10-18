# Dispatcher's check (overnight 2026-10-18, SR): every quoted fragment adjacent to a v5 id is in that row.
import csv, re, sys, unicodedata
root = sys.argv[1]
def norm(s):
    s = unicodedata.normalize("NFKC", s).replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).lower().strip()
rows = {}
with open(root + "/principle_ledger_v5.csv", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        rows[r["id"]] = norm(r["quote_verbatim"])
text = open(sys.argv[2], encoding="utf-8").read()
idre = r"[MLR]\d{4}-\d{3}"
bad = n = 0
eids = re.findall(r"\bE\d+-\d+\b", text)
missing = sorted({i for i in re.findall(idre, text) if i not in rows})
for m in re.finditer(r'[\"“]([^\"”]{6,}?)[\"”]\s*\**\s*\[?\**((?:' + idre + r')(?:[,; ]+' + idre + r')*)', text):
    frag, ids = m.group(1), re.findall(idre, m.group(2))
    n += 1
    for piece in re.split(r"\s*\[\.\.\.\]\s*|\s*\.\.\.\s*|\s*…\s*", frag):
        p = norm(piece).strip(" .,;:")
        if p and not any(p in rows.get(i, "") for i in ids):
            bad += 1; print("SLIP", ids, repr(piece[:90]))
print("E-ids", eids, "missing", missing, "fragments", n, "slips", bad)
