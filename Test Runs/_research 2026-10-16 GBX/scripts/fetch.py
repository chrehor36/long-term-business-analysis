import sys, os, re, html, time, urllib.request
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
def get(url):
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=60).read()
        except Exception as e:
            print("retry", e); time.sleep(3)
    raise SystemExit("fail " + url)
def strip(b):
    t = b.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</t[dh]>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t
if __name__ == "__main__":
    url, out = sys.argv[1], sys.argv[2]
    b = get(url)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(strip(b))
    print(out, len(b))
