"""Verify every '> ' quote in SECTION_*.md / PEER_ROW.md is a verbatim substring of its Source file (whitespace-normalised),
and that the cited line number holds (part of) the quote. Also flag em dashes in prose. Checks only; no conclusions."""
import re, os, sys, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
norm = lambda s: re.sub(r"\s+", " ", s).strip()
files = sys.argv[1:] or sorted(glob.glob("SECTION_*.md"))
cache = {}
tot = bad = linebad = 0
for md in files:
    L = open(md, encoding="utf-8").read().split("\n")
    em = [i + 1 for i, l in enumerate(L) if "—" in l and not l.startswith("> ")]
    fails = []
    for i, l in enumerate(L):
        if not l.startswith("> "):
            continue
        q = l[2:]
        src = None
        for j in range(i + 1, min(i + 4, len(L))):
            m = re.match(r"\s*Source:\s*(\S+)\s+line[s]?\s+(\d+)", L[j])
            if m:
                src = m
                break
            if L[j].startswith("> "):
                break
        tot += 1
        if not src:
            # a multi-line quote block: accept if the next quote line carries the source
            k = i + 1
            while k < len(L) and L[k].startswith("> "):
                k += 1
            m = re.match(r"\s*Source:\s*(\S+)\s+line[s]?\s+(\d+)", L[k]) if k < len(L) else None
            if not m:
                fails.append((i + 1, "NO SOURCE LINE", q[:90]))
                bad += 1
                continue
            src = m
        fn, ln = src.group(1), int(src.group(2))
        if fn not in cache:
            if not os.path.exists(fn):
                fails.append((i + 1, f"SOURCE FILE MISSING {fn}", q[:90])); bad += 1; continue
            raw = open(fn, encoding="utf-8").read()
            cache[fn] = (norm(raw), raw.split("\n"))
        whole, lines = cache[fn]
        qn = norm(q)
        if qn not in whole:
            fails.append((i + 1, f"NOT VERBATIM in {fn}", q[:120])); bad += 1; continue
        window = norm(" ".join(lines[max(0, ln - 3): ln + 4]))
        probe = qn[:40]
        if probe not in window and norm(lines[ln] if ln < len(lines) else "")[:30] not in qn:
            fails.append((i + 1, f"line number off ({fn} line {ln})", q[:90])); linebad += 1
    print(f"{md}: quotes checked so far {tot}; failures in file {len(fails)}; em-dash prose lines {em[:10]}")
    for f in fails:
        print("   ", f)
print("TOTAL quotes", tot, "not verbatim/missing source", bad, "line-number mismatches", linebad)
