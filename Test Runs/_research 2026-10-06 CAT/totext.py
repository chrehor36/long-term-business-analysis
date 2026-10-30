"""Strip an EDGAR .htm filing to plain text. Usage: python totext.py in.htm out.txt"""
import sys, re, html

raw = open(sys.argv[1], encoding="utf-8", errors="replace").read()
raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
raw = re.sub(r"(?i)</(p|div|tr|br|li|h\d)>", "\n", raw)
raw = re.sub(r"(?i)<br\s*/?>", "\n", raw)
raw = re.sub(r"(?i)</t[dh]>", " | ", raw)
txt = re.sub(r"(?s)<[^>]+>", "", raw)
txt = html.unescape(txt).replace("\xa0", " ")
txt = re.sub(r"[ \t]+", " ", txt)
txt = re.sub(r"\n\s*\n+", "\n", txt)
open(sys.argv[2], "w", encoding="utf-8").write(txt)
print(sys.argv[2], len(txt))
