"""Strip an HTML filing to text. Usage: python html2txt.py IN OUT (paths in cache/)."""
import sys, re, html, os
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
s = open(os.path.join(d, sys.argv[1]), encoding="utf-8", errors="replace").read()
s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
s = re.sub(r"(?i)</td>", " | ", s)
s = re.sub(r"<[^>]+>", " ", s)
s = html.unescape(s).replace("\xa0", " ")
s = re.sub(r"[ \t]+", " ", s)
s = re.sub(r"\n\s*\n+", "\n", s)
open(os.path.join(d, sys.argv[2]), "w", encoding="utf-8").write(s)
print(len(s))
