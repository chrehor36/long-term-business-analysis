# Check for the WAB run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# placed immediately before an id (the pattern "fragment" **[ID]**) is in that row's quote (elisions [...] split).
import csv, re, sys
RUN = "Test Runs/2026-10-16 Run - WAB Wabtec.md"
LEDGER = "principle_ledger_v5.csv"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(LEDGER, encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s).strip()
bad = []
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids: bad.append(f"E-ids present: {eids}")
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
for i in sorted(set(ids)):
    if i not in rows: bad.append(f"missing id {i}")
# quoted fragment immediately before an id: "..." optional punctuation/space, then **[ID]** (possibly a run of ids)
pat = re.compile(r"[\"“]([^\"“”]{3,600}?)[\"”][\s,.;:)]*(?:\([^)]*\)\s*)?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)")
checked = 0
for m in pat.finditer(text):
    frag = m.group(1)
    fid = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))
    pieces = [norm(p).strip(" .,;:") for p in re.split(r"\[\.\.\.\]|\.\.\.", frag) if norm(p).strip(" .,;:")]
    ok = False
    for i in fid:
        q = norm(rows.get(i, ""))
        if all(p in q for p in pieces):
            ok = True; break
    checked += 1
    if not ok:
        bad.append(f"fragment not in {fid}: {frag[:120]!r}")
print(f"ids cited: {len(set(ids))} distinct, {len(ids)} total; fragments checked: {checked}")
if bad:
    print("FAIL"); print("\n".join(bad)); sys.exit(1)
print("check_ids PASS")
