# Check the run file: no E-ids; every M/L/R id is in principle_ledger_v5.csv; every quoted fragment that stands
# immediately before an id (the "..." or “...” nearest before the bold id, on the same paragraph) is in that row.
import csv, re, sys
RUN = "Test Runs/2026-10-23 Run - NEE NextEra Energy.md"
rows = {x["id"]: x["quote_verbatim"] for x in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
print("E-ids:", eids or "none"); bad += len(eids)
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
print("ids cited:", len(ids), "distinct:", len(set(ids)))
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING ID", i); bad += 1
# quoted fragments: for each id occurrence, the last quote ending within 25 characters before it;, take the paragraph text before it back to the previous id or paragraph start,
# and check every double-quoted fragment there against the row(s) cited in that same stretch.
paras = re.split(r"\n\s*\n", text)
def frags(seg):
    out = []
    for m in re.finditer(r"\"([^\"]{6,}?)\"|“([^”]{6,}?)”", seg):
        out.append(m.group(1) or m.group(2))
    return out
def norm(s):
    return re.sub(r"\s+", " ", s).strip()
checked = 0
for para in paras:
    p = norm(para)
    pos = 0
    for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*((?:,? ?\*\*\[[MLR]\d{4}-\d{3}\]\*\*)*)", p):
        group = [m.group(1)] + re.findall(r"\[([MLR]\d{4}-\d{3})\]", m.group(2) or "")
        seg = p[pos:m.start()]
        pos = m.end()
        last = list(re.finditer(r"\"([^\"]{6,}?)\"|“([^”]{6,}?)”", seg))
        if not last: continue
        lm = last[-1]
        if len(seg) - lm.end() > 25: continue      # the quote is not beside the id
        for f in [lm.group(1) or lm.group(2)]:
            parts = [x.strip() for x in f.split("[...]") if x.strip()]
            ok = all(any(norm(x) in norm(rows.get(g, "")) for g in group) for x in parts)
            checked += 1
            if not ok:
                print(f"NOT IN ROW {group}: \"{f[:120]}\"")
                bad += 1
print("fragments checked:", checked)
print("RESULT:", "PASS" if bad == 0 else f"FAIL ({bad})")
