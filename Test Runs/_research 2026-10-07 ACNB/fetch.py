import sys, urllib.request, gzip, time, re, html, os
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
            print("retry", e, file=sys.stderr); time.sleep(2+i*2)
    raise SystemExit("failed "+url)
def to_text(b):
    s = b.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>", "\n", s)
    s = re.sub(r"(?i)</td>|</th>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    url, out = sys.argv[1], sys.argv[2]
    b = get(url)
    if out.endswith(".txt") and not url.endswith(".txt") and not url.endswith(".json"):
        open(out, "w", encoding="utf-8").write(to_text(b))
    else:
        open(out, "wb").write(b)
    print(out, os.path.getsize(out))
