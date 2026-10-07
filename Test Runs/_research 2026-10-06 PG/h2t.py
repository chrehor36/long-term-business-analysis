"""Strip an EDGAR .htm filing to plain text (cache/<name>.txt). Usage: python h2t.py cache/file.htm"""
import sys, re, html

for p in sys.argv[1:]:
    raw = open(p, encoding="utf-8", errors="replace").read()
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", raw)
    raw = re.sub(r"(?i)</td>|</th>", " | ", raw)
    raw = re.sub(r"<[^>]+>", "", raw)
    txt = html.unescape(raw).replace("\xa0", " ")
    txt = re.sub(r"[ \t]+", " ", txt)
    txt = re.sub(r"\n\s*\n+", "\n", txt)
    out = p.rsplit(".", 1)[0] + ".txt"
    open(out, "w", encoding="utf-8").write(txt)
    print(out, len(txt))
