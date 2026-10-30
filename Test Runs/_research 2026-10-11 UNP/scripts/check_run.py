"""Check the UNP run file: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment that ends just before an
id (within a few characters) is found verbatim in that row (fragments split at [...]). Prints failures for review."""
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RUN = "Test Runs/2026-10-11 Run - UNP Union Pacific.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
eids = re.findall(r"\[E\d+-\d+\]", text)
print("E-ids:", eids or "none")
ids = re.findall(r"\*\*\[([A-Z]\d{4}-\d{3})\]\*\*", text)
missing = sorted({i for i in ids if i not in rows})
print(f"ids cited: {len(ids)} occurrences, {len(set(ids))} distinct; missing from ledger: {missing or 'none'}")
bad_prefix = sorted({i for i in ids if i[0] not in 'MLR'})
print("ids with a prefix other than M, L, R:", bad_prefix or "none")
norm = lambda x: re.sub(r"\s+", " ", x).strip()
checked = ok = 0
fails = []
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text):
    i = m.group(1)
    before = text[max(0, m.start() - 1200):m.start()]
    tail = before.rstrip(" ,;:(")
    tail = re.sub(r"\(\s*[^()]*\)\s*$", "", tail).rstrip(" ,;:")  # allow a parenthesis between quote and id
    if not tail.endswith('"'):
        continue
    # find the opening quote: the last '"' preceded by start, space, '(' or '—' such that pairing holds
    body = tail[:-1]
    k = len(body)
    start = None
    for j in range(k - 1, -1, -1):
        if body[j] == '"' and (j == 0 or body[j - 1] in " (\n:"):
            start = j
            # nested quotes: keep going if the count of quotes inside is odd
            inner = body[j + 1:]
            if inner.count('"') % 2 == 0:
                break
    if start is None:
        continue
    frag = body[start + 1:]
    checked += 1
    row = norm(rows.get(i, ""))
    pieces = [norm(p) for p in frag.split("[...]") if norm(p)]
    good = all(p.strip(' .,;') in row for p in pieces)
    if good:
        ok += 1
    else:
        fails.append((i, frag[:160]))
print(f"quoted fragments checked: {checked}; verbatim in row: {ok}; to review: {len(fails)}")
for i, f in fails:
    print("  REVIEW", i, "|", f)
