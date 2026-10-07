"""Convert a cached filing HTML to plain text in the cache folder (raw text stays gitignored).
Usage: python totext.py cache/IN.htm cache/OUT.txt"""
import sys, re, html
src = open(sys.argv[1], encoding="utf-8", errors="replace").read()
src = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", src)
src = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", src)
src = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", src)
src = re.sub(r"(?i)<br\s*/?>", "\n", src)
src = re.sub(r"(?i)</t[dh]>", " | ", src)
src = re.sub(r"(?s)<[^>]+>", " ", src)
src = html.unescape(src).replace("\xa0", " ")
lines = [re.sub(r"[ \t]+", " ", l).strip() for l in src.split("\n")]
lines = [l for l in lines if l and l.strip("| ")]
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(lines))
print(len(lines), "lines")
