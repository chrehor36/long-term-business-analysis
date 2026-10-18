"""Check the TEX run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
standing immediately before an id (in the same paragraph, the quote ending within a few characters of the id) is in
that row's quote_verbatim (normalised for curly quotes, dashes and whitespace; [...] splits the fragment)."""
import csv, re, sys, unicodedata
RUN = "Test Runs/2026-10-13 Run - TEX Terex.md"
rows = {r["﻿id"] if "﻿id" in r else r["id"]: r for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8"))}
def norm(t):
    t = unicodedata.normalize("NFKC", t)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("—", "-"), ("–", "-")):
        t = t.replace(a, b)
    t = t.replace('"', "").replace("**", "")
    return re.sub(r"\s+", " ", t).strip().lower()
s = open(RUN, encoding="utf-8").read()
bad = 0; CHECKED = []
for m in re.finditer(r"\[(E\d[\w-]*)\]", s):
    print("E-ID", m.group(1)); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", s)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING", i); bad += 1
# quoted fragments: "...." followed by up to 12 chars then **[ID]**
for para in s.split("\n\n"):
    flat = para.replace("\n", " ")
    for m in re.finditer(r"([\"“])([^\"“”]{3,}?)([\"”])([^\"“”]{0,14}?)((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[ ,;]*)+)", flat):
        frag = m.group(2)
        idl = re.findall(r"\[([MLR]\d{4}-\d{3})\]", m.group(5))
        parts = [norm(x) for x in re.split(r"\[\.\.\.\]|\.\.\.", frag) if norm(x)]
        ok_any = False; CHECKED.append(frag)
        for i in idl:
            if i in rows:
                q = norm(rows[i]["quote_verbatim"])
                if all(pt.strip(" .,;:") in q for pt in parts):
                    ok_any = True
        if not ok_any:
            print("QUOTE NOT IN ROW", idl, "|", frag[:120]); bad += 1
print("ids:", len(set(ids)), "fragments checked:", len(CHECKED), "problems:", bad)
sys.exit(1 if bad else 0)
