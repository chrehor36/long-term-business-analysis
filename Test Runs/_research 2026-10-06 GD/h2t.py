"""Convert an HTML filing in cache/ to plain text in cache/. Usage: python h2t.py IN.htm OUT.txt"""
import sys, re, html, os
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
s = open(os.path.join(base, sys.argv[1]), encoding="utf-8", errors="replace").read()
s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
s = re.sub(r"(?i)</td>", " | ", s)
s = re.sub(r"<[^>]+>", " ", s)
s = html.unescape(s)
s = re.sub(r"[ \t\xa0]+", " ", s)
s = re.sub(r"\n\s*\n+", "\n", s)
s = re.sub(r"(\| )+\|", "|", s)
open(os.path.join(base, sys.argv[2]), "w", encoding="utf-8").write(s)
print(len(s))
