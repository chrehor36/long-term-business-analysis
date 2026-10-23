import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
run, ledger = sys.argv[1], sys.argv[2]
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(ledger, encoding="utf-8-sig"))}
t = open(run, encoding="utf-8").read()
def norm(x): return re.sub(r"[^a-z0-9]", "", x.lower().replace("�", ""))
probs = 0
ids = re.findall(r"\*\*\[([A-Z]+\d{4}-\d{3})\]\*\*", t)
eids = re.findall(r"\[E\d+-\d+\]", t)
if eids: print("E-ids found:", eids); probs += len(eids)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); probs += 1
checked = 0
# a quoted fragment ending within 15 characters before an id: "...." **[ID]**
for m in re.finditer(r"\*\*\[([A-Z]+\d{4}-\d{3})\]\*\*", t):
    before = t[max(0, m.start()-15):m.start()]
    if not re.search(r"[\"”]\s*[).,;:]?\s*$", before): continue
    end = m.start() - len(before) + max(before.rfind('"'), before.rfind("”"))
    # walk back to the opening quote of this fragment (balanced on straight quotes inside allowed: take the nearest opening quote
    # that starts a quotation: preceded by space, colon, parenthesis or line start)
    seg = t[:end]
    k = max(seg.rfind(' "'), seg.rfind('\n"'), seg.rfind('("'), seg.rfind(' “'), seg.rfind('“'))
    frag = t[k+1:end].lstrip('"“ ')
    if '"' in frag[:0]: pass
    row = norm(rows.get(m.group(1), ""))
    parts = [p for p in re.split(r"\[\.\.\.\]|\.\.\.", frag) if norm(p)]
    ok = all(norm(p) in row for p in parts)
    checked += 1
    if not ok:
        # retry: fragment may contain an inner quotation; take the text from the quote two back
        k2 = max(seg[:k].rfind(' "'), seg[:k].rfind('\n"'), seg[:k].rfind('("'))
        frag2 = t[k2+1:end].lstrip('"“ ')
        parts2 = [p for p in re.split(r"\[\.\.\.\]|\.\.\.", frag2) if norm(p)]
        ok = all(norm(p.replace('"','')) in row for p in parts2)
        if not ok:
            print("NOT IN ROW", m.group(1), "|", frag[:160]); probs += 1
print(f"ids cited: {len(set(ids))} distinct, {len(ids)} total; quoted fragments checked: {checked}; problems: {probs}")
