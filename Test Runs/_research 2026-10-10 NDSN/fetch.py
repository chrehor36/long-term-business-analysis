"""Fetch helper for the NDSN run: SEC EDGAR with the operator's User-Agent; caches under cache/."""
import sys, os, json, time, re, urllib.request, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
def get(url, out=None):
    if out and os.path.exists(out):
        return open(out, "rb").read()
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers=UA)
            data = urllib.request.urlopen(req, timeout=60).read()
            if out:
                os.makedirs(os.path.dirname(out), exist_ok=True)
                open(out, "wb").write(data)
            time.sleep(0.15)
            return data
        except Exception as e:
            print("retry", url, e, file=sys.stderr); time.sleep(2)
    raise SystemExit("failed " + url)
def text(raw):
    s = raw.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    url, out = sys.argv[1], sys.argv[2]
    raw = get(url, out + ".raw" if out.endswith(".txt") else out)
    if out.endswith(".txt"):
        open(out, "w", encoding="utf-8").write(text(raw))
    print(out, len(raw))
