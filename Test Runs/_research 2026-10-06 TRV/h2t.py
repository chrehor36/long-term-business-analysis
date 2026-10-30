"""Convert a cached EDGAR .htm into plain text (one line per block), for reading and grepping.
Usage: python -I h2t.py IN.htm OUT.txt
"""
import html
import re
import sys

raw = open(sys.argv[1], encoding="utf-8", errors="replace").read()
raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
raw = re.sub(r"(?i)</(p|div|tr|li|h\d|table|br)\s*>", "\n", raw)
raw = re.sub(r"(?i)<br\s*/?>", "\n", raw)
raw = re.sub(r"(?i)</t[dh]\s*>", " | ", raw)
raw = re.sub(r"(?s)<[^>]+>", " ", raw)
txt = html.unescape(raw).replace("\xa0", " ")
lines = []
for ln in txt.split("\n"):
    ln = re.sub(r"[ \t]+", " ", ln).strip()
    ln = re.sub(r"(\|\s*)+\|", "|", ln)
    if ln and ln != "|":
        lines.append(ln)
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(lines))
print(sys.argv[2], len(lines))
