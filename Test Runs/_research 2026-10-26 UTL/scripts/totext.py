import sys, re, html
src, out = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8", errors="replace").read()
t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
def clean(s):
    s = re.sub(r"<[^>]+>", " ", s); s = html.unescape(s).replace("\xa0"," ")
    return re.sub(r"\s+", " ", s).strip()
def row(m):
    cells = re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", m.group(0))
    cells = [clean(c) for c in cells]
    cells = [c for c in cells if c not in ("", "$", ")", "%")]
    return "\n" + " | ".join(cells) + "\n"
t = re.sub(r"(?is)<tr[^>]*>.*?</tr>", row, t)
t = re.sub(r"(?i)<br\s*/?>", "\n", t)
t = re.sub(r"(?i)</(p|div|li|h\d)>", "\n", t)
t = re.sub(r"<[^>]+>", "", t)
t = html.unescape(t).replace("\xa0", " ")
t = re.sub(r"[ \t]+", " ", t)
t = re.sub(r"\n\s*\n+", "\n", t)
open(out, "w", encoding="utf-8").write(t)
print(out, len(t))
