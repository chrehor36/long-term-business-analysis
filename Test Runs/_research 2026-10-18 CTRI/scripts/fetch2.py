import sys, re, html
sys.path.insert(0, sys.argv[0].rsplit("/",1)[0])
from fetch import get
def cell(t):
    t = re.sub(r"<[^>]+>", " ", t); t = html.unescape(t)
    return re.sub(r"[\s\xa0]+", " ", t).strip()
def strip(b):
    t = b.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    def tr(m):
        cells = [cell(c) for c in re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", m.group(0))]
        cells = [c for c in cells if c not in ("", "$", ")", "%")]
        return "\n" + " | ".join(cells) + "\n"
    t = re.sub(r"(?is)<tr[^>]*>.*?</tr>", tr, t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t); t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
    return t
if __name__ == "__main__":
    open(sys.argv[2], "w", encoding="utf-8").write(strip(get(sys.argv[1]))); print(sys.argv[2])
