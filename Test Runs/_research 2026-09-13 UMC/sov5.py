import urllib.request, os, re, html
H = {"User-Agent": "Mozilla/5.0"}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sov")
def g(u, name):
    b = urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=60).read()
    open(os.path.join(out, name), "wb").write(b)
    t = re.sub(r"<[^>]+>", " ", b.decode("utf-8", "replace"))
    return re.sub(r"\s+", " ", html.unescape(t))
for code in ["cp-448-191306-0372c-2", "cp-448-192798-d1d6e-2"]:
    t = g(f"https://www.cbc.gov.tw/en/{code}.html", f"cbc_{code}.html")
    i = t.find("The Bank")
    print(code, "::", t[i:i+900], "\n")
t = open(os.path.join(out, "cbc_fx.html"), encoding="utf-8", errors="replace").read()
rows = re.findall(r"<tr[^>]*>(.*?)</tr>", t, flags=re.S)
for r in rows[:12]:
    print(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", r)).strip())
