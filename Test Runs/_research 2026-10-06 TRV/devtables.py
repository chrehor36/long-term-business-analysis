"""Parse the incurred-loss development tables (claims and allocated CAE, net of reinsurance, by accident year)
from a TRV 10-K text dump (made by h2t.py), and print for each table and accident year every incurred figure shown.
Usage: python -I devtables.py cache/k2025.txt
Output: one line per table and accident year: file|table|AY|initial|latest|n_years_shown|all values.
Only the incurred block is read; collection stops at the cumulative-paid block or the table total.
"""
import re
import sys

NUM = re.compile(r"\(\s*\d[\d,]*\s*\)|\d[\d,]*")
NAMES = ("General Liability", "Commercial Property", "Commercial Multi-Peril", "Commercial Automobile",
         "Workers’ Compensation", "Workers' Compensation", "Fidelity and Surety", "Automobile",
         "Homeowners (excluding Other)", "Homeowners and Other", "International - Canada", "International")
SEGS = ("Business Insurance", "Bond & Specialty Insurance", "Personal Insurance")


def nums(s):
    out = []
    for t in NUM.findall(s.replace("$", " ")):
        neg = t.strip().startswith("(")
        v = int(re.sub(r"[^\d]", "", t))
        out.append(-v if neg else v)
    return out


def clean(s):
    return s.strip().strip("|").strip()


def parse(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    res = []
    seg = ""
    heads = [i for i, ln in enumerate(lines) if "Incurred Claims and Allocated Claim" in ln]
    for i in heads:
        years = None
        for j in list(range(i - 1, max(i - 9, 0), -1)) + [i + 1, i + 2, i + 3]:
            ys = [int(y) for y in re.findall(r"\b(20\d\d)\b", lines[j])]
            run = ys[:1]
            for y in ys[1:]:
                if y == run[-1] + 1:
                    run.append(y)
                else:
                    break
            if len(run) >= 3:
                years = run
                break
        name = "?"
        for j in range(i - 1, max(i - 14, 0), -1):
            c = clean(lines[j])
            if c in NAMES:
                name = c
                for k in range(j - 1, max(j - 3, 0), -1):
                    if clean(lines[k]) in SEGS:
                        seg = clean(lines[k])
                break
        if name == "General Liability" and seg == "":
            seg = "Business Insurance"
        label = (seg + " / " if seg and name in ("General Liability",) else "") + name
        k = i + 1
        while k < len(lines):
            ln = lines[k]
            if ln.startswith("Total") or clean(ln).startswith("Total") or "Cumulative Paid" in ln:
                break
            m = re.match(r"^\|?\s*(20\d\d)\s*\|(.*)$", ln)
            if m and years:
                ay = int(m.group(1))
                n = len([y for y in years if y >= ay])
                v = nums(m.group(2))
                if n and len(v) >= n:
                    res.append((label, ay, v[0], v[n - 1], n, v[:n]))
            k += 1
    return res


if __name__ == "__main__":
    for p in sys.argv[1:]:
        for name, ay, a, b, n, vals in parse(p):
            print(f"{p}|{name}|{ay}|{a}|{b}|{n}|{' '.join(map(str, vals))}")
