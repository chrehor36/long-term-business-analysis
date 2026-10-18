# Dispatcher's citation check at the fold: every quoted fragment within 300 chars before a v5 id must be in that row.
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
root = r"C:/Users/chreh/OneDrive/Documents/BRK/"
L = {r[0]: r[2] for r in csv.reader(open(root + "principle_ledger_v5.csv", encoding="utf-8"))}
t = open(root + "Test Runs/2026-10-17 Run - BLGO BioLargo.md", encoding="utf-8").read()
n = lambda s: re.sub(r"\s+", " ", s.replace("\u201c", '"').replace("\u201d", '"').replace("\u2019", "'")).lower()
T = n(t); checked = 0; flags = 0
for m in re.finditer(r"\[([mlr]\d{4}-\d{3})\]", T):
    i = m.group(1).upper(); row = n(L.get(i, ""))
    if not row: print("MISSING", i); flags += 1; continue
    win = T[max(0, m.start() - 300):m.start()]
    win = win.split("**[")[-1] if "**[" in win else win
    for q in re.findall(r'"([^"]{5,})"', win):
        for p in q.split("[...]"):
            p = p.strip(" .,;:")
            if len(p) < 5: continue
            checked += 1
            if p not in row: print("FLAG", i, "::", p[:150]); flags += 1
print("fragments checked:", checked, "flags:", flags)
