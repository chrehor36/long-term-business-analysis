"""Fetch helper for the HAS run: saves SEC documents under cache/ (gitignored). Transcription only."""
import sys, os, time, json, re, urllib.request, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
def get(url, out=None):
    req = urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            data = urllib.request.urlopen(req, timeout=60).read()
            break
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(2)
    else:
        raise SystemExit("failed " + url)
    if out:
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        open(out, "wb").write(data)
    time.sleep(0.15)
    return data
def text(path_in, path_out):
    s = open(path_in, encoding="utf-8", errors="replace").read()
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>|</th>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    open(path_out, "w", encoding="utf-8").write(s)
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "get":
        get(sys.argv[2], sys.argv[3])
        if sys.argv[3].endswith((".htm", ".html")):
            text(sys.argv[3], sys.argv[3] + ".txt")
