"""Strip cached filings (HTML) to text under cache/. Usage: python totext.py file.htm [...]  -> cache/file.txt"""
import sys, os, re, html

HERE = os.path.dirname(os.path.abspath(__file__))


def strip(raw):
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", raw)
    raw = re.sub(r"(?i)</td>|</th>", " | ", raw)
    raw = re.sub(r"(?s)<[^>]+>", "", raw)
    raw = html.unescape(raw).replace("\xa0", " ")
    raw = re.sub(r"[ \t]+", " ", raw)
    raw = re.sub(r"\n\s*\n+", "\n", raw)
    return raw


for a in sys.argv[1:]:
    p = os.path.join(HERE, "cache", a)
    t = strip(open(p, encoding="utf-8", errors="replace").read())
    out = os.path.splitext(p)[0] + ".txt"
    open(out, "w").write(t)
    print(out, len(t))
