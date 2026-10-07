import urllib.request, os, re, html
H = {"User-Agent": "Mozilla/5.0"}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sov")
def g(u, name):
    b = urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=60).read()
    open(os.path.join(out, name), "wb").write(b)
    t = re.sub(r"<[^>]+>", " ", b.decode("utf-8", "replace"))
    return re.sub(r"\s+", " ", html.unescape(t))
t = g("https://www.cbc.gov.tw/en/lp-448-2.html", "cbc_auction_list.html")
for m in re.finditer(r"(Auction[^.]{0,160}?Bonds?[^.]{0,60})", t):
    print(m.group(1)[:220])
links = re.findall(r'href="([^"]*cp-448-[^"]+)"[^>]*title="([^"]*)"', open(os.path.join(out, "cbc_auction_list.html"), encoding="utf-8", errors="replace").read())
for l in links[:25]:
    print(l)
t2 = g("https://www.cbc.gov.tw/en/lp-700-2.html", "cbc_fx.html")
i = t2.find("Closing")
print(t2[i-200:i+900])
