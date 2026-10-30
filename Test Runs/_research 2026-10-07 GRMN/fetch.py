"""EDGAR fetch helper for the GRMN run of 2026-10-07. Writes raw files under cache/ (ignored)."""
import sys, os, json, re, time, urllib.request, gzip, html
UA = "Chris Hrehor chrehor36@gmail.com"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
os.makedirs(CACHE, exist_ok=True)

def get(url, name=None):
    path = os.path.join(CACHE, name or re.sub(r"[^A-Za-z0-9._-]", "_", url.split("/")[-1] or "index"))
    if os.path.exists(path):
        return open(path, "rb").read()
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    for i in range(4):
        try:
            r = urllib.request.urlopen(req, timeout=60)
            data = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                data = gzip.decompress(data)
            open(path, "wb").write(data)
            time.sleep(0.2)
            return data
        except Exception as e:
            print("retry", url, e, file=sys.stderr); time.sleep(2)
    raise SystemExit("failed " + url)

def text(data):
    s = data.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s

if __name__ == "__main__":
    url, name = sys.argv[1], sys.argv[2]
    d = get(url, name)
    if name.endswith(".htm") or name.endswith(".html"):
        open(os.path.join(CACHE, name + ".txt"), "w", encoding="utf-8").write(text(d))
        print("wrote", name + ".txt", len(d))
    else:
        print("wrote", name, len(d))
