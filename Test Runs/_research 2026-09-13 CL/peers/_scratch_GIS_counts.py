import re, glob, sys
sys.stdout.reconfigure(encoding="utf-8")
pats = {"Colgate": r"colgate", "Hill": r"hill", "Purina": r"purina", "Nestl": r"nestl", "Mars": r"mars", "Blue Buffalo": r"blue buffalo", "Hill's": r"hill['’]s", "Walmart": r"wal-?mart"}
for t in ["GIS", "SJM", "FRPT"]:
    for f in sorted(glob.glob(f"{t}_10*.txt")):
        s = open(f, encoding="utf-8").read()
        row = []
        for k, p in pats.items():
            ms = list(re.finditer(p, s, re.I))
            words = sorted(set(re.search(r"\w*" + p + r"\w*", s[max(0,m.start()-20):m.end()+20], re.I).group(0) for m in ms)) if ms else []
            row.append(f"{k}={len(ms)} {words[:8]}")
        print(f, " | ".join(row))
