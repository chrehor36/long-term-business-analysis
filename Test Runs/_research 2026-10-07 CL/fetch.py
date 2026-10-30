# fetch helper for the CL run: SEC EDGAR with the declared User-Agent; raw files go to cache/ (gitignored)
import sys, os, time, json, re, urllib.request, gzip, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url):
    for i in range(4):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)
            b = r.read()
            if r.headers.get("Content-Encoding") == "gzip": b = gzip.decompress(b)
            time.sleep(0.15); return b
        except Exception as e:
            print("retry", url, e, file=sys.stderr); time.sleep(2)
    raise SystemExit("failed " + url)
def strip(b):
    t = b.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>|</th>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t
if __name__ == "__main__":
    url, out = sys.argv[1], sys.argv[2]
    b = get(url)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    if out.endswith(".txt"): open(out, "w", encoding="utf-8").write(strip(b))
    else: open(out, "wb").write(b)
    print(out, len(b))
