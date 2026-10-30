import re, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
F = {
    "F21": "PG_10K_FY2021_2021-06-30.txt",
    "F22": "PG_10K_FY2022_2022-06-30.txt",
    "F23": "PG_10K_FY2023_2023-06-30.txt",
    "F24": "PG_10K_FY2024_2024-06-30.txt",
    "F25": "PG_10K_FY2025_2025-06-30.txt",
    "F26": "PG_10K_FY2026_2026-06-30.txt",
}
cache = {}
def lines(k):
    if k not in cache:
        cache[k] = open(F[k], encoding="utf-8").read().split("\n")
    return cache[k]

def rep(m):
    parts = m.group(1).split("~~")
    kind, k, n = parts[0], parts[1], int(parts[2])
    L = lines(k)[n].strip()
    if kind == "L":
        q = L
    else:
        s, e = parts[3], parts[4]
        i = L.find(s)
        if i < 0:
            raise SystemExit(f"start not found {parts}")
        j = L.find(e, i)
        while j >= 0 and j + len(e) < i + len(s):
            j = L.find(e, j + 1)
        if j < 0:
            raise SystemExit(f"end not found {parts}")
        q = L[i:j + len(e)]
    return f"> {q}\nSource: {F[k]} line {n}"

T = open("_scratch_PG_tmpl.py", encoding="utf-8").read()
T = T.split('"""', 2)[1]
out = re.sub(r"@@(.+?)@@", rep, T)
open("SECTION_PG.md", "w", encoding="utf-8", newline="\n").write(out)
print("written", len(out))
