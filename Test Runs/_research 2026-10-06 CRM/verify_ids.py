"""Check the run file: every bold v5 id exists in principle_ledger_v5.csv, and every double-quoted fragment that sits
directly before a bold id (same sentence run, up to the id) appears in that row's quote. Italic filing quotes (*"..."*)
are skipped. Usage: python -I verify_ids.py
"""
import csv, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
RUN = os.path.join(ROOT, "Test Runs", "2026-10-06 Run - CRM Salesforce.md")
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
bad = sorted({i for i in ids if i not in rows})
other = sorted(set(re.findall(r"\[(E\d+-\d+)\]", text)))
print(f"{len(set(ids))} distinct v5 ids cited; missing from ledger: {bad or 'none'}; E-ids: {other or 'none'}")

fails = 0
checked = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text):
    rid = m.group(1)
    start = max(0, m.start() - 400)
    seg = text[start:m.start()]
    seg = seg.split("**[")[-1] if "**[" in seg else seg
    for q in re.findall(r'(?<!\*)"([^"]{6,}?)"(?!\*)', seg):
        if "*" in q:
            continue
        checked += 1
        if norm(q).rstrip(".,") not in norm(rows.get(rid, "")):
            fails += 1
            print(f"  NOT IN {rid}: {q[:90]}")
print(f"{checked} quoted fragments checked against the row cited after them; {fails} not found")
