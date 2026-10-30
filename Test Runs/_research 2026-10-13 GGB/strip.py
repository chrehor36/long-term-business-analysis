import sys, re, html
src, dst = sys.argv[1], sys.argv[2]
raw = open(src, "rb").read()
try:
    t = raw.decode("utf-8")
except UnicodeDecodeError:
    t = raw.decode("cp1252", errors="replace")
t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
t = re.sub(r"(?i)</td>|</th>", "\x01", t)
t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", t)
t = re.sub(r"<[^>]+>", " ", t)
t = html.unescape(t).replace("\u200b", " ").replace("\xa0", " ")
out = []
for line in t.split("\n"):
    if "\x01" in line:
        cells = [c.strip() for c in line.split("\x01")]
        cells = [c for c in cells if c and c not in ("$", "R$", "%", ")")]
        line = " | ".join(cells)
    line = re.sub(r"[ \t]+", " ", line).strip()
    if line:
        out.append(line)
open(dst, "w", encoding="utf-8").write("\n".join(out))
print(dst, len(out))
