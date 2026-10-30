"""Citation check for the CKSNY run file (dispatcher copy): (1) no E-ids; (2) every M/L/R id exists in principle_ledger_v5.csv;
(3) every quoted fragment that sits immediately before a bold id (same sentence span) is in that row's quote,
pieces split on [...]. Usage: python check_cites.py RUNFILE LEDGER"""
import sys, re, csv, unicodedata
run = open(sys.argv[1], encoding="utf-8").read()
rows = {}
with open(sys.argv[2], encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        rows[r["id"]] = r["quote_verbatim"]
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("**", "")
    return re.sub(r"\s+", " ", s).strip().lower()
probs = 0
for m in re.finditer(r"\[(E\d[-\w]*)\]", run):
    print("E-ID:", m.group(1)); probs += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING ID:", i); probs += 1
# quoted fragment followed (within 12 chars) by one or more bold ids
pat = re.compile(r"[\"“]([^\"“”]{3,}?)[\"”][^\"“\n]{0,40}?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[ ,;and]*)+)")
n = 0
for m in pat.finditer(run):
    frag = m.group(1); cited = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))
    pieces = [p for p in re.split(r"\[\.\.\.\]", frag) if norm(p).strip(" .,;:")]
    ok = any(i in rows and all(norm(p).strip(" .,;:") in norm(rows[i]) for p in pieces) for i in cited)
    n += 1
    if not ok:
        print("FRAGMENT NOT IN ROW:", cited, "|", frag[:120]); probs += 1
print(f"ids cited: {len(set(ids))}; quoted fragments checked: {n}; problems: {probs}")
