import sys, os, re, time, html, urllib.request
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
CIK = "276720"
out = sys.argv[1]
def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()
def strip(b):
    t = b.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</(p|div|tr|li|h\d)>", "\n", t)
    t = re.sub(r"(?i)</t[dh]>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t
for arg in sys.argv[2:]:
    acc, doc, name = arg.split(",")
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-','')}/{doc}"
    p = os.path.join(out, name + ".txt")
    if os.path.exists(p): continue
    b = get(url); time.sleep(0.3)
    open(p, "w", encoding="utf-8").write(f"SOURCE {url}\n" + strip(b))
    print(name, len(b))
