"""Fetch an EDGAR URL to cache/ with the SEC User-Agent; optionally strip HTML to text (tables one row per line)."""
import sys, os, re, time, urllib.request, html, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
CACHE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cache")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
                return data
        except Exception as e:
            print("retry", e, file=sys.stderr)
            time.sleep(2)
    raise SystemExit("failed " + url)


def _row(m):
    cells = re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", m.group(0))
    out = []
    for c in cells:
        c = html.unescape(re.sub(r"<[^>]+>", " ", c))
        c = re.sub(r"\s+", " ", c).strip()
        if c in ("%", ")") and out:
            out[-1] += c
        elif c and c != "$":
            out.append(c)
    return "\n" + " | ".join(out) + "\n"


def totext(b):
    s = b.decode("utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?is)<tr[^>]*>.*?</tr>", _row, s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</h\d>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s


if __name__ == "__main__":
    url, name = sys.argv[1], sys.argv[2]
    b = get(url)
    out = os.path.join(CACHE, name)
    if name.endswith(".txt"):
        open(out, "w", encoding="utf-8").write(totext(b))
    else:
        open(out, "wb").write(b)
    print(out, os.path.getsize(out))
