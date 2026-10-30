"""Citation check for the PNW run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
that stands immediately before an id (quote, then up to a few characters, then **[ID]**) is found in that row's quote.
Also lists em dashes outside headings. Run from the repository root: python -I "Test Runs/_research 2026-10-26 PNW/check_cites.py" """
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = "Test Runs/2026-10-26 Run - PNW Pinnacle West.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
t = open(RUN, encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s.replace("�", "").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()
bad = 0
ids = re.findall(r"\[([A-Z]+\d{0,4}-\d{2,3})\]", t)
eids = [i for i in ids if i.startswith("E")]
if eids: print("E-ids:", eids); bad += 1
missing = sorted({i for i in ids if i not in rows})
if missing: print("missing ids:", missing); bad += 1
# quote immediately followed by an id: "....." **[ID]**  or "....." [ID] ; also "...", ... **[ID]** chains not attempted
for m in re.finditer(r'"([^"\n]{6,400}?)"\s*[.,;:]?\s*\*\*\[([A-Z]\d{4}-\d{3})\]\*\*', t.replace("\n  ", " ").replace("\n", " ")):
    q, i = m.group(1), m.group(2)
    if i not in rows: continue
    frags = [f for f in re.split(r"\[\.\.\.\]", q) if f.strip()]
    for f in frags:
        f2 = norm(f).strip(" .,;")
        if f2 and f2 not in norm(rows[i]):
            print(f"NOT IN ROW {i}: {f2[:120]}"); bad += 1
dash = [ln for ln in t.splitlines() if "—" in ln and not ln.startswith("#")]
dash = [ln for ln in dash if not any(k in ln for k in ("— reinvest —",))]
for ln in dash: print("em dash outside heading:", ln[:120])
print(f"{len(set(ids))} distinct ids; {'FAIL' if bad else 'PASS'}")
