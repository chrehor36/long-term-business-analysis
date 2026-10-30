import sys, re, html
src, out = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8", errors="replace").read()
t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", t)
t = re.sub(r"(?i)</td>|</th>", " | ", t)
t = re.sub(r"<[^>]+>", "", t)
t = html.unescape(t).replace("\xa0", " ")
t = re.sub(r"[ \t]+", " ", t)
t = re.sub(r"\n\s*\n+", "\n", t)
open(out, "w", encoding="utf-8").write(t)
print(out, len(t))
