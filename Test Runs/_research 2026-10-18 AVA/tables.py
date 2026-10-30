import sys, re, html

src, out = sys.argv[1], sys.argv[2]
h = open(src, encoding="utf-8", errors="replace").read()
h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
lines = []
pos = 0
for m in re.finditer(r"(?is)<table.*?</table>", h):
    pre = h[pos:m.start()]
    t = re.sub(r"<[^>]+>", " ", pre)
    t = re.sub(r"\s+", " ", html.unescape(t)).strip()
    if t:
        lines.append(t[-400:])
    pos = m.end()
    lines.append("### TABLE")
    for tr in re.findall(r"(?is)<tr.*?</tr>", m.group(0)):
        cells = []
        for td in re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", tr):
            s = re.sub(r"<[^>]+>", " ", td)
            s = re.sub(r"\s+", " ", html.unescape(s)).strip()
            if s in ("", "$", ")", "%", ")%"):
                if s.startswith(")") and cells:
                    cells[-1] = cells[-1] + ")"
                continue
            cells.append(s)
        if cells:
            lines.append(" | ".join(cells))
open(out, "w", encoding="utf-8").write("\n".join(lines))
print(len(lines))
