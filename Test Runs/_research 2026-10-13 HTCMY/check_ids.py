# Citation check for the HTCMY run: (1) no E-ids; (2) every M/L/R id exists in principle_ledger_v5.csv;
# (3) every quoted fragment that sits immediately before an id (same paragraph, nothing but punctuation, an
# attribution or other ids between) appears in that id's row, after normalising quotes, dashes and spaces, with
# [...] treated as an elision. Usage: python check_ids.py <run file> <ledger csv>
import csv, re, sys
run, ledger = sys.argv[1], sys.argv[2]
rows = {}
with open(ledger, encoding="utf-8") as f:
    r = csv.reader(f); next(r)
    for row in r:
        rows[row[0]] = row[2]
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-").replace("�", "")
    s = re.sub(r"[^\w\s'\-\.,;:\?!\$%/&\(\)\"]", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()
text = open(run, encoding="utf-8").read()
bad = 0
eids = re.findall(r"\[(E\d-\d+)\]", text)
if eids: print("E-IDS FOUND:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING ID", i); bad += 1
print(f"{len(ids)} id citations, {len(set(ids))} distinct, all in ledger: {all(i in rows for i in ids)}")
# quoted fragment immediately before an id
paras = re.split(r"\n\s*\n|\n- |\n\| ", text)
checked = 0
for p in paras:
    p1 = p.replace("\n", " ")
    for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", p1):
        before = p1[:m.start()]
        # the nearest quotation that closes within 40 characters before the id
        q = list(re.finditer(r"\"([^\"]{3,}?)\"|“([^”]{3,}?)”", before))
        if not q: continue
        last = q[-1]
        gap = before[last.end():]
        if len(gap) > 40 or re.search(r"\*\*\[", gap) and len(gap) > 40: continue
        frag = last.group(1) or last.group(2)
        row = norm(rows.get(m.group(1), ""))
        ok = all(norm(part) in row for part in re.split(r"\[\.\.\.\]", frag) if norm(part))
        checked += 1
        if not ok:
            # a quote may belong to a neighbouring id in the same cluster; try ids within 60 chars after
            after_ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", p1[m.start():m.start()+80])
            if any(all(norm(part) in norm(rows.get(a, "")) for part in re.split(r"\[\.\.\.\]", frag) if norm(part)) for a in after_ids):
                continue
            print("FRAGMENT NOT IN ROW", m.group(1), "|", frag[:120]); bad += 1
print(f"quoted fragments checked: {checked}; problems: {bad}")
sys.exit(1 if bad else 0)
