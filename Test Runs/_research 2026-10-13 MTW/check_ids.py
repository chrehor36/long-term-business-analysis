"""Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that stands
before an id (since the previous id in the same paragraph or bullet) appears in one of the ids of that citation group.
Elisions [...] split a fragment into parts, each of which must be in the same row. Prints problems."""
import csv, re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
root = pathlib.Path(__file__).resolve().parents[2]
run = (root / "Test Runs" / "2026-10-13 Run - MTW Manitowoc.md").read_text(encoding="utf-8")
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(root / "principle_ledger_v5.csv", encoding="utf-8-sig"))}
bad = 0
for m in re.finditer(r"\[E\d+-\d+\]", run):
    print("E-id:", m.group()); bad += 1
ids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", run))
for i in sorted(ids):
    if i not in rows:
        print("missing id:", i); bad += 1

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

blocks = re.split(r"\n\s*\n|\n(?=\s*- )|\n(?=\|)", run)
GROUP = re.compile(r"(\*\*\[[MLR]\d{4}-\d{3}\]\*\*(,\s*)?)+")
checked = 0
for b in blocks:
    line = norm(b)
    pos = 0
    for m in GROUP.finditer(line):
        seg = line[pos:m.start()]
        pos = m.end()
        group = re.findall(r"\[([MLR]\d{4}-\d{3})\]", m.group())
        for q in re.findall(r"[“\"]([^”\"]{6,})[”\"]", seg):
            parts = [p.strip(" ,.;") for p in q.split("[...]") if len(p.strip(" ,.;")) > 5]
            checked += 1
            ok = any(all(norm(p) in norm(rows.get(g, "")) for p in parts) for g in group)
            if not ok:
                print(f"CHECK not in {group}: “{q[:100]}”"); bad += 1
print("ids:", len(ids), "fragments checked:", checked, "problems:", bad)
