# Citation check for the MAR run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every double-quoted fragment immediately before an id (or a run of ids) is in that id's row (normalised; [...] splits).
import csv, re, sys, unicodedata
ROOT = "../.."
run = open(f"{ROOT}/Test Runs/2026-10-14 Run - MAR Marriott International.md", encoding="utf-8").read()
rows = {r["﻿id"] if "﻿id" in r else r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(f"{ROOT}/principle_ledger_v5.csv", encoding="utf-8-sig"))}
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a,b in [("’","'"),("‘","'"),("“",'"'),("”",'"'),("—","-"),("–","-"),("*","")]: s = s.replace(a,b)
    return re.sub(r"\s+"," ",s).strip().lower()
bad = 0
eids = re.findall(r"\[E\d-\d+\]", run)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); bad += 1
# fragment then ids: “...” or "..." followed within 40 chars by **[ID]** (possibly several)
pat = re.compile(r'[“"]([^“”"]{3,600})[”"][^“”"\[]{0,40}((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[ ,;and]*)+)')
nfrag = 0
for m in pat.finditer(run):
    frag = m.group(1); idl = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))
    pieces = [p.strip(" .,;:") for p in re.split(r"\[\.\.\.\]|\.\.\.", frag) if p.strip(" .,;:")]
    for p in pieces:
        nfrag += 1
        if not any(i in rows and norm(p) in norm(rows[i]) for i in idl):
            print("FRAGMENT NOT IN ROW", idl, "::", p[:120]); bad += 1
print(f"ids cited: {len(set(ids))}; fragments checked: {nfrag}; problems: {bad}")
sys.exit(1 if bad else 0)
