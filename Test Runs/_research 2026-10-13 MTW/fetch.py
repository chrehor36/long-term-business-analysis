"""Fetch SEC documents into cache/ and strip HTML to text. Usage: fetch.py URL OUTNAME"""
import sys, re, html, time, pathlib, urllib.request, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url):
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
                return data
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(2)
    raise SystemExit("fail " + url)
def totext(b):
    s = b.decode("utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    url, out = sys.argv[1], sys.argv[2]
    d = pathlib.Path(__file__).parent / "cache"
    b = get(url)
    p = d / out
    if out.endswith(".json"):
        p.write_bytes(b)
    else:
        p.write_text(totext(b), encoding="utf-8")
    print(p, p.stat().st_size)
