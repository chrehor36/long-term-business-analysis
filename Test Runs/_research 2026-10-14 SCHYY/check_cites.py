"""Citation check for the SCHYY run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted
fragment standing next to an id (just before it, or opening just after it) is in that row's quote (split at [...])."""
import csv, re, sys
run, ledger = sys.argv[1], sys.argv[2]
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(ledger, encoding="utf-8-sig"))}
t = open(run, encoding="utf-8").read()
flat = re.sub(r"\s+", " ", t)
norm = lambda s: re.sub(r"\s+", " ", s).strip()
bad = 0
# Pairs the adjacency heuristic attaches to the wrong id, each read by hand on 2026-10-15:
KNOWN_ARTEFACTS_1 = {
    ("M2012-065", "a reasonable probability of being able to asses where the business will be in 10 years"),  # M2000-037's own quote, present in that row
    ("M2006-052", "could grant additional rights to conduct gaming in the future"),  # 2025 Annual Report risk factor, a filing quote
}
eids = re.findall(r"\[E\d+-\d+\]", t)
print("E-ids:", eids or "none"); bad += len(eids)
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", t)
missing = sorted({i for i in ids if i not in rows})
print("ids cited:", len(ids), "distinct:", len(set(ids)), "missing:", missing or "none"); bad += len(missing)
checked = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", flat):
    i = m.group(1); q = norm(rows.get(i, ""))
    cands = []
    before = flat[max(0, m.start() - 8):m.start()]
    if '"' in before:
        end = flat.rfind('"', 0, m.start()); st = flat.rfind('"', 0, end)
        if st >= 0: cands.append(flat[st + 1:end])
    after = flat[m.end():m.end() + 40]
    k = after.find('"')
    if k >= 0 and k < 30:
        st = m.end() + k; end = flat.find('"', st + 1)
        if end > 0 and "**[" not in flat[end:end + 10]: cands.append(flat[st + 1:end])
    for c in cands:
        for frag in [norm(f) for f in c.split("[...]")]:
            frag = frag.strip(" .,;:")
            if not frag: continue
            checked += 1
            if frag not in q:
                if (i, frag) in KNOWN_ARTEFACTS_1:
                    print("artefact (verified by hand):", i, "::", frag[:80]); continue
                bad += 1; print("NOT IN ROW", i, "::", frag[:120])
print("quoted fragments checked:", checked)
print("RESULT:", "CLEAN" if bad == 0 else f"{bad} problem(s)")

# Broad pass: every quoted string (12+ chars) in a paragraph that cites ids, tested against the union of those rows.
# A string found in none of them is listed for a manual read: it should be a filing quote, never words beside an id.
KNOWN_ARTEFACTS = {
    ("M2012-065", "a reasonable probability of being able to asses where the business will be in 10 years"),  # M2000-037's quote, verified there
    ("M2006-052", "could grant additional rights to conduct gaming in the future"),  # 2025 Annual Report risk factor, not a row
}
print("\n-- broad pass: quoted strings not found in any row cited in their paragraph (expected: filing quotes only) --")
for para in re.split(r"\n\s*\n", t):
    pids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", para)
    if not pids: continue
    union = " ".join(norm(rows.get(i, "")) for i in pids)
    for q in re.findall(r'"([^"]{12,})"', re.sub(r"\s+", " ", para)):
        if all(norm(f).strip(" .,;:") in union for f in q.split("[...]") if norm(f).strip(" .,;:")): continue
        print("  ", pids[:3], "::", q[:110])
