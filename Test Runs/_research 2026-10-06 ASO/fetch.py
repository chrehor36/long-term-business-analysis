import sys, json, urllib.request, gzip, re, html, os, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url):
    for i in range(4):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)
            b = r.read()
            if r.headers.get("Content-Encoding") == "gzip": b = gzip.decompress(b)
            return b
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(2)
    raise SystemExit("failed " + url)
def totext(b):
    s = b.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "sub":
        cik = sys.argv[2]; out = sys.argv[3]
        open(out, "wb").write(get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"))
    elif cmd == "doc":
        url = sys.argv[2]; out = sys.argv[3]
        open(out, "w", encoding="utf-8").write(totext(get(url)))
    elif cmd == "raw":
        url = sys.argv[2]; out = sys.argv[3]
        open(out, "wb").write(get(url))
