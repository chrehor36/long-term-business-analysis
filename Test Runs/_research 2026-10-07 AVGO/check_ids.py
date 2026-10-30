# check: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment in the same sentence-span as an id is in that row.
import csv, re, sys, unicodedata
RUN = "Test Runs/2026-10-07 Run - AVGO Broadcom.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
def norm(s): return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s).replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().lower()
probs = 0; CHECKED = []
for e in re.findall(r"\[E\d+-\d+\]", text): print("E-id found:", e); probs += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); probs += 1
# fragments: for each id occurrence, take quoted strings in the preceding 400 chars of the same paragraph that are not already claimed
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text):
    i = m.group(1); start = max(text.rfind("\n\n", 0, m.start()), text.rfind("**[", 0, m.start()-1), 0)
    seg = text[start:m.start()]
    # restrict to the sentence carrying the id: mask quoted text, then cut at the last sentence break outside quotes
    masked = re.sub(r"“[^”]*”|\"[^\"]*\"", lambda q: "Q" * len(q.group(0)), seg)
    cuts = [b.end() for b in re.finditer(r"[.;)]\s+(?=[A-Z(*])", masked[:-3])]
    if cuts: seg = seg[cuts[-1]:]
    for q in re.findall(r"“([^”]{6,})”|\"([^\"]{6,})\"", seg):
        frag = q[0] or q[1]
        parts = [p for p in re.split(r"\s*\[\.\.\.\]\s*", frag) if p.strip()]
        row = norm(rows.get(i, ""))
        CHECKED.append(i)
        if not all(norm(p) in row for p in parts):
            print(f"FRAGMENT not in {i}: {frag[:90]}"); probs += 1
print("ids cited:", len(set(ids)), "fragments checked:", len(CHECKED), "problems:", probs)
