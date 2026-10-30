"""Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment on the same
line as an id (and within 300 characters before it) appears in one of the ids on that line. Normalizes quotes and the
replacement character. Prints problems; exit 1 if any."""
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
RUN = ROOT + r"\Test Runs\2026-10-12 Run - FSRDQ Fisker.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8-sig"))}
def norm(s):
    s = s.replace("\ufffd", "").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip().lower()
txt = open(RUN, encoding="utf-8").read()
probs = []
if re.search(r"\[E\d+-\d+\]", txt): probs.append("E-id present")
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", txt)
for i in set(ids):
    if i not in rows: probs.append(f"missing id {i}")
nfrag = 0
for para in re.split(r"\n(?=\S)|\n\s*-\s", txt):
    for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", para):
        pre = para[:m.start()]
        cands = [i for i in re.findall(r"\[([MLR]\d{4}-\d{3})\]", para)]
        # the fragment immediately before this id
        frs = re.findall(r'"([^"]{4,})"', pre)
        if not frs: continue
        fr = frs[-1]
        if len(pre) - pre.rfind('"') > 300: continue  # fragment not adjacent to the id
        # skip fragments that are filing quotes (they precede a parenthesised accession) -- flagged for hand check
        ok = any(norm(fr) in norm(rows.get(c, "")) for c in cands)
        nfrag += 1
        if not ok: probs.append(f"fragment not in {cands}: {fr[:90]!r}")
print(f"ids cited: {len(set(ids))} distinct; fragments checked: {nfrag}")
for p in probs: print("PROBLEM:", p)
sys.exit(1 if probs else 0)
