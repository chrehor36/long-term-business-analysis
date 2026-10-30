import urllib.request, urllib.error, json, time, gzip, zlib

UA = "Chris Hrehor chrehor36@gmail.com"
BASE = "https://efts.sec.gov/LATEST/search-index"

def raw_get(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", UA)
    req.add_header("Accept", "application/json, text/javascript, */*; q=0.01")
    req.add_header("Accept-Encoding", "gzip, deflate")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            b = r.read()
            enc = r.headers.get("Content-Encoding", "")
            if enc == "gzip":
                b = gzip.decompress(b)
            elif enc == "deflate":
                b = zlib.decompress(b)
            return r.status, b
    except urllib.error.HTTPError as e:
        b = e.read()
        return e.code, b
    except Exception as e:
        return -1, ("CONN ERROR: %r" % e).encode()

def fts(phrase, forms=None, frm=0, startdt=None, enddt=None, ciks=None, tries=5):
    q = urllib.request.quote('"%s"' % phrase, safe="")
    url = "%s?q=%s" % (BASE, q)
    if forms:
        url += "&forms=" + urllib.request.quote(forms, safe=",")
    if frm:
        url += "&from=%d" % frm
    if startdt:
        url += "&startdt=%s&enddt=%s&dateRange=custom" % (startdt, enddt)
    if ciks:
        url += "&ciks=" + ciks
    last = None
    for t in range(tries):
        st, b = raw_get(url)
        time.sleep(0.4)
        last = (st, b)
        if st == 200:
            try:
                return st, url, json.loads(b.decode("utf-8", "replace")), b
            except Exception:
                return st, url, None, b
        time.sleep(1.0 + 1.5 * t)
    return last[0], url, None, last[1]
