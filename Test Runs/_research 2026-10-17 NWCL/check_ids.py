"""Check the NWCL run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every quoted fragment that is followed (within the same sentence, before any other quote) by one or
more bold ids is found, after normalising quotes and whitespace, in at least one of those rows.
Elisions written [...] split a quote into fragments."""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "Test Runs" / "2026-10-17 Run - NWCL newcleo.md"
LEDGER = ROOT / "principle_ledger_v5.csv"

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("�", "")
    return re.sub(r"\s+", " ", s).strip().lower()

rows = {r["id"]: norm(r["quote_verbatim"]) for r in csv.DictReader(open(LEDGER, encoding="utf-8-sig"))}
text = RUN.read_text(encoding="utf-8")
flat = re.sub(r"\s+", " ", text)
bad = 0
if re.search(r"\[E\d", text):
    print("E-id found"); bad += 1
ids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", text))
for i in sorted(ids):
    if i not in rows:
        print("MISSING id", i); bad += 1
print(len(ids), "distinct ids")

# quote followed by ids: "....." then up to 60 non-quote chars then **[ID]**(, **[ID]**)*
pat = re.compile(r'"([^"]{8,}?)"([^"]{0,60}?)((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[ ,;and]*)+)')
checked = 0
for m in pat.finditer(flat.replace("“", '"').replace("”", '"')):
    q, between, idblock = m.group(1), m.group(2), m.group(3)
    if "**[" in between:
        continue
    qids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", idblock)
    frags = [f for f in re.split(r"\[\.\.\.\]", q) if len(f.strip(" .,;:")) > 3]
    for f in frags:
        nf = norm(f).strip(" .,;:")
        if not any(nf in rows.get(i, "") for i in qids):
            print("NOT IN ROW", qids, "|", f[:120]); bad += 1
        checked += 1
print(checked, "fragments checked")
print("PASS" if not bad else f"FAIL ({bad})")
sys.exit(1 if bad else 0)
