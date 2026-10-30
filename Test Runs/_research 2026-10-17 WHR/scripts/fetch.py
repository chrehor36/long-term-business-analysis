"""Fetch an SEC URL to the cache folder, and optionally strip HTML to text."""
import sys, os, re, time, html, urllib.request, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
CACHE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cache")
def get(url):
    name = re.sub(r"[^A-Za-z0-9._-]", "_", url.split("://",1)[1])[-150:]
    path = os.path.join(CACHE, name)
    if not os.path.exists(path):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
        for i in range(4):
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    data = r.read()
                    if r.headers.get("Content-Encoding") == "gzip":
                        data = gzip.decompress(data)
                break
            except Exception as e:
                print("retry", e, file=sys.stderr); time.sleep(2)
        else:
            raise SystemExit("failed " + url)
        open(path, "wb").write(data)
        time.sleep(0.3)
    return path
def strip(path):
    t = open(path, "rb").read().decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>|</th>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    out = path + ".stripped.txt"
    open(out, "w", encoding="utf-8").write(t)
    return out
if __name__ == "__main__":
    p = get(sys.argv[1])
    if len(sys.argv) > 2 and sys.argv[2] == "strip":
        p = strip(p)
    print(p)
