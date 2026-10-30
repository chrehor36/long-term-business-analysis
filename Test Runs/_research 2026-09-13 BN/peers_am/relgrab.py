"""Grab one exhibit document and print margin / fee-rate hits.
usage: relgrab.py TICKER ACCESSION DOC NAME"""
import sys, os, re
from fetch import grab, OUT

tk, acc, doc, name = sys.argv[1:5]
grab(tk, acc, doc, name)
t = re.sub(r"\s+", " ", open(os.path.join(OUT, name + ".txt"), encoding="utf-8").read())
pat = sys.argv[5] if len(sys.argv) > 5 else r"FRE margin|fee[- ]related earnings margin|margin"
for m in list(re.finditer(pat, t, re.I))[:8]:
    print("  >", t[max(0, m.start() - 250):m.end() + 250].encode("ascii", "replace").decode())
