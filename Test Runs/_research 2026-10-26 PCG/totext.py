"""usage: totext.py in.htm out.txt  -- crude html to text"""
import sys, re, html
t = open(sys.argv[1], encoding="utf-8", errors="ignore").read()
t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
t = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", t)
t = re.sub(r"(?i)<br\s*/?>", "\n", t)
t = re.sub(r"(?i)</t[dh]>", " | ", t)
t = re.sub(r"<[^>]+>", "", t)
t = html.unescape(t).replace("\xa0", " ")
t = re.sub(r"[ \t]+", " ", t)
t = re.sub(r"\n\s*\n+", "\n", t)
open(sys.argv[2], "w", encoding="utf-8").write(t)
print(sys.argv[2], len(t))
