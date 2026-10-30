import sys, re, html, os
from fetch import get
def totext(url, name):
    p = get(url, name + ".htm")
    out = p[:-4] + ".txt"
    if os.path.exists(out): return out
    s = open(p, encoding="utf-8", errors="replace").read()
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", s)
    s = re.sub(r"(?i)</(p|div|tr|br|h\d|li)>", "\n", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    open(out, "w", encoding="utf-8").write(s)
    return out
if __name__ == "__main__":
    print(totext(sys.argv[1], sys.argv[2]))
