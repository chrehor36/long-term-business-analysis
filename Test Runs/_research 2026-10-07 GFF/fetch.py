"""Fetch EDGAR documents for the GFF run into cache/ (ignored). Usage: python fetch.py URL [outname]"""
import sys, os, time, urllib.request, gzip, re, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip, deflate"}
def get(url):
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
                return data
        except Exception as e:
            print("retry", e); time.sleep(2 + i * 3)
    raise SystemExit("failed " + url)
def strip(b):
    t = b.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>|</th>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t
if __name__ == "__main__":
    url = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else url.rsplit("/", 1)[-1]
    os.makedirs("cache", exist_ok=True)
    d = get(url)
    p = os.path.join("cache", out)
    if out.endswith(".txt"):
        open(p, "w", encoding="utf-8").write(strip(d))
    else:
        open(p, "wb").write(d)
    print(p, len(d))
    time.sleep(0.3)
