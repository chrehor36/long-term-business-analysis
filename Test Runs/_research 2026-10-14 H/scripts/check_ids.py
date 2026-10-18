"""Citation check for the H run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every quoted fragment in the same sentence-clause before an id is found in that row."""
import csv, re, sys, unicodedata
RUN = "Test Runs/2026-10-14 Run - H Hyatt Hotels.md"
rows = {}
for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig")):
    rows[r["id"]] = r["quote_verbatim"]
text = open(RUN, encoding="utf-8").read()
def norm(s):
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
allids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
for i in sorted(set(allids)):
    if i not in rows: print("MISSING id", i); bad += 1
# fragments: for each id occurrence, take the text since the previous id or line start, find "..." quotes
checked = 0
for line in text.splitlines():
    pos = 0
    for m in re.finditer(r"\[([MLR]\d{4}-\d{3})\]", line):
        seg = line[pos:m.start()]
        pos = m.end()
        # only quotes immediately governing this id: the last quoted run(s) in the segment after the last ';' or '.'
        frags = re.findall(r"“([^”]+)”|\"([^\"]+)\"", seg)
        if not frags: continue
        # take only the last fragment(s) in the segment (those adjacent to the id)
        tail = re.split(r"(?<=[;.])\s(?=[A-Z(*])", seg)[-1]
        tf = re.findall(r"\"([^\"]+)\"", tail)
        for f in tf:
            parts = [p.strip(" .,") for p in f.split("[...]")]
            row = norm(rows.get(m.group(1), ""))
            for p in parts:
                if not p: continue
                checked += 1
                if norm(p) not in row:
                    print(f"FRAGMENT NOT IN {m.group(1)}: {p[:90]!r}")
                    bad += 1
print(f"ids cited: {len(set(allids))} distinct, {len(allids)} total; fragments checked: {checked}; problems: {bad}")
sys.exit(1 if bad else 0)
