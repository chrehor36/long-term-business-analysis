# Citation check for the ITOCY run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately before an id (same sentence) appears in that row.
import csv, re, sys
base = r"C:/Users/chreh/OneDrive/Documents/BRK/"
run = open(base + "Test Runs/2026-10-12 Run - ITOCY ITOCHU Corporation.md", encoding="utf-8").read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(base + "principle_ledger_v5.csv", encoding="utf-8-sig"))}
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", run)
print("E-ids:", eids); bad += len(eids)
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", run)
missing = sorted(set(i for i in ids if i not in rows))
print("ids cited:", len(set(ids)), "missing:", missing); bad += len(missing)
norm = lambda x: re.sub(r"\s+", " ", x.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')).strip()
# quoted fragment followed (within 12 chars) by one or more ids
for m in re.finditer(r'"([^"]{8,600}?)"\s*(?:\([^)]{0,40}\))?\s*\**\s*((?:\[[MLR]\d{4}-\d{3}\]\**,?\s*\**)+)', run, re.S):
    frag = norm(m.group(1))
    for i in re.findall(r"[MLR]\d{4}-\d{3}", m.group(2)):
        q = norm(rows.get(i, ""))
        parts = [p.strip(" .,;:") for p in frag.split("[...]")]
        ok = all(p == "" or p in q for p in parts)
        if not ok:
            # tolerate a quote that contains nested quotes the regex cut
            print("FRAGMENT NOT IN ROW", i, "|", frag[:160]); bad += 1
print("RESULT:", "PASS" if bad == 0 else f"FAIL ({bad})")
