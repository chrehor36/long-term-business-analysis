import urllib.request, urllib.parse, json, os, ssl
H = {"User-Agent": "Mozilla/5.0"}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sov")
def get(url, data=None):
    req = urllib.request.Request(url, data=data, headers=H)
    return urllib.request.urlopen(req, timeout=60).read()
for d in ["2026/09/11", "2026/09/12", "2026/09/13"]:
    try:
        body = urllib.parse.urlencode({"date": d, "fileCode": "Curve", "response": "json"}).encode()
        r = get("https://www.tpex.org.tw/www/en-us/bond/govDaily2", body)
        print(d, r[:600])
        open(os.path.join(out, "tpex_govDaily2_" + d.replace("/", "") + ".json"), "wb").write(r)
    except Exception as e:
        print(d, "ERR", e)
