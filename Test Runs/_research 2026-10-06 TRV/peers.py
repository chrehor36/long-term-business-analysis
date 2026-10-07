"""Fetch the competitors' 10-K filings (FY2025 and FY2022) for the competitor row, into cache/peers/,
and print the accession and the lines carrying the consolidated (or P&C) combined ratio.
Usage: python -I peers.py
"""
import json
import os
import re
import subprocess
import sys

PEERS = {"CB": 896159, "HIG": 874766, "CNA": 21175, "PGR": 80661, "WRB": 11544}
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from fetch import get  # noqa: E402


def tenks(cik):
    p = get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json", f"cache/peers/sub_{cik}.json")
    r = json.load(open(p))["filings"]["recent"]
    out = []
    for i in range(len(r["form"])):
        if r["form"][i] == "10-K":
            out.append((r["reportDate"][i], r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i]))
    return out


for t, cik in PEERS.items():
    ks = tenks(cik)
    for rd, fd, acc, doc in ks:
        if rd[:4] not in ("2025", "2022"):
            continue
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{doc}"
        h = get(url, f"cache/peers/{t}_{rd[:4]}.htm")
        txt = f"cache/peers/{t}_{rd[:4]}.txt"
        if not os.path.exists(txt):
            subprocess.run([sys.executable, "-I", os.path.join(HERE, "h2t.py"), h, txt], check=True,
                           stdout=subprocess.DEVNULL)
        print(f"== {t} 10-K period {rd} filed {fd} accession {acc}")
        n = 0
        for ln in open(txt, encoding="utf-8"):
            if re.search(r"^\|?\s*(Combined ratio|GAAP combined ratio|Combined ratio \(|Total combined ratio)", ln.strip(), re.I):
                print("   ", ln.strip()[:200])
                n += 1
                if n >= 6:
                    break
