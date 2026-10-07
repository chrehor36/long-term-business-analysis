"""Strip an EDGAR .htm to plain text (one line per block). Usage: python -I strip.py IN.htm OUT.txt"""
import sys, re, html

raw = open(sys.argv[1], encoding="utf-8", errors="replace").read()
raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
raw = re.sub(r"(?i)</(p|div|tr|li|h\d|table|br)\s*>|<br\s*/?>", "\n", raw)
raw = re.sub(r"(?i)</t[dh]\s*>", " | ", raw)
txt = re.sub(r"(?s)<[^>]+>", " ", raw)
txt = html.unescape(txt).replace("\xa0", " ")
lines = [re.sub(r"[ \t]+", " ", l).strip(" |") for l in txt.split("\n")]
lines = [l for l in lines if l.strip()]
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(lines))
print(len(lines), "lines")
