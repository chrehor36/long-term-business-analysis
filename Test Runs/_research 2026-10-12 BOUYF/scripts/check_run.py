"""Citation check for the BOUYF run file. Usage (from repo root): python -I -X utf8 "Test Runs/_research 2026-10-12 BOUYF/scripts/check_run.py"
1. no E-ids; 2. every M/L/R id exists in principle_ledger_v5.csv;
3. every quoted fragment immediately followed by bold ids is found (after whitespace and quote normalisation, [...] splits) in at least
   one of the ids in that cluster; failures are listed with the fragment and the ids."""
import csv, re, sys
RUN = "Test Runs/2026-10-12 Run - BOUYF Bouygues.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf8").read()

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip().lower()

problems = []
eids = re.findall(r"\[(E\d+-\d+)\]", text)
if eids:
    problems.append(f"E-ids present: {sorted(set(eids))}")
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
missing = sorted({i for i in ids if i not in rows})
if missing:
    problems.append(f"ids not in ledger: {missing}")

flat = re.sub(r"\s+", " ", text)
# a quoted fragment followed (optionally after punctuation/space) by a cluster of bold ids
pat = re.compile(r'"([^"]{3,600})"\s*[,.;:]?\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[;,]?\s*)+)')
n_frag = 0
for m in pat.finditer(flat):
    frag, cluster = m.group(1), m.group(2)
    cids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", cluster)
    parts = [p for p in re.split(r"\s*\[\.\.\.\]\s*", frag) if p.strip()]
    n_frag += 1
    ok = any(all(norm(p) in norm(rows.get(c, "")) for p in parts) for c in cids)
    if not ok:
        problems.append(f"fragment not in {cids}: \"{frag[:120]}\"")
print(f"ids cited: {len(ids)} ({len(set(ids))} distinct); fragments checked: {n_frag}; problems: {len(problems)}")
for p in problems:
    print(" -", p)
sys.exit(1 if problems else 0)
