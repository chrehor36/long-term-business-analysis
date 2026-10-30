"""Fetch an SEC URL into cache/ with the project's User-Agent; print the saved path. Optional html->text."""
import sys, os, re, time, urllib.request, gzip, html as H
UA = "Chris Hrehor chrehor36@gmail.com"
here = os.path.dirname(os.path.abspath(__file__))
cache = os.path.join(here, "cache")
def get(url, name, text=False):
    p = os.path.join(cache, name)
    if not os.path.exists(p):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
        for i in range(4):
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    b = r.read()
                    if r.headers.get("Content-Encoding") == "gzip": b = gzip.decompress(b)
                break
            except Exception as e:
                print("retry", e); time.sleep(2)
        open(p, "wb").write(b); time.sleep(0.3)
    if text:
        t = open(p, "rb").read().decode("utf-8", "ignore")
        t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
        t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
        t = re.sub(r"(?i)</td>", " | ", t)
        t = re.sub(r"<[^>]+>", " ", t)
        t = H.unescape(t).replace("\xa0", " ")
        t = re.sub(r"[ \t]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
        tp = p + ".txt"; open(tp, "w", encoding="utf-8").write(t); print(tp)
    else:
        print(p)
if __name__ == "__main__":
    get(sys.argv[1], sys.argv[2], len(sys.argv) > 3)
