"""Print the Non-Financial Services cash-flow block from each 20-F MD&A, flattened.
Transcription aid only: every figure used in the run is read off this printout, which is the filed text."""
import re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
files = sys.argv[1:] or ["20F_FY2021.txt", "20F_FY2022.txt", "20F_FY2023.txt", "20F_FY2024.txt", "20F_FY2025.txt", "20F_FY2026.txt"]
KEYS = r"(Cash flows from|Net cash|Depreciation|Additions|Purchases|Proceeds|Share-based|Changes in|Income taxes|Income tax|Interest|Dividends|Reissuance|Repurchase|Payments|Net income|Other, net|Effect|Cash and cash|Increase|Decrease|Share of|Provision|Loss|Gain|Deferred|Pension|Net change|Equity in|Accounts|Accrued|Inventories|Finance receivables|Year ended|\(Financial Services|\(Non-Financial|\(Consolidated)"
for fn in files:
    lines = open(os.path.join(HERE, fn), encoding="utf-8").read().split("\n")
    idx = [i for i, l in enumerate(lines) if re.search(r"Cash Flows on Non-Financial", l, re.I)]
    if not idx:
        idx = [i - 40 for i, l in enumerate(lines) if "(Non-Financial Services Businesses)" in l
               and any("Cash flows from operating activities" in x for x in lines[i:i + 80])]
    print("#" * 20, fn, idx[:5])
    if not idx:
        continue
    i0 = idx[0]
    block = " ".join(l.strip() for l in lines[i0:i0 + 1100] if l.strip() not in ("", "|"))
    block = re.sub(r" \| ", " ", block)
    block = re.sub(r"\s+", " ", block).replace(" )", ")")
    cut = block.find("Financial Position")
    block = block[:cut if cut > 0 else 12000]
    print(re.sub(KEYS, r"\n\1", block))
