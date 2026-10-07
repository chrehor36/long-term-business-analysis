"""Fetch every exhibit .htm of CL's 8-Ks since 2023 whose name the first pass's EX-99 regex missed."""
import os, re, json
import fetch as F
HERE = os.path.dirname(os.path.abspath(__file__))
sub = json.load(open(os.path.join(HERE, "submissions.json"), encoding="utf-8"))["filings"]["recent"]
for f, fd, acc, doc, it in zip(sub["form"], sub["filingDate"], sub["accessionNumber"], sub["primaryDocument"], sub["items"]):
    if not f.startswith("8-K") or fd < "2023-07-01":
        continue
    names = F.exhibits(acc)
    for n in names:
        if not n.lower().endswith(".htm") or n == doc or re.match(r"R\d+\.htm", n) or "index" in n:
            continue
        F.grab(acc, n, f"EX_{fd}_{acc[-6:]}_{re.sub(r'[^A-Za-z0-9]', '', n)[:40]}")
