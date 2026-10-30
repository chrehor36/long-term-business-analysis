# Ledger check for the TURV run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately before an id (same paragraph) is in that row (elisions [...] split).
import csv, re, sys, unicodedata

RUN = r"C:\Projects\BRK\Test Runs\2026-10-29 Run - TURV Two Rivers Water & Farming.md"
LEDGER = r"C:\Projects\BRK\principle_ledger_v5.csv"

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\ufffd", "")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()

rows = {}
with open(LEDGER, encoding="utf-8") as f:
    for r in csv.DictReader(f):
        rows[r["\ufeffid"] if "\ufeffid" in r else r["id"]] = norm(r["quote_verbatim"])

text = open(RUN, encoding="utf-8").read()
fail = 0
if re.search(r"\[E\d", text):
    print("FAIL: E-id present"); fail += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
for i in sorted(set(ids)):
    if i not in rows:
        print("FAIL: missing id", i); fail += 1
# quoted fragment directly followed by an id: "...." **[ID]**  or  "...." (anything up to 3 chars) **[ID]**
for m in re.finditer(r"[\"\u201c]([^\"\u201c\u201d]{6,600})[\"\u201d][^\"\n]{0,4}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text):
    frag, i = m.group(1), m.group(2)
    if i not in rows:
        continue
    for piece in re.split(r"\[\.\.\.\]", frag):
        p = norm(piece).strip(" .,;:")
        if p and p not in rows[i]:
            print("FAIL: fragment not in", i, "->", piece[:90]); fail += 1
print("ids cited:", len(set(ids)), "| quote-id pairs checked:",
      len(re.findall(r"[\"\u201c][^\"\u201c\u201d]{6,600}[\"\u201d][^\"\n]{0,4}?\*\*\[[MLR]\d{4}-\d{3}\]\*\*", text)))
print("PASS" if not fail else f"FAIL ({fail})")
sys.exit(1 if fail else 0)
