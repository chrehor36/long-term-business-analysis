import json, sys, urllib.request, urllib.parse, collections
sys.stdout.reconfigure(encoding="utf-8")
def q(phrase, forms="10-K,20-F,10-K405", frm=0):
    p = {"q": '"%s"' % phrase, "forms": forms, "from": frm}
    url = "https://efts.sec.gov/LATEST/search-index?" + urllib.parse.urlencode(p)
    r = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Chris Hrehor chrehor36@gmail.com"}), timeout=60)
    return json.loads(r.read())
for ph in sys.argv[1:]:
    d = q(ph); tot = d["hits"]["total"]["value"]
    c = collections.Counter()
    hits = d["hits"]["hits"]
    frm = 100
    while frm < min(tot, 400):
        hits += q(ph, frm=frm)["hits"]["hits"]; frm += 100
    for h in hits:
        s = h["_source"]; c[(s["display_names"][0], s["form"])] += 1
    print("==", ph, tot)
    for k, v in sorted(c.items()): print("  ", k, v, )
