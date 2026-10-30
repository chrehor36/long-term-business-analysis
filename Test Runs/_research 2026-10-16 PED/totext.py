"""Convert cached EDGAR htm to text with table rows on one line. Usage: totext.py NAME"""
import sys, re, html
name = sys.argv[1]
raw = open(f"cache/{name}.htm", encoding="utf-8").read()
raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
def clean(s):
    s = re.sub(r"<[^>]+>", " ", s); s = html.unescape(s)
    return re.sub(r"[\s\xa0]+", " ", s).strip()
def table(m):
    rows = []
    for tr in re.findall(r"(?is)<tr.*?</tr>", m.group(0)):
        cells = [clean(c) for c in re.findall(r"(?is)<t[dh].*?</t[dh]>", tr)]
        cells = [c for c in cells if c not in ("", "$", "%", ")")]
        if cells: rows.append(" | ".join(cells))
    return "\n[T] " + "\n[T] ".join(rows) + "\n" if rows else "\n"
raw = re.sub(r"(?is)<table.*?</table>", table, raw)
t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</h\d>", "\n", raw)
t = re.sub(r"<[^>]+>", " ", t); t = html.unescape(t)
t = re.sub(r"[ \t\xa0]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
open(f"cache/{name}.txt", "w", encoding="utf-8").write(t)
print(name, len(t))
