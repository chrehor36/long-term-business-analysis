import sys, re, html
from fetch import get
def totext(url, out):
    raw = get(url).decode("utf-8", "ignore")
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", raw)
    raw = re.sub(r"(?i)</td>|</th>", " | ", raw)
    raw = re.sub(r"<[^>]+>", "", raw)
    t = html.unescape(raw).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    open(out, "w", encoding="utf-8").write(t)
    print(out, len(t))
if __name__ == "__main__":
    totext(sys.argv[1], sys.argv[2])
