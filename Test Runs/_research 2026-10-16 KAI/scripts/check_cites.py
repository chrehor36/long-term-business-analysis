# Citation check for the KAI run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment next to an id appears verbatim (elisions [...] split) in one of the adjacent ids' rows.
import csv, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
run = "Test Runs/2026-10-16 Run - KAI Kadant.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(run, encoding="utf-8").read()
flat = re.sub(r"\s*\n\s*", " ", text)
norm = lambda s: re.sub(r"\s+", " ", s).strip()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); bad += 1
print(len(set(ids)), "distinct ids,", len(ids), "citations")
ID = r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*"
pairs = []
# quote then ids: "..." **[ID]**(, **[ID]**)*
for m in re.finditer(r'"([^"]{4,}?)"\s*((?:' + ID + r'(?:,\s*)?)+)', flat):
    pairs.append((m.group(1), re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))))
# ids then (" ... ")
for m in re.finditer(ID + r'\s*\("([^"]{4,}?)"\)', flat):
    pairs.append((m.group(2), [m.group(1)]))
# quote ... **[ID]** within same sentence:  "..." [words without quotes] **[ID]**
checked = 0
for q, idl in pairs:
    parts = [norm(p) for p in q.split("[...]") if norm(p)]
    ok = any(all(p in norm(rows.get(i, "")) for p in parts) for i in idl)
    checked += 1
    if not ok:
        print("NOT FOUND:", idl, "::", q[:160]); bad += 1
print(checked, "quoted fragments checked;", "FAIL" if bad else "PASS")
