# Extract the first (Digital Realty Trust, Inc.) cash-flow statement, income statement and balance sheet from a 10-K text
import sys, re, subprocess, os
sys.stdout.reconfigure(encoding="utf-8")
f = sys.argv[1]
L = open(f, encoding="utf-8").read().split("\n")
def find(pat, start=0):
    for i in range(start, len(L)):
        if re.search(pat, L[i]): return i
    return None
# skip table of contents: find statement heading after 'ITEM 8' region
i8 = find(r"(?i)report of independent registered public accounting firm")
for name, pat, span in [("BS", r"^\s*CONSOLIDATED BALANCE SHEETS\s*$", 700), ("IS", r"^\s*CONSOLIDATED (INCOME STATEMENTS|STATEMENTS OF OPERATIONS)\s*$", 700), ("CF", r"^\s*CONSOLIDATED STATEMENTS OF CASH FLOWS\s*$", 900)]:
    i = find(pat, i8 or 0)
    if i is None: print(name, "NOT FOUND"); continue
    out = subprocess.run([sys.executable, "rows.py", f, str(i+1), str(i+span)], capture_output=True, text=True, encoding="utf-8").stdout
    # stop at 'See accompanying'
    k = out.find("See accompanying")
    print("=====", name, "line", i+1); print(out[:k if k > 0 else 20000])
