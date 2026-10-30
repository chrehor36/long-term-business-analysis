import sys, re, html
def cell_text(s):
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    return re.sub(r"\s+", " ", s).strip()
def row(m):
    cells = re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", m.group(0))
    cells = [cell_text(c) for c in cells]
    cells = [c for c in cells if c not in ("", "$", "%", ")")]
    return "\n" + " | ".join(cells) + "\n"
def strip(src, dst):
    t = open(src, encoding="utf-8", errors="replace").read()
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?is)<ix:header.*?</ix:header>", " ", t)
    t = t.replace("\n", " ")
    t = re.sub(r"(?is)<tr[^>]*>.*?</tr>", row, t)
    t = re.sub(r"(?i)<br\s*/?>|</(p|div|li|h\d|table)>", "\n", t)
    t = re.sub(r"(?s)<[^>]+>", "", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    open(dst, "w", encoding="utf-8").write(t)
for a in sys.argv[1:]:
    strip(a, a.rsplit(".",1)[0]+".txt")
