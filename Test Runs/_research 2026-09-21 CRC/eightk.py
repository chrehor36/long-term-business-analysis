import json, os, re, sys, time, html, urllib.request, gzip, zlib
UA = {"User-Agent": "BRK research chrehor36@gmail.com", "Accept-Encoding": "gzip, deflate"}
OUT = os.path.dirname(os.path.abspath(__file__))

def get(url, timeout=120):
    req = urllib.request.Request(url, headers=UA)
    for a in range(4):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                d = r.read()
                e = r.headers.get("Content-Encoding", "")
                if e == "gzip": d = gzip.decompress(d)
                elif e == "deflate": d = zlib.decompress(d)
                return d
        except Exception as ex:
            print("  retry", a, ex); time.sleep(3)
    raise SystemExit("failed " + url)

def totext(raw):
    t = raw.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)</(p|div|tr|h[1-6]|li)>", "\n", t)
    t = re.sub(r"(?i)</t[dh]>", " | ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return "\n".join(l for l in t.split("\n")
                     if not (len(l) > 400 and ("http://" in l or "us-gaap:" in l)))

acc = sys.argv[1]                       # e.g. 0001609253-26-000127
cik = "1609253"
base = "https://www.sec.gov/Archives/edgar/data/%s/%s/" % (cik, acc.replace("-", ""))
idx = json.loads(get(base + "index.json"))
names = [i["name"] for i in idx["directory"]["item"]]
print(acc, names)
for n in names:
    if n.lower().endswith((".htm", ".html")) and not n.lower().endswith("-index.htm"):
        txt = totext(get(base + n))
        p = os.path.join(OUT, "8K_%s_%s.txt" % (acc[-6:], n.rsplit(".", 1)[0]))
        open(p, "w", encoding="utf-8").write(txt)
        print("  wrote", os.path.basename(p), len(txt))
