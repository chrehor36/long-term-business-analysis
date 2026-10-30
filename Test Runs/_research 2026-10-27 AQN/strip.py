import sys, re, html
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8", errors="replace").read()
t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", t)
t = re.sub(r"(?i)</td>|</th>", " | ", t)
t = re.sub(r"<[^>]+>", " ", t)
t = html.unescape(t)
t = re.sub(r"[ \t\xa0]+", " ", t)
t = re.sub(r"\n\s*\n+", "\n", t)
open(dst, "w", encoding="utf-8").write(t)
print(dst, len(t))
