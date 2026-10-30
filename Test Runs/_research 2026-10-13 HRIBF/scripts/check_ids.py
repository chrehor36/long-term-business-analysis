# Check: no E-ids; every M/L/R id exists in the v5 ledger; every quoted fragment directly before a run of ids is in one of those rows.
import csv, re, sys
L = "C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv"
RUN = sys.argv[1] if len(sys.argv) > 1 else "C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-13 Run - HRIBF Horiba.md"
rows = {}
for x in csv.DictReader(open(L, encoding="utf-8-sig")):
    rows[x.get("id") or x.get("\ufeffid")] = x["quote_verbatim"]
text = open(RUN, encoding="utf-8").read()
def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-").replace("\ufffd", "")
    return re.sub(r"\s+", " ", s).strip().lower()
bad = 0
eids = re.findall(r"\[E\d-\d+\]", text)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
loose = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
for i in sorted(set(loose)):
    if i not in rows: print("MISSING id", i); bad += 1
print(f"{len(ids)} bold cites, {len(set(loose))} distinct ids")
# quoted fragment(s) immediately followed by one or more bold ids
flat = re.sub(r"\s+", " ", text)
pat = re.compile(r'"([^"]{3,600})"\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:\s*,\s*)?)+)')
n = 0
for m in pat.finditer(flat):
    frag = m.group(1); idl = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))
    parts = [p for p in re.split(r"\[\.\.\.\]", frag) if p.strip()]
    ok = any(all(norm(p) in norm(rows.get(i, "")) for p in parts) for i in idl)
    n += 1
    if not ok:
        bad += 1; print("NOT IN ROW:", idl, "<<", frag[:160], ">>")
print(f"{n} quoted fragments checked; problems: {bad}")
sys.exit(1 if bad else 0)
