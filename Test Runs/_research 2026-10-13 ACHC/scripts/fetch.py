import sys, os, json, time, urllib.request, re, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
OUT = sys.argv[1]
def get(url):
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            print("retry", url, e, file=sys.stderr); time.sleep(2+i*3)
    raise SystemExit("failed "+url)
def strip(b):
    t = b.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</(p|div|tr|li|h\d)>", "\n", t)
    t = re.sub(r"(?i)</t[dh]>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t
if __name__ == "__main__":
    mode = sys.argv[2]
    if mode == "subs":
        b = get("https://data.sec.gov/submissions/CIK%s.json" % sys.argv[3])
        open(os.path.join(OUT, "subs.json"), "wb").write(b)
    elif mode == "doc":
        url, name = sys.argv[3], sys.argv[4]
        b = get(url)
        open(os.path.join(OUT, name + ".htm"), "wb").write(b)
        open(os.path.join(OUT, name + ".txt"), "w", encoding="utf-8").write(strip(b))
        print(name, len(b))
    elif mode == "raw":
        url, name = sys.argv[3], sys.argv[4]
        open(os.path.join(OUT, name), "wb").write(get(url))
