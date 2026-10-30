"""Dispatcher check: for each bold id, every double-quoted fragment in the 400 characters before it (same paragraph) must be in that row."""
import csv, re
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
run = open(ROOT + r"\Test Runs\2026-10-16 Run - CTBG Coil Tubing Technology.md", encoding="utf-8").read()
rows = {r[0]: r[2] for r in csv.reader(open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8-sig"))}
def norm(s):
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u2014", "-"), ("\u2013", "-")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()
n = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run):
    i = m.group(1); start = max(0, m.start() - 400)
    ctx = run[start:m.start()]
    ctx = ctx.split("\n\n")[-1]
    prev = list(re.finditer(r"\*\*\[[MLR]\d{4}-\d{3}\]\*\*", ctx))
    if prev: ctx = ctx[prev[-1].end():]
    for q in re.findall(r'["\u201c]([^"\u201d]{4,})["\u201d]', ctx):
        for part in re.split(r"\[\.\.\.\]|\.\.\.", q):
            p = norm(part).strip(" .,;:'")
            if p and p not in norm(rows.get(i, "MISSING")):
                print("SLIP?", i, "|", part[:120]); n += 1
print("ids:", len(re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)), "possible slips:", n)
