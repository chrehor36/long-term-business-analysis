# Citation check for the BAC run of 2026-10-13: no E-ids; every M/L/R id in principle_ledger_v5.csv;
# every quoted fragment that stands immediately before an id is found in that row (elisions [...] split).
import csv, re, sys, unicodedata

RUN = "Test Runs/2026-10-13 Run - BAC Bank of America.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("—", "-"), ("–", "-"), ("�", "")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()

bad = 0
e_ids = re.findall(r"\[E\d+-\d+\]", text)
if e_ids:
    print("E-ids found:", e_ids); bad += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING id", i); bad += 1
# quoted fragment(s) directly before a bold id, allowing a few words between the closing quote and the id
for m in re.finditer(r'"([^"]{3,900})"[^"\[\n]{0,40}\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text):
    frag, i = m.group(1), m.group(2)
    if i not in rows:
        continue
    row = norm(rows[i])
    for part in re.split(r"\[\.\.\.\]", frag):
        p = norm(part).strip(" .,;:?")
        p = p.replace('"', "'") if p not in row else p
        if p and p not in row and p.replace("'", '"') not in row and norm(part).strip(" .,;:?") not in row.replace('"', "'"):
            print(f"NOT IN ROW {i}: {part[:120]!r}"); bad += 1
print(f"{len(set(ids))} distinct ids checked; {'PASS' if not bad else 'FAIL'}")
sys.exit(1 if bad else 0)
