"""Print an HTML filing with each table row on one line (cells joined by ' | '); prose kept. Usage: rows.py IN.htm OUT.txt"""
import sys, re, html
raw = open(sys.argv[1], encoding="utf-8").read()
raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    return re.sub(r"\s+", " ", s).strip()
out = []
pos = 0
for m in re.finditer(r"(?is)<tr\b.*?</tr>", raw):
    pre = raw[pos:m.start()]
    pre = re.sub(r"(?i)</p>|</div>|<br\s*/?>", "\n", pre)
    for line in clean_lines if False else re.split(r"\n", pre):
        c = clean(line)
        if c: out.append(c)
    cells = [clean(c) for c in re.findall(r"(?is)<t[dh]\b.*?</t[dh]>", m.group(0))]
    cells = [c for c in cells if c not in ("", "$", "HK$", "US$", ")", "%")]
    if cells: out.append(" | ".join(cells))
    pos = m.end()
tail = re.sub(r"(?i)</p>|</div>|<br\s*/?>", "\n", raw[pos:])
out += [clean(l) for l in tail.split("\n") if clean(l)]
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(out))
print(len(out))
