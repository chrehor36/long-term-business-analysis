import sys, os, json, time, re, urllib.request, gzip, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
HERE = os.path.dirname(os.path.abspath(__file__))
def get(url):
    req = urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                d = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    d = gzip.decompress(d)
                return d
        except Exception as e:
            print("retry", url, e, file=sys.stderr); time.sleep(2)
    raise SystemExit("fail " + url)
def save(name, data):
    p = os.path.join(HERE, name)
    with open(p, "wb") as f: f.write(data)
    return p
def to_text(b):
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
        save(out, get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"))
    elif cmd == "facts":
        cik = sys.argv[2]; out = sys.argv[3]
        save(out, get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json"))
    elif cmd == "doc":
        url = sys.argv[2]; out = sys.argv[3]
        b = get(url); save(out, to_text(b).encode("utf-8"))
    elif cmd == "raw":
        url = sys.argv[2]; out = sys.argv[3]
        save(out, get(url))
