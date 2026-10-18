# Citation check for the AMTM run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment in the same sentence as an id is found in that id's row (quotes normalised).
import csv, re, sys, unicodedata
RUN = "Test Runs/2026-10-17 Run - AMTM Amentum.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
def norm(x):
    x = x.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("�", "'")
    x = x.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", x).strip().lower()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
missing = sorted(set(i for i in ids if i not in rows))
if missing: print("MISSING ids:", missing); bad += 1
print(f"ids cited: {len(ids)} ({len(set(ids))} distinct); missing: {len(missing)}")
# fragment check: for each id occurrence, take the text from the previous id/sentence boundary to the id,
# collect double-quoted fragments, and require each to appear in the row (ellipsis [...] splits it).
checked = 0; fails = []
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text):
    i = m.group(1); start = max(text.rfind("**[", 0, m.start()-1), text.rfind("\n", 0, m.start()), 0)
    seg = text[start:m.start()]
    seg = seg.split("**[")[-1] if "**[" in seg else seg
    # sentence scope: only the sentence that holds the id (split at a full stop or semicolon followed by a space)
    seg = re.split(r"(?<=[.;:])\s+(?=[A-Z*(])", seg)[-1]
    frags = re.findall(r"[\"“]([^\"”]{6,}?)[\"”]", seg)
    row = norm(rows.get(i, ""))
    for f in frags:
        parts = [p.strip(" .,;:") for p in re.split(r"\[\.\.\.\]", f) if len(p.strip(" .,;:")) > 3]
        for p in parts:
            checked += 1
            if norm(p) not in row:
                fails.append((i, p))
print(f"quoted fragments checked: {checked}; not found in the cited row: {len(fails)}")
for i, p in fails: print("  ", i, "|", p[:160])
sys.exit(1 if (bad or fails) else 0)
