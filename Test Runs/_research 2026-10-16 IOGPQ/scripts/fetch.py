import sys, os, re, time, urllib.request, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for spec in sys.argv[2:]:
    name, url = spec.split("=", 1)
    p = os.path.join(out, name)
    if not os.path.exists(p):
        data = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        open(p, "wb").write(data); time.sleep(0.3)
    if p.endswith((".htm", ".html")):
        t = open(p, "rb").read().decode("utf-8", "ignore")
        t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
        t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
        t = re.sub(r"(?i)</td>", " | ", t)
        t = re.sub(r"<[^>]+>", " ", t); t = html.unescape(t)
        t = re.sub(r"[ \t\xa0]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
        open(p + ".txt", "w", encoding="utf-8").write(t)
    print(name, os.path.getsize(p))
