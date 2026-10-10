"""Run-file check for the NDSN run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every quoted fragment that sits immediately before an id (within 40 characters, before the bold id) is in that row.
Matching ignores case, whitespace, apostrophes, quotation marks, dashes and the shelf's replacement character."""
import csv, re, sys, unicodedata
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
RUN = ROOT + r"\Test Runs\2026-10-10 Run - NDSN Nordson.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8-sig"))}
DROP = "\ufffd'\"-\u2019\u2018\u201c\u201d\u2014\u2013"
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = "".join(ch for ch in s if ch not in DROP)
    return re.sub(r"\s+", " ", s).strip().lower()
txt = open(RUN, encoding="utf-8").read()
bad = 0
eids = re.findall(r"\[E\d-\d+\]", txt)
if eids:
    print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", txt)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING id", i); bad += 1
pat = r"[\"\u201c]([^\"\u201c\u201d]{6,}?)[\"\u201d][^\"\u201c\n]{0,40}?((?:\s*,?\s*\*\*\[[MLR]\d{4}-\d{3}\]\*\*)+)"
n = 0
for m in re.finditer(pat, txt):
    frag = m.group(1); idl = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2)); n += 1
    parts = [p for p in re.split(r"\s*\[\.\.\.\]\s*", frag) if p.strip()]
    ok = any(all(norm(p) in norm(rows.get(i, "")) for p in parts) for i in idl)
    if not ok:
        print("NOT IN ROW:", idl, "|", frag[:120]); bad += 1
print("ids cited:", len(set(ids)), "| quoted fragments checked:", n, "| problems:", bad)
sys.exit(1 if bad else 0)
