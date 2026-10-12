"""Fetch a URL from SEC EDGAR into the cache folder; optionally convert HTML to text."""
import sys, os, re, time, urllib.request, html, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    for i in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
                return data
        except Exception as e:
            print("retry", i, e, file=sys.stderr); time.sleep(2 + 3 * i)
    raise SystemExit("failed " + url)
def to_text(b):
    s = b.decode("utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>|</th>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    url, out = sys.argv[1], sys.argv[2]
    data = get(url)
    if out.endswith(".txt") and not url.endswith(".txt") and not url.endswith(".json"):
        open(out, "w", encoding="utf-8").write(to_text(data))
    else:
        open(out, "wb").write(data)
    print("wrote", out, len(data))
